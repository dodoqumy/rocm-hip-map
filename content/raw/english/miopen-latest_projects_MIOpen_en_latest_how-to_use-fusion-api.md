---
title: "Using the fusion API &#8212; MIOpen 3.5.1 Documentation"
source_url: "https://rocm.docs.amd.com/projects/MIOpen/en/latest/how-to/use-fusion-api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:09:38.881170+00:00
content_hash: "6692db5076344140"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Using the Fusion API" name="description" />
<meta content="MIOpen, ROCm, API, documentation, fusion API" name="keywords" />

    <title>Using the fusion API &#8212; MIOpen 3.5.1 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/use-fusion-api';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Logging and debugging" href="debug-log.html" />
    <link rel="prev" title="Porting to MIOpen" href="../conceptual/porting-guide.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-miopen" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/use-fusion-api.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Use the fusion API</a></li>
<li class="toctree-l1"><a class="reference internal" href="debug-log.html">Log and debug</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Using the fusion API</span></li>
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
    <h1>Using the fusion API</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#creating-a-fusion-plan">Creating a fusion plan</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#creating-and-adding-operators">Creating and adding operators</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#compiling-the-fusion-plan">Compiling the fusion plan</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#setting-runtime-arguments">Setting runtime arguments</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#running-a-fusion-plan">Running a fusion plan</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cleanup">Cleanup</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-fusions">Supported fusions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#convolution-based-fp32-fusion-for-inference">Convolution-based FP32 fusion for inference</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#convolution-based-fp16-fusion-for-inference">Convolution-based FP16 fusion for inference</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#convolution-based-bfp16-fusion-for-inference">Convolution-based BFP16 fusion for inference</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#batch-normalization-based-fusion-for-fp32-bfp16-and-fp16-for-inference-and-training">Batch Normalization-based fusion for FP32, BFP16, and FP16 for inference and training</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#comparing-performance-with-non-fused-kernels">Comparing performance with non-fused kernels</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="using-the-fusion-api">
