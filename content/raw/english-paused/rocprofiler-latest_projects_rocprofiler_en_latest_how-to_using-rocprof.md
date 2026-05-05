---
title: "Using rocprof &#8212; ROCProfiler 2.0.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler/en/latest/how-to/using-rocprof.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:29:04.544568+00:00
content_hash: "2e3275a5d8c01fa9"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="ROCProfiler is a powerful tool for profiling HIP and ROCm applications on AMD ROCm software" name="description" />
<meta content="ROCProfiler tool usage, ROCProfiler command line, rocprof usage, rocprof user manual, rocprof guide, rocprofv1" name="keywords" />

    <title>Using rocprof &#8212; ROCProfiler 2.0.0 Documentation</title>
  
  
  
  <script data-cfasync="false">
    document.documentElement.dataset.mode = localStorage.getItem("mode") || "";
    document.documentElement.dataset.theme = localStorage.getItem("theme") || "";
  </script>
  
  <!-- Loaded before other Sphinx assets -->
  <link href="../_static/styles/theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../_static/styles/bootstrap.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../_static/styles/pydata-sphinx-theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />

  
  <link href="../_static/vendor/fontawesome/6.5.2/css/all.min.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
  <link rel="preload" as="font" type="font/woff2" crossorigin href="../_static/vendor/fontawesome/6.5.2/webfonts/fa-solid-900.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../_static/vendor/fontawesome/6.5.2/webfonts/fa-brands-400.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../_static/vendor/fontawesome/6.5.2/webfonts/fa-regular-400.woff2" />

    <link rel="stylesheet" type="text/css" href="../_static/pygments.css?v=a746c00c" />
    <link rel="stylesheet" type="text/css" href="../_static/styles/sphinx-book-theme.css?v=eba8b062" />
    <link rel="stylesheet" type="text/css" href="../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
    <link rel="stylesheet" type="text/css" href="../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../_static/design-style.1e8bd061cd6da7fc9cf755528e8ffc24.min.css?v=0a3b3ea7" />
  
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b" />
<link rel="preload" as="script" href="../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b" />
  <script src="../_static/vendor/fontawesome/6.5.2/js/all.min.js?digest=dfe6caa3a7d634c4db9b"></script>

    <script src="../_static/documentation_options.js?v=ce394494"></script>
    <script src="../_static/doctools.js?v=9a2dae69"></script>
    <script src="../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../_static/search.js?v=90a4452c"></script>
    <script src="../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
    <script src="../_static/design-tabs.js?v=36754332"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/using-rocprof';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="rocprof command help" href="rocprof-command.html" />
    <link rel="prev" title="Installing ROCProfilerV2" href="../install/installv2.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-docs" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/using-rocprof.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
      action="../search.html"
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
                    <img src="../_static/images/amd-header-logo.svg" alt="AMD Logo" title="AMD Logo" width="90" class="d-inline-block align-text-top hover-opacity"/>
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

  
    
  

<a class="navbar-brand logo" href="../index.html">
  
  
  
  
  
  
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
<li class="toctree-l1"><a class="reference internal" href="../install/installv1.html">Installing ROCProfiler</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/installv2.html">Installing ROCProfilerV2</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Tutorials</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/hip-tests/blob/develop/samples/2_Cookbook/0_MatrixTranspose">MatrixTranspose application</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples/">ROCm examples</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/HIP-Examples/tree/master">HIP examples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Using rocprof</a></li>
<li class="toctree-l1"><a class="reference internal" href="rocprof-command.html">rocprof command help</a></li>
<li class="toctree-l1"><a class="reference internal" href="rocprofv2-usage.html">Using rocprofv2</a></li>
<li class="toctree-l1"><a class="reference internal" href="rocprofv2-command.html">rocprofv2 command help</a></li>
<li class="toctree-l1"><a class="reference internal" href="using-rocsys.html">Using rocsys</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">References</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../reference/rocprofiler_spec.html">ROCProfiler library specification</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../doxygen/html/index.html">ROCProfiler API library</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../doxygen/html/modules.html">Modules</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../doxygen/html/annotated_data_structures.html">Data Structures</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/classes.html">Data Structure Index</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../doxygen/html/functions_data_fields.html">Data Fields</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_all.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_vars_variables.html">Variables</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../doxygen/html/files_files.html">Files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/files.html">File List</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../doxygen/html/globals_globals.html">Globals</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_all.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_func.html">Functions</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_type.html">Typedefs</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_enum.html">Enumerations</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_eval.html">Enumerator</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/globals_defs.html">Macros</a></li>
</ul>
</details></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/rocprofilerv2-api.html">ROCProfilerV2 API</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">About</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../license.html">License</a></li>
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
      <a href="../index.html" class="nav-link" aria-label="Home">
        <i class="fa-solid fa-home"></i>
      </a>
    </li>
    <li class="breadcrumb-item active" aria-current="page">Using rocprof</li>
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
<button class="sidebar-toggle secondary-toggle btn btn-sm" title="Toggle secondary sidebar" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <span class="fa-solid fa-list"></span>
</button>
</div></div>
      
    </div>
  
</div>
</div>
              
              

<div id="jb-print-docs-body" class="onlyprint">
    <h1>Using rocprof</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#application-tracing">Application tracing</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#command-line-options-for-application-tracing">Command-line options for application tracing</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-trace">HIP Trace</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#statistics-files">Statistics Files</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hsa-trace">HSA Trace</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#system-trace">System Trace</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#roctx-trace">ROCTx Trace</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#tracing-control">Tracing Control</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filter-tasks">Filter Tasks</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#adjust-trace-flush-rate">Adjust Trace Flush Rate</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#function-name-truncation">Function Name Truncation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#tracing-control-for-api-or-code-block">Tracing Control for API or Code Block</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#set-initial-delay-periodic-sample-length-and-rate">Set Initial Delay, Periodic Sample Length and Rate</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#roctracer-api">ROCTracer API</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#performance-counter-collection">Performance Counter Collection</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#command-line-options-for-counter-collection">Command-line options for counter collection</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#listing-performance-counters">Listing Performance Counters</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#using-rocprof-for-application-profiling">Using <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> for Application Profiling</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#input-file">Input file</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#metric-file">Metric File</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#generated-output">Generated Output</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#profiling-multiple-mpi-ranks">Profiling Multiple MPI Ranks</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="using-rocprof">
