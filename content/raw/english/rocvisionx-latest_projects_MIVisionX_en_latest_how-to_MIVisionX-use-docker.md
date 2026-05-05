---
title: "Using Docker with MIVisionX &#8212; MIVisionX 3.5.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/MIVisionX/en/latest/how-to/MIVisionX-use-docker.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:11:01.407186+00:00
content_hash: "1ae741691a62caf2"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="MIVisionX API" name="description" />
<meta content="MIVisionX, ROCm, API, reference, data type, support" name="keywords" />

    <title>Using Docker with MIVisionX &#8212; MIVisionX 3.5.0 Documentation</title>
  
  
  
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
    <link rel="stylesheet" type="text/css" href="../_static/styles/sphinx-book-theme.css?v=a3416100" />
    <link rel="stylesheet" type="text/css" href="../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
    <link rel="stylesheet" type="text/css" href="../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../_static/sphinx-design.min.css?v=95c83b7e" />
  
  <!-- So that users can add custom icons -->
  <script src="../_static/scripts/fontawesome.js?digest=8878045cc6db502f8baf"></script>
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../_static/scripts/bootstrap.js?digest=8878045cc6db502f8baf" />
<link rel="preload" as="script" href="../_static/scripts/pydata-sphinx-theme.js?digest=8878045cc6db502f8baf" />

    <script src="../_static/documentation_options.js?v=d3112e53"></script>
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
    <script src="../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/MIVisionX-use-docker';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-mivisionx" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/MIVisionX-use-docker.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/MIVisionX" id="navgithub" role="button" aria-expanded="false" target="_blank" >
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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/MIVisionX/issues/new/choose" id="navsupport" role="button" aria-expanded="false" target="_blank" >
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
  
  
  
  
  
  
    <p class="title logo__title">MIVisionX 3.5.0 Documentation</p>
  
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
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-prerequisites.html">Prerequisites</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-linux-build-and-install.html">Build and install on Linux</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-package-install.html">Install using the package installer on Linux</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-windows-install.html">Install on Windows</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-macOS-install.html">Install on macOS</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-model-compiler-install.html">Install the model compiler</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-install-OpenVX.html">Install OpenVX</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/MIVisionX-test-install.html">Test the installation</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="MIVisionX-how-to-model-compiler.html">Use the model compiler</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../reference/MIVisionX-AMD-Openvx.html">AMD OpenVX</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/MIVisionX-supported-models.html">Supported models and operators</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/MIVisionX-toolkits.html">Toolkits</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/MIVisionX-env-variables.html">Environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="../doxygen/html/modules.html">API Reference</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Examples</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../tutorials/MIVisionX-apps-samples.html">Sample applications</a></li>
<li class="toctree-l1"><a class="reference internal" href="../tutorials/MIVisionX-model-comp-samples.html">Model compiler samples</a></li>
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
    <li class="breadcrumb-item active" aria-current="page"><span class="ellipsis">Using Docker with MIVisionX</span></li>
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
<button class="sidebar-toggle secondary-toggle btn btn-sm" title="Toggle secondary sidebar" data-bs-placement="bottom" data-bs-toggle="tooltip">
    <span class="fa-solid fa-list"></span>
</button>
</div></div>
      
    </div>
  
</div>
</div>
              
              

<div id="jb-print-docs-body" class="onlyprint">
    <h1>Using Docker with MIVisionX</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#docker-workflow-on-ubuntu-22-04-24-04">Docker workflow on Ubuntu 22.04/24.04</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#prerequisites">Prerequisites</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#workflow">Workflow</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#run-docker-image-local-machine">Run docker image: Local Machine</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#option-1-map-localhost-directory-on-the-docker-image">Option 1: Map localhost directory on the docker image</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#option-2-display-with-docker">Option 2: Display with docker</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#run-docker-image-with-display-remote-server-machine">Run docker image with display: Remote Server Machine</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#build-dockerfiles">Build - dockerfiles</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#run-docker">Run - docker</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#ubuntu-20-22-dockerfiles">Ubuntu <cite>20</cite>/<cite>22</cite> DockerFiles</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="using-docker-with-mivisionx">
