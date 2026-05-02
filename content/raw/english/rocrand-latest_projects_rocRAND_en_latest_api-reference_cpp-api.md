---
title: "C/C++ API reference &#8212; rocRAND 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocRAND/en/latest/api-reference/cpp-api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:09:08.832039+00:00
content_hash: "8a72b8f49e6deaca"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="rocRAND C/C++ API reference" name="description" />
<meta content="rocRAND, ROCm, API, documentation, C, C++" name="keywords" />

    <title>C/C++ API reference &#8212; rocRAND 4.2.0 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'api-reference/cpp-api';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Python API reference" href="python-api.html" />
    <link rel="prev" title="rocRAND data type support" href="data-type-support.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocrand" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/api-reference/cpp-api.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1 current active"><a class="current reference internal" href="#">C/C++ API reference</a></li>
<li class="toctree-l1"><a class="reference internal" href="python-api.html">Python API reference</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">C/C++ API reference</span></li>
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
    <h1>C/C++ API reference</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#api-index">API index</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#device-functions">Device functions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP27rocrand_state_philox4x32_10K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417rocrand_discrete4P27rocrand_state_philox4x32_10K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP22rocrand_state_mrg31k3pK29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP22rocrand_state_mrg32k3aK29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP20rocrand_state_xorwowK29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP20rocrand_state_mtgp32K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP21rocrand_state_sobol32K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP31rocrand_state_scrambled_sobol32K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP21rocrand_state_sobol64K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP31rocrand_state_scrambled_sobol64K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP21rocrand_state_lfsr113K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP29rocrand_state_threefry2x32_20K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP29rocrand_state_threefry2x64_20K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP29rocrand_state_threefry4x32_20K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP29rocrand_state_threefry4x64_20K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initK5uint4KjP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initK5uint4KjKyP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421skipahead_subsequencejP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">skipahead_subsequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418skipahead_sequencejP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">skipahead_sequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP27rocrand_state_philox4x32_10ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P27rocrand_state_philox4x32_10ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal4P27rocrand_state_philox4x32_10ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP27rocrand_state_philox4x32_10dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P27rocrand_state_philox4x32_10dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double4P27rocrand_state_philox4x32_10dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP22rocrand_state_mrg31k3pff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P22rocrand_state_mrg31k3pff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP22rocrand_state_mrg31k3pdd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P22rocrand_state_mrg31k3pdd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP22rocrand_state_mrg32k3aff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P22rocrand_state_mrg32k3aff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP22rocrand_state_mrg32k3add"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P22rocrand_state_mrg32k3add"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP20rocrand_state_xorwowff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P20rocrand_state_xorwowff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP20rocrand_state_xorwowdd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P20rocrand_state_xorwowdd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP20rocrand_state_mtgp32ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P20rocrand_state_mtgp32ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP20rocrand_state_mtgp32dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P20rocrand_state_mtgp32dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP21rocrand_state_sobol32ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP21rocrand_state_sobol32dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP31rocrand_state_scrambled_sobol32ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP31rocrand_state_scrambled_sobol32dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP21rocrand_state_sobol64ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP21rocrand_state_sobol64dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP31rocrand_state_scrambled_sobol64ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP31rocrand_state_scrambled_sobol64dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP21rocrand_state_lfsr113ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P21rocrand_state_lfsr113ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP21rocrand_state_lfsr113dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P21rocrand_state_lfsr113dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP29rocrand_state_threefry2x32_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P29rocrand_state_threefry2x32_20ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry2x32_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry2x32_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP29rocrand_state_threefry2x64_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P29rocrand_state_threefry2x64_20ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry2x64_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry2x64_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP29rocrand_state_threefry4x32_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P29rocrand_state_threefry4x32_20ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry4x32_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry4x32_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP29rocrand_state_threefry4x64_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P29rocrand_state_threefry4x64_20ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry4x64_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry4x64_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initKyKyKyP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421skipahead_subsequenceyP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">skipahead_subsequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418skipahead_sequenceyP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">skipahead_sequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initKyKyKyP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421skipahead_subsequenceyP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">skipahead_subsequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418skipahead_sequenceyP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">skipahead_sequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_make_state_mtgp32P20rocrand_state_mtgp32A_18mtgp32_fast_paramsiy"><code class="docutils literal notranslate"><span class="pre">rocrand_make_state_mtgp32()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_make_constantA_K18mtgp32_fast_paramsP13mtgp32_params"><code class="docutils literal notranslate"><span class="pre">rocrand_make_constant()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_mtgp32_block_copyP20rocrand_state_mtgp32P20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_mtgp32_block_copy()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_mtgp32_set_paramsP20rocrand_state_mtgp32P13mtgp32_params"><code class="docutils literal notranslate"><span class="pre">rocrand_mtgp32_set_params()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal4P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_normal4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double4P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP29rocrand_state_threefry2x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P29rocrand_state_threefry2x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP29rocrand_state_threefry2x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P29rocrand_state_threefry2x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP29rocrand_state_threefry2x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P29rocrand_state_threefry2x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP29rocrand_state_threefry2x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P29rocrand_state_threefry2x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP29rocrand_state_threefry4x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P29rocrand_state_threefry4x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP29rocrand_state_threefry4x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P29rocrand_state_threefry4x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP29rocrand_state_threefry4x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P29rocrand_state_threefry4x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP29rocrand_state_threefry4x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P29rocrand_state_threefry4x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initKyKyKyP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv48rocrand4P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421skipahead_subsequenceyP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">skipahead_subsequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418skipahead_sequenceyP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">skipahead_sequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP27rocrand_state_philox4x32_10d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_poisson4P27rocrand_state_philox4x32_10d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP22rocrand_state_mrg31k3pd"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP22rocrand_state_mrg32k3ad"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP20rocrand_state_xorwowd"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP20rocrand_state_mtgp32d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP21rocrand_state_sobol32d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP31rocrand_state_scrambled_sobol32d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP21rocrand_state_sobol64d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP31rocrand_state_scrambled_sobol64d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP21rocrand_state_lfsr113d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP29rocrand_state_threefry2x32_20d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP29rocrand_state_threefry2x64_20d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP29rocrand_state_threefry4x32_20d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP29rocrand_state_threefry4x64_20d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initPKjKjKjP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initPKyKyKjP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initPKjKjP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initPKyKjP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_uniform2P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_uniform4P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423rocrand_uniform_double2P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423rocrand_uniform_double4P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP29rocrand_state_threefry2x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry2x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP29rocrand_state_threefry2x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry2x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP29rocrand_state_threefry4x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry4x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP29rocrand_state_threefry4x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry4x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initKyKyKyP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421skipahead_subsequenceyP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">skipahead_subsequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418skipahead_sequenceyP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">skipahead_sequence()</span></code></a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#c-host-api">C host API</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_status"><code class="docutils literal notranslate"><span class="pre">rocrand_status</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status22ROCRAND_STATUS_SUCCESSE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_SUCCESS</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status31ROCRAND_STATUS_VERSION_MISMATCHE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_VERSION_MISMATCH</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status26ROCRAND_STATUS_NOT_CREATEDE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_NOT_CREATED</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status32ROCRAND_STATUS_ALLOCATION_FAILEDE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_ALLOCATION_FAILED</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status25ROCRAND_STATUS_TYPE_ERRORE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_TYPE_ERROR</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status27ROCRAND_STATUS_OUT_OF_RANGEE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_OUT_OF_RANGE</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status34ROCRAND_STATUS_LENGTH_NOT_MULTIPLEE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_LENGTH_NOT_MULTIPLE</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status40ROCRAND_STATUS_DOUBLE_PRECISION_REQUIREDE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_DOUBLE_PRECISION_REQUIRED</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status29ROCRAND_STATUS_LAUNCH_FAILUREE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_LAUNCH_FAILURE</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status29ROCRAND_STATUS_INTERNAL_ERRORE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_INTERNAL_ERROR</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_rng_type"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_DEFAULTE"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_DEFAULT</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_PSEUDO_XORWOWE"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_XORWOW</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type27ROCRAND_RNG_PSEUDO_MRG32K3AE"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_MRG32K3A</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_PSEUDO_MTGP32E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_MTGP32</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type32ROCRAND_RNG_PSEUDO_PHILOX4_32_10E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_PHILOX4_32_10</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type27ROCRAND_RNG_PSEUDO_MRG31K3PE"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_MRG31K3P</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_LFSR113E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_LFSR113</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_MT19937E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_MT19937</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY2_32_20E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_THREEFRY2_32_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY2_64_20E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_THREEFRY2_64_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY4_32_20E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_THREEFRY4_32_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY4_64_20E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_THREEFRY4_64_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_QUASI_DEFAULTE"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_QUASI_DEFAULT</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_QUASI_SOBOL32E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_QUASI_SOBOL32</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type35ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL32E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL32</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_QUASI_SOBOL64E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_QUASI_SOBOL64</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type35ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL64E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL64</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_ordering"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_ordering28ROCRAND_ORDERING_PSEUDO_BESTE"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering::ROCRAND_ORDERING_PSEUDO_BEST</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_ordering31ROCRAND_ORDERING_PSEUDO_DEFAULTE"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering::ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_ordering30ROCRAND_ORDERING_PSEUDO_SEEDEDE"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering::ROCRAND_ORDERING_PSEUDO_SEEDED</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_ordering30ROCRAND_ORDERING_PSEUDO_LEGACYE"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering::ROCRAND_ORDERING_PSEUDO_LEGACY</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_ordering31ROCRAND_ORDERING_PSEUDO_DYNAMICE"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering::ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_ordering30ROCRAND_ORDERING_QUASI_DEFAULTE"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering::ROCRAND_ORDERING_QUASI_DEFAULT</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428rocrand_direction_vector_set"><code class="docutils literal notranslate"><span class="pre">rocrand_direction_vector_set</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N28rocrand_direction_vector_set36ROCRAND_DIRECTION_VECTORS_32_JOEKUO6E"><code class="docutils literal notranslate"><span class="pre">rocrand_direction_vector_set::ROCRAND_DIRECTION_VECTORS_32_JOEKUO6</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N28rocrand_direction_vector_set46ROCRAND_SCRAMBLED_DIRECTION_VECTORS_32_JOEKUO6E"><code class="docutils literal notranslate"><span class="pre">rocrand_direction_vector_set::ROCRAND_SCRAMBLED_DIRECTION_VECTORS_32_JOEKUO6</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N28rocrand_direction_vector_set36ROCRAND_DIRECTION_VECTORS_64_JOEKUO6E"><code class="docutils literal notranslate"><span class="pre">rocrand_direction_vector_set::ROCRAND_DIRECTION_VECTORS_64_JOEKUO6</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N28rocrand_direction_vector_set46ROCRAND_SCRAMBLED_DIRECTION_VECTORS_64_JOEKUO6E"><code class="docutils literal notranslate"><span class="pre">rocrand_direction_vector_set::ROCRAND_SCRAMBLED_DIRECTION_VECTORS_64_JOEKUO6</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424rocrand_create_generatorP17rocrand_generator16rocrand_rng_type"><code class="docutils literal notranslate"><span class="pre">rocrand_create_generator()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429rocrand_create_generator_hostP17rocrand_generator16rocrand_rng_type"><code class="docutils literal notranslate"><span class="pre">rocrand_create_generator_host()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv438rocrand_create_generator_host_blockingP17rocrand_generator16rocrand_rng_type"><code class="docutils literal notranslate"><span class="pre">rocrand_create_generator_host_blocking()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_destroy_generator17rocrand_generator"><code class="docutils literal notranslate"><span class="pre">rocrand_destroy_generator()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_generate17rocrand_generatorPj6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_generate_long_long17rocrand_generatorPy6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_long_long()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_generate_char17rocrand_generatorPh6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_char()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_generate_short17rocrand_generatorPt6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_short()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424rocrand_generate_uniform17rocrand_generatorPf6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431rocrand_generate_uniform_double17rocrand_generatorPd6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429rocrand_generate_uniform_half17rocrand_generatorP4half6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_uniform_half()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423rocrand_generate_normal17rocrand_generatorPf6size_tff"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430rocrand_generate_normal_double17rocrand_generatorPd6size_tdd"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428rocrand_generate_normal_half17rocrand_generatorP4half6size_t4half4half"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_normal_half()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427rocrand_generate_log_normal17rocrand_generatorPf6size_tff"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv434rocrand_generate_log_normal_double17rocrand_generatorPd6size_tdd"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv432rocrand_generate_log_normal_half17rocrand_generatorP4half6size_t4half4half"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_log_normal_half()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424rocrand_generate_poisson17rocrand_generatorPj6size_td"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428rocrand_initialize_generator17rocrand_generator"><code class="docutils literal notranslate"><span class="pre">rocrand_initialize_generator()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_set_stream17rocrand_generator11hipStream_t"><code class="docutils literal notranslate"><span class="pre">rocrand_set_stream()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_set_seed17rocrand_generatory"><code class="docutils literal notranslate"><span class="pre">rocrand_set_seed()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_set_seed_uint417rocrand_generator5uint4"><code class="docutils literal notranslate"><span class="pre">rocrand_set_seed_uint4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_set_offset17rocrand_generatory"><code class="docutils literal notranslate"><span class="pre">rocrand_set_offset()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420rocrand_set_ordering17rocrand_generator16rocrand_ordering"><code class="docutils literal notranslate"><span class="pre">rocrand_set_ordering()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv445rocrand_set_quasi_random_generator_dimensions17rocrand_generatorj"><code class="docutils literal notranslate"><span class="pre">rocrand_set_quasi_random_generator_dimensions()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_get_versionPi"><code class="docutils literal notranslate"><span class="pre">rocrand_get_version()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv435rocrand_create_poisson_distributiondP29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_create_poisson_distribution()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv436rocrand_create_discrete_distributionPKdjjP29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_create_discrete_distribution()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv437rocrand_destroy_discrete_distribution29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_destroy_discrete_distribution()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431rocrand_get_direction_vectors32PPKj28rocrand_direction_vector_set"><code class="docutils literal notranslate"><span class="pre">rocrand_get_direction_vectors32()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431rocrand_get_direction_vectors64PPKy28rocrand_direction_vector_set"><code class="docutils literal notranslate"><span class="pre">rocrand_get_direction_vectors64()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv432rocrand_get_scramble_constants32PPKj"><code class="docutils literal notranslate"><span class="pre">rocrand_get_scramble_constants32()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv432rocrand_get_scramble_constants64PPKy"><code class="docutils literal notranslate"><span class="pre">rocrand_get_scramble_constants64()</span></code></a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#c-host-api-wrapper">C++ host API wrapper</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413philox4x32_10"><code class="docutils literal notranslate"><span class="pre">philox4x32_10</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv46xorwow"><code class="docutils literal notranslate"><span class="pre">xorwow</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv48mrg31k3p"><code class="docutils literal notranslate"><span class="pre">mrg31k3p</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv48mrg32k3a"><code class="docutils literal notranslate"><span class="pre">mrg32k3a</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv46mtgp32"><code class="docutils literal notranslate"><span class="pre">mtgp32</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47lfsr113"><code class="docutils literal notranslate"><span class="pre">lfsr113</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47mt19937"><code class="docutils literal notranslate"><span class="pre">mt19937</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412threefry2x32"><code class="docutils literal notranslate"><span class="pre">threefry2x32</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412threefry2x64"><code class="docutils literal notranslate"><span class="pre">threefry2x64</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412threefry4x32"><code class="docutils literal notranslate"><span class="pre">threefry4x32</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412threefry4x64"><code class="docutils literal notranslate"><span class="pre">threefry4x64</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47sobol32"><code class="docutils literal notranslate"><span class="pre">sobol32</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">scrambled_sobol32</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47sobol64"><code class="docutils literal notranslate"><span class="pre">sobol64</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">scrambled_sobol64</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421default_random_engine"><code class="docutils literal notranslate"><span class="pre">default_random_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413random_device"><code class="docutils literal notranslate"><span class="pre">random_device</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47versionv"><code class="docutils literal notranslate"><span class="pre">version()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N11rocrand_cpp5errorE"><code class="docutils literal notranslate"><span class="pre">error</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0EN11rocrand_cpp24uniform_int_distributionE"><code class="docutils literal notranslate"><span class="pre">uniform_int_distribution</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0EN11rocrand_cpp25uniform_real_distributionE"><code class="docutils literal notranslate"><span class="pre">uniform_real_distribution</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0EN11rocrand_cpp19normal_distributionE"><code class="docutils literal notranslate"><span class="pre">normal_distribution</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0EN11rocrand_cpp22lognormal_distributionE"><code class="docutils literal notranslate"><span class="pre">lognormal_distribution</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0EN11rocrand_cpp20poisson_distributionE"><code class="docutils literal notranslate"><span class="pre">poisson_distribution</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp20philox4x32_10_engineE"><code class="docutils literal notranslate"><span class="pre">philox4x32_10_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp13xorwow_engineE"><code class="docutils literal notranslate"><span class="pre">xorwow_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp15mrg31k3p_engineE"><code class="docutils literal notranslate"><span class="pre">mrg31k3p_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp15mrg32k3a_engineE"><code class="docutils literal notranslate"><span class="pre">mrg32k3a_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp13mtgp32_engineE"><code class="docutils literal notranslate"><span class="pre">mtgp32_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_j_j_j_jEN11rocrand_cpp14lfsr113_engineE"><code class="docutils literal notranslate"><span class="pre">lfsr113_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp14mt19937_engineE"><code class="docutils literal notranslate"><span class="pre">mt19937_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_jEN11rocrand_cpp14sobol32_engineE"><code class="docutils literal notranslate"><span class="pre">sobol32_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_jEN11rocrand_cpp24scrambled_sobol32_engineE"><code class="docutils literal notranslate"><span class="pre">scrambled_sobol32_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_jEN11rocrand_cpp14sobol64_engineE"><code class="docutils literal notranslate"><span class="pre">sobol64_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_jEN11rocrand_cpp24scrambled_sobol64_engineE"><code class="docutils literal notranslate"><span class="pre">scrambled_sobol64_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp22threefry2x32_20_engineE"><code class="docutils literal notranslate"><span class="pre">threefry2x32_20_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp22threefry2x64_20_engineE"><code class="docutils literal notranslate"><span class="pre">threefry2x64_20_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp22threefry4x32_20_engineE"><code class="docutils literal notranslate"><span class="pre">threefry4x32_20_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp22threefry4x64_20_engineE"><code class="docutils literal notranslate"><span class="pre">threefry4x64_20_engine</span></code></a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="c-c-api-reference">
<span id="cpp-api"></span><h1>C/C++ API reference<a class="headerlink" href="#c-c-api-reference" title="Link to this heading">#</a></h1>
<p>This chapter describes the rocRAND C and C++ API.</p>
<section id="api-index">
<h2>API index<a class="headerlink" href="#api-index" title="Link to this heading">#</a></h2>
<p>To search the API, refer to the API <a class="reference internal" href="../genindex.html"><span class="std std-ref">Index</span></a>.</p>
</section>
<section id="device-functions">
<h2>Device functions<a class="headerlink" href="#device-functions" title="Link to this heading">#</a></h2>
<p>To use the device API, include the file <code class="docutils literal notranslate"><span class="pre">rocrand_kernel.h</span></code> in files that define kernels that use rocRAND device functions.
Follow these steps to use the device functions in the device kernel definition:</p>
<ol class="arabic simple">
<li><p>Create a new generator state object of the desired generator type.</p></li>
<li><p>Initialize the generator state parameters using <code class="docutils literal notranslate"><span class="pre">rocrand_init</span></code>.</p></li>
<li><p>Generate random numbers by calling the generation function on the generator state.</p></li>
<li><p>Use the results.</p></li>
</ol>
<p>The rocRAND device functions are invoked from inside the user kernel.
This means the generated numbers can be used immediately in the kernel without copying them to the host memory.</p>
<p>In the following example, random number generation uses the XORWOW generator.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;rocrand/rocrand_kernel.h&gt;</span>

