---
title: "AMD SMI: Data Fields - Variables &#8212; AMD SMI 26.2.2 documentation"
source_url: "https://rocm.docs.amd.com/projects/amdsmi/en/latest/doxygen/docBin/html/functions_vars_c.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:25:06.950088+00:00
content_hash: "8c99dd0346e7c70b"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>AMD SMI: Data Fields - Variables &#8212; AMD SMI 26.2.2 documentation</title>
  
  
  
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
  <link href="../../../_static/styles/theme.css?digest=8878045cc6db502f8baf" rel="stylesheet" />
<link href="../../../_static/styles/pydata-sphinx-theme.css?digest=8878045cc6db502f8baf" rel="stylesheet" />

    <link rel="stylesheet" type="text/css" href="../../../_static/pygments.css?v=8f2a1f02" />
    <link rel="stylesheet" type="text/css" href="../../../_static/styles/sphinx-book-theme.css?v=a3416100" />
    <link rel="stylesheet" type="text/css" href="../../../_static/mystnb.8ecb98da25f57f5357bf6f572d296f466b2cfe2517ffebfabe82451661e28f02.css" />
    <link rel="stylesheet" type="text/css" href="../../../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../../../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../../../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../../../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../../../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../../../_static/sphinx-design.min.css?v=95c83b7e" />
  
  <!-- So that users can add custom icons -->
  <script src="../../../_static/scripts/fontawesome.js?digest=8878045cc6db502f8baf"></script>
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../../../_static/scripts/bootstrap.js?digest=8878045cc6db502f8baf" />
<link rel="preload" as="script" href="../../../_static/scripts/pydata-sphinx-theme.js?digest=8878045cc6db502f8baf" />

    <script src="../../../_static/documentation_options.js?v=de9f5bbb"></script>
    <script src="../../../_static/doctools.js?v=9bcbadda"></script>
    <script src="../../../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../../../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../../../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../../../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../../../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../../../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../../../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../../../_static/search.js?v=90a4452c"></script>
    <script src="../../../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
    <script src="../../../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/docBin/html/functions_vars_c';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Data Fields - Variables" href="functions_vars_d.html" />
    <link rel="prev" title="Data Fields - Variables" href="functions_vars_b.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-amdsmi" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/docBin/html/functions_vars_c.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
  <body data-bs-spy="scroll" data-bs-target=".bd-toc-nav" data-offset="180" data-bs-root-margin="0px 0px -60%" data-default-mode="">

  
  
  <div id="pst-skip-link" class="skip-link d-print-none"><a href="#main-content">Skip to main content</a></div>
  
  <div id="pst-scroll-pixel-helper"></div>
  
  <button type="button" class="btn rounded-pill" id="pst-back-to-top">
    <i class="fa-solid fa-arrow-up"></i>Back to top</button>

  
  <dialog id="pst-search-dialog">
    
<form class="bd-search d-flex align-items-center"
      action="../../../search.html"
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
                    <img src="../../../_static/images/amd-header-logo.svg" alt="AMD Logo" title="AMD Logo" width="90" class="d-inline-block align-text-top hover-opacity"/>
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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/rocm-systems" id="navgithub" role="button" aria-expanded="false" target="_blank" >
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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/rocm-systems/issues/new/choose" id="navsupport" role="button" aria-expanded="false" target="_blank" >
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

  
    
  