<span id="id1"></span><h1>Using rocprof<a class="headerlink" href="#using-rocprof" title="Link to this heading">#</a></h1>
<p><code class="docutils literal notranslate"><span class="pre">rocprof</span></code> is a powerful tool for profiling <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/index.html" title="(in HIP Documentation v7.2.53211)"><span class="xref std std-doc">HIP</span></a> applications on AMD ROCm platforms. It can be used to identify performance bottlenecks in applications and to optimize their performance. <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> provides a variety of profiling data, including performance counters, hardware traces, and runtime API/activity traces.  This document provides a detailed description of the features and usage of the <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> command-line tool.</p>
<p>To demonstrate the usage of <code class="docutils literal notranslate"><span class="pre">rocprof</span></code>, this document refers to
the <a class="reference external" href="https://github.com/ROCm/hip-tests/blob/develop/samples/2_Cookbook/0_MatrixTranspose">MatrixTranspose application</a> as an example.</p>
<p>To see all the <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> options, refer to <a class="reference internal" href="rocprof-command.html#rocprof-command"><span class="std std-ref">rocprof command help</span></a>, or run the following from the command line:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>--help
</pre></div>
</div>
<section id="application-tracing">
<h2>Application tracing<a class="headerlink" href="#application-tracing" title="Link to this heading">#</a></h2>
<p>Application tracing provides the big picture of a program’s execution by collecting data on the execution times of API calls and GPU commands, such as kernel execution, async memory copy, and barrier packets. This information can be used as the first step in the profiling process to answer important questions, such as which kernel took the longest time to execute, and what percentage of time was spent on memory copy.</p>
<p>There are two ways to use application tracing: <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> and <code class="docutils literal notranslate"><span class="pre">ROCTracer</span></code> API.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rocprof</span></code> is a command line interface (CLI) profiler that can be used on the applications running on ROCm-supported GPUs, without the requirement of any code modification in the application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCTracer</span></code> API is a library that requires minor code modification in the application to be traced but provides greater flexibility, such as adjusting execution based on profiling results.</p></li>
</ul>
<section id="command-line-options-for-application-tracing">
<span id="trace-options"></span><h3>Command-line options for application tracing<a class="headerlink" href="#command-line-options-for-application-tracing" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> CLI allows you to trace the entire execution of <cite>HIP</cite> applications. It allows tracing at different levels such as <cite>HIP</cite>-level, <cite>HSA</cite>-level, and system-level. These levels can be selected by supplying the respective command-line options to <cite>rocprof</cite>.</p>
<p>The command-line options used with <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> for tracing:</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 28.6%" />
<col style="width: 71.4%" />
</colgroup>
<tbody>
<tr class="row-odd"><td><p><strong>Options</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">-d</span> <span class="pre">&lt;output</span> <span class="pre">directory&gt;</span></code></p></td>
<td><p>To specify the directory where the profiler stores traces and the profiling data. The profiler stores the profiling data in a temporary directory [/tmp] by default, which is removed automatically after a specific period. Specifying a directory explicitly allows you to prevent loss of data.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">--hip-trace</span></code></p></td>
<td><p>To trace API execution stats, <cite>HIP</cite> API calls, and copy operation calls.|br| For more information refer to <a class="reference internal" href="#trace-hip"><span class="std std-ref">HIP Trace</span></a>.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">--hsa-trace</span></code></p></td>
<td><p>To trace API execution stats, <cite>HIP</cite> API calls, and copy operation calls.|br| For more information refer to <a class="reference internal" href="#trace-hsa"><span class="std std-ref">HSA Trace</span></a>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">--roctx-trace</span></code></p></td>
<td><p>To enable <code class="docutils literal notranslate"><span class="pre">roctx</span></code> application code annotation trace. Allows you to trace a particular block of code when Markers and Ranges are specified in the application code. <br /> For more information refer to <a class="reference internal" href="#trace-roctx"><span class="std std-ref">ROCTx Trace</span></a>.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">--stats</span></code></p></td>
<td><p>To trace API execution stats and kernel execution stats. <br /> For more information refer to <span class="xref std std-ref">stats-file</span>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">--sys-trace</span></code></p></td>
<td><p>To trace API execution stats, <cite>HIP</cite> and <cite>HSA</cite> API calls, and copy operation calls. <br /> For more information refer to <a class="reference internal" href="#trace-sys"><span class="std std-ref">System Trace</span></a>.</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="hip-trace">
<span id="trace-hip"></span><h3>HIP Trace<a class="headerlink" href="#hip-trace" title="Link to this heading">#</a></h3>
<p>Use the <code class="docutils literal notranslate"><span class="pre">--hip-trace</span></code> option to collect execution trace data for the entire application with <code class="docutils literal notranslate"><span class="pre">rocprof</span></code>, including <code class="docutils literal notranslate"><span class="pre">HIP</span></code> API functions and their asynchronous activities at the runtime level.</p>
<p><strong>Usage:</strong></p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>-d<span class="w"> </span>outputFolder<span class="w"> </span>--hip-trace<span class="w"> </span>./Matrixtranspose
</pre></div>
</div>
<p>The above command generates three groups of files: viewable trace data, statistics files, and intermediate tracing data.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This document does not discuss the intermediate tracing data as it is not designed to be read by users.</p>
</div>
<p><strong>Viewable Trace Data</strong></p>
<p>The viewable trace data is available in <code class="docutils literal notranslate"><span class="pre">results.json</span></code>, which is a <code class="docutils literal notranslate"><span class="pre">JSON</span></code> file that follows the Chromium Project’s <a class="reference external" href="https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/edit">trace-event format</a>. You can view the trace using viewing tools such as <cite>Chrome Tracing &lt;chrome://tracing/&gt;</cite> or <a class="reference external" href="https://ui.perfetto.dev">Perfetto UI</a>. In the following figure a short segment of the trace data is viewed:</p>
<figure class="align-default" id="id5">
<img alt="Viewing HIP Trace" src="../_images/hip_trace.svg" /><figcaption>
<p><span class="caption-text">Viewing HIP Trace</span><a class="headerlink" href="#id5" title="Link to this image">#</a></p>
</figcaption>
</figure>
<p>In the time axis at the top of the following figure there is a small, highlighted region between 0.22s to 0.24s, that indicates the currently selected time range.</p>
<figure class="align-default" id="id6">
<img alt="Time Range" src="../_images/hip_trace_time_range.svg" /><figcaption>
<p><span class="caption-text">Time Range</span><a class="headerlink" href="#id6" title="Link to this image">#</a></p>
</figcaption>
</figure>
<p>Below the time axis in the following figure there are Gantt chart-style boxes that show the duration of each task. There are three rows of tasks divided by the black rows mentioning their categories. The first row is the <cite>CPU HIP API</cite>, which lists the execution time of each API trace.</p>
<figure class="align-default" id="id7">
<img alt="Duration of API Trace Execution" src="../_images/hip_api_execution.svg" /><figcaption>
<p><span class="caption-text">Duration of API Trace Execution</span><a class="headerlink" href="#id7" title="Link to this image">#</a></p>
</figcaption>
</figure>
<p>In the following figure the second row titled <cite>COPY</cite> shows the tasks completed by the copy engine. See that the <code class="docutils literal notranslate"><span class="pre">CopyHostToDevice</span></code> and <code class="docutils literal notranslate"><span class="pre">CopyDeviceToHost</span></code> tasks are being completed at the beginning and the end of the time range, respectively.</p>
<figure class="align-default" id="id8">
<img alt="Trace of Copy Tasks" src="../_images/hip_copy_tasks.svg" /><figcaption>
<p><span class="caption-text">Copy Tasks</span><a class="headerlink" href="#id8" title="Link to this image">#</a></p>
</figcaption>
</figure>
<p>In the following figure the GPU tasks are listed at the bottom. Note that the <code class="docutils literal notranslate"><span class="pre">matrixTranspose</span></code> kernel is executed from about 0.185s to 0.20s.</p>
<figure class="align-default" id="id9">
<img alt="Trace of GPU Tasks" src="../_images/hip_gpu_tasks.svg" /><figcaption>
<p><span class="caption-text">GPU Tasks</span><a class="headerlink" href="#id9" title="Link to this image">#</a></p>
</figcaption>
</figure>
<section id="statistics-files">
<h4>Statistics Files<a class="headerlink" href="#statistics-files" title="Link to this heading">#</a></h4>
<p>The statistics files include:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">results.stats.csv</span></code> for kernel statistics</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">results.hip_stats.csv</span></code> for <code class="docutils literal notranslate"><span class="pre">HIP</span></code> API</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">results.copy_stats.csv</span></code> for activity statistics</p></li>
</ul>
<p>The files are organized in comma-separated values (CSV) format, with the columns:</p>
<ul class="simple">
<li><p><strong>Name:</strong> Name of the action</p></li>
<li><p><strong>Calls:</strong> Number of invocations</p></li>
<li><p><strong>TotalDurationNS:</strong> Total duration in nanosecond</p></li>
<li><p><strong>AverageNS:</strong> Average time in nanoseconds required to execute the action</p></li>
<li><p><strong>Percentage:</strong> Percentage of the action with respect to the complete execution of the application</p></li>
</ul>
</section>
</section>
<section id="hsa-trace">
<span id="trace-hsa"></span><h3>HSA Trace<a class="headerlink" href="#hsa-trace" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">HIP</span></code> runtime library is implemented with the low-level <code class="docutils literal notranslate"><span class="pre">HSA</span></code> runtime. To trace the application at a lower level, you can use <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> to collect application traces at the <code class="docutils literal notranslate"><span class="pre">HSA</span></code> runtime level. In general, tracing at the <code class="docutils literal notranslate"><span class="pre">HIP</span></code>-level is recommended for most users. You are advised to use <code class="docutils literal notranslate"><span class="pre">HSA</span></code> trace only if you are familiar with <code class="docutils literal notranslate"><span class="pre">HSA</span></code> runtime.</p>
<p><code class="docutils literal notranslate"><span class="pre">HSA</span></code> trace contains the start/end time of <code class="docutils literal notranslate"><span class="pre">HSA</span></code> runtime API calls and their asynchronous activities. Use the <code class="docutils literal notranslate"><span class="pre">--hsa-trace</span></code> option with rocprof to collect <code class="docutils literal notranslate"><span class="pre">HSA</span></code>-level trace:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>--hsa-trace<span class="w"> </span>./MatrixTranspose
</pre></div>
</div>
<p>As in <code class="docutils literal notranslate"><span class="pre">HIP</span></code> trace, the generated <code class="docutils literal notranslate"><span class="pre">HSA</span></code> trace also includes three groups of files, namely viewable traces, statistics files, and intermediate tracing data. You can visualize the generated <code class="docutils literal notranslate"><span class="pre">results.json</span></code> using third-party tools such as Perfetto, as shown in the following figure.</p>
<figure class="align-default" id="id10">
<img alt="Viewing HSA Trace" src="../_images/hsa_trace.svg" /><figcaption>
<p><span class="caption-text">Viewing HSA Trace</span><a class="headerlink" href="#id10" title="Link to this image">#</a></p>
</figcaption>
</figure>
<p>In the preceding figure you can see that <code class="docutils literal notranslate"><span class="pre">HSA</span></code> trace shows <code class="docutils literal notranslate"><span class="pre">HSA</span></code> trace rows, just like <code class="docutils literal notranslate"><span class="pre">HIP</span></code> trace shows the <code class="docutils literal notranslate"><span class="pre">HIP</span></code> API row in <cite>{numref}hip-trace-visualize</cite>. However, note that there are more <code class="docutils literal notranslate"><span class="pre">HSA</span></code> API calls as compared to <code class="docutils literal notranslate"><span class="pre">HIP</span></code> API calls because <code class="docutils literal notranslate"><span class="pre">HSA</span></code> works closer to the hardware.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>GPU ID in the <cite>HSA</cite> visualization is always 0.</p>
</div>
<p>The statistics files are:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">results.stats.csv</span></code> for kernel statistics</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">results.hsa_stats.csv</span></code> for <cite>HSA</cite> API</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">results.copy_stats.csv</span></code> for memory copy statistics</p></li>
</ul>
<p>Each file is a CSV table with columns as described in the <span class="xref std std-ref">stats-file</span>.</p>
</section>
<section id="system-trace">
<span id="trace-sys"></span><h3>System Trace<a class="headerlink" href="#system-trace" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> tool can also generate both the <code class="docutils literal notranslate"><span class="pre">HIP</span></code> and <code class="docutils literal notranslate"><span class="pre">HSA</span></code> traces together with the <code class="docutils literal notranslate"><span class="pre">--sys-trace</span></code> option.</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>--sys-trace<span class="w"> </span>./MatrixTranspose
</pre></div>
</div>
<p>The following figure shows the generated <code class="docutils literal notranslate"><span class="pre">results.json</span></code> visualized using Perfetto. It contains sections from both <code class="docutils literal notranslate"><span class="pre">HIP</span></code> and <code class="docutils literal notranslate"><span class="pre">HSA</span></code> trace.</p>
<figure class="align-default" id="id11">
<img alt="Viewing Sys Trace" src="../_images/sys_trace.svg" /><figcaption>
<p><span class="caption-text">Viewing Sys Trace</span><a class="headerlink" href="#id11" title="Link to this image">#</a></p>
</figcaption>
</figure>
</section>
<section id="roctx-trace">
<span id="trace-roctx"></span><h3>ROCTx Trace<a class="headerlink" href="#roctx-trace" title="Link to this heading">#</a></h3>
<p>In certain situations, such as debugging performance issues in large-scale GPU programs, API-level tracing may be too fine-grained to provide a big picture of the program execution. In such cases, you might find it helpful to define specific tasks to be traced.</p>
<p>To specify the tasks for tracing, enclose the respective source code with the API calls provided by <code class="docutils literal notranslate"><span class="pre">roctx</span></code>. This process is also known as instrumentation. As the scope of code for instrumentation is defined using the enclosing API calls, it is called a range. A range is a programmer-defined task that has a well-defined start and end code scope. You can also fine grain the scope specified within a range using further nested ranges. The <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> tool also reports the timelines for these nested ranges.</p>
<p>Here is a list of useful APIs for code instrumentation.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">roctxMark</span></code>: Inserts a marker in the code with a message. Creating marks can help you see when a line of code is executed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roctxRangeStart</span></code>: Starts a range. Ranges can be started by different threads.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roctxRangePush</span></code>: Starts a new nested range.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roctxRangePop</span></code>: Stops the current nested range.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roctxRangeStop</span></code>: Stops the given range.</p></li>
</ul>
<p>See <code class="docutils literal notranslate"><span class="pre">roctx</span></code> code annotations in the <code class="docutils literal notranslate"><span class="pre">MatrixTranspose</span></code> application below:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>roctxMark<span class="o">(</span><span class="s2">&quot;before hipLaunchKernel&quot;</span><span class="o">)</span><span class="p">;</span>
int<span class="w"> </span><span class="nv">rangeId</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>roctxRangeStart<span class="o">(</span><span class="s2">&quot;hipLaunchKernel range&quot;</span><span class="o">)</span><span class="p">;</span>
roctxRangePush<span class="o">(</span><span class="s2">&quot;hipLaunchKernel&quot;</span><span class="o">)</span><span class="p">;</span>

