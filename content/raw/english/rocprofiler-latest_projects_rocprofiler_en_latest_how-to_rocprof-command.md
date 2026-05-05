---
title: "rocprof command help &#8212; ROCProfiler 2.0.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler/en/latest/how-to/rocprof-command.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:20:57.028290+00:00
content_hash: "026f711a362d8290"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="ROCProfiler is a powerful tool for profiling HIP and ROCm applications on AMD ROCm software" name="description" />
<meta content="ROCProfiler command line tool, ROCProfiler command line, rocprof, rocprofv1" name="keywords" />

    <title>rocprof command help &#8212; ROCProfiler 2.0.0 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/rocprof-command';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Using rocprofv2" href="rocprofv2-usage.html" />
    <link rel="prev" title="Using rocprof" href="using-rocprof.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocprofiler-docs" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/rocprof-command.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1 current active"><a class="current reference internal" href="#">rocprof command help</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">rocprof command help</li>
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
    <h1>rocprof command help</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="rocprof-command-help">
<span id="rocprof-command"></span><h1>rocprof command help<a class="headerlink" href="#rocprof-command-help" title="Link to this heading">#</a></h1>
<p>Obtain command line help by typing the following:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>-h
</pre></div>
</div>
<p>This returns the following information:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>RPL:<span class="w"> </span>on<span class="w"> </span><span class="s1">&#39;240505_115025&#39;</span><span class="w"> </span>from<span class="w"> </span><span class="s1">&#39;/opt/rocm-6.2.0-13748&#39;</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="s1">&#39;/home/rocm&#39;</span>
ROCm<span class="w"> </span>Profiling<span class="w"> </span>Library<span class="w"> </span><span class="o">(</span>RPL<span class="o">)</span><span class="w"> </span>run<span class="w"> </span>script,<span class="w"> </span>a<span class="w"> </span>part<span class="w"> </span>of<span class="w"> </span>ROCprofiler<span class="w"> </span>library<span class="w"> </span>package.
Full<span class="w"> </span>path:<span class="w"> </span>/opt/rocm-6.2.0-13748/bin/rocprof
Metrics<span class="w"> </span>definition:<span class="w"> </span>/opt/rocm-6.2.0-13748/lib/rocprofiler/metrics.xml

Usage:
rocprof<span class="w"> </span><span class="o">[</span>-h<span class="o">]</span><span class="w"> </span><span class="o">[</span>--list-basic<span class="o">]</span><span class="w"> </span><span class="o">[</span>--list-derived<span class="o">]</span><span class="w"> </span><span class="o">[</span>-i<span class="w"> </span>&lt;input<span class="w"> </span>.txt/.xml<span class="w"> </span>file&gt;<span class="o">]</span><span class="w"> </span><span class="o">[</span>-o<span class="w"> </span>&lt;output<span class="w"> </span>CSV<span class="w"> </span>file&gt;<span class="o">]</span><span class="w"> </span>&lt;app<span class="w"> </span><span class="nb">command</span><span class="w"> </span>line&gt;

Options:
-h<span class="w"> </span>-<span class="w"> </span>this<span class="w"> </span><span class="nb">help</span>
--tool-version<span class="w"> </span>&lt;<span class="m">1</span><span class="p">|</span><span class="m">2</span>&gt;<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span>use<span class="w"> </span>specific<span class="w"> </span>version<span class="w"> </span>of<span class="w"> </span>rocprof<span class="w"> </span>tool,<span class="w"> </span>by<span class="w"> </span>default<span class="w"> </span>v1<span class="w"> </span>is<span class="w"> </span>used
<span class="w">            </span><span class="m">1</span><span class="w"> </span>-<span class="w"> </span>rocprofiler<span class="w"> </span>tool<span class="w"> </span>v1
<span class="w">            </span><span class="m">2</span><span class="w"> </span>-<span class="w"> </span>rocprofiler<span class="w"> </span>tool<span class="w"> </span>v2
--verbose<span class="w"> </span>-<span class="w"> </span>verbose<span class="w"> </span>mode,<span class="w"> </span>dumping<span class="w"> </span>all<span class="w"> </span>base<span class="w"> </span>counters<span class="w"> </span>used<span class="w"> </span><span class="k">in</span><span class="w"> </span>the<span class="w"> </span>input<span class="w"> </span>metrics
--list-basic<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span>print<span class="w"> </span>the<span class="w"> </span>list<span class="w"> </span>of<span class="w"> </span>basic<span class="w"> </span>HW<span class="w"> </span>counters
--list-derived<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span>print<span class="w"> </span>the<span class="w"> </span>list<span class="w"> </span>of<span class="w"> </span>derived<span class="w"> </span>metrics<span class="w"> </span>with<span class="w"> </span>formulas
--cmd-qts<span class="w"> </span>&lt;on<span class="p">|</span>off&gt;<span class="w"> </span>-<span class="w"> </span>quoting<span class="w"> </span>profiled<span class="w"> </span>cmd<span class="w"> </span>line<span class="w"> </span><span class="o">[</span>on<span class="o">]</span>

