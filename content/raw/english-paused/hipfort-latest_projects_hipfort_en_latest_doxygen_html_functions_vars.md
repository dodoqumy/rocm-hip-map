---
title: "HIPFORT API Reference: Data Fields - Variables &#8212; hipfort 0.7.1 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipfort/en/latest/doxygen/html/functions_vars.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:30:42.152375+00:00
content_hash: "dc878fcc828d4ba0"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>HIPFORT API Reference: Data Fields - Variables &#8212; hipfort 0.7.1 Documentation</title>
  
  
  
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

    <link rel="stylesheet" type="text/css" href="../../_static/pygments.css?v=a746c00c" />
    <link rel="stylesheet" type="text/css" href="../../_static/styles/sphinx-book-theme.css?v=384b581d" />
    <link rel="stylesheet" type="text/css" href="../../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
    <link rel="stylesheet" type="text/css" href="../../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../../_static/sphinx-design.min.css?v=87e54e7c" />
  
  <!-- So that users can add custom icons -->
  <script src="../../_static/scripts/fontawesome.js?digest=8878045cc6db502f8baf"></script>
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../../_static/scripts/bootstrap.js?digest=8878045cc6db502f8baf" />
<link rel="preload" as="script" href="../../_static/scripts/pydata-sphinx-theme.js?digest=8878045cc6db502f8baf" />

    <script src="../../_static/documentation_options.js?v=7dd04bbd"></script>
    <script src="../../_static/doctools.js?v=9a2dae69"></script>
    <script src="../../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../../_static/search.js?v=90a4452c"></script>
    <script src="../../_static/scripts/sphinx-book-theme.js?v=efea14e4"></script>
    <script src="../../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/html/functions_vars';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="File List" href="files.html" />
    <link rel="prev" title="Data Fields - Functions/Subroutines" href="functions_func_r.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hipfort" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/functions_vars.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/hipfort" id="navgithub" role="button" aria-expanded="false" target="_blank" >
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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/hipfort/issues/new/choose" id="navsupport" role="button" aria-expanded="false" target="_blank" >
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
  
  
  
  
  
  
    <p class="title logo__title">hipfort 0.7.1 Documentation</p>
  
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
<li class="toctree-l1"><a class="reference internal" href="../../install/quick-start.html">Quick start installation guide</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../install/install.html">Detailed install</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../how-to/using-hipfort.html">Use hipFORT</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Tutorials</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../tutorials/examples.html">Examples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">API reference</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active has-children"><a class="reference internal" href="index.html">hipFORT API reference</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2"><a class="reference internal" href="pages.html">Related Pages</a></li>
<li class="toctree-l2"><a class="reference internal" href="modules.html">Modules</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="namespaces_modules.html">Modules</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="namespaces.html">Modules List</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="namespacemembers_module_members.html">Module Members</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="namespacemembers_all.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="namespacemembers_func_functions_subroutines.html">Functions/Subroutines</a></li>
<li class="toctree-l4"><a class="reference internal" href="namespacemembers_vars.html">Variables</a></li>
<li class="toctree-l4"><a class="reference internal" href="namespacemembers_eval_enumerator.html">Enumerator</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2 current active has-children"><a class="reference internal" href="annotated_data_types_list.html">Data Types List</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l3"><a class="reference internal" href="annotated.html">Data Types List</a></li>
<li class="toctree-l3"><a class="reference internal" href="classes.html">Data Types</a></li>
<li class="toctree-l3 current active has-children"><a class="reference internal" href="functions_data_fields.html">Data Fields</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l4"><a class="reference internal" href="functions_all.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_func_functions_subroutines.html">Functions/Subroutines</a></li>
<li class="toctree-l4 current active"><a class="current reference internal" href="#">Variables</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="files.html">Files</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/index.html">Supported APIs</a></li>
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
    
    <li class="breadcrumb-item"><a href="index.html" class="nav-link">HIPFORT API Reference</a></li>
    
    
    <li class="breadcrumb-item"><a href="annotated_data_types_list.html" class="nav-link">Data Types List</a></li>
    
    
    <li class="breadcrumb-item"><a href="functions_data_fields.html" class="nav-link">Data Fields</a></li>
    
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">HIPFORT API Reference: Data Fields - Variables</span></li>
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
<html xmlns="http://www.w3.org/1999/xhtml" lang="$langISO">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.1"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>HIPFORT API Reference: Data Fields - Variables</title>
<link href="tabs.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="dynsections.js"></script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    extensions: ["tex2jax.js"],
    jax: ["input/TeX","output/HTML-CSS"],
});
</script>
<script type="text/javascript" async="async" src="https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js"></script>
<link href="stylesheet.css" rel="stylesheet" type="text/css" />
<link href="extra_stylesheet.css" rel="stylesheet" type="text/css"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hipfort" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/functions_vars.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
&#160;