<span id="mivisionx-docker"></span><h1>Using Docker with MIVisionX<a class="headerlink" href="#using-docker-with-mivisionx" title="Link to this heading">#</a></h1>
<p>Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers. Refer to <a class="reference external" href="https://github.com/ROCm/MIVisionX/wiki/Docker">Rocm Docker Wiki</a> for additional information.</p>
<section id="docker-workflow-on-ubuntu-22-04-24-04">
<h2>Docker workflow on Ubuntu 22.04/24.04<a class="headerlink" href="#docker-workflow-on-ubuntu-22-04-24-04" title="Link to this heading">#</a></h2>
<section id="prerequisites">
<h3>Prerequisites<a class="headerlink" href="#prerequisites" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p>Ubuntu 22.04/24.04</p></li>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html">ROCm supported hardware</a></p></li>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/">Install ROCm</a> with <code class="docutils literal notranslate"><span class="pre">--usecase=rocm</span></code></p></li>
<li><p><a class="reference external" href="https://docs.docker.com/engine/install/ubuntu/">Docker</a></p></li>
</ul>
</section>
<section id="workflow">
<h3>Workflow<a class="headerlink" href="#workflow" title="Link to this heading">#</a></h3>
<ol class="arabic simple">
<li><p>Get the latest docker image. Use the following command to bring in the latest changes from upstream.</p></li>
</ol>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>docker<span class="w"> </span>pull<span class="w"> </span>mivisionx/ubuntu-22.04:latest
</pre></div>
</div>
<ol class="arabic simple" start="2">
<li><p>Run docker image</p></li>
</ol>
</section>
<section id="run-docker-image-local-machine">
<h3>Run docker image: Local Machine<a class="headerlink" href="#run-docker-image-local-machine" title="Link to this heading">#</a></h3>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>docker<span class="w"> </span>run<span class="w"> </span>-it<span class="w"> </span>--privileged<span class="w"> </span>--device<span class="o">=</span>/dev/kfd<span class="w"> </span>--device<span class="o">=</span>/dev/dri<span class="w"> </span>--device<span class="o">=</span>/dev/mem<span class="w"> </span>--cap-add<span class="o">=</span>SYS_RAWIO<span class="w">  </span>--group-add<span class="w"> </span>video<span class="w"> </span>--shm-size<span class="o">=</span>4g<span class="w"> </span>--ipc<span class="o">=</span><span class="s2">&quot;host&quot;</span><span class="w"> </span>--network<span class="o">=</span>host<span class="w"> </span>mivisionx/ubuntu-20.04:latest
</pre></div>
</div>
<ul class="simple">
<li><p>Computer Vision Test</p></li>
</ul>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>python3<span class="w"> </span>/workspace/MIVisionX/tests/vision_tests/runVisionTests.py<span class="w"> </span>--num_frames<span class="w"> </span><span class="m">1</span>
</pre></div>
</div>
<ul class="simple">
<li><p>Neural Network Test</p></li>
</ul>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>python3<span class="w"> </span>/workspace/MIVisionX/tests/neural_network_tests/runNeuralNetworkTests.py<span class="w"> </span>--profiler_level<span class="w"> </span><span class="m">1</span>
</pre></div>
</div>
<ul class="simple">
<li><p>Khronos OpenVX 1.3.0 Conformance Test</p></li>
</ul>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>python3<span class="w"> </span>/workspace/MIVisionX/tests/conformance_tests/runConformanceTests.py<span class="w"> </span>--backend_type<span class="w"> </span>HOST
</pre></div>
</div>
<section id="option-1-map-localhost-directory-on-the-docker-image">
<h4>Option 1: Map localhost directory on the docker image<a class="headerlink" href="#option-1-map-localhost-directory-on-the-docker-image" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Option to map the localhost directory with data to be accessed on the docker image: <code class="docutils literal notranslate"><span class="pre">-v</span> <span class="pre">{LOCAL_HOST_DIRECTORY_PATH}:{DOCKER_DIRECTORY_PATH}</span></code></p></li>
</ul>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>docker<span class="w"> </span>run<span class="w"> </span>-it<span class="w"> </span>-v<span class="w"> </span>/home/:/root/hostDrive/<span class="w"> </span>--privileged<span class="w"> </span>--device<span class="o">=</span>/dev/kfd<span class="w"> </span>--device<span class="o">=</span>/dev/dri<span class="w"> </span>--device<span class="o">=</span>/dev/mem<span class="w"> </span>--cap-add<span class="o">=</span>SYS_RAWIO<span class="w">  </span>--group-add<span class="w"> </span>video<span class="w"> </span>--shm-size<span class="o">=</span>4g<span class="w"> </span>--ipc<span class="o">=</span><span class="s2">&quot;host&quot;</span><span class="w"> </span>--network<span class="o">=</span>host<span class="w"> </span>mivisionx/ubuntu-20.04:latest
</pre></div>
</div>
</section>
<section id="option-2-display-with-docker">
<h4>Option 2: Display with docker<a class="headerlink" href="#option-2-display-with-docker" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Using host display for docker</p></li>
</ul>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>xhost<span class="w"> </span>+local:root
sudo<span class="w"> </span>docker<span class="w"> </span>run<span class="w"> </span>-it<span class="w"> </span>--privileged<span class="w"> </span>--device<span class="o">=</span>/dev/kfd<span class="w"> </span>--device<span class="o">=</span>/dev/dri<span class="w"> </span>--cap-add<span class="o">=</span>SYS_RAWIO<span class="w"> </span>--device<span class="o">=</span>/dev/mem<span class="w"> </span>--group-add<span class="w"> </span>video<span class="w"> </span>--network<span class="w"> </span>host<span class="w"> </span>--env<span class="w"> </span><span class="nv">DISPLAY</span><span class="o">=</span><span class="nv">$DISPLAY</span><span class="w"> </span>--volume<span class="o">=</span><span class="s2">&quot;</span><span class="nv">$HOME</span><span class="s2">/.Xauthority:/root/.Xauthority:rw&quot;</span><span class="w"> </span>--volume<span class="w"> </span>/tmp/.X11-unix/:/tmp/.X11-unix<span class="w"> </span>mivisionx/ubuntu-22.04:latest
</pre></div>
</div>
<ul class="simple">
<li><p>Test display with MIVisionX sample</p></li>
</ul>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>runvx<span class="w"> </span>-v<span class="w"> </span>/opt/rocm/share/mivisionx/samples/gdf/canny.gdf
</pre></div>
</div>
</section>
</section>
<section id="run-docker-image-with-display-remote-server-machine">
<h3>Run docker image with display: Remote Server Machine<a class="headerlink" href="#run-docker-image-with-display-remote-server-machine" title="Link to this heading">#</a></h3>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>docker<span class="w"> </span>run<span class="w"> </span>-it<span class="w"> </span>--privileged<span class="w"> </span>--device<span class="o">=</span>/dev/kfd<span class="w"> </span>--device<span class="o">=</span>/dev/dri<span class="w"> </span>--cap-add<span class="o">=</span>SYS_RAWIO<span class="w"> </span>--device<span class="o">=</span>/dev/mem<span class="w"> </span>--group-add<span class="w"> </span>video<span class="w"> </span>--network<span class="w"> </span>host<span class="w"> </span>--env<span class="w"> </span><span class="nv">DISPLAY</span><span class="o">=</span><span class="nv">$DISPLAY</span><span class="w"> </span>--volume<span class="o">=</span><span class="s2">&quot;</span><span class="nv">$HOME</span><span class="s2">/.Xauthority:/root/.Xauthority:rw&quot;</span><span class="w"> </span>--volume<span class="w"> </span>/tmp/.X11-unix/:/tmp/.X11-unix<span class="w"> </span>mivisionx/ubuntu-22.04:latest
</pre></div>
</div>
<ul class="simple">
<li><p>Display with MIVisionX sample</p></li>
</ul>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>runvx<span class="w"> </span>-v<span class="w"> </span>/opt/rocm/share/mivisionx/samples/gdf/canny.gdf
</pre></div>
</div>
</section>
</section>
<section id="build-dockerfiles">
<h2>Build - dockerfiles<a class="headerlink" href="#build-dockerfiles" title="Link to this heading">#</a></h2>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>docker<span class="w"> </span>build<span class="w"> </span>--build-arg<span class="w"> </span><span class="o">{</span>ARG_1_NAME<span class="o">}={</span>ARG_1_VALUE<span class="o">}</span><span class="w"> </span><span class="o">[</span>--build-arg<span class="w"> </span><span class="o">{</span>ARG_2_NAME<span class="o">}={</span>ARG_2_VALUE<span class="o">}]</span><span class="w"> </span>-f<span class="w"> </span><span class="o">{</span>DOCKER_FILE_NAME<span class="o">}</span>.dockerfile<span class="w"> </span>-t<span class="w"> </span><span class="o">{</span>DOCKER_IMAGE_NAME<span class="o">}</span><span class="w"> </span>.
</pre></div>
</div>
</section>
<section id="run-docker">
<h2>Run - docker<a class="headerlink" href="#run-docker" title="Link to this heading">#</a></h2>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>docker<span class="w"> </span>run<span class="w"> </span>-it<span class="w"> </span>--privileged<span class="w"> </span>--device<span class="o">=</span>/dev/kfd<span class="w"> </span>--device<span class="o">=</span>/dev/dri<span class="w"> </span>--cap-add<span class="o">=</span>SYS_RAWIO<span class="w"> </span>--device<span class="o">=</span>/dev/mem<span class="w"> </span>--group-add<span class="w"> </span>video<span class="w"> </span>--network<span class="w"> </span>host<span class="w"> </span>--env<span class="w"> </span><span class="nv">DISPLAY</span><span class="o">=</span><span class="nv">$DISPLAY</span><span class="w"> </span>--volume<span class="o">=</span><span class="s2">&quot;</span><span class="nv">$HOME</span><span class="s2">/.Xauthority:/root/.Xauthority:rw&quot;</span><span class="w"> </span>--volume<span class="w"> </span>/tmp/.X11-unix/:/tmp/.X11-unix<span class="w"> </span><span class="o">{</span>DOCKER_IMAGE_NAME<span class="o">}</span>
</pre></div>
</div>
</section>
<section id="ubuntu-20-22-dockerfiles">
<h2>Ubuntu <cite>20</cite>/<cite>22</cite> DockerFiles<a class="headerlink" href="#ubuntu-20-22-dockerfiles" title="Link to this heading">#</a></h2>
<ul class="simple">
<li><p><img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> New component added to the level</p></li>
<li><p><img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> Existing component from the previous level</p></li>
</ul>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 12.8%" />
<col style="width: 12.8%" />
<col style="width: 20.5%" />
<col style="width: 41.0%" />
<col style="width: 12.8%" />
</colgroup>
<tbody>
<tr class="row-odd"><td><p><strong>Build Level</strong></p></td>
<td><p><strong>MIVisionX Dependencies</strong></p></td>
<td><p><strong>Modules</strong></p></td>
<td><p><strong>Libraries and Executables</strong></p></td>
<td><p><strong>Docker File</strong></p></td>
</tr>
<tr class="row-even"><td><p>Level_1</p></td>
<td><p>cmake <br /> gcc <br /> g++</p></td>
<td><p>amd_openvx  <br /> utilities</p></td>
<td><p><img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> <code class="docutils literal notranslate"><span class="pre">libopenvx.so</span></code> - OpenVX Lib - CPU <br /> <img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvxu.so</span></code> - OpenVX immediate node Lib - CPU <br /> <img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> <code class="docutils literal notranslate"><span class="pre">runvx</span></code> - OpenVX Graph Executor - CPU with Display OFF</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">level-1.dockerfile</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Level_2</p></td>
<td><p>ROCm OpenCL <br /> +Level 1</p></td>
<td><p>amd_openvx <br /> amd_openvx_extensions <br /> utilities</p></td>
<td><p><img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libopenvx.so</span></code> - OpenVX Lib - CPU/GPU <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvxu.so</span></code> - OpenVX immediate node Lib - CPU/GPU <br /> <img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_loomsl.so</span></code> - Loom 360 Stitch Lib <br /> <img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> <code class="docutils literal notranslate"><span class="pre">loom_shell</span></code> - 360 Stitch App <br /> <img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> <code class="docutils literal notranslate"><span class="pre">runcl</span></code> - OpenCL Debug App <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">runvx</span></code> - OpenVX Graph Executor - Display OFF</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">level-2.dockerfile</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Level_3</p></td>
<td><p>OpenCV <br /> FFMPEG <br /> +Level 2</p></td>
<td><p>amd_openvx <br /> amd_openvx_extensions <br /> utilities</p></td>
<td><p><img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libopenvx.so</span></code> - OpenVX Lib <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvxu.so</span></code> - OpenVX immediate node Lib <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_loomsl.so</span></code> - Loom 360 Stitch Lib <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">loom_shell</span></code> - 360 Stitch App <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">runcl</span></code> - OpenCL Debug App <br /> <img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_amd_media.so</span></code> - OpenVX Media Extension <br /> <img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_opencv.so</span></code> - OpenVX OpenCV InterOp Extension <br /> <img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> <code class="docutils literal notranslate"><span class="pre">mv_compile</span></code> - Neural Net Model Compile <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">runvx</span></code> - OpenVX Graph Executor - Display ON</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">level-3.dockerfile</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Level_4</p></td>
<td><p>MIOpenGEMM <br /> MIOpen <br /> ProtoBuf <br /> +Level 3</p></td>
<td><p>amd_openvx <br /> amd_openvx_extensions <br /> apps <br /> utilities</p></td>
<td><p><img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libopenvx.so</span></code> - OpenVX Lib <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvxu.so</span></code> - OpenVX immediate node Lib <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_loomsl.so</span></code> - Loom 360 Stitch Lib <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">loom_shell</span></code> - 360 Stitch App <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_amd_media.so</span></code> - OpenVX Media Extension <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_opencv.so</span></code> - OpenVX OpenCV InterOp Extension <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">mv_compile</span></code> - Neural Net Model Compile <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">runcl</span></code> - OpenCL Debug App <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">runvx</span></code> - OpenVX Graph Executor - Display ON <br /> <img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_nn.so</span></code> - OpenVX Neural Net Extension <br /> <img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> <code class="docutils literal notranslate"><span class="pre">inference_server_app</span></code> - Cloud Inference App</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">level-4.dockerfile</span></code></p></td>
</tr>
<tr class="row-even"><td><p>Level_5</p></td>
<td><p>AMD_RPP <br /> RPP deps <br /> +Level 4</p></td>
<td><p>amd_openvx <br /> amd_openvx_extensions <br /> apps <br /> AMD VX RPP <br /> utilities</p></td>
<td><p><img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libopenvx.so</span></code> - OpenVX Lib <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvxu.so</span></code> - OpenVX immediate node Lib <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_loomsl.so</span></code> - Loom 360 Stitch Lib <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">loom_shell</span></code> - 360 Stitch App <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_amd_media.so</span></code> - OpenVX Media Extension <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_opencv.so</span></code> - OpenVX OpenCV InterOp Extension <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">mv_compile</span></code> - Neural Net Model Compile <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">runcl</span></code> - OpenCL Debug App <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">runvx</span></code> - OpenVX Graph Executor - Display ON <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_nn.so</span></code> - OpenVX Neural Net Extension <br /> <img alt="Blue Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/blue_square.png" /> <code class="docutils literal notranslate"><span class="pre">inference_server_app</span></code> - Cloud Inference App <br /> <img alt="Green Square" src="https://raw.githubusercontent.com/ROCm/MIVisionX/master/docs/data/green_square.png" /> <code class="docutils literal notranslate"><span class="pre">libvx_rpp.so</span></code> - OpenVX RPP Extension</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">level-5.dockerfile</span></code></p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#docker-workflow-on-ubuntu-22-04-24-04">Docker workflow on Ubuntu 22.04/24.04</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#prerequisites">Prerequisites</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#workflow">Workflow</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#run-docker-image-local-machine">Run docker image: Local Machine</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#option-1-map-localhost-directory-on-the-docker-image">Option 1: Map localhost directory on the docker image</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#option-2-display-with-docker">Option 2: Display with docker</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#run-docker-image-with-display-remote-server-machine">Run docker image with display: Remote Server Machine</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#build-dockerfiles">Build - dockerfiles</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#run-docker">Run - docker</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#ubuntu-20-22-dockerfiles">Ubuntu <cite>20</cite>/<cite>22</cite> DockerFiles</a></li>
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
