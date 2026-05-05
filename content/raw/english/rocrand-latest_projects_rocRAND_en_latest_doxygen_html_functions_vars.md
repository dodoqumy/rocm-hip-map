---
title: "API library: Class Members - Variables &#8212; rocRAND 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocRAND/en/latest/doxygen/html/functions_vars.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:09:12.835043+00:00
content_hash: "5b280ef29571d89f"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>API library: Class Members - Variables &#8212; rocRAND 4.2.0 Documentation</title>
  
  
  
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
    <script src="../../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/html/functions_vars';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="Class Members - Typedefs" href="functions_type.html" />
    <link rel="prev" title="Class Members - Functions" href="functions_func_~.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocrand" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/functions_vars.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1"><a class="reference internal" href="../../install/installing.html">Installation guide</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../conceptual/programmers-guide.html">Programming guide</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../conceptual/curand-compatibility.html">cuRAND compatibility</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../conceptual/dynamic_ordering_configuration.html">Kernel configurations for dynamic ordering</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../conceptual/generator-types.html">Random number generators</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Examples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocrand/python/rocrand/examples">Examples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">API reference</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../api-reference/data-type-support.html">rocRAND data type support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../api-reference/cpp-api.html">C/C++ API reference</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../api-reference/python-api.html">Python API reference</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../fortran-api-reference.html">Fortran API reference</a></li>
<li class="toctree-l1 current active has-children"><a class="reference internal" href="index.html">API library</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2"><a class="reference internal" href="modules.html">Modules</a></li>
<li class="toctree-l2 current active has-children"><a class="reference internal" href="annotated_classes.html">Classes</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l3"><a class="reference internal" href="annotated.html">Class List</a></li>
<li class="toctree-l3"><a class="reference internal" href="hierarchy.html">Class Hierarchy</a></li>
<li class="toctree-l3 current active has-children"><a class="reference internal" href="functions_class_members.html">Class Members</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l4"><a class="reference internal" href="functions_all.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_func_functions.html">Functions</a></li>
<li class="toctree-l4 current active"><a class="current reference internal" href="#">Variables</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_type.html">Typedefs</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_rela.html">Related Functions</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="files.html">Files</a></li>
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
    
    <li class="breadcrumb-item"><a href="index.html" class="nav-link">API library</a></li>
    
    
    <li class="breadcrumb-item"><a href="annotated_classes.html" class="nav-link">Classes</a></li>
    
    
    <li class="breadcrumb-item"><a href="functions_class_members.html" class="nav-link">Class Members</a></li>
    
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">API library: Class Members - Variables</span></li>
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
    <h1>Class Members - Variables</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="class-members-variables">
