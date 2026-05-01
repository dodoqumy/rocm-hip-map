---
title: "Using the find APIs and immediate mode &#8212; MIOpen 3.5.1 Documentation"
source_url: "https://rocm.docs.amd.com/projects/MIOpen/en/latest/how-to/find-and-immediate.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:36.628853+00:00
content_hash: "73b1f9f8b751d041"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Using the MIOpen find and immediate modes" name="description" />
<meta content="MIOpen, ROCm, API, documentation, find mode, immediate mode" name="keywords" />

    <title>Using the find APIs and immediate mode &#8212; MIOpen 3.5.1 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/find-and-immediate';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Using NHWC Batch Normalization with PyTorch" href="use-nhwc-batchnorm-in-pytorch.html" />
    <link rel="prev" title="Logging and debugging" href="debug-log.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-miopen" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/find-and-immediate.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1"><a class="reference internal" href="debug-log.html">Log and debug</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Use the find APIs and immediate mode</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Using the find APIs and immediate mode</span></li>
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
    <h1>Using the find APIs and immediate mode</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#immediate-mode">Immediate mode</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#immediate-mode-fallback">Immediate mode fallback</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#ai-based-heuristic-fallback-default">AI-based heuristic fallback (default)</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#weighted-throughput-index-based-fallback">Weighted throughput index-based fallback</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#limitations-of-immediate-mode">Limitations of immediate mode</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#backend-limitations">Backend limitations</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#find-modes">Find modes</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="using-the-find-apis-and-immediate-mode">
<h1>Using the find APIs and immediate mode<a class="headerlink" href="#using-the-find-apis-and-immediate-mode" title="Link to this heading">#</a></h1>
<p>MIOpen contains several convolution algorithms for each stage of training or inference. Prior to
MIOpen version 2.0, you had to call find methods to generate a set of applicable algorithms.</p>
<p>Here’s a typical workflow for the find stage:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenConvolutionForwardGetWorkSpaceSize</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">weightTensorDesc</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">inputTensorDesc</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">outputTensorDesc</span><span class="p">,</span>
<span class="w">                                        </span><span class="o">&amp;</span><span class="n">maxWorkSpaceSize</span><span class="p">);</span>

<span class="c1">// &lt; allocate workspace &gt;</span>


<span class="c1">// NOTE:</span>
<span class="c1">// The miopenFindConvolution*() call is expensive in terms of run time and required workspace.</span>
<span class="c1">// Therefore, we highly recommend reserving the required algorithm and workspace so that you can</span>
<span class="c1">// reuse them later (within the lifetime of the same MIOpen handle object).</span>
<span class="c1">// With this approach, there should be no need to invoke miopenFind*() more than once per</span>
<span class="c1">// application lifetime.</span>

<span class="n">miopenFindConvolutionForwardAlgorithm</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">inputTensorDesc</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">input_device_mem</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">weightTensorDesc</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">weight_device_mem</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">outputTensorDesc</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">output_device_mem</span><span class="p">,,</span>
<span class="w">                                      </span><span class="n">request_algo_count</span><span class="p">,</span>
<span class="w">                                      </span><span class="o">&amp;</span><span class="n">ret_algo_count</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">perf_results</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">workspace_device_mem</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">maxWorkSpaceSize</span><span class="p">,</span>
<span class="w">                                      </span><span class="mi">1</span><span class="p">);</span>

<span class="c1">// &lt; select fastest algorithm &gt;</span>

<span class="c1">// &lt; free previously allocated workspace and allocate workspace required for the selected algorithm&gt;</span>

