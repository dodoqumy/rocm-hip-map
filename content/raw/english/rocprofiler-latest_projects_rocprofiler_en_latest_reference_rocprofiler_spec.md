---
title: "ROCProfiler library specification &#8212; ROCProfiler 2.0.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler/en/latest/reference/rocprofiler_spec.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:28:53.364148+00:00
content_hash: "a9f2425b73a09b88"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Installation, configuration, and use of the rocprof command line tool" name="description" />
<meta content="ROCProfiler tool, ROCProfiler library, rocprof, rocprofv1, rocprofv2, ROCm, API, reference" name="keywords" />

    <title>ROCProfiler library specification &#8212; ROCProfiler 2.0.0 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/rocprofiler_spec';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="ROCProfiler API library" href="../doxygen/html/index.html" />
    <link rel="prev" title="Using rocsys" href="../how-to/using-rocsys.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-docs" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/rocprofiler_spec.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../how-to/using-rocprof.html">Using rocprof</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/rocprof-command.html">rocprof command help</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/rocprofv2-usage.html">Using rocprofv2</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/rocprofv2-command.html">rocprofv2 command help</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/using-rocsys.html">Using rocsys</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">References</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active"><a class="current reference internal" href="#">ROCProfiler library specification</a></li>
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
<li class="toctree-l1"><a class="reference internal" href="rocprofilerv2-api.html">ROCProfilerV2 API</a></li>
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
<button class="sidebar-toggle secondary-toggle btn btn-sm" title="Toggle secondary sidebar" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <span class="fa-solid fa-list"></span>
</button>
</div></div>
      
    </div>
  
</div>
</div>
              
              

<div id="jb-print-docs-body" class="onlyprint">
    <h1>ROCProfiler library specification</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#environment-variables">Environment variables</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#logging">Logging</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#general-api">General API</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#returning-the-error-and-error-string-methods">Returning the error and error string methods</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-version">Library version</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#backend-api">Backend API</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#loading-and-configuring">Loading and configuring</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#info-api">Info API</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#context-api">Context API</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sampling-api">Sampling API</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#intercepting-api">Intercepting API</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#profiling-context-pools">Profiling context pools</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#application-code-examples">Application code examples</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#querying-available-metrics">Querying available metrics</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#profiling-code-example">Profiling code example</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#option-to-use-completion-callback">Option to use completion callback</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#option-to-use-context-pool">Option to use context pool</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#standalone-sampling-usage-code-example">Standalone sampling usage code example</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#printing-out-profiling-results">Printing out profiling results</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="rocprofiler-library-specification">
<span id="rocprof-spec"></span><h1>ROCProfiler library specification<a class="headerlink" href="#rocprofiler-library-specification" title="Link to this heading">#</a></h1>
<p>The goal of the implementation is to provide a hardware-specific low-level performance analysis
interface for profiling of GPU compute applications. The profiling includes hardware performance
counters with complex performance metrics and hardware traces. Performance counters are treated as the basic
metrics, and formulas can be defined to derive more complex metrics.</p>
<p>The library can be loaded by HSA runtime as a tool plugin and it can be loaded by higher
level hardware-independent performance analysis API like PAPI. The library provides a C API and is
based on AQL profile AMD-specific HSA extensions. The library features are listed here:</p>
<ul class="simple">
<li><p>Provides methods to query the list of supported hardware features.</p></li>
<li><p>Provides profiling APIs to start, stop, and read metrics results and tracing data.</p></li>
<li><p>Provides intercepting API for collecting per-kernel profiling data for the kernels dispatched to HSA AQL queues.</p></li>
<li><p>Provides mechanism to load profiling tool library plugin by env variable <code class="docutils literal notranslate"><span class="pre">ROCP_TOOL_LIB</span></code>.</p></li>
<li><p>Responsible for allocation of the buffers for profiling and notifying about output data buffer overflow for traces.</p></li>
<li><p>Implemented based on AMD-specific AQLprofile HSA extension.</p></li>
<li><p>Implementation is abstracted from the specific GFXIP.</p></li>
<li><p>Implementation is extensible:</p>
<ul>
<li><p>Easy addition of counters and metrics</p></li>
<li><p>Counters enumeration</p></li>
<li><p>Counters and metrics can be dynamically configured using XML configuration files (<code class="docutils literal notranslate"><span class="pre">metrics.xml</span></code>) with counters and metrics tables:</p>
<ul>
<li><p>Counters table entry, basic metric: counter name, block name, event id</p></li>
<li><p>Complex metrics table entry: metric name, an expression for calculating the metric from the counters</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p><strong>Metrics XML file example:</strong></p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>&lt;gfx8&gt;
<span class="w">    </span>&lt;metric<span class="w"> </span><span class="nv">name</span><span class="o">=</span>L1_CYCLES_COUNTER<span class="w"> </span><span class="nv">block</span><span class="o">=</span>L1<span class="w"> </span><span class="nv">event</span><span class="o">=</span><span class="m">0</span><span class="w"> </span>&gt;
<span class="w">    </span>&lt;metric<span class="w"> </span><span class="nv">name</span><span class="o">=</span>L1_MISS_COUNTER<span class="w"> </span><span class="nv">block</span><span class="o">=</span>L1<span class="w"> </span><span class="nv">event</span><span class="o">=</span><span class="m">33</span><span class="w"> </span>&gt;
<span class="w">    </span>...
&lt;/gfx8&gt;

&lt;gfx9&gt;
<span class="w">    </span>...
&lt;/gfx9&gt;

