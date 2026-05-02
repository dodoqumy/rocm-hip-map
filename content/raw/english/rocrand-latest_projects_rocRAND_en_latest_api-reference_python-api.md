---
title: "Python API reference &#8212; rocRAND 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocRAND/en/latest/api-reference/python-api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:11:09.655627+00:00
content_hash: "5e3b5952a3060e3a"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="rocRAND Python API reference" name="description" />
<meta content="rocRAND, ROCm, API, documentation, Python" name="keywords" />

    <title>Python API reference &#8212; rocRAND 4.2.0 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'api-reference/python-api';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Fortran API reference" href="../fortran-api-reference.html" />
    <link rel="prev" title="C/C++ API reference" href="cpp-api.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocrand" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/api-reference/python-api.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../install/installing.html">Installation guide</a></li>
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
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="data-type-support.html">rocRAND data type support</a></li>
<li class="toctree-l1"><a class="reference internal" href="cpp-api.html">C/C++ API reference</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Python API reference</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Python API reference</span></li>
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
    <h1>Python API reference</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#api-index">API index</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#class-prng">class PRNG</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG"><code class="docutils literal notranslate"><span class="pre">PRNG</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.DEFAULT"><code class="docutils literal notranslate"><span class="pre">PRNG.DEFAULT</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.LFSR113"><code class="docutils literal notranslate"><span class="pre">PRNG.LFSR113</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.MRG31K3P"><code class="docutils literal notranslate"><span class="pre">PRNG.MRG31K3P</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.MRG32K3A"><code class="docutils literal notranslate"><span class="pre">PRNG.MRG32K3A</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.MT19937"><code class="docutils literal notranslate"><span class="pre">PRNG.MT19937</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.MTGP32"><code class="docutils literal notranslate"><span class="pre">PRNG.MTGP32</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.PHILOX4_32_10"><code class="docutils literal notranslate"><span class="pre">PRNG.PHILOX4_32_10</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.THREEFRY2_32_20"><code class="docutils literal notranslate"><span class="pre">PRNG.THREEFRY2_32_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.THREEFRY2_64_20"><code class="docutils literal notranslate"><span class="pre">PRNG.THREEFRY2_64_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.THREEFRY4_32_20"><code class="docutils literal notranslate"><span class="pre">PRNG.THREEFRY4_32_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.THREEFRY4_64_20"><code class="docutils literal notranslate"><span class="pre">PRNG.THREEFRY4_64_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.XORWOW"><code class="docutils literal notranslate"><span class="pre">PRNG.XORWOW</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.generate"><code class="docutils literal notranslate"><span class="pre">PRNG.generate()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.lognormal"><code class="docutils literal notranslate"><span class="pre">PRNG.lognormal()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.normal"><code class="docutils literal notranslate"><span class="pre">PRNG.normal()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.offset"><code class="docutils literal notranslate"><span class="pre">PRNG.offset</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.poisson"><code class="docutils literal notranslate"><span class="pre">PRNG.poisson()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.seed"><code class="docutils literal notranslate"><span class="pre">PRNG.seed</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.uniform"><code class="docutils literal notranslate"><span class="pre">PRNG.uniform()</span></code></a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#class-qrng">class QRNG</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG"><code class="docutils literal notranslate"><span class="pre">QRNG</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.DEFAULT"><code class="docutils literal notranslate"><span class="pre">QRNG.DEFAULT</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.SCRAMBLED_SOBOL32"><code class="docutils literal notranslate"><span class="pre">QRNG.SCRAMBLED_SOBOL32</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.SCRAMBLED_SOBOL64"><code class="docutils literal notranslate"><span class="pre">QRNG.SCRAMBLED_SOBOL64</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.SOBOL32"><code class="docutils literal notranslate"><span class="pre">QRNG.SOBOL32</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.SOBOL64"><code class="docutils literal notranslate"><span class="pre">QRNG.SOBOL64</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.generate"><code class="docutils literal notranslate"><span class="pre">QRNG.generate()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.lognormal"><code class="docutils literal notranslate"><span class="pre">QRNG.lognormal()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.ndim"><code class="docutils literal notranslate"><span class="pre">QRNG.ndim</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.normal"><code class="docutils literal notranslate"><span class="pre">QRNG.normal()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.offset"><code class="docutils literal notranslate"><span class="pre">QRNG.offset</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.poisson"><code class="docutils literal notranslate"><span class="pre">QRNG.poisson()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.uniform"><code class="docutils literal notranslate"><span class="pre">QRNG.uniform()</span></code></a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#exceptions">Exceptions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.RocRandError"><code class="docutils literal notranslate"><span class="pre">RocRandError</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.HipError"><code class="docutils literal notranslate"><span class="pre">HipError</span></code></a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#utilities">Utilities</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.DeviceNDArray"><code class="docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.DeviceNDArray.copy_to_host"><code class="docutils literal notranslate"><span class="pre">DeviceNDArray.copy_to_host()</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.empty"><code class="docutils literal notranslate"><span class="pre">empty()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.get_version"><code class="docutils literal notranslate"><span class="pre">get_version()</span></code></a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="python-api-reference">
