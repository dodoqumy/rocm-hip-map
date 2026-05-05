---
title: "AMD SMI: Globals &#8212; AMD SMI 26.2.2 documentation"
source_url: "https://rocm.docs.amd.com/projects/amdsmi/en/latest/doxygen/docBin/html/globals.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:13:37.119925+00:00
content_hash: "d4d90d58911af37f"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>AMD SMI: Globals &#8212; AMD SMI 26.2.2 documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/docBin/html/globals';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Data Structures" href="annotated.html" />
    <link rel="prev" title="File List" href="files.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-amdsmi" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/docBin/html/globals.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l2 current active"><a class="current reference internal" href="#">Globals</a></li>
<li class="toctree-l2"><a class="reference internal" href="annotated.html">Data structures</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">AMD SMI: Globals</span></li>
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
    <h1>Globals</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="globals">
<h1>Globals<a class="headerlink" href="#globals" title="Link to this heading">#</a></h1>
<div class="doxygen-content docutils container">
<!-- HTML header for doxygen 1.9.6-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>AMD SMI: Globals</title>
<link href="tabs.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="dynsections.js"></script>
<link href="stylesheet.css" rel="stylesheet" type="text/css" />
<link href="extra_stylesheet.css" rel="stylesheet" type="text/css"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-amdsmi" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/docBin/html/globals.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
<div class="textblock">Here is a list of all documented functions, variables, defines, enums, and typedefs with links to the documentation:</div>