&lt;global&gt;
<span class="w">    </span>&lt;metric<span class="w"> </span><span class="nv">name</span><span class="o">=</span>L1_MISS_RATIO<span class="w"> </span><span class="nv">expr</span><span class="o">=</span>L1_CYCLES_COUNT/<span class="w"> </span>L1_MISS_COUNTER<span class="w"> </span>&gt;&lt;/metric&gt;
&lt;/global&gt;
</pre></div>
</div>
<section id="environment-variables">
<h2>Environment variables<a class="headerlink" href="#environment-variables" title="Link to this heading">#</a></h2>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">HSA_TOOLS_LIB</span></code> - required to be set to the name of rocprofiler library to be loaded by HSA runtime</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCP_METRICS</span></code> - path to the metrics XML file</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCP_TOOL_LIB</span></code> - path to profiling tool library loaded by ROCProfiler</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCP_HSA_INTERCEPT</span></code> - if set then HSA dispatches intercepting is enabled</p></li>
</ul>
</section>
<section id="logging">
<h2>Logging<a class="headerlink" href="#logging" title="Link to this heading">#</a></h2>
<p>Set the following environment variables to enable logging:</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Environment Variable</p></th>
<th class="head"><p>Purpose</p></th>
<th class="head"><p>Log Files</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCPROFILER_LOG=1</span></code></p></td>
<td><p>Enables error message logging</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">/tmp/rocprofiler_log.txt</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCPROFILER_TRACE=1</span></code></p></td>
<td><p>Enables verbose tracing</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">/tmp/roctracer_log.txt</span></code></p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="general-api">
<h2>General API<a class="headerlink" href="#general-api" title="Link to this heading">#</a></h2>
<p>The library supports a method for getting the error number and error string of the last failed library API call.
To check the conformance of the library API header, and the library binary, the following version macros and API methods can be used.</p>
<p>Returning the error and error string methods:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_error_string</span></code> - method for returning the error string</p></li>
</ul>
<p>Library version:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ROCPROFILER_VERSION_MAJOR</span></code> - API major version macro</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCPROFILER_VERSION_MINOR</span></code> - API minor version macro</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_version_major</span></code> - library major version</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_version_minor</span></code> - library minor version</p></li>
</ul>
<section id="returning-the-error-and-error-string-methods">
<h3>Returning the error and error string methods<a class="headerlink" href="#returning-the-error-and-error-string-methods" title="Link to this heading">#</a></h3>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>const<span class="w"> </span>char*<span class="w"> </span>rocprofiler_error_string<span class="o">()</span><span class="p">;</span>
</pre></div>
</div>
</section>
<section id="library-version">
<h3>Library version<a class="headerlink" href="#library-version" title="Link to this heading">#</a></h3>
<p>The library provides back compatibility if the library major version is less or equal then the API major version macro.</p>
<p>API version macros defined in the library API header <code class="docutils literal notranslate"><span class="pre">rocprofiler.h</span></code>:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>ROCPROFILER_VERSION_MAJOR
ROCPROFILER_VERSION_MINOR
</pre></div>
</div>
<p>Methods to check library major and minor versions:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>uint32_t<span class="w"> </span>rocprofiler_major_version<span class="o">()</span><span class="p">;</span>
uint32_t<span class="w"> </span>rocprofiler_minor_version<span class="o">()</span><span class="p">;</span>
</pre></div>
</div>
</section>
</section>
<section id="backend-api">
<h2>Backend API<a class="headerlink" href="#backend-api" title="Link to this heading">#</a></h2>
<p>The library provides methods to open/close a profiling context, to start, stop, and read
HW performance counters and traces, to intercept kernel dispatches to collect per-kernel
profiling data. The library also provides methods to calculate complex performance metrics
and to query the list of available metrics.</p>
<p>The library distinguishes two profiling features, metrics and traces, where HW performance
counters are treated as the basic metrics. To check if there was an error the library methods
return HSA standard status code. For a given context the profiling can be started/stopped
and counters sampled in standalone mode or profiling can be initiated by intercepting the
kernel dispatches with registering a dispatch callback.</p>
<p>For counters sampling, which is the usage model of higher level APIs like PAPI, the start/stop/read APIs should be used.
To collect per-kernel data for kernels submitted to HSA queues, the dispatch callback API should be used.</p>
<p>The library provides back compatibility if the library major version is less or equal.</p>
<p>Returned API status:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hsa_status_t</span></code> - HSA status codes are used from hsa.h header</p></li>
</ul>
<p>Loading and Configuring, loadable plugin on-load/unload methods:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_settings_t</span></code> - global properties</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">OnLoadTool</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">OnLoadToolProp</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">OnUnloadTool</span></code></p></li>
</ul>
<p>Info API:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_info_kind_t</span></code> - profiling info kind</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_info_query_t</span></code> - profiling info query</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_info_data_t</span></code> - profiling info data</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_get_info</span></code> - return the info for a given info kind</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_iterote_inf_</span></code> - iterate over the info for a given info kind</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_query_info</span></code> - iterate over the info for a given info query</p></li>
</ul>
<p>Context API:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_t</span></code> - profiling context handle</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_feature_kind_t</span></code> - profiling feature kind</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_feature_parameter_t</span></code> - profiling feature parameter</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_data_kind_t</span></code> - profiling data kind</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_data_t</span></code> - profiling data</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_feature_t</span></code> - profiling feature</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_mode_t</span></code> - profiling modes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_properties_t</span></code> - profiler properties</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_open</span></code> - open new profiling context</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_close</span></code> - close profiling context and release all allocated resources</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_group_count</span></code> - return profiling groups count</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_get_group</span></code> - return profiling group for a given index</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_get_metrics</span></code> - method for calculating the metrics data</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_iterate_trace_data</span></code> - method for iterating output trace data instances</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_time_id_t</span></code> - supported time value ID enumeration</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_get_time</span></code> - return time for a given time ID and profiling timestamp value</p></li>
</ul>
<p>Sampling API:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_start</span></code> - start profiling</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_stop</span></code> - stop profiling</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_read</span></code> - read profiling data to the profiling features objects</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_get_data</span></code> - wait for profiling data</p>
<p>Group versions of start/stop/read/get_data methods:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_group_start</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_group_stop</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_group_read</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_group_get_data</span></code></p></li>
</ul>
</li>
</ul>
<p>Intercepting API:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_callback_t</span></code> - profiling callback type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_callback_data_t</span></code> - profiling callback data type</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_dispatch_record_t</span></code> - dispatch record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_queue_callbacks_t</span></code> - queue callbacks, dispatch/destroy</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_set_queue_callbacks</span></code> - set queue kernel dispatch and queue destroy callbacks</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_remove_queue_callbacks</span></code> - remove queue callbacks</p></li>
</ul>
<p>Context pool API:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_pool_t</span></code> - context pool handle</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_pool_entry_t</span></code> - context pool entry</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_pool_properties_t</span></code> - context pool properties</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_pool_handler_t</span></code> - context pool completion handler</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_pool_open</span></code> - context pool open</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_pool_close</span></code> - context pool close</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_pool_fetch</span></code> - fetch and empty context entry to pool</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_pool_release</span></code> - release a context entry</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_pool_iterate</span></code> - iterated fetched context entries</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprofiler_pool_flush</span></code> - flush completed context entries</p></li>
</ul>
<section id="loading-and-configuring">
<h3>Loading and configuring<a class="headerlink" href="#loading-and-configuring" title="Link to this heading">#</a></h3>
<p>The profiling properties can be set by profiler plugin on loading by ROC runtime.
The profiler library plugin can be set by <code class="docutils literal notranslate"><span class="pre">ROCP_TOOL_LIB</span></code> env var.</p>
<p>Global properties:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">    </span>uint32_t<span class="w"> </span>intercept_mode<span class="p">;</span>
<span class="w">    </span>uint64_t<span class="w"> </span>timeout<span class="p">;</span>
<span class="w">    </span>uint32_t<span class="w"> </span>timestamp_on<span class="p">;</span>
<span class="o">}</span><span class="w"> </span>rocprofiler_settings_t<span class="p">;</span>
</pre></div>
</div>
<p>On load/unload methods defined in profiling tool library loaded by <code class="docutils literal notranslate"><span class="pre">ROCP_TOOL_LIB</span></code> env var:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>extern<span class="w"> </span><span class="s2">&quot;C&quot;</span><span class="w"> </span>void<span class="w"> </span>OnLoadTool<span class="o">()</span><span class="p">;</span>
extern<span class="w"> </span><span class="s2">&quot;C&quot;</span><span class="w"> </span>void<span class="w"> </span>OnLoadToolProp<span class="o">(</span>rocprofiler_settings_t*<span class="w"> </span>settings<span class="o">)</span><span class="p">;</span>
extern<span class="w"> </span><span class="s2">&quot;C&quot;</span><span class="w"> </span>void<span class="w"> </span>OnUnloadTool<span class="o">()</span><span class="p">;</span>
</pre></div>
</div>
</section>
<section id="info-api">
<h3>Info API<a class="headerlink" href="#info-api" title="Link to this heading">#</a></h3>
<p>The profiling metrics are defined by name and the traces are defined by name and parameters.
All supported features can be iterated using <code class="docutils literal notranslate"><span class="pre">iterate_info</span></code>/<code class="docutils literal notranslate"><span class="pre">query_info</span></code> methods. The counter
names are defined in counters table configuration file, each counter has a unique name and
defined by block name and event ID. The traces and trace parameters names are the same as in
the hardware documentation and the parameters codes are <code class="docutils literal notranslate"><span class="pre">rocprofiler_feature_parameter_t</span></code> values,
see below in the <a class="reference internal" href="#contxt-api"><span class="std std-ref">Context API</span></a> section.</p>
<p>Profiling info kind:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>enum<span class="w"> </span><span class="o">{</span>
<span class="w">    </span><span class="nv">ROCPROFILER_INFO_KIND_METRIC</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>,<span class="w">               </span>//<span class="w"> </span>metric<span class="w"> </span>info
<span class="w">    </span><span class="nv">ROCPROFILER_INFO_KIND_METRIC_COUNT</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">1</span>,<span class="w">         </span>//<span class="w"> </span>metrics<span class="w"> </span>count
<span class="w">    </span><span class="nv">ROCPROFILER_INFO_KIND_TRACE</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">2</span>,<span class="w">                </span>//<span class="w"> </span>trace<span class="w"> </span>info
<span class="w">    </span><span class="nv">ROCPROFILER_INFO_KIND_TRACE_COUNT</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">3</span>,<span class="w">          </span>//<span class="w"> </span>traces<span class="w"> </span>count
<span class="o">}</span><span class="w"> </span>rocprofiler_info_kind_t<span class="p">;</span>
</pre></div>
</div>
<p>Profiling info data:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">    </span>rocprofiler_info_kind_t<span class="w"> </span>kind<span class="p">;</span><span class="w">                   </span>//<span class="w"> </span>info<span class="w"> </span>data<span class="w"> </span>kind
<span class="w">    </span>union<span class="w"> </span><span class="o">{</span>
<span class="w">        </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">            </span>const<span class="w"> </span>char*<span class="w"> </span>name<span class="p">;</span><span class="w">               </span>//<span class="w"> </span>metric<span class="w"> </span>name
<span class="w">            </span>uint32_t<span class="w"> </span>instances<span class="p">;</span><span class="w">             </span>//<span class="w"> </span>instances<span class="w"> </span>number
<span class="w">            </span>const<span class="w"> </span>char*<span class="w"> </span>expr<span class="p">;</span><span class="w">               </span>//<span class="w"> </span>metric<span class="w"> </span>expression,<span class="w"> </span>NULL<span class="w"> </span><span class="k">for</span><span class="w"> </span>basic<span class="w"> </span>counters
<span class="w">            </span>const<span class="w"> </span>char*<span class="w"> </span>description<span class="p">;</span><span class="w">        </span>//<span class="w"> </span>metric<span class="w"> </span>description
<span class="w">            </span>const<span class="w"> </span>char*<span class="w"> </span>block_name<span class="p">;</span><span class="w">         </span>//<span class="w"> </span>block<span class="w"> </span>name
<span class="w">            </span>uint32_t<span class="w"> </span>block_counters<span class="p">;</span><span class="w">        </span>//<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>block<span class="w"> </span>counters
<span class="w">        </span><span class="o">}</span><span class="w"> </span>metric<span class="p">;</span>
<span class="w">        </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">            </span>const<span class="w"> </span>char*<span class="w"> </span>name<span class="p">;</span><span class="w">               </span>//<span class="w"> </span>trace<span class="w"> </span>name
<span class="w">            </span>const<span class="w"> </span>char*<span class="w"> </span>description<span class="p">;</span><span class="w">        </span>//<span class="w"> </span>trace<span class="w"> </span>description
<span class="w">            </span>uint32_t<span class="w"> </span>parameter_count<span class="p">;</span><span class="w">       </span>//<span class="w"> </span>supported<span class="w"> </span>by<span class="w"> </span>the<span class="w"> </span>trace<span class="w"> </span>number
<span class="w">                                            </span>//<span class="w"> </span>parameters
<span class="w">        </span><span class="o">}</span><span class="w"> </span>trace<span class="p">;</span>
<span class="w">    </span><span class="o">}</span><span class="p">;</span>
<span class="o">}</span><span class="w"> </span>rocprofiler_info_data_t<span class="p">;</span>
</pre></div>
</div>
<p>Return info for a given info kind:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>has_status_t<span class="w"> </span>rocprofiler_get_info<span class="o">(</span>
<span class="w">    </span>const<span class="w"> </span>hsa_agent_t*<span class="w"> </span>agent,<span class="w">                       </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span><span class="o">]</span><span class="w"> </span>GPU<span class="w"> </span>handle,<span class="w"> </span>NULL<span class="w"> </span><span class="k">for</span><span class="w"> </span>all
<span class="w">                                                    </span>//<span class="w"> </span>GPU<span class="w"> </span>agents
<span class="w">    </span>rocprofiler<span class="w"> </span>info_kind_t<span class="w"> </span>kind,<span class="w">                   </span>//<span class="w"> </span>kind<span class="w"> </span>of<span class="w"> </span>iterated<span class="w"> </span>info
<span class="w">    </span>void<span class="w"> </span>*data<span class="o">)</span><span class="p">;</span><span class="w">                                    </span>//<span class="w"> </span>data<span class="w"> </span>passed<span class="w"> </span>to<span class="w"> </span>callback
</pre></div>
</div>
<p>Iterate over the info for a given info kind, and invoke an application-defined callback on
every iteration:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>has_status_t<span class="w"> </span>rocprofiler_iterate_info<span class="o">(</span>
<span class="w">    </span>const<span class="w"> </span>hsa_agent_t*<span class="w"> </span>agent,<span class="w">                       </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span><span class="o">]</span><span class="w"> </span>GPU<span class="w"> </span>handle,<span class="w"> </span>NULL<span class="w"> </span><span class="k">for</span><span class="w"> </span>all
<span class="w">                                                    </span>//<span class="w"> </span>GPU<span class="w"> </span>agents
<span class="w">    </span>rocprofiler<span class="w"> </span>info_kind_t<span class="w"> </span>kind,<span class="w">                   </span>//<span class="w"> </span>kind<span class="w"> </span>of<span class="w"> </span>iterated<span class="w"> </span>info
<span class="w">    </span>hsa_status_t<span class="w"> </span><span class="o">(</span>*callback<span class="o">)(</span>const<span class="w"> </span>rocprofiler_info_data_t<span class="w"> </span>info,<span class="w"> </span>void<span class="w"> </span>*data<span class="o">)</span>,<span class="w"> </span>//<span class="w"> </span>callback
<span class="w">    </span>void<span class="w"> </span>*data<span class="o">)</span><span class="p">;</span>
</pre></div>
</div>
<p>Iterate over the info for a given info query, and invoke an application-defined callback on
every iteration. The query fields set to NULL define the query wildcard:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>has_status_t<span class="w"> </span>rocprofiler_query_info<span class="o">(</span>
<span class="w">    </span>const<span class="w"> </span>hsa_agent_t*<span class="w"> </span>agent,<span class="w">                       </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span><span class="o">]</span><span class="w"> </span>GPU<span class="w"> </span>handle,<span class="w"> </span>NULL<span class="w"> </span><span class="k">for</span><span class="w"> </span>all
<span class="w">                                                    </span>//<span class="w"> </span>GPU<span class="w"> </span>agents
<span class="w">    </span>rocprofiler<span class="w"> </span>info_kind_t<span class="w"> </span>kind,<span class="w">                   </span>//<span class="w"> </span>kind<span class="w"> </span>of<span class="w"> </span>iterated<span class="w"> </span>info
<span class="w">    </span>rocprofiler_info_data_t<span class="w"> </span>query,<span class="w">                  </span>//<span class="w"> </span>info<span class="w"> </span>query
<span class="w">    </span>hsa_status_t<span class="w"> </span><span class="o">(</span>*callback<span class="o">)(</span>const<span class="w"> </span>rocprofiler_info_data_t<span class="w"> </span>info,<span class="w"> </span>void<span class="w"> </span>*data<span class="o">)</span>,<span class="w"> </span>//<span class="w"> </span>callback
<span class="w">    </span>void<span class="w"> </span>*data<span class="o">)</span><span class="p">;</span><span class="w">                                    </span>//<span class="w"> </span>data<span class="w"> </span>passed<span class="w"> </span>to<span class="w"> </span>callback
</pre></div>
</div>
</section>
<section id="context-api">
<span id="contxt-api"></span><h3>Context API<a class="headerlink" href="#context-api" title="Link to this heading">#</a></h3>
<p>Profiling context is accumulating all profiling information including profiling features
which carry profiling data, required buffers for profiling command packets and output data.
The context can be created and deleted by the library open/close methods.</p>
<p>By deleting the context all accumulated by the library resources associated with this context will be
released. If more than one run is required to collect all requested counters data, then
data for all profiling groups should be collected first, then the metrics can be calculated by
loading the saved groups’ data to the profiling context. Saving and loading of the groups
data is responsibility of the tool. The groups are automatically identified on the profiling
context open and there is API to access them, as shown in the <em>Profiling Groups</em> example that follows.</p>
<p>Profiling context handle:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typename<span class="w"> </span>rocprofiler_t<span class="p">;</span>