<h3><a id="index_a"></a>- a -</h3><ul>
<li>arch
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#ad8016d109276da0d51a5ab811bb8953c">hipfort_types::hipdeviceprop_t</a>
</li>
<li>asicrevision
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#add04bce05bd9ec1db4dafcab0fe8da80">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_c"></a>- c -</h3><ul>
<li>canmaphostmemory
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a2b5203f41c37d539eca93e255233bfc1">hipfort_types::hipdeviceprop_t</a>
</li>
<li>clockinstructionrate
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a740c21d34e878021386b824f406a7049">hipfort_types::hipdeviceprop_t</a>
</li>
<li>clockrate
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#aa5a8ebb91638cb24596880c85758e853">hipfort_types::hipdeviceprop_t</a>
</li>
<li>computemode
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#ade8406a9eed3860f69a016041c8d7183">hipfort_types::hipdeviceprop_t</a>
</li>
<li>concurrentkernels
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a123cffabf0f191e22036904df60e855e">hipfort_types::hipdeviceprop_t</a>
</li>
<li>concurrentmanagedaccess
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a191cc55c8c2d9198ff9027011ac9eeaa">hipfort_types::hipdeviceprop_t</a>
</li>
<li>cooperativelaunch
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#aa838925e684788191a94278c30d775ac">hipfort_types::hipdeviceprop_t</a>
</li>
<li>cooperativemultidevicelaunch
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#ab478c99cbe7f92d28734c209ffd0af37">hipfort_types::hipdeviceprop_t</a>
</li>
<li>cooperativemultideviceunmatchedblockdim
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#ad4b86d69a07d9e68c3b7053e7637024e">hipfort_types::hipdeviceprop_t</a>
</li>
<li>cooperativemultideviceunmatchedfunc
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#aa388d5f3e8548fadb963008999aa4a9a">hipfort_types::hipdeviceprop_t</a>
</li>
<li>cooperativemultideviceunmatchedgriddim
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a34bed2290b51719eebdca2e4d3dec09d">hipfort_types::hipdeviceprop_t</a>
</li>
<li>cooperativemultideviceunmatchedsharedmem
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#ab6e13e942555805ff90f2a42d4ce3d84">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_d"></a>- d -</h3><ul>
<li>directmanagedmemaccessfromhost
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a8c3d8e91e11aa2ef7daba6e7a1e9b0a6">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_e"></a>- e -</h3><ul>
<li>eccenabled
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#acb2d9e80308b3284c7b9df4170bf9d0a">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_g"></a>- g -</h3><ul>
<li>gcnarch
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a481b2a70d53194c0bb6236737433009f">hipfort_types::hipdeviceprop_t</a>
</li>
<li>gcnarchname
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a23abcba259f66dd397fef1f162756cec">hipfort_types::hipdeviceprop_t</a>
</li>
<li>gpufort_padding
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#ad99767af0541be5d3ded40fcbad3bdcd">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_h"></a>- h -</h3><ul>
<li>hdpmemflushcntl
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#aac78bc03ebdaff547d391575eb4f3b2f">hipfort_types::hipdeviceprop_t</a>
</li>
<li>hdpregflushcntl
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a7e6ed97b88d21c87ba9176571d7d965b">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_i"></a>- i -</h3><ul>
<li>integrated
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a031c11bf8ac89ed14b093d18101bd55e">hipfort_types::hipdeviceprop_t</a>
</li>
<li>islargebar
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a390f68679b907966a4466744215876bf">hipfort_types::hipdeviceprop_t</a>
</li>
<li>ismultigpuboard
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#ad8d62328ffba079383946d81cb35b424">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_k"></a>- k -</h3><ul>
<li>kernelexectimeoutenabled
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#ad25dae0a165bd7505cedd254f5e52c85">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_l"></a>- l -</h3><ul>
<li>l2cachesize
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a8ededa30567154ee8f9e4ed8841e0893">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_m"></a>- m -</h3><ul>
<li>major
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a22d51e8e7b997d2fb1c3cf8288eefdf6">hipfort_types::hipdeviceprop_t</a>
</li>
<li>managedmemory
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#abe6be76ee5185d13c0985e46cc9b1e96">hipfort_types::hipdeviceprop_t</a>
</li>
<li>maxgridsize
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a0165194aefa0026e9560fb6a1f2ad5a9">hipfort_types::hipdeviceprop_t</a>
</li>
<li>maxsharedmemorypermultiprocessor
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a6cb1cac7acf04cfe346a27b86590170a">hipfort_types::hipdeviceprop_t</a>
</li>
<li>maxtexture1d
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a351487d097705ce8d240b5638a62c595">hipfort_types::hipdeviceprop_t</a>
</li>
<li>maxtexture1dlinear
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a01ad5f5fa1e78f5481a4d3d000164d87">hipfort_types::hipdeviceprop_t</a>
</li>
<li>maxtexture2d
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a451b96bbbcbfe72866f2e428e4321b65">hipfort_types::hipdeviceprop_t</a>
</li>
<li>maxtexture3d
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a48ef09658b4af912d1c79ad970cda163">hipfort_types::hipdeviceprop_t</a>
</li>
<li>maxthreadsdim
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#adfc70c668bdd9a2c7810bb5e818a2299">hipfort_types::hipdeviceprop_t</a>
</li>
<li>maxthreadsperblock
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a79acb9c65b8c40e3e3c8b9c5de207a39">hipfort_types::hipdeviceprop_t</a>
</li>
<li>maxthreadspermultiprocessor
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#ac5ed0fd93228700bfd29cd1b16ee7be4">hipfort_types::hipdeviceprop_t</a>
</li>
<li>memorybuswidth
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#af21df0a3ea45f00376d49acc3579a723">hipfort_types::hipdeviceprop_t</a>
</li>
<li>memoryclockrate
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a222b327511c5335396833181cc22d08f">hipfort_types::hipdeviceprop_t</a>
</li>
<li>mempitch
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a8f55653a94d164962af6172e2e965f6a">hipfort_types::hipdeviceprop_t</a>
</li>
<li>minor
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#af5540f0a8f2be9b9a8bc0524808df309">hipfort_types::hipdeviceprop_t</a>
</li>
<li>multiprocessorcount
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a6701411b904d7c296b565ec95fcc4b19">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_n"></a>- n -</h3><ul>
<li>name
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a78f545f2a16d0450ed643631e9b6ffa7">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_p"></a>- p -</h3><ul>
<li>pageablememoryaccess
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#aaa303d0ce1967dad12e9948206d055ce">hipfort_types::hipdeviceprop_t</a>
</li>
<li>pageablememoryaccessuseshostpagetables
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a2e43b5de241f21a7a063455cbc13b4dc">hipfort_types::hipdeviceprop_t</a>
</li>
<li>pcibusid
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#ae57d2e3f883f08a9fd3596b795683c7a">hipfort_types::hipdeviceprop_t</a>
</li>
<li>pcideviceid
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a126e8dee5bdfae3eff69cc7e42815ba8">hipfort_types::hipdeviceprop_t</a>
</li>
<li>pcidomainid
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a619395d9a2970462c419bc255aeafab5">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_r"></a>- r -</h3><ul>
<li>regsperblock
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a9265994bf6ef8737a40f331a2196e87a">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_s"></a>- s -</h3><ul>
<li>sharedmemperblock
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a4bd406072d3d232481310bf796cb7c5d">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_t"></a>- t -</h3><ul>
<li>tccdriver
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a45ecb98ae131b89d0e2ae77d08ac44ab">hipfort_types::hipdeviceprop_t</a>
</li>
<li>texturealignment
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a931b81edb21d6effd3976556330d80b1">hipfort_types::hipdeviceprop_t</a>
</li>
<li>texturepitchalignment
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#aa65f3889b0028ba37f80bd7e33fa9e05">hipfort_types::hipdeviceprop_t</a>
</li>
<li>totalconstmem
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#a700258a31269f820bf588312feb08704">hipfort_types::hipdeviceprop_t</a>
</li>
<li>totalglobalmem
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#abf4676125e6e82e660a1c495fc457d53">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_w"></a>- w -</h3><ul>
<li>warpsize
: <a class="el" href="structhipfort__types_1_1hipdeviceprop__t.html#ada31a8032d0d3eef1296f9fd59342b3f">hipfort_types::hipdeviceprop_t</a>
</li>
</ul>


<h3><a id="index_x"></a>- x -</h3><ul>
<li>x
: <a class="el" href="structhipfort__types_1_1dim3.html#a04d0b480235331d2e636538b40ebaf6d">hipfort_types::dim3</a>
</li>
</ul>


<h3><a id="index_y"></a>- y -</h3><ul>
<li>y
: <a class="el" href="structhipfort__types_1_1dim3.html#af2bffd6cebc93fde63f8c27d7dfc47a7">hipfort_types::dim3</a>
</li>
</ul>


<h3><a id="index_z"></a>- z -</h3><ul>
<li>z
: <a class="el" href="structhipfort__types_1_1dim3.html#a816c9589b285673131481a39131ad696">hipfort_types::dim3</a>
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
       href="functions_func_r.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Data Fields - Functions/Subroutines</p>
      </div>
    </a>
    <a class="right-next"
       href="files.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">File List</p>
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
