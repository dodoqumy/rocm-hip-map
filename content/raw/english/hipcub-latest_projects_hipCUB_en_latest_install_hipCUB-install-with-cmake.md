---
title: "Building and installing hipCUB with CMake &#8212; hipCUB 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipCUB/en/latest/install/hipCUB-install-with-cmake.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:18:33.527959+00:00
content_hash: "01400c6a3bc96324"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Build and install hipCUB with CMake" name="description" />
<meta content="install, building, hipCUB, AMD, ROCm, source code, cmake" name="keywords" />

    <title>Building and installing hipCUB with CMake &#8212; hipCUB 4.2.0 Documentation</title>
  
  
  
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
    <link rel="stylesheet" type="text/css" href="../_static/styles/sphinx-book-theme.css?v=384b581d" />
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
    <script src="../_static/design-tabs.js?v=36754332"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'install/hipCUB-install-with-cmake';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="hipCUB" href="../doxygen/html/index.html" />
    <link rel="prev" title="Building and installing hipCUB on Windows" href="hipCUB-install-on-Windows.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hipcub" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/install/hipCUB-install-with-cmake.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
  
  
  
  
  
  
    <p class="title logo__title">hipCUB 4.2.0 Documentation</p>
  
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
        <p aria-level="2" class="caption" role="heading"><span class="caption-text">Installation</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="hipCUB-prerequisites.html">Installation prerequisites</a></li>
<li class="toctree-l1"><a class="reference internal" href="hipCUB-install-overview.html">Installation overview</a></li>
<li class="toctree-l1"><a class="reference internal" href="hipCUB-install-on-Windows.html">Installing on Windows</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Installing on Linux and Windows with CMake</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../doxygen/html/index.html">API library</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2 has-children"><a class="reference internal" href="../doxygen/html/namespaces_namespaces.html">Namespaces</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/namespaces.html">Namespace List</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../doxygen/html/namespacemembers_namespace_members.html">Namespace Members</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/namespacemembers.html">All</a></li>
<li class="toctree-l4"><a class="reference internal" href="../doxygen/html/namespacemembers_func.html">Functions</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">Building...</li>
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
    <h1>Building and installing hipCUB with CMake</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="building-and-installing-hipcub-with-cmake">