Profiling<span class="w"> </span>feature<span class="w"> </span>kind:

typedef<span class="w"> </span>enum<span class="w"> </span><span class="o">{</span>
<span class="w">    </span><span class="nv">ROCPROFILER_FEATURE_KIND_METRIC</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>,<span class="w">    </span>//<span class="w"> </span>metric
<span class="w">    </span><span class="nv">ROCPROFILER_FEATURE_KIND_TRACE</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">1</span><span class="w">      </span>//<span class="w"> </span>trace
<span class="o">}</span><span class="w"> </span>rocprofiler_feature_kind_t<span class="p">;</span>
</pre></div>
</div>
<p>Profiling feature parameter:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>hsa_ven_amd_aqlprofile_parameter_t<span class="w"> </span>rocprofiler_feature_parameter_t<span class="p">;</span>
</pre></div>
</div>
<p>Profiling data kind:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>enum<span class="w"> </span><span class="o">{</span>
<span class="w">    </span><span class="nv">ROCPROFILER_DATA_KIND_UNINIT</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>,<span class="w">       </span>//<span class="w"> </span>data<span class="w"> </span>uninitialized
<span class="w">    </span><span class="nv">ROCPROFILER_DATA_KIND_INT32</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">1</span>,<span class="w">        </span>//<span class="w"> </span>32bit<span class="w"> </span>integer
<span class="w">    </span><span class="nv">ROCPROFILER_DATA_KIND_INT64</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">2</span>,<span class="w">        </span>//<span class="w"> </span>64bit<span class="w"> </span>integer
<span class="w">    </span><span class="nv">ROCPROFILER_DATA_KIND_FLOAT</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">3</span>,<span class="w">        </span>//<span class="w"> </span>float<span class="w"> </span>single-precision<span class="w"> </span>result
<span class="w">    </span><span class="nv">ROCPROFILER_DATA_KIND_DOUBLE</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">4</span>,<span class="w">       </span>//<span class="w"> </span>float<span class="w"> </span>double-precision<span class="w"> </span>result
<span class="w">    </span><span class="nv">ROCPROFILER_DATA_KIND_BYTES</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">5</span><span class="w">         </span>//<span class="w"> </span>trace<span class="w"> </span>output<span class="w"> </span>as<span class="w"> </span>a<span class="w"> </span>bytes<span class="w"> </span>array
<span class="o">}</span><span class="w"> </span>rocprofiler_data_kind_t<span class="p">;</span>
</pre></div>
</div>
<p>Profiling data:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">    </span>rocprofiler_data_kind_t<span class="w"> </span>kind<span class="p">;</span><span class="w">           </span>//<span class="w"> </span>result<span class="w"> </span>kind
<span class="w">    </span>union<span class="w"> </span><span class="o">{</span>
<span class="w">        </span>uint32_t<span class="w"> </span>result_int32<span class="p">;</span><span class="w">              </span>//<span class="w"> </span>32bit<span class="w"> </span>integer<span class="w"> </span>result
<span class="w">        </span>uint64_t<span class="w"> </span>result_int64<span class="p">;</span><span class="w">              </span>//<span class="w"> </span>64bit<span class="w"> </span>integer<span class="w"> </span>result
<span class="w">        </span>float<span class="w"> </span>result_float<span class="p">;</span><span class="w">         </span>//<span class="w"> </span>float<span class="w"> </span>single-precision<span class="w"> </span>result
<span class="w">        </span>double<span class="w"> </span>result_double<span class="p">;</span><span class="w">               </span>//<span class="w"> </span>float<span class="w"> </span>double-precision<span class="w"> </span>result
<span class="w">        </span>typedef<span class="w"> </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">            </span>void*<span class="w"> </span>ptr<span class="p">;</span><span class="w">              </span>//<span class="w"> </span>pointer
<span class="w">            </span>uint32_t<span class="w"> </span>size<span class="p">;</span><span class="w">          </span>//<span class="w"> </span>byte<span class="w"> </span>size
<span class="w">            </span>uint32_t<span class="w"> </span>instances<span class="p">;</span><span class="w">     </span>//<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>trace<span class="w"> </span>instances
<span class="w">        </span><span class="o">}</span><span class="w"> </span>result_bytes<span class="p">;</span><span class="w">                     </span>//<span class="w"> </span>data<span class="w"> </span>by<span class="w"> </span>ptr<span class="w"> </span>and<span class="w"> </span>byte<span class="w"> </span>size
<span class="w">    </span><span class="o">}</span><span class="p">;</span>
<span class="o">}</span><span class="w"> </span>rocprofiler_data_t<span class="p">;</span>
</pre></div>
</div>
<p>Profiling feature:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">    </span>rocprofiler_feature_kind_t<span class="w"> </span>type<span class="p">;</span><span class="w">                        </span>//<span class="w"> </span>feature<span class="w"> </span><span class="nb">type</span>
<span class="w">    </span>const<span class="w"> </span>char*<span class="w"> </span>name<span class="p">;</span><span class="w">                                       </span>//<span class="w"> </span>feature<span class="w"> </span>name
<span class="w">    </span>const<span class="w"> </span>rocprofiler_feature_parameter_t*<span class="w"> </span>parameters<span class="p">;</span><span class="w">      </span>//<span class="w"> </span>feature<span class="w"> </span>parameters
<span class="w">    </span>uint32_t<span class="w"> </span>parameter_count<span class="p">;</span><span class="w">                               </span>//<span class="w"> </span>feature<span class="w"> </span>parameter<span class="w"> </span>count
<span class="w">    </span>rocprofiler_data_t*<span class="w"> </span>data<span class="p">;</span><span class="w">                               </span>//<span class="w"> </span>profiling<span class="w"> </span>data
<span class="o">}</span><span class="w"> </span>rocprofiler_feature_t<span class="p">;</span>
</pre></div>
</div>
<p>Profiling mode masks:</p>
<p>There are several modes which can be specified for the profiling context.
<code class="docutils literal notranslate"><span class="pre">STANDALONE</span></code> mode can be used for the counters sampling in another then application context
to support statistical system-wide profiling. In this mode the profiling context supports
its own queue which can be created on the context open if the <code class="docutils literal notranslate"><span class="pre">CREATEQUEUE</span></code> mode is also specified.
See the <em>Profiler Properties</em> example that follows for the standalone mode queue properties.
The profiler supports several profiling groups for collecting profiling data in several
runs and <code class="docutils literal notranslate"><span class="pre">SINGLEGROUP</span></code> mode allows only one group and the context open will fail if more
groups are needed.</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>enum<span class="w"> </span><span class="o">{</span>
<span class="w">    </span><span class="nv">ROCPROFILER_MODE_STANDALONE</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">1</span>,<span class="w">        </span>//<span class="w"> </span>standalone<span class="w"> </span>mode<span class="w"> </span>when<span class="w"> </span>ROC<span class="w"> </span>profiler
<span class="w">                                            </span>//<span class="w"> </span>supports<span class="w"> </span>own<span class="w"> </span>AQL<span class="w"> </span>queue
<span class="w">    </span><span class="nv">ROCPROFILER_MODE_CREATEQUEUE</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">2</span>,<span class="w">       </span>//<span class="w"> </span>profiler<span class="w"> </span>creates<span class="w"> </span>queue<span class="w"> </span><span class="k">in</span><span class="w"> </span>STANDALONE<span class="w"> </span>mode
<span class="w">    </span><span class="nv">ROCPROFILER_MODE_SINGLEGROUP</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">4</span><span class="w">        </span>//<span class="w"> </span>profiler<span class="w"> </span>allows<span class="w"> </span>one<span class="w"> </span>group<span class="w"> </span>only<span class="w"> </span>and<span class="w"> </span>fails
<span class="w">                                            </span>//<span class="w"> </span><span class="k">if</span><span class="w"> </span>more<span class="w"> </span>groups<span class="w"> </span>are<span class="w"> </span>needed
<span class="o">}</span><span class="w"> </span>rocprofiler_mode_t<span class="p">;</span>
</pre></div>
</div>
<p>Context data readiness callback:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>void<span class="w"> </span><span class="o">(</span>*rocprofiler_context_callback_t<span class="o">)(</span>
<span class="w">    </span>rocprofiler_group_t*<span class="w"> </span>group,<span class="w">             </span>//<span class="w"> </span>profiling<span class="w"> </span>group
<span class="w">    </span>void*<span class="w"> </span>arg<span class="o">)</span><span class="p">;</span><span class="w">                             </span>//<span class="w"> </span>callback<span class="w"> </span>arg
</pre></div>
</div>
<p>Profiler properties:</p>
<p>There are several properties which can be specified for the context. A callback can be
registered which will be called when the context data is ready. In standalone profiling mode
<code class="docutils literal notranslate"><span class="pre">ROCPROFILER_MODE_STANDALONE</span></code> the context supports its own queue, and the queue can be set by
the property <code class="docutils literal notranslate"><span class="pre">queue</span></code> or a queue will be created with the specified depth <code class="docutils literal notranslate"><span class="pre">queue_depth</span></code> if mode
<code class="docutils literal notranslate"><span class="pre">ROCPROFILER_MODE_CREATEQUEUE</span></code> is also specified.</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">    </span>rocprofiler_context_callback_t<span class="w"> </span>callback<span class="p">;</span><span class="w"> </span>//<span class="w"> </span>callback<span class="w"> </span>on<span class="w"> </span>the<span class="w"> </span>context<span class="w"> </span>data<span class="w"> </span>readiness
<span class="w">    </span>void*<span class="w"> </span>callback_arg<span class="p">;</span><span class="w">                      </span>//<span class="w"> </span>callback<span class="w"> </span>arg
<span class="w">    </span>has_queue_t*<span class="w"> </span>queue<span class="p">;</span><span class="w">                      </span>//<span class="w"> </span>HSA<span class="w"> </span>queue<span class="w"> </span><span class="k">for</span><span class="w"> </span>standalone<span class="w"> </span>mode
<span class="w">    </span>uint32_t<span class="w"> </span>queue_depth<span class="p">;</span><span class="w">                    </span>//<span class="w"> </span>created<span class="w"> </span>queue<span class="w"> </span>depth,<span class="w"> </span><span class="k">for</span><span class="w"> </span>create-queue<span class="w"> </span>mode
<span class="o">}</span><span class="w"> </span>rocprofiler_properties_t<span class="p">;</span>
</pre></div>
</div>
<p>Open/close profiling context:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_open<span class="o">(</span>
<span class="w">    </span>hsa_agent_t<span class="w"> </span>agent,<span class="w">                      </span>//<span class="w"> </span>GPU<span class="w"> </span>handle
<span class="w">    </span>rocprofiler_feature_t*<span class="w"> </span>features,<span class="w">        </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>feature<span class="w"> </span>array
<span class="w">    </span>uint32_t<span class="w"> </span>feature_count,<span class="w">                 </span>//<span class="w"> </span>profiling<span class="w"> </span>feature<span class="w"> </span>count
<span class="w">    </span>rocprofiler_t**<span class="w"> </span>context,<span class="w">                </span>//<span class="w"> </span><span class="o">[</span>out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>context<span class="w"> </span>handle
<span class="w">    </span>uint32_t<span class="w"> </span>mode,<span class="w">                          </span>//<span class="w"> </span>profiling<span class="w"> </span>mode<span class="w"> </span>mask
<span class="w">    </span>rocprofiler_properties_t*<span class="w"> </span>properties<span class="o">)</span><span class="p">;</span><span class="w">  </span>//<span class="w"> </span>profiler<span class="w"> </span>properties