//<span class="w"> </span>Lauching<span class="w"> </span>kernel<span class="w"> </span>from<span class="w"> </span>host
hipLaunchKernelGGL<span class="o">(</span>matrixTranspose,<span class="w"> </span>dim3<span class="o">(</span>WIDTH/THREADS_PER_BLOCK_X,<span class="w"> </span>WIDTH/THREADS_PER_BLOCK_Y<span class="o">)</span>,<span class="w"> </span>dim3<span class="o">(</span>THREADS_PER_BLOCK_X,<span class="w"> </span>THREADS_PER_BLOCK_Y<span class="o">)</span>,<span class="w"> </span><span class="m">0</span>,0,gpuTransposeMatrix,gpuMatrix,<span class="w"> </span>WIDTH<span class="o">)</span><span class="p">;</span>

roctxMark<span class="o">(</span><span class="s2">&quot;after hipLaunchKernel&quot;</span><span class="o">)</span><span class="p">;</span>

//<span class="w"> </span>Memory<span class="w"> </span>transfer<span class="w"> </span>from<span class="w"> </span>device<span class="w"> </span>to<span class="w"> </span>host
roctxRangePush<span class="o">(</span><span class="s2">&quot;hipMemcpy&quot;</span><span class="o">)</span><span class="p">;</span>

hipMemcpy<span class="o">(</span>TransposeMatrix,<span class="w"> </span>gpuTransposeMatrix,<span class="w"> </span>NUM<span class="w"> </span>*<span class="w"> </span>sizeof<span class="o">(</span>float<span class="o">)</span>,<span class="w"> </span>hipMemcpyDeviceToHost<span class="o">)</span><span class="p">;</span>

roctxRangePop<span class="o">()</span><span class="p">;</span><span class="w">  </span>//<span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="s2">&quot;hipMemcpy&quot;</span>
roctxRangePop<span class="o">()</span><span class="p">;</span><span class="w">  </span>//<span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="s2">&quot;hipLaunchKernel&quot;</span>
roctxRangeStop<span class="o">(</span>rangeId<span class="o">)</span><span class="p">;</span>
</pre></div>
</div>
<div class="admonition tip">
<p class="admonition-title">Tip</p>
<p>A version of the <a class="reference external" href="https://github.com/ROCm/rocprofiler/blob/amd-master/tests-v2/featuretests/tracer/apps/MatrixTranspose.cpp">MatrixTranspose application</a>
instrumented using the ROCTx API is available in the
<a class="reference external" href="https://github.com/ROCm/rocprofiler/blob/amd-master/tests-v2/">rocprofiler/tests-v2</a>
folder on GitHub.</p>
</div>
<p>Using <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> with <code class="docutils literal notranslate"><span class="pre">roctx-trace</span></code> option:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>-d<span class="w"> </span>outputFolder<span class="w"> </span>--roctx-trace<span class="w"> </span>./
</pre></div>
</div>
<p>You can visualize the generated output file <code class="docutils literal notranslate"><span class="pre">results.json</span></code> using Perfetto as shown in the following figure. The sections <cite>Markers</cite> and <cite>Ranges</cite> show the marked events and ranges.</p>
<figure class="align-default" id="id12">
<img alt="Viewing Roctx Trace" src="../_images/roctx_trace.svg" /><figcaption>
<p><span class="caption-text">Viewing Roctx Trace</span><a class="headerlink" href="#id12" title="Link to this image">#</a></p>
</figcaption>
</figure>
</section>
</section>
<section id="tracing-control">
<h2>Tracing Control<a class="headerlink" href="#tracing-control" title="Link to this heading">#</a></h2>
<p>The <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> tool provides these customization options:</p>
<section id="filter-tasks">
<h3>Filter Tasks<a class="headerlink" href="#filter-tasks" title="Link to this heading">#</a></h3>
<p>To filter tasks, specify the trace category and the tasks to be traced in an input file.</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>cat<span class="w"> </span>input.txt
hsa<span class="w"> </span>:<span class="w"> </span>hsa_queue_create<span class="w"> </span>hsa_amd_memory_pool_allocate
</pre></div>
</div>
<p>Then supply this input file to <code class="docutils literal notranslate"><span class="pre">rocprof</span></code>.</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>-i<span class="w"> </span>input.txt<span class="w"> </span>--hsa-trace<span class="w"> </span>./MatrixTranspose
</pre></div>
</div>
<p>The above sample input file generates <code class="docutils literal notranslate"><span class="pre">HSA</span></code> tracing information for only the two events specified in the file.</p>
</section>
<section id="adjust-trace-flush-rate">
<span id="trace-flush"></span><h3>Adjust Trace Flush Rate<a class="headerlink" href="#adjust-trace-flush-rate" title="Link to this heading">#</a></h3>
<p>Use the <code class="docutils literal notranslate"><span class="pre">--flush-rate</span></code> option to specify the flush rate in seconds, milliseconds, or microseconds. This determines how often the trace data is dumped to files. In the following example the flush rate is set to 10 microseconds:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>--flush-rate<span class="w"> </span>10us<span class="w"> </span>--hsa-trace<span class="w"> </span>./MatrixTranspose
</pre></div>
</div>
</section>
<section id="function-name-truncation">
<span id="func-trunc"></span><h3>Function Name Truncation<a class="headerlink" href="#function-name-truncation" title="Link to this heading">#</a></h3>
<p>To truncate the kernel full function name in the trace files to the base name of the function, use <code class="docutils literal notranslate"><span class="pre">--basename</span></code> as shown in the following example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>rocprof<span class="w"> </span>--basename<span class="w"> </span>on<span class="w"> </span>--hip-trace<span class="w"> </span>./MatrixTranspose

