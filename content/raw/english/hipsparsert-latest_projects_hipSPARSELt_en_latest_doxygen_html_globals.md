---
title: "hipSPARSELt: Globals &#8212; hipSPARSELt 0.2.6 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSELt/en/latest/doxygen/html/globals.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:10:33.242419+00:00
content_hash: "e6dfaadfea260e68"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>hipSPARSELt: Globals &#8212; hipSPARSELt 0.2.6 Documentation</title>
  
  
  
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
  <link href="../../_static/styles/theme.css?digest=8878045cc6db502f8baf" rel="stylesheet" />
<link href="../../_static/styles/pydata-sphinx-theme.css?digest=8878045cc6db502f8baf" rel="stylesheet" />

    <link rel="stylesheet" type="text/css" href="../../_static/pygments.css?v=8f2a1f02" />
    <link rel="stylesheet" type="text/css" href="../../_static/styles/sphinx-book-theme.css?v=a3416100" />
    <link rel="stylesheet" type="text/css" href="../../_static/mystnb.8ecb98da25f57f5357bf6f572d296f466b2cfe2517ffebfabe82451661e28f02.css" />
    <link rel="stylesheet" type="text/css" href="../../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../../_static/sphinx-design.min.css?v=95c83b7e" />
  
  <!-- So that users can add custom icons -->
  <script src="../../_static/scripts/fontawesome.js?digest=8878045cc6db502f8baf"></script>
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../../_static/scripts/bootstrap.js?digest=8878045cc6db502f8baf" />
<link rel="preload" as="script" href="../../_static/scripts/pydata-sphinx-theme.js?digest=8878045cc6db502f8baf" />

    <script src="../../_static/documentation_options.js?v=519527b2"></script>
    <script src="../../_static/doctools.js?v=9bcbadda"></script>
    <script src="../../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../../_static/search.js?v=90a4452c"></script>
    <script src="../../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
    <script src="../../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/html/globals';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="Globals" href="globals_func.html" />
    <link rel="prev" title="Globals" href="globals_globals.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hipsparselt" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/globals.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
  <body data-bs-spy="scroll" data-bs-target=".bd-toc-nav" data-offset="180" data-bs-root-margin="0px 0px -60%" data-default-mode="">

  
  
  <div id="pst-skip-link" class="skip-link d-print-none"><a href="#main-content">Skip to main content</a></div>
  
  <div id="pst-scroll-pixel-helper"></div>
  
  <button type="button" class="btn rounded-pill" id="pst-back-to-top">
    <i class="fa-solid fa-arrow-up"></i>Back to top</button>

  
  <dialog id="pst-search-dialog">
    
<form class="bd-search d-flex align-items-center"
      action="../../search.html"
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
                    <img src="../../_static/images/amd-header-logo.svg" alt="AMD Logo" title="AMD Logo" width="90" class="d-inline-block align-text-top hover-opacity"/>
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

  
    
  

