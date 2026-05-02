---
title: "rocRAND programming guide &#8212; rocRAND 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocRAND/en/latest/conceptual/programmers-guide.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:08:33.670949+00:00
content_hash: "664b58228914622e"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Programming guide for rocRAND" name="description" />
<meta content="rocRAND, ROCm, API, documentation, programming, generator types" name="keywords" />

    <title>rocRAND programming guide &#8212; rocRAND 4.2.0 Documentation</title>
  
  
  
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
  <link href="../_static/styles/theme.css?digest=8878045cc6db502f8baf" rel="stylesheet" />
<link href="../_static/styles/pydata-sphinx-theme.css?digest=8878045cc6db502f8baf" rel="stylesheet" />

    <link rel="stylesheet" type="text/css" href="../_static/pygments.css?v=a746c00c" />
    <link rel="stylesheet" type="text/css" href="../_static/styles/sphinx-book-theme.css?v=384b581d" />
    <link rel="stylesheet" type="text/css" href="../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
    <link rel="stylesheet" type="text/css" href="../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../_static/sphinx-design.min.css?v=87e54e7c" />
  
  <!-- So that users can add custom icons -->
  <script src="../_static/scripts/fontawesome.js?digest=8878045cc6db502f8baf"></script>
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../_static/scripts/bootstrap.js?digest=8878045cc6db502f8baf" />
<link rel="preload" as="script" href="../_static/scripts/pydata-sphinx-theme.js?digest=8878045cc6db502f8baf" />

    <script src="../_static/documentation_options.js?v=830d3dd9"></script>
    <script src="../_static/doctools.js?v=9a2dae69"></script>
    <script src="../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../_static/search.js?v=90a4452c"></script>
    <script src="../_static/scripts/sphinx-book-theme.js?v=efea14e4"></script>
    <script src="../_static/design-tabs.js?v=f930bc37"></script>
    <script>window.MathJax = {"options": {"processHtmlClass": "tex2jax_process|mathjax_process|math|output_area"}}</script>
    <script defer="defer" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'conceptual/programmers-guide';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="cuRAND compatibility" href="curand-compatibility.html" />
    <link rel="prev" title="Installing and building rocRAND" href="../install/installing.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocrand" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/conceptual/programmers-guide.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
  <body data-bs-spy="scroll" data-bs-target=".bd-toc-nav" data-offset="180" data-bs-root-margin="0px 0px -60%" data-default-mode="">

  
  
  <div id="pst-skip-link" class="skip-link d-print-none"><a href="#main-content">Skip to main content</a></div>
  
  <div id="pst-scroll-pixel-helper"></div>
  
  <button type="button" class="btn rounded-pill" id="pst-back-to-top">
    <i class="fa-solid fa-arrow-up"></i>Back to top</button>

  
  <dialog id="pst-search-dialog">
    
<form class="bd-search d-flex align-items-center"
      action="../search.html"
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

  
    
  

<a class="navbar-brand logo" href="../index.html">
  
  
  
  
  
  
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
<li class="toctree-l1"><a class="reference internal" href="../install/installing.html">Installation guide</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Programming guide</a></li>
<li class="toctree-l1"><a class="reference internal" href="curand-compatibility.html">cuRAND compatibility</a></li>
<li class="toctree-l1"><a class="reference internal" href="dynamic_ordering_configuration.html">Kernel configurations for dynamic ordering</a></li>
<li class="toctree-l1"><a class="reference internal" href="generator-types.html">Random number generators</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Examples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocrand/python/rocrand/examples">Examples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">API reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../api-reference/data-type-support.html">rocRAND data type support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../api-reference/cpp-api.html">C/C++ API reference</a></li>
<li class="toctree-l1"><a class="reference internal" href="../api-reference/python-api.html">Python API reference</a></li>
<li class="toctree-l1"><a class="reference internal" href="../fortran-api-reference.html">Fortran API reference</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../doxygen/html/index.html">API library</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../doxygen/html/modules.html">Modules</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../doxygen/html/annotated_classes.html">Classes</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/annotated.html">Class List</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/hierarchy.html">Class Hierarchy</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../doxygen/html/functions_class_members.html">Class Members</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_all.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_func_functions.html">Functions</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_vars.html">Variables</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_type.html">Typedefs</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/functions_rela.html">Related Functions</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="../doxygen/html/files.html">Files</a></li>
</ul>
</details></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">About</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../license.html">License</a></li>
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
      <a href="../index.html" class="nav-link" aria-label="Home">
        <i class="fa-solid fa-home"></i>
      </a>
    </li>
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">rocRAND programming guide</span></li>
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
<label class="sidebar-toggle secondary-toggle btn btn-sm" for="__secondary"title="Toggle secondary sidebar" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <span class="fa-solid fa-list"></span>
</label>
</div></div>
      
    </div>
  