<span class="s2">&quot;Name&quot;</span>,<span class="s2">&quot;Calls&quot;</span>,<span class="s2">&quot;TotalDurationNs&quot;</span>,<span class="s2">&quot;AverageNs&quot;</span>,<span class="s2">&quot;Percentage&quot;</span>
<span class="s2">&quot;vectoradd_float&quot;</span>,1,46373,46373,100.0
</pre></div>
</div>
<p>When <code class="docutils literal notranslate"><span class="pre">--basename</span></code> is not explicitly enabled, the full kernel function name is displayed in the trace:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>rocprof<span class="w"> </span>--basename<span class="w"> </span>off<span class="w"> </span>--hip-trace<span class="w"> </span>./MatrixTranspose

<span class="s2">&quot;Name&quot;</span>,<span class="s2">&quot;Calls&quot;</span>,<span class="s2">&quot;TotalDurationNs&quot;</span>,<span class="s2">&quot;AverageNs&quot;</span>,<span class="s2">&quot;Percentage&quot;</span>
<span class="s2">&quot;vectoradd_float(float*, float const*, float const*, int, int)&quot;</span>,1,45633,45633,100.0
</pre></div>
</div>
</section>
<section id="tracing-control-for-api-or-code-block">
<span id="trace-start"></span><h3>Tracing Control for API or Code Block<a class="headerlink" href="#tracing-control-for-api-or-code-block" title="Link to this heading">#</a></h3>
<p>To enable selective tracing for a <code class="docutils literal notranslate"><span class="pre">HIP</span></code> API or code block instead of the entire application, follow these steps:</p>
<ol class="arabic simple">
<li><p>Enclose the API or code block within <cite>roctracer_start()</cite> and <cite>roctracer_stop()</cite>. This ensures that tracing starts only when it encounters <cite>roctracer_start()</cite> and stops once it encounters <cite>roctracer_stop()</cite>. See the usage of these API calls here, where the user wants to trace only <cite>hipMemcpy()</cite> API:</p></li>
</ol>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="c1">#include &lt;roctracer/include/roctracer_ext.h&gt;</span>

//<span class="w"> </span>allocate<span class="w"> </span>the<span class="w"> </span>memory<span class="w"> </span>on<span class="w"> </span>the<span class="w"> </span>device<span class="w"> </span>side
hipMalloc<span class="o">((</span>void**<span class="o">)</span><span class="p">&amp;</span>gpuMatrix,<span class="w"> </span>NUM<span class="w"> </span>*<span class="w"> </span>sizeof<span class="o">(</span>float<span class="o">))</span><span class="p">;</span>
hipMalloc<span class="o">((</span>void**<span class="o">)</span><span class="p">&amp;</span>gpuTransposeMatrix,<span class="w"> </span>NUM<span class="w"> </span>*<span class="w"> </span>sizeof<span class="o">(</span>float<span class="o">))</span><span class="p">;</span>

roctracer_start<span class="o">()</span><span class="p">;</span>

//<span class="w"> </span>Memory<span class="w"> </span>transfer<span class="w"> </span>from<span class="w"> </span>host<span class="w"> </span>to<span class="w"> </span>device
hipMemcpy<span class="o">(</span>gpuMatrix,<span class="w"> </span>Matrix,<span class="w"> </span>NUM<span class="w"> </span>*<span class="w"> </span>sizeof<span class="o">(</span>float<span class="o">)</span>,<span class="w"> </span>hipMemcpyHostToDevice<span class="o">)</span><span class="p">;</span>

roctracer_stop<span class="o">()</span><span class="p">;</span>
</pre></div>
</div>
<ol class="arabic simple" start="2">
<li><p>Use <cite>–trace-start</cite> off to disable application tracing from the beginning and start tracing only when <cite>roctracer_start()</cite> is encountered.</p></li>
</ol>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>rocprof<span class="w"> </span>--trace-start<span class="w"> </span>off<span class="w"> </span>--hip-trace<span class="w"> </span>MatrixTranspose

cat<span class="w"> </span>results.hip_stats.csv
<span class="s2">&quot;Name&quot;</span>,<span class="s2">&quot;Calls&quot;</span>,<span class="s2">&quot;TotalDurationNs&quot;</span>,<span class="s2">&quot;AverageNs&quot;</span>,<span class="s2">&quot;Percentage&quot;</span>
<span class="s2">&quot;hipMemcpy&quot;</span>,10,255048886,25504888,100.0
</pre></div>
</div>
</section>
<section id="set-initial-delay-periodic-sample-length-and-rate">
<span id="trace-period"></span><h3>Set Initial Delay, Periodic Sample Length and Rate<a class="headerlink" href="#set-initial-delay-periodic-sample-length-and-rate" title="Link to this heading">#</a></h3>
<p>Use option <cite>-trace-period &lt;delay:length:rate&gt;</cite> to fine tune tracing by setting the following attributes:</p>
<ul class="simple">
<li><p><strong>Initial Delay:</strong> The time interval between the start of the profiler and start of tracing. So an initial delay of 10 ms causes the tracing to commence after 10 ms since the start of the profiler.</p></li>
<li><p><strong>Periodic Sample Length:</strong> The duration for which tracing runs</p></li>
<li><p><strong>Rate:</strong> Rate at which the tracing results are flushed to the user</p></li>
</ul>
<p><strong>Example:</strong> Tracing with a delay of 10ms, length of 1ms and rate of 10ms</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>rocprof<span class="w"> </span>--hip-trace<span class="w"> </span>--trace-period<span class="w"> </span>10ms:1ms:10ms<span class="w"> </span>MatrixTranspose

cat<span class="w"> </span>results.hip_stats.csv
<span class="s2">&quot;Name&quot;</span>,<span class="s2">&quot;Calls&quot;</span>,<span class="s2">&quot;TotalDurationNs&quot;</span>,<span class="s2">&quot;AverageNs&quot;</span>,<span class="s2">&quot;Percentage&quot;</span>
<span class="s2">&quot;hipMemcpy&quot;</span>,6,6358906,1059817,100.0
</pre></div>
</div>
<p><strong>Example:</strong> Tracing with a delay of 10ms, length of 1ms and rate of 1ms</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>rocprof<span class="w"> </span>--hip-trace<span class="w"> </span>--trace-period<span class="w"> </span>10ms:1ms:1ms<span class="w"> </span>MatrixTranspose

