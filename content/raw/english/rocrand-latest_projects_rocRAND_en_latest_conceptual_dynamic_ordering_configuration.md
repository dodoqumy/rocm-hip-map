---
title: "Kernel configurations for dynamic ordering &#8212; rocRAND 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocRAND/en/latest/conceptual/dynamic_ordering_configuration.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:08:27.621511+00:00
content_hash: "81b3375484d25712"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="rocRAND documentation for dynamic ordering configuration" name="description" />
<meta content="rocRAND, ROCm, API, documentation, dynamic ordering" name="keywords" />

    <title>Kernel configurations for dynamic ordering &#8212; rocRAND 4.2.0 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'conceptual/dynamic_ordering_configuration';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Random number generators" href="generator-types.html" />
    <link rel="prev" title="cuRAND compatibility" href="curand-compatibility.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-rocrand" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/conceptual/dynamic_ordering_configuration.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1"><a class="reference internal" href="programmers-guide.html">Programming guide</a></li>
<li class="toctree-l1"><a class="reference internal" href="curand-compatibility.html">cuRAND compatibility</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Kernel configurations for dynamic ordering</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Kernel configurations for dynamic ordering</span></li>
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
    <h1>Kernel configurations for dynamic ordering</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#building-the-tuning-benchmarks">Building the tuning benchmarks</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-the-number-of-multiprocessors-as-candidates">Using the number of multiprocessors as candidates</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#running-the-tuning-benchmarks">Running the tuning benchmarks</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#processing-the-benchmark-results">Processing the benchmark results</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#adding-support-for-a-new-gpu-architecture">Adding support for a new GPU architecture</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="kernel-configurations-for-dynamic-ordering">
