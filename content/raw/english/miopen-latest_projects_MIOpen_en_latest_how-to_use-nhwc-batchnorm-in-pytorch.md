---
title: "Using NHWC Batch Normalization with PyTorch &#8212; MIOpen 3.5.1 Documentation"
source_url: "https://rocm.docs.amd.com/projects/MIOpen/en/latest/how-to/use-nhwc-batchnorm-in-pytorch.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:45.113279+00:00
content_hash: "25f68cc283f9a819"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Using NHWC Batch Normalization on PyTorch" name="description" />
<meta content="MIOpen, ROCm, API, documentation, NHWC Batch Normalization, PyTorch" name="keywords" />

    <title>Using NHWC Batch Normalization with PyTorch &#8212; MIOpen 3.5.1 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/use-nhwc-batchnorm-in-pytorch';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="API reference library" href="../reference/index.html" />
    <link rel="prev" title="Using the find APIs and immediate mode" href="find-and-immediate.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-miopen" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/use-nhwc-batchnorm-in-pytorch.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1"><a class="reference internal" href="find-and-immediate.html">Use the find APIs and immediate mode</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Use NHWC Batch Normalization with PyTorch</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Using NHWC Batch Normalization with PyTorch</span></li>
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
    <h1>Using NHWC Batch Normalization with PyTorch</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#nhwc-versus-nchw">NHWC versus NCHW</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#batch-normalization">Batch Normalization</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#enabling-or-disabling-nhwc-batch-normalization-for-miopen-using-pytorch">Enabling or disabling NHWC Batch Normalization for MIOpen using PyTorch</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#pytorch-branch-support">PyTorch branch support</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-configurations">Supported configurations</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#disabling-miopen-for-batch-normalization-in-pytorch">Disabling MIOpen for Batch Normalization in PyTorch</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#verifying-nhwc-batch-normalization-use-with-miopen">Verifying NHWC Batch Normalization use with MIOpen</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#running-batch-normalization-tests">Running Batch Normalization tests</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="using-nhwc-batch-normalization-with-pytorch">