cat<span class="w"> </span>results.hip_stats.csv
<span class="s2">&quot;Name&quot;</span>,<span class="s2">&quot;Calls&quot;</span>,<span class="s2">&quot;TotalDurationNs&quot;</span>,<span class="s2">&quot;AverageNs&quot;</span>,<span class="s2">&quot;Percentage&quot;</span>
<span class="s2">&quot;hipMemcpy&quot;</span>,11,272473856,24770350,99.9468484848238
<span class="s2">&quot;hipMalloc&quot;</span>,2,102871,51435,0.037734380837192355
<span class="s2">&quot;hipFree&quot;</span>,2,39940,19970,0.014650495967157534
<span class="s2">&quot;hipGetDeviceProperties&quot;</span>,1,2090,2090,0.0007666383718417439
</pre></div>
</div>
</section>
</section>
<section id="roctracer-api">
<h2>ROCTracer API<a class="headerlink" href="#roctracer-api" title="Link to this heading">#</a></h2>
<p>The <cite>ROCTracer</cite> APIs are runtime-independent APIs for tracing runtime calls and asynchronous activity, like GPU kernel dispatches and memory moves. The tracing includes callback API for
runtime API tracing and activity API for asynchronous activity records logging.
You can utilize these APIs to develop a tracing tool or to implement tracing within an application. Refer to the <a class="reference external" href="https://github.com/ROCm-Developer-Tools/roctracer/blob/amd-master/doc/roctracer_spec.md">ROCTracer API Specification</a> for more information.</p>
<p>To use the <cite>ROCTracer</cite> API, link the application with <cite>ROCTracer</cite> using the API header and dynamic library as shown below:</p>
<ul class="simple">
<li><p><strong>API header:</strong> <cite>/opt/rocm-{version}/include/roctracer/roctracer.h</cite></p></li>
<li><p><strong>Dynamic library (.so):</strong> <cite>/opt/rocm-{version}/lib/libroctracer64.so.&lt;version major&gt;</cite></p></li>
</ul>
</section>
<section id="performance-counter-collection">
<h2>Performance Counter Collection<a class="headerlink" href="#performance-counter-collection" title="Link to this heading">#</a></h2>
<p>As discussed in the sections above, the application trace mode is limited to providing an overview of program execution and does not provide an insight into kernel execution. To address performance issues, the counter and metric collection functionality of <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> can be used to report hardware component performance metrics during kernel execution.</p>
<p>Counter and metric collection is supported on the following GPUs:</p>
<ul class="simple">
<li><p>AMD Radeon Instinct MI25, MI50, MI100, MI2XX</p></li>
<li><p>AMD Radeon VII, Radeon Pro VII</p></li>
</ul>
<section id="command-line-options-for-counter-collection">
<span id="counter-options"></span><h3>Command-line options for counter collection<a class="headerlink" href="#command-line-options-for-counter-collection" title="Link to this heading">#</a></h3>
<p>The command-line options used with <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> for profiling:</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 28.6%" />
<col style="width: 71.4%" />
</colgroup>
<tbody>
<tr class="row-odd"><td><p><strong>Options</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">--list-basic</span></code></p></td>
<td><p>To print the list of basic hardware counters. <br /> For more information refer to <a class="reference internal" href="#listing-counters"><span class="std std-ref">Listing Performance Counters</span></a>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">--list-derived</span></code></p></td>
<td><p>To print the list of derived metrics with formulas.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">-i</span> <span class="pre">&lt;.txt/.xml</span> <span class="pre">file&gt;</span></code></p></td>
<td><p>To retrieve the values of the desired list of basic counters and/or derived metrics. <br /> For more information refer to <a class="reference internal" href="#input-file"><span class="std std-ref">Input file</span></a>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">-m</span> <span class="pre">&lt;.xml</span> <span class="pre">file&gt;</span></code></p></td>
<td><p>To define new derived metrics or modify the existing metrics defined in the <cite>metrics.xml</cite> by default. <br /> For more information refer to <a class="reference internal" href="#metric-file"><span class="std std-ref">Metric File</span></a>.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">-o</span> <span class="pre">&lt;output</span> <span class="pre">file.csv&gt;</span></code></p></td>
<td><p>Specify a name for the output file generated when used with <code class="docutils literal notranslate"><span class="pre">-i</span></code>. <br /> For more information refer to <a class="reference internal" href="#output-file"><span class="std std-ref">Generated Output</span></a>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">--timestamp</span> <span class="pre">&lt;on/off&gt;</span></code></p></td>
<td><p>To enable or disable the kernel dispatch timestamps in nanoseconds for events such as dispatch, begin, end, and complete, as described in the following. Default value: <code class="docutils literal notranslate"><span class="pre">on</span></code>. <br /> For more information refer to <a class="reference internal" href="#output-file"><span class="std std-ref">Generated Output</span></a>. <br /> * <code class="docutils literal notranslate"><span class="pre">DispatchNs</span></code>: indicates the time when the GPU receives notification to work on a specific kernel as the kernel Architected Queuing Language (AQL) dispatch packet is submitted to the queue. <br /> * <code class="docutils literal notranslate"><span class="pre">BeginNs</span></code>: indicates when the kernel begins execution <br /> * <code class="docutils literal notranslate"><span class="pre">EndNs</span></code>: time when the kernel finishes execution <br /> * <code class="docutils literal notranslate"><span class="pre">CompleteNs</span></code>: inidcates the time when the system receives notification from the GPU about completion of work by the kernel through the completion signal of the AQL dispatch packet.</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="listing-performance-counters">
<span id="listing-counters"></span><h3>Listing Performance Counters<a class="headerlink" href="#listing-performance-counters" title="Link to this heading">#</a></h3>
<p>AMD GPUs are equipped with hardware performance counters that can be used to measure specific values during kernel execution, which are then exported from the GPU and written into the output files at the end of the kernel execution. These performance counters vary according to the GPU. Therefore, it is recommended to examine the hardware counters that can be collected before running the profile.</p>
<p>There are two types of data available for profiling: hardware basic counters and derived metrics.</p>
<p>To obtain the list of supported basic counters, use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>--list-basic
</pre></div>
</div>
<p>The derived metrics are calculated from the basic counters using mathematical expressions. To list the supported derived metrics along with their mathematical expressions, use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>--list-derived
</pre></div>
</div>
<p>You can also customize the derived metrics as explained in <a class="reference internal" href="#metric-file"><span class="std std-ref">Metric File</span></a>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The output generated from the <code class="docutils literal notranslate"><span class="pre">--list_basic</span></code> and <code class="docutils literal notranslate"><span class="pre">--list_derived</span></code> commands can be significant, and is sometimes worth capturing by redirecting the output to a file.</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>--list-derived<span class="w"> </span>./MatrixTranspose<span class="w"> </span>&gt;<span class="w"> </span>output.txt
</pre></div>
</div>
</div>
</section>
</section>
<section id="using-rocprof-for-application-profiling">
<h2>Using <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> for Application Profiling<a class="headerlink" href="#using-rocprof-for-application-profiling" title="Link to this heading">#</a></h2>
<p>To profile kernels in GPU applications, define the profiling scope in an input file and use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>-i<span class="w"> </span>input.txt<span class="w"> </span>./MatrixTranspose
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Refer to the <a class="reference external" href="https://github.com/ROCm/hip-tests/blob/develop/samples/2_Cookbook/0_MatrixTranspose">MatrixTranspose application tutorial</a> for the example application.</p>
</div>
<section id="input-file">
<span id="id3"></span><h3>Input file<a class="headerlink" href="#input-file" title="Link to this heading">#</a></h3>
<p>As mentioned above, an input file is a text file that can be supplied to <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> for basic counter and derived metric collection. It typically consists of four parts: the counters and derived metrics to collect, GPUs to profile, names and range of kernels to profile.</p>
<p>The collected data is written to an output CSV file that has the same name as the input file specified. For example`` -i input.txt`` results in <code class="docutils literal notranslate"><span class="pre">input.csv</span></code> being generated.</p>
<p><strong>Sample Input File</strong></p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="c1"># Perf counters group 1</span>
pmc:<span class="w"> </span>MemUnitStalled,TCC_MISS<span class="o">[</span><span class="m">0</span><span class="o">]</span>
<span class="c1"># Filter by dispatches range, GPU index and kernel names</span>
<span class="c1"># supported range formats: &quot;3:9&quot;, &quot;3:&quot;, &quot;3&quot;</span>
range:<span class="w"> </span><span class="m">0</span>:1
gpu:<span class="w"> </span><span class="m">0</span>
kernel:<span class="w"> </span>matrixTranspose
</pre></div>
</div>
<p>The fields in the input file are as follows:</p>
<p><strong>PMC:</strong> The rows in the text file beginning with <code class="docutils literal notranslate"><span class="pre">pmc:</span></code> are the group of basic counters or derived metrics you are interested in collecting. The performance counters can be selected from the output generated by <code class="docutils literal notranslate"><span class="pre">--list-basic</span></code> or <code class="docutils literal notranslate"><span class="pre">--list-derived</span></code> command.</p>
<p>The number of basic counters or derived metrics that can be collected in one run of profiling is limited by the GPU hardware resources. If too many counters/metrics are selected, the kernels need to be executed multiple times to collect the counters/metrics. For multi-pass execution, include multiple rows of <code class="docutils literal notranslate"><span class="pre">pmc:</span></code> in the input file. Counters or metrics in each <code class="docutils literal notranslate"><span class="pre">pmc:</span></code> row can be collected in each run of the kernel.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><code class="docutils literal notranslate"><span class="pre">rocprof</span></code> will provide suggestions to group the counters/metrics if you exceed the hardware limits. You can use this suggestion to split the counters/metrics into group sets and successfully perform counter/metric collection.</p>
</div>
<p><strong>Example:</strong> to see the suggestion to group the counters/metrics:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>cat<span class="w"> </span>input.txt
pmc<span class="w"> </span>:<span class="w"> </span>Wavefronts,<span class="w"> </span>VALUInsts,<span class="w"> </span>SALUInsts,<span class="w"> </span>SFetchInsts,
FlatVMemInsts,
LDSInsts,<span class="w"> </span>FlatLDSInsts,<span class="w"> </span>GDSInsts,<span class="w"> </span>VALUUtilization,<span class="w"> </span>FetchSize,
WriteSize,<span class="w"> </span>L2CacheHit,<span class="w"> </span>VWriteInsts,<span class="w"> </span>GPUBusy,<span class="w"> </span>VALUBusy,<span class="w"> </span>SALUBusy,
MemUnitStalled,<span class="w"> </span>WriteUnitStalled,<span class="w"> </span>LDSBankConflict,<span class="w"> </span>MemUnitBusy
range:<span class="w"> </span><span class="m">0</span><span class="w"> </span>:<span class="w"> </span><span class="m">1</span>
gpu:<span class="w"> </span><span class="m">0</span>
kernel:matrixTranspose