hsa_status_t<span class="w"> </span>rocprofiler_close<span class="o">(</span>
<span class="w">    </span>rocprofiler_t*<span class="w"> </span>context<span class="o">)</span><span class="p">;</span><span class="w">                </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span><span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>context
</pre></div>
</div>
<p>Profiling groups:</p>
<p>The profiler on the context open automatically identifies a required number of the application
runs to collect all data needed for all specified metrics, and creates a metric group for each
run. Data for all profiling groups should be collected, and then the metrics can be calculated
by loading the saved groups’ data to the profiling context. Saving and loading of the groups
data is the responsibility of the tool.</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">    </span>uint32_t<span class="w"> </span>index<span class="p">;</span><span class="w">                         </span>//<span class="w"> </span>profiling<span class="w"> </span>group<span class="w"> </span>index
<span class="w">    </span>rocprofiler_feature_t**<span class="w"> </span>features<span class="p">;</span><span class="w">       </span>//<span class="w"> </span>profiling<span class="w"> </span>features<span class="w"> </span>array
<span class="w">    </span>uint32_t<span class="w"> </span>feature_count<span class="p">;</span><span class="w">                 </span>//<span class="w"> </span>profiling<span class="w"> </span>feature<span class="w"> </span>count
<span class="w">    </span>rocprofiler_t*<span class="w"> </span>context<span class="p">;</span><span class="w">                 </span>//<span class="w"> </span>profiling<span class="w"> </span>context<span class="w"> </span>handle
<span class="o">}</span><span class="w"> </span>rocprofiler_group_t<span class="p">;</span>
</pre></div>
</div>
<p>Return profiling groups count:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_group_count<span class="o">(</span>
<span class="w">    </span>rocprofiler_t*<span class="w"> </span>context<span class="o">)</span><span class="p">;</span><span class="w">                </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>context
<span class="w">    </span>uint32*<span class="w"> </span>count<span class="o">)</span><span class="p">;</span><span class="w">                         </span>//<span class="w"> </span><span class="o">[</span>out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>groups<span class="w"> </span>count
</pre></div>
</div>
<p>Return the profiling group for a given index:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_get_group<span class="o">(</span>
<span class="w">    </span>rocprofiler_t*<span class="w"> </span>context,<span class="w">                 </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>context,
<span class="w">                                            </span>//<span class="w"> </span>will<span class="w"> </span>be<span class="w"> </span>returned<span class="w"> </span>as
<span class="w">                        </span>//<span class="w"> </span>a<span class="w"> </span>part<span class="w"> </span>of<span class="w"> </span>the<span class="w"> </span>group<span class="w"> </span>structure
<span class="w">    </span>uint32_t<span class="w"> </span>index,<span class="w">                         </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span><span class="o">]</span><span class="w"> </span>group<span class="w"> </span>index
<span class="w">    </span>rocprofiler_group_t*<span class="w"> </span>group<span class="o">)</span><span class="p">;</span><span class="w">            </span>//<span class="w"> </span><span class="o">[</span>out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>group
</pre></div>
</div>
<p>Calculate metrics data. The data will be stored to the registered profiling features data fields.
After all profiling context data is ready the registered metrics can be calculated. The context
data readiness can be checked by <code class="docutils literal notranslate"><span class="pre">get_data</span></code> API or using the context callback.</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_get_metrics<span class="o">(</span>
<span class="w">    </span>rocprofiler_t*<span class="w"> </span>context<span class="o">)</span><span class="p">;</span><span class="w">                </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>context
</pre></div>
</div>
<p>Method for iterating trace data instances:</p>
<p>Trace data can have several instances, for example, one instance per Shader Engine.</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_iterate_trace_data<span class="o">(</span>
<span class="w">    </span>const<span class="w"> </span>rocprofiler_t*<span class="w"> </span>contex,<span class="w">                    </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span><span class="o">]</span><span class="w"> </span>context<span class="w"> </span>object
<span class="w">    </span>hsa_ven_amd_aqlprofile_data_callback_t<span class="w"> </span>callback,<span class="w"> </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span><span class="o">]</span><span class="w"> </span>callback<span class="w"> </span>to<span class="w"> </span>iterate
<span class="w">                                                    </span>//<span class="w"> </span>the<span class="w"> </span>output<span class="w"> </span>data
<span class="w">    </span>void*<span class="w"> </span>callback_data<span class="o">)</span><span class="p">;</span><span class="w">                           </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>passed<span class="w"> </span>to<span class="w"> </span>callback<span class="w"> </span>data
</pre></div>
</div>
<p>Converting of profiling timestamp to time value for supported time ID.</p>
<p>Supported time value ID enumeration:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>enum<span class="w"> </span><span class="o">{</span>
<span class="nv">ROCPROFILER_TIME_ID_CLOCK_REALTIME</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>,<span class="w">   </span>//<span class="w"> </span>Linux<span class="w"> </span>realtime<span class="w"> </span>clock<span class="w"> </span><span class="nb">time</span>
<span class="nv">ROCPROFILER_TIME_ID_CLOCK_MONOTONIC</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">1</span>,<span class="w">  </span>//<span class="w"> </span>Linux<span class="w"> </span>monotonic<span class="w"> </span>clock<span class="w"> </span><span class="nb">time</span>
<span class="o">}</span><span class="w"> </span>rocprofiler_time_id_t<span class="p">;</span>
</pre></div>
</div>
<p>Method for converting of profiling timestamp to time value for a given time ID:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_get_time<span class="o">(</span>
rocprofiler_time_id_t<span class="w"> </span>time_id,<span class="w">            </span>//<span class="w"> </span>identifier<span class="w"> </span>of<span class="w"> </span>the<span class="w"> </span>particular
<span class="w">                                            </span>//<span class="w"> </span><span class="nb">time</span><span class="w"> </span>to<span class="w"> </span>convert<span class="w"> </span>the<span class="w"> </span>timestamp
uint64_t<span class="w"> </span>timestamp,<span class="w">                       </span>//<span class="w"> </span>profiling<span class="w"> </span>timestamp
uint64_t*<span class="w"> </span>value_ns<span class="o">)</span><span class="p">;</span><span class="w">                      </span>//<span class="w"> </span><span class="o">[</span>out<span class="o">]</span><span class="w"> </span>returned<span class="w"> </span><span class="nb">time</span><span class="w"> </span>‘ns’<span class="w"> </span>value
</pre></div>
</div>
</section>
<section id="sampling-api">
<h3>Sampling API<a class="headerlink" href="#sampling-api" title="Link to this heading">#</a></h3>
<p>The API supports the counters sampling usage model with start/read/stop methods and also lets
to wait for the profiling data in the intercepting usage model with get_data method.</p>
<p>Start/stop/read methods:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_start<span class="o">(</span>
<span class="w">    </span>rocprofiler_t*<span class="w"> </span>context,<span class="w">                 </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>context
<span class="w">    </span>uint32_t<span class="w"> </span><span class="nv">group_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span><span class="o">)</span><span class="p">;</span><span class="w">              </span>//<span class="w"> </span>group<span class="w"> </span>index