<a class="navbar-brand logo" href="../../index.html">
  
  
  
  
  
  
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
<li class="toctree-l1"><a class="reference internal" href="../../what-is-hipsparselt.html">What is hipSPARSELt?</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../install/quick-start-install.html">Quick start installation guide</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../install/install-hipsparselt.html">Detailed installation guide</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../conceptual/storage-format.html">Storage formats</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../conceptual/mi300-features.html">Features for the Instinct MI300 series</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../how-to/device-stream-management.html">Manage devices and streams</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../how-to/porting.html">Port from NVIDIA CUDA</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Examples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparselt/clients/samples">Client samples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">API Reference</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../reference/supported-functions.html">Supported functions</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/data-type-support.html">Data type support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/env-variables.html">Environment variables</a></li>
<li class="toctree-l1 current active has-children"><a class="reference internal" href="index.html">API library</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2"><a class="reference internal" href="modules.html">Modules</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="annotated_data_structures.html">Data Structures</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="classes.html">Data Structure Index</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="functions_data_fields.html">Data Fields</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="functions.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars.html">Variables</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2 current active has-children"><a class="reference internal" href="files_files.html">Files</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l3"><a class="reference internal" href="files.html">File List</a></li>
<li class="toctree-l3 current active has-children"><a class="reference internal" href="globals_globals.html">Globals</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l4 current active"><a class="current reference internal" href="#">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="globals_func.html">Functions</a></li>
<li class="toctree-l4"><a class="reference internal" href="globals_enum.html">Enumerations</a></li>
<li class="toctree-l4"><a class="reference internal" href="globals_eval.html">Enumerator</a></li>
<li class="toctree-l4"><a class="reference internal" href="globals_defs.html">Macros</a></li>
</ul>
</details></li>
</ul>
</details></li>
</ul>
</details></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">About</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../license.html">License</a></li>
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
      <a href="../../index.html" class="nav-link" aria-label="Home">
        <i class="fa-solid fa-home"></i>
      </a>
    </li>
    
    <li class="breadcrumb-item"><a href="index.html" class="nav-link">hipSPARSELt</a></li>
    
    
    <li class="breadcrumb-item"><a href="files_files.html" class="nav-link">Files</a></li>
    
    
    <li class="breadcrumb-item"><a href="globals_globals.html" class="nav-link">Globals</a></li>
    
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">hipSPARSELt: Globals</span></li>
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
<html xmlns="http://www.w3.org/1999/xhtml" lang="$langISO">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.1"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>hipSPARSELt: Globals</title>
<link href="tabs.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="dynsections.js"></script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    extensions: ["tex2jax.js"],
    jax: ["input/TeX","output/HTML-CSS"],
});
</script>
<script type="text/javascript" async="async" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js"></script>
<link href="stylesheet.css" rel="stylesheet" type="text/css" />
<link href="extra_stylesheet.css" rel="stylesheet" type="text/css"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hipsparselt" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/globals.html" /><meta name="readthedocs-http-status" content="200" /></head>
<body>
<div id="top"><!-- do not remove this div, it is closed by doxygen! -->
<!-- Generated by Doxygen 1.9.1 -->
<script type="text/javascript" src="menudata.js"></script>
<script type="text/javascript" src="menu.js"></script>
<script type="text/javascript">
/* @license magnet:?xt=urn:btih:cf05388f2679ee054f2beb29a391d25f4e673ac3&amp;dn=gpl-2.0.txt GPL-v2 */
$(function() {
  initMenu('',false,false,'search.php','Search');
});
/* @license-end */</script>
<div id="main-nav"></div>
</div><!-- top -->
<div class="contents">
<div class="textblock">Here is a list of all functions, variables, defines, enums, and typedefs with links to the files they belong to:</div>

<h3><a id="index__5F"></a>- _ -</h3><ul>
<li>_HIPSPARSELT_H_
: <a class="el" href="hipsparselt_8h.html#ad9ba969a65728feb75577dd23ab72f84">hipsparselt.h</a>
</li>
</ul>


