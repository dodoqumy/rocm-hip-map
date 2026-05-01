---
title: "HIP Graph API Tutorial &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/graph_api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:07:27.337833+00:00
content_hash: "3dc44f12b42b9582"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="HIP graph API tutorial" name="description" />
<meta content="AMD, ROCm, HIP, graph API, tutorial" name="keywords" />

    <title>HIP Graph API Tutorial &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <link rel="stylesheet" type="text/css" href="../_static/styles/sphinx-book-theme.css?v=a3416100" />
    <link rel="stylesheet" type="text/css" href="../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
    <link rel="stylesheet" type="text/css" href="../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../_static/sphinx-design.min.css?v=95c83b7e" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_custom.css?v=35d74aab" />
  
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b" />
<link rel="preload" as="script" href="../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b" />
  <script src="../_static/vendor/fontawesome/6.5.2/js/all.min.js?digest=dfe6caa3a7d634c4db9b"></script>

    <script src="../_static/documentation_options.js?v=75144bb1"></script>
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
    <script>window.MathJax = {"options": {"processHtmlClass": "tex2jax_process|mathjax_process|math|output_area"}}</script>
    <script defer="defer" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'tutorial/graph_api';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="License" href="../license.html" />
    <link rel="prev" title="Cooperative groups" href="cooperative_groups_tutorial.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/tutorial/graph_api.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/rocm-systems" id="navgithub" role="button" aria-expanded="false" target="_blank" >
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
                            <a class="nav-link top-level header-menu-links" href="https://github.com/ROCm/rocm-systems/issues/new/choose" id="navsupport" role="button" aria-expanded="false" target="_blank" >
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
  
  
  
  
  
  
    <p class="title logo__title">HIP 7.2.53211 Documentation</p>
  
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
        <ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../what_is_hip.html">What is HIP?</a></li>
<li class="toctree-l1"><a class="reference internal" href="../hip-7-changes.html">HIP API 7.0 changes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../faq.html">Frequently asked questions</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../install/install.html">Installing HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/build.html">Building HIP from source</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Programming guide</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../understand/programming_model.html">Introduction to the HIP programming model</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/performance_optimization.html">Understanding GPU performance</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/hardware_implementation.html">Hardware implementation</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/compilers.html">HIP compilers</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/performance_guidelines.html">Performance guidelines</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/debugging.html">Debugging with HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/logging.html">Logging HIP activity</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../how-to/hip_runtime_api.html">Using HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/initialization.html">Initialization</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/host_memory.html">Host memory</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/device_memory.html">Device memory</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/device_memory/texture_fetching.html">Texture fetching</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/coherence_control.html">Coherence control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/unified_memory.html">Unified memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/virtual_memory.html">Virtual memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/stream_ordered_allocator.html">Stream Ordered Memory Allocator</a></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/error_handling.html">Error handling</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/call_stack.html">Call stack</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/asynchronous.html">Asynchronous concurrent execution</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/hipgraph.html">HIP graphs</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/cooperative_groups.html">Cooperative groups</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/multi_device.html">Multi-device management</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/opengl_interop.html">OpenGL interoperability</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/external_interop.html">External resource interoperability</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/hip_cpp_language_extensions.html">HIP C++ language extensions</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/kernel_language_cpp_support.html">Kernel language C++ support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/hip_porting_guide.html">Porting CUDA code to HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/hip_rtc.html">Programming for HIP runtime compiler (RTC)</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/amd_clr.html">AMD compute language runtimes (CLR)</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../reference/hip_runtime_api_reference.html">HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2 has-children"><a class="reference internal" href="../reference/hip_runtime_api/modules.html">Modules</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/initialization_and_version.html">Initialization and version</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/device_management.html">Device management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/execution_control.html">Execution control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/error_handling.html">Error handling</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/stream_management.html">Stream management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/stream_memory_operations.html">Stream memory operations</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/event_management.html">Event management</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/memory_management_deprecated.html">Memory management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/external_resource_interoperability.html">External resource interoperability</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html">Stream ordered memory allocator</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html">Managed memory</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html">Virtual memory management</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/texture_management.html">Texture management</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/texture_management_deprecated.html">Texture management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/surface_object.html">Surface object</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/peer_to_peer_device_memory_access.html">Peer to peer device memory access</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/context_management.html">Context management [deprecated]</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/module_management.html">Module management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/occupancy.html">Occupancy</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/profiler_control.html">Profiler control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/launch_api.html">Launch API</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html">Runtime compilation</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/callback_activity_apis.html">Callback activity APIs</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html">Graph management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/graphics_interoperability.html">Graphics interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/opengl_interoperability.html">OpenGL interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/cooperative_groups_reference.html">Cooperative groups</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../reference/hip_runtime_api/global_defines_enums_structs_files.html">Global defines, enums, structs and files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/group___global_defs.html">Global enum and defines</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/group___driver_types.html">Driver Types</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/files.html">File List</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/math_api.html">HIP math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/complex_math_api.html">HIP complex math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/env_variables.html">HIP environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/error_codes.html">HIP error codes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/api_syntax.html">CUDA to HIP API Function Comparison</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/deprecated_api_list.html">List of deprecated APIs</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/low_fp_types.html">Low Precision Floating Point Types</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/hardware_features.html">Hardware features</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Tutorials</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic">HIP basic examples</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples">HIP examples</a></li>
<li class="toctree-l1"><a class="reference internal" href="saxpy.html">SAXPY - Hello, HIP</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="programming-patterns.html">GPU programming patterns</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="programming-patterns/matrix_multiplication.html">Two-dimensional kernels: Matrix multiplication tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="programming-patterns/atomic_operations_histogram.html">Atomic operations: Histogram tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="programming-patterns/cpu_gpu_kmeans.html">CPU-GPU cooperative computing: K-means clustering tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="programming-patterns/stencil_operations.html">Stencil operations: Image convolution tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="programming-patterns/multikernel_bfs.html">Multi-kernel programming: breadth-first search tutorial</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="reduction.html">Reduction</a></li>
<li class="toctree-l1"><a class="reference internal" href="cooperative_groups_tutorial.html">Cooperative groups</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">HIP Graph API Tutorial</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">HIP Graph...</li>
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
    <h1>HIP Graph API Tutorial</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#introduction">Introduction</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#modeling-dependencies-between-gpu-operations">Modeling dependencies between GPU operations</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#streams">Streams</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#graphs">Graphs</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#when-to-use-graphs">When to use graphs</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#transitioning-a-ct-reconstruction-pipeline">Transitioning a CT reconstruction pipeline</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#what-you-will-learn">What you will learn</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#before-you-begin">Before you begin</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#required-knowledge">Required knowledge</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hardware-and-software-requirements">Hardware and software requirements</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#optional-knowledge">Optional knowledge</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#step-1-build-the-tutorial-code">Step 1: Build the tutorial code</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#step-2-examining-the-stream-based-baseline-application">Step 2: Examining the stream-based baseline application</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#understanding-batched-processing">Understanding batched processing</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#determining-parallel-capacity">Determining parallel capacity</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#processing-projections-in-batches">Processing projections in batches</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#synchronization">Synchronization</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#exploring-the-processing-pipeline">Exploring the processing pipeline</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#creating-a-trace-file">Creating a trace file</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#analyzing-the-trace">Analyzing the trace</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#step-3-converting-to-graphs-via-stream-capture">Step 3: Converting to graphs via stream capture</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#creating-a-trace">Creating a trace</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id4">Analyzing the trace</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#step-4-manual-graph-creation-advanced">Step 4: Manual graph creation (advanced)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#adding-hipfft-nodes">Adding hipFFT nodes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-1-save-existing-nodes">Step 1: Save existing nodes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-2-capture-hipfft-operations">Step 2: Capture hipFFT operations</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-3-get-updated-node-list">Step 3: Get updated node list</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-4-find-new-nodes">Step 4: Find new nodes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-5-identify-the-leaf-node">Step 5: Identify the leaf node</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id5">Creating a trace</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id6">Analyzing the trace</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#updating-individual-nodes">Updating individual nodes</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#conclusion">Conclusion</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#resources">Resources</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="hip-graph-api-tutorial">
