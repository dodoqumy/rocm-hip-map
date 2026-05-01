---
title: "Creating and running a rocAL pipeline &#8212; rocAL 2.5.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocAL/en/latest/how-to/rocAL-use-pipeline.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:22:51.450669+00:00
content_hash: "ee7272209c17e261"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="rocAL pipeline" name="description" />
<meta content="rocAL, ROCm, API, pipeline, decorator" name="keywords" />

    <title>Creating and running a rocAL pipeline &#8212; rocAL 2.5.0 Documentation</title>
  
  
  
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
    <link rel="stylesheet" type="text/css" href="../_static/styles/sphinx-book-theme.css?v=384b581d" />
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

    <script src="../_static/documentation_options.js?v=7769aa4a"></script>
    <script src="../_static/doctools.js?v=9bcbadda"></script>
    <script src="../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../_static/search.js?v=90a4452c"></script>
    <script src="../_static/scripts/sphinx-book-theme.js?v=efea14e4"></script>
    <script src="../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/rocAL-use-pipeline';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Using rocAL with PyTorch for training" href="rocAL-pytorch-framework.html" />
    <link rel="prev" title="rocAL Operators" href="../conceptual/rocAL-operators.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocal" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/rocAL-use-pipeline.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/rocAL" id="navgithub" role="button" aria-expanded="false" target="_blank" >
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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/rocAL/issues/new/choose" id="navsupport" role="button" aria-expanded="false" target="_blank" >
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
  
  
  
  
  
  
    <p class="title logo__title">rocAL 2.5.0 Documentation</p>
  
</a></div>
        <div class="sidebar-primary-item">

<button class="btn search-button-field search-button__button pst-js-only" title="Search" aria-label="Search" data-bs-placement="bottom" data-bs-toggle="tooltip">
 <i class="fa-solid fa-magnifying-glass"></i>
 <span class="search-button__default-text">Search</span>
 <span class="search-button__kbd-shortcut"><kbd class="kbd-shortcut__modifier">Ctrl</kbd>+<kbd class="kbd-shortcut__modifier">K</kbd></span>
</button></div>
        <div class="sidebar-primary-item"><nav class="bd-links bd-docs-nav" aria-label="Main">
    <div class="bd-toc-item navbar-nav active">
        <p aria-level="2" class="caption" role="heading"><span class="caption-text">Installation</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../install/rocAL-prerequisites.html">rocAL prerequisites</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/rocAL-package-install.html">Installing rocAL with the package installer</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/rocAL-build-and-install.html">Building and installing rocAL from source</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../conceptual/rocAL-operators.html">Operators</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Create and run the pipeline</a></li>
<li class="toctree-l1"><a class="reference internal" href="rocAL-pytorch-framework.html">Run PyTorch training</a></li>
<li class="toctree-l1"><a class="reference internal" href="rocAL-tensorflow-framework.html">Run TensorFlow training</a></li>
<li class="toctree-l1"><a class="reference internal" href="rocAL-jax-framework.html">Run JAX training</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Examples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../examples/examples.html">Framework integration examples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../reference/rocAL-pipeline.html">Pipelines</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/rocAL-and-RNNT.html">RNNT dataloading</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/rocAL-cpp-api.html">C++ API overview</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/rocAL-cpp-api-list.html">C++ reference</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/rocAL-python-api.html">Python API overview</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/rocAL-python-api-list.html">Python API reference</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Creating and running a rocAL pipeline</span></li>
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

</div></div>
      
    </div>
  
</div>
</div>
              
              

<div id="jb-print-docs-body" class="onlyprint">
    <h1>Creating and running a rocAL pipeline</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="creating-and-running-a-rocal-pipeline">
