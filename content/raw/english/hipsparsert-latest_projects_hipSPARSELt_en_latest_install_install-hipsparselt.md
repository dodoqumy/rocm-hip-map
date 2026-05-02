---
title: "Installing and building hipSPARSELt &#8212; hipSPARSELt 0.2.6 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSELt/en/latest/install/install-hipsparselt.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:11:01.413629+00:00
content_hash: "2e28a04aacdbb062"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Installing hipSPARSELt on Linux" name="description" />
<meta content="hipSPARSELt, ROCm, install, Linux" name="keywords" />

    <title>Installing and building hipSPARSELt &#8212; hipSPARSELt 0.2.6 Documentation</title>
  
  
  
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
    <link rel="stylesheet" type="text/css" href="../_static/styles/sphinx-book-theme.css?v=a3416100" />
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

    <script src="../_static/documentation_options.js?v=519527b2"></script>
    <script src="../_static/doctools.js?v=9bcbadda"></script>
    <script src="../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../_static/search.js?v=90a4452c"></script>
    <script src="../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
    <script src="../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'install/install-hipsparselt';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="hipSPARSELt storage format" href="../conceptual/storage-format.html" />
    <link rel="prev" title="Quick start hipSPARSELt installation guide" href="quick-start-install.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hipsparselt" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/install/install-hipsparselt.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
  
  
  
  
  
  
    <p class="title logo__title">hipSPARSELt 0.2.6 Documentation</p>
  
</a></div>
        <div class="sidebar-primary-item">

<button class="btn search-button-field search-button__button pst-js-only" title="Search" aria-label="Search" data-bs-placement="bottom" data-bs-toggle="tooltip">
 <i class="fa-solid fa-magnifying-glass"></i>
 <span class="search-button__default-text">Search</span>
 <span class="search-button__kbd-shortcut"><kbd class="kbd-shortcut__modifier">Ctrl</kbd>+<kbd class="kbd-shortcut__modifier">K</kbd></span>
</button></div>
        <div class="sidebar-primary-item"><nav class="bd-links bd-docs-nav" aria-label="Main">
    <div class="bd-toc-item navbar-nav active">
        <ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../what-is-hipsparselt.html">What is hipSPARSELt?</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="quick-start-install.html">Quick start installation guide</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Detailed installation guide</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../conceptual/storage-format.html">Storage formats</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/mi300-features.html">Features for the Instinct MI300 series</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../how-to/device-stream-management.html">Manage devices and streams</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/porting.html">Port from NVIDIA CUDA</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Examples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparselt/clients/samples">Client samples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">API Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../reference/supported-functions.html">Supported functions</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/data-type-support.html">Data type support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/env-variables.html">Environment variables</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../doxygen/html/index.html">API library</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../doxygen/html/modules.html">Modules</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../doxygen/html/annotated_data_structures.html">Data Structures</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/classes.html">Data Structure Index</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../doxygen/html/functions_data_fields.html">Data Fields</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_vars.html">Variables</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../doxygen/html/files_files.html">Files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/files.html">File List</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../doxygen/html/globals_globals.html">Globals</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_func.html">Functions</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_enum.html">Enumerations</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_eval.html">Enumerator</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_defs.html">Macros</a></li>
</ul>
</details></li>
</ul>
</details></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Installing and building hipSPARSELt</span></li>
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
<button class="sidebar-toggle secondary-toggle btn btn-sm" title="Toggle secondary sidebar" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <span class="fa-solid fa-list"></span>
</button>
</div></div>
      
    </div>
  
</div>
</div>
              
              

