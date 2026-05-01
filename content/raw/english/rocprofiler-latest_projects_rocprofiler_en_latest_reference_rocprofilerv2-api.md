---
title: "ROCProfilerV2 API &#8212; ROCProfiler 2.0.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler/en/latest/reference/rocprofilerv2-api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:29:12.518820+00:00
content_hash: "600ab699151a890f"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Use of rocprofv2 API" name="description" />
<meta content="ROCProfilerV2 tool, ROCProfilerV2 library, rocprofv2, ROCm, API, reference" name="keywords" />

    <title>ROCProfilerV2 API &#8212; ROCProfiler 2.0.0 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/rocprofilerv2-api';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="License" href="../license.html" />
    <link rel="prev" title="Globals" href="../doxygen/html/globals_defs.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-docs" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/rocprofilerv2-api.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1"><a class="reference internal" href="rocprofiler_spec.html">ROCProfiler library specification</a></li>
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
<li class="toctree-l1 current active"><a class="current reference internal" href="#">ROCProfilerV2 API</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">ROCProfilerV2 API</li>
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
    <h1>ROCProfilerV2 API</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#profiling-sessions">Profiling sessions</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#id2">Filters</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#application-tracing-1">Application tracing</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-profiling-1">Kernel profiling</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#environment-variables">Environment variables</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="rocprofilerv2-api">
<span id="id1"></span><h1>ROCProfilerV2 API<a class="headerlink" href="#rocprofilerv2-api" title="Link to this heading">#</a></h1>
<p>ROCProfilerV2 provides an API that allows fine-grained control over the
profiling process. Like the CLI tool <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code>, the API supports both application
tracing and kernel profiling. ROCProfilerV2 API allows you to create a session
and invoke application tracing or kernel profiling within the session. The following
sections describe session management, application tracing and kernel profiling
using ROCProfilerV2 API.</p>
<section id="profiling-sessions">
<h2>Profiling sessions<a class="headerlink" href="#profiling-sessions" title="Link to this heading">#</a></h2>
<p>A ROCProfilerV2 session maintains the global profiling state for an
application. It is a unique identifier for a profiling or tracing task
that is specified within the session. A session contains sufficient
information about what needs to be collected or traced and it allows you
to start/stop profiling/tracing as and when required.</p>
<p>The following demonstrates the use of session management APIs:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Initialize the tools</span>
<span class="w">   </span><span class="n">rocprofiler_initialize</span><span class="p">();</span>