<h1>Class Members - Variables<a class="headerlink" href="#class-members-variables" title="Link to this heading">#</a></h1>
<div class="doxygen-content docutils container">
<!-- HTML header for doxygen 1.9.6-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="$langISO">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.1"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>API library: Class Members - Variables</title>
<link href="tabs.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="dynsections.js"></script>
<link href="stylesheet.css" rel="stylesheet" type="text/css" />
<link href="extra_stylesheet.css" rel="stylesheet" type="text/css"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocrand" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/functions_vars.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
&#160;<ul>
<li>alias
: <a class="el" href="structrocrand__discrete__distribution__st.html#a08b200fe998759268d810abbcef90a9c">rocrand_discrete_distribution_st</a>
</li>
<li>cdf
: <a class="el" href="structrocrand__discrete__distribution__st.html#a4204272a7723dcbe515451c024eab669">rocrand_discrete_distribution_st</a>
</li>
<li>default_num_dimensions
: <a class="el" href="classrocrand__cpp_1_1scrambled__sobol32__engine.html#aa183d264f2084d6eef83083f05f84838">rocrand_cpp::scrambled_sobol32_engine&lt; DefaultNumDimensions &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1scrambled__sobol64__engine.html#a77b052e927386181e94669aa93684eaf">rocrand_cpp::scrambled_sobol64_engine&lt; DefaultNumDimensions &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1sobol32__engine.html#ac9f4075aa758267d7bddaee1e2537f7d">rocrand_cpp::sobol32_engine&lt; DefaultNumDimensions &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1sobol64__engine.html#a7a3156f799bd1718b99f824d5cfaa2c6">rocrand_cpp::sobol64_engine&lt; DefaultNumDimensions &gt;</a>
</li>
<li>default_seed
: <a class="el" href="classrocrand__cpp_1_1lfsr113__engine.html#a778b9191d41139f8d8183b1c0210b359">rocrand_cpp::lfsr113_engine&lt; DefaultSeedX, DefaultSeedY, DefaultSeedZ, DefaultSeedW &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1mrg31k3p__engine.html#a61fc847f3d5835343e50bfee60c371fb">rocrand_cpp::mrg31k3p_engine&lt; DefaultSeed &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1mrg32k3a__engine.html#a8968a1f82defaf26eeaae16b17459b5d">rocrand_cpp::mrg32k3a_engine&lt; DefaultSeed &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1mt19937__engine.html#aeafe28ce6a1dba9aa43a1d721b8dd0e7">rocrand_cpp::mt19937_engine&lt; DefaultSeed &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1mtgp32__engine.html#a937c15a3de6c1b0ed1794337473090dd">rocrand_cpp::mtgp32_engine&lt; DefaultSeed &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1philox4x32__10__engine.html#a12df42f9d43a7c34f36fd34717413961">rocrand_cpp::philox4x32_10_engine&lt; DefaultSeed &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1threefry2x32__20__engine.html#ab64762a727ac7701a7dbfcaf31b35dc3">rocrand_cpp::threefry2x32_20_engine&lt; DefaultSeed &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1threefry2x64__20__engine.html#a1c38bbb4da54e23efe9ebced9fb4ceb8">rocrand_cpp::threefry2x64_20_engine&lt; DefaultSeed &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1threefry4x32__20__engine.html#adb3ee4a59a7c97701ee39893cd87b320">rocrand_cpp::threefry4x32_20_engine&lt; DefaultSeed &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1threefry4x64__20__engine.html#a3e1e6ea634df52ef41132309a78ebe6a">rocrand_cpp::threefry4x64_20_engine&lt; DefaultSeed &gt;</a>
, <a class="el" href="classrocrand__cpp_1_1xorwow__engine.html#acc333dc181a70af7b5572988d7c9a2ac">rocrand_cpp::xorwow_engine&lt; DefaultSeed &gt;</a>
</li>
<li>flt_tmp_tbl
: <a class="el" href="structmtgp32__params__fast__t.html#acf6032845969cd69195b797adeb4c901">mtgp32_params_fast_t</a>
</li>
<li>mask
: <a class="el" href="structmtgp32__params__fast__t.html#a8d630ac4c50518932098adc58eaead8a">mtgp32_params_fast_t</a>
</li>
<li>mexp
: <a class="el" href="structmtgp32__params__fast__t.html#a2c4be5532efdca6a9650c1460b20dcd7">mtgp32_params_fast_t</a>
</li>
<li>offset
: <a class="el" href="structrocrand__discrete__distribution__st.html#ae4907493e0c93e46ddf3399451c82607">rocrand_discrete_distribution_st</a>
</li>
<li>poly_sha1
: <a class="el" href="structmtgp32__params__fast__t.html#a8e08f5b175887f09749145c724eb9bc2">mtgp32_params_fast_t</a>
</li>
<li>pos
: <a class="el" href="structmtgp32__params__fast__t.html#a25cdbfed1da9d2c429698f51f1cd1108">mtgp32_params_fast_t</a>
</li>
<li>probability
: <a class="el" href="structrocrand__discrete__distribution__st.html#a4eb8401e1eea397b493c6b19238dfa14">rocrand_discrete_distribution_st</a>
</li>
<li>sh1
: <a class="el" href="structmtgp32__params__fast__t.html#a7c30035713da02c6218f126875bcbaf0">mtgp32_params_fast_t</a>
</li>
<li>sh2
: <a class="el" href="structmtgp32__params__fast__t.html#a54e1d077b1a23eece387c89f4ce3604d">mtgp32_params_fast_t</a>
</li>
<li>size
: <a class="el" href="structrocrand__discrete__distribution__st.html#a018cf62245131b0c8f2525340b6b8580">rocrand_discrete_distribution_st</a>
</li>
<li>tbl
: <a class="el" href="structmtgp32__params__fast__t.html#a92d39b1a02d03834b74c47a68e80ce37">mtgp32_params_fast_t</a>
</li>
<li>tmp_tbl
: <a class="el" href="structmtgp32__params__fast__t.html#a03e17b91b1f02b7e337574fa797a40ee">mtgp32_params_fast_t</a>
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
       href="functions_func_~.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Class Members - Functions</p>
      </div>
    </a>
    <a class="right-next"
       href="functions_type.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Class Members - Typedefs</p>
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
