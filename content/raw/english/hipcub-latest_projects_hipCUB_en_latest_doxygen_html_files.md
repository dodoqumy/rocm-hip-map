---
title: "hipCUB: File List &#8212; hipCUB 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipCUB/en/latest/doxygen/html/files.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:18:51.517037+00:00
content_hash: "5b128b82f7de6a54"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>hipCUB: File List &#8212; hipCUB 4.2.0 Documentation</title>
  
  
  
  <script data-cfasync="false">
    document.documentElement.dataset.mode = localStorage.getItem("mode") || "";
    document.documentElement.dataset.theme = localStorage.getItem("theme") || "";
  </script>
  
  <!-- Loaded before other Sphinx assets -->
  <link href="../../_static/styles/theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../../_static/styles/bootstrap.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../../_static/styles/pydata-sphinx-theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />

  
  <link href="../../_static/vendor/fontawesome/6.5.2/css/all.min.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
  <link rel="preload" as="font" type="font/woff2" crossorigin href="../../_static/vendor/fontawesome/6.5.2/webfonts/fa-solid-900.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../_static/vendor/fontawesome/6.5.2/webfonts/fa-brands-400.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../_static/vendor/fontawesome/6.5.2/webfonts/fa-regular-400.woff2" />

    <link rel="stylesheet" type="text/css" href="../../_static/pygments.css?v=a746c00c" />
    <link rel="stylesheet" type="text/css" href="../../_static/styles/sphinx-book-theme.css?v=384b581d" />
    <link rel="stylesheet" type="text/css" href="../../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
    <link rel="stylesheet" type="text/css" href="../../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../../_static/design-style.1e8bd061cd6da7fc9cf755528e8ffc24.min.css?v=0a3b3ea7" />
  
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b" />
<link rel="preload" as="script" href="../../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b" />
  <script src="../../_static/vendor/fontawesome/6.5.2/js/all.min.js?digest=dfe6caa3a7d634c4db9b"></script>

    <script src="../../_static/documentation_options.js?v=830d3dd9"></script>
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
    <script src="../../_static/design-tabs.js?v=36754332"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/html/files';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="License" href="../../license.html" />
    <link rel="prev" title="Namespace Members" href="namespacemembers_func.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hipcub" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/files.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
  <body data-bs-spy="scroll" data-bs-target=".bd-toc-nav" data-offset="180" data-bs-root-margin="0px 0px -60%" data-default-mode="">

  
  
  <div id="pst-skip-link" class="skip-link d-print-none"><a href="#main-content">Skip to main content</a></div>
  
  <div id="pst-scroll-pixel-helper"></div>
  
  <button type="button" class="btn rounded-pill" id="pst-back-to-top">
    <i class="fa-solid fa-arrow-up"></i>Back to top</button>

  
  <input type="checkbox"
          class="sidebar-toggle"
          id="pst-primary-sidebar-checkbox"/>
  <label class="overlay overlay-primary" for="pst-primary-sidebar-checkbox"></label>
  
  <input type="checkbox"
          class="sidebar-toggle"
          id="pst-secondary-sidebar-checkbox"/>
  <label class="overlay overlay-secondary" for="pst-secondary-sidebar-checkbox"></label>
  
  <div class="search-button__wrapper">
    <div class="search-button__overlay"></div>
    <div class="search-button__search-container">
<form class="bd-search d-flex align-items-center"
      action="../../search.html"
      method="get">
  <i class="fa-solid fa-magnifying-glass"></i>
  <input type="search"
         class="form-control"
         name="q"
         id="search-input"
         placeholder="Search..."
         aria-label="Search..."
         autocomplete="off"
         autocorrect="off"
         autocapitalize="off"
         spellcheck="false"/>
  <span class="search-button__kbd-shortcut"><kbd class="kbd-shortcut__modifier">Ctrl</kbd>+<kbd>K</kbd></span>