<span class="n">__global__</span>
<span class="kt">void</span><span class="w"> </span><span class="n">test</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">uint</span><span class="w">                 </span><span class="n">tid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="n">rocrand_state_xorwow</span><span class="w"> </span><span class="n">state</span><span class="p">;</span>
<span class="w">    </span><span class="n">rocrand_init</span><span class="p">(</span><span class="mi">123</span><span class="p">,</span><span class="w"> </span><span class="n">tid</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">state</span><span class="p">);</span>

<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">3</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">const</span><span class="w"> </span><span class="k">auto</span><span class="w"> </span><span class="n">value</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">rocrand</span><span class="p">(</span><span class="o">&amp;</span><span class="n">state</span><span class="p">);</span>
<span class="w">        </span><span class="n">printf</span><span class="p">(</span><span class="s">&quot;thread %d, index %u: %u</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">,</span><span class="w"> </span><span class="n">tid</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">,</span><span class="w"> </span><span class="n">value</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">test</span><span class="o">&lt;&lt;&lt;</span><span class="n">dim3</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span><span class="w"> </span><span class="n">dim3</span><span class="p">(</span><span class="mi">32</span><span class="p">)</span><span class="o">&gt;&gt;&gt;</span><span class="p">();</span>
<span class="w">    </span><span class="n">hipDeviceSynchronize</span><span class="p">();</span>
<span class="p">}</span>
</pre></div>
</div>
<dl>
<dt class="sig sig-object cpp">
<span class="target" id="group__rocranddevice"></span><em><span class="pre">group</span></em> <span class="sig-name descname"><span class="pre">rocranddevice</span></span></dt>
<dd><div class="breathe-sectiondef docutils container">
<p class="breathe-sectiondef-title rubric" id="breathe-section-title-defines">Defines</p>
<dl class="cpp macro">
<dt class="sig sig-object cpp" id="c.ROCRAND_LFSR113_DEFAULT_SEED_X">
<span class="target" id="group__rocranddevice_1gad7b9a9998c875ff2fc450eb5fda8123c"></span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_LFSR113_DEFAULT_SEED_X</span></span></span><a class="headerlink" href="#c.ROCRAND_LFSR113_DEFAULT_SEED_X" title="Link to this definition">#</a><br /></dt>
<dd><p>Default X seed for LFSR113 PRNG. </p>
</dd></dl>

<dl class="cpp macro">
<dt class="sig sig-object cpp" id="c.ROCRAND_LFSR113_DEFAULT_SEED_Y">
<span class="target" id="group__rocranddevice_1ga42b6caeb3146cf57d8095ba69b2faed6"></span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_LFSR113_DEFAULT_SEED_Y</span></span></span><a class="headerlink" href="#c.ROCRAND_LFSR113_DEFAULT_SEED_Y" title="Link to this definition">#</a><br /></dt>
<dd><p>Default Y seed for LFSR113 PRNG. </p>
</dd></dl>

<dl class="cpp macro">
<dt class="sig sig-object cpp" id="c.ROCRAND_LFSR113_DEFAULT_SEED_Z">
<span class="target" id="group__rocranddevice_1gab01fbf3f2209f949b60ee0990b471007"></span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_LFSR113_DEFAULT_SEED_Z</span></span></span><a class="headerlink" href="#c.ROCRAND_LFSR113_DEFAULT_SEED_Z" title="Link to this definition">#</a><br /></dt>
<dd><p>Default Z seed for LFSR113 PRNG. </p>
</dd></dl>

<dl class="cpp macro">
<dt class="sig sig-object cpp" id="c.ROCRAND_LFSR113_DEFAULT_SEED_W">
<span class="target" id="group__rocranddevice_1ga4e427750c6a51bfd63a7f02cb6e62b1e"></span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_LFSR113_DEFAULT_SEED_W</span></span></span><a class="headerlink" href="#c.ROCRAND_LFSR113_DEFAULT_SEED_W" title="Link to this definition">#</a><br /></dt>
<dd><p>Default W seed for LFSR113 PRNG. </p>
</dd></dl>

<dl class="cpp macro">
<dt class="sig sig-object cpp" id="c.ROCRAND_MRG31K3P_DEFAULT_SEED">
<span class="target" id="group__rocranddevice_1ga0ea93cf8d2d16d5fd7db45ada5ddac05"></span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_MRG31K3P_DEFAULT_SEED</span></span></span><a class="headerlink" href="#c.ROCRAND_MRG31K3P_DEFAULT_SEED" title="Link to this definition">#</a><br /></dt>
<dd><p>Default seed for MRG31K3P PRNG. </p>
</dd></dl>

<dl class="cpp macro">
<dt class="sig sig-object cpp" id="c.ROCRAND_MRG32K3A_DEFAULT_SEED">
<span class="target" id="group__rocranddevice_1ga2b4b37e72c090e6d99373ff68d14c173"></span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_MRG32K3A_DEFAULT_SEED</span></span></span><a class="headerlink" href="#c.ROCRAND_MRG32K3A_DEFAULT_SEED" title="Link to this definition">#</a><br /></dt>
<dd><p>Default seed for MRG32K3A PRNG. </p>
</dd></dl>

<dl class="cpp macro">
<dt class="sig sig-object cpp" id="c.ROCRAND_PHILOX4x32_DEFAULT_SEED">
<span class="target" id="group__rocranddevice_1ga545da3f91883ce1a2990a1ec8141d5fb"></span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_PHILOX4x32_DEFAULT_SEED</span></span></span><a class="headerlink" href="#c.ROCRAND_PHILOX4x32_DEFAULT_SEED" title="Link to this definition">#</a><br /></dt>
<dd><p>Default seed for PHILOX4x32 PRNG. </p>
</dd></dl>

<dl class="cpp macro">
<dt class="sig sig-object cpp" id="c.ROCRAND_XORWOW_DEFAULT_SEED">
<span class="target" id="group__rocranddevice_1gafb4aa9f4548403e34c00b271c7ef1a77"></span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_XORWOW_DEFAULT_SEED</span></span></span><a class="headerlink" href="#c.ROCRAND_XORWOW_DEFAULT_SEED" title="Link to this definition">#</a><br /></dt>
<dd><p>Default seed for XORWOW PRNG. </p>
</dd></dl>

</div>
<div class="breathe-sectiondef docutils container">
<p class="breathe-sectiondef-title rubric" id="breathe-section-title-functions">Functions</p>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP27rocrand_state_philox4x32_10K29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP27rocrand_state_philox4x32_10K29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP27rocrand_state_philox4x32_10K29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_philox4x32_10P.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1gac248f160916362d5bc50766d60592bc3"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP27rocrand_state_philox4x32_10K29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417rocrand_discrete4P27rocrand_state_philox4x32_10K29rocrand_discrete_distribution">
<span id="_CPPv317rocrand_discrete4P27rocrand_state_philox4x32_10K29rocrand_discrete_distribution"></span><span id="_CPPv217rocrand_discrete4P27rocrand_state_philox4x32_10K29rocrand_discrete_distribution"></span><span id="rocrand_discrete4__rocrand_state_philox4x32_10P.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1ga9e99fa4a17904bf3fa2be1ab264aba63"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">uint4</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete4</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417rocrand_discrete4P27rocrand_state_philox4x32_10K29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns four discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values. </p>
<p>Returns four <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by four.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Four <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> as <code class="docutils literal notranslate"><span class="pre">uint4</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP22rocrand_state_mrg31k3pK29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP22rocrand_state_mrg31k3pK29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP22rocrand_state_mrg31k3pK29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_mrg31k3pP.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1gafaa4675b5ed08c49bb292755754c4cb7"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP22rocrand_state_mrg31k3pK29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using MRG31k3p generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP22rocrand_state_mrg32k3aK29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP22rocrand_state_mrg32k3aK29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP22rocrand_state_mrg32k3aK29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_mrg32k3aP.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1gab612b1a6bf4163b554e830d84dfeb3b3"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP22rocrand_state_mrg32k3aK29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using MRG32k3a generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP20rocrand_state_xorwowK29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP20rocrand_state_xorwowK29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP20rocrand_state_xorwowK29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_xorwowP.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1ga77a05abee603e12174f4d1d4e71aa98a"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP20rocrand_state_xorwowK29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using XORWOW generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP20rocrand_state_mtgp32K29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP20rocrand_state_mtgp32K29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP20rocrand_state_mtgp32K29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_mtgp32P.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1ga195fabe11fc7a654b10a05bb8f3e5ef6"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP20rocrand_state_mtgp32K29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP21rocrand_state_sobol32K29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP21rocrand_state_sobol32K29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP21rocrand_state_sobol32K29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_sobol32P.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1ga206ff2526201eeb05aca9279f0d27eb2"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP21rocrand_state_sobol32K29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP31rocrand_state_scrambled_sobol32K29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP31rocrand_state_scrambled_sobol32K29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP31rocrand_state_scrambled_sobol32K29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_scrambled_sobol32P.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1ga414693434bef4479c192bd004c77358d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP31rocrand_state_scrambled_sobol32K29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using SCRAMBLED_SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP21rocrand_state_sobol64K29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP21rocrand_state_sobol64K29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP21rocrand_state_sobol64K29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_sobol64P.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1gad1efce9139634d61b55b06d85ca1b002"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP21rocrand_state_sobol64K29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP31rocrand_state_scrambled_sobol64K29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP31rocrand_state_scrambled_sobol64K29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP31rocrand_state_scrambled_sobol64K29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_scrambled_sobol64P.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1gabb576c4b85a8dc84ef57718cbd358b0c"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP31rocrand_state_scrambled_sobol64K29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using SCRAMBLED_SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP21rocrand_state_lfsr113K29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP21rocrand_state_lfsr113K29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP21rocrand_state_lfsr113K29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_lfsr113P.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1ga9312999cf76758db78b4a8189e84614a"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP21rocrand_state_lfsr113K29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP29rocrand_state_threefry2x32_20K29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP29rocrand_state_threefry2x32_20K29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP29rocrand_state_threefry2x32_20K29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_threefry2x32_20P.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1ga486c8dd1fe820ef5872bed48078de16a"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP29rocrand_state_threefry2x32_20K29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP29rocrand_state_threefry2x64_20K29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP29rocrand_state_threefry2x64_20K29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP29rocrand_state_threefry2x64_20K29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_threefry2x64_20P.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1ga6f01653b03881a3b425b3d6e16752f71"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP29rocrand_state_threefry2x64_20K29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP29rocrand_state_threefry4x32_20K29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP29rocrand_state_threefry4x32_20K29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP29rocrand_state_threefry4x32_20K29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_threefry4x32_20P.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1gaeabcd7fdbd06c119592da4953fc9cc58"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP29rocrand_state_threefry4x32_20K29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_discreteP29rocrand_state_threefry4x64_20K29rocrand_discrete_distribution">
<span id="_CPPv316rocrand_discreteP29rocrand_state_threefry4x64_20K29rocrand_discrete_distribution"></span><span id="_CPPv216rocrand_discreteP29rocrand_state_threefry4x64_20K29rocrand_discrete_distribution"></span><span id="rocrand_discrete__rocrand_state_threefry4x64_20P.rocrand_discrete_distributionC"></span><span class="target" id="group__rocranddevice_1ga291b6bc600cc0014c94fed6f640aa6ff"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_discrete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_discreteP29rocrand_state_threefry4x64_20K29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a discrete distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value. </p>
<p>Returns a <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> distributed according to with discrete distribution <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments the position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>discrete_distribution</strong> – Related discrete distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value distributed according to <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412rocrand_initK5uint4KjP21rocrand_state_lfsr113">
<span id="_CPPv312rocrand_initK5uint4KjP21rocrand_state_lfsr113"></span><span id="_CPPv212rocrand_initK5uint4KjP21rocrand_state_lfsr113"></span><span id="rocrand_init__uint4C.unsigned-iC.rocrand_state_lfsr113P"></span><span class="target" id="group__rocranddevice_1ga09a4e64bee35d4e6496050c48431685a"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_init</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">uint4</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">seed</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">subsequence</span></span>, <span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412rocrand_initK5uint4KjP21rocrand_state_lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Initializes LFSR113 state. </p>
<p>Initializes the LFSR113 generator <code class="docutils literal notranslate"><span class="pre">state</span></code> with the given <code class="docutils literal notranslate"><span class="pre">seed</span></code>, <code class="docutils literal notranslate"><span class="pre">subsequence</span></code>, and <code class="docutils literal notranslate"><span class="pre">offset</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>seed</strong> – Value to use as a seed </p></li>
<li><p><strong>subsequence</strong> – Subsequence to start at </p></li>
<li><p><strong>state</strong> – Pointer to state to initialize </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412rocrand_initK5uint4KjKyP21rocrand_state_lfsr113">
<span id="_CPPv312rocrand_initK5uint4KjKyP21rocrand_state_lfsr113"></span><span id="_CPPv212rocrand_initK5uint4KjKyP21rocrand_state_lfsr113"></span><span id="rocrand_init__uint4C.unsigned-iC.unsigned-l-lC.rocrand_state_lfsr113P"></span><span class="target" id="group__rocranddevice_1ga3c0fe333a9b120eabad97599ecef5d97"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_init</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">uint4</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">seed</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">subsequence</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412rocrand_initK5uint4KjKyP21rocrand_state_lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Initializes LFSR113 state. </p>
<p>Initializes the LFSR113 generator <code class="docutils literal notranslate"><span class="pre">state</span></code> with the given <code class="docutils literal notranslate"><span class="pre">seed</span></code>, <code class="docutils literal notranslate"><span class="pre">subsequence</span></code>, and <code class="docutils literal notranslate"><span class="pre">offset</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>seed</strong> – Value to use as a seed </p></li>
<li><p><strong>subsequence</strong> – Subsequence to start at </p></li>
<li><p><strong>offset</strong> – Absolute offset into subsequence </p></li>
<li><p><strong>state</strong> – Pointer to state to initialize </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv47rocrandP21rocrand_state_lfsr113">
<span id="_CPPv37rocrandP21rocrand_state_lfsr113"></span><span id="_CPPv27rocrandP21rocrand_state_lfsr113"></span><span id="rocrand__rocrand_state_lfsr113P"></span><span class="target" id="group__rocranddevice_1gae14489c1fd9550e94132db23f360fc21"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv47rocrandP21rocrand_state_lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range. </p>
<p>Generates and returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Pseudorandom value (32-bit) as an <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49skipaheadyP21rocrand_state_lfsr113">
<span id="_CPPv39skipaheadyP21rocrand_state_lfsr113"></span><span id="_CPPv29skipaheadyP21rocrand_state_lfsr113"></span><span id="skipahead__unsigned-l-l.rocrand_state_lfsr113P"></span><span class="target" id="group__rocranddevice_1ga0dc552a709292a01283fc4ef17dd58cb"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49skipaheadyP21rocrand_state_lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates LFSR113 state to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements. </p>
<p>Updates the LFSR113 state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – Number of elements to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421skipahead_subsequencejP21rocrand_state_lfsr113">
<span id="_CPPv321skipahead_subsequencejP21rocrand_state_lfsr113"></span><span id="_CPPv221skipahead_subsequencejP21rocrand_state_lfsr113"></span><span id="skipahead_subsequence__unsigned-i.rocrand_state_lfsr113P"></span><span class="target" id="group__rocranddevice_1ga5270d303b65046b75d4bb1faae8e5621"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead_subsequence</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">subsequence</span></span>, <span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421skipahead_subsequencejP21rocrand_state_lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates LFSR113 state to skip ahead by <code class="docutils literal notranslate"><span class="pre">subsequence</span></code> subsequences. </p>
<p>Updates the LFSR113 <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">subsequence</span></code> subsequences. Each subsequence is 2^55 numbers long.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>subsequence</strong> – Number of subsequences to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418skipahead_sequencejP21rocrand_state_lfsr113">
<span id="_CPPv318skipahead_sequencejP21rocrand_state_lfsr113"></span><span id="_CPPv218skipahead_sequencejP21rocrand_state_lfsr113"></span><span id="skipahead_sequence__unsigned-i.rocrand_state_lfsr113P"></span><span class="target" id="group__rocranddevice_1ga4414ed01949e3cda52e2a326b5f62121"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead_sequence</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sequence</span></span>, <span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418skipahead_sequencejP21rocrand_state_lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates LFSR113 state to skip ahead by <code class="docutils literal notranslate"><span class="pre">sequence</span></code> sequences. </p>
<p>Updates the LFSR113 <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">sequence</span></code> sequences. For LFSR113 each sequence is 2^55 numbers long (equal to the size of a subsequence).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>sequence</strong> – Number of sequences to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP27rocrand_state_philox4x32_10ff">
<span id="_CPPv318rocrand_log_normalP27rocrand_state_philox4x32_10ff"></span><span id="_CPPv218rocrand_log_normalP27rocrand_state_philox4x32_10ff"></span><span id="rocrand_log_normal__rocrand_state_philox4x32_10P.float.float"></span><span class="target" id="group__rocranddevice_1gacffc17d6bd44b57151cc468459cf23ed"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP27rocrand_state_philox4x32_10ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419rocrand_log_normal2P27rocrand_state_philox4x32_10ff">
<span id="_CPPv319rocrand_log_normal2P27rocrand_state_philox4x32_10ff"></span><span id="_CPPv219rocrand_log_normal2P27rocrand_state_philox4x32_10ff"></span><span id="rocrand_log_normal2__rocrand_state_philox4x32_10P.float.float"></span><span class="target" id="group__rocranddevice_1gad6cf57ff46d01c23770c244a785ab092"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419rocrand_log_normal2P27rocrand_state_philox4x32_10ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419rocrand_log_normal4P27rocrand_state_philox4x32_10ff">
<span id="_CPPv319rocrand_log_normal4P27rocrand_state_philox4x32_10ff"></span><span id="_CPPv219rocrand_log_normal4P27rocrand_state_philox4x32_10ff"></span><span id="rocrand_log_normal4__rocrand_state_philox4x32_10P.float.float"></span><span class="target" id="group__rocranddevice_1gac1f7951ee3236ecfe0bccace80b56e75"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float4</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal4</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419rocrand_log_normal4P27rocrand_state_philox4x32_10ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns four log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns four log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. The function uses the Box-Muller transform method to generate four normally distributed values, transforms them to log-normally distributed values, and returns them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Four log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float4</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP27rocrand_state_philox4x32_10dd">
<span id="_CPPv325rocrand_log_normal_doubleP27rocrand_state_philox4x32_10dd"></span><span id="_CPPv225rocrand_log_normal_doubleP27rocrand_state_philox4x32_10dd"></span><span id="rocrand_log_normal_double__rocrand_state_philox4x32_10P.double.double"></span><span class="target" id="group__rocranddevice_1ga1b9021f11b0e72dec0ef0343541fd427"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP27rocrand_state_philox4x32_10dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values, transforms them to log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426rocrand_log_normal_double2P27rocrand_state_philox4x32_10dd">
<span id="_CPPv326rocrand_log_normal_double2P27rocrand_state_philox4x32_10dd"></span><span id="_CPPv226rocrand_log_normal_double2P27rocrand_state_philox4x32_10dd"></span><span id="rocrand_log_normal_double2__rocrand_state_philox4x32_10P.double.double"></span><span class="target" id="group__rocranddevice_1gadd3c12b9c1ac1e73f1f5a95431ac655a"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426rocrand_log_normal_double2P27rocrand_state_philox4x32_10dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426rocrand_log_normal_double4P27rocrand_state_philox4x32_10dd">
<span id="_CPPv326rocrand_log_normal_double4P27rocrand_state_philox4x32_10dd"></span><span id="_CPPv226rocrand_log_normal_double4P27rocrand_state_philox4x32_10dd"></span><span id="rocrand_log_normal_double4__rocrand_state_philox4x32_10P.double.double"></span><span class="target" id="group__rocranddevice_1gadadf3796cfb5b8943fc67f4f6a471e81"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double4</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double4</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426rocrand_log_normal_double4P27rocrand_state_philox4x32_10dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns four log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns four log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by eight. The function uses the Box-Muller transform method to generate four normally distributed values, transforms them to log-normally distributed values, and returns them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Four log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double4</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP22rocrand_state_mrg31k3pff">
<span id="_CPPv318rocrand_log_normalP22rocrand_state_mrg31k3pff"></span><span id="_CPPv218rocrand_log_normalP22rocrand_state_mrg31k3pff"></span><span id="rocrand_log_normal__rocrand_state_mrg31k3pP.float.float"></span><span class="target" id="group__rocranddevice_1gaea0a83f0a800d10c4b6b9e5fc9f0cc2e"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP22rocrand_state_mrg31k3pff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using MRG31k3p generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419rocrand_log_normal2P22rocrand_state_mrg31k3pff">
<span id="_CPPv319rocrand_log_normal2P22rocrand_state_mrg31k3pff"></span><span id="_CPPv219rocrand_log_normal2P22rocrand_state_mrg31k3pff"></span><span id="rocrand_log_normal2__rocrand_state_mrg31k3pP.float.float"></span><span class="target" id="group__rocranddevice_1ga6e72ac54acb2d712607f4020e0be9d2b"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419rocrand_log_normal2P22rocrand_state_mrg31k3pff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using MRG31k3p generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP22rocrand_state_mrg31k3pdd">
<span id="_CPPv325rocrand_log_normal_doubleP22rocrand_state_mrg31k3pdd"></span><span id="_CPPv225rocrand_log_normal_doubleP22rocrand_state_mrg31k3pdd"></span><span id="rocrand_log_normal_double__rocrand_state_mrg31k3pP.double.double"></span><span class="target" id="group__rocranddevice_1ga342f0fe3f67e36cc23554a1769f1d75d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP22rocrand_state_mrg31k3pdd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using MRG31k3p generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. The function uses the Box-Muller transform method to generate two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values, transforms them to log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426rocrand_log_normal_double2P22rocrand_state_mrg31k3pdd">
<span id="_CPPv326rocrand_log_normal_double2P22rocrand_state_mrg31k3pdd"></span><span id="_CPPv226rocrand_log_normal_double2P22rocrand_state_mrg31k3pdd"></span><span id="rocrand_log_normal_double2__rocrand_state_mrg31k3pP.double.double"></span><span class="target" id="group__rocranddevice_1gafac1439b49bfbf9f7eebb3e392525439"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426rocrand_log_normal_double2P22rocrand_state_mrg31k3pdd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using MRG31k3p generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP22rocrand_state_mrg32k3aff">
<span id="_CPPv318rocrand_log_normalP22rocrand_state_mrg32k3aff"></span><span id="_CPPv218rocrand_log_normalP22rocrand_state_mrg32k3aff"></span><span id="rocrand_log_normal__rocrand_state_mrg32k3aP.float.float"></span><span class="target" id="group__rocranddevice_1ga38ed3f5634bdd873546c2de9230c6246"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP22rocrand_state_mrg32k3aff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using MRG32k3a generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419rocrand_log_normal2P22rocrand_state_mrg32k3aff">
<span id="_CPPv319rocrand_log_normal2P22rocrand_state_mrg32k3aff"></span><span id="_CPPv219rocrand_log_normal2P22rocrand_state_mrg32k3aff"></span><span id="rocrand_log_normal2__rocrand_state_mrg32k3aP.float.float"></span><span class="target" id="group__rocranddevice_1ga588f77966121ac4301f9721cee1b6f9d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419rocrand_log_normal2P22rocrand_state_mrg32k3aff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using MRG32k3a generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP22rocrand_state_mrg32k3add">
<span id="_CPPv325rocrand_log_normal_doubleP22rocrand_state_mrg32k3add"></span><span id="_CPPv225rocrand_log_normal_doubleP22rocrand_state_mrg32k3add"></span><span id="rocrand_log_normal_double__rocrand_state_mrg32k3aP.double.double"></span><span class="target" id="group__rocranddevice_1ga613b83ccd5f156bdcb8704082aa406aa"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP22rocrand_state_mrg32k3add" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using MRG32k3a generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. The function uses the Box-Muller transform method to generate two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values, transforms them to log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426rocrand_log_normal_double2P22rocrand_state_mrg32k3add">
<span id="_CPPv326rocrand_log_normal_double2P22rocrand_state_mrg32k3add"></span><span id="_CPPv226rocrand_log_normal_double2P22rocrand_state_mrg32k3add"></span><span id="rocrand_log_normal_double2__rocrand_state_mrg32k3aP.double.double"></span><span class="target" id="group__rocranddevice_1ga2b865690be3a2a360b277917c979f37a"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426rocrand_log_normal_double2P22rocrand_state_mrg32k3add" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using MRG32k3a generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP20rocrand_state_xorwowff">
<span id="_CPPv318rocrand_log_normalP20rocrand_state_xorwowff"></span><span id="_CPPv218rocrand_log_normalP20rocrand_state_xorwowff"></span><span id="rocrand_log_normal__rocrand_state_xorwowP.float.float"></span><span class="target" id="group__rocranddevice_1ga2b9572e6cfc433ab807ae89c9f2f2f44"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP20rocrand_state_xorwowff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using XORWOW generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419rocrand_log_normal2P20rocrand_state_xorwowff">
<span id="_CPPv319rocrand_log_normal2P20rocrand_state_xorwowff"></span><span id="_CPPv219rocrand_log_normal2P20rocrand_state_xorwowff"></span><span id="rocrand_log_normal2__rocrand_state_xorwowP.float.float"></span><span class="target" id="group__rocranddevice_1ga99ba75351bfaf0247b4c249ea0980c32"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419rocrand_log_normal2P20rocrand_state_xorwowff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using XORWOW generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP20rocrand_state_xorwowdd">
<span id="_CPPv325rocrand_log_normal_doubleP20rocrand_state_xorwowdd"></span><span id="_CPPv225rocrand_log_normal_doubleP20rocrand_state_xorwowdd"></span><span id="rocrand_log_normal_double__rocrand_state_xorwowP.double.double"></span><span class="target" id="group__rocranddevice_1ga69c1efe7a85a7c952478a46902963a57"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP20rocrand_state_xorwowdd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using XORWOW generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values, transforms them to log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426rocrand_log_normal_double2P20rocrand_state_xorwowdd">
<span id="_CPPv326rocrand_log_normal_double2P20rocrand_state_xorwowdd"></span><span id="_CPPv226rocrand_log_normal_double2P20rocrand_state_xorwowdd"></span><span id="rocrand_log_normal_double2__rocrand_state_xorwowP.double.double"></span><span class="target" id="group__rocranddevice_1ga04fc4a82705707b3e1ad54fef06de455"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426rocrand_log_normal_double2P20rocrand_state_xorwowdd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using XORWOW generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP20rocrand_state_mtgp32ff">
<span id="_CPPv318rocrand_log_normalP20rocrand_state_mtgp32ff"></span><span id="_CPPv218rocrand_log_normalP20rocrand_state_mtgp32ff"></span><span id="rocrand_log_normal__rocrand_state_mtgp32P.float.float"></span><span class="target" id="group__rocranddevice_1ga123f707dbdbb2ffacae3d7a931ca0f4a"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP20rocrand_state_mtgp32ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419rocrand_log_normal2P20rocrand_state_mtgp32ff">
<span id="_CPPv319rocrand_log_normal2P20rocrand_state_mtgp32ff"></span><span id="_CPPv219rocrand_log_normal2P20rocrand_state_mtgp32ff"></span><span id="rocrand_log_normal2__rocrand_state_mtgp32P.float.float"></span><span class="target" id="group__rocranddevice_1ga688ca9e3c1ef81bd94170bbe87b0a451"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419rocrand_log_normal2P20rocrand_state_mtgp32ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP20rocrand_state_mtgp32dd">
<span id="_CPPv325rocrand_log_normal_doubleP20rocrand_state_mtgp32dd"></span><span id="_CPPv225rocrand_log_normal_doubleP20rocrand_state_mtgp32dd"></span><span id="rocrand_log_normal_double__rocrand_state_mtgp32P.double.double"></span><span class="target" id="group__rocranddevice_1gae0d2dbfd6e36333fa54448fe90555932"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP20rocrand_state_mtgp32dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426rocrand_log_normal_double2P20rocrand_state_mtgp32dd">
<span id="_CPPv326rocrand_log_normal_double2P20rocrand_state_mtgp32dd"></span><span id="_CPPv226rocrand_log_normal_double2P20rocrand_state_mtgp32dd"></span><span id="rocrand_log_normal_double2__rocrand_state_mtgp32P.double.double"></span><span class="target" id="group__rocranddevice_1gabd118b156aa045b262672f80b17aaafb"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426rocrand_log_normal_double2P20rocrand_state_mtgp32dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP21rocrand_state_sobol32ff">
<span id="_CPPv318rocrand_log_normalP21rocrand_state_sobol32ff"></span><span id="_CPPv218rocrand_log_normalP21rocrand_state_sobol32ff"></span><span id="rocrand_log_normal__rocrand_state_sobol32P.float.float"></span><span class="target" id="group__rocranddevice_1gac43e23dd6afda54caf2093649f3afba9"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP21rocrand_state_sobol32ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP21rocrand_state_sobol32dd">
<span id="_CPPv325rocrand_log_normal_doubleP21rocrand_state_sobol32dd"></span><span id="_CPPv225rocrand_log_normal_doubleP21rocrand_state_sobol32dd"></span><span id="rocrand_log_normal_double__rocrand_state_sobol32P.double.double"></span><span class="target" id="group__rocranddevice_1gae838b5849f08212af43c73f499b287ef"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP21rocrand_state_sobol32dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP31rocrand_state_scrambled_sobol32ff">
<span id="_CPPv318rocrand_log_normalP31rocrand_state_scrambled_sobol32ff"></span><span id="_CPPv218rocrand_log_normalP31rocrand_state_scrambled_sobol32ff"></span><span id="rocrand_log_normal__rocrand_state_scrambled_sobol32P.float.float"></span><span class="target" id="group__rocranddevice_1ga07a81ad0adf6656c6459dd3b4f4cb2e3"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP31rocrand_state_scrambled_sobol32ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using SCRAMBLED_SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP31rocrand_state_scrambled_sobol32dd">
<span id="_CPPv325rocrand_log_normal_doubleP31rocrand_state_scrambled_sobol32dd"></span><span id="_CPPv225rocrand_log_normal_doubleP31rocrand_state_scrambled_sobol32dd"></span><span id="rocrand_log_normal_double__rocrand_state_scrambled_sobol32P.double.double"></span><span class="target" id="group__rocranddevice_1gadf5da8d5b2f1bbd7178b600739341e70"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP31rocrand_state_scrambled_sobol32dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using SCRAMBLED_SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP21rocrand_state_sobol64ff">
<span id="_CPPv318rocrand_log_normalP21rocrand_state_sobol64ff"></span><span id="_CPPv218rocrand_log_normalP21rocrand_state_sobol64ff"></span><span id="rocrand_log_normal__rocrand_state_sobol64P.float.float"></span><span class="target" id="group__rocranddevice_1ga73191185eaae4b950aa6113031122de8"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP21rocrand_state_sobol64ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP21rocrand_state_sobol64dd">
<span id="_CPPv325rocrand_log_normal_doubleP21rocrand_state_sobol64dd"></span><span id="_CPPv225rocrand_log_normal_doubleP21rocrand_state_sobol64dd"></span><span id="rocrand_log_normal_double__rocrand_state_sobol64P.double.double"></span><span class="target" id="group__rocranddevice_1gab31c92f5fc0c7ae45f18c6d21cf40298"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP21rocrand_state_sobol64dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP31rocrand_state_scrambled_sobol64ff">
<span id="_CPPv318rocrand_log_normalP31rocrand_state_scrambled_sobol64ff"></span><span id="_CPPv218rocrand_log_normalP31rocrand_state_scrambled_sobol64ff"></span><span id="rocrand_log_normal__rocrand_state_scrambled_sobol64P.float.float"></span><span class="target" id="group__rocranddevice_1ga055dc0a0e3d909be9c69911ade391900"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP31rocrand_state_scrambled_sobol64ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using SCRAMBLED_SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP31rocrand_state_scrambled_sobol64dd">
<span id="_CPPv325rocrand_log_normal_doubleP31rocrand_state_scrambled_sobol64dd"></span><span id="_CPPv225rocrand_log_normal_doubleP31rocrand_state_scrambled_sobol64dd"></span><span id="rocrand_log_normal_double__rocrand_state_scrambled_sobol64P.double.double"></span><span class="target" id="group__rocranddevice_1gad38daf3f3589cb88f2549edc6a690bea"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP31rocrand_state_scrambled_sobol64dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using SCRAMBLED_SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP21rocrand_state_lfsr113ff">
<span id="_CPPv318rocrand_log_normalP21rocrand_state_lfsr113ff"></span><span id="_CPPv218rocrand_log_normalP21rocrand_state_lfsr113ff"></span><span id="rocrand_log_normal__rocrand_state_lfsr113P.float.float"></span><span class="target" id="group__rocranddevice_1ga290dfb809d1a2f1f98d570fe730e8085"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP21rocrand_state_lfsr113ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419rocrand_log_normal2P21rocrand_state_lfsr113ff">
<span id="_CPPv319rocrand_log_normal2P21rocrand_state_lfsr113ff"></span><span id="_CPPv219rocrand_log_normal2P21rocrand_state_lfsr113ff"></span><span id="rocrand_log_normal2__rocrand_state_lfsr113P.float.float"></span><span class="target" id="group__rocranddevice_1ga9c8c910755c75b2f4071ef133944b696"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419rocrand_log_normal2P21rocrand_state_lfsr113ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP21rocrand_state_lfsr113dd">
<span id="_CPPv325rocrand_log_normal_doubleP21rocrand_state_lfsr113dd"></span><span id="_CPPv225rocrand_log_normal_doubleP21rocrand_state_lfsr113dd"></span><span id="rocrand_log_normal_double__rocrand_state_lfsr113P.double.double"></span><span class="target" id="group__rocranddevice_1ga24d251fa77042670fdbc90dd4d7e0631"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP21rocrand_state_lfsr113dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426rocrand_log_normal_double2P21rocrand_state_lfsr113dd">
<span id="_CPPv326rocrand_log_normal_double2P21rocrand_state_lfsr113dd"></span><span id="_CPPv226rocrand_log_normal_double2P21rocrand_state_lfsr113dd"></span><span id="rocrand_log_normal_double2__rocrand_state_lfsr113P.double.double"></span><span class="target" id="group__rocranddevice_1ga59e4b79231c22228e95482275b745389"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426rocrand_log_normal_double2P21rocrand_state_lfsr113dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP29rocrand_state_threefry2x32_20dd">
<span id="_CPPv318rocrand_log_normalP29rocrand_state_threefry2x32_20dd"></span><span id="_CPPv218rocrand_log_normalP29rocrand_state_threefry2x32_20dd"></span><span id="rocrand_log_normal__rocrand_state_threefry2x32_20P.double.double"></span><span class="target" id="group__rocranddevice_1ga26840acda9ba00c610e4a88e3cd7abf5"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP29rocrand_state_threefry2x32_20dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419rocrand_log_normal2P29rocrand_state_threefry2x32_20ff">
<span id="_CPPv319rocrand_log_normal2P29rocrand_state_threefry2x32_20ff"></span><span id="_CPPv219rocrand_log_normal2P29rocrand_state_threefry2x32_20ff"></span><span id="rocrand_log_normal2__rocrand_state_threefry2x32_20P.float.float"></span><span class="target" id="group__rocranddevice_1ga90a68914214dab64bb5cb62dbc711187"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419rocrand_log_normal2P29rocrand_state_threefry2x32_20ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry2x32_20dd">
<span id="_CPPv325rocrand_log_normal_doubleP29rocrand_state_threefry2x32_20dd"></span><span id="_CPPv225rocrand_log_normal_doubleP29rocrand_state_threefry2x32_20dd"></span><span id="rocrand_log_normal_double__rocrand_state_threefry2x32_20P.double.double"></span><span class="target" id="group__rocranddevice_1gafd7b405ac310646a63b8ab21f4393ce7"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry2x32_20dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry2x32_20dd">
<span id="_CPPv326rocrand_log_normal_double2P29rocrand_state_threefry2x32_20dd"></span><span id="_CPPv226rocrand_log_normal_double2P29rocrand_state_threefry2x32_20dd"></span><span id="rocrand_log_normal_double2__rocrand_state_threefry2x32_20P.double.double"></span><span class="target" id="group__rocranddevice_1ga0b3ed490f7ebd985a19d93d88726f64c"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry2x32_20dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP29rocrand_state_threefry2x64_20dd">
<span id="_CPPv318rocrand_log_normalP29rocrand_state_threefry2x64_20dd"></span><span id="_CPPv218rocrand_log_normalP29rocrand_state_threefry2x64_20dd"></span><span id="rocrand_log_normal__rocrand_state_threefry2x64_20P.double.double"></span><span class="target" id="group__rocranddevice_1gae759cfada76def5807c0a475e006b0eb"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP29rocrand_state_threefry2x64_20dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419rocrand_log_normal2P29rocrand_state_threefry2x64_20ff">
<span id="_CPPv319rocrand_log_normal2P29rocrand_state_threefry2x64_20ff"></span><span id="_CPPv219rocrand_log_normal2P29rocrand_state_threefry2x64_20ff"></span><span id="rocrand_log_normal2__rocrand_state_threefry2x64_20P.float.float"></span><span class="target" id="group__rocranddevice_1ga1b4c01b8ff44a31795e4204ee45aa1ae"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419rocrand_log_normal2P29rocrand_state_threefry2x64_20ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry2x64_20dd">
<span id="_CPPv325rocrand_log_normal_doubleP29rocrand_state_threefry2x64_20dd"></span><span id="_CPPv225rocrand_log_normal_doubleP29rocrand_state_threefry2x64_20dd"></span><span id="rocrand_log_normal_double__rocrand_state_threefry2x64_20P.double.double"></span><span class="target" id="group__rocranddevice_1gac70c7a84d81962cb5fdc52d09d10e520"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry2x64_20dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry2x64_20dd">
<span id="_CPPv326rocrand_log_normal_double2P29rocrand_state_threefry2x64_20dd"></span><span id="_CPPv226rocrand_log_normal_double2P29rocrand_state_threefry2x64_20dd"></span><span id="rocrand_log_normal_double2__rocrand_state_threefry2x64_20P.double.double"></span><span class="target" id="group__rocranddevice_1ga8670a42e95d371967df87b20a8a44c95"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry2x64_20dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP29rocrand_state_threefry4x32_20dd">
<span id="_CPPv318rocrand_log_normalP29rocrand_state_threefry4x32_20dd"></span><span id="_CPPv218rocrand_log_normalP29rocrand_state_threefry4x32_20dd"></span><span id="rocrand_log_normal__rocrand_state_threefry4x32_20P.double.double"></span><span class="target" id="group__rocranddevice_1ga05182c6947957a9a412b5c12d2b922c2"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP29rocrand_state_threefry4x32_20dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419rocrand_log_normal2P29rocrand_state_threefry4x32_20ff">
<span id="_CPPv319rocrand_log_normal2P29rocrand_state_threefry4x32_20ff"></span><span id="_CPPv219rocrand_log_normal2P29rocrand_state_threefry4x32_20ff"></span><span id="rocrand_log_normal2__rocrand_state_threefry4x32_20P.float.float"></span><span class="target" id="group__rocranddevice_1gae342eca928af9c2ecc7aef78856d4864"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419rocrand_log_normal2P29rocrand_state_threefry4x32_20ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry4x32_20dd">
<span id="_CPPv325rocrand_log_normal_doubleP29rocrand_state_threefry4x32_20dd"></span><span id="_CPPv225rocrand_log_normal_doubleP29rocrand_state_threefry4x32_20dd"></span><span id="rocrand_log_normal_double__rocrand_state_threefry4x32_20P.double.double"></span><span class="target" id="group__rocranddevice_1ga521e9db8c3ba9cc932f8e986a876bc2c"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry4x32_20dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry4x32_20dd">
<span id="_CPPv326rocrand_log_normal_double2P29rocrand_state_threefry4x32_20dd"></span><span id="_CPPv226rocrand_log_normal_double2P29rocrand_state_threefry4x32_20dd"></span><span id="rocrand_log_normal_double2__rocrand_state_threefry4x32_20P.double.double"></span><span class="target" id="group__rocranddevice_1gaacc93c3d36e10e39207e058fdd766ae9"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry4x32_20dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_log_normalP29rocrand_state_threefry4x64_20dd">
<span id="_CPPv318rocrand_log_normalP29rocrand_state_threefry4x64_20dd"></span><span id="_CPPv218rocrand_log_normalP29rocrand_state_threefry4x64_20dd"></span><span id="rocrand_log_normal__rocrand_state_threefry4x64_20P.double.double"></span><span class="target" id="group__rocranddevice_1ga79370a5363f8d2249a6272b14b508f3b"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_log_normalP29rocrand_state_threefry4x64_20dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419rocrand_log_normal2P29rocrand_state_threefry4x64_20ff">
<span id="_CPPv319rocrand_log_normal2P29rocrand_state_threefry4x64_20ff"></span><span id="_CPPv219rocrand_log_normal2P29rocrand_state_threefry4x64_20ff"></span><span id="rocrand_log_normal2__rocrand_state_threefry4x64_20P.float.float"></span><span class="target" id="group__rocranddevice_1ga682de57f98ea8baddd4db1860ed77133"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419rocrand_log_normal2P29rocrand_state_threefry4x64_20ff" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry4x64_20dd">
<span id="_CPPv325rocrand_log_normal_doubleP29rocrand_state_threefry4x64_20dd"></span><span id="_CPPv225rocrand_log_normal_doubleP29rocrand_state_threefry4x64_20dd"></span><span id="rocrand_log_normal_double__rocrand_state_threefry4x64_20P.double.double"></span><span class="target" id="group__rocranddevice_1gad500a84a25386b31c3d46489673a85d4"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry4x64_20dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry4x64_20dd">
<span id="_CPPv326rocrand_log_normal_double2P29rocrand_state_threefry4x64_20dd"></span><span id="_CPPv226rocrand_log_normal_double2P29rocrand_state_threefry4x64_20dd"></span><span id="rocrand_log_normal_double2__rocrand_state_threefry4x64_20P.double.double"></span><span class="target" id="group__rocranddevice_1ga4211c3977a1ab5e430f51e4361adcb8d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_log_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry4x64_20dd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using Threefry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. The function uses the Box-Muller transform method to generate two normally distributed values, transforms them to log-normally distributed values, and returns both.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>mean</strong> – Mean of the related log-normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation of the related log-normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412rocrand_initKyKyKyP22rocrand_state_mrg31k3p">
<span id="_CPPv312rocrand_initKyKyKyP22rocrand_state_mrg31k3p"></span><span id="_CPPv212rocrand_initKyKyKyP22rocrand_state_mrg31k3p"></span><span id="rocrand_init__unsigned-l-lC.unsigned-l-lC.unsigned-l-lC.rocrand_state_mrg31k3pP"></span><span class="target" id="group__rocranddevice_1gae83ca3096fbde399683c115259a93f64"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_init</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">seed</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">subsequence</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412rocrand_initKyKyKyP22rocrand_state_mrg31k3p" title="Link to this definition">#</a><br /></dt>
<dd><p>Initializes MRG31K3P state. </p>
<p>Initializes the MRG31K3P generator <code class="docutils literal notranslate"><span class="pre">state</span></code> with the given <code class="docutils literal notranslate"><span class="pre">seed</span></code>, <code class="docutils literal notranslate"><span class="pre">subsequence</span></code>, and <code class="docutils literal notranslate"><span class="pre">offset</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>seed</strong> – Value to use as a seed </p></li>
<li><p><strong>subsequence</strong> – Subsequence to start at </p></li>
<li><p><strong>offset</strong> – Absolute offset into subsequence </p></li>
<li><p><strong>state</strong> – Pointer to state to initialize </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv47rocrandP22rocrand_state_mrg31k3p">
<span id="_CPPv37rocrandP22rocrand_state_mrg31k3p"></span><span id="_CPPv27rocrandP22rocrand_state_mrg31k3p"></span><span id="rocrand__rocrand_state_mrg31k3pP"></span><span class="target" id="group__rocranddevice_1ga1d070a822b17f1c220cdb2dd599f793d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv47rocrandP22rocrand_state_mrg31k3p" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range. </p>
<p>Generates and returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range using MRG31K3P generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Pseudorandom value (32-bit) as an <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49skipaheadyP22rocrand_state_mrg31k3p">
<span id="_CPPv39skipaheadyP22rocrand_state_mrg31k3p"></span><span id="_CPPv29skipaheadyP22rocrand_state_mrg31k3p"></span><span id="skipahead__unsigned-l-l.rocrand_state_mrg31k3pP"></span><span class="target" id="group__rocranddevice_1ga413246e08b91fea4fbf794ac8bbd32e9"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49skipaheadyP22rocrand_state_mrg31k3p" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates MRG31K3P state to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements. </p>
<p>Updates the MRG31K3P state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – Number of elements to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421skipahead_subsequenceyP22rocrand_state_mrg31k3p">
<span id="_CPPv321skipahead_subsequenceyP22rocrand_state_mrg31k3p"></span><span id="_CPPv221skipahead_subsequenceyP22rocrand_state_mrg31k3p"></span><span id="skipahead_subsequence__unsigned-l-l.rocrand_state_mrg31k3pP"></span><span class="target" id="group__rocranddevice_1ga3fa358bc2c13b92de6c469014af30481"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead_subsequence</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">subsequence</span></span>, <span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421skipahead_subsequenceyP22rocrand_state_mrg31k3p" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates MRG31K3P state to skip ahead by <code class="docutils literal notranslate"><span class="pre">subsequence</span></code> subsequences. </p>
<p>Updates the MRG31K3P state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">subsequence</span></code> subsequences. Each subsequence is 2^72 numbers long.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>subsequence</strong> – Number of subsequences to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418skipahead_sequenceyP22rocrand_state_mrg31k3p">
<span id="_CPPv318skipahead_sequenceyP22rocrand_state_mrg31k3p"></span><span id="_CPPv218skipahead_sequenceyP22rocrand_state_mrg31k3p"></span><span id="skipahead_sequence__unsigned-l-l.rocrand_state_mrg31k3pP"></span><span class="target" id="group__rocranddevice_1ga6fc1c84f26d1db78e61ecf6dfee8ef02"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead_sequence</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sequence</span></span>, <span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418skipahead_sequenceyP22rocrand_state_mrg31k3p" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates MRG31K3P state to skip ahead by <code class="docutils literal notranslate"><span class="pre">sequence</span></code> sequences. </p>
<p>Updates the MRG31K3P state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">sequence</span></code> sequences. Each sequence is 2^134 numbers long.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>sequence</strong> – Number of sequences to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412rocrand_initKyKyKyP22rocrand_state_mrg32k3a">
<span id="_CPPv312rocrand_initKyKyKyP22rocrand_state_mrg32k3a"></span><span id="_CPPv212rocrand_initKyKyKyP22rocrand_state_mrg32k3a"></span><span id="rocrand_init__unsigned-l-lC.unsigned-l-lC.unsigned-l-lC.rocrand_state_mrg32k3aP"></span><span class="target" id="group__rocranddevice_1ga4ab313e70bd3823210311d15bfe18328"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_init</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">seed</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">subsequence</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412rocrand_initKyKyKyP22rocrand_state_mrg32k3a" title="Link to this definition">#</a><br /></dt>
<dd><p>Initializes MRG32K3A state. </p>
<p>Initializes the MRG32K3A generator <code class="docutils literal notranslate"><span class="pre">state</span></code> with the given <code class="docutils literal notranslate"><span class="pre">seed</span></code>, <code class="docutils literal notranslate"><span class="pre">subsequence</span></code>, and <code class="docutils literal notranslate"><span class="pre">offset</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>seed</strong> – Value to use as a seed </p></li>
<li><p><strong>subsequence</strong> – Subsequence to start at </p></li>
<li><p><strong>offset</strong> – Absolute offset into subsequence </p></li>
<li><p><strong>state</strong> – Pointer to state to initialize </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv47rocrandP22rocrand_state_mrg32k3a">
<span id="_CPPv37rocrandP22rocrand_state_mrg32k3a"></span><span id="_CPPv27rocrandP22rocrand_state_mrg32k3a"></span><span id="rocrand__rocrand_state_mrg32k3aP"></span><span class="target" id="group__rocranddevice_1gae01cb10d385f67d85509087e183a32c6"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv47rocrandP22rocrand_state_mrg32k3a" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range. </p>
<p>Generates and returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range using MRG32K3A generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Pseudorandom value (32-bit) as an <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49skipaheadyP22rocrand_state_mrg32k3a">
<span id="_CPPv39skipaheadyP22rocrand_state_mrg32k3a"></span><span id="_CPPv29skipaheadyP22rocrand_state_mrg32k3a"></span><span id="skipahead__unsigned-l-l.rocrand_state_mrg32k3aP"></span><span class="target" id="group__rocranddevice_1gad4690ff2abc3d8a3dc01cc5f561c9da3"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49skipaheadyP22rocrand_state_mrg32k3a" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates MRG32K3A state to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements. </p>
<p>Updates the MRG32K3A state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – Number of elements to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421skipahead_subsequenceyP22rocrand_state_mrg32k3a">
<span id="_CPPv321skipahead_subsequenceyP22rocrand_state_mrg32k3a"></span><span id="_CPPv221skipahead_subsequenceyP22rocrand_state_mrg32k3a"></span><span id="skipahead_subsequence__unsigned-l-l.rocrand_state_mrg32k3aP"></span><span class="target" id="group__rocranddevice_1gab718c6d8c234ec277e79112b3784c971"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead_subsequence</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">subsequence</span></span>, <span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421skipahead_subsequenceyP22rocrand_state_mrg32k3a" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates MRG32K3A state to skip ahead by <code class="docutils literal notranslate"><span class="pre">subsequence</span></code> subsequences. </p>
<p>Updates the MRG32K3A state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">subsequence</span></code> subsequences. Each subsequence is 2^76 numbers long.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>subsequence</strong> – Number of subsequences to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418skipahead_sequenceyP22rocrand_state_mrg32k3a">
<span id="_CPPv318skipahead_sequenceyP22rocrand_state_mrg32k3a"></span><span id="_CPPv218skipahead_sequenceyP22rocrand_state_mrg32k3a"></span><span id="skipahead_sequence__unsigned-l-l.rocrand_state_mrg32k3aP"></span><span class="target" id="group__rocranddevice_1gaf5a82e09294f99d0e273dd89d774efbf"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead_sequence</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sequence</span></span>, <span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418skipahead_sequenceyP22rocrand_state_mrg32k3a" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates MRG32K3A state to skip ahead by <code class="docutils literal notranslate"><span class="pre">sequence</span></code> sequences. </p>
<p>Updates the MRG32K3A state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">sequence</span></code> sequences. Each sequence is 2^127 numbers long.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>sequence</strong> – Number of sequences to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_make_state_mtgp32P20rocrand_state_mtgp32A_18mtgp32_fast_paramsiy">
<span id="_CPPv325rocrand_make_state_mtgp32P20rocrand_state_mtgp32A_18mtgp32_fast_paramsiy"></span><span id="_CPPv225rocrand_make_state_mtgp32P20rocrand_state_mtgp32A_18mtgp32_fast_paramsiy"></span><span id="rocrand_make_state_mtgp32__rocrand_state_mtgp32P.mtgp32_fast_paramsA.i.unsigned-l-l"></span><span class="target" id="group__rocranddevice_1ga39837656c6fb57bb88dd10a1a07cdb4b"></span><span class="pre">__host__</span><span class="w"> </span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_make_state_mtgp32</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="n"><span class="pre">mtgp32_fast_params</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">params</span></span><span class="p"><span class="pre">[</span></span><span class="p"><span class="pre">]</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">seed</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_make_state_mtgp32P20rocrand_state_mtgp32A_18mtgp32_fast_paramsiy" title="Link to this definition">#</a><br /></dt>
<dd><p>Initializes MTGP32 states. </p>
<p>Initializes MTGP32 states on the host-side by allocating a state array in host memory, initializes that array, and copies the result to device or host memory.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to an array of states in device or host memory </p></li>
<li><p><strong>params</strong> – Pointer to an array of type mtgp32_fast_params in host memory </p></li>
<li><p><strong>n</strong> – Number of states to initialize </p></li>
<li><p><strong>seed</strong> – Seed value</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_ALLOCATION_FAILED if states could not be initialized</p></li>
<li><p>ROCRAND_STATUS_SUCCESS if states are initialized </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_make_constantA_K18mtgp32_fast_paramsP13mtgp32_params">
<span id="_CPPv321rocrand_make_constantA_K18mtgp32_fast_paramsP13mtgp32_params"></span><span id="_CPPv221rocrand_make_constantA_K18mtgp32_fast_paramsP13mtgp32_params"></span><span id="rocrand_make_constant__mtgp32_fast_paramsCA.mtgp32_paramsP"></span><span class="target" id="group__rocranddevice_1ga814a21dd3196c0466029eaeb54f48b52"></span><span class="pre">__host__</span><span class="w"> </span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_make_constant</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">mtgp32_fast_params</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">params</span></span><span class="p"><span class="pre">[</span></span><span class="p"><span class="pre">]</span></span>, <span class="n"><span class="pre">mtgp32_params</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">p</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_make_constantA_K18mtgp32_fast_paramsP13mtgp32_params" title="Link to this definition">#</a><br /></dt>
<dd><p>Loads parameters for MTGP32. </p>
<p>Loads parameters for use by kernel functions on the host-side and copies the results to the specified location in device memory.</p>
<p>NOTE: Not used as rocrand_make_state_mtgp32 handles loading parameters into state.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>params</strong> – Pointer to an array of type mtgp32_fast_params in host memory </p></li>
<li><p><strong>p</strong> – Pointer to a mtgp32_params structure allocated in device memory</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_ALLOCATION_FAILED if parameters could not be loaded</p></li>
<li><p>ROCRAND_STATUS_SUCCESS if parameters are loaded </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv47rocrandP20rocrand_state_mtgp32">
<span id="_CPPv37rocrandP20rocrand_state_mtgp32"></span><span id="_CPPv27rocrandP20rocrand_state_mtgp32"></span><span id="rocrand__rocrand_state_mtgp32P"></span><span class="target" id="group__rocranddevice_1ga5a7bb1d274a25f14434083ec84e3f6db"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv47rocrandP20rocrand_state_mtgp32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range. </p>
<p>Generates and returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Pseudorandom value (32-bit) as an <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_mtgp32_block_copyP20rocrand_state_mtgp32P20rocrand_state_mtgp32">
<span id="_CPPv325rocrand_mtgp32_block_copyP20rocrand_state_mtgp32P20rocrand_state_mtgp32"></span><span id="_CPPv225rocrand_mtgp32_block_copyP20rocrand_state_mtgp32P20rocrand_state_mtgp32"></span><span id="rocrand_mtgp32_block_copy__rocrand_state_mtgp32P.rocrand_state_mtgp32P"></span><span class="target" id="group__rocranddevice_1ga226c9907e3ffc21ebe626f9ffc1bed78"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_mtgp32_block_copy</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dest</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_mtgp32_block_copyP20rocrand_state_mtgp32P20rocrand_state_mtgp32" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies MTGP32 state to another state using block of threads. </p>
<p>Copies a MTGP32 state <code class="docutils literal notranslate"><span class="pre">src</span></code> to <code class="docutils literal notranslate"><span class="pre">dest</span></code> using a block of threads efficiently. Example usage would be:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">__global__</span>
<span class="n">void</span> <span class="n">generate_kernel</span><span class="p">(</span><span class="n">rocrand_state_mtgp32</span> <span class="o">*</span> <span class="n">states</span><span class="p">,</span> <span class="n">unsigned</span> <span class="nb">int</span> <span class="o">*</span> <span class="n">output</span><span class="p">,</span> <span class="n">const</span> <span class="n">size_t</span> <span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
     <span class="n">const</span> <span class="n">unsigned</span> <span class="nb">int</span> <span class="n">state_id</span> <span class="o">=</span> <span class="n">blockIdx</span><span class="o">.</span><span class="n">x</span><span class="p">;</span>
     <span class="n">unsigned</span> <span class="nb">int</span> <span class="n">index</span> <span class="o">=</span> <span class="n">blockIdx</span><span class="o">.</span><span class="n">x</span> <span class="o">*</span> <span class="n">blockDim</span><span class="o">.</span><span class="n">x</span> <span class="o">+</span> <span class="n">threadIdx</span><span class="o">.</span><span class="n">x</span><span class="p">;</span>
     <span class="n">unsigned</span> <span class="nb">int</span> <span class="n">stride</span> <span class="o">=</span> <span class="n">gridDim</span><span class="o">.</span><span class="n">x</span> <span class="o">*</span> <span class="n">blockDim</span><span class="o">.</span><span class="n">x</span><span class="p">;</span>

     <span class="n">__shared__</span> <span class="n">GeneratorState</span> <span class="n">state</span><span class="p">;</span>
     <span class="n">rocrand_mtgp32_block_copy</span><span class="p">(</span><span class="o">&amp;</span><span class="n">states</span><span class="p">[</span><span class="n">state_id</span><span class="p">],</span> <span class="o">&amp;</span><span class="n">state</span><span class="p">);</span>

     <span class="k">while</span><span class="p">(</span><span class="n">index</span> <span class="o">&lt;</span> <span class="n">size</span><span class="p">)</span>
     <span class="p">{</span>
         <span class="n">output</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">rocrand</span><span class="p">(</span><span class="o">&amp;</span><span class="n">state</span><span class="p">);</span>
         <span class="n">index</span> <span class="o">+=</span> <span class="n">stride</span><span class="p">;</span>
     <span class="p">}</span>

     <span class="n">rocrand_mtgp32_block_copy</span><span class="p">(</span><span class="o">&amp;</span><span class="n">state</span><span class="p">,</span> <span class="o">&amp;</span><span class="n">states</span><span class="p">[</span><span class="n">state_id</span><span class="p">]);</span>
<span class="p">}</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>src</strong> – Pointer to a state to copy from </p></li>
<li><p><strong>dest</strong> – Pointer to a state to copy to </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_mtgp32_set_paramsP20rocrand_state_mtgp32P13mtgp32_params">
<span id="_CPPv325rocrand_mtgp32_set_paramsP20rocrand_state_mtgp32P13mtgp32_params"></span><span id="_CPPv225rocrand_mtgp32_set_paramsP20rocrand_state_mtgp32P13mtgp32_params"></span><span id="rocrand_mtgp32_set_params__rocrand_state_mtgp32P.mtgp32_paramsP"></span><span class="target" id="group__rocranddevice_1gab23894c8ba2d0ad9a6d86e59d92d09d1"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_mtgp32_set_params</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="n"><span class="pre">mtgp32_params</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">params</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_mtgp32_set_paramsP20rocrand_state_mtgp32P13mtgp32_params" title="Link to this definition">#</a><br /></dt>
<dd><p>Changes parameters of a MTGP32 state. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a MTGP32 state </p></li>
<li><p><strong>params</strong> – Pointer to new parameters </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP27rocrand_state_philox4x32_10">
<span id="_CPPv314rocrand_normalP27rocrand_state_philox4x32_10"></span><span id="_CPPv214rocrand_normalP27rocrand_state_philox4x32_10"></span><span id="rocrand_normal__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1ga6d9a5ff1462d1646a2a78b526cd36983"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_normal2P27rocrand_state_philox4x32_10">
<span id="_CPPv315rocrand_normal2P27rocrand_state_philox4x32_10"></span><span id="_CPPv215rocrand_normal2P27rocrand_state_philox4x32_10"></span><span id="rocrand_normal2__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1gaef372b08f933f418f5c11fcd00493b08"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_normal2P27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_normal4P27rocrand_state_philox4x32_10">
<span id="_CPPv315rocrand_normal4P27rocrand_state_philox4x32_10"></span><span id="_CPPv215rocrand_normal4P27rocrand_state_philox4x32_10"></span><span id="rocrand_normal4__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1gad92ce70496448391bee4411e72f66faa"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float4</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal4</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_normal4P27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns four normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns four normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate four normally distributed values, and returns them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Four normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float4</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP27rocrand_state_philox4x32_10">
<span id="_CPPv321rocrand_normal_doubleP27rocrand_state_philox4x32_10"></span><span id="_CPPv221rocrand_normal_doubleP27rocrand_state_philox4x32_10"></span><span id="rocrand_normal_double__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1ga8e537bf196f569b5d50439466afd651b"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_normal_double2P27rocrand_state_philox4x32_10">
<span id="_CPPv322rocrand_normal_double2P27rocrand_state_philox4x32_10"></span><span id="_CPPv222rocrand_normal_double2P27rocrand_state_philox4x32_10"></span><span id="rocrand_normal_double2__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1ga4f865e28ce1a8cf5ac9e2e1157955138"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_normal_double2P27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_normal_double4P27rocrand_state_philox4x32_10">
<span id="_CPPv322rocrand_normal_double4P27rocrand_state_philox4x32_10"></span><span id="_CPPv222rocrand_normal_double4P27rocrand_state_philox4x32_10"></span><span id="rocrand_normal_double4__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1ga3b9e735ec2db0ab77bf5e5578dbd7897"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double4</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double4</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_normal_double4P27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns four normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns four normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by eight. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate four normally distributed values, and returns them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Four normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values as <code class="docutils literal notranslate"><span class="pre">double4</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP22rocrand_state_mrg31k3p">
<span id="_CPPv314rocrand_normalP22rocrand_state_mrg31k3p"></span><span id="_CPPv214rocrand_normalP22rocrand_state_mrg31k3p"></span><span id="rocrand_normal__rocrand_state_mrg31k3pP"></span><span class="target" id="group__rocranddevice_1gac5558c8c061fd38617c3cadd3c0b3def"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP22rocrand_state_mrg31k3p" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using MRG31k3p generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_normal2P22rocrand_state_mrg31k3p">
<span id="_CPPv315rocrand_normal2P22rocrand_state_mrg31k3p"></span><span id="_CPPv215rocrand_normal2P22rocrand_state_mrg31k3p"></span><span id="rocrand_normal2__rocrand_state_mrg31k3pP"></span><span class="target" id="group__rocranddevice_1ga6ef989c67024a58443fbbc1aba79fa80"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_normal2P22rocrand_state_mrg31k3p" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using MRG31k3p generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP22rocrand_state_mrg31k3p">
<span id="_CPPv321rocrand_normal_doubleP22rocrand_state_mrg31k3p"></span><span id="_CPPv221rocrand_normal_doubleP22rocrand_state_mrg31k3p"></span><span id="rocrand_normal_double__rocrand_state_mrg31k3pP"></span><span class="target" id="group__rocranddevice_1gacf9a6a2bef106591fcc1443b4ca6017e"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP22rocrand_state_mrg31k3p" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using MRG31k3p generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_normal_double2P22rocrand_state_mrg31k3p">
<span id="_CPPv322rocrand_normal_double2P22rocrand_state_mrg31k3p"></span><span id="_CPPv222rocrand_normal_double2P22rocrand_state_mrg31k3p"></span><span id="rocrand_normal_double2__rocrand_state_mrg31k3pP"></span><span class="target" id="group__rocranddevice_1ga19a401d66ffa967928364535394eeabd"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_normal_double2P22rocrand_state_mrg31k3p" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using MRG31k3p generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP22rocrand_state_mrg32k3a">
<span id="_CPPv314rocrand_normalP22rocrand_state_mrg32k3a"></span><span id="_CPPv214rocrand_normalP22rocrand_state_mrg32k3a"></span><span id="rocrand_normal__rocrand_state_mrg32k3aP"></span><span class="target" id="group__rocranddevice_1ga753c1f4cea9489f4b8fa2835b80a6a22"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP22rocrand_state_mrg32k3a" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using MRG32k3a generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_normal2P22rocrand_state_mrg32k3a">
<span id="_CPPv315rocrand_normal2P22rocrand_state_mrg32k3a"></span><span id="_CPPv215rocrand_normal2P22rocrand_state_mrg32k3a"></span><span id="rocrand_normal2__rocrand_state_mrg32k3aP"></span><span class="target" id="group__rocranddevice_1ga457d373f03ea2bbc02022af35d60b2e6"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_normal2P22rocrand_state_mrg32k3a" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using MRG32k3a generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP22rocrand_state_mrg32k3a">
<span id="_CPPv321rocrand_normal_doubleP22rocrand_state_mrg32k3a"></span><span id="_CPPv221rocrand_normal_doubleP22rocrand_state_mrg32k3a"></span><span id="rocrand_normal_double__rocrand_state_mrg32k3aP"></span><span class="target" id="group__rocranddevice_1ga402bffba9154af230fb34f2951f4793b"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP22rocrand_state_mrg32k3a" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using MRG32k3a generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_normal_double2P22rocrand_state_mrg32k3a">
<span id="_CPPv322rocrand_normal_double2P22rocrand_state_mrg32k3a"></span><span id="_CPPv222rocrand_normal_double2P22rocrand_state_mrg32k3a"></span><span id="rocrand_normal_double2__rocrand_state_mrg32k3aP"></span><span class="target" id="group__rocranddevice_1gafa3d21c52aa675d4e59e03809dbc39d3"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_normal_double2P22rocrand_state_mrg32k3a" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using MRG32k3a generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP20rocrand_state_xorwow">
<span id="_CPPv314rocrand_normalP20rocrand_state_xorwow"></span><span id="_CPPv214rocrand_normalP20rocrand_state_xorwow"></span><span id="rocrand_normal__rocrand_state_xorwowP"></span><span class="target" id="group__rocranddevice_1ga5d10d9bc2338b98214b3758814030c08"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP20rocrand_state_xorwow" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using XORWOW generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_normal2P20rocrand_state_xorwow">
<span id="_CPPv315rocrand_normal2P20rocrand_state_xorwow"></span><span id="_CPPv215rocrand_normal2P20rocrand_state_xorwow"></span><span id="rocrand_normal2__rocrand_state_xorwowP"></span><span class="target" id="group__rocranddevice_1gad589fd4371813f03f9de29f83fb04a39"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_normal2P20rocrand_state_xorwow" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using XORWOW generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP20rocrand_state_xorwow">
<span id="_CPPv321rocrand_normal_doubleP20rocrand_state_xorwow"></span><span id="_CPPv221rocrand_normal_doubleP20rocrand_state_xorwow"></span><span id="rocrand_normal_double__rocrand_state_xorwowP"></span><span class="target" id="group__rocranddevice_1ga32018b73555d0916689d2c3b90a015d9"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP20rocrand_state_xorwow" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using XORWOW generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, returns first of them, and saves the second to be returned on the next call.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_normal_double2P20rocrand_state_xorwow">
<span id="_CPPv322rocrand_normal_double2P20rocrand_state_xorwow"></span><span id="_CPPv222rocrand_normal_double2P20rocrand_state_xorwow"></span><span id="rocrand_normal_double2__rocrand_state_xorwowP"></span><span class="target" id="group__rocranddevice_1ga236a89e2894b960a51d8c73315992401"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_normal_double2P20rocrand_state_xorwow" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using XORWOW generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP20rocrand_state_mtgp32">
<span id="_CPPv314rocrand_normalP20rocrand_state_mtgp32"></span><span id="_CPPv214rocrand_normalP20rocrand_state_mtgp32"></span><span id="rocrand_normal__rocrand_state_mtgp32P"></span><span class="target" id="group__rocranddevice_1gaf2acdc6795595327fc24a9492a8606f6"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP20rocrand_state_mtgp32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_normal2P20rocrand_state_mtgp32">
<span id="_CPPv315rocrand_normal2P20rocrand_state_mtgp32"></span><span id="_CPPv215rocrand_normal2P20rocrand_state_mtgp32"></span><span id="rocrand_normal2__rocrand_state_mtgp32P"></span><span class="target" id="group__rocranddevice_1ga31fa02c7148253207f5311dac5c9a649"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_normal2P20rocrand_state_mtgp32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP20rocrand_state_mtgp32">
<span id="_CPPv321rocrand_normal_doubleP20rocrand_state_mtgp32"></span><span id="_CPPv221rocrand_normal_doubleP20rocrand_state_mtgp32"></span><span id="rocrand_normal_double__rocrand_state_mtgp32P"></span><span class="target" id="group__rocranddevice_1gaee05f522a5ff31dd1f9576829a67d4c3"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP20rocrand_state_mtgp32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_normal_double2P20rocrand_state_mtgp32">
<span id="_CPPv322rocrand_normal_double2P20rocrand_state_mtgp32"></span><span id="_CPPv222rocrand_normal_double2P20rocrand_state_mtgp32"></span><span id="rocrand_normal_double2__rocrand_state_mtgp32P"></span><span class="target" id="group__rocranddevice_1ga2a07a4d9ec70707795a812060160d631"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_normal_double2P20rocrand_state_mtgp32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP21rocrand_state_sobol32">
<span id="_CPPv314rocrand_normalP21rocrand_state_sobol32"></span><span id="_CPPv214rocrand_normalP21rocrand_state_sobol32"></span><span id="rocrand_normal__rocrand_state_sobol32P"></span><span class="target" id="group__rocranddevice_1gafcfa4b5fcfd50a36e8506ee9efd5511d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP21rocrand_state_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP21rocrand_state_sobol32">
<span id="_CPPv321rocrand_normal_doubleP21rocrand_state_sobol32"></span><span id="_CPPv221rocrand_normal_doubleP21rocrand_state_sobol32"></span><span id="rocrand_normal_double__rocrand_state_sobol32P"></span><span class="target" id="group__rocranddevice_1ga1d2f8e50aa46181da047a3792bb1579a"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP21rocrand_state_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP31rocrand_state_scrambled_sobol32">
<span id="_CPPv314rocrand_normalP31rocrand_state_scrambled_sobol32"></span><span id="_CPPv214rocrand_normalP31rocrand_state_scrambled_sobol32"></span><span id="rocrand_normal__rocrand_state_scrambled_sobol32P"></span><span class="target" id="group__rocranddevice_1gae44b3acd8e379a98d0cf8a858cdb3e19"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP31rocrand_state_scrambled_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using SCRAMBLED_SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP31rocrand_state_scrambled_sobol32">
<span id="_CPPv321rocrand_normal_doubleP31rocrand_state_scrambled_sobol32"></span><span id="_CPPv221rocrand_normal_doubleP31rocrand_state_scrambled_sobol32"></span><span id="rocrand_normal_double__rocrand_state_scrambled_sobol32P"></span><span class="target" id="group__rocranddevice_1ga7c58710020e78ee188a9ae0d45d2b066"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP31rocrand_state_scrambled_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using SCRAMBLED_SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP21rocrand_state_sobol64">
<span id="_CPPv314rocrand_normalP21rocrand_state_sobol64"></span><span id="_CPPv214rocrand_normalP21rocrand_state_sobol64"></span><span id="rocrand_normal__rocrand_state_sobol64P"></span><span class="target" id="group__rocranddevice_1gabdd28e677f1056672a7bffabab24c395"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP21rocrand_state_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP21rocrand_state_sobol64">
<span id="_CPPv321rocrand_normal_doubleP21rocrand_state_sobol64"></span><span id="_CPPv221rocrand_normal_doubleP21rocrand_state_sobol64"></span><span id="rocrand_normal_double__rocrand_state_sobol64P"></span><span class="target" id="group__rocranddevice_1ga85d634f345a281246bdcfc38702b1583"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP21rocrand_state_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP31rocrand_state_scrambled_sobol64">
<span id="_CPPv314rocrand_normalP31rocrand_state_scrambled_sobol64"></span><span id="_CPPv214rocrand_normalP31rocrand_state_scrambled_sobol64"></span><span id="rocrand_normal__rocrand_state_scrambled_sobol64P"></span><span class="target" id="group__rocranddevice_1ga3a2a90f2397e108df8d6f841afc15485"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP31rocrand_state_scrambled_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using SCRAMBLED_SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP31rocrand_state_scrambled_sobol64">
<span id="_CPPv321rocrand_normal_doubleP31rocrand_state_scrambled_sobol64"></span><span id="_CPPv221rocrand_normal_doubleP31rocrand_state_scrambled_sobol64"></span><span id="rocrand_normal_double__rocrand_state_scrambled_sobol64P"></span><span class="target" id="group__rocranddevice_1ga0c3abab909dede4b2a4a69f7bc3b8977"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP31rocrand_state_scrambled_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using SCRAMBLED_SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP21rocrand_state_lfsr113">
<span id="_CPPv314rocrand_normalP21rocrand_state_lfsr113"></span><span id="_CPPv214rocrand_normalP21rocrand_state_lfsr113"></span><span id="rocrand_normal__rocrand_state_lfsr113P"></span><span class="target" id="group__rocranddevice_1gad9b117f9239c536063e229eeaee76d7a"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP21rocrand_state_lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_normal2P21rocrand_state_lfsr113">
<span id="_CPPv315rocrand_normal2P21rocrand_state_lfsr113"></span><span id="_CPPv215rocrand_normal2P21rocrand_state_lfsr113"></span><span id="rocrand_normal2__rocrand_state_lfsr113P"></span><span class="target" id="group__rocranddevice_1gaf65ce68bf5091fb3171fe1471550c705"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_normal2P21rocrand_state_lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP21rocrand_state_lfsr113">
<span id="_CPPv321rocrand_normal_doubleP21rocrand_state_lfsr113"></span><span id="_CPPv221rocrand_normal_doubleP21rocrand_state_lfsr113"></span><span id="rocrand_normal_double__rocrand_state_lfsr113P"></span><span class="target" id="group__rocranddevice_1gad75d24af18f55e52952a0b0e4d3eeba2"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP21rocrand_state_lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_normal_double2P21rocrand_state_lfsr113">
<span id="_CPPv322rocrand_normal_double2P21rocrand_state_lfsr113"></span><span id="_CPPv222rocrand_normal_double2P21rocrand_state_lfsr113"></span><span id="rocrand_normal_double2__rocrand_state_lfsr113P"></span><span class="target" id="group__rocranddevice_1ga34f1edd0dccb1a32e0c99da137f5d347"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_normal_double2P21rocrand_state_lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP29rocrand_state_threefry2x32_20">
<span id="_CPPv314rocrand_normalP29rocrand_state_threefry2x32_20"></span><span id="_CPPv214rocrand_normalP29rocrand_state_threefry2x32_20"></span><span id="rocrand_normal__rocrand_state_threefry2x32_20P"></span><span class="target" id="group__rocranddevice_1gad3277dfa5fb8b259513c280ebad7d4ad"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP29rocrand_state_threefry2x32_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_normal2P29rocrand_state_threefry2x32_20">
<span id="_CPPv315rocrand_normal2P29rocrand_state_threefry2x32_20"></span><span id="_CPPv215rocrand_normal2P29rocrand_state_threefry2x32_20"></span><span id="rocrand_normal2__rocrand_state_threefry2x32_20P"></span><span class="target" id="group__rocranddevice_1gafa7100e44b5f43ac0775929ef8108679"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_normal2P29rocrand_state_threefry2x32_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP29rocrand_state_threefry2x32_20">
<span id="_CPPv321rocrand_normal_doubleP29rocrand_state_threefry2x32_20"></span><span id="_CPPv221rocrand_normal_doubleP29rocrand_state_threefry2x32_20"></span><span id="rocrand_normal_double__rocrand_state_threefry2x32_20P"></span><span class="target" id="group__rocranddevice_1ga209523da54b02f9ef180c98e7be55a04"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP29rocrand_state_threefry2x32_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_normal_double2P29rocrand_state_threefry2x32_20">
<span id="_CPPv322rocrand_normal_double2P29rocrand_state_threefry2x32_20"></span><span id="_CPPv222rocrand_normal_double2P29rocrand_state_threefry2x32_20"></span><span id="rocrand_normal_double2__rocrand_state_threefry2x32_20P"></span><span class="target" id="group__rocranddevice_1ga7b7ea65841293f119ba8648506847576"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_normal_double2P29rocrand_state_threefry2x32_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP29rocrand_state_threefry2x64_20">
<span id="_CPPv314rocrand_normalP29rocrand_state_threefry2x64_20"></span><span id="_CPPv214rocrand_normalP29rocrand_state_threefry2x64_20"></span><span id="rocrand_normal__rocrand_state_threefry2x64_20P"></span><span class="target" id="group__rocranddevice_1ga65fb63b1e78510900b2a2d8532887fa7"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP29rocrand_state_threefry2x64_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_normal2P29rocrand_state_threefry2x64_20">
<span id="_CPPv315rocrand_normal2P29rocrand_state_threefry2x64_20"></span><span id="_CPPv215rocrand_normal2P29rocrand_state_threefry2x64_20"></span><span id="rocrand_normal2__rocrand_state_threefry2x64_20P"></span><span class="target" id="group__rocranddevice_1ga9be9f47814b768a4a5b54f00740165d6"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_normal2P29rocrand_state_threefry2x64_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP29rocrand_state_threefry2x64_20">
<span id="_CPPv321rocrand_normal_doubleP29rocrand_state_threefry2x64_20"></span><span id="_CPPv221rocrand_normal_doubleP29rocrand_state_threefry2x64_20"></span><span id="rocrand_normal_double__rocrand_state_threefry2x64_20P"></span><span class="target" id="group__rocranddevice_1ga1400aa2224890f959be7c4ba5e8bbbf1"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP29rocrand_state_threefry2x64_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_normal_double2P29rocrand_state_threefry2x64_20">
<span id="_CPPv322rocrand_normal_double2P29rocrand_state_threefry2x64_20"></span><span id="_CPPv222rocrand_normal_double2P29rocrand_state_threefry2x64_20"></span><span id="rocrand_normal_double2__rocrand_state_threefry2x64_20P"></span><span class="target" id="group__rocranddevice_1ga38f649c15f72784f492bbe33ddb675fc"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_normal_double2P29rocrand_state_threefry2x64_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP29rocrand_state_threefry4x32_20">
<span id="_CPPv314rocrand_normalP29rocrand_state_threefry4x32_20"></span><span id="_CPPv214rocrand_normalP29rocrand_state_threefry4x32_20"></span><span id="rocrand_normal__rocrand_state_threefry4x32_20P"></span><span class="target" id="group__rocranddevice_1ga8548efde6d279c3f81751629f9fd56bb"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP29rocrand_state_threefry4x32_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_normal2P29rocrand_state_threefry4x32_20">
<span id="_CPPv315rocrand_normal2P29rocrand_state_threefry4x32_20"></span><span id="_CPPv215rocrand_normal2P29rocrand_state_threefry4x32_20"></span><span id="rocrand_normal2__rocrand_state_threefry4x32_20P"></span><span class="target" id="group__rocranddevice_1ga1f6a5271d5e8d77d7752a6bc5277bfaf"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_normal2P29rocrand_state_threefry4x32_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP29rocrand_state_threefry4x32_20">
<span id="_CPPv321rocrand_normal_doubleP29rocrand_state_threefry4x32_20"></span><span id="_CPPv221rocrand_normal_doubleP29rocrand_state_threefry4x32_20"></span><span id="rocrand_normal_double__rocrand_state_threefry4x32_20P"></span><span class="target" id="group__rocranddevice_1ga564ac0007471ddcd03c3ec115b3b8425"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP29rocrand_state_threefry4x32_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_normal_double2P29rocrand_state_threefry4x32_20">
<span id="_CPPv322rocrand_normal_double2P29rocrand_state_threefry4x32_20"></span><span id="_CPPv222rocrand_normal_double2P29rocrand_state_threefry4x32_20"></span><span id="rocrand_normal_double2__rocrand_state_threefry4x32_20P"></span><span class="target" id="group__rocranddevice_1ga67c84c14850c41878ecc6fb9eb7ad273"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_normal_double2P29rocrand_state_threefry4x32_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_normalP29rocrand_state_threefry4x64_20">
<span id="_CPPv314rocrand_normalP29rocrand_state_threefry4x64_20"></span><span id="_CPPv214rocrand_normalP29rocrand_state_threefry4x64_20"></span><span id="rocrand_normal__rocrand_state_threefry4x64_20P"></span><span class="target" id="group__rocranddevice_1gabd21db109a8d5b81974274970e325c52"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414rocrand_normalP29rocrand_state_threefry4x64_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_normal2P29rocrand_state_threefry4x64_20">
<span id="_CPPv315rocrand_normal2P29rocrand_state_threefry4x64_20"></span><span id="_CPPv215rocrand_normal2P29rocrand_state_threefry4x64_20"></span><span id="rocrand_normal2__rocrand_state_threefry4x64_20P"></span><span class="target" id="group__rocranddevice_1ga4f7cd390df2b95834e5e4e8cb719495e"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_normal2P29rocrand_state_threefry4x64_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value as <code class="docutils literal notranslate"><span class="pre">float2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_normal_doubleP29rocrand_state_threefry4x64_20">
<span id="_CPPv321rocrand_normal_doubleP29rocrand_state_threefry4x64_20"></span><span id="_CPPv221rocrand_normal_doubleP29rocrand_state_threefry4x64_20"></span><span id="rocrand_normal_double__rocrand_state_threefry4x64_20P"></span><span class="target" id="group__rocranddevice_1ga08029a1d3a6cf353b3831e0f170e01d7"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_normal_doubleP29rocrand_state_threefry4x64_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value. </p>
<p>Generates and returns a normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_normal_double2P29rocrand_state_threefry4x64_20">
<span id="_CPPv322rocrand_normal_double2P29rocrand_state_threefry4x64_20"></span><span id="_CPPv222rocrand_normal_double2P29rocrand_state_threefry4x64_20"></span><span id="rocrand_normal_double2__rocrand_state_threefry4x64_20P"></span><span class="target" id="group__rocranddevice_1ga44b4f85f0aed2a30451d2ff4a8c03ea3"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_normal_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_normal_double2P29rocrand_state_threefry4x64_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates and returns two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two. Used normal distribution has mean value equal to 0.0f, and standard deviation equal to 1.0f. The function uses the Box-Muller transform method to generate two normally distributed values, and returns both of them.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value as <code class="docutils literal notranslate"><span class="pre">double2</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412rocrand_initKyKyKyP27rocrand_state_philox4x32_10">
<span id="_CPPv312rocrand_initKyKyKyP27rocrand_state_philox4x32_10"></span><span id="_CPPv212rocrand_initKyKyKyP27rocrand_state_philox4x32_10"></span><span id="rocrand_init__unsigned-l-lC.unsigned-l-lC.unsigned-l-lC.rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1ga430f31fb3c3854584bb0072643b3a54d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_init</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">seed</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">subsequence</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412rocrand_initKyKyKyP27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Initializes Philox state. </p>
<p>Initializes the Philox generator <code class="docutils literal notranslate"><span class="pre">state</span></code> with the given <code class="docutils literal notranslate"><span class="pre">seed</span></code>, <code class="docutils literal notranslate"><span class="pre">subsequence</span></code>, and <code class="docutils literal notranslate"><span class="pre">offset</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>seed</strong> – Value to use as a seed </p></li>
<li><p><strong>subsequence</strong> – Subsequence to start at </p></li>
<li><p><strong>offset</strong> – Absolute offset into subsequence </p></li>
<li><p><strong>state</strong> – Pointer to state to initialize </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv47rocrandP27rocrand_state_philox4x32_10">
<span id="_CPPv37rocrandP27rocrand_state_philox4x32_10"></span><span id="_CPPv27rocrandP27rocrand_state_philox4x32_10"></span><span id="rocrand__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1gaabee10972105cf6306a0a9f5bc93e4d8"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv47rocrandP27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range. </p>
<p>Generates and returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Pseudorandom value (32-bit) as an <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv48rocrand4P27rocrand_state_philox4x32_10">
<span id="_CPPv38rocrand4P27rocrand_state_philox4x32_10"></span><span id="_CPPv28rocrand4P27rocrand_state_philox4x32_10"></span><span id="rocrand4__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1ga75b36b141d3ca288d6e5332aaa34a06c"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">uint4</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand4</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv48rocrand4P27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns four uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values from [0; 2^32 - 1] range. </p>
<p>Generates and returns four uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values from [0; 2^32 - 1] range using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by four positions.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Four pseudorandom values (32-bit) as an <code class="docutils literal notranslate"><span class="pre">uint4</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49skipaheadyP27rocrand_state_philox4x32_10">
<span id="_CPPv39skipaheadyP27rocrand_state_philox4x32_10"></span><span id="_CPPv29skipaheadyP27rocrand_state_philox4x32_10"></span><span id="skipahead__unsigned-l-l.rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1ga3c9f4ef124c9d36148398ee29c34ec45"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49skipaheadyP27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates Philox state to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements. </p>
<p>Updates the Philox generator state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – Number of elements to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421skipahead_subsequenceyP27rocrand_state_philox4x32_10">
<span id="_CPPv321skipahead_subsequenceyP27rocrand_state_philox4x32_10"></span><span id="_CPPv221skipahead_subsequenceyP27rocrand_state_philox4x32_10"></span><span id="skipahead_subsequence__unsigned-l-l.rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1gad214a2ef867b636423e661f97d8608f5"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead_subsequence</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">subsequence</span></span>, <span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421skipahead_subsequenceyP27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates Philox state to skip ahead by <code class="docutils literal notranslate"><span class="pre">subsequence</span></code> subsequences. </p>
<p>Updates the Philox generator state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">subsequence</span></code> subsequences. Each subsequence is 4 * 2^64 numbers long.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>subsequence</strong> – Number of subsequences to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418skipahead_sequenceyP27rocrand_state_philox4x32_10">
<span id="_CPPv318skipahead_sequenceyP27rocrand_state_philox4x32_10"></span><span id="_CPPv218skipahead_sequenceyP27rocrand_state_philox4x32_10"></span><span id="skipahead_sequence__unsigned-l-l.rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1gaa7027291eff0d89adc44e4a5f79bb7c4"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead_sequence</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sequence</span></span>, <span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418skipahead_sequenceyP27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates Philox state to skip ahead by <code class="docutils literal notranslate"><span class="pre">sequence</span></code> sequences. </p>
<p>Updates the Philox generator state in <code class="docutils literal notranslate"><span class="pre">state</span></code> skipping <code class="docutils literal notranslate"><span class="pre">sequence</span></code> sequences ahead. For Philox each sequence is 4 * 2^64 numbers long (equal to the size of a subsequence).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>sequence</strong> – Number of sequences to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP27rocrand_state_philox4x32_10d">
<span id="_CPPv315rocrand_poissonP27rocrand_state_philox4x32_10d"></span><span id="_CPPv215rocrand_poissonP27rocrand_state_philox4x32_10d"></span><span id="rocrand_poisson__rocrand_state_philox4x32_10P.double"></span><span class="target" id="group__rocranddevice_1ga0e08a23b6ab84de34a65cff37f40ab49"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP27rocrand_state_philox4x32_10d" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using Philox generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by a variable amount.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_poisson4P27rocrand_state_philox4x32_10d">
<span id="_CPPv316rocrand_poisson4P27rocrand_state_philox4x32_10d"></span><span id="_CPPv216rocrand_poisson4P27rocrand_state_philox4x32_10d"></span><span id="rocrand_poisson4__rocrand_state_philox4x32_10P.double"></span><span class="target" id="group__rocranddevice_1ga412d08c8771fe30aff6a0f085c38042c"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">uint4</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson4</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_poisson4P27rocrand_state_philox4x32_10d" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns four Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using Philox generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by a variable amount.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Four Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values as <code class="docutils literal notranslate"><span class="pre">uint4</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP22rocrand_state_mrg31k3pd">
<span id="_CPPv315rocrand_poissonP22rocrand_state_mrg31k3pd"></span><span id="_CPPv215rocrand_poissonP22rocrand_state_mrg31k3pd"></span><span id="rocrand_poisson__rocrand_state_mrg31k3pP.double"></span><span class="target" id="group__rocranddevice_1ga590eb7a4c6015978ddd1e629f9f0b3ec"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP22rocrand_state_mrg31k3pd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using MRG31k3p generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using MRG31k3p generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by a variable amount.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP22rocrand_state_mrg32k3ad">
<span id="_CPPv315rocrand_poissonP22rocrand_state_mrg32k3ad"></span><span id="_CPPv215rocrand_poissonP22rocrand_state_mrg32k3ad"></span><span id="rocrand_poisson__rocrand_state_mrg32k3aP.double"></span><span class="target" id="group__rocranddevice_1ga329f6846b6672a335e495b5441036886"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP22rocrand_state_mrg32k3ad" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using MRG32k3a generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using MRG32k3a generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by a variable amount.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP20rocrand_state_xorwowd">
<span id="_CPPv315rocrand_poissonP20rocrand_state_xorwowd"></span><span id="_CPPv215rocrand_poissonP20rocrand_state_xorwowd"></span><span id="rocrand_poisson__rocrand_state_xorwowP.double"></span><span class="target" id="group__rocranddevice_1gaff45971267b84e7c846497b6e7a899d1"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP20rocrand_state_xorwowd" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using XORWOW generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using XORWOW generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by a variable amount.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP20rocrand_state_mtgp32d">
<span id="_CPPv315rocrand_poissonP20rocrand_state_mtgp32d"></span><span id="_CPPv215rocrand_poissonP20rocrand_state_mtgp32d"></span><span id="rocrand_poisson__rocrand_state_mtgp32P.double"></span><span class="target" id="group__rocranddevice_1ga03eb2915f12ab6b2596fdf8ea5a36184"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP20rocrand_state_mtgp32d" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using MTGP32 generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP21rocrand_state_sobol32d">
<span id="_CPPv315rocrand_poissonP21rocrand_state_sobol32d"></span><span id="_CPPv215rocrand_poissonP21rocrand_state_sobol32d"></span><span id="rocrand_poisson__rocrand_state_sobol32P.double"></span><span class="target" id="group__rocranddevice_1gaba4d10c608906eeeeb763f44f04ec273"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP21rocrand_state_sobol32d" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using SOBOL32 generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP31rocrand_state_scrambled_sobol32d">
<span id="_CPPv315rocrand_poissonP31rocrand_state_scrambled_sobol32d"></span><span id="_CPPv215rocrand_poissonP31rocrand_state_scrambled_sobol32d"></span><span id="rocrand_poisson__rocrand_state_scrambled_sobol32P.double"></span><span class="target" id="group__rocranddevice_1ga549bdc698a75313a416edf234e78aee8"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP31rocrand_state_scrambled_sobol32d" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using SCRAMBLED_SOBOL32 generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using SCRAMBLED_SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP21rocrand_state_sobol64d">
<span id="_CPPv315rocrand_poissonP21rocrand_state_sobol64d"></span><span id="_CPPv215rocrand_poissonP21rocrand_state_sobol64d"></span><span id="rocrand_poisson__rocrand_state_sobol64P.double"></span><span class="target" id="group__rocranddevice_1ga74eb26e6b3cd32c1e23fbeb68a82f269"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP21rocrand_state_sobol64d" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using SOBOL64 generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP31rocrand_state_scrambled_sobol64d">
<span id="_CPPv315rocrand_poissonP31rocrand_state_scrambled_sobol64d"></span><span id="_CPPv215rocrand_poissonP31rocrand_state_scrambled_sobol64d"></span><span id="rocrand_poisson__rocrand_state_scrambled_sobol64P.double"></span><span class="target" id="group__rocranddevice_1ga01d0346b2fd49601bc3a928bf31cdf23"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP31rocrand_state_scrambled_sobol64d" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using SCRAMBLED_SOBOL64 generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using SCRAMBLED_SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP21rocrand_state_lfsr113d">
<span id="_CPPv315rocrand_poissonP21rocrand_state_lfsr113d"></span><span id="_CPPv215rocrand_poissonP21rocrand_state_lfsr113d"></span><span id="rocrand_poisson__rocrand_state_lfsr113P.double"></span><span class="target" id="group__rocranddevice_1gaefbe4fad5dcfb9077c7b6567d45af0d8"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP21rocrand_state_lfsr113d" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using LFSR113 generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP29rocrand_state_threefry2x32_20d">
<span id="_CPPv315rocrand_poissonP29rocrand_state_threefry2x32_20d"></span><span id="_CPPv215rocrand_poissonP29rocrand_state_threefry2x32_20d"></span><span id="rocrand_poisson__rocrand_state_threefry2x32_20P.double"></span><span class="target" id="group__rocranddevice_1ga5b5f76ebb5d4ef59242ff64ff7d20010"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP29rocrand_state_threefry2x32_20d" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using ThreeFry generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP29rocrand_state_threefry2x64_20d">
<span id="_CPPv315rocrand_poissonP29rocrand_state_threefry2x64_20d"></span><span id="_CPPv215rocrand_poissonP29rocrand_state_threefry2x64_20d"></span><span id="rocrand_poisson__rocrand_state_threefry2x64_20P.double"></span><span class="target" id="group__rocranddevice_1ga5c35ce1c488ad7f88db2f6258c27640d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP29rocrand_state_threefry2x64_20d" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using ThreeFry generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP29rocrand_state_threefry4x32_20d">
<span id="_CPPv315rocrand_poissonP29rocrand_state_threefry4x32_20d"></span><span id="_CPPv215rocrand_poissonP29rocrand_state_threefry4x32_20d"></span><span id="rocrand_poisson__rocrand_state_threefry4x32_20P.double"></span><span class="target" id="group__rocranddevice_1ga4040729bb6aee652efa047e777a24671"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP29rocrand_state_threefry4x32_20d" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using ThreeFry generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_poissonP29rocrand_state_threefry4x64_20d">
<span id="_CPPv315rocrand_poissonP29rocrand_state_threefry4x64_20d"></span><span id="_CPPv215rocrand_poissonP29rocrand_state_threefry4x64_20d"></span><span id="rocrand_poisson__rocrand_state_threefry4x64_20P.double"></span><span class="target" id="group__rocranddevice_1ga914665ffe48aed269bd164f04172f875"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_poissonP29rocrand_state_threefry4x64_20d" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> using ThreeFry generator. </p>
<p>Generates and returns Poisson-distributed distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> values using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – Pointer to a state to use </p></li>
<li><p><strong>lambda</strong> – Lambda parameter of the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Poisson-distributed <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412rocrand_initPKjKjKjP31rocrand_state_scrambled_sobol32">
<span id="_CPPv312rocrand_initPKjKjKjP31rocrand_state_scrambled_sobol32"></span><span id="_CPPv212rocrand_initPKjKjKjP31rocrand_state_scrambled_sobol32"></span><span id="rocrand_init__unsigned-iCP.unsigned-iC.unsigned-iC.rocrand_state_scrambled_sobol32P"></span><span class="target" id="group__rocranddevice_1gaa1739b2e5a2d4227cc770fe2d0721e0c"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_init</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">vectors</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">scramble_constant</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_scrambled_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412rocrand_initPKjKjKjP31rocrand_state_scrambled_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Initialize scrambled_sobol32 state. </p>
<p>Initializes the scrambled_sobol32 generator <code class="docutils literal notranslate"><span class="pre">state</span></code> with the given direction <code class="docutils literal notranslate"><span class="pre">vectors</span></code> and <code class="docutils literal notranslate"><span class="pre">offset</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>vectors</strong> – Direction vectors </p></li>
<li><p><strong>scramble_constant</strong> – Constant used for scrambling the sequence </p></li>
<li><p><strong>offset</strong> – Absolute offset into sequence </p></li>
<li><p><strong>state</strong> – Pointer to state to initialize </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv47rocrandP31rocrand_state_scrambled_sobol32">
<span id="_CPPv37rocrandP31rocrand_state_scrambled_sobol32"></span><span id="_CPPv27rocrandP31rocrand_state_scrambled_sobol32"></span><span id="rocrand__rocrand_state_scrambled_sobol32P"></span><span class="target" id="group__rocranddevice_1ga4e3edff459103f1d0ee59160dd473350"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv47rocrandP31rocrand_state_scrambled_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range. </p>
<p>Generates and returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range using scrambled_sobol32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Quasirandom value (32-bit) as an <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49skipaheadyP31rocrand_state_scrambled_sobol32">
<span id="_CPPv39skipaheadyP31rocrand_state_scrambled_sobol32"></span><span id="_CPPv29skipaheadyP31rocrand_state_scrambled_sobol32"></span><span id="skipahead__unsigned-l-l.rocrand_state_scrambled_sobol32P"></span><span class="target" id="group__rocranddevice_1gaca68611a1b0b7b4c3fdfdca62c1a3a9e"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_scrambled_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49skipaheadyP31rocrand_state_scrambled_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates SCRAMBLED_SOBOL32 state to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements. </p>
<p>Updates the SCRAMBLED_SOBOL32 state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – Number of elements to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412rocrand_initPKyKyKjP31rocrand_state_scrambled_sobol64">
<span id="_CPPv312rocrand_initPKyKyKjP31rocrand_state_scrambled_sobol64"></span><span id="_CPPv212rocrand_initPKyKyKjP31rocrand_state_scrambled_sobol64"></span><span id="rocrand_init__unsigned-l-l-iCP.unsigned-l-l-iC.unsigned-iC.rocrand_state_scrambled_sobol64P"></span><span class="target" id="group__rocranddevice_1gae2e82fe9741262111f9cfe10e63c1106"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_init</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">vectors</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">scramble_constant</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_scrambled_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412rocrand_initPKyKyKjP31rocrand_state_scrambled_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Initialize scrambled_sobol64 state. </p>
<p>Initializes the scrambled_sobol64 generator <code class="docutils literal notranslate"><span class="pre">state</span></code> with the given direction <code class="docutils literal notranslate"><span class="pre">vectors</span></code> and <code class="docutils literal notranslate"><span class="pre">offset</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>vectors</strong> – Direction vectors </p></li>
<li><p><strong>scramble_constant</strong> – Constant used for scrambling the sequence </p></li>
<li><p><strong>offset</strong> – Absolute offset into sequence </p></li>
<li><p><strong>state</strong> – Pointer to state to initialize </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv47rocrandP31rocrand_state_scrambled_sobol64">
<span id="_CPPv37rocrandP31rocrand_state_scrambled_sobol64"></span><span id="_CPPv27rocrandP31rocrand_state_scrambled_sobol64"></span><span id="rocrand__rocrand_state_scrambled_sobol64P"></span><span class="target" id="group__rocranddevice_1ga34b5063789e23e65695ac802336c9dba"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv47rocrandP31rocrand_state_scrambled_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span></code> value from [0; 2^64 - 1] range. </p>
<p>Generates and returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span></code> value from [0; 2^64 - 1] range using scrambled_sobol64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Quasirandom value (64-bit) as an <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49skipaheadyP31rocrand_state_scrambled_sobol64">
<span id="_CPPv39skipaheadyP31rocrand_state_scrambled_sobol64"></span><span id="_CPPv29skipaheadyP31rocrand_state_scrambled_sobol64"></span><span id="skipahead__unsigned-l-l.rocrand_state_scrambled_sobol64P"></span><span class="target" id="group__rocranddevice_1ga38fa00d2540682b762115e7b76bfece7"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_scrambled_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49skipaheadyP31rocrand_state_scrambled_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates scrambled_sobol64 state to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements. </p>
<p>Updates the scrambled_sobol64 state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – Number of elements to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412rocrand_initPKjKjP21rocrand_state_sobol32">
<span id="_CPPv312rocrand_initPKjKjP21rocrand_state_sobol32"></span><span id="_CPPv212rocrand_initPKjKjP21rocrand_state_sobol32"></span><span id="rocrand_init__unsigned-iCP.unsigned-iC.rocrand_state_sobol32P"></span><span class="target" id="group__rocranddevice_1ga72b62d9fafbfb11505fb7cc901ada453"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_init</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">vectors</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412rocrand_initPKjKjP21rocrand_state_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Initialize SOBOL32 state. </p>
<p>Initializes the SOBOL32 generator <code class="docutils literal notranslate"><span class="pre">state</span></code> with the given direction <code class="docutils literal notranslate"><span class="pre">vectors</span></code> and <code class="docutils literal notranslate"><span class="pre">offset</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>vectors</strong> – Direction vectors </p></li>
<li><p><strong>offset</strong> – Absolute offset into sequence </p></li>
<li><p><strong>state</strong> – Pointer to state to initialize </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv47rocrandP21rocrand_state_sobol32">
<span id="_CPPv37rocrandP21rocrand_state_sobol32"></span><span id="_CPPv27rocrandP21rocrand_state_sobol32"></span><span id="rocrand__rocrand_state_sobol32P"></span><span class="target" id="group__rocranddevice_1ga04aefd88dfb077ad61de5120b97cc89d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv47rocrandP21rocrand_state_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range. </p>
<p>Generates and returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range using Sobol32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Quasirandom value (32-bit) as an <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49skipaheadyP21rocrand_state_sobol32">
<span id="_CPPv39skipaheadyP21rocrand_state_sobol32"></span><span id="_CPPv29skipaheadyP21rocrand_state_sobol32"></span><span id="skipahead__unsigned-l-l.rocrand_state_sobol32P"></span><span class="target" id="group__rocranddevice_1ga9284c4bb61bfbfbbb55b5bc4d0d2ce72"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49skipaheadyP21rocrand_state_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates SOBOL32 state to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements. </p>
<p>Updates the SOBOL32 state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – Number of elements to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412rocrand_initPKyKjP21rocrand_state_sobol64">
<span id="_CPPv312rocrand_initPKyKjP21rocrand_state_sobol64"></span><span id="_CPPv212rocrand_initPKyKjP21rocrand_state_sobol64"></span><span id="rocrand_init__unsigned-l-l-iCP.unsigned-iC.rocrand_state_sobol64P"></span><span class="target" id="group__rocranddevice_1gab1fcb9054e7399918ca560e8f8fe7131"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_init</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">vectors</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412rocrand_initPKyKjP21rocrand_state_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Initialize sobol64 state. </p>
<p>Initializes the sobol64 generator <code class="docutils literal notranslate"><span class="pre">state</span></code> with the given direction <code class="docutils literal notranslate"><span class="pre">vectors</span></code> and <code class="docutils literal notranslate"><span class="pre">offset</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>vectors</strong> – Direction vectors </p></li>
<li><p><strong>offset</strong> – Absolute offset into sequence </p></li>
<li><p><strong>state</strong> – Pointer to state to initialize </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv47rocrandP21rocrand_state_sobol64">
<span id="_CPPv37rocrandP21rocrand_state_sobol64"></span><span id="_CPPv27rocrandP21rocrand_state_sobol64"></span><span id="rocrand__rocrand_state_sobol64P"></span><span class="target" id="group__rocranddevice_1ga3eb6040d189c1894a91d06eb655ce6ad"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv47rocrandP21rocrand_state_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span></code> value from [0; 2^64 - 1] range. </p>
<p>Generates and returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span></code> value from [0; 2^64 - 1] range using sobol64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Quasirandom value (64-bit) as an <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49skipaheadyP21rocrand_state_sobol64">
<span id="_CPPv39skipaheadyP21rocrand_state_sobol64"></span><span id="_CPPv29skipaheadyP21rocrand_state_sobol64"></span><span id="skipahead__unsigned-l-l-i.rocrand_state_sobol64P"></span><span class="target" id="group__rocranddevice_1ga64a7081d8de83928f938d7981cb446ef"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49skipaheadyP21rocrand_state_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates sobol64 state to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements. </p>
<p>Updates the sobol64 state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – Number of elements to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP27rocrand_state_philox4x32_10">
<span id="_CPPv315rocrand_uniformP27rocrand_state_philox4x32_10"></span><span id="_CPPv215rocrand_uniformP27rocrand_state_philox4x32_10"></span><span id="rocrand_uniform__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1gacef26a9971f1d9a6418807d5bcd2a730"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0f</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0f</span></code>) using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_uniform2P27rocrand_state_philox4x32_10">
<span id="_CPPv316rocrand_uniform2P27rocrand_state_philox4x32_10"></span><span id="_CPPv216rocrand_uniform2P27rocrand_state_philox4x32_10"></span><span id="rocrand_uniform2__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1gadadb530114436b9b2d1e58a9fe048c84"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_uniform2P27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> values from (0; 1] range. </p>
<p>Generates and returns two uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0f</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0f</span></code>) using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values from (0; 1] range as <code class="docutils literal notranslate"><span class="pre">float2</span></code>. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_uniform4P27rocrand_state_philox4x32_10">
<span id="_CPPv316rocrand_uniform4P27rocrand_state_philox4x32_10"></span><span id="_CPPv216rocrand_uniform4P27rocrand_state_philox4x32_10"></span><span id="rocrand_uniform4__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1ga03e764c95a0b9ec87473f65986e8fba7"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">float4</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform4</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_uniform4P27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns four uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> values from (0; 1] range. </p>
<p>Generates and returns four uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0f</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0f</span></code>) using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Four uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values from (0; 1] range as <code class="docutils literal notranslate"><span class="pre">float4</span></code>. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP27rocrand_state_philox4x32_10">
<span id="_CPPv322rocrand_uniform_doubleP27rocrand_state_philox4x32_10"></span><span id="_CPPv222rocrand_uniform_doubleP27rocrand_state_philox4x32_10"></span><span id="rocrand_uniform_double__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1ga879ca4924e517964ab13040019fea916"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423rocrand_uniform_double2P27rocrand_state_philox4x32_10">
<span id="_CPPv323rocrand_uniform_double2P27rocrand_state_philox4x32_10"></span><span id="_CPPv223rocrand_uniform_double2P27rocrand_state_philox4x32_10"></span><span id="rocrand_uniform_double2__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1gaffb7b4dce780501440854493e7a1ac5c"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double2</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423rocrand_uniform_double2P27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns two uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> values from (0; 1] range. </p>
<p>Generates and returns two uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by four.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Two uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values from (0; 1] range as <code class="docutils literal notranslate"><span class="pre">double2</span></code>. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423rocrand_uniform_double4P27rocrand_state_philox4x32_10">
<span id="_CPPv323rocrand_uniform_double4P27rocrand_state_philox4x32_10"></span><span id="_CPPv223rocrand_uniform_double4P27rocrand_state_philox4x32_10"></span><span id="rocrand_uniform_double4__rocrand_state_philox4x32_10P"></span><span class="target" id="group__rocranddevice_1ga304daff0db2417a17d3f69b5d2a42815"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="n"><span class="pre">double4</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double4</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_philox4x32_10</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423rocrand_uniform_double4P27rocrand_state_philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns four uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> values from (0; 1] range. </p>
<p>Generates and returns four uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using Philox generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by eight.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Four uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values from (0; 1] range as <code class="docutils literal notranslate"><span class="pre">double4</span></code>. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP22rocrand_state_mrg31k3p">
<span id="_CPPv315rocrand_uniformP22rocrand_state_mrg31k3p"></span><span id="_CPPv215rocrand_uniformP22rocrand_state_mrg31k3p"></span><span id="rocrand_uniform__rocrand_state_mrg31k3pP"></span><span class="target" id="group__rocranddevice_1ga58ad4b8747f7d6e883936adfdff6026b"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP22rocrand_state_mrg31k3p" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0f</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0f</span></code>) using MRG31K3P generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP22rocrand_state_mrg31k3p">
<span id="_CPPv322rocrand_uniform_doubleP22rocrand_state_mrg31k3p"></span><span id="_CPPv222rocrand_uniform_doubleP22rocrand_state_mrg31k3p"></span><span id="rocrand_uniform_double__rocrand_state_mrg31k3pP"></span><span class="target" id="group__rocranddevice_1gac36ea0d938d8d581c52492712ce4524b"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg31k3p</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP22rocrand_state_mrg31k3p" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using MRG31K3P generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<p>
Note: In this implementation returned <code class="docutils literal notranslate"><span class="pre">double</span></code> value is generated from only 32 random bits (one <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP22rocrand_state_mrg32k3a">
<span id="_CPPv315rocrand_uniformP22rocrand_state_mrg32k3a"></span><span id="_CPPv215rocrand_uniformP22rocrand_state_mrg32k3a"></span><span id="rocrand_uniform__rocrand_state_mrg32k3aP"></span><span class="target" id="group__rocranddevice_1gae3511f6e0a1506dfc29268f8b753633d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP22rocrand_state_mrg32k3a" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0f</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0f</span></code>) using MRG32K3A generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP22rocrand_state_mrg32k3a">
<span id="_CPPv322rocrand_uniform_doubleP22rocrand_state_mrg32k3a"></span><span id="_CPPv222rocrand_uniform_doubleP22rocrand_state_mrg32k3a"></span><span id="rocrand_uniform_double__rocrand_state_mrg32k3aP"></span><span class="target" id="group__rocranddevice_1gabb177e9ddc391e071c7a8284eca90c8d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mrg32k3a</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP22rocrand_state_mrg32k3a" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using MRG32K3A generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<p>
Note: In this implementation returned <code class="docutils literal notranslate"><span class="pre">double</span></code> value is generated from only 32 random bits (one <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP20rocrand_state_xorwow">
<span id="_CPPv315rocrand_uniformP20rocrand_state_xorwow"></span><span id="_CPPv215rocrand_uniformP20rocrand_state_xorwow"></span><span id="rocrand_uniform__rocrand_state_xorwowP"></span><span class="target" id="group__rocranddevice_1ga1b0b592aebb25e6f4d68f3ee25222294"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP20rocrand_state_xorwow" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0f</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0f</span></code>) using XORWOW generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP20rocrand_state_xorwow">
<span id="_CPPv322rocrand_uniform_doubleP20rocrand_state_xorwow"></span><span id="_CPPv222rocrand_uniform_doubleP20rocrand_state_xorwow"></span><span id="rocrand_uniform_double__rocrand_state_xorwowP"></span><span class="target" id="group__rocranddevice_1ga31e4bd345722e4bf0224539c79b8d184"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP20rocrand_state_xorwow" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using MRG32K3A generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by two.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP20rocrand_state_mtgp32">
<span id="_CPPv315rocrand_uniformP20rocrand_state_mtgp32"></span><span id="_CPPv215rocrand_uniformP20rocrand_state_mtgp32"></span><span id="rocrand_uniform__rocrand_state_mtgp32P"></span><span class="target" id="group__rocranddevice_1ga7082030def386fbf8eca759f63a63d99"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP20rocrand_state_mtgp32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0f</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0f</span></code>) using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP20rocrand_state_mtgp32">
<span id="_CPPv322rocrand_uniform_doubleP20rocrand_state_mtgp32"></span><span id="_CPPv222rocrand_uniform_doubleP20rocrand_state_mtgp32"></span><span id="rocrand_uniform_double__rocrand_state_mtgp32P"></span><span class="target" id="group__rocranddevice_1ga19ecedd115c4cfa025ee450d020bf9c7"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_mtgp32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP20rocrand_state_mtgp32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using MTGP32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<p>
Note: In this implementation returned <code class="docutils literal notranslate"><span class="pre">double</span></code> value is generated from only 32 random bits (one <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP21rocrand_state_sobol32">
<span id="_CPPv315rocrand_uniformP21rocrand_state_sobol32"></span><span id="_CPPv215rocrand_uniformP21rocrand_state_sobol32"></span><span id="rocrand_uniform__rocrand_state_sobol32P"></span><span class="target" id="group__rocranddevice_1ga98402d185568014b4db12a7e15fea94a"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP21rocrand_state_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0f</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0f</span></code>) using SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP21rocrand_state_sobol32">
<span id="_CPPv322rocrand_uniform_doubleP21rocrand_state_sobol32"></span><span id="_CPPv222rocrand_uniform_doubleP21rocrand_state_sobol32"></span><span id="rocrand_uniform_double__rocrand_state_sobol32P"></span><span class="target" id="group__rocranddevice_1ga75b5b3ec2893528a6bde00bd943688b9"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP21rocrand_state_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<p>
Note: In this implementation returned <code class="docutils literal notranslate"><span class="pre">double</span></code> value is generated from only 32 random bits (one <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP31rocrand_state_scrambled_sobol32">
<span id="_CPPv315rocrand_uniformP31rocrand_state_scrambled_sobol32"></span><span id="_CPPv215rocrand_uniformP31rocrand_state_scrambled_sobol32"></span><span id="rocrand_uniform__rocrand_state_scrambled_sobol32P"></span><span class="target" id="group__rocranddevice_1gac117b7f55e5e31b3676ce296899c51eb"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP31rocrand_state_scrambled_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0f</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0f</span></code>) using SCRAMBLED_SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP31rocrand_state_scrambled_sobol32">
<span id="_CPPv322rocrand_uniform_doubleP31rocrand_state_scrambled_sobol32"></span><span id="_CPPv222rocrand_uniform_doubleP31rocrand_state_scrambled_sobol32"></span><span id="rocrand_uniform_double__rocrand_state_scrambled_sobol32P"></span><span class="target" id="group__rocranddevice_1ga0ecbe6d5c8553aa324be356d2ade2a7f"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol32</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP31rocrand_state_scrambled_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using SCRAMBLED_SOBOL32 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<p>
Note: In this implementation returned <code class="docutils literal notranslate"><span class="pre">double</span></code> value is generated from only 32 random bits (one <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP21rocrand_state_sobol64">
<span id="_CPPv315rocrand_uniformP21rocrand_state_sobol64"></span><span id="_CPPv215rocrand_uniformP21rocrand_state_sobol64"></span><span id="rocrand_uniform__rocrand_state_sobol64P"></span><span class="target" id="group__rocranddevice_1ga1eaeb9cb630889eaedfd0afb9eb14df1"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP21rocrand_state_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP21rocrand_state_sobol64">
<span id="_CPPv322rocrand_uniform_doubleP21rocrand_state_sobol64"></span><span id="_CPPv222rocrand_uniform_doubleP21rocrand_state_sobol64"></span><span id="rocrand_uniform_double__rocrand_state_sobol64P"></span><span class="target" id="group__rocranddevice_1ga59aad4e35df2651b844d50506ad63aab"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP21rocrand_state_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP31rocrand_state_scrambled_sobol64">
<span id="_CPPv315rocrand_uniformP31rocrand_state_scrambled_sobol64"></span><span id="_CPPv215rocrand_uniformP31rocrand_state_scrambled_sobol64"></span><span id="rocrand_uniform__rocrand_state_scrambled_sobol64P"></span><span class="target" id="group__rocranddevice_1ga80939d6082bcd8087a020e966f5e7a17"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP31rocrand_state_scrambled_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using SCRAMBLED_SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP31rocrand_state_scrambled_sobol64">
<span id="_CPPv322rocrand_uniform_doubleP31rocrand_state_scrambled_sobol64"></span><span id="_CPPv222rocrand_uniform_doubleP31rocrand_state_scrambled_sobol64"></span><span id="rocrand_uniform_double__rocrand_state_scrambled_sobol64P"></span><span class="target" id="group__rocranddevice_1gad10fca54ab2f9e8082420be11cdb2978"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_scrambled_sobol64</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP31rocrand_state_scrambled_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using SCRAMBLED_SOBOL64 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP21rocrand_state_lfsr113">
<span id="_CPPv315rocrand_uniformP21rocrand_state_lfsr113"></span><span id="_CPPv215rocrand_uniformP21rocrand_state_lfsr113"></span><span id="rocrand_uniform__rocrand_state_lfsr113P"></span><span class="target" id="group__rocranddevice_1ga0486f1994c49424f03a6c987463dc161"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP21rocrand_state_lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0f</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0f</span></code>) using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP21rocrand_state_lfsr113">
<span id="_CPPv322rocrand_uniform_doubleP21rocrand_state_lfsr113"></span><span id="_CPPv222rocrand_uniform_doubleP21rocrand_state_lfsr113"></span><span id="rocrand_uniform_double__rocrand_state_lfsr113P"></span><span class="target" id="group__rocranddevice_1gafc61afc0e85641c66324dcebd0e0c15d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_lfsr113</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP21rocrand_state_lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using LFSR113 generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<p>
Note: In this implementation returned <code class="docutils literal notranslate"><span class="pre">double</span></code> value is generated from only 32 random bits (one <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP29rocrand_state_threefry2x32_20">
<span id="_CPPv315rocrand_uniformP29rocrand_state_threefry2x32_20"></span><span id="_CPPv215rocrand_uniformP29rocrand_state_threefry2x32_20"></span><span id="rocrand_uniform__rocrand_state_threefry2x32_20P"></span><span class="target" id="group__rocranddevice_1gaa1dca941e4e11a69d6d336f382ad1fdc"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP29rocrand_state_threefry2x32_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry2x32_20">
<span id="_CPPv322rocrand_uniform_doubleP29rocrand_state_threefry2x32_20"></span><span id="_CPPv222rocrand_uniform_doubleP29rocrand_state_threefry2x32_20"></span><span id="rocrand_uniform_double__rocrand_state_threefry2x32_20P"></span><span class="target" id="group__rocranddevice_1gaa8a1e6a0b18072a5e13133464938b866"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry2x32_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<p>
Note: In this implementation returned <code class="docutils literal notranslate"><span class="pre">double</span></code> value is generated from only 32 random bits (one <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP29rocrand_state_threefry2x64_20">
<span id="_CPPv315rocrand_uniformP29rocrand_state_threefry2x64_20"></span><span id="_CPPv215rocrand_uniformP29rocrand_state_threefry2x64_20"></span><span id="rocrand_uniform__rocrand_state_threefry2x64_20P"></span><span class="target" id="group__rocranddevice_1ga9e7463ebc5d06e65da555a86a85516a2"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP29rocrand_state_threefry2x64_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry2x64_20">
<span id="_CPPv322rocrand_uniform_doubleP29rocrand_state_threefry2x64_20"></span><span id="_CPPv222rocrand_uniform_doubleP29rocrand_state_threefry2x64_20"></span><span id="rocrand_uniform_double__rocrand_state_threefry2x64_20P"></span><span class="target" id="group__rocranddevice_1gaa1e7b8d262351d29eabc34985d95bc8c"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry2x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry2x64_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<p>
Note: In this implementation returned <code class="docutils literal notranslate"><span class="pre">double</span></code> value is generated from only 32 random bits (one <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP29rocrand_state_threefry4x32_20">
<span id="_CPPv315rocrand_uniformP29rocrand_state_threefry4x32_20"></span><span id="_CPPv215rocrand_uniformP29rocrand_state_threefry4x32_20"></span><span id="rocrand_uniform__rocrand_state_threefry4x32_20P"></span><span class="target" id="group__rocranddevice_1gafcfbd6e0455046812c0f67a6c5e5dd1c"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP29rocrand_state_threefry4x32_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry4x32_20">
<span id="_CPPv322rocrand_uniform_doubleP29rocrand_state_threefry4x32_20"></span><span id="_CPPv222rocrand_uniform_doubleP29rocrand_state_threefry4x32_20"></span><span id="rocrand_uniform_double__rocrand_state_threefry4x32_20P"></span><span class="target" id="group__rocranddevice_1ga098f8102121af9ebbd62b8bb914ba458"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x32_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry4x32_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<p>
Note: In this implementation returned <code class="docutils literal notranslate"><span class="pre">double</span></code> value is generated from only 32 random bits (one <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415rocrand_uniformP29rocrand_state_threefry4x64_20">
<span id="_CPPv315rocrand_uniformP29rocrand_state_threefry4x64_20"></span><span id="_CPPv215rocrand_uniformP29rocrand_state_threefry4x64_20"></span><span id="rocrand_uniform__rocrand_state_threefry4x64_20P"></span><span class="target" id="group__rocranddevice_1gab0e59febc588b31067ee01fce26a12ae"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415rocrand_uniformP29rocrand_state_threefry4x64_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry4x64_20">
<span id="_CPPv322rocrand_uniform_doubleP29rocrand_state_threefry4x64_20"></span><span id="_CPPv222rocrand_uniform_doubleP29rocrand_state_threefry4x64_20"></span><span id="rocrand_uniform_double__rocrand_state_threefry4x64_20P"></span><span class="target" id="group__rocranddevice_1gacb706887956e893dbf4b3620ee7e8b12"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_threefry4x64_20</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry4x64_20" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a uniformly distributed random <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
<p>Generates and returns a uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range (excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code>, including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>) using ThreeFry generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>, and increments position of the generator by one.</p>
<p>
Note: In this implementation returned <code class="docutils literal notranslate"><span class="pre">double</span></code> value is generated from only 32 random bits (one <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Uniformly distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> value from (0; 1] range. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412rocrand_initKyKyKyP20rocrand_state_xorwow">
<span id="_CPPv312rocrand_initKyKyKyP20rocrand_state_xorwow"></span><span id="_CPPv212rocrand_initKyKyKyP20rocrand_state_xorwow"></span><span id="rocrand_init__unsigned-l-lC.unsigned-l-lC.unsigned-l-lC.rocrand_state_xorwowP"></span><span class="target" id="group__rocranddevice_1gade9462ca7f962bf20532a4e05b6fef9d"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_init</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">seed</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">subsequence</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412rocrand_initKyKyKyP20rocrand_state_xorwow" title="Link to this definition">#</a><br /></dt>
<dd><p>Initialize XORWOW state. </p>
<p>Initializes the XORWOW generator <code class="docutils literal notranslate"><span class="pre">state</span></code> with the given <code class="docutils literal notranslate"><span class="pre">seed</span></code>, <code class="docutils literal notranslate"><span class="pre">subsequence</span></code>, and <code class="docutils literal notranslate"><span class="pre">offset</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>seed</strong> – Value to use as a seed </p></li>
<li><p><strong>subsequence</strong> – Subsequence to start at </p></li>
<li><p><strong>offset</strong> – Absolute offset into subsequence </p></li>
<li><p><strong>state</strong> – Pointer to state to initialize </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv47rocrandP20rocrand_state_xorwow">
<span id="_CPPv37rocrandP20rocrand_state_xorwow"></span><span id="_CPPv27rocrandP20rocrand_state_xorwow"></span><span id="rocrand__rocrand_state_xorwowP"></span><span class="target" id="group__rocranddevice_1ga45fb25531e024e8f7e8fbc46fb3c0117"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv47rocrandP20rocrand_state_xorwow" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range. </p>
<p>Generates and returns uniformly distributed random <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> value from [0; 2^32 - 1] range using XORWOW generator in <code class="docutils literal notranslate"><span class="pre">state</span></code>. State is incremented by one position.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – Pointer to a state to use</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Pseudorandom value (32-bit) as an <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49skipaheadyP20rocrand_state_xorwow">
<span id="_CPPv39skipaheadyP20rocrand_state_xorwow"></span><span id="_CPPv29skipaheadyP20rocrand_state_xorwow"></span><span id="skipahead__unsigned-l-l.rocrand_state_xorwowP"></span><span class="target" id="group__rocranddevice_1gac0c410634c43419fc8dc71420d71c1dd"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49skipaheadyP20rocrand_state_xorwow" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates XORWOW state to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements. </p>
<p>Updates the XORWOW state in <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">offset</span></code> elements.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – Number of elements to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421skipahead_subsequenceyP20rocrand_state_xorwow">
<span id="_CPPv321skipahead_subsequenceyP20rocrand_state_xorwow"></span><span id="_CPPv221skipahead_subsequenceyP20rocrand_state_xorwow"></span><span id="skipahead_subsequence__unsigned-l-l.rocrand_state_xorwowP"></span><span class="target" id="group__rocranddevice_1gaf02bf7b54b12c486332f3bb595003e63"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead_subsequence</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">subsequence</span></span>, <span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421skipahead_subsequenceyP20rocrand_state_xorwow" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates XORWOW state to skip ahead by <code class="docutils literal notranslate"><span class="pre">subsequence</span></code> subsequences. </p>
<p>Updates the XORWOW <code class="docutils literal notranslate"><span class="pre">state</span></code> to skip ahead by <code class="docutils literal notranslate"><span class="pre">subsequence</span></code> subsequences. Each subsequence is 2^67 numbers long.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>subsequence</strong> – Number of subsequences to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418skipahead_sequenceyP20rocrand_state_xorwow">
<span id="_CPPv318skipahead_sequenceyP20rocrand_state_xorwow"></span><span id="_CPPv218skipahead_sequenceyP20rocrand_state_xorwow"></span><span id="skipahead_sequence__unsigned-l-l.rocrand_state_xorwowP"></span><span class="target" id="group__rocranddevice_1gaad0a44153031269825ee2619bc094fd9"></span><span class="pre">__forceinline__</span><span class="w"> </span><span class="pre">__device__</span><span class="w"> </span><span class="pre">__host__</span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">skipahead_sequence</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sequence</span></span>, <span class="n"><span class="pre">rocrand_state_xorwow</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418skipahead_sequenceyP20rocrand_state_xorwow" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates XORWOW state to skip ahead by <code class="docutils literal notranslate"><span class="pre">sequence</span></code> sequences. </p>
<p>Updates the XORWOW <code class="docutils literal notranslate"><span class="pre">state</span></code> skipping <code class="docutils literal notranslate"><span class="pre">sequence</span></code> sequences ahead. For XORWOW each sequence is 2^67 numbers long (equal to the size of a subsequence).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>sequence</strong> – Number of sequences to skip </p></li>
<li><p><strong>state</strong> – Pointer to state to update </p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
</dd></dl>

</section>
<section id="c-host-api">
<h2>C host API<a class="headerlink" href="#c-host-api" title="Link to this heading">#</a></h2>
<p>The C host API allows encapsulation of the internal generator state.
Random numbers can be produced either on the host or device, depending on the created generator object.
The typical sequence of operations for device generation consists of the following steps:</p>
<ol class="arabic simple">
<li><p>Allocate memory on the device with <code class="docutils literal notranslate"><span class="pre">hipMalloc</span></code>.</p></li>
<li><p>Create a new generator of the desired type with <code class="docutils literal notranslate"><span class="pre">rocrand_create_generator</span></code>.</p></li>
<li><p>Set the generator options, for example, use <code class="docutils literal notranslate"><span class="pre">rocrand_set_seed</span></code> to set the seed.</p></li>
<li><p>Generate random numbers with <code class="docutils literal notranslate"><span class="pre">rocrand_generate</span></code> or another generation function.</p></li>
<li><p>Use the results.</p></li>
<li><p>Clean up with <code class="docutils literal notranslate"><span class="pre">rocrand_destroy_generator</span></code> and <code class="docutils literal notranslate"><span class="pre">hipFree</span></code>.</p></li>
</ol>
<p>To generate random numbers on the host, allocate the memory in the first step
using a host memory allocation call. In step two, call <code class="docutils literal notranslate"><span class="pre">rocrand_create_generator_host</span></code> instead.
In the last step, release the appropriate memory using <code class="docutils literal notranslate"><span class="pre">rocrand_destroy_generator</span></code>.
All other calls work identically whether you are generating random numbers on the device or on the host CPU.</p>
<p>The example below uses the C host API to generate ten random floats using GPU capabilities.</p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;rocrand.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;stdio.h&gt;</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">n</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">10</span><span class="p">;</span>

<span class="w">    </span><span class="n">rocrand_generator</span><span class="w"> </span><span class="n">gen</span><span class="p">;</span>
<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="w">           </span><span class="n">d_rand</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">h_rand</span><span class="p">;</span>

<span class="w">    </span><span class="n">h_rand</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="kt">float</span><span class="o">*</span><span class="p">)</span><span class="n">malloc</span><span class="p">(</span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">n</span><span class="p">);</span>
<span class="w">    </span><span class="n">hipMalloc</span><span class="p">((</span><span class="kt">void</span><span class="o">**</span><span class="p">)</span><span class="o">&amp;</span><span class="n">d_rand</span><span class="p">,</span><span class="w"> </span><span class="n">n</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">));</span>

<span class="w">    </span><span class="n">rocrand_create_generator</span><span class="p">(</span><span class="o">&amp;</span><span class="n">gen</span><span class="p">,</span><span class="w"> </span><span class="n">ROCRAND_RNG_PSEUDO_DEFAULT</span><span class="p">);</span>
<span class="w">    </span><span class="n">rocrand_set_seed</span><span class="p">(</span><span class="n">gen</span><span class="p">,</span><span class="w"> </span><span class="mi">123</span><span class="p">);</span>
<span class="w">    </span><span class="n">rocrand_generate_uniform</span><span class="p">(</span><span class="n">gen</span><span class="p">,</span><span class="w"> </span><span class="n">d_rand</span><span class="p">,</span><span class="w"> </span><span class="n">n</span><span class="p">);</span>

<span class="w">    </span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">h_rand</span><span class="p">,</span><span class="w"> </span><span class="n">d_rand</span><span class="p">,</span><span class="w"> </span><span class="n">n</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">);</span>

<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">n</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">printf</span><span class="p">(</span><span class="s">&quot;%f</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">,</span><span class="w"> </span><span class="n">h_rand</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="n">rocrand_destroy_generator</span><span class="p">(</span><span class="n">gen</span><span class="p">);</span>
<span class="w">    </span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_rand</span><span class="p">);</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<dl>
<dt class="sig sig-object cpp">
<span class="target" id="group__rocrandhost"></span><em><span class="pre">group</span></em> <span class="sig-name descname"><span class="pre">rocrandhost</span></span></dt>
<dd><div class="breathe-sectiondef docutils container">
<p class="breathe-sectiondef-title rubric" id="breathe-section-title-defines">Defines</p>
<dl class="cpp macro">
<dt class="sig sig-object cpp" id="c.ROCRAND_DEFAULT_MAX_BLOCK_SIZE">
<span class="target" id="group__rocrandhost_1gab88aa464e90a06aa26f38ebcb297e301"></span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_DEFAULT_MAX_BLOCK_SIZE</span></span></span><a class="headerlink" href="#c.ROCRAND_DEFAULT_MAX_BLOCK_SIZE" title="Link to this definition">#</a><br /></dt>
<dd><p>The default maximum number of threads per block. </p>
</dd></dl>

</div>
<div class="breathe-sectiondef docutils container">
<p class="breathe-sectiondef-title rubric" id="breathe-section-title-enums">Enums</p>
<dl class="cpp enum">
<dt class="sig sig-object cpp" id="_CPPv414rocrand_status">
<span id="_CPPv314rocrand_status"></span><span id="_CPPv214rocrand_status"></span><span class="target" id="group__rocrandhost_1ga8baefa0d48532cd7d239f0f9cf8a36b7"></span><span class="k"><span class="pre">enum</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_status</span></span></span><a class="headerlink" href="#_CPPv414rocrand_status" title="Link to this definition">#</a><br /></dt>
<dd><p>rocRAND function call status type </p>
<p><em>Values:</em></p>
<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N14rocrand_status22ROCRAND_STATUS_SUCCESSE">
<span id="_CPPv3N14rocrand_status22ROCRAND_STATUS_SUCCESSE"></span><span id="_CPPv2N14rocrand_status22ROCRAND_STATUS_SUCCESSE"></span><span class="target" id="group__rocrandhost_1gga8baefa0d48532cd7d239f0f9cf8a36b7a5637c668e1f344bdd9b03d237ef5bf7f"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_STATUS_SUCCESS</span></span></span><a class="headerlink" href="#_CPPv4N14rocrand_status22ROCRAND_STATUS_SUCCESSE" title="Link to this definition">#</a><br /></dt>
<dd><p>No errors. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N14rocrand_status31ROCRAND_STATUS_VERSION_MISMATCHE">
<span id="_CPPv3N14rocrand_status31ROCRAND_STATUS_VERSION_MISMATCHE"></span><span id="_CPPv2N14rocrand_status31ROCRAND_STATUS_VERSION_MISMATCHE"></span><span class="target" id="group__rocrandhost_1gga8baefa0d48532cd7d239f0f9cf8a36b7a27406c4e369652c161c3846c975d4212"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_STATUS_VERSION_MISMATCH</span></span></span><a class="headerlink" href="#_CPPv4N14rocrand_status31ROCRAND_STATUS_VERSION_MISMATCHE" title="Link to this definition">#</a><br /></dt>
<dd><p>Header file and linked library version do not match. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N14rocrand_status26ROCRAND_STATUS_NOT_CREATEDE">
<span id="_CPPv3N14rocrand_status26ROCRAND_STATUS_NOT_CREATEDE"></span><span id="_CPPv2N14rocrand_status26ROCRAND_STATUS_NOT_CREATEDE"></span><span class="target" id="group__rocrandhost_1gga8baefa0d48532cd7d239f0f9cf8a36b7a11b69d6b4f12084309743dbf410e1bba"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_STATUS_NOT_CREATED</span></span></span><a class="headerlink" href="#_CPPv4N14rocrand_status26ROCRAND_STATUS_NOT_CREATEDE" title="Link to this definition">#</a><br /></dt>
<dd><p>Generator was not created using rocrand_create_generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N14rocrand_status32ROCRAND_STATUS_ALLOCATION_FAILEDE">
<span id="_CPPv3N14rocrand_status32ROCRAND_STATUS_ALLOCATION_FAILEDE"></span><span id="_CPPv2N14rocrand_status32ROCRAND_STATUS_ALLOCATION_FAILEDE"></span><span class="target" id="group__rocrandhost_1gga8baefa0d48532cd7d239f0f9cf8a36b7ae857b00237b8464d1e92afc69db79746"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_STATUS_ALLOCATION_FAILED</span></span></span><a class="headerlink" href="#_CPPv4N14rocrand_status32ROCRAND_STATUS_ALLOCATION_FAILEDE" title="Link to this definition">#</a><br /></dt>
<dd><p>Memory allocation failed during execution. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N14rocrand_status25ROCRAND_STATUS_TYPE_ERRORE">
<span id="_CPPv3N14rocrand_status25ROCRAND_STATUS_TYPE_ERRORE"></span><span id="_CPPv2N14rocrand_status25ROCRAND_STATUS_TYPE_ERRORE"></span><span class="target" id="group__rocrandhost_1gga8baefa0d48532cd7d239f0f9cf8a36b7af0ff3448f279a13c7a7a6f9b326317d4"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_STATUS_TYPE_ERROR</span></span></span><a class="headerlink" href="#_CPPv4N14rocrand_status25ROCRAND_STATUS_TYPE_ERRORE" title="Link to this definition">#</a><br /></dt>
<dd><p>Generator type is wrong. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N14rocrand_status27ROCRAND_STATUS_OUT_OF_RANGEE">
<span id="_CPPv3N14rocrand_status27ROCRAND_STATUS_OUT_OF_RANGEE"></span><span id="_CPPv2N14rocrand_status27ROCRAND_STATUS_OUT_OF_RANGEE"></span><span class="target" id="group__rocrandhost_1gga8baefa0d48532cd7d239f0f9cf8a36b7a8e77c368f38af31378bbe396af85071c"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_STATUS_OUT_OF_RANGE</span></span></span><a class="headerlink" href="#_CPPv4N14rocrand_status27ROCRAND_STATUS_OUT_OF_RANGEE" title="Link to this definition">#</a><br /></dt>
<dd><p>Argument out of range. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N14rocrand_status34ROCRAND_STATUS_LENGTH_NOT_MULTIPLEE">
<span id="_CPPv3N14rocrand_status34ROCRAND_STATUS_LENGTH_NOT_MULTIPLEE"></span><span id="_CPPv2N14rocrand_status34ROCRAND_STATUS_LENGTH_NOT_MULTIPLEE"></span><span class="target" id="group__rocrandhost_1gga8baefa0d48532cd7d239f0f9cf8a36b7a33e647d9cebaaea10272be5a3389ee41"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_STATUS_LENGTH_NOT_MULTIPLE</span></span></span><a class="headerlink" href="#_CPPv4N14rocrand_status34ROCRAND_STATUS_LENGTH_NOT_MULTIPLEE" title="Link to this definition">#</a><br /></dt>
<dd><p>Requested size is not a multiple of quasirandom generator’s dimension, or requested size is not even (see <a class="reference internal" href="#group__rocrandhost_1ga129d77afa101cdd647707251f554a1df"><span class="std std-ref">rocrand_generate_normal()</span></a>), or pointer is misaligned (see <a class="reference internal" href="#group__rocrandhost_1ga129d77afa101cdd647707251f554a1df"><span class="std std-ref">rocrand_generate_normal()</span></a>) </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N14rocrand_status40ROCRAND_STATUS_DOUBLE_PRECISION_REQUIREDE">
<span id="_CPPv3N14rocrand_status40ROCRAND_STATUS_DOUBLE_PRECISION_REQUIREDE"></span><span id="_CPPv2N14rocrand_status40ROCRAND_STATUS_DOUBLE_PRECISION_REQUIREDE"></span><span class="target" id="group__rocrandhost_1gga8baefa0d48532cd7d239f0f9cf8a36b7a4624012d6838616cad7e5759b0c99a18"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_STATUS_DOUBLE_PRECISION_REQUIRED</span></span></span><a class="headerlink" href="#_CPPv4N14rocrand_status40ROCRAND_STATUS_DOUBLE_PRECISION_REQUIREDE" title="Link to this definition">#</a><br /></dt>
<dd><p>GPU does not have double precision. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N14rocrand_status29ROCRAND_STATUS_LAUNCH_FAILUREE">
<span id="_CPPv3N14rocrand_status29ROCRAND_STATUS_LAUNCH_FAILUREE"></span><span id="_CPPv2N14rocrand_status29ROCRAND_STATUS_LAUNCH_FAILUREE"></span><span class="target" id="group__rocrandhost_1gga8baefa0d48532cd7d239f0f9cf8a36b7a1daefd533a02ef65b2220ba67c0a98ef"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_STATUS_LAUNCH_FAILURE</span></span></span><a class="headerlink" href="#_CPPv4N14rocrand_status29ROCRAND_STATUS_LAUNCH_FAILUREE" title="Link to this definition">#</a><br /></dt>
<dd><p>Kernel launch failure. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N14rocrand_status29ROCRAND_STATUS_INTERNAL_ERRORE">
<span id="_CPPv3N14rocrand_status29ROCRAND_STATUS_INTERNAL_ERRORE"></span><span id="_CPPv2N14rocrand_status29ROCRAND_STATUS_INTERNAL_ERRORE"></span><span class="target" id="group__rocrandhost_1gga8baefa0d48532cd7d239f0f9cf8a36b7a5b5f6efbea8305bf1f4b2dd6986347b4"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_STATUS_INTERNAL_ERROR</span></span></span><a class="headerlink" href="#_CPPv4N14rocrand_status29ROCRAND_STATUS_INTERNAL_ERRORE" title="Link to this definition">#</a><br /></dt>
<dd><p>Internal library error. </p>
</dd></dl>

</dd></dl>

<dl class="cpp enum">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_rng_type">
<span id="_CPPv316rocrand_rng_type"></span><span id="_CPPv216rocrand_rng_type"></span><span class="target" id="group__rocrandhost_1ga993ef21b35670ba85459f27e5ceff63c"></span><span class="k"><span class="pre">enum</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_rng_type</span></span></span><a class="headerlink" href="#_CPPv416rocrand_rng_type" title="Link to this definition">#</a><br /></dt>
<dd><p>rocRAND generator type </p>
<p><em>Values:</em></p>
<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_DEFAULTE">
<span id="_CPPv3N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_DEFAULTE"></span><span id="_CPPv2N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_DEFAULTE"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca0e3ec56247b4ebf27c868dd8e7e7c975"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_PSEUDO_DEFAULT</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_DEFAULTE" title="Link to this definition">#</a><br /></dt>
<dd><p>Default pseudorandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type25ROCRAND_RNG_PSEUDO_XORWOWE">
<span id="_CPPv3N16rocrand_rng_type25ROCRAND_RNG_PSEUDO_XORWOWE"></span><span id="_CPPv2N16rocrand_rng_type25ROCRAND_RNG_PSEUDO_XORWOWE"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca4c69983abe43422dd63ded337838fc86"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_PSEUDO_XORWOW</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_PSEUDO_XORWOWE" title="Link to this definition">#</a><br /></dt>
<dd><p>XORWOW pseudorandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type27ROCRAND_RNG_PSEUDO_MRG32K3AE">
<span id="_CPPv3N16rocrand_rng_type27ROCRAND_RNG_PSEUDO_MRG32K3AE"></span><span id="_CPPv2N16rocrand_rng_type27ROCRAND_RNG_PSEUDO_MRG32K3AE"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63caf9e08b618f5be8d60ebeeb609cba4d78"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_PSEUDO_MRG32K3A</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type27ROCRAND_RNG_PSEUDO_MRG32K3AE" title="Link to this definition">#</a><br /></dt>
<dd><p>MRG32k3a pseudorandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type25ROCRAND_RNG_PSEUDO_MTGP32E">
<span id="_CPPv3N16rocrand_rng_type25ROCRAND_RNG_PSEUDO_MTGP32E"></span><span id="_CPPv2N16rocrand_rng_type25ROCRAND_RNG_PSEUDO_MTGP32E"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca70542ed568393b589c4bdb0e095c217a"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_PSEUDO_MTGP32</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_PSEUDO_MTGP32E" title="Link to this definition">#</a><br /></dt>
<dd><p>Mersenne Twister MTGP32 pseudorandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type32ROCRAND_RNG_PSEUDO_PHILOX4_32_10E">
<span id="_CPPv3N16rocrand_rng_type32ROCRAND_RNG_PSEUDO_PHILOX4_32_10E"></span><span id="_CPPv2N16rocrand_rng_type32ROCRAND_RNG_PSEUDO_PHILOX4_32_10E"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca63788724014a57b525d0956db01253e3"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_PSEUDO_PHILOX4_32_10</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type32ROCRAND_RNG_PSEUDO_PHILOX4_32_10E" title="Link to this definition">#</a><br /></dt>
<dd><p>PHILOX-4x32-10 pseudorandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type27ROCRAND_RNG_PSEUDO_MRG31K3PE">
<span id="_CPPv3N16rocrand_rng_type27ROCRAND_RNG_PSEUDO_MRG31K3PE"></span><span id="_CPPv2N16rocrand_rng_type27ROCRAND_RNG_PSEUDO_MRG31K3PE"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca55ec2966fe80e3f7e345dc798e5f1f17"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_PSEUDO_MRG31K3P</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type27ROCRAND_RNG_PSEUDO_MRG31K3PE" title="Link to this definition">#</a><br /></dt>
<dd><p>MRG31k3p pseudorandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_LFSR113E">
<span id="_CPPv3N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_LFSR113E"></span><span id="_CPPv2N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_LFSR113E"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca30f00beffb679f08828ffb1fe3dbe18a"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_PSEUDO_LFSR113</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_LFSR113E" title="Link to this definition">#</a><br /></dt>
<dd><p>LFSR113 pseudorandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_MT19937E">
<span id="_CPPv3N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_MT19937E"></span><span id="_CPPv2N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_MT19937E"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca62038fa66fd37cef8c18c83a086285a6"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_PSEUDO_MT19937</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_MT19937E" title="Link to this definition">#</a><br /></dt>
<dd><p>Mersenne Twister MT19937 pseudorandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY2_32_20E">
<span id="_CPPv3N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY2_32_20E"></span><span id="_CPPv2N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY2_32_20E"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca63f573f6d6353009b8ffdcd7304960d8"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_PSEUDO_THREEFRY2_32_20</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY2_32_20E" title="Link to this definition">#</a><br /></dt>
<dd><p>ThreeFry 32 bit state size 2 pseudorandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY2_64_20E">
<span id="_CPPv3N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY2_64_20E"></span><span id="_CPPv2N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY2_64_20E"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca3b06b10054af354b987304dbe31ef331"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_PSEUDO_THREEFRY2_64_20</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY2_64_20E" title="Link to this definition">#</a><br /></dt>
<dd><p>ThreeFry 64 bit state size 2 pseudorandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY4_32_20E">
<span id="_CPPv3N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY4_32_20E"></span><span id="_CPPv2N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY4_32_20E"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca4da3806708ff9853c1fca64da83a6283"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_PSEUDO_THREEFRY4_32_20</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY4_32_20E" title="Link to this definition">#</a><br /></dt>
<dd><p>ThreeFry 32 bit state size 4 pseudorandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY4_64_20E">
<span id="_CPPv3N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY4_64_20E"></span><span id="_CPPv2N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY4_64_20E"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca663c6fec4d8fb318e07c78cab3894216"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_PSEUDO_THREEFRY4_64_20</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY4_64_20E" title="Link to this definition">#</a><br /></dt>
<dd><p>ThreeFry 64 bit state size 4 pseudorandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type25ROCRAND_RNG_QUASI_DEFAULTE">
<span id="_CPPv3N16rocrand_rng_type25ROCRAND_RNG_QUASI_DEFAULTE"></span><span id="_CPPv2N16rocrand_rng_type25ROCRAND_RNG_QUASI_DEFAULTE"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca411554d2d63dc9b0061b520641f70138"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_QUASI_DEFAULT</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_QUASI_DEFAULTE" title="Link to this definition">#</a><br /></dt>
<dd><p>Default quasirandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type25ROCRAND_RNG_QUASI_SOBOL32E">
<span id="_CPPv3N16rocrand_rng_type25ROCRAND_RNG_QUASI_SOBOL32E"></span><span id="_CPPv2N16rocrand_rng_type25ROCRAND_RNG_QUASI_SOBOL32E"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca761e3aaea6e175f4f40880b3b3764f88"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_QUASI_SOBOL32</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_QUASI_SOBOL32E" title="Link to this definition">#</a><br /></dt>
<dd><p>Sobol32 quasirandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type35ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL32E">
<span id="_CPPv3N16rocrand_rng_type35ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL32E"></span><span id="_CPPv2N16rocrand_rng_type35ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL32E"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63caa1b0a46966437ac6e1e58bf6ff740f91"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL32</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type35ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL32E" title="Link to this definition">#</a><br /></dt>
<dd><p>Scrambled Sobol32 quasirandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type25ROCRAND_RNG_QUASI_SOBOL64E">
<span id="_CPPv3N16rocrand_rng_type25ROCRAND_RNG_QUASI_SOBOL64E"></span><span id="_CPPv2N16rocrand_rng_type25ROCRAND_RNG_QUASI_SOBOL64E"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63ca2380d4b5c804e9489e9515c8838e9e3e"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_QUASI_SOBOL64</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_QUASI_SOBOL64E" title="Link to this definition">#</a><br /></dt>
<dd><p>Sobol64 quasirandom generator. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_rng_type35ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL64E">
<span id="_CPPv3N16rocrand_rng_type35ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL64E"></span><span id="_CPPv2N16rocrand_rng_type35ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL64E"></span><span class="target" id="group__rocrandhost_1gga993ef21b35670ba85459f27e5ceff63caac11ede9f85266b48624ce1077cdc9dd"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL64</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_rng_type35ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL64E" title="Link to this definition">#</a><br /></dt>
<dd><p>Scrambled Sobol64 quasirandom generator. </p>
</dd></dl>

</dd></dl>

<dl class="cpp enum">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_ordering">
<span id="_CPPv316rocrand_ordering"></span><span id="_CPPv216rocrand_ordering"></span><span class="target" id="group__rocrandhost_1ga7e83887c5123bcb0778bafb0bcc45d03"></span><span class="k"><span class="pre">enum</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_ordering</span></span></span><a class="headerlink" href="#_CPPv416rocrand_ordering" title="Link to this definition">#</a><br /></dt>
<dd><p>rocRAND generator ordering </p>
<p><em>Values:</em></p>
<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_ordering28ROCRAND_ORDERING_PSEUDO_BESTE">
<span id="_CPPv3N16rocrand_ordering28ROCRAND_ORDERING_PSEUDO_BESTE"></span><span id="_CPPv2N16rocrand_ordering28ROCRAND_ORDERING_PSEUDO_BESTE"></span><span class="target" id="group__rocrandhost_1gga7e83887c5123bcb0778bafb0bcc45d03ae24279f855adacac25bcd99e4f9cbe92"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_ORDERING_PSEUDO_BEST</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_ordering28ROCRAND_ORDERING_PSEUDO_BESTE" title="Link to this definition">#</a><br /></dt>
<dd><p>Best ordering for pseudorandom results. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_ordering31ROCRAND_ORDERING_PSEUDO_DEFAULTE">
<span id="_CPPv3N16rocrand_ordering31ROCRAND_ORDERING_PSEUDO_DEFAULTE"></span><span id="_CPPv2N16rocrand_ordering31ROCRAND_ORDERING_PSEUDO_DEFAULTE"></span><span class="target" id="group__rocrandhost_1gga7e83887c5123bcb0778bafb0bcc45d03a0491b4c1db82216f0e17ca62a37e7c5f"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_ordering31ROCRAND_ORDERING_PSEUDO_DEFAULTE" title="Link to this definition">#</a><br /></dt>
<dd><p>Default ordering for pseudorandom results. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_ordering30ROCRAND_ORDERING_PSEUDO_SEEDEDE">
<span id="_CPPv3N16rocrand_ordering30ROCRAND_ORDERING_PSEUDO_SEEDEDE"></span><span id="_CPPv2N16rocrand_ordering30ROCRAND_ORDERING_PSEUDO_SEEDEDE"></span><span class="target" id="group__rocrandhost_1gga7e83887c5123bcb0778bafb0bcc45d03a8b3d8fac9a7593ddcb0d8168cf9b9c35"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_ORDERING_PSEUDO_SEEDED</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_ordering30ROCRAND_ORDERING_PSEUDO_SEEDEDE" title="Link to this definition">#</a><br /></dt>
<dd><p>Fast lower quality pseudorandom results. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_ordering30ROCRAND_ORDERING_PSEUDO_LEGACYE">
<span id="_CPPv3N16rocrand_ordering30ROCRAND_ORDERING_PSEUDO_LEGACYE"></span><span id="_CPPv2N16rocrand_ordering30ROCRAND_ORDERING_PSEUDO_LEGACYE"></span><span class="target" id="group__rocrandhost_1gga7e83887c5123bcb0778bafb0bcc45d03ae9496a66a7370b6396aadb1942d18d90"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_ordering30ROCRAND_ORDERING_PSEUDO_LEGACYE" title="Link to this definition">#</a><br /></dt>
<dd><p>Legacy ordering for pseudorandom results. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_ordering31ROCRAND_ORDERING_PSEUDO_DYNAMICE">
<span id="_CPPv3N16rocrand_ordering31ROCRAND_ORDERING_PSEUDO_DYNAMICE"></span><span id="_CPPv2N16rocrand_ordering31ROCRAND_ORDERING_PSEUDO_DYNAMICE"></span><span class="target" id="group__rocrandhost_1gga7e83887c5123bcb0778bafb0bcc45d03ad3c0525d92a4d30eb36fbb0a02893b7c"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_ordering31ROCRAND_ORDERING_PSEUDO_DYNAMICE" title="Link to this definition">#</a><br /></dt>
<dd><p>Adjust to the device executing the generator. The global memory usage may be higher than with the other orderings. </p>
</dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N16rocrand_ordering30ROCRAND_ORDERING_QUASI_DEFAULTE">
<span id="_CPPv3N16rocrand_ordering30ROCRAND_ORDERING_QUASI_DEFAULTE"></span><span id="_CPPv2N16rocrand_ordering30ROCRAND_ORDERING_QUASI_DEFAULTE"></span><span class="target" id="group__rocrandhost_1gga7e83887c5123bcb0778bafb0bcc45d03a4519701009c5801da1073b1b435090f8"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_ORDERING_QUASI_DEFAULT</span></span></span><a class="headerlink" href="#_CPPv4N16rocrand_ordering30ROCRAND_ORDERING_QUASI_DEFAULTE" title="Link to this definition">#</a><br /></dt>
<dd><p>n-dimensional ordering for quasirandom results </p>
</dd></dl>

</dd></dl>

<dl class="cpp enum">
<dt class="sig sig-object cpp" id="_CPPv428rocrand_direction_vector_set">
<span id="_CPPv328rocrand_direction_vector_set"></span><span id="_CPPv228rocrand_direction_vector_set"></span><span class="target" id="group__rocrandhost_1gae73a36036c9ad4dbd0e2dc1b7c504921"></span><span class="k"><span class="pre">enum</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_direction_vector_set</span></span></span><a class="headerlink" href="#_CPPv428rocrand_direction_vector_set" title="Link to this definition">#</a><br /></dt>
<dd><p>rocRAND vector set </p>
<p><em>Values:</em></p>
<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N28rocrand_direction_vector_set36ROCRAND_DIRECTION_VECTORS_32_JOEKUO6E">
<span id="_CPPv3N28rocrand_direction_vector_set36ROCRAND_DIRECTION_VECTORS_32_JOEKUO6E"></span><span id="_CPPv2N28rocrand_direction_vector_set36ROCRAND_DIRECTION_VECTORS_32_JOEKUO6E"></span><span class="target" id="group__rocrandhost_1ggae73a36036c9ad4dbd0e2dc1b7c504921a1e153dea5b07c2b9011e7fa7b9042d7e"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_DIRECTION_VECTORS_32_JOEKUO6</span></span></span><a class="headerlink" href="#_CPPv4N28rocrand_direction_vector_set36ROCRAND_DIRECTION_VECTORS_32_JOEKUO6E" title="Link to this definition">#</a><br /></dt>
<dd></dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N28rocrand_direction_vector_set46ROCRAND_SCRAMBLED_DIRECTION_VECTORS_32_JOEKUO6E">
<span id="_CPPv3N28rocrand_direction_vector_set46ROCRAND_SCRAMBLED_DIRECTION_VECTORS_32_JOEKUO6E"></span><span id="_CPPv2N28rocrand_direction_vector_set46ROCRAND_SCRAMBLED_DIRECTION_VECTORS_32_JOEKUO6E"></span><span class="target" id="group__rocrandhost_1ggae73a36036c9ad4dbd0e2dc1b7c504921a8bf078557f6ae095f199039a8fda291c"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_SCRAMBLED_DIRECTION_VECTORS_32_JOEKUO6</span></span></span><a class="headerlink" href="#_CPPv4N28rocrand_direction_vector_set46ROCRAND_SCRAMBLED_DIRECTION_VECTORS_32_JOEKUO6E" title="Link to this definition">#</a><br /></dt>
<dd></dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N28rocrand_direction_vector_set36ROCRAND_DIRECTION_VECTORS_64_JOEKUO6E">
<span id="_CPPv3N28rocrand_direction_vector_set36ROCRAND_DIRECTION_VECTORS_64_JOEKUO6E"></span><span id="_CPPv2N28rocrand_direction_vector_set36ROCRAND_DIRECTION_VECTORS_64_JOEKUO6E"></span><span class="target" id="group__rocrandhost_1ggae73a36036c9ad4dbd0e2dc1b7c504921a29ab375d6f18ca87f339351257a9cd83"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_DIRECTION_VECTORS_64_JOEKUO6</span></span></span><a class="headerlink" href="#_CPPv4N28rocrand_direction_vector_set36ROCRAND_DIRECTION_VECTORS_64_JOEKUO6E" title="Link to this definition">#</a><br /></dt>
<dd></dd></dl>

<dl class="cpp enumerator">
<dt class="sig sig-object cpp" id="_CPPv4N28rocrand_direction_vector_set46ROCRAND_SCRAMBLED_DIRECTION_VECTORS_64_JOEKUO6E">
<span id="_CPPv3N28rocrand_direction_vector_set46ROCRAND_SCRAMBLED_DIRECTION_VECTORS_64_JOEKUO6E"></span><span id="_CPPv2N28rocrand_direction_vector_set46ROCRAND_SCRAMBLED_DIRECTION_VECTORS_64_JOEKUO6E"></span><span class="target" id="group__rocrandhost_1ggae73a36036c9ad4dbd0e2dc1b7c504921a16e0519cc7ba32ce5b87b4f80aca6943"></span><span class="k"><span class="pre">enumerator</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ROCRAND_SCRAMBLED_DIRECTION_VECTORS_64_JOEKUO6</span></span></span><a class="headerlink" href="#_CPPv4N28rocrand_direction_vector_set46ROCRAND_SCRAMBLED_DIRECTION_VECTORS_64_JOEKUO6E" title="Link to this definition">#</a><br /></dt>
<dd></dd></dl>

</dd></dl>

</div>
<div class="breathe-sectiondef docutils container">
<p class="breathe-sectiondef-title rubric" id="breathe-section-title-functions">Functions</p>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424rocrand_create_generatorP17rocrand_generator16rocrand_rng_type">
<span id="_CPPv324rocrand_create_generatorP17rocrand_generator16rocrand_rng_type"></span><span id="_CPPv224rocrand_create_generatorP17rocrand_generator16rocrand_rng_type"></span><span id="rocrand_create_generator__rocrand_generatorP.rocrand_rng_type"></span><span class="target" id="group__rocrandhost_1ga8d0449c097371bbcbd28addd1e7f77b9"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_create_generator</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">generator</span></span>, <a class="reference internal" href="#_CPPv416rocrand_rng_type" title="rocrand_rng_type"><span class="n"><span class="pre">rocrand_rng_type</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">rng_type</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424rocrand_create_generatorP17rocrand_generator16rocrand_rng_type" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a new random number generator. </p>
<p>Creates a new pseudo random number generator of type <code class="docutils literal notranslate"><span class="pre">rng_type</span></code> and returns it in <code class="docutils literal notranslate"><span class="pre">generator</span></code>.</p>
<p>Values for <code class="docutils literal notranslate"><span class="pre">rng_type</span></code> are:<ul class="simple">
<li><p>ROCRAND_RNG_PSEUDO_XORWOW</p></li>
<li><p>ROCRAND_RNG_PSEUDO_MRG31K3P</p></li>
<li><p>ROCRAND_RNG_PSEUDO_MRG32K3A</p></li>
<li><p>ROCRAND_RNG_PSEUDO_MTGP32</p></li>
<li><p>ROCRAND_RNG_PSEUDO_PHILOX4_32_10</p></li>
<li><p>ROCRAND_RNG_PSEUDO_LFSR113</p></li>
<li><p>ROCRAND_RNG_PSEUDO_THREEFRY2_32_20</p></li>
<li><p>ROCRAND_RNG_PSEUDO_THREEFRY2_64_20</p></li>
<li><p>ROCRAND_RNG_PSEUDO_THREEFRY4_32_20</p></li>
<li><p>ROCRAND_RNG_PSEUDO_THREEFRY4_64_20</p></li>
<li><p>ROCRAND_RNG_QUASI_SOBOL32</p></li>
<li><p>ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL32</p></li>
<li><p>ROCRAND_RNG_QUASI_SOBOL64</p></li>
<li><p>ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL64</p></li>
</ul>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Pointer to generator </p></li>
<li><p><strong>rng_type</strong> – Type of generator to create</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_ALLOCATION_FAILED, if memory could not be allocated </p></li>
<li><p>ROCRAND_STATUS_VERSION_MISMATCH if the header file version does not match the dynamically linked library version </p></li>
<li><p>ROCRAND_STATUS_TYPE_ERROR if the value for <code class="docutils literal notranslate"><span class="pre">rng_type</span></code> is invalid </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if generator was created successfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv429rocrand_create_generator_hostP17rocrand_generator16rocrand_rng_type">
<span id="_CPPv329rocrand_create_generator_hostP17rocrand_generator16rocrand_rng_type"></span><span id="_CPPv229rocrand_create_generator_hostP17rocrand_generator16rocrand_rng_type"></span><span id="rocrand_create_generator_host__rocrand_generatorP.rocrand_rng_type"></span><span class="target" id="group__rocrandhost_1ga5cc44bbcc39838b59db2cdd752492a3c"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_create_generator_host</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">generator</span></span>, <a class="reference internal" href="#_CPPv416rocrand_rng_type" title="rocrand_rng_type"><span class="n"><span class="pre">rocrand_rng_type</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">rng_type</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv429rocrand_create_generator_hostP17rocrand_generator16rocrand_rng_type" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a new host random number generator. </p>
<p>Creates a new pseudo random number generator of type <code class="docutils literal notranslate"><span class="pre">rng_type</span></code> and returns it in <code class="docutils literal notranslate"><span class="pre">generator</span></code>. This generator is executed on the host rather than on a device, and it is enqueued on the stream associated with the generator.</p>
<p>All generators are supported.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Pointer to generator </p></li>
<li><p><strong>rng_type</strong> – Type of generator to create</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_ALLOCATION_FAILED, if memory could not be allocated </p></li>
<li><p>ROCRAND_STATUS_VERSION_MISMATCH if the header file version does not match the dynamically linked library version </p></li>
<li><p>ROCRAND_STATUS_TYPE_ERROR if the value for <code class="docutils literal notranslate"><span class="pre">rng_type</span></code> is invalid </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if generator was created successfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv438rocrand_create_generator_host_blockingP17rocrand_generator16rocrand_rng_type">
<span id="_CPPv338rocrand_create_generator_host_blockingP17rocrand_generator16rocrand_rng_type"></span><span id="_CPPv238rocrand_create_generator_host_blockingP17rocrand_generator16rocrand_rng_type"></span><span id="rocrand_create_generator_host_blocking__rocrand_generatorP.rocrand_rng_type"></span><span class="target" id="group__rocrandhost_1ga3ecf9789b5c3fb6023cca352a32bf412"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_create_generator_host_blocking</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">generator</span></span>, <a class="reference internal" href="#_CPPv416rocrand_rng_type" title="rocrand_rng_type"><span class="n"><span class="pre">rocrand_rng_type</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">rng_type</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv438rocrand_create_generator_host_blockingP17rocrand_generator16rocrand_rng_type" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a new host random number generator, similar to <code class="docutils literal notranslate"><span class="pre">rocrand_create_generator_host</span></code>. The exception is that, instead of enqueuing the host function in the stream, execution happens synchronously with respect to the calling thread and the stream is ignored. </p>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425rocrand_destroy_generator17rocrand_generator">
<span id="_CPPv325rocrand_destroy_generator17rocrand_generator"></span><span id="_CPPv225rocrand_destroy_generator17rocrand_generator"></span><span id="rocrand_destroy_generator__rocrand_generator"></span><span class="target" id="group__rocrandhost_1gafc4dd689a2b5144aa6a788a33d0e32c2"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_destroy_generator</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425rocrand_destroy_generator17rocrand_generator" title="Link to this definition">#</a><br /></dt>
<dd><p>Destroys random number generator. </p>
<p>Destroys random number generator and frees related memory.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>generator</strong> – Generator to be destroyed</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if generator was destroyed successfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_generate17rocrand_generatorPj6size_t">
<span id="_CPPv316rocrand_generate17rocrand_generatorPj6size_t"></span><span id="_CPPv216rocrand_generate17rocrand_generatorPj6size_t"></span><span id="rocrand_generate__rocrand_generator.unsigned-iP.s"></span><span class="target" id="group__rocrandhost_1gae3e149217c6ad892e2c46c7122756099"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_generate17rocrand_generatorPj6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates uniformly distributed 32-bit unsigned integers. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> uniformly distributed 32-bit unsigned integers and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<p>Generated numbers are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">2^32</span></code>, including <code class="docutils literal notranslate"><span class="pre">0</span></code> and excluding <code class="docutils literal notranslate"><span class="pre">2^32</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of 32-bit unsigned integers to generate</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426rocrand_generate_long_long17rocrand_generatorPy6size_t">
<span id="_CPPv326rocrand_generate_long_long17rocrand_generatorPy6size_t"></span><span id="_CPPv226rocrand_generate_long_long17rocrand_generatorPy6size_t"></span><span id="rocrand_generate_long_long__rocrand_generator.unsigned-l-l-iP.s"></span><span class="target" id="group__rocrandhost_1ga9e095f3670624a2312c1f19bc235b939"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_long_long</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426rocrand_generate_long_long17rocrand_generatorPy6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates uniformly distributed 64-bit unsigned integers. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> uniformly distributed 64-bit unsigned integers and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<p>Generated numbers are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">2^64</span></code>, including <code class="docutils literal notranslate"><span class="pre">0</span></code> and excluding <code class="docutils literal notranslate"><span class="pre">2^64</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of 64-bit unsigned integers to generate</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_TYPE_ERROR if the generator can’t natively generate 64-bit random numbers </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421rocrand_generate_char17rocrand_generatorPh6size_t">
<span id="_CPPv321rocrand_generate_char17rocrand_generatorPh6size_t"></span><span id="_CPPv221rocrand_generate_char17rocrand_generatorPh6size_t"></span><span id="rocrand_generate_char__rocrand_generator.unsigned-cP.s"></span><span class="target" id="group__rocrandhost_1ga803fa46f877d00a58a02816b35f28b5d"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_char</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421rocrand_generate_char17rocrand_generatorPh6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates uniformly distributed 8-bit unsigned integers. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> uniformly distributed 8-bit unsigned integers and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<p>Generated numbers are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">2^8</span></code>, including <code class="docutils literal notranslate"><span class="pre">0</span></code> and excluding <code class="docutils literal notranslate"><span class="pre">2^8</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of 8-bit unsigned integers to generate</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_generate_short17rocrand_generatorPt6size_t">
<span id="_CPPv322rocrand_generate_short17rocrand_generatorPt6size_t"></span><span id="_CPPv222rocrand_generate_short17rocrand_generatorPt6size_t"></span><span id="rocrand_generate_short__rocrand_generator.unsigned-shortP.s"></span><span class="target" id="group__rocrandhost_1ga062bd3bc4187a0ee9860fdbeda6cb3e3"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_short</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">short</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_generate_short17rocrand_generatorPt6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates uniformly distributed 16-bit unsigned integers. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> uniformly distributed 16-bit unsigned integers and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<p>Generated numbers are between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">2^16</span></code>, including <code class="docutils literal notranslate"><span class="pre">0</span></code> and excluding <code class="docutils literal notranslate"><span class="pre">2^16</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of 16-bit unsigned integers to generate</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424rocrand_generate_uniform17rocrand_generatorPf6size_t">
<span id="_CPPv324rocrand_generate_uniform17rocrand_generatorPf6size_t"></span><span id="_CPPv224rocrand_generate_uniform17rocrand_generatorPf6size_t"></span><span id="rocrand_generate_uniform__rocrand_generator.floatP.s"></span><span class="target" id="group__rocrandhost_1gabce19bf091ad9dd1d58ac389fb141af6"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_uniform</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424rocrand_generate_uniform17rocrand_generatorPf6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates uniformly distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> uniformly distributed 32-bit floating-point values and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<p>Generated numbers are between <code class="docutils literal notranslate"><span class="pre">0.0f</span></code> and <code class="docutils literal notranslate"><span class="pre">1.0f</span></code>, excluding <code class="docutils literal notranslate"><span class="pre">0.0f</span></code> and including <code class="docutils literal notranslate"><span class="pre">1.0f</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of <code class="docutils literal notranslate"><span class="pre">float</span></code>s to generate</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv431rocrand_generate_uniform_double17rocrand_generatorPd6size_t">
<span id="_CPPv331rocrand_generate_uniform_double17rocrand_generatorPd6size_t"></span><span id="_CPPv231rocrand_generate_uniform_double17rocrand_generatorPd6size_t"></span><span id="rocrand_generate_uniform_double__rocrand_generator.doubleP.s"></span><span class="target" id="group__rocrandhost_1gab8f6e7b40f0dc6373c0c79fd68c76b8c"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_uniform_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv431rocrand_generate_uniform_double17rocrand_generatorPd6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates uniformly distributed double-precision floating-point values. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> uniformly distributed 64-bit double-precision floating-point values and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<p>Generated numbers are between <code class="docutils literal notranslate"><span class="pre">0.0</span></code> and <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code> and including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of <code class="docutils literal notranslate"><span class="pre">double</span></code>s to generate</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv429rocrand_generate_uniform_half17rocrand_generatorP4half6size_t">
<span id="_CPPv329rocrand_generate_uniform_half17rocrand_generatorP4half6size_t"></span><span id="_CPPv229rocrand_generate_uniform_half17rocrand_generatorP4half6size_t"></span><span id="rocrand_generate_uniform_half__rocrand_generator.halfP.s"></span><span class="target" id="group__rocrandhost_1gaaa329ca0784ae76ebe2529ec36166267"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_uniform_half</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="n"><span class="pre">half</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv429rocrand_generate_uniform_half17rocrand_generatorP4half6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates uniformly distributed half-precision floating-point values. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> uniformly distributed 16-bit half-precision floating-point values and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<p>Generated numbers are between <code class="docutils literal notranslate"><span class="pre">0.0</span></code> and <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, excluding <code class="docutils literal notranslate"><span class="pre">0.0</span></code> and including <code class="docutils literal notranslate"><span class="pre">1.0</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of <code class="docutils literal notranslate"><span class="pre">half</span></code>s to generate</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423rocrand_generate_normal17rocrand_generatorPf6size_tff">
<span id="_CPPv323rocrand_generate_normal17rocrand_generatorPf6size_tff"></span><span id="_CPPv223rocrand_generate_normal17rocrand_generatorPf6size_tff"></span><span id="rocrand_generate_normal__rocrand_generator.floatP.s.float.float"></span><span class="target" id="group__rocrandhost_1ga129d77afa101cdd647707251f554a1df"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423rocrand_generate_normal17rocrand_generatorPf6size_tff" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> normally distributed distributed 32-bit floating-point values and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of <code class="docutils literal notranslate"><span class="pre">float</span></code>s to generate </p></li>
<li><p><strong>mean</strong> – Mean value of normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation value of normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv430rocrand_generate_normal_double17rocrand_generatorPd6size_tdd">
<span id="_CPPv330rocrand_generate_normal_double17rocrand_generatorPd6size_tdd"></span><span id="_CPPv230rocrand_generate_normal_double17rocrand_generatorPd6size_tdd"></span><span id="rocrand_generate_normal_double__rocrand_generator.doubleP.s.double.double"></span><span class="target" id="group__rocrandhost_1ga72af3e3f0207634bb5b240f07d81e406"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv430rocrand_generate_normal_double17rocrand_generatorPd6size_tdd" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> normally distributed 64-bit double-precision floating-point numbers and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of <code class="docutils literal notranslate"><span class="pre">double</span></code>s to generate </p></li>
<li><p><strong>mean</strong> – Mean value of normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation value of normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv428rocrand_generate_normal_half17rocrand_generatorP4half6size_t4half4half">
<span id="_CPPv328rocrand_generate_normal_half17rocrand_generatorP4half6size_t4half4half"></span><span id="_CPPv228rocrand_generate_normal_half17rocrand_generatorP4half6size_t4half4half"></span><span id="rocrand_generate_normal_half__rocrand_generator.halfP.s.half.half"></span><span class="target" id="group__rocrandhost_1gaacff42dbc8601de4f86651ea9d9575cb"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_normal_half</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="n"><span class="pre">half</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span>, <span class="n"><span class="pre">half</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="n"><span class="pre">half</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv428rocrand_generate_normal_half17rocrand_generatorP4half6size_t4half4half" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates normally distributed <code class="docutils literal notranslate"><span class="pre">half</span></code> values. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> normally distributed 16-bit half-precision floating-point numbers and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of <code class="docutils literal notranslate"><span class="pre">half</span></code>s to generate </p></li>
<li><p><strong>mean</strong> – Mean value of normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation value of normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv427rocrand_generate_log_normal17rocrand_generatorPf6size_tff">
<span id="_CPPv327rocrand_generate_log_normal17rocrand_generatorPf6size_tff"></span><span id="_CPPv227rocrand_generate_log_normal17rocrand_generatorPf6size_tff"></span><span id="rocrand_generate_log_normal__rocrand_generator.floatP.s.float.float"></span><span class="target" id="group__rocrandhost_1ga850572f66ae25ebb1301649af78d80d1"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_log_normal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv427rocrand_generate_log_normal17rocrand_generatorPf6size_tff" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates log-normally distributed <code class="docutils literal notranslate"><span class="pre">float</span></code> values. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> log-normally distributed 32-bit floating-point values and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of <code class="docutils literal notranslate"><span class="pre">float</span></code>s to generate </p></li>
<li><p><strong>mean</strong> – Mean value of log normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation value of log normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv434rocrand_generate_log_normal_double17rocrand_generatorPd6size_tdd">
<span id="_CPPv334rocrand_generate_log_normal_double17rocrand_generatorPd6size_tdd"></span><span id="_CPPv234rocrand_generate_log_normal_double17rocrand_generatorPd6size_tdd"></span><span id="rocrand_generate_log_normal_double__rocrand_generator.doubleP.s.double.double"></span><span class="target" id="group__rocrandhost_1gaf6c54363e2c9612f005a52367a57c983"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_log_normal_double</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv434rocrand_generate_log_normal_double17rocrand_generatorPd6size_tdd" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates log-normally distributed <code class="docutils literal notranslate"><span class="pre">double</span></code> values. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> log-normally distributed 64-bit double-precision floating-point values and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of <code class="docutils literal notranslate"><span class="pre">double</span></code>s to generate </p></li>
<li><p><strong>mean</strong> – Mean value of log normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation value of log normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv432rocrand_generate_log_normal_half17rocrand_generatorP4half6size_t4half4half">
<span id="_CPPv332rocrand_generate_log_normal_half17rocrand_generatorP4half6size_t4half4half"></span><span id="_CPPv232rocrand_generate_log_normal_half17rocrand_generatorP4half6size_t4half4half"></span><span id="rocrand_generate_log_normal_half__rocrand_generator.halfP.s.half.half"></span><span class="target" id="group__rocrandhost_1gaf8ef3c8b92c736b0633010a989ca9824"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_log_normal_half</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="n"><span class="pre">half</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span>, <span class="n"><span class="pre">half</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mean</span></span>, <span class="n"><span class="pre">half</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stddev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv432rocrand_generate_log_normal_half17rocrand_generatorP4half6size_t4half4half" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates log-normally distributed <code class="docutils literal notranslate"><span class="pre">half</span></code> values. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> log-normally distributed 16-bit half-precision floating-point values and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of <code class="docutils literal notranslate"><span class="pre">half</span></code>s to generate </p></li>
<li><p><strong>mean</strong> – Mean value of log normal distribution </p></li>
<li><p><strong>stddev</strong> – Standard deviation value of log normal distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424rocrand_generate_poisson17rocrand_generatorPj6size_td">
<span id="_CPPv324rocrand_generate_poisson17rocrand_generatorPj6size_td"></span><span id="_CPPv224rocrand_generate_poisson17rocrand_generatorPj6size_td"></span><span id="rocrand_generate_poisson__rocrand_generator.unsigned-iP.s.double"></span><span class="target" id="group__rocrandhost_1gace088e83d118e5cf683a82573bbe5bd7"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_generate_poisson</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">output_data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">n</span></span>, <span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424rocrand_generate_poisson17rocrand_generatorPj6size_td" title="Link to this definition">#</a><br /></dt>
<dd><p>Generates Poisson-distributed 32-bit unsigned integers. </p>
<p>Generates <code class="docutils literal notranslate"><span class="pre">n</span></code> Poisson-distributed 32-bit unsigned integers and saves them to <code class="docutils literal notranslate"><span class="pre">output_data</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to use </p></li>
<li><p><strong>output_data</strong> – Pointer to memory to store generated numbers </p></li>
<li><p><strong>n</strong> – Number of 32-bit unsigned integers to generate </p></li>
<li><p><strong>lambda</strong> – lambda for the Poisson distribution</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_OUT_OF_RANGE if lambda is non-positive </p></li>
<li><p>ROCRAND_STATUS_LENGTH_NOT_MULTIPLE if <code class="docutils literal notranslate"><span class="pre">n</span></code> is not a multiple of the dimension of used quasi-random generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if random numbers were successfully generated </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv428rocrand_initialize_generator17rocrand_generator">
<span id="_CPPv328rocrand_initialize_generator17rocrand_generator"></span><span id="_CPPv228rocrand_initialize_generator17rocrand_generator"></span><span id="rocrand_initialize_generator__rocrand_generator"></span><span class="target" id="group__rocrandhost_1ga3fd2ae6565bd073ccd22a3476ba5be12"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_initialize_generator</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv428rocrand_initialize_generator17rocrand_generator" title="Link to this definition">#</a><br /></dt>
<dd><p>Initializes the generator’s state on GPU or host. </p>
<p>Initializes the generator’s state on GPU or host. User it not required to call this function before using a generator.</p>
<p>If rocrand_initialize() was not called for a generator, it will be automatically called by functions which generates random numbers like <a class="reference internal" href="#group__rocrandhost_1gae3e149217c6ad892e2c46c7122756099"><span class="std std-ref">rocrand_generate()</span></a>, <a class="reference internal" href="#group__rocrandhost_1gabce19bf091ad9dd1d58ac389fb141af6"><span class="std std-ref">rocrand_generate_uniform()</span></a> etc.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>generator</strong> – Generator to initialize</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_LAUNCH_FAILURE if a HIP kernel launch failed </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if the seeds were generated successfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_set_stream17rocrand_generator11hipStream_t">
<span id="_CPPv318rocrand_set_stream17rocrand_generator11hipStream_t"></span><span id="_CPPv218rocrand_set_stream17rocrand_generator11hipStream_t"></span><span id="rocrand_set_stream__rocrand_generator.hipStream_t"></span><span class="target" id="group__rocrandhost_1gaacb4167bfafd9e7511ffdaa19f59ac21"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_set_stream</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_set_stream17rocrand_generator11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the current stream for kernel launches. </p>
<p>Sets the current stream for all kernel launches of the generator. All functions will use this stream.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Generator to modify </p></li>
<li><p><strong>stream</strong> – Stream to use or NULL for default stream</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if stream was set successfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416rocrand_set_seed17rocrand_generatory">
<span id="_CPPv316rocrand_set_seed17rocrand_generatory"></span><span id="_CPPv216rocrand_set_seed17rocrand_generatory"></span><span id="rocrand_set_seed__rocrand_generator.unsigned-l-l"></span><span class="target" id="group__rocrandhost_1gaf8dae4c6c5c83a97e1d67339e6eb202a"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_set_seed</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">seed</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416rocrand_set_seed17rocrand_generatory" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the seed of a pseudo-random number generator. </p>
<p>Sets the seed of the pseudo-random number generator.</p>
<p><ul class="simple">
<li><p>This operation resets the generator’s internal state.</p></li>
<li><p>This operation does not change the generator’s offset.</p></li>
</ul>
</p>
<p>For an MRG32K3a or MRG31K3p generator the seed value can’t be zero. If <code class="docutils literal notranslate"><span class="pre">seed</span></code> is equal to zero and generator’s type is ROCRAND_RNG_PSEUDO_MRG32K3A or ROCRAND_RNG_PSEUDO_MRG31K3P, value <code class="docutils literal notranslate"><span class="pre">12345</span></code> is used as seed instead.</p>
<p>For a LFSR113 generator seed values must be larger than 1, 7, 15,<ol class="loweralpha simple">
<li><p>The <code class="docutils literal notranslate"><span class="pre">seed</span></code> upper and lower 32 bits used as first and second seed value. If those values smaller than 2 and/or 8, those are increased with 1 and/or 7.</p></li>
</ol>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Pseudo-random number generator </p></li>
<li><p><strong>seed</strong> – New seed value</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_TYPE_ERROR if the generator is a quasi-random number generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if seed was set successfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422rocrand_set_seed_uint417rocrand_generator5uint4">
<span id="_CPPv322rocrand_set_seed_uint417rocrand_generator5uint4"></span><span id="_CPPv222rocrand_set_seed_uint417rocrand_generator5uint4"></span><span id="rocrand_set_seed_uint4__rocrand_generator.uint4"></span><span class="target" id="group__rocrandhost_1gadf1111db21cb282ece74ce3d15c2562c"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_set_seed_uint4</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="n"><span class="pre">uint4</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">seed</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422rocrand_set_seed_uint417rocrand_generator5uint4" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the seeds of a pseudo-random number generator. </p>
<p>Sets the seed of the pseudo-random number generator. Currently only for LFSR113</p>
<p><ul class="simple">
<li><p>This operation resets the generator’s internal state.</p></li>
<li><p>This operation does not change the generator’s offset.</p></li>
</ul>
</p>
<p>Only usable for LFSR113.</p>
<p>For a LFSR113 generator seed values must be bigger than 1, 7, 15,<ol class="loweralpha simple">
<li><p>If those values smaller, than the requested minimum values [2, 8, 16, 128], then it will be increased with the minimum values minus 1 [1, 7, 15, 127].</p></li>
</ol>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Pseudo-random number generator </p></li>
<li><p><strong>seed</strong> – New seed value</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_TYPE_ERROR if the generator is a quasi-random number generator </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if seed was set successfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418rocrand_set_offset17rocrand_generatory">
<span id="_CPPv318rocrand_set_offset17rocrand_generatory"></span><span id="_CPPv218rocrand_set_offset17rocrand_generatory"></span><span id="rocrand_set_offset__rocrand_generator.unsigned-l-l"></span><span class="target" id="group__rocrandhost_1ga24815d9f073a0abc714479bef4ad34af"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_set_offset</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418rocrand_set_offset17rocrand_generatory" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the offset of a random number generator. </p>
<p>Sets the absolute offset of the random number generator.</p>
<p><ul class="simple">
<li><p>This operation resets the generator’s internal state.</p></li>
<li><p>This operation does not change the generator’s seed.</p></li>
</ul>
</p>
<p>Absolute offset cannot be set if generator’s type is ROCRAND_RNG_PSEUDO_MTGP32 or ROCRAND_RNG_PSEUDO_LFSR113.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Random number generator </p></li>
<li><p><strong>offset</strong> – New absolute offset</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if offset was successfully set </p></li>
<li><p>ROCRAND_STATUS_TYPE_ERROR if generator’s type is ROCRAND_RNG_PSEUDO_MTGP32 or ROCRAND_RNG_PSEUDO_LFSR113 </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420rocrand_set_ordering17rocrand_generator16rocrand_ordering">
<span id="_CPPv320rocrand_set_ordering17rocrand_generator16rocrand_ordering"></span><span id="_CPPv220rocrand_set_ordering17rocrand_generator16rocrand_ordering"></span><span id="rocrand_set_ordering__rocrand_generator.rocrand_ordering"></span><span class="target" id="group__rocrandhost_1gacb1caa806c7bf42e024a4bb9057ce07e"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_set_ordering</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <a class="reference internal" href="#_CPPv416rocrand_ordering" title="rocrand_ordering"><span class="n"><span class="pre">rocrand_ordering</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">order</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420rocrand_set_ordering17rocrand_generator16rocrand_ordering" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the ordering of a random number generator. </p>
<p>Sets the ordering of the results of a random number generator.</p>
<p><ul class="simple">
<li><p>This operation resets the generator’s internal state.</p></li>
<li><p>This operation does not change the generator’s seed.</p></li>
</ul>
</p>
<p>
The ordering choices for pseudorandom sequences are the following. Note that not all generators support all orderings. For details, see the Programmer’s Guide in the documentation.<ul class="simple">
<li><p>ROCRAND_ORDERING_PSEUDO_DEFAULT</p></li>
<li><p>ROCRAND_ORDERING_PSEUDO_LEGACY</p></li>
<li><p>ROCRAND_ORDERING_PSEUDO_BEST</p></li>
<li><p>ROCRAND_ORDERING_PSEUDO_SEEDED</p></li>
<li><p>ROCRAND_ORDERING_PSEUDO_DYNAMIC</p></li>
</ul>
</p>
<p>For quasirandom sequences there is only one ordering, ROCRAND_ORDERING_QUASI_DEFAULT.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Random number generator </p></li>
<li><p><strong>order</strong> – New ordering of results</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_OUT_OF_RANGE if the ordering is not valid </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if the ordering was successfully set </p></li>
<li><p>ROCRAND_STATUS_TYPE_ERROR if generator’s type is not valid </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv445rocrand_set_quasi_random_generator_dimensions17rocrand_generatorj">
<span id="_CPPv345rocrand_set_quasi_random_generator_dimensions17rocrand_generatorj"></span><span id="_CPPv245rocrand_set_quasi_random_generator_dimensions17rocrand_generatorj"></span><span id="rocrand_set_quasi_random_generator_dimensions__rocrand_generator.unsigned-i"></span><span class="target" id="group__rocrandhost_1gad60207411c2a634aa851fc033c401180"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_set_quasi_random_generator_dimensions</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_generator</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">generator</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dimensions</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv445rocrand_set_quasi_random_generator_dimensions17rocrand_generatorj" title="Link to this definition">#</a><br /></dt>
<dd><p>Set the number of dimensions of a quasi-random number generator. </p>
<p>Set the number of dimensions of a quasi-random number generator. Supported values of <code class="docutils literal notranslate"><span class="pre">dimensions</span></code> are 1 to 20000.</p>
<p><ul class="simple">
<li><p>This operation resets the generator’s internal state.</p></li>
<li><p>This operation does not change the generator’s offset.</p></li>
</ul>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generator</strong> – Quasi-random number generator </p></li>
<li><p><strong>dimensions</strong> – Number of dimensions</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_NOT_CREATED if the generator wasn’t created </p></li>
<li><p>ROCRAND_STATUS_TYPE_ERROR if the generator is not a quasi-random number generator </p></li>
<li><p>ROCRAND_STATUS_OUT_OF_RANGE if <code class="docutils literal notranslate"><span class="pre">dimensions</span></code> is out of range </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if the number of dimensions was set successfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419rocrand_get_versionPi">
<span id="_CPPv319rocrand_get_versionPi"></span><span id="_CPPv219rocrand_get_versionPi"></span><span id="rocrand_get_version__iP"></span><span class="target" id="group__rocrandhost_1gada98d41f4545f7abbd0f1be2ba8ea176"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_get_version</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">version</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419rocrand_get_versionPi" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns the version number of the library. </p>
<p>Returns in <code class="docutils literal notranslate"><span class="pre">version</span></code> the version number of the dynamically linked rocRAND library.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>version</strong> – Version of the library</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_OUT_OF_RANGE if <code class="docutils literal notranslate"><span class="pre">version</span></code> is NULL </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if the version number was successfully returned </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv435rocrand_create_poisson_distributiondP29rocrand_discrete_distribution">
<span id="_CPPv335rocrand_create_poisson_distributiondP29rocrand_discrete_distribution"></span><span id="_CPPv235rocrand_create_poisson_distributiondP29rocrand_discrete_distribution"></span><span id="rocrand_create_poisson_distribution__double.rocrand_discrete_distributionP"></span><span class="target" id="group__rocrandhost_1ga02bb152d66cc67c799d217200de7ef90"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_create_poisson_distribution</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lambda</span></span>, <span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv435rocrand_create_poisson_distributiondP29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Construct the histogram for a Poisson distribution. </p>
<p>Construct the histogram for the Poisson distribution with lambda <code class="docutils literal notranslate"><span class="pre">lambda</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>lambda</strong> – lambda for the Poisson distribution </p></li>
<li><p><strong>discrete_distribution</strong> – pointer to the histogram in device memory</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_ALLOCATION_FAILED if memory could not be allocated </p></li>
<li><p>ROCRAND_STATUS_OUT_OF_RANGE if <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> pointer was null </p></li>
<li><p>ROCRAND_STATUS_OUT_OF_RANGE if lambda is non-positive </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if the histogram was constructed successfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv436rocrand_create_discrete_distributionPKdjjP29rocrand_discrete_distribution">
<span id="_CPPv336rocrand_create_discrete_distributionPKdjjP29rocrand_discrete_distribution"></span><span id="_CPPv236rocrand_create_discrete_distributionPKdjjP29rocrand_discrete_distribution"></span><span id="rocrand_create_discrete_distribution__doubleCP.unsigned-i.unsigned-i.rocrand_discrete_distributionP"></span><span class="target" id="group__rocrandhost_1gac600927326dd87006ce2a7f24e609fa1"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_create_discrete_distribution</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">double</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">probabilities</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv436rocrand_create_discrete_distributionPKdjjP29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Construct the histogram for a custom discrete distribution. </p>
<p>Construct the histogram for the discrete distribution of <code class="docutils literal notranslate"><span class="pre">size</span></code> 32-bit unsigned integers from the range [<code class="docutils literal notranslate"><span class="pre">offset</span></code>, <code class="docutils literal notranslate"><span class="pre">offset</span></code> + <code class="docutils literal notranslate"><span class="pre">size</span></code>) using <code class="docutils literal notranslate"><span class="pre">probabilities</span></code> as probabilities.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>probabilities</strong> – probabilities of the the distribution in host memory </p></li>
<li><p><strong>size</strong> – size of <code class="docutils literal notranslate"><span class="pre">probabilities</span></code></p></li>
<li><p><strong>offset</strong> – offset of values </p></li>
<li><p><strong>discrete_distribution</strong> – pointer to the histogram in device memory</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_ALLOCATION_FAILED if memory could not be allocated </p></li>
<li><p>ROCRAND_STATUS_OUT_OF_RANGE if <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> pointer was null </p></li>
<li><p>ROCRAND_STATUS_OUT_OF_RANGE if <code class="docutils literal notranslate"><span class="pre">size</span></code> was zero </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if the histogram was constructed successfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv437rocrand_destroy_discrete_distribution29rocrand_discrete_distribution">
<span id="_CPPv337rocrand_destroy_discrete_distribution29rocrand_discrete_distribution"></span><span id="_CPPv237rocrand_destroy_discrete_distribution29rocrand_discrete_distribution"></span><span id="rocrand_destroy_discrete_distribution__rocrand_discrete_distribution"></span><span class="target" id="group__rocrandhost_1gaf2e95cb1e61842a42801950f553d5750"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_destroy_discrete_distribution</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">rocrand_discrete_distribution</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">discrete_distribution</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv437rocrand_destroy_discrete_distribution29rocrand_discrete_distribution" title="Link to this definition">#</a><br /></dt>
<dd><p>Destroy the histogram array for a discrete distribution. </p>
<p>Destroy the histogram array for a discrete distribution created by rocrand_create_poisson_distribution.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>discrete_distribution</strong> – pointer to the histogram in device memory</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_OUT_OF_RANGE if <code class="docutils literal notranslate"><span class="pre">discrete_distribution</span></code> was null </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if the histogram was destroyed successfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv431rocrand_get_direction_vectors32PPKj28rocrand_direction_vector_set">
<span id="_CPPv331rocrand_get_direction_vectors32PPKj28rocrand_direction_vector_set"></span><span id="_CPPv231rocrand_get_direction_vectors32PPKj28rocrand_direction_vector_set"></span><span id="rocrand_get_direction_vectors32__unsigned-iCPP.rocrand_direction_vector_set"></span><span class="target" id="group__rocrandhost_1ga43952417ccd3f490cf7b2c5385ea8518"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_get_direction_vectors32</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">vectors</span></span>, <a class="reference internal" href="#_CPPv428rocrand_direction_vector_set" title="rocrand_direction_vector_set"><span class="n"><span class="pre">rocrand_direction_vector_set</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">set</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv431rocrand_get_direction_vectors32PPKj28rocrand_direction_vector_set" title="Link to this definition">#</a><br /></dt>
<dd><p>Get the vector for 32-bit (scrambled-)sobol generation. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>vectors</strong> – location where to write the vector pointer to</p></li>
<li><p><strong>set</strong> – which direction vector set to use</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_OUT_OF_RANGE if <code class="docutils literal notranslate"><span class="pre">set</span></code> was invalid for this method </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if the pointer was set succesfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv431rocrand_get_direction_vectors64PPKy28rocrand_direction_vector_set">
<span id="_CPPv331rocrand_get_direction_vectors64PPKy28rocrand_direction_vector_set"></span><span id="_CPPv231rocrand_get_direction_vectors64PPKy28rocrand_direction_vector_set"></span><span id="rocrand_get_direction_vectors64__unsigned-l-lCPP.rocrand_direction_vector_set"></span><span class="target" id="group__rocrandhost_1gab9f1d7371bc18cfb382d4c668596a964"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_get_direction_vectors64</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">vectors</span></span>, <a class="reference internal" href="#_CPPv428rocrand_direction_vector_set" title="rocrand_direction_vector_set"><span class="n"><span class="pre">rocrand_direction_vector_set</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">set</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv431rocrand_get_direction_vectors64PPKy28rocrand_direction_vector_set" title="Link to this definition">#</a><br /></dt>
<dd><p>Get the vector for 64-bit (scrambled-)sobol generation. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>vectors</strong> – location where to write the vector pointer to</p></li>
<li><p><strong>set</strong> – which direction vector set to use</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_OUT_OF_RANGE if <code class="docutils literal notranslate"><span class="pre">set</span></code> was invalid for this method </p></li>
<li><p>ROCRAND_STATUS_SUCCESS if the pointer was set succesfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv432rocrand_get_scramble_constants32PPKj">
<span id="_CPPv332rocrand_get_scramble_constants32PPKj"></span><span id="_CPPv232rocrand_get_scramble_constants32PPKj"></span><span id="rocrand_get_scramble_constants32__unsigned-iCPP"></span><span class="target" id="group__rocrandhost_1gab50b7863745242edc3177d24bb08c1ff"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_get_scramble_constants32</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">constants</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv432rocrand_get_scramble_constants32PPKj" title="Link to this definition">#</a><br /></dt>
<dd><p>Get the scramble constants for 32-bit scrambled sobol generation. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>constants</strong> – location where to write the constants pointer to</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_SUCCESS if the pointer was set succesfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv432rocrand_get_scramble_constants64PPKy">
<span id="_CPPv332rocrand_get_scramble_constants64PPKy"></span><span id="_CPPv232rocrand_get_scramble_constants64PPKy"></span><span id="rocrand_get_scramble_constants64__unsigned-l-lCPP"></span><span class="target" id="group__rocrandhost_1gaf8db0cd9061b879f34f96de8ef672147"></span><a class="reference internal" href="#_CPPv414rocrand_status" title="rocrand_status"><span class="n"><span class="pre">rocrand_status</span></span></a><span class="w"> </span><span class="pre">ROCRANDAPI</span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">rocrand_get_scramble_constants64</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">constants</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv432rocrand_get_scramble_constants64PPKy" title="Link to this definition">#</a><br /></dt>
<dd><p>Get the scramble constants for 64-bit scrambled sobol generation. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>constants</strong> – location where to write the constants pointer to</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><ul class="simple">
<li><p>ROCRAND_STATUS_SUCCESS if the pointer was set succesfully </p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>

</div>
</dd></dl>

</section>
<section id="c-host-api-wrapper">
<h2>C++ host API wrapper<a class="headerlink" href="#c-host-api-wrapper" title="Link to this heading">#</a></h2>
<p>The C++ host API wrapper provides resource management and an object-oriented interface for random number
generation facilities.</p>
<p>The example below uses the C++ host API wrapper to produce a random number using the default generation parameters.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;rocrand/rocrand.hpp&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">d_rand</span><span class="p">;</span>
<span class="w">    </span><span class="kt">float</span><span class="w">  </span><span class="n">h_rand</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipMalloc</span><span class="p">((</span><span class="kt">void</span><span class="o">**</span><span class="p">)</span><span class="o">&amp;</span><span class="n">d_rand</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">));</span>

<span class="w">    </span><span class="n">rocrand_cpp</span><span class="o">::</span><span class="n">xorwow</span><span class="w">                </span><span class="n">gen</span><span class="p">;</span>
<span class="w">    </span><span class="n">rocrand_cpp</span><span class="o">::</span><span class="n">normal_distribution</span><span class="o">&lt;&gt;</span><span class="w"> </span><span class="n">dist</span><span class="p">;</span>

<span class="w">    </span><span class="n">dist</span><span class="p">(</span><span class="n">gen</span><span class="p">,</span><span class="w"> </span><span class="n">d_rand</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">);</span>

<span class="w">    </span><span class="n">hipMemcpy</span><span class="p">(</span><span class="o">&amp;</span><span class="n">h_rand</span><span class="p">,</span><span class="w"> </span><span class="n">d_rand</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">);</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">h_rand</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_rand</span><span class="p">);</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<dl>
<dt class="sig sig-object cpp">
<span class="target" id="group__rocrandhostcpp"></span><em><span class="pre">group</span></em> <span class="sig-name descname"><span class="pre">rocrandhostcpp</span></span></dt>
<dd><div class="breathe-sectiondef docutils container">
<p class="breathe-sectiondef-title rubric" id="breathe-section-title-typedefs">Typedefs</p>
<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv413philox4x32_10">
<span id="_CPPv313philox4x32_10"></span><span id="_CPPv213philox4x32_10"></span><span id="philox4x32_10"></span><span class="target" id="group__rocrandhostcpp_1gaed266730800c29167fef57ecffc766cf"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">philox4x32_10_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">philox4x32_10</span></span></span><a class="headerlink" href="#_CPPv413philox4x32_10" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <a class="reference internal" href="#classrocrand__cpp_1_1philox4x32__10__engine"><span class="std std-ref">rocrand_cpp::philox4x32_10_engine</span></a> PRNG engine with default seed (<a class="reference internal" href="#group__rocranddevice_1ga545da3f91883ce1a2990a1ec8141d5fb"><span class="std std-ref">ROCRAND_PHILOX4x32_DEFAULT_SEED</span></a>). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv46xorwow">
<span id="_CPPv36xorwow"></span><span id="_CPPv26xorwow"></span><span id="xorwow"></span><span class="target" id="group__rocrandhostcpp_1gabc91fa4ea7737363c8db15b2e22a4a3f"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">xorwow_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">xorwow</span></span></span><a class="headerlink" href="#_CPPv46xorwow" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1xorwow__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::xorwow_engine</span></span></a></code> PRNG engine with default seed (<a class="reference internal" href="#group__rocranddevice_1gafb4aa9f4548403e34c00b271c7ef1a77"><span class="std std-ref">ROCRAND_XORWOW_DEFAULT_SEED</span></a>). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv48mrg31k3p">
<span id="_CPPv38mrg31k3p"></span><span id="_CPPv28mrg31k3p"></span><span id="mrg31k3p"></span><span class="target" id="group__rocrandhostcpp_1ga24ecd1d53abcea642018871ae1a06b85"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">mrg31k3p_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">mrg31k3p</span></span></span><a class="headerlink" href="#_CPPv48mrg31k3p" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1mrg31k3p__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::mrg31k3p_engine</span></span></a></code> PRNG engine with default seed (<a class="reference internal" href="#group__rocranddevice_1ga0ea93cf8d2d16d5fd7db45ada5ddac05"><span class="std std-ref">ROCRAND_MRG31K3P_DEFAULT_SEED</span></a>). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv48mrg32k3a">
<span id="_CPPv38mrg32k3a"></span><span id="_CPPv28mrg32k3a"></span><span id="mrg32k3a"></span><span class="target" id="group__rocrandhostcpp_1ga41e4586d94c436c2072fc1104135befd"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">mrg32k3a_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">mrg32k3a</span></span></span><a class="headerlink" href="#_CPPv48mrg32k3a" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1mrg32k3a__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::mrg32k3a_engine</span></span></a></code> PRNG engine with default seed (<a class="reference internal" href="#group__rocranddevice_1ga2b4b37e72c090e6d99373ff68d14c173"><span class="std std-ref">ROCRAND_MRG32K3A_DEFAULT_SEED</span></a>). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv46mtgp32">
<span id="_CPPv36mtgp32"></span><span id="_CPPv26mtgp32"></span><span id="mtgp32"></span><span class="target" id="group__rocrandhostcpp_1gaf97fad61d2ae3c7033584faa63ba957d"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">mtgp32_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">mtgp32</span></span></span><a class="headerlink" href="#_CPPv46mtgp32" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1mtgp32__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::mtgp32_engine</span></span></a></code> PRNG engine with default seed (0). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv47lfsr113">
<span id="_CPPv37lfsr113"></span><span id="_CPPv27lfsr113"></span><span id="lfsr113"></span><span class="target" id="group__rocrandhostcpp_1gab2554c6af0f70f157eabc863dd7beb1e"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">lfsr113_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">lfsr113</span></span></span><a class="headerlink" href="#_CPPv47lfsr113" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1lfsr113__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::lfsr113_engine</span></span></a></code> PRNG engine with default seed (<a class="reference internal" href="#group__rocranddevice_1gad7b9a9998c875ff2fc450eb5fda8123c"><span class="std std-ref">ROCRAND_LFSR113_DEFAULT_SEED_X</span></a>, <a class="reference internal" href="#group__rocranddevice_1ga42b6caeb3146cf57d8095ba69b2faed6"><span class="std std-ref">ROCRAND_LFSR113_DEFAULT_SEED_Y</span></a>, <a class="reference internal" href="#group__rocranddevice_1gab01fbf3f2209f949b60ee0990b471007"><span class="std std-ref">ROCRAND_LFSR113_DEFAULT_SEED_Z</span></a>, <a class="reference internal" href="#group__rocranddevice_1ga4e427750c6a51bfd63a7f02cb6e62b1e"><span class="std std-ref">ROCRAND_LFSR113_DEFAULT_SEED_W</span></a>). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv47mt19937">
<span id="_CPPv37mt19937"></span><span id="_CPPv27mt19937"></span><span id="mt19937"></span><span class="target" id="group__rocrandhostcpp_1ga9e9497e330fa717e2b502d0873de65be"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">mt19937_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">mt19937</span></span></span><a class="headerlink" href="#_CPPv47mt19937" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1mt19937__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::mt19937_engine</span></span></a></code> PRNG engine with default seed (0). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv412threefry2x32">
<span id="_CPPv312threefry2x32"></span><span id="_CPPv212threefry2x32"></span><span id="threefry2x32"></span><span class="target" id="group__rocrandhostcpp_1ga16f2926fa3f9ae67dda5a55779d8de51"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">threefry2x32_20_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">threefry2x32</span></span></span><a class="headerlink" href="#_CPPv412threefry2x32" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1threefry2x32__20__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::threefry2x32_20_engine</span></span></a></code> PRNG engine with default seed (0). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv412threefry2x64">
<span id="_CPPv312threefry2x64"></span><span id="_CPPv212threefry2x64"></span><span id="threefry2x64"></span><span class="target" id="group__rocrandhostcpp_1gae4497a2fa6769dc6736d00f8e79a1ec1"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">threefry2x64_20_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">threefry2x64</span></span></span><a class="headerlink" href="#_CPPv412threefry2x64" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1threefry2x64__20__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::threefry2x64_20_engine</span></span></a></code> PRNG engine with default seed (0). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv412threefry4x32">
<span id="_CPPv312threefry4x32"></span><span id="_CPPv212threefry4x32"></span><span id="threefry4x32"></span><span class="target" id="group__rocrandhostcpp_1gad03bed41243ccf8281eb20bf0c5492c8"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">threefry4x32_20_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">threefry4x32</span></span></span><a class="headerlink" href="#_CPPv412threefry4x32" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1threefry4x32__20__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::threefry4x32_20_engine</span></span></a></code> PRNG engine with default seed (0). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv412threefry4x64">
<span id="_CPPv312threefry4x64"></span><span id="_CPPv212threefry4x64"></span><span id="threefry4x64"></span><span class="target" id="group__rocrandhostcpp_1gab7652524bd1228a16e0dede27f9db24f"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">threefry4x64_20_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">threefry4x64</span></span></span><a class="headerlink" href="#_CPPv412threefry4x64" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1threefry4x64__20__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::threefry4x64_20_engine</span></span></a></code> PRNG engine with default seed (0). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv47sobol32">
<span id="_CPPv37sobol32"></span><span id="_CPPv27sobol32"></span><span id="sobol32"></span><span class="target" id="group__rocrandhostcpp_1gaac6c97f286f1eafbb181e7c0e80ed682"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">sobol32_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">sobol32</span></span></span><a class="headerlink" href="#_CPPv47sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1sobol32__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::sobol32_engine</span></span></a></code> QRNG engine with default number of dimensions (1). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv417scrambled_sobol32">
<span id="_CPPv317scrambled_sobol32"></span><span id="_CPPv217scrambled_sobol32"></span><span id="scrambled_sobol32"></span><span class="target" id="group__rocrandhostcpp_1ga5d2370cc545a4bf0f0f8ef3a20d21de7"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">scrambled_sobol32_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">scrambled_sobol32</span></span></span><a class="headerlink" href="#_CPPv417scrambled_sobol32" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1scrambled__sobol32__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::scrambled_sobol32_engine</span></span></a></code> QRNG engine with default number of dimensions (1). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv47sobol64">
<span id="_CPPv37sobol64"></span><span id="_CPPv27sobol64"></span><span id="sobol64"></span><span class="target" id="group__rocrandhostcpp_1ga75ce3a14366d873ea9c65ffc78fd6093"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">sobol64_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">sobol64</span></span></span><a class="headerlink" href="#_CPPv47sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1sobol64__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::sobol64_engine</span></span></a></code> QRNG engine with default number of dimensions (1). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv417scrambled_sobol64">
<span id="_CPPv317scrambled_sobol64"></span><span id="_CPPv217scrambled_sobol64"></span><span id="scrambled_sobol64"></span><span class="target" id="group__rocrandhostcpp_1ga4bf3ebb685267a05859100aa9ea7dca1"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">scrambled_sobol64_engine</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">scrambled_sobol64</span></span></span><a class="headerlink" href="#_CPPv417scrambled_sobol64" title="Link to this definition">#</a><br /></dt>
<dd><p>Typedef of <code class="docutils literal notranslate"><a class="reference internal" href="#classrocrand__cpp_1_1scrambled__sobol64__engine"><span class="std std-ref"><span class="pre">rocrand_cpp::scrambled_sobol64_engine</span></span></a></code> QRNG engine with default number of dimensions (1). </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv421default_random_engine">
<span id="_CPPv321default_random_engine"></span><span id="_CPPv221default_random_engine"></span><span id="default_random_engine"></span><span class="target" id="group__rocrandhostcpp_1gaeb5d7c54dab07c51c6f241585543c1e3"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv46xorwow" title="xorwow"><span class="n"><span class="pre">xorwow</span></span></a><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">default_random_engine</span></span></span><a class="headerlink" href="#_CPPv421default_random_engine" title="Link to this definition">#</a><br /></dt>
<dd><p>Default random engine. </p>
</dd></dl>

<dl class="cpp type">
<dt class="sig sig-object cpp" id="_CPPv413random_device">
<span id="_CPPv313random_device"></span><span id="_CPPv213random_device"></span><span id="random_device"></span><span class="target" id="group__rocrandhostcpp_1gafa11687825531fab552a5d8e075417b7"></span><span class="k"><span class="pre">typedef</span></span><span class="w"> </span><span class="n"><span class="pre">std</span></span><span class="p"><span class="pre">::</span></span><span class="n"><span class="pre">random_device</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">random_device</span></span></span><a class="headerlink" href="#_CPPv413random_device" title="Link to this definition">#</a><br /></dt>
<dd><p>A non-deterministic uniform random number generator. </p>
<p>rocrand_cpp::random_device is non-deterministic uniform random number generator, or a pseudo-random number engine if there is no support for non-deterministic random number generation. It’s implemented as a typedef of std::random_device.</p>
<p>For practical use rocrand_cpp::random_device is generally only used to seed a PRNG such as <a class="reference internal" href="#classrocrand__cpp_1_1mtgp32__engine"><span class="std std-ref">rocrand_cpp::mtgp32_engine</span></a>.</p>
<p>Example: <div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="c1">#include &lt;rocrand/rocrand.hpp&gt;</span>

<span class="nb">int</span> <span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
    <span class="n">const</span> <span class="n">size_t</span> <span class="n">size</span> <span class="o">=</span> <span class="mi">8192</span><span class="p">;</span>
    <span class="nb">float</span> <span class="o">*</span> <span class="n">output</span><span class="p">;</span>
    <span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">output</span><span class="p">,</span> <span class="n">size</span> <span class="o">*</span> <span class="n">sizeof</span><span class="p">(</span><span class="nb">float</span><span class="p">));</span>

    <span class="n">rocrand_cpp</span><span class="p">::</span><span class="n">random_device</span> <span class="n">rd</span><span class="p">;</span>
    <span class="n">rocrand_cpp</span><span class="p">::</span><span class="n">mtgp32</span> <span class="n">engine</span><span class="p">(</span><span class="n">rd</span><span class="p">());</span> <span class="o">//</span> <span class="n">seed</span> <span class="n">engine</span> <span class="k">with</span> <span class="n">a</span> <span class="n">real</span> <span class="n">random</span> <span class="n">value</span><span class="p">,</span> <span class="k">if</span> <span class="n">available</span>
    <span class="n">rocrand_cpp</span><span class="p">::</span><span class="n">normal_distribution</span><span class="o">&lt;</span><span class="nb">float</span><span class="o">&gt;</span> <span class="n">dist</span><span class="p">(</span><span class="mf">0.0</span><span class="p">,</span> <span class="mf">1.5</span><span class="p">);</span>
    <span class="n">dist</span><span class="p">(</span><span class="n">engine</span><span class="p">,</span> <span class="n">output</span><span class="p">,</span> <span class="n">size</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
</p>
</dd></dl>

</div>
<div class="breathe-sectiondef docutils container">
<p class="breathe-sectiondef-title rubric" id="breathe-section-title-functions">Functions</p>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv47versionv">
<span id="_CPPv37versionv"></span><span id="_CPPv27versionv"></span><span id="version"></span><span class="target" id="group__rocrandhostcpp_1ga3ac75ea7bbd4ade1a4fdabdf2a629201"></span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">version</span></span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv47versionv" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns rocRAND version. </p>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>rocRAND version number as an <code class="docutils literal notranslate"><span class="pre">int</span></code> value. </p>
</dd>
</dl>
</dd></dl>

</div>
<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4N11rocrand_cpp5errorE">
<span id="_CPPv3N11rocrand_cpp5errorE"></span><span id="_CPPv2N11rocrand_cpp5errorE"></span><span id="rocrand_cpp::error"></span><span class="target" id="classrocrand__cpp_1_1error"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">error</span></span></span><span class="w"> </span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="k"><span class="pre">public</span></span><span class="w"> </span><span class="n"><span class="pre">std</span></span><span class="p"><span class="pre">::</span></span><span class="n"><span class="pre">exception</span></span><a class="headerlink" href="#_CPPv4N11rocrand_cpp5errorE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>A run-time rocRAND error. </p>
<p>The error class represents an error returned by a rocRAND function. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I0EN11rocrand_cpp24uniform_int_distributionE">
<span id="_CPPv3I0EN11rocrand_cpp24uniform_int_distributionE"></span><span id="_CPPv2I0EN11rocrand_cpp24uniform_int_distributionE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">IntType</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1uniform__int__distribution"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">uniform_int_distribution</span></span></span><a class="headerlink" href="#_CPPv4I0EN11rocrand_cpp24uniform_int_distributionE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Produces random integer values uniformly distributed on the interval [0, 2^(sizeof(IntType)*8) - 1]. </p>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>IntType</strong> – type of generated values. Only <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">char</span></code>, <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">short</span></code> and <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> and <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">long</span></code> <code class="docutils literal notranslate"><span class="pre">long</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> type is supported. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I0EN11rocrand_cpp25uniform_real_distributionE">
<span id="_CPPv3I0EN11rocrand_cpp25uniform_real_distributionE"></span><span id="_CPPv2I0EN11rocrand_cpp25uniform_real_distributionE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">RealType</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1uniform__real__distribution"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">uniform_real_distribution</span></span></span><a class="headerlink" href="#_CPPv4I0EN11rocrand_cpp25uniform_real_distributionE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Produces random floating-point values uniformly distributed on the interval (0, 1]. </p>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>RealType</strong> – type of generated values. Only <code class="docutils literal notranslate"><span class="pre">float</span></code>, <code class="docutils literal notranslate"><span class="pre">double</span></code> and <code class="docutils literal notranslate"><span class="pre">half</span></code> types are supported. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I0EN11rocrand_cpp19normal_distributionE">
<span id="_CPPv3I0EN11rocrand_cpp19normal_distributionE"></span><span id="_CPPv2I0EN11rocrand_cpp19normal_distributionE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">RealType</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1normal__distribution"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">normal_distribution</span></span></span><a class="headerlink" href="#_CPPv4I0EN11rocrand_cpp19normal_distributionE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Produces random numbers according to a normal distribution. </p>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>RealType</strong> – type of generated values. Only <code class="docutils literal notranslate"><span class="pre">float</span></code>, <code class="docutils literal notranslate"><span class="pre">double</span></code> and <code class="docutils literal notranslate"><span class="pre">half</span></code> types are supported. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I0EN11rocrand_cpp22lognormal_distributionE">
<span id="_CPPv3I0EN11rocrand_cpp22lognormal_distributionE"></span><span id="_CPPv2I0EN11rocrand_cpp22lognormal_distributionE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">RealType</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="kt"><span class="pre">float</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1lognormal__distribution"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">lognormal_distribution</span></span></span><a class="headerlink" href="#_CPPv4I0EN11rocrand_cpp22lognormal_distributionE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Produces positive random numbers according to a log-normal distribution. </p>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>RealType</strong> – type of generated values. Only <code class="docutils literal notranslate"><span class="pre">float</span></code>, <code class="docutils literal notranslate"><span class="pre">double</span></code> and <code class="docutils literal notranslate"><span class="pre">half</span></code> types are supported. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I0EN11rocrand_cpp20poisson_distributionE">
<span id="_CPPv3I0EN11rocrand_cpp20poisson_distributionE"></span><span id="_CPPv2I0EN11rocrand_cpp20poisson_distributionE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">IntType</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1poisson__distribution"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">poisson_distribution</span></span></span><a class="headerlink" href="#_CPPv4I0EN11rocrand_cpp20poisson_distributionE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Produces random non-negative integer values distributed according to Poisson distribution. </p>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>IntType</strong> – type of generated values. Only <code class="docutils literal notranslate"><span class="pre">unsinged</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> type is supported. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_yEN11rocrand_cpp20philox4x32_10_engineE">
<span id="_CPPv3I_yEN11rocrand_cpp20philox4x32_10_engineE"></span><span id="_CPPv2I_yEN11rocrand_cpp20philox4x32_10_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeed</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="n"><span class="pre">ROCRAND_PHILOX4x32_DEFAULT_SEED</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1philox4x32__10__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">philox4x32_10_engine</span></span></span><a class="headerlink" href="#_CPPv4I_yEN11rocrand_cpp20philox4x32_10_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Pseudorandom number engine based Philox algorithm. </p>
<p>It generates random numbers of type <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> on the interval [0; 2^32 - 1]. Random numbers are generated in sets of four. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_yEN11rocrand_cpp13xorwow_engineE">
<span id="_CPPv3I_yEN11rocrand_cpp13xorwow_engineE"></span><span id="_CPPv2I_yEN11rocrand_cpp13xorwow_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeed</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="n"><span class="pre">ROCRAND_XORWOW_DEFAULT_SEED</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1xorwow__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">xorwow_engine</span></span></span><a class="headerlink" href="#_CPPv4I_yEN11rocrand_cpp13xorwow_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Pseudorandom number engine based XORWOW algorithm. </p>
<p><a class="reference internal" href="#classrocrand__cpp_1_1xorwow__engine"><span class="std std-ref">xorwow_engine</span></a> is a xorshift pseudorandom number engine based on XORWOW algorithm. It produces random numbers of type <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> on the interval [0; 2^32 - 1]. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_yEN11rocrand_cpp15mrg31k3p_engineE">
<span id="_CPPv3I_yEN11rocrand_cpp15mrg31k3p_engineE"></span><span id="_CPPv2I_yEN11rocrand_cpp15mrg31k3p_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeed</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="n"><span class="pre">ROCRAND_MRG31K3P_DEFAULT_SEED</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1mrg31k3p__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">mrg31k3p_engine</span></span></span><a class="headerlink" href="#_CPPv4I_yEN11rocrand_cpp15mrg31k3p_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Pseudorandom number engine based MRG31k3p CMRG. </p>
<p><a class="reference internal" href="#classrocrand__cpp_1_1mrg31k3p__engine"><span class="std std-ref">mrg31k3p_engine</span></a> is an implementation of MRG31k3p pseudorandom number generator, which is a Combined Multiple Recursive Generator (CMRG) created by Pierre L’Ecuyer. It produces random 32-bit <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> values on the interval [0; 2^32 - 1]. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_yEN11rocrand_cpp15mrg32k3a_engineE">
<span id="_CPPv3I_yEN11rocrand_cpp15mrg32k3a_engineE"></span><span id="_CPPv2I_yEN11rocrand_cpp15mrg32k3a_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeed</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="n"><span class="pre">ROCRAND_MRG32K3A_DEFAULT_SEED</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1mrg32k3a__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">mrg32k3a_engine</span></span></span><a class="headerlink" href="#_CPPv4I_yEN11rocrand_cpp15mrg32k3a_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Pseudorandom number engine based MRG32k3a CMRG. </p>
<p><a class="reference internal" href="#classrocrand__cpp_1_1mrg32k3a__engine"><span class="std std-ref">mrg32k3a_engine</span></a> is an implementation of MRG32k3a pseudorandom number generator, which is a Combined Multiple Recursive Generator (CMRG) created by Pierre L’Ecuyer. It produces random 32-bit <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> values on the interval [0; 2^32 - 1]. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_yEN11rocrand_cpp13mtgp32_engineE">
<span id="_CPPv3I_yEN11rocrand_cpp13mtgp32_engineE"></span><span id="_CPPv2I_yEN11rocrand_cpp13mtgp32_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeed</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="m"><span class="pre">0</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1mtgp32__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">mtgp32_engine</span></span></span><a class="headerlink" href="#_CPPv4I_yEN11rocrand_cpp13mtgp32_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Random number engine based on the Mersenne Twister for Graphic Processors algorithm. </p>
<p><a class="reference internal" href="#classrocrand__cpp_1_1mtgp32__engine"><span class="std std-ref">mtgp32_engine</span></a> is a random number engine based on the Mersenne Twister for Graphic Processors algorithm, which is a version of well-known Mersenne Twister algorithm. It produces high quality random numbers of type <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> on the interval [0; 2^32 - 1]. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_j_j_j_jEN11rocrand_cpp14lfsr113_engineE">
<span id="_CPPv3I_j_j_j_jEN11rocrand_cpp14lfsr113_engineE"></span><span id="_CPPv2I_j_j_j_jEN11rocrand_cpp14lfsr113_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeedX</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="n"><span class="pre">ROCRAND_LFSR113_DEFAULT_SEED_X</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeedY</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="n"><span class="pre">ROCRAND_LFSR113_DEFAULT_SEED_Y</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeedZ</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="n"><span class="pre">ROCRAND_LFSR113_DEFAULT_SEED_Z</span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeedW</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="n"><span class="pre">ROCRAND_LFSR113_DEFAULT_SEED_W</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1lfsr113__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">lfsr113_engine</span></span></span><a class="headerlink" href="#_CPPv4I_j_j_j_jEN11rocrand_cpp14lfsr113_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Random number engine based on the LFSR113 algorithm. </p>
<p><a class="reference internal" href="#classrocrand__cpp_1_1lfsr113__engine"><span class="std std-ref">lfsr113_engine</span></a> is an implementation of LFSR113 pseudorandom number generator, which is a linear feedback shift resgisters (LFSR) based generator created by Pierre L’Ecuyer. It produces random 32-bit <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> values on the interval [0; 2^32 - 1]. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_yEN11rocrand_cpp14mt19937_engineE">
<span id="_CPPv3I_yEN11rocrand_cpp14mt19937_engineE"></span><span id="_CPPv2I_yEN11rocrand_cpp14mt19937_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeed</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="m"><span class="pre">0ULL</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1mt19937__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">mt19937_engine</span></span></span><a class="headerlink" href="#_CPPv4I_yEN11rocrand_cpp14mt19937_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Random number engine based on the Mersenne Twister algorithm. </p>
<p><p>mt19937 is a random number engine based on the Mersenne Twister algorithm as proposed in “Mersenne Twister: A 623-Dimensionally Equidistributed Uniform</p>
<p>Pseudo-Random Number Generator”. It produces high quality random numbers of type</p>
<code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> on the interval [0; 2^32 - 1]. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_jEN11rocrand_cpp14sobol32_engineE">
<span id="_CPPv3I_jEN11rocrand_cpp14sobol32_engineE"></span><span id="_CPPv2I_jEN11rocrand_cpp14sobol32_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultNumDimensions</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="m"><span class="pre">1</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1sobol32__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">sobol32_engine</span></span></span><a class="headerlink" href="#_CPPv4I_jEN11rocrand_cpp14sobol32_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Sobol’s quasi-random sequence generator. </p>
<p><a class="reference internal" href="#classrocrand__cpp_1_1sobol32__engine"><span class="std std-ref">sobol32_engine</span></a> is quasi-random number engine which produced Sobol sequences. This implementation supports generating sequences in up to 20,000 dimensions. The engine produces random unsigned integers on the interval [0, 2^32 - 1]. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_jEN11rocrand_cpp24scrambled_sobol32_engineE">
<span id="_CPPv3I_jEN11rocrand_cpp24scrambled_sobol32_engineE"></span><span id="_CPPv2I_jEN11rocrand_cpp24scrambled_sobol32_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultNumDimensions</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="m"><span class="pre">1</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1scrambled__sobol32__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">scrambled_sobol32_engine</span></span></span><a class="headerlink" href="#_CPPv4I_jEN11rocrand_cpp24scrambled_sobol32_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Sobol’s scrambled quasi-random sequence generator. </p>
<p><a class="reference internal" href="#classrocrand__cpp_1_1scrambled__sobol32__engine"><span class="std std-ref">scrambled_sobol32_engine</span></a> is a quasi-random number engine which produces scrambled Sobol sequences. This implementation supports generating sequences in up to 20,000 dimensions. The engine produces random unsigned integers on the interval [0, 2^32 - 1]. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_jEN11rocrand_cpp14sobol64_engineE">
<span id="_CPPv3I_jEN11rocrand_cpp14sobol64_engineE"></span><span id="_CPPv2I_jEN11rocrand_cpp14sobol64_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultNumDimensions</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="m"><span class="pre">1</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1sobol64__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">sobol64_engine</span></span></span><a class="headerlink" href="#_CPPv4I_jEN11rocrand_cpp14sobol64_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Sobol’s quasi-random sequence generator. </p>
<p>sobol64 is a quasi-random number engine which produces Sobol sequences. This implementation supports generating sequences in up to 20,000 dimensions. The engine produces random unsigned integers on the interval [0, 2^64 - 1]. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_jEN11rocrand_cpp24scrambled_sobol64_engineE">
<span id="_CPPv3I_jEN11rocrand_cpp24scrambled_sobol64_engineE"></span><span id="_CPPv2I_jEN11rocrand_cpp24scrambled_sobol64_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultNumDimensions</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="m"><span class="pre">1</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1scrambled__sobol64__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">scrambled_sobol64_engine</span></span></span><a class="headerlink" href="#_CPPv4I_jEN11rocrand_cpp24scrambled_sobol64_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Sobol’s scrambled quasi-random sequence generator. </p>
<p><a class="reference internal" href="#classrocrand__cpp_1_1scrambled__sobol64__engine"><span class="std std-ref">scrambled_sobol64_engine</span></a> is a quasi-random number engine which produces scrambled Sobol sequences. This implementation supports generating sequences in up to 20,000 dimensions. The engine produces random unsigned long long integers on the interval [0, 2^64 - 1]. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_yEN11rocrand_cpp22threefry2x32_20_engineE">
<span id="_CPPv3I_yEN11rocrand_cpp22threefry2x32_20_engineE"></span><span id="_CPPv2I_yEN11rocrand_cpp22threefry2x32_20_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeed</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="m"><span class="pre">0</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1threefry2x32__20__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">threefry2x32_20_engine</span></span></span><a class="headerlink" href="#_CPPv4I_yEN11rocrand_cpp22threefry2x32_20_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Pseudorandom number engine based on 2 state ThreeFry. </p>
<p>It generates random numbers of type <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> on the interval [0; 2^32 - 1]. Random numbers are generated in sets of two. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_yEN11rocrand_cpp22threefry2x64_20_engineE">
<span id="_CPPv3I_yEN11rocrand_cpp22threefry2x64_20_engineE"></span><span id="_CPPv2I_yEN11rocrand_cpp22threefry2x64_20_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeed</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="m"><span class="pre">0</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1threefry2x64__20__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">threefry2x64_20_engine</span></span></span><a class="headerlink" href="#_CPPv4I_yEN11rocrand_cpp22threefry2x64_20_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Pseudorandom number engine based 2 state ThreeFry. </p>
<p>It generates random numbers of type <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> on the interval [0; 2^62 - 1]. Random numbers are generated in sets of two. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_yEN11rocrand_cpp22threefry4x32_20_engineE">
<span id="_CPPv3I_yEN11rocrand_cpp22threefry4x32_20_engineE"></span><span id="_CPPv2I_yEN11rocrand_cpp22threefry4x32_20_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeed</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="m"><span class="pre">0</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1threefry4x32__20__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">threefry4x32_20_engine</span></span></span><a class="headerlink" href="#_CPPv4I_yEN11rocrand_cpp22threefry4x32_20_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Pseudorandom number engine based on 2 state ThreeFry. </p>
<p>It generates random numbers of type <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> on the interval [0; 2^32 - 1]. Random numbers are generated in sets of two. </p>
</dd></dl>

<dl class="cpp class">
<dt class="sig sig-object cpp" id="_CPPv4I_yEN11rocrand_cpp22threefry4x64_20_engineE">
<span id="_CPPv3I_yEN11rocrand_cpp22threefry4x64_20_engineE"></span><span id="_CPPv2I_yEN11rocrand_cpp22threefry4x64_20_engineE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">DefaultSeed</span></span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="m"><span class="pre">0</span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classrocrand__cpp_1_1threefry4x64__20__engine"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">threefry4x64_20_engine</span></span></span><a class="headerlink" href="#_CPPv4I_yEN11rocrand_cpp22threefry4x64_20_engineE" title="Link to this definition">#</a><br /></dt>
<dd><div class="docutils container">
<em>#include &lt;rocrand.hpp&gt;</em></div>
<p>Pseudorandom number engine based 2 state ThreeFry. </p>
<p>It generates random numbers of type <code class="docutils literal notranslate"><span class="pre">unsigned</span></code> <code class="docutils literal notranslate"><span class="pre">int</span></code> on the interval [0; 2^62 - 1]. Random numbers are generated in sets of two. </p>
</dd></dl>

</dd></dl>

</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="data-type-support.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">rocRAND data type support</p>
      </div>
    </a>
    <a class="right-next"
       href="python-api.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Python API reference</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#device-functions">Device functions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP27rocrand_state_philox4x32_10K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417rocrand_discrete4P27rocrand_state_philox4x32_10K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP22rocrand_state_mrg31k3pK29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP22rocrand_state_mrg32k3aK29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP20rocrand_state_xorwowK29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP20rocrand_state_mtgp32K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP21rocrand_state_sobol32K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP31rocrand_state_scrambled_sobol32K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP21rocrand_state_sobol64K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP31rocrand_state_scrambled_sobol64K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP21rocrand_state_lfsr113K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP29rocrand_state_threefry2x32_20K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP29rocrand_state_threefry2x64_20K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP29rocrand_state_threefry4x32_20K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_discreteP29rocrand_state_threefry4x64_20K29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_discrete()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initK5uint4KjP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initK5uint4KjKyP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421skipahead_subsequencejP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">skipahead_subsequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418skipahead_sequencejP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">skipahead_sequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP27rocrand_state_philox4x32_10ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P27rocrand_state_philox4x32_10ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal4P27rocrand_state_philox4x32_10ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP27rocrand_state_philox4x32_10dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P27rocrand_state_philox4x32_10dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double4P27rocrand_state_philox4x32_10dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP22rocrand_state_mrg31k3pff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P22rocrand_state_mrg31k3pff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP22rocrand_state_mrg31k3pdd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P22rocrand_state_mrg31k3pdd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP22rocrand_state_mrg32k3aff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P22rocrand_state_mrg32k3aff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP22rocrand_state_mrg32k3add"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P22rocrand_state_mrg32k3add"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP20rocrand_state_xorwowff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P20rocrand_state_xorwowff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP20rocrand_state_xorwowdd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P20rocrand_state_xorwowdd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP20rocrand_state_mtgp32ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P20rocrand_state_mtgp32ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP20rocrand_state_mtgp32dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P20rocrand_state_mtgp32dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP21rocrand_state_sobol32ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP21rocrand_state_sobol32dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP31rocrand_state_scrambled_sobol32ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP31rocrand_state_scrambled_sobol32dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP21rocrand_state_sobol64ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP21rocrand_state_sobol64dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP31rocrand_state_scrambled_sobol64ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP31rocrand_state_scrambled_sobol64dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP21rocrand_state_lfsr113ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P21rocrand_state_lfsr113ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP21rocrand_state_lfsr113dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P21rocrand_state_lfsr113dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP29rocrand_state_threefry2x32_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P29rocrand_state_threefry2x32_20ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry2x32_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry2x32_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP29rocrand_state_threefry2x64_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P29rocrand_state_threefry2x64_20ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry2x64_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry2x64_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP29rocrand_state_threefry4x32_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P29rocrand_state_threefry4x32_20ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry4x32_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry4x32_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_log_normalP29rocrand_state_threefry4x64_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_log_normal2P29rocrand_state_threefry4x64_20ff"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_log_normal_doubleP29rocrand_state_threefry4x64_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_log_normal_double2P29rocrand_state_threefry4x64_20dd"><code class="docutils literal notranslate"><span class="pre">rocrand_log_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initKyKyKyP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421skipahead_subsequenceyP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">skipahead_subsequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418skipahead_sequenceyP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">skipahead_sequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initKyKyKyP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421skipahead_subsequenceyP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">skipahead_subsequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418skipahead_sequenceyP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">skipahead_sequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_make_state_mtgp32P20rocrand_state_mtgp32A_18mtgp32_fast_paramsiy"><code class="docutils literal notranslate"><span class="pre">rocrand_make_state_mtgp32()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_make_constantA_K18mtgp32_fast_paramsP13mtgp32_params"><code class="docutils literal notranslate"><span class="pre">rocrand_make_constant()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_mtgp32_block_copyP20rocrand_state_mtgp32P20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_mtgp32_block_copy()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_mtgp32_set_paramsP20rocrand_state_mtgp32P13mtgp32_params"><code class="docutils literal notranslate"><span class="pre">rocrand_mtgp32_set_params()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal4P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_normal4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double4P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP29rocrand_state_threefry2x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P29rocrand_state_threefry2x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP29rocrand_state_threefry2x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P29rocrand_state_threefry2x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP29rocrand_state_threefry2x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P29rocrand_state_threefry2x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP29rocrand_state_threefry2x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P29rocrand_state_threefry2x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP29rocrand_state_threefry4x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P29rocrand_state_threefry4x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP29rocrand_state_threefry4x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P29rocrand_state_threefry4x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_normalP29rocrand_state_threefry4x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_normal2P29rocrand_state_threefry4x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_normal_doubleP29rocrand_state_threefry4x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_normal_double2P29rocrand_state_threefry4x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_normal_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initKyKyKyP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv48rocrand4P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421skipahead_subsequenceyP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">skipahead_subsequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418skipahead_sequenceyP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">skipahead_sequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP27rocrand_state_philox4x32_10d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_poisson4P27rocrand_state_philox4x32_10d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP22rocrand_state_mrg31k3pd"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP22rocrand_state_mrg32k3ad"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP20rocrand_state_xorwowd"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP20rocrand_state_mtgp32d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP21rocrand_state_sobol32d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP31rocrand_state_scrambled_sobol32d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP21rocrand_state_sobol64d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP31rocrand_state_scrambled_sobol64d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP21rocrand_state_lfsr113d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP29rocrand_state_threefry2x32_20d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP29rocrand_state_threefry2x64_20d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP29rocrand_state_threefry4x32_20d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_poissonP29rocrand_state_threefry4x64_20d"><code class="docutils literal notranslate"><span class="pre">rocrand_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initPKjKjKjP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initPKyKyKjP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initPKjKjP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initPKyKjP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_uniform2P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_uniform4P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423rocrand_uniform_double2P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double2()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423rocrand_uniform_double4P27rocrand_state_philox4x32_10"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP22rocrand_state_mrg31k3p"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP22rocrand_state_mrg32k3a"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP20rocrand_state_mtgp32"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP21rocrand_state_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP31rocrand_state_scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP21rocrand_state_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP31rocrand_state_scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP21rocrand_state_lfsr113"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP29rocrand_state_threefry2x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry2x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP29rocrand_state_threefry2x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry2x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP29rocrand_state_threefry4x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry4x32_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415rocrand_uniformP29rocrand_state_threefry4x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_uniform_doubleP29rocrand_state_threefry4x64_20"><code class="docutils literal notranslate"><span class="pre">rocrand_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412rocrand_initKyKyKyP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand_init()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47rocrandP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">rocrand()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49skipaheadyP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">skipahead()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421skipahead_subsequenceyP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">skipahead_subsequence()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418skipahead_sequenceyP20rocrand_state_xorwow"><code class="docutils literal notranslate"><span class="pre">skipahead_sequence()</span></code></a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#c-host-api">C host API</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414rocrand_status"><code class="docutils literal notranslate"><span class="pre">rocrand_status</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status22ROCRAND_STATUS_SUCCESSE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_SUCCESS</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status31ROCRAND_STATUS_VERSION_MISMATCHE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_VERSION_MISMATCH</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status26ROCRAND_STATUS_NOT_CREATEDE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_NOT_CREATED</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status32ROCRAND_STATUS_ALLOCATION_FAILEDE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_ALLOCATION_FAILED</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status25ROCRAND_STATUS_TYPE_ERRORE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_TYPE_ERROR</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status27ROCRAND_STATUS_OUT_OF_RANGEE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_OUT_OF_RANGE</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status34ROCRAND_STATUS_LENGTH_NOT_MULTIPLEE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_LENGTH_NOT_MULTIPLE</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status40ROCRAND_STATUS_DOUBLE_PRECISION_REQUIREDE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_DOUBLE_PRECISION_REQUIRED</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status29ROCRAND_STATUS_LAUNCH_FAILUREE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_LAUNCH_FAILURE</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N14rocrand_status29ROCRAND_STATUS_INTERNAL_ERRORE"><code class="docutils literal notranslate"><span class="pre">rocrand_status::ROCRAND_STATUS_INTERNAL_ERROR</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_rng_type"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_DEFAULTE"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_DEFAULT</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_PSEUDO_XORWOWE"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_XORWOW</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type27ROCRAND_RNG_PSEUDO_MRG32K3AE"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_MRG32K3A</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_PSEUDO_MTGP32E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_MTGP32</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type32ROCRAND_RNG_PSEUDO_PHILOX4_32_10E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_PHILOX4_32_10</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type27ROCRAND_RNG_PSEUDO_MRG31K3PE"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_MRG31K3P</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_LFSR113E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_LFSR113</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type26ROCRAND_RNG_PSEUDO_MT19937E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_MT19937</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY2_32_20E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_THREEFRY2_32_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY2_64_20E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_THREEFRY2_64_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY4_32_20E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_THREEFRY4_32_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type34ROCRAND_RNG_PSEUDO_THREEFRY4_64_20E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_PSEUDO_THREEFRY4_64_20</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_QUASI_DEFAULTE"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_QUASI_DEFAULT</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_QUASI_SOBOL32E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_QUASI_SOBOL32</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type35ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL32E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL32</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type25ROCRAND_RNG_QUASI_SOBOL64E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_QUASI_SOBOL64</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_rng_type35ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL64E"><code class="docutils literal notranslate"><span class="pre">rocrand_rng_type::ROCRAND_RNG_QUASI_SCRAMBLED_SOBOL64</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_ordering"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_ordering28ROCRAND_ORDERING_PSEUDO_BESTE"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering::ROCRAND_ORDERING_PSEUDO_BEST</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_ordering31ROCRAND_ORDERING_PSEUDO_DEFAULTE"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering::ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_ordering30ROCRAND_ORDERING_PSEUDO_SEEDEDE"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering::ROCRAND_ORDERING_PSEUDO_SEEDED</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_ordering30ROCRAND_ORDERING_PSEUDO_LEGACYE"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering::ROCRAND_ORDERING_PSEUDO_LEGACY</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_ordering31ROCRAND_ORDERING_PSEUDO_DYNAMICE"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering::ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N16rocrand_ordering30ROCRAND_ORDERING_QUASI_DEFAULTE"><code class="docutils literal notranslate"><span class="pre">rocrand_ordering::ROCRAND_ORDERING_QUASI_DEFAULT</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428rocrand_direction_vector_set"><code class="docutils literal notranslate"><span class="pre">rocrand_direction_vector_set</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N28rocrand_direction_vector_set36ROCRAND_DIRECTION_VECTORS_32_JOEKUO6E"><code class="docutils literal notranslate"><span class="pre">rocrand_direction_vector_set::ROCRAND_DIRECTION_VECTORS_32_JOEKUO6</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N28rocrand_direction_vector_set46ROCRAND_SCRAMBLED_DIRECTION_VECTORS_32_JOEKUO6E"><code class="docutils literal notranslate"><span class="pre">rocrand_direction_vector_set::ROCRAND_SCRAMBLED_DIRECTION_VECTORS_32_JOEKUO6</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N28rocrand_direction_vector_set36ROCRAND_DIRECTION_VECTORS_64_JOEKUO6E"><code class="docutils literal notranslate"><span class="pre">rocrand_direction_vector_set::ROCRAND_DIRECTION_VECTORS_64_JOEKUO6</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N28rocrand_direction_vector_set46ROCRAND_SCRAMBLED_DIRECTION_VECTORS_64_JOEKUO6E"><code class="docutils literal notranslate"><span class="pre">rocrand_direction_vector_set::ROCRAND_SCRAMBLED_DIRECTION_VECTORS_64_JOEKUO6</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424rocrand_create_generatorP17rocrand_generator16rocrand_rng_type"><code class="docutils literal notranslate"><span class="pre">rocrand_create_generator()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429rocrand_create_generator_hostP17rocrand_generator16rocrand_rng_type"><code class="docutils literal notranslate"><span class="pre">rocrand_create_generator_host()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv438rocrand_create_generator_host_blockingP17rocrand_generator16rocrand_rng_type"><code class="docutils literal notranslate"><span class="pre">rocrand_create_generator_host_blocking()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425rocrand_destroy_generator17rocrand_generator"><code class="docutils literal notranslate"><span class="pre">rocrand_destroy_generator()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_generate17rocrand_generatorPj6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426rocrand_generate_long_long17rocrand_generatorPy6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_long_long()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421rocrand_generate_char17rocrand_generatorPh6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_char()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_generate_short17rocrand_generatorPt6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_short()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424rocrand_generate_uniform17rocrand_generatorPf6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_uniform()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431rocrand_generate_uniform_double17rocrand_generatorPd6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_uniform_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429rocrand_generate_uniform_half17rocrand_generatorP4half6size_t"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_uniform_half()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423rocrand_generate_normal17rocrand_generatorPf6size_tff"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430rocrand_generate_normal_double17rocrand_generatorPd6size_tdd"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428rocrand_generate_normal_half17rocrand_generatorP4half6size_t4half4half"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_normal_half()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427rocrand_generate_log_normal17rocrand_generatorPf6size_tff"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_log_normal()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv434rocrand_generate_log_normal_double17rocrand_generatorPd6size_tdd"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_log_normal_double()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv432rocrand_generate_log_normal_half17rocrand_generatorP4half6size_t4half4half"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_log_normal_half()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424rocrand_generate_poisson17rocrand_generatorPj6size_td"><code class="docutils literal notranslate"><span class="pre">rocrand_generate_poisson()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428rocrand_initialize_generator17rocrand_generator"><code class="docutils literal notranslate"><span class="pre">rocrand_initialize_generator()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_set_stream17rocrand_generator11hipStream_t"><code class="docutils literal notranslate"><span class="pre">rocrand_set_stream()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416rocrand_set_seed17rocrand_generatory"><code class="docutils literal notranslate"><span class="pre">rocrand_set_seed()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422rocrand_set_seed_uint417rocrand_generator5uint4"><code class="docutils literal notranslate"><span class="pre">rocrand_set_seed_uint4()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418rocrand_set_offset17rocrand_generatory"><code class="docutils literal notranslate"><span class="pre">rocrand_set_offset()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420rocrand_set_ordering17rocrand_generator16rocrand_ordering"><code class="docutils literal notranslate"><span class="pre">rocrand_set_ordering()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv445rocrand_set_quasi_random_generator_dimensions17rocrand_generatorj"><code class="docutils literal notranslate"><span class="pre">rocrand_set_quasi_random_generator_dimensions()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419rocrand_get_versionPi"><code class="docutils literal notranslate"><span class="pre">rocrand_get_version()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv435rocrand_create_poisson_distributiondP29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_create_poisson_distribution()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv436rocrand_create_discrete_distributionPKdjjP29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_create_discrete_distribution()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv437rocrand_destroy_discrete_distribution29rocrand_discrete_distribution"><code class="docutils literal notranslate"><span class="pre">rocrand_destroy_discrete_distribution()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431rocrand_get_direction_vectors32PPKj28rocrand_direction_vector_set"><code class="docutils literal notranslate"><span class="pre">rocrand_get_direction_vectors32()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431rocrand_get_direction_vectors64PPKy28rocrand_direction_vector_set"><code class="docutils literal notranslate"><span class="pre">rocrand_get_direction_vectors64()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv432rocrand_get_scramble_constants32PPKj"><code class="docutils literal notranslate"><span class="pre">rocrand_get_scramble_constants32()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv432rocrand_get_scramble_constants64PPKy"><code class="docutils literal notranslate"><span class="pre">rocrand_get_scramble_constants64()</span></code></a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#c-host-api-wrapper">C++ host API wrapper</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413philox4x32_10"><code class="docutils literal notranslate"><span class="pre">philox4x32_10</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv46xorwow"><code class="docutils literal notranslate"><span class="pre">xorwow</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv48mrg31k3p"><code class="docutils literal notranslate"><span class="pre">mrg31k3p</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv48mrg32k3a"><code class="docutils literal notranslate"><span class="pre">mrg32k3a</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv46mtgp32"><code class="docutils literal notranslate"><span class="pre">mtgp32</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47lfsr113"><code class="docutils literal notranslate"><span class="pre">lfsr113</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47mt19937"><code class="docutils literal notranslate"><span class="pre">mt19937</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412threefry2x32"><code class="docutils literal notranslate"><span class="pre">threefry2x32</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412threefry2x64"><code class="docutils literal notranslate"><span class="pre">threefry2x64</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412threefry4x32"><code class="docutils literal notranslate"><span class="pre">threefry4x32</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412threefry4x64"><code class="docutils literal notranslate"><span class="pre">threefry4x64</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47sobol32"><code class="docutils literal notranslate"><span class="pre">sobol32</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417scrambled_sobol32"><code class="docutils literal notranslate"><span class="pre">scrambled_sobol32</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47sobol64"><code class="docutils literal notranslate"><span class="pre">sobol64</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417scrambled_sobol64"><code class="docutils literal notranslate"><span class="pre">scrambled_sobol64</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421default_random_engine"><code class="docutils literal notranslate"><span class="pre">default_random_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413random_device"><code class="docutils literal notranslate"><span class="pre">random_device</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47versionv"><code class="docutils literal notranslate"><span class="pre">version()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N11rocrand_cpp5errorE"><code class="docutils literal notranslate"><span class="pre">error</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0EN11rocrand_cpp24uniform_int_distributionE"><code class="docutils literal notranslate"><span class="pre">uniform_int_distribution</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0EN11rocrand_cpp25uniform_real_distributionE"><code class="docutils literal notranslate"><span class="pre">uniform_real_distribution</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0EN11rocrand_cpp19normal_distributionE"><code class="docutils literal notranslate"><span class="pre">normal_distribution</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0EN11rocrand_cpp22lognormal_distributionE"><code class="docutils literal notranslate"><span class="pre">lognormal_distribution</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0EN11rocrand_cpp20poisson_distributionE"><code class="docutils literal notranslate"><span class="pre">poisson_distribution</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp20philox4x32_10_engineE"><code class="docutils literal notranslate"><span class="pre">philox4x32_10_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp13xorwow_engineE"><code class="docutils literal notranslate"><span class="pre">xorwow_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp15mrg31k3p_engineE"><code class="docutils literal notranslate"><span class="pre">mrg31k3p_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp15mrg32k3a_engineE"><code class="docutils literal notranslate"><span class="pre">mrg32k3a_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp13mtgp32_engineE"><code class="docutils literal notranslate"><span class="pre">mtgp32_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_j_j_j_jEN11rocrand_cpp14lfsr113_engineE"><code class="docutils literal notranslate"><span class="pre">lfsr113_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp14mt19937_engineE"><code class="docutils literal notranslate"><span class="pre">mt19937_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_jEN11rocrand_cpp14sobol32_engineE"><code class="docutils literal notranslate"><span class="pre">sobol32_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_jEN11rocrand_cpp24scrambled_sobol32_engineE"><code class="docutils literal notranslate"><span class="pre">scrambled_sobol32_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_jEN11rocrand_cpp14sobol64_engineE"><code class="docutils literal notranslate"><span class="pre">sobol64_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_jEN11rocrand_cpp24scrambled_sobol64_engineE"><code class="docutils literal notranslate"><span class="pre">scrambled_sobol64_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp22threefry2x32_20_engineE"><code class="docutils literal notranslate"><span class="pre">threefry2x32_20_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp22threefry2x64_20_engineE"><code class="docutils literal notranslate"><span class="pre">threefry2x64_20_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp22threefry4x32_20_engineE"><code class="docutils literal notranslate"><span class="pre">threefry4x32_20_engine</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_yEN11rocrand_cpp22threefry4x64_20_engineE"><code class="docutils literal notranslate"><span class="pre">threefry4x64_20_engine</span></code></a></li>
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