<div id="jb-print-docs-body" class="onlyprint">
    <h1>Installing and building hipSPARSELt</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#prerequisites">Prerequisites</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#installing-prebuilt-packages">Installing prebuilt packages</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#building-hipsparselt-from-source">Building hipSPARSELt from source</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#downloading-hipsparselt">Downloading hipSPARSELt</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#building-hipsparselt-using-the-install-script">Building hipSPARSELt using the install script</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#using-install-sh-to-build-hipsparselt-with-dependencies">Using install.sh to build hipSPARSELt with dependencies</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#using-install-sh-to-build-hipsparselt-with-dependencies-and-clients">Using install.sh to build hipSPARSELt with dependencies and clients</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#building-hipsparselt-using-individual-make-commands">Building hipSPARSELt using individual make commands</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#testing-the-hipsparselt-installation">Testing the hipSPARSELt installation</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#running-the-benchmarks-and-unit-tests">Running the benchmarks and unit tests</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="installing-and-building-hipsparselt">
<span id="install-linux"></span><h1>Installing and building hipSPARSELt<a class="headerlink" href="#installing-and-building-hipsparselt" title="Link to this heading">#</a></h1>
<p>This topic explains how to install and build the hipSPARSELt library.</p>
<section id="prerequisites">
<h2>Prerequisites<a class="headerlink" href="#prerequisites" title="Link to this heading">#</a></h2>
<p>hipSPARSELt requires a <a class="reference external" href="https://rocm.docs.amd.com/en/latest/index.html" title="(in ROCm Documentation v7.2.2)"><span class="xref std std-doc">ROCm-enabled platform</span></a> and the
<a class="reference external" href="https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/index.html" title="(in hipSPARSE Documentation v4.2.0)"><span class="xref std std-doc">hipSPARSE library</span></a> for the header file.</p>
</section>
<section id="installing-prebuilt-packages">
<h2>Installing prebuilt packages<a class="headerlink" href="#installing-prebuilt-packages" title="Link to this heading">#</a></h2>
<p>hipSPARSELt can be installed from the AMD ROCm repository.
For detailed instructions on installing ROCm, see <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/index.html" title="(in ROCm installation on Linux v7.2.2)"><span class="xref std std-doc">ROCm installation</span></a>.</p>
<p>To install hipSPARSELt on Ubuntu, run these commands:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt-get<span class="w"> </span>update
sudo<span class="w"> </span>apt-get<span class="w"> </span>install<span class="w"> </span>hipsparselt
</pre></div>
</div>
<p>After hipSPARSELt is installed, it can be used just like any other library with a C API.
To call hipSPARSELt, the header file must be included in the user code.
This means the hipSPARSELt shared library becomes a link-time and run-time dependency for the user application.</p>
</section>
<section id="building-hipsparselt-from-source">
<h2>Building hipSPARSELt from source<a class="headerlink" href="#building-hipsparselt-from-source" title="Link to this heading">#</a></h2>
<p>It isn’t necessary to build hipSPARSELt from source because it’s ready to use after installing
the prebuilt packages, as described above.
To build hipSPARSELt from source, follow the instructions in this section.</p>
<p>To compile and run hipSPARSELt, the <a class="reference external" href="https://github.com/ROCm/ROCm">ROCm platform</a> is required.
The build also requires the following compile-time dependencies:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparse">hipSPARSE</a></p></li>
<li><p><a class="reference external" href="https://git-scm.com/">git</a></p></li>
<li><p><a class="reference external" href="https://cmake.org/">CMake</a> (Version 3.5 or later)</p></li>
<li><p><a class="reference external" href="https://github.com/google/googletest">GoogleTest</a> (Optional: only required to build the clients)</p></li>
</ul>
<section id="downloading-hipsparselt">
<h3>Downloading hipSPARSELt<a class="headerlink" href="#downloading-hipsparselt" title="Link to this heading">#</a></h3>
<p>The hipSPARSELt source code is available from the
the <a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparselt">hipSPARSELt</a> directory
of the <a class="reference external" href="https://github.com/ROCm/rocm-libraries">rocm-libraries</a> GitHub.</p>
<p>Download the develop branch for hipSPARSELt and all projects in the rocm-libraries repository
using these commands:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>git<span class="w"> </span>clone<span class="w"> </span>-b<span class="w"> </span>develop<span class="w"> </span>https://github.com/ROCm/rocm-libraries.git
<span class="nb">cd</span><span class="w"> </span>rocm-libraries/projects/hipsparselt
</pre></div>
</div>
<p>To limit your local checkout to the hipSPARSELt project, configure <code class="docutils literal notranslate"><span class="pre">sparse-checkout</span></code> before cloning.
This uses the Git partial clone feature (<code class="docutils literal notranslate"><span class="pre">--filter=blob:none</span></code>) to reduce how much data is downloaded.
Use the following commands for a sparse checkout:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>git<span class="w"> </span>clone<span class="w"> </span>--no-checkout<span class="w"> </span>--filter<span class="o">=</span>blob:none<span class="w"> </span>https://github.com/ROCm/rocm-libraries.git
<span class="nb">cd</span><span class="w"> </span>rocm-libraries
git<span class="w"> </span>sparse-checkout<span class="w"> </span>init<span class="w"> </span>--cone
git<span class="w"> </span>sparse-checkout<span class="w"> </span><span class="nb">set</span><span class="w"> </span>projects/hipsparselt
git<span class="w"> </span>checkout<span class="w"> </span>develop<span class="w"> </span><span class="c1"># or use the branch you want to work with</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>To build ROCm 6.4.3 and earlier, use the hipSPARSELt repository at <a class="github reference external" href="https://github.com/ROCm/hipSPARSELt">ROCm/hipSPARSELt</a>.
For more information, see the documentation associated with the release you want to build.</p>
</div>
</section>
<section id="building-hipsparselt-using-the-install-script">
<h3>Building hipSPARSELt using the install script<a class="headerlink" href="#building-hipsparselt-using-the-install-script" title="Link to this heading">#</a></h3>
<p>It’s recommended to use the <code class="docutils literal notranslate"><span class="pre">install.sh</span></code> script to install hipSPARSELt.
Here are the steps required to build different packages of the library, including the dependencies and clients.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>You can run the <code class="docutils literal notranslate"><span class="pre">install.sh</span></code> script from the <code class="docutils literal notranslate"><span class="pre">projects/hipsparselt</span></code> directory.</p>
</div>
<section id="using-install-sh-to-build-hipsparselt-with-dependencies">
<h4>Using install.sh to build hipSPARSELt with dependencies<a class="headerlink" href="#using-install-sh-to-build-hipsparselt-with-dependencies" title="Link to this heading">#</a></h4>
<p>The following table lists the common ways to use <code class="docutils literal notranslate"><span class="pre">install.sh</span></code> to build the hipSPARSELt dependencies and library.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 23.1%" />
<col style="width: 76.9%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Command</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">./install.sh</span> <span class="pre">-h</span></code></p></td>
<td><p>Print the help information.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">./install.sh</span> <span class="pre">-d</span></code></p></td>
<td><p>Build the dependencies and library in your local directory.  The <code class="docutils literal notranslate"><span class="pre">-d</span></code> flag only needs to be used once. For subsequent invocations of the script, it isn’t necessary to rebuild the dependencies.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">./install.sh</span></code></p></td>
<td><p>Build the library in your local directory. The script assumes the dependencies are available.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">./install.sh</span> <span class="pre">-i</span></code></p></td>
<td><p>Build the library, then build and install the hipSPARSELt package in <code class="docutils literal notranslate"><span class="pre">/opt/rocm/hipsparselt</span></code>. The script prompts you for <code class="docutils literal notranslate"><span class="pre">sudo</span></code> access. This installs hipSPARSELt for all users.</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="using-install-sh-to-build-hipsparselt-with-dependencies-and-clients">
<h4>Using install.sh to build hipSPARSELt with dependencies and clients<a class="headerlink" href="#using-install-sh-to-build-hipsparselt-with-dependencies-and-clients" title="Link to this heading">#</a></h4>
<p>The clients contains example code and unit tests. Common uses of <code class="docutils literal notranslate"><span class="pre">install.sh</span></code> to build them are listed in the table below.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 23.1%" />
<col style="width: 76.9%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Command</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">./install.sh</span> <span class="pre">-h</span></code></p></td>
<td><p>Print the help information.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">./install.sh</span> <span class="pre">-dc</span></code></p></td>
<td><p>Build the dependencies, library, and client in your local directory. The <code class="docutils literal notranslate"><span class="pre">-d</span></code> flag only needs to be used once. For subsequent invocations of the script, it isn’t necessary to rebuild the dependencies.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">./install.sh</span> <span class="pre">-c</span></code></p></td>
<td><p>Build the library and client in your local directory. The script assumes the dependencies are available.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">./install.sh</span> <span class="pre">-idc</span></code></p></td>
<td><p>Build the library, dependencies, and client, then build and install the hipSPARSELt package in <code class="docutils literal notranslate"><span class="pre">/opt/rocm/hipsparselt</span></code>. The script prompts you for <code class="docutils literal notranslate"><span class="pre">sudo</span></code> access. This installs hipSPARSELt for all users.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">./install.sh</span> <span class="pre">-ic</span></code></p></td>
<td><p>Build the library and client, then build and install the hipSPARSELt package in <code class="docutils literal notranslate"><span class="pre">opt/rocm/hipsparselt</span></code>. The script prompts you for <code class="docutils literal notranslate"><span class="pre">sudo</span></code> access. This installs hipSPARSELt for all users.</p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<section id="building-hipsparselt-using-individual-make-commands">
<h3>Building hipSPARSELt using individual make commands<a class="headerlink" href="#building-hipsparselt-using-individual-make-commands" title="Link to this heading">#</a></h3>
<p>You can build hipSPARSELt using the following commands:</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Run these commands from the <code class="docutils literal notranslate"><span class="pre">projects/hipsparselt</span></code> directory.</p>
<p>CMake 3.16.8 or later is required to build hipSPARSELt.</p>
</div>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="c1"># Create and change the build directory</span>
mkdir<span class="w"> </span>-p<span class="w"> </span>build/release<span class="w"> </span><span class="p">;</span><span class="w"> </span><span class="nb">cd</span><span class="w"> </span>build/release

