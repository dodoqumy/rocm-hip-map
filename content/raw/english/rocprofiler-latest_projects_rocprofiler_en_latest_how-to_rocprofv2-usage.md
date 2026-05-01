---
title: "Using rocprofv2 &#8212; ROCProfiler 2.0.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler/en/latest/how-to/rocprofv2-usage.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:29:08.200064+00:00
content_hash: "676716fc9f550a7f"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="ROCProfiler is a powerful tool for profiling HIP and ROCm applications on AMD ROCm software" name="description" />
<meta content="ROCProfilerV2 tool usage, ROCProfilerV2 command line, rocprofv2 usage, rocprofv2 user manual, rocprofv2 guide" name="keywords" />

    <title>Using rocprofv2 &#8212; ROCProfiler 2.0.0 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/rocprofv2-usage';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="rocprofv2 command help" href="rocprofv2-command.html" />
    <link rel="prev" title="rocprof command help" href="rocprof-command.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-docs" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/rocprofv2-usage.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1"><a class="reference internal" href="using-rocprof.html">Using rocprof</a></li>
<li class="toctree-l1"><a class="reference internal" href="rocprof-command.html">rocprof command help</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Using rocprofv2</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">Using rocprofv2</li>
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
    <h1>Using rocprofv2</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#application-tracing">Application tracing</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#visualize-tracing-results">Visualize tracing results</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-profiling">Kernel profiling</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#input-file">Input file</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#counter-collection-without-kernel-serialization">Counter collection without kernel serialization</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-profiling-output">Kernel profiling output</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#formatting-output-using-plugins">Formatting output using plugins</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#file-plugin">File plugin</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#perfetto-plugin">Perfetto plugin</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#common-trace-format-plugin">Common Trace Format plugin</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#json-plugin">JSON plugin</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#configuration-options">Configuration options</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#flush-interval">Flush interval</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#trace-period">Trace period</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#limitations">Limitations</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="using-rocprofv2">