-i<span class="w"> </span>&lt;.txt<span class="p">|</span>.xml<span class="w"> </span>file&gt;<span class="w"> </span>-<span class="w"> </span>input<span class="w"> </span>file
<span class="w">    </span>Input<span class="w"> </span>file<span class="w"> </span>.txt<span class="w"> </span>format,<span class="w"> </span>automatically<span class="w"> </span>rerun<span class="w"> </span>application<span class="w"> </span><span class="k">for</span><span class="w"> </span>every<span class="w"> </span>profiling<span class="w"> </span>features<span class="w"> </span>line:

<span class="w">        </span><span class="c1"># Perf counters group 1</span>
<span class="w">        </span>pmc<span class="w"> </span>:<span class="w"> </span>Wavefronts<span class="w"> </span>VALUInsts<span class="w"> </span>SALUInsts<span class="w"> </span>SFetchInsts<span class="w"> </span>FlatVMemInsts<span class="w"> </span>LDSInsts<span class="w"> </span>FlatLDSInsts<span class="w"> </span>GDSInsts<span class="w"> </span>VALUUtilization<span class="w"> </span>FetchSize
<span class="w">        </span><span class="c1"># Perf counters group 2</span>
<span class="w">        </span>pmc<span class="w"> </span>:<span class="w"> </span>WriteSize<span class="w"> </span>L2CacheHit
<span class="w">        </span><span class="c1"># Filter by dispatches range, GPU index and kernel names</span>
<span class="w">        </span><span class="c1"># supported range formats: &quot;3:9&quot;, &quot;3:&quot;, &quot;3&quot;</span>
<span class="w">        </span>range:<span class="w"> </span><span class="m">1</span><span class="w"> </span>:<span class="w"> </span><span class="m">4</span>
<span class="w">        </span>gpu:<span class="w"> </span><span class="m">0</span><span class="w"> </span><span class="m">1</span><span class="w"> </span><span class="m">2</span><span class="w"> </span><span class="m">3</span>
<span class="w">        </span>kernel:<span class="w"> </span>simple<span class="w"> </span>Pass1<span class="w"> </span>simpleConvolutionPass2

<span class="w">    </span>Input<span class="w"> </span>file<span class="w"> </span>.xml<span class="w"> </span>format,<span class="w"> </span><span class="k">for</span><span class="w"> </span>single<span class="w"> </span>profiling<span class="w"> </span>run:

<span class="w">        </span><span class="c1"># Metrics list definition, also the form &quot;&lt;block-name&gt;:&lt;event-id&gt;&quot; can be used</span>
<span class="w">        </span><span class="c1"># All defined metrics can be found in the &#39;metrics.xml&#39;</span>
<span class="w">        </span><span class="c1"># There are basic metrics for raw HW counters and high-level metrics for derived counters</span>
<span class="w">        </span>&lt;metric<span class="w"> </span><span class="nv">name</span><span class="o">=</span>SQ:4,SQ_WAVES,VFetchInsts
<span class="w">        </span>&gt;&lt;/metric&gt;

<span class="w">        </span><span class="c1"># Filter by dispatches range, GPU index and kernel names</span>
<span class="w">        </span>&lt;metric
<span class="w">        </span><span class="c1"># range formats: &quot;3:9&quot;, &quot;3:&quot;, &quot;3&quot;</span>
<span class="w">        </span><span class="nv">range</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
<span class="w">        </span><span class="c1"># list of gpu indexes &quot;0,1,2,3&quot;</span>
<span class="w">        </span><span class="nv">gpu_index</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
<span class="w">        </span><span class="c1"># list of matched sub-strings &quot;Simple1,Conv1,SimpleConvolution&quot;</span>
<span class="w">        </span><span class="nv">kernel</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
<span class="w">        </span>&gt;&lt;/metric&gt;