<span id="id1"></span><h1>HIP Graph API Tutorial<a class="headerlink" href="#hip-graph-api-tutorial" title="Link to this heading">#</a></h1>
<p><strong>Time to complete</strong>: 60 minutes | <strong>Difficulty</strong>: Intermediate | <strong>Domain</strong>: Medical Imaging</p>
<section id="introduction">
<h2>Introduction<a class="headerlink" href="#introduction" title="Link to this heading">#</a></h2>
<p>Imagine you are directing a movie. In traditional GPU programming with streams, you are like a director who must call
“action!” for every single shot, waiting between each take. With HIP graphs, you pre-plan the entire scene sequence and
then call “action!” just once to film everything in one go. This tutorial will show you how to transform your GPU
applications from repeated direction to choreographed performance.</p>
<section id="modeling-dependencies-between-gpu-operations">
<h3>Modeling dependencies between GPU operations<a class="headerlink" href="#modeling-dependencies-between-gpu-operations" title="Link to this heading">#</a></h3>
<p>Most movies in the world follow a plot where certain scenes must happen before the following scenes; otherwise the
movie might not make much sense. If a scene <em>A</em> must happen before scenes <em>B</em> and <em>C</em>, <em>B</em> and <em>C</em> depend on <em>A</em>. If
<em>B</em> and <em>C</em> contain different stories that (at this point) are unrelated to each other, <em>B</em> and <em>C</em> are independent and
can be shown to the audience in any order. However, both scenes might be a prerequisite for the final scene <em>D</em>, so <em>D</em>
depends on both of them. When you represent scenes as <em>nodes</em> and dependencies as <em>edges</em>, you can create a graph, and
the graph representing your imaginary movie script will have a diamond-like shape:</p>
<figure class="align-center">
<img alt="Diagram showing a graph with diamond-like shape. Nodes represent movie scenes and edges represent dependencies between scenes." src="../_images/diamond.svg" />
</figure>
<p>You can think about GPU operations in a similar way. For example, most kernels require at least one data buffer to work
with, so they will depend on a preceding copy or <code class="docutils literal notranslate"><span class="pre">memset</span></code> operation. Others might process the results of preceding
kernels. Real-world applications typically involve multiple GPU operations with dependencies between them. HIP offers
two ways to think about and model these dependencies: streams and graphs.</p>
<section id="streams">
<h4>Streams<a class="headerlink" href="#streams" title="Link to this heading">#</a></h4>
<p>Streams are HIP’s default model for organizing and launching GPU operations on the device. They are sequential sets of
operations, similar to CPU threads. Adding operation <em>A</em> before operation <em>B</em> to a stream ensures <em>A</em> happens before
<em>B</em>, regardless of any interdependencies (or lack thereof) between them. A stream can be thought of as a first-in,
first-out (FIFO) queue of operations.</p>
<p>Multiple streams operate independently, and manual synchronization is required when dependencies cross stream
boundaries. Additionally, each operation in a stream is scheduled independently, which — depending on the complexity of
the enqueued operation — might lead to noticeable CPU launch overhead and kernel dispatch latency, especially for
workloads with many small kernels. However, applications that use streams are well suited for workloads that are
dynamic and unpredictable.</p>
<p>For more information about HIP streams, see <a class="reference internal" href="../how-to/hip_runtime_api/asynchronous.html#asynchronous-how-to"><span class="std std-ref">Asynchronous concurrent execution</span></a>.</p>
</section>
<section id="graphs">
<h4>Graphs<a class="headerlink" href="#graphs" title="Link to this heading">#</a></h4>
<p>HIP graphs model dependencies between operations as nodes and edges on a diagram. Each node in the graph represents an
operation, and each edge represents a dependency between two nodes. If no edge exists between two nodes, they are
independent and can execute in any order.</p>
<p>Because dependency information is built into the graph, the HIP runtime automatically inserts the necessary
synchronization points. Launching all operations in a graph requires only a single API call, reducing launch overhead
and dispatch latency to near-zero. This is especially beneficial for workloads with many small kernels, where launch
overhead can dominate overall execution time.</p>
<p>Graphs must be defined once before use, making them ideal for fixed workflows that run repeatedly. While node
parameters can be updated between executions, the graph structure itself cannot change after instantiation. This
structural immutability is the primary trade-off compared to the flexibility of streams.</p>
<p>For more information about HIP graphs, see <a class="reference internal" href="../how-to/hip_runtime_api/hipgraph.html#how-to-hip-graph"><span class="std std-ref">HIP graphs</span></a>.</p>
</section>
<section id="when-to-use-graphs">
<h4>When to use graphs<a class="headerlink" href="#when-to-use-graphs" title="Link to this heading">#</a></h4>
<p>This table shows when to use graphs in your application.</p>
<div class="pst-scrollable-table-container"><table class="decision-matrix table">
<thead>
<tr class="row-odd"><th class="head"><p>✅ <strong>Use Graphs When</strong></p></th>
<th class="head"><p>❌ <strong>Avoid Graphs When</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Workflow is fixed and repetitive</p></td>
<td><p>Workflow changes dynamically</p></td>
</tr>
<tr class="row-odd"><td><p>Same kernels execute many times</p></td>
<td><p>One-shot operations</p></td>
</tr>
<tr class="row-even"><td><p>Launch overhead is significant (many small kernels)</p></td>
<td><p>Kernels are long-running</p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<section id="transitioning-a-ct-reconstruction-pipeline">
<h3>Transitioning a CT reconstruction pipeline<a class="headerlink" href="#transitioning-a-ct-reconstruction-pipeline" title="Link to this heading">#</a></h3>
<p>In this tutorial, you will modify an existing GPU-accelerated stream-based image processing pipeline that reconstructs
computer tomography (CT) data (the classic Shepp-Logan phantom <a class="reference internal" href="#shlo74" id="id2"><span>[ShLo74]</span></a>). The pipeline transforms raw X-ray
projections into clear cross-sectional images used in medical diagnosis.</p>
<figure class="align-center">
<img alt="Diagram showing raw projection data being transformed into a reconstructed CT slice" src="../_images/ct_reconstruction_overview.png" />
</figure>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The tutorial application generates a phantom volume and forward projections. This GPU-accelerated operation uses
multiple streams and appears in the traces. You can ignore the dataset generation — it is not relevant to this
tutorial.</p>
</div>
<p>The reconstruction pipeline consists of:</p>
<ol class="arabic simple">
<li><p><strong>Load</strong> projection data into GPU memory</p></li>
<li><p><strong>Preprocess</strong> the projection through six stages:</p></li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>Logarithmic transformation (convert X-ray intensities)</p></li>
<li><p>Pixel weighting (correct for cone-beam geometry)</p></li>
<li><p>Forward FFT (transform to frequency domain)</p></li>
<li><p>Shepp-Logan filtering (enhance edges and improve contrast)</p></li>
<li><p>Inverse FFT (return to spatial domain)</p></li>
<li><p>Normalization (account for unnormalized FFT)</p></li>
</ol>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p><strong>Reconstruct</strong> the 3D volume using the Feldkamp-Davis-Kress (FDK) algorithm <a class="reference internal" href="#fedk84" id="id3"><span>[FeDK84]</span></a></p></li>
</ol>
<p><strong>Why HIP graphs?</strong> CT scanners process hundreds of projections per scan. By capturing this fixed workflow as a graph,
you will reduce the amount of API calls required for launching the workflow on a GPU to 1 per projection, thus reducing
launch overhead and dispatch latency to near-zero.</p>
</section>
<section id="what-you-will-learn">
<h3>What you will learn<a class="headerlink" href="#what-you-will-learn" title="Link to this heading">#</a></h3>
<p>After completing this tutorial, you will be able to:</p>
<ul class="simple">
<li><p>Convert a stream-based HIP application to a graph-based application via stream capturing</p></li>
<li><p>Create graphs manually for fine-grained control</p></li>
<li><p>Integrate graph-safe libraries like hipFFT into your graphs</p></li>
<li><p>Understand when graphs provide performance benefits</p></li>
<li><p>Apply graph concepts to your own workflows</p></li>
</ul>
</section>
<section id="before-you-begin">
<h3>Before you begin<a class="headerlink" href="#before-you-begin" title="Link to this heading">#</a></h3>
<section id="required-knowledge">
<h4>Required knowledge<a class="headerlink" href="#required-knowledge" title="Link to this heading">#</a></h4>
<p>You should be comfortable writing and debugging HIP kernels, understand basic GPU memory management concepts like
device allocation and host-to-device transfers, be familiar with HIP streams and events, and have experience using
CMake to build C++ projects. This tutorial assumes you have written at least a few HIP programs before and understand
concepts like grid dimensions and thread blocks.</p>
</section>
<section id="hardware-and-software-requirements">
<h4>Hardware and software requirements<a class="headerlink" href="#hardware-and-software-requirements" title="Link to this heading">#</a></h4>
<p>Your system needs ROCm 6.2 or later with the hipFFT library installed. The tutorial works on
all <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html" title="(in ROCm installation on Linux v7.2.2)"><span class="xref std std-doc">supported AMD GPUs</span></a>, though at least 4 GiB of GPU
memory are recommended for comfortable performance with the reconstruction workload. You will also need
<a class="reference external" href="https://git-scm.com/">git</a> to check out the code repository, <a class="reference external" href="https://www.cmake.org">CMake</a> 3.21 or later to
build the code, along with a CMake generator that supports the HIP language such as GNU Make or Ninja.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Visual Studio generators currently do not support HIP. The (optional) <code class="docutils literal notranslate"><span class="pre">rocprofv3</span></code> tool is currently supported on
Linux only.</p>
</div>
<p>To save the output volume, you need a recent version of <a class="reference external" href="https://libtiff.gitlab.io/libtiff/">libTIFF</a>. If CMake
cannot find libTIFF on your system, it automatically downloads and builds it.</p>
<p>To view both the input projections and the output volume produced by this tutorial, install a scientific image viewer
that can display 16-bit and 32-bit grayscale data, such as <a class="reference external" href="https://imagej.net/software/fiji/downloads">Fiji</a>.
Standard image viewers may be unable to correctly display the output.</p>
</section>
<section id="optional-knowledge">
<h4>Optional knowledge<a class="headerlink" href="#optional-knowledge" title="Link to this heading">#</a></h4>
<p>While not required, familiarity with Fast Fourier Transform (FFT) operations will help you understand the filtering
steps. Similarly, knowledge of medical imaging or CT reconstruction is helpful for understanding the application
context. If you have worked with signal processing or image filtering before, you will recognize some of the applied
concepts.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>You can skip the reconstruction algorithm and concentrate on the stream and graph implementations in the files
prefixed with <code class="docutils literal notranslate"><span class="pre">main_</span></code>.</p>
</div>
</section>
</section>
</section>
<section id="step-1-build-the-tutorial-code">
<h2>Step 1: Build the tutorial code<a class="headerlink" href="#step-1-build-the-tutorial-code" title="Link to this heading">#</a></h2>
<p>The full code for this tutorial is part of the <a class="reference external" href="https://github.com/ROCm/rocm-examples">ROCm examples repository</a>.
Check out the repository:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>git<span class="w"> </span>clone<span class="w"> </span>https://github.com/ROCm/rocm-examples.git
</pre></div>
</div>
<p>Then navigate to <code class="docutils literal notranslate"><span class="pre">rocm-examples/HIP-Doc/Tutorials/graph_api/</span></code>. The code can be found in the <code class="docutils literal notranslate"><span class="pre">src</span></code> subdirectory.</p>
<p>Create a separate <code class="docutils literal notranslate"><span class="pre">build</span></code> directory inside <code class="docutils literal notranslate"><span class="pre">rocm-examples/HIP-Doc/Tutorials/graph_api/</span></code>. Then
configure the project (adjust <code class="docutils literal notranslate"><span class="pre">CMAKE_HIP_ARCHITECTURES</span></code> to match your GPU):</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="nb">cd</span><span class="w"> </span>build
cmake<span class="w"> </span>-DCMAKE_PREFIX_PATH<span class="o">=</span>/opt/rocm<span class="w"> </span>-DCMAKE_BUILD_TYPE<span class="o">=</span>Release<span class="w"> </span>-DCMAKE_HIP_ARCHITECTURES<span class="o">=</span>gfx1100<span class="w"> </span>-DCMAKE_HIP_PLATFORM<span class="o">=</span>amd<span class="w"> </span>-DCMAKE_CXX_COMPILER<span class="o">=</span>amdclang++<span class="w"> </span>-DCMAKE_C_COMPILER<span class="o">=</span>amdclang<span class="w"> </span>-DCMAKE_HIP_COMPILER<span class="o">=</span>amdclang++<span class="w"> </span>..
</pre></div>
</div>
<p>Now you can build the three variants of the tutorial code:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>cmake<span class="w"> </span>--build<span class="w"> </span>.<span class="w"> </span>--target<span class="w"> </span>hip_graph_api_tutorial_streams<span class="w"> </span>hip_graph_api_tutorial_graph_capture<span class="w"> </span>hip_graph_api_tutorial_graph_creation
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The <code class="docutils literal notranslate"><span class="pre">graph_capture</span></code> variant is currently not supported on Windows and the build target is therefore unavailable.</p>
</div>
</section>
<section id="step-2-examining-the-stream-based-baseline-application">
<h2>Step 2: Examining the stream-based baseline application<a class="headerlink" href="#step-2-examining-the-stream-based-baseline-application" title="Link to this heading">#</a></h2>
<p>Open <code class="docutils literal notranslate"><span class="pre">src/main_streams.hip</span></code> in your editor. You will explore how this application processes data.</p>
<section id="understanding-batched-processing">
<h3>Understanding batched processing<a class="headerlink" href="#understanding-batched-processing" title="Link to this heading">#</a></h3>
<p>The application processes multiple projections simultaneously to maximize GPU utilization.</p>
<section id="determining-parallel-capacity">
<h4>Determining parallel capacity<a class="headerlink" href="#determining-parallel-capacity" title="Link to this heading">#</a></h4>
<p>At the beginning of <code class="docutils literal notranslate"><span class="pre">main()</span></code>, the program queries the GPU for its number of asynchronous engines to determine how
many streams it can create, indicating how many data transfer or compute operations can run in parallel.</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Fetch device properties</span>
<span class="k">auto</span><span class="w"> </span><span class="n">devProps</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipDeviceProp_t</span><span class="p">{};</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipGetDeviceProperties</span><span class="p">(</span><span class="o">&amp;</span><span class="n">devProps</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>

<span class="k">auto</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">numStreams</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">devProps</span><span class="p">.</span><span class="n">asyncEngineCount</span><span class="p">;</span>

<span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Device has &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">numStreams</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; asynchronous engines; preprocessing will use &quot;</span>
<span class="w">          </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">numStreams</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; parallel streams.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="k">auto</span><span class="w"> </span><span class="n">streams</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">hipStream_t</span><span class="o">&gt;</span><span class="p">{};</span>
<span class="n">streams</span><span class="p">.</span><span class="n">resize</span><span class="p">(</span><span class="n">numStreams</span><span class="p">);</span>
<span class="k">for</span><span class="p">(</span><span class="k">auto</span><span class="o">&amp;&amp;</span><span class="w"> </span><span class="n">stream</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">streams</span><span class="p">)</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipStreamCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">stream</span><span class="p">));</span>
</pre></div>
</div>
<div class="admonition tip">
<p class="admonition-title">Tip</p>
<p>Each asynchronous engine executes operations independently. More engines mean more parallelism.</p>
</div>
</section>
<section id="processing-projections-in-batches">
<h4>Processing projections in batches<a class="headerlink" href="#processing-projections-in-batches" title="Link to this heading">#</a></h4>
<p>Find the <code class="docutils literal notranslate"><span class="pre">MAIN</span> <span class="pre">LOOP</span></code> comment. Here the application groups projections into parallel batches:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="k">auto</span><span class="w"> </span><span class="n">projIdx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0u</span><span class="p">;</span>
<span class="k">while</span><span class="p">(</span><span class="n">projIdx</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">numProj</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">auto</span><span class="w"> </span><span class="n">batchSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">min</span><span class="p">(</span><span class="n">numStreams</span><span class="p">,</span><span class="w"> </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="n">projGeom</span><span class="p">.</span><span class="n">numProj</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">projIdx</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Launch batch in parallel streams</span>
<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="k">auto</span><span class="w"> </span><span class="n">streamIdx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">streamIdx</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">batchSize</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">streamIdx</span><span class="p">,</span><span class="w"> </span><span class="o">++</span><span class="n">projIdx</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">auto</span><span class="w"> </span><span class="n">stream</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">streams</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">);</span>
</pre></div>
</div>
<p>Notice how each batch size equals the stream count — this ensures every stream stays busy.</p>
</section>
<section id="synchronization">
<h4>Synchronization<a class="headerlink" href="#synchronization" title="Link to this heading">#</a></h4>
<p>Each projection processes independently, so you only need to synchronize once at the end.
<a class="reference internal" href="../reference/hip_runtime_api/modules/stream_management.html#_CPPv418hipStreamWaitEvent11hipStream_t10hipEvent_tj" title="hipStreamWaitEvent"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamWaitEvent()</span></code></a> function makes the first stream wait for all other streams to complete.</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// First stream waits for other streams to complete</span>
<span class="k">auto</span><span class="w"> </span><span class="n">completionEvents</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">hipEvent_t</span><span class="o">&gt;</span><span class="p">{};</span>
<span class="k">for</span><span class="p">(</span><span class="k">auto</span><span class="w"> </span><span class="n">streamIdx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1u</span><span class="p">;</span><span class="w"> </span><span class="n">streamIdx</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">streams</span><span class="p">.</span><span class="n">size</span><span class="p">();</span><span class="w"> </span><span class="o">++</span><span class="n">streamIdx</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">auto</span><span class="w"> </span><span class="n">event</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipEvent_t</span><span class="p">{};</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipEventCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">event</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipEventRecord</span><span class="p">(</span><span class="n">event</span><span class="p">,</span><span class="w"> </span><span class="n">streams</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">)));</span>
<span class="w">    </span><span class="n">completionEvents</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="n">event</span><span class="p">);</span>
<span class="p">}</span>

