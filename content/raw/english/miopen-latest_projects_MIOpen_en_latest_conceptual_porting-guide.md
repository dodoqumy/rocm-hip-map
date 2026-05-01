---
title: "Porting to MIOpen &#8212; MIOpen 3.5.1 Documentation"
source_url: "https://rocm.docs.amd.com/projects/MIOpen/en/latest/conceptual/porting-guide.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:57.649159+00:00
content_hash: "c3aac9ebd81ab356"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Porting to MIOpen" name="description" />
<meta content="MIOpen, ROCm, API, documentation, porting" name="keywords" />

    <title>Porting to MIOpen &#8212; MIOpen 3.5.1 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'conceptual/porting-guide';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Using the fusion API" href="../how-to/use-fusion-api.html" />
    <link rel="prev" title="MI200 matrix fused multiply-add (MFMA) behavior specifics" href="MI200-alt-implementation.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-miopen" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/conceptual/porting-guide.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1"><a class="reference internal" href="perfdb.html">Performance database</a></li>
<li class="toctree-l1"><a class="reference internal" href="tuningdb.html">Manual tuning</a></li>
<li class="toctree-l1"><a class="reference internal" href="MI200-alt-implementation.html">MI200 alternate implementation</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Porting to MIOpen</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Porting to MIOpen</span></li>
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
    <h1>Porting to MIOpen</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cuda-cudnn-versus-miopen-apis">CUDA cuDNN versus MIOpen APIs</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#handle-operations">Handle operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#tensor-operations">Tensor operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filter-operations">Filter operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#convolution-operations">Convolution operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#softmax-operations">Softmax operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#pooling-operations">Pooling operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#activation-operations">Activation operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#lrn-operations">LRN operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#batch-normalization-operations">Batch normalization operations</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="porting-to-miopen">
