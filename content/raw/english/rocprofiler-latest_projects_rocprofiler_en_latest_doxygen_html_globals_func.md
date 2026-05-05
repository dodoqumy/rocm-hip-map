---
title: "ROCProfiler API library: Globals &#8212; ROCProfiler 2.0.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler/en/latest/doxygen/html/globals_func.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:29:10.434822+00:00
content_hash: "75f1ce37c2cb36cb"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>ROCProfiler API library: Globals &#8212; ROCProfiler 2.0.0 Documentation</title>
  
  
  
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
    <link rel="stylesheet" type="text/css" href="../../_static/styles/sphinx-book-theme.css?v=eba8b062" />
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

    <script src="../../_static/documentation_options.js?v=ce394494"></script>
    <script src="../../_static/doctools.js?v=9a2dae69"></script>
    <script src="../../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../../_static/search.js?v=90a4452c"></script>
    <script src="../../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
    <script src="../../_static/design-tabs.js?v=36754332"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/html/globals_func';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="Globals" href="globals_type.html" />
    <link rel="prev" title="Globals" href="globals_r.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-docs" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/globals_func.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<aside class="bd-header-announcement" aria-label="Announcement">
  <div class="bd-header-announcement__content">The ROCm 7.12.0 technology preview release documentation is available at <a id='rocm-banner' href='https://rocm.docs.amd.com/en/7.12.0-preview/'>ROCm Preview documentation</a>. For production use, continue to use ROCm 7.2.2 documentation.</div>
</aside>

  

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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/rocprofiler" id="navgithub" role="button" aria-expanded="false" target="_blank" >
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
                            <a class="nav-link top-level header-menu-links" href="https://instinct.docs.amd.com" id="navsystems-and-infra-docs" role="button" aria-expanded="false" target="_blank" >
                                Systems and Infra Docs
                            </a>
                        </li>
                    
                        <li class="nav-item">
                            <a class="nav-link top-level header-menu-links" href="https://www.amd.com/en/developer/resources/infinity-hub.html" id="navinfinity-hub" role="button" aria-expanded="false" target="_blank" >
                                Infinity Hub
                            </a>
                        </li>
                    
                        <li class="nav-item">
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/rocprofiler/issues/new/choose" id="navsupport" role="button" aria-expanded="false" target="_blank" >
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
  
  
  
  
  
  
    <p class="title logo__title">ROCProfiler 2.0.0 Documentation</p>
  
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
        <p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../install/installv1.html">Installing ROCProfiler</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../install/installv2.html">Installing ROCProfilerV2</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Tutorials</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/hip-tests/blob/develop/samples/2_Cookbook/0_MatrixTranspose">MatrixTranspose application</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples/">ROCm examples</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/HIP-Examples/tree/master">HIP examples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../how-to/using-rocprof.html">Using rocprof</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../how-to/rocprof-command.html">rocprof command help</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../how-to/rocprofv2-usage.html">Using rocprofv2</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../how-to/rocprofv2-command.html">rocprofv2 command help</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../how-to/using-rocsys.html">Using rocsys</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">References</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../reference/rocprofiler_spec.html">ROCProfiler library specification</a></li>