<span class="k">for</span><span class="p">(</span><span class="k">auto</span><span class="o">&amp;&amp;</span><span class="w"> </span><span class="n">event</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">completionEvents</span><span class="p">)</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipStreamWaitEvent</span><span class="p">(</span><span class="n">streams</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="mi">0</span><span class="p">),</span><span class="w"> </span><span class="n">event</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
</pre></div>
</div>
</section>
</section>
<section id="exploring-the-processing-pipeline">
<h3>Exploring the processing pipeline<a class="headerlink" href="#exploring-the-processing-pipeline" title="Link to this heading">#</a></h3>
<p>Next, examine what happens to each projection. Find the <code class="docutils literal notranslate"><span class="pre">START</span> <span class="pre">HERE</span></code> comment to see the reconstruction pipeline’s
first steps:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">////////////////////////////////////////////////////////////////////////////////////////////////////</span>
<span class="c1">// START HERE</span>
<span class="c1">////////////////////////////////////////////////////////////////////////////////////////////////////</span>
<span class="k">auto</span><span class="w"> </span><span class="n">proj</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">projections</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">);</span>
<span class="k">auto</span><span class="w"> </span><span class="n">projPitch</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">projectionPitches</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">);</span>
<span class="n">normalization_kernel</span><span class="o">&lt;&lt;&lt;</span><span class="n">blocksPerGrid</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span>
<span class="w">    </span><span class="n">input</span><span class="p">,</span><span class="w"> </span><span class="n">inputPitch</span><span class="p">,</span><span class="w"> </span><span class="n">proj</span><span class="p">,</span><span class="w"> </span><span class="n">projPitch</span><span class="p">,</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">,</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">bps</span>
<span class="p">);</span>

<span class="n">log_transformation_kernel</span><span class="o">&lt;&lt;&lt;</span><span class="n">blocksPerGrid</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">proj</span><span class="p">,</span><span class="w"> </span><span class="n">projPitch</span><span class="p">,</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">);</span>