<h3><a id="index_h"></a>- h -</h3><ul>
<li>HIPSPARSELT_COMPUTE_16F
: <a class="el" href="group__types__module.html#gga799f01caed605aea534e9b601df5cc6fadf0fa31abfbe6211b00f704dc4bcff5a">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_COMPUTE_32F
: <a class="el" href="group__types__module.html#gga799f01caed605aea534e9b601df5cc6fa2954b605b8355c6c4218ee3f68fb2ed2">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_COMPUTE_32I
: <a class="el" href="group__types__module.html#gga799f01caed605aea534e9b601df5cc6fad032a860bbcb08d7e22c00dfc8c85d04">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_COMPUTE_TF32
: <a class="el" href="group__types__module.html#gga799f01caed605aea534e9b601df5cc6fac603bef5dffe1e852409f6d9b32a00b0">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_COMPUTE_TF32_FAST
: <a class="el" href="group__types__module.html#gga799f01caed605aea534e9b601df5cc6fa3a65c2c5594a4473f3adc530c6c52fe2">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MAT_BATCH_STRIDE
: <a class="el" href="group__types__module.html#ggad7518adae6ff2568bd611aa33415b21aa7b37b150a2827c14dcb73a9caf67caa8">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MAT_NUM_BATCHES
: <a class="el" href="group__types__module.html#ggad7518adae6ff2568bd611aa33415b21aae14141a4d218e2fdbc91987d36eca885">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ACTIVATION_ABS
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6ad7b893e809171ca491b8e038ac6be9f6">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ACTIVATION_GELU
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6ad5c9949d291160baf4eeda5f4969985a">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ACTIVATION_GELU_SCALING
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6a59a9c7efb70869510f922a4d6076090a">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ACTIVATION_LEAKYRELU
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6a2b98b9c1954518a8d44de1c014b172d6">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ACTIVATION_LEAKYRELU_ALPHA
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6a4aeec9efd6ba13890931252e54b11d5a">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ACTIVATION_RELU
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6ad081d412bc74df4c3cd3af88e07df5a3">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ACTIVATION_RELU_THRESHOLD
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6ae09b63e1212e13fd3253fc16dad60a77">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ACTIVATION_RELU_UPPERBOUND
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6a160c85e175b33639b174fe4af319a876">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ACTIVATION_SIGMOID
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6abb643d36cbdeec9ef32d7e76d50997a2">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ACTIVATION_TANH
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6a915b50638f90082087baefe5091014d8">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ACTIVATION_TANH_ALPHA
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6aca83467a7d487ea16de64e0e0f34eefa">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ACTIVATION_TANH_BETA
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6a597aee79b9a2c999eabed2d6779deed5">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ALG_CONFIG_ID
: <a class="el" href="group__types__module.html#gga4ad639909160f12aa0f72aac70e4aecbab13be181949ecf972dd29540180d2ecf">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ALG_CONFIG_MAX_ID
: <a class="el" href="group__types__module.html#gga4ad639909160f12aa0f72aac70e4aecbaf7c217902fdc88935f428aeeee436fc4">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ALG_DEFAULT
: <a class="el" href="group__types__module.html#gga3623439a847b90ec55394320a6c559ffad828ad2948c0fdb1fa1c4a34a9d1977d">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_ALPHA_VECTOR_SCALING
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6a8b7b649ab310b7f65772b78b495c557e">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_BETA_VECTOR_SCALING
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6ad07bdd33e71899318e11724ec57073d5">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_BIAS_POINTER
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6a289dbee5f6a2cd5ea6384209c4167317">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_BIAS_STRIDE
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6a27d427fcdb37e3a8f653d84bbc2c351a">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_BIAS_TYPE
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6a2dd720ee5014168c978a3a13c8d677e8">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_SEARCH_ITERATIONS
: <a class="el" href="group__types__module.html#gga4ad639909160f12aa0f72aac70e4aecbaadabc07e66f50838879f63ac44f61ed8">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_SPARSE_MAT_POINTER
: <a class="el" href="group__types__module.html#ggaab48de8d7e9a0777eebda8e27db196b6afe04256c87b8992d20818d0a6edf6cbb">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_SPLIT_K
: <a class="el" href="group__types__module.html#gga4ad639909160f12aa0f72aac70e4aecba3777c7eb20bd4147a42809cbcfd0f0f9">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_SPLIT_K_BUFFERS
: <a class="el" href="group__types__module.html#gga4ad639909160f12aa0f72aac70e4aecba45ffbf81302644f8716931238589365f">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_MATMUL_SPLIT_K_MODE
: <a class="el" href="group__types__module.html#gga4ad639909160f12aa0f72aac70e4aecbaadee35a575a37281914f227da1437581">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_PRUNE_SPMMA_STRIP
: <a class="el" href="group__types__module.html#ggacbdbf2fd179cd61f918dc6f7eb2eca5da754defd6bed1f0fffc1769ca60e1e762">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_PRUNE_SPMMA_TILE
: <a class="el" href="group__types__module.html#ggacbdbf2fd179cd61f918dc6f7eb2eca5da584d549812d4d7d4b3d598c8845c38af">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_SPARSITY_50_PERCENT
: <a class="el" href="group__types__module.html#gga1a34328c8f8454db5da99f841b140274a7f552df2611e829ee63a153feaaaef81">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_SPLIT_K_MODE_ONE_KERNEL
: <a class="el" href="group__types__module.html#gga97a3db1aa6b2f60fbad1f2843bf39574a59fbabc247e563b949b580bb008c1bfb">hipsparselt.h</a>
</li>
<li>HIPSPARSELT_SPLIT_K_MODE_TWO_KERNELS
: <a class="el" href="group__types__module.html#gga97a3db1aa6b2f60fbad1f2843bf39574a2dbd6565aab74a7b82bcd85c6a0088fd">hipsparselt.h</a>
</li>
<li>hipsparseLtComputetype_t
: <a class="el" href="group__types__module.html#ga799f01caed605aea534e9b601df5cc6f">hipsparselt.h</a>
</li>
<li>hipsparseLtDenseDescriptorInit()
: <a class="el" href="group__matrix__desc__module.html#ga82d9f40b07888dd124f14807695be6f0">hipsparselt.h</a>
</li>
<li>hipsparseLtDestroy()
: <a class="el" href="group__library__module.html#gaa0d5bbc911007a099b86c57c551340a1">hipsparselt.h</a>
</li>
<li>hipsparseLtGetArchName()
: <a class="el" href="hipsparselt_8h.html#a358185f9aae3d1da89c07b87ff47501c">hipsparselt.h</a>
</li>
<li>hipsparseLtGetGitRevision()
: <a class="el" href="hipsparselt_8h.html#a072838ca3915e0aae1f7fee1fd3566bc">hipsparselt.h</a>
</li>
<li>hipsparseLtGetProperty()
: <a class="el" href="group__library__module.html#gaac4519fbbe9179a0e7e0658a9fe5e738">hipsparselt.h</a>
</li>
<li>hipsparseLtGetVersion()
: <a class="el" href="group__library__module.html#ga7ff18d1af1842734492a95be60b6b806">hipsparselt.h</a>
</li>
<li>hipsparseLtInit()
: <a class="el" href="group__library__module.html#ga3c9c0f507a6a88d579b4d932e6155ad7">hipsparselt.h</a>
</li>
<li>hipsparseLtInitialize()
: <a class="el" href="group__aux__module.html#ga3447a540086b0cedf8822d40c54b7d33">hipsparselt.h</a>
</li>
<li>hipsparseLtMatDescAttribute_t
: <a class="el" href="group__types__module.html#gad7518adae6ff2568bd611aa33415b21a">hipsparselt.h</a>
</li>
<li>hipsparseLtMatDescGetAttribute()
: <a class="el" href="group__matrix__desc__module.html#ga46aa94b3bf8429830adae36ab46f5ed7">hipsparselt.h</a>
</li>
<li>hipsparseLtMatDescriptorDestroy()
: <a class="el" href="group__matrix__desc__module.html#gace64690f478190d6ca0257db216c8d9b">hipsparselt.h</a>
</li>
<li>hipsparseLtMatDescSetAttribute()
: <a class="el" href="group__matrix__desc__module.html#ga565b7581216a123b034aeb4d94eb69f2">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmul()
: <a class="el" href="group__matmul__module.html#gac6456af5bf13f55fd37e090b28509a73">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulAlg_t
: <a class="el" href="group__types__module.html#ga3623439a847b90ec55394320a6c559ff">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulAlgAttribute_t
: <a class="el" href="group__types__module.html#ga4ad639909160f12aa0f72aac70e4aecb">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulAlgGetAttribute()
: <a class="el" href="group__matmul__algo__module.html#gaceebbc954c97b4dc9d23f990b21d8761">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulAlgSelectionInit()
: <a class="el" href="group__matmul__algo__module.html#ga7f88a0a97ced9e8fdbe9749311f7115e">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulAlgSetAttribute()
: <a class="el" href="group__matmul__algo__module.html#gabe8fd5d641a015f798d5d1c638c51cf9">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulDescAttribute_t
: <a class="el" href="group__types__module.html#gaab48de8d7e9a0777eebda8e27db196b6">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulDescGetAttribute()
: <a class="el" href="group__matmul__desc__module.html#ga1540620f823a27daa99a6a7860cef13f">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulDescriptorInit()
: <a class="el" href="group__matmul__desc__module.html#ga395b02712c053ea0591b6d8af5f7fe6a">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulDescSetAttribute()
: <a class="el" href="group__matmul__desc__module.html#gae9e62ce538b5de36cf655bacc6fb7b3f">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulGetWorkspace()
: <a class="el" href="group__matmul__module.html#gad46ad238a2a4419b616e2ab21cccb726">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulPlanDestroy()
: <a class="el" href="group__matmul__module.html#gada5ad89501cfab7f7712f4a5a4a69bc6">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulPlanInit()
: <a class="el" href="group__matmul__module.html#gae031c2068e645c38cea8f98673c7a197">hipsparselt.h</a>
</li>
<li>hipsparseLtMatmulSearch()
: <a class="el" href="group__matmul__module.html#ga83ae27a6656d28a4df577643a2e327e3">hipsparselt.h</a>
</li>
<li>hipsparseLtPruneAlg_t
: <a class="el" href="group__types__module.html#gacbdbf2fd179cd61f918dc6f7eb2eca5d">hipsparselt.h</a>
</li>
<li>hipsparseLtSparsity_t
: <a class="el" href="group__types__module.html#ga1a34328c8f8454db5da99f841b140274">hipsparselt.h</a>
</li>
<li>hipsparseLtSplitKMode_t
: <a class="el" href="group__types__module.html#ga97a3db1aa6b2f60fbad1f2843bf39574">hipsparselt.h</a>
</li>
<li>hipsparseLtSpMMACompress()
: <a class="el" href="group__helper__module.html#ga982409bdcd64904075904c6e53a2fb16">hipsparselt.h</a>
</li>
<li>hipsparseLtSpMMACompress2()
: <a class="el" href="group__helper__module.html#ga6be234117bca933336b6cc1310e6df43">hipsparselt.h</a>
</li>
<li>hipsparseLtSpMMACompressedSize()
: <a class="el" href="group__helper__module.html#ga969a53651ac49ebfe6091ae93a14ec48">hipsparselt.h</a>
</li>
<li>hipsparseLtSpMMACompressedSize2()
: <a class="el" href="group__helper__module.html#ga265c5991ca7d972ce7d654463267fb62">hipsparselt.h</a>
</li>
<li>hipsparseLtSpMMAPrune()
: <a class="el" href="group__helper__module.html#ga8bbedf41f453e00dbe00d25229afbb19">hipsparselt.h</a>
</li>
<li>hipsparseLtSpMMAPrune2()
: <a class="el" href="group__helper__module.html#ga1af0fe3dac7cb17f5434a6a57afde58a">hipsparselt.h</a>
</li>
<li>hipsparseLtSpMMAPruneCheck()
: <a class="el" href="group__helper__module.html#gaf05eb5a9a8cb4e6c17cc096651dacdd8">hipsparselt.h</a>
</li>
<li>hipsparseLtSpMMAPruneCheck2()
: <a class="el" href="group__helper__module.html#ga700af5ff039e248c11143a37906be366">hipsparselt.h</a>
</li>
<li>hipsparseLtStructuredDescriptorInit()
: <a class="el" href="group__matrix__desc__module.html#ga468214d4d018a36e5e9bda1882a3df4a">hipsparselt.h</a>
</li>
</ul>
</div><!-- contents -->
<!-- HTML footer for doxygen 1.9.6-->
<!-- start footer part -->
<!--BEGIN GENERATE_TREEVIEW-->
</body>
</html>
</div>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="globals_globals.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Globals</p>
      </div>
    </a>
    <a class="right-next"
       href="globals_func.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Globals</p>
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
  <script defer src="../../_static/scripts/bootstrap.js?digest=8878045cc6db502f8baf"></script>
<script defer src="../../_static/scripts/pydata-sphinx-theme.js?digest=8878045cc6db502f8baf"></script>

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
    <img id="rdc-watermark" src="../../_static/images/alpha-watermark.svg" alt="DRAFT watermark"/>
</div> -->
  </body>
</html>