<h1>Using the fusion API<a class="headerlink" href="#using-the-fusion-api" title="Link to this heading">#</a></h1>
<p>Increasing the depth of deep-learning networks requires novel mechanisms to improve GPU
performance. One mechanism to achieve higher efficiency is to <em>fuse</em> separate kernels into a single
kernel in order to reduce off-chip memory access and avoid kernel launch overhead.</p>
<p>Using MIOpen’s fusion API, you can specify operators that you want to fuse into a single kernel,
compile that kernel, and then launch it. While not all combinations are supported, the API is flexible
enough to allow the specification of several operations, in any order, from the set of supported
operations. The API provides a mechanism to report unsupported combinations.</p>
<p>You can find a complete example of MIOpen’s fusion API in the MIOpen GitHub repository
<a class="reference external" href="https://github.com/ROCm/MIOpenExamples/tree/master/fusion">example folder</a>. The code
examples in this document are taken from this example project.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The example project creates a fusion plan to merge the convolution, bias, and activation operations.
For a list of supported fusion operations and associated constraints, see the
<a class="reference internal" href="#supported-fusions"><span class="std std-ref">Supported fusions</span></a> section. For simplicity, the example doesn’t populate
the tensors with meaningful data and only shows the basic code without any error checking.</p>
</div>
<p>After you’ve initialized an MIOpen handle object, the workflow for using the fusion API is:</p>
<ul class="simple">
<li><p>Create a fusion plan</p></li>
<li><p>Create and add the convolution, bias, and activation operators</p></li>
<li><p>Compile the fusion plan</p></li>
<li><p>Set the runtime arguments for each operator</p></li>
<li><p>Run the fusion plan</p></li>
<li><p>Cleanup</p></li>
</ul>
<p>The order in which you create operators is important because this order represents the order of
operations for the data. Therefore, a fusion plan where convolution is created before activation differs
from a fusion plan where activation is added before convolution.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The primary consumers of the fusion API are high-level frameworks, such as TensorFlow/XLA and
PyTorch.</p>
</div>
<section id="creating-a-fusion-plan">
<h2>Creating a fusion plan<a class="headerlink" href="#creating-a-fusion-plan" title="Link to this heading">#</a></h2>
<p>A <em>fusion plan</em> is the data structure that holds all the metadata regarding fusion intent along with the
logic to compile and run a fusion plan. The fusion plan not only contains the order in which different
operations are applied on the data, but also specifies the <em>axis</em> of fusion. Currently, only <em>vertical</em>
(sequential) fusions are supported, implying the flow of data between operations is sequential.</p>
<p>You can create a fusion plan using <code class="docutils literal notranslate"><span class="pre">miopenCreateFusionPlan</span></code>, as follows:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="nf">miopenCreateFusionPlan</span><span class="p">(</span><span class="n">miopenFusionPlanDescriptor_t</span><span class="o">*</span><span class="w"> </span><span class="n">fusePlanDesc</span><span class="p">,</span>
<span class="k">const</span><span class="w"> </span><span class="n">miopenFusionDirection_t</span><span class="w"> </span><span class="n">fuseDirection</span><span class="p">,</span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">inputDesc</span><span class="p">);</span>
</pre></div>
</div>
<p>The <em>input tensor descriptor</em> specifies the geometry of the incoming data. Because the data geometry
of the intermediate operations can be derived from the input tensor descriptor, this is only required for
the fusion plan. The input tensor descriptor isn’t required for the individual operations.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenCreateFusionPlan</span><span class="p">(</span><span class="o">&amp;</span><span class="n">fusePlanDesc</span><span class="p">,</span><span class="w"> </span><span class="n">miopenVerticalFusion</span><span class="p">,</span><span class="w"> </span><span class="n">input</span><span class="p">.</span><span class="n">desc</span><span class="p">);</span>
</pre></div>
</div>
<p>In the previous example, <code class="docutils literal notranslate"><span class="pre">fusePlanDesc</span></code> is an object of type <code class="docutils literal notranslate"><span class="pre">miopenFusionPlanDescriptor_t</span></code> and <code class="docutils literal notranslate"><span class="pre">input.desc</span></code> is
the <code class="docutils literal notranslate"><span class="pre">miopenTensorDescriptor_t</span></code> object.</p>
</section>
<section id="creating-and-adding-operators">
<h2>Creating and adding operators<a class="headerlink" href="#creating-and-adding-operators" title="Link to this heading">#</a></h2>
<p>Operators represent the different operations to fuse. Currently, the API supports these
operators:</p>
<ul class="simple">
<li><p>Convolution forward</p></li>
<li><p>Activation forward</p></li>
<li><p>BatchNorm inference</p></li>
<li><p>Bias forward</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Although bias is a separate operator, it’s typically only used with convolution.</p>
</div>
<p>MIOpen plans to add support for more operators, including operators for backward passes, in the future.</p>
<p>The fusion API provides calls for the creation of the supported operators. To learn more, refer to the
<a class="reference internal" href="../doxygen/html/group___f_u_s_i_o_n.html"><span class="doc">Fusion</span></a> API documentation.</p>
<p>After you’ve created the fusion plan descriptor, you can add two or more operators to it by using the
individual operator creation API calls. If the API doesn’t support the fusion of the operations you add,
the creation might fail.</p>
<p>This example adds the convolution, bias, and activation operations to the newly created fusion
plan.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="nf">miopenCreateOpConvForward</span><span class="p">(</span><span class="n">miopenFusionPlanDescriptor_t</span><span class="w"> </span><span class="n">fusePlanDesc</span><span class="p">,</span>
<span class="w">                          </span><span class="n">miopenFusionOpDescriptor_t</span><span class="o">*</span><span class="w"> </span><span class="n">convOp</span><span class="p">,</span>
<span class="w">                          </span><span class="n">miopenConvolutionDescriptor_t</span><span class="w"> </span><span class="n">convDesc</span><span class="p">,</span>
<span class="w">                          </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">wDesc</span><span class="p">);</span>
<span class="n">miopenStatus_t</span>
<span class="nf">miopenCreateOpBiasForward</span><span class="p">(</span><span class="n">miopenFusionPlanDescriptor_t</span><span class="w"> </span><span class="n">fusePlanDesc</span><span class="p">,</span>
<span class="w">                          </span><span class="n">miopenFusionOpDescriptor_t</span><span class="o">*</span><span class="w"> </span><span class="n">biasOp</span><span class="p">,</span>
<span class="w">                          </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">bDesc</span><span class="p">);</span>

<span class="n">miopenStatus_t</span>
<span class="nf">miopenCreateOpActivationForward</span><span class="p">(</span><span class="n">miopenFusionPlanDescriptor_t</span><span class="w"> </span><span class="n">fusePlanDesc</span><span class="p">,</span>
<span class="w">                                </span><span class="n">miopenFusionOpDescriptor_t</span><span class="o">*</span><span class="w"> </span><span class="n">activOp</span><span class="p">,</span>
<span class="w">                                </span><span class="n">miopenActivationMode_t</span><span class="w"> </span><span class="n">mode</span><span class="p">);</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">conv_desc</span></code> is the regular MIOpen convolution descriptor. For more information on creating and
setting this descriptor, see the example code and the
<a class="reference internal" href="../doxygen/html/group__convolutions.html"><span class="doc">Convolution</span></a> API documentation.</p>
<p><code class="docutils literal notranslate"><span class="pre">weights.desc</span></code> refers to <code class="docutils literal notranslate"><span class="pre">miopenTensorDescriptor_t</span></code> for the convolution operations.
<code class="docutils literal notranslate"><span class="pre">bias.desc</span></code> refers to the object of the same type for the bias operation.</p>
<p>In the preceding code, the convolution operation is the first operation to run on the incoming data,
followed by the bias, and then activation operations.</p>
<p>During this process, it is important to verify the return codes to ensure the operations and
sequence are supported. The operator insertion can fail for a number of reasons, such as an unsupported
operation sequence, unsupported input dimensions, or, in the case of convolution, unsupported filter
dimensions. In the preceding example, these aspects are ignored for the sake of simplicity.</p>
</section>
<section id="compiling-the-fusion-plan">
<h2>Compiling the fusion plan<a class="headerlink" href="#compiling-the-fusion-plan" title="Link to this heading">#</a></h2>
<p>Following the addition of the operators, you can compile the fusion plan. This populates the MIOpen kernel
cache with the fused kernel and gets it ready to run.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="nf">miopenCompileFusionPlan</span><span class="p">(</span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="n">miopenFusionPlanDescriptor_t</span><span class="w"> </span><span class="n">fusePlanDesc</span><span class="p">);</span>
</pre></div>
</div>
<p>The corresponding code snippet in the example is:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">auto</span><span class="w"> </span><span class="n">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">miopenCompileFusionPlan</span><span class="p">(</span><span class="n">mio</span><span class="o">::</span><span class="n">handle</span><span class="p">(),</span><span class="w"> </span><span class="n">fusePlanDesc</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">status</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">miopenStatusSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="k">return</span><span class="w"> </span><span class="mi">-1</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>To compile the fusion plan, you must acquire an MIOpen handle object. In the
preceding code, this is accomplished using the <code class="docutils literal notranslate"><span class="pre">mio::handle()</span></code> helper function. While a fusion plan is
itself not bound to an MIOpen handle object, it must be recompiled separately for each handle.</p>
<p>Compiling a fusion plan is a costly operation in terms of run-time, and compilation can fail for a
number of reasons. Therefore, the recommendation is to only compile your fusion plan once and reuse it
with different runtime parameters, as described in the next section.</p>
</section>
<section id="setting-runtime-arguments">
<h2>Setting runtime arguments<a class="headerlink" href="#setting-runtime-arguments" title="Link to this heading">#</a></h2>
<p>While the fusion operator for the underlying MIOpen descriptor specifies the data geometry and
parameters, the fusion plan still needs access to the data to run a successfully compiled fusion plan.
The arguments mechanism in the fusion API provides this data before a fusion plan can be run. For
example, the convolution operator requires <em>weights</em> to carry out the convolution computation, and the
bias operator requires the actual bias values. Therefore, before you can run a fusion plan, you must
specify the arguments required by each fusion operator.</p>
<p>First create the <code class="docutils literal notranslate"><span class="pre">miopenOperatorArgs_t</span></code> object using this code:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span><span class="w"> </span><span class="nf">miopenCreateOperatorArgs</span><span class="p">(</span><span class="n">miopenOperatorArgs_t</span><span class="o">*</span><span class="w"> </span><span class="n">args</span><span class="p">);</span>
</pre></div>
</div>
<p>After it is created, you can set the runtime arguments for each operation. In this example, the forward
convolution operator requires the convolution weights argument, which is supplied using:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="nf">miopenSetOpArgsConvForward</span><span class="p">(</span><span class="n">miopenOperatorArgs_t</span><span class="w"> </span><span class="n">args</span><span class="p">,</span>
<span class="w">                          </span><span class="k">const</span><span class="w"> </span><span class="n">miopenFusionOpDescriptor_t</span><span class="w"> </span><span class="n">convOp</span><span class="p">,</span>
<span class="w">                          </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">alpha</span><span class="p">,</span>
<span class="w">                          </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">beta</span><span class="p">,</span>
<span class="w">                          </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">w</span><span class="p">);</span>
</pre></div>
</div>
<p>Similarly, the parameters for bias and activation are supplied by:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span><span class="w"> </span><span class="nf">miopenSetOpArgsBiasForward</span><span class="p">(</span><span class="n">miopenOperatorArgs_t</span><span class="w"> </span><span class="n">args</span><span class="p">,</span>
<span class="w">                                          </span><span class="k">const</span><span class="w"> </span><span class="n">miopenFusionOpDescriptor_t</span><span class="w"> </span><span class="n">biasOp</span><span class="p">,</span>
<span class="w">                                          </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">alpha</span><span class="p">,</span>
<span class="w">                                          </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">beta</span><span class="p">,</span>
<span class="w">                                          </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">bias</span><span class="p">);</span>

<span class="n">miopenStatus_t</span><span class="w"> </span><span class="nf">miopenSetOpArgsActivForward</span><span class="p">(</span><span class="n">miopenOperatorArgs_t</span><span class="w"> </span><span class="n">args</span><span class="p">,</span>
<span class="w">                                          </span><span class="k">const</span><span class="w"> </span><span class="n">miopenFusionOpDescriptor_t</span><span class="w"> </span><span class="n">activOp</span><span class="p">,</span>
<span class="w">                                          </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">alpha</span><span class="p">,</span>
<span class="w">                                          </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">beta</span><span class="p">,</span>
<span class="w">                                          </span><span class="kt">double</span><span class="w"> </span><span class="n">activAlpha</span><span class="p">,</span>
<span class="w">                                          </span><span class="kt">double</span><span class="w"> </span><span class="n">activBeta</span><span class="p">,</span>
<span class="w">                                          </span><span class="kt">double</span><span class="w"> </span><span class="n">activGamma</span><span class="p">);</span>
</pre></div>
</div>
<p>In the example code, the arguments for the operations are set as follows:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenSetOpArgsConvForward</span><span class="p">(</span><span class="n">fusionArgs</span><span class="p">,</span><span class="w"> </span><span class="n">convoOp</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">alpha</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">beta</span><span class="p">,</span><span class="w"> </span><span class="n">weights</span><span class="p">.</span><span class="n">data</span><span class="p">);</span>
<span class="n">miopenSetOpArgsActivForward</span><span class="p">(</span><span class="n">fusionArgs</span><span class="p">,</span><span class="w"> </span><span class="n">activOp</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">alpha</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">beta</span><span class="p">,</span><span class="w"> </span><span class="n">activ_alpha</span><span class="p">,</span>
<span class="w">                          </span><span class="n">activ_beta</span><span class="p">,</span><span class="w"> </span><span class="n">activ_gamma</span><span class="p">);</span>
<span class="n">miopenSetOpArgsBiasForward</span><span class="p">(</span><span class="n">fusionArgs</span><span class="p">,</span><span class="w"> </span><span class="n">biasOp</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">alpha</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">beta</span><span class="p">,</span><span class="w"> </span><span class="n">bias</span><span class="p">.</span><span class="n">data</span><span class="p">);</span>
</pre></div>
</div>
<p>Having a separation between the fusion plan and the arguments required by each operator allows better
reuse of the fusion plan with different arguments. It also avoids the necessity to recompile the fusion
plan to run the same combination of operators with different arguments.</p>
<p>As previously mentioned, the compilation step for a fusion plan can be costly. Therefore, it is
recommended that you only compile a fusion plan once in its lifetime. A fusion plan doesn’t need to be
recompiled if the input descriptor or any of the parameters in the <code class="docutils literal notranslate"><span class="pre">miopenCreateOp*</span></code> API calls are
different. You can repeatedly reuse a compiled fusion plan with a different set of arguments.</p>
<p>In the example, this is demonstrated in <code class="docutils literal notranslate"><span class="pre">main.cpp</span></code>, lines 77 through 85.</p>
</section>
<section id="running-a-fusion-plan">
<h2>Running a fusion plan<a class="headerlink" href="#running-a-fusion-plan" title="Link to this heading">#</a></h2>
<p>Once you’ve compiled the fusion plan and set the arguments for each operator, you can run it as
follows:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span>
<span class="nf">miopenExecuteFusionPlan</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">miopenHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span>
<span class="w">                        </span><span class="k">const</span><span class="w"> </span><span class="n">miopenFusionPlanDescriptor_t</span><span class="w"> </span><span class="n">fusePlanDesc</span><span class="p">,</span>
<span class="w">                        </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">inputDesc</span><span class="p">,</span>
<span class="w">                        </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">input</span><span class="p">,</span>
<span class="w">                        </span><span class="k">const</span><span class="w"> </span><span class="n">miopenTensorDescriptor_t</span><span class="w"> </span><span class="n">outputDesc</span><span class="p">,</span>
<span class="w">                        </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">output</span><span class="p">,</span>
<span class="w">                        </span><span class="n">miopenOperatorArgs_t</span><span class="w"> </span><span class="n">args</span><span class="p">);</span>
</pre></div>
</div>
<p>The following code snippet runs the fusion plan:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenExecuteFusionPlan</span><span class="p">(</span><span class="n">mio</span><span class="o">::</span><span class="n">handle</span><span class="p">(),</span><span class="w"> </span><span class="n">fusePlanDesc</span><span class="p">,</span><span class="w"> </span><span class="n">input</span><span class="p">.</span><span class="n">desc</span><span class="p">,</span><span class="w"> </span><span class="n">input</span><span class="p">.</span><span class="n">data</span><span class="p">,</span>
<span class="w">                        </span><span class="n">output</span><span class="p">.</span><span class="n">desc</span><span class="p">,</span><span class="w"> </span><span class="n">output</span><span class="p">.</span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="n">fusionArgs</span><span class="p">);</span>
</pre></div>
</div>
<p>If you try to run a fusion plan that is not compiled, or has been invalidated by changing the input
tensor descriptor or any of the operation parameters, you’ll get an error.</p>
</section>
<section id="cleanup">
<h2>Cleanup<a class="headerlink" href="#cleanup" title="Link to this heading">#</a></h2>
<p>After the application is finished with the fusion plan, you can destroy the fusion plan and the fusion <code class="docutils literal notranslate"><span class="pre">args</span></code>
objects:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">miopenStatus_t</span><span class="w"> </span><span class="nf">miopenDestroyFusionPlan</span><span class="p">(</span><span class="n">miopenFusionPlanDescriptor_t</span><span class="w"> </span><span class="n">fusePlanDesc</span><span class="p">);</span>
</pre></div>
</div>
<p>After the fusion plan object is destroyed, all the operations are automatically destroyed. You don’t
need to worry about additional cleanup.</p>
</section>
<section id="supported-fusions">
<span id="id1"></span><h2>Supported fusions<a class="headerlink" href="#supported-fusions" title="Link to this heading">#</a></h2>
<p>The following tables outline the supported fusions for <code class="docutils literal notranslate"><span class="pre">FP32</span></code>, <code class="docutils literal notranslate"><span class="pre">FP16</span></code>, and <code class="docutils literal notranslate"><span class="pre">BFP16</span></code>, including any applicable
constraints.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Fusion Plans with grouped convolutions are supported in the inference direction for
convolution, bias, and activation.</p>
</div>
<p>The following abbreviations apply to the combination column in the following tables:</p>
<ul class="simple">
<li><p><strong>C</strong>: Convolution</p></li>
<li><p><strong>B</strong>: Bias</p></li>
<li><p><strong>N</strong>: Batch Normalization</p></li>
<li><p><strong>A</strong>: Activation</p></li>
</ul>
<p>For example, CBA refers to convolution plus bias plus activation.</p>
<section id="convolution-based-fp32-fusion-for-inference">
<h3>Convolution-based FP32 fusion for inference<a class="headerlink" href="#convolution-based-fp32-fusion-for-inference" title="Link to this heading">#</a></h3>
<p>The following table applies to single-precision floating point.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 12.8%" />
<col style="width: 12.8%" />
<col style="width: 12.8%" />
<col style="width: 17.1%" />
<col style="width: 10.3%" />
<col style="width: 17.1%" />
<col style="width: 17.1%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Combination</p></th>
<th class="head"><p>Conv algo</p></th>
<th class="head"><p>Stride</p></th>
<th class="head"><p>Filter dims</p></th>
<th class="head"><p>N mode</p></th>
<th class="head"><p>Activations</p></th>
<th class="head"><p>Other constraints</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>CBNA</p></td>
<td><p>Direct</p></td>
<td><p>1 and 2</p></td>
<td><p>3x3, 5x5, 7x7, 9x9, 11x11</p></td>
<td><p>All</p></td>
<td><p>All</p></td>
<td><p>stride and padding must be either 1 or 2</p></td>
</tr>
<tr class="row-odd"><td><p>CBA</p></td>
<td><p>Direct</p></td>
<td><p>–</p></td>
<td><p>1x1</p></td>
<td><p>–</p></td>
<td><p>All</p></td>
<td><p>stride and padding not supported</p></td>
</tr>
<tr class="row-even"><td><p>CBA</p></td>
<td><p>Winograd</p></td>
<td><p>1</p></td>
<td><p>1x1, 2x2</p></td>
<td><p>N/A</p></td>
<td><p>Relu, Leaky Relu</p></td>
<td><p>c &gt;= 18</p></td>
</tr>
<tr class="row-odd"><td><p>CBA</p></td>
<td><p>Winograd</p></td>
<td><p>1</p></td>
<td><p>3x3</p></td>
<td><p>–</p></td>
<td><p>Relu, Leaky Relu</p></td>
<td><p>c &gt;= 18 and c is even</p></td>
</tr>
<tr class="row-even"><td><p>CBA</p></td>
<td><p>Winograd</p></td>
<td><p>1</p></td>
<td><p>4x4, 5x5, 6x6</p></td>
<td><p>–</p></td>
<td><p>Relu, Leaky Relu</p></td>
<td><p>4 x c &gt;= 18</p></td>
</tr>
<tr class="row-odd"><td><p>CBA</p></td>
<td><p>Winograd</p></td>
<td><p>1</p></td>
<td><p>7x7, 8x8, 9x9</p></td>
<td><p>–</p></td>
<td><p>Relu, Leaky Relu</p></td>
<td><p>12 x c &gt;= 18</p></td>
</tr>
<tr class="row-even"><td><p>CBA</p></td>
<td><p>Winograd</p></td>
<td><p>1</p></td>
<td><p>10x10, 11x11, 12x12</p></td>
<td><p>–</p></td>
<td><p>Relu, Leaky Relu</p></td>
<td><p>16 x c &gt;= 18</p></td>
</tr>
<tr class="row-odd"><td><p>CBA</p></td>
<td><p>Winograd</p></td>
<td><p>1</p></td>
<td><p>larger filter sizes</p></td>
<td><p>–</p></td>
<td><p>Relu, Leaky Relu</p></td>
<td><p>none</p></td>
</tr>
<tr class="row-even"><td><p>CBA</p></td>
<td><p>Winograd</p></td>
<td><p>2</p></td>
<td><p>1x1</p></td>
<td><p>–</p></td>
<td><p>Relu, Leaky Relu</p></td>
<td><p>2 x c &gt;= 18</p></td>
</tr>
<tr class="row-odd"><td><p>CBA</p></td>
<td><p>Winograd</p></td>
<td><p>2</p></td>
<td><p>2x2, 3x3, 4x4, 5x5, 6x6</p></td>
<td><p>–</p></td>
<td><p>Relu, Leaky Relu</p></td>
<td><p>4 x c &gt;= 18</p></td>
</tr>
<tr class="row-even"><td><p>CBA</p></td>
<td><p>Winograd</p></td>
<td><p>2</p></td>
<td><p>7x7</p></td>
<td><p>–</p></td>
<td><p>Relu, Leaky Relu</p></td>
<td><p>12 x c &gt;= 18</p></td>
</tr>
<tr class="row-odd"><td><p>CBA</p></td>
<td><p>Winograd</p></td>
<td><p>2</p></td>
<td><p>8x8, 9x9, 10x10, 11x11, 12x12</p></td>
<td><p>–</p></td>
<td><p>Relu, Leaky Relu</p></td>
<td><p>16 x c &gt;= 18</p></td>
</tr>
<tr class="row-even"><td><p>CBA</p></td>
<td><p>Winograd</p></td>
<td><p>2</p></td>
<td><p>larger filter sizes</p></td>
<td><p>–</p></td>
<td><p>Relu, Leaky Relu</p></td>
<td><p>none</p></td>
</tr>
<tr class="row-odd"><td><p>CBA</p></td>
<td><p>CK</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>Relu, Clipped Relu, CLAMP</p></td>
<td><p>none</p></td>
</tr>
<tr class="row-even"><td><p>NA</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>All</p></td>
<td><p>All</p></td>
<td><p>padding not supported</p></td>
</tr>
<tr class="row-odd"><td><p>CA</p></td>
<td><p>Direct</p></td>
<td><p>–</p></td>
<td><p>1x1</p></td>
<td><p>–</p></td>
<td><p>All</p></td>
<td><p>stride and padding not supported</p></td>
</tr>
<tr class="row-even"><td><p>CA</p></td>
<td><p>CK</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>Relu, Clipped Relu, CLAMP</p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>N mode is either spatial or per activation. For CBA, other asymmetric kernels are supported but for brevity are not enumerated here.</p>
</div>
</section>
<section id="convolution-based-fp16-fusion-for-inference">
<h3>Convolution-based FP16 fusion for inference<a class="headerlink" href="#convolution-based-fp16-fusion-for-inference" title="Link to this heading">#</a></h3>
<p>The following table applies to half-precision floating point.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 12.8%" />
<col style="width: 12.8%" />
<col style="width: 12.8%" />
<col style="width: 17.1%" />
<col style="width: 10.3%" />
<col style="width: 17.1%" />
<col style="width: 17.1%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Combination</p></th>
<th class="head"><p>Conv algo</p></th>
<th class="head"><p>Stride</p></th>
<th class="head"><p>Filter dims</p></th>
<th class="head"><p>N mode</p></th>
<th class="head"><p>Activations</p></th>
<th class="head"><p>Other constraints</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>CBNA</p></td>
<td><p>Direct</p></td>
<td><p>1 and 2</p></td>
<td><p>3x3, 5x5, 7x7, 9x9, 11x11</p></td>
<td><p>All</p></td>
<td><p>All</p></td>
<td><p>stride and padding must be either 1 or 2</p></td>
</tr>
<tr class="row-odd"><td><p>CBA</p></td>
<td><p>Direct</p></td>
<td><p>–</p></td>
<td><p>1x1</p></td>
<td><p>–</p></td>
<td><p>All</p></td>
<td><p>stride and padding not supported</p></td>
</tr>
<tr class="row-even"><td><p>CBA</p></td>
<td><p>CK</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>Relu, Clipped Relu, CLAMP</p></td>
<td><p>none</p></td>
</tr>
<tr class="row-odd"><td><p>CA</p></td>
<td><p>Direct</p></td>
<td><p>–</p></td>
<td><p>1x1</p></td>
<td><p>–</p></td>
<td><p>All</p></td>
<td><p>stride and padding not supported</p></td>
</tr>
<tr class="row-even"><td><p>CA</p></td>
<td><p>CK</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>Relu, Clipped Relu, CLAMP</p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>N mode is either spatial or per activation.</p>
</div>
</section>
<section id="convolution-based-bfp16-fusion-for-inference">
<h3>Convolution-based BFP16 fusion for inference<a class="headerlink" href="#convolution-based-bfp16-fusion-for-inference" title="Link to this heading">#</a></h3>
<p>The following table applies to half-precision block floating point.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 12.8%" />
<col style="width: 12.8%" />
<col style="width: 12.8%" />
<col style="width: 17.1%" />
<col style="width: 10.3%" />
<col style="width: 17.1%" />
<col style="width: 17.1%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Combination</p></th>
<th class="head"><p>Conv algo</p></th>
<th class="head"><p>Stride</p></th>
<th class="head"><p>Filter dims</p></th>
<th class="head"><p>N mode</p></th>
<th class="head"><p>Activations</p></th>
<th class="head"><p>Other constraints</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>CBNA</p></td>
<td><p>Direct</p></td>
<td><p>1 and 2</p></td>
<td><p>3x3, 5x5, 7x7, 9x9, 11x11</p></td>
<td><p>All</p></td>
<td><p>All</p></td>
<td><p>stride and padding must be either 1 or 2</p></td>
</tr>
<tr class="row-odd"><td><p>CBA</p></td>
<td><p>Direct</p></td>
<td><p>–</p></td>
<td><p>1x1</p></td>
<td><p>–</p></td>
<td><p>All</p></td>
<td><p>stride and padding not supported</p></td>
</tr>
<tr class="row-even"><td><p>CBA</p></td>
<td><p>CK</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>Relu, Clipped Relu, CLAMP</p></td>
<td><p>none</p></td>
</tr>
<tr class="row-odd"><td><p>CA</p></td>
<td><p>Direct</p></td>
<td><p>–</p></td>
<td><p>1x1</p></td>
<td><p>–</p></td>
<td><p>All</p></td>
<td><p>stride and padding not supported</p></td>
</tr>
<tr class="row-even"><td><p>CA</p></td>
<td><p>CK</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>–</p></td>
<td><p>Relu, Clipped Relu, CLAMP</p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>N mode is either spatial or per activation.</p>
</div>
</section>
<section id="batch-normalization-based-fusion-for-fp32-bfp16-and-fp16-for-inference-and-training">
<h3>Batch Normalization-based fusion for FP32, BFP16, and FP16 for inference and training<a class="headerlink" href="#batch-normalization-based-fusion-for-fp32-bfp16-and-fp16-for-inference-and-training" title="Link to this heading">#</a></h3>
<p>The following table applies to both full-precision and half-precision floating point.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 40.0%" />
<col style="width: 20.0%" />
<col style="width: 20.0%" />
<col style="width: 20.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Combination</p></th>
<th class="head"><p>N mode</p></th>
<th class="head"><p>Activations</p></th>
<th class="head"><p>Constraints</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>NA for inference</p></td>
<td><p>All</p></td>
<td><p>All</p></td>
<td><p>None</p></td>
</tr>
<tr class="row-odd"><td><p>NA forward training</p></td>
<td><p>All</p></td>
<td><p>All</p></td>
<td><p>None</p></td>
</tr>
<tr class="row-even"><td><p>NA backward training</p></td>
<td><p>All</p></td>
<td><p>All</p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>N mode is either spatial or per activation.</p>
</div>
</section>
</section>
<section id="comparing-performance-with-non-fused-kernels">
<h2>Comparing performance with non-fused kernels<a class="headerlink" href="#comparing-performance-with-non-fused-kernels" title="Link to this heading">#</a></h2>
<p>The following graph depicts the speedup gained for a fused convolution+bias+activation over a
non-fused version. All configurations have a batch size of 64:</p>
<a class="reference internal image-reference" href="../_images/cba.png"><img alt="convolution-bias-activation graph" src="../_images/cba.png" style="width: 800px;" />
</a>
<p>The following graph depicts the speedup obtained by fusing BatchNorm (in spatial mode) with activation:</p>
<a class="reference internal image-reference" href="../_images/bn_activ_fused.png"><img alt="BatchNorm activation fusion" src="../_images/bn_activ_fused.png" style="width: 800px;" />
</a>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../conceptual/porting-guide.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Porting to MIOpen</p>
      </div>
    </a>
    <a class="right-next"
       href="debug-log.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Logging and debugging</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#creating-a-fusion-plan">Creating a fusion plan</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#creating-and-adding-operators">Creating and adding operators</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#compiling-the-fusion-plan">Compiling the fusion plan</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#setting-runtime-arguments">Setting runtime arguments</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#running-a-fusion-plan">Running a fusion plan</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cleanup">Cleanup</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-fusions">Supported fusions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#convolution-based-fp32-fusion-for-inference">Convolution-based FP32 fusion for inference</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#convolution-based-fp16-fusion-for-inference">Convolution-based FP16 fusion for inference</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#convolution-based-bfp16-fusion-for-inference">Convolution-based BFP16 fusion for inference</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#batch-normalization-based-fusion-for-fp32-bfp16-and-fp16-for-inference-and-training">Batch Normalization-based fusion for FP32, BFP16, and FP16 for inference and training</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#comparing-performance-with-non-fused-kernels">Comparing performance with non-fused kernels</a></li>
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