<span class="n">weighting_kernel</span><span class="o">&lt;&lt;&lt;</span><span class="n">blocksPerGrid</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span>
<span class="w">    </span><span class="n">proj</span><span class="p">,</span>
<span class="w">    </span><span class="n">projPitch</span><span class="p">,</span>
<span class="w">    </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">,</span>
<span class="w">    </span><span class="n">projGeom</span><span class="p">.</span><span class="n">d_sd</span><span class="p">,</span>
<span class="w">    </span><span class="n">projGeom</span><span class="p">.</span><span class="n">d_so</span><span class="p">,</span>
<span class="w">    </span><span class="n">projGeom</span><span class="p">.</span><span class="n">minCoord</span><span class="p">,</span>
<span class="w">    </span><span class="n">projGeom</span><span class="p">.</span><span class="n">pixelDim</span>
<span class="p">);</span>
</pre></div>
</div>
<p>This is a typical pattern found across many HIP applications: multiple kernels executing in sequence with data
dependencies. In the next step, the weighted projections need to be transformed into Fourier space and filtered. For
optimal performance, it is recommended to execute a 1D FFT on a buffer size which is a power of two. Copy the weighted
projection to another buffer where the row length is a power of two equal to or larger than the projection’s row
length:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Expand projection to filter length</span>
<span class="k">auto</span><span class="w"> </span><span class="n">expanded</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">expandedProjections</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">);</span>
<span class="k">auto</span><span class="w"> </span><span class="n">expandedPitch</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">expandedPitches</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">);</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemset2DAsync</span><span class="p">(</span>
<span class="w">    </span><span class="n">expanded</span><span class="p">,</span><span class="w"> </span><span class="n">expandedPitch</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dimFFT</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">),</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dimFFT</span><span class="p">.</span><span class="n">y</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span>
<span class="p">));</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy2DAsync</span><span class="p">(</span>
<span class="w">    </span><span class="n">expanded</span><span class="p">,</span>
<span class="w">    </span><span class="n">expandedPitch</span><span class="p">,</span>
<span class="w">    </span><span class="n">proj</span><span class="p">,</span>
<span class="w">    </span><span class="n">projPitch</span><span class="p">,</span>
<span class="w">    </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">),</span>
<span class="w">    </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">.</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="n">hipMemcpyDeviceToDevice</span><span class="p">,</span>
<span class="w">    </span><span class="n">stream</span>
<span class="p">));</span>
</pre></div>
</div>
<p>Next, transform the expanded projection into Fourier space for filtering:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// R2C Fourier-transform projection</span>
<span class="k">auto</span><span class="w"> </span><span class="n">transformed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">transformedProjections</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">);</span>
<span class="k">auto</span><span class="w"> </span><span class="n">transformedPitch</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">transformedPitches</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">);</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemset2DAsync</span><span class="p">(</span>
<span class="w">    </span><span class="n">transformed</span><span class="p">,</span>
<span class="w">    </span><span class="n">transformedPitch</span><span class="p">,</span>
<span class="w">    </span><span class="mi">0</span><span class="p">,</span>
<span class="w">    </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dimTrans</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">hipfftComplex</span><span class="p">),</span>
<span class="w">    </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dimTrans</span><span class="p">.</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="n">stream</span>
<span class="p">));</span>
<span class="k">auto</span><span class="o">&amp;</span><span class="w"> </span><span class="n">forward</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">forwardPlans</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">);</span>
<span class="n">hipfft_check</span><span class="p">(</span><span class="n">hipfftExecR2C</span><span class="p">(</span><span class="n">forward</span><span class="p">,</span><span class="w"> </span><span class="n">expanded</span><span class="p">,</span><span class="w"> </span><span class="n">transformed</span><span class="p">));</span>
</pre></div>
</div>
<div class="admonition tip">
<p class="admonition-title">Tip</p>
<p>Some hipFFT operations are graph-safe: As long as these operations are operating on the capturing stream, they will
be captured into the graph as well. Refer to <a class="reference external" href="https://rocm.docs.amd.com/projects/hipFFT/en/latest/reference/hipfft-api-usage.html#hipfft-api-usage" title="(in hipFFT Documentation v1.0.22)"><span class="xref std std-ref">hipFFT’s documentation</span></a> for more
information on its graph-safe operations.</p>
</div>
<p>In Fourier space, apply the Shepp-Logan filter, then transform back:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Apply filter</span>
<span class="k">auto</span><span class="w"> </span><span class="n">filterBlocksPerGrid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="kt">dim3</span><span class="p">{</span>
<span class="w">    </span><span class="p">(</span><span class="n">projGeom</span><span class="p">.</span><span class="n">dimTrans</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">.</span><span class="n">x</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
<span class="w">    </span><span class="p">(</span><span class="n">projGeom</span><span class="p">.</span><span class="n">dimTrans</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">.</span><span class="n">y</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
<span class="w">    </span><span class="mi">1</span>
<span class="p">};</span>
<span class="n">filter_application_kernel</span><span class="o">&lt;&lt;&lt;</span><span class="n">filterBlocksPerGrid</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span>
<span class="w">    </span><span class="n">transformed</span><span class="p">,</span><span class="w"> </span><span class="n">transformedPitch</span><span class="p">,</span><span class="w"> </span><span class="n">R</span><span class="p">,</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dimTrans</span>
<span class="p">);</span>

<span class="k">auto</span><span class="o">&amp;</span><span class="w"> </span><span class="n">backward</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">backwardPlans</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">);</span>
<span class="n">hipfft_check</span><span class="p">(</span><span class="n">hipfftExecC2R</span><span class="p">(</span><span class="n">backward</span><span class="p">,</span><span class="w"> </span><span class="n">transformed</span><span class="p">,</span><span class="w"> </span><span class="n">expanded</span><span class="p">));</span>
</pre></div>
</div>
<p>Shrink to original size and normalize the FFT output:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Shrink projection to original size and normalize</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy2DAsync</span><span class="p">(</span>
<span class="w">    </span><span class="n">proj</span><span class="p">,</span>
<span class="w">    </span><span class="n">projPitch</span><span class="p">,</span>
<span class="w">    </span><span class="n">expanded</span><span class="p">,</span>
<span class="w">    </span><span class="n">expandedPitch</span><span class="p">,</span>
<span class="w">    </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">),</span>
<span class="w">    </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">.</span><span class="n">y</span><span class="p">,</span>
<span class="w">    </span><span class="n">hipMemcpyDeviceToDevice</span><span class="p">,</span>
<span class="w">    </span><span class="n">stream</span>
<span class="p">));</span>

<span class="n">filter_normalization_kernel</span><span class="o">&lt;&lt;&lt;</span><span class="n">blocksPerGrid</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span>
<span class="w">    </span><span class="n">proj</span><span class="p">,</span><span class="w"> </span><span class="n">projPitch</span><span class="p">,</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dimFFT</span><span class="p">.</span><span class="n">x</span><span class="p">,</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dim</span>
<span class="p">);</span>
</pre></div>
</div>
<p>Finally, back-project the filtered projection into the 3D volume using <code class="docutils literal notranslate"><span class="pre">atomicAdd</span></code> operations to accumulate voxel
values from multiple kernels:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Backprojection</span>
<span class="k">auto</span><span class="w"> </span><span class="n">thetaDeg</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">thetaSign</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">thetaStep</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">projIdx</span><span class="p">;</span><span class="w"> </span><span class="c1">// Current angle</span>
<span class="k">auto</span><span class="w"> </span><span class="n">thetaRad</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">thetaDeg</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">numbers</span><span class="o">::</span><span class="n">pi_v</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mf">180.f</span><span class="p">;</span><span class="w"> </span><span class="c1">// Convert to radians</span>
<span class="k">auto</span><span class="w"> </span><span class="n">sinTheta</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">sin</span><span class="p">(</span><span class="n">thetaRad</span><span class="p">);</span>
<span class="k">auto</span><span class="w"> </span><span class="n">cosTheta</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">cos</span><span class="p">(</span><span class="n">thetaRad</span><span class="p">);</span>