<span class="n">miopenConvolutionForward</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">alpha</span><span class="p">,</span>
<span class="w">                        </span><span class="n">inputTensorDesc</span><span class="p">,</span>
<span class="w">                        </span><span class="n">input_device_mem</span><span class="p">,</span>
<span class="w">                        </span><span class="n">weightTensorDesc</span><span class="p">,</span>
<span class="w">                        </span><span class="n">weight_device_mem</span><span class="p">,</span>
<span class="w">                        </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">                        </span><span class="n">perf_results</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">fwd_algo</span><span class="p">,</span><span class="w"> </span><span class="c1">// use the fastest algo</span>
<span class="w">                        </span><span class="o">&amp;</span><span class="n">beta</span><span class="p">,</span>
<span class="w">                        </span><span class="n">outputTensorDesc</span><span class="p">,</span>
<span class="w">                        </span><span class="n">output_device_mem</span><span class="p">,</span>
<span class="w">                        </span><span class="n">workspace_device_mem</span><span class="p">,</span>
<span class="w">                        </span><span class="n">perf_results</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">memory</span><span class="p">);</span><span class="w"> </span><span class="c1">//workspace size</span>
</pre></div>
</div>
<p>The results of the find call are returned in an array of <code class="docutils literal notranslate"><span class="pre">miopenConvAlgoPerf_t</span></code> structures in order of
performance, with the fastest at index <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
<p>This call sequence is only run once per session, as it’s inherently expensive. Within the sequence,
<code class="docutils literal notranslate"><span class="pre">miopenFindConvolution*()</span></code> is the most expensive call. <code class="docutils literal notranslate"><span class="pre">miopenFindConvolution*()</span></code> caches its own
results on disk so subsequent calls during the same MIOpen session run faster.</p>
<p>Internally, MIOpen’s find calls compile and benchmark a set of <code class="docutils literal notranslate"><span class="pre">solvers</span></code> contained in
<code class="docutils literal notranslate"><span class="pre">miopenConvAlgoPerf_t</span></code>. This is performed in parallel with <code class="docutils literal notranslate"><span class="pre">miopenConvAlgorithm_t</span></code>. You can
control the level of parallelism using an environmental variable. See the debugging section on
<a class="reference internal" href="debug-log.html#control-parallel-compilation"><span class="std std-ref">controlling parallel compilation</span></a> for more information.</p>
<section id="immediate-mode">
<h2>Immediate mode<a class="headerlink" href="#immediate-mode" title="Link to this heading">#</a></h2>
<p>MIOpen v2.0 introduces immediate mode, which removes the requirement for
<code class="docutils literal notranslate"><span class="pre">miopenFindConvolution*()</span></code> calls, thereby reducing runtime costs. In this mode, you can query the
MIOpen runtime for all of the supported solutions for a given convolution configuration. The sequence
of operations for immediate mode is similar to launching regular convolutions in MIOpen, for instance, through
the <code class="docutils literal notranslate"><span class="pre">miopenFindConvolution*()</span></code> API. However, in this case, the different APIs have a lower
runtime cost.</p>
<p>A typical convolution call is similar to the following sequence:</p>
<ul class="simple">
<li><p>Construct the MIOpen handle and relevant descriptors, such as the convolution descriptor.</p></li>
<li><p>With the above data structures, call <code class="docutils literal notranslate"><span class="pre">miopenConvolution*GetSolutionCount</span></code> to get the
maximum number of supported solutions for the convolution descriptor.</p></li>
<li><p>Use the obtained count to allocate memory for the <code class="docutils literal notranslate"><span class="pre">miopenConvSolution_t</span></code> structure
(introduced in MIOpen v2.0).</p></li>
<li><p>Call <code class="docutils literal notranslate"><span class="pre">miopenConvolution*GetSolution</span></code> to populate the <code class="docutils literal notranslate"><span class="pre">miopenConvSolution_t</span></code> structures
allocated above. The returned list is sorted in order of best performance, where the first element is the
fastest.</p></li>
<li><p>While the above structure returns the amount of workspace required for an algorithm, you can
query the amount of a workspace required for a known solution ID using
<code class="docutils literal notranslate"><span class="pre">miopenConvolution*GetSolutionWorkspaceSize</span></code>. However, this is not a requirement because the
structure returned by <code class="docutils literal notranslate"><span class="pre">miopenConvolution*GetSolution</span></code> already has this information.</p></li>
<li><p>Initiate the convolution operation in <code class="docutils literal notranslate"><span class="pre">immediate</span></code> mode by calling
<code class="docutils literal notranslate"><span class="pre">miopenConvolution*Immediate</span></code>. This populates the output tensor descriptor with the respective
convolution result. However, the first call to <code class="docutils literal notranslate"><span class="pre">miopenConvolution*Immediate</span></code> might take more
time because the kernel must be compiled if it isn’t present in the kernel cache.</p></li>
<li><p>Optionally, you can compile the solution of choice by calling <code class="docutils literal notranslate"><span class="pre">miopenConvolution*CompileSolution</span></code>.
This ensures that the kernel represented by the chosen solution is populated in the kernel cache,
removing the need to compile it.</p></li>
</ul>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenConvolutionForwardGetSolutionCount</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">weightTensorDesc</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">inputTensorDesc</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">outputTensorDesc</span><span class="p">,</span>
<span class="w">                                        </span><span class="o">&amp;</span><span class="n">solutionCount</span><span class="p">);</span>