-o<span class="w"> </span>&lt;output<span class="w"> </span>file&gt;<span class="w"> </span>-<span class="w"> </span>output<span class="w"> </span>CSV<span class="w"> </span>file<span class="w"> </span><span class="o">[</span>&lt;input<span class="w"> </span>file<span class="w"> </span>base&gt;.csv<span class="o">]</span>
-d<span class="w"> </span>&lt;data<span class="w"> </span>directory&gt;<span class="w"> </span>-<span class="w"> </span>directory<span class="w"> </span>where<span class="w"> </span>profiler<span class="w"> </span>store<span class="w"> </span>profiling<span class="w"> </span>data<span class="w"> </span>including<span class="w"> </span>traces<span class="w"> </span><span class="o">[</span>/tmp<span class="o">]</span>
<span class="w">    </span>The<span class="w"> </span>data<span class="w"> </span>directory<span class="w"> </span>is<span class="w"> </span>automatically<span class="w"> </span>removed<span class="w"> </span><span class="k">if</span><span class="w"> </span>it<span class="w"> </span>is<span class="w"> </span>matching<span class="w"> </span>the<span class="w"> </span>default<span class="w"> </span>temporary<span class="w"> </span>directory.
-t<span class="w"> </span>&lt;temporary<span class="w"> </span>directory&gt;<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span>change<span class="w"> </span>the<span class="w"> </span>temporary<span class="w"> </span>directory<span class="w"> </span><span class="o">[</span>/tmp<span class="o">]</span>
<span class="w">    </span>By<span class="w"> </span>changing<span class="w"> </span>the<span class="w"> </span>temporary<span class="w"> </span>directory<span class="w"> </span>you<span class="w"> </span>can<span class="w"> </span>prevent<span class="w"> </span>removing<span class="w"> </span>the<span class="w"> </span>profiling<span class="w"> </span>data<span class="w"> </span>from<span class="w"> </span>/tmp<span class="w"> </span>or<span class="w"> </span><span class="nb">enable</span><span class="w"> </span>removing<span class="w"> </span>from<span class="w"> </span>not<span class="w"> </span><span class="s1">&#39;/tmp&#39;</span><span class="w"> </span>directory.
-m<span class="w"> </span>&lt;metric<span class="w"> </span>file&gt;<span class="w"> </span>-<span class="w"> </span>file<span class="w"> </span>defining<span class="w"> </span>custom<span class="w"> </span>metrics<span class="w"> </span>to<span class="w"> </span>use<span class="w"> </span><span class="k">in</span>-place<span class="w"> </span>of<span class="w"> </span>defaults.

--basenames<span class="w"> </span>&lt;on<span class="p">|</span>off&gt;<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span>turn<span class="w"> </span>on/off<span class="w"> </span>truncating<span class="w"> </span>of<span class="w"> </span>the<span class="w"> </span>kernel<span class="w"> </span>full<span class="w"> </span><span class="k">function</span><span class="w"> </span>names<span class="w"> </span>till<span class="w"> </span>the<span class="w"> </span>base<span class="w"> </span>ones<span class="w"> </span><span class="o">[</span>off<span class="o">]</span>
--timestamp<span class="w"> </span>&lt;on<span class="p">|</span>off&gt;<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span>turn<span class="w"> </span>on/off<span class="w"> </span>the<span class="w"> </span>kernel<span class="w"> </span>dispatches<span class="w"> </span>timestamps,<span class="w"> </span>dispatch/begin/end/complete<span class="w"> </span>during<span class="w"> </span>kernel<span class="w"> </span>profiling<span class="w"> </span><span class="o">[</span>off<span class="o">]</span>
--ctx-wait<span class="w"> </span>&lt;on<span class="p">|</span>off&gt;<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span><span class="nb">wait</span><span class="w"> </span><span class="k">for</span><span class="w"> </span>outstanding<span class="w"> </span>contexts<span class="w"> </span>on<span class="w"> </span>profiler<span class="w"> </span><span class="nb">exit</span><span class="w"> </span><span class="o">[</span>on<span class="o">]</span>
--ctx-limit<span class="w"> </span>&lt;max<span class="w"> </span>number&gt;<span class="w"> </span>-<span class="w"> </span>maximum<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>outstanding<span class="w"> </span>contexts<span class="w"> </span><span class="o">[</span><span class="m">0</span><span class="w"> </span>-<span class="w"> </span>unlimited<span class="o">]</span>
--heartbeat<span class="w"> </span>&lt;rate<span class="w"> </span>sec&gt;<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span>print<span class="w"> </span>progress<span class="w"> </span>heartbeats<span class="w"> </span><span class="o">[</span><span class="m">0</span><span class="w"> </span>-<span class="w"> </span>disabled<span class="o">]</span>
--obj-tracking<span class="w"> </span>&lt;on<span class="p">|</span>off&gt;<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span>turn<span class="w"> </span>on/off<span class="w"> </span>kernels<span class="w"> </span>code<span class="w"> </span>objects<span class="w"> </span>tracking<span class="w"> </span><span class="o">[</span>on<span class="o">]</span>
<span class="w">    </span>To<span class="w"> </span>support<span class="w"> </span>V3<span class="w"> </span>code<span class="w"> </span>object