<span class="k">auto</span><span class="w"> </span><span class="n">bpBlockSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="kt">dim3</span><span class="p">{</span><span class="mi">32u</span><span class="p">,</span><span class="w"> </span><span class="mi">8u</span><span class="p">,</span><span class="w"> </span><span class="mi">4u</span><span class="p">};</span>
<span class="k">auto</span><span class="w"> </span><span class="n">bpBlocks</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="kt">dim3</span><span class="p">{</span>
<span class="w">    </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="o">&gt;</span><span class="p">(</span><span class="n">volGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">bpBlockSize</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="p">),</span>
<span class="w">    </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="o">&gt;</span><span class="p">(</span><span class="n">volGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">bpBlockSize</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="p">),</span>
<span class="w">    </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="o">&gt;</span><span class="p">(</span><span class="n">volGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">.</span><span class="n">z</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">bpBlockSize</span><span class="p">.</span><span class="n">z</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="p">)</span>
<span class="p">};</span>

<span class="k">if</span><span class="p">(</span><span class="n">hasTextures</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">auto</span><span class="o">&amp;</span><span class="w"> </span><span class="n">projTex</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">textureProjections</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">);</span>
<span class="w">    </span><span class="n">backprojection_kernel</span><span class="o">&lt;&lt;&lt;</span><span class="n">bpBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">bpBlockSize</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span>
<span class="w">        </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">*&gt;</span><span class="p">(</span><span class="n">vol</span><span class="p">.</span><span class="n">ptr</span><span class="p">),</span>
<span class="w">        </span><span class="n">vol</span><span class="p">.</span><span class="n">pitch</span><span class="p">,</span>
<span class="w">        </span><span class="n">volGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">,</span>
<span class="w">        </span><span class="n">volGeom</span><span class="p">.</span><span class="n">voxelDim</span><span class="p">,</span>
<span class="w">        </span><span class="n">projTex</span><span class="p">,</span>
<span class="w">        </span><span class="n">projGeom</span><span class="p">.</span><span class="n">minCoord</span><span class="p">,</span>
<span class="w">        </span><span class="n">sinTheta</span><span class="p">,</span>
<span class="w">        </span><span class="n">cosTheta</span><span class="p">,</span>
<span class="w">        </span><span class="n">projGeom</span><span class="p">.</span><span class="n">pixelDim</span><span class="p">,</span>
<span class="w">        </span><span class="n">projGeom</span><span class="p">.</span><span class="n">d_sd</span><span class="p">,</span>
<span class="w">        </span><span class="n">projGeom</span><span class="p">.</span><span class="n">d_so</span>
<span class="w">    </span><span class="p">);</span>
<span class="p">}</span>
<span class="k">else</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// Fallback for devices without support for texture instructions</span>
<span class="w">    </span><span class="n">backprojection_kernel_no_tex</span><span class="o">&lt;&lt;&lt;</span><span class="n">bpBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">bpBlockSize</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span>
<span class="w">        </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">*&gt;</span><span class="p">(</span><span class="n">vol</span><span class="p">.</span><span class="n">ptr</span><span class="p">),</span>
<span class="w">        </span><span class="n">vol</span><span class="p">.</span><span class="n">pitch</span><span class="p">,</span>
<span class="w">        </span><span class="n">volGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">,</span>
<span class="w">        </span><span class="n">volGeom</span><span class="p">.</span><span class="n">voxelDim</span><span class="p">,</span>
<span class="w">        </span><span class="n">proj</span><span class="p">,</span>
<span class="w">        </span><span class="n">projPitch</span><span class="p">,</span>
<span class="w">        </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">,</span>
<span class="w">        </span><span class="n">projGeom</span><span class="p">.</span><span class="n">minCoord</span><span class="p">,</span>
<span class="w">        </span><span class="n">sinTheta</span><span class="p">,</span>
<span class="w">        </span><span class="n">cosTheta</span><span class="p">,</span>
<span class="w">        </span><span class="n">projGeom</span><span class="p">.</span><span class="n">pixelDim</span><span class="p">,</span>
<span class="w">        </span><span class="n">projGeom</span><span class="p">.</span><span class="n">d_sd</span><span class="p">,</span>
<span class="w">        </span><span class="n">projGeom</span><span class="p">.</span><span class="n">d_so</span>
<span class="w">    </span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The preprocessing kernels process 512 × 512 pixels (<span class="math notranslate nohighlight">\(\mathcal{O}(n²)\)</span>), while the back-projection kernel
processes 512 × 512 × 512 voxels (<span class="math notranslate nohighlight">\(\mathcal{O}(n³)\)</span>). This cubic complexity makes back-projection the
computational bottleneck.</p>
</div>
<section id="creating-a-trace-file">
<h4>Creating a trace file<a class="headerlink" href="#creating-a-trace-file" title="Link to this heading">#</a></h4>
<p>Inside the <code class="docutils literal notranslate"><span class="pre">build</span></code> directory you will now generate a trace:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>rocprofv3<span class="w"> </span>-o<span class="w"> </span>streams<span class="w"> </span>-d<span class="w"> </span>outDir<span class="w"> </span>-f<span class="w"> </span>pftrace<span class="w"> </span>--hip-trace<span class="w"> </span>--kernel-trace<span class="w"> </span>--memory-copy-trace<span class="w"> </span>--memory-allocation-trace<span class="w"> </span>--<span class="w"> </span>./bin/hip_graph_api_tutorial_streams
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>For more information on the <code class="docutils literal notranslate"><span class="pre">rocprofv3</span></code> tool, please refer to its
<a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3.html#using-rocprofv3" title="(in Rocprofiler SDK v1.1.0)"><span class="xref std std-ref">documentation</span></a>.</p>
</div>
</section>
<section id="analyzing-the-trace">
<h4>Analyzing the trace<a class="headerlink" href="#analyzing-the-trace" title="Link to this heading">#</a></h4>
<p>Open the trace file to see what is really happening:</p>
<ol class="arabic simple">
<li><p>Navigate to your <code class="docutils literal notranslate"><span class="pre">build/outDir</span></code> directory</p></li>
<li><p>Open <code class="docutils literal notranslate"><span class="pre">streams_results.pftrace</span></code> in <a class="reference external" href="https://ui.perfetto.dev">Perfetto</a></p></li>
<li><p>Click the arrow next to your executable name under <code class="docutils literal notranslate"><span class="pre">System</span></code></p></li>
<li><p>Focus on the kernel execution pattern on the right</p></li>
</ol>
<figure class="align-center">
<img alt="Stream execution showing gaps between kernel launches" src="../_images/streams_trace.png" />
</figure>
<p>While projections process in parallel, there are visible gaps between operations. These gaps represent overhead caused
by scheduling and launching the operations. In the next section, you will eliminate these gaps by capturing streams into
a graph.</p>
</section>
</section>
</section>
<section id="step-3-converting-to-graphs-via-stream-capture">
<h2>Step 3: Converting to graphs via stream capture<a class="headerlink" href="#step-3-converting-to-graphs-via-stream-capture" title="Link to this heading">#</a></h2>
<p>Stream capture is a feature that allows you to record a sequence of GPU operations (kernel launches, memory copies,
etc.) into a HIP Graph, which can later be executed as a single, optimized unit. Open the file
<code class="docutils literal notranslate"><span class="pre">src/main_graph_capture.hip</span></code>, which contains the code from the previous subsection, with a few changes that allow you
to capture the streams into a single graph.</p>
<p>Before the main loop, declare graph-specific variables:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="k">auto</span><span class="w"> </span><span class="n">graphCreated</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">false</span><span class="p">;</span>
<span class="k">auto</span><span class="w"> </span><span class="n">graphExec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipGraphExec_t</span><span class="p">{};</span>
<span class="k">auto</span><span class="w"> </span><span class="n">graphFinalCreated</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">false</span><span class="p">;</span>
<span class="k">auto</span><span class="w"> </span><span class="n">graphExecFinal</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipGraphExec_t</span><span class="p">{};</span>
<span class="k">auto</span><span class="w"> </span><span class="n">graphStream</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipStream_t</span><span class="p">{};</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipStreamCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">graphStream</span><span class="p">));</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">graphExec</span></code> and <code class="docutils literal notranslate"><span class="pre">graphExecFinal</span></code> will be instances of the graph template that you will create in the following
steps. You will typically instantiate a graph template once and update its parameters for repeated launches. If the
graph topology changes, you will need a new instance. The <code class="docutils literal notranslate"><span class="pre">graphStream</span></code> will launch the final graph instances.</p>
<p>Inside the main loop, activate capture mode on the first stream:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Capture the current batch into a graph template</span>
<span class="k">auto</span><span class="w"> </span><span class="n">graph</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipGraph_t</span><span class="p">{};</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipStreamBeginCapture</span><span class="p">(</span><span class="n">streams</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="mi">0</span><span class="p">),</span><span class="w"> </span><span class="n">hipStreamCaptureModeGlobal</span><span class="p">));</span>
</pre></div>
</div>
<div class="admonition-what-happens-during-capture admonition">
<p class="admonition-title">What happens during capture?</p>
<p>When <a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv421hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode" title="hipStreamBeginCapture"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamBeginCapture()</span></code></a> is called, the stream stops executing operations immediately. Instead, it
records operations into a graph template (<code class="docutils literal notranslate"><span class="pre">graph</span></code> in the code shown here).</p>
</div>
<p>To capture multiple streams, use events to implement the fork-join pattern:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Fork: Record events on stream 0, then have other streams wait</span>
<span class="k">for</span><span class="p">(</span><span class="k">auto</span><span class="w"> </span><span class="n">streamIdx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span><span class="w"> </span><span class="n">streamIdx</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">batchSize</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">streamIdx</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">auto</span><span class="w"> </span><span class="n">forkEvent</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipEvent_t</span><span class="p">{};</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipEventCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">forkEvent</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipEventRecord</span><span class="p">(</span><span class="n">forkEvent</span><span class="p">,</span><span class="w"> </span><span class="n">streams</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="mi">0</span><span class="p">)));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipStreamWaitEvent</span><span class="p">(</span><span class="n">streams</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">),</span><span class="w"> </span><span class="n">forkEvent</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipEventDestroy</span><span class="p">(</span><span class="n">forkEvent</span><span class="p">));</span><span class="w"> </span><span class="c1">// Can destroy after wait is recorded</span>
<span class="p">}</span>
</pre></div>
</div>
<p>This creates dependencies between streams, activating capture mode on the additional streams and ensuring they are all
part of the same graph.</p>
<p><strong>The processing pipeline itself remains unchanged.</strong></p>
<p>After recording all operations of the current batch, join the streams:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Join: Record events on all streams except stream 0, then have stream 0 wait</span>
<span class="k">for</span><span class="p">(</span><span class="k">auto</span><span class="w"> </span><span class="n">streamIdx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span><span class="w"> </span><span class="n">streamIdx</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">batchSize</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">streamIdx</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">auto</span><span class="w"> </span><span class="n">joinEvent</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipEvent_t</span><span class="p">{};</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipEventCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">joinEvent</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipEventRecord</span><span class="p">(</span><span class="n">joinEvent</span><span class="p">,</span><span class="w"> </span><span class="n">streams</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">streamIdx</span><span class="p">)));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipStreamWaitEvent</span><span class="p">(</span><span class="n">streams</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="mi">0</span><span class="p">),</span><span class="w"> </span><span class="n">joinEvent</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipEventDestroy</span><span class="p">(</span><span class="n">joinEvent</span><span class="p">));</span><span class="w"> </span><span class="c1">// Can destroy after wait is recorded</span>
<span class="p">}</span>
</pre></div>
</div>
<p>Then stop capturing:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Stop capturing -- this will stop capturing on all streams</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipStreamEndCapture</span><span class="p">(</span><span class="n">streams</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="mi">0</span><span class="p">),</span><span class="w"> </span><span class="o">&amp;</span><span class="n">graph</span><span class="p">));</span>
</pre></div>
</div>
<p>The graph template is now complete. In order to execute the recorded operations, you need to instantiate the graph
and execute it on the <code class="docutils literal notranslate"><span class="pre">graphStream</span></code>. The graph template can be safely destroyed after instantiating:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="k">if</span><span class="p">(</span><span class="o">!</span><span class="n">graphCreated</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphDebugDotPrint</span><span class="p">(</span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;graph_capture.dot&quot;</span><span class="p">,</span><span class="w"> </span><span class="n">hipGraphDebugDotFlagsVerbose</span><span class="p">));</span>