<h1>Using NHWC Batch Normalization with PyTorch<a class="headerlink" href="#using-nhwc-batch-normalization-with-pytorch" title="Link to this heading">#</a></h1>
<p>This topic explains how to use NHWC Batch Normalization for MIOpen operations in PyTorch. NHWC is
a deep-learning memory format that has certain performance advantages over traditional
memory formats.</p>
<p>For information about installing and using PyTorch with ROCm, see <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html" title="(in ROCm installation on Linux v7.2.2)"><span class="xref std std-doc">PyTorch on ROCm</span></a>.
For a list of the ROCm components and features that PyTorch supports, see <a class="reference external" href="https://rocm.docs.amd.com/en/latest/compatibility/ml-compatibility/pytorch-compatibility.html" title="(in ROCm Documentation v7.2.2)"><span class="xref std std-doc">PyTorch compatibility</span></a>.
For more background on using PyTorch and ROCm for AI tasks, see
<a class="reference external" href="https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/pytorch-training.html" title="(in ROCm Documentation v7.2.2)"><span class="xref std std-doc">Training a model with PyTorch for ROCm</span></a>.</p>
<section id="nhwc-versus-nchw">
<h2>NHWC versus NCHW<a class="headerlink" href="#nhwc-versus-nchw" title="Link to this heading">#</a></h2>
<p>NHWC (also known as “Channels Last”) and NCHW are two types of memory formats for deep learning. They describe how
multidimensional arrays (nD) are translated to a linear (one-dimensional) memory address space.</p>
<ul class="simple">
<li><p>NCHW (Number of samples, channels, height, width): This is the default data layout in which channels
are stored separately from one another. The height and width information is stored after
the channels.</p></li>
<li><p>NHWC (Number of samples, height, width, channels): In this alternative format, channels are stored next
to each other after the height and width information.</p></li>
</ul>
<p>The performance of NHWC is better than that of NCHW and is close to that observed when using a blocked memory format. NHWC is also
easier to work with for common operations.</p>
<p>For more information about these memory formats, see the
<a class="reference external" href="https://pytorch.org/tutorials/intermediate/memory_format_tutorial.html">PyTorch memory format documentation</a>
and the <a class="reference external" href="https://intel.github.io/intel-extension-for-pytorch/cpu/latest/tutorials/features/nhwc.html">Intel Extension for PyTorch GitHub</a>.</p>
</section>
<section id="batch-normalization">
<h2>Batch Normalization<a class="headerlink" href="#batch-normalization" title="Link to this heading">#</a></h2>
<p>Batch Normalization (also known as Batchnorm or BatchNorm) enables higher learning rates and reduces initialization overhead by
normalizing layer inputs. Ordinarily, the distribution of the inputs to each layer changes as the
parameters to the previous layer change. This makes it more difficult to train deep learning models
and leads to lower learning rates. With Batch Normalization, normalization is part of the architecture
and is performed for each training batch.</p>
<p>For more information on Batch Normalization, see <a class="reference external" href="https://arxiv.org/abs/1502.03167">Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift</a>.</p>
</section>
<section id="enabling-or-disabling-nhwc-batch-normalization-for-miopen-using-pytorch">
<h2>Enabling or disabling NHWC Batch Normalization for MIOpen using PyTorch<a class="headerlink" href="#enabling-or-disabling-nhwc-batch-normalization-for-miopen-using-pytorch" title="Link to this heading">#</a></h2>
<p>The PyTorch open-source tensor library provides support for using NHWC Batch Normalization with MIOpen.
In addition to Batch Normalization, NHWC support is also available for convolution and other MIOpen features.</p>
<p>NHWC Batch Normalization support in MIOpen can be used in a PyTorch environment using ROCm 7.0 or later.
This configuration supports 2D and 3D NHWC Batch Normalization. 1D Batch Normalization is not applicable to the NHWC format.</p>
<section id="pytorch-branch-support">
<h3>PyTorch branch support<a class="headerlink" href="#pytorch-branch-support" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">ROCm/pytorch</span></code> PyTorch images support NHWC Batch Normalization. ROCm 7.0 or later is required.
The following PyTorch branches support the NHWC Batch Normalization feature:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://github.com/ROCm/pytorch/tree/release/2.6">release/2.6</a></p></li>
<li><p><a class="reference external" href="https://github.com/ROCm/pytorch/tree/release/2.7">release/2.7</a></p></li>
</ul>
<p>In the <code class="docutils literal notranslate"><span class="pre">release/2.7</span></code> PyTorch branch, NHWC Batch Normalization support in MIOpen is enabled by default.
To use the native Batch Normalization approach with this image, use this command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nv">PYTORCH_MIOPEN_SUGGEST_NHWC_BATCHNORM</span><span class="o">=</span><span class="m">0</span>
</pre></div>
</div>
<p>In the <code class="docutils literal notranslate"><span class="pre">release/2.6</span></code> PyTorch branch, NHWC Batch Normalization support in MIOpen is disabled by default.
To enable NHWC Batch Normalization for this image, use this command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nv">PYTORCH_MIOPEN_SUGGEST_NHWC_BATCHNORM</span><span class="o">=</span><span class="m">1</span>
</pre></div>
</div>
<p>For information about installing and using PyTorch on ROCm, see <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html" title="(in ROCm installation on Linux v7.2.2)"><span class="xref std std-doc">PyTorch on ROCm</span></a>.</p>
</section>
</section>
<section id="supported-configurations">
<h2>Supported configurations<a class="headerlink" href="#supported-configurations" title="Link to this heading">#</a></h2>
<p>The following table shows the Batch Normalization support for NHWC and NCHW with various data types and modes.
It also indicates which backend is used with and without the <code class="docutils literal notranslate"><span class="pre">PYTORCH_MIOPEN_SUGGEST_NHWC_BATCHNORM</span></code>
environment variable enabled.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Mixed mode means that the Batch Normalization module has a different type than the inputs, for example,
an input or gradient data type of <code class="docutils literal notranslate"><span class="pre">FP16</span></code> or <code class="docutils literal notranslate"><span class="pre">BF16</span></code> and a Batch Normalization type of <code class="docutils literal notranslate"><span class="pre">FP32</span></code>.
If the Batch Normalization module has the same data type as the inputs, for instance, an
input or gradient data type of <code class="docutils literal notranslate"><span class="pre">FP32</span></code> and a Batch Normalization module that is also <code class="docutils literal notranslate"><span class="pre">FP32</span></code>, the mode is
“not mixed”.</p>
</div>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 16.7%" />
<col style="width: 16.7%" />
<col style="width: 12.5%" />
<col style="width: 12.5%" />
<col style="width: 20.8%" />
<col style="width: 20.8%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Input data type</p></th>
<th class="head"><p>Memory format</p></th>
<th class="head"><p>Mode</p></th>
<th class="head"><p>Mixed/not mixed</p></th>
<th class="head"><p>Backend with NHWC Batch Normalization enabled</p></th>
<th class="head"><p>Backend with NHWC Batch Normalization disabled</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">float32</span></code></p></td>
<td><p>NCHW</p></td>
<td><p>1D/2D/3D</p></td>
<td><p>not mixed</p></td>
<td><p>MIOpen</p></td>
<td><p>MIOpen</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">float32</span></code></p></td>
<td><p>NHWC</p></td>
<td><p>2D/3D</p></td>
<td><p>not mixed</p></td>
<td><p>native</p></td>
<td><p>MIOpen</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">float16</span></code></p></td>
<td><p>NCHW</p></td>
<td><p>1D/2D/3D</p></td>
<td><p>mixed</p></td>
<td><p>MIOpen</p></td>
<td><p>MIOpen</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">float16</span></code></p></td>
<td><p>NCHW</p></td>
<td><p>1D/2D/3D</p></td>
<td><p>not mixed</p></td>
<td><p>native</p></td>
<td><p>native</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">float16</span></code></p></td>
<td><p>NHWC</p></td>
<td><p>2D/3D</p></td>
<td><p>mixed</p></td>
<td><p>native</p></td>
<td><p>MIOpen</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">float16</span></code></p></td>
<td><p>NHWC</p></td>
<td><p>2D/3D</p></td>
<td><p>not mixed</p></td>
<td><p>native</p></td>
<td><p>native</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">bfloat16</span></code></p></td>
<td><p>NCHW</p></td>
<td><p>1D/2D/3D</p></td>
<td><p>mixed</p></td>
<td><p>MIOpen (*)</p></td>
<td><p>MIOpen (*)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">bfloat16</span></code></p></td>
<td><p>NCHW</p></td>
<td><p>1D/2D/3D</p></td>
<td><p>not mixed</p></td>
<td><p>native</p></td>
<td><p>native</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">bfloat16</span></code></p></td>
<td><p>NHWC</p></td>
<td><p>2D/3D</p></td>
<td><p>mixed</p></td>
<td><p>native</p></td>
<td><p>MIOpen</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">bfloat16</span></code></p></td>
<td><p>NHWC</p></td>
<td><p>2D/3D</p></td>
<td><p>not mixed</p></td>
<td><p>native</p></td>
<td><p>native</p></td>
</tr>
</tbody>
</table>
</div>
<p>(*) MIOpen is used with ROCm 6.4 and later. Otherwise, the native backend is used.</p>
</section>
<section id="disabling-miopen-for-batch-normalization-in-pytorch">
<h2>Disabling MIOpen for Batch Normalization in PyTorch<a class="headerlink" href="#disabling-miopen-for-batch-normalization-in-pytorch" title="Link to this heading">#</a></h2>
<p>In some situations, you might not want to use MIOpen as the backend for Batch Normalization operations.
To disable the use of MIOpen with Batch Normalization, add this code to your application.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="n">inp</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="n">size</span><span class="p">,</span> <span class="n">requires_grad</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">grad</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="n">size</span><span class="p">,</span> <span class="n">requires_grad</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">mod</span> <span class="o">=</span> <span class="n">nn</span><span class="o">.</span><span class="n">BatchNorm2d</span><span class="p">(</span><span class="n">inp</span><span class="o">.</span><span class="n">size</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span> <span class="n">device</span><span class="o">=</span><span class="s2">&quot;cuda&quot;</span><span class="p">)</span>