--stats<span class="w"> </span>-<span class="w"> </span>generating<span class="w"> </span>kernel<span class="w"> </span>execution<span class="w"> </span>stats,<span class="w"> </span>file<span class="w"> </span>&lt;output<span class="w"> </span>name&gt;.stats.csv

--roctx-trace<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span><span class="nb">enable</span><span class="w"> </span>rocTX<span class="w"> </span>application<span class="w"> </span>code<span class="w"> </span>annotation<span class="w"> </span>trace,<span class="w"> </span><span class="s2">&quot;Markers and Ranges&quot;</span><span class="w"> </span>JSON<span class="w"> </span>trace<span class="w"> </span>section.
--hip-trace<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span>trace<span class="w"> </span>HIP,<span class="w"> </span>generates<span class="w"> </span>API<span class="w"> </span>execution<span class="w"> </span>stats<span class="w"> </span>and<span class="w"> </span>JSON<span class="w"> </span>file<span class="w"> </span>chrome-tracing<span class="w"> </span>compatible
--hsa-trace<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span>trace<span class="w"> </span>HSA,<span class="w"> </span>generates<span class="w"> </span>API<span class="w"> </span>execution<span class="w"> </span>stats<span class="w"> </span>and<span class="w"> </span>JSON<span class="w"> </span>file<span class="w"> </span>chrome-tracing<span class="w"> </span>compatible
--sys-trace<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span>trace<span class="w"> </span>HIP/HSA<span class="w"> </span>APIs<span class="w"> </span>and<span class="w"> </span>GPU<span class="w"> </span>activity,<span class="w"> </span>generates<span class="w"> </span>stats<span class="w"> </span>and<span class="w"> </span>JSON<span class="w"> </span>trace<span class="w"> </span>chrome-tracing<span class="w"> </span>compatible
<span class="w">    </span><span class="s1">&#39;--hsa-trace&#39;</span><span class="w"> </span>can<span class="w"> </span>be<span class="w"> </span>used<span class="w"> </span><span class="k">in</span><span class="w"> </span>addition<span class="w"> </span>to<span class="w"> </span><span class="k">select</span><span class="w"> </span>activity<span class="w"> </span>tracing<span class="w"> </span>from<span class="w"> </span>HSA<span class="w"> </span><span class="o">(</span>ROCr<span class="w"> </span>runtime<span class="o">)</span><span class="w"> </span>level
<span class="w">    </span>Generated<span class="w"> </span>files:<span class="w"> </span>&lt;output<span class="w"> </span>name&gt;.&lt;domain&gt;_stats.txt<span class="w"> </span>&lt;output<span class="w"> </span>name&gt;.json
<span class="w">    </span>Traced<span class="w"> </span>API<span class="w"> </span>list<span class="w"> </span>can<span class="w"> </span>be<span class="w"> </span><span class="nb">set</span><span class="w"> </span>by<span class="w"> </span>input<span class="w"> </span>.txt<span class="w"> </span>or<span class="w"> </span>.xml<span class="w"> </span>files.
<span class="w">    </span>Input<span class="w"> </span>.txt:
<span class="w">    </span>hsa:<span class="w"> </span>hsa_queue_create<span class="w"> </span>hsa_amd_memory_pool_allocate
<span class="w">    </span>Input<span class="w"> </span>.xml:
<span class="w">    </span>&lt;trace<span class="w"> </span><span class="nv">name</span><span class="o">=</span><span class="s2">&quot;HSA&quot;</span>&gt;
<span class="w">        </span>&lt;parameters<span class="w"> </span><span class="nv">list</span><span class="o">=</span><span class="s2">&quot;hsa_queue_create, hsa_amd_memory_pool_allocate&quot;</span>&gt;
<span class="w">        </span>&lt;/parameters&gt;
<span class="w">    </span>&lt;/trace&gt;