<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphInstantiate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">graphExec</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="n">nullptr</span><span class="p">,</span><span class="w"> </span><span class="n">nullptr</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphDestroy</span><span class="p">(</span><span class="n">graph</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphLaunch</span><span class="p">(</span><span class="n">graphExec</span><span class="p">,</span><span class="w"> </span><span class="n">graphStream</span><span class="p">));</span>
<span class="w">    </span><span class="n">graphCreated</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">true</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<div class="admonition tip">
<p class="admonition-title">Tip</p>
<p>Use <a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv421hipGraphDebugDotPrint10hipGraph_tPKcj" title="hipGraphDebugDotPrint"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphDebugDotPrint()</span></code></a> to save a graph’s topology into a <code class="docutils literal notranslate"><span class="pre">*.dot</span></code> file. The resulting file
contains a <a class="reference external" href="https://graphviz.org/doc/info/lang.html">DOT</a> description which can be processed with
<a class="reference external" href="https://graphviz.org/">Graphviz</a> or visualized with several tools. For example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>dot<span class="w"> </span>-Tpng<span class="w"> </span>graph_capture.dot<span class="w"> </span>-o<span class="w"> </span>graph_capture.png
</pre></div>
</div>
</div>
<p>Instantiating a graph is a relatively costly operation. However, you need to update the parameters whenever a new batch
is processed. Since the graph templates are the same for all batches (i.e., the topology of the resulting graph does
not change), it is sufficient to update the existing graph instance’s parameters instead of creating a new instance:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="k">else</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// Update existing executable graph after each iteration with new input data</span>
<span class="w">    </span><span class="k">auto</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipGraphExecUpdateResult</span><span class="p">{};</span>
<span class="w">    </span><span class="k">auto</span><span class="w"> </span><span class="n">errorNode</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipGraphNode_t</span><span class="p">{};</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphExecUpdate</span><span class="p">(</span><span class="n">graphExec</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">errorNode</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">result</span><span class="p">));</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">result</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipGraphExecUpdateSuccess</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">auto</span><span class="w"> </span><span class="n">msg</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="p">{</span><span class="s">&quot;Failed to update graph: &quot;</span><span class="p">};</span>
<span class="w">        </span><span class="k">switch</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="k">case</span><span class="w"> </span><span class="no">hipGraphExecUpdateError</span><span class="p">:</span>
<span class="w">            </span><span class="n">msg</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="s">&quot;Invalid value.&quot;</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="k">case</span><span class="w"> </span><span class="no">hipGraphExecUpdateErrorFunctionChanged</span><span class="p">:</span>
<span class="w">            </span><span class="n">msg</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="s">&quot;Function of kernel node changed.&quot;</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="k">case</span><span class="w"> </span><span class="no">hipGraphExecUpdateErrorNodeTypeChanged</span><span class="p">:</span>
<span class="w">            </span><span class="n">msg</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="s">&quot;Type of node changed.&quot;</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="k">case</span><span class="w"> </span><span class="no">hipGraphExecUpdateErrorNotSupported</span><span class="p">:</span>
<span class="w">            </span><span class="n">msg</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="s">&quot;Something about the node is not supported.&quot;</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="k">case</span><span class="w"> </span><span class="no">hipGraphExecUpdateErrorParametersChanged</span><span class="p">:</span>
<span class="w">            </span><span class="n">msg</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="s">&quot;Unsupported parameter change.&quot;</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="k">case</span><span class="w"> </span><span class="no">hipGraphExecUpdateErrorTopologyChanged</span><span class="p">:</span>
<span class="w">            </span><span class="n">msg</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="s">&quot;Graph topology changed.&quot;</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="k">case</span><span class="w"> </span><span class="no">hipGraphExecUpdateErrorUnsupportedFunctionChange</span><span class="p">:</span>
<span class="w">            </span><span class="n">msg</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="s">&quot;Unsupported change of kernel node function.&quot;</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="k">default</span><span class="o">:</span>
<span class="w">            </span><span class="n">msg</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="s">&quot;Unknown error.&quot;</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="n">throw</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">runtime_error</span><span class="p">{</span><span class="n">msg</span><span class="p">};</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphDestroy</span><span class="p">(</span><span class="n">graph</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphLaunch</span><span class="p">(</span><span class="n">graphExec</span><span class="p">,</span><span class="w"> </span><span class="n">graphStream</span><span class="p">));</span>
<span class="p">}</span>
</pre></div>
</div>
<p>Should the graph’s topology change between iterations, it is necessary to create a new graph instance. In your
application’s case, this can happen when the number of projections is not evenly divisible by the number of
asynchronous engines:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphDebugDotPrint</span><span class="p">(</span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;graph_capture_final.dot&quot;</span><span class="p">,</span><span class="w"> </span><span class="n">hipGraphDebugDotFlagsVerbose</span><span class="p">));</span>