<li class="toctree-l1 current active has-children"><a class="reference internal" href="index.html">ROCProfiler API library</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2"><a class="reference internal" href="modules.html">Modules</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="annotated_data_structures.html">Data Structures</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="classes.html">Data Structure Index</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="functions_data_fields.html">Data Fields</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="functions_all.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_variables.html">Variables</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2 current active has-children"><a class="reference internal" href="files_files.html">Files</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l3"><a class="reference internal" href="files.html">File List</a></li>
<li class="toctree-l3 current active has-children"><a class="reference internal" href="globals_globals.html">Globals</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l4"><a class="reference internal" href="globals_all.html">All</a></li>
<li class="toctree-l4 current active"><a class="current reference internal" href="#">Functions</a></li>
<li class="toctree-l4"><a class="reference internal" href="globals_type.html">Typedefs</a></li>
<li class="toctree-l4"><a class="reference internal" href="globals_enum.html">Enumerations</a></li>
<li class="toctree-l4"><a class="reference internal" href="globals_eval.html">Enumerator</a></li>
<li class="toctree-l4"><a class="reference internal" href="globals_defs.html">Macros</a></li>
</ul>
</details></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/rocprofilerv2-api.html">ROCProfilerV2 API</a></li>
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
    
    <li class="breadcrumb-item"><a href="index.html" class="nav-link">ROCProfiler API library</a></li>
    
    
    <li class="breadcrumb-item"><i class="fa-solid fa-ellipsis"></i></li>
    
    
    <li class="breadcrumb-item"><a href="globals_globals.html" class="nav-link">Globals</a></li>
    
    <li class="breadcrumb-item active" aria-current="page">ROCProfiler...</li>
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
<title>ROCProfiler API library: Globals</title>
<link href="tabs.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="dynsections.js"></script>
<link href="stylesheet.css" rel="stylesheet" type="text/css" />
<link href="extra_stylesheet.css" rel="stylesheet" type="text/css"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-docs" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/globals_func.html" /><meta name="readthedocs-http-status" content="200" /></head>
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