<span class="c1"># Change default install path (/opt/rocm); use -DCMAKE_INSTALL_PREFIX=&lt;path&gt; to adjust the path</span>
cmake<span class="w"> </span>../..

<span class="c1"># Compile the hipSPARSELt library</span>
make<span class="w"> </span>-j<span class="k">$(</span>nproc<span class="k">)</span>

<span class="c1"># Install hipSPARSELt to `/opt/rocm`</span>
make<span class="w"> </span>install
</pre></div>
</div>
<p>You can build hipSPARSELt with the dependencies and clients using the following commands:</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>GoogleTest is required to build the hipSPARSELt clients.</p>
</div>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="c1"># Install GoogleTest</span>
mkdir<span class="w"> </span>-p<span class="w"> </span>build/release/deps<span class="w"> </span><span class="p">;</span><span class="w"> </span><span class="nb">cd</span><span class="w"> </span>build/release/deps
cmake<span class="w"> </span>../../../deps
make<span class="w"> </span>-j<span class="k">$(</span>nproc<span class="k">)</span><span class="w"> </span>install

<span class="c1"># Change to build directory</span>
<span class="nb">cd</span><span class="w"> </span>..

<span class="c1"># Default install path is /opt/rocm, use -DCMAKE_INSTALL_PREFIX=&lt;path&gt; to adjust it</span>
cmake<span class="w"> </span>../..<span class="w"> </span>-DBUILD_CLIENTS_TESTS<span class="o">=</span>ON<span class="w"> </span>-DBUILD_CLIENTS_SAMPLES<span class="o">=</span>ON