<a class="navbar-brand logo" href="../../../index.html">
  
  
  
  
  
  
    <p class="title logo__title">AMD SMI 26.2.2 documentation</p>
  
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
<li class="toctree-l1"><a class="reference internal" href="../../../install/install.html">Library and CLI tool installation</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../install/build.html">Build from source</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/amdsmi-cpp-lib.html">C++ library usage</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/amdsmi-py-lib.html">Python library usage</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/amdsmi-go-lib.html">Go library usage</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/amdsmi-cli-tool.html">CLI tool usage</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/setup-docker-container.html">Use AMD SMI in a Docker container</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active has-children"><a class="reference internal" href="../../../reference/amdsmi-cpp-api.html">C++ API</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2"><a class="reference internal" href="topics.html">Modules</a></li>
<li class="toctree-l2"><a class="reference internal" href="files.html">Files</a></li>
<li class="toctree-l2"><a class="reference internal" href="globals.html">Globals</a></li>
<li class="toctree-l2"><a class="reference internal" href="annotated.html">Data structures</a></li>
<li class="toctree-l2 current active has-children"><a class="reference internal" href="functions_data_fields.html">Data fields</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l3 has-children"><a class="reference internal" href="functions_all.html">All</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="functions.html">a</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_b.html">b</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_c.html">c</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_d.html">d</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_e.html">e</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_f.html">f</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_g.html">g</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_h.html">h</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_i.html">i</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_j.html">j</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_k.html">k</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_l.html">l</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_m.html">m</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_n.html">n</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_o.html">o</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_p.html">p</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_r.html">r</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_s.html">s</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_t.html">t</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_u.html">u</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_v.html">v</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_w.html">w</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_x.html">x</a></li>
</ul>
</details></li>
<li class="toctree-l3 current active has-children"><a class="reference internal" href="functions_vars_variables.html">Variables</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l4"><a class="reference internal" href="functions_vars.html">a</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_b.html">b</a></li>
<li class="toctree-l4 current active"><a class="current reference internal" href="#">c</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_d.html">d</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_e.html">e</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_f.html">f</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_g.html">g</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_h.html">h</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_i.html">i</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_j.html">j</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_k.html">k</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_l.html">l</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_m.html">m</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_n.html">n</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_o.html">o</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_p.html">p</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_r.html">r</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_s.html">s</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_t.html">t</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_u.html">u</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_v.html">v</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_w.html">w</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_x.html">x</a></li>
</ul>
</details></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../../reference/amdsmi-py-api.html">Python API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../reference/amdsmi-go-api.html">Go API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../reference/changelog.html">Changelog</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../conceptual/ras.html">Reliability, availability, serviceability (RAS)</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Tutorials</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-systems/tree/latest/projects/amdsmi/example">AMD SMI examples (GitHub)</a></li>
<li class="toctree-l1"><a class="reference external" href="https://rocm.blogs.amd.com/software-tools-optimization/amd-smi-overview/README.html">AMD SMI CLI walkthrough</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">About</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../license.html">License</a></li>
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
      <a href="../../../index.html" class="nav-link" aria-label="Home">
        <i class="fa-solid fa-home"></i>
      </a>
    </li>
    
    <li class="breadcrumb-item"><a href="../../../reference/amdsmi-cpp-api.html" class="nav-link">AMD SMI C++ API reference</a></li>
    
    
    <li class="breadcrumb-item"><a href="functions_data_fields.html" class="nav-link">Data Fields</a></li>
    
    
    <li class="breadcrumb-item"><a href="functions_vars_variables.html" class="nav-link">Variables</a></li>
    
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">AMD SMI: Data Fields - Variables</span></li>
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
    <h1>Data Fields - Variables</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="data-fields-variables">
<h1>Data Fields - Variables<a class="headerlink" href="#data-fields-variables" title="Link to this heading">#</a></h1>
<div class="doxygen-content docutils container">
<!-- HTML header for doxygen 1.9.6-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>AMD SMI: Data Fields - Variables</title>
<link href="tabs.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="dynsections.js"></script>
<link href="stylesheet.css" rel="stylesheet" type="text/css" />
<link href="extra_stylesheet.css" rel="stylesheet" type="text/css"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-amdsmi" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/docBin/html/functions_vars_c.html" /><meta name="readthedocs-http-status" content="200" /></head>
<body>
<div id="top"><!-- do not remove this div, it is closed by doxygen! -->
<!-- Generated by Doxygen 1.9.8 -->
<script type="text/javascript" src="menudata.js"></script>
<script type="text/javascript" src="menu.js"></script>
<script type="text/javascript">
/* @license magnet:?xt=urn:btih:d3d9a9a6595521f9666a5e94cc830dab83b65699&amp;dn=expat.txt MIT */
$(function() {
  initMenu('',false,false,'search.php','Search');
});
/* @license-end */
</script>
<div id="main-nav"></div>
</div><!-- top -->
<div class="contents">
<div class="textblock">Here is a list of all documented variables with links to the struct/union documentation for each field:</div>