$<span class="w"> </span>ropcprof<span class="w"> </span>-i<span class="w"> </span>input.txt<span class="w"> </span>./MatrixTranspose
Input<span class="w"> </span>metrics<span class="w"> </span>out<span class="w"> </span>of<span class="w"> </span>hardware<span class="w"> </span>limit.<span class="w"> </span>Proposed<span class="w"> </span>metrics<span class="w"> </span>group<span class="w"> </span>set:
group1:<span class="w"> </span>FetchSize<span class="w"> </span>WriteSize<span class="w"> </span>VWriteInsts<span class="w"> </span>MemUnitStalled<span class="w"> </span>MemUnitBusy
FlatVMemInsts<span class="w"> </span>LDSInsts<span class="w"> </span>VALUInsts<span class="w"> </span>SALUInsts<span class="w"> </span>SFetchInsts
FlatLDSInsts<span class="w"> </span>GPUBusy<span class="w"> </span>Wavefronts
group2:<span class="w"> </span>WriteUnitStalled<span class="w"> </span>L2CacheHit<span class="w"> </span>GDSInsts<span class="w"> </span>VALUUtilization
VALUBusy<span class="w"> </span>SALUBusy<span class="w"> </span>LDSBankConflict
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The results reported vary depending on the GPU device being profiled.</p>
</div>
<p><strong>GPU:</strong> The row beginning with the keyword <code class="docutils literal notranslate"><span class="pre">gpu:</span></code> specifies the GPU(s) on which the hardware counters are to be collected. This enables the support for profiling multiple GPUs. You can specify multiple GPUs separated by comma such as <code class="docutils literal notranslate"><span class="pre">gpu:</span> <span class="pre">1,3</span></code>.</p>
<p><strong>Kernel:</strong> specifies the names of kernels to profile.</p>
<p><strong>Range:</strong> specifies the range of kernel dispatches. Specifying range is helpful in cases where the application causes multiple kernel dispatches and users want to filter some kernel dispatches. In the above example, the range 0:1 depicts that one kernel is profiled.</p>
</section>
<section id="metric-file">
<span id="id4"></span><h3>Metric File<a class="headerlink" href="#metric-file" title="Link to this heading">#</a></h3>
<p>The derived metrics are defined in the <code class="docutils literal notranslate"><span class="pre">/opt/rocm/lib/rocprofiler/metrics.xml</span></code> by default.</p>
<p>Here is an entry from <code class="docutils literal notranslate"><span class="pre">metrics.xml</span></code>:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>&lt;global&gt;
<span class="c1"># Wavefronts</span>
&lt;metric
<span class="w">    </span><span class="nv">name</span><span class="o">=</span><span class="s2">&quot;Wavefronts&quot;</span>
<span class="w">    </span><span class="nv">descr</span><span class="o">=</span><span class="s2">&quot;Total wavefronts.&quot;</span>
<span class="w">    </span><span class="nv">expr</span><span class="o">=</span>SQ_WAVES
&gt;&lt;/metric&gt;
&lt;/global&gt;
</pre></div>
</div>
<p>To override the properties (description/expression) of the derived metrics that are predefined in the <code class="docutils literal notranslate"><span class="pre">metrics.xml</span></code>, redefine the derived metrics in the custom derived metrics file as shown here:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="c1">#include &quot;gfx_metrics.xml&quot;</span>

&lt;global&gt;
&lt;metric
<span class="w">    </span><span class="nv">name</span><span class="o">=</span><span class="s2">&quot;Wavefronts&quot;</span>
<span class="w">    </span><span class="nv">descr</span><span class="o">=</span><span class="s2">&quot;Total wavefronts. Description redefined by user.&quot;</span>
<span class="w">    </span><span class="nv">expr</span><span class="o">=</span>SQ_WAVES
&gt;&lt;/metric&gt;
&lt;/global&gt;
</pre></div>
</div>
<p>Note that while specifying your custom metrics file, you must include <code class="docutils literal notranslate"><span class="pre">rocprofiler/test/tool/gfx_metrics.xml</span></code> file as all the basic counters are defined here. The basic counters are used in calculating the derived metrics.</p>
<p>Here is an entry from <code class="docutils literal notranslate"><span class="pre">gfx_metrics.xml</span></code>:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>&lt;gfx9&gt;
&lt;metric<span class="w"> </span><span class="nv">name</span><span class="o">=</span><span class="s2">&quot;SQ_WAVES&quot;</span><span class="w"> </span><span class="nv">block</span><span class="o">=</span>SQ<span class="w"> </span><span class="nv">event</span><span class="o">=</span><span class="m">4</span><span class="w"> </span><span class="nv">descr</span><span class="o">=</span><span class="s2">&quot;Count number of waves sent to SQs. (per-simd, emulated, global)&quot;</span>&gt;&lt;/metric&gt;
&lt;gfx9&gt;
</pre></div>
</div>
<p>You can also define new derived metrics in the custom metrics file as shown here:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="c1">#include &quot;gfx_metrics.xml&quot;</span>