<span class="c1"># Compile hipSPARSELt library</span>
make<span class="w"> </span>-j<span class="k">$(</span>nproc<span class="k">)</span>

<span class="c1"># Install hipSPARSELt to /opt/rocm</span>
make<span class="w"> </span>install
</pre></div>
</div>
</section>
</section>
<section id="testing-the-hipsparselt-installation">
<h2>Testing the hipSPARSELt installation<a class="headerlink" href="#testing-the-hipsparselt-installation" title="Link to this heading">#</a></h2>
<p>After successfully compiling the library with the clients, you can test the hipSPARSELt installation by running an example:</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Run these commands from the <code class="docutils literal notranslate"><span class="pre">projects/hipsparselt</span></code> directory.</p>
</div>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="c1"># Navigate to clients binary directory</span>
<span class="nb">cd</span><span class="w"> </span>build/release/clients/staging

<span class="c1"># Execute hipSPARSELt example</span>
./example_spmm_strided_batched<span class="w"> </span>-m<span class="w"> </span><span class="m">32</span><span class="w"> </span>-n<span class="w"> </span><span class="m">32</span><span class="w"> </span>-k<span class="w"> </span><span class="m">32</span><span class="w"> </span>--batch_count<span class="w"> </span><span class="m">1</span>
</pre></div>
</div>
<section id="running-the-benchmarks-and-unit-tests">
<h3>Running the benchmarks and unit tests<a class="headerlink" href="#running-the-benchmarks-and-unit-tests" title="Link to this heading">#</a></h3>
<p>To run the benchmarks, build hipSPARSELt with the <code class="docutils literal notranslate"><span class="pre">-DBUILD_CLIENTS_BENCHMARKS=ON</span></code> option (or use <code class="docutils literal notranslate"><span class="pre">./install.sh</span> <span class="pre">-c</span></code>).</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="c1"># Go to hipSPARSELt build directory</span>
<span class="nb">cd</span><span class="w"> </span>build/release