<span class="c1">// &lt; allocate an array of miopenConvSolution_t of size solutionCount &gt;</span>


<span class="n">miopenConvolutionForwardGetSolution</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span>
<span class="w">                                    </span><span class="n">weightTensorDesc</span><span class="p">,</span>
<span class="w">                                    </span><span class="n">inputTensorDesc</span><span class="p">,</span>
<span class="w">                                    </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">                                    </span><span class="n">outputTensorDesc</span><span class="p">,</span>
<span class="w">                                    </span><span class="n">solutionCount</span><span class="p">,</span>
<span class="w">                                    </span><span class="o">&amp;</span><span class="n">actualCount</span><span class="p">,</span>
<span class="w">                                    </span><span class="n">solutions</span><span class="p">);</span>

<span class="c1">// &lt; select a solution from solutions array &gt;</span>

<span class="n">miopenConvolutionForwardGetSolutionWorkspaceSize</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span>
<span class="w">                                                </span><span class="n">weightTensorDesc</span><span class="p">,</span>
<span class="w">                                                </span><span class="n">inputTensorDesc</span><span class="p">,</span>
<span class="w">                                                </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">                                                </span><span class="n">outputTensorDesc</span><span class="p">,</span>
<span class="w">                                                </span><span class="n">selected</span><span class="o">-&gt;</span><span class="n">solution_id</span><span class="p">,</span>
<span class="w">                                                </span><span class="o">&amp;</span><span class="n">ws_size</span><span class="p">);</span>

<span class="c1">// &lt; allocate solution workspace of size ws_size &gt;</span>


<span class="c1">// This stage is optional.</span>
<span class="n">miopenConvolutionForwardCompileSolution</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">weightTensorDesc</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">inputTensorDesc</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">outputTensorDesc</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">selected</span><span class="o">-&gt;</span><span class="n">solution_id</span><span class="p">);</span>



