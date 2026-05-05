---
title: "ROCProfiler API library: Globals &#8212; ROCProfiler 2.0.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler/en/latest/doxygen/html/globals_eval.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:21:01.979448+00:00
content_hash: "51322512c282cd80"
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/html/globals_eval';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="Globals" href="globals_defs.html" />
    <link rel="prev" title="Globals" href="globals_enum.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-docs" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/globals_eval.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l4"><a class="reference internal" href="globals_func.html">Functions</a></li>
<li class="toctree-l4"><a class="reference internal" href="globals_type.html">Typedefs</a></li>
<li class="toctree-l4"><a class="reference internal" href="globals_enum.html">Enumerations</a></li>
<li class="toctree-l4 current active"><a class="current reference internal" href="#">Enumerator</a></li>
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
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-docs" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/globals_eval.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
<li>ACTIVITY_DOMAIN_EXT_API
: <a class="el" href="group__tracing__api__group.html#gga57666e770c7e482a831652d87d664a06a61b11f6adec49b629e54b5b77954b9a0">rocprofiler.h</a>
</li>
<li>ACTIVITY_DOMAIN_HIP_API
: <a class="el" href="group__tracing__api__group.html#gga57666e770c7e482a831652d87d664a06a77fd60534b7425cf79585664a0eb5ae8">rocprofiler.h</a>
</li>
<li>ACTIVITY_DOMAIN_HIP_OPS
: <a class="el" href="group__tracing__api__group.html#gga57666e770c7e482a831652d87d664a06ac365bca532f0a6756e3f824604edb3a7">rocprofiler.h</a>
</li>
<li>ACTIVITY_DOMAIN_HSA_API
: <a class="el" href="group__tracing__api__group.html#gga57666e770c7e482a831652d87d664a06ab93f50713d0896c1bb6b2c7f362b8319">rocprofiler.h</a>
</li>
<li>ACTIVITY_DOMAIN_HSA_EVT
: <a class="el" href="group__tracing__api__group.html#gga57666e770c7e482a831652d87d664a06a63e6657cd0875e440caa26890fe62644">rocprofiler.h</a>
</li>
<li>ACTIVITY_DOMAIN_HSA_OPS
: <a class="el" href="group__tracing__api__group.html#gga57666e770c7e482a831652d87d664a06a743347f9e500e44b470f99b6df9dc346">rocprofiler.h</a>
</li>
<li>ACTIVITY_DOMAIN_KFD_API
: <a class="el" href="group__tracing__api__group.html#gga57666e770c7e482a831652d87d664a06adcbb0afdf1c2e2b257885fe88397b550">rocprofiler.h</a>
</li>
<li>ACTIVITY_DOMAIN_NUMBER
: <a class="el" href="group__tracing__api__group.html#gga57666e770c7e482a831652d87d664a06a786f6dea985a77d6f4e47d61ae04762b">rocprofiler.h</a>
</li>
<li>ACTIVITY_DOMAIN_ROCTX
: <a class="el" href="group__tracing__api__group.html#gga57666e770c7e482a831652d87d664a06a05b3101654d570649db439e0b2020caf">rocprofiler.h</a>
</li>
</ul>


