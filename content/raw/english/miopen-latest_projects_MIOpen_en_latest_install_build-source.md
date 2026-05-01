---
title: "Build MIOpen from source &#8212; MIOpen 3.5.1 Documentation"
source_url: "https://rocm.docs.amd.com/projects/MIOpen/en/latest/install/build-source.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:41.054146+00:00
content_hash: "66aee561430788f4"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Building MIOpen from source" name="description" />
<meta content="MIOpen, ROCm, API, documentation, build, installation, testing" name="keywords" />

    <title>Build MIOpen from source &#8212; MIOpen 3.5.1 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'install/build-source';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Build MIOpen for embedded systems" href="embed.html" />
    <link rel="prev" title="Install MIOpen" href="install.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-miopen" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/install/build-source.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="prerequisites.html">MIOpen prerequisites</a></li>
<li class="toctree-l1"><a class="reference internal" href="install.html">Install MIOpen</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Build MIOpen from source</a></li>
<li class="toctree-l1"><a class="reference internal" href="embed.html">Build MIOpen for embedded systems</a></li>
<li class="toctree-l1"><a class="reference internal" href="docker-build.html">Build MIOpen using Docker</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Build MIOpen from source</span></li>
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
    <h1>Build MIOpen from source</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#building-miopen">Building MIOpen</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-backend">HIP backend</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#opencl-backend">OpenCL backend</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#setting-the-install-location">Setting the install location</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#system-performance-database-and-user-database">System performance database and user database</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#persistent-program-cache">Persistent program cache</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#for-miopen-version-2-3-and-earlier">For MIOpen version 2.3 and earlier</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#for-miopen-version-2-4-and-later">For MIOpen version 2.4 and later</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#changing-the-cmake-configuration">Changing the CMake configuration</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#building-the-library">Building the library</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#building-the-driver">Building the driver</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#running-the-tests">Running the tests</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#formatting-the-code">Formatting the code</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#storing-large-file-using-git-large-file-storage">Storing large file using Git Large File Storage</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#installing-the-dependencies-manually">Installing the dependencies manually</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="build-miopen-from-source">