<span class="c1">// Incomplete batch: topology changed, must instantiate new executable graph</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphInstantiate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">graphExecFinal</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="n">nullptr</span><span class="p">,</span><span class="w"> </span><span class="n">nullptr</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphDestroy</span><span class="p">(</span><span class="n">graph</span><span class="p">));</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphLaunch</span><span class="p">(</span><span class="n">graphExecFinal</span><span class="p">,</span><span class="w"> </span><span class="n">graphStream</span><span class="p">));</span>
</pre></div>
</div>
<section id="creating-a-trace">
<h3>Creating a trace<a class="headerlink" href="#creating-a-trace" title="Link to this heading">#</a></h3>
<p>Now you have successfully converted the processing pipeline into an executable graph. You can examine the effects of
this change and generate another trace:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>rocprofv3<span class="w"> </span>-o<span class="w"> </span>graph_capture<span class="w"> </span>-d<span class="w"> </span>outDir<span class="w"> </span>-f<span class="w"> </span>pftrace<span class="w"> </span>--hip-trace<span class="w"> </span>--kernel-trace<span class="w"> </span>--memory-copy-trace<span class="w"> </span>--memory-allocation-trace<span class="w"> </span>--<span class="w"> </span>./bin/hip_graph_api_tutorial_graph_capture
</pre></div>
</div>
</section>
<section id="id4">
<h3>Analyzing the trace<a class="headerlink" href="#id4" title="Link to this heading">#</a></h3>
<p>Opening the resulting trace file <code class="docutils literal notranslate"><span class="pre">outDir/graph_capture_results.pftrace</span></code> with Perfetto shows a significant change:</p>
<figure class="align-center">
<img alt="Diagram showing a trace of the capturing variant." src="../_images/capture_trace.png" />
</figure>
<p>The gaps have disappeared! By capturing all operations of a batch into a single graph, you have successfully
eliminated the launching and scheduling overhead previously observed in the stream-based variant.</p>
<p>A limitation of stream capture is that it preserves stream ordering even when unnecessary. Operations that could run in
parallel still execute sequentially. Another approach to graphs is manual construction. This is quite verbose but also
offers much more control over dependencies and parallelism.</p>
</section>
</section>
<section id="step-4-manual-graph-creation-advanced">
<h2>Step 4: Manual graph creation (advanced)<a class="headerlink" href="#step-4-manual-graph-creation-advanced" title="Link to this heading">#</a></h2>
<p>Open <code class="docutils literal notranslate"><span class="pre">src/main_graph_creation.hip</span></code> and find the main loop. The code here differs from the other variants: rather than
capturing streams into graphs, you will build the graph manually. Consider how the weighting kernel is invoked through
a kernel node:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">weightingKernelParams</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">proj</span><span class="p">),</span>
<span class="w">    </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">projPitch</span><span class="p">),</span>
<span class="w">    </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">projGeom</span><span class="p">.</span><span class="n">dim</span><span class="p">),</span>
<span class="w">    </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">projGeom</span><span class="p">.</span><span class="n">d_sd</span><span class="p">),</span>
<span class="w">    </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">projGeom</span><span class="p">.</span><span class="n">d_so</span><span class="p">),</span>
<span class="w">    </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">projGeom</span><span class="p">.</span><span class="n">minCoord</span><span class="p">),</span>
<span class="w">    </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">projGeom</span><span class="p">.</span><span class="n">pixelDim</span><span class="p">)</span>
<span class="p">};</span>
<span class="k">auto</span><span class="w"> </span><span class="n">weightingKernelNodeParams</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipKernelNodeParams</span><span class="p">{};</span>
<span class="n">weightingKernelNodeParams</span><span class="p">.</span><span class="nb">blockDim</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">;</span>
<span class="n">weightingKernelNodeParams</span><span class="p">.</span><span class="n">extra</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">nullptr</span><span class="p">;</span>
<span class="n">weightingKernelNodeParams</span><span class="p">.</span><span class="n">func</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">reinterpret_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="n">weighting_kernel</span><span class="p">);</span>
<span class="n">weightingKernelNodeParams</span><span class="p">.</span><span class="nb">gridDim</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blocksPerGrid</span><span class="p">;</span>
<span class="n">weightingKernelNodeParams</span><span class="p">.</span><span class="n">kernelParams</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">weightingKernelParams</span><span class="p">;</span>
<span class="n">weightingKernelNodeParams</span><span class="p">.</span><span class="n">sharedMemBytes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="k">auto</span><span class="w"> </span><span class="n">weightingKernelNode</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipGraphNode_t</span><span class="p">{};</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphAddKernelNode</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">weightingKernelNode</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">logTransformationKernelNode</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">weightingKernelNodeParams</span>
<span class="p">));</span>
</pre></div>
</div>
<p>You create an array of <code class="docutils literal notranslate"><span class="pre">void*</span></code> pointers containing the kernel parameters. Next, configure the kernel launch
parameters: grid and block dimensions, the kernel function pointer, and the dynamic shared memory size. Finally, add
the kernel node to the graph template. Note the <code class="docutils literal notranslate"><span class="pre">&amp;logTransformationKernelNode,</span> <span class="pre">1</span></code> part: this is how you specify a
dependency from the preceding log transformation kernel node to the weighting kernel node.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>For specifying multiple dependencies, you would pass an array of <code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipGraphNode_t</span></code> objects and the number of
nodes inside the array to <a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv421hipGraphAddKernelNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK19hipKernelNodeParams" title="hipGraphAddKernelNode"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphAddKernelNode()</span></code></a>.</p>
</div>
<p>The HIP graph API supports multiple different node types. For example, this is how a <code class="docutils literal notranslate"><span class="pre">memset</span></code> node is set up:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="k">auto</span><span class="w"> </span><span class="n">expandedMemsetNodeParams</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemsetParams</span><span class="p">{};</span>
<span class="n">expandedMemsetNodeParams</span><span class="p">.</span><span class="n">dst</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">static_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="n">expanded</span><span class="p">);</span>
<span class="n">expandedMemsetNodeParams</span><span class="p">.</span><span class="n">elementSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">);</span>
<span class="n">expandedMemsetNodeParams</span><span class="p">.</span><span class="n">height</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dimFFT</span><span class="p">.</span><span class="n">y</span><span class="p">;</span>
<span class="n">expandedMemsetNodeParams</span><span class="p">.</span><span class="n">pitch</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">expandedPitch</span><span class="p">;</span>
<span class="n">expandedMemsetNodeParams</span><span class="p">.</span><span class="n">value</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="n">expandedMemsetNodeParams</span><span class="p">.</span><span class="n">width</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">projGeom</span><span class="p">.</span><span class="n">dimFFT</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="k">auto</span><span class="w"> </span><span class="n">expandedMemsetNode</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipGraphNode_t</span><span class="p">{};</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphAddMemsetNode</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">expandedMemsetNode</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">weightingKernelNode</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">expandedMemsetNodeParams</span>
<span class="p">));</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Despite the different construction method, graph instantiation and updates
work exactly as before. You can find the same patterns at the loop’s end.</p>
</div>
<section id="adding-hipfft-nodes">
<h3>Adding hipFFT nodes<a class="headerlink" href="#adding-hipfft-nodes" title="Link to this heading">#</a></h3>
<p>While hipFFT provides graph-safe functionality, it does not support manual node creation. Integrating hipFFT into the
graph requires a workaround using stream capture with additional bookkeeping.</p>
<p>You capture the graph state before and after hipFFT operations, then identify the nodes hipFFT added:</p>
<section id="step-1-save-existing-nodes">
<h4>Step 1: Save existing nodes<a class="headerlink" href="#step-1-save-existing-nodes" title="Link to this heading">#</a></h4>
<p>Record all current graph nodes in a sorted <code class="docutils literal notranslate"><span class="pre">std::set</span></code>:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Before capturing the FFT operations, obtain the set of nodes already present in the graph</span>
<span class="k">auto</span><span class="w"> </span><span class="n">nodesBeforeForward</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">hipGraphNode_t</span><span class="o">&gt;</span><span class="p">{};</span>
<span class="k">auto</span><span class="w"> </span><span class="n">numNodesBeforeForward</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="p">{};</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphGetNodes</span><span class="p">(</span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="n">nullptr</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">numNodesBeforeForward</span><span class="p">));</span>
<span class="n">nodesBeforeForward</span><span class="p">.</span><span class="n">resize</span><span class="p">(</span><span class="n">numNodesBeforeForward</span><span class="p">);</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphGetNodes</span><span class="p">(</span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="n">nodesBeforeForward</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="o">&amp;</span><span class="n">numNodesBeforeForward</span><span class="p">));</span>
<span class="k">auto</span><span class="w"> </span><span class="n">nodesBeforeForwardSorted</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">set</span><span class="o">&lt;</span><span class="n">hipGraphNode_t</span><span class="o">&gt;</span><span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">begin</span><span class="p">(</span><span class="n">nodesBeforeForward</span><span class="p">),</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">end</span><span class="p">(</span><span class="n">nodesBeforeForward</span><span class="p">)</span>
<span class="p">};</span>
</pre></div>
</div>
</section>
<section id="step-2-capture-hipfft-operations">
<h4>Step 2: Capture hipFFT operations<a class="headerlink" href="#step-2-capture-hipfft-operations" title="Link to this heading">#</a></h4>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipStreamBeginCaptureToGraph</span><span class="p">(</span>
<span class="w">    </span><span class="n">stream</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">transformedMemsetNode</span><span class="p">,</span><span class="w"> </span><span class="n">nullptr</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">hipStreamCaptureModeGlobal</span><span class="p">));</span>

<span class="k">auto</span><span class="o">&amp;</span><span class="w"> </span><span class="n">forward</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">forwardPlans</span><span class="p">.</span><span class="n">at</span><span class="p">(</span><span class="n">branchIdx</span><span class="p">);</span>
<span class="n">hipfft_check</span><span class="p">(</span><span class="n">hipfftExecR2C</span><span class="p">(</span><span class="n">forward</span><span class="p">,</span><span class="w"> </span><span class="n">expanded</span><span class="p">,</span><span class="w"> </span><span class="n">transformed</span><span class="p">));</span>