<h1>Porting to MIOpen<a class="headerlink" href="#porting-to-miopen" title="Link to this heading">#</a></h1>
<p>The following is a summary of the key differences between MIOpen and NVIDIA CUDA cuDNN.</p>
<ul class="simple">
<li><p>Calling <code class="docutils literal notranslate"><span class="pre">miopenFindConvolution*Algorithm()</span></code> is <strong>mandatory</strong> before calling any Convolution API</p></li>
<li><p>The typical calling sequence for the MIOpen Convolution APIs is:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">miopenConvolution*GetWorkSpaceSize()</span></code> (returns the workspace size required by <code class="docutils literal notranslate"><span class="pre">Find()</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">miopenFindConvolution*Algorithm()</span></code> (returns the performance information for various algorithms)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">miopenConvolution*()</span></code></p></li>
</ul>
</li>
</ul>
<p>MIOpen supports:</p>
<ul class="simple">
<li><p>4D tensors in the NCHW and NHWC storage format. The CUDA cuDNN <code class="docutils literal notranslate"><span class="pre">__“\*Nd\*”__</span></code> APIs don’t have a
corresponding MIOpen API.</p></li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">__`float(fp32)`__</span></code> datatype</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__2D</span> <span class="pre">Convolutions__</span></code> and <code class="docutils literal notranslate"><span class="pre">__3D</span> <span class="pre">Convolutions__</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__2D</span> <span class="pre">Pooling__</span></code></p></li>
</ul>
<p>MIOpen doesn’t support:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">__Preferences__</span></code> for convolutions</p></li>
<li><p>Softmax modes (MIOpen implements the <code class="docutils literal notranslate"><span class="pre">__SOFTMAX_MODE_CHANNEL__</span></code> flavor)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__Transform-Tensor__</span></code>, <code class="docutils literal notranslate"><span class="pre">__Dropout__</span></code>, <code class="docutils literal notranslate"><span class="pre">__RNNs__</span></code>, and <code class="docutils literal notranslate"><span class="pre">__Divisive</span> <span class="pre">Normalization__</span></code></p></li>
</ul>
<p>Useful MIOpen environment variables include:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_LOGGING=1</span></code>: Logs all the MIOpen APIs that are called, including the parameters passed
to those APIs</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_GCN_ASM_KERNELS=0</span></code>: Disables hand-tuned ASM kernels (the fallback is to use
kernels written in a high-level language)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_FFT=0</span></code>: Disables the FFT convolution algorithm</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">MIOPEN_DEBUG_CONV_DIRECT=0</span></code>: Disables the direct convolution algorithm</p></li>
</ul>
<section id="cuda-cudnn-versus-miopen-apis">
<h2>CUDA cuDNN versus MIOpen APIs<a class="headerlink" href="#cuda-cudnn-versus-miopen-apis" title="Link to this heading">#</a></h2>
<p>The following sections compare the CUDA cuDNN and MIOpen APIs with similar functions.</p>
<section id="handle-operations">
<h3>Handle operations<a class="headerlink" href="#handle-operations" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>cuDNN</p></th>
<th class="head"><p>MIOpen</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnCreate</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="o">*</span><span class="n">handle</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenCreate</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="o">*</span><span class="n">handle</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnDestroy</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenDestroy</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnSetStream</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudaStream_t</span><span class="w"> </span><span class="n">streamId</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenSetStream</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenAcceleratorQueue_t</span><span class="w"> </span><span class="n">streamID</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetStream</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudaStream_t</span><span class="w"> </span><span class="o">*</span><span class="n">streamId</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenGetStream</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenAcceleratorQueue_t</span><span class="w">  </span><span class="o">*</span><span class="n">streamID</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="tensor-operations">
<h3>Tensor operations<a class="headerlink" href="#tensor-operations" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>cuDNN</p></th>
<th class="head"><p>MIOpen</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnCreateTensorDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="o">*</span><span class="n">tensorDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenCreateTensorDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenTensorDescriptor_t</span>
<span class="w">    </span><span class="o">*</span><span class="n">tensorDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnDestroyTensorDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">tensorDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenDestroyTensorDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">tensorDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnSetTensor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">valuePtr</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenSetTensor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnSetTensor4dDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">tensorDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnTensorFormat_t</span><span class="w"> </span><span class="n">format</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnDataType_t</span><span class="w"> </span><span class="n">dataType</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">n</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">c</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">h</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">w</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span><span class="w"> </span><span class="n">miopenSet4dTensorDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">tensorDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenDataType_t</span><span class="w"> </span><span class="n">dataType</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">n</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">c</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">h</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">w</span><span class="p">)</span>
</pre></div>
</div>
<p>Only the <code class="docutils literal notranslate"><span class="pre">NCHW</span></code> format is supported</p>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetTensor4dDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">tensorDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnDataType_t</span><span class="w"> </span><span class="o">*</span><span class="n">dataType</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">n</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">h</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">nStride</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">cStride</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">hStride</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">wStride</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenGet4dTensorDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">tensorDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenDataType_t</span><span class="w"> </span><span class="o">*</span><span class="n">dataType</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">n</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">h</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">nStride</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">cStride</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">hStride</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">wStride</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnAddTensor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">aDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">A</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">cDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">C</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenOpTensor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenTensorOp_t</span><span class="w"> </span><span class="n">tensorOp</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha1</span><span class="p">,</span>
<span class="w">    </span><span class="n">constmiopenTensorDescriptor_t</span><span class="w">  </span><span class="n">aDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">A</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha2</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">bDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">B</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w">  </span><span class="n">cDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">C</span><span class="p">)</span>
</pre></div>
</div>
<p>For forward bias, use <code class="docutils literal notranslate"><span class="pre">miopenConvolutionForwardBias</span></code></p>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnOpTensor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnOpTensorDescriptor_t</span><span class="w"> </span><span class="n">opTensorDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha1</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">aDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">A</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha2</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">bDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">B</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">cDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">C</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenOpTensor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenTensorOp_t</span><span class="w"> </span><span class="n">tensorOp</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha1</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">aDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">A</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha2</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w">  </span><span class="n">bDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">B</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w">  </span><span class="n">cDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">C</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnOpTensor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnOpTensorDescriptor_t</span><span class="w"> </span><span class="n">opTensorDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha1</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">aDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">A</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha2</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">bDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">B</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">cDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">C</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenOpTensor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenTensorOp_t</span><span class="w"> </span><span class="n">tensorOp</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha1</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">aDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">A</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha2</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w">  </span><span class="n">bDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">B</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w">  </span><span class="n">cDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">C</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnScaleTensor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenScaleTensor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="filter-operations">
<h3>Filter operations<a class="headerlink" href="#filter-operations" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>cuDNN</p></th>
<th class="head"><p>MIOpen</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnCreateFilterDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="o">*</span><span class="n">filterDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><p>All <code class="docutils literal notranslate"><span class="pre">TensorDescriptor</span></code> APIs substitute for the respective <code class="docutils literal notranslate"><span class="pre">FilterDescriptor</span></code> APIs.</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="convolution-operations">
<h3>Convolution operations<a class="headerlink" href="#convolution-operations" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>cuDNN</p></th>
<th class="head"><p>MIOpen</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnCreateConvolutionDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="o">*</span><span class="n">convDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenCreateConvolutionDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="o">*</span><span class="n">convDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnDestroyConvolutionDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenDestroyConvolutionDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetConvolution2dDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">pad_h</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">pad_y</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">u</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">v</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">upscalex</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">upscaley</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionMode_t</span><span class="w"> </span><span class="o">*</span><span class="n">mode</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenGetConvolutionDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenConvolutionMode_t</span><span class="w"> </span><span class="o">*</span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">pad_h</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">pad_y</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">u</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">v</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">upscalex</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">upscaley</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetConvolution2dForwardOutputDim</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">inputTensorDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">filterDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">n</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">h</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenGetConvolutionForwardOutputDim</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">inputTensorDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">filterDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">n</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">h</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetConvolutionForwardWorkspaceSize</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionFwdAlgo_t</span><span class="w"> </span><span class="n">algo</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="o">*</span><span class="n">sizeInBytes</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenConvolutionForwardGetWorkSpaceSize</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="o">*</span><span class="n">workSpaceSize</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetConvolutionBackwardFilterWorkspaceSize</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">gradDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionBwdFilterAlgo_t</span><span class="w"> </span><span class="n">algo</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="o">*</span><span class="n">sizeInBytes</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenConvolutionBackwardWeightsGetWorkSpaceSize</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dwDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="o">*</span><span class="n">workSpaceSize</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetConvolutionBackwardDataWorkspaceSize</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionBwdDataAlgo_t</span><span class="w"> </span><span class="n">algo</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="o">*</span><span class="n">sizeInBytes</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenConvolutionBackwardDataGetWorkSpaceSize</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="o">*</span><span class="n">workSpaceSize</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnConvolutionForward</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionFwdAlgo_t</span><span class="w"> </span><span class="n">algo</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSizeInBytes</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenConvolutionForward</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenConvFwdAlgorithm_t</span><span class="w"> </span><span class="n">algo</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSize</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnFindConvolutionForwardAlgorithm</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">requestedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">returnedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionFwdAlgoPerf_t</span><span class="w"> </span><span class="o">*</span><span class="n">perfResults</span><span class="p">)</span>

