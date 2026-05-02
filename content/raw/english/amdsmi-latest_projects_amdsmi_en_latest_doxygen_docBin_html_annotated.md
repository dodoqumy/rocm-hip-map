---
title: "AMD SMI: Data Structures &#8212; AMD SMI 26.2.2 documentation"
source_url: "https://rocm.docs.amd.com/projects/amdsmi/en/latest/doxygen/docBin/html/annotated.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:13:04.136622+00:00
content_hash: "dc93e0be411038de"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>AMD SMI: Data Structures &#8212; AMD SMI 26.2.2 documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/docBin/html/annotated';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Data Fields" href="functions_data_fields.html" />
    <link rel="prev" title="Globals" href="globals.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-amdsmi" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/docBin/html/annotated.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l2 current active"><a class="current reference internal" href="#">Data structures</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="functions_data_fields.html">Data fields</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
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
    
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">AMD SMI: Data Structures</span></li>
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
    <h1>Data Structures</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="data-structures">
<h1>Data Structures<a class="headerlink" href="#data-structures" title="Link to this heading">#</a></h1>
<div class="doxygen-content docutils container">
<!-- HTML header for doxygen 1.9.6-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>AMD SMI: Data Structures</title>
<link href="tabs.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="dynsections.js"></script>
<link href="stylesheet.css" rel="stylesheet" type="text/css" />
<link href="extra_stylesheet.css" rel="stylesheet" type="text/css"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-amdsmi" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/docBin/html/annotated.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
<div class="header">
  <div class="headertitle"><div class="title">Data Structures</div></div>