<span id="dynamic-ordering-configuration"></span><h1>Kernel configurations for dynamic ordering<a class="headerlink" href="#kernel-configurations-for-dynamic-ordering" title="Link to this heading">#</a></h1>
<p>When dynamic ordering (<code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DYNAMIC</span></code>) is set, rocRAND selects the number of blocks and threads
to launch on the GPU to accommodate the specific GPU model best.
Consequently, the number of allocated generators and the sequence of the generated numbers can also vary.</p>
<p>The tuning, which is the selection of the most performant configuration for each GPU architecture,
can be performed in an automated manner. The necessary tools and benchmarks for the tuning are provided
in the rocRAND repository. The following sections provide additional details about the tuning process.</p>
<section id="building-the-tuning-benchmarks">
<span id="tuning-benchmark-build"></span><h2>Building the tuning benchmarks<a class="headerlink" href="#building-the-tuning-benchmarks" title="Link to this heading">#</a></h2>
<p>The principle behind the tuning is straightforward. The random number generation kernel is run
for a list of kernel block size and kernel grid size combinations. The fastest combination
is then selected as the dynamic ordering configuration for that particular device.
rocRAND provides an executable target named <code class="docutils literal notranslate"><span class="pre">benchmark_rocrand_tuning</span></code> that runs the benchmarks with all these
combinations.</p>
<p>This target is disabled by default, but it can be enabled and built using the following snippet.
Use the <code class="docutils literal notranslate"><span class="pre">GPU_TARGETS</span></code> variable to specify a comma-separated list of GPU architectures to build the benchmarks for.
To determine the architecture of the installed GPU(s), run the <code class="docutils literal notranslate"><span class="pre">rocminfo</span></code> command
and look for <code class="docutils literal notranslate"><span class="pre">gfx</span></code> in the “ISA Info” section.</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nb">cd</span><span class="w"> </span>rocm-libraries/projects/rocrand
cmake<span class="w"> </span>-S<span class="w"> </span>.<span class="w"> </span>-B<span class="w"> </span>./build
<span class="w">   </span>-D<span class="w"> </span><span class="nv">BUILD_BENCHMARK</span><span class="o">=</span>ON
<span class="w">   </span>-D<span class="w"> </span><span class="nv">BUILD_BENCHMARK_TUNING</span><span class="o">=</span>ON
<span class="w">   </span>-D<span class="w"> </span><span class="nv">CMAKE_CXX_COMPILER</span><span class="o">=</span>/opt/rocm/bin/amdclang++
<span class="w">   </span>-D<span class="w"> </span><span class="nv">GPU_TARGETS</span><span class="o">=</span>gfx908
cmake<span class="w"> </span>--build<span class="w"> </span>build<span class="w"> </span>--target<span class="w"> </span>benchmark_rocrand_tuning
</pre></div>
</div>
<p>The following CMake cache variables control the generation of the benchmarked matrix:</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Variable name</p></th>
<th class="head"><p>Explanation</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">BENCHMARK_TUNING_THREAD_OPTIONS</span></code></p></td>
<td><p>Comma-separated list of benchmarked block sizes</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">BENCHMARK_TUNING_BLOCK_OPTIONS</span></code></p></td>
<td><p>Comma-separated list of benchmarked grid sizes</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">BENCHMARK_TUNING_MIN_GRID_SIZE</span></code></p></td>
<td><p>Configurations with fewer total threads are omitted</p></td>
</tr>
</tbody>
</table>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The benchmark tuning is only supported for AMD GPUs.</p>
</div>
<section id="using-the-number-of-multiprocessors-as-candidates">
<h3>Using the number of multiprocessors as candidates<a class="headerlink" href="#using-the-number-of-multiprocessors-as-candidates" title="Link to this heading">#</a></h3>
<p>Multiples of the number of multiprocessors on the GPU being benchmarked are
good candidate values for <code class="docutils literal notranslate"><span class="pre">BENCHMARK_TUNING_BLOCK_OPTIONS</span></code>.
The <code class="docutils literal notranslate"><span class="pre">rocm-libraries/projects/rocrand/scripts/config-tuning/get_tuned_grid_sizes.py</span></code> executable
runs <code class="docutils literal notranslate"><span class="pre">rocminfo</span></code> to acquire the number of multiprocessors and prints a comma-separated list
of grid size candidates to the standard output.</p>
</section>
</section>
<section id="running-the-tuning-benchmarks">
<span id="tuning-benchmark-run"></span><h2>Running the tuning benchmarks<a class="headerlink" href="#running-the-tuning-benchmarks" title="Link to this heading">#</a></h2>
<p>After building the <code class="docutils literal notranslate"><span class="pre">benchmark_rocrand_tuning</span></code> target, you can run the benchmarks
and collect the results for further processing.
The benchmarks can run for a long time, so it is crucial that the GPU in use is thermally stable.
For instance, there must be adequate cooling to keep the GPU at the preset clock rates without throttling.
Additionally, ensure that no other workload is concurrently dispatched to the GPU.
Otherwise, the resulting dynamic ordering configurations might not be the optimal ones.
Run the full benchmark suite using the following command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nb">cd</span><span class="w"> </span>./build/benchmark/tuning
./benchmark_rocrand_tuning<span class="w"> </span>--benchmark_out_format<span class="o">=</span>json<span class="w"> </span>--benchmark_out<span class="o">=</span>rocrand_tuning_gfx908.json
</pre></div>
</div>
<p>This executes the benchmarks and saves the benchmark results to the <code class="docutils literal notranslate"><span class="pre">rocrand_tuning_gfx908.json</span></code> JSON file.
To only run a subset of the benchmarks, such as for a single generator, use the <code class="docutils literal notranslate"><span class="pre">--benchmark_filter=&lt;regex&gt;</span></code> option,
for example, <code class="docutils literal notranslate"><span class="pre">--benchmark_filter=&quot;.*philox.*&quot;</span></code>.</p>
</section>
<section id="processing-the-benchmark-results">
<span id="tuning-benchmark-process"></span><h2>Processing the benchmark results<a class="headerlink" href="#processing-the-benchmark-results" title="Link to this heading">#</a></h2>
<p>After the benchmark results from all architectures in JSON format are available, the best configurations
are selected using the <code class="docutils literal notranslate"><span class="pre">rocm-libraries/projects/rocrand/scripts/config-tuning/select_best_config.py</span></code> script.
Ensure the prerequisite libraries are installed by running the following command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>-r<span class="w"> </span>rocm-libraries/projects/rocrand/scripts/config-tuning/requirements.txt.
</pre></div>
</div>
<p>Each rocRAND generator can generate a multitude of output types and distributions.
However, a single configuration is selected for each GPU architecture, which applies uniformly to all types
and distributions. It’s possible that the best performing configuration for one distribution
isn’t the fastest for another. <code class="docutils literal notranslate"><span class="pre">select_best_config.py</span></code> selects the configuration that performs best <strong>on average</strong>.
If any type or distribution performs worse than <code class="docutils literal notranslate"><span class="pre">ROCRAND_ORDERING_PSEUDO_DEFAULT</span></code> under the selected configuration,
a warning is printed to the standard output.
The eventual decision about whether to apply the configuration is made by the library’s maintainers.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">select_best_config.py</span></code>  script produces a set of C++ header files as output
that contain the definitions of the dynamic ordering configuration for the benchmarked architectures.
These files are intended to be copied to the <code class="docutils literal notranslate"><span class="pre">rocm-libraries/projects/rocrand/library/src/rng/config</span></code> directory of the source tree
and checked in to the version control system. The directory where the header files are written to
can be specified using the <code class="docutils literal notranslate"><span class="pre">--out-dir</span></code> option.</p>
<p>For more readable results, <code class="docutils literal notranslate"><span class="pre">select_best_config.py</span></code> can generate colorized diagrams to visually
compare the performance of the configuration candidates. To select this option, use the
optional <code class="docutils literal notranslate"><span class="pre">--plot-out</span></code> argument, for example, <code class="docutils literal notranslate"><span class="pre">--plot-out</span> <span class="pre">rocrand-tuning.svg</span></code>.
This generates an SVG image for each GPU architecture processed by the script.</p>
<p>The following invokation of the <code class="docutils literal notranslate"><span class="pre">select_best_config.py</span></code> script demonstrates all these options:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>./rocm-libraries/projects/rocrand/scripts/config-tuning/select_best_config.py<span class="w"> </span>--plot-out<span class="w"> </span>./rocrand-tuning.svg<span class="w"> </span>--out-dir<span class="w"> </span>./rocm-libraries/projects/rocrand/library/src/rng/config/<span class="w"> </span>./rocm-libraries/projects/rocrand/build/benchmark/tuning/rocrand_tuning_gfx908.json<span class="w"> </span>./rocm-libraries/projects/rocrand/build/benchmark/tuning/rocrand_tuning_gfx1030.json
</pre></div>
</div>
</section>
<section id="adding-support-for-a-new-gpu-architecture">
<h2>Adding support for a new GPU architecture<a class="headerlink" href="#adding-support-for-a-new-gpu-architecture" title="Link to this heading">#</a></h2>
<p>This section is intended for developers who want to add rocRAND support for a new GPU architecture.
To add support, follow this checklist:</p>
<ol class="arabic simple">
<li><p>Update the hard-coded list of recognized architectures in the <code class="docutils literal notranslate"><span class="pre">library/src/rng/config_types.hpp</span></code> file. The following symbols must be updated accordingly:</p>
<ul class="simple">
<li><p>Enum class <code class="docutils literal notranslate"><span class="pre">target_arch</span></code>: Lists the recognized architectures as an enumeration.</p></li>
<li><p>Function <code class="docutils literal notranslate"><span class="pre">get_device_arch</span></code>: The device to compile to in the device code.</p></li>
<li><p>Function <code class="docutils literal notranslate"><span class="pre">parse_gcn_arch</span></code>: Translates from the name of the architecture to the <code class="docutils literal notranslate"><span class="pre">target_arch</span></code> enum in the host code.</p></li>
</ul>
</li>
<li><p>The tuning benchmarks must be compiled and run for the new architecture. See <a class="reference internal" href="#tuning-benchmark-build"><span class="std std-ref">Building the tuning benchmarks</span></a> and <a class="reference internal" href="#tuning-benchmark-run"><span class="std std-ref">Running the tuning benchmarks</span></a>.</p></li>
<li><p>The benchmark results must be processed by the <code class="docutils literal notranslate"><span class="pre">select_best_config.py</span></code> script. See <a class="reference internal" href="#tuning-benchmark-process"><span class="std std-ref">Processing the benchmark results</span></a>.</p></li>
<li><p>The resulting header files must be added to version control in the <code class="docutils literal notranslate"><span class="pre">rocm-libraries/projects/rocrand/library/src/rng/config</span></code> directory.</p></li>
</ol>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="curand-compatibility.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">cuRAND compatibility</p>
      </div>
    </a>
    <a class="right-next"
       href="generator-types.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Random number generators</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#building-the-tuning-benchmarks">Building the tuning benchmarks</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-the-number-of-multiprocessors-as-candidates">Using the number of multiprocessors as candidates</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#running-the-tuning-benchmarks">Running the tuning benchmarks</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#processing-the-benchmark-results">Processing the benchmark results</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#adding-support-for-a-new-gpu-architecture">Adding support for a new GPU architecture</a></li>
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
