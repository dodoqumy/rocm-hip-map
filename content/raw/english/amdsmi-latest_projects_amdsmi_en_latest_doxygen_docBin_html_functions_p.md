---
title: "AMD SMI: Data Fields &#8212; AMD SMI 26.2.2 documentation"
source_url: "https://rocm.docs.amd.com/projects/amdsmi/en/latest/doxygen/docBin/html/functions_p.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:25:17.502760+00:00
content_hash: "78309a84b782823f"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>AMD SMI: Data Fields &#8212; AMD SMI 26.2.2 documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/docBin/html/functions_p';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Data Fields" href="functions_r.html" />
    <link rel="prev" title="Data Fields" href="functions_o.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-amdsmi" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/docBin/html/functions_p.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l3 current active has-children"><a class="reference internal" href="functions_all.html">All</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
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
<li class="toctree-l4 current active"><a class="current reference internal" href="#">p</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_r.html">r</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_s.html">s</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_t.html">t</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_u.html">u</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_v.html">v</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_w.html">w</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_x.html">x</a></li>
</ul>
</details></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="functions_vars_variables.html">Variables</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="functions_vars.html">a</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_b.html">b</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_c.html">c</a></li>
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
    
    
    <li class="breadcrumb-item"><a href="functions_all.html" class="nav-link">All</a></li>
    
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">AMD SMI: Data Fields</span></li>
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
    <h1>Data Fields</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="data-fields">
<h1>Data Fields<a class="headerlink" href="#data-fields" title="Link to this heading">#</a></h1>
<div class="doxygen-content docutils container">
<!-- HTML header for doxygen 1.9.6-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>AMD SMI: Data Fields</title>
<link href="tabs.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="dynsections.js"></script>
<link href="stylesheet.css" rel="stylesheet" type="text/css" />
<link href="extra_stylesheet.css" rel="stylesheet" type="text/css"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-amdsmi" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/docBin/html/functions_p.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
<div class="textblock">Here is a list of all documented struct and union fields with links to the struct/union documentation for each field:</div>