<h3><a id="index_r"></a>- r -</h3><ul>
<li>ROCPROFILER_AGENT_NAME
: <a class="el" href="group__record__agents__group.html#gga85fabd61ab968970f1622019aab71590aed29cb81ca4f8d893f9651c76fdb9ca0">rocprofiler.h</a>
</li>
<li>ROCPROFILER_AGENT_TYPE
: <a class="el" href="group__record__agents__group.html#gga85fabd61ab968970f1622019aab71590a83aee30189eee855a1401cd60ed286bd">rocprofiler.h</a>
</li>
<li>ROCPROFILER_API_TRACE
: <a class="el" href="group__session__filter__group.html#gga0046196ba16e3b630a56feab4833c35cab5aa9731dde3525351822f0777f1cdfc">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_BUFFER_SIZE
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04eaa03d0f2de3faf50fb6ee3ac4fcd87fb5">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_CAPTURE_MODE
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea091bb3746300810547d28262a1466b23">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_COMPUTE_UNIT
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea22b6e3664f60d15ac46f1b376f2994be">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_MASK
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea7d73618bc41a8667baae7f706d9a8490">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_MAXVALUE
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea4e300c56e05b38eeffc6246a5bba528d">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_OCCUPANCY
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea74e8b8f666c14d5fcbdabc2c217c52aa">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_PERF_CTRL
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea446649f8b72f672fd7ef80c50b324b0d">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_PERF_MASK
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04eaeea59a47a67d2ae0fcd8a56c23dbe732">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_PERFCOUNTER
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea5b5058c81731ee7ac7e78342c51a2321">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_PERFCOUNTER_NAME
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea596ada24e782f4f096fee04794befcfb">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_SAMPLE_RATE
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea9c21ce01576ee56619f50880c316cb99">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_SE_MASK
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04eaad051072a5e6bc277123ff7e04a95bce">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_SIMD_SELECT
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea1675437762fd15f3c8f70978f0ff3c7b">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_TOKEN_MASK
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea2832dd4175ae1e52949582fd6821cdd4">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_TOKEN_MASK2
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea590a5b23422221bc2603d6ad4e35fd57">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_TRACE_COLLECTION
: <a class="el" href="group__session__filter__group.html#gga0046196ba16e3b630a56feab4833c35ca3b7db4f42833ff4802427194644d388f">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_TRACER_RECORD
: <a class="el" href="group__generic__record__group.html#gga89a0f080122fed6cfff58f4597d52115af91ec0b1d6ae380cd8ea9a5cf77ddda3">rocprofiler.h</a>
</li>
<li>ROCPROFILER_ATT_VMID_MASK
: <a class="el" href="group__session__filter__group.html#ggae4389d597b3258d6d22974958fb0e04ea1351c889eebf34eac702d4e5b83b0667">rocprofiler.h</a>
</li>
<li>ROCPROFILER_BUFFER_PROPERTY_KIND_INTERVAL_FLUSH
: <a class="el" href="group__memory__storage__buffer__group.html#ggacf4c6b1a4b2759d6eb88c445a12b88aba559af46aa6f4d4ec0069d671e16db0da">rocprofiler.h</a>
</li>
<li>ROCPROFILER_CAPTURE_COPY_FILE_AND_MEMORY
: <a class="el" href="group__profiling__api__counters__group.html#gga97a277031f9c9df8a4c3cae68dfbe598a98dc10a4b2b59f5c9d08f57a7fd3aeae">rocprofiler.h</a>
</li>
<li>ROCPROFILER_CAPTURE_COPY_MEMORY
: <a class="el" href="group__profiling__api__counters__group.html#gga97a277031f9c9df8a4c3cae68dfbe598a03d3418285ef6bba0323519a03877553">rocprofiler.h</a>
</li>
<li>ROCPROFILER_CAPTURE_SYMBOLS_ONLY
: <a class="el" href="group__profiling__api__counters__group.html#gga97a277031f9c9df8a4c3cae68dfbe598a2f7b6046622f682577fd520667a7d43b">rocprofiler.h</a>
</li>
<li>ROCPROFILER_COUNTER_BLOCK_ID
: <a class="el" href="group__profiling__api__counters__group.html#gga81aaeba8d77c565d78893e3630799750a0f2a85bb0ad0d2ee988785be7c4bc8ea">rocprofiler.h</a>
</li>
<li>ROCPROFILER_COUNTER_HIERARCHY_LEVEL
: <a class="el" href="group__profiling__api__counters__group.html#gga81aaeba8d77c565d78893e3630799750a46e24a0824928040b5c11aa98254b343">rocprofiler.h</a>
</li>
<li>ROCPROFILER_COUNTER_NAME
: <a class="el" href="group__profiling__api__counters__group.html#gga81aaeba8d77c565d78893e3630799750a01b62e569f7480fefdb32479f530c9f9">rocprofiler.h</a>
</li>
<li>ROCPROFILER_COUNTERS_COLLECTION
: <a class="el" href="group__session__filter__group.html#gga0046196ba16e3b630a56feab4833c35ca46423adb3044012a96673b402d71676c">rocprofiler.h</a>
</li>
<li>ROCPROFILER_COUNTERS_SAMPLER
: <a class="el" href="group__session__filter__group.html#gga0046196ba16e3b630a56feab4833c35cae97c345311930d78a17c422e906eeaa9">rocprofiler.h</a>
</li>
<li>ROCPROFILER_COUNTERS_SAMPLER_PCIE_COUNTERS
: <a class="el" href="group__session__filter__group.html#gga2d4ec856af58d99f33af98a2babb6780a55ff64ee94b056a2d8306c207a7ba90a">rocprofiler.h</a>
</li>
<li>ROCPROFILER_COUNTERS_SAMPLER_RECORD
: <a class="el" href="group__generic__record__group.html#gga89a0f080122fed6cfff58f4597d52115a5ddb7c93a247335a5c71f508f52af9ff">rocprofiler.h</a>
</li>
<li>ROCPROFILER_COUNTERS_SAMPLER_XGMI_COUNTERS
: <a class="el" href="group__session__filter__group.html#gga2d4ec856af58d99f33af98a2babb6780a33da3569d01e881f56e2f546e07619c5">rocprofiler.h</a>
</li>
<li>ROCPROFILER_CPU_AGENT
: <a class="el" href="group__record__agents__group.html#ggaf9f1cb8a1d2b462aaf7ba2d687c3351aad4a3f2163484559d2ebae6fb500f9e03">rocprofiler.h</a>
</li>
<li>ROCPROFILER_DATA_KIND_BYTES
: <a class="el" href="rocprofiler_8h.html#a026a2d7363f732f41bdf2642cac278cba53f07abf899fbb144f555e68ed78760e">rocprofiler.h</a>
</li>
<li>ROCPROFILER_DATA_KIND_DOUBLE
: <a class="el" href="rocprofiler_8h.html#a026a2d7363f732f41bdf2642cac278cba12590dcb1dcce9d967e45a552592d83b">rocprofiler.h</a>
</li>
<li>ROCPROFILER_DATA_KIND_FLOAT
: <a class="el" href="rocprofiler_8h.html#a026a2d7363f732f41bdf2642cac278cbac6b402d1bd10c02e8f5d3371099e658a">rocprofiler.h</a>
</li>
<li>ROCPROFILER_DATA_KIND_INT32
: <a class="el" href="rocprofiler_8h.html#a026a2d7363f732f41bdf2642cac278cba5c00fbd1549023b8535195ce97bfdf43">rocprofiler.h</a>
</li>
<li>ROCPROFILER_DATA_KIND_INT64
: <a class="el" href="rocprofiler_8h.html#a026a2d7363f732f41bdf2642cac278cbab5357482d82fd6a85b1e3217559140a4">rocprofiler.h</a>
</li>
<li>ROCPROFILER_DATA_KIND_UNINIT
: <a class="el" href="rocprofiler_8h.html#a026a2d7363f732f41bdf2642cac278cbaf9c5ae3ca1f16f76de645cd12e9ffa5b">rocprofiler.h</a>
</li>
<li>ROCPROFILER_DISPATCH_TIMESTAMPS_COLLECTION
: <a class="el" href="group__session__filter__group.html#gga0046196ba16e3b630a56feab4833c35ca298af20dd741cfa8f58ef9d323bf0034">rocprofiler.h</a>
</li>
<li>ROCPROFILER_FEATURE_KIND_METRIC
: <a class="el" href="rocprofiler_8h.html#ac2920b78f85e0fb30af5bf67ff12b4bba93d97732b31d3ae5a3666ee86a6c9fe2">rocprofiler.h</a>
</li>
<li>ROCPROFILER_FEATURE_KIND_PCSMP_MOD
: <a class="el" href="rocprofiler_8h.html#ac2920b78f85e0fb30af5bf67ff12b4bba9e9ef82dd08974d66ce0fe85ebc95726">rocprofiler.h</a>
</li>
<li>ROCPROFILER_FEATURE_KIND_SPM_MOD
: <a class="el" href="rocprofiler_8h.html#ac2920b78f85e0fb30af5bf67ff12b4bbaffa81188ab55e8df6d378d3083777385">rocprofiler.h</a>
</li>
<li>ROCPROFILER_FEATURE_KIND_TRACE
: <a class="el" href="rocprofiler_8h.html#ac2920b78f85e0fb30af5bf67ff12b4bbab09466ed972d9bf7e3a8e6314a2bfca5">rocprofiler.h</a>
</li>
<li>ROCPROFILER_FILTER_DISPATCH_IDS
: <a class="el" href="group__session__filter__group.html#ggaf939ad3e0d006e3f27f30ab4cf4e15d4aa1ee411bbe49a9d7ce5a39d56861ef9f">rocprofiler.h</a>
</li>
<li>ROCPROFILER_FILTER_GPU_NAME
: <a class="el" href="group__session__filter__group.html#ggaf939ad3e0d006e3f27f30ab4cf4e15d4aa79c2273af823653315cede20da9ab48">rocprofiler.h</a>
</li>
<li>ROCPROFILER_FILTER_HIP_TRACER_API_FUNCTIONS
: <a class="el" href="group__session__filter__group.html#ggaf939ad3e0d006e3f27f30ab4cf4e15d4a73b4a1c1a97f171633d1539f32ef7358">rocprofiler.h</a>
</li>
<li>ROCPROFILER_FILTER_HSA_TRACER_API_FUNCTIONS
: <a class="el" href="group__session__filter__group.html#ggaf939ad3e0d006e3f27f30ab4cf4e15d4a8d73096bade022c63d234a8ffe8dbf18">rocprofiler.h</a>
</li>
<li>ROCPROFILER_FILTER_KERNEL_NAMES
: <a class="el" href="group__session__filter__group.html#ggaf939ad3e0d006e3f27f30ab4cf4e15d4a970516eaf155ca4aea3401ae7dd5e50e">rocprofiler.h</a>
</li>
<li>ROCPROFILER_FILTER_RANGE
: <a class="el" href="group__session__filter__group.html#ggaf939ad3e0d006e3f27f30ab4cf4e15d4a47f76853e3e65f2548c621e95f10f87b">rocprofiler.h</a>
</li>
<li>ROCPROFILER_GPU_AGENT
: <a class="el" href="group__record__agents__group.html#ggaf9f1cb8a1d2b462aaf7ba2d687c3351aad5d969aa3f84d921fb5f4d3345657ed5">rocprofiler.h</a>
</li>
<li>ROCPROFILER_HSA_CB_ID_ALLOCATE
: <a class="el" href="rocprofiler_8h.html#a1ff86643d3ebf5f0e8474b7a791c80d3a50d8c49774f4dfb7e5c6349fa0493bc4">rocprofiler.h</a>
</li>
<li>ROCPROFILER_HSA_CB_ID_CODEOBJ
: <a class="el" href="rocprofiler_8h.html#a1ff86643d3ebf5f0e8474b7a791c80d3abd62f7b1d43c361d8d439bb66f927f4f">rocprofiler.h</a>
</li>
<li>ROCPROFILER_HSA_CB_ID_DEVICE
: <a class="el" href="rocprofiler_8h.html#a1ff86643d3ebf5f0e8474b7a791c80d3a6e92aee5bd60bebf6ba505b05f35cc52">rocprofiler.h</a>
</li>
<li>ROCPROFILER_HSA_CB_ID_KSYMBOL
: <a class="el" href="rocprofiler_8h.html#a1ff86643d3ebf5f0e8474b7a791c80d3a85d9390ff29750f1253303112d83dfd5">rocprofiler.h</a>
</li>
<li>ROCPROFILER_HSA_CB_ID_MEMCOPY
: <a class="el" href="rocprofiler_8h.html#a1ff86643d3ebf5f0e8474b7a791c80d3ad5a1f1714b5832e4cb7b3b0af318583d">rocprofiler.h</a>
</li>
<li>ROCPROFILER_HSA_CB_ID_SUBMIT
: <a class="el" href="rocprofiler_8h.html#a1ff86643d3ebf5f0e8474b7a791c80d3a9213d0dce01be8fe2f4b8944e2828d70">rocprofiler.h</a>
</li>
<li>ROCPROFILER_INFO_KIND_METRIC
: <a class="el" href="rocprofiler_8h.html#a4eccb33bde277e7628ff26a5c6371b35a342f56cf9cf7f65301d8e7c42dcdac38">rocprofiler.h</a>
</li>
<li>ROCPROFILER_INFO_KIND_METRIC_COUNT
: <a class="el" href="rocprofiler_8h.html#a4eccb33bde277e7628ff26a5c6371b35a2b9292afbd3fb1a978d904e2c7720b6e">rocprofiler.h</a>
</li>
<li>ROCPROFILER_INFO_KIND_TRACE
: <a class="el" href="rocprofiler_8h.html#a4eccb33bde277e7628ff26a5c6371b35a8857a8f77df58725748a152b2bc6aa2c">rocprofiler.h</a>
</li>
<li>ROCPROFILER_INFO_KIND_TRACE_COUNT
: <a class="el" href="rocprofiler_8h.html#a4eccb33bde277e7628ff26a5c6371b35a65e3016282630bbec7a6be2a8c46e4e7">rocprofiler.h</a>
</li>
<li>ROCPROFILER_INFO_KIND_TRACE_PARAMETER
: <a class="el" href="rocprofiler_8h.html#a4eccb33bde277e7628ff26a5c6371b35a5677830e05adaa61652e5fb550f2c0d9">rocprofiler.h</a>
</li>
<li>ROCPROFILER_INFO_KIND_TRACE_PARAMETER_COUNT
: <a class="el" href="rocprofiler_8h.html#a4eccb33bde277e7628ff26a5c6371b35aa64d7b3fd5ecc35265ea7e1b4714cdfb">rocprofiler.h</a>
</li>
<li>ROCPROFILER_KERNEL_NAME
: <a class="el" href="group__record__kernels__group.html#gga0084f37a58e77a5941d794bbee29d1fcab2db4016c0f665d56f582a014ce62f38">rocprofiler.h</a>
</li>
<li>ROCPROFILER_MODE_CREATEQUEUE
: <a class="el" href="rocprofiler_8h.html#a95238ebe64aef6be0eee38e3caf3d2eea8ea4498ae2f04b8c3a49f3fc6e26ba26">rocprofiler.h</a>
</li>
<li>ROCPROFILER_MODE_SINGLEGROUP
: <a class="el" href="rocprofiler_8h.html#a95238ebe64aef6be0eee38e3caf3d2eeab0e0dc72d25d407fbda1207cbd921627">rocprofiler.h</a>
</li>
<li>ROCPROFILER_MODE_STANDALONE
: <a class="el" href="rocprofiler_8h.html#a95238ebe64aef6be0eee38e3caf3d2eeae9d50cb249db177ebc26bee3bc3c13e2">rocprofiler.h</a>
</li>
<li>ROCPROFILER_NONE_REPLAY_MODE
: <a class="el" href="group__sessions__handling__group.html#ggabcf8a5945160311e3bcc6cf801418838a37a40fba9ae8408f3bc60f108a0ba0b3">rocprofiler.h</a>
</li>
<li>ROCPROFILER_PC_SAMPLING_COLLECTION
: <a class="el" href="group__session__filter__group.html#gga0046196ba16e3b630a56feab4833c35cabd697ab5639eabd469c01ad49850b9ff">rocprofiler.h</a>
</li>
<li>ROCPROFILER_PC_SAMPLING_RECORD
: <a class="el" href="group__generic__record__group.html#gga89a0f080122fed6cfff58f4597d52115a22081f1d6a59eced5499548ab613fa05">rocprofiler.h</a>
</li>
<li>ROCPROFILER_PHASE_ENTER
: <a class="el" href="group__tracing__api__group.html#ggac33b5bfb9fbaf32ff295f554f1f536bfaa17ff93d2f61a7a9744e6aa2b5f160ec">rocprofiler.h</a>
</li>
<li>ROCPROFILER_PHASE_EXIT
: <a class="el" href="group__tracing__api__group.html#ggac33b5bfb9fbaf32ff295f554f1f536bfaaefbdf9d8b538d3fa5b5f69a0d2aa6ca">rocprofiler.h</a>
</li>
<li>ROCPROFILER_PHASE_NONE
: <a class="el" href="group__tracing__api__group.html#ggac33b5bfb9fbaf32ff295f554f1f536bfa335485dad3ad3d04c1ca3de62595d203">rocprofiler.h</a>
</li>
<li>ROCPROFILER_PROFILER_RECORD
: <a class="el" href="group__generic__record__group.html#gga89a0f080122fed6cfff58f4597d52115a9a478aa6a8af9b055f887ecfaf8e3c14">rocprofiler.h</a>
</li>
<li>ROCPROFILER_QUEUE_SIZE
: <a class="el" href="group__record__queues__group.html#gga4c6b56f3d0fdae0944a91267701bd3a7aba5542b1e36ff3b48a0d2343ac15dd59">rocprofiler.h</a>
</li>
<li>ROCPROFILER_SPM_COLLECTION
: <a class="el" href="group__session__filter__group.html#gga0046196ba16e3b630a56feab4833c35ca5296a5a6ecc4b6a0e5f41189339f4dfb">rocprofiler.h</a>
</li>
<li>ROCPROFILER_SPM_RECORD
: <a class="el" href="group__generic__record__group.html#gga89a0f080122fed6cfff58f4597d52115ac7415411313caa88f3b4ff3a5077463c">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcaaf9f57d96e8d8bea5cd18252beb2756b">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_AGENT_INFORMATION_MISSING
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcafb26c4683f12b105f7c49b7ee19ff02b">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_AGENT_NOT_FOUND
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcaa7128778ad3f0dd611b2da94af1b79c7">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_ALREADY_INITIALIZED
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcad7b12be9bfda85021be0b0f413a14b84">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_BUFFER_NOT_FOUND
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca30fbcdea2625c1e35f39f00ee8a6e268">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_CORRUPTED_LABEL_DATA
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca32849640867c795971ad73c278bf9900">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_CORRUPTED_SESSION_BUFFER
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca019f553febb7b6eaee16e10b2ce8b880">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_COUNTER_INFORMATION_MISSING
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca0603d74510ec2ae68212239e75b57554">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_COUNTER_NOT_FOUND
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca3114b5fbfb25f42cc363b125100b435e">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_FILTER_DATA_CORRUPTED
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca2c4163a2984a36b3b879e1edf005c361">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_FILTER_NOT_FOUND
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcabaa34c793f61b11afe1067fa0f7b5ecb">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_FILTER_NOT_SUPPORTED
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcafa03dd8694ee0f7cdd0c5946b3d68524">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_HAS_ACTIVE_SESSION
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca2564b61dccd2802c1b471ed9564c33e3">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_INCORRECT_DOMAIN
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca9879a8a7f267462fce336e359828bc8c">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_INCORRECT_FLUSH_INTERVAL
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca88f78879e5fde70a46956a67e329e30a">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_INCORRECT_REPLAY_MODE
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca3667f87181ff369ee1242d6c5d709026">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_INCORRECT_SIZE
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcaccf712fc3f5f106e1b29bb138bd7fb06">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_INVALID_ARGUMENTS
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcaa4a2cfe997ba3f0672befeefebc2f8e8">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_INVALID_DOMAIN_ID
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca699d9bc645a398c4c7b89bf3c83db944">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_INVALID_OPERATION_ID
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca699c83d40953f2ee2ab271fb0a29de3c">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_KERNEL_INFORMATION_MISSING
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcab3add3972c2f4d3dd537d370a09da550">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_KERNEL_NOT_FOUND
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca2780e6072a87097b0ef04ab17006b48b">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_MISMATCHED_EXTERNAL_CORRELATION_ID
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca94e11d2484bddcfd2c5a5eb21727ac18">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_NOT_IMPLEMENTED
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca516d7996dc81b1888168cdf71c99a7d3">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_NOT_INITIALIZED
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcafbf0b46f596cab79ee5f937823a62a37">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_PASS_NOT_STARTED
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcaf757fd359014abd95b276388cf115638">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_QUEUE_INFORMATION_MISSING
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca0488f4fed1e216acec842201d1d10ae2">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_QUEUE_NOT_FOUND
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca6393b835df103eb7a457e8292fd0a61b">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_RANGE_STACK_IS_EMPTY
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcab5b497e8f8d88a2f1e92c7f26a6d9ccc">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_RECORD_CORRUPTED
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcacd4e97bf71ed7ef123d768746fa8cbfa">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_SESSION_FILTER_DATA_MISMATCH
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca96d935be23b6487215bd933f41e98688">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_SESSION_MISSING_BUFFER
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca1c856fa47a37b68bd4949166421e3e74">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_SESSION_MISSING_FILTER
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca17458d1defdccf8cf02b998560a84b3b">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_SESSION_NOT_ACTIVE
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcaa851054040ee9b20aaeb2f2cefbe81ec">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_SESSION_NOT_FOUND
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca948b0764d381c47ba1520bdcb9193133">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_TIMESTAMP_NOT_APPLICABLE
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcab8f7f9489a4b9a3a14a7e13532a9f9e1">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_TRACER_API_DATA_INFORMATION_MISSING
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca03bfd62ff25cc70ef2b5ac14b736ccc2">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_ERROR_TRACER_API_DATA_NOT_FOUND
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddca8adebd36a043540834e6ffe3011222f2">rocprofiler.h</a>
</li>
<li>ROCPROFILER_STATUS_SUCCESS
: <a class="el" href="group__status__codes__group.html#gga952efee747482031f1478b1fcc4eeddcaf545f805974933ffd3ad33bbd422dd8b">rocprofiler.h</a>
</li>
<li>ROCPROFILER_TIME_ID_CLOCK_MONOTONIC
: <a class="el" href="rocprofiler_8h.html#acc755e29a333a42ce274ab8f3262ecbaaefa3fa69b8b7d90e75011d0ee3e8c6bf">rocprofiler.h</a>
</li>
<li>ROCPROFILER_TIME_ID_CLOCK_MONOTONIC_COARSE
: <a class="el" href="rocprofiler_8h.html#acc755e29a333a42ce274ab8f3262ecbaac102e5f14e59b4409fe462a70ccd8045">rocprofiler.h</a>
</li>
<li>ROCPROFILER_TIME_ID_CLOCK_MONOTONIC_RAW
: <a class="el" href="rocprofiler_8h.html#acc755e29a333a42ce274ab8f3262ecbaa28e0b49ca4ed481b1378a81566103cd7">rocprofiler.h</a>
</li>
<li>ROCPROFILER_TIME_ID_CLOCK_REALTIME
: <a class="el" href="rocprofiler_8h.html#acc755e29a333a42ce274ab8f3262ecbaa9ab4a3a5787e4300b04da288517b1ddb">rocprofiler.h</a>
</li>
<li>ROCPROFILER_TIME_ID_CLOCK_REALTIME_COARSE
: <a class="el" href="rocprofiler_8h.html#acc755e29a333a42ce274ab8f3262ecbaa60a1e0c5d6c5d1200482dbbeb20fb9ac">rocprofiler.h</a>
</li>
<li>ROCPROFILER_TRACER_RECORD
: <a class="el" href="group__generic__record__group.html#gga89a0f080122fed6cfff58f4597d52115a588e9b0c26f14e4fd9dc4df369450ab6">rocprofiler.h</a>
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
       href="globals_enum.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Globals</p>
      </div>
    </a>
    <a class="right-next"
       href="globals_defs.html"
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