<h3><a id="index_a" name="index_a"></a>- a -</h3><ul>
<li>AGG_BW0&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5018e391c7a552858e2a6836fdf3f828a9850816336eb68decce031d7e6ce6ba1">amdsmi.h</a></li>
<li>AMDSMI_ACCELERATOR_DECODER&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e9998bae93699cef5cb76434a96fcc4a270195edd86a5c9200f1b1e335a1ed5d">amdsmi.h</a></li>
<li>AMDSMI_ACCELERATOR_DMA&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e9998bae93699cef5cb76434a96fcc4a017a1b8aee9701c9fd450142818250de">amdsmi.h</a></li>
<li>AMDSMI_ACCELERATOR_ENCODER&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e9998bae93699cef5cb76434a96fcc4ab129900fcf64a49b3242f04487b4471a">amdsmi.h</a></li>
<li>AMDSMI_ACCELERATOR_JPEG&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e9998bae93699cef5cb76434a96fcc4a2cd5c30c29be0571ff26d8b832718f16">amdsmi.h</a></li>
<li>AMDSMI_ACCELERATOR_PARTITION_CPX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2af14e25dc091311fc8ed3af876c5ee4af27d609148b38209143840d5b75dcef3">amdsmi.h</a></li>
<li>AMDSMI_ACCELERATOR_PARTITION_DPX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2af14e25dc091311fc8ed3af876c5ee4a07d37372a51358cfffe11a71221d7c74">amdsmi.h</a></li>
<li>AMDSMI_ACCELERATOR_PARTITION_INVALID&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2af14e25dc091311fc8ed3af876c5ee4a3dd6074b8d50195088dbd7b028cf97e7">amdsmi.h</a></li>
<li>AMDSMI_ACCELERATOR_PARTITION_QPX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2af14e25dc091311fc8ed3af876c5ee4a2c1d1174d6ac8823befdfd23b2a1f48c">amdsmi.h</a></li>
<li>amdsmi_accelerator_partition_resource_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e9998bae93699cef5cb76434a96fcc4">amdsmi.h</a></li>
<li>AMDSMI_ACCELERATOR_PARTITION_SPX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2af14e25dc091311fc8ed3af876c5ee4a6e538b5fdf7c01c358379e376fe0779e">amdsmi.h</a></li>
<li>AMDSMI_ACCELERATOR_PARTITION_TPX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2af14e25dc091311fc8ed3af876c5ee4acd0ca95dcf79636f4c2d1c3d55a2cb1e">amdsmi.h</a></li>
<li>amdsmi_accelerator_partition_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2af14e25dc091311fc8ed3af876c5ee4">amdsmi.h</a></li>
<li>AMDSMI_ACCELERATOR_XCC&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e9998bae93699cef5cb76434a96fcc4a07bf2725e74985131f4f7aeafe808c5d">amdsmi.h</a></li>
<li>AMDSMI_AFFINITY_SCOPE_NODE&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac3d10c84b1b759ff548643b55cd8b78aa0c46ac61770e9739f749c1bc174f0dc1">amdsmi.h</a></li>
<li>AMDSMI_AFFINITY_SCOPE_SOCKET&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac3d10c84b1b759ff548643b55cd8b78aae614734c56b4ffda589946bfbd0dc127">amdsmi.h</a></li>
<li>amdsmi_affinity_scope_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac3d10c84b1b759ff548643b55cd8b78a">amdsmi.h</a></li>
<li>amdsmi_bit_field_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9aadad72b99ced6d777a810f17130384">amdsmi.h</a></li>
<li>AMDSMI_CACHE_PROPERTY_CPU_CACHE&#160;:&#160;<a class="el" href="amdsmi_8h.html#aa4d8adba67307114dda2de8ac1cbf5a9af9296777aff0a8ccf45a124636caf29b">amdsmi.h</a></li>
<li>AMDSMI_CACHE_PROPERTY_DATA_CACHE&#160;:&#160;<a class="el" href="amdsmi_8h.html#aa4d8adba67307114dda2de8ac1cbf5a9a85c1c71765a9ce7505f3c6d178e10a64">amdsmi.h</a></li>
<li>AMDSMI_CACHE_PROPERTY_ENABLED&#160;:&#160;<a class="el" href="amdsmi_8h.html#aa4d8adba67307114dda2de8ac1cbf5a9a66559819b876a42958f9aba3948e321e">amdsmi.h</a></li>
<li>AMDSMI_CACHE_PROPERTY_INST_CACHE&#160;:&#160;<a class="el" href="amdsmi_8h.html#aa4d8adba67307114dda2de8ac1cbf5a9a713db5c294d9e2cdd057b31361700ed4">amdsmi.h</a></li>
<li>AMDSMI_CACHE_PROPERTY_SIMD_CACHE&#160;:&#160;<a class="el" href="amdsmi_8h.html#aa4d8adba67307114dda2de8ac1cbf5a9acd57e4e47eb033b9f1a0cdbdd8d9bb06">amdsmi.h</a></li>
<li>amdsmi_cache_property_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#aa4d8adba67307114dda2de8ac1cbf5a9">amdsmi.h</a></li>
<li>AMDSMI_CARD_FORM_FACTOR_CEM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a309f999721928dfa9b977ed0a63e3ff7afcf2646459b36607e1dadc9dd1e5703a">amdsmi.h</a></li>
<li>AMDSMI_CARD_FORM_FACTOR_OAM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a309f999721928dfa9b977ed0a63e3ff7ab81e86bf8e4c4e11bfcd8d140da0bdcc">amdsmi.h</a></li>
<li>AMDSMI_CARD_FORM_FACTOR_PCIE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a309f999721928dfa9b977ed0a63e3ff7ae76ab1172d8d29c3ac8b21d8f2987338">amdsmi.h</a></li>
<li>amdsmi_card_form_factor_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a309f999721928dfa9b977ed0a63e3ff7">amdsmi.h</a></li>
<li>AMDSMI_CARD_FORM_FACTOR_UNKNOWN&#160;:&#160;<a class="el" href="amdsmi_8h.html#a309f999721928dfa9b977ed0a63e3ff7ace3aa3cd6a41efee395dfc139d5fd2e4">amdsmi.h</a></li>
<li>amdsmi_clean_gpu_local_data()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfControl.html#ga43281474f038a5d2a5889653e9f7fd93">amdsmi.h</a></li>
<li>amdsmi_clk_limit_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9e41284d1b76884023ae813c361b9517">amdsmi.h</a></li>
<li>AMDSMI_CLK_TYPE_DCEF&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e8c1b5fd3c2b15d8755b33afde5223fa5c8a7789a55205ca664c92cc8db3d5b6">amdsmi.h</a></li>
<li>AMDSMI_CLK_TYPE_DCLK0&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e8c1b5fd3c2b15d8755b33afde5223fa52d5e1db9c243b7c915275f16156cfb5">amdsmi.h</a></li>
<li>AMDSMI_CLK_TYPE_DCLK1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e8c1b5fd3c2b15d8755b33afde5223fa035bf811572f7b66519fdb2acbe580ad">amdsmi.h</a></li>
<li>AMDSMI_CLK_TYPE_DF&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e8c1b5fd3c2b15d8755b33afde5223fa71b1eec155fbd246b3a9ea55edc07dad">amdsmi.h</a></li>
<li>AMDSMI_CLK_TYPE_GFX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e8c1b5fd3c2b15d8755b33afde5223fa4b68ebcaaa072461b3c258eee284339f">amdsmi.h</a></li>
<li>AMDSMI_CLK_TYPE_MEM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e8c1b5fd3c2b15d8755b33afde5223fa219904fde650ee3b2f8d3e25a1122592">amdsmi.h</a></li>
<li>AMDSMI_CLK_TYPE_PCIE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e8c1b5fd3c2b15d8755b33afde5223fac682dc1aa5d4e89bff3915552d7f9a5c">amdsmi.h</a></li>
<li>AMDSMI_CLK_TYPE_SOC&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e8c1b5fd3c2b15d8755b33afde5223fa46a46b0e4ded8f265958094b37ea1471">amdsmi.h</a></li>
<li>AMDSMI_CLK_TYPE_SYS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e8c1b5fd3c2b15d8755b33afde5223fa3be09425e6365d216d7b40ab3408999a">amdsmi.h</a></li>
<li>amdsmi_clk_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e8c1b5fd3c2b15d8755b33afde5223f">amdsmi.h</a></li>
<li>AMDSMI_CLK_TYPE_VCLK0&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e8c1b5fd3c2b15d8755b33afde5223fab4e51e9414778657b49a23c4ff9deb47">amdsmi.h</a></li>
<li>AMDSMI_CLK_TYPE_VCLK1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2e8c1b5fd3c2b15d8755b33afde5223fa6b3efe32e6d9e1b7f64748a49d6cda99">amdsmi.h</a></li>
<li>AMDSMI_CNTR_CMD_START&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae0957d87bf3ed2d21728a7e9fb95afacaac534535f3205689aedc9a5f5613b874">amdsmi.h</a></li>
<li>AMDSMI_CNTR_CMD_STOP&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae0957d87bf3ed2d21728a7e9fb95afaca4137c3d8a69277df550bea5c1dd79e8b">amdsmi.h</a></li>
<li>AMDSMI_COARSE_DECODER_ACTIVITY&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9453dac970283a7815c067f996064141ae8e4372a448463c05909260049592abc">amdsmi.h</a></li>
<li>AMDSMI_COARSE_GRAIN_GFX_ACTIVITY&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9453dac970283a7815c067f996064141a5000831dabb9eb8152f5af2838c32d38">amdsmi.h</a></li>
<li>AMDSMI_COARSE_GRAIN_MEM_ACTIVITY&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9453dac970283a7815c067f996064141a4a131c64c40baa94df85262e9bebd5e6">amdsmi.h</a></li>
<li>AMDSMI_COMPUTE_PARTITION_CPX&#160;:&#160;<a class="el" href="amdsmi_8h.html#af5c57809078d4345b08b59b4162cd6baa87da203969a838921eb97c703d38c71c">amdsmi.h</a></li>
<li>AMDSMI_COMPUTE_PARTITION_DPX&#160;:&#160;<a class="el" href="amdsmi_8h.html#af5c57809078d4345b08b59b4162cd6baa9cbc8aad1e0fd7d8993ca445fce50f56">amdsmi.h</a></li>
<li>AMDSMI_COMPUTE_PARTITION_INVALID&#160;:&#160;<a class="el" href="amdsmi_8h.html#af5c57809078d4345b08b59b4162cd6baad5b0ebde8bb73e1fedbaa7ef18105cb2">amdsmi.h</a></li>
<li>AMDSMI_COMPUTE_PARTITION_QPX&#160;:&#160;<a class="el" href="amdsmi_8h.html#af5c57809078d4345b08b59b4162cd6baa3fdda94749d4a62c2b450cfc6143467e">amdsmi.h</a></li>
<li>AMDSMI_COMPUTE_PARTITION_SPX&#160;:&#160;<a class="el" href="amdsmi_8h.html#af5c57809078d4345b08b59b4162cd6baa8f77cdea6f848f95c3945cdeb4b116c3">amdsmi.h</a></li>
<li>AMDSMI_COMPUTE_PARTITION_TPX&#160;:&#160;<a class="el" href="amdsmi_8h.html#af5c57809078d4345b08b59b4162cd6baa76de711925487a0f4d3ee12023b9a607">amdsmi.h</a></li>
<li>amdsmi_compute_partition_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#af5c57809078d4345b08b59b4162cd6ba">amdsmi.h</a></li>
<li>AMDSMI_CONTAINER_DOCKER&#160;:&#160;<a class="el" href="amdsmi_8h.html#a203f0587147f10da2051058e98fc36f3a87a51443743217e7fefcfc8e13af7372">amdsmi.h</a></li>
<li>AMDSMI_CONTAINER_LXC&#160;:&#160;<a class="el" href="amdsmi_8h.html#a203f0587147f10da2051058e98fc36f3aed6537212977e624a09ae974e0aa0075">amdsmi.h</a></li>
<li>amdsmi_container_types_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a203f0587147f10da2051058e98fc36f3">amdsmi.h</a></li>
<li>amdsmi_counter_command_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae0957d87bf3ed2d21728a7e9fb95afac">amdsmi.h</a></li>
<li>AMDSMI_CPER_NOTIFY_TYPE_BOOT&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479a9284a3c4bfb5d8de9fdc4338bed8d79c">amdsmi.h</a></li>
<li>AMDSMI_CPER_NOTIFY_TYPE_CMC&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479a2e75658a6927d49660400f5ab5697e98">amdsmi.h</a></li>
<li>AMDSMI_CPER_NOTIFY_TYPE_CPE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479a47d7bc0971a392793a6b831e4cb300f7">amdsmi.h</a></li>
<li>AMDSMI_CPER_NOTIFY_TYPE_CXL_COMPONENT&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479a566730d3b48caac3624eb9b64a6843bc">amdsmi.h</a></li>
<li>AMDSMI_CPER_NOTIFY_TYPE_DMAR&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479a0f0eee6e2678fb64c2b5dd6d51d50864">amdsmi.h</a></li>
<li>AMDSMI_CPER_NOTIFY_TYPE_INIT&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479af002d591007554853dc72a74db7f86dd">amdsmi.h</a></li>
<li>AMDSMI_CPER_NOTIFY_TYPE_MCE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479a85c2f399c3a3d011522b8b3470608170">amdsmi.h</a></li>
<li>AMDSMI_CPER_NOTIFY_TYPE_NMI&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479a11e67f63c386e45c1c38daa71308a32b">amdsmi.h</a></li>
<li>AMDSMI_CPER_NOTIFY_TYPE_PCIE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479aad06543acca760767de788ffa199d856">amdsmi.h</a></li>
<li>AMDSMI_CPER_NOTIFY_TYPE_PEI&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479a743dc926aeca9c31e7441f1609ff930e">amdsmi.h</a></li>
<li>AMDSMI_CPER_NOTIFY_TYPE_SEA&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479a67df9007fa992927c1d62836395fc2e8">amdsmi.h</a></li>
<li>AMDSMI_CPER_NOTIFY_TYPE_SEI&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479a15280438daa0f05accc00439ffc5beb6">amdsmi.h</a></li>
<li>amdsmi_cper_notify_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a593f7a7e14a1738a313c8b19cd67c479">amdsmi.h</a></li>
<li>AMDSMI_CPER_SEV_FATAL&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfaba95d1994dc17c45bd8314af45770ad4e8ce7b39c63c71caadd5cabbb82c32">amdsmi.h</a></li>
<li>AMDSMI_CPER_SEV_NON_FATAL_CORRECTED&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfaba95d1994dc17c45bd8314af45770a3d3f2bdfb2ed79ca2fedc04f8de5a47e">amdsmi.h</a></li>
<li>AMDSMI_CPER_SEV_NON_FATAL_UNCORRECTED&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfaba95d1994dc17c45bd8314af45770aa62557edadf1cb8148156d4a37e936c3">amdsmi.h</a></li>
<li>AMDSMI_CPER_SEV_NUM&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfaba95d1994dc17c45bd8314af45770a1d9a6bd3aa7037511e5462c273d9ee26">amdsmi.h</a></li>
<li>amdsmi_cper_sev_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfaba95d1994dc17c45bd8314af45770">amdsmi.h</a></li>
<li>AMDSMI_CPER_SEV_UNUSED&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfaba95d1994dc17c45bd8314af45770ae4f3a772f1b10e52123d032d6b9f7db2">amdsmi.h</a></li>
<li>amdsmi_cpu_apb_disable()&#160;:&#160;<a class="el" href="group__tagPstateSelect.html#ga072526944c6a44407213ee63d01146cd">amdsmi.h</a></li>
<li>amdsmi_cpu_apb_enable()&#160;:&#160;<a class="el" href="group__tagPstateSelect.html#gab0ececb2d3c5b4a63255036e9cc03bc4">amdsmi.h</a></li>
<li>amdsmi_cpusocket_handle&#160;:&#160;<a class="el" href="amdsmi_8h.html#abedf44b4e192089e2fb19fcaa31e4d94">amdsmi.h</a></li>
<li>AMDSMI_DATE_FORMAT&#160;:&#160;<a class="el" href="amdsmi_8h.html#a7880cf76705371faa47364f4e0048b71">amdsmi.h</a></li>
<li>AMDSMI_DEV_PERF_LEVEL_AUTO&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6fdb7867a4bb489ad391a898ff412d5da912bb0a58fc08319e6359240f8342a19">amdsmi.h</a></li>
<li>AMDSMI_DEV_PERF_LEVEL_DETERMINISM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6fdb7867a4bb489ad391a898ff412d5dae8be30724a0c17ad0db28eb9f55c0523">amdsmi.h</a></li>
<li>AMDSMI_DEV_PERF_LEVEL_HIGH&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6fdb7867a4bb489ad391a898ff412d5daf24d0a0211c8e86649e9a31bdcc626c2">amdsmi.h</a></li>
<li>AMDSMI_DEV_PERF_LEVEL_LOW&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6fdb7867a4bb489ad391a898ff412d5daec482a5887bf4ebd431450274a28fa1a">amdsmi.h</a></li>
<li>AMDSMI_DEV_PERF_LEVEL_MANUAL&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6fdb7867a4bb489ad391a898ff412d5daf41661be7ee85c71e11d548a47b60b8d">amdsmi.h</a></li>
<li>AMDSMI_DEV_PERF_LEVEL_STABLE_MIN_MCLK&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6fdb7867a4bb489ad391a898ff412d5dad0623ebb9e469b30b4a202910ee6e809">amdsmi.h</a></li>
<li>AMDSMI_DEV_PERF_LEVEL_STABLE_MIN_SCLK&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6fdb7867a4bb489ad391a898ff412d5da9489ef582ac14e48d5d0072f70fa478c">amdsmi.h</a></li>
<li>AMDSMI_DEV_PERF_LEVEL_STABLE_PEAK&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6fdb7867a4bb489ad391a898ff412d5da81535f86dd08139fcd13f5b5558b9961">amdsmi.h</a></li>
<li>AMDSMI_DEV_PERF_LEVEL_STABLE_STD&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6fdb7867a4bb489ad391a898ff412d5da19201f6d089aaae7547960ec26ebf795">amdsmi.h</a></li>
<li>amdsmi_dev_perf_level_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6fdb7867a4bb489ad391a898ff412d5d">amdsmi.h</a></li>
<li>AMDSMI_DEV_PERF_LEVEL_UNKNOWN&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6fdb7867a4bb489ad391a898ff412d5daf7ad6c52449f042bdb55c4d19bdfe5f8">amdsmi.h</a></li>
<li>amdsmi_event_group_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a46c692f59758cb9f54a1ecf32a995f20">amdsmi.h</a></li>
<li>amdsmi_event_handle_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a281b97f71fe1d844800eb0f9f0899800">amdsmi.h</a></li>
<li>AMDSMI_EVENT_MASK_FROM_INDEX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a8caa16314b92f26b6f7fd5d14ed1a45c">amdsmi.h</a></li>
<li>amdsmi_event_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972c">amdsmi.h</a></li>
<li>AMDSMI_EVNT_GRP_INVALID&#160;:&#160;<a class="el" href="amdsmi_8h.html#a46c692f59758cb9f54a1ecf32a995f20ad66451993382e99d96c5b3489938ef73">amdsmi.h</a></li>
<li>AMDSMI_EVNT_GRP_XGMI&#160;:&#160;<a class="el" href="amdsmi_8h.html#a46c692f59758cb9f54a1ecf32a995f20a4ad21b77cf8ddc4dde4db04976a45320">amdsmi.h</a></li>
<li>AMDSMI_EVNT_GRP_XGMI_DATA_OUT&#160;:&#160;<a class="el" href="amdsmi_8h.html#a46c692f59758cb9f54a1ecf32a995f20a86f17c649850585e08618999486ea5ea">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_0_BEATS_TX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972ca13f838643ce667372307c74f9d8d40f5">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_0_NOP_TX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972ca545201b01e7aaf9748fd72d4531e2123">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_0_REQUEST_TX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972cadcb70f8dc057cfe09d2551723fd6d977">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_0_RESPONSE_TX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972ca807cb67a95b0afa1fa047db4d13ae94b">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_1_BEATS_TX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972ca98efabee11d0ae9854ba032034c06028">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_1_NOP_TX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972ca72d3601039fa62d79f106f7d2671ff5d">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_1_REQUEST_TX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972cab28cc1d80a669d73219a0f550e4e9b7e">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_1_RESPONSE_TX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972caf224bf2ad6dc152e565c6cc2b4c9c798">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_DATA_OUT_0&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972cacce359dba327323aed611366753b2cdb">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_DATA_OUT_1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972caa4782a47d8c949195149badfd2e8d23d">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_DATA_OUT_2&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972caaacb9986b453554da13b0a2990619cdf">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_DATA_OUT_3&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972ca54032f9e9be9d2059f5f9fd1a6014dec">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_DATA_OUT_4&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972ca9b3fd3ac4c1383d97c5d57a45db97359">amdsmi.h</a></li>
<li>AMDSMI_EVNT_XGMI_DATA_OUT_5&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5bd63d39a692bb31e9b0d63faebe972cac1c0c987e3b700d811b8f26718459f7e">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_GPU_POST_RESET&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61a0eb505f8c9516bee94301163f2973cd2">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_GPU_PRE_RESET&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61ac7f9bfd374d387b314d70cdadce37d17">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_MIGRATE_END&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61ab00f60ed4571c0e66d495c27eaf2f5ba">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_MIGRATE_START&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61a91d32292f62846d2cc7d470b843aa442">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_NONE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61a69a8d61db0f824aa178af695a8bce59f">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_PAGE_FAULT_END&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61ad8c0dcc8a943dbde3a964eba53593787">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_PAGE_FAULT_START&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61ac3c808604789446ed590e4b0cb52249f">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_PROCESS_END&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61af0d5d5d5a746307b5f5cb47909d8c719">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_PROCESS_START&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61a23efda52ce0a5212d0b645ad34efe3cb">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_QUEUE_EVICTION&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61abaf21bdff31117687b0b3785387c2c4d">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_QUEUE_RESTORE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61ace8b80485df32e61b202734795480e89">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_THERMAL_THROTTLE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61ad36c7178f488fa04c651d396d7b0c462">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_UNMAP_FROM_GPU&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61a698bf9db67cff208dcb54d233324c6d7">amdsmi.h</a></li>
<li>AMDSMI_EVT_NOTIF_VMFAULT&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61a7ffb33873478b6f2e579afa66e58f6c1">amdsmi.h</a></li>
<li>amdsmi_evt_notification_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1cf08148e6cc52a1dae42a4b1c30fe61">amdsmi.h</a></li>
<li>AMDSMI_FINE_DECODER_ACTIVITY&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9453dac970283a7815c067f996064141aab471eb2dc65b5f41d12840ec296841c">amdsmi.h</a></li>
<li>AMDSMI_FINE_GRAIN_GFX_ACTIVITY&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9453dac970283a7815c067f996064141a57a402727f6e1a29d9df0c1b35e13231">amdsmi.h</a></li>
<li>AMDSMI_FINE_GRAIN_MEM_ACTIVITY&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9453dac970283a7815c067f996064141a2b78d730b0921f7e91cf79662db6f476">amdsmi.h</a></li>
<li>amdsmi_first_online_core_on_cpu_socket()&#160;:&#160;<a class="el" href="group__tagCPUAuxillary.html#ga44a67ab3f2ba4c0c3f96814ab50efdd1">amdsmi.h</a></li>
<li>AMDSMI_FREQ_IND_INVALID&#160;:&#160;<a class="el" href="amdsmi_8h.html#a22dd52c02a89114a71e9022e591f9dbaa4d43cad0f6d37b11bf378b4dedf31420">amdsmi.h</a></li>
<li>AMDSMI_FREQ_IND_MAX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a22dd52c02a89114a71e9022e591f9dbaa63390c0bb85fc3ac946e9c1ffaa14271">amdsmi.h</a></li>
<li>AMDSMI_FREQ_IND_MIN&#160;:&#160;<a class="el" href="amdsmi_8h.html#a22dd52c02a89114a71e9022e591f9dbaa6381fcdde3a7c35650b37b4bf8a44442">amdsmi.h</a></li>
<li>amdsmi_freq_ind_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a22dd52c02a89114a71e9022e591f9dba">amdsmi.h</a></li>
<li>amdsmi_fw_block_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eb">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_ASD&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba01147f8fa9167b2bbbb1627660d7a156">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_CP_CE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba3235bdb1e929223ac770b925d72c774c">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_CP_ME&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba7f9ee68679bdd1db530916c8fbb58e01">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_CP_MEC1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaaeba6f197c8b574bdba04ce172da12ac">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_CP_MEC2&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebafa428360517f28ca0a601367cd88a6e0">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_CP_MEC_JT1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba82a5eee73010f9540af531d4970a1e15">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_CP_MEC_JT2&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebacd9709927bb6325c3cfa239e0d9daca2">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_CP_MES&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaf07c80b53ece789c9ed2ff1b35a5c2c0">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_CP_PFP&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebad4afcdca837ca72c98c363387739c749">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_CP_PM4&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba4dd74f0377c65825c1d670ef3e8c70b0">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_DFC&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaf6073731f49fd8b54219ffbf53fac306">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_DMCU&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba9b23ce106e46f63afe00e84bdccc1fb5">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_DMCU_ERAM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaf0fa7f4bc5a06a0c60493ffdae4f0c2f">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_DMCU_ISR&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba2b7bae8c87edb6888f7ce0726a197a32">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_DRV_CAP&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba36d5b758133dbf5d36a5d2d3f73efd0d">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_IMU_DRAM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaae08ddd26f706fe5f62d1cfce397470a">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_IMU_IRAM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba663eeaa4f47003d613484baedebf3866">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_ISP&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba47ef858534ec1b393e27e792b7e4c474">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_MC&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba568f16c065c3d5cef5d93886de00398d">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_MES_KIQ&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba91ae5637ce429f59c1a203d8143a97f7">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_MES_STACK&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba5dc133b520103e0cbab3c474536d0fff">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_MES_THREAD1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba40139706a4f455243a6c41ef7d97ed5e">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_MES_THREAD1_STACK&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebad92262321e1787f2fa2a31cdde375010">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_MMSCH&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba184b525962d8224785c29defba87605b">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_PLDM_BUNDLE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba6db258d161e3a65e54b1fea2161fa4f2">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_PM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba4036d0c97eb368ab3ccaeeb97b7cbafb">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_PPTABLE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebadd3a753d00f60169ec72c110e9566565">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_PSP_BL&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba0974e4fafdb45c3335b92356d23ba73d">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_PSP_DBG&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba2eab8ef2cfcf513f8254dda6f2e0ac9e">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_PSP_INTF&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebacae75136ff00f03fe49deb2997fff48a">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_PSP_KEYDB&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba2062f2528f135a8b3a6707e2aa42190e">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_PSP_SOC&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba4889741bbacb5b94900489f6b964b9be">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_PSP_SOSDRV&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba1f4f4078c37a5c77c30024dcd94d25a8">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_PSP_SPL&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebae091aa45f96ee2d39caba146642efe03">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_PSP_SYSDRV&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebae1c2ab990e4d897b69eadd5b7175d93a">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_PSP_TOC&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba63d46f2182dbb4cc653bcbc97162f7e7">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_REG_ACCESS_WHITELIST&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebae111f62da71cec5d8e2840da2893f82a">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLC&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba0f7857b41ff5ee61e0c1cc4925680a44">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLC_P&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba5289912f93b4d209fd0403a833fea467">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLC_RESTORE_LIST_CNTL&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebab55b8058df3a2070662bd24446a87b20">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLC_RESTORE_LIST_GPM_MEM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebac72767808783c304e1335ca0bbb61544">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLC_RESTORE_LIST_SRM_MEM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba03b22e109d846e9780bc61328929fedb">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLC_SAVE_RESTORE_LIST&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebad472e335aa6ed6fa8554ce45735a0705">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLC_SRLG&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaa786a170387b3b9bd4f836f23d7a1b5b">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLC_SRLS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba252b287a0b27591faccdae2e95b9795f">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLC_V&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba8bddb7301d7535ef21ad43ccd6179a3d">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLCV_LX7&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaf502ef17b716466f983d7855ae458103">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLX6&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba1d53f70ec97ecd95e8ee3a365f667906">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLX6_CORE1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebac08a8613b22212716efd95054f2dd121">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLX6_DRAM_BOOT&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaad74be2b50e921b3764eda64981489a6">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RLX6_DRAM_BOOT_CORE1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba5be408e9457f4b19f25b7aeb3c913028">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RS64_ME&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba73927a213d63abffb5c42e396e749365">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RS64_ME_P0_DATA&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba027133839453b41c88c035ff3e3ae41b">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RS64_ME_P1_DATA&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba388410211a82005226ea4d1e4063ac6c">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RS64_MEC&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaf5d8ade5774e599ef6c201bdb01a6e6c">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RS64_MEC_P0_DATA&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebab737891cd288acd0e3651f91abee2eac">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RS64_MEC_P1_DATA&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebac5054a43e1dc69205303c4762b81c74e">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RS64_MEC_P2_DATA&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba6ab96d79e88aaa902d91795d7632559d">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RS64_MEC_P3_DATA&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba805b72d6c2f34bd7db51d7293e25a623">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RS64_PFP&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba10fb06d8ec612016ba6cea82baff387c">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RS64_PFP_P0_DATA&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaeaf64ef8560065ba60b301f40d09cb26">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_RS64_PFP_P1_DATA&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaacc85bdb01ba55584eaab7e26b58ee54">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_SDMA0&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba410b6c3439ddda7becce7970bc674039">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_SDMA1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba7c62d7901cab386ff1ec32df0cf1591a">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_SDMA2&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaee04f6e66f9ee5b7c28366ac406ad56d">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_SDMA3&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba76e2f8e5196481797d2135fdd2ff55d8">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_SDMA4&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba8d5a870cd10ded2f4c330d797adbce07">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_SDMA5&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebaebea1edbdfae8726cdf6992b772a6b4f">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_SDMA6&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba2bdf6b7171fdf2197903e99251f88a26">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_SDMA7&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba06392b7cd75ad232b14d0c5a57b31181">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_SDMA_TH0&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba53619602e80edda9332d16b4bc9fd5cd">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_SDMA_TH1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba16b880177337a9c7ace806619c75ca24">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_SEC_POLICY_STAGE2&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba6a68ecec023552e833cb82d85ee08949">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_SMU&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0ebada503ddb3eefe8a95e7978727d7e3af1">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_TA_RAS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba1f6e6e299a23a54ec860a8c6bad23970">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_TA_XGMI&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba6e3e5de6b7a4e9393e1e5ce82927898c">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_UVD&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba87dc89d0fef15e3ad32fb8baaf30b87d">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_VCE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba2aa1b3497945ea8e1cf309ade2cc5a65">amdsmi.h</a></li>
<li>AMDSMI_FW_ID_VCN&#160;:&#160;<a class="el" href="amdsmi_8h.html#a62970568dc405d9f86a86dab5cadc0eba56e780fd58364e19c884ee3b16889824">amdsmi.h</a></li>
<li>amdsmi_get_afids_from_cper()&#160;:&#160;<a class="el" href="group__tagRasInfo.html#gaa6cd69223f79fed1aadfedee4ecf953d">amdsmi.h</a></li>
<li>amdsmi_get_clk_freq()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#gaa26eb97ee5ddfd2100d02eb8dc70b391">amdsmi.h</a></li>
<li>amdsmi_get_clock_info()&#160;:&#160;<a class="el" href="group__tagGPUMonitor.html#ga7353130cacc7e3643dcadc7ce0125590">amdsmi.h</a></li>
<li>amdsmi_get_cpu_affinity_with_scope()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#gaeffd4cea95ecf3226cebb5c340b69151">amdsmi.h</a></li>
<li>amdsmi_get_cpu_cclk_limit()&#160;:&#160;<a class="el" href="group__tagHSMPSystemStats.html#gaba184f00543778999edee6efbbbbf6a8">amdsmi.h</a></li>
<li>amdsmi_get_cpu_core_boostlimit()&#160;:&#160;<a class="el" href="group__tagPerfBoostControl.html#gacdeeabc9ed40252e26793afeef95ed6f">amdsmi.h</a></li>
<li>amdsmi_get_cpu_core_current_freq_limit()&#160;:&#160;<a class="el" href="group__tagHSMPSystemStats.html#ga95855065e14dc70b46a3525ffae7f127">amdsmi.h</a></li>
<li>amdsmi_get_cpu_core_energy()&#160;:&#160;<a class="el" href="group__tagEnergyInfo.html#ga4a4988e2164b4bbdd32252467d090d56">amdsmi.h</a></li>
<li>amdsmi_get_cpu_cores_per_socket()&#160;:&#160;<a class="el" href="group__tagCPUAuxillary.html#gadfcd8290ee518b926f0964fa56eb9c78">amdsmi.h</a></li>
<li>amdsmi_get_cpu_current_io_bandwidth()&#160;:&#160;<a class="el" href="group__tagBandwidthMon.html#ga96806ebf57a730e0becc318d5a86db2c">amdsmi.h</a></li>
<li>amdsmi_get_cpu_current_xgmi_bw()&#160;:&#160;<a class="el" href="group__tagBandwidthMon.html#gaf4880b7c6296162f5f35d0a3e971e3a7">amdsmi.h</a></li>
<li>amdsmi_get_cpu_ddr_bw()&#160;:&#160;<a class="el" href="group__tagDDRBandwidthMonitor.html#ga2cf61b9ab41646e675930347edec4877">amdsmi.h</a></li>
<li>amdsmi_get_cpu_dimm_power_consumption()&#160;:&#160;<a class="el" href="group__tagDimmStatistics.html#ga164368b2f036e1bef8831bf77accefd5">amdsmi.h</a></li>
<li>amdsmi_get_cpu_dimm_temp_range_and_refresh_rate()&#160;:&#160;<a class="el" href="group__tagDimmStatistics.html#ga16b75382b652c386d6105174e0112642">amdsmi.h</a></li>
<li>amdsmi_get_cpu_dimm_thermal_sensor()&#160;:&#160;<a class="el" href="group__tagDimmStatistics.html#ga49b34e44479949c37d62e772008edaed">amdsmi.h</a></li>
<li>amdsmi_get_cpu_family()&#160;:&#160;<a class="el" href="group__tagCPUAuxillary.html#ga067aa60cc74cf61e5539dc484ac3aead">amdsmi.h</a></li>
<li>amdsmi_get_cpu_fclk_mclk()&#160;:&#160;<a class="el" href="group__tagHSMPSystemStats.html#ga081c3dc9524f6d6a4b35d0cd6e713eeb">amdsmi.h</a></li>
<li>amdsmi_get_cpu_handles()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#ga5e279471be1b91179e5c60068e97ace6">amdsmi.h</a></li>
<li>amdsmi_get_cpu_hsmp_driver_version()&#160;:&#160;<a class="el" href="group__tagHSMPSystemStats.html#ga56087f977466e7c059a11c34209113d0">amdsmi.h</a></li>
<li>amdsmi_get_cpu_hsmp_proto_ver()&#160;:&#160;<a class="el" href="group__tagHSMPSystemStats.html#ga6d30d5516893a28ed9e9c0ada5060bc6">amdsmi.h</a></li>
<li>amdsmi_get_cpu_model()&#160;:&#160;<a class="el" href="group__tagCPUAuxillary.html#gaab80e6742c3faa3b372342d0cc4c5c2b">amdsmi.h</a></li>
<li>amdsmi_get_cpu_model_name()&#160;:&#160;<a class="el" href="group__tagCPUAuxillary.html#ga2d6f1e7d834079a78754e9584e47ae43">amdsmi.h</a></li>
<li>amdsmi_get_cpu_prochot_status()&#160;:&#160;<a class="el" href="group__tagHSMPSystemStats.html#ga51c8deb4d54d0e7f93938096c8309d84">amdsmi.h</a></li>
<li>amdsmi_get_cpu_pwr_svi_telemetry_all_rails()&#160;:&#160;<a class="el" href="group__tagPowerControl.html#gab6fb7068791447c63c784b15cfe65189">amdsmi.h</a></li>
<li>amdsmi_get_cpu_smu_fw_version()&#160;:&#160;<a class="el" href="group__tagHSMPSystemStats.html#ga815e60aba2cc2d17cb4c23ca6a0ea561">amdsmi.h</a></li>
<li>amdsmi_get_cpu_socket_c0_residency()&#160;:&#160;<a class="el" href="group__tagPerfBoostControl.html#ga417c67d6180780148cf06737e1671ad9">amdsmi.h</a></li>
<li>amdsmi_get_cpu_socket_count()&#160;:&#160;<a class="el" href="group__tagCPUAuxillary.html#ga7e2f2dd5d8b92173c7ad1d426127c2a8">amdsmi.h</a></li>
<li>amdsmi_get_cpu_socket_current_active_freq_limit()&#160;:&#160;<a class="el" href="group__tagHSMPSystemStats.html#ga9166384370ae7cb3026ae3eba58ddda5">amdsmi.h</a></li>
<li>amdsmi_get_cpu_socket_energy()&#160;:&#160;<a class="el" href="group__tagEnergyInfo.html#ga10285cd03b81236b689102ac1f3da136">amdsmi.h</a></li>
<li>amdsmi_get_cpu_socket_freq_range()&#160;:&#160;<a class="el" href="group__tagHSMPSystemStats.html#gab2eb1e6d30be17cced75f780b768b614">amdsmi.h</a></li>
<li>amdsmi_get_cpu_socket_lclk_dpm_level()&#160;:&#160;<a class="el" href="group__tagPstateSelect.html#ga87603e88e57da61ab3ff5cc2967a4a4a">amdsmi.h</a></li>
<li>amdsmi_get_cpu_socket_power()&#160;:&#160;<a class="el" href="group__tagPowerControl.html#gaa9788d2cc26b5c97561250db2d25ecbc">amdsmi.h</a></li>
<li>amdsmi_get_cpu_socket_power_cap()&#160;:&#160;<a class="el" href="group__tagPowerControl.html#gab413b04094e57cc8b355b09fd1366cc5">amdsmi.h</a></li>
<li>amdsmi_get_cpu_socket_power_cap_max()&#160;:&#160;<a class="el" href="group__tagPowerControl.html#ga2550e328f729fe37e989e8d0beead31a">amdsmi.h</a></li>
<li>amdsmi_get_cpu_socket_temperature()&#160;:&#160;<a class="el" href="group__tagTempQuery.html#gaeb9e5af78c8f1a4a288b16bb211df4c0">amdsmi.h</a></li>
<li>amdsmi_get_cpucore_handles()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#ga8108de71f44606c25d3d288ac0b3d422">amdsmi.h</a></li>
<li>amdsmi_get_energy_count()&#160;:&#160;<a class="el" href="group__tagPowerQuery.html#ga079dce724260f293667c2726f10facb5">amdsmi.h</a></li>
<li>amdsmi_get_esmi_err_msg()&#160;:&#160;<a class="el" href="group__tagCPUAuxillary.html#gafeba4788743dd3604ab33d4de93088e8">amdsmi.h</a></li>
<li>amdsmi_get_fw_info()&#160;:&#160;<a class="el" href="group__tagFWVbiosQuery.html#ga47f22c0325763133d54e4e4bcde20806">amdsmi.h</a></li>
<li>amdsmi_get_gpu_accelerator_partition_profile()&#160;:&#160;<a class="el" href="group__tagAcceleratorPartition.html#ga84243905e6cf77b541219f1b0cecd395">amdsmi.h</a></li>
<li>amdsmi_get_gpu_accelerator_partition_profile_config()&#160;:&#160;<a class="el" href="group__tagAcceleratorPartition.html#ga48b804260e3c616b33207476db26657a">amdsmi.h</a></li>
<li>amdsmi_get_gpu_activity()&#160;:&#160;<a class="el" href="group__tagGPUMonitor.html#ga607c889de3d46bc2e830d93c1bd6a8a5">amdsmi.h</a></li>
<li>amdsmi_get_gpu_asic_info()&#160;:&#160;<a class="el" href="group__tagAsicBoardInfo.html#gac69063027bcadc936babfe0c77d23290">amdsmi.h</a></li>
<li>amdsmi_get_gpu_available_counters()&#160;:&#160;<a class="el" href="group__tagPerfCounter.html#ga0e28dc909ea6c1f457ca75be36b4ffff">amdsmi.h</a></li>
<li>amdsmi_get_gpu_bad_page_info()&#160;:&#160;<a class="el" href="group__tagMemoryQuery.html#ga39f1dc66d322a3a4dcedbb9faed0ac2f">amdsmi.h</a></li>
<li>amdsmi_get_gpu_bad_page_threshold()&#160;:&#160;<a class="el" href="group__tagMemoryQuery.html#ga03d9acb20a0a738ba64586e4f7752448">amdsmi.h</a></li>
<li>amdsmi_get_gpu_bdf_id()&#160;:&#160;<a class="el" href="group__tagPCIeQuery.html#gafc9fa9bc0bf20186ecc62cf99ea02067">amdsmi.h</a></li>
<li>amdsmi_get_gpu_board_info()&#160;:&#160;<a class="el" href="group__tagAsicBoardInfo.html#ga88ec48fdabd10464404d7ae1f1af822b">amdsmi.h</a></li>
<li>amdsmi_get_gpu_busy_percent()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#ga4882f16f9c28e88ea64611ff3c76f2fe">amdsmi.h</a></li>
<li>amdsmi_get_gpu_cache_info()&#160;:&#160;<a class="el" href="group__tagPhysicalStateQuery.html#gad214bfeee423b58722d5a09ed4f2a6d8">amdsmi.h</a></li>
<li>amdsmi_get_gpu_compute_partition()&#160;:&#160;<a class="el" href="group__tagComputePartition.html#ga80d787dc0eafe700b82955607fd038d6">amdsmi.h</a></li>
<li>amdsmi_get_gpu_compute_process_gpus()&#160;:&#160;<a class="el" href="group__tagSystemInfo.html#gaf1dfa58ed77699fbd23283e517823489">amdsmi.h</a></li>
<li>amdsmi_get_gpu_compute_process_info()&#160;:&#160;<a class="el" href="group__tagSystemInfo.html#ga9a48487a6e87754c9d6a9c091e15120f">amdsmi.h</a></li>
<li>amdsmi_get_gpu_compute_process_info_by_pid()&#160;:&#160;<a class="el" href="group__tagSystemInfo.html#gae45aedee9ed92ad3c04bad7d5b279476">amdsmi.h</a></li>
<li>amdsmi_get_gpu_cper_entries()&#160;:&#160;<a class="el" href="group__tagECCInfo.html#gad9d09a511bb40f90fa6d13c81f70bbdc">amdsmi.h</a></li>
<li>amdsmi_get_gpu_device_bdf()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#gad8548220f2501bec2efb45b18cf2824b">amdsmi.h</a></li>
<li>amdsmi_get_gpu_device_uuid()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#ga2c0e9226742b23d7bcb9d90890dedbb0">amdsmi.h</a></li>
<li>amdsmi_get_gpu_driver_info()&#160;:&#160;<a class="el" href="group__tagSoftwareVersion.html#ga517bfce7c554890761208e534dc877fe">amdsmi.h</a></li>
<li>amdsmi_get_gpu_ecc_count()&#160;:&#160;<a class="el" href="group__tagECCInfo.html#ga82bc8b416fe91718c56624af73956b69">amdsmi.h</a></li>
<li>amdsmi_get_gpu_ecc_enabled()&#160;:&#160;<a class="el" href="group__tagECCInfo.html#ga8345e03f3ff0bf1462cf517dfa4c20b6">amdsmi.h</a></li>
<li>amdsmi_get_gpu_ecc_status()&#160;:&#160;<a class="el" href="group__tagErrorQuery.html#ga7bb224e140c4f2123c7223279fb37898">amdsmi.h</a></li>
<li>amdsmi_get_gpu_enumeration_info()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#ga8e7133c50b3c5fbd6f99f997fd3a696b">amdsmi.h</a></li>
<li>amdsmi_get_gpu_event_notification()&#160;:&#160;<a class="el" href="group__tagEventNotification.html#ga6b68982dfd3c56d2c6fca40f5a003b5d">amdsmi.h</a></li>
<li>amdsmi_get_gpu_fan_rpms()&#160;:&#160;<a class="el" href="group__tagPhysicalStateQuery.html#gadd29a52502dd3e51dd8f56455df1bf39">amdsmi.h</a></li>
<li>amdsmi_get_gpu_fan_speed()&#160;:&#160;<a class="el" href="group__tagPhysicalStateQuery.html#ga4f9df5b361a420124eb305c010f6ef89">amdsmi.h</a></li>
<li>amdsmi_get_gpu_fan_speed_max()&#160;:&#160;<a class="el" href="group__tagPhysicalStateQuery.html#ga6a70b88b26dd240ce85818147bc60531">amdsmi.h</a></li>
<li>amdsmi_get_gpu_id()&#160;:&#160;<a class="el" href="group__tagIdentQuery.html#ga949a646ab376ed1e788efc83a70c1767">amdsmi.h</a></li>
<li>amdsmi_get_gpu_kfd_info()&#160;:&#160;<a class="el" href="group__tagAsicBoardInfo.html#ga4c0c6c43840e2cc22964d3700b160851">amdsmi.h</a></li>
<li>amdsmi_get_gpu_mem_overdrive_level()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#ga9fa1d436c99aeac1314285bb6a2f9282">amdsmi.h</a></li>
<li>amdsmi_get_gpu_memory_partition()&#160;:&#160;<a class="el" href="group__tagMemoryPartition.html#ga51050902b4af32502f0aed6732c6d41a">amdsmi.h</a></li>
<li>amdsmi_get_gpu_memory_partition_config()&#160;:&#160;<a class="el" href="group__tagMemoryPartition.html#ga432b45677afa3722e21ffa84d610961a">amdsmi.h</a></li>
<li>amdsmi_get_gpu_memory_reserved_pages()&#160;:&#160;<a class="el" href="group__tagMemoryQuery.html#ga96e9f235ac9f32d0852fa6d4b5de82f4">amdsmi.h</a></li>
<li>amdsmi_get_gpu_memory_total()&#160;:&#160;<a class="el" href="group__tagMemoryQuery.html#ga158552db49128193a82a75f7537304fd">amdsmi.h</a></li>
<li>amdsmi_get_gpu_memory_usage()&#160;:&#160;<a class="el" href="group__tagMemoryQuery.html#gab75f30e1e8992a6f52ed052a560bda9c">amdsmi.h</a></li>
<li>amdsmi_get_gpu_metrics_header_info()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#ga84ad16eb7299954ce75e2ace39f1e4ae">amdsmi.h</a></li>
<li>amdsmi_get_gpu_metrics_info()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#ga29b1e1a9fc2f4473a796f8dd15e34b5e">amdsmi.h</a></li>
<li>amdsmi_get_gpu_od_volt_curve_regions()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#gacc605bf744646ee4cc0cda92d8f21752">amdsmi.h</a></li>
<li>amdsmi_get_gpu_od_volt_info()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#gacb65202c1f186fd18ad5533a5401161e">amdsmi.h</a></li>
<li>amdsmi_get_gpu_overdrive_level()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#gafd9f0389a933c161a8fe1ac00f2db945">amdsmi.h</a></li>
<li>amdsmi_get_gpu_partition_metrics_info()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#ga8a35183bdeda839a60b0e785878e6954">amdsmi.h</a></li>
<li>amdsmi_get_gpu_pci_bandwidth()&#160;:&#160;<a class="el" href="group__tagPCIeQuery.html#gac9e9561c8ccd97e3ac1ad0d195174f2e">amdsmi.h</a></li>
<li>amdsmi_get_gpu_pci_replay_counter()&#160;:&#160;<a class="el" href="group__tagPCIeQuery.html#gaf78128b17693a8f5f2dda6c368e9ff90">amdsmi.h</a></li>
<li>amdsmi_get_gpu_pci_throughput()&#160;:&#160;<a class="el" href="group__tagPCIeQuery.html#ga8f53f0344e02fb58176044ca567a3eeb">amdsmi.h</a></li>
<li>amdsmi_get_gpu_perf_level()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#gab40582e822b579552fac6617f7c3415f">amdsmi.h</a></li>
<li>amdsmi_get_gpu_pm_metrics_info()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#ga5fef085f80fcf96510ea363669d7b563">amdsmi.h</a></li>
<li>amdsmi_get_gpu_power_profile_presets()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#ga2b48354bd68cd30799a32f9096c5002d">amdsmi.h</a></li>
<li>amdsmi_get_gpu_process_isolation()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfControl.html#gad08e64238480f6a0c98e3687e13124e3">amdsmi.h</a></li>
<li>amdsmi_get_gpu_process_list()&#160;:&#160;<a class="el" href="group__tagProcessInfo.html#ga07971c81d833b37c8c012a2a91dd6459">amdsmi.h</a></li>
<li>amdsmi_get_gpu_ptl_formats()&#160;:&#160;<a class="el" href="group__tagPTL.html#gab2fd90e4015a4f46931c5bb5fae6a1c1">amdsmi.h</a></li>
<li>amdsmi_get_gpu_ptl_state()&#160;:&#160;<a class="el" href="group__tagPTL.html#ga06a920f6ee43f12d34eb02bb3def79a1">amdsmi.h</a></li>
<li>amdsmi_get_gpu_ras_block_features_enabled()&#160;:&#160;<a class="el" href="group__tagMemoryQuery.html#ga2c11bf35d7f46575f012ac120594d9fe">amdsmi.h</a></li>
<li>amdsmi_get_gpu_ras_feature_info()&#160;:&#160;<a class="el" href="group__tagRasInfo.html#gadeb899cf4593a3f044b4169f05bf3bb1">amdsmi.h</a></li>
<li>amdsmi_get_gpu_reg_table_info()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#gaf86cf1873ebda7584e5f44afdcc8dd3b">amdsmi.h</a></li>
<li>amdsmi_get_gpu_revision()&#160;:&#160;<a class="el" href="group__tagIdentQuery.html#ga6539d6e24b354e5e683b06bbeaad775f">amdsmi.h</a></li>
<li>amdsmi_get_gpu_subsystem_id()&#160;:&#160;<a class="el" href="group__tagIdentQuery.html#gafad6357852da420dea35c826827ef089">amdsmi.h</a></li>
<li>amdsmi_get_gpu_subsystem_name()&#160;:&#160;<a class="el" href="group__tagIdentQuery.html#ga580ae87aa8b2f1a50bbca8ba0c2a4f4d">amdsmi.h</a></li>
<li>amdsmi_get_gpu_topo_numa_affinity()&#160;:&#160;<a class="el" href="group__tagPCIeQuery.html#ga58eb0d6689bb6e1b819129dab6c82b62">amdsmi.h</a></li>
<li>amdsmi_get_gpu_total_ecc_count()&#160;:&#160;<a class="el" href="group__tagECCInfo.html#ga62db9b031800bf53237a468b34adb8c3">amdsmi.h</a></li>
<li>amdsmi_get_gpu_vbios_info()&#160;:&#160;<a class="el" href="group__tagFWVbiosQuery.html#ga3d7250f6251f51946c58a82c8c78a9e9">amdsmi.h</a></li>
<li>amdsmi_get_gpu_vendor_name()&#160;:&#160;<a class="el" href="group__tagIdentQuery.html#ga802ae9b4d876fa1e2c12dff85fb28c8e">amdsmi.h</a></li>
<li>amdsmi_get_gpu_virtualization_mode()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#ga5c7716f5c97e37ecc11dc139f90f2f44">amdsmi.h</a></li>
<li>amdsmi_get_gpu_volt_metric()&#160;:&#160;<a class="el" href="group__tagPhysicalStateQuery.html#gaff7c20b116539a8cd81015577120b5b2">amdsmi.h</a></li>
<li>amdsmi_get_gpu_vram_info()&#160;:&#160;<a class="el" href="group__tagAsicBoardInfo.html#ga212a9ff5e6d862f8c25b1a0677a9ee71">amdsmi.h</a></li>
<li>amdsmi_get_gpu_vram_usage()&#160;:&#160;<a class="el" href="group__tagGPUMonitor.html#ga1d6d122a96115a11278c86c4c6cba3e2">amdsmi.h</a></li>
<li>amdsmi_get_gpu_vram_vendor()&#160;:&#160;<a class="el" href="group__tagIdentQuery.html#gacdce1ea2e4645574653fe855f82a6f1c">amdsmi.h</a></li>
<li>amdsmi_get_gpu_xcd_counter()&#160;:&#160;<a class="el" href="group__tagAsicBoardInfo.html#ga46ab4d56bacec10220fe1e88dc6eb43e">amdsmi.h</a></li>
<li>amdsmi_get_gpu_xgmi_link_status()&#160;:&#160;<a class="el" href="group__tagXGMI.html#ga4a4dc58714f52eb75f28b634da973b80">amdsmi.h</a></li>
<li>amdsmi_get_hsmp_metrics_table()&#160;:&#160;<a class="el" href="group__tagHSMPMetricsTable.html#ga13d09b204deeda124430470b12ad0ada">amdsmi.h</a></li>
<li>amdsmi_get_hsmp_metrics_table_version()&#160;:&#160;<a class="el" href="group__tagHSMPMetricsTable.html#ga612a2929a8ab4bc29485575a46d8ffe8">amdsmi.h</a></li>
<li>amdsmi_get_lib_version()&#160;:&#160;<a class="el" href="group__tagVersionQuery.html#ga8b846bf9fe2cfdef7b410c3fdd18ca61">amdsmi.h</a></li>
<li>amdsmi_get_link_metrics()&#160;:&#160;<a class="el" href="group__tagHWTopology.html#gab3d2eb1be203b52764e031a6c52d679c">amdsmi.h</a></li>
<li>amdsmi_get_link_topology_nearest()&#160;:&#160;<a class="el" href="group__tagHWTopology.html#gaeaa0d3d290613b2e19441636812305a4">amdsmi.h</a></li>
<li>amdsmi_get_minmax_bandwidth_between_processors()&#160;:&#160;<a class="el" href="group__tagHWTopology.html#ga974959443cc78daeec676d62ebadb343">amdsmi.h</a></li>
<li>amdsmi_get_node_handle()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#ga4b41e7650c3669322dd8a4c7974adfe9">amdsmi.h</a></li>
<li>amdsmi_get_npm_info()&#160;:&#160;<a class="el" href="group__tagAsicBoardInfo.html#ga5fbb388c57606d9d22938b125a6ae62b">amdsmi.h</a></li>
<li>amdsmi_get_pcie_info()&#160;:&#160;<a class="el" href="group__tagAsicBoardInfo.html#ga1c9b9cda6778dc4e28641859ebb352db">amdsmi.h</a></li>
<li>amdsmi_get_power_cap_info()&#160;:&#160;<a class="el" href="group__tagAsicBoardInfo.html#ga1a9ba2304c5a14d7e8bfd6f167f23942">amdsmi.h</a></li>
<li>amdsmi_get_power_info()&#160;:&#160;<a class="el" href="group__tagGPUMonitor.html#ga07ca16b959dbc14e9cb632cac5089d1c">amdsmi.h</a></li>
<li>amdsmi_get_processor_count_from_handles()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#gaf1cd4e58019dad154039cc992a2ec65f">amdsmi.h</a></li>
<li>amdsmi_get_processor_handle_from_bdf()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#gaafbcdbaf9b2e6ad48cc93d3f94adae1b">amdsmi.h</a></li>
<li>amdsmi_get_processor_handles()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#ga197fe8a857d4bf5eacea1bfaf9b81114">amdsmi.h</a></li>
<li>amdsmi_get_processor_handles_by_type()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#gabe8410612322dd1c14cdbc90cb7c658f">amdsmi.h</a></li>
<li>amdsmi_get_processor_info()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#ga0a47ae666c033c9486ae22858d539269">amdsmi.h</a></li>
<li>amdsmi_get_processor_type()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#ga30a25fa354b6c5be78406b7d65ba81e2">amdsmi.h</a></li>
<li>amdsmi_get_soc_pstate()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfControl.html#gaad6803d2a9232a2d31556a7975bf8bdf">amdsmi.h</a></li>
<li>amdsmi_get_socket_handles()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#ga9101e98774e9d6389f7e4ad6251ef176">amdsmi.h</a></li>
<li>amdsmi_get_socket_info()&#160;:&#160;<a class="el" href="group__tagProcDiscovery.html#ga4a0d957f0dd4a54587bd4401e1d2054d">amdsmi.h</a></li>
<li>amdsmi_get_supported_power_cap()&#160;:&#160;<a class="el" href="group__tagPowerControl.html#gaaf4de8392aaa2057cebee547eac1c502">amdsmi.h</a></li>
<li>amdsmi_get_temp_metric()&#160;:&#160;<a class="el" href="group__tagGPUMonitor.html#ga48337eb057bc24ef4c661f91ceb36c9a">amdsmi.h</a></li>
<li>amdsmi_get_threads_per_core()&#160;:&#160;<a class="el" href="group__tagHSMPSystemStats.html#gaac43e16f02184daf861d5122859255ba">amdsmi.h</a></li>
<li>amdsmi_get_utilization_count()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#ga649d757b74118d6ab8e2afde0675f6cf">amdsmi.h</a></li>
<li>amdsmi_get_violation_status()&#160;:&#160;<a class="el" href="group__tagGPUMonitor.html#gac8c772cee54beae0ec024c4eef0978c8">amdsmi.h</a></li>
<li>amdsmi_get_xgmi_info()&#160;:&#160;<a class="el" href="group__tagXGMI.html#gad96ce9dc886ab35178522c2866eaac75">amdsmi.h</a></li>
<li>amdsmi_get_xgmi_plpd()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfControl.html#ga03ad3a2ddc146c1efcf1b78b2d66c376">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_ATHUB&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976da6d59976c1f1401b79bededf423f628f8">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_DF&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976dad16ba4bba46c21ad15dd2f2f4cc5d39d">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_FUSE&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976dace7dfdbe5fcc41e251d18ea1fd377665">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_GFX&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976da1a72a322e41ce7bc81ff1eee65b07a51">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_HDP&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976da5370ea0a8638446bdbc7dbbd569c8a6b">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_IH&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976da301c605c5ab438ad384dd2dfa609eda7">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_INVALID&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976da45204dd49f81a592fdcb7109be6aa380">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_JPEG&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976dab65c78f9fa07651a74cf635ebeae4887">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_MCA&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976dafd8980e03ecd22cedf00d6e09ef72bcb">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_MMHUB&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976dae5d07f12a877d4cbc2bf668542196b75">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_MP0&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976da46c0e5e452676b6bde76196fba7490ac">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_MP1&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976da9e7d21547debf617e429272d48d5b623">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_MPIO&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976da63d280961faf75bbf63c4c27e8eb7287">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_PCIE_BIF&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976da9f6d038f28ae765a45aeaca3aac918e0">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_SDMA&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976daae260e6a0a721cb196744a4e284e2f1a">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_SEM&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976dafa266f93c44b21f494da4992d6f9279d">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_SMN&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976daf6c76faac5e240904834fa3b97939634">amdsmi.h</a></li>
<li>amdsmi_gpu_block_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976d">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_UMC&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976dabfdac947c5790127d82169f45ca0da14">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_VCN&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976da43b48134dca02d4d7bd922674de39075">amdsmi.h</a></li>
<li>AMDSMI_GPU_BLOCK_XGMI_WAFL&#160;:&#160;<a class="el" href="amdsmi_8h.html#acfb53db651ea977990be3f1e1a55976da11560ff4404d776cbb1fdfbb448aaef1">amdsmi.h</a></li>
<li>amdsmi_gpu_control_counter()&#160;:&#160;<a class="el" href="group__tagPerfCounter.html#ga3b22d26e61aa805b4359b826274c0c83">amdsmi.h</a></li>
<li>amdsmi_gpu_counter_group_supported()&#160;:&#160;<a class="el" href="group__tagPerfCounter.html#ga55ec8836c281b9ee2199af1e4ba4fcd9">amdsmi.h</a></li>
<li>amdsmi_gpu_create_counter()&#160;:&#160;<a class="el" href="group__tagPerfCounter.html#gafcfaeba25f842149c9bc74ffbd9ca31d">amdsmi.h</a></li>
<li>amdsmi_gpu_destroy_counter()&#160;:&#160;<a class="el" href="group__tagPerfCounter.html#ga5ff90b5effed73a0520cf161b35b2da2">amdsmi.h</a></li>
<li>amdsmi_gpu_driver_reload()&#160;:&#160;<a class="el" href="group__tagDriverControl.html#ga27e6b93e9389f212d076a64c6fe1ac79">amdsmi.h</a></li>
<li>amdsmi_gpu_read_counter()&#160;:&#160;<a class="el" href="group__tagPerfCounter.html#ga17d099c46614b5ccdb3e50ea48a4bcfe">amdsmi.h</a></li>
<li>AMDSMI_GPU_UUID_SIZE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6b44d2bcb3631554a05699449209a93a">amdsmi.h</a></li>
<li>amdsmi_gpu_validate_ras_eeprom()&#160;:&#160;<a class="el" href="group__tagMemoryQuery.html#gab91d0761ac0b8cb0f9b80f1fed5c0938">amdsmi.h</a></li>
<li>amdsmi_gpu_xgmi_error_status()&#160;:&#160;<a class="el" href="group__tagXGMI.html#ga78da75bf6a1b3fd14e5eae329a597734">amdsmi.h</a></li>
<li>amdsmi_init()&#160;:&#160;<a class="el" href="group__tagInitShutdown.html#ga3619686bf1a95a70ceddd9887bf0621b">amdsmi.h</a></li>
<li>AMDSMI_INIT_ALL_PROCESSORS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a3ea3ba05a1d96d7e9d78d651f6257bbca2fb1940c9cfadcba2e0f5470b08b116c">amdsmi.h</a></li>
<li>AMDSMI_INIT_AMD_APUS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a3ea3ba05a1d96d7e9d78d651f6257bbcafb8de66b0dbcd9c5c9015d1c538792d1">amdsmi.h</a></li>
<li>AMDSMI_INIT_AMD_CPUS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a3ea3ba05a1d96d7e9d78d651f6257bbca41f7173e03a536f36e3600de6934520c">amdsmi.h</a></li>
<li>AMDSMI_INIT_AMD_GPUS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a3ea3ba05a1d96d7e9d78d651f6257bbca009cb2ab2850b38d4da8851888ac64e5">amdsmi.h</a></li>
<li>amdsmi_init_flags_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a3ea3ba05a1d96d7e9d78d651f6257bbc">amdsmi.h</a></li>
<li>amdsmi_init_gpu_event_notification()&#160;:&#160;<a class="el" href="group__tagEventNotification.html#ga57b79c9acfbd0c6840cf6140dad3e4b5">amdsmi.h</a></li>
<li>AMDSMI_INIT_NON_AMD_CPUS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a3ea3ba05a1d96d7e9d78d651f6257bbcab8f4b0d44c16974a97cc64c1993aeaf6">amdsmi.h</a></li>
<li>AMDSMI_INIT_NON_AMD_GPUS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a3ea3ba05a1d96d7e9d78d651f6257bbca80226e4e01722b876643e603b4add97f">amdsmi.h</a></li>
<li>amdsmi_io_bw_encoding_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5018e391c7a552858e2a6836fdf3f828">amdsmi.h</a></li>
<li>amdsmi_is_gpu_power_management_enabled()&#160;:&#160;<a class="el" href="group__tagGPUMonitor.html#gae344b77769be3f96800b45fb77bc81b4">amdsmi.h</a></li>
<li>amdsmi_is_P2P_accessible()&#160;:&#160;<a class="el" href="group__tagHWTopology.html#gaa4b34d380cca12a65f5d2b20ca4b78ef">amdsmi.h</a></li>
<li>AMDSMI_LIB_VERSION_MAJOR&#160;:&#160;<a class="el" href="amdsmi_8h.html#a47c483bd94fbead7d3ef67940e40efd0">amdsmi.h</a></li>
<li>AMDSMI_LIB_VERSION_MINOR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada67253f213cc8a4cdaaadec112eac21">amdsmi.h</a></li>
<li>AMDSMI_LIB_VERSION_RELEASE&#160;:&#160;<a class="el" href="amdsmi_8h.html#ad11bba7a5811de16ca1b6e569535d8eb">amdsmi.h</a></li>
<li>AMDSMI_LINK_TYPE_INTERNAL&#160;:&#160;<a class="el" href="amdsmi_8h.html#a0f4bd19b05386cf7d5bc0254d5422406a37f97dcf62052c094559957d8c07ef51">amdsmi.h</a></li>
<li>AMDSMI_LINK_TYPE_NOT_APPLICABLE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a0f4bd19b05386cf7d5bc0254d5422406a13e7172b5fc710eb6d8efc83fe1e36cd">amdsmi.h</a></li>
<li>AMDSMI_LINK_TYPE_PCIE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a0f4bd19b05386cf7d5bc0254d5422406aa217ba952d3d8d4a844ce47e55d53d63">amdsmi.h</a></li>
<li>amdsmi_link_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a0f4bd19b05386cf7d5bc0254d5422406">amdsmi.h</a></li>
<li>AMDSMI_LINK_TYPE_UNKNOWN&#160;:&#160;<a class="el" href="amdsmi_8h.html#a0f4bd19b05386cf7d5bc0254d5422406a784193c93758c94dda341877170d7b5c">amdsmi.h</a></li>
<li>AMDSMI_LINK_TYPE_XGMI&#160;:&#160;<a class="el" href="amdsmi_8h.html#a0f4bd19b05386cf7d5bc0254d5422406af41307856c5063c0b6aa674f8d3594e4">amdsmi.h</a></li>
<li>AMDSMI_MAX_ACCELERATOR_PARTITIONS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a50ca244f7ee87f52c2055ad655e77065">amdsmi.h</a></li>
<li>AMDSMI_MAX_ACCELERATOR_PROFILE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a01e9539f67d6fd5c32cffbd7cbed81d4">amdsmi.h</a></li>
<li>AMDSMI_MAX_AID&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4ebbc99a70f700f062c0068642fe455e">amdsmi.h</a></li>
<li>AMDSMI_MAX_CACHE_TYPES&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae2a3be89a2d1879d56a2f8ec0482f9ba">amdsmi.h</a></li>
<li>AMDSMI_MAX_CONTAINER_TYPE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6f0f134aad85d0c0be4d16035aff1e41">amdsmi.h</a></li>
<li>AMDSMI_MAX_CP_PROFILE_RESOURCES&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5d34f5ff8ecf5f3768d2592d742dd8a8">amdsmi.h</a></li>
<li>AMDSMI_MAX_DEVICES&#160;:&#160;<a class="el" href="amdsmi_8h.html#aa90bed6d0b3af78009a03f8797443ff3">amdsmi.h</a></li>
<li>AMDSMI_MAX_ENGINES&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9accabd6a40ad6d135a7e5322bef5de2">amdsmi.h</a></li>
<li>AMDSMI_MAX_FAN_SPEED&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac550c8c8e7b70486b25657c6b363af14">amdsmi.h</a></li>
<li>AMDSMI_MAX_MM_IP_COUNT&#160;:&#160;<a class="el" href="amdsmi_8h.html#a0abf102ebe3d4d8b5c758933ee2778e5">amdsmi.h</a></li>
<li>AMDSMI_MAX_NUM_CLKS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a1d31a0ec370289f2bbbd27342daa347b">amdsmi.h</a></li>
<li>AMDSMI_MAX_NUM_FREQUENCIES&#160;:&#160;<a class="el" href="amdsmi_8h.html#ade9a45825f49035cfcf8c0373ee68877">amdsmi.h</a></li>
<li>AMDSMI_MAX_NUM_GFX_CLKS&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae744a5e5bdadb7f83adc67c8060eac8f">amdsmi.h</a></li>
<li>AMDSMI_MAX_NUM_JPEG&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab25643c171dca2a700fd5262b68515b3">amdsmi.h</a></li>
<li>AMDSMI_MAX_NUM_JPEG_ENG_V1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9a55a92f9a8c30fb6c28a9c5ecf6612f">amdsmi.h</a></li>
<li>AMDSMI_MAX_NUM_NUMA_NODES&#160;:&#160;<a class="el" href="amdsmi_8h.html#aee087c2a2d52b9524ad971151ceb33e8">amdsmi.h</a></li>
<li>AMDSMI_MAX_NUM_PM_POLICIES&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab73c8cd717935aa1972ca34b4e0a9ec4">amdsmi.h</a></li>
<li>AMDSMI_MAX_NUM_VCN&#160;:&#160;<a class="el" href="amdsmi_8h.html#afe9805b16e1d4c6a345716742a6335eb">amdsmi.h</a></li>
<li>AMDSMI_MAX_NUM_XCC&#160;:&#160;<a class="el" href="amdsmi_8h.html#a444f8d32a95a5bb7b366a6b06a14fe2e">amdsmi.h</a></li>
<li>AMDSMI_MAX_NUM_XCP&#160;:&#160;<a class="el" href="amdsmi_8h.html#a3a1e8ea252a03811abfb6b296b5897a6">amdsmi.h</a></li>
<li>AMDSMI_MAX_NUM_XGMI_LINKS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a216a5bb50c44c99936a154ff4cf7abe0">amdsmi.h</a></li>
<li>AMDSMI_MAX_NUM_XGMI_PHYSICAL_LINK&#160;:&#160;<a class="el" href="amdsmi_8h.html#a32bc25d802ad62bc7e303221983ea035">amdsmi.h</a></li>
<li>AMDSMI_MAX_STRING_LENGTH&#160;:&#160;<a class="el" href="amdsmi_8h.html#a784cab5e53ed993a638262f525d88741">amdsmi.h</a></li>
<li>AMDSMI_MAX_UTILIZATION_VALUES&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5f03a0b38c1b24dfefb90af828ee7fbd">amdsmi.h</a></li>
<li>AMDSMI_MEM_PAGE_STATUS_PENDING&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6b286dc2d4ff982d92cb6c26ba18d13ea78f239840373e5a9855fc84f03219f1c">amdsmi.h</a></li>
<li>AMDSMI_MEM_PAGE_STATUS_RESERVED&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6b286dc2d4ff982d92cb6c26ba18d13ea6f06d5a84850d9a464c2a6dc388daa3d">amdsmi.h</a></li>
<li>AMDSMI_MEM_PAGE_STATUS_UNRESERVABLE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6b286dc2d4ff982d92cb6c26ba18d13ea6eff0506b5f54e2c83275f46bec56bd3">amdsmi.h</a></li>
<li>AMDSMI_MEM_TYPE_GTT&#160;:&#160;<a class="el" href="amdsmi_8h.html#a298a422c1c354edf23a3c3585b08c6beadf85e1f374db6e690a98dffee04554b1">amdsmi.h</a></li>
<li>AMDSMI_MEM_TYPE_VIS_VRAM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a298a422c1c354edf23a3c3585b08c6bea6a87a4ba836b26fb79703bbb683d459d">amdsmi.h</a></li>
<li>AMDSMI_MEM_TYPE_VRAM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a298a422c1c354edf23a3c3585b08c6bea1f2fe2e6fd612fe4a4888ac1a0814ddc">amdsmi.h</a></li>
<li>amdsmi_memory_page_status_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6b286dc2d4ff982d92cb6c26ba18d13e">amdsmi.h</a></li>
<li>AMDSMI_MEMORY_PARTITION_NPS1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a952c3f1ce7b91fd32e58f2485d55623ea80fbef1053848839f31bc67ac7750c9b">amdsmi.h</a></li>
<li>AMDSMI_MEMORY_PARTITION_NPS2&#160;:&#160;<a class="el" href="amdsmi_8h.html#a952c3f1ce7b91fd32e58f2485d55623ea9e1032b45dc4767ccd8c4079b29a9d93">amdsmi.h</a></li>
<li>AMDSMI_MEMORY_PARTITION_NPS4&#160;:&#160;<a class="el" href="amdsmi_8h.html#a952c3f1ce7b91fd32e58f2485d55623eaab92b526283d7a424e69248aabe14e62">amdsmi.h</a></li>
<li>AMDSMI_MEMORY_PARTITION_NPS8&#160;:&#160;<a class="el" href="amdsmi_8h.html#a952c3f1ce7b91fd32e58f2485d55623ea6ad7a31bf116c8f92379b21086c9ace7">amdsmi.h</a></li>
<li>amdsmi_memory_partition_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a952c3f1ce7b91fd32e58f2485d55623e">amdsmi.h</a></li>
<li>amdsmi_memory_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a298a422c1c354edf23a3c3585b08c6be">amdsmi.h</a></li>
<li>amdsmi_mm_ip_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a695fb1bf1b82aa99d75a413f86984513">amdsmi.h</a></li>
<li>AMDSMI_MM_UVD&#160;:&#160;<a class="el" href="amdsmi_8h.html#a695fb1bf1b82aa99d75a413f86984513a384cb3eb4b11477a593b9773d0b7d068">amdsmi.h</a></li>
<li>AMDSMI_MM_VCE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a695fb1bf1b82aa99d75a413f86984513a5617f03ac53018545ce9462008a55a45">amdsmi.h</a></li>
<li>AMDSMI_MM_VCN&#160;:&#160;<a class="el" href="amdsmi_8h.html#a695fb1bf1b82aa99d75a413f86984513a688937b60c1af81a0a6c6f8b560b2170">amdsmi.h</a></li>
<li>amdsmi_node_handle&#160;:&#160;<a class="el" href="amdsmi_8h.html#a3153c7d4861232e4a55bab844c30428f">amdsmi.h</a></li>
<li>amdsmi_npm_status_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a0dcd824cc46a24ca30092c28a9bfe5f3">amdsmi.h</a></li>
<li>AMDSMI_NUM_HBM_INSTANCES&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4536ee3b850a40eca014ddf39ab1ecf9">amdsmi.h</a></li>
<li>AMDSMI_NUM_VOLTAGE_CURVE_POINTS&#160;:&#160;<a class="el" href="amdsmi_8h.html#af3ca09673d34f498173f0ae5898e3c4b">amdsmi.h</a></li>
<li>AMDSMI_POWER_CAP_TYPE_PPT0&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2ddeaa654db7876a88dd45bd23fecc8eaeab80717a177125301ce2c70c383677c">amdsmi.h</a></li>
<li>AMDSMI_POWER_CAP_TYPE_PPT1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2ddeaa654db7876a88dd45bd23fecc8ea453937379818c9838bde7e2eeb29f14d">amdsmi.h</a></li>
<li>amdsmi_power_cap_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2ddeaa654db7876a88dd45bd23fecc8e">amdsmi.h</a></li>
<li>amdsmi_power_profile_preset_masks_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae6f6809c055fe09f93bc974c0c88f410">amdsmi.h</a></li>
<li>amdsmi_process_handle_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a81277070964241adba59cb6ce24847f2">amdsmi.h</a></li>
<li>amdsmi_processor_handle&#160;:&#160;<a class="el" href="amdsmi_8h.html#aa24fa0128575971b3a476364f3b7ba87">amdsmi.h</a></li>
<li>AMDSMI_PROCESSOR_TYPE_AMD_APU&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5ef8c2a3ccd206d2cba44d63ba29367aa0306c272ec5125123b50ab473e384ae5">amdsmi.h</a></li>
<li>AMDSMI_PROCESSOR_TYPE_AMD_CPU&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5ef8c2a3ccd206d2cba44d63ba29367aa3eeaaed8c993c3313c639012fb0d04ad">amdsmi.h</a></li>
<li>AMDSMI_PROCESSOR_TYPE_AMD_CPU_CORE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5ef8c2a3ccd206d2cba44d63ba29367aa47b9fef5a9a4937463a798a4ad6d7f0e">amdsmi.h</a></li>
<li>AMDSMI_PROCESSOR_TYPE_AMD_GPU&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5ef8c2a3ccd206d2cba44d63ba29367aaa7857634313f2cd12bc92863ef25571d">amdsmi.h</a></li>
<li>AMDSMI_PROCESSOR_TYPE_NON_AMD_CPU&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5ef8c2a3ccd206d2cba44d63ba29367aa1ef29013270a6a408ab98d2165f1b372">amdsmi.h</a></li>
<li>AMDSMI_PROCESSOR_TYPE_NON_AMD_GPU&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5ef8c2a3ccd206d2cba44d63ba29367aad127c22211d0a59c969c0a2089e79e71">amdsmi.h</a></li>
<li>AMDSMI_PROCESSOR_TYPE_UNKNOWN&#160;:&#160;<a class="el" href="amdsmi_8h.html#a5ef8c2a3ccd206d2cba44d63ba29367aa0a4d690e6128f6c0e884d9a29440f2e6">amdsmi.h</a></li>
<li>AMDSMI_PTL_DATA_FORMAT_BF16&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab8f0937fd76e2066dc17805c9ec3853caa2967a8ab1e96ef94f18dd84f44db3cb">amdsmi.h</a></li>
<li>AMDSMI_PTL_DATA_FORMAT_F16&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab8f0937fd76e2066dc17805c9ec3853cab06b4731f5e97766c677b4717e596357">amdsmi.h</a></li>
<li>AMDSMI_PTL_DATA_FORMAT_F32&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab8f0937fd76e2066dc17805c9ec3853caa4c9a22ad9a9edf36cd1aa5e2fd3a49b">amdsmi.h</a></li>
<li>AMDSMI_PTL_DATA_FORMAT_F64&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab8f0937fd76e2066dc17805c9ec3853ca98ca65ad2d2be673672bd97bf4bc61d9">amdsmi.h</a></li>
<li>AMDSMI_PTL_DATA_FORMAT_F8&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab8f0937fd76e2066dc17805c9ec3853ca9dd0557e6a32099120f3af8420463051">amdsmi.h</a></li>
<li>AMDSMI_PTL_DATA_FORMAT_I8&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab8f0937fd76e2066dc17805c9ec3853ca1e4b044e38c9fefcb0bf095debab5bae">amdsmi.h</a></li>
<li>AMDSMI_PTL_DATA_FORMAT_INVALID&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab8f0937fd76e2066dc17805c9ec3853ca1bc63141b88028c6f0aba47920c7c880">amdsmi.h</a></li>
<li>amdsmi_ptl_data_format_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab8f0937fd76e2066dc17805c9ec3853c">amdsmi.h</a></li>
<li>AMDSMI_PTL_DATA_FORMAT_VECTOR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab8f0937fd76e2066dc17805c9ec3853caf2253f16d0e38aacdd129906150924eb">amdsmi.h</a></li>
<li>AMDSMI_PWR_PROF_PRST_3D_FULL_SCR_MASK&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae6f6809c055fe09f93bc974c0c88f410afa2116dcab977575f8a9b22dbda9cfc1">amdsmi.h</a></li>
<li>AMDSMI_PWR_PROF_PRST_BOOTUP_DEFAULT&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae6f6809c055fe09f93bc974c0c88f410a8ccfd6ae3092590dcf1faf22e061c141">amdsmi.h</a></li>
<li>AMDSMI_PWR_PROF_PRST_COMPUTE_MASK&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae6f6809c055fe09f93bc974c0c88f410a0d047bba43ee6d13bcbdb46e7cd12d24">amdsmi.h</a></li>
<li>AMDSMI_PWR_PROF_PRST_CUSTOM_MASK&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae6f6809c055fe09f93bc974c0c88f410ad3f2334a235d5465f4a1790f97e00f01">amdsmi.h</a></li>
<li>AMDSMI_PWR_PROF_PRST_INVALID&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae6f6809c055fe09f93bc974c0c88f410acbaedea24688205e3be00becdc98a619">amdsmi.h</a></li>
<li>AMDSMI_PWR_PROF_PRST_POWER_SAVING_MASK&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae6f6809c055fe09f93bc974c0c88f410a4317474a127465a9e9bb2c5780990779">amdsmi.h</a></li>
<li>AMDSMI_PWR_PROF_PRST_VIDEO_MASK&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae6f6809c055fe09f93bc974c0c88f410a79a607ade18027cd08c810d14e8b638d">amdsmi.h</a></li>
<li>AMDSMI_PWR_PROF_PRST_VR_MASK&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae6f6809c055fe09f93bc974c0c88f410afe435294f2baadcc561e50633fca4e7a">amdsmi.h</a></li>
<li>AMDSMI_RAS_ERR_STATE_DISABLED&#160;:&#160;<a class="el" href="amdsmi_8h.html#a48a0dac5f4801dc64bb96c2420c70e89aece267a9ed926b51a31138081d9d8c8a">amdsmi.h</a></li>
<li>AMDSMI_RAS_ERR_STATE_ENABLED&#160;:&#160;<a class="el" href="amdsmi_8h.html#a48a0dac5f4801dc64bb96c2420c70e89a98d4fe3921036bafcfc45b9ccf6a7bb5">amdsmi.h</a></li>
<li>AMDSMI_RAS_ERR_STATE_MULT_UC&#160;:&#160;<a class="el" href="amdsmi_8h.html#a48a0dac5f4801dc64bb96c2420c70e89a5a077cf5b37090ea035275c8a105c653">amdsmi.h</a></li>
<li>AMDSMI_RAS_ERR_STATE_NONE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a48a0dac5f4801dc64bb96c2420c70e89abb763a54c42211908fbe3c4596d3ecd9">amdsmi.h</a></li>
<li>AMDSMI_RAS_ERR_STATE_PARITY&#160;:&#160;<a class="el" href="amdsmi_8h.html#a48a0dac5f4801dc64bb96c2420c70e89a249b148f7b7a8b6dd43d603a117e6254">amdsmi.h</a></li>
<li>AMDSMI_RAS_ERR_STATE_POISON&#160;:&#160;<a class="el" href="amdsmi_8h.html#a48a0dac5f4801dc64bb96c2420c70e89a7c161f0a7d7ce482a6316d5dbbb9bf72">amdsmi.h</a></li>
<li>AMDSMI_RAS_ERR_STATE_SING_C&#160;:&#160;<a class="el" href="amdsmi_8h.html#a48a0dac5f4801dc64bb96c2420c70e89a4c5b41b3bfacfd618b717ef98da94c5a">amdsmi.h</a></li>
<li>amdsmi_ras_err_state_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a48a0dac5f4801dc64bb96c2420c70e89">amdsmi.h</a></li>
<li>AMDSMI_REG_PCIE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2530aff0ca5f74118f2c616a7cae2771aba42ed393e6e39ef144d93899149def7">amdsmi.h</a></li>
<li>amdsmi_reg_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2530aff0ca5f74118f2c616a7cae2771">amdsmi.h</a></li>
<li>AMDSMI_REG_USR&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2530aff0ca5f74118f2c616a7cae2771a4d2bb7630e567a9a4033774f58736596">amdsmi.h</a></li>
<li>AMDSMI_REG_USR1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2530aff0ca5f74118f2c616a7cae2771a920462d64ec0562ccb8f78d62e140bdf">amdsmi.h</a></li>
<li>AMDSMI_REG_WAFL&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2530aff0ca5f74118f2c616a7cae2771a646b4c0a304b7ef212a18925659d7994">amdsmi.h</a></li>
<li>AMDSMI_REG_XGMI&#160;:&#160;<a class="el" href="amdsmi_8h.html#a2530aff0ca5f74118f2c616a7cae2771a4109d233cfeb168d8418863aab571020">amdsmi.h</a></li>
<li>amdsmi_reset_gpu()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#ga8598b6493803f783d6f0b9c7d50e6927">amdsmi.h</a></li>
<li>amdsmi_reset_gpu_fan()&#160;:&#160;<a class="el" href="group__tagPhysicalStateControl.html#gabf429557b9a87a03fd260ccd3d4cc20a">amdsmi.h</a></li>
<li>amdsmi_reset_gpu_xgmi_error()&#160;:&#160;<a class="el" href="group__tagXGMI.html#gaa191dfb92964ed677a7219c5476f346a">amdsmi.h</a></li>
<li>amdsmi_set_clk_freq()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfControl.html#gad45b1f51e67a5c4ed934fcbc9aae5594">amdsmi.h</a></li>
<li>amdsmi_set_cpu_core_boostlimit()&#160;:&#160;<a class="el" href="group__tagPerfBoostControl.html#ga2b8bce3671542188baddc865765b2844">amdsmi.h</a></li>
<li>amdsmi_set_cpu_df_pstate_range()&#160;:&#160;<a class="el" href="group__tagPstateSelect.html#ga891f241c91bc94b1c17d3f0bde435530">amdsmi.h</a></li>
<li>amdsmi_set_cpu_gmi3_link_width_range()&#160;:&#160;<a class="el" href="group__tagGMI3WidthCont.html#ga3826a42500db113ce91b40a9861b3bde">amdsmi.h</a></li>
<li>amdsmi_set_cpu_pcie_link_rate()&#160;:&#160;<a class="el" href="group__tagPstateSelect.html#ga72b2bf59c679bed434123e212cec34dc">amdsmi.h</a></li>
<li>amdsmi_set_cpu_pwr_efficiency_mode()&#160;:&#160;<a class="el" href="group__tagPowerControl.html#gac25282366a44da043efe0730ab5bd9a7">amdsmi.h</a></li>
<li>amdsmi_set_cpu_socket_boostlimit()&#160;:&#160;<a class="el" href="group__tagPerfBoostControl.html#ga98d0b1799e5ffab7ffcd9a77add464ef">amdsmi.h</a></li>
<li>amdsmi_set_cpu_socket_lclk_dpm_level()&#160;:&#160;<a class="el" href="group__tagPstateSelect.html#ga25c3aeae12cbb4f423ff87284fc60465">amdsmi.h</a></li>
<li>amdsmi_set_cpu_socket_power_cap()&#160;:&#160;<a class="el" href="group__tagPowerControl.html#ga967b2989419fce1ba404cb67e6034f3d">amdsmi.h</a></li>
<li>amdsmi_set_cpu_xgmi_width()&#160;:&#160;<a class="el" href="group__tagXGMIBandwidthCont.html#ga45ff50294b993955d0fb9c121824c541">amdsmi.h</a></li>
<li>amdsmi_set_gpu_accelerator_partition_profile()&#160;:&#160;<a class="el" href="group__tagAcceleratorPartition.html#ga4180e5f1ea3777c31edb4c8461451bc7">amdsmi.h</a></li>
<li>amdsmi_set_gpu_clk_limit()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#ga4cd106aabb086fcc4e436c31a5b26517">amdsmi.h</a></li>
<li>amdsmi_set_gpu_clk_range()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#ga9f1db41ad0c34c57623896bc3a570d93">amdsmi.h</a></li>
<li>amdsmi_set_gpu_compute_partition()&#160;:&#160;<a class="el" href="group__tagComputePartition.html#ga5c222fec73ee53a688646be74de21923">amdsmi.h</a></li>
<li>amdsmi_set_gpu_event_notification_mask()&#160;:&#160;<a class="el" href="group__tagEventNotification.html#ga2f598d28df90d7084004328885b259b6">amdsmi.h</a></li>
<li>amdsmi_set_gpu_fan_speed()&#160;:&#160;<a class="el" href="group__tagPhysicalStateControl.html#ga2a277d0001fca06abf3a91bc12fe1583">amdsmi.h</a></li>
<li>amdsmi_set_gpu_memory_partition()&#160;:&#160;<a class="el" href="group__tagMemoryPartition.html#gaef29704cd516aa29f1c3d1a06a3077d7">amdsmi.h</a></li>
<li>amdsmi_set_gpu_memory_partition_mode()&#160;:&#160;<a class="el" href="group__tagMemoryPartition.html#ga492b237e2ec6d4e6ddd3e86c61f2f8c9">amdsmi.h</a></li>
<li>amdsmi_set_gpu_od_clk_info()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#gaffeeef46fd29d4b5362e8532b7d4b198">amdsmi.h</a></li>
<li>amdsmi_set_gpu_od_volt_info()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#ga880e858067cb60c35aa39b8507bf6a4d">amdsmi.h</a></li>
<li>amdsmi_set_gpu_overdrive_level()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfControl.html#gab09ce8bdd7e2fad1c532aaff01a5639c">amdsmi.h</a></li>
<li>amdsmi_set_gpu_pci_bandwidth()&#160;:&#160;<a class="el" href="group__tagPCIeControl.html#gad54b3e76e1394ec9de315449e0643fe2">amdsmi.h</a></li>
<li>amdsmi_set_gpu_perf_determinism_mode()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfQuery.html#gaba03597b9b70711dfdc6cb982c2063f4">amdsmi.h</a></li>
<li>amdsmi_set_gpu_perf_level()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfControl.html#ga5c21ddd1ab3cd8a1fceda7d79664659c">amdsmi.h</a></li>
<li>amdsmi_set_gpu_power_profile()&#160;:&#160;<a class="el" href="group__tagPowerControl.html#ga7784697b62fa5822f904ab0ed4cfa799">amdsmi.h</a></li>
<li>amdsmi_set_gpu_process_isolation()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfControl.html#gab5301e144324ac3375dbe3cd0ccaa095">amdsmi.h</a></li>
<li>amdsmi_set_gpu_ptl_formats()&#160;:&#160;<a class="el" href="group__tagPTL.html#ga3b1bbc398f877be6142f6b9bad61d349">amdsmi.h</a></li>
<li>amdsmi_set_gpu_ptl_state()&#160;:&#160;<a class="el" href="group__tagPTL.html#ga2d7a44b5c5c6c9f3c474727b1578ab3e">amdsmi.h</a></li>
<li>amdsmi_set_power_cap()&#160;:&#160;<a class="el" href="group__tagPowerControl.html#gaa29e20b71316c5bbe15bcf16716ab398">amdsmi.h</a></li>
<li>amdsmi_set_soc_pstate()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfControl.html#gacf21a428b91a11cd4c345195a39025b4">amdsmi.h</a></li>
<li>amdsmi_set_xgmi_plpd()&#160;:&#160;<a class="el" href="group__tagClkPowerPerfControl.html#ga3672a583e9ae205b440b19fce86c794b">amdsmi.h</a></li>
<li>amdsmi_shut_down()&#160;:&#160;<a class="el" href="group__tagInitShutdown.html#ga1718bc95de0b2287dd8c1517e22aac0f">amdsmi.h</a></li>
<li>AMDSMI_STATUS_ADDRESS_FAULT&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba875460a6690b63a5b0bde6aa59446a1e">amdsmi.h</a></li>
<li>AMDSMI_STATUS_AMDGPU_RESTART_ERR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06baaf664c052a68276d9b1f48bb6d035ea4">amdsmi.h</a></li>
<li>AMDSMI_STATUS_API_FAILED&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06baea856e3ccffa195cee9f004eb4b64eed">amdsmi.h</a></li>
<li>AMDSMI_STATUS_ARG_PTR_NULL&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba225d6cb55ae088fef8fee0c7f4a86499">amdsmi.h</a></li>
<li>AMDSMI_STATUS_BUSY&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba16cd13d40bd3f552f4c1440310d1877e">amdsmi.h</a></li>
<li>amdsmi_status_code_to_string()&#160;:&#160;<a class="el" href="group__tagErrorQuery.html#ga3a77d8d2e0d8c57cd9bfd66f25d92c0a">amdsmi.h</a></li>
<li>AMDSMI_STATUS_CORRUPTED_EEPROM&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba1ffb629673fe6f73048388d3a0f8e3c3">amdsmi.h</a></li>
<li>AMDSMI_STATUS_DIRECTORY_NOT_FOUND&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba0b49d868878a4eac36427a5c6fc4930f">amdsmi.h</a></li>
<li>AMDSMI_STATUS_DRIVER_NOT_LOADED&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba17d41bd20a399023284aae6e57bb3ca0">amdsmi.h</a></li>
<li>AMDSMI_STATUS_DRM_ERROR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba1ed695998501f647ad3a2543d0a52f8a">amdsmi.h</a></li>
<li>AMDSMI_STATUS_FAIL_LOAD_MODULE&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06baac7615b98c46328e322fafcede220a81">amdsmi.h</a></li>
<li>AMDSMI_STATUS_FAIL_LOAD_SYMBOL&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba5f5a6774e8520ae051f24c5622a56d10">amdsmi.h</a></li>
<li>AMDSMI_STATUS_FILE_ERROR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba19d7f9e854c69b62284b09b637f2f409">amdsmi.h</a></li>
<li>AMDSMI_STATUS_FILE_NOT_FOUND&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba420d13d2ada9292eedac8caaf8003dd1">amdsmi.h</a></li>
<li>AMDSMI_STATUS_HSMP_TIMEOUT&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba35792bfd78a912a4430f4e2ff1cfaf29">amdsmi.h</a></li>
<li>AMDSMI_STATUS_INIT_ERROR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba612f89f1246c3cdc4000b979923afa55">amdsmi.h</a></li>
<li>AMDSMI_STATUS_INPUT_OUT_OF_BOUNDS&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06baf51fe42f07000a2d6416589ab5a53881">amdsmi.h</a></li>
<li>AMDSMI_STATUS_INSUFFICIENT_SIZE&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba604e18606fd9c8064b6cf07889a063ef">amdsmi.h</a></li>
<li>AMDSMI_STATUS_INTERNAL_EXCEPTION&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba48e1ab6d937c1adf49e75946ae1823db">amdsmi.h</a></li>
<li>AMDSMI_STATUS_INTERRUPT&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba6df2abee1f2c94b8e21a2185fa71c5a0">amdsmi.h</a></li>
<li>AMDSMI_STATUS_INVAL&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba13e1d90abd53702e867b932d1a3a0df8">amdsmi.h</a></li>
<li>AMDSMI_STATUS_IO&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba259d2c4cad729e74d4d0ae63caa5ae9c">amdsmi.h</a></li>
<li>AMDSMI_STATUS_MAP_ERROR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba503344c615f51d364b9f1cf4f4cec847">amdsmi.h</a></li>
<li>AMDSMI_STATUS_MORE_DATA&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba93138f1b442c724cb8139803043f07b7">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NO_DATA&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba364576c0a7b629ab185c27adfd5ab69a">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NO_DRV&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba976cfa123701a84522999a8b5a31249f">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NO_ENERGY_DRV&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba748634c2a4936b5a0a4ee12a87040f53">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NO_HSMP_DRV&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba2c04b7661ab36762feda54422a8c659f">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NO_HSMP_MSG_SUP&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06baf2819ab25db26c62686d95dafb09281b">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NO_HSMP_SUP&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba4c74bdcc905b3145c4507e6b85c4a100">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NO_MSR_DRV&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba6cfd251d1b792ca07e62373f347719ab">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NO_PERM&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba9e666b96efb15462d0eec656e4325092">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NO_SLOT&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba67dce933fda96ca7cba3919beb182e75">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NON_AMD_CPU&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba0a0145f9cb1f94bba85dea47182dc44a">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NOT_FOUND&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06baa1f0973934e67f6734e5d5153876005a">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NOT_INIT&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba034fa8f2203716d3b4541bc9b8b5d54d">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NOT_SUPPORTED&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06bac120ff5d0095a65a3f17f63acfbf955e">amdsmi.h</a></li>
<li>AMDSMI_STATUS_NOT_YET_IMPLEMENTED&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba96b5b300eabb5f7e9aceb0e2dc3ebd8b">amdsmi.h</a></li>
<li>AMDSMI_STATUS_OUT_OF_RESOURCES&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba6420f81a250bdc35bb88af70fe851d28">amdsmi.h</a></li>
<li>AMDSMI_STATUS_REFCOUNT_OVERFLOW&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06bafb2344a030e6c477c1d7285b530a0bec">amdsmi.h</a></li>
<li>AMDSMI_STATUS_RETRY&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba3728ca2e672793fcc37700a16ca5d800">amdsmi.h</a></li>
<li>AMDSMI_STATUS_SETTING_UNAVAILABLE&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba3a19655694a61a8449915b586239c6c8">amdsmi.h</a></li>
<li>AMDSMI_STATUS_SUCCESS&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba6e0093d7a96f6e6c796fcedebf7e4963">amdsmi.h</a></li>
<li>amdsmi_status_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06b">amdsmi.h</a></li>
<li>AMDSMI_STATUS_TIMEOUT&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06baf0f54c274238442b5e147fef274e8a11">amdsmi.h</a></li>
<li>AMDSMI_STATUS_UNEXPECTED_DATA&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06bacf457da30d806869b62f2180d873b444">amdsmi.h</a></li>
<li>AMDSMI_STATUS_UNEXPECTED_SIZE&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba388ba4c1509941f644e643b030aaff86">amdsmi.h</a></li>
<li>AMDSMI_STATUS_UNKNOWN_ERROR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ab05c37a8d1e512898eef2d25fb9fe06ba17bf36a001b9ef5894331fee4ab5a0e8">amdsmi.h</a></li>
<li>amdsmi_stop_gpu_event_notification()&#160;:&#160;<a class="el" href="group__tagEventNotification.html#ga412b2cf0244b28b8bbb3c2fc8c9d1202">amdsmi.h</a></li>
<li>AMDSMI_TEMP_CRIT_MIN&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064a886a9d7479042562e6a5d1400ee7c496">amdsmi.h</a></li>
<li>AMDSMI_TEMP_CRIT_MIN_HYST&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064af1b9a50425c7807057510c0b4222e86e">amdsmi.h</a></li>
<li>AMDSMI_TEMP_CRITICAL&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064a52fdc120962ae218237cd7003de90db6">amdsmi.h</a></li>
<li>AMDSMI_TEMP_CRITICAL_HYST&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064a4b7e3fe43466aeb08c4b78b3a787bfad">amdsmi.h</a></li>
<li>AMDSMI_TEMP_CURRENT&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064ac07ca18e077a674b5e571906a2cf9120">amdsmi.h</a></li>
<li>AMDSMI_TEMP_EMERGENCY&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064a629ac5426093e38135dbf3d5cd91a975">amdsmi.h</a></li>
<li>AMDSMI_TEMP_EMERGENCY_HYST&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064abf52bbce263f5b802d3cc1a1657d3e6c">amdsmi.h</a></li>
<li>AMDSMI_TEMP_HIGHEST&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064add28e4b7aa6ac76a5cd2b9673a35906a">amdsmi.h</a></li>
<li>AMDSMI_TEMP_LOWEST&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064a7c27fd16105ad9fbd8f5755c8e7caedc">amdsmi.h</a></li>
<li>AMDSMI_TEMP_MAX&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064afab9c85a806ada761fd631a54b6bbcba">amdsmi.h</a></li>
<li>AMDSMI_TEMP_MAX_HYST&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064af86b17ef7c3bd1f3ca8ff33f96cd4c44">amdsmi.h</a></li>
<li>AMDSMI_TEMP_MIN&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064adc0df448db448211536f6af003cab115">amdsmi.h</a></li>
<li>AMDSMI_TEMP_MIN_HYST&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064af67d00636a9ca76ae5c6cef8cc1185ab">amdsmi.h</a></li>
<li>AMDSMI_TEMP_OFFSET&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064a60bd837746c28fa47283409214f65538">amdsmi.h</a></li>
<li>AMDSMI_TEMP_SHUTDOWN&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064a9a4309614d42ed48da46fbc920259200">amdsmi.h</a></li>
<li>amdsmi_temperature_metric_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#ac7a4fecaab14d714f21d4aeb68971064">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE__MAX&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fafbeb93a25813f7c4d40fd73387532d60">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_IBC&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fad4a38a82dfab5557cb6c4151ded9c29c">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_IBC_HSC&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa81aabfbc736345af5c8965de91a4e0b0">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_OAM_0_1_2_3_3V3_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fab35d7dd5936ea5b978344d0c86a3b7ce">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_OAM_0_1_HSC&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa1f4f5e3152c8b948ffc96cb423db63e7">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_OAM_2_3_HSC&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa62bcccc8b3ab38c5bb20648c180bb430">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_OAM_4_5_6_7_3V3_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126faf93b8eaa566708ed2c9376e3c5045976">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_OAM_4_5_HSC&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa847321ba9ee6ef95e9fdbb80c3772e99">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_OAM_6_7_HSC&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa25c0f1830448eb4a7350f9ef9abbe82d">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_RETIMER_0_1_0V9_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa91d6020e6e919559d01611ae0eae326b">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_RETIMER_0_1_2_3_1V2_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fae1b15d05883c672e536e5ec9c03fadc3">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_RETIMER_2_3_0V9_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa88dd598789db27a564acbcb76c25e361">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_RETIMER_4_5_0V9_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa30d4d7b8f2d32ce9545b5d76cb168714">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_RETIMER_4_5_6_7_1V2_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa556637532a20b8921c894821fcd6c333">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_RETIMER_6_7_0V9_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126faf04d21b910b303afd4b0e9fbd288a392">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_UBB_BACK&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fabbc60e39b6136d4acee0ca27617fc609">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_UBB_FPGA&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fac581ec4812e7a6ac7d8173afd7b375b7">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_UBB_FPGA_0V72_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa9fa57270f104cbbb6d2035ef11f478fe">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_UBB_FPGA_3V3_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126faa0b061efb6ff8af23eb189b0f5d3c764">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_UBB_FRONT&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126faead71dd8f25080f516d0ac1fa742aadf">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_UBB_IBC&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa42273d6e6e57930a79aedcf8c694ed38">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_UBB_OAM1&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fafdc60d50fc40a3e13b45f16d4823d4f3">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_UBB_OAM7&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fab33dc4d889e93b1dffd35dbf65836608">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_BASEBOARD_UBB_UFPGA&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa649c461881a6cffefe54afa0ce7167f1">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_EDGE&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa6495646facd6193e698902493804e450">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_NODE_OAM_X_04_HBM_B_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa6d8397530f07aa928de17bc42fec4d55">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_NODE_OAM_X_04_HBM_D_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa10b6ac60a637923253ee044b916a6dbb">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_NODE_OAM_X_IBC&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fadfa085cdde571e6d0d30d719f19b8f3a">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_NODE_OAM_X_IBC_2&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa2921de18dfdd758b71961e22603c2b2b">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_NODE_OAM_X_VDD18_VR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fad95d1fc4de2e018f1416fe60db6591a5">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_NODE_RETIMER_X&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fac772b5a3ac59a18b6770d65f7253703f">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDD_085_HBM&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa3c1e39acd59922b8eb1cc61783e514fa">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDD_USR&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa668c1a62abb941601afe9eec6b64d778">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDDCR_11_HBM_B&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126faba8e3f4d17be9adaa1d4bd37611bff96">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDDCR_11_HBM_D&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa43d0204818715828c5cded1ffd8fb0b9">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDDCR_SOC_A&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa23b0523cfb1e6781d5778ede115ce92c">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDDCR_SOC_C&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa6e7ca1b762ea03f8b98faa66ab1fa419">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDDCR_SOCIO_A&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa7858812d307a7f7efa1076bf86b96571">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDDCR_SOCIO_C&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa8b6ee1d1cd33c89a94d75f1b2801c680">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDDCR_VDD0&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa9e9c9968e87d9f5291ef9d12b7aa9b2f">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDDCR_VDD1&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa8a3a618852cfe37796c88bcdb531baae">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDDCR_VDD2&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa3e32d83b0973869ec0c17043d342ca06">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDDCR_VDD3&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa13fd1eee7e7bd718d11a217778e4eef1">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_GPUBOARD_VDDIO_11_E32&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126faa4bf9bde29af9d1d7b86dcc404c0f058">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_HBM_0&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa3c3f35949dd59db067205595af439b41">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_HBM_1&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fab1a368d9c2a79a906b3b4bf5bef1d340">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_HBM_2&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa2758179156b0f516e547b3c601237264">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_HBM_3&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa5e78149bf626343224e26d4e7a1a4de9">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_HOTSPOT&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa3b1776d26a12995c204f4e9b29947bd5">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_JUNCTION&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa4b86820bbf3102ac423fc586e7b394e0">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_PLX&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126faa5941c15286aa22bc31439ce3203d9c2">amdsmi.h</a></li>
<li>amdsmi_temperature_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126f">amdsmi.h</a></li>
<li>AMDSMI_TEMPERATURE_TYPE_VRAM&#160;:&#160;<a class="el" href="amdsmi_8h.html#ada6d0794ef2bcf2ab00d7fff9403126fa62b525535b812d230f20e178c892c72d">amdsmi.h</a></li>
<li>AMDSMI_TIME_FORMAT&#160;:&#160;<a class="el" href="amdsmi_8h.html#aade8ec5d9e59484ca329e068a52b4541">amdsmi.h</a></li>
<li>amdsmi_topo_get_link_type()&#160;:&#160;<a class="el" href="group__tagHWTopology.html#ga07911f54237e6c2ac02b0bdafe43be0e">amdsmi.h</a></li>
<li>amdsmi_topo_get_link_weight()&#160;:&#160;<a class="el" href="group__tagHWTopology.html#gac8f669bdd7bf49a3da69daac77408e02">amdsmi.h</a></li>
<li>amdsmi_topo_get_numa_node_number()&#160;:&#160;<a class="el" href="group__tagHWTopology.html#ga4566405f387ad5ba88f39828a19099eb">amdsmi.h</a></li>
<li>amdsmi_topo_get_p2p_status()&#160;:&#160;<a class="el" href="group__tagHWTopology.html#gac711004367f628c5d4fcac4abab968e6">amdsmi.h</a></li>
<li>amdsmi_utilization_counter_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9453dac970283a7815c067f996064141">amdsmi.h</a></li>
<li>AMDSMI_VIRTUALIZATION_MODE_BAREMETAL&#160;:&#160;<a class="el" href="amdsmi_8h.html#a73c4d3616f02f3cad28d1b6a4ea5c8dfa015f7929eb251337212d15ce7183332c">amdsmi.h</a></li>
<li>AMDSMI_VIRTUALIZATION_MODE_GUEST&#160;:&#160;<a class="el" href="amdsmi_8h.html#a73c4d3616f02f3cad28d1b6a4ea5c8dfacf85dd24cf8dbacd6945c73dec004dcf">amdsmi.h</a></li>
<li>AMDSMI_VIRTUALIZATION_MODE_HOST&#160;:&#160;<a class="el" href="amdsmi_8h.html#a73c4d3616f02f3cad28d1b6a4ea5c8dfa3c9bcc42399e7fb62e70a80e9f44206e">amdsmi.h</a></li>
<li>AMDSMI_VIRTUALIZATION_MODE_PASSTHROUGH&#160;:&#160;<a class="el" href="amdsmi_8h.html#a73c4d3616f02f3cad28d1b6a4ea5c8dfadeca99dd750d3139be1676997a648b37">amdsmi.h</a></li>
<li>amdsmi_virtualization_mode_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a73c4d3616f02f3cad28d1b6a4ea5c8df">amdsmi.h</a></li>
<li>AMDSMI_VIRTUALIZATION_MODE_UNKNOWN&#160;:&#160;<a class="el" href="amdsmi_8h.html#a73c4d3616f02f3cad28d1b6a4ea5c8dfa08c71c956bbfd95908308bad43af9504">amdsmi.h</a></li>
<li>AMDSMI_VOLT_AVERAGE&#160;:&#160;<a class="el" href="amdsmi_8h.html#a990b09744764e2e70c3c17a205d336a1a6cdee756ae7a1066db50971dea96bc11">amdsmi.h</a></li>
<li>AMDSMI_VOLT_CURRENT&#160;:&#160;<a class="el" href="amdsmi_8h.html#a990b09744764e2e70c3c17a205d336a1a8b4259456b46713824a157994e633f20">amdsmi.h</a></li>
<li>AMDSMI_VOLT_HIGHEST&#160;:&#160;<a class="el" href="amdsmi_8h.html#a990b09744764e2e70c3c17a205d336a1a51559c63ff33c8d583eceae4c084b1db">amdsmi.h</a></li>
<li>AMDSMI_VOLT_LOWEST&#160;:&#160;<a class="el" href="amdsmi_8h.html#a990b09744764e2e70c3c17a205d336a1a0a3f433cf998ee350b8e72e12c8656fa">amdsmi.h</a></li>
<li>AMDSMI_VOLT_MAX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a990b09744764e2e70c3c17a205d336a1ac7baccb342f07bd01feb9e16eda4421b">amdsmi.h</a></li>
<li>AMDSMI_VOLT_MAX_CRIT&#160;:&#160;<a class="el" href="amdsmi_8h.html#a990b09744764e2e70c3c17a205d336a1a2bf98fd39ffa8d760bab038c39c70019">amdsmi.h</a></li>
<li>AMDSMI_VOLT_MIN&#160;:&#160;<a class="el" href="amdsmi_8h.html#a990b09744764e2e70c3c17a205d336a1a6668523008b328abf4866a2a58141949">amdsmi.h</a></li>
<li>AMDSMI_VOLT_MIN_CRIT&#160;:&#160;<a class="el" href="amdsmi_8h.html#a990b09744764e2e70c3c17a205d336a1af8ebd0f5bba7a1566c570e3cef2c8a4f">amdsmi.h</a></li>
<li>AMDSMI_VOLT_TYPE_INVALID&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9d1d79f9bb22b9f6eaa6a6afc0bde37da7e05cbe8703048cc79e9e2893a027db9">amdsmi.h</a></li>
<li>AMDSMI_VOLT_TYPE_VDDBOARD&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9d1d79f9bb22b9f6eaa6a6afc0bde37da76c4145d1d0fbc02c97f5e696d0a7ca5">amdsmi.h</a></li>
<li>AMDSMI_VOLT_TYPE_VDDGFX&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9d1d79f9bb22b9f6eaa6a6afc0bde37daa2ab14d9babf1619939a11f727f27dae">amdsmi.h</a></li>
<li>amdsmi_voltage_metric_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a990b09744764e2e70c3c17a205d336a1">amdsmi.h</a></li>
<li>amdsmi_voltage_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a9d1d79f9bb22b9f6eaa6a6afc0bde37d">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_DDR2&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea7825d31a2f6e481c4b3f05e47a7d407e">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_DDR3&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea54f1a957b6b1db47c1ca4d63c6ff5098">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_DDR4&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2eaf826b2c6bbdd3815ff3b6953fcedf8c1">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_DDR5&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2eaaaa186787f3ed898bfb8445b40f11687">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_GDDR1&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea3b115648ea85911709b7adcaa26befe9">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_GDDR2&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea0ad8ae8577f0ddd7e4bee478631030ed">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_GDDR3&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea36d1ad6b891ef085b67d04612664ce5e">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_GDDR4&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea6bb5e968ac48546b751d41b917590619">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_GDDR5&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea4e43e33683f59c15f13a903794d64834">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_GDDR6&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea0fe25fea62bcd0565c03cf8b676acad1">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_GDDR7&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea807bdea1affcbdeebecdc3429a206079">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_HBM&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea221d9654dd13d7caf9f0cd4aeba0523e">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_HBM2&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea874835c6c559198af6390b11bfad16ea">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_HBM2E&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea0eaef2f9e9746039ef14001cc5b80659">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_HBM3&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea3b1e6c662c43392dc00e8d5e0b055844">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_HBM3E&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea4af4e202f3b69d737f6e829ad4568262">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_LPDDR4&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea971f06453d8e1363c0b11fcaadf48790">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_LPDDR5&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2ea3f1b6f6a439a8e8d13af6eab8fa516d5">amdsmi.h</a></li>
<li>amdsmi_vram_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2e">amdsmi.h</a></li>
<li>AMDSMI_VRAM_TYPE_UNKNOWN&#160;:&#160;<a class="el" href="amdsmi_8h.html#a4696b5e60938646a59444e35ee23fc2eafb343beaed34ffb7698c7a28941b0cf3">amdsmi.h</a></li>
<li>AMDSMI_XGMI_LINK_DISABLE&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae3411f9c0d61267e6349261a2e011225ae3777d30cd7bbc3a5efd6330740533ab">amdsmi.h</a></li>
<li>AMDSMI_XGMI_LINK_DOWN&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae3411f9c0d61267e6349261a2e011225a94c304c6e04fbc3a9ca2d86d8faedc9e">amdsmi.h</a></li>
<li>amdsmi_xgmi_link_status_type_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae3411f9c0d61267e6349261a2e011225">amdsmi.h</a></li>
<li>AMDSMI_XGMI_LINK_UP&#160;:&#160;<a class="el" href="amdsmi_8h.html#ae3411f9c0d61267e6349261a2e011225a3be84be3fb1fd54ba51864b0e82ee944">amdsmi.h</a></li>
<li>AMDSMI_XGMI_STATUS_ERROR&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6c43df28ab18047c877ce8d0e508a354adb5fa86ba92c0eea28ec687cdbc4ff0f">amdsmi.h</a></li>
<li>AMDSMI_XGMI_STATUS_MULTIPLE_ERRORS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6c43df28ab18047c877ce8d0e508a354a2f9055414475f35c1d53a5a3a064f3b9">amdsmi.h</a></li>
<li>AMDSMI_XGMI_STATUS_NO_ERRORS&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6c43df28ab18047c877ce8d0e508a354a8745368cb747aed1fc7b5ae46f962bac">amdsmi.h</a></li>
<li>amdsmi_xgmi_status_t&#160;:&#160;<a class="el" href="amdsmi_8h.html#a6c43df28ab18047c877ce8d0e508a354">amdsmi.h</a></li>
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
       href="files.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">File List</p>
      </div>
    </a>
    <a class="right-next"
       href="annotated.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Data Structures</p>
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