</div><!--header-->
<div class="contents">
<div class="textblock">Here are the data structures with brief descriptions:</div><div class="directory">
<div class="levels">[detail level <span onclick="javascript:toggleLevel(1);">1</span><span onclick="javascript:toggleLevel(2);">2</span>]</div><table class="directory">
<tr id="row_0_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamd__metrics__table__header__t.html" target="_self">amd_metrics_table_header_t</a></td><td class="desc">Structure holds the gpu metrics table header for a device </td></tr>
<tr id="row_1_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__accelerator__partition__profile__config__t.html" target="_self">amdsmi_accelerator_partition_profile_config_t</a></td><td class="desc">Accelerator Partition Profile Configurations </td></tr>
<tr id="row_2_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__accelerator__partition__profile__t.html" target="_self">amdsmi_accelerator_partition_profile_t</a></td><td class="desc">Accelerator Partition Resource Profile </td></tr>
<tr id="row_3_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__accelerator__partition__resource__profile__t.html" target="_self">amdsmi_accelerator_partition_resource_profile_t</a></td><td class="desc">Accelerator Partition Resources. This struct is used to identify various partition resource profiles </td></tr>
<tr id="row_4_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__asic__info__t.html" target="_self">amdsmi_asic_info_t</a></td><td class="desc">ASIC Information </td></tr>
<tr id="row_5_" class="odd"><td class="entry"><span style="width:0px;display:inline-block;">&#160;</span><span id="arr_5_" class="arrow" onclick="toggleFolder('5_')">&#9660;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="unionamdsmi__bdf__t.html" target="_self">amdsmi_bdf_t</a></td><td class="desc">Bdf types </td></tr>
<tr id="row_5_0_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__bdf__t_1_1bdf__.html" target="_self">bdf_</a></td><td class="desc"></td></tr>
<tr id="row_6_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__board__info__t.html" target="_self">amdsmi_board_info_t</a></td><td class="desc">Board Information </td></tr>
<tr id="row_7_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__clk__info__t.html" target="_self">amdsmi_clk_info_t</a></td><td class="desc">Clock Information </td></tr>
<tr id="row_8_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__counter__value__t.html" target="_self">amdsmi_counter_value_t</a></td><td class="desc">Counter value </td></tr>
<tr id="row_9_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__cper__guid__t.html" target="_self">amdsmi_cper_guid_t</a></td><td class="desc">Cper </td></tr>
<tr id="row_10_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__cper__hdr__t.html" target="_self">amdsmi_cper_hdr_t</a></td><td class="desc"></td></tr>
<tr id="row_11_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__cper__timestamp__t.html" target="_self">amdsmi_cper_timestamp_t</a></td><td class="desc"></td></tr>
<tr id="row_12_" class="odd"><td class="entry"><span style="width:0px;display:inline-block;">&#160;</span><span id="arr_12_" class="arrow" onclick="toggleFolder('12_')">&#9660;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="unionamdsmi__cper__valid__bits__t.html" target="_self">amdsmi_cper_valid_bits_t</a></td><td class="desc"></td></tr>
<tr id="row_12_0_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__cper__valid__bits__t_1_1valid__bits__.html" target="_self">valid_bits_</a></td><td class="desc"></td></tr>
<tr id="row_13_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__cpu__info__t.html" target="_self">amdsmi_cpu_info_t</a></td><td class="desc">Cpu info data </td></tr>
<tr id="row_14_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__cpu__util__t.html" target="_self">amdsmi_cpu_util_t</a></td><td class="desc">This structure holds CPU utilization information </td></tr>
<tr id="row_15_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__ddr__bw__metrics__t.html" target="_self">amdsmi_ddr_bw_metrics_t</a></td><td class="desc">DDR bandwidth metrics </td></tr>
<tr id="row_16_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__dimm__power__t.html" target="_self">amdsmi_dimm_power_t</a></td><td class="desc">DIMM Power(mW), power update rate(ms) and dimm address </td></tr>
<tr id="row_17_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__dimm__thermal__t.html" target="_self">amdsmi_dimm_thermal_t</a></td><td class="desc">DIMM temperature(°C) and update rate(ms) and dimm address </td></tr>
<tr id="row_18_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__dpm__level__t.html" target="_self">amdsmi_dpm_level_t</a></td><td class="desc">Max and min LCLK DPM level on a given NBIO ID. Valid max and min DPM level values are 0 - 1 </td></tr>
<tr id="row_19_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__dpm__policy__entry__t.html" target="_self">amdsmi_dpm_policy_entry_t</a></td><td class="desc">The dpm policy </td></tr>
<tr id="row_20_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__dpm__policy__t.html" target="_self">amdsmi_dpm_policy_t</a></td><td class="desc">DPM Policy </td></tr>
<tr id="row_21_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__driver__info__t.html" target="_self">amdsmi_driver_info_t</a></td><td class="desc">Driver Information </td></tr>
<tr id="row_22_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__engine__usage__t.html" target="_self">amdsmi_engine_usage_t</a></td><td class="desc">Engine Usage <a class="el" href="structamdsmi__engine__usage__t.html" title="Engine Usage amdsmi_engine_usage_t: This structure holds common GPU activity values seen in both BM o...">amdsmi_engine_usage_t</a>: This structure holds common GPU activity values seen in both BM or SRIOV </td></tr>
<tr id="row_23_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__enumeration__info__t.html" target="_self">amdsmi_enumeration_info_t</a></td><td class="desc">Structure holds enumeration information </td></tr>
<tr id="row_24_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__error__count__t.html" target="_self">amdsmi_error_count_t</a></td><td class="desc">This structure holds error counts </td></tr>
<tr id="row_25_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__evt__notification__data__t.html" target="_self">amdsmi_evt_notification_data_t</a></td><td class="desc">Event notification data returned from event notification API </td></tr>
<tr id="row_26_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__freq__volt__region__t.html" target="_self">amdsmi_freq_volt_region_t</a></td><td class="desc">This structure holds 2 <a class="el" href="structamdsmi__range__t.html" title="This structure represents a range (e.g., frequencies or voltages).">amdsmi_range_t</a>'s, one for frequency and one for voltage. These 2 ranges indicate the range of possible values for the corresponding <a class="el" href="structamdsmi__od__vddc__point__t.html" title="This structure represents a point on the frequency-voltage plane.">amdsmi_od_vddc_point_t</a> </td></tr>
<tr id="row_27_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__frequencies__t.html" target="_self">amdsmi_frequencies_t</a></td><td class="desc">This structure holds information about clock frequencies </td></tr>
<tr id="row_28_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__frequency__range__t.html" target="_self">amdsmi_frequency_range_t</a></td><td class="desc">Frequency Range </td></tr>
<tr id="row_29_" class="odd"><td class="entry"><span style="width:0px;display:inline-block;">&#160;</span><span id="arr_29_" class="arrow" onclick="toggleFolder('29_')">&#9660;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__fw__info__t.html" target="_self">amdsmi_fw_info_t</a></td><td class="desc">Firmware Information </td></tr>
<tr id="row_29_0_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__fw__info__t_1_1fw__info__list__.html" target="_self">fw_info_list_</a></td><td class="desc"></td></tr>
<tr id="row_30_" class="odd"><td class="entry"><span style="width:0px;display:inline-block;">&#160;</span><span id="arr_30_" class="arrow" onclick="toggleFolder('30_')">&#9660;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__gpu__cache__info__t.html" target="_self">amdsmi_gpu_cache_info_t</a></td><td class="desc">GPU Cache Information </td></tr>
<tr id="row_30_0_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__gpu__cache__info__t_1_1cache__.html" target="_self">cache_</a></td><td class="desc"></td></tr>
<tr id="row_31_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__gpu__metrics__t.html" target="_self">amdsmi_gpu_metrics_t</a></td><td class="desc">Structure holds the gpu metrics values for a device </td></tr>
<tr id="row_32_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__gpu__xcp__metrics__t.html" target="_self">amdsmi_gpu_xcp_metrics_t</a></td><td class="desc">The following structures hold the gpu statistics for a device </td></tr>
<tr id="row_33_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__hsmp__driver__version__t.html" target="_self">amdsmi_hsmp_driver_version_t</a></td><td class="desc">This structure holds HSMP Driver version information </td></tr>
<tr id="row_34_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__hsmp__metrics__table__t.html" target="_self">amdsmi_hsmp_metrics_table_t</a></td><td class="desc">HSMP Metrics table (supported only with hsmp proto version 6) </td></tr>
<tr id="row_35_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__kfd__info__t.html" target="_self">amdsmi_kfd_info_t</a></td><td class="desc">Structure holds kfd information </td></tr>
<tr id="row_36_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__link__id__bw__type__t.html" target="_self">amdsmi_link_id_bw_type_t</a></td><td class="desc">LINK name and Bandwidth type Information.It contains link names i.e valid link names are "P0", "P1", "P2", "P3", "P4", "G0", "G1", "G2", "G3", "G4" "G5", "G6", "G7" Valid bandwidth types 1(Aggregate_BW), 2 (Read BW), 4 (Write BW) </td></tr>
<tr id="row_37_" class="odd"><td class="entry"><span style="width:0px;display:inline-block;">&#160;</span><span id="arr_37_" class="arrow" onclick="toggleFolder('37_')">&#9660;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__link__metrics__t.html" target="_self">amdsmi_link_metrics_t</a></td><td class="desc">Link Metrics </td></tr>
<tr id="row_37_0_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__link__metrics__t_1_1__links.html" target="_self">_links</a></td><td class="desc"></td></tr>
<tr id="row_38_" class="odd"><td class="entry"><span style="width:0px;display:inline-block;">&#160;</span><span id="arr_38_" class="arrow" onclick="toggleFolder('38_')">&#9660;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__memory__partition__config__t.html" target="_self">amdsmi_memory_partition_config_t</a></td><td class="desc">Memory Partition Configuration. This structure is used to identify various memory partition configurations </td></tr>
<tr id="row_38_0_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__memory__partition__config__t_1_1numa__range__.html" target="_self">numa_range_</a></td><td class="desc"></td></tr>
<tr id="row_39_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__name__value__t.html" target="_self">amdsmi_name_value_t</a></td><td class="desc">This structure holds the name value pairs </td></tr>
<tr id="row_40_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__npm__info__t.html" target="_self">amdsmi_npm_info_t</a></td><td class="desc">NPM info </td></tr>
<tr id="row_41_" class="odd"><td class="entry"><span style="width:0px;display:inline-block;">&#160;</span><span id="arr_41_" class="arrow" onclick="toggleFolder('41_')">&#9660;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="unionamdsmi__nps__caps__t.html" target="_self">amdsmi_nps_caps_t</a></td><td class="desc">This union holds memory partition bitmask </td></tr>
<tr id="row_41_0_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__nps__caps__t_1_1nps__flags__.html" target="_self">nps_flags_</a></td><td class="desc"></td></tr>
<tr id="row_42_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__od__vddc__point__t.html" target="_self">amdsmi_od_vddc_point_t</a></td><td class="desc">This structure represents a point on the frequency-voltage plane </td></tr>
<tr id="row_43_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__od__volt__curve__t.html" target="_self">amdsmi_od_volt_curve_t</a></td><td class="desc">OD Vold Curve <a class="el" href="amdsmi_8h.html#af3ca09673d34f498173f0ae5898e3c4b">AMDSMI_NUM_VOLTAGE_CURVE_POINTS</a> number of <a class="el" href="structamdsmi__od__vddc__point__t.html" title="This structure represents a point on the frequency-voltage plane.">amdsmi_od_vddc_point_t</a>'s </td></tr>
<tr id="row_44_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__od__volt__freq__data__t.html" target="_self">amdsmi_od_volt_freq_data_t</a></td><td class="desc">This structure holds the frequency-voltage values for a device </td></tr>
<tr id="row_45_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__p2p__capability__t.html" target="_self">amdsmi_p2p_capability_t</a></td><td class="desc">IO Link P2P Capability </td></tr>
<tr id="row_46_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__pcie__bandwidth__t.html" target="_self">amdsmi_pcie_bandwidth_t</a></td><td class="desc">This structure holds information about the possible PCIe bandwidths. Specifically, the possible transfer rates and their associated numbers of lanes are stored here </td></tr>
<tr id="row_47_" class="even"><td class="entry"><span style="width:0px;display:inline-block;">&#160;</span><span id="arr_47_" class="arrow" onclick="toggleFolder('47_')">&#9660;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__pcie__info__t.html" target="_self">amdsmi_pcie_info_t</a></td><td class="desc">Pcie information </td></tr>
<tr id="row_47_0_" class="odd"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__pcie__info__t_1_1pcie__metric__.html" target="_self">pcie_metric_</a></td><td class="desc"></td></tr>
<tr id="row_47_1_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__pcie__info__t_1_1pcie__static__.html" target="_self">pcie_static_</a></td><td class="desc"></td></tr>
<tr id="row_48_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__power__cap__info__t.html" target="_self">amdsmi_power_cap_info_t</a></td><td class="desc">Power Cap Information </td></tr>
<tr id="row_49_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__power__info__t.html" target="_self">amdsmi_power_info_t</a></td><td class="desc">Power Information </td></tr>
<tr id="row_50_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__power__profile__status__t.html" target="_self">amdsmi_power_profile_status_t</a></td><td class="desc">This structure contains information about which power profiles are supported by the system for a given device, and which power profile is currently active </td></tr>
<tr id="row_51_" class="even"><td class="entry"><span style="width:0px;display:inline-block;">&#160;</span><span id="arr_51_" class="arrow" onclick="toggleFolder('51_')">&#9660;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__proc__info__t.html" target="_self">amdsmi_proc_info_t</a></td><td class="desc">Process Information </td></tr>
<tr id="row_51_0_" class="odd"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__proc__info__t_1_1engine__usage__.html" target="_self">engine_usage_</a></td><td class="desc"></td></tr>
<tr id="row_51_1_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__proc__info__t_1_1memory__usage__.html" target="_self">memory_usage_</a></td><td class="desc"></td></tr>
<tr id="row_52_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__process__info__t.html" target="_self">amdsmi_process_info_t</a></td><td class="desc">This structure contains information specific to a process. Sum of the process memory is not expected to be the total memory usage </td></tr>
<tr id="row_53_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__range__t.html" target="_self">amdsmi_range_t</a></td><td class="desc">This structure represents a range (e.g., frequencies or voltages) </td></tr>
<tr id="row_54_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__ras__feature__t.html" target="_self">amdsmi_ras_feature_t</a></td><td class="desc">This structure holds ras feature </td></tr>
<tr id="row_55_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__retired__page__record__t.html" target="_self">amdsmi_retired_page_record_t</a></td><td class="desc">Reserved Memory Page Record </td></tr>
<tr id="row_56_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__smu__fw__version__t.html" target="_self">amdsmi_smu_fw_version_t</a></td><td class="desc">This structure holds SMU Firmware version information </td></tr>
<tr id="row_57_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__sock__info__t.html" target="_self">amdsmi_sock_info_t</a></td><td class="desc">Cpu socket info data </td></tr>
<tr id="row_58_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__temp__range__refresh__rate__t.html" target="_self">amdsmi_temp_range_refresh_rate_t</a></td><td class="desc">Temperature range and refresh rate metrics of a DIMM </td></tr>
<tr id="row_59_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__topology__nearest__t.html" target="_self">amdsmi_topology_nearest_t</a></td><td class="desc">Topology Nearest </td></tr>
<tr id="row_60_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__utilization__counter__t.html" target="_self">amdsmi_utilization_counter_t</a></td><td class="desc">The utilization counter data </td></tr>
<tr id="row_61_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__vbios__info__t.html" target="_self">amdsmi_vbios_info_t</a></td><td class="desc">VBios Information </td></tr>
<tr id="row_62_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__version__t.html" target="_self">amdsmi_version_t</a></td><td class="desc">This structure holds version information </td></tr>
<tr id="row_63_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__violation__status__t.html" target="_self">amdsmi_violation_status_t</a></td><td class="desc">This structure hold violation status information. Note: for MI3x asics and higher, older ASICs will show unsupported </td></tr>
<tr id="row_64_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__vram__info__t.html" target="_self">amdsmi_vram_info_t</a></td><td class="desc">VRam Information </td></tr>
<tr id="row_65_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__vram__usage__t.html" target="_self">amdsmi_vram_usage_t</a></td><td class="desc">VRam Usage </td></tr>
<tr id="row_66_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__xgmi__info__t.html" target="_self">amdsmi_xgmi_info_t</a></td><td class="desc">XGMI Information </td></tr>
<tr id="row_67_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structamdsmi__xgmi__link__status__t.html" target="_self">amdsmi_xgmi_link_status_t</a></td><td class="desc">XGMI Link Status </td></tr>
</table>
</div><!-- directory -->
</div><!-- contents -->
<!-- HTML footer for doxygen 1.9.6-->
<!-- start footer part -->
</div>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="globals.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Globals</p>
      </div>
    </a>
    <a class="right-next"
       href="functions_data_fields.html"
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