hsa_status_t<span class="w"> </span>rocprofiler_stop<span class="o">(</span>
<span class="w">    </span>rocprofiler_t*<span class="w"> </span>context,<span class="w">                 </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>context
<span class="w">    </span>uint32_t<span class="w"> </span><span class="nv">group_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span><span class="o">)</span><span class="p">;</span><span class="w">              </span>//<span class="w"> </span>group<span class="w"> </span>index

hsa_status_t<span class="w"> </span>rocprofiler_read<span class="o">(</span>
<span class="w">    </span>rocprofiler_t*<span class="w"> </span>context,<span class="w">                 </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>context
<span class="w">    </span>uint32_t<span class="w"> </span><span class="nv">group_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span><span class="o">)</span><span class="p">;</span><span class="w">              </span>//<span class="w"> </span>group<span class="w"> </span>index
</pre></div>
</div>
<p>Wait for profiling data:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_get_data<span class="o">(</span>
<span class="w">    </span>rocprofiler_t*<span class="w"> </span>context,<span class="w">                 </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>context
<span class="w">    </span>uint32_t<span class="w"> </span><span class="nv">group_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span><span class="o">)</span><span class="p">;</span><span class="w">              </span>//<span class="w"> </span>group<span class="w"> </span>index
</pre></div>
</div>
<p>Group versions of the above start/stop/read/get_data methods:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_group_start<span class="o">(</span>
<span class="w">    </span>rocprofiler_group_t*<span class="w"> </span>group<span class="o">)</span><span class="p">;</span><span class="w">            </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>group

hsa_status_t<span class="w"> </span>rocprofiler_group_stop<span class="o">(</span>
<span class="w">    </span>rocprofiler_group_t*<span class="w"> </span>group<span class="o">)</span><span class="p">;</span><span class="w">            </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>group


hsa_status_t<span class="w"> </span>rocprofiler_group_read<span class="o">(</span>
<span class="w">    </span>rocprofiler_group_t*<span class="w"> </span>group<span class="o">)</span><span class="p">;</span><span class="w">            </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>group


hsa_status_t<span class="w"> </span>rocprofiler_group_get_data<span class="o">(</span>
<span class="w">    </span>rocprofiler_group_t*<span class="w"> </span>group<span class="o">)</span><span class="p">;</span><span class="w">            </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>group
</pre></div>
</div>
</section>
<section id="intercepting-api">
<h3>Intercepting API<a class="headerlink" href="#intercepting-api" title="Link to this heading">#</a></h3>
<p>The library provides a callback API for enabling profiling for the kernels dispatched to
HSA AQL queues. The API enables per-kernel profiling data collection.
Currently implemented the option with serializing the kernels execution.</p>
<p>ROC profiler callback type:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span><span class="o">(</span>*rocprofiler_callback_t<span class="o">)(</span>
<span class="w">    </span>const<span class="w"> </span>rocprofiler_callback_data_t*<span class="w"> </span>callback_data,<span class="w"> </span>//<span class="w"> </span>callback<span class="w"> </span>data<span class="w"> </span>passed<span class="w"> </span>by<span class="w"> </span>HSA<span class="w"> </span>runtime
<span class="w">    </span>void*<span class="w"> </span>user_data,<span class="w">                                  </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>user<span class="w"> </span>data<span class="w"> </span>passed
<span class="w">                                                    </span>//<span class="w"> </span>to<span class="w"> </span>the<span class="w"> </span>callback
<span class="w">    </span>rocprofiler_group**<span class="w"> </span>group<span class="o">)</span><span class="p">;</span><span class="w">                       </span>//<span class="w"> </span><span class="o">[</span>out<span class="o">]</span><span class="w"> </span>returned<span class="w"> </span>profiling<span class="w"> </span>group
</pre></div>
</div>
<p>Profiling callback data:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">    </span>uint64_t<span class="w"> </span>dispatch<span class="p">;</span><span class="w">                                   </span>//<span class="w"> </span>dispatch<span class="w"> </span>timestamp
<span class="w">    </span>uint64_t<span class="w"> </span>begin<span class="p">;</span><span class="w">                                      </span>//<span class="w"> </span>begin<span class="w"> </span>timestamp
<span class="w">    </span>uint64_t<span class="w"> </span>end<span class="p">;</span><span class="w">                                        </span>//<span class="w"> </span>end<span class="w"> </span>timestamp
<span class="w">    </span>uint64_t<span class="w"> </span>complete<span class="p">;</span><span class="w">                                   </span>//<span class="w"> </span>completion<span class="w"> </span>signal<span class="w"> </span>timestamp
<span class="o">}</span><span class="w"> </span>rocprofiler_dispatch_record_t<span class="p">;</span>

typedef<span class="w"> </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">    </span>hsa_agent_t<span class="w"> </span>agent<span class="p">;</span><span class="w">                                   </span>//<span class="w"> </span>GPU<span class="w"> </span>agent<span class="w"> </span>handle
<span class="w">    </span>uint32_t<span class="w"> </span>agent_index<span class="p">;</span><span class="w">                                </span>//<span class="w"> </span>GPU<span class="w"> </span>index
<span class="w">    </span>const<span class="w"> </span>hsa_queue_t*<span class="w"> </span>queue<span class="p">;</span><span class="w">                            </span>//<span class="w"> </span>HSA<span class="w"> </span>queue
<span class="w">    </span>uint64_t<span class="w"> </span>queue_index<span class="p">;</span><span class="w">                                </span>//<span class="w"> </span>Index<span class="w"> </span><span class="k">in</span><span class="w"> </span>the<span class="w"> </span>queue
<span class="w">    </span>const<span class="w"> </span>hsa_kernel_dispatch_packet_t*<span class="w"> </span>packet<span class="p">;</span><span class="w">          </span>//<span class="w"> </span>HSA<span class="w"> </span>dispatch<span class="w"> </span>packet
<span class="w">    </span>const<span class="w"> </span>char*<span class="w"> </span>kernel_name<span class="p">;</span><span class="w">                             </span>//<span class="w"> </span>Kernel<span class="w"> </span>name
<span class="w">    </span>const<span class="w"> </span>rocprofiler_dispatch_record_t*<span class="w"> </span>record<span class="p">;</span><span class="w">         </span>//<span class="w"> </span>Dispatch<span class="w"> </span>record
<span class="o">}</span><span class="w"> </span>rocprofiler_callback_data_t<span class="p">;</span>
</pre></div>
</div>
<p>Queue callbacks:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">    </span>rocprofiler_callback_t<span class="w"> </span>dispatch<span class="p">;</span><span class="w">                             </span>//<span class="w"> </span>kernel<span class="w"> </span>dispatch<span class="w"> </span>callback
<span class="w">    </span>hsa_status_t<span class="w"> </span><span class="o">(</span>*destroy<span class="o">)(</span>hsa_queue_t*<span class="w"> </span>queue,<span class="w"> </span>void*<span class="w"> </span>data<span class="o">)</span><span class="p">;</span><span class="w">     </span>//<span class="w"> </span>queue<span class="w"> </span>destroy<span class="w"> </span>callback
<span class="o">}</span><span class="w"> </span>rocprofiler_queue_callbacks_t<span class="p">;</span>
</pre></div>
</div>
<p>Adding/removing kernel dispatch and queue destroy callbacks:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_set_intercepting<span class="o">(</span>
<span class="w">    </span>rocprofiler_intercepting_t<span class="w"> </span>callbacks,<span class="w">                        </span>//<span class="w"> </span>intercepting<span class="w"> </span>callbacks
<span class="w">    </span>void*<span class="w"> </span>data<span class="o">)</span><span class="p">;</span><span class="w">                                                 </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>passed<span class="w"> </span>callbacks<span class="w"> </span>data