<h3><a id="index_r"></a>- r -</h3><ul>
<li>rocprofiler_add_feature()
: <a class="el" href="rocprofiler_8h.html#a4a034ce9d31b1668a879c57a9b52f652">rocprofiler.h</a>
</li>
<li>rocprofiler_close()
: <a class="el" href="rocprofiler_8h.html#ac004031974d07c421d2a0dc420874464">rocprofiler.h</a>
</li>
<li>rocprofiler_codeobj_capture_create()
: <a class="el" href="group__device__profiling.html#gadab62c43314489db6b079e43d5bbd852">rocprofiler.h</a>
</li>
<li>rocprofiler_codeobj_capture_free()
: <a class="el" href="group__device__profiling.html#ga4eae9e522f2eb57af2d3fdb62a7f91b3">rocprofiler.h</a>
</li>
<li>rocprofiler_codeobj_capture_get()
: <a class="el" href="group__device__profiling.html#gac3457e88e8fea273ad5a1bbec601a227">rocprofiler.h</a>
</li>
<li>rocprofiler_codeobj_capture_start()
: <a class="el" href="group__device__profiling.html#ga0dbad75a15d8d0796bf004f27d9d73e7">rocprofiler.h</a>
</li>
<li>rocprofiler_codeobj_capture_stop()
: <a class="el" href="group__device__profiling.html#ga9a8b6edbfc9422be31756bfad675b06a">rocprofiler.h</a>
</li>
<li>rocprofiler_create_buffer()
: <a class="el" href="group__session__filter__group.html#gacdcd85c97d6b70011f3ab0dbef095359">rocprofiler.h</a>
</li>
<li>rocprofiler_create_filter()
: <a class="el" href="group__session__filter__group.html#gaa49c9b9ae19a30fc88d00124c3e38234">rocprofiler.h</a>
</li>
<li>rocprofiler_create_ready_session()
: <a class="el" href="group__sessions__handling__group.html#ga78ee3333fbc9005ff1391777674c4f6d">rocprofiler.h</a>
</li>
<li>rocprofiler_create_session()
: <a class="el" href="group__sessions__handling__group.html#gab9d3d2ce93fe21b9250e0b175b42d30d">rocprofiler.h</a>
</li>
<li>rocprofiler_destroy_buffer()
: <a class="el" href="group__session__filter__group.html#gad78379763ce85b00ad07265ada50f9ad">rocprofiler.h</a>
</li>
<li>rocprofiler_destroy_filter()
: <a class="el" href="group__session__filter__group.html#ga57a8374634be090845d8214e875bef0a">rocprofiler.h</a>
</li>
<li>rocprofiler_destroy_session()
: <a class="el" href="group__sessions__handling__group.html#ga6a38e14f1211372afd78237d6089066b">rocprofiler.h</a>
</li>
<li>rocprofiler_device_profiling_session_create()
: <a class="el" href="group__device__profiling.html#ga69428ceac6d7a9430a1db018b3839179">rocprofiler.h</a>
</li>
<li>rocprofiler_device_profiling_session_destroy()
: <a class="el" href="group__device__profiling.html#ga2d44fb23c25676e7f9a4abc0264da7ea">rocprofiler.h</a>
</li>
<li>rocprofiler_device_profiling_session_poll()
: <a class="el" href="group__device__profiling.html#gac0747b6d48cd427dfb8e25bbeed1f4cd">rocprofiler.h</a>
</li>
<li>rocprofiler_device_profiling_session_start()
: <a class="el" href="group__device__profiling.html#gadb1bb3d5f263cd8e4e23b403e376c283">rocprofiler.h</a>
</li>
<li>rocprofiler_device_profiling_session_stop()
: <a class="el" href="group__device__profiling.html#ga62f5fc29136fae3bbe0f49bb46c7ab1b">rocprofiler.h</a>
</li>
<li>rocprofiler_error_str()
: <a class="el" href="group__status__codes__group.html#ga31b8917e5e249d72d57ca29fabb8b8f5">rocprofiler.h</a>
</li>
<li>rocprofiler_error_string()
: <a class="el" href="rocprofiler_8h.html#aca52cdda6b7f36328406f96439e2104a">rocprofiler.h</a>
</li>
<li>rocprofiler_features_set_open()
: <a class="el" href="rocprofiler_8h.html#a8eced279d7edb96a7d374a4720634fd1">rocprofiler.h</a>
</li>
<li>rocprofiler_finalize()
: <a class="el" href="group__rocprofiler__general__group.html#ga3cafdedbd7f965aad1fbd47821296ee9">rocprofiler.h</a>
</li>
<li>rocprofiler_flush_data()
: <a class="el" href="group__memory__storage__buffer__group.html#gafa12d8978c52c6bffa7ad99899c796d1">rocprofiler.h</a>
</li>
<li>rocprofiler_get_agent()
: <a class="el" href="rocprofiler_8h.html#abbe60d19ec46e8dfc29601a2c23a4a49">rocprofiler.h</a>
</li>
<li>rocprofiler_get_data()
: <a class="el" href="rocprofiler_8h.html#aaa2398fc073f541c8fa9c70f5e6a3833">rocprofiler.h</a>
</li>
<li>rocprofiler_get_group()
: <a class="el" href="rocprofiler_8h.html#a96de5e93e5e02e83853ec7538ceccd16">rocprofiler.h</a>
</li>
<li>rocprofiler_get_info()
: <a class="el" href="rocprofiler_8h.html#a18fa3d00f3378343c41728f55207bd04">rocprofiler.h</a>
</li>
<li>rocprofiler_get_metrics()
: <a class="el" href="rocprofiler_8h.html#a063b5ee12045c6f3190fafa080b04af7">rocprofiler.h</a>
</li>
<li>rocprofiler_get_time()
: <a class="el" href="rocprofiler_8h.html#ad002a3fc3abe2928b14b933ad25d7307">rocprofiler.h</a>
</li>
<li>rocprofiler_get_timestamp()
: <a class="el" href="group__timestamp__group.html#gac48329ed42ca2055c629631f3b5ab7b3">rocprofiler.h</a>
</li>
<li>rocprofiler_group_count()
: <a class="el" href="rocprofiler_8h.html#a998e6ddcb2e95720145c6557c473a2eb">rocprofiler.h</a>
</li>
<li>rocprofiler_group_get_data()
: <a class="el" href="rocprofiler_8h.html#a18fd700c314a6c696cc906d4ea881426">rocprofiler.h</a>
</li>
<li>rocprofiler_group_read()
: <a class="el" href="rocprofiler_8h.html#aea2cc8ea869cc852ec7d3f53f5a3add5">rocprofiler.h</a>
</li>
<li>rocprofiler_group_start()
: <a class="el" href="rocprofiler_8h.html#a71764ce37a70747364724c1525d4ab1e">rocprofiler.h</a>
</li>
<li>rocprofiler_group_stop()
: <a class="el" href="rocprofiler_8h.html#a510c962bac4d3a33cb25545b1af2e3c9">rocprofiler.h</a>
</li>
<li>rocprofiler_initialize()
: <a class="el" href="group__rocprofiler__general__group.html#gaaa4ece1073c9a20583380194177c9425">rocprofiler.h</a>
</li>
<li>rocprofiler_iterate_counters()
: <a class="el" href="group__profiling__api__counters__group.html#ga88955c5a313a413a8b2fe91e275c7525">rocprofiler.h</a>
</li>
<li>rocprofiler_iterate_info()
: <a class="el" href="rocprofiler_8h.html#ab5ad6ab6cfe2acb52c3644a501751794">rocprofiler.h</a>
</li>
<li>rocprofiler_iterate_trace_data()
: <a class="el" href="rocprofiler_8h.html#a11e65ebcf67904b13941fb2866d35d0b">rocprofiler.h</a>
</li>
<li>rocprofiler_next_record()
: <a class="el" href="group__memory__storage__buffer__group.html#gab89c4e75210eacfa6387acc223fbab1a">rocprofiler.h</a>
</li>
<li>rocprofiler_open()
: <a class="el" href="rocprofiler_8h.html#a32c80887abd783e998dabdf04e23c294">rocprofiler.h</a>
</li>
<li>rocprofiler_pool_close()
: <a class="el" href="rocprofiler_8h.html#ae4d420938d854407753627ffc6f52ecc">rocprofiler.h</a>
</li>
<li>rocprofiler_pool_fetch()
: <a class="el" href="rocprofiler_8h.html#aa928fcac9acf0c1b47795202e6589d70">rocprofiler.h</a>
</li>
<li>rocprofiler_pool_flush()
: <a class="el" href="rocprofiler_8h.html#a4529e7ca4f3b4248bebb9651e2056175">rocprofiler.h</a>
</li>
<li>rocprofiler_pool_iterate()
: <a class="el" href="rocprofiler_8h.html#a1ccb907fc77b206cef68a43c5f6d6403">rocprofiler.h</a>
</li>
<li>rocprofiler_pool_open()
: <a class="el" href="rocprofiler_8h.html#a76dd4c699cb32c6318fd9d99b90532c2">rocprofiler.h</a>
</li>
<li>rocprofiler_pool_release()
: <a class="el" href="rocprofiler_8h.html#ac058a2ef8cff2cd46e8764b14429d95b">rocprofiler.h</a>
</li>
<li>rocprofiler_query_agent_info()
: <a class="el" href="group__record__agents__group.html#ga554392db97dfb4cbc16fdd25d7ca1daf">rocprofiler.h</a>
</li>
<li>rocprofiler_query_agent_info_size()
: <a class="el" href="group__record__agents__group.html#ga5bacb884e57df0121f2ea2ddba2a5f48">rocprofiler.h</a>
</li>
<li>rocprofiler_query_counter_info()
: <a class="el" href="group__profiling__api__counters__group.html#ga6cf4eadee125bcd771db5bb3c0629345">rocprofiler.h</a>
</li>
<li>rocprofiler_query_counter_info_size()
: <a class="el" href="group__profiling__api__counters__group.html#ga29c3dcb159afc47f0190d9b7ac775d3e">rocprofiler.h</a>
</li>
<li>rocprofiler_query_info()
: <a class="el" href="rocprofiler_8h.html#a09e51aa590194758c234f80a866674f7">rocprofiler.h</a>
</li>
<li>rocprofiler_query_kernel_info()
: <a class="el" href="group__record__kernels__group.html#ga148d85615c926dd90612b3be38829e06">rocprofiler.h</a>
</li>
<li>rocprofiler_query_kernel_info_size()
: <a class="el" href="group__record__kernels__group.html#gae63c7e65f203e9973a155fa0dfcb03dd">rocprofiler.h</a>
</li>
<li>rocprofiler_query_queue_info()
: <a class="el" href="group__record__queues__group.html#ga740788580af7282cf585f4f35f459520">rocprofiler.h</a>
</li>
<li>rocprofiler_query_queue_info_size()
: <a class="el" href="group__record__queues__group.html#ga7067a7c8af019b0f35a55b70991cb294">rocprofiler.h</a>
</li>
<li>rocprofiler_query_tracer_operation_name()
: <a class="el" href="group__tracing__api__group.html#gaef1ce795d8f19268c69c1767498173f0">rocprofiler.h</a>
</li>
<li>rocprofiler_queue_create_profiled()
: <a class="el" href="rocprofiler_8h.html#abeeafefd0dafb8c2dfba6b3e02420002">rocprofiler.h</a>
</li>
<li>rocprofiler_read()
: <a class="el" href="rocprofiler_8h.html#adac16141423f299f581d842672a582e7">rocprofiler.h</a>
</li>
<li>rocprofiler_remove_queue_callbacks()
: <a class="el" href="rocprofiler_8h.html#ac96427f92893bbf06a4de41680c63ff7">rocprofiler.h</a>
</li>
<li>rocprofiler_reset()
: <a class="el" href="rocprofiler_8h.html#a9a7c169772a8cf86a0d3b2ff29175d69">rocprofiler.h</a>
</li>
<li>rocprofiler_set_api_trace_sync_callback()
: <a class="el" href="group__session__filter__group.html#ga33e103650de8eb12a02b2d1f55de879b">rocprofiler.h</a>
</li>
<li>rocprofiler_set_buffer_properties()
: <a class="el" href="group__session__filter__group.html#ga7318add019a3a05d0b5387a0f89c139c">rocprofiler.h</a>
</li>
<li>rocprofiler_set_filter_buffer()
: <a class="el" href="group__session__filter__group.html#ga1d0276068b2871878d7aefa866a56b23">rocprofiler.h</a>
</li>
<li>rocprofiler_set_hsa_callbacks()
: <a class="el" href="rocprofiler_8h.html#ae9aa0a5ecb7515ba87ee1ec82a651d01">rocprofiler.h</a>
</li>
<li>rocprofiler_set_queue_callbacks()
: <a class="el" href="rocprofiler_8h.html#af4d7e3d585ff28c0d5cad12f610461b7">rocprofiler.h</a>
</li>
<li>rocprofiler_start()
: <a class="el" href="rocprofiler_8h.html#ac48b1dba77351f869a2e7dfdf4a040e8">rocprofiler.h</a>
</li>
<li>rocprofiler_start_queue_callbacks()
: <a class="el" href="rocprofiler_8h.html#a438974526cbe56c35db41cd8bc52edbe">rocprofiler.h</a>
</li>
<li>rocprofiler_start_session()
: <a class="el" href="group__sessions__handling__group.html#gafc34479260b63e27a59617d00b27800e">rocprofiler.h</a>
</li>
<li>rocprofiler_stop()
: <a class="el" href="rocprofiler_8h.html#ae323913e66c7dd0c6fa008d7a5d75f8f">rocprofiler.h</a>
</li>
<li>rocprofiler_stop_queue_callbacks()
: <a class="el" href="rocprofiler_8h.html#a7aceb542b1ae89c89630827491c4a528">rocprofiler.h</a>
</li>
<li>rocprofiler_terminate_session()
: <a class="el" href="group__sessions__handling__group.html#ga6f627f98d798c145c3a53d720a34c5e6">rocprofiler.h</a>
</li>
<li>rocprofiler_tracer_operation_id()
: <a class="el" href="group__tracing__api__group.html#ga8ef960475cb58c774bb42bb212d6490b">rocprofiler.h</a>
</li>
<li>rocprofiler_version_major()
: <a class="el" href="rocprofiler_8h.html#acc51b0771d0fce7d7a73d744c06c39cb">rocprofiler.h</a>
</li>
<li>rocprofiler_version_minor()
: <a class="el" href="rocprofiler_8h.html#a4532186dc0753bcf27258fcdfc00ca67">rocprofiler.h</a>
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
       href="globals_r.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Globals</p>
      </div>
    </a>
    <a class="right-next"
       href="globals_type.html"
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
                        <span class="copyright">© 2026 Advanced Micro Devices, Inc</span>
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