&lt;gfx9_expr&gt;
&lt;metric<span class="w"> </span><span class="nv">name</span><span class="o">=</span><span class="s2">&quot;TotalWorkItems&quot;</span><span class="w"> </span><span class="nv">expr</span><span class="o">=</span>SQ_WAVES*4<span class="w">  </span><span class="nv">descr</span><span class="o">=</span><span class="s2">&quot;Total number of waves sent to SQs(For all simd&#39;s). Defined by user.&quot;</span><span class="w"> </span>&gt;&lt;/metric&gt;
&lt;/gfx9_expr&gt;
</pre></div>
</div>
<p>To see the list of customized derived metrics, use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>rocprof<span class="w"> </span>-m<span class="w"> </span>custom_metrics.xml<span class="w"> </span>--list-derived
gpu-agent1<span class="w"> </span>:<span class="w"> </span>TotalWorkItems<span class="w"> </span>:<span class="w"> </span>Total<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>waves<span class="w"> </span>sent<span class="w"> </span>to<span class="w"> </span>SQs<span class="o">(</span>For<span class="w"> </span>all<span class="w"> </span>simd<span class="err">&#39;</span>s<span class="o">)</span>.<span class="w"> </span>Defined<span class="w"> </span>by<span class="w"> </span>user.
<span class="nv">TotalWorkItems</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>SQ_WAVES*4
</pre></div>
</div>
<p>To collect the values of custom derived metrics, use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cat<span class="w"> </span>input.txt
pmc:<span class="w"> </span>TotalWorkItems

$<span class="w"> </span>rocprof<span class="w"> </span>-i<span class="w"> </span>input.txt<span class="w"> </span>-m<span class="w"> </span>custom_metrics.xml<span class="w"> </span>./MatrixTranspose
Index,KernelName,gpu-id,queue-id,queue-index,pid,tid,grd,wgr,lds,scr,arch_vgpr,accum_vgpr,sgpr,wave_size,sig,obj,TotalWorkItems
<span class="m">0</span>,<span class="s2">&quot;matrixTranspose(float*, float*, int) [clone .kd]&quot;</span>,1,0,0,2746,2746,1048576,16,0,0,8,0,16,64,0x0,0x7fead980e800,262144.0000000000
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>You must use the input file to supply the list of derived metrics to be collected while the custom metrics file provides the expressions for calculating those derived metrics. When collecting the custom derived metrics, make sure to mention only those derived metrics in the input file that you have defined in the custom derived metrics file. When not using the option <code class="docutils literal notranslate"><span class="pre">-m</span></code>, <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> refers to the default <code class="docutils literal notranslate"><span class="pre">metrics.xml</span></code> for expressions of all the derived metrics specified in the input file.</p>
</div>
<p>The basic counters and derived metrics specific to the AMD GPUs are listed in the xml files under the respective GPU family. The LLVM target <code class="docutils literal notranslate"><span class="pre">gfx9</span></code> corresponds to <code class="docutils literal notranslate"><span class="pre">MI50</span></code> and <code class="docutils literal notranslate"><span class="pre">MI100</span></code> while <code class="docutils literal notranslate"><span class="pre">gfx90a</span></code> corresponds to the <code class="docutils literal notranslate"><span class="pre">MI200</span></code> family. The counters and metrics applicable to all GPUs are listed under global. See the supported GPUs and their respective LLVM targets in the <a class="reference external" href="rocm:release/gpu_os_support">Linux Supported GPUs</a>.</p>
</section>
<section id="generated-output">
<span id="output-file"></span><h3>Generated Output<a class="headerlink" href="#generated-output" title="Link to this heading">#</a></h3>
<p>Executing <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> with an input file <code class="docutils literal notranslate"><span class="pre">input.txt</span></code> produces an output CSV (the file name can be specified with the <code class="docutils literal notranslate"><span class="pre">-o</span></code> option) with the counter information as shown below:</p>
<p><strong>Example:</strong> Executing <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> on <code class="docutils literal notranslate"><span class="pre">MatrixTranspose</span></code> application with sample input file</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>rocprof<span class="w"> </span>-i<span class="w"> </span>input.txt<span class="w"> </span>./MatrixTranspose
$<span class="w"> </span>cat<span class="w"> </span>input.csv
Index,KernelName,gpu-id,queue-id,queue-index,pid,tid,grd,wgr,lds,
scr,vgpr,sgpr,fbar,sig,obj,MemUnitStalled,TCC_MISS<span class="o">[</span><span class="m">0</span><span class="o">]</span>
<span class="m">0</span>,<span class="s2">&quot;matrixTranspose(float*, float*, int) [clone .kd]&quot;</span>,0,0,0,2614,2614,
<span class="m">1048576</span>,16,0,0,8,24,0,0x0,0x7fbfcb37c580,6.6756117852,4096.
</pre></div>
</div>
<p>Each row of the CSV file is an instance of kernel execution. The columns in the output file are:</p>
<ul class="simple">
<li><p><strong>Index</strong> - kernels dispatch order index</p></li>
<li><p><strong>KernelName</strong> - kernel name</p></li>
<li><p><strong>gpu-id</strong> - GPU ID the kernel was submitted to</p></li>
<li><p><strong>queue-id</strong> - ROCm queue unique ID the kernel was submitted to</p></li>
<li><p><strong>queue-index</strong> - ROCm queue write index for the submitted AQL packet</p></li>
<li><p><strong>pid</strong> - system application process ID</p></li>
<li><p><strong>tid</strong> - system application thread id that submitted the kernel</p></li>
<li><p><strong>grd</strong> - kernel’s grid size</p></li>
<li><p><strong>wgr</strong> - kernel’s work group size</p></li>
<li><p><strong>lds</strong> - kernel’s LDS memory size</p></li>
<li><p><strong>scr</strong> - kernel’s scratch memory size</p></li>
<li><p><strong>vgpr</strong> - kernel’s VGPR size</p></li>
<li><p><strong>sgpr</strong> - kernel’s SGPR size</p></li>
<li><p><strong>fbar</strong> - kernel’s barriers limitation</p></li>
<li><p><strong>sig</strong> - kernel’s completion signal</p></li>
</ul>
<p><strong>Example:</strong> To enable the timestamp</p>
<p>To enable timestamp in the output, use option <code class="docutils literal notranslate"><span class="pre">--timestamp</span> <span class="pre">on</span></code> as shown in the following example.</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>rocprof<span class="w"> </span>-i<span class="w"> </span>input.txt<span class="w"> </span>--timestamp<span class="w"> </span>on<span class="w"> </span>./MatrixTranspose
$<span class="w"> </span>cat<span class="w"> </span>input.csv
Index,KernelName,gpu-id,queue-id,queue-index,pid,tid,grd,
wgr,lds,scr,vgpr,sgpr,fbar,sig,obj,
MemUnitStalled,TCC_MISS<span class="o">[</span><span class="m">0</span><span class="o">]</span>,DispatchNs,BeginNs,EndNs,CompleteNs
<span class="m">0</span>,<span class="s2">&quot;matrixTranspose(float*, float*, int) [clone .kd]&quot;</span>,0,0,0,2837,2837,
<span class="m">1048576</span>,16,0,0,8,24,0,0x0,
0x7fcd75984580,5.9792124305,4096,87851328156768,
<span class="m">87851334047658</span>,87851334141098,87851334732528
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The <code class="docutils literal notranslate"><span class="pre">--timestamp</span></code> is on by default.</p>
</div>
<p><strong>Example:</strong> To specify the output file name.</p>
<p>The default output CSV file has the same name as the input file specified. To specify a name for the output file, use option <code class="docutils literal notranslate"><span class="pre">-o</span> <span class="pre">&lt;file</span> <span class="pre">name&gt;</span></code> as shown in the following example.</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>rocprof<span class="w"> </span>-i<span class="w"> </span>input.txt<span class="w"> </span>--timestamp<span class="w"> </span>on<span class="w"> </span>-o<span class="w"> </span>output.csv<span class="w"> </span>./MatrixTranspose
$<span class="w"> </span>cat<span class="w"> </span>output.csv
Index,KernelName,gpu-id,queue-id,queue-index,pid,tid,
grd,wgr,lds,scr,vgpr,sgpr,fbar,
sig,obj,MemUnitStalled,
TCC_MISS<span class="o">[</span><span class="m">0</span><span class="o">]</span>,DispatchNs,BeginNs,EndNs,CompleteNs
<span class="m">0</span>,<span class="s2">&quot;matrixTranspose(float*, float*, int) [clone .kd]&quot;</span>,0,0,0,
<span class="m">215</span>,215,1048576,16,0,0,8,24,0,0x0,0x7f961080a580,7.0675214726,4096,
<span class="m">91063585321414</span>,91063591158627,91063591252551,91063592018031
</pre></div>
</div>
</section>
<section id="profiling-multiple-mpi-ranks">
<h3>Profiling Multiple MPI Ranks<a class="headerlink" href="#profiling-multiple-mpi-ranks" title="Link to this heading">#</a></h3>
<p>To profile multiple MPI ranks use the following command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>mpirun<span class="w"> </span>...<span class="w"> </span>&lt;mpi<span class="w"> </span>args&gt;<span class="w"> </span>...<span class="w"> </span>rocprof<span class="w"> </span>...<span class="w"> </span>&lt;rocprof<span class="w"> </span>args&gt;<span class="w"> </span>...<span class="w"> </span>application<span class="w"> </span>...<span class="w"> </span>&lt;application<span class="w"> </span>args&gt;
</pre></div>
</div>
<div class="admonition important">
<p class="admonition-title">Important</p>
<p>When using <cite>OpenMPI</cite>, you must run <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> inside the <code class="docutils literal notranslate"><span class="pre">mpirun</span></code> command, as shown above, to enable ROCProfiler to handle process forking and launching via <code class="docutils literal notranslate"><span class="pre">mpirun</span></code> and related executables. If you run the <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> command before <code class="docutils literal notranslate"><span class="pre">mpirun</span></code>, then the tool fails with the error <cite>roctracer: Loading ‘libamdhip64.so’ failed, (null)</cite>.</p>
</div>
<p>This execution mode requires the following:</p>
<ol class="arabic">
<li><p>Generation of trace data per <cite>MPI</cite> (or process) rank</p>
<p>ROCm provides a simple bash wrapper that demonstrates how to generate a unique output directory per process as given below:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>cat<span class="w"> </span>wrapper.sh
<span class="c1">#! /usr/bin/env bash</span>
<span class="k">if</span><span class="w"> </span><span class="o">[[</span><span class="w"> </span>-n<span class="w"> </span><span class="si">${</span><span class="nv">OMPI_COMM_WORLD_RANK</span><span class="p">+z</span><span class="si">}</span><span class="w"> </span><span class="o">]]</span><span class="p">;</span><span class="w"> </span><span class="k">then</span>
<span class="w">    </span><span class="c1"># mpich</span>
<span class="w">    </span><span class="nb">export</span><span class="w"> </span><span class="nv">MPI_RANK</span><span class="o">=</span><span class="si">${</span><span class="nv">OMPI_COMM_WORLD_RANK</span><span class="si">}</span>

<span class="k">elif</span><span class="w"> </span><span class="o">[[</span><span class="w"> </span>-n<span class="w"> </span><span class="si">${</span><span class="nv">MV2_COMM_WORLD_RANK</span><span class="p">+z</span><span class="si">}</span><span class="w"> </span><span class="o">]]</span><span class="p">;</span><span class="w"> </span><span class="k">then</span>
<span class="w">    </span><span class="c1"># ompi</span>
<span class="w">    </span><span class="nb">export</span><span class="w"> </span><span class="nv">MPI_RANK</span><span class="o">=</span><span class="si">${</span><span class="nv">MV2_COMM_WORLD_RANK</span><span class="si">}</span>
<span class="k">fi</span>

<span class="nv">args</span><span class="o">=</span><span class="s2">&quot;</span><span class="nv">$*</span><span class="s2">&quot;</span>
<span class="nv">pid</span><span class="o">=</span><span class="s2">&quot;</span><span class="nv">$$</span><span class="s2">&quot;</span>
<span class="nv">outdir</span><span class="o">=</span><span class="s2">&quot;rank_</span><span class="si">${</span><span class="nv">pid</span><span class="si">}</span><span class="s2">_</span><span class="si">${</span><span class="nv">MPI_RANK</span><span class="si">}</span><span class="s2">&quot;</span>
<span class="nv">outfile</span><span class="o">=</span><span class="s2">&quot;results_</span><span class="si">${</span><span class="nv">pid</span><span class="si">}</span><span class="s2">_</span><span class="si">${</span><span class="nv">MPI_RANK</span><span class="si">}</span><span class="s2">.csv&quot;</span>
<span class="nb">eval</span><span class="w"> </span><span class="s2">&quot;rocprof -d </span><span class="si">${</span><span class="nv">outdir</span><span class="si">}</span><span class="s2"> -o </span><span class="si">${</span><span class="nv">outdir</span><span class="si">}</span><span class="s2">/</span><span class="si">${</span><span class="nv">outfile</span><span class="si">}</span><span class="s2"> </span><span class="nv">$*</span><span class="s2">&quot;</span>
</pre></div>
</div>
<p>This script:</p>
<ul class="simple">
<li><p>Determines the global <cite>MPI</cite> rank (implemented here for <cite>OpenMPI</cite> and <cite>MPICH</cite> only)</p></li>
<li><p>Determines the process id of the <cite>MPI</cite> rank</p></li>
<li><p>Generates a unique output directory using the two</p></li>
</ul>
<p>To invoke this wrapper, use the following command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>mpirun<span class="w"> </span>&lt;mpi<span class="w"> </span>args&gt;<span class="w"> </span>./wrapper.sh<span class="w"> </span>--hip-trace<span class="w"> </span>&lt;application&gt;<span class="w"> </span>&lt;args&gt;
</pre></div>
</div>
<p>This generates an output directory for each MPI rank used.</p>
<p><strong>Example:</strong></p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>ls<span class="w"> </span>-ld<span class="w"> </span>rank_*<span class="w"> </span><span class="p">|</span><span class="w"> </span>awk<span class="w"> </span><span class="o">{</span><span class="s1">&#39;print $5&quot; &quot;$9&#39;</span><span class="o">}</span>
<span class="m">4096</span><span class="w"> </span>rank_513555_0
<span class="m">4096</span><span class="w"> </span>rank_513556_1
</pre></div>
</div>
</li>
<li><p>Combining traces from multiple processes</p>
<p>The multiple traces as generated above can be combined into a unified trace for profiling using <code class="docutils literal notranslate"><span class="pre">merge_traces.sh</span></code> utility script. The full path for the script is <code class="docutils literal notranslate"><span class="pre">/opt/rocm/bin/merge_traces.sh</span></code></p>
<p>Usage:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>merge_traces.sh<span class="w"> </span>-o<span class="w"> </span>&lt;outputdir&gt;<span class="w"> </span><span class="o">[</span>&lt;inputdir&gt;...<span class="o">]</span>
</pre></div>
</div>
<p>For example:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>./merge_traces.sh<span class="w"> </span>-h
</pre></div>
</div>
<p>Use the following input arguments to the <cite>merge_traces.sh</cite> script to control which traces are merged and where the resulting merged trace is saved.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">&lt;inputdir&gt;...</span></code> - space-separated list of ROCProfiler directories to merge. If not specified, the current working directory is used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">-o</span> <span class="pre">&lt;outputdir&gt;</span></code> - output directory where the results are aggregated. The file <code class="docutils literal notranslate"><span class="pre">unified/results.json</span></code> is generated, and it contains trace data from the specified input directories.</p></li>
</ul>
</li>
</ol>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../install/installv2.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Installing ROCProfilerV2</p>
      </div>
    </a>
    <a class="right-next"
       href="rocprof-command.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">rocprof command help</p>
      </div>
      <i class="fa-solid fa-angle-right"></i>
    </a>
</div>
                </footer>
              
            </div>
            
            
              
                <div class="bd-sidebar-secondary bd-toc"><div class="sidebar-secondary-items sidebar-secondary__inner">


  <div class="sidebar-secondary-item">
  <div class="page-toc tocsection onthispage">
    <i class="fa-solid fa-list"></i> Contents
  </div>
  <nav class="bd-toc-nav page-toc">
    <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#application-tracing">Application tracing</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#command-line-options-for-application-tracing">Command-line options for application tracing</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-trace">HIP Trace</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#statistics-files">Statistics Files</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hsa-trace">HSA Trace</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#system-trace">System Trace</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#roctx-trace">ROCTx Trace</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#tracing-control">Tracing Control</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filter-tasks">Filter Tasks</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#adjust-trace-flush-rate">Adjust Trace Flush Rate</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#function-name-truncation">Function Name Truncation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#tracing-control-for-api-or-code-block">Tracing Control for API or Code Block</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#set-initial-delay-periodic-sample-length-and-rate">Set Initial Delay, Periodic Sample Length and Rate</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#roctracer-api">ROCTracer API</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#performance-counter-collection">Performance Counter Collection</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#command-line-options-for-counter-collection">Command-line options for counter collection</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#listing-performance-counters">Listing Performance Counters</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#using-rocprof-for-application-profiling">Using <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> for Application Profiling</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#input-file">Input file</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#metric-file">Metric File</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#generated-output">Generated Output</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#profiling-multiple-mpi-ranks">Profiling Multiple MPI Ranks</a></li>
</ul>
</li>
</ul>
  </nav></div>

</div></div>
              
            
          </div>
          <footer class="bd-footer-content">
            <p>
  </p>
          </footer>
        

      </main>
    </div>
  </div>
  
  <!-- Scripts loaded after <body> so the DOM is not blocked -->
  <script src="../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b"></script>
<script src="../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b"></script>

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
    <img id="rdc-watermark" src="../_static/images/alpha-watermark.svg" alt="DRAFT watermark"/>
</div> -->
  </body>
</html>