<h1>Creating and running a rocAL pipeline<a class="headerlink" href="#creating-and-running-a-rocal-pipeline" title="Link to this heading">#</a></h1>
<p>rocAL pipelines are used to load, decode, and augment audio, video, and image files that will be used in training and inference.</p>
<p>The pipeline can either be instantiated using the <code class="docutils literal notranslate"><span class="pre">Pipeline()</span></code> constructor or by using the <code class="docutils literal notranslate"><span class="pre">&#64;pipeline_def</span></code> decorator. This document demonstrates how to use the decorator. For information about using the constructor, see <a class="reference internal" href="../reference/rocAL-pipeline.html"><span class="doc">the rocAL pipeline reference</span></a>.</p>
<p>To create and use a pipeline in your rocAL application with the <code class="docutils literal notranslate"><span class="pre">&#64;pipeline_def</span></code> decorator, you’ll need to import <code class="docutils literal notranslate"><span class="pre">&#64;pipeline_def</span></code> from <code class="docutils literal notranslate"><span class="pre">amd.rocal.pipeline</span></code>:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span><span class="w"> </span><span class="nn">amd.rocal.pipeline</span><span class="w"> </span><span class="kn">import</span> <span class="n">pipeline_def</span>
</pre></div>
</div>
<p>There are two ways to run a pipeline. The first is using the <code class="docutils literal notranslate"><span class="pre">pipeline.run()</span></code> function. This function will run the pipeline exactly once on one batch of files. The second way is to use an iterator that runs all batches of files through the pipeline.</p>
<p>Audio, video, and image iterators are available, with some iterators designed to work with specific framework integrations. For example, if you’re using <a class="reference internal" href="rocAL-pytorch-framework.html"><span class="doc">PyTorch for training</span></a>, you would import the <code class="docutils literal notranslate"><span class="pre">ROCALClassificationIterator</span></code> in <code class="docutils literal notranslate"><span class="pre">amd.rocal.plugin.pytorch</span></code>:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span><span class="w"> </span><span class="nn">amd.rocal.plugin.pytorch</span><span class="w"> </span><span class="kn">import</span> <span class="n">ROCALClassificationIterator</span>
</pre></div>
</div>
<p>Generic iterators are imported from <code class="docutils literal notranslate"><span class="pre">amd.rocal.plugin.generic</span></code>:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span><span class="w"> </span><span class="nn">amd.rocal.plugin.generic</span><span class="w"> </span><span class="kn">import</span> <span class="n">ROCALClassificationIterator</span>
</pre></div>
</div>
<p>A pipeline is created by decorating a graph definition function with <code class="docutils literal notranslate"><span class="pre">&#64;pipeline_def</span></code>.</p>
<p>Graph definition functions are user-defined functions that import audio, video, or image files, decode them, and augment them. The <code class="docutils literal notranslate"><span class="pre">&#64;pipeline_def</span></code> decorator turns a graph definition function into a pipeline factory. The output of the graph definition function becomes the output of the pipeline.</p>
<p>For example, in <a class="reference external" href="https://github.com/ROCm/rocAL/tree/develop/tests/python_api/decoder.py"><code class="docutils literal notranslate"><span class="pre">decoder.py</span></code></a> the graph definition function, <code class="docutils literal notranslate"><span class="pre">image_decoder_pipeline</span></code>, reads in an image file, decodes it, and resizes it. It then returns the resized image:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="nd">@pipeline_def</span><span class="p">(</span><span class="n">seed</span><span class="o">=</span><span class="n">seed</span><span class="p">)</span>
<span class="k">def</span><span class="w"> </span><span class="nf">image_decoder_pipeline</span><span class="p">(</span><span class="n">device</span><span class="o">=</span><span class="s2">&quot;cpu&quot;</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">image_dir</span><span class="p">):</span>
  <span class="n">jpegs</span><span class="p">,</span> <span class="n">labels</span> <span class="o">=</span> <span class="n">fn</span><span class="o">.</span><span class="n">readers</span><span class="o">.</span><span class="n">file</span><span class="p">(</span><span class="n">file_root</span><span class="o">=</span><span class="n">path</span><span class="p">)</span>
  <span class="n">images</span> <span class="o">=</span> <span class="n">fn</span><span class="o">.</span><span class="n">decoders</span><span class="o">.</span><span class="n">image</span><span class="p">(</span><span class="n">jpegs</span><span class="p">,</span> <span class="n">file_root</span><span class="o">=</span><span class="n">path</span><span class="p">,</span> <span class="n">device</span><span class="o">=</span><span class="n">device</span><span class="p">,</span> <span class="n">output_type</span><span class="o">=</span><span class="n">types</span><span class="o">.</span><span class="n">RGB</span><span class="p">,</span> <span class="n">shard_id</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">num_shards</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">random_shuffle</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
  <span class="k">return</span> <span class="n">fn</span><span class="o">.</span><span class="n">resize</span><span class="p">(</span><span class="n">images</span><span class="p">,</span> <span class="n">device</span><span class="o">=</span><span class="n">device</span><span class="p">,</span> <span class="n">resize_width</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span> <span class="n">resize_height</span><span class="o">=</span><span class="mi">300</span><span class="p">)</span>
</pre></div>
</div>
<p>The pipeline object requires additional parameters such as batch size, number of threads, and device ID. These are passed to the decorated function.</p>
<p>For example, in <code class="docutils literal notranslate"><span class="pre">decoder.py</span></code>:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="n">pipe</span> <span class="o">=</span> <span class="n">image_decoder_pipeline</span><span class="p">(</span><span class="n">batch_size</span><span class="o">=</span><span class="n">bs</span><span class="p">,</span> <span class="n">num_threads</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">device_id</span><span class="o">=</span><span class="n">gpu_id</span><span class="p">,</span> <span class="n">rocal_cpu</span><span class="o">=</span><span class="n">rocal_cpu</span><span class="p">,</span> <span class="n">tensor_layout</span><span class="o">=</span><span class="n">types</span><span class="o">.</span><span class="n">NHWC</span><span class="p">,</span> <span class="n">reverse_channels</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">mean</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span> <span class="n">std</span><span class="o">=</span><span class="p">[</span><span class="mi">255</span><span class="p">,</span><span class="mi">255</span><span class="p">,</span><span class="mi">255</span><span class="p">],</span> <span class="n">device</span><span class="o">=</span><span class="n">rocal_device</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">img_folder</span><span class="p">)</span>
</pre></div>
</div>
<p>See the <a class="reference internal" href="../doxygen/html/pipeline_8py.html"><span class="doc">pipeline API reference</span></a> for the complete list of parameters.</p>
<p>Once the pipeline is created, <code class="docutils literal notranslate"><span class="pre">pipeline.build()</span></code> is called to build the pipeline. The pipeline can only be run after it’s been built.</p>
<p>Use an iterator to run the pipeline over every batch of files. In <code class="docutils literal notranslate"><span class="pre">decoder.py</span></code>, the pipeline is run using <code class="docutils literal notranslate"><span class="pre">ROCALClassificationIterator</span></code>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">show_pipeline_output</span><span class="p">(</span><span class="n">pipe</span><span class="p">,</span> <span class="n">device</span><span class="p">):</span>
  <span class="n">pipe</span><span class="o">.</span><span class="n">build</span><span class="p">()</span>
  <span class="n">data_loader</span> <span class="o">=</span> <span class="n">ROCALClassificationIterator</span><span class="p">(</span><span class="n">pipe</span><span class="p">,</span> <span class="n">device</span><span class="o">=</span><span class="n">device</span><span class="p">)</span>
  <span class="n">images</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">data_loader</span><span class="p">))</span>
  <span class="n">show_images</span><span class="p">(</span><span class="n">images</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">])</span>

<span class="p">[</span><span class="o">...</span><span class="p">]</span>

<span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
  <span class="p">[</span><span class="o">...</span><span class="p">]</span>
  <span class="n">pipe</span> <span class="o">=</span> <span class="n">image_decoder_pipeline</span><span class="p">(</span><span class="n">batch_size</span><span class="o">=</span><span class="n">bs</span><span class="p">,</span> <span class="n">num_threads</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">device_id</span><span class="o">=</span><span class="n">gpu_id</span><span class="p">,</span> <span class="n">rocal_cpu</span><span class="o">=</span><span class="n">rocal_cpu</span><span class="p">,</span> <span class="n">tensor_layout</span><span class="o">=</span><span class="n">types</span><span class="o">.</span><span class="n">NHWC</span><span class="p">,</span><span class="n">reverse_channels</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">mean</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span> <span class="n">std</span><span class="o">=</span><span class="p">[</span><span class="mi">255</span><span class="p">,</span><span class="mi">255</span><span class="p">,</span><span class="mi">255</span><span class="p">],</span> <span class="n">device</span><span class="o">=</span><span class="n">rocal_device</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="n">img_folder</span><span class="p">)</span>
  <span class="n">show_pipeline_output</span><span class="p">(</span><span class="n">pipe</span><span class="p">,</span> <span class="n">device</span><span class="o">=</span><span class="n">rocal_device</span><span class="p">)</span>
</pre></div>
</div>
<p>The iterator will run the pipeline until all batches of files have been processed.</p>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../conceptual/rocAL-operators.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">rocAL Operators</p>
      </div>
    </a>
    <a class="right-next"
       href="rocAL-pytorch-framework.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Using rocAL with PyTorch for training</p>
      </div>
      <i class="fa-solid fa-angle-right"></i>
    </a>
</div>
                </footer>
              
            </div>
            
            
              
            
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