<span class="n">miopenConvolutionForwardImmediate</span><span class="p">(</span><span class="n">handle</span><span class="p">,</span>
<span class="w">                                  </span><span class="n">weightTensor</span><span class="p">,</span>
<span class="w">                                  </span><span class="n">weight_device_mem</span><span class="p">,</span>
<span class="w">                                  </span><span class="n">inputTensorDesc</span><span class="p">,</span>
<span class="w">                                  </span><span class="n">input_device_mem</span><span class="p">,</span>
<span class="w">                                  </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">                                  </span><span class="n">outputTensorDesc</span><span class="p">,</span>
<span class="w">                                  </span><span class="n">output_device_mem</span><span class="p">,</span>
<span class="w">                                  </span><span class="n">workspace_device_mem</span><span class="p">,</span>
<span class="w">                                  </span><span class="n">ws_size</span><span class="p">,</span>
<span class="w">                                  </span><span class="n">selected</span><span class="o">-&gt;</span><span class="n">solution_id</span><span class="p">);</span>
</pre></div>
</div>
<section id="immediate-mode-fallback">
<h3>Immediate mode fallback<a class="headerlink" href="#immediate-mode-fallback" title="Link to this heading">#</a></h3>
<p>Although immediate mode is underpinned by <a class="reference internal" href="../conceptual/finddb.html"><span class="doc">FindDb</span></a>, it might not contain every
configuration of interest. If FindDb encounters a database miss, there are two fallback paths it can take,
depending on whether the CMake variable <code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_AI_IMMED_MODE_FALLBACK</span></code> is set to
<code class="docutils literal notranslate"><span class="pre">ON</span></code> or <code class="docutils literal notranslate"><span class="pre">OFF</span></code>.</p>
<p>If you require the best possible performance, run the find stage at least once.</p>
<section id="ai-based-heuristic-fallback-default">
<h4>AI-based heuristic fallback (default)<a class="headerlink" href="#ai-based-heuristic-fallback-default" title="Link to this heading">#</a></h4>
<p>If <code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_AI_IMMED_MODE_FALLBACK</span></code> is set to <code class="docutils literal notranslate"><span class="pre">ON</span></code> (the default), the immediate mode
behavior upon encountering a database miss is to use an AI-based heuristic to pick the optimal
solution.</p>
<p>It first checks the applicability of the AI-based heuristic for the given configuration. If the heuristic is
applicable, it feeds various parameters of the given configuration into a neural network that has been
tuned to predict the optimal solution with 90% accuracy.</p>
</section>
<section id="weighted-throughput-index-based-fallback">
<h4>Weighted throughput index-based fallback<a class="headerlink" href="#weighted-throughput-index-based-fallback" title="Link to this heading">#</a></h4>
<p>When <code class="docutils literal notranslate"><span class="pre">MIOPEN_ENABLE_AI_IMMED_MODE_FALLBACK</span></code> is set to <code class="docutils literal notranslate"><span class="pre">OFF</span></code> or the AI heuristic is not
applicable for the given convolution configuration, immediate mode
uses a weighted throughput index-based mechanism when encountering
a database miss. This mechanism estimates which solution
would be optimal based on the convolution configuration parameters.</p>
</section>
</section>
<section id="limitations-of-immediate-mode">
<h3>Limitations of immediate mode<a class="headerlink" href="#limitations-of-immediate-mode" title="Link to this heading">#</a></h3>
<p>System FindDb has only been populated for these architectures:</p>
<ul class="simple">
<li><p>gfx906 with 64 CUs</p></li>
<li><p>gfx906 with 60 CUs</p></li>
<li><p>gfx900 with 64 CUs</p></li>
<li><p>gfx900 with 56 CUs</p></li>
</ul>
<p>If your architecture isn’t listed, you must run the find API on your system (once per application)
to take advantage of immediate mode’s more efficient behavior.</p>
</section>
<section id="backend-limitations">
<h3>Backend limitations<a class="headerlink" href="#backend-limitations" title="Link to this heading">#</a></h3>
<p>OpenCL support for immediate mode via the fallback is limited to <code class="docutils literal notranslate"><span class="pre">FP32</span></code> datatypes. This is because the
current release’s fallback path uses GEMM, which is serviced through MIOpenGEMM (on
OpenCL). MIOpenGEMM only contains support for <code class="docutils literal notranslate"><span class="pre">FP32</span></code>.</p>
<p>The HIP backend uses rocBLAS as its fallback path, which contains a more robust set of data types.</p>
</section>
</section>
<section id="find-modes">
<span id="id1"></span><h2>Find modes<a class="headerlink" href="#find-modes" title="Link to this heading">#</a></h2>
<p>MIOpen provides a set of find modes that are used to accelerate find API calls. Set the different
modes by using the <code class="docutils literal notranslate"><span class="pre">MIOPEN_FIND_MODE</span></code> environment variable with one of these values:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">NORMAL</span></code>/<code class="docutils literal notranslate"><span class="pre">1</span></code> (normal find): This is the full find mode call, which benchmarks all the solvers and
returns a list.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">FAST</span></code>/<code class="docutils literal notranslate"><span class="pre">2</span></code> (fast find): Checks <a class="reference internal" href="../conceptual/finddb.html"><span class="doc">FindDb</span></a> for an entry. If there’s a FindDb
hit, it uses that entry. If there’s a miss, it uses the immediate mode fallback. This mode offers fast start-up times
at the cost of GPU performance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HYBRID</span></code>/<code class="docutils literal notranslate"><span class="pre">3</span></code> or unset <code class="docutils literal notranslate"><span class="pre">MIOPEN_FIND_MODE</span></code> (hybrid find): Checks
<a class="reference internal" href="../conceptual/finddb.html"><span class="doc">FindDb</span></a> for an entry. If there’s a FindDb hit, it uses that entry. If there’s a
miss, it uses the existing find machinery. This mode offers slower start-up times than fast find without the GPU
performance drop.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">4</span></code>: This value is reserved and should not be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">DYNAMIC_HYBRID</span></code>/<code class="docutils literal notranslate"><span class="pre">5</span></code> (dynamic hybrid find): Checks <a class="reference internal" href="../conceptual/finddb.html"><span class="doc">FindDb</span></a> for an
entry. If there’s a FindDb hit, it uses that entry. If there’s a miss, it uses the existing find machinery,
skipping non-dynamic kernels. It offers faster start-up times than hybrid find, but GPU performance
might decrease.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">TRUST_VERIFY</span></code>/<code class="docutils literal notranslate"><span class="pre">6</span></code> (trust verify find): Checks <a class="reference internal" href="../conceptual/finddb.html"><span class="doc">FindDb</span></a> for an entry.
If there’s a UserFindDb hit, it uses that entry.
If there’s a FindDb hit, the result is evaluated. If the ratio of evaluated to reported result time is
below the tolerance threshold, the result is used and added to the UserFindDb. Otherwise tuning will be triggered.
If there’s a miss, tuning will be triggered, skipping non-dynamic kernels.
Tuning time is constrained by a max compile time and tuning patience
This mode can have slow start-up times but typically selects the most performant solutions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">TRUST_VERIFY_FULL</span></code>/<code class="docutils literal notranslate"><span class="pre">7</span></code> (trust verify full find): Checks <a class="reference internal" href="../conceptual/finddb.html"><span class="doc">FindDb</span></a>
Same as TRUST_VERIFY, with no limitations on tuning time.</p></li>
</ul>
<p>The default find mode is <code class="docutils literal notranslate"><span class="pre">DYNAMIC_HYBRID</span></code>. To run the full <code class="docutils literal notranslate"><span class="pre">NORMAL</span></code> find mode, use
<code class="docutils literal notranslate"><span class="pre">export</span> <span class="pre">MIOPEN_FIND_MODE=NORMAL</span></code> or <code class="docutils literal notranslate"><span class="pre">export</span> <span class="pre">MIOPEN_FIND_MODE=1</span></code>.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="debug-log.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Logging and debugging</p>
      </div>
    </a>
    <a class="right-next"
       href="use-nhwc-batchnorm-in-pytorch.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Using NHWC Batch Normalization with PyTorch</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#immediate-mode">Immediate mode</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#immediate-mode-fallback">Immediate mode fallback</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#ai-based-heuristic-fallback-default">AI-based heuristic fallback (default)</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#weighted-throughput-index-based-fallback">Weighted throughput index-based fallback</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#limitations-of-immediate-mode">Limitations of immediate mode</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#backend-limitations">Backend limitations</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#find-modes">Find modes</a></li>
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