<span class="n">hip_check</span><span class="p">(</span><span class="n">hipStreamEndCapture</span><span class="p">(</span><span class="n">stream</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">graph</span><span class="p">));</span>
</pre></div>
</div>
</section>
<section id="step-3-get-updated-node-list">
<h4>Step 3: Get updated node list<a class="headerlink" href="#step-3-get-updated-node-list" title="Link to this heading">#</a></h4>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Obtain nodes in graph again, the new nodes will be our dependencies for the next step</span>
<span class="k">auto</span><span class="w"> </span><span class="n">nodesAfterForward</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">hipGraphNode_t</span><span class="o">&gt;</span><span class="p">{};</span>
<span class="k">auto</span><span class="w"> </span><span class="n">numNodesAfterForward</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="p">{};</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphGetNodes</span><span class="p">(</span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="n">nullptr</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">numNodesAfterForward</span><span class="p">));</span>
<span class="n">nodesAfterForward</span><span class="p">.</span><span class="n">resize</span><span class="p">(</span><span class="n">numNodesAfterForward</span><span class="p">);</span>
<span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphGetNodes</span><span class="p">(</span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="n">nodesAfterForward</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="o">&amp;</span><span class="n">numNodesAfterForward</span><span class="p">));</span>
<span class="k">auto</span><span class="w"> </span><span class="n">nodesAfterForwardSorted</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">set</span><span class="o">&lt;</span><span class="n">hipGraphNode_t</span><span class="o">&gt;</span><span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">begin</span><span class="p">(</span><span class="n">nodesAfterForward</span><span class="p">),</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">end</span><span class="p">(</span><span class="n">nodesAfterForward</span><span class="p">)</span>
<span class="p">};</span>
</pre></div>
</div>
</section>
<section id="step-4-find-new-nodes">
<h4>Step 4: Find new nodes<a class="headerlink" href="#step-4-find-new-nodes" title="Link to this heading">#</a></h4>
<p>Compute the difference between both node sets:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Compute difference between both sets</span>
<span class="k">auto</span><span class="w"> </span><span class="n">forwardFFTNodes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">hipGraphNode_t</span><span class="o">&gt;</span><span class="p">{};</span>
<span class="n">std</span><span class="o">::</span><span class="n">set_difference</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">begin</span><span class="p">(</span><span class="n">nodesAfterForwardSorted</span><span class="p">),</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">end</span><span class="p">(</span><span class="n">nodesAfterForwardSorted</span><span class="p">),</span>
<span class="w">                    </span><span class="n">std</span><span class="o">::</span><span class="n">begin</span><span class="p">(</span><span class="n">nodesBeforeForwardSorted</span><span class="p">),</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">end</span><span class="p">(</span><span class="n">nodesBeforeForwardSorted</span><span class="p">),</span>
<span class="w">                    </span><span class="n">std</span><span class="o">::</span><span class="n">back_inserter</span><span class="p">(</span><span class="n">forwardFFTNodes</span><span class="p">));</span>
</pre></div>
</div>
</section>
<section id="step-5-identify-the-leaf-node">
<h4>Step 5: Identify the leaf node<a class="headerlink" href="#step-5-identify-the-leaf-node" title="Link to this heading">#</a></h4>
<p>Find hipFFT’s final node for dependency tracking:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Find leaf node in difference set</span>
<span class="k">auto</span><span class="w"> </span><span class="n">forwardLeafNode</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">*</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">find_if</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">begin</span><span class="p">(</span><span class="n">forwardFFTNodes</span><span class="p">),</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">end</span><span class="p">(</span><span class="n">forwardFFTNodes</span><span class="p">),</span><span class="w"> </span><span class="n">is_leaf</span><span class="p">));</span>
</pre></div>
</div>
<p>The leaf detection logic checks if a node has no outgoing edges:</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="k">auto</span><span class="w"> </span><span class="n">is_leaf</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[](</span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">node</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">auto</span><span class="w"> </span><span class="n">numDependentNodes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="p">{};</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipGraphNodeGetDependentNodes</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="w"> </span><span class="n">nullptr</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">numDependentNodes</span><span class="p">));</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">numDependentNodes</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">};</span>
</pre></div>
</div>
<p>With hipFFT integrated and its leaf node identified, subsequent nodes can establish proper dependencies.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>You can also capture hipFFT operations into a separate graph template, then add it to the main graph as a child graph
using <a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv425hipGraphAddChildGraphNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipGraph_t" title="hipGraphAddChildGraphNode"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphAddChildGraphNode()</span></code></a>. The approach above adds hipFFT nodes directly to the main graph as
first-class nodes. A child graph acts as a single node that expands recursively into its components. The scheduler
may handle these approaches differently, potentially affecting performance.</p>
</div>
</section>
</section>
<section id="id5">
<h3>Creating a trace<a class="headerlink" href="#id5" title="Link to this heading">#</a></h3>
<p>Now you have manually implemented the processing pipeline with the graph API. You can examine the result by generating
another trace:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>rocprofv3<span class="w"> </span>-o<span class="w"> </span>graph_creation<span class="w"> </span>-d<span class="w"> </span>outDir<span class="w"> </span>-f<span class="w"> </span>pftrace<span class="w"> </span>--hip-trace<span class="w"> </span>--kernel-trace<span class="w"> </span>--memory-copy-trace<span class="w"> </span>--memory-allocation-trace<span class="w"> </span>--<span class="w"> </span>./bin/hip_graph_api_tutorial_graph_creation
</pre></div>
</div>
</section>
<section id="id6">
<h3>Analyzing the trace<a class="headerlink" href="#id6" title="Link to this heading">#</a></h3>
<p>Opening the resulting trace file <code class="docutils literal notranslate"><span class="pre">outDir/graph_creation_results.pftrace</span></code> with Perfetto shows a similar trace to what
you achieved with the capture variant:</p>
<figure class="align-center">
<img alt="Diagram showing a trace of the creation variant." src="../_images/creation_trace.png" />
</figure>
<p>Like before, the kernels are executed <em>en bloc</em>. By creating nodes for all operations in the processing pipeline, you
avoided the launching and scheduling overhead you previously observed in the stream-based variant.</p>
</section>
<section id="updating-individual-nodes">
<h3>Updating individual nodes<a class="headerlink" href="#updating-individual-nodes" title="Link to this heading">#</a></h3>
<p>The code presented in this tutorial updates the entire graph instance for each new batch. Applications that require
updates to only a small subset of nodes might experience excessive overhead. For these cases, the HIP Graph API
provides the following methods for updating individual nodes:</p>
<ul class="simple">
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv435hipGraphExecChildGraphNodeSetParams14hipGraphExec_t14hipGraphNode_t10hipGraph_t" title="hipGraphExecChildGraphNodeSetParams"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecChildGraphNodeSetParams()</span></code></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv435hipGraphExecEventRecordNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t" title="hipGraphExecEventRecordNodeSetEvent"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecEventRecordNodeSetEvent()</span></code></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv433hipGraphExecEventWaitNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t" title="hipGraphExecEventWaitNodeSetEvent"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecEventWaitNodeSetEvent()</span></code></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv449hipGraphExecExternalSemaphoresSignalNodeSetParams14hipGraphExec_t14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams" title="hipGraphExecExternalSemaphoresSignalNodeSetParams"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecExternalSemaphoresSignalNodeSetParams()</span></code></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv447hipGraphExecExternalSemaphoresWaitNodeSetParams14hipGraphExec_t14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams" title="hipGraphExecExternalSemaphoresWaitNodeSetParams"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecExternalSemaphoresWaitNodeSetParams()</span></code></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv429hipGraphExecHostNodeSetParams14hipGraphExec_t14hipGraphNode_tPK17hipHostNodeParams" title="hipGraphExecHostNodeSetParams"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecHostNodeSetParams()</span></code></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv431hipGraphExecKernelNodeSetParams14hipGraphExec_t14hipGraphNode_tPK19hipKernelNodeParams" title="hipGraphExecKernelNodeSetParams"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecKernelNodeSetParams()</span></code></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv431hipGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tP16hipMemcpy3DParms" title="hipGraphExecMemcpyNodeSetParams"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecMemcpyNodeSetParams()</span></code></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv433hipGraphExecMemcpyNodeSetParams1D14hipGraphExec_t14hipGraphNode_tPvPKv6size_t13hipMemcpyKind" title="hipGraphExecMemcpyNodeSetParams1D"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecMemcpyNodeSetParams1D()</span></code></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv441hipGraphExecMemcpyNodeSetParamsFromSymbol14hipGraphExec_t14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind" title="hipGraphExecMemcpyNodeSetParamsFromSymbol"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecMemcpyNodeSetParamsFromSymbol()</span></code></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv439hipGraphExecMemcpyNodeSetParamsToSymbol14hipGraphExec_t14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind" title="hipGraphExecMemcpyNodeSetParamsToSymbol"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecMemcpyNodeSetParamsToSymbol()</span></code></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv431hipGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams" title="hipGraphExecMemsetNodeSetParams"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecMemsetNodeSetParams()</span></code></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#_CPPv425hipGraphExecNodeSetParams14hipGraphExec_t14hipGraphNode_tP18hipGraphNodeParams" title="hipGraphExecNodeSetParams"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphExecNodeSetParams()</span></code></a></p></li>
</ul>
</section>
</section>
<section id="conclusion">
<h2>Conclusion<a class="headerlink" href="#conclusion" title="Link to this heading">#</a></h2>
<p>When an application has predictable, repetitive workflows, transitioning from streams to graphs can significantly
reduce launch overhead and improve performance. HIP provides two approaches for creating graphs: stream capture and
explicit graph construction.</p>
<p><strong>Stream capture</strong> converts existing stream-based code into a graph by recording the operations between start and stop
capture calls. This approach minimizes code changes and works well when your application already has a graph-like
structure with clear dependencies.</p>
<p><strong>Explicit graph construction</strong> involves manually creating nodes and defining edges between them using the graph API.
While this approach requires more code changes and is more verbose, it provides fine-grained control over dependencies
and allows for optimizations that might not be possible with stream capture. This method is ideal when you need precise
control over the graph topology or when working with complex dependency patterns.</p>
<div class="admonition tip">
<p class="admonition-title">Tip</p>
<p>Choose stream capture for quick conversions of existing code with minimal changes. Choose explicit construction when
you need maximum control and optimization opportunities.</p>
</div>
</section>
<section id="resources">
<h2>Resources<a class="headerlink" href="#resources" title="Link to this heading">#</a></h2>
<ul class="simple">
<li><p><a class="reference internal" href="../how-to/hip_runtime_api/hipgraph.html#how-to-hip-graph"><span class="std std-ref">HIP Programming Guide’s section on HIP graphs</span></a></p></li>
<li><p><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html#graph-management-reference"><span class="std std-ref">HIP graph API reference</span></a></p></li>
</ul>
<p class="rubric">References</p>
<div role="list" class="citation-list">
<div class="citation" id="fedk84" role="doc-biblioentry">
<span class="label"><span class="fn-bracket">[</span><a role="doc-backlink" href="#id3">FeDK84</a><span class="fn-bracket">]</span></span>
<p>L.A. Feldkamp, L.C. Davis and J.W. Kress: “Practical cone-beam algorithm”. In <em>Journal of the Optical Society of America A</em>, vol. 1, no. 6, pp. 612-619, June 1984, DOI <a class="reference external" href="https://dx.doi.org/10.1364/JOSAA.1.000612">10.1364/JOSAA.1.000612</a>.</p>
</div>
<div class="citation" id="shlo74" role="doc-biblioentry">
<span class="label"><span class="fn-bracket">[</span><a role="doc-backlink" href="#id2">ShLo74</a><span class="fn-bracket">]</span></span>
<p>L.A. Shepp and B.F. Logan: “The Fourier reconstruction of a head section”. In <em>IEEE Transactions on Nuclear Science</em>, vol. 21, no. 3, pp. 21-43, June 1974, DOI <a class="reference external" href="https://dx.doi.org/10.1109/TNS.1974.6499235">10.1109/TNS.1974.6499235</a>.</p>
</div>
</div>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="cooperative_groups_tutorial.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Cooperative groups</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#introduction">Introduction</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#modeling-dependencies-between-gpu-operations">Modeling dependencies between GPU operations</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#streams">Streams</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#graphs">Graphs</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#when-to-use-graphs">When to use graphs</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#transitioning-a-ct-reconstruction-pipeline">Transitioning a CT reconstruction pipeline</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#what-you-will-learn">What you will learn</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#before-you-begin">Before you begin</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#required-knowledge">Required knowledge</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hardware-and-software-requirements">Hardware and software requirements</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#optional-knowledge">Optional knowledge</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#step-1-build-the-tutorial-code">Step 1: Build the tutorial code</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#step-2-examining-the-stream-based-baseline-application">Step 2: Examining the stream-based baseline application</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#understanding-batched-processing">Understanding batched processing</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#determining-parallel-capacity">Determining parallel capacity</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#processing-projections-in-batches">Processing projections in batches</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#synchronization">Synchronization</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#exploring-the-processing-pipeline">Exploring the processing pipeline</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#creating-a-trace-file">Creating a trace file</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#analyzing-the-trace">Analyzing the trace</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#step-3-converting-to-graphs-via-stream-capture">Step 3: Converting to graphs via stream capture</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#creating-a-trace">Creating a trace</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id4">Analyzing the trace</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#step-4-manual-graph-creation-advanced">Step 4: Manual graph creation (advanced)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#adding-hipfft-nodes">Adding hipFFT nodes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-1-save-existing-nodes">Step 1: Save existing nodes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-2-capture-hipfft-operations">Step 2: Capture hipFFT operations</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-3-get-updated-node-list">Step 3: Get updated node list</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-4-find-new-nodes">Step 4: Find new nodes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-5-identify-the-leaf-node">Step 5: Identify the leaf node</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id5">Creating a trace</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id6">Analyzing the trace</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#updating-individual-nodes">Updating individual nodes</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#conclusion">Conclusion</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#resources">Resources</a></li>
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