<h3><a id="index_c" name="index_c"></a>- c -</h3><ul>
<li>cache_properties&#160;:&#160;<a class="el" href="structamdsmi__gpu__cache__info__t_1_1cache__.html#aba20f166b843821d1ae5e82bcbbd3e4e">amdsmi_gpu_cache_info_t::cache_</a></li>
<li>cache_size&#160;:&#160;<a class="el" href="structamdsmi__gpu__cache__info__t_1_1cache__.html#a1ca3ad66f9f16ad538e90bb484214b23">amdsmi_gpu_cache_info_t::cache_</a></li>
<li>ccd_energy_acc&#160;:&#160;<a class="el" href="structamdsmi__hsmp__metrics__table__t.html#a4002dc6abd5b1c554b41bb1b070b9e59">amdsmi_hsmp_metrics_table_t</a></li>
<li>cclk_frequency_acc&#160;:&#160;<a class="el" href="structamdsmi__hsmp__metrics__table__t.html#a0ad623636987a20f1c4d99ae1dd1c84b">amdsmi_hsmp_metrics_table_t</a></li>
<li>cclk_frequency_limit&#160;:&#160;<a class="el" href="structamdsmi__hsmp__metrics__table__t.html#aa106c2d94c6c72d3967739a8e165eaa8">amdsmi_hsmp_metrics_table_t</a></li>
<li>clk&#160;:&#160;<a class="el" href="structamdsmi__clk__info__t.html#a12556ef6d65866e4c1a1192b788df34c">amdsmi_clk_info_t</a></li>
<li>clk_deep_sleep&#160;:&#160;<a class="el" href="structamdsmi__clk__info__t.html#a42fda71c1bbd0b2a9366075cc9cd24fb">amdsmi_clk_info_t</a></li>
<li>clk_locked&#160;:&#160;<a class="el" href="structamdsmi__clk__info__t.html#a3fcddcbb576c948a134cb4654dbea2e3">amdsmi_clk_info_t</a></li>
<li>core_count&#160;:&#160;<a class="el" href="structamdsmi__cpu__info__t.html#af43685be42337760020cee3e04f2aca9">amdsmi_cpu_info_t</a></li>
<li>core_id&#160;:&#160;<a class="el" href="structamdsmi__cpu__info__t.html#a441b34ddd8e0a9a7d5ba7a92d4ccfa6f">amdsmi_cpu_info_t</a></li>
<li>cores_per_socket&#160;:&#160;<a class="el" href="structamdsmi__cpu__info__t.html#ac13b07f128a5f9323680422a8cf7eb0c">amdsmi_cpu_info_t</a></li>
<li>correctable_count&#160;:&#160;<a class="el" href="structamdsmi__error__count__t.html#a1264fa52597be4a409f782ec86de7f2d">amdsmi_error_count_t</a></li>
<li>cpu_family_id&#160;:&#160;<a class="el" href="structamdsmi__cpu__info__t.html#a66dd1fb7ec967c9d53c52cc5f70cd848">amdsmi_cpu_info_t</a></li>
<li>cpu_mem&#160;:&#160;<a class="el" href="structamdsmi__proc__info__t_1_1memory__usage__.html#adcd71f68ed42886c2bcbffffd9d83afa">amdsmi_proc_info_t::memory_usage_</a></li>
<li>cu_occupancy&#160;:&#160;<a class="el" href="structamdsmi__proc__info__t.html#ac2283044f1770ca3fb73616fac758a21">amdsmi_proc_info_t</a>, <a class="el" href="structamdsmi__process__info__t.html#a3a0f94bef3dfab974003d476524d4057">amdsmi_process_info_t</a></li>
<li>curr_mclk_range&#160;:&#160;<a class="el" href="structamdsmi__od__volt__freq__data__t.html#a0bfc34ae49b0e09a8e5971c85cfc9b6a">amdsmi_od_volt_freq_data_t</a></li>
<li>curr_sclk_range&#160;:&#160;<a class="el" href="structamdsmi__od__volt__freq__data__t.html#aae21883a75c1105d329ead6b76e153b7">amdsmi_od_volt_freq_data_t</a></li>
<li>current&#160;:&#160;<a class="el" href="structamdsmi__dpm__policy__t.html#a43da7daaa0c7303edfe58de1c0638b98">amdsmi_dpm_policy_t</a>, <a class="el" href="structamdsmi__frequencies__t.html#a1d1698729e256c965be5e31acb200435">amdsmi_frequencies_t</a>, <a class="el" href="structamdsmi__power__profile__status__t.html#a6fcd26a6fac85dc1a640cf7152a7e873">amdsmi_power_profile_status_t</a></li>
<li>current_dclk0s&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#a69e133cd2b1b2dbb83f14688f5f118cb">amdsmi_gpu_metrics_t</a></li>
<li>current_fan_speed&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#a350c5ba293c983a87ee6663a8b08869c">amdsmi_gpu_metrics_t</a></li>
<li>current_freq_range&#160;:&#160;<a class="el" href="structamdsmi__frequency__range__t.html#a680408f973aebdb87adfad5c82018e28">amdsmi_frequency_range_t</a></li>
<li>current_gfxclk&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#ad44b04b3d97abec078440b60acca672d">amdsmi_gpu_metrics_t</a></li>
<li>current_gfxclks&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#ad4eab2bfd40ea9067c6816df1c2a8f07">amdsmi_gpu_metrics_t</a></li>
<li>current_partition_id&#160;:&#160;<a class="el" href="structamdsmi__kfd__info__t.html#a275d99c3dc6935fc88659d4c8c3fc3d8">amdsmi_kfd_info_t</a></li>
<li>current_socclks&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#a50ef3fbcbbca8d991ee4a5ef9613ae14">amdsmi_gpu_metrics_t</a></li>
<li>current_socket_power&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#a492b396b9bde0848cc00c281be75c30f">amdsmi_gpu_metrics_t</a>, <a class="el" href="structamdsmi__power__info__t.html#a862241df891d3436554a34774165b719">amdsmi_power_info_t</a></li>
<li>current_vclk0s&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#ae87613c5daf7b1f1c2bfc47672f3f0b7">amdsmi_gpu_metrics_t</a></li>
<li>curve&#160;:&#160;<a class="el" href="structamdsmi__od__volt__freq__data__t.html#ad021ae1bc45e1cc4539eb9778f4ee7aa">amdsmi_od_volt_freq_data_t</a></li>
</ul>
</div><!-- contents -->
<!-- HTML footer for doxygen 1.9.6-->
<!-- start footer part -->
</div>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="functions_vars_b.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Data Fields - Variables</p>
      </div>
    </a>
    <a class="right-next"
       href="functions_vars_d.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Data Fields - Variables</p>
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
  <script defer src="../../../_static/scripts/bootstrap.js?digest=8878045cc6db502f8baf"></script>
<script defer src="../../../_static/scripts/pydata-sphinx-theme.js?digest=8878045cc6db502f8baf"></script>

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
    <img id="rdc-watermark" src="../../../_static/images/alpha-watermark.svg" alt="DRAFT watermark"/>
</div> -->
  </body>
</html>