<span class="n">cudnnStatus_t</span>
<span class="n">cudnnFindConvolutionForwardAlgorithmEx</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">requestedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">returnedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionFwdAlgoPerf_t</span><span class="w"> </span><span class="o">*</span><span class="n">perfResults</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSizeInBytes</span><span class="p">)</span>

<span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetConvolutionForwardAlgorithm</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionFwdPreference_t</span><span class="w"> </span><span class="n">preference</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">memoryLimitInBytes</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionFwdAlgo_t</span><span class="w"> </span><span class="o">*</span><span class="n">algo</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><dl>
<dt><code class="docutils literal notranslate"><span class="pre">FindConvolution()</span></code> is mandatory.</dt><dd><p>Allocate the workspace prior to running this API.
A table with times and memory requirements for different algorithms is returned.
Choose the top-most algorithm if you only want the fastest algorithm.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenFindConvolutionForwardAlgorithm</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">requestAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">returnedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenConvAlgoPerf_t</span><span class="w"> </span><span class="o">*</span><span class="n">perfResults</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSize</span><span class="p">,</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">exhaustiveSearch</span><span class="p">)</span>
</pre></div>
</div>
</dd>
</dl>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnConvolutionBackwardBias</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dbDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">db</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenConvolutionBackwardBias</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dbDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">db</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnFindConvolutionBackwardFilterAlgorithm</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">dwDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">requestedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">returnedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionBwdFilterAlgoPerf_t</span><span class="w"> </span><span class="o">*</span><span class="n">perfResults</span><span class="p">)</span>

