---
title: "ROCProfiler API library: Data Structures &#8212; ROCProfiler 2.0.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler/en/latest/doxygen/html/annotated.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:29:02.573024+00:00
content_hash: "87e543af5f85817e"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>ROCProfiler API library: Data Structures &#8212; ROCProfiler 2.0.0 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/html/annotated';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="Data Structure Index" href="classes.html" />
    <link rel="prev" title="Data Structures" href="annotated_data_structures.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-docs" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/annotated.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l2 current active has-children"><a class="reference internal" href="annotated_data_structures.html">Data Structures</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="classes.html">Data Structure Index</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="functions_data_fields.html">Data Fields</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="functions_all.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="functions_vars_variables.html">Variables</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="files_files.html">Files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="files.html">File List</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="globals_globals.html">Globals</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="globals_all.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="globals_func.html">Functions</a></li>
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
    
    
    <li class="breadcrumb-item"><a href="annotated_data_structures.html" class="nav-link">Data Structures</a></li>
    
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
<html xmlns="http://www.w3.org/1999/xhtml" lang="$langISO">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.1"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>ROCProfiler API library: Data Structures</title>
<link href="tabs.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="dynsections.js"></script>
<link href="stylesheet.css" rel="stylesheet" type="text/css" />
<link href="extra_stylesheet.css" rel="stylesheet" type="text/css"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-docs" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/annotated.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
<div class="title">Data Structures</div>  </div>
</div><!--header-->
<div class="contents">
<div class="textblock">Here are the data structures with brief descriptions:</div><div class="directory">
<table class="directory">
<tr id="row_0_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__agent__id__t.html" target="_self">rocprofiler_agent_id_t</a></td><td class="desc">Agent ID handle, which represents a unique id to the agent reported as it can be used to retrieve Agent information using <a class="el" href="group__record__agents__group.html#ga554392db97dfb4cbc16fdd25d7ca1daf" title="Query Agent Information Data using an allocated data pointer by the user, user can get the size of th...">rocprofiler_query_agent_info</a>, Agents can be CPUs or GPUs </td></tr>
<tr id="row_1_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__att__parameter__t.html" target="_self">rocprofiler_att_parameter_t</a></td><td class="desc"></td></tr>
<tr id="row_2_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__buffer__id__t.html" target="_self">rocprofiler_buffer_id_t</a></td><td class="desc"></td></tr>
<tr id="row_3_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__buffer__property__t.html" target="_self">rocprofiler_buffer_property_t</a></td><td class="desc"></td></tr>
<tr id="row_4_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__callback__data__t.html" target="_self">rocprofiler_callback_data_t</a></td><td class="desc"></td></tr>
<tr id="row_5_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__codeobj__symbols__t.html" target="_self">rocprofiler_codeobj_symbols_t</a></td><td class="desc">Struct to store the filepaths and their addresses for intercepted code objects </td></tr>
<tr id="row_6_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__correlation__id__t.html" target="_self">rocprofiler_correlation_id_t</a></td><td class="desc">Correlation ID </td></tr>
<tr id="row_7_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__counter__id__t.html" target="_self">rocprofiler_counter_id_t</a></td><td class="desc">Counter ID to be used to query counter information using <a class="el" href="group__profiling__api__counters__group.html#ga6cf4eadee125bcd771db5bb3c0629345" title="Query Counter Information Data using an allocated data pointer by the user, user can get the size of ...">rocprofiler_query_counter_info</a> </td></tr>
<tr id="row_8_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__counter__info__t.html" target="_self">rocprofiler_counter_info_t</a></td><td class="desc"></td></tr>
<tr id="row_9_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__counter__value__t.html" target="_self">rocprofiler_counter_value_t</a></td><td class="desc"></td></tr>
<tr id="row_10_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__counters__sampler__counter__input__t.html" target="_self">rocprofiler_counters_sampler_counter_input_t</a></td><td class="desc"></td></tr>
<tr id="row_11_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__counters__sampler__counter__output__t.html" target="_self">rocprofiler_counters_sampler_counter_output_t</a></td><td class="desc"></td></tr>
<tr id="row_12_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__counters__sampler__parameters__t.html" target="_self">rocprofiler_counters_sampler_parameters_t</a></td><td class="desc"></td></tr>
<tr id="row_13_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__data__t.html" target="_self">rocprofiler_data_t</a></td><td class="desc"></td></tr>
<tr id="row_14_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__device__profile__metric__t.html" target="_self">rocprofiler_device_profile_metric_t</a></td><td class="desc"></td></tr>
<tr id="row_15_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__dispatch__record__t.html" target="_self">rocprofiler_dispatch_record_t</a></td><td class="desc"></td></tr>
<tr id="row_16_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__event__id__t.html" target="_self">rocprofiler_event_id_t</a></td><td class="desc"></td></tr>
<tr id="row_17_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__feature__t.html" target="_self">rocprofiler_feature_t</a></td><td class="desc"></td></tr>
<tr id="row_18_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="unionrocprofiler__filter__data__t.html" target="_self">rocprofiler_filter_data_t</a></td><td class="desc">Filter Kind Data </td></tr>
<tr id="row_19_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__filter__id__t.html" target="_self">rocprofiler_filter_id_t</a></td><td class="desc"></td></tr>
<tr id="row_20_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__filter__property__t.html" target="_self">rocprofiler_filter_property_t</a></td><td class="desc">Filter Data Type filter data will be used to report required and optional filters for the sessions using ::rocprofiler_session_add_filters </td></tr>
<tr id="row_21_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__group__t.html" target="_self">rocprofiler_group_t</a></td><td class="desc"></td></tr>
<tr id="row_22_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__hsa__callback__data__t.html" target="_self">rocprofiler_hsa_callback_data_t</a></td><td class="desc"></td></tr>
<tr id="row_23_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__hsa__callbacks__t.html" target="_self">rocprofiler_hsa_callbacks_t</a></td><td class="desc"></td></tr>
<tr id="row_24_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__info__data__t.html" target="_self">rocprofiler_info_data_t</a></td><td class="desc"></td></tr>
<tr id="row_25_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="unionrocprofiler__info__query__t.html" target="_self">rocprofiler_info_query_t</a></td><td class="desc"></td></tr>
<tr id="row_26_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__intercepted__codeobj__t.html" target="_self">rocprofiler_intercepted_codeobj_t</a></td><td class="desc">Struct to store the filepaths and their addresses for intercepted code objects </td></tr>
<tr id="row_27_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__kernel__dispatch__id__t.html" target="_self">rocprofiler_kernel_dispatch_id_t</a></td><td class="desc">Kernel dispatch correlation ID, unique across all dispatches </td></tr>
<tr id="row_28_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__kernel__id__t.html" target="_self">rocprofiler_kernel_id_t</a></td><td class="desc">Kernel identifier that represent a unique id for every kernel </td></tr>
<tr id="row_29_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__kernel__properties__t.html" target="_self">rocprofiler_kernel_properties_t</a></td><td class="desc">Kernel properties, this will represent the kernel properties such as its grid size, workgroup size, wave_size </td></tr>
<tr id="row_30_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__pc__sample__t.html" target="_self">rocprofiler_pc_sample_t</a></td><td class="desc">An individual PC sample </td></tr>
<tr id="row_31_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__pool__entry__t.html" target="_self">rocprofiler_pool_entry_t</a></td><td class="desc"></td></tr>
<tr id="row_32_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__pool__properties__t.html" target="_self">rocprofiler_pool_properties_t</a></td><td class="desc"></td></tr>
<tr id="row_33_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__properties__t.html" target="_self">rocprofiler_properties_t</a></td><td class="desc"></td></tr>
<tr id="row_34_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__queue__callbacks__t.html" target="_self">rocprofiler_queue_callbacks_t</a></td><td class="desc"></td></tr>
<tr id="row_35_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__queue__id__t.html" target="_self">rocprofiler_queue_id_t</a></td><td class="desc">Unique ID handle to represent an HSA Queue of type <code>hsa_queue_t</code>, this id can be used by the user to get queue information using <a class="el" href="group__record__queues__group.html#ga740788580af7282cf585f4f35f459520" title="Query Queue Information Data using an allocated data pointer by the user, user can get the size of th...">rocprofiler_query_queue_info</a> </td></tr>
<tr id="row_36_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__queue__index__t.html" target="_self">rocprofiler_queue_index_t</a></td><td class="desc"></td></tr>
<tr id="row_37_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__att__tracer__t.html" target="_self">rocprofiler_record_att_tracer_t</a></td><td class="desc">ATT tracing record structure </td></tr>
<tr id="row_38_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__counter__instance__t.html" target="_self">rocprofiler_record_counter_instance_t</a></td><td class="desc">Counter Instance Structure, it will represent every counter reported in the array of counters reported by every profiler record if counters were needed to be collected </td></tr>
<tr id="row_39_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__counter__value__t.html" target="_self">rocprofiler_record_counter_value_t</a></td><td class="desc">Counter Value Structure </td></tr>
<tr id="row_40_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__counters__instances__count__t.html" target="_self">rocprofiler_record_counters_instances_count_t</a></td><td class="desc">Counters Instances Count Structure, every profiling record has this structure included to report the number of counters collected for this kernel dispatch </td></tr>
<tr id="row_41_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__counters__sampler__t.html" target="_self">rocprofiler_record_counters_sampler_t</a></td><td class="desc"></td></tr>
<tr id="row_42_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__header__t.html" target="_self">rocprofiler_record_header_t</a></td><td class="desc">Generic ROCProfiler record header </td></tr>
<tr id="row_43_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__header__timestamp__t.html" target="_self">rocprofiler_record_header_timestamp_t</a></td><td class="desc">Timestamps (start &amp; end), it will be used for kernel dispatch tracing as well as API Tracing </td></tr>
<tr id="row_44_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__id__t.html" target="_self">rocprofiler_record_id_t</a></td><td class="desc">A unique identifier for every record </td></tr>
<tr id="row_45_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__pc__sample__t.html" target="_self">rocprofiler_record_pc_sample_t</a></td><td class="desc">PC sample record: contains the program counter/instruction pointer observed during periodic sampling of a kernel </td></tr>
<tr id="row_46_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__profiler__t.html" target="_self">rocprofiler_record_profiler_t</a></td><td class="desc">Profiling record, this will represent all the information reported by the profiler regarding kernel dispatches and their counters that were collected by the profiler and requested by the user, this can be used as the type of the flushed records that is reported to the user using <a class="el" href="group__memory__storage__buffer__group.html#ga3e2e1dec6aee727dd1f19aae84041dbe" title="Memory pool buffer callback.">rocprofiler_buffer_callback_t</a> </td></tr>
<tr id="row_47_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__se__att__data__t.html" target="_self">rocprofiler_record_se_att_data_t</a></td><td class="desc">Struct to store the trace data from a shader engine </td></tr>
<tr id="row_48_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__se__spm__data__t.html" target="_self">rocprofiler_record_se_spm_data_t</a></td><td class="desc">Counters, including identifiers to get counter information and Counters values </td></tr>
<tr id="row_49_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__spm__counters__instances__count__t.html" target="_self">rocprofiler_record_spm_counters_instances_count_t</a></td><td class="desc"></td></tr>
<tr id="row_50_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__spm__t.html" target="_self">rocprofiler_record_spm_t</a></td><td class="desc">SPM record, this will represent all the information reported by the SPM regarding counters and their timestamps this can be used as the type of the flushed records that is reported to the user using <a class="el" href="group__memory__storage__buffer__group.html#ga3e2e1dec6aee727dd1f19aae84041dbe" title="Memory pool buffer callback.">rocprofiler_buffer_callback_t</a> </td></tr>
<tr id="row_51_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__record__tracer__t.html" target="_self">rocprofiler_record_tracer_t</a></td><td class="desc">Tracing record, this will represent all the information reported by the tracer regarding APIs and their data that were traced and collected by the tracer and requested by the user, this can be used as the type of the flushed records that is reported to the user using ::rocprofiler_buffer_async_callback_t </td></tr>
<tr id="row_52_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__session__id__t.html" target="_self">rocprofiler_session_id_t</a></td><td class="desc">Session Identifier </td></tr>
<tr id="row_53_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__settings__t.html" target="_self">rocprofiler_settings_t</a></td><td class="desc"></td></tr>
<tr id="row_54_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__spm__parameter__t.html" target="_self">rocprofiler_spm_parameter_t</a></td><td class="desc"></td></tr>
<tr id="row_55_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__thread__id__t.html" target="_self">rocprofiler_thread_id_t</a></td><td class="desc">Holds the thread id </td></tr>
<tr id="row_56_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__timestamp__t.html" target="_self">rocprofiler_timestamp_t</a></td><td class="desc">ROCProfiling Timestamp Type </td></tr>
<tr id="row_57_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__tracer__activity__correlation__id__t.html" target="_self">rocprofiler_tracer_activity_correlation_id_t</a></td><td class="desc">Correlation identifier </td></tr>
<tr id="row_58_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__tracer__api__data__t.html" target="_self">rocprofiler_tracer_api_data_t</a></td><td class="desc">Tracer API Calls Data Handler </td></tr>
<tr id="row_59_"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__tracer__external__id__t.html" target="_self">rocprofiler_tracer_external_id_t</a></td><td class="desc">Tracing external ID </td></tr>
<tr id="row_60_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structrocprofiler__tracer__operation__id__t.html" target="_self">rocprofiler_tracer_operation_id_t</a></td><td class="desc">Tracing Operation ID for HIP/HSA </td></tr>
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
       href="annotated_data_structures.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Data Structures</p>
      </div>
    </a>
    <a class="right-next"
       href="classes.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Data Structure Index</p>
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