<span id="rocprofv2-usage"></span><h1>Using rocprofv2<a class="headerlink" href="#using-rocprofv2" title="Link to this heading">#</a></h1>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> is considered beta software.</p>
</div>
<p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> is a command-line interface tool (CLI) that lets you profile <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/index.html" title="(in HIP Documentation v7.2.53211)"><span class="xref std std-doc">HIP</span></a> applications on AMD ROCm platform without requiring source code modification. The usage of <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> along with
various command-line arguments is described in the following sections.</p>
<p>To see all the <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> options, refer to <a class="reference internal" href="rocprofv2-command.html#v2-command"><span class="std std-ref">rocprofv2 command help</span></a>, or run the following from the command line:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>--help
</pre></div>
</div>
<section id="application-tracing">
<h2>Application tracing<a class="headerlink" href="#application-tracing" title="Link to this heading">#</a></h2>
<p>Tracing of application and hardware events is a primary feature of the <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> command.
The command-line options for application tracing are listed in the table below:</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 30.0%" />
<col style="width: 20.0%" />
<col style="width: 50.0%" />
</colgroup>
<tbody>
<tr class="row-odd"><td><p><strong>Option</strong></p></td>
<td><p><strong>Description</strong></p></td>
<td><p><strong>Usage</strong></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">--hip-api</span></code></p></td>
<td><p>HIP API tracing</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--hip-api</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">--hip-activity</span></code> <br /> or <code class="docutils literal notranslate"><span class="pre">--hip-trace</span></code></p></td>
<td><p>Combined HIP API and asynchronous activity tracing</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--hip-activity</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">--hsa-api</span></code></p></td>
<td><p>HSA API tracing</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--hsa-api</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">--hip-activity</span></code> <br /> or <code class="docutils literal notranslate"><span class="pre">--hsa-trace</span></code></p></td>
<td><p>Combined HSA API and asynchronous activity tracing</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--hsa-api</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">--roctx-trace</span></code></p></td>
<td><p>ROCTx API tracing</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--roctx-trace</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">--kernel-trace</span></code></p></td>
<td><p>Kernel dispatches tracing</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--kernel-trace</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">--sys-trace</span></code></p></td>
<td><p>HIP, HSA, and ROCTx traces combined</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--sys-trace</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">--basenames</span></code></p></td>
<td><p>Truncates the kernel names in the trace files to the base name of the function</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--basename</span> <span class="pre">on</span> <span class="pre">--hip-trace</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">-o</span> <span class="pre">|</span> <span class="pre">--output-file-name</span></code></p></td>
<td><p>Specifies the output file name</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--hip-trace</span> <span class="pre">-o</span> <span class="pre">&lt;file_name&gt;</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">-d</span> <span class="pre">|</span> <span class="pre">--output-directory</span></code></p></td>
<td><p>Specifies the path for output files</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--hip-trace</span> <span class="pre">-d</span> <span class="pre">&lt;output_dir&gt;</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
</tbody>
</table>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>By default, the output of these options is directed to <code class="docutils literal notranslate"><span class="pre">stdout</span></code> unless
the <code class="docutils literal notranslate"><span class="pre">-o</span></code> option is also specified.</p>
</div>
<p>To generate output from these trace options, use one of the supported plugins that
generate output in a specific format, as explained in <a class="reference internal" href="#using-plugins"><span class="std std-ref">Formatting output using plugins</span></a>. The default
plugin is the <code class="docutils literal notranslate"><span class="pre">file</span></code> plugin that generates a CSV file returned to <code class="docutils literal notranslate"><span class="pre">stdout</span></code>, or
returned to a file when used with <code class="docutils literal notranslate"><span class="pre">-o</span></code> option.</p>
<p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> supports API tracing at both HIP and HSA level. In general, HIP APIs
directly interact with the user program. It is easier to analyze HIP traces as you
can directly map the traces to the program. HSA API tracing is more suited for
advanced users who want to understand the application behavior at the lower level.</p>
<p>Both HIP and HSA APIs support asynchronous behavior (e.g., asynchronous
memory copy). If trace collection is triggered using either <code class="docutils literal notranslate"><span class="pre">--hip-api</span></code>
or <code class="docutils literal notranslate"><span class="pre">--hsa-api</span></code>, the trace records only the start, stop, and duration of
API events, but not the execution time of associated actions like memory copy.
To record the duration of asynchronous activities, use <code class="docutils literal notranslate"><span class="pre">--hip-activity</span></code> and
<code class="docutils literal notranslate"><span class="pre">--hsa-activity</span></code> options, which record both the API events and asynchronous
events.</p>
<section id="visualize-tracing-results">
<h3>Visualize tracing results<a class="headerlink" href="#visualize-tracing-results" title="Link to this heading">#</a></h3>
<p>You can view the traces generated by <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> using the Perfetto UI that
enables you to view and analyze traces in a web browser. To begin go to
<a class="reference external" href="https://ui.perfetto.dev">Perfetto UI</a>, select <em>Open trace file</em>
from the left-side menu, and select the ROCProfiler trace file to view.</p>
<p>The following is a screenshot from the Perfetto interface. The tasks are
organized in a Gantt chart style with the x-axis representing time and
each rectangle representing the start and the end time of a task. The
tasks are organized in rows. In the figure is the HIP API, HSA API, a queue,
and a stream.</p>
<figure class="align-default" id="id4">
<img alt="Viewing HIP Trace" src="../_images/view-trace-1.png" />
<figcaption>
<p><span class="caption-text">Visualizing Traces Generated Using sys-trace</span><a class="headerlink" href="#id4" title="Link to this image">#</a></p>
</figcaption>
</figure>
<div class="admonition tip">
<p class="admonition-title">Tip</p>
<p>To enlarge the image, right click on the image and use the <em>Open image in new tab</em>
option.</p>
</div>
</section>
</section>
<section id="kernel-profiling">
<h2>Kernel profiling<a class="headerlink" href="#kernel-profiling" title="Link to this heading">#</a></h2>
<p>As explained in <span class="xref std std-ref">rocprof-counters</span> application tracing lets you evaluate
the timeline of application events, but is little help in providing insight into
kernel execution details. The kernel profiling functionality lets you select
kernels for profiling and choose the basic counters or derived metrics to be
collected for each kernel execution, thus providing a greater insight into hardware
performance.</p>
<p>The command-line options for kernel profiling are listed in the table below:</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 30.0%" />
<col style="width: 20.0%" />
<col style="width: 50.0%" />
</colgroup>
<tbody>
<tr class="row-odd"><td><p><strong>Option</strong></p></td>
<td><p><strong>Description</strong></p></td>
<td><p><strong>Usage</strong></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">list-counters</span></code></p></td>
<td><p>Displays all available counters for the current GPUs.</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--list-counters</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">-m</span></code></p></td>
<td><p>Provides the absolute path for custom metrics file.</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">-m</span> <span class="pre">custom_metrics.xml</span> <span class="pre">--list-counters</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">--plugin</span>&#160; <span class="pre">&lt;plugin_name&gt;</span></code></p></td>
<td><p>Enables plugin for generating output in a specific format where &lt;plugin_name&gt; = [file/perfetto/ctf/json].</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--plugin</span> <span class="pre">&lt;plugin_name&gt;</span> <span class="pre">-i</span> <span class="pre">input.txt</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">--plugin-version</span></code></p></td>
<td><p>Specifies the plugin version where a value of <code class="docutils literal notranslate"><span class="pre">1</span></code> = legacy output format and <code class="docutils literal notranslate"><span class="pre">2</span></code> = New output format. The default value is <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--plugin</span> <span class="pre">&lt;plugin_name&gt;</span> <span class="pre">--plugin-version</span> <span class="pre">&lt;plugin_version_value&gt;</span> <span class="pre">&lt;rocprofv2_options&gt;</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">-i</span> <span class="pre">|</span> <span class="pre">--input</span></code></p></td>
<td><p>Specifies the path to the input file consisting of the counters for collection.</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">-i</span> <span class="pre">input.txt</span> <span class="pre">-d</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">-o</span> <span class="pre">|</span> <span class="pre">--output-file-name</span></code></p></td>
<td><p>Specifies the output file name</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">-i</span> <span class="pre">input.txt</span> <span class="pre">--plugin</span> <span class="pre">file</span> <span class="pre">-o</span> <span class="pre">result</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">-d</span> <span class="pre">|</span> <span class="pre">--output-directory</span></code></p></td>
<td><p>Specifies the path for output files</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">--plugin</span> <span class="pre">file</span> <span class="pre">-i</span> <span class="pre">input.txt</span> <span class="pre">-d</span> <span class="pre">output_dir</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">-n</span> <span class="pre">|</span> <span class="pre">--no-serialization</span></code></p></td>
<td><p>Disables kernel serialization. <a class="reference internal" href="#kernel-serialization"><span class="std std-ref">Read more..</span></a>.</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span> <span class="pre">-ns</span> <span class="pre">-i</span> <span class="pre">input.txt</span> <span class="pre">&lt;app_relative_path&gt;</span></code></p></td>
</tr>
</tbody>
</table>
</div>
<p>To check the supported performance counters and metrics, use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>--list-counters
</pre></div>
</div>
<p>The following is a sample output from the <code class="docutils literal notranslate"><span class="pre">--list-counters</span></code> option. The output has
been truncated for explanation:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>gfx1030:0<span class="w"> </span>:<span class="w"> </span>SQ_WAVES
:<span class="w"> </span>Count<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>waves<span class="w"> </span>sent<span class="w"> </span>to<span class="w"> </span>SQs.<span class="w"> </span><span class="o">{</span>emulated,<span class="w"> </span>global,<span class="w"> </span>C1<span class="o">}</span>
block<span class="w"> </span>SQ<span class="w"> </span>can<span class="w"> </span>only<span class="w"> </span>handle<span class="w"> </span><span class="m">8</span><span class="w"> </span>counters<span class="w"> </span>at<span class="w"> </span>a<span class="w"> </span><span class="nb">time</span>
</pre></div>
</div>
<p>The fields in the output are:</p>
<ul class="simple">
<li><p><strong>gfx1030:0</strong> - The GPU architecture and GPU ID (separated by colon).
The GPU ID needs to be specified as there might be multiple GPUs in
the system.</p></li>
<li><p><strong>SQ_WAVES</strong> - The counter name. Typically, the first token before
the first underscore is the GPU block name. Here, SQ is the block
that is responsible for managing wavefronts and issuing instructions.</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>For more information on the performance counters available on AMD GPUs, refer
to the <a class="reference external" href="https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch.html#gpu-arch-documentation">GPU architecture documentation</a>.</p>
</div>
<section id="input-file">
<h3>Input file<a class="headerlink" href="#input-file" title="Link to this heading">#</a></h3>
<p>To collect basic counters and derived metrics, define the profiling
scope in an input file, and specify the file on the command line:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>-i<span class="w"> </span>input.txt<span class="w"> </span>&lt;app_relative_path&gt;
</pre></div>
</div>
<p>An input file is a text file that can be supplied to <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> for basic
counter and derived metric collection. It contains the list of basic counters or derived metrics to be collected.</p>
<p>Sample Input File:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>pmc:<span class="w"> </span>SQ_WAVES<span class="w"> </span>TA_UTIL
</pre></div>
</div>
<p>The fields in the input file are detailed in <a class="reference internal" href="using-rocprof.html#input-file"><span class="std std-ref">Input file</span></a>.</p>
<p><strong>PMC:</strong> The rows in the text file beginning with <code class="docutils literal notranslate"><span class="pre">pmc:</span></code> are the group of
basic counters or derived metrics the user is interested in collecting.
The basic counters or derived metrics can be selected from the output
generated by <code class="docutils literal notranslate"><span class="pre">--list-counters</span></code> option.</p>
<p>The number of basic counters or derived metrics that can be collected in
one run of profiling is limited by the GPU hardware resources. If too
many counters/metrics are selected, the kernels need to be executed
multiple times to collect the counters/metrics. For multi-pass
execution, include multiple rows of <code class="docutils literal notranslate"><span class="pre">pmc:</span></code> in the input file. Counters or
metrics in each <code class="docutils literal notranslate"><span class="pre">pmc:</span></code> row can be collected in each run of the kernel.</p>
<p><strong>GPU:</strong> The row beginning with the keyword <code class="docutils literal notranslate"><span class="pre">gpu:</span></code> specifies the GPU(s) on
which the hardware counters are to be collected. This enables the
support for profiling multiple GPUs. You can specify multiple GPUs
separated by comma such as <code class="docutils literal notranslate"><span class="pre">gpu:</span> <span class="pre">1,3</span></code>.</p>
<p><strong>Kernel:</strong> The row beginning with the <code class="docutils literal notranslate"><span class="pre">kernel:</span></code> keyword specifies the
names of kernels to be profiled. This kernel filtration can also be enabled using flag <code class="docutils literal notranslate"><span class="pre">ROCPROFILER_KERNEL_FILTER</span></code>.</p>
<p><strong>Range:</strong> The row beginning with the keyword <code class="docutils literal notranslate"><span class="pre">range:</span></code> specifies the range
of kernel dispatches. Specifying range is helpful in cases where the
application causes multiple kernel dispatches and users want to filter
some kernel dispatches. In the above example, the <code class="docutils literal notranslate"><span class="pre">range:</span> <span class="pre">0:1</span></code> depicts that
one kernel is profiled.</p>
</section>
<section id="counter-collection-without-kernel-serialization">
<span id="kernel-serialization"></span><h3>Counter collection without kernel serialization<a class="headerlink" href="#counter-collection-without-kernel-serialization" title="Link to this heading">#</a></h3>
<p>By default, <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> performs counter collection with kernel serialization enabled. With serialization enabled, there is a possibility of deadlock occurring, if the program being profiled attempts to launch two kernels relying on each other to progress. For example, kernel A waits in a while-loop until kernel B modifies a location in memory, but kernel serialization prevents launching kernel B until kernel A finishes execution. To avoid this deadlock issue, disable kernel serialization using:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>-ns<span class="w"> </span>-i<span class="w"> </span>input.txt<span class="w"> </span>&lt;app_relative_path&gt;