<span class="n">cudnnStatus_t</span>
<span class="n">cudnnFindConvolutionBackwardFilterAlgorithmEx</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">dwDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dw</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">requestedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">returnedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionBwdFilterAlgoPerf_t</span><span class="w"> </span><span class="o">*</span><span class="n">perfResults</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSizeInBytes</span><span class="p">)</span>

<span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetConvolutionBackwardFilterAlgorithm</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">dwDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionBwdFilterPreference_t</span><span class="w"> </span><span class="n">preference</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">memoryLimitInBytes</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionBwdFilterAlgo_t</span><span class="w"> </span><span class="o">*</span><span class="n">algo</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><dl>
<dt><code class="docutils literal notranslate"><span class="pre">FindConvolution()</span></code> is mandatory.</dt><dd><p>Allocate the workspace prior to running this API.
A table with times and memory requirements for different algorithms is returned.
Choose the top-most algorithm if you only want the fastest algorithm.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenFindConvolutionBackwardWeightsAlgorithm</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dwDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dw</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">requestAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">returnedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenConvAlgoPerf_t</span><span class="w"> </span><span class="o">*</span><span class="n">perfResults</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSize</span><span class="p">,</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">exhaustiveSearch</span><span class="p">)</span>
</pre></div>
</div>
</dd>
</dl>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnFindConvolutionBackwardDataAlgorithm</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">requestedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">returnedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionBwdDataAlgoPerf_t</span><span class="w"> </span><span class="o">*</span><span class="n">perfResults</span><span class="p">)</span>

<span class="n">cudnnStatus_t</span>
<span class="n">cudnnFindConvolutionBackwardDataAlgorithmEx</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">requestedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">returnedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionBwdDataAlgoPerf_t</span><span class="w"> </span><span class="o">*</span><span class="n">perfResults</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSizeInBytes</span><span class="p">)</span>