<span class="k">with</span> <span class="n">torch</span><span class="o">.</span><span class="n">backends</span><span class="o">.</span><span class="n">cudnn</span><span class="o">.</span><span class="n">flags</span><span class="p">(</span><span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span> <span class="c1"># this line disables MIOpen for the two lines below, native batchnorm will be used</span>

   <span class="n">out</span> <span class="o">=</span> <span class="n">mod</span><span class="p">(</span><span class="n">inp</span><span class="p">)</span>
   <span class="n">out</span><span class="o">.</span><span class="n">backward</span><span class="p">(</span><span class="n">grad</span><span class="p">)</span>
</pre></div>
</div>
</section>
<section id="verifying-nhwc-batch-normalization-use-with-miopen">
<h2>Verifying NHWC Batch Normalization use with MIOpen<a class="headerlink" href="#verifying-nhwc-batch-normalization-use-with-miopen" title="Link to this heading">#</a></h2>
<p>For some operations, it can be difficult to determine the backend and memory format used.
To verify whether MIOpen is being used and whether the memory format is NHWC or NCHW, run your program
with the following environment variable:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nv">MIOPEN_ENABLE_LOGGING_CMD</span><span class="o">=</span><span class="m">1</span>
</pre></div>
</div>
<p>Here is an example command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nv">MIOPEN_ENABLE_LOGGING_CMD</span><span class="o">=</span><span class="m">1</span><span class="w"> </span>python<span class="w"> </span>test_nn.py<span class="w"> </span>-v<span class="w"> </span>-k<span class="w"> </span>test_batchnorm_cudnn_nhwc
</pre></div>
</div>
<p>The output might look like this:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>MIOpen<span class="o">(</span>HIP<span class="o">)</span>:<span class="w"> </span>Command<span class="w"> </span><span class="o">[</span>LogCmdBNorm<span class="o">]</span><span class="w"> </span>./bin/MIOpenDriver<span class="w"> </span>bnorm<span class="w"> </span>-n<span class="w"> </span><span class="m">4</span><span class="w"> </span>-c<span class="w"> </span><span class="m">8</span><span class="w"> </span>-H<span class="w"> </span><span class="m">2</span><span class="w"> </span>-W<span class="w"> </span><span class="m">2</span><span class="w"> </span>-m<span class="w"> </span><span class="m">1</span><span class="w"> </span>--forw<span class="w"> </span><span class="m">1</span><span class="w"> </span>-b<span class="w"> </span><span class="m">0</span><span class="w"> </span>-r<span class="w"> </span><span class="m">1</span><span class="w"> </span>-s<span class="w"> </span><span class="m">1</span><span class="w"> </span>--layout<span class="w"> </span>NHWC
MIOpen<span class="o">(</span>HIP<span class="o">)</span>:<span class="w"> </span>Command<span class="w"> </span><span class="o">[</span>LogCmdBNorm<span class="o">]</span><span class="w"> </span>./bin/MIOpenDriver<span class="w"> </span>bnorm<span class="w"> </span>-n<span class="w"> </span><span class="m">4</span><span class="w"> </span>-c<span class="w"> </span><span class="m">8</span><span class="w"> </span>-H<span class="w"> </span><span class="m">2</span><span class="w"> </span>-W<span class="w"> </span><span class="m">2</span><span class="w"> </span>-m<span class="w"> </span><span class="m">1</span><span class="w"> </span>--forw<span class="w"> </span><span class="m">0</span><span class="w"> </span>-b<span class="w"> </span><span class="m">1</span><span class="w"> </span>-s<span class="w"> </span><span class="m">1</span><span class="w"> </span>--layout<span class="w"> </span>NHWC
MIOpen<span class="o">(</span>HIP<span class="o">)</span>:<span class="w"> </span>Command<span class="w"> </span><span class="o">[</span>LogCmdBNorm<span class="o">]</span><span class="w"> </span>./bin/MIOpenDriver<span class="w"> </span>bnorm<span class="w"> </span>-n<span class="w"> </span><span class="m">4</span><span class="w"> </span>-c<span class="w"> </span><span class="m">8</span><span class="w"> </span>-H<span class="w"> </span><span class="m">2</span><span class="w"> </span>-W<span class="w"> </span><span class="m">2</span><span class="w"> </span>-m<span class="w"> </span><span class="m">1</span><span class="w"> </span>--forw<span class="w"> </span><span class="m">1</span><span class="w"> </span>-b<span class="w"> </span><span class="m">0</span><span class="w"> </span>-r<span class="w"> </span><span class="m">1</span><span class="w"> </span>-s<span class="w"> </span><span class="m">1</span><span class="w"> </span>--layout<span class="w"> </span>NCHW
MIOpen<span class="o">(</span>HIP<span class="o">)</span>:<span class="w"> </span>Command<span class="w"> </span><span class="o">[</span>LogCmdBNorm<span class="o">]</span><span class="w"> </span>./bin/MIOpenDriver<span class="w"> </span>bnorm<span class="w"> </span>-n<span class="w"> </span><span class="m">4</span><span class="w"> </span>-c<span class="w"> </span><span class="m">8</span><span class="w"> </span>-H<span class="w"> </span><span class="m">2</span><span class="w"> </span>-W<span class="w"> </span><span class="m">2</span><span class="w"> </span>-m<span class="w"> </span><span class="m">1</span><span class="w"> </span>--forw<span class="w"> </span><span class="m">0</span><span class="w"> </span>-b<span class="w"> </span><span class="m">1</span><span class="w"> </span>-s<span class="w"> </span><span class="m">1</span><span class="w"> </span>--layout<span class="w"> </span>NCHW
MIOpen<span class="o">(</span>HIP<span class="o">)</span>:<span class="w"> </span>Command<span class="w"> </span><span class="o">[</span>LogCmdBNorm<span class="o">]</span><span class="w"> </span>./bin/MIOpenDriver<span class="w"> </span>bnorm<span class="w"> </span>-n<span class="w"> </span><span class="m">2</span><span class="w"> </span>-c<span class="w"> </span><span class="m">8</span><span class="w"> </span>-H<span class="w"> </span><span class="m">8</span><span class="w"> </span>-W<span class="w"> </span><span class="m">1</span><span class="w"> </span>-m<span class="w"> </span><span class="m">1</span><span class="w"> </span>--forw<span class="w"> </span><span class="m">1</span><span class="w"> </span>-b<span class="w"> </span><span class="m">0</span><span class="w"> </span>-r<span class="w"> </span><span class="m">1</span><span class="w"> </span>-s<span class="w"> </span><span class="m">1</span><span class="w"> </span>--layout<span class="w"> </span>NHWC
MIOpen<span class="o">(</span>HIP<span class="o">)</span>:<span class="w"> </span>Command<span class="w"> </span><span class="o">[</span>LogCmdBNorm<span class="o">]</span><span class="w"> </span>./bin/MIOpenDriver<span class="w"> </span>bnorm<span class="w"> </span>-n<span class="w"> </span><span class="m">2</span><span class="w"> </span>-c<span class="w"> </span><span class="m">8</span><span class="w"> </span>-H<span class="w"> </span><span class="m">8</span><span class="w"> </span>-W<span class="w"> </span><span class="m">1</span><span class="w"> </span>-m<span class="w"> </span><span class="m">1</span><span class="w"> </span>--forw<span class="w"> </span><span class="m">0</span><span class="w"> </span>-b<span class="w"> </span><span class="m">1</span><span class="w"> </span>-s<span class="w"> </span><span class="m">1</span><span class="w"> </span>--layout<span class="w"> </span>NHWC
MIOpen<span class="o">(</span>HIP<span class="o">)</span>:<span class="w"> </span>Command<span class="w"> </span><span class="o">[</span>LogCmdBNorm<span class="o">]</span><span class="w"> </span>./bin/MIOpenDriver<span class="w"> </span>bnorm<span class="w"> </span>-n<span class="w"> </span><span class="m">2</span><span class="w"> </span>-c<span class="w"> </span><span class="m">8</span><span class="w"> </span>-H<span class="w"> </span><span class="m">8</span><span class="w"> </span>-W<span class="w"> </span><span class="m">1</span><span class="w"> </span>-m<span class="w"> </span><span class="m">1</span><span class="w"> </span>--forw<span class="w"> </span><span class="m">1</span><span class="w"> </span>-b<span class="w"> </span><span class="m">0</span><span class="w"> </span>-r<span class="w"> </span><span class="m">1</span><span class="w"> </span>-s<span class="w"> </span><span class="m">1</span><span class="w"> </span>--layout<span class="w"> </span>NCHW
MIOpen<span class="o">(</span>HIP<span class="o">)</span>:<span class="w"> </span>Command<span class="w"> </span><span class="o">[</span>LogCmdBNorm<span class="o">]</span><span class="w"> </span>./bin/MIOpenDriver<span class="w"> </span>bnorm<span class="w"> </span>-n<span class="w"> </span><span class="m">2</span><span class="w"> </span>-c<span class="w"> </span><span class="m">8</span><span class="w"> </span>-H<span class="w"> </span><span class="m">8</span><span class="w"> </span>-W<span class="w"> </span><span class="m">1</span><span class="w"> </span>-m<span class="w"> </span><span class="m">1</span><span class="w"> </span>--forw<span class="w"> </span><span class="m">0</span><span class="w"> </span>-b<span class="w"> </span><span class="m">1</span><span class="w"> </span>-s<span class="w"> </span><span class="m">1</span><span class="w"> </span>--layout<span class="w"> </span>NCHW
</pre></div>
</div>
<p>Each line corresponds to a different command or operation.
The <code class="docutils literal notranslate"><span class="pre">./bin/MIOpenDriver</span></code> string indicates that MIOpen was used for the operation.
The <code class="docutils literal notranslate"><span class="pre">--layout</span></code> parameter shows whether NHWC or NCHW was used, for example, <code class="docutils literal notranslate"><span class="pre">--layout</span> <span class="pre">NHWC</span></code> means the
NHWC memory format was used.</p>
</section>
<section id="running-batch-normalization-tests">
<h2>Running Batch Normalization tests<a class="headerlink" href="#running-batch-normalization-tests" title="Link to this heading">#</a></h2>
<p>Several test suites are available for Batch Normalization. To test Batch Normalization training using both NHWC and NCHW in 2D,
run the following command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>python<span class="w"> </span>test_nn.py<span class="w"> </span>-v<span class="w"> </span>-k<span class="w"> </span>test_batchnorm_2D_train
</pre></div>
</div>
<p>To test Batch Normalization training using both NHWC and NCHW in 3D,
run the following command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>python<span class="w"> </span>test_nn.py<span class="w"> </span>-v<span class="w"> </span>-k<span class="w"> </span>test_batchnorm_3D_train
</pre></div>
</div>
<p>To test Batch Normalization inference for 2D using both memory formats, use this command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>python<span class="w"> </span>test_nn.py<span class="w"> </span>-v<span class="w"> </span>-k<span class="w"> </span>test_batchnorm_2D_inference
</pre></div>
</div>
<p>To test the same functionality for 3D, use this command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>python<span class="w"> </span>test_nn.py<span class="w"> </span>-v<span class="w"> </span>-k<span class="w"> </span>test_batchnorm_3D_inference
</pre></div>
</div>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="find-and-immediate.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Using the find APIs and immediate mode</p>
      </div>
    </a>
    <a class="right-next"
       href="../reference/index.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">API reference library</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#nhwc-versus-nchw">NHWC versus NCHW</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#batch-normalization">Batch Normalization</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#enabling-or-disabling-nhwc-batch-normalization-for-miopen-using-pytorch">Enabling or disabling NHWC Batch Normalization for MIOpen using PyTorch</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#pytorch-branch-support">PyTorch branch support</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-configurations">Supported configurations</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#disabling-miopen-for-batch-normalization-in-pytorch">Disabling MIOpen for Batch Normalization in PyTorch</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#verifying-nhwc-batch-normalization-use-with-miopen">Verifying NHWC Batch Normalization use with MIOpen</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#running-batch-normalization-tests">Running Batch Normalization tests</a></li>
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