<span class="c1"># Run benchmark, e.g.</span>
./clients/staging/hipsparselt-bench<span class="w"> </span>-f<span class="w"> </span>spmm<span class="w"> </span>-i<span class="w"> </span><span class="m">200</span><span class="w"> </span>-m<span class="w"> </span><span class="m">256</span><span class="w"> </span>-n<span class="w"> </span><span class="m">256</span><span class="w"> </span>-k<span class="w"> </span><span class="m">256</span>
</pre></div>
</div>
<p>To run the unit tests, build hipSPARSELt with the <code class="docutils literal notranslate"><span class="pre">-DBUILD_CLIENTS_TESTS=ON</span></code> option (or use <code class="docutils literal notranslate"><span class="pre">./install.sh</span> <span class="pre">-c</span></code>).</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="c1"># Go to hipSPARSELt build directory</span>
<span class="nb">cd</span><span class="w"> </span>build/release

<span class="c1"># Run all tests</span>
./clients/staging/hipsparselt-test
</pre></div>
</div>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="quick-start-install.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Quick start hipSPARSELt installation guide</p>
      </div>
    </a>
    <a class="right-next"
       href="../conceptual/storage-format.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">hipSPARSELt storage format</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#prerequisites">Prerequisites</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#installing-prebuilt-packages">Installing prebuilt packages</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#building-hipsparselt-from-source">Building hipSPARSELt from source</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#downloading-hipsparselt">Downloading hipSPARSELt</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#building-hipsparselt-using-the-install-script">Building hipSPARSELt using the install script</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#using-install-sh-to-build-hipsparselt-with-dependencies">Using install.sh to build hipSPARSELt with dependencies</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#using-install-sh-to-build-hipsparselt-with-dependencies-and-clients">Using install.sh to build hipSPARSELt with dependencies and clients</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#building-hipsparselt-using-individual-make-commands">Building hipSPARSELt using individual make commands</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#testing-the-hipsparselt-installation">Testing the hipSPARSELt installation</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#running-the-benchmarks-and-unit-tests">Running the benchmarks and unit tests</a></li>
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