<span class="c1"># OR</span>

rocprofv2<span class="w"> </span>--no-serialization<span class="w"> </span>-i<span class="w"> </span>input.txt<span class="w"> </span>&lt;app_relative_path&gt;
</pre></div>
</div>
<p>Alternatively, set the following environment variable:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nb">export</span><span class="w"> </span><span class="nv">ROCPROFILER_NO_SERIALIZATION</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">1</span>
</pre></div>
</div>
</section>
<section id="kernel-profiling-output">
<h3>Kernel profiling output<a class="headerlink" href="#kernel-profiling-output" title="Link to this heading">#</a></h3>
<p>This section discusses the kernel profiling output generated using the
<a class="reference external" href="#input-file">Input File</a>. <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> reports one value per metric per
kernel in the output. You can generate the output in desired format
as described in <a class="reference internal" href="#using-plugins"><span class="std std-ref">Formatting output using plugins</span></a>. If no plugin is
specified while generating the output, the result is dumped on the
command-line.</p>
<p>The following sample output is generated using the <code class="docutils literal notranslate"><span class="pre">file</span></code> plugin. Each
row of the file is an instance of kernel execution.</p>
<p>For each kernel, basic information (e.g., <code class="docutils literal notranslate"><span class="pre">GPU_ID</span></code>, <code class="docutils literal notranslate"><span class="pre">SGPR</span></code>, <code class="docutils literal notranslate"><span class="pre">PID</span></code>, etc.) and
performance counters (specified in the input file) values are listed.
The information is generated in the format of field name and value.</p>
<p>Note that the use of <a class="reference external" href="https://github.com/ROCm/hip-tests/blob/develop/samples/2_Cookbook/0_MatrixTranspose">MatrixTranspose</a> application is for demonstration purposes only.</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>rocprofv2<span class="w"> </span>-i<span class="w"> </span>input.txt<span class="w"> </span>--plugin<span class="w"> </span>file<span class="w"> </span>-o<span class="w"> </span>result<span class="w"> </span>MatrixTranspose