<span id="python-api"></span><h1>Python API reference<a class="headerlink" href="#python-api-reference" title="Link to this heading">#</a></h1>
<p>This chapter describes the rocRAND Python module API.</p>
<section id="api-index">
<h2>API index<a class="headerlink" href="#api-index" title="Link to this heading">#</a></h2>
<p>To search the API, see the API <a class="reference internal" href="../genindex.html"><span class="std std-ref">Index</span></a>.</p>
</section>
<section id="class-prng">
<h2>class PRNG<a class="headerlink" href="#class-prng" title="Link to this heading">#</a></h2>
<dl class="py class">
<dt class="sig sig-object py" id="rocrand.PRNG">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">rocrand.</span></span><span class="sig-name descname"><span class="pre">PRNG</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">rngtype</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">400</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">seed</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">stream</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">is_host</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.PRNG" title="Link to this definition">#</a></dt>
<dd><dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.PRNG.DEFAULT">
<span class="sig-name descname"><span class="pre">DEFAULT</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">400</span></em><a class="headerlink" href="#rocrand.PRNG.DEFAULT" title="Link to this definition">#</a></dt>
<dd><p>Default pseudo-random generator type, <a class="reference internal" href="#rocrand.PRNG.XORWOW" title="rocrand.PRNG.XORWOW"><code class="xref py py-const docutils literal notranslate"><span class="pre">XORWOW</span></code></a></p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.PRNG.LFSR113">
<span class="sig-name descname"><span class="pre">LFSR113</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">406</span></em><a class="headerlink" href="#rocrand.PRNG.LFSR113" title="Link to this definition">#</a></dt>
<dd><p>LFSR113 pseudo-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.PRNG.MRG31K3P">
<span class="sig-name descname"><span class="pre">MRG31K3P</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">405</span></em><a class="headerlink" href="#rocrand.PRNG.MRG31K3P" title="Link to this definition">#</a></dt>
<dd><p>MRG31k3p pseudo-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.PRNG.MRG32K3A">
<span class="sig-name descname"><span class="pre">MRG32K3A</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">402</span></em><a class="headerlink" href="#rocrand.PRNG.MRG32K3A" title="Link to this definition">#</a></dt>
<dd><p>MRG32k3a pseudo-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.PRNG.MT19937">
<span class="sig-name descname"><span class="pre">MT19937</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">407</span></em><a class="headerlink" href="#rocrand.PRNG.MT19937" title="Link to this definition">#</a></dt>
<dd><p>Mersenne Twister pseudo-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.PRNG.MTGP32">
<span class="sig-name descname"><span class="pre">MTGP32</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">403</span></em><a class="headerlink" href="#rocrand.PRNG.MTGP32" title="Link to this definition">#</a></dt>
<dd><p>Mersenne Twister MTGP32 pseudo-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.PRNG.PHILOX4_32_10">
<span class="sig-name descname"><span class="pre">PHILOX4_32_10</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">404</span></em><a class="headerlink" href="#rocrand.PRNG.PHILOX4_32_10" title="Link to this definition">#</a></dt>
<dd><p>PHILOX_4x32 (10 rounds) pseudo-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.PRNG.THREEFRY2_32_20">
<span class="sig-name descname"><span class="pre">THREEFRY2_32_20</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">408</span></em><a class="headerlink" href="#rocrand.PRNG.THREEFRY2_32_20" title="Link to this definition">#</a></dt>
<dd><p>THREEFRY2_32_20 pseudo-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.PRNG.THREEFRY2_64_20">
<span class="sig-name descname"><span class="pre">THREEFRY2_64_20</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">409</span></em><a class="headerlink" href="#rocrand.PRNG.THREEFRY2_64_20" title="Link to this definition">#</a></dt>
<dd><p>THREEFRY2_64_20 pseudo-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.PRNG.THREEFRY4_32_20">
<span class="sig-name descname"><span class="pre">THREEFRY4_32_20</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">410</span></em><a class="headerlink" href="#rocrand.PRNG.THREEFRY4_32_20" title="Link to this definition">#</a></dt>
<dd><p>THREEFRY4_32_20 pseudo-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.PRNG.THREEFRY4_64_20">
<span class="sig-name descname"><span class="pre">THREEFRY4_64_20</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">411</span></em><a class="headerlink" href="#rocrand.PRNG.THREEFRY4_64_20" title="Link to this definition">#</a></dt>
<dd><p>THREEFRY4_64_20 pseudo-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.PRNG.XORWOW">
<span class="sig-name descname"><span class="pre">XORWOW</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">401</span></em><a class="headerlink" href="#rocrand.PRNG.XORWOW" title="Link to this definition">#</a></dt>
<dd><p>XORWOW pseudo-random generator type</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="rocrand.PRNG.generate">
<span class="sig-name descname"><span class="pre">generate</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ary</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.PRNG.generate" title="Link to this definition">#</a></dt>
<dd><p>Generates uniformly distributed integers.</p>
<p>Generates <strong>size</strong> (if present) or <strong>ary.size</strong> uniformly distributed
integers and saves them to <strong>ary</strong>.</p>
<p>Supported <strong>dtype</strong> of <strong>ary</strong>: <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.uint32</span></code>, <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.int32</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ary</strong> – NumPy array (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>) or
HIP device-side array (<a class="reference internal" href="#rocrand.DeviceNDArray" title="rocrand.DeviceNDArray"><code class="xref py py-class docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a>)</p></li>
<li><p><strong>size</strong> – Number of samples to generate, default to <strong>ary.size</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="rocrand.PRNG.lognormal">
<span class="sig-name descname"><span class="pre">lognormal</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ary</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">mean</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">stddev</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.PRNG.lognormal" title="Link to this definition">#</a></dt>
<dd><p>Generates log-normally distributed floats.</p>
<p>Generates <strong>size</strong> (if present) or <strong>ary.size</strong> log-normally distributed
floats and saves them to <strong>ary</strong>.</p>
<p>Supported <strong>dtype</strong> of <strong>ary</strong>: <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.float32</span></code>, <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.float64</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ary</strong> – NumPy array (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>) or
HIP device-side array (<a class="reference internal" href="#rocrand.DeviceNDArray" title="rocrand.DeviceNDArray"><code class="xref py py-class docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a>)</p></li>
<li><p><strong>mean</strong> – Mean value of log normal distribution</p></li>
<li><p><strong>stddev</strong> – Standard deviation value of log normal distribution</p></li>
<li><p><strong>size</strong> – Number of samples to generate, default to <strong>ary.size</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="rocrand.PRNG.normal">
<span class="sig-name descname"><span class="pre">normal</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ary</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">mean</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">stddev</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.PRNG.normal" title="Link to this definition">#</a></dt>
<dd><p>Generates normally distributed floats.</p>
<p>Generates <strong>size</strong> (if present) or <strong>ary.size</strong> normally distributed
floats and saves them to <strong>ary</strong>.</p>
<p>Supported <strong>dtype</strong> of <strong>ary</strong>: <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.float32</span></code>, <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.float64</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ary</strong> – NumPy array (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>) or
HIP device-side array (<a class="reference internal" href="#rocrand.DeviceNDArray" title="rocrand.DeviceNDArray"><code class="xref py py-class docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a>)</p></li>
<li><p><strong>mean</strong> – Mean value of normal distribution</p></li>
<li><p><strong>stddev</strong> – Standard deviation value of normal distribution</p></li>
<li><p><strong>size</strong> – Number of samples to generate, default to <strong>ary.size</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py property">
<dt class="sig sig-object py" id="rocrand.PRNG.offset">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">offset</span></span><a class="headerlink" href="#rocrand.PRNG.offset" title="Link to this definition">#</a></dt>
<dd><p>Mutable attribute of the offset of random numbers sequence.</p>
<p>Setting this attribute resets the sequence.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="rocrand.PRNG.poisson">
<span class="sig-name descname"><span class="pre">poisson</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ary</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">lmbd</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.PRNG.poisson" title="Link to this definition">#</a></dt>
<dd><p>Generates Poisson-distributed integers.</p>
<p>Generates <strong>size</strong> (if present) or <strong>ary.size</strong> Poisson-distributed
integers and saves them to <strong>ary</strong>.</p>
<p>Supported <strong>dtype</strong> of <strong>ary</strong>: <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.uint32</span></code>, <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.int32</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ary</strong> – NumPy array (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>) or
HIP device-side array (<a class="reference internal" href="#rocrand.DeviceNDArray" title="rocrand.DeviceNDArray"><code class="xref py py-class docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a>)</p></li>
<li><p><strong>lmbd</strong> – lambda for the Poisson distribution</p></li>
<li><p><strong>size</strong> – Number of samples to generate, default to <strong>ary.size</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py property">
<dt class="sig sig-object py" id="rocrand.PRNG.seed">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">seed</span></span><a class="headerlink" href="#rocrand.PRNG.seed" title="Link to this definition">#</a></dt>
<dd><p>Mutable attribute of the seed of random numbers sequence.</p>
<p>Setting this attribute resets the sequence.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="rocrand.PRNG.uniform">
<span class="sig-name descname"><span class="pre">uniform</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ary</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.PRNG.uniform" title="Link to this definition">#</a></dt>
<dd><p>Generates uniformly distributed floats.</p>
<p>Generates <strong>size</strong> (if present) or <strong>ary.size</strong> uniformly distributed
floats and saves them to <strong>ary</strong>.</p>
<p>Supported <strong>dtype</strong> of <strong>ary</strong>: <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.float32</span></code>, <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.float64</span></code>.</p>
<p>Generated numbers are between 0.0 and 1.0, excluding 0.0 and
including 1.0.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ary</strong> – NumPy array (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>) or
HIP device-side array (<a class="reference internal" href="#rocrand.DeviceNDArray" title="rocrand.DeviceNDArray"><code class="xref py py-class docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a>)</p></li>
<li><p><strong>size</strong> – Number of samples to generate, default to <strong>ary.size</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

</dd></dl>

</section>
<section id="class-qrng">
<h2>class QRNG<a class="headerlink" href="#class-qrng" title="Link to this heading">#</a></h2>
<dl class="py class">
<dt class="sig sig-object py" id="rocrand.QRNG">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">rocrand.</span></span><span class="sig-name descname"><span class="pre">QRNG</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">rngtype</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">500</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">ndim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">stream</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">is_host</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.QRNG" title="Link to this definition">#</a></dt>
<dd><dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.QRNG.DEFAULT">
<span class="sig-name descname"><span class="pre">DEFAULT</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">500</span></em><a class="headerlink" href="#rocrand.QRNG.DEFAULT" title="Link to this definition">#</a></dt>
<dd><p>Default quasi-random generator type, <a class="reference internal" href="#rocrand.QRNG.SOBOL32" title="rocrand.QRNG.SOBOL32"><code class="xref py py-const docutils literal notranslate"><span class="pre">SOBOL32</span></code></a></p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.QRNG.SCRAMBLED_SOBOL32">
<span class="sig-name descname"><span class="pre">SCRAMBLED_SOBOL32</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">502</span></em><a class="headerlink" href="#rocrand.QRNG.SCRAMBLED_SOBOL32" title="Link to this definition">#</a></dt>
<dd><p>Scrambled Sobol32 quasi-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.QRNG.SCRAMBLED_SOBOL64">
<span class="sig-name descname"><span class="pre">SCRAMBLED_SOBOL64</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">505</span></em><a class="headerlink" href="#rocrand.QRNG.SCRAMBLED_SOBOL64" title="Link to this definition">#</a></dt>
<dd><p>Scrambled Sobol64 quasi-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.QRNG.SOBOL32">
<span class="sig-name descname"><span class="pre">SOBOL32</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">501</span></em><a class="headerlink" href="#rocrand.QRNG.SOBOL32" title="Link to this definition">#</a></dt>
<dd><p>Sobol32 quasi-random generator type</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="rocrand.QRNG.SOBOL64">
<span class="sig-name descname"><span class="pre">SOBOL64</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">504</span></em><a class="headerlink" href="#rocrand.QRNG.SOBOL64" title="Link to this definition">#</a></dt>
<dd><p>Sobol64 quasi-random generator type</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="rocrand.QRNG.generate">
<span class="sig-name descname"><span class="pre">generate</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ary</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.QRNG.generate" title="Link to this definition">#</a></dt>
<dd><p>Generates uniformly distributed integers.</p>
<p>Generates <strong>size</strong> (if present) or <strong>ary.size</strong> uniformly distributed
integers and saves them to <strong>ary</strong>.</p>
<p>Supported <strong>dtype</strong> of <strong>ary</strong>: <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.uint32</span></code>, <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.int32</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ary</strong> – NumPy array (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>) or
HIP device-side array (<a class="reference internal" href="#rocrand.DeviceNDArray" title="rocrand.DeviceNDArray"><code class="xref py py-class docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a>)</p></li>
<li><p><strong>size</strong> – Number of samples to generate, default to <strong>ary.size</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="rocrand.QRNG.lognormal">
<span class="sig-name descname"><span class="pre">lognormal</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ary</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">mean</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">stddev</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.QRNG.lognormal" title="Link to this definition">#</a></dt>
<dd><p>Generates log-normally distributed floats.</p>
<p>Generates <strong>size</strong> (if present) or <strong>ary.size</strong> log-normally distributed
floats and saves them to <strong>ary</strong>.</p>
<p>Supported <strong>dtype</strong> of <strong>ary</strong>: <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.float32</span></code>, <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.float64</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ary</strong> – NumPy array (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>) or
HIP device-side array (<a class="reference internal" href="#rocrand.DeviceNDArray" title="rocrand.DeviceNDArray"><code class="xref py py-class docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a>)</p></li>
<li><p><strong>mean</strong> – Mean value of log normal distribution</p></li>
<li><p><strong>stddev</strong> – Standard deviation value of log normal distribution</p></li>
<li><p><strong>size</strong> – Number of samples to generate, default to <strong>ary.size</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py property">
<dt class="sig sig-object py" id="rocrand.QRNG.ndim">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">ndim</span></span><a class="headerlink" href="#rocrand.QRNG.ndim" title="Link to this definition">#</a></dt>
<dd><p>Mutable attribute of the number of dimensions of random numbers sequence.</p>
<p>Supported values are 1 to 20000.
Setting this attribute resets the sequence.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="rocrand.QRNG.normal">
<span class="sig-name descname"><span class="pre">normal</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ary</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">mean</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">stddev</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.QRNG.normal" title="Link to this definition">#</a></dt>
<dd><p>Generates normally distributed floats.</p>
<p>Generates <strong>size</strong> (if present) or <strong>ary.size</strong> normally distributed
floats and saves them to <strong>ary</strong>.</p>
<p>Supported <strong>dtype</strong> of <strong>ary</strong>: <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.float32</span></code>, <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.float64</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ary</strong> – NumPy array (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>) or
HIP device-side array (<a class="reference internal" href="#rocrand.DeviceNDArray" title="rocrand.DeviceNDArray"><code class="xref py py-class docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a>)</p></li>
<li><p><strong>mean</strong> – Mean value of normal distribution</p></li>
<li><p><strong>stddev</strong> – Standard deviation value of normal distribution</p></li>
<li><p><strong>size</strong> – Number of samples to generate, default to <strong>ary.size</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py property">
<dt class="sig sig-object py" id="rocrand.QRNG.offset">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">offset</span></span><a class="headerlink" href="#rocrand.QRNG.offset" title="Link to this definition">#</a></dt>
<dd><p>Mutable attribute of the offset of random numbers sequence.</p>
<p>Setting this attribute resets the sequence.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="rocrand.QRNG.poisson">
<span class="sig-name descname"><span class="pre">poisson</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ary</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">lmbd</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.QRNG.poisson" title="Link to this definition">#</a></dt>
<dd><p>Generates Poisson-distributed integers.</p>
<p>Generates <strong>size</strong> (if present) or <strong>ary.size</strong> Poisson-distributed
integers and saves them to <strong>ary</strong>.</p>
<p>Supported <strong>dtype</strong> of <strong>ary</strong>: <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.uint32</span></code>, <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.int32</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ary</strong> – NumPy array (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>) or
HIP device-side array (<a class="reference internal" href="#rocrand.DeviceNDArray" title="rocrand.DeviceNDArray"><code class="xref py py-class docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a>)</p></li>
<li><p><strong>lmbd</strong> – lambda for the Poisson distribution</p></li>
<li><p><strong>size</strong> – Number of samples to generate, default to <strong>ary.size</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="rocrand.QRNG.uniform">
<span class="sig-name descname"><span class="pre">uniform</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ary</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.QRNG.uniform" title="Link to this definition">#</a></dt>
<dd><p>Generates uniformly distributed floats.</p>
<p>Generates <strong>size</strong> (if present) or <strong>ary.size</strong> uniformly distributed
floats and saves them to <strong>ary</strong>.</p>
<p>Supported <strong>dtype</strong> of <strong>ary</strong>: <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.float32</span></code>, <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.float64</span></code>.</p>
<p>Generated numbers are between 0.0 and 1.0, excluding 0.0 and
including 1.0.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ary</strong> – NumPy array (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>) or
HIP device-side array (<a class="reference internal" href="#rocrand.DeviceNDArray" title="rocrand.DeviceNDArray"><code class="xref py py-class docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a>)</p></li>
<li><p><strong>size</strong> – Number of samples to generate, default to <strong>ary.size</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

</dd></dl>

</section>
<section id="exceptions">
<h2>Exceptions<a class="headerlink" href="#exceptions" title="Link to this heading">#</a></h2>
<dl class="py exception">
<dt class="sig sig-object py" id="rocrand.RocRandError">
<em class="property"><span class="pre">exception</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">rocrand.</span></span><span class="sig-name descname"><span class="pre">RocRandError</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">value</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.RocRandError" title="Link to this definition">#</a></dt>
<dd><p>Run-time rocRAND error.</p>
</dd></dl>

<dl class="py exception">
<dt class="sig sig-object py" id="rocrand.HipError">
<em class="property"><span class="pre">exception</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">rocrand.</span></span><span class="sig-name descname"><span class="pre">HipError</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">value</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.HipError" title="Link to this definition">#</a></dt>
<dd><p>Run-time HIP error.</p>
</dd></dl>

</section>
<section id="utilities">
<h2>Utilities<a class="headerlink" href="#utilities" title="Link to this heading">#</a></h2>
<dl class="py class">
<dt class="sig sig-object py" id="rocrand.DeviceNDArray">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">rocrand.</span></span><span class="sig-name descname"><span class="pre">DeviceNDArray</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">shape</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">dtype</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">data</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.DeviceNDArray" title="Link to this definition">#</a></dt>
<dd><dl class="py method">
<dt class="sig sig-object py" id="rocrand.DeviceNDArray.copy_to_host">
<span class="sig-name descname"><span class="pre">copy_to_host</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ary</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.DeviceNDArray.copy_to_host" title="Link to this definition">#</a></dt>
<dd><p>Copy from data device memory to host memory.</p>
<p>If <strong>ary</strong> is passed then <strong>ary</strong> must have the same <strong>dtype</strong>
and greater or equal <strong>size</strong> as <strong>self</strong> has.</p>
<p>If <strong>ary</strong> is not passed then a new <code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code> will be
created.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>ary</strong> – NumPy array (<code class="xref py py-class docutils literal notranslate"><span class="pre">numpy.ndarray</span></code>)</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>a new array or <strong>ary</strong></p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="rocrand.empty">
<span class="sig-prename descclassname"><span class="pre">rocrand.</span></span><span class="sig-name descname"><span class="pre">empty</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">shape</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">dtype</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.empty" title="Link to this definition">#</a></dt>
<dd><p>Create a new device-side array of given shape and type, without initializing entries.</p>
<p>This function is a limited version of <code class="xref py py-func docutils literal notranslate"><span class="pre">numpy.empty()</span></code> for device-side
arrays.</p>
<p>Example:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">rocrand</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="n">gen</span> <span class="o">=</span> <span class="n">rocrand</span><span class="o">.</span><span class="n">QRNG</span><span class="p">(</span><span class="n">ndim</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>
<span class="n">d_a</span> <span class="o">=</span> <span class="n">rocrand</span><span class="o">.</span><span class="n">empty</span><span class="p">((</span><span class="mi">5</span><span class="p">,</span> <span class="mi">10000</span><span class="p">),</span> <span class="n">dtype</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">float32</span><span class="p">)</span>
<span class="n">gen</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="n">d_a</span><span class="p">)</span>
<span class="n">a</span> <span class="o">=</span> <span class="n">d_a</span><span class="o">.</span><span class="n">copy_to_host</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
</pre></div>
</div>
<p>See <a class="reference internal" href="#rocrand.DeviceNDArray" title="rocrand.DeviceNDArray"><code class="xref py py-class docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>shape</strong> (<a class="reference external" href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><em>int</em></a><em> or </em><a class="reference external" href="https://docs.python.org/3/library/stdtypes.html#tuple" title="(in Python v3.14)"><em>tuple</em></a><em> of </em><a class="reference external" href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><em>int</em></a>) – Shape of the array (see <code class="xref py py-attr docutils literal notranslate"><span class="pre">numpy.ndarray.shape</span></code>)</p></li>
<li><p><strong>dtype</strong> – Type of the array (see <code class="xref py py-attr docutils literal notranslate"><span class="pre">numpy.ndarray.dtype</span></code>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt class="sig sig-object py" id="rocrand.get_version">
<span class="sig-prename descclassname"><span class="pre">rocrand.</span></span><span class="sig-name descname"><span class="pre">get_version</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#rocrand.get_version" title="Link to this definition">#</a></dt>
<dd><p>Returns the version number of the rocRAND library.</p>
</dd></dl>

<p>To search the API, see the <a class="reference internal" href="../genindex.html"><span class="std std-ref">Index</span></a> for all rocRAND APIs.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="cpp-api.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">C/C++ API reference</p>
      </div>
    </a>
    <a class="right-next"
       href="../fortran-api-reference.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Fortran API reference</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#api-index">API index</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#class-prng">class PRNG</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG"><code class="docutils literal notranslate"><span class="pre">PRNG</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.DEFAULT"><code class="docutils literal notranslate"><span class="pre">PRNG.DEFAULT</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.LFSR113"><code class="docutils literal notranslate"><span class="pre">PRNG.LFSR113</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.MRG31K3P"><code class="docutils literal notranslate"><span class="pre">PRNG.MRG31K3P</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.MRG32K3A"><code class="docutils literal notranslate"><span class="pre">PRNG.MRG32K3A</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.MT19937"><code class="docutils literal notranslate"><span class="pre">PRNG.MT19937</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.MTGP32"><code class="docutils literal notranslate"><span class="pre">PRNG.MTGP32</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.PHILOX4_32_10"><code class="docutils literal notranslate"><span class="pre">PRNG.PHILOX4_32_10</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.THREEFRY2_32_20"><code class="docutils literal notranslate"><span class="pre">PRNG.THREEFRY2_32_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.THREEFRY2_64_20"><code class="docutils literal notranslate"><span class="pre">PRNG.THREEFRY2_64_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.THREEFRY4_32_20"><code class="docutils literal notranslate"><span class="pre">PRNG.THREEFRY4_32_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.THREEFRY4_64_20"><code class="docutils literal notranslate"><span class="pre">PRNG.THREEFRY4_64_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.XORWOW"><code class="docutils literal notranslate"><span class="pre">PRNG.XORWOW</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.generate"><code class="docutils literal notranslate"><span class="pre">PRNG.generate()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.lognormal"><code class="docutils literal notranslate"><span class="pre">PRNG.lognormal()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.normal"><code class="docutils literal notranslate"><span class="pre">PRNG.normal()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.offset"><code class="docutils literal notranslate"><span class="pre">PRNG.offset</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.poisson"><code class="docutils literal notranslate"><span class="pre">PRNG.poisson()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.seed"><code class="docutils literal notranslate"><span class="pre">PRNG.seed</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.PRNG.uniform"><code class="docutils literal notranslate"><span class="pre">PRNG.uniform()</span></code></a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#class-qrng">class QRNG</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG"><code class="docutils literal notranslate"><span class="pre">QRNG</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.DEFAULT"><code class="docutils literal notranslate"><span class="pre">QRNG.DEFAULT</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.SCRAMBLED_SOBOL32"><code class="docutils literal notranslate"><span class="pre">QRNG.SCRAMBLED_SOBOL32</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.SCRAMBLED_SOBOL64"><code class="docutils literal notranslate"><span class="pre">QRNG.SCRAMBLED_SOBOL64</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.SOBOL32"><code class="docutils literal notranslate"><span class="pre">QRNG.SOBOL32</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.SOBOL64"><code class="docutils literal notranslate"><span class="pre">QRNG.SOBOL64</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.generate"><code class="docutils literal notranslate"><span class="pre">QRNG.generate()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.lognormal"><code class="docutils literal notranslate"><span class="pre">QRNG.lognormal()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.ndim"><code class="docutils literal notranslate"><span class="pre">QRNG.ndim</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.normal"><code class="docutils literal notranslate"><span class="pre">QRNG.normal()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.offset"><code class="docutils literal notranslate"><span class="pre">QRNG.offset</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.poisson"><code class="docutils literal notranslate"><span class="pre">QRNG.poisson()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.QRNG.uniform"><code class="docutils literal notranslate"><span class="pre">QRNG.uniform()</span></code></a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#exceptions">Exceptions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.RocRandError"><code class="docutils literal notranslate"><span class="pre">RocRandError</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.HipError"><code class="docutils literal notranslate"><span class="pre">HipError</span></code></a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#utilities">Utilities</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.DeviceNDArray"><code class="docutils literal notranslate"><span class="pre">DeviceNDArray</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.DeviceNDArray.copy_to_host"><code class="docutils literal notranslate"><span class="pre">DeviceNDArray.copy_to_host()</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.empty"><code class="docutils literal notranslate"><span class="pre">empty()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand.get_version"><code class="docutils literal notranslate"><span class="pre">get_version()</span></code></a></li>
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