<span id="install-with-cmake"></span><h1>Building and installing hipCUB with CMake<a class="headerlink" href="#building-and-installing-hipcub-with-cmake" title="Link to this heading">#</a></h1>
<p>You can build and install hipCUB with CMake on Windows or Linux.</p>
<p>Before you begin, set <code class="docutils literal notranslate"><span class="pre">CXX</span></code> to <code class="docutils literal notranslate"><span class="pre">amdclang++</span></code> or <code class="docutils literal notranslate"><span class="pre">hipcc</span></code>, and set <code class="docutils literal notranslate"><span class="pre">CMAKE_CXX_COMPILER</span></code> to the compiler’s absolute path. For example:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="nv">CXX</span><span class="o">=</span>amdclang++
<span class="nv">CMAKE_CXX_COMPILER</span><span class="o">=</span>/opt/rocm/bin/amdclang++
</pre></div>
</div>
<p>After <a class="reference internal" href="hipCUB-install-overview.html"><span class="doc">cloning the project</span></a>, create the <code class="docutils literal notranslate"><span class="pre">build</span></code> directory under the <code class="docutils literal notranslate"><span class="pre">hipcub</span></code> root directory, then change directory to the <code class="docutils literal notranslate"><span class="pre">build</span></code> directory:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>mkdir<span class="w"> </span>build
<span class="nb">cd</span><span class="w"> </span>build
</pre></div>
</div>
<p>Generate the makefile using the <code class="docutils literal notranslate"><span class="pre">cmake</span></code> command:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>../.<span class="w"> </span><span class="o">[</span>-D&lt;<span class="nv">OPTION1</span><span class="o">=</span>VALUE1&gt;<span class="w"> </span><span class="o">[</span>-D&lt;<span class="nv">OPTION2</span><span class="o">=</span>VALUE2&gt;<span class="o">]</span><span class="w"> </span>...<span class="o">]</span>
</pre></div>
</div>
<p>The available build options are:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">BUILD_BENCHMARK</span></code>. Set this to <code class="docutils literal notranslate"><span class="pre">ON</span></code> to build benchmark tests. Off by default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BUILD_TEST</span></code>. Set this to <code class="docutils literal notranslate"><span class="pre">ON</span></code> to build tests. Off by default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BUILD_EXAMPLE</span></code>. Set this to <code class="docutils literal notranslate"><span class="pre">ON</span></code> to build the hipCUB examples. Default is <code class="docutils literal notranslate"><span class="pre">OFF</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">USE_SYSTEM_LIB</span></code>: Set to <code class="docutils literal notranslate"><span class="pre">ON</span></code> to use the installed <code class="docutils literal notranslate"><span class="pre">hipCUB</span></code> from the system when building the tests. Off by default. For this option to take effect, <code class="docutils literal notranslate"><span class="pre">BUILD_TEST</span></code> must be <code class="docutils literal notranslate"><span class="pre">ON</span></code> and the <code class="docutils literal notranslate"><span class="pre">hipCUB</span></code> install (with its dependencies) must be compatible with the version of the tests.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BUILD_ADDRESS_SANITIZER</span></code>. Set this to <code class="docutils literal notranslate"><span class="pre">ON</span></code> to build with the Clang address sanitizer enabled. Default is <code class="docutils literal notranslate"><span class="pre">OFF</span></code>.</p></li>
<li><p>`` EXTERNAL_DEPS_FORCE_DOWNLOAD``. Set this to <code class="docutils literal notranslate"><span class="pre">ON</span></code> to download the non-ROCm dependencies such as Google Test even if they’re already installed. Default is <code class="docutils literal notranslate"><span class="pre">OFF</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BUILD_OFFLOAD_COMPRESS</span></code>. Set this to <code class="docutils literal notranslate"><span class="pre">OFF</span></code> to prevent the <code class="docutils literal notranslate"><span class="pre">--offload-compress</span></code> switch from being passed to the compiler and compressing the binary. On by default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">USE_HIPCXX</span></code>. Set this to <code class="docutils literal notranslate"><span class="pre">ON</span></code> to build with CMake HIP language support. Setting this to <code class="docutils literal notranslate"><span class="pre">ON</span></code> eliminates the need to use <code class="docutils literal notranslate"><span class="pre">CXX=hipcc</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">OFF</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ROCPRIM_FETCH_METHOD</span></code>. Set this to the method to use to download rocPRIM. Can be set to <code class="docutils literal notranslate"><span class="pre">PACKAGE</span></code>, <code class="docutils literal notranslate"><span class="pre">DOWNLOAD</span></code>, or <code class="docutils literal notranslate"><span class="pre">MONOREPO</span></code>. Set to <code class="docutils literal notranslate"><span class="pre">MONOREPO</span></code> if rocPRIM isn’t already installed and you’re building hipCUB from within a clone of the <a class="reference external" href="https://github.com/ROCm/rocm-libraries/">rocm-libraries</a> repository that also includes rocPRIM. Set to <code class="docutils literal notranslate"><span class="pre">DOWNLOAD</span></code> if rocPRIM isn’t installed and you aren’t in a clone of the <code class="docutils literal notranslate"><span class="pre">rocm-libraries</span></code> repository that includes rocPRIM. <code class="docutils literal notranslate"><span class="pre">DOWNLOAD</span></code> will clone the repository using sparse checkout so that only the necessary files are downloaded. Set to <code class="docutils literal notranslate"><span class="pre">PACKAGE</span></code> if rocPRIM is already installed. If you specify <code class="docutils literal notranslate"><span class="pre">PACKAGE</span></code> but rocPRIM isn’t installed, the files will be downloaded using the same method as the <code class="docutils literal notranslate"><span class="pre">DOWNLOAD</span></code> option. The default method is <code class="docutils literal notranslate"><span class="pre">PACKAGE</span></code>.</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If you’re using a version of git earlier than 2.25, <code class="docutils literal notranslate"><span class="pre">-DROCPRIM_FETCH_METHOD=DOWNLOAD</span></code> will download the entire <code class="docutils literal notranslate"><span class="pre">rocm-libraries</span></code> repository.</p>
</div>
<p>Build hipCUB using the generated make file:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>make<span class="w"> </span>-j4
</pre></div>
</div>
<p>After you’ve built hipCUB, you can optionally generate tar, zip, and deb packages:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>make<span class="w"> </span>package
</pre></div>
</div>
<p>Finally, install hipCUB:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>make<span class="w"> </span>install
</pre></div>
</div>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="hipCUB-install-on-Windows.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Building and installing hipCUB on Windows</p>
      </div>
    </a>
    <a class="right-next"
       href="../doxygen/html/index.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">hipCUB</p>
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