<span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetConvolutionBackwardDataAlgorithm</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionBwdDataPreference_t</span><span class="w"> </span><span class="n">preference</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">memoryLimitInBytes</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionBwdDataAlgo_t</span><span class="w"> </span><span class="o">*</span><span class="n">algo</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><dl>
<dt><code class="docutils literal notranslate"><span class="pre">FindConvolution()</span></code> is mandatory.</dt><dd><p>Allocate the workspace prior to running this API.
A table with times and memory requirements for different algorithms is returned.
Choose the top-most algorithm if you only want the fastest algorithm.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenFindConvolutionBackwardDataAlgorithm</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">requestAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">returnedAlgoCount</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenConvAlgoPerf_t</span><span class="w"> </span><span class="o">*</span><span class="n">perfResults</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSize</span><span class="p">,</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">exhaustiveSearch</span><span class="p">)</span>
</pre></div>
</div>
</dd>
</dl>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnConvolutionBackwardFilter</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionBwdFilterAlgo_t</span><span class="w"> </span><span class="n">algo</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSizeInBytes</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">dwDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dw</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenConvolutionBackwardWeights</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenConvBwdWeightsAlgorithm_t</span><span class="w"> </span><span class="n">algo</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dwDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dw</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSize</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnConvolutionBackwardData</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnFilterDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnConvolutionBwdDataAlgo_t</span><span class="w"> </span><span class="n">algo</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSizeInBytes</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenConvolutionBackwardData</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenConvBwdDataAlgorithm_t</span><span class="w"> </span><span class="n">algo</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSize</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="softmax-operations">
<h3>Softmax operations<a class="headerlink" href="#softmax-operations" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>cuDNN</p></th>
<th class="head"><p>MIOpen</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnSoftmaxForward</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnSoftmaxAlgorithm_t</span><span class="w"> </span><span class="n">algo</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnSoftmaxMode_t</span><span class="w"> </span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenSoftmaxForward</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnSoftmaxBackward</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnSoftmaxAlgorithm_t</span><span class="w"> </span><span class="n">algo</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnSoftmaxMode_t</span><span class="w"> </span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenSoftmaxBackward</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="pooling-operations">
<h3>Pooling operations<a class="headerlink" href="#pooling-operations" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>cuDNN</p></th>
<th class="head"><p>MIOpen</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnCreatePoolingDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnPoolingDescriptor_t</span><span class="w"> </span><span class="o">*</span><span class="n">poolingDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenCreatePoolingDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenPoolingDescriptor_t</span><span class="w"> </span><span class="o">*</span><span class="n">poolDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnSetPooling2dDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnPoolingDescriptor_t</span><span class="w"> </span><span class="n">poolingDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnPoolingMode_t</span><span class="w"> </span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnNanPropagation_t</span><span class="w"> </span><span class="n">maxpoolingNanOpt</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">windowHeight</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">windowWidth</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">verticalPadding</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">horizontalPadding</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">verticalStride</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">horizontalStride</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenSet2dPoolingDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenPoolingDescriptor_t</span><span class="w"> </span><span class="n">poolDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenPoolingMode_t</span><span class="w"> </span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">windowHeight</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">windowWidth</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">pad_h</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">pad_w</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">u</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">v</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetPooling2dDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnPoolingDescriptor_t</span><span class="w"> </span><span class="n">poolingDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnPoolingMode_t</span><span class="w"> </span><span class="o">*</span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnNanPropagation_t</span><span class="w"> </span><span class="o">*</span><span class="n">maxpoolingNanOpt</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">windowHeight</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">windowWidth</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">verticalPadding</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">horizontalPadding</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">verticalStride</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">horizontalStride</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenGet2dPoolingDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenPoolingDescriptor_t</span><span class="w"> </span><span class="n">poolDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenPoolingMode_t</span><span class="w"> </span><span class="o">*</span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">windowHeight</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">windowWidth</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">pad_h</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">pad_w</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">u</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">v</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetPooling2dForwardOutputDim</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnPoolingDescriptor_t</span><span class="w"> </span><span class="n">poolingDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">inputTensorDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">n</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">h</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenGetPoolingForwardOutputDim</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenPoolingDescriptor_t</span><span class="w"> </span><span class="n">poolDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">tensorDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">n</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">h</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">w</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnDestroyPoolingDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnPoolingDescriptor_t</span><span class="w"> </span><span class="n">poolingDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenDestroyPoolingDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenPoolingDescriptor_t</span><span class="w"> </span><span class="n">poolDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnPoolingForward</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnPoolingDescriptor_t</span><span class="w"> </span><span class="n">poolingDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenPoolingForward</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenPoolingDescriptor_t</span><span class="w"> </span><span class="n">poolDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">do_backward</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workSpace</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">workSpaceSize</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>NA</p></td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenPoolingGetWorkSpaceSize</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="o">*</span><span class="n">workSpaceSize</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnPoolingBackward</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnPoolingDescriptor_t</span><span class="w"> </span><span class="n">poolingDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenPoolingBackward</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenPoolingDescriptor_t</span><span class="w"> </span><span class="n">poolDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workspace</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="activation-operations">
<h3>Activation operations<a class="headerlink" href="#activation-operations" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>cuDNN</p></th>
<th class="head"><p>MIOpen</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnCreateActivationDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnActivationDescriptor_t</span><span class="w"> </span><span class="o">*</span><span class="n">activationDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenCreateActivationDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenActivationDescriptor_t</span><span class="w"> </span><span class="o">*</span><span class="n">activDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnSetActivationDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnActivationDescriptor_t</span><span class="w"> </span><span class="n">activationDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnActivationMode_t</span><span class="w"> </span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnNanPropagation_t</span><span class="w"> </span><span class="n">reluNanOpt</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">reluCeiling</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenSetActivationDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenActivationDescriptor_t</span><span class="w"> </span><span class="n">activDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenActivationMode_t</span><span class="w"> </span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">activAlpha</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">activBeta</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">activPower</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetActivationDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnActivationDescriptor_t</span><span class="w"> </span><span class="n">activationDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnActivationMode_t</span><span class="w"> </span><span class="o">*</span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnNanPropagation_t</span><span class="w"> </span><span class="o">*</span><span class="n">reluNanOpt</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">reluCeiling</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenGetActivationDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenActivationDescriptor_t</span><span class="w"> </span><span class="n">activDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenActivationMode_t</span><span class="w"> </span><span class="o">*</span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">activAlpha</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">activBeta</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">activPower</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnDestroyActivationDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnActivationDescriptor_t</span><span class="w"> </span><span class="n">activationDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenDestroyActivationDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenActivationDescriptor_t</span><span class="w"> </span><span class="n">activDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnActivationForward</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnActivationDescriptor_t</span><span class="w"> </span><span class="n">activationDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenActivationForward</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenActivationDescriptor_t</span><span class="w"> </span><span class="n">activDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnActivationBackward</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnActivationDescriptor_t</span><span class="w"> </span><span class="n">activationDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenActivationBackward</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenActivationDescriptor_t</span><span class="w"> </span><span class="n">activDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="lrn-operations">
<h3>LRN operations<a class="headerlink" href="#lrn-operations" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>cuDNN</p></th>
<th class="head"><p>MIOpen</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnCreateLRNDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnLRNDescriptor_t</span><span class="w"> </span><span class="o">*</span><span class="n">normDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenCreateLRNDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenLRNDescriptor_t</span>
<span class="w">    </span><span class="o">*</span><span class="n">lrnDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnSetLRNDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnLRNDescriptor_t</span><span class="w"> </span><span class="n">normDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">unsigned</span><span class="w"> </span><span class="n">lrnN</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">lrnAlpha</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">lrnBeta</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">lrnK</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenSetLRNDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenLRNDescriptor_t</span><span class="w"> </span><span class="n">lrnDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenLRNMode_t</span><span class="w"> </span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="kt">unsigned</span><span class="w"> </span><span class="n">lrnN</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">lrnAlpha</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">lrnBeta</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">lrnK</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnGetLRNDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnLRNDescriptor_t</span><span class="w"> </span><span class="n">normDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">unsigned</span><span class="o">*</span><span class="w"> </span><span class="n">lrnN</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">lrnAlpha</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">lrnBeta</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">lrnK</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenGetLRNDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenLRNDescriptor_t</span><span class="w"> </span><span class="n">lrnDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenLRNMode_t</span><span class="w"> </span><span class="o">*</span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="kt">unsigned</span><span class="w"> </span><span class="o">*</span><span class="n">lrnN</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">lrnAlpha</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">lrnBeta</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">lrnK</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnDestroyLRNDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnLRNDescriptor_t</span><span class="w"> </span><span class="n">lrnDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenDestroyLRNDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenLRNDescriptor_t</span><span class="w"> </span><span class="n">lrnDesc</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnLRNCrossChannelForward</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnLRNDescriptor_t</span><span class="w"> </span><span class="n">normDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnLRNMode_t</span><span class="w"> </span><span class="n">lrnMode</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenLRNForward</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenLRNDescriptor_t</span><span class="w"> </span><span class="n">lrnDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">do_backward</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w">  </span><span class="o">*</span><span class="n">workspace</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnLRNCrossChannelBackward</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnLRNDescriptor_t</span><span class="w"> </span><span class="n">normDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnLRNMode_t</span><span class="w"> </span><span class="n">lrnMode</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenLRNBackward</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenLRNDescriptor_t</span><span class="w"> </span><span class="n">lrnDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">workspace</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>NA</p></td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenLRNGetWorkSpaceSize</span><span class="p">(</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="o">*</span><span class="n">workSpaceSize</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnDeriveBNTensorDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">derivedBnDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnBatchNormMode_t</span><span class="w"> </span><span class="n">mode</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenDeriveBNTensorDescriptor</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">derivedBnDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenBatchNormMode_t</span><span class="w"> </span><span class="n">bn_mode</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="batch-normalization-operations">
<h3>Batch normalization operations<a class="headerlink" href="#batch-normalization-operations" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>cuDNN</p></th>
<th class="head"><p>MIOpen</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnBatchNormalizationForwardTraining</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnBatchNormMode_t</span><span class="w"> </span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span>
<span class="w">        </span><span class="n">bnScaleBiasMeanVarDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">bnScale</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">bnBias</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">exponentialAverageFactor</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">resultRunningMean</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">resultRunningVariance</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">epsilon</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">resultSaveMean</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">resultSaveInvVariance</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenBatchNormalizationForwardTraining</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenBatchNormMode_t</span><span class="w"> </span><span class="n">bn_mode</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span>
<span class="w">        </span><span class="n">bnScaleBiasMeanVarDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">bnScale</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">bnBias</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">expAvgFactor</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">resultRunningMean</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">resultRunningVariance</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">epsilon</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">resultSaveMean</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">resultSaveInvVariance</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnnBatchNormalizationForwardInference</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnBatchNormMode_t</span><span class="w"> </span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span>
<span class="w">        </span><span class="n">bnScaleBiasMeanVarDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">bnScale</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">bnBias</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">estimatedMean</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">estimatedVariance</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">epsilon</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenBatchNormalizationForwardInference</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenBatchNormMode_t</span><span class="w"> </span><span class="n">bn_mode</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">beta</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">yDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span>
<span class="w">        </span><span class="n">bnScaleBiasMeanVarDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">bnScale</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">bnBias</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">estimatedMean</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">estimatedVariance</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">epsilon</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">cudnnStatus_t</span>
<span class="n">cudnnBatchNormalizationBackward</span><span class="p">(</span>
<span class="w">    </span><span class="n">cudnnHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">cudnnBatchNormMode_t</span><span class="w"> </span><span class="n">mode</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alphaDataDiff</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">betaDataDiff</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alphaParamDiff</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">betaParamDiff</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">cudnnTensorDescriptor_t</span>
<span class="w">        </span><span class="n">bnScaleBiasDiffDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">bnScale</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">resultBnScaleDiff</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">resultBnBiasDiff</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">epsilon</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">savedMean</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">savedInvVariance</span><span class="p">)</span>
</pre></div>
</div>
</td>
<td><div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="n">miopenBatchNormalizationBackward</span><span class="p">(</span>
<span class="w">    </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">miopenBatchNormMode_t</span><span class="w"> </span><span class="n">bn_mode</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alphaDataDiff</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">betaDataDiff</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">alphaParamDiff</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">betaParamDiff</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">xDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">x</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dyDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dy</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">dxDesc</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">dx</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span>
<span class="w">        </span><span class="n">bnScaleBiasDiffDesc</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">bnScale</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">resultBnScaleDiff</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">resultBnBiasDiff</span><span class="p">,</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">epsilon</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">savedMean</span><span class="p">,</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">savedInvVariance</span><span class="p">)</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="MI200-alt-implementation.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">MI200 matrix fused multiply-add (MFMA) behavior specifics</p>
      </div>
    </a>
    <a class="right-next"
       href="../how-to/use-fusion-api.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Using the fusion API</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cuda-cudnn-versus-miopen-apis">CUDA cuDNN versus MIOpen APIs</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#handle-operations">Handle operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#tensor-operations">Tensor operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filter-operations">Filter operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#convolution-operations">Convolution operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#softmax-operations">Softmax operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#pooling-operations">Pooling operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#activation-operations">Activation operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#lrn-operations">LRN operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#batch-normalization-operations">Batch normalization operations</a></li>
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