--roctx-rename<span class="w"> </span>-<span class="w"> </span>to<span class="w"> </span>rename<span class="w"> </span>kernels<span class="w"> </span>with<span class="w"> </span>their<span class="w"> </span>enclosing<span class="w"> </span>rocTX<span class="w"> </span>range<span class="s1">&#39;s message.</span>

<span class="s1">--trace-start &lt;on|off&gt; - to enable tracing on start [on]</span>
<span class="s1">--trace-period &lt;dealy:length:rate&gt; - to enable trace with initial delay, with periodic sample length and rate</span>
<span class="s1">    Supported time formats: &lt;number(m|s|ms|us)&gt;</span>
<span class="s1">--flush-rate &lt;rate&gt; - to enable trace flush rate (time period)</span>
<span class="s1">    Supported time formats: &lt;number(m|s|ms|us)&gt;</span>
<span class="s1">--parallel-kernels - to enable concurrent kernels</span>

<span class="s1">Configuration file:</span>
<span class="s1">You can set your parameters defaults preferences in the configuration file &#39;</span>rpl_rc.xml<span class="s1">&#39;. The search path sequence: .:/home/rocm:&lt;installation directory&gt;</span>
<span class="s1">First the configuration file is searched in the current directory, then in the current user&#39;</span>s<span class="w"> </span>home<span class="w"> </span>directory,<span class="w"> </span>and<span class="w"> </span><span class="k">then</span><span class="w"> </span><span class="k">in</span><span class="w"> </span>the<span class="w"> </span>installation<span class="w"> </span>directory.
Configurable<span class="w"> </span>options:<span class="w"> </span><span class="s1">&#39;basenames&#39;</span>,<span class="w"> </span><span class="s1">&#39;timestamp&#39;</span>,<span class="w"> </span><span class="s1">&#39;ctx-limit&#39;</span>,<span class="w"> </span><span class="s1">&#39;heartbeat&#39;</span>,<span class="w"> </span><span class="s1">&#39;obj-tracking&#39;</span>.
An<span class="w"> </span>example<span class="w"> </span>of<span class="w"> </span><span class="s1">&#39;rpl_rc.xml&#39;</span>:
<span class="w">    </span>&lt;defaults
<span class="w">    </span><span class="nv">basenames</span><span class="o">=</span>off
<span class="w">    </span><span class="nv">timestamp</span><span class="o">=</span>off
<span class="w">    </span>ctx-limit<span class="o">=</span><span class="m">0</span>
<span class="w">    </span><span class="nv">heartbeat</span><span class="o">=</span><span class="m">0</span>
<span class="w">    </span>obj-tracking<span class="o">=</span>off
<span class="w">    </span>&gt;&lt;/defaults&gt;

--merge-traces<span class="w"> </span>-<span class="w"> </span>Script<span class="w"> </span><span class="k">for</span><span class="w"> </span>aggregating<span class="w"> </span>results<span class="w"> </span>from<span class="w"> </span>multiple<span class="w"> </span>rocprofiler<span class="w"> </span>out<span class="w"> </span>directries.
<span class="w">                </span>Usage:<span class="w"> </span><span class="k">if</span><span class="w"> </span>running<span class="w"> </span>with<span class="w"> </span>rocprof
<span class="w">                </span>rocprof<span class="w"> </span>--merge-traces<span class="w"> </span>-o<span class="w"> </span>&lt;outputdir&gt;<span class="w"> </span><span class="o">[</span>&lt;inputdir&gt;...<span class="o">]</span>
</pre></div>
</div>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="using-rocprof.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Using rocprof</p>
      </div>
    </a>
    <a class="right-next"
       href="rocprofv2-usage.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Using rocprofv2</p>
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
