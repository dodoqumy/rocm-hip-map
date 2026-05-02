---
title: "Installing and building rocRAND &#8212; rocRAND 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocRAND/en/latest/install/installing.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:11:15.746859+00:00
content_hash: "9af4f352c1f8b589"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="rocRAND installation guide" name="description" />
<meta content="rocRAND, ROCm, API, documentation, installation" name="keywords" />

    <title>Installing and building rocRAND &#8212; rocRAND 4.2.0 Documentation</title>
  
  
  
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
    <link rel="stylesheet" type="text/css" href="../_static/sphinx-design.min.css?v=87e54e7c" />
  
  <!-- So that users can add custom icons -->
  <script src="../_static/scripts/fontawesome.js?digest=8878045cc6db502f8baf"></script>
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../_static/scripts/bootstrap.js?digest=8878045cc6db502f8baf" />
<link rel="preload" as="script" href="../_static/scripts/pydata-sphinx-theme.js?digest=8878045cc6db502f8baf" />

    <script src="../_static/documentation_options.js?v=830d3dd9"></script>
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
    <script src="../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'install/installing';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="rocRAND programming guide" href="../conceptual/programmers-guide.html" />
    <link rel="prev" title="rocRAND documentation" href="../index.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocrand" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/install/installing.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
  
  
  
  
  
  
    <p class="title logo__title">rocRAND 4.2.0 Documentation</p>
  
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
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Installation guide</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../conceptual/programmers-guide.html">Programming guide</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/curand-compatibility.html">cuRAND compatibility</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/dynamic_ordering_configuration.html">Kernel configurations for dynamic ordering</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/generator-types.html">Random number generators</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Examples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocrand/python/rocrand/examples">Examples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">API reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../api-reference/data-type-support.html">rocRAND data type support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../api-reference/cpp-api.html">C/C++ API reference</a></li>
<li class="toctree-l1"><a class="reference internal" href="../api-reference/python-api.html">Python API reference</a></li>
<li class="toctree-l1"><a class="reference internal" href="../fortran-api-reference.html">Fortran API reference</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../doxygen/html/index.html">API library</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../doxygen/html/modules.html">Modules</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../doxygen/html/annotated_classes.html">Classes</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/annotated.html">Class List</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/hierarchy.html">Class Hierarchy</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../doxygen/html/functions_class_members.html">Class Members</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_all.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_func_functions.html">Functions</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_vars.html">Variables</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_type.html">Typedefs</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_rela.html">Related Functions</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="../doxygen/html/files.html">Files</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Installing and building rocRAND</span></li>
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
    <h1>Installing and building rocRAND</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#requirements">Requirements</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#install-using-prebuilt-packages">Install using prebuilt packages</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#build-rocrand-from-source">Build rocRAND from source</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#obtaining-the-rocrand-source-code">Obtaining the rocRAND source code</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#building-the-library">Building the library</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#building-with-cmake">Building with CMake</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-with-hip-on-windows">rocRAND with HIP on Windows</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#building-the-python-api-wrapper">Building the Python API wrapper</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id2">Requirements</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#installation">Installation</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="installing-and-building-rocrand">