</form></div>
  </div>

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
      
      
      
      <div class="bd-sidebar-primary bd-sidebar">
        

  
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
  
  
  
  
  
  
    <p class="title logo__title">hipCUB 4.2.0 Documentation</p>
  
</a></div>
        <div class="sidebar-primary-item">

 <script>
 document.write(`
   <button class="btn search-button-field search-button__button" title="Search" aria-label="Search" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <i class="fa-solid fa-magnifying-glass"></i>
    <span class="search-button__default-text">Search</span>
    <span class="search-button__kbd-shortcut"><kbd class="kbd-shortcut__modifier">Ctrl</kbd>+<kbd class="kbd-shortcut__modifier">K</kbd></span>
   </button>
 `);
 </script></div>
        <div class="sidebar-primary-item"><nav class="bd-links bd-docs-nav" aria-label="Main">
    <div class="bd-toc-item navbar-nav active">
        <p aria-level="2" class="caption" role="heading"><span class="caption-text">Installation</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../install/hipCUB-prerequisites.html">Installation prerequisites</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../install/hipCUB-install-overview.html">Installation overview</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../install/hipCUB-install-on-Windows.html">Installing on Windows</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../install/hipCUB-install-with-cmake.html">Installing on Linux and Windows with CMake</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active has-children"><a class="reference internal" href="index.html">API library</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2 has-children"><a class="reference internal" href="namespaces_namespaces.html">Namespaces</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="namespaces.html">Namespace List</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="namespacemembers_namespace_members.html">Namespace Members</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="namespacemembers.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="namespacemembers_func.html">Functions</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2 current active"><a class="current reference internal" href="#">Files</a></li>
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
  </div>
  
  <div id="rtd-footer-container"></div>


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
    
    <li class="breadcrumb-item"><a href="index.html" class="nav-link">hipCUB</a></li>
    
    <li class="breadcrumb-item active" aria-current="page">hipCUB: File List</li>
  </ul>
</nav>
</div>
      
    </div>
  
  
    <div class="header-article-items__end">
      
        <div class="header-article-item">

<div class="article-header-buttons">


<script>
document.write(`
  <button class="btn btn-sm nav-link pst-navbar-icon theme-switch-button" title="light/dark" aria-label="light/dark" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <i class="theme-switch fa-solid fa-sun fa-lg" data-mode="light"></i>
    <i class="theme-switch fa-solid fa-moon fa-lg" data-mode="dark"></i>
    <i class="theme-switch fa-solid fa-circle-half-stroke fa-lg" data-mode="auto"></i>
  </button>
`);
</script>


<script>
document.write(`
  <button class="btn btn-sm pst-navbar-icon search-button search-button__button" title="Search" aria-label="Search" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <i class="fa-solid fa-magnifying-glass fa-lg"></i>
  </button>
`);
</script>

</div></div>
      
    </div>
  
</div>
</div>
              
              

<div id="jb-print-docs-body" class="onlyprint">
    <h1>File List</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="file-list">
<h1>File List<a class="headerlink" href="#file-list" title="Link to this heading">#</a></h1>
<div class="doxygen-content docutils container">
<!-- HTML header for doxygen 1.9.6-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="$langISO">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.1"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>hipCUB: File List</title>
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
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hipcub" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/files.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
<div class="header">
  <div class="headertitle">