</div>
</div>
              
              

<div id="jb-print-docs-body" class="onlyprint">
    <h1>rocRAND programming guide</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#generator-types">Generator types</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#ordering">Ordering</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#using-rocrand-in-hip-graphs">Using rocRAND in HIP Graphs</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="rocrand-programming-guide">
<span id="programmers-guide"></span><h1>rocRAND programming guide<a class="headerlink" href="#rocrand-programming-guide" title="Link to this heading">#</a></h1>
<p>This topic discusses some issues to consider when using rocRAND in your application.</p>
<section id="generator-types">
<h2>Generator types<a class="headerlink" href="#generator-types" title="Link to this heading">#</a></h2>
<p>There are two main generator classes in rocRAND</p>
<ul class="simple">
<li><p>Pseudo-Random Number Generators (PRNGs)</p></li>
<li><p>Quasi-Random Number Generators (QRNGs)</p></li>
</ul>
<p>The following pseudo-random number generators are available:</p>
<ul class="simple">
<li><p>XORWOW</p></li>
<li><p>MRG32K3A</p></li>
<li><p>MTGP32</p></li>
<li><p>Philox 4x32-10</p></li>
<li><p>MRG31K3P</p></li>
<li><p>LFSR113</p></li>
<li><p>MT19937</p></li>
<li><p>ThreeFry 2x32-20, 4x32-30, 2x64-20, and 4x64-20</p></li>
</ul>
<p>The following quasi-random number generators are available:</p>
<ul class="simple">
<li><p>Sobol32</p></li>
<li><p>Sobol64</p></li>
<li><p>Scrambled Sobol32</p></li>
<li><p>Scrambled Sobol64</p></li>
</ul>
<p>For more information about the generator types, see <a class="reference internal" href="generator-types.html"><span class="doc">Random number generators</span></a>.</p>
</section>
<section id="ordering">
<h2>Ordering<a class="headerlink" href="#ordering" title="Link to this heading">#</a></h2>
<p>rocRAND generators can be configured to change how the results are ordered in global memory.
These parameters can be used to, for example, tune the performance versus the reproducibility of rocRAND generators.
The following ordering types are available:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_BEST</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_SEEDED</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_QUASI_DEFAULT</span></code></p></li>
</ul>
<p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code> and <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_QUASI_DEFAULT</span></code> are the default ordering types
for pseudo- and quasi-random number generators, respectively. <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code> is the
same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_BEST</span></code> and <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p>
<p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code> indicates that rocRAND can change the output ordering
to obtain the best performance for a particular generator on a particular GPU.
Using this ordering, the generated sequences can vary between GPU models and rocRAND versions.
For more information about generating these configurations, see <a class="reference internal" href="dynamic_ordering_configuration.html"><span class="doc">Kernel configurations for dynamic ordering</span></a>.
<code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code> is not supported for generators created with <code class="docutils literal notranslate"><span class="pre">rocrand_create_generator_host</span></code>.</p>
<p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code> indicates that rocRAND should generate values in a backward-compatible way.
When this type is set, rocRAND generates exactly the same sequences across releases.</p>
<p>All supported orderings for all generators are listed below:</p>
<div class="pst-scrollable-table-container"><table class="table" id="id1">
<caption><span class="caption-number">Table 1 </span><span class="caption-text">XORWOW ordering support</span><a class="headerlink" href="#id1" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Ordering</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_BEST</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_SEEDED</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code></p></td>
<td><p>There are <span class="math notranslate nohighlight">\(131072\)</span> generators in total, each of which are separated by <span class="math notranslate nohighlight">\(2^{67}\)</span> values. The results are generated in an interleaved fashion. The result at offset <span class="math notranslate nohighlight">\(n\)</span> in memory is generated from offset <span class="math notranslate nohighlight">\((n\;\mathrm{mod}\; 131072) \cdot 2^{67} + \lfloor n / 131072 \rfloor\)</span> in the XORWOW sequence for a particular seed.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code></p></td>
<td><p>The ordering depends on the GPU that is used.</p></td>
</tr>
</tbody>
</table>
</div>
<div class="pst-scrollable-table-container"><table class="table" id="id2">
<caption><span class="caption-number">Table 2 </span><span class="caption-text">MRG32K3A ordering support</span><a class="headerlink" href="#id2" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Ordering</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_BEST</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code></p></td>
<td><p>There are <span class="math notranslate nohighlight">\(131072\)</span> generators in total, each of which are separated by <span class="math notranslate nohighlight">\(2^{76}\)</span> values. The results are generated in an interleaved fashion. The result at offset <span class="math notranslate nohighlight">\(n\)</span> in memory is generated from offset <span class="math notranslate nohighlight">\((n\;\mathrm{mod}\; 131072) \cdot 2^{76} + \lfloor n / 131072 \rfloor\)</span> in the MRG32K3A sequence for a particular seed.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code></p></td>
<td><p>The ordering depends on the GPU that is used.</p></td>
</tr>
</tbody>
</table>
</div>
<div class="pst-scrollable-table-container"><table class="table" id="id3">
<caption><span class="caption-number">Table 3 </span><span class="caption-text">MTGP32 ordering support</span><a class="headerlink" href="#id3" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Ordering</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_BEST</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code></p></td>
<td><p>There are <span class="math notranslate nohighlight">\(512\)</span> generators in total, each of which generates <span class="math notranslate nohighlight">\(256\)</span> values per iteration. Blocks of <span class="math notranslate nohighlight">\(256\)</span> elements from generators are concatenated to form the output. The result at offset <span class="math notranslate nohighlight">\(n\)</span> in memory is generated from generator <span class="math notranslate nohighlight">\(\lfloor n / 256\rfloor\;\mathrm{mod}\; 512\)</span>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code></p></td>
<td><p>The ordering depends on the GPU that is used.</p></td>
</tr>
</tbody>
</table>
</div>
<div class="pst-scrollable-table-container"><table class="table" id="id4">
<caption><span class="caption-number">Table 4 </span><span class="caption-text">Philox 4x32-10 ordering support</span><a class="headerlink" href="#id4" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Ordering</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_BEST</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code></p></td>
<td><p>There is only one Philox generator, and the result at offset <span class="math notranslate nohighlight">\(n\)</span> is the <span class="math notranslate nohighlight">\(n\)</span>-th value from this generator.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code></p></td>
<td><p>The ordering depends on the GPU that is used.</p></td>
</tr>
</tbody>
</table>
</div>
<div class="pst-scrollable-table-container"><table class="table" id="id5">
<caption><span class="caption-number">Table 5 </span><span class="caption-text">MT19937 ordering support</span><a class="headerlink" href="#id5" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Ordering</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_BEST</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code></p></td>
<td><p>The Mersenne Twister sequence is generated from <span class="math notranslate nohighlight">\(8192\)</span> generators in total, and each of these are separated by <span class="math notranslate nohighlight">\(2^{1000}\)</span> values. Each generator generates <span class="math notranslate nohighlight">\(8\)</span> elements per iteration. The result at offset <span class="math notranslate nohighlight">\(n\)</span> is generated from generator <span class="math notranslate nohighlight">\((\lfloor n / 8\rfloor\;\mathrm{mod}\; 8192) \cdot 2^{1000} + \lfloor n / (8 \cdot 8192) \rfloor + \lfloor n / 8 \rfloor\)</span>.</p></td>
</tr>
</tbody>
</table>
</div>
<div class="pst-scrollable-table-container"><table class="table" id="id6">
<caption><span class="caption-number">Table 6 </span><span class="caption-text">MRG31K3P ordering support</span><a class="headerlink" href="#id6" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Ordering</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_BEST</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code></p></td>
<td><p>There are <span class="math notranslate nohighlight">\(131072\)</span> generators in total, each of which are separated by <span class="math notranslate nohighlight">\(2^{72}\)</span> values. The results are generated in an interleaved fashion. The result at offset <span class="math notranslate nohighlight">\(n\)</span> in memory is generated from offset <span class="math notranslate nohighlight">\((n\;\mathrm{mod}\; 131072) \cdot 2^{72} + \lfloor n / 131072 \rfloor\)</span> in the MRG31K3P sequence for a particular seed.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code></p></td>
<td><p>The ordering depends on the GPU that is used.</p></td>
</tr>
</tbody>
</table>
</div>
<div class="pst-scrollable-table-container"><table class="table" id="id7">
<caption><span class="caption-number">Table 7 </span><span class="caption-text">LFSR113 ordering support</span><a class="headerlink" href="#id7" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Ordering</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_BEST</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code></p></td>
<td><p>There are <span class="math notranslate nohighlight">\(131072\)</span> generators in total, each of which are separated by <span class="math notranslate nohighlight">\(2^{55}\)</span> values. The results are generated in an interleaved fashion. The result at offset <span class="math notranslate nohighlight">\(n\)</span> in memory is generated from offset <span class="math notranslate nohighlight">\((n\;\mathrm{mod}\; 131072) \cdot 2^{55} + \lfloor n / 131072 \rfloor\)</span> in the LFSR113 sequence for a particular seed.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code></p></td>
<td><p>The ordering depends on the GPU that is used.</p></td>
</tr>
</tbody>
</table>
</div>
<div class="pst-scrollable-table-container"><table class="table" id="id8">
<caption><span class="caption-number">Table 8 </span><span class="caption-text">ThreeFry ordering support</span><a class="headerlink" href="#id8" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Ordering</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_BEST</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code></p></td>
<td><p>The same as <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code>.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_LEGACY</span></code></p></td>
<td><p>There is only one ThreeFry generator, and the result at offset <span class="math notranslate nohighlight">\(n\)</span> is the <span class="math notranslate nohighlight">\(n\)</span>-th value from this generator.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code></p></td>
<td><p>The ordering depends on the GPU that is used.</p></td>
</tr>
</tbody>
</table>
</div>
<div class="pst-scrollable-table-container"><table class="table" id="id9">
<caption><span class="caption-number">Table 9 </span><span class="caption-text">Sobol ordering support</span><a class="headerlink" href="#id9" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Ordering</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_QUASI_DEFAULT</span></code></p></td>
<td><p>The (scrambled) 32- and 64-bit sobol quasi-random number generators generated the result from <span class="math notranslate nohighlight">\(d\)</span> dimensions by flattening them into the output. The result at offset <span class="math notranslate nohighlight">\(n\)</span> in memory is generated from offset <span class="math notranslate nohighlight">\(n\;\mathrm{mod}\; d\)</span> in dimension <span class="math notranslate nohighlight">\(\lfloor n / d \rfloor\)</span>, where <span class="math notranslate nohighlight">\(d\)</span> is the generator’s number of dimensions.</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="using-rocrand-in-hip-graphs">
<h2>Using rocRAND in HIP Graphs<a class="headerlink" href="#using-rocrand-in-hip-graphs" title="Link to this heading">#</a></h2>
<p>rocRAND supports capturing the random number generation with HIP Graphs.
However, the construction, initialization, and cleanup of the generator objects must take place
outside of the recorded section. See the following example (error handling is omitted for brevity):</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="kt">size_t</span><span class="w">        </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1000</span><span class="p">;</span>
<span class="kt">float</span><span class="o">*</span><span class="w">        </span><span class="n">data_0</span><span class="p">;</span>
<span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">data_1</span><span class="p">;</span>