hsa_status_t<span class="w"> </span>rocprofiler_remove_intercepting<span class="o">()</span><span class="p">;</span>
</pre></div>
</div>
</section>
<section id="profiling-context-pools">
<h3>Profiling context pools<a class="headerlink" href="#profiling-context-pools" title="Link to this heading">#</a></h3>
<p>The API provide capability to create a context pool for a given agent and a set of features, to fetch/release a context entry, to register a callback for  pool’s contexts completion.
Profiling pool handle:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typename<span class="w"> </span>rocprofiler_pool_t<span class="p">;</span>
Profiling<span class="w"> </span>pool<span class="w"> </span>entry:
typedef<span class="w"> </span>struct<span class="w"> </span><span class="o">{</span>
<span class="w">    </span>rocprofiler_t*<span class="w"> </span>context<span class="p">;</span><span class="w">           </span>//<span class="w"> </span>context<span class="w"> </span>object
<span class="w">    </span>void*<span class="w"> </span>payload<span class="p">;</span><span class="w">                    </span>//<span class="w"> </span>payload<span class="w"> </span>data<span class="w"> </span>object
<span class="o">}</span><span class="w"> </span>rocprofiler_pool_entry_t<span class="p">;</span>
</pre></div>
</div>
<p>Profiling handler, calling on profiling completion:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>bool<span class="w"> </span><span class="o">(</span>*rocprofiler_pool_handler_t<span class="o">)(</span>const<span class="w"> </span>rocprofiler_pool_entry_t*<span class="w"> </span>entry,<span class="w"> </span>void*<span class="w"> </span>arg<span class="o">)</span><span class="p">;</span>
</pre></div>
</div>
<p>Profiling properties:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>typedef<span class="w"> </span>struct<span class="w"> </span><span class="o">{</span>
uint32_t<span class="w"> </span>num_entries<span class="p">;</span><span class="w">                    </span>//<span class="w"> </span>pool<span class="w"> </span>size<span class="w"> </span>entries
uint32_t<span class="w"> </span>payload_bytes<span class="p">;</span><span class="w">                  </span>//<span class="w"> </span>payload<span class="w"> </span>size<span class="w"> </span>bytes
rocprofiler_pool_handler_t<span class="w"> </span>handler<span class="p">;</span><span class="w">      </span>//<span class="w"> </span>handler<span class="w"> </span>on<span class="w"> </span>context<span class="w"> </span>completion
void*<span class="w"> </span>handler_arg<span class="p">;</span><span class="w">                       </span>//<span class="w"> </span>the<span class="w"> </span>handler<span class="w"> </span>arg
<span class="o">}</span><span class="w"> </span>rocprofiler_pool_properties_t<span class="p">;</span>
</pre></div>
</div>
<p>Open profiling pool:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_pool_open<span class="o">(</span>
hsa_agent_t<span class="w"> </span>agent,<span class="w">                       </span>//<span class="w"> </span>GPU<span class="w"> </span>handle
rocprofiler_feature_t*<span class="w"> </span>features,<span class="w">         </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span><span class="o">]</span><span class="w"> </span>profiling<span class="w"> </span>features<span class="w"> </span>array
uint32_t<span class="w"> </span>feature_count,<span class="w">                  </span>//<span class="w"> </span>profiling<span class="w"> </span>info<span class="w"> </span>count
rocprofiler_pool_t**<span class="w"> </span>pool,<span class="w">               </span>//<span class="w"> </span><span class="o">[</span>out<span class="o">]</span><span class="w"> </span>context<span class="w"> </span>object
uint32_t<span class="w"> </span>mode,<span class="w">                           </span>//<span class="w"> </span>profiling<span class="w"> </span>mode<span class="w"> </span>mask
rocprofiler_pool_properties_t*<span class="o">)</span><span class="p">;</span><span class="w">         </span>//<span class="w"> </span>pool<span class="w"> </span>properties
</pre></div>
</div>
<p>Close profiling pool:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_pool_close<span class="o">(</span>
rocprofiler_pool_t*<span class="w"> </span>pool<span class="o">)</span><span class="p">;</span><span class="w">               </span>//<span class="w"> </span>profiling<span class="w"> </span>pool<span class="w"> </span>handle
</pre></div>
</div>
<p>Fetch profiling pool entry:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_pool_fetch<span class="o">(</span>
rocprofiler_pool_t*<span class="w"> </span>pool,<span class="w">          </span>//<span class="w"> </span>profiling<span class="w"> </span>pool<span class="w"> </span>handle
rocprofiler_pool_entry_t*<span class="w"> </span>entry<span class="o">)</span><span class="p">;</span><span class="w">  </span>//<span class="w"> </span><span class="o">[</span>out<span class="o">]</span><span class="w"> </span>empty<span class="w"> </span>profiling<span class="w"> </span>pool<span class="w"> </span>entry
</pre></div>
</div>
<p>Release profiling pool entry:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_pool_release<span class="o">(</span>
rocprofiler_pool_entry_t*<span class="w"> </span>entry<span class="o">)</span><span class="p">;</span><span class="w">  </span>//<span class="w"> </span>released<span class="w"> </span>profiling<span class="w"> </span>pool<span class="w"> </span>entry
</pre></div>
</div>
<p>Iterate fetched profiling pool entries:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_pool_iterate<span class="o">(</span>
rocprofiler_pool_t*<span class="w"> </span>pool,<span class="w">           </span>//<span class="w"> </span>profiling<span class="w"> </span>pool<span class="w"> </span>handle
hsa_status_t<span class="w"> </span><span class="o">(</span>*callback<span class="o">)(</span>rocprofiler_pool_entry_t*<span class="w"> </span>entry,<span class="w"> </span>void*<span class="w"> </span>data<span class="o">)</span>,
<span class="w">                                    </span>//<span class="w"> </span>callback
void<span class="w"> </span>*data<span class="o">)</span><span class="p">;</span><span class="w">                               </span>//<span class="w"> </span><span class="o">[</span><span class="k">in</span>/out<span class="o">]</span><span class="w"> </span>data<span class="w"> </span>passed<span class="w"> </span>to<span class="w"> </span>callback
</pre></div>
</div>
<p>Flush completed entries in profiling pool:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>rocprofiler_pool_flush<span class="o">(</span>
<span class="w">    </span>rocprofiler_pool_t*<span class="w"> </span>pool<span class="o">)</span><span class="p">;</span><span class="w">       </span>//<span class="w"> </span>profiling<span class="w"> </span>pool<span class="w"> </span>handle
</pre></div>
</div>
</section>
</section>
<section id="application-code-examples">
<h2>Application code examples<a class="headerlink" href="#application-code-examples" title="Link to this heading">#</a></h2>
<section id="querying-available-metrics">
<h3>Querying available metrics<a class="headerlink" href="#querying-available-metrics" title="Link to this heading">#</a></h3>
<p>Info data callback:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>info_data_callback<span class="o">(</span>const<span class="w"> </span>rocprofiler_info_data_t<span class="w"> </span>info,<span class="w"> </span>void<span class="w"> </span>*data<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>switch<span class="w"> </span><span class="o">(</span>info.kind<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">        </span><span class="k">case</span><span class="w"> </span>ROCPROFILER_INFO_KIND_METRIC:<span class="w"> </span><span class="o">{</span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="o">(</span>info.metric.expr<span class="w"> </span>!<span class="o">=</span><span class="w"> </span>NULL<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">                </span>fprintf<span class="o">(</span>stdout,<span class="w"> </span><span class="s2">&quot;Derived counter:  gpu-agent%d : %s : %s\n&quot;</span>,
<span class="w">                    </span>info.agent_index,<span class="w"> </span>info.metric.name,<span class="w"> </span>info.metric.description<span class="o">)</span><span class="p">;</span>
<span class="w">                </span>fprintf<span class="o">(</span>stdout,<span class="w"> </span><span class="s2">&quot;      %s = %s\n&quot;</span>,<span class="w"> </span>info.metric.name,<span class="w"> </span>info.metric.expr<span class="o">)</span><span class="p">;</span>
<span class="w">            </span><span class="o">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="o">{</span>
<span class="w">                </span>fprintf<span class="o">(</span>stdout,<span class="w"> </span><span class="s2">&quot;Basic counter:  gpu-agent%d : %s&quot;</span>,
<span class="w">                    </span>info.agent_index,<span class="w"> </span>info.metric.name<span class="o">)</span><span class="p">;</span>
<span class="w">                </span><span class="k">if</span><span class="w"> </span><span class="o">(</span>info.metric.instances<span class="w"> </span>&gt;<span class="w"> </span><span class="m">1</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">                    </span>fprintf<span class="o">(</span>stdout,<span class="w"> </span><span class="s2">&quot;[0-%u]&quot;</span>,<span class="w"> </span>info.metric.instances<span class="w"> </span>-<span class="w"> </span><span class="m">1</span><span class="o">)</span><span class="p">;</span>
<span class="w">                </span><span class="o">}</span>
<span class="w">                </span>fprintf<span class="o">(</span>stdout,<span class="w"> </span><span class="s2">&quot; : %s\n&quot;</span>,<span class="w"> </span>info.metric.description<span class="o">)</span><span class="p">;</span>
<span class="w">                </span>fprintf<span class="o">(</span>stdout,<span class="w"> </span><span class="s2">&quot;      block %s has %u counters\n&quot;</span>,
<span class="w">                    </span>info.metric.block_name,<span class="w"> </span>info.metric.block_counters<span class="o">)</span><span class="p">;</span>
<span class="w">            </span><span class="o">}</span>
<span class="w">            </span>fflush<span class="o">(</span>stdout<span class="o">)</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="o">}</span>
<span class="w">        </span>default:
<span class="w">            </span>printf<span class="o">(</span><span class="s2">&quot;wrong info kind %u\n&quot;</span>,<span class="w"> </span>kind<span class="o">)</span><span class="p">;</span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span>HSA_STATUS_ERROR<span class="p">;</span>
<span class="w">    </span><span class="o">}</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span>HSA_STATUS_SUCCESS<span class="p">;</span>
<span class="o">}</span>
</pre></div>
</div>
<p>Printing all available metrics:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_iterate_info<span class="o">(</span>
<span class="w">    </span>agent,
<span class="w">    </span>ROCPROFILER_INFO_KIND_METRIC,
<span class="w">    </span>info_data_callback,
<span class="w">    </span>NULL<span class="o">)</span><span class="p">;</span>
&lt;check<span class="w"> </span>status&gt;
</pre></div>
</div>
</section>
<section id="profiling-code-example">
<h3>Profiling code example<a class="headerlink" href="#profiling-code-example" title="Link to this heading">#</a></h3>
<p>Profiling of L1 miss ratio, average memory bandwidth</p>
<p>In the example below <code class="docutils literal notranslate"><span class="pre">rocprofiler_group_get_data</span></code> group APIs are used for the purpose of a usage
example but in <code class="docutils literal notranslate"><span class="pre">SINGLEGROUP</span></code> mode when only one group is allowed the context handle itself can be
saved and then direct context method <code class="docutils literal notranslate"><span class="pre">rocprofiler_get_data</span></code> with default group index equal to 0
can be used.</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>hsa_status_t<span class="w"> </span>dispatch_callback<span class="o">(</span>
<span class="w">    </span>const<span class="w"> </span>rocprofiler_callback_data_t*<span class="w"> </span>callback_data,
<span class="w">    </span>void*<span class="w"> </span>user_data,
<span class="w">    </span>rocprofiler_group_t*<span class="w"> </span>group<span class="o">)</span>
<span class="o">{</span>
<span class="w">    </span>hsa_status_t<span class="w"> </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>HSA_STATUS_SUCCESS<span class="p">;</span>
<span class="w">    </span>//<span class="w"> </span>Profiling<span class="w"> </span>context
<span class="w">    </span>rocprofiler_t*<span class="w"> </span>context<span class="p">;</span>
<span class="w">    </span>//<span class="w"> </span>Profiling<span class="w"> </span>info<span class="w"> </span>objects
<span class="w">    </span>rocprofiler_feature_t<span class="w"> </span>features*<span class="w"> </span><span class="o">=</span><span class="w"> </span>new<span class="w"> </span>rocprofiler_feature_t<span class="o">[</span><span class="m">2</span><span class="o">]</span><span class="p">;</span>
<span class="w">    </span>//<span class="w"> </span>Tracing<span class="w"> </span>parameters
<span class="w">    </span>rocprofiler_feature_parameter_t*<span class="w"> </span><span class="nv">parameters</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>new<span class="w"> </span>rocprofiler_feature_parameter_t<span class="o">[</span><span class="m">2</span><span class="o">]</span><span class="p">;</span>

<span class="w">    </span>//<span class="w"> </span>Setting<span class="w"> </span>profiling<span class="w"> </span>features
<span class="w">    </span>features<span class="o">[</span><span class="m">0</span><span class="o">]</span>.type<span class="w"> </span><span class="o">=</span><span class="w"> </span>ROCPROFILER_METRIC<span class="p">;</span>
<span class="w">    </span>features<span class="o">[</span><span class="m">0</span><span class="o">]</span>.name<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;L1_MISS_RATIO&quot;</span><span class="p">;</span>
<span class="w">    </span>features<span class="o">[</span><span class="m">1</span><span class="o">]</span>.type<span class="w"> </span><span class="o">=</span><span class="w"> </span>ROCPROFILER_METRIC<span class="p">;</span>
<span class="w">    </span>features<span class="o">[</span><span class="m">1</span><span class="o">]</span>.name<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;DRAM_BANDWIDTH&quot;</span><span class="p">;</span>

<span class="w">    </span>//<span class="w"> </span>Creating<span class="w"> </span>profiling<span class="w"> </span>context
<span class="w">    </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_open<span class="o">(</span>callback_data-&gt;dispatch.agent,<span class="w"> </span>features,<span class="w"> </span><span class="m">2</span>,<span class="w"> </span><span class="p">&amp;</span>context,
<span class="w">        </span>ROCPROFILER_MODE_SINGLEGROUP,<span class="w"> </span>NULL<span class="o">)</span><span class="p">;</span>
<span class="w">    </span>&lt;check<span class="w"> </span>status&gt;

<span class="w">    </span>//<span class="w"> </span>Get<span class="w"> </span>the<span class="w"> </span>profiling<span class="w"> </span>group
<span class="w">    </span>//<span class="w"> </span>For<span class="w"> </span>general<span class="w"> </span><span class="k">case</span><span class="w"> </span>with<span class="w"> </span>many<span class="w"> </span>groups<span class="w"> </span>there<span class="w"> </span>is<span class="w"> </span>rocprofiler_group_count<span class="o">()</span><span class="w"> </span>API
<span class="w">    </span>const<span class="w"> </span>uint32_t<span class="w"> </span><span class="nv">group_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>
<span class="w">    </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_get_group<span class="o">(</span>context,<span class="w"> </span>group_index,<span class="w"> </span>group<span class="o">)</span><span class="p">;</span>
<span class="w">    </span>&lt;check_status&gt;

<span class="w">    </span>//<span class="w"> </span>In<span class="w"> </span>SINGLEGROUP<span class="w"> </span>mode<span class="w"> </span>the<span class="w"> </span>context<span class="w"> </span>handle<span class="w"> </span>itself<span class="w"> </span>can<span class="w"> </span>be<span class="w"> </span>saved,<span class="w"> </span>because<span class="w"> </span>there<span class="w"> </span>is<span class="w"> </span>just<span class="w"> </span>one<span class="w"> </span>group
<span class="w">    </span>&lt;saving<span class="w"> </span>the<span class="w"> </span>callback<span class="w"> </span>data/profiling<span class="w"> </span>group/profiling<span class="w"> </span>features&gt;

<span class="w">    </span><span class="k">return</span><span class="w"> </span>status<span class="p">;</span>
<span class="o">}</span>
</pre></div>
</div>
<p>Profiling tool constructor is adding the dispatch callback:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>void<span class="w"> </span>profiling_libary_constructor<span class="o">()</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>//<span class="w"> </span>Defining<span class="w"> </span>callback<span class="w"> </span>data,<span class="w"> </span>no<span class="w"> </span>data<span class="w"> </span><span class="k">in</span><span class="w"> </span>this<span class="w"> </span>simple<span class="w"> </span>example
<span class="w">    </span>void*<span class="w"> </span><span class="nv">callback_data</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>NULL<span class="p">;</span>