<div class="title">File List</div>  </div>
</div><!--header-->
<div class="contents">
<div class="textblock">Here is a list of all documented files with brief descriptions:</div><div class="directory">
<div class="levels">[detail level <span onclick="javascript:toggleLevel(1);">1</span><span onclick="javascript:toggleLevel(2);">2</span><span onclick="javascript:toggleLevel(3);">3</span>]</div><table class="directory">
<tr id="row_0_" class="even"><td class="entry"><span style="width:0px;display:inline-block;">&#160;</span><span id="arr_0_" class="arrow" onclick="toggleFolder('0_')">&#9660;</span><span id="img_0_" class="iconfopen" onclick="toggleFolder('0_')">&#160;</span><a class="el" href="dir_c2e03ffbc44d09593608bae5167a5d77.html" target="_self">hipcub</a></td><td class="desc"></td></tr>
<tr id="row_0_0_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span id="arr_0_0_" class="arrow" onclick="toggleFolder('0_0_')">&#9660;</span><span id="img_0_0_" class="iconfopen" onclick="toggleFolder('0_0_')">&#160;</span><a class="el" href="dir_c790359788194b78e733bb602c616450.html" target="_self">agent</a></td><td class="desc"></td></tr>
<tr id="row_0_0_0_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="single__pass__scan__operators_8hpp_source.html"><span class="icondoc"></span></a><b>single_pass_scan_operators.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span id="arr_0_1_" class="arrow" onclick="toggleFolder('0_1_')">&#9660;</span><span id="img_0_1_" class="iconfopen" onclick="toggleFolder('0_1_')">&#160;</span><a class="el" href="dir_1297cde55068466a76ed7707471a42a2.html" target="_self">block</a></td><td class="desc"></td></tr>
<tr id="row_0_1_0_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__adjacent__difference_8hpp_source.html"><span class="icondoc"></span></a><b>block_adjacent_difference.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_1_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__discontinuity_8hpp_source.html"><span class="icondoc"></span></a><b>block_discontinuity.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_2_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__exchange_8hpp_source.html"><span class="icondoc"></span></a><b>block_exchange.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_3_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__histogram_8hpp_source.html"><span class="icondoc"></span></a><b>block_histogram.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_4_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__load_8hpp_source.html"><span class="icondoc"></span></a><b>block_load.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_5_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__merge__sort_8hpp_source.html"><span class="icondoc"></span></a><b>block_merge_sort.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_6_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__radix__rank_8hpp_source.html"><span class="icondoc"></span></a><b>block_radix_rank.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_7_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__radix__sort_8hpp_source.html"><span class="icondoc"></span></a><b>block_radix_sort.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_8_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__raking__layout_8hpp_source.html"><span class="icondoc"></span></a><b>block_raking_layout.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_9_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__reduce_8hpp_source.html"><span class="icondoc"></span></a><b>block_reduce.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_10_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__run__length__decode_8hpp_source.html"><span class="icondoc"></span></a><b>block_run_length_decode.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_11_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__scan_8hpp_source.html"><span class="icondoc"></span></a><b>block_scan.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_12_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__shuffle_8hpp_source.html"><span class="icondoc"></span></a><b>block_shuffle.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_13_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="block__store_8hpp_source.html"><span class="icondoc"></span></a><b>block_store.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_1_14_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="radix__rank__sort__operations_8hpp_source.html"><span class="icondoc"></span></a><b>radix_rank_sort_operations.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span id="arr_0_2_" class="arrow" onclick="toggleFolder('0_2_')">&#9660;</span><span id="img_0_2_" class="iconfopen" onclick="toggleFolder('0_2_')">&#160;</span><a class="el" href="dir_c2574c4295834f48fb719536be8b8d17.html" target="_self">device</a></td><td class="desc"></td></tr>
<tr id="row_0_2_0_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__adjacent__difference_8hpp_source.html"><span class="icondoc"></span></a><b>device_adjacent_difference.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_1_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__copy_8hpp_source.html"><span class="icondoc"></span></a><b>device_copy.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_2_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__for_8hpp_source.html"><span class="icondoc"></span></a><b>device_for.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_3_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__histogram_8hpp_source.html"><span class="icondoc"></span></a><b>device_histogram.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_4_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__memcpy_8hpp_source.html"><span class="icondoc"></span></a><b>device_memcpy.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_5_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__merge_8hpp_source.html"><span class="icondoc"></span></a><b>device_merge.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_6_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__merge__sort_8hpp_source.html"><span class="icondoc"></span></a><b>device_merge_sort.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_7_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__partition_8hpp_source.html"><span class="icondoc"></span></a><b>device_partition.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_8_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__radix__sort_8hpp_source.html"><span class="icondoc"></span></a><b>device_radix_sort.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_9_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__reduce_8hpp_source.html"><span class="icondoc"></span></a><b>device_reduce.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_10_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__run__length__encode_8hpp_source.html"><span class="icondoc"></span></a><b>device_run_length_encode.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_11_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__scan_8hpp_source.html"><span class="icondoc"></span></a><b>device_scan.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_12_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__segmented__radix__sort_8hpp_source.html"><span class="icondoc"></span></a><b>device_segmented_radix_sort.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_13_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__segmented__reduce_8hpp_source.html"><span class="icondoc"></span></a><b>device_segmented_reduce.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_14_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__segmented__sort_8hpp_source.html"><span class="icondoc"></span></a><b>device_segmented_sort.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_15_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__select_8hpp_source.html"><span class="icondoc"></span></a><b>device_select.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_16_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__spmv_8hpp_source.html"><span class="icondoc"></span></a><b>device_spmv.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_2_17_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="device__transform_8hpp_source.html"><span class="icondoc"></span></a><b>device_transform.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_3_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span id="arr_0_3_" class="arrow" onclick="toggleFolder('0_3_')">&#9660;</span><span id="img_0_3_" class="iconfopen" onclick="toggleFolder('0_3_')">&#160;</span><a class="el" href="dir_cea5c3558a9a6aa34aecd6fb72032a9c.html" target="_self">grid</a></td><td class="desc"></td></tr>
<tr id="row_0_3_0_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="grid__barrier_8hpp_source.html"><span class="icondoc"></span></a><b>grid_barrier.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_3_1_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="grid__even__share_8hpp_source.html"><span class="icondoc"></span></a><b>grid_even_share.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_3_2_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="grid__mapping_8hpp_source.html"><span class="icondoc"></span></a><b>grid_mapping.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_3_3_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="grid__queue_8hpp_source.html"><span class="icondoc"></span></a><b>grid_queue.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_4_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span id="arr_0_4_" class="arrow" onclick="toggleFolder('0_4_')">&#9660;</span><span id="img_0_4_" class="iconfopen" onclick="toggleFolder('0_4_')">&#160;</span><a class="el" href="dir_d93e8a4c98792bed435b0071c686442f.html" target="_self">iterator</a></td><td class="desc"></td></tr>
<tr id="row_0_4_0_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="arg__index__input__iterator_8hpp_source.html"><span class="icondoc"></span></a><b>arg_index_input_iterator.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_4_1_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="cache__modified__input__iterator_8hpp_source.html"><span class="icondoc"></span></a><b>cache_modified_input_iterator.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_4_2_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="cache__modified__output__iterator_8hpp_source.html"><span class="icondoc"></span></a><b>cache_modified_output_iterator.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_4_3_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="constant__input__iterator_8hpp_source.html"><span class="icondoc"></span></a><b>constant_input_iterator.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_4_4_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="counting__input__iterator_8hpp_source.html"><span class="icondoc"></span></a><b>counting_input_iterator.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_4_5_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="discard__output__iterator_8hpp_source.html"><span class="icondoc"></span></a><b>discard_output_iterator.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_4_6_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="tex__obj__input__iterator_8hpp_source.html"><span class="icondoc"></span></a><b>tex_obj_input_iterator.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_4_7_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="transform__input__iterator_8hpp_source.html"><span class="icondoc"></span></a><b>transform_input_iterator.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_5_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span id="arr_0_5_" class="arrow" onclick="toggleFolder('0_5_')">&#9660;</span><span id="img_0_5_" class="iconfopen" onclick="toggleFolder('0_5_')">&#160;</span><a class="el" href="dir_5e363f5965424fee92f20ee140ec3373.html" target="_self">thread</a></td><td class="desc"></td></tr>
<tr id="row_0_5_0_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="thread__load_8hpp_source.html"><span class="icondoc"></span></a><b>thread_load.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_5_1_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="thread__operators_8hpp_source.html"><span class="icondoc"></span></a><b>thread_operators.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_5_2_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="thread__reduce_8hpp_source.html"><span class="icondoc"></span></a><b>thread_reduce.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_5_3_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="thread__scan_8hpp_source.html"><span class="icondoc"></span></a><a class="el" href="thread__scan_8hpp.html" target="_self">thread_scan.hpp</a></td><td class="desc"></td></tr>
<tr id="row_0_5_4_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="thread__search_8hpp_source.html"><span class="icondoc"></span></a><a class="el" href="thread__search_8hpp.html" target="_self">thread_search.hpp</a></td><td class="desc"></td></tr>
<tr id="row_0_5_5_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="thread__sort_8hpp_source.html"><span class="icondoc"></span></a><b>thread_sort.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_5_6_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="thread__store_8hpp_source.html"><span class="icondoc"></span></a><b>thread_store.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_6_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span id="arr_0_6_" class="arrow" onclick="toggleFolder('0_6_')">&#9660;</span><span id="img_0_6_" class="iconfopen" onclick="toggleFolder('0_6_')">&#160;</span><a class="el" href="dir_f472c4f9425807e24daf8885351b1c3c.html" target="_self">warp</a></td><td class="desc"></td></tr>
<tr id="row_0_6_0_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="warp__exchange_8hpp_source.html"><span class="icondoc"></span></a><b>warp_exchange.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_6_1_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="warp__load_8hpp_source.html"><span class="icondoc"></span></a><b>warp_load.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_6_2_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="warp__merge__sort_8hpp_source.html"><span class="icondoc"></span></a><b>warp_merge_sort.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_6_3_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="warp__reduce_8hpp_source.html"><span class="icondoc"></span></a><b>warp_reduce.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_6_4_"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="warp__scan_8hpp_source.html"><span class="icondoc"></span></a><b>warp_scan.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_6_5_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><a href="warp__store_8hpp_source.html"><span class="icondoc"></span></a><b>warp_store.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_7_"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><a href="config_8hpp_source.html"><span class="icondoc"></span></a><b>config.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_8_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><a href="hipcub_8hpp_source.html"><span class="icondoc"></span></a><a class="el" href="hipcub_8hpp.html" target="_self">hipcub.hpp</a></td><td class="desc"></td></tr>
<tr id="row_0_9_"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><a href="tuple_8hpp_source.html"><span class="icondoc"></span></a><b>tuple.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_10_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><a href="util__allocator_8hpp_source.html"><span class="icondoc"></span></a><b>util_allocator.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_11_"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><a href="util__deprecated_8hpp_source.html"><span class="icondoc"></span></a><b>util_deprecated.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_12_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><a href="util__device_8hpp_source.html"><span class="icondoc"></span></a><b>util_device.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_13_"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><a href="util__macro_8hpp_source.html"><span class="icondoc"></span></a><b>util_macro.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_14_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><a href="util__ptx_8hpp_source.html"><span class="icondoc"></span></a><b>util_ptx.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_15_"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><a href="util__temporary__storage_8hpp_source.html"><span class="icondoc"></span></a><b>util_temporary_storage.hpp</b></td><td class="desc"></td></tr>
<tr id="row_0_16_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><a href="util__type_8hpp_source.html"><span class="icondoc"></span></a><b>util_type.hpp</b></td><td class="desc"></td></tr>
</table>
</div><!-- directory -->
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
       href="namespacemembers_func.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Namespace Members</p>
      </div>
    </a>
    <a class="right-next"
       href="../../license.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">License</p>
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
  <script src="../../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b"></script>
<script src="../../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b"></script>

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