<span id="installing"></span><h1>Installing and building rocRAND<a class="headerlink" href="#installing-and-building-rocrand" title="Link to this heading">#</a></h1>
<p>This topic describes how to install or build rocRAND. The easiest method is to install the prebuilt
packages from the ROCm repositories, but this chapter also describes how to build rocRAND from source.</p>
<section id="requirements">
<h2>Requirements<a class="headerlink" href="#requirements" title="Link to this heading">#</a></h2>
<p>rocRAND has the following prerequisites:</p>
<ul>
<li><p>CMake (version 3.16 or later)</p></li>
<li><p>C++ compiler with C++17 support to build the library</p>
<ul class="simple">
<li><p>gcc version 9 or later is recommended</p></li>
<li><p>Clang uses the development headers and libraries from gcc, so a recent version of it must still be installed when compiling with clang</p></li>
</ul>
</li>
<li><p>C++ compiler with C++11 support to use the library</p></li>
<li><p>(Optional) Fortran compiler (This is only required for the Fortran wrapper. GFortran is recommended.)</p></li>
<li><p>(Optional) GoogleTest (This is only required to build and use the tests. Building the tests is enabled by default.)</p>
<p>Use <code class="docutils literal notranslate"><span class="pre">GTEST_ROOT</span></code> to specify the GoogleTest location. For more information,
see <a class="reference external" href="https://cmake.org/cmake/help/latest/module/FindGTest.html">FindGTest</a>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If GoogleTest is not already installed, it will be automatically downloaded and built.</p>
</div>
</li>
<li><p>ROCm (see the <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html" title="(in ROCm installation on Linux v7.2.2)"><span class="xref std std-doc">ROCm installation guide</span></a>)</p></li>
<li><p>A HIP-clang compiler, which must be set as the C++ compiler on the ROCm platform.</p></li>
</ul>
</section>
<section id="install-using-prebuilt-packages">
<h2>Install using prebuilt packages<a class="headerlink" href="#install-using-prebuilt-packages" title="Link to this heading">#</a></h2>
<p>To install the prebuilt rocRAND packages, you require a ROCm-enabled platform.
For information on installing ROCm, see the <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html" title="(in ROCm installation on Linux v7.2.2)"><span class="xref std std-doc">ROCm installation guide</span></a>.
After installing ROCm or enabling the ROCm repositories, use the system package manager to install rocRAND.</p>
<p>For Ubuntu and Debian:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt-get<span class="w"> </span>install<span class="w"> </span>rocrand
</pre></div>
</div>
<p>For CentOS-based systems:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>yum<span class="w"> </span>install<span class="w"> </span>rocrand
</pre></div>
</div>
<p>For SLES:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>dnf<span class="w"> </span>install<span class="w"> </span>rocrand
</pre></div>
</div>
<p>These commands install rocRAND in the <code class="docutils literal notranslate"><span class="pre">/opt/rocm</span></code> directory.</p>
</section>
<section id="build-rocrand-from-source">
<h2>Build rocRAND from source<a class="headerlink" href="#build-rocrand-from-source" title="Link to this heading">#</a></h2>
<p>This section provides the information required to build rocRAND from source.</p>
<section id="obtaining-the-rocrand-source-code">
<h3>Obtaining the rocRAND source code<a class="headerlink" href="#obtaining-the-rocrand-source-code" title="Link to this heading">#</a></h3>
<p>The rocRAND source code is available from the <a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocrand">rocrand folder</a> of
the <a class="reference external" href="https://github.com/ROCm/rocm-libraries">rocm-libraries</a> GitHub repository.
Use the branch that matches the ROCm version installed on the system.
The rocRAND source code can be cloned in two different ways.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>For both methods, replace all occurrences of “x.y” in the commands with the version number matching your ROCm installation.
For example, if you have ROCm 7.0 installed, clone the <code class="docutils literal notranslate"><span class="pre">release/rocm-rel-7.0</span></code> branch.</p>
</div>
<ul>
<li><p>Clone the entire <a class="reference external" href="https://github.com/ROCm/rocm-libraries">rocm-libraries</a> repository.
This is the default method and is the recommended option if you need to install other
ROCm libraries alongside rocRAND. However, due to the download size, <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code>
might take a significant amount of time to complete.</p>
<p>On a system with ROCm x.y installed, use the following command to obtain the source code
for rocRAND version x.y. Replace x.y with the actual version:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>git<span class="w"> </span>clone<span class="w"> </span>-b<span class="w"> </span>release/rocm-rel-x.y<span class="w"> </span>https://github.com/ROCm/rocm-libraries.git
</pre></div>
</div>
</li>
<li><p>Clone the individual rocRAND project folder. This option only fetches the rocRAND source code,
without any additional ROCm libraries. This significantly reduces the amount of time required
to complete the clone operation. However, it requires Git 2.25 or later.
To use this method to obtain the source code for rocRAND version x.y, run the following commands.
Replace x.y with the actual version:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>git<span class="w"> </span>clone<span class="w"> </span>-b<span class="w"> </span>release/rocm-rel-x.y<span class="w"> </span>--no-checkout<span class="w"> </span>--depth<span class="o">=</span><span class="m">1</span><span class="w"> </span>--filter<span class="o">=</span>tree:0<span class="w"> </span>https://github.com/ROCm/rocm-libraries.git
<span class="nb">cd</span><span class="w"> </span>rocm-libraries
git<span class="w"> </span>sparse-checkout<span class="w"> </span><span class="nb">set</span><span class="w"> </span>--cone<span class="w"> </span>projects/rocrand
git<span class="w"> </span>checkout<span class="w"> </span>release/rocm-rel-x.y
</pre></div>
</div>
</li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>To build ROCm 6.4 and earlier, use the rocRAND repository at <a class="github reference external" href="https://github.com/ROCm/rocRAND">ROCm/rocRAND</a>.
For more information, see the documentation associated with the release you want to build.</p>
</div>
</section>
<section id="building-the-library">
<h3>Building the library<a class="headerlink" href="#building-the-library" title="Link to this heading">#</a></h3>
<p>After downloading the source code, use the installation script to build rocRAND:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nb">cd</span><span class="w"> </span>rocm-libraries/projects/rocrand
./install<span class="w"> </span>--install
</pre></div>
</div>
<p>This automatically builds all required dependencies, excluding HIP and Git, and installs the project
to <code class="docutils literal notranslate"><span class="pre">/opt/rocm</span></code>. For further information, run the <code class="docutils literal notranslate"><span class="pre">./install</span> <span class="pre">--help</span></code> command.</p>
</section>
<section id="building-with-cmake">
<h3>Building with CMake<a class="headerlink" href="#building-with-cmake" title="Link to this heading">#</a></h3>
<p>For a more detailed installation process, build rocRAND manually using CMake.
This enables certain configuration options that are not available through the <code class="docutils literal notranslate"><span class="pre">install</span></code> script.
To build rocRAND, use CMake with the following configuration:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nb">cd</span><span class="w"> </span>rocm-libraries/projects/rocrand<span class="p">;</span><span class="w"> </span>mkdir<span class="w"> </span>build<span class="p">;</span><span class="w"> </span><span class="nb">cd</span><span class="w"> </span>build
<span class="c1"># Configure the project</span>
<span class="nv">CXX</span><span class="o">=</span>&lt;compiler&gt;<span class="w"> </span>cmake<span class="w"> </span><span class="o">[</span>options<span class="o">]</span><span class="w"> </span>..
<span class="c1"># Build</span>
make<span class="w"> </span>-j4
<span class="c1"># Optionally, run the tests</span>
ctest<span class="w"> </span>--output-on-failure
<span class="c1"># Install</span>
<span class="o">[</span>sudo<span class="o">]</span><span class="w"> </span>make<span class="w"> </span>install
</pre></div>
</div>
<p>To build for the ROCm platform, <code class="docutils literal notranslate"><span class="pre">&lt;compiler&gt;</span></code> should be set to <code class="docutils literal notranslate"><span class="pre">hipcc</span></code>.
Additionally, the directory where <code class="docutils literal notranslate"><span class="pre">FindHIP.cmake</span></code> is installed needs to be passed explicitly
using <code class="docutils literal notranslate"><span class="pre">-DCMAKE_MODULE_PATH</span></code>. By default, this file is installed in <code class="docutils literal notranslate"><span class="pre">/opt/rocm/hip/cmake</span></code>.</p>
<p>In addition to the built-in CMake options, the following configuration options are available:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">BUILD_FORTRAN_WRAPPER</span></code>: Controls whether to build the Fortran wrapper. Defaults to <code class="docutils literal notranslate"><span class="pre">OFF</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BUILD_TEST</span></code>: Controls whether to build the rocRAND tests. Defaults to <code class="docutils literal notranslate"><span class="pre">OFF</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BUILD_BENCHMARK</span></code>: Controls whether to build the rocRAND benchmarks. Defaults to <code class="docutils literal notranslate"><span class="pre">OFF</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BUILD_ADDRESS_SANITIZER</span></code> Controls whether to build with address sanitization enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">OFF</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">USE_SYSTEM_LIB</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Set to <code class="docutils literal notranslate"><span class="pre">ON</span></code> to use the installed <code class="docutils literal notranslate"><span class="pre">ROCm</span></code> libraries when building the
tests. For this option to take effect, <code class="docutils literal notranslate"><span class="pre">BUILD_TEST</span></code> must be <code class="docutils literal notranslate"><span class="pre">ON</span></code> and the version of the installed <code class="docutils literal notranslate"><span class="pre">rocrand</span></code>
library must be compatible with the version of the tests.</p></li>
</ul>
<p>To install rocRAND with a non-standard installation location of ROCm, pass <code class="docutils literal notranslate"><span class="pre">-DCMAKE_PREFIX_PATH=&lt;/path/to/opt/rocm/&gt;</span></code>
or set the environment variable <code class="docutils literal notranslate"><span class="pre">ROCM_PATH</span></code> to <code class="docutils literal notranslate"><span class="pre">path/to/opt/rocm</span></code>.</p>
</section>
</section>
<section id="rocrand-with-hip-on-windows">
<h2>rocRAND with HIP on Windows<a class="headerlink" href="#rocrand-with-hip-on-windows" title="Link to this heading">#</a></h2>
<p>rocRAND with HIP on Microsoft Windows has the following additional prerequisites:</p>
<ul class="simple">
<li><p>Python 3.6 or higher (Only required for the install script)</p></li>
<li><p>Visual Studio 2019 with Clang support</p></li>
<li><p>Strawberry Perl</p></li>
</ul>
<p>To install support for rocRAND and HIP on Windows, use the <code class="docutils literal notranslate"><span class="pre">rmake.py</span></code> Python script as follows:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>git<span class="w"> </span>clone<span class="w"> </span>https://github.com/ROCm/rocm-libraries.git
<span class="nb">cd</span><span class="w"> </span>rocm-libraries/projects/rocrand

<span class="c1"># the -i option will install rocRAND to C:\hipSDK by default</span>
python<span class="w"> </span>rmake.py<span class="w"> </span>-i

<span class="c1"># the -c option will build all clients including unit tests</span>
python<span class="w"> </span>rmake.py<span class="w"> </span>-c
</pre></div>
</div>
<p>Any existing GoogleTest library in the system (especially static GoogleTest libraries built with other compilers)
might cause a build failure. If you encounter errors with the existing GoogleTest library or other dependencies,
pass the <code class="docutils literal notranslate"><span class="pre">DEPENDENCIES_FORCE_DOWNLOAD</span></code> flag to CMake to help solve the problem.</p>
<p>To disable inline assembly optimizations in rocRAND for both the host library and the device functions provided in <code class="docutils literal notranslate"><span class="pre">rocrand_kernel.h</span></code>,
set the CMake option <code class="docutils literal notranslate"><span class="pre">ENABLE_INLINE_ASM</span></code> to <code class="docutils literal notranslate"><span class="pre">OFF</span></code>.</p>
</section>
<section id="building-the-python-api-wrapper">
<h2>Building the Python API wrapper<a class="headerlink" href="#building-the-python-api-wrapper" title="Link to this heading">#</a></h2>
<p>This section provides the information required to build the rocRAND Python API wrapper.</p>
<section id="id2">
<h3>Requirements<a class="headerlink" href="#id2" title="Link to this heading">#</a></h3>
<p>The rocRAND Python API Wrapper requires the following dependencies:</p>
<ul class="simple">
<li><p>rocRAND</p></li>
<li><p>Python 3.5</p></li>
<li><p>NumPy (will be installed automatically as a dependency if necessary)</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If rocRAND is built from source but is either not installed or installed in a
non-standard directory, set the <code class="docutils literal notranslate"><span class="pre">ROCRAND_PATH</span></code> environment variable
to the library location. For example:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nb">export</span><span class="w"> </span><span class="nv">ROCRAND_PATH</span><span class="o">=</span>~rocm-libraries/projects/rocrand/build/library/
</pre></div>
</div>
</div>
</section>
<section id="installation">
<h3>Installation<a class="headerlink" href="#installation" title="Link to this heading">#</a></h3>
<p>The Python rocRAND module can be installed using <code class="docutils literal notranslate"><span class="pre">pip</span></code>:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nb">cd</span><span class="w"> </span>rocm-libraries/projects/rocrand/python/rocrand
pip<span class="w"> </span>install<span class="w"> </span>.
</pre></div>
</div>
<p>The tests can be executed as follows:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nb">cd</span><span class="w"> </span>rocm-libraries/projects/rocrand/python/rocrand
python<span class="w"> </span>tests/rocrand_test.py
</pre></div>
</div>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../index.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">rocRAND documentation</p>
      </div>
    </a>
    <a class="right-next"
       href="../conceptual/programmers-guide.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">rocRAND programming guide</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#requirements">Requirements</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#install-using-prebuilt-packages">Install using prebuilt packages</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#build-rocrand-from-source">Build rocRAND from source</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#obtaining-the-rocrand-source-code">Obtaining the rocRAND source code</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#building-the-library">Building the library</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#building-with-cmake">Building with CMake</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-with-hip-on-windows">rocRAND with HIP on Windows</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#building-the-python-api-wrapper">Building the Python API wrapper</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id2">Requirements</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#installation">Installation</a></li>
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