<h1>Build MIOpen from source<a class="headerlink" href="#build-miopen-from-source" title="Link to this heading">#</a></h1>
<p>This topic discusses how to build MIOpen from source and configure the resulting application.
It also explains how to build the library and driver and run the tests. For a list of MIOpen
prerequisites, see <a class="reference internal" href="prerequisites.html"><span class="doc">MIOpen prerequisites</span></a>. To install MIOpen from a
package, see <a class="reference internal" href="install.html"><span class="doc">install MIOpen</span></a>.</p>
<section id="building-miopen">
<h2>Building MIOpen<a class="headerlink" href="#building-miopen" title="Link to this heading">#</a></h2>
<p>You can build MIOpen form source using either a HIP backend or an OpenCL backend.</p>
<section id="hip-backend">
<h3>HIP backend<a class="headerlink" href="#hip-backend" title="Link to this heading">#</a></h3>
<p>To build MIOpen using the HIP backend (in ROCm 3.5 and later), follow these steps:</p>
<ol class="arabic">
<li><p>Create the build directory:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>mkdir<span class="w"> </span>build<span class="p">;</span><span class="w"> </span><span class="nb">cd</span><span class="w"> </span>build<span class="p">;</span>
</pre></div>
</div>
</li>
<li><p>Configure CMake. Set the backend using the <code class="docutils literal notranslate"><span class="pre">-DMIOPEN_BACKEND</span></code> CMake variable and
set the C++ compiler to <code class="docutils literal notranslate"><span class="pre">clang++</span></code>. The command to build MIOpen with a HIP backend follows this format:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nb">export</span><span class="w"> </span><span class="nv">CXX</span><span class="o">=</span>&lt;location-of-clang++-compiler&gt;
cmake<span class="w"> </span>-DMIOPEN_BACKEND<span class="o">=</span>HIP<span class="w"> </span>-DCMAKE_PREFIX_PATH<span class="o">=</span><span class="s2">&quot;&lt;hip-installed-path&gt;;&lt;rocm-installed-path&gt;;&lt;miopen-dependency-path&gt;&quot;</span><span class="w"> </span>..
</pre></div>
</div>
<p>An example of a CMake build is:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nb">export</span><span class="w"> </span><span class="nv">CXX</span><span class="o">=</span>/opt/rocm/llvm/bin/clang++<span class="w"> </span><span class="o">&amp;&amp;</span><span class="w"> </span><span class="se">\</span>
cmake<span class="w"> </span>-DMIOPEN_BACKEND<span class="o">=</span>HIP<span class="w"> </span>-DCMAKE_PREFIX_PATH<span class="o">=</span><span class="s2">&quot;/opt/rocm/;/opt/rocm/hip;/root/MIOpen/install_dir&quot;</span><span class="w"> </span>..
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>When specifying the path for the <code class="docutils literal notranslate"><span class="pre">CMAKE_PREFIX_PATH</span></code> variable, <strong>do not</strong> use the tilde (<code class="docutils literal notranslate"><span class="pre">~</span></code>)
symbol to represent the home directory.</p>
</div>
</li>
</ol>
</section>
<section id="opencl-backend">
<h3>OpenCL backend<a class="headerlink" href="#opencl-backend" title="Link to this heading">#</a></h3>
<p>To build MIOpen using an OpenCL backend, run the following command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>-DMIOPEN_BACKEND<span class="o">=</span>OpenCL<span class="w"> </span>..
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>OpenCL is deprecated and the HIP backend is recommended instead. To install MIOpen using HIP, follow the instructions in
the preceding section.</p>
</div>
<p>The preceding code assumes OpenCL is installed in one of the standard locations. If not, then manually
set these CMake variables:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>-DMIOPEN_BACKEND<span class="o">=</span>OpenCL<span class="w"> </span>-DMIOPEN_HIP_COMPILER<span class="o">=</span>&lt;hip-compiler-path&gt;<span class="w"> </span>-DOPENCL_LIBRARIES<span class="o">=</span>&lt;opencl-library-path&gt;<span class="w"> </span>-DOPENCL_INCLUDE_DIRS<span class="o">=</span>&lt;opencl-headers-path&gt;<span class="w"> </span>..
</pre></div>
</div>
<p>Here’s an example showing how to configure the dependency path for an environment (applies to ROCm version 3.5 and later):</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>-DMIOPEN_BACKEND<span class="o">=</span>OpenCL<span class="w"> </span>-DMIOPEN_HIP_COMPILER<span class="o">=</span>/opt/rocm/llvm/bin/clang++<span class="w"> </span>-DCMAKE_PREFIX_PATH<span class="o">=</span><span class="s2">&quot;/opt/rocm/;/opt/rocm/hip;/root/MIOpen/install_dir&quot;</span><span class="w"> </span>..
</pre></div>
</div>
</section>
<section id="setting-the-install-location">
<span id="setting-up-locations"></span><h3>Setting the install location<a class="headerlink" href="#setting-the-install-location" title="Link to this heading">#</a></h3>
<p>By default, the install location is set to <code class="docutils literal notranslate"><span class="pre">/opt/rocm</span></code>. To change this, use <code class="docutils literal notranslate"><span class="pre">CMAKE_INSTALL_PREFIX</span></code>:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>-DMIOPEN_BACKEND<span class="o">=</span>HIP<span class="w"> </span>-DCMAKE_INSTALL_PREFIX<span class="o">=</span>&lt;miopen-installed-path&gt;<span class="w"> </span>..
</pre></div>
</div>
</section>
<section id="system-performance-database-and-user-database">
<h3>System performance database and user database<a class="headerlink" href="#system-performance-database-and-user-database" title="Link to this heading">#</a></h3>
<p>The default path to the system performance database (System PerfDb) is <code class="docutils literal notranslate"><span class="pre">miopen/share/miopen/db/</span></code>
within the install location. The default path to the user performance database (User PerfDb) is
<code class="docutils literal notranslate"><span class="pre">~/.config/miopen/</span></code>. Setting <code class="docutils literal notranslate"><span class="pre">BUILD_DEV</span></code> for development purposes changes the default path for
both database files to the source directory:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>-DMIOPEN_BACKEND<span class="o">=</span>HIP<span class="w"> </span>-DBUILD_DEV<span class="o">=</span>On<span class="w"> </span>..
</pre></div>
</div>
<p>To customize the database paths, use the <code class="docutils literal notranslate"><span class="pre">MIOPEN_SYSTEM_DB_PATH</span></code> (for the System PerfDb and FindDb)
and <code class="docutils literal notranslate"><span class="pre">MIOPEN_USER_DB_PATH</span></code> (for the User PerfDb and FindDb) CMake variables.
These db location variables are also settable at runtime through the environment.</p>
<p>It is safe to share the User Db location on a networked file system, however it is required that the machines
accessing the shared files have unique hostnames for the file sharing implemented in MIOpen to function correctly.</p>
<p>To learn more, see
<a class="reference internal" href="../conceptual/perfdb.html"><span class="doc">using the performance database</span></a>
<a class="reference internal" href="../conceptual/finddb.html"><span class="doc">using the find database</span></a></p>
</section>
<section id="persistent-program-cache">
<h3>Persistent program cache<a class="headerlink" href="#persistent-program-cache" title="Link to this heading">#</a></h3>
<p>By default, MIOpen caches device programs in the <code class="docutils literal notranslate"><span class="pre">~/.cache/miopen/</span></code> directory. Within the cache
directory, there is a directory for each version of MIOpen. To change the location of the cache
directory during configuration, use the <code class="docutils literal notranslate"><span class="pre">-DMIOPEN_CACHE_DIR=&lt;cache-directory-path&gt;</span></code> flag.</p>
<p>To disable the cache during runtime, set the <code class="docutils literal notranslate"><span class="pre">MIOPEN_DISABLE_CACHE=1</span></code> environmental
variable.</p>
<section id="for-miopen-version-2-3-and-earlier">
<h4>For MIOpen version 2.3 and earlier<a class="headerlink" href="#for-miopen-version-2-3-and-earlier" title="Link to this heading">#</a></h4>
<p>If the compiler changes or you modify the kernels, then you must delete the cache for the MIOpen
version in use, for example, <code class="docutils literal notranslate"><span class="pre">rm</span> <span class="pre">-rf</span> <span class="pre">~/.cache/miopen/&lt;miopen-version-number&gt;</span></code>. For more
information, see <a class="reference internal" href="../conceptual/cache.html"><span class="doc">kernel cache</span></a>.</p>
</section>
<section id="for-miopen-version-2-4-and-later">
<h4>For MIOpen version 2.4 and later<a class="headerlink" href="#for-miopen-version-2-4-and-later" title="Link to this heading">#</a></h4>
<p>MIOpen’s kernel cache directory is versioned, so cached kernels don’t collide when upgrading
from an earlier version.</p>
</section>
</section>
<section id="changing-the-cmake-configuration">
<h3>Changing the CMake configuration<a class="headerlink" href="#changing-the-cmake-configuration" title="Link to this heading">#</a></h3>
<p>The configuration can be changed after running CMake by using <code class="docutils literal notranslate"><span class="pre">ccmake</span></code>:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>ccmake<span class="w"> </span>..
</pre></div>
</div>
<p>or</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cmake-gui:<span class="w"> </span>cmake-gui<span class="w"> </span>..
</pre></div>
</div>
<p>The <code class="docutils literal notranslate"><span class="pre">ccmake</span></code> program can be downloaded using the Linux package <code class="docutils literal notranslate"><span class="pre">cmake-curses-gui</span></code>, but is not
available on Windows.</p>
</section>
</section>
<section id="building-the-library">
<h2>Building the library<a class="headerlink" href="#building-the-library" title="Link to this heading">#</a></h2>
<p>You can build the library from the <code class="docutils literal notranslate"><span class="pre">build</span></code> directory using the <code class="docutils literal notranslate"><span class="pre">Release</span></code> configuration:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>--build<span class="w"> </span>.<span class="w"> </span>--config<span class="w"> </span>Release
</pre></div>
</div>
<p>or</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>make
</pre></div>
</div>
<p>You can install it using the <code class="docutils literal notranslate"><span class="pre">install</span></code> target:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>--build<span class="w"> </span>.<span class="w"> </span>--config<span class="w"> </span>Release<span class="w"> </span>--target<span class="w"> </span>install
</pre></div>
</div>
<p>or</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>make<span class="w"> </span>install
</pre></div>
</div>
<p>This command installs the library to the <code class="docutils literal notranslate"><span class="pre">CMAKE_INSTALL_PREFIX</span></code> directory path.</p>
</section>
<section id="building-the-driver">
<h2>Building the driver<a class="headerlink" href="#building-the-driver" title="Link to this heading">#</a></h2>
<p>MIOpen provides an application driver that can run any layer in isolation and measure
library performance and verification.</p>
<p>To build the driver, use the <code class="docutils literal notranslate"><span class="pre">MIOpenDriver</span></code> target:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>--build<span class="w"> </span>.<span class="w"> </span>--config<span class="w"> </span>Release<span class="w"> </span>--target<span class="w"> </span>MIOpenDriver
</pre></div>
</div>
<p>or</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>make<span class="w"> </span>MIOpenDriver
</pre></div>
</div>
</section>
<section id="running-the-tests">
<h2>Running the tests<a class="headerlink" href="#running-the-tests" title="Link to this heading">#</a></h2>
<p>To run tests, use the <code class="docutils literal notranslate"><span class="pre">check</span></code> target:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>--build<span class="w"> </span>.<span class="w"> </span>--config<span class="w"> </span>Release<span class="w"> </span>--target<span class="w"> </span>check
</pre></div>
</div>
<p>or</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>make<span class="w"> </span>check
</pre></div>
</div>
<p>To build and run a single test, use the following commands:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>--build<span class="w"> </span>.<span class="w"> </span>--config<span class="w"> </span>Release<span class="w"> </span>--target<span class="w"> </span>test_tensor
./bin/test_tensor
</pre></div>
</div>
</section>
<section id="formatting-the-code">
<h2>Formatting the code<a class="headerlink" href="#formatting-the-code" title="Link to this heading">#</a></h2>
<p>To format the code using <code class="docutils literal notranslate"><span class="pre">clang-format</span></code>, use this command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>clang-format<span class="w"> </span>-style<span class="o">=</span>file<span class="w"> </span>-i<span class="w"> </span>&lt;path-to-source-file&gt;
</pre></div>
</div>
<p>To format the code per commit, install githooks:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>./.githooks/install
</pre></div>
</div>
</section>
<section id="storing-large-file-using-git-large-file-storage">
<h2>Storing large file using Git Large File Storage<a class="headerlink" href="#storing-large-file-using-git-large-file-storage" title="Link to this heading">#</a></h2>
<p><a class="reference external" href="https://dvc.org/">Data Versioning System (DVS)</a> replaces large files, such as audio samples, videos, datasets, and
graphics with text pointers inside Git, while storing the file contents on a remote server. MIOpen uses DVC to
store large files, such as kernel database files (<code class="docutils literal notranslate"><span class="pre">*.kdb</span></code>), which are normally &gt; 0.5 GB.</p>
<p>To install DVC, use the <a class="reference external" href="https://dvc.org/doc/install">instructions provided for your platform here</a>.</p>
<p>You can <a class="reference external" href="https://dvc.org/doc/command-reference/pull">pull</a> all large files or a single large file using:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>dvc<span class="w"> </span>pull
</pre></div>
</div>
<p>or</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>dvc<span class="w"> </span>pull<span class="w"> </span><span class="s2">&quot;filename&quot;</span>
</pre></div>
</div>
<p>If you are familiar with using Git LFS, a key difference with DVC is that you must manually run <code class="docutils literal notranslate"><span class="pre">dvc</span> <span class="pre">pull</span></code> after you
switch branches or merge changes in Git to ensure any large binaries are kept in sync with your checkout.</p>
</section>
<section id="installing-the-dependencies-manually">
<h2>Installing the dependencies manually<a class="headerlink" href="#installing-the-dependencies-manually" title="Link to this heading">#</a></h2>
<p>If you’re using Ubuntu v16, you can install the <code class="docutils literal notranslate"><span class="pre">Boost</span></code> packages using:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt-get<span class="w"> </span>install<span class="w"> </span>libboost-dev
sudo<span class="w"> </span>apt-get<span class="w"> </span>install<span class="w"> </span>libboost-system-dev
sudo<span class="w"> </span>apt-get<span class="w"> </span>install<span class="w"> </span>libboost-filesystem-dev
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>By default, MIOpen attempts to build with Boost statically linked libraries. To build
with dynamically linked Boost libraries, use the <code class="docutils literal notranslate"><span class="pre">-DBoost_USE_STATIC_LIBS=Off</span></code> flag during the
configuration stage. However, this is not recommended.</p>
</div>
<p>You must install the <code class="docutils literal notranslate"><span class="pre">half</span></code> header from the <a class="reference external" href="http://half.sourceforge.net/">half website</a>.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="install.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Install MIOpen</p>
      </div>
    </a>
    <a class="right-next"
       href="embed.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Build MIOpen for embedded systems</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#building-miopen">Building MIOpen</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-backend">HIP backend</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#opencl-backend">OpenCL backend</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#setting-the-install-location">Setting the install location</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#system-performance-database-and-user-database">System performance database and user database</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#persistent-program-cache">Persistent program cache</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#for-miopen-version-2-3-and-earlier">For MIOpen version 2.3 and earlier</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#for-miopen-version-2-4-and-later">For MIOpen version 2.4 and later</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#changing-the-cmake-configuration">Changing the CMake configuration</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#building-the-library">Building the library</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#building-the-driver">Building the driver</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#running-the-tests">Running the tests</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#formatting-the-code">Formatting the code</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#storing-large-file-using-git-large-file-storage">Storing large file using Git Large File Storage</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#installing-the-dependencies-manually">Installing the dependencies manually</a></li>
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