<span class="w">    </span>//<span class="w"> </span>Adding<span class="w"> </span>observers
<span class="w">    </span>hsa_sttaus_t<span class="w"> </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_add_dispatch_callback<span class="o">(</span>dispatch_callback,<span class="w"> </span>callback_data<span class="o">)</span><span class="p">;</span>
<span class="w">    </span>&lt;check<span class="w"> </span>status&gt;

<span class="w">    </span>//<span class="w"> </span>Dispatching<span class="w"> </span>profiled<span class="w"> </span>kernel
<span class="w">    </span>&lt;dispatching<span class="w"> </span>profiled<span class="w"> </span>kernels&gt;
<span class="o">}</span>

void<span class="w"> </span>profiling_libary_destructor<span class="o">()</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>&lt;<span class="k">for</span><span class="w"> </span>entry<span class="w"> </span>:<span class="w"> </span>&lt;saved<span class="w"> </span>callbacks<span class="w"> </span>data&gt;&gt;<span class="w"> </span><span class="o">{</span>
<span class="w">        </span>//<span class="w"> </span>In<span class="w"> </span>SINGLEGROUP<span class="w"> </span>mode<span class="w"> </span>the<span class="w"> </span>rocprofiler_get_group<span class="o">()</span><span class="w"> </span>method<span class="w"> </span>with<span class="w"> </span>default<span class="w"> </span>zero<span class="w"> </span>group
<span class="w">        </span>//<span class="w"> </span>index<span class="w"> </span>can<span class="w"> </span>be<span class="w"> </span>used,<span class="w"> </span><span class="k">if</span><span class="w"> </span>context<span class="w"> </span>handle<span class="w"> </span>would<span class="w"> </span>be<span class="w"> </span>saved
<span class="w">        </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_group_get_data<span class="o">(</span>entry-&gt;group<span class="o">)</span><span class="p">;</span>
<span class="w">        </span>&lt;check<span class="w"> </span>status&gt;
<span class="w">        </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_get_metrics<span class="o">(</span>entry-&gt;group-&gt;context<span class="o">)</span><span class="p">;</span>
<span class="w">        </span>&lt;check<span class="w"> </span>status&gt;
<span class="w">        </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_close<span class="o">(</span>entry-&gt;group-&gt;context<span class="o">)</span><span class="p">;</span>
<span class="w">        </span>&lt;check<span class="w"> </span>status&gt;

<span class="w">        </span>&lt;tool_dump_data_method<span class="o">(</span>entry-&gt;dispatch_data,<span class="w"> </span>entry-&gt;features,<span class="w"> </span>entry-&gt;features_count<span class="o">)</span>&gt;<span class="p">;</span>
<span class="w">    </span><span class="o">}</span>
<span class="o">}</span>
</pre></div>
</div>
</section>
<section id="option-to-use-completion-callback">
<h3>Option to use completion callback<a class="headerlink" href="#option-to-use-completion-callback" title="Link to this heading">#</a></h3>
<p>Creating profiling context with completion callback:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>...
rocprofiler_properties_t<span class="w"> </span><span class="nv">properties</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">{}</span><span class="p">;</span>
properties.callback<span class="w"> </span><span class="o">=</span><span class="w"> </span>completion_callback<span class="p">;</span>
properties.callback_arg<span class="w"> </span><span class="o">=</span><span class="w"> </span>NULL<span class="p">;</span><span class="w">     </span>//<span class="w"> </span>no<span class="w"> </span>args<span class="w"> </span>defined
<span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_open<span class="o">(</span>agent,<span class="w"> </span>features,<span class="w"> </span><span class="m">3</span>,<span class="w"> </span><span class="p">&amp;</span>context,
<span class="w">    </span>ROCPROFILER_MODE_SINGLEGROUP,<span class="w"> </span>properties<span class="o">)</span><span class="p">;</span>
&lt;check<span class="w"> </span>status&gt;
...
</pre></div>
</div>
<p>Definition of completion callback:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>void<span class="w"> </span>completion_callback<span class="o">(</span>profiler_group_t<span class="w"> </span>group,<span class="w"> </span>void*<span class="w"> </span>arg<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>&lt;tool_dump_data_method<span class="o">(</span>group<span class="o">)</span>&gt;
<span class="w">    </span>hsa_status_t<span class="w"> </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_close<span class="o">(</span>group.context<span class="o">)</span><span class="p">;</span>
<span class="w">    </span>&lt;check<span class="w"> </span>status&gt;
<span class="o">}</span>
</pre></div>
</div>
</section>
<section id="option-to-use-context-pool">
<h3>Option to use context pool<a class="headerlink" href="#option-to-use-context-pool" title="Link to this heading">#</a></h3>
<p>Code example of context pool usage.</p>
<p>Creating profiling contexts pool:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="w"> </span>...
rocprofiler_pool_properties_t<span class="w"> </span>properties<span class="o">{}</span><span class="p">;</span>
properties.num_entries<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">100</span><span class="p">;</span>
properties.payload_bytes<span class="w"> </span><span class="o">=</span><span class="w"> </span>sizeof<span class="o">(</span>context_entry_t<span class="o">)</span><span class="p">;</span>
properties.handler<span class="w"> </span><span class="o">=</span><span class="w"> </span>context_handler<span class="p">;</span>
properties.handler_arg<span class="w"> </span><span class="o">=</span><span class="w"> </span>handler_arg<span class="p">;</span>
<span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_pool_open<span class="o">(</span>agent,<span class="w"> </span>features,<span class="w"> </span><span class="m">3</span>,<span class="w"> </span><span class="p">&amp;</span>context,
<span class="w">             </span>ROCPROFILER_MODE_SINGLEGROUP,<span class="w"> </span>properties<span class="o">)</span><span class="p">;</span>
&lt;check<span class="w"> </span>status&gt;
<span class="w"> </span>...
</pre></div>
</div>
<p>Fetching a context entry:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="w"> </span>rocprofiler_pool_entry_t<span class="w"> </span>pool_entry<span class="o">{}</span><span class="p">;</span>
<span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_pool_fetch<span class="o">(</span>pool,<span class="w"> </span><span class="p">&amp;</span>pool_entry<span class="o">)</span><span class="p">;</span>
&lt;check<span class="w"> </span>status&gt;
//<span class="w"> </span>Profiling<span class="w"> </span>context<span class="w"> </span>entry
rocprofiler_t*<span class="w"> </span><span class="nv">context</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>pool_entry.context<span class="p">;</span>
context_entry_t*<span class="w"> </span><span class="nv">entry</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>reinterpret_cast<span class="w"> </span>&lt;context_entry_t*&gt;
<span class="w">                         </span><span class="o">(</span>pool_entry.payload<span class="o">)</span><span class="p">;</span>
</pre></div>
</div>
</section>
<section id="standalone-sampling-usage-code-example">
<h3>Standalone sampling usage code example<a class="headerlink" href="#standalone-sampling-usage-code-example" title="Link to this heading">#</a></h3>
<p>The profiling metrics are being read from separate standalone queue other than the application kernels are submitted to.
To enable the sampling mode, the profiling mode in all user queues should be enabled.  It can be done by loading ROC-profiler
library to HSA runtime using the environment variable <code class="docutils literal notranslate"><span class="pre">HSA_TOOLS_LIB</span></code> for all shell sessions.</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="w"> </span>//<span class="w"> </span>Sampling<span class="w"> </span>rate
uint32_t<span class="w"> </span><span class="nv">sampling_rate</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>&lt;some<span class="w"> </span>rate&gt;<span class="p">;</span>
//<span class="w"> </span>Sampling<span class="w"> </span>count
uint32_t<span class="w"> </span><span class="nv">sampling_count</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>&lt;some<span class="w"> </span>count&gt;<span class="p">;</span>
//<span class="w"> </span>HSA<span class="w"> </span>status
hsa_status_t<span class="w"> </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>HSA_STATUS_ERROR<span class="p">;</span>
//<span class="w"> </span>HSA<span class="w"> </span>agent
hsa_agent_t<span class="w"> </span>agent<span class="p">;</span>
//<span class="w"> </span>Profiling<span class="w"> </span>context
rocprofiler_t*<span class="w"> </span><span class="nv">context</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>NULL<span class="p">;</span>
//<span class="w"> </span>Profiling<span class="w"> </span>properties
rocprofiler_properties_t<span class="w"> </span>properties<span class="p">;</span>