<h3><a id="index_p" name="index_p"></a>- p -</h3><ul>
<li>page_address&#160;:&#160;<a class="el" href="structamdsmi__retired__page__record__t.html#a7bad89b76386a81c145fbd37a952663b">amdsmi_retired_page_record_t</a></li>
<li>page_size&#160;:&#160;<a class="el" href="structamdsmi__retired__page__record__t.html#a22f2ea24f39c0197b641225b3f69a93f">amdsmi_retired_page_record_t</a></li>
<li>partition_id&#160;:&#160;<a class="el" href="structamdsmi__cper__hdr__t.html#ac2366cf57778f42a72e76bb166dfe2bb">amdsmi_cper_hdr_t</a></li>
<li>partition_resource&#160;:&#160;<a class="el" href="structamdsmi__accelerator__partition__resource__profile__t.html#a0f4d1f5239f95f8686c828310d75ce17">amdsmi_accelerator_partition_resource_profile_t</a></li>
<li>pcie_bandwidth&#160;:&#160;<a class="el" href="structamdsmi__pcie__info__t_1_1pcie__metric__.html#a7f0705d9837424482a5b66df9fa00b49">amdsmi_pcie_info_t::pcie_metric_</a></li>
<li>pcie_bandwidth_acc&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#aaa4bb66a86af5cd95505c348234cd74b">amdsmi_gpu_metrics_t</a>, <a class="el" href="structamdsmi__hsmp__metrics__table__t.html#ad5dce2ab70dde549af5f86cea8bf4f93">amdsmi_hsmp_metrics_table_t</a></li>
<li>pcie_bandwidth_inst&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#afdbf1b04d634fa362785eb1b70107ce2">amdsmi_gpu_metrics_t</a></li>
<li>pcie_interface_version&#160;:&#160;<a class="el" href="structamdsmi__pcie__info__t_1_1pcie__static__.html#afb06f2dfcbc054670e1501ffcb79579d">amdsmi_pcie_info_t::pcie_static_</a></li>
<li>pcie_l0_to_recov_count_acc&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#a5e54cba308f535bcff3baec4f44df9ea">amdsmi_gpu_metrics_t</a></li>
<li>pcie_l0_to_recovery_count&#160;:&#160;<a class="el" href="structamdsmi__pcie__info__t_1_1pcie__metric__.html#aa73955954d63b907ce7f730e2437838d">amdsmi_pcie_info_t::pcie_metric_</a></li>
<li>pcie_lc_perf_other_end_recovery&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#a3e53df7f7a5614be757aeb7ad0127edc">amdsmi_gpu_metrics_t</a></li>
<li>pcie_lc_perf_other_end_recovery_count&#160;:&#160;<a class="el" href="structamdsmi__pcie__info__t_1_1pcie__metric__.html#aec4d9ae82827cbfb57a3b99771dd9a23">amdsmi_pcie_info_t::pcie_metric_</a></li>
<li>pcie_link_speed&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#aa1dd73d3dddd8814e22bf2d5879546db">amdsmi_gpu_metrics_t</a></li>
<li>pcie_link_width&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#a5fb3f8725593490b262c92240a3fcf64">amdsmi_gpu_metrics_t</a></li>
<li>pcie_nak_rcvd_count_acc&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#afbe008ad9848b43843c067f4b7d9efe2">amdsmi_gpu_metrics_t</a></li>
<li>pcie_nak_received_count&#160;:&#160;<a class="el" href="structamdsmi__pcie__info__t_1_1pcie__metric__.html#a05df3804e79cd5eb24609062fdfb318a">amdsmi_pcie_info_t::pcie_metric_</a></li>
<li>pcie_nak_sent_count&#160;:&#160;<a class="el" href="structamdsmi__pcie__info__t_1_1pcie__metric__.html#ab9faa3c8e1053abe29c2dfbf8636eab0">amdsmi_pcie_info_t::pcie_metric_</a></li>
<li>pcie_nak_sent_count_acc&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#af71b831bd95e02a734d7efe874fc2159">amdsmi_gpu_metrics_t</a></li>
<li>pcie_replay_count&#160;:&#160;<a class="el" href="structamdsmi__pcie__info__t_1_1pcie__metric__.html#a3cf6a147d77cd7a998bf345436544f43">amdsmi_pcie_info_t::pcie_metric_</a></li>
<li>pcie_replay_count_acc&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#accef27c58de51883b7d35bb83467d5ea">amdsmi_gpu_metrics_t</a></li>
<li>pcie_replay_roll_over_count&#160;:&#160;<a class="el" href="structamdsmi__pcie__info__t_1_1pcie__metric__.html#ad8f090afb20047e7e86c93cebe77f32e">amdsmi_pcie_info_t::pcie_metric_</a></li>
<li>pcie_replay_rover_count_acc&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#ac2057df791842578f55807421de88567">amdsmi_gpu_metrics_t</a></li>
<li>pcie_speed&#160;:&#160;<a class="el" href="structamdsmi__pcie__info__t_1_1pcie__metric__.html#a7b2f02a949e39513c073b936ab41c0d3">amdsmi_pcie_info_t::pcie_metric_</a></li>
<li>pcie_width&#160;:&#160;<a class="el" href="structamdsmi__pcie__info__t_1_1pcie__metric__.html#a650398a5589c3d6888520c180563a870">amdsmi_pcie_info_t::pcie_metric_</a></li>
<li>per_gfx_clk_below_host_limit&#160;:&#160;<a class="el" href="structamdsmi__violation__status__t.html#a8a6ad199dbac1c0b13e3deeda583b26a">amdsmi_violation_status_t</a></li>
<li>per_gfx_clk_below_host_limit_pwr&#160;:&#160;<a class="el" href="structamdsmi__violation__status__t.html#a6e1c7ad49a870b4b6f47d5f3b8e661d2">amdsmi_violation_status_t</a></li>
<li>per_gfx_clk_below_host_limit_thm&#160;:&#160;<a class="el" href="structamdsmi__violation__status__t.html#a086c67b1738924b7ce20696770d74634">amdsmi_violation_status_t</a></li>
<li>per_gfx_clk_below_host_limit_total&#160;:&#160;<a class="el" href="structamdsmi__violation__status__t.html#a32c0ca23cb68d405827351b24923d88a">amdsmi_violation_status_t</a></li>
<li>per_hbm_thrm&#160;:&#160;<a class="el" href="structamdsmi__violation__status__t.html#a4f965230d94eb6148afcb7da74822520">amdsmi_violation_status_t</a></li>
<li>per_low_utilization&#160;:&#160;<a class="el" href="structamdsmi__violation__status__t.html#a4539b4535b7f9d962579d9b87933fc9a">amdsmi_violation_status_t</a></li>
<li>per_ppt_pwr&#160;:&#160;<a class="el" href="structamdsmi__violation__status__t.html#a66c2904216ebe8d3bdce238ecc07e421">amdsmi_violation_status_t</a></li>
<li>per_prochot_thrm&#160;:&#160;<a class="el" href="structamdsmi__violation__status__t.html#a51e6df313ce922169cb6726a31441974">amdsmi_violation_status_t</a></li>
<li>per_socket_thrm&#160;:&#160;<a class="el" href="structamdsmi__violation__status__t.html#a9328395e03c70e09950a678070be79ce">amdsmi_violation_status_t</a></li>
<li>per_vr_thrm&#160;:&#160;<a class="el" href="structamdsmi__violation__status__t.html#a93cb941e1fc289bdbe43689f02daeb49">amdsmi_violation_status_t</a></li>
<li>persistence_info&#160;:&#160;<a class="el" href="structamdsmi__cper__hdr__t.html#a2df1c3d4874088d0ddff21c18f469d53">amdsmi_cper_hdr_t</a></li>
<li>policies&#160;:&#160;<a class="el" href="structamdsmi__dpm__policy__t.html#ab3b5f487cdc3e18b62a0c697428310b6">amdsmi_dpm_policy_t</a></li>
<li>power&#160;:&#160;<a class="el" href="structamdsmi__dimm__power__t.html#acc70a83f95acba81b91f5c5d1dfa4779">amdsmi_dimm_power_t</a></li>
<li>power_cap&#160;:&#160;<a class="el" href="structamdsmi__power__cap__info__t.html#a062d13753882d3ca0a575fd2bc126ae9">amdsmi_power_cap_info_t</a></li>
<li>power_limit&#160;:&#160;<a class="el" href="structamdsmi__power__info__t.html#a8208a13aa6fda0701b671e3b2cbc23c9">amdsmi_power_info_t</a></li>
<li>ppt_residency_acc&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#a51e2ffa9052dd4869f12d64cca8cfb49">amdsmi_gpu_metrics_t</a>, <a class="el" href="structamdsmi__hsmp__metrics__table__t.html#ae3c63a33c2da60f68133a5d976aa296c">amdsmi_hsmp_metrics_table_t</a></li>
<li>process_id&#160;:&#160;<a class="el" href="structamdsmi__process__info__t.html#a1b7efc75558513a5deab51288cb4563f">amdsmi_process_info_t</a></li>
<li>processor_handle&#160;:&#160;<a class="el" href="structamdsmi__evt__notification__data__t.html#a56853b387ce794d6dfb7647c29d85c1d">amdsmi_evt_notification_data_t</a></li>
<li>prochot_residency_acc&#160;:&#160;<a class="el" href="structamdsmi__gpu__metrics__t.html#abfc4964fc7655f4f137b4b178fd4e666">amdsmi_gpu_metrics_t</a>, <a class="el" href="structamdsmi__hsmp__metrics__table__t.html#a3868f0a9a0a1481a38cf37a54e39687c">amdsmi_hsmp_metrics_table_t</a></li>
<li>profile_index&#160;:&#160;<a class="el" href="structamdsmi__accelerator__partition__profile__t.html#a43683ea61f929ad96455d9aa380442ab">amdsmi_accelerator_partition_profile_t</a></li>
<li>profile_type&#160;:&#160;<a class="el" href="structamdsmi__accelerator__partition__profile__t.html#a8aaa63ea57c4c2192ea2059ea384e5fe">amdsmi_accelerator_partition_profile_t</a></li>
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
       href="functions_o.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Data Fields</p>
      </div>
    </a>
    <a class="right-next"
       href="functions_r.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Data Fields</p>
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