$<span class="w"> </span>cat<span class="w"> </span>results_result.csv

Dispatch_ID,GPU_ID,Queue_ID,Queue_Index,PID,TID,GRD,WGR,LDS,SCR,Arch_VGPR,ACCUM_VGPR,
SGPR,Wave_Size,SIG,OBJ,Kernel_Name,Start_Timestamp,End_Timestamp,Correlation_ID,
SQ_WAVES,GRBM_COUNT,GRBM_GUI_ACTIVE,SQ_INSTS_VALU,FETCH_SIZE

<span class="m">1</span>,64700,1,0,353,353,1048576,16,0,0,8,0,16,64,140356026185088,1,<span class="s2">&quot;matrixTranspose(float*, float*, int)</span>
<span class="s2">(.kd)&quot;</span>,7,30064771072,0,65536.000000,398333.000000,398333.000000,917504.000000,4136.000000

<span class="m">2</span>,64700,1,2,353,353,1048576,16,0,0,8,0,16,64,140356026184832,2,<span class="s2">&quot;matrixTranspose(float*,</span>
<span class="s2">float*, int)</span>
<span class="s2">(.kd)&quot;</span>,7,30064771072,0,65536.000000,586424.000000,586424.000000,917504.000000,4130.437500

<span class="m">3</span>,64700,1,4,353,353,1048576,16,0,0,8,0,16,64,140356026184576,3,<span class="s2">&quot;matrixTranspose(float*,</span>
<span class="s2">float*, int)</span>
<span class="s2">(.kd)&quot;</span>,7,30064771072,0,65536.000000,392460.000000,392460.000000,917504.000000,4129.937500
</pre></div>
</div>
<p>The fields in the output file are:</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Output fields</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">Dispatch_ID</span></code></p></td>
<td><p>Kernel’s dispatch Id</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">GPU_ID</span></code></p></td>
<td><p>GPU identifier to which the kernel was submitted</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">Queue_ID</span></code></p></td>
<td><p><em>ROCm</em> queue unique identifier to which the
kernel was submitted</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">Queue_Index</span></code></p></td>
<td><p><em>ROCm</em> queue write index for the submitted AQL
packet</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">PID</span></code></p></td>
<td><p>System application process id that submitted the
kernel</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">TID</span></code></p></td>
<td><p>System application thread id that submitted the
kernel</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">GRD</span></code></p></td>
<td><p>Kernel’s grid size</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">WGR</span></code></p></td>
<td><p>Kernel’s work group size</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">LDS</span></code></p></td>
<td><p>Kernel’s Local Data Share (LDS) memory size</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">SCR</span></code></p></td>
<td><p>Kernel’s scratch memory size</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">Arch_VGPR</span></code></p></td>
<td><p>Number of Vector General Purpose Registers (VGPR)
used in kernel dispatch</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ACCUM_VGPR</span></code></p></td>
<td><p>Total Count of VGPRs</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">SGPR</span></code></p></td>
<td><p>Kernel’s Scalar General-Purpose Register (SGPR)
size</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">Wave_Size</span></code></p></td>
<td><p>Number of wavefronts</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">SIG</span></code></p></td>
<td><p>Kernel’s completion signal</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">OBJ</span></code></p></td>
<td><p>Code object</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">Kernel_Name</span></code></p></td>
<td><p>Name of the dispatched kernel</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">Start_Timestamp</span></code></p></td>
<td><p>Begin time in nanoseconds (ns) when the kernel
begins execution</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">End_Timestamp</span></code></p></td>
<td><p>End time in ns when the kernel finishes execution</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">Correlation_ID</span></code></p></td>
<td><p>Unique identifier for correlation between HIP and
HSA async calls during activity tracing</p></td>
</tr>
</tbody>
</table>
</div>
<p>You can view the generated output using the <em>Perfetto UI</em> as previously described
in <a class="reference external" href="#visualize-tracing-results">Visualize Tracing Results</a>. The following is
a screenshot of the Perfetto UI when viewing the kernel profiling
output.</p>
<figure class="align-default" id="id5">
<img alt="Viewing Kernel Profile" src="../_images/view-trace-2.png" />
<figcaption>
<p><span class="caption-text">Viewing kernel profiling output</span><a class="headerlink" href="#id5" title="Link to this image">#</a></p>
</figcaption>
</figure>
<p>The first four rows represent the performance counters as
specified in the input file. The last row is the kernel execution
timeline, which is the same as the <code class="docutils literal notranslate"><span class="pre">--kernel-trace</span></code> option used in the
<a class="reference external" href="#application-tracing">Application tracing</a> mode.</p>
<p>Viewing the profile results provides a good overview of kernel execution times and how
performance metrics values change across the kernels. Additionally, you can also
see the exact value of a counter/metric by hovering over or clicking the bar.</p>
</section>
</section>
<section id="formatting-output-using-plugins">
<span id="using-plugins"></span><h2>Formatting output using plugins<a class="headerlink" href="#formatting-output-using-plugins" title="Link to this heading">#</a></h2>
<p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> uses a modular plugin system which allows you to generate
profiling output in the desired format. Because these plugins are modular in
nature, they can easily be decoupled from the code based on need. By
default, <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> generates the profiling output using the <code class="docutils literal notranslate"><span class="pre">file</span></code> and CLI
plugins.</p>
<p>You can install other plugins (as listed in the table below) using the
plugins package as shown:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprofiler-plugins_2.0.0-local_amd64.deb
-or-
rocprofiler-plugins-2.0.0-local.x86_64.rpm
</pre></div>
</div>
<p>You can also create your own plugins if you are using <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> with source code and not just as a CLI tool. To write new plugins import the <code class="docutils literal notranslate"><span class="pre">include/rocprofiler/v2/rocprofiler_plugins.h</span></code> header file.</p>
<p>To generate the profiling output using a plugin, use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>--plugin<span class="w"> </span>plugin_name<span class="w"> </span>-i<span class="w"> </span>input.txt<span class="w"> </span>&lt;app_relative_path&gt;