//<span class="w"> </span>Getting<span class="w"> </span>HSA<span class="w"> </span>agent
&lt;query<span class="w"> </span><span class="k">for</span><span class="w"> </span>HSA<span class="w"> </span>agent<span class="w"> </span>by<span class="w"> </span>‘hsa_iterate_agents<span class="o">()</span>’&gt;

//<span class="w"> </span>Profiling<span class="w"> </span>feature<span class="w"> </span>objects
const<span class="w"> </span>unsigned<span class="w"> </span><span class="nv">feature_count</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">2</span><span class="p">;</span>
rocprofiler_feature_t<span class="w"> </span>feature<span class="o">[</span>feature_count<span class="o">]</span><span class="p">;</span>

//<span class="w"> </span>Counters<span class="w"> </span>and<span class="w"> </span>metrics
feature<span class="o">[</span><span class="m">0</span><span class="o">]</span>.kind<span class="w"> </span><span class="o">=</span><span class="w"> </span>ROCPROFILER_FEATURE_KIND_METRIC<span class="p">;</span>
feature<span class="o">[</span><span class="m">0</span><span class="o">]</span>.name<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;GPUBusy&quot;</span><span class="p">;</span>
feature<span class="o">[</span><span class="m">1</span><span class="o">]</span>.kind<span class="w"> </span><span class="o">=</span><span class="w"> </span>ROCPROFILER_FEATURE_KIND_METRIC<span class="p">;</span>
feature<span class="o">[</span><span class="m">1</span><span class="o">]</span>.name<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;SQ_WAVES&quot;</span><span class="p">;</span>

//<span class="w"> </span>Creating<span class="w"> </span>profiling<span class="w"> </span>context<span class="w"> </span>with<span class="w"> </span>standalone<span class="w"> </span>queue
<span class="nv">properties</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">{}</span><span class="p">;</span>
properties.queue_depth<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">128</span><span class="p">;</span>
<span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_open<span class="o">(</span>agent,<span class="w"> </span>feature,<span class="w"> </span>feature_count,<span class="w"> </span><span class="p">&amp;</span>context,
<span class="w">         </span>ROCPROFILER_MODE_STANDALONE<span class="p">|</span><span class="w"> </span>ROCPROFILER_MODE_CREATEQUEUE<span class="p">|</span>
<span class="w">         </span>ROCPROFILER_MODE_SINGLEGROUP,<span class="w"> </span><span class="p">&amp;</span>properties<span class="o">)</span><span class="p">;</span>
&lt;check<span class="w"> </span>status&gt;

//<span class="w"> </span>Start<span class="w"> </span>counters<span class="w"> </span>and<span class="w"> </span>sample<span class="w"> </span>them<span class="w"> </span><span class="k">in</span><span class="w"> </span>the<span class="w"> </span>loop<span class="w"> </span>with<span class="w"> </span>the<span class="w"> </span>sampling<span class="w"> </span>rate
<span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_start<span class="o">(</span>context,<span class="w"> </span><span class="m">0</span><span class="o">)</span><span class="p">;</span>
&lt;check<span class="w"> </span>status&gt;

<span class="k">for</span><span class="w"> </span><span class="o">(</span>unsigned<span class="w"> </span><span class="nv">ind</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span><span class="p">;</span><span class="w"> </span>ind<span class="w"> </span>&lt;<span class="w"> </span>sampling_count<span class="p">;</span><span class="w"> </span>++ind<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">   </span>sleep<span class="o">(</span>sampling_rate<span class="o">)</span><span class="p">;</span>
<span class="w">   </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_read<span class="o">(</span>context,<span class="w"> </span><span class="m">0</span><span class="o">)</span><span class="p">;</span>
<span class="w">   </span>&lt;check<span class="w"> </span>status&gt;
<span class="w">   </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_get_data<span class="o">(</span>context,<span class="w"> </span><span class="m">0</span><span class="o">)</span><span class="p">;</span>
<span class="w">   </span>&lt;check<span class="w"> </span>status&gt;
<span class="w">   </span><span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_get_metrics<span class="o">(</span>context<span class="o">)</span><span class="p">;</span>
<span class="w">   </span>&lt;check<span class="w"> </span>status&gt;
<span class="w">   </span>print_results<span class="o">(</span>feature,<span class="w"> </span>feature_count<span class="o">)</span><span class="p">;</span>
<span class="o">}</span>

//<span class="w"> </span>Stop<span class="w"> </span>counters
<span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_stop<span class="o">(</span>context,<span class="w"> </span>group_n<span class="o">)</span><span class="p">;</span>
&lt;check<span class="w"> </span>status&gt;

//<span class="w"> </span>Finishing<span class="w"> </span>cleanup
//<span class="w"> </span>Deleting<span class="w"> </span>profiling<span class="w"> </span>context<span class="w"> </span>will<span class="w"> </span>delete<span class="w"> </span>all<span class="w"> </span>allocated<span class="w"> </span>resources
<span class="nv">status</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>rocprofiler_close<span class="o">(</span>context<span class="o">)</span><span class="p">;</span>
&lt;check<span class="w"> </span>status&gt;
</pre></div>
</div>
</section>
<section id="printing-out-profiling-results">
<h3>Printing out profiling results<a class="headerlink" href="#printing-out-profiling-results" title="Link to this heading">#</a></h3>
<p>The following is a code example for printing out the profiling results from profiling features array:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>void<span class="w"> </span>print_results<span class="o">(</span>rocprofiler_feature_t*<span class="w"> </span>feature,<span class="w"> </span>uint32_t<span class="w"> </span>feature_count<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="k">for</span><span class="w"> </span><span class="o">(</span>rocprofiler_feature_t*<span class="w"> </span><span class="nv">p</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>feature<span class="p">;</span><span class="w"> </span>p<span class="w"> </span>&lt;<span class="w"> </span>feature<span class="w"> </span>+<span class="w"> </span>feature_count<span class="p">;</span><span class="w"> </span>++p<span class="o">)</span>
<span class="o">{</span>
<span class="w">    </span>std::cout<span class="w"> </span>&lt;&lt;<span class="w"> </span><span class="o">(</span>p<span class="w"> </span>-<span class="w"> </span>feature<span class="o">)</span><span class="w"> </span>&lt;&lt;<span class="w"> </span><span class="s2">&quot;: &quot;</span><span class="w"> </span><span class="s">&lt;&lt; p-&gt;name;</span>
<span class="s">    switch (p</span>-&gt;data.kind<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">        </span><span class="k">case</span><span class="w"> </span>ROCPROFILER_DATA_KIND_INT64:
<span class="w">            </span>std::cout<span class="w"> </span>&lt;&lt;<span class="w"> </span><span class="s2">&quot; result_int64 (&quot;</span><span class="w"> </span><span class="s">&lt;&lt; p-&gt;data.result_int64 &lt;&lt; &quot;)&quot;</span>
<span class="s">                    &lt;&lt; std::endl;</span>
<span class="s">            break;</span>

<span class="s">        case ROCPROFILER_DATA_KIND_BYTES: {</span>
<span class="s">            std::cout &lt;&lt; &quot; result_bytes p</span>tr<span class="o">(</span><span class="s2">&quot; &lt;&lt; p-&gt;data.result_bytes.ptr &lt;&lt;</span>
<span class="s2">                &quot;</span><span class="o">)</span><span class="w"> </span><span class="s2">&quot; &lt;&lt; &quot;</span><span class="w"> </span>size<span class="o">(</span><span class="s2">&quot; &lt;&lt; p-&gt;data.result_bytes.size &lt;&lt; &quot;</span><span class="o">)</span><span class="s2">&quot;</span>
<span class="s2">                &lt;&lt; &quot;</span><span class="w"> </span>instance_count<span class="o">(</span><span class="s2">&quot; &lt;&lt; p-&gt;data.result_bytes.instance_count</span>
<span class="s2">                &lt;&lt; &quot;</span><span class="o">)</span><span class="s2">&quot;;</span>
<span class="s2">            break;</span>
<span class="s2">        }</span>
<span class="s2">        default:</span>
<span class="s2">            std::cout &lt;&lt; &quot;</span>bad<span class="w"> </span>result<span class="w"> </span>kind<span class="w"> </span><span class="o">(</span><span class="s2">&quot; &lt;&lt; p-&gt;data.kind &lt;&lt; &quot;</span><span class="o">)</span><span class="s2">&quot;</span>
<span class="s2">                    &lt;&lt; std::endl;</span>
<span class="s2">            &lt;abort&gt;</span>
<span class="s2">    }</span>
<span class="s2">}</span>
<span class="s2">}</span>
</pre></div>
</div>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../how-to/using-rocsys.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Using rocsys</p>
      </div>
    </a>
    <a class="right-next"
       href="../doxygen/html/index.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">ROCProfiler API library</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#environment-variables">Environment variables</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#logging">Logging</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#general-api">General API</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#returning-the-error-and-error-string-methods">Returning the error and error string methods</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-version">Library version</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#backend-api">Backend API</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#loading-and-configuring">Loading and configuring</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#info-api">Info API</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#context-api">Context API</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#sampling-api">Sampling API</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#intercepting-api">Intercepting API</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#profiling-context-pools">Profiling context pools</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#application-code-examples">Application code examples</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#querying-available-metrics">Querying available metrics</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#profiling-code-example">Profiling code example</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#option-to-use-completion-callback">Option to use completion callback</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#option-to-use-context-pool">Option to use context pool</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#standalone-sampling-usage-code-example">Standalone sampling usage code example</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#printing-out-profiling-results">Printing out profiling results</a></li>
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