<span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">data_0</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">data_0</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>
<span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">data_1</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">data_1</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>

<span class="n">hipGraph_t</span><span class="w"> </span><span class="n">graph</span><span class="p">;</span>
<span class="n">hipGraphCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>

<span class="n">hipStream_t</span><span class="w"> </span><span class="n">stream</span><span class="p">;</span>
<span class="n">hipStreamCreateWithFlags</span><span class="p">(</span><span class="o">&amp;</span><span class="n">stream</span><span class="p">,</span><span class="w"> </span><span class="n">hipStreamNonBlocking</span><span class="p">);</span>

<span class="n">rocrand_generator</span><span class="w"> </span><span class="n">generator</span><span class="p">;</span>
<span class="n">rocrand_create_generator</span><span class="p">(</span><span class="o">&amp;</span><span class="n">generator</span><span class="p">,</span><span class="w"> </span><span class="n">ROCRAND_RNG_PSEUDO_DEFAULT</span><span class="p">);</span>
<span class="n">rocrand_set_stream</span><span class="p">(</span><span class="n">generator</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="p">);</span>
<span class="n">rocrand_initialize_generator</span><span class="p">(</span><span class="n">generator</span><span class="p">);</span>

<span class="n">hipStreamBeginCapture</span><span class="p">(</span><span class="n">stream</span><span class="p">,</span><span class="w"> </span><span class="n">hipStreamCaptureModeGlobal</span><span class="p">);</span>

