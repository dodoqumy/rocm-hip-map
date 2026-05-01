---
title: "Installing ROCProfiler &#8212; ROCProfiler 2.0.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler/en/latest/install/installv1.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:29:06.045356+00:00
content_hash: "c4dd9295afad1ffa"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Installation of ROCProfiler, a powerful tool for profiling HIP and ROCm applications on AMD ROCm software" name="description" />
<meta content="ROCProfiler installation, Install ROCProfiler, Build ROCProfiler, Building ROCProfiler" name="keywords" />

    <title>Installing ROCProfiler &#8212; ROCProfiler 2.0.0 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'install/installv1';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Installing ROCProfilerV2" href="installv2.html" />
    <link rel="prev" title="ROCProfiler documentation" href="../index.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-docs" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/install/installv1.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Installing ROCProfiler</a></li>
<li class="toctree-l1"><a class="reference internal" href="installv2.html">Installing ROCProfilerV2</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">Installing...</li>
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
    <h1>Installing ROCProfiler</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#installing-from-source-files">Installing from source files</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#prerequisites">Prerequisites</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#building-from-source">Building from source</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="installing-rocprofiler">
<span id="rocprof-install"></span><h1>Installing ROCProfiler<a class="headerlink" href="#installing-rocprofiler" title="Link to this heading">#</a></h1>
<p>As ROCProfiler library and <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> are included as standard components of the ROCm distribution, the easiest installation method is to perform a complete ROCm installation as described in <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/index.html" title="(in ROCm installation on Linux v7.2.2)"><span class="xref std std-doc">Installation Guide</span></a>. This approach is straightforward and dependable, making it suitable for most users.</p>
<p>Alternatively, installing ROCProfiler from the source files offers some advantages. Due to the additional complexity involved, this option is only recommended for experienced users when necessary.</p>
<section id="installing-from-source-files">
<h2>Installing from source files<a class="headerlink" href="#installing-from-source-files" title="Link to this heading">#</a></h2>
<p>The following section discusses how to install and build from the source files.</p>
<section id="prerequisites">
<h3>Prerequisites<a class="headerlink" href="#prerequisites" title="Link to this heading">#</a></h3>
<p>Installing ROCProfiler from the source requires:</p>
<ul class="simple">
<li><p>AMD GPU driver for <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html" title="(in ROCm installation on Linux v7.2.2)"><span class="xref std std-doc">supported GPUs</span></a></p></li>
<li><p>Linux system supported by ROCm as described in <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html" title="(in ROCm installation on Linux v7.2.2)"><span class="xref std std-doc">System requirements</span></a></p></li>
<li><p>ROCm installed in the system</p></li>
<li><p>Packages necessary for ROCProfiler on supported Linux distributions as described in the following:</p></li>
</ul>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
</input><label class="sd-tab-label" data-sync-id="ubuntu" for="sd-tab-item-0">
Ubuntu</label><div class="sd-tab-content docutils">
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>apt<span class="w"> </span>install<span class="w"> </span>libudev-dev<span class="w"> </span>libnuma1<span class="w"> </span>libnuma-dev<span class="w"> </span>Python3<span class="w"> </span>python3-pip<span class="w"> </span>gcc<span class="w"> </span>g++<span class="w"> </span>make<span class="w"> </span>cmake<span class="w"> </span>doxygen
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
</input><label class="sd-tab-label" data-sync-id="rhel" for="sd-tab-item-1">
RHEL</label><div class="sd-tab-content docutils">
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>yum<span class="w"> </span>install<span class="w"> </span>-y<span class="w"> </span>systemd-devel<span class="w"> </span>numactl<span class="w"> </span>numactl-devel<span class="w"> </span>Python3<span class="w"> </span>python3-pip<span class="w"> </span>gcc<span class="w"> </span>gcc-g++<span class="w"> </span>make<span class="w"> </span>cmake<span class="w"> </span>libatomic<span class="w"> </span>doxygen
</pre></div>
</div>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
</input><label class="sd-tab-label" data-sync-id="sles" for="sd-tab-item-2">
SLES</label><div class="sd-tab-content docutils">
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>zypper<span class="w"> </span><span class="k">in</span><span class="w"> </span>libudev-devel<span class="w"> </span>libnuma1<span class="w"> </span>libnuma-devel<span class="w"> </span>Python3<span class="w"> </span>python3-pip<span class="w"> </span>gcc<span class="w"> </span>gcc-g++<span class="w"> </span>make<span class="w"> </span>cmake<span class="w"> </span>libatomic<span class="w"> </span>doxygen
</pre></div>
</div>
</div>
</div>
<ul class="simple">
<li><p>Python libraries such as <code class="docutils literal notranslate"><span class="pre">CppHeaderParser</span></code>, <code class="docutils literal notranslate"><span class="pre">argparse</span></code>, and <code class="docutils literal notranslate"><span class="pre">sqlite3</span></code>. To install the libraries based on the default Python installation on the system, use:</p></li>
</ul>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>pip3<span class="w"> </span>install<span class="w"> </span>cppheaderparser<span class="w"> </span>argparse<span class="w"> </span>sqlite3
</pre></div>
</div>
</section>
<section id="building-from-source">
<h3>Building from source<a class="headerlink" href="#building-from-source" title="Link to this heading">#</a></h3>
<p>With the dependencies installed, build ROCProfiler from the source code using the following steps:</p>
<ol class="arabic">
<li><p>After cloning the repository, use <code class="docutils literal notranslate"><span class="pre">CMake</span></code> to compile and install ROCProfiler. To use <code class="docutils literal notranslate"><span class="pre">CMake</span></code>, set the environment variable:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">export</span><span class="w"> </span><span class="nv">CMAKE_PREFIX_PATH</span><span class="o">=</span>/opt/rocm/include/hsa:/opt/rocm
</pre></div>
</div>
</li>
<li><p>Then, build ROCProfiler with a premade bash script.</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>./build.sh
</pre></div>
</div>
</li>
<li><p>You now have two options for utilizing the newly built ROCProfiler and its associated libraries.</p>
<ol class="loweralpha">
<li><p>The first option involves setting an environment variable to indicate the location of the executable and libraries. This enables the system to use the new <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> and related libraries instead of the default version.</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">export</span><span class="w"> </span><span class="nv">LD_LIBRARY_PATH</span><span class="o">=</span>&lt;BUILD_LOCATION&gt;:<span class="nv">$LD_LIBRARY_PATH</span>
<span class="nb">export</span><span class="w"> </span><span class="nv">PATH</span><span class="o">=</span>&lt;BUILD_LOCATION&gt;/bin:<span class="nv">$PATH</span>
</pre></div>
</div>
</li>
<li><p>A second option is to specify the desired location for the installation of the executable and libraries if you don’t want the installation process to move the executable and libraries to the default location. To specify the installation location, set the environment variable:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">export</span><span class="w"> </span><span class="nv">CMAKE_INSTALL_PREFIX</span><span class="o">=</span>&lt;LOCAL<span class="w"> </span>INSTALL<span class="w"> </span>FOLDER&gt;
</pre></div>
</div>
</li>
</ol>
</li>
<li><p>To install <code class="docutils literal notranslate"><span class="pre">rocprof</span></code> in the build directory, run:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">cd</span><span class="w"> </span>build
make<span class="w"> </span>install
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The Makefile is generated by <code class="docutils literal notranslate"><span class="pre">CMake</span></code>.</p>
</div>
</li>
</ol>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../index.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">ROCProfiler documentation</p>
      </div>
    </a>
    <a class="right-next"
       href="installv2.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Installing ROCProfilerV2</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#installing-from-source-files">Installing from source files</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#prerequisites">Prerequisites</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#building-from-source">Building from source</a></li>
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