<span class="c1">// Create the session with no replay mode</span>
<span class="w">   </span><span class="n">rocprofiler_session_id_t</span><span class="w"> </span><span class="n">session_id</span><span class="p">;</span>
<span class="w">   </span><span class="n">rocprofiler_create_session</span><span class="p">(</span><span class="n">ROCPROFILER_NONE_REPLAY_MODE</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">session_id</span><span class="p">);</span>

<span class="c1">// Start Session</span>
<span class="w">   </span><span class="n">rocprofiler_start_session</span><span class="p">(</span><span class="n">session_id</span><span class="p">);</span>

<span class="c1">// profile a kernel -kernelA</span>
<span class="w">   </span><span class="n">hipLaunchKernelGGL</span><span class="p">(</span><span class="n">kernelA</span><span class="p">,</span><span class="w"> </span><span class="n">dim3</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span><span class="w"> </span><span class="n">dim3</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>

<span class="c1">// Deactivating session</span>
<span class="w">   </span><span class="n">rocprofiler_terminate_session</span><span class="p">(</span><span class="n">session_id</span><span class="p">);</span>

<span class="c1">// Destroy sessions</span>
<span class="w">   </span><span class="n">rocprofiler_destroy_session</span><span class="p">(</span><span class="n">session_id</span><span class="p">);</span>

<span class="c1">// Destroy all profiling related objects</span>
<span class="w">   </span><span class="n">rocprofiler_finalize</span><span class="p">();</span>
</pre></div>
</div>
<p>The following is a typical session management workflow:</p>
<ol class="arabic">
<li><p>Initialize ROCProfilerV2 using <code class="docutils literal notranslate"><span class="pre">rocprofiler_initialize</span></code>.</p></li>
<li><p>Create a session using <code class="docutils literal notranslate"><span class="pre">rocprofiler_create_session</span></code>. The created
session keeps track of the global status of the application
profiling.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>You can only create a session in no-replay mode
(ROCPROFILER_NONE_REPLAY_MODE) which allows kernels to be
run only once.</p>
</div>
</li>
<li><p>Create a buffer to hold the results using <code class="docutils literal notranslate"><span class="pre">rocprofiler_create_buffer</span></code>.</p></li>
<li><p>Create filters using <code class="docutils literal notranslate"><span class="pre">rocprofiler_create_filter</span></code> to specify the
profiling task such as application tracing or metrics/counters
collection.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If the same filter is applied twice with different values, the latter
application of the filter is considered the recent one, which overwrites
the former application of the filter. To learn about the types of filters
and their utility, see <a class="reference external" href="#filters">Filters</a>.</p>
</div>
</li>
<li><p>Start the session with <code class="docutils literal notranslate"><span class="pre">rocprofiler_start_session</span></code>.</p></li>
<li><p>Run the specified kernels to collect traces or counters/metrics (as
specified in the filter)</p></li>
<li><p>Terminate the session with <code class="docutils literal notranslate"><span class="pre">rocprofiler_terminate_session</span></code> and flush
the profiling results using <code class="docutils literal notranslate"><span class="pre">rocprofiler_flush_data</span></code>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The session must be terminated after the kernel completes (synchronization
required). If a session is stopped before the completion of kernel execution
within that session, the instrumentation data is undefined. Additionally,
a session can be restarted after terminating.</p>
</div>
</li>
<li><p>Destroy the session with <code class="docutils literal notranslate"><span class="pre">rocprofiler_destroy_session</span></code> and finalize
profiling with <code class="docutils literal notranslate"><span class="pre">rocprofiler_finalize</span></code>.</p></li>
</ol>
<p>See working examples demonstrating the use of the ROCProfilerV2 API in <a class="reference external" href="#_Application_Tracing_1">Application
Tracing</a> and <a class="reference external" href="#kernel-profiling-1">Kernel Profiling</a>.</p>
</section>
<section id="id2">
<h2>Filters<a class="headerlink" href="#id2" title="Link to this heading">#</a></h2>
<p>As explained in <a class="reference external" href="#profiling-sessions">Profiling Sessions</a>, filters
allow you to specify a profiling task within a session. For different
profiling tasks, different filters are specified as a parameter to
<code class="docutils literal notranslate"><span class="pre">rocprofiler_create_filter</span></code>.</p>
<p>See the list of filters in the table below:</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Filter</p></th>
<th class="head"><p>Purpose</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCPROFILER_API_TRACE</span></code></p></td>
<td><p>To trace API calls. You must
specify the API calls to be
traced, in a vector.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCPROFILER_DISPATCH</span>
<span class="pre">_TIMESTAMPS_COLLECTION</span></code></p></td>
<td><p>To track all the kernel
execution’s start and end times
on the GPUs</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCPROFILER_COUNTERS_COLLECTION</span></code></p></td>
<td><p>To collect counters. You must
specify the counters to be
collected, in a vector.</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="application-tracing-1">
<span id="id4"></span><h2>Application tracing<a class="headerlink" href="#application-tracing-1" title="Link to this heading">#</a></h2>
<p>The following code demonstrates the usage of ROCProfilerV2 APIs to
trace an application. This example traces HIP APIs, HIP
asynchronous activities, HSA APIs, HSA asynchronous activities, and
ROCTX ranges. Note the use of <code class="docutils literal notranslate"><span class="pre">ROCPROFILER_API_TRACE</span></code> filter to trace
API calls, and <code class="docutils literal notranslate"><span class="pre">ROCPROFILER_DISPATCH_TIMESTAMPS_COLLECTION</span></code> filter to trace the
kernel.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">argc</span><span class="p">,</span><span class="w"> </span><span class="kt">char</span><span class="o">*</span><span class="err">\</span><span class="o">*</span><span class="w"> </span><span class="n">argv</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="kt">int</span><span class="err">\</span><span class="o">*</span><span class="w"> </span><span class="n">gpuMem</span><span class="p">;</span>
<span class="w">   </span><span class="n">prepare</span><span class="p">();</span>
<span class="w">   </span><span class="c1">// Initialize the tools</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_initialize</span><span class="p">());</span>

<span class="w">   </span><span class="c1">// Creating the session with given replay mode</span>
<span class="w">   </span><span class="n">rocprofiler_session_id_t</span><span class="w"> </span><span class="n">session_id</span><span class="p">;</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_create_session</span><span class="p">(</span><span class="n">ROCPROFILER_NONE_REPLAY_MODE</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">session_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Creating Output Buffer for the data</span>
<span class="w">   </span><span class="n">rocprofiler_buffer_id_t</span><span class="w"> </span><span class="n">buffer_id</span><span class="p">;</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_create_buffer</span><span class="p">(</span><span class="n">session_id</span><span class="p">,</span>
<span class="w">      </span><span class="p">[](</span><span class="k">const</span><span class="w"> </span><span class="n">rocprofiler_record_header_t</span><span class="err">\</span><span class="o">*</span><span class="w"> </span><span class="n">record</span><span class="p">,</span><span class="w"> </span><span class="k">const</span>
<span class="w">      </span><span class="n">rocprofiler_record_header_t</span><span class="err">\</span><span class="o">*</span><span class="w"> </span><span class="n">end_record</span><span class="p">,</span>
<span class="w">      </span><span class="n">rocprofiler_session_id_t</span><span class="w"> </span><span class="n">session_id</span><span class="p">,</span><span class="w"> </span><span class="n">rocprofiler_buffer_id_t</span>
<span class="w">      </span><span class="n">buffer_id</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">         </span><span class="n">WriteBufferRecords</span><span class="p">(</span><span class="n">record</span><span class="p">,</span><span class="w"> </span><span class="n">end_record</span><span class="p">,</span><span class="w"> </span><span class="n">session_id</span><span class="p">,</span><span class="w"> </span><span class="n">buffer_id</span><span class="p">);</span>
<span class="w">      </span><span class="p">},</span>
<span class="w">      </span><span class="mh">0x9999</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">buffer_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Specifying the APIs to be traced in a vector</span>
<span class="w">   </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">rocprofiler_tracer_activity_domain_t</span><span class="o">&gt;</span><span class="w"> </span><span class="n">apis_requested</span><span class="p">;</span>
<span class="w">   </span><span class="n">apis_requested</span><span class="p">.</span><span class="n">emplace_back</span><span class="p">(</span><span class="n">ACTIVITY_DOMAIN_HIP_API</span><span class="p">);</span>
<span class="w">   </span><span class="n">apis_requested</span><span class="p">.</span><span class="n">emplace_back</span><span class="p">(</span><span class="n">ACTIVITY_DOMAIN_HIP_OPS</span><span class="p">);</span>
<span class="w">   </span><span class="n">apis_requested</span><span class="p">.</span><span class="n">emplace_back</span><span class="p">(</span><span class="n">ACTIVITY_DOMAIN_HSA_API</span><span class="p">);</span>
<span class="w">   </span><span class="n">apis_requested</span><span class="p">.</span><span class="n">emplace_back</span><span class="p">(</span><span class="n">ACTIVITY_DOMAIN_HSA_OPS</span><span class="p">);</span>
<span class="w">   </span><span class="n">apis_requested</span><span class="p">.</span><span class="n">emplace_back</span><span class="p">(</span><span class="n">ACTIVITY_DOMAIN_ROCTX</span><span class="p">);</span>
<span class="w">   </span><span class="n">rocprofiler_filter_id_t</span><span class="w"> </span><span class="n">api_tracing_filter_id</span><span class="p">;</span>

<span class="w">   </span><span class="c1">// Creating filter for tracing APIs</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_create_filter</span><span class="p">(</span>
<span class="w">      </span><span class="n">session_id</span><span class="p">,</span><span class="w"> </span><span class="n">ROCPROFILER_API_TRACE</span><span class="p">,</span>
<span class="w">      </span><span class="n">rocprofiler_filter_data_t</span><span class="p">{</span><span class="o">&amp;</span><span class="n">apis_requested</span><span class="p">[</span><span class="mi">0</span><span class="p">]},</span><span class="w"> </span><span class="n">apis_requested</span><span class="p">.</span><span class="n">size</span><span class="p">(),</span>
<span class="w">      </span><span class="o">&amp;</span><span class="n">api_tracing_filter_id</span><span class="p">,</span><span class="w"> </span><span class="n">rocprofiler_filter_property_t</span><span class="p">{}));</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_set_filter_buffer</span><span class="p">(</span><span class="n">session_id</span><span class="p">,</span>
<span class="w">      </span><span class="n">api_tracing_filter_id</span><span class="p">,</span><span class="w"> </span><span class="n">buffer_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Kernel Tracing</span>
<span class="w">   </span><span class="n">rocprofiler_filter_id_t</span><span class="w"> </span><span class="n">kernel_tracing_filter_id</span><span class="p">;</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_create_filter</span><span class="p">(</span><span class="n">session_id</span><span class="p">,</span>
<span class="w">      </span><span class="n">ROCPROFILER_DISPATCH_TIMESTAMPS_COLLECTION</span><span class="p">,</span><span class="w"> </span><span class="n">rocprofiler_filter_data_t</span><span class="p">{},</span>
<span class="w">      </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">kernel_tracing_filter_id</span><span class="p">,</span><span class="w"> </span><span class="n">rocprofiler_filter_property_t</span><span class="p">{}));</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_set_filter_buffer</span><span class="p">(</span><span class="n">session_id</span><span class="p">,</span>
<span class="w">      </span><span class="n">kernel_tracing_filter_id</span><span class="p">,</span><span class="w"> </span><span class="n">buffer_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Normal HIP Calls won&#39;t be traced</span>
<span class="w">   </span><span class="n">hipDeviceProp_t</span><span class="w"> </span><span class="n">devProp</span><span class="p">;</span>
<span class="w">   </span><span class="n">HIP_CALL</span><span class="p">(</span><span class="n">hipGetDeviceProperties</span><span class="p">(</span><span class="o">&amp;</span><span class="n">devProp</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="w">   </span><span class="n">HIP_CALL</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">((</span><span class="kt">void</span><span class="o">**</span><span class="p">)</span><span class="o">&amp;</span><span class="n">gpuMem</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="err">\</span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">)));</span>
<span class="w">   </span><span class="c1">// KernelA and KernelB won&#39;t be traced</span>
<span class="w">   </span><span class="n">kernelCalls</span><span class="p">(</span><span class="sc">&#39;A&#39;</span><span class="p">);</span>
<span class="w">   </span><span class="n">kernelCalls</span><span class="p">(</span><span class="sc">&#39;B&#39;</span><span class="p">);</span>

<span class="w">   </span><span class="c1">// Activating Profiling Session to profile whatever kernel launches occur</span>
<span class="w">   </span><span class="c1">// up to the next terminate session</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_start_session</span><span class="p">(</span><span class="n">session_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// KernelC, KernelD, KernelE and KernelF to be traced as part of the session</span>
<span class="w">   </span><span class="n">kernelCalls</span><span class="p">(</span><span class="sc">&#39;C&#39;</span><span class="p">);</span>
<span class="w">   </span><span class="n">kernelCalls</span><span class="p">(</span><span class="sc">&#39;D&#39;</span><span class="p">);</span>
<span class="w">   </span><span class="n">kernelCalls</span><span class="p">(</span><span class="sc">&#39;E&#39;</span><span class="p">);</span>
<span class="w">   </span><span class="n">kernelCalls</span><span class="p">(</span><span class="sc">&#39;F&#39;</span><span class="p">);</span>
<span class="w">   </span><span class="c1">// Normal HIP Calls that will be traced</span>
<span class="w">   </span><span class="n">HIP_CALL</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">gpuMem</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Deactivating session</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_terminate_session</span><span class="p">(</span><span class="n">session_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Manual Flush user buffer request</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_flush_data</span><span class="p">(</span><span class="n">session_id</span><span class="p">,</span><span class="w"> </span><span class="n">buffer_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Destroy sessions</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_destroy_session</span><span class="p">(</span><span class="n">session_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Destroy all profiling related objects (User buffer, sessions, filters, etc..)</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_finalize</span><span class="p">());</span>

<span class="w">   </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="kernel-profiling-1">
<span id="id5"></span><h2>Kernel profiling<a class="headerlink" href="#kernel-profiling-1" title="Link to this heading">#</a></h2>
<p>The following is a full-application example that utilizes the ROCProfilerV2
API to profile the kernels. The <code class="docutils literal notranslate"><span class="pre">ROCPROFILER_COUNTERS_COLLECTION</span></code> filter for
counter collection distinguishes this example from the one in <a class="reference internal" href="#application-tracing-1"><span class="std std-ref">Application tracing</span></a>.
The <code class="docutils literal notranslate"><span class="pre">GRBM_COUNT</span></code> counter to be collected is specified in a vector of strings as
shown.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;rocprofiler/v2/rocprofiler.h&gt;</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">argc</span><span class="p">,</span><span class="w"> </span><span class="kt">char</span><span class="o">*</span><span class="err">\</span><span class="o">*</span><span class="w"> </span><span class="n">argv</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="kt">int</span><span class="err">\</span><span class="o">*</span><span class="w"> </span><span class="n">gpuMem</span><span class="p">;</span>

<span class="w">   </span><span class="c1">// Initialize the tools</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_initialize</span><span class="p">());</span>

<span class="w">   </span><span class="c1">// Creating the session with given replay mode</span>
<span class="w">   </span><span class="n">rocprofiler_session_id_t</span><span class="w"> </span><span class="n">session_id</span><span class="p">;</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_create_session</span><span class="p">(</span><span class="n">ROCPROFILER_NONE_REPLAY_MODE</span><span class="p">,</span>
<span class="w">   </span><span class="o">&amp;</span><span class="n">session_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Creating Output Buffer for the data</span>
<span class="w">   </span><span class="n">rocprofiler_buffer_id_t</span><span class="w"> </span><span class="n">buffer_id</span><span class="p">;</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_create_buffer</span><span class="p">(</span><span class="n">session_id</span><span class="p">,</span>
<span class="w">      </span><span class="p">[](</span><span class="k">const</span><span class="w"> </span><span class="n">rocprofiler_record_header_t</span><span class="err">\</span><span class="o">*</span><span class="w"> </span><span class="n">record</span><span class="p">,</span><span class="w"> </span><span class="k">const</span>
<span class="w">      </span><span class="n">rocprofiler_record_header_t</span><span class="err">\</span><span class="o">*</span><span class="w"> </span><span class="n">end_record</span><span class="p">,</span>
<span class="w">      </span><span class="n">rocprofiler_session_id_t</span><span class="w"> </span><span class="n">session_id</span><span class="p">,</span><span class="w"> </span><span class="n">rocprofiler_buffer_id_t</span>
<span class="w">      </span><span class="n">buffer_id</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">         </span><span class="n">WriteBufferRecords</span><span class="p">(</span><span class="n">record</span><span class="p">,</span><span class="w"> </span><span class="n">end_record</span><span class="p">,</span><span class="w"> </span><span class="n">session_id</span><span class="p">,</span><span class="w"> </span><span class="n">buffer_id</span><span class="p">);</span>
<span class="w">      </span><span class="p">},</span>
<span class="w">      </span><span class="mh">0x9999</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">buffer_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Counter Collection Filter</span>
<span class="w">   </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">*&gt;</span><span class="w"> </span><span class="n">counters</span><span class="p">;</span>
<span class="w">   </span><span class="n">counters</span><span class="p">.</span><span class="n">emplace_back</span><span class="p">(</span><span class="s">&quot;GRBM_COUNT&quot;</span><span class="p">);</span>
<span class="w">   </span><span class="n">rocprofiler_filter_id_t</span><span class="w"> </span><span class="n">filter_id</span><span class="p">;</span>
<span class="w">   </span><span class="p">[[</span><span class="n">maybe_unused</span><span class="p">]]</span><span class="w"> </span><span class="n">rocprofiler_filter_property_t</span><span class="w"> </span><span class="n">property</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{};</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_create_filter</span><span class="p">(</span><span class="n">session_id</span><span class="p">,</span>
<span class="w">      </span><span class="n">ROCPROFILER_COUNTERS_COLLECTION</span><span class="p">,</span>
<span class="w">      </span><span class="n">rocprofiler_filter_data_t</span><span class="p">{.</span><span class="n">counters_names</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">&amp;</span><span class="n">counters</span><span class="p">[</span><span class="mi">0</span><span class="p">]},</span>
<span class="w">      </span><span class="n">counters</span><span class="p">.</span><span class="n">size</span><span class="p">(),</span><span class="w"> </span><span class="o">&amp;</span><span class="n">filter_id</span><span class="p">,</span><span class="w"> </span><span class="n">property</span><span class="p">));</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_set_filter_buffer</span><span class="p">(</span><span class="n">session_id</span><span class="p">,</span><span class="w"> </span><span class="n">filter_id</span><span class="p">,</span>
<span class="w">      </span><span class="n">buffer_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Normal HIP Calls</span>
<span class="w">   </span><span class="n">hipDeviceProp_t</span><span class="w"> </span><span class="n">devProp</span><span class="p">;</span>
<span class="w">   </span><span class="n">HIP_CALL</span><span class="p">(</span><span class="n">hipGetDeviceProperties</span><span class="p">(</span><span class="o">&amp;</span><span class="n">devProp</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="w">   </span><span class="n">HIP_CALL</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">((</span><span class="kt">void</span><span class="o">**</span><span class="p">)</span><span class="o">&amp;</span><span class="n">gpuMem</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="err">\</span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">)));</span>

<span class="w">   </span><span class="c1">// KernelA and KernelB won&#39;t be profiled</span>
<span class="w">   </span><span class="n">kernelCalls</span><span class="p">(</span><span class="sc">&#39;A&#39;</span><span class="p">);</span>
<span class="w">   </span><span class="n">kernelCalls</span><span class="p">(</span><span class="sc">&#39;B&#39;</span><span class="p">);</span>

<span class="w">   </span><span class="c1">// Activating Profiling Session to profile whatever kernel launches occur</span>
<span class="w">   </span><span class="c1">// up to the next terminate session</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_start_session</span><span class="p">(</span><span class="n">session_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// KernelC, KernelD, KernelE and KernelF to be profiled as part of the session</span>
<span class="w">   </span><span class="n">kernelCalls</span><span class="p">(</span><span class="sc">&#39;C&#39;</span><span class="p">);</span>
<span class="w">   </span><span class="n">kernelCalls</span><span class="p">(</span><span class="sc">&#39;D&#39;</span><span class="p">);</span>
<span class="w">   </span><span class="n">kernelCalls</span><span class="p">(</span><span class="sc">&#39;E&#39;</span><span class="p">);</span>
<span class="w">   </span><span class="n">kernelCalls</span><span class="p">(</span><span class="sc">&#39;F&#39;</span><span class="p">);</span>
<span class="w">   </span><span class="c1">// Normal HIP Calls</span>
<span class="w">   </span><span class="n">HIP_CALL</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">gpuMem</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Deactivating session</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_terminate_session</span><span class="p">(</span><span class="n">session_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Manual Flush user buffer request</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_flush_data</span><span class="p">(</span><span class="n">session_id</span><span class="p">,</span><span class="w"> </span><span class="n">buffer_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Destroy sessions</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_destroy_session</span><span class="p">(</span><span class="n">session_id</span><span class="p">));</span>

<span class="w">   </span><span class="c1">// Destroy all profiling related objects (User buffer, sessions, filters, etc..)</span>
<span class="w">   </span><span class="n">CHECK_ROCPROFILER</span><span class="p">(</span><span class="n">rocprofiler_finalize</span><span class="p">());</span>

<span class="w">   </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="environment-variables">
<h2>Environment variables<a class="headerlink" href="#environment-variables" title="Link to this heading">#</a></h2>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ROCPROFILER_LOG</span></code>: When set to 1, enables error messages logging to <code class="docutils literal notranslate"><span class="pre">/tmp/rocprofiler_log.txt</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCPROFILER_TRUNCATE_KERNEL_PATH</span></code>: When set to 1, enables truncation of kernel names for improved output readability. By default, the kernel names are not truncated.</p></li>
</ul>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../doxygen/html/globals_defs.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Globals</p>
      </div>
    </a>
    <a class="right-next"
       href="../license.html"
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
            
            
              
                <div class="bd-sidebar-secondary bd-toc"><div class="sidebar-secondary-items sidebar-secondary__inner">


  <div class="sidebar-secondary-item">
  <div class="page-toc tocsection onthispage">
    <i class="fa-solid fa-list"></i> Contents
  </div>
  <nav class="bd-toc-nav page-toc">
    <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#profiling-sessions">Profiling sessions</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#id2">Filters</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#application-tracing-1">Application tracing</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-profiling-1">Kernel profiling</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#environment-variables">Environment variables</a></li>
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