<span class="n">rocrand_generate_normal</span><span class="p">(</span><span class="n">generator</span><span class="p">,</span><span class="w"> </span><span class="n">data_0</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="mf">10.0F</span><span class="p">,</span><span class="w"> </span><span class="mf">2.0F</span><span class="p">);</span>
<span class="n">rocrand_generate_poisson</span><span class="p">(</span><span class="n">generator</span><span class="p">,</span><span class="w"> </span><span class="n">data_1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="mi">3</span><span class="p">);</span>

<span class="n">hipStreamEndCapture</span><span class="p">(</span><span class="n">stream</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">graph</span><span class="p">);</span>

<span class="n">hipGraphExec_t</span><span class="w"> </span><span class="n">instance</span><span class="p">;</span>
<span class="n">hipGraphInstantiate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">instance</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>

<span class="n">hipGraphLaunch</span><span class="p">(</span><span class="n">instance</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="p">);</span>
<span class="n">hipStreamSynchronize</span><span class="p">(</span><span class="n">stream</span><span class="p">);</span>

<span class="n">hipGraphExecDestroy</span><span class="p">(</span><span class="n">instance</span><span class="p">);</span>
<span class="n">rocrand_destroy_generator</span><span class="p">(</span><span class="n">generator</span><span class="p">);</span>
<span class="n">hipStreamDestroy</span><span class="p">(</span><span class="n">stream</span><span class="p">);</span>
<span class="n">hipGraphDestroy</span><span class="p">(</span><span class="n">graph</span><span class="p">);</span>
<span class="n">hipFree</span><span class="p">(</span><span class="n">data_1</span><span class="p">);</span>
<span class="n">hipFree</span><span class="p">(</span><span class="n">data_0</span><span class="p">);</span>
</pre></div>
</div>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../install/installing.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Installing and building rocRAND</p>
      </div>
    </a>
    <a class="right-next"
       href="curand-compatibility.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">cuRAND compatibility</p>
      </div>
      <i class="fa-solid fa-angle-right"></i>
    </a>
</div>
                </footer>
              
            </div>
            
            
              
                <dialog id="pst-secondary-sidebar-modal"></dialog>
                <div id="pst-secondary-sidebar" class="bd-sidebar-secondary bd-toc"><div class="sidebar-secondary-items sidebar-secondary__inner">


  <div class="sidebar-secondary-item">
  <div class="page-toc tocsection onthispage">
    <i class="fa-solid fa-list"></i> Contents
  </div>
  <nav class="bd-toc-nav page-toc">
    <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#generator-types">Generator types</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#ordering">Ordering</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#using-rocrand-in-hip-graphs">Using rocRAND in HIP Graphs</a></li>
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
  <script defer src="../_static/scripts/bootstrap.js?digest=8878045cc6db502f8baf"></script>
<script defer src="../_static/scripts/pydata-sphinx-theme.js?digest=8878045cc6db502f8baf"></script>

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
    <img id="rdc-watermark" src="../_static/images/alpha-watermark.svg" alt="DRAFT watermark"/>
</div> -->
  </body>
</html>