<span class="c1"># where plugin_name is file, perfetto, or ctf</span>
</pre></div>
</div>
<p>To specify the plugin version to be used in case of multiple versions, use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>--plugin<span class="w"> </span>&lt;plugin_name&gt;<span class="w"> </span>--plugin-version<span class="w"> </span>&lt;plugin_version_required&gt;<span class="w"> </span>&lt;rocprofv2_options&gt;<span class="w"> </span>&lt;app_relative_path&gt;
</pre></div>
</div>
<p>The following table lists the available plugins:</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Plugin</p></th>
<th class="head"><p>Output format</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>File</p></td>
<td><p>Text files (.csv or .txt)</p></td>
</tr>
<tr class="row-odd"><td><p>Perfetto</p></td>
<td><p>Protobuf in the format of the Chromium
Project’s <a class="reference external" href="https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/edit">trace-event
format</a></p></td>
</tr>
<tr class="row-even"><td><p>Common Trace Format
(CTF)</p></td>
<td><p>Binary, formatted in the ctf format that
can be consumed by public tools such as
<a class="reference external" href="https://babeltrace.org/">Babeltrace</a>
and
<a class="reference external" href="https://projects.eclipse.org/projects/tools.tracecompass">TraceCompass</a></p></td>
</tr>
<tr class="row-odd"><td><p>JSON</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">.json</span></code> file</p></td>
</tr>
</tbody>
</table>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>To generate output, the plugins require you to set the <em>OUTPUT_PATH</em>
variable to the desired directory. File plugin is the only plugin that
still generates output in the absence of <em>OUTPUT_PATH</em> by dumping the
output to standard output.</p>
</div>
<section id="file-plugin">
<h3>File plugin<a class="headerlink" href="#file-plugin" title="Link to this heading">#</a></h3>
<p>To output the data in <code class="docutils literal notranslate"><span class="pre">.txt</span></code> files using file plugin, use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>--plugin<span class="w"> </span>file<span class="w"> </span>-i<span class="w"> </span>samples/input.txt<span class="w"> </span>-d<span class="w"> </span>output_dir<span class="w"> </span>&lt;app_relative_path&gt;
</pre></div>
</div>
<p>Note that specifying the directory for output files using <code class="docutils literal notranslate"><span class="pre">-d</span></code> is optional.</p>
<p>File plugin has two versions with version 2 being the default. The headers in the output files generated using file plugin version 1 and 2 differ as shown below.</p>
<p>Version 1 header:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>Index,KernelName,gpu-id,queue-id,queue-index,pid,tid,grd,wgr,lds,scr,arch_vgpr,accum_vgpr,sgpr,wave_size,sig,obj,DispatchNs,BeginNs,EndNs,CompleteNs,Counters
</pre></div>
</div>
<p>Note that the version 1 header is same as the legacy <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> output.</p>
<p>Version 2 header:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>Dispatch_ID,GPU_ID,Queue_ID,PID,TID,Grid_Size,Workgroup_Size,LDS_Per_Workgroup,Scratch_Per_Workitem,Arch_VGPR,Accum_VGPR,SGPR,Wave_Size,Kernel_Name,Start_Timestamp,End_Timestamp,Correlation_ID,Counters
</pre></div>
</div>
</section>
<section id="perfetto-plugin">
<h3>Perfetto plugin<a class="headerlink" href="#perfetto-plugin" title="Link to this heading">#</a></h3>
<p>To output the data in <cite>Protobuf</cite> format using the Perfetto plugin, use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>--plugin<span class="w"> </span>perfetto<span class="w"> </span>--hsa-trace<span class="w"> </span>&lt;app_relative_path&gt;
</pre></div>
</div>
<p>You can view the <cite>Protobuf</cite> files using <a class="reference external" href="https://ui.perfetto.dev/">Perfetto</a> or <a class="reference external" href="https://perfetto.dev/docs/analysis/trace-processor">Trace processor</a>.</p>
</section>
<section id="common-trace-format-plugin">
<h3>Common Trace Format plugin<a class="headerlink" href="#common-trace-format-plugin" title="Link to this heading">#</a></h3>
<p>To output the data in Common Trace Format (CTF), which is a binary trace format, use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>--plugin<span class="w"> </span>ctf<span class="w"> </span>--hip-trace<span class="w"> </span>&lt;app_relative_path&gt;
</pre></div>
</div>
<p>You can view the CTF binary output using <a class="reference external" href="https://eclipse.dev/tracecompass/">TraceCompass</a> or <a class="reference external" href="https://babeltrace.org/">Babeltrace</a>.</p>
</section>
<section id="json-plugin">
<h3>JSON plugin<a class="headerlink" href="#json-plugin" title="Link to this heading">#</a></h3>
<p>The JSON file matches Google Trace Format, making it easy to load on Perfetto, Chrome tracing or Speedscope. When loading on Speedscope, use <code class="docutils literal notranslate"><span class="pre">--disable-json-data-flows</span></code> option as Speedscope doesn’t work with data flows.</p>
<p>To output the data in <code class="docutils literal notranslate"><span class="pre">.json</span></code> format using the JSON plugin, use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>--plugin<span class="w"> </span>json<span class="w"> </span>--hip-trace<span class="w"> </span>-d<span class="w"> </span>output_dir<span class="w"> </span>&lt;app_relative_path&gt;
</pre></div>
</div>
</section>
</section>
<section id="configuration-options">
<h2>Configuration options<a class="headerlink" href="#configuration-options" title="Link to this heading">#</a></h2>
<p><code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> provides options to control the rate at which the buffers are flushed and the rate at which profiling or tracing is performed.</p>
<section id="flush-interval">
<h3>Flush interval<a class="headerlink" href="#flush-interval" title="Link to this heading">#</a></h3>
<p>Flush interval controls the time interval in milliseconds (ms) between the flushing of the tool’s buffers. However, flushing occurs irrespective of the flush interval settings if the buffers are full.</p>
<p>To set the flush interval, use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>--flush-interval<span class="w"> </span>&lt;TIME_INTERVAL_IN_MILLISECONDS&gt;<span class="w"> </span>&lt;rest_of_rocprofv2_arguments&gt;<span class="w"> </span>&lt;app_relative_path&gt;
</pre></div>
</div>
</section>
<section id="trace-period">
<h3>Trace period<a class="headerlink" href="#trace-period" title="Link to this heading">#</a></h3>
<p>Trace period controls the rate at which profiling or tracing is performed. It is set using the following three arguments:</p>
<ul class="simple">
<li><p>delay: Time in ms spent idle without tracing or profiling</p></li>
<li><p>active_time: Profiling or tracing duration in ms</p></li>
<li><p>interval: If set, profiling or tracing sessions loop every <em>interval</em> and run for the given <em>active_time</em>, until the application ends. The <em>interval</em> value must be higher than the specified <em>active_time</em>.</p></li>
</ul>
<p>To set the trace period, use:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>--trace-period<span class="w"> </span>&lt;delay&gt;:&lt;active_time&gt;:&lt;interval&gt;<span class="w"> </span>&lt;rest_of_rocprofv2_arguments&gt;<span class="w"> </span>&lt;app_relative_path&gt;
</pre></div>
</div>
</section>
<section id="limitations">
<h3>Limitations<a class="headerlink" href="#limitations" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p>For counter collection on Navi3x, a stable power state is required. To achieve this, set <code class="docutils literal notranslate"><span class="pre">power_dpm_force_performance_level</span></code> to be writeable for non-root users, then set performance level to <code class="docutils literal notranslate"><span class="pre">profile_standard</span></code>:</p></li>
</ul>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>chmod<span class="w"> </span><span class="m">777</span><span class="w"> </span>/sys/class/drm/card0/device/power_dpm_force_performance_level
<span class="nb">echo</span><span class="w"> </span>profile_standard<span class="w"> </span>&gt;&gt;<span class="w"> </span>/sys/class/drm/card0/device/power_dpm_force_performance_level
</pre></div>
</div>
<p>Use <code class="docutils literal notranslate"><span class="pre">profile_standard</span></code> for counter collection and <code class="docutils literal notranslate"><span class="pre">auto</span></code> for other profiling. Use <code class="docutils literal notranslate"><span class="pre">rocm-smi</span></code> to verify the current power state. For multiGPU systems including integrated graphics, replace <code class="docutils literal notranslate"><span class="pre">card0</span></code> with the desired card.</p>
<ul class="simple">
<li><p>When the system has been in the sleep state, the generated timestamps might be incorrect with <code class="docutils literal notranslate"><span class="pre">HIP_OPS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIP_OPS</span></code> are mutually exclusive with <code class="docutils literal notranslate"><span class="pre">HSA_OPS</span></code>.</p></li>
<li><p>JSON plugin is not equipped to automatically merge for multiple processes. A file is generated per process (rank).</p></li>
</ul>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="rocprof-command.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">rocprof command help</p>
      </div>
    </a>
    <a class="right-next"
       href="rocprofv2-command.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">rocprofv2 command help</p>
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
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#visualize-tracing-results">Visualize tracing results</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-profiling">Kernel profiling</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#input-file">Input file</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#counter-collection-without-kernel-serialization">Counter collection without kernel serialization</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-profiling-output">Kernel profiling output</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#formatting-output-using-plugins">Formatting output using plugins</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#file-plugin">File plugin</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#perfetto-plugin">Perfetto plugin</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#common-trace-format-plugin">Common Trace Format plugin</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#json-plugin">JSON plugin</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#configuration-options">Configuration options</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#flush-interval">Flush interval</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#trace-period">Trace period</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#limitations">Limitations</a></li>
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
