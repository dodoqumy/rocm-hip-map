---
title: "Reduction &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/reduction.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:07:49.261420+00:00
content_hash: "fe3b2c7f22180378"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="HIP reduction tutorial" name="description" />
<meta content="AMD, ROCm, HIP, reduction, tutorial" name="keywords" />

    <title>Reduction &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'tutorial/reduction';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Cooperative groups" href="cooperative_groups_tutorial.html" />
    <link rel="prev" title="Multi-kernel programming: breadth-first search tutorial" href="programming-patterns/multikernel_bfs.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/tutorial/reduction.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Reduction</a></li>
<li class="toctree-l1"><a class="reference internal" href="cooperative_groups_tutorial.html">Cooperative groups</a></li>
<li class="toctree-l1"><a class="reference internal" href="graph_api.html">HIP Graph API Tutorial</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">Reduction</li>
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
    <h1>Reduction</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#the-algorithm">The algorithm</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#reduction-on-gpus">Reduction on GPUs</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#naive-shared-reduction">Naive shared reduction</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#reducing-thread-divergence">Reducing thread divergence</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#resolving-bank-conflicts">Resolving bank conflicts</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#utilize-upper-half-of-the-block">Utilize upper half of the block</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#unroll-all-loops">Unroll all loops</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#communicate-using-warp-collective-functions">Communicate using warp-collective functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#prefer-warp-communication-over-shared">Prefer warp communication over shared</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amortize-bookkeeping-variable-overhead">Amortize bookkeeping variable overhead</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#reading-itemsperthread">Reading <code class="docutils literal notranslate"><span class="pre">ItemsPerThread</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#processing-itemsperthread">Processing <code class="docutils literal notranslate"><span class="pre">ItemsPerThread</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#two-pass-reduction">Two-pass reduction</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#global-data-share">Global data share</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#conclusion">Conclusion</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="reduction">
<h1>Reduction<a class="headerlink" href="#reduction" title="Link to this heading">#</a></h1>
<p>Reduction is a common algorithmic operation used in parallel programming to reduce an array of elements into a shorter array of elements or a single value. This document exploits reduction to introduce some key considerations while designing and optimizing GPU algorithms.</p>
<p>This document is a rejuvenation and extension of the invaluable <a class="reference external" href="https://developer.download.nvidia.com/assets/cuda/files/reduction.pdf">work of Mark Harris</a>. While the author approaches the topic with a less naive approach, reviewing some original material is valuable to see how much the underlying hardware has changed. This document provides a greater insight to demonstrate progress.</p>
<section id="the-algorithm">
<h2>The algorithm<a class="headerlink" href="#the-algorithm" title="Link to this heading">#</a></h2>
<p>Reduction has many names depending on the domain; in functional programming it’s referred to as <a class="reference external" href="https://en.wikipedia.org/wiki/Fold_(higher-order_function)">fold</a>, in C++, it’s called <code class="docutils literal notranslate"><span class="pre">std::accumulate</span></code> and in C++17, as <code class="docutils literal notranslate"><span class="pre">std::reduce</span></code>. A reduction takes a range of inputs and “reduces” the given range with a binary operation to a singular or scalar output. Canonically, a reduction requires a “zero” element that bootstraps the algorithm and serves as one of the initial operands to the binary operation. The “zero” element is generally called <a class="reference external" href="https://en.wikipedia.org/wiki/Identity_element">identity or neutral</a> element in the group theory, which implies that it is an operand that doesn’t change the result. Some typical use cases are: calculating a sum or normalizing a dataset and finding the maximum value in the dataset. The latter use case is discussed further in this tutorial.</p>
<figure class="align-default">
<img alt="Diagram demonstrating fold left" src="../_images/foldl.svg" />
</figure>
<p>There are multiple variations of reduction that allow parallel processing. The approach taken by <code class="docutils literal notranslate"><span class="pre">std::reduce</span></code> requires the user-provided binary operator to operate on any combination of identity and input range elements, or even exclusively on any of them. This allows you to insert any number of identities to facilitate parallel processing and then combine the partial results of parallel execution.</p>
<figure class="align-default">
<img alt="Diagram demonstrating parallel fold left" src="../_images/parallel_foldl.svg" />
</figure>
</section>
<section id="reduction-on-gpus">
<h2>Reduction on GPUs<a class="headerlink" href="#reduction-on-gpus" title="Link to this heading">#</a></h2>
<p>Implementing reductions on GPUs requires a basic understanding of the <a class="reference internal" href="../understand/programming_model.html"><span class="doc">Introduction to the HIP programming model</span></a>. The document explores aspects of low-level optimization best discussed through the <a class="reference internal" href="../understand/programming_model.html#inherent-thread-model"><span class="std std-ref">Hierarchical thread model</span></a>, and refrains from using cooperative groups.</p>
<p>Synchronizing parallel threads of execution across a GPU is crucial for correctness as the partial results can’t be synchronized before they manifest. Synchronizing all the threads running on a GPU at any given time is possible, however, it is a costly and intricate operation. If synchronization is not absolutely necessary, map the parallel algorithm so that multiprocessors and blocks can make independent progress and need not sync frequently.</p>
<p>There are ten reduction implementations in the <a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/Tutorials/reduction/include/Reduction">rocm-examples</a>, which are described in the following sections.</p>
<section id="naive-shared-reduction">
<h3>Naive shared reduction<a class="headerlink" href="#naive-shared-reduction" title="Link to this heading">#</a></h3>
<p>The naive algorithm takes a tree-like shape, where the computational domain is purposefully distributed among blocks. In all blocks, all threads participate in loading data from persistent (from the kernel’s perspective) global memory into the shared memory. This helps to perform tree-like reduction for a single thread by writing the partial result to global, in a location unique to the block, which allows the block to make independent progress. The partial results are combined in subsequent launches of the same kernel until a scalar result is reached.</p>
<figure class="align-default">
<img alt="Diagram demonstrating naive reduction" src="../_images/naive_reduction.svg" />
</figure>
<p>This approach requires temporary storage based on the number of blocks launched, as each block outputs a scalar partial result. Depending on the need to store or destroy the input, a second temporary storage might be needed, which could be large enough to store the results of the second kernel launch. Alternatively, you can reuse the storage of the larger than necessary original input. These implementations differ so slightly that the document only considers the use case where the input could be destroyed.</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">factor</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">block_size</span><span class="p">;</span><span class="w"> </span><span class="c1">// block_size from hipGetDeviceProperties()</span>
<span class="k">auto</span><span class="w"> </span><span class="n">new_size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="n">factor</span><span class="p">](</span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">actual</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// Every pass reduces input length by &#39;factor&#39;. If actual size is not divisible by factor,</span>
<span class="w">    </span><span class="c1">// an extra output element is produced using some number of zero_elem inputs.</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">actual</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">factor</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="p">(</span><span class="n">actual</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="n">factor</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="mi">0</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="mi">1</span><span class="p">);</span>
<span class="p">};</span>
</pre></div>
</div>
<p>For threads that don’t have unique inputs, feed <code class="docutils literal notranslate"><span class="pre">zero_elem</span></code> instances to threads. The backing of double-buffering is allocated as such:</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="c1">// Initialize host-side storage</span>
<span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">unsigned</span><span class="o">&gt;</span><span class="w"> </span><span class="n">input</span><span class="p">(</span><span class="n">input_count</span><span class="p">);</span>
<span class="n">std</span><span class="o">::</span><span class="n">iota</span><span class="p">(</span><span class="n">input</span><span class="p">.</span><span class="n">begin</span><span class="p">(),</span><span class="w"> </span><span class="n">input</span><span class="p">.</span><span class="n">end</span><span class="p">(),</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>

<span class="c1">// Initialize device-side storage</span>
<span class="kt">unsigned</span><span class="w"> </span><span class="o">*</span><span class="n">front</span><span class="p">,</span>
<span class="w">         </span><span class="o">*</span><span class="n">back</span><span class="p">;</span>
<span class="n">hipMalloc</span><span class="p">((</span><span class="kt">void</span><span class="o">**</span><span class="p">)</span><span class="o">&amp;</span><span class="n">front</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">unsigned</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">input_count</span><span class="p">);</span>
<span class="n">hipMalloc</span><span class="p">((</span><span class="kt">void</span><span class="o">**</span><span class="p">)</span><span class="o">&amp;</span><span class="n">back</span><span class="p">,</span><span class="w">  </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">unsigned</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">new_size</span><span class="p">(</span><span class="n">input_count</span><span class="p">));</span>

<span class="n">hipMemcpy</span><span class="p">(</span><span class="n">front</span><span class="p">,</span><span class="w"> </span><span class="n">input</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">input</span><span class="p">.</span><span class="n">size</span><span class="p">()</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">unsigned</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">);</span>
</pre></div>
</div>
<p>Data is initialized on the host and dispatched to the device followed by the commencement of device-side reduction. The swapping of the double-buffer on the last iteration is omitted, therefore the result is in the back-buffer irrespective of the input size.</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">curr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">input_count</span><span class="p">;</span><span class="w"> </span><span class="n">curr</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="mi">1</span><span class="p">;)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">hipLaunchKernelGGL</span><span class="p">(</span>
<span class="w">        </span><span class="n">kernel</span><span class="p">,</span>
<span class="w">        </span><span class="n">dim3</span><span class="p">(</span><span class="n">new_size</span><span class="p">(</span><span class="n">curr</span><span class="p">)),</span>
<span class="w">        </span><span class="n">dim3</span><span class="p">(</span><span class="n">block_size</span><span class="p">),</span>
<span class="w">        </span><span class="n">factor</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">unsigned</span><span class="p">),</span>
<span class="w">        </span><span class="n">hipStreamDefault</span><span class="p">,</span>
<span class="w">        </span><span class="n">front</span><span class="p">,</span>
<span class="w">        </span><span class="n">back</span><span class="p">,</span>
<span class="w">        </span><span class="n">kernel_op</span><span class="p">,</span>
<span class="w">        </span><span class="n">zero_elem</span><span class="p">,</span>
<span class="w">        </span><span class="n">curr</span><span class="p">);</span>

<span class="w">    </span><span class="n">curr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">new_size</span><span class="p">(</span><span class="n">curr</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">curr</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="mi">1</span><span class="p">)</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">swap</span><span class="p">(</span><span class="n">front</span><span class="p">,</span><span class="w"> </span><span class="n">back</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p>This structure persists in the kernel throughout all the variations of reduction with slight modifications to <code class="docutils literal notranslate"><span class="pre">factor</span></code> and shared memory allocation:</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="k">template</span><span class="o">&lt;</span><span class="k">typename</span><span class="w"> </span><span class="nc">T</span><span class="p">,</span><span class="w"> </span><span class="k">typename</span><span class="w"> </span><span class="nc">F</span><span class="o">&gt;</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernel</span><span class="p">(</span>
<span class="w">    </span><span class="n">T</span><span class="o">*</span><span class="w"> </span><span class="n">front</span><span class="p">,</span>
<span class="w">    </span><span class="n">T</span><span class="o">*</span><span class="w"> </span><span class="n">back</span><span class="p">,</span>
<span class="w">    </span><span class="n">F</span><span class="w"> </span><span class="n">op</span><span class="p">,</span>
<span class="w">    </span><span class="n">T</span><span class="w"> </span><span class="n">zero_elem</span><span class="p">,</span>
<span class="w">    </span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">front_size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">extern</span><span class="w"> </span><span class="n">__shared__</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">shared</span><span class="p">[];</span>

<span class="w">    </span><span class="c1">// Overindex-safe read of input</span>
<span class="w">    </span><span class="k">auto</span><span class="w"> </span><span class="n">read_global_safe</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="o">&amp;</span><span class="p">](</span><span class="k">const</span><span class="w"> </span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">i</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">front_size</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="n">front</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">zero_elem</span><span class="p">;</span>
<span class="w">    </span><span class="p">};</span>

<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">,</span>
<span class="w">                   </span><span class="n">bid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">,</span>
<span class="w">                   </span><span class="n">gid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">bid</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">tid</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Read input from front buffer to shared</span>
<span class="w">    </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">read_global_safe</span><span class="p">(</span><span class="n">gid</span><span class="p">);</span>
<span class="w">    </span><span class="n">__syncthreads</span><span class="p">();</span>

<span class="w">    </span><span class="c1">// Shared reduction</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">*=</span><span class="w"> </span><span class="mi">2</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="p">(</span><span class="mi">2</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span>
<span class="w">            </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">op</span><span class="p">(</span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="p">],</span><span class="w"> </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">]);</span>
<span class="w">        </span><span class="n">__syncthreads</span><span class="p">();</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Write result from shared to back buffer</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span>
<span class="w">        </span><span class="n">back</span><span class="p">[</span><span class="n">bid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">shared</span><span class="p">[</span><span class="mi">0</span><span class="p">];</span>
<span class="p">}</span>
</pre></div>
</div>
<p>While the <code class="docutils literal notranslate"><span class="pre">tid</span> <span class="pre">%</span> <span class="pre">(2</span> <span class="pre">*</span> <span class="pre">i)</span> <span class="pre">==</span> <span class="pre">0</span></code> indexing scheme yields correct results, it also leads to high thread divergence. Thread divergence indicates the event when the threads in a warp diverge, which implies that the threads have to execute different instructions in a given clock cycle. This is easily manifested using <code class="docutils literal notranslate"><span class="pre">if-else</span></code> statements as shown here, but can also be manifested as <code class="docutils literal notranslate"><span class="pre">for</span></code> loop dependent on thread ID lengths. Even though the number of active threads participating in the reduction reduces, warps remain active longer than necessary, as at least one lane in a warp hits the <code class="docutils literal notranslate"><span class="pre">if</span></code> statement.</p>
</section>
<section id="reducing-thread-divergence">
<h3>Reducing thread divergence<a class="headerlink" href="#reducing-thread-divergence" title="Link to this heading">#</a></h3>
<p>You can reduce divergence by keeping dataflow between memory addresses identical but reassigning the thread ids.</p>
<figure class="align-default">
<img alt="Diagram demonstrating reduced divergence reduction" src="../_images/reduced_divergence_reduction.svg" />
</figure>
<div class="highlight-diff notranslate"><div class="highlight"><pre><span></span>// Shared reduction
for (uint32_t i = 1; i &lt; blockDim.x; i *= 2)
{
<span class="hll"><span class="gd">-    if (tid % (2 * i) == 0)</span>
</span><span class="hll"><span class="gd">-        shared[tid] = op(shared[tid], shared[tid + i]);</span>
</span><span class="hll"><span class="gi">+    if (uint32_t j = 2 * i * tid; j &lt; blockDim.x)</span>
</span><span class="hll"><span class="gi">+        shared[j] = op(shared[j], shared[j + i]);</span>
</span><span class="w"> </span>   __syncthreads();
}
</pre></div>
</div>
<p>This way inactive threads start accumulating uniformly towards the higher thread ID index range and might uniformly skip to <code class="docutils literal notranslate"><span class="pre">__syncthreads()</span></code>. However, this introduces a bank conflicts issue.</p>
</section>
<section id="resolving-bank-conflicts">
<h3>Resolving bank conflicts<a class="headerlink" href="#resolving-bank-conflicts" title="Link to this heading">#</a></h3>
<p>Both AMD and NVIDIA implement shared memory in the hardware by organizing storage into banks of various sizes. This hardware element is known as Local Data Share (LDS) on AMD hardware. On NVIDIA hardware, it’s implemented using the same silicon as the L1 data cache. You can think of shared memory as a striped 2-dimensional range of memory. Shared memory bank’s count, width, and depth depend on the architecture. A bank conflict occurs when different threads in a warp access the same bank during the same operation. In this case, the hardware prevents the attempted concurrent accesses to the same bank by converting them into serial accesses.</p>
<ul class="simple">
<li><p><a class="reference external" href="https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/instinct-mi200-cdna2-instruction-set-architecture.pdf">“AMD Instinct MI200” Instruction Set Architecture, Chapter 11.1</a></p></li>
<li><p><a class="reference external" href="https://www.amd.com/content/dam/amd/en/documents/radeon-tech-docs/instruction-set-architectures/rdna2-shader-instruction-set-architecture.pdf">“RDNA 2” Instruction Set Architecture, Chapter 10.1</a></p></li>
</ul>
<p>A notable exception is when the shared read uniformly broadcasts to the same address across the entire warp. A better implementation of the naive algorithm is to form continuous ranges of the threads activities and their memory accesses.</p>
<div class="highlight-diff notranslate"><div class="highlight"><pre><span></span>// Shared reduction
<span class="hll"><span class="gd">-for (uint32_t i = 1; i &lt; blockDim.x; i *= 2)</span>
</span><span class="hll"><span class="gd">-{</span>
</span><span class="hll"><span class="gd">-    if (tid % (2 * i) == 0)</span>
</span><span class="hll"><span class="gi">+for (uint32_t i = blockDim.x / 2; i != 0; i /= 2)</span>
</span><span class="hll"><span class="gi">+{</span>
</span><span class="hll"><span class="gi">+    if (tid &lt; i)</span>
</span><span class="w"> </span>       shared[tid] = op(shared[tid], shared[tid + i]);
<span class="w"> </span>   __syncthreads();
}
</pre></div>
</div>
<figure class="align-default">
<img alt="Diagram demonstrating bank conflict free reduction" src="../_images/conflict_free_reduction.svg" />
</figure>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>To avoid bank conflicts, read shared memory in a coalesced manner, which implies that reads/writes of each lane in a warp evaluate to consecutive locations. Analyzing the read/write patterns could help you to understand the cause of bank conflicts. For more details, check <a class="reference external" href="https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-mi300-cdna3-instruction-set-architecture.pdf">CDNA3 ISA</a> or <a class="reference external" href="https://www.amd.com/content/dam/amd/en/documents/radeon-tech-docs/instruction-set-architectures/rdna3-shader-instruction-set-architecture-feb-2023_0.pdf">RDNA3 ISA</a> data share operations chapter.</p>
</div>
</section>
<section id="utilize-upper-half-of-the-block">
<h3>Utilize upper half of the block<a class="headerlink" href="#utilize-upper-half-of-the-block" title="Link to this heading">#</a></h3>
<p>The preceding implementation is free of low-level GPU-specific anti-patterns. However, it still exhibits some common shortcomings. The loop performing the reduction in the shared memory starts from <code class="docutils literal notranslate"><span class="pre">i</span> <span class="pre">=</span> <span class="pre">blockDim.x</span> <span class="pre">/</span> <span class="pre">2</span></code> and the first predicate <code class="docutils literal notranslate"><span class="pre">if</span> <span class="pre">(tid</span> <span class="pre">&lt;</span> <span class="pre">i)</span></code> immediately disables half of the block, which only helps load the data into the shared memory. You can change the kernel along with the calculation of <code class="docutils literal notranslate"><span class="pre">factor</span></code> on the host, as shown here:</p>
<div class="highlight-diff notranslate"><div class="highlight"><pre><span></span>const uint32_t tid = threadIdx.x,
<span class="w"> </span>              bid = blockIdx.x,
<span class="hll"><span class="gd">-              gid = bid * blockDim.x + tid;</span>
</span><span class="hll"><span class="gi">+              gid = bid * (blockDim.x * 2) + tid;</span>
</span>
// Read input from front buffer to shared
<span class="gd">-shared[tid] = read_global_safe(gid);</span>
<span class="gi">+shared[tid] = op(read_global_safe(gid), read_global_safe(gid + blockDim.x));</span>
__syncthreads();
</pre></div>
</div>
<p>By eliminating half of the threads and giving meaningful work to all the threads by unconditionally performing a binary <code class="docutils literal notranslate"><span class="pre">op</span></code>, you can prevent the wastage of half of the threads.</p>
<p>Even though global memory is read in a coalesced fashion, as preferred by the memory controller, optimal performance is still limited by the instruction throughput.
Omit superfluous synchronization
——————————–</p>
<p>Warps are known to execute in a strict lockstep fashion. Therefore, once shared reduction reaches a point where only a single warp participates meaningfully, you can cut short the loop and let the rest of the warps terminate. Moreover, you can also unroll the loop without syncing the entire block.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">tmp</span></code> namespace used beyond this point in this document holds a handful of template meta-programmed utilities to facilitate writing flexible and optimal code.</p>
<p><code class="code docutils literal notranslate"><span class="pre">tmp::static_for</span></code> is not just a constant folding within the optimizer but a variation of the language <code class="code docutils literal notranslate"><span class="pre">for</span></code> loop, where the running index is a compile-time constant and is eligible for use in compile-time evaluated contexts.</p>
<p>Consider the following code:</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">4</span><span class="p">;</span>
<span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="w"> </span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">&quot;%d&quot;</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p>This compiles to the following binaries:</p>
<p><strong>LLVM Block</strong></p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">main</span><span class="p">:</span>
    <span class="n">push</span>    <span class="n">rbx</span>
    <span class="n">lea</span>     <span class="n">rbx</span><span class="p">,</span> <span class="p">[</span><span class="n">rip</span> <span class="o">+</span> <span class="o">.</span><span class="n">L</span><span class="o">.</span><span class="n">str</span><span class="p">]</span>
    <span class="n">mov</span>     <span class="n">rdi</span><span class="p">,</span> <span class="n">rbx</span>
    <span class="n">xor</span>     <span class="n">esi</span><span class="p">,</span> <span class="n">esi</span>
    <span class="n">xor</span>     <span class="n">eax</span><span class="p">,</span> <span class="n">eax</span>
    <span class="n">call</span>    <span class="n">printf</span><span class="nd">@PLT</span>
    <span class="n">mov</span>     <span class="n">rdi</span><span class="p">,</span> <span class="n">rbx</span>
    <span class="n">mov</span>     <span class="n">esi</span><span class="p">,</span> <span class="mi">1</span>
    <span class="n">xor</span>     <span class="n">eax</span><span class="p">,</span> <span class="n">eax</span>
    <span class="n">call</span>    <span class="n">printf</span><span class="nd">@PLT</span>
    <span class="n">mov</span>     <span class="n">rdi</span><span class="p">,</span> <span class="n">rbx</span>
    <span class="n">mov</span>     <span class="n">esi</span><span class="p">,</span> <span class="mi">2</span>
    <span class="n">xor</span>     <span class="n">eax</span><span class="p">,</span> <span class="n">eax</span>
    <span class="n">call</span>    <span class="n">printf</span><span class="nd">@PLT</span>
    <span class="n">mov</span>     <span class="n">rdi</span><span class="p">,</span> <span class="n">rbx</span>
    <span class="n">mov</span>     <span class="n">esi</span><span class="p">,</span> <span class="mi">3</span>
    <span class="n">xor</span>     <span class="n">eax</span><span class="p">,</span> <span class="n">eax</span>
    <span class="n">call</span>    <span class="n">printf</span><span class="nd">@PLT</span>
    <span class="n">xor</span>     <span class="n">eax</span><span class="p">,</span> <span class="n">eax</span>
    <span class="n">pop</span>     <span class="n">rbx</span>
    <span class="n">ret</span>
<span class="o">.</span><span class="n">L</span><span class="o">.</span><span class="n">str</span><span class="p">:</span>
    <span class="o">.</span><span class="n">asciz</span>  <span class="s2">&quot;</span><span class="si">%d</span><span class="s2">&quot;</span>
</pre></div>
</div>
<p><strong>GCC</strong></p>
<div class="highlight-asm notranslate"><div class="highlight"><pre><span></span><span class="nl">.LC0:</span>
<span class="w">    </span><span class="na">.string</span><span class="w"> </span><span class="s">&quot;%d&quot;</span>
<span class="nl">main:</span>
<span class="w">    </span><span class="nf">push</span><span class="w">    </span><span class="no">rbx</span>
<span class="w">    </span><span class="nf">xor</span><span class="w">     </span><span class="no">ebx</span><span class="p">,</span><span class="w"> </span><span class="no">ebx</span>
<span class="nl">.L2:</span>
<span class="w">    </span><span class="nf">mov</span><span class="w">     </span><span class="no">esi</span><span class="p">,</span><span class="w"> </span><span class="no">ebx</span>
<span class="w">    </span><span class="nf">mov</span><span class="w">     </span><span class="no">edi</span><span class="p">,</span><span class="w"> </span><span class="no">OFFSET</span><span class="w"> </span><span class="no">FLAT</span><span class="p">:.</span><span class="no">LC0</span>
<span class="w">    </span><span class="nf">xor</span><span class="w">     </span><span class="no">eax</span><span class="p">,</span><span class="w"> </span><span class="no">eax</span>
<span class="w">    </span><span class="nf">add</span><span class="w">     </span><span class="no">ebx</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span>
<span class="w">    </span><span class="nf">call</span><span class="w">    </span><span class="no">printf</span>
<span class="w">    </span><span class="nf">cmp</span><span class="w">     </span><span class="no">ebx</span><span class="p">,</span><span class="w"> </span><span class="mi">4</span>
<span class="w">    </span><span class="nf">jne</span><span class="w">     </span><span class="no">.L2</span>
<span class="w">    </span><span class="nf">xor</span><span class="w">     </span><span class="no">eax</span><span class="p">,</span><span class="w"> </span><span class="no">eax</span>
<span class="w">    </span><span class="nf">pop</span><span class="w">     </span><span class="no">rbx</span>
<span class="w">    </span><span class="nf">ret</span>
</pre></div>
</div>
<p><strong>MSVC</strong></p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>main    PROC
    $LN12:
    push    rbx
    sub     rsp, 32
    xor     ebx, ebx
    npad    8
$LL4@main:
    mov     edx, ebx
    lea     rcx, OFFSET FLAT:&#39;string&#39;
    call    printf
    inc     ebx
    cmp     ebx, 4
    jl      SHORT $LL4@main
    xor     eax, eax
    add     rsp, 32
    pop     rbx
    ret     0
main    ENDP
</pre></div>
</div>
<p>LLVM unrolls the loop and compiles to a flat series of <code class="docutils literal notranslate"><span class="pre">printf</span></code> invocations, while both GCC and MSVC keep the loop intact, as visible from the compare (<code class="docutils literal notranslate"><span class="pre">cmp</span></code>) and the jump (<code class="docutils literal notranslate"><span class="pre">jne</span></code>, <code class="docutils literal notranslate"><span class="pre">jl</span></code>) instructions. LLVM code generation is identical to manually writing the unrolled loop:</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="n">printf</span><span class="p">(</span><span class="s">&quot;%d&quot;</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">&quot;%d&quot;</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">&quot;%d&quot;</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">);</span>
<span class="n">printf</span><span class="p">(</span><span class="s">&quot;%d&quot;</span><span class="p">,</span><span class="w"> </span><span class="mi">3</span><span class="p">);</span>
</pre></div>
</div>
<p>While various non-standard pragmas are available to hint or force the compiler to unroll the loop, we instead use template meta-programming to force feed the compiler the unrolled loop.</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">4</span><span class="p">;</span>

<span class="c1">// Maybe unrolled loop</span>
<span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="w"> </span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">&quot;%d&quot;</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">);</span>
<span class="p">}</span>

<span class="c1">// Force unrolled loop</span>
<span class="k">using</span><span class="w"> </span><span class="k">namespace</span><span class="w"> </span><span class="nn">tmp</span><span class="p">;</span>
<span class="n">static_for</span><span class="o">&lt;</span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">less_than</span><span class="o">&lt;</span><span class="n">size</span><span class="o">&gt;</span><span class="p">,</span><span class="w"> </span><span class="n">increment</span><span class="o">&lt;</span><span class="mi">1</span><span class="o">&gt;&gt;</span><span class="p">([]</span><span class="o">&lt;</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="o">&gt;</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">&quot;%d&quot;</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">);</span>
<span class="p">});</span>
</pre></div>
</div>
<p>The most notable structural difference is that in the language <code class="docutils literal notranslate"><span class="pre">for</span></code> loop, the loop variable is given a name in the beginning, while in the <code class="docutils literal notranslate"><span class="pre">static_for</span></code> utility, the loop variable is given a name in the end. An important bonus is that in the loop’s body, you can use the running index <code class="docutils literal notranslate"><span class="pre">i</span></code> in contexts requiring constant expressions such as template arguments or inside <code class="docutils literal notranslate"><span class="pre">if</span> <span class="pre">constexpr</span></code>.</p>
<p><code class="code docutils literal notranslate"><span class="pre">tmp::static_switch</span></code> takes runtime value and runtime dispatches to a range of set of tabulated functions, where said value is a compile-time constant and is eligible for use in compile-time evaluated contexts.</p>
<p>Consider the following code:</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">warp_size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">device_props</span><span class="p">.</span><span class="n">warpSize</span><span class="p">;</span>
<span class="k">switch</span><span class="w"> </span><span class="p">(</span><span class="n">warp_size</span><span class="p">)</span>
<span class="p">{</span>
<span class="k">case</span><span class="w"> </span><span class="mi">32</span><span class="p">:</span>
<span class="w">    </span><span class="n">hipLaunchKernelGGL</span><span class="p">(</span><span class="n">kernel</span><span class="o">&lt;</span><span class="mi">32</span><span class="o">&gt;</span><span class="p">,</span><span class="w"> </span><span class="p">...);</span>
<span class="w">    </span><span class="k">break</span><span class="p">;</span>
<span class="k">case</span><span class="w"> </span><span class="mi">64</span><span class="p">:</span>
<span class="w">    </span><span class="n">hipLaunchKernelGGL</span><span class="p">(</span><span class="n">kernel</span><span class="o">&lt;</span><span class="mi">64</span><span class="o">&gt;</span><span class="p">,</span><span class="w"> </span><span class="p">...);</span>
<span class="w">    </span><span class="k">break</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>In the preceding code, note the code repetition for all possible values of <code class="docutils literal notranslate"><span class="pre">warp_size</span></code>, the code is prepared to handle. To avoid this, use <code class="docutils literal notranslate"><span class="pre">tmp::static_switch</span></code>, as shown:</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="n">tmp</span><span class="o">::</span><span class="n">static_switch</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="n">array</span><span class="p">{</span><span class="mi">32</span><span class="p">,</span><span class="w"> </span><span class="mi">64</span><span class="p">}</span><span class="o">&gt;</span><span class="p">(</span><span class="n">warp_size</span><span class="p">,</span><span class="w"> </span><span class="p">[</span><span class="o">&amp;</span><span class="p">]</span><span class="o">&lt;</span><span class="kt">int</span><span class="w"> </span><span class="n">WarpSize</span><span class="o">&gt;</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">hipLaunchKernelGGL</span><span class="p">(</span><span class="n">kernel</span><span class="o">&lt;</span><span class="n">WarpSize</span><span class="o">&gt;</span><span class="p">,</span><span class="w"> </span><span class="p">...);</span>
<span class="p">});</span>
</pre></div>
</div>
<div class="highlight-diff notranslate"><div class="highlight"><pre><span></span><span class="hll"><span class="gd">-template&lt;typename T, typename F&gt;</span>
</span><span class="hll"><span class="gi">+template&lt;uint32_t WarpSize, typename T, typename F&gt;</span>
</span>__global__ void kernel(
<span class="w"> </span>   ...
)
{
<span class="w"> </span>   ...
// Shared reduction
<span class="hll"><span class="gd">-for (uint32_t i = blockDim.x / 2; i != 0; i /= 2)</span>
</span><span class="hll"><span class="gi">+for (uint32_t i = blockDim.x / 2; i &gt; WarpSize; i /= 2)</span>
</span>{
<span class="w"> </span>   if (tid &lt; i)
<span class="w"> </span>       shared[tid] = op(shared[tid], shared[tid + i]);
<span class="w"> </span>   __syncthreads();
}
<span class="hll"><span class="gi">+// Warp reduction</span>
</span><span class="hll"><span class="gi">+tmp::static_for&lt;WarpSize, tmp::not_equal&lt;0&gt;, tmp::divide&lt;2&gt;&gt;([&amp;]&lt;int I&gt;()</span>
</span><span class="hll"><span class="gi">+{</span>
</span><span class="hll"><span class="gi">+    if (tid &lt; I)</span>
</span><span class="hll"><span class="gi">+        shared[tid] = op(shared[tid], shared[tid + I]);</span>
</span><span class="hll"><span class="gi">+});</span>
</span></pre></div>
</div>
<p>Because HIP targets AMD hardware with warp sizes of 32 (RDNA AMD GPUs) and 64 (CDNA AMD GPUs), HIP code must handle both. That is why instead of assuming a warp size of 32, make the warp size a template argument of the kernel. This allows you to unroll the final loop using <code class="docutils literal notranslate"><span class="pre">tmp::static_for</span></code> in a parametric way but still having the code read much like an ordinary loop.</p>
<p>Promoting the warp size to being a compile-time constant also requires you to handle it similarly on the host-side. You can sandwich the kernel launch with <code class="docutils literal notranslate"><span class="pre">tmp::static_switch</span></code>, promoting the snake-case run-time <code class="docutils literal notranslate"><span class="pre">warp_size</span></code> variable to a camel-case compile-time constant <code class="docutils literal notranslate"><span class="pre">WarpSize</span></code>.</p>
<div class="highlight-diff notranslate"><div class="highlight"><pre><span></span>// Device-side reduction
for (uint32_t curr = input_count; curr &gt; 1;)
{
<span class="hll"><span class="gi">+    tmp::static_range_switch&lt;std::array{32, 64}&gt;(warp_size, [&amp;]&lt;int WarpSize&gt;() noexcept</span>
</span><span class="hll"><span class="gi">+    {</span>
</span><span class="w"> </span>       hipLaunchKernelGGL(
<span class="hll"><span class="gd">-            kernel,</span>
</span><span class="hll"><span class="gi">+            kernel&lt;WarpSize&gt;,</span>
</span><span class="w"> </span>           dim3(new_size(curr)),
<span class="w"> </span>           dim3(block_size),
<span class="w"> </span>           factor * sizeof(unsigned),
<span class="w"> </span>           hipStreamDefault,
<span class="w"> </span>           front,
<span class="w"> </span>           back,
<span class="w"> </span>           kernel_op,
<span class="w"> </span>           zero_elem,
<span class="w"> </span>           curr);
<span class="hll"><span class="gi">+    });</span>
</span><span class="w"> </span>   ...
}
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Neither RDNA- nor CDNA-based AMD hardware provides guaranteed independent progress to lanes of the same warp. AMD GPUs execute warps in lockstep, meaning all lanes progress together. This lockstep behavior simplifies synchronization within a warp, as you can rely on all active lanes executing instructions at the same time without requiring explicit warp-level synchronization primitives.</p>
</div>
</section>
<section id="unroll-all-loops">
<h3>Unroll all loops<a class="headerlink" href="#unroll-all-loops" title="Link to this heading">#</a></h3>
<p>While the previous step primarily aims to remove unnecessary syncing, it also unrolls the end of the loop. However, you could also force unrolling the first part of the loop. This saves a few scalar registers (values the compiler can prove to be uniform across warps).</p>
<div class="highlight-diff notranslate"><div class="highlight"><pre><span></span><span class="hll"><span class="gd">-template&lt;uint32_t WarpSize, typename T, typename F&gt;</span>
</span><span class="hll"><span class="gd">-__global__ void kernel(</span>
</span><span class="hll"><span class="gi">+template&lt;uint32_t BlockSize, uint32_t WarpSize, typename T, typename F&gt;</span>
</span><span class="hll"><span class="gi">+__global__ __launch_bounds__(BlockSize) void kernel(</span>
</span><span class="w"> </span>   T* front,
<span class="w"> </span>   T* back,
<span class="w"> </span>   F op,
<span class="w"> </span>   T zero_elem,
<span class="w"> </span>   uint32_t front_size)
{
<span class="hll"><span class="gd">-    extern __shared__ T shared[];</span>
</span><span class="hll"><span class="gi">+    __shared__ T shared[BlockSize];</span>
</span>
<span class="w"> </span>   ...

<span class="w"> </span>   // Shared reduction
<span class="hll"><span class="gd">-    for (uint32_t i = blockDim.x / 2; i &gt; WarpSize; i /= 2)</span>
</span><span class="hll"><span class="gi">+    tmp::static_for&lt;BlockSize / 2, tmp::greater_than&lt;WarpSize&gt;, tmp::divide&lt;2&gt;&gt;([&amp;]&lt;int I&gt;()</span>
</span><span class="w"> </span>   {
<span class="hll"><span class="gd">-        if (tid &lt; i)</span>
</span><span class="hll"><span class="gd">-            shared[tid] = op(shared[tid], shared[tid + i]);</span>
</span><span class="hll"><span class="gi">+        if (tid &lt; I)</span>
</span><span class="hll"><span class="gi">+            shared[tid] = op(shared[tid], shared[tid + I]);</span>
</span><span class="w"> </span>       __syncthreads();
<span class="w"> </span>   }
<span class="hll"><span class="gi">+    );</span>
</span></pre></div>
</div>
<p>Introducing yet another template argument for the kernel and moving from <code class="docutils literal notranslate"><span class="pre">for</span></code> to <code class="docutils literal notranslate"><span class="pre">tmp::static_for</span></code> leads to the following two notable improvements:</p>
<ul class="simple">
<li><p>Introducing new attribute <code class="docutils literal notranslate"><span class="pre">__launch_bounds__(BlockSize)</span></code> to the kernel instructs the compiler that the kernel will only be launched using the designated block size. This implies that the launches of differing block sizes will fail. This allows the optimizer to enroll the <code class="docutils literal notranslate"><span class="pre">blockDim.x</span></code> variable in constant folding as well as get information about register usage.</p></li>
<li><p>Turning the block size into a compile-time constant allows you to statically allocate the shared memory.</p></li>
</ul>
</section>
<section id="communicate-using-warp-collective-functions">
<h3>Communicate using warp-collective functions<a class="headerlink" href="#communicate-using-warp-collective-functions" title="Link to this heading">#</a></h3>
<p>Shared memory provides a fast communication path within a block, however when performing reduction within the last warp, you can use faster means of communication, which is warp-collective or cross-lane functions. Instead of using the hardware-backed shared memory, you can directly copy between the local memory (registers) of each lane in a warp. This can be achieve using the shuffle functions.</p>
<p>See how to use <code class="docutils literal notranslate"><span class="pre">__shfl_down()</span></code>, which is one of the most restrictive but also the most structured communication schemes.</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="c1">// Warp reduction</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">WarpSize</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">T</span><span class="w"> </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">op</span><span class="p">(</span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="p">],</span><span class="w"> </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">WarpSize</span><span class="p">]);</span>
<span class="w">    </span><span class="n">tmp</span><span class="o">::</span><span class="n">static_for</span><span class="o">&lt;</span><span class="n">WarpSize</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="n">tmp</span><span class="o">::</span><span class="n">not_equal</span><span class="o">&lt;</span><span class="mi">0</span><span class="o">&gt;</span><span class="p">,</span><span class="w"> </span><span class="n">tmp</span><span class="o">::</span><span class="n">divide</span><span class="o">&lt;</span><span class="mi">2</span><span class="o">&gt;&gt;</span><span class="p">([</span><span class="o">&amp;</span><span class="p">]</span><span class="o">&lt;</span><span class="kt">int</span><span class="w"> </span><span class="n">Delta</span><span class="o">&gt;</span><span class="p">()</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">op</span><span class="p">(</span><span class="n">res</span><span class="p">,</span><span class="w"> </span><span class="n">__shfl_down</span><span class="p">(</span><span class="n">res</span><span class="p">,</span><span class="w"> </span><span class="n">Delta</span><span class="p">));</span>
<span class="w">    </span><span class="p">});</span>

<span class="w">    </span><span class="c1">// Write result from shared to back buffer</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span>
<span class="w">        </span><span class="n">back</span><span class="p">[</span><span class="n">bid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">res</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>Using warp-collective functions for communication requires the control flow to be uniform across warps, as the name warp-collective implies. Therefore, you can see that the thread ID is being checked outside the loop, but the result is written inside due to variable scoping.</p>
</section>
<section id="prefer-warp-communication-over-shared">
<h3>Prefer warp communication over shared<a class="headerlink" href="#prefer-warp-communication-over-shared" title="Link to this heading">#</a></h3>
<p>As mentioned in the previous step, communication between local memory is faster than shared memory. Instead of relying on the local memory only at the end of the tree-like reduction, a better approach is to turn the tree reduction inside out and perform multiple warp reductions in parallel on all active threads, thus communicating only their partial results through the shared memory.</p>
<figure class="align-default">
<img alt="Diagram demonstrating warp reduction" src="../_images/warp_reduction.svg" />
</figure>
<figure class="align-default">
<img alt="Diagram demonstrating warp reduction and results store in shared memory" src="../_images/warp_reduction_with_shared.svg" />
</figure>
<p>The kernel versions differ significantly enough to be described using a diff; use afresh instead.</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="k">template</span><span class="o">&lt;</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">BlockSize</span><span class="p">,</span><span class="w"> </span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">WarpSize</span><span class="p">,</span><span class="w"> </span><span class="k">typename</span><span class="w"> </span><span class="nc">T</span><span class="p">,</span><span class="w"> </span><span class="k">typename</span><span class="w"> </span><span class="nc">F</span><span class="o">&gt;</span>
<span class="n">__global__</span><span class="w"> </span><span class="n">__launch_bounds__</span><span class="p">(</span><span class="n">BlockSize</span><span class="p">)</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernel</span><span class="p">(</span>
<span class="w">    </span><span class="n">T</span><span class="o">*</span><span class="w"> </span><span class="n">front</span><span class="p">,</span>
<span class="w">    </span><span class="n">T</span><span class="o">*</span><span class="w"> </span><span class="n">back</span><span class="p">,</span>
<span class="w">    </span><span class="n">F</span><span class="w"> </span><span class="n">op</span><span class="p">,</span>
<span class="w">    </span><span class="n">T</span><span class="w"> </span><span class="n">zero_elem</span><span class="p">,</span>
<span class="w">    </span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">front_size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// ...</span>
<span class="p">}</span>
</pre></div>
</div>
<p>The kernel signature and the reduction factor are the same as in previous cases; only the implementation differs.</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="k">static</span><span class="w"> </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">WarpCount</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">BlockSize</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">WarpSize</span><span class="p">;</span>

<span class="n">__shared__</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">shared</span><span class="p">[</span><span class="n">WarpCount</span><span class="p">];</span>

<span class="k">auto</span><span class="w"> </span><span class="n">read_global_safe</span><span class="w"> </span><span class="o">=</span>
<span class="w">    </span><span class="p">[</span><span class="o">&amp;</span><span class="p">](</span><span class="k">const</span><span class="w"> </span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="k">return</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">front_size</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="n">front</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">zero_elem</span><span class="p">;</span><span class="w"> </span><span class="p">};</span>
<span class="k">auto</span><span class="w"> </span><span class="n">read_shared_safe</span><span class="w"> </span><span class="o">=</span>
<span class="w">    </span><span class="p">[</span><span class="o">&amp;</span><span class="p">](</span><span class="k">const</span><span class="w"> </span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="k">return</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">WarpCount</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="n">shared</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">zero_elem</span><span class="p">;</span><span class="w"> </span><span class="p">};</span>

<span class="k">const</span><span class="w"> </span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">,</span>
<span class="w">               </span><span class="n">bid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">,</span>
<span class="w">               </span><span class="n">gid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">bid</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="p">(</span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">2</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">tid</span><span class="p">,</span>
<span class="w">               </span><span class="n">wid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">WarpSize</span><span class="p">,</span>
<span class="w">               </span><span class="n">lid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="n">WarpSize</span><span class="p">;</span>

<span class="c1">// Read input from front buffer to local</span>
<span class="n">T</span><span class="w"> </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">op</span><span class="p">(</span><span class="n">read_global_safe</span><span class="p">(</span><span class="n">gid</span><span class="p">),</span><span class="w"> </span><span class="n">read_global_safe</span><span class="p">(</span><span class="n">gid</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="p">));</span>
</pre></div>
</div>
<p>As we communicate the results of warps through shared memory, the same number of elements are required in the shared memory as warps within the block. Similar to how you can only launch kernels at block granularity, you can only warp reduce with <code class="docutils literal notranslate"><span class="pre">WarpSize</span></code> granularity due to the collective nature of the cross-lane builtins. To address this, you can use <code class="docutils literal notranslate"><span class="pre">read_shared_safe</span></code> to pad overindexing by reading <code class="docutils literal notranslate"><span class="pre">zero_elem</span></code>. Reading from global remains unaffected.</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="c1">// Perform warp reductions and communicate results via shared</span>
<span class="c1">// for (uint32_t ActiveWarps = WarpCount;</span>
<span class="c1">//      ActiveWarps != 0;</span>
<span class="c1">//      ActiveWarps = ActiveWarps != 1 ?</span>
<span class="c1">//          divide_ceil(ActiveWarps, WarpSize) :</span>
<span class="c1">//          ActiveWarps = 0)</span>
<span class="n">tmp</span><span class="o">::</span><span class="n">static_for</span><span class="o">&lt;</span>
<span class="w">    </span><span class="n">WarpCount</span><span class="p">,</span>
<span class="w">    </span><span class="n">tmp</span><span class="o">::</span><span class="n">not_equal</span><span class="o">&lt;</span><span class="mi">0</span><span class="o">&gt;</span><span class="p">,</span>
<span class="w">    </span><span class="n">tmp</span><span class="o">::</span><span class="n">select</span><span class="o">&lt;</span>
<span class="w">        </span><span class="n">tmp</span><span class="o">::</span><span class="n">not_equal</span><span class="o">&lt;</span><span class="mi">1</span><span class="o">&gt;</span><span class="p">,</span>
<span class="w">        </span><span class="n">tmp</span><span class="o">::</span><span class="n">divide_ceil</span><span class="o">&lt;</span><span class="n">WarpSize</span><span class="o">&gt;</span><span class="p">,</span>
<span class="w">        </span><span class="n">tmp</span><span class="o">::</span><span class="n">constant</span><span class="o">&lt;</span><span class="mi">0</span><span class="o">&gt;&gt;&gt;</span><span class="p">([</span><span class="o">&amp;</span><span class="p">]</span><span class="o">&lt;</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">ActiveWarps</span><span class="o">&gt;</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">wid</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">ActiveWarps</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="c1">// Warp reduction</span>
<span class="w">        </span><span class="n">tmp</span><span class="o">::</span><span class="n">static_for</span><span class="o">&lt;</span><span class="n">WarpSize</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="n">tmp</span><span class="o">::</span><span class="n">not_equal</span><span class="o">&lt;</span><span class="mi">0</span><span class="o">&gt;</span><span class="p">,</span><span class="w"> </span><span class="n">tmp</span><span class="o">::</span><span class="n">divide</span><span class="o">&lt;</span><span class="mi">2</span><span class="o">&gt;&gt;</span><span class="p">([</span><span class="o">&amp;</span><span class="p">]</span><span class="o">&lt;</span><span class="kt">int</span><span class="w"> </span><span class="n">Delta</span><span class="o">&gt;</span><span class="p">()</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">op</span><span class="p">(</span><span class="n">res</span><span class="p">,</span><span class="w"> </span><span class="n">__shfl_down</span><span class="p">(</span><span class="n">res</span><span class="p">,</span><span class="w"> </span><span class="n">Delta</span><span class="p">));</span>
<span class="w">        </span><span class="p">});</span>

<span class="w">        </span><span class="c1">// Write warp result from local to shared</span>
<span class="w">        </span><span class="k">if</span><span class="p">(</span><span class="n">lid</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span>
<span class="w">            </span><span class="n">shared</span><span class="p">[</span><span class="n">wid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">res</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="n">__syncthreads</span><span class="p">();</span>

<span class="w">    </span><span class="c1">// Read warp result from shared to local</span>
<span class="w">    </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">read_shared_safe</span><span class="p">(</span><span class="n">tid</span><span class="p">);</span>
<span class="p">});</span>

<span class="c1">// Write result from local to back buffer</span>
<span class="k">if</span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span>
<span class="w">    </span><span class="n">back</span><span class="p">[</span><span class="n">bid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">res</span><span class="p">;</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">ActiveWarps</span></code> iterates from <code class="docutils literal notranslate"><span class="pre">WarpCount</span></code> until it reaches <code class="docutils literal notranslate"><span class="pre">0</span></code>. Every iteration of <code class="docutils literal notranslate"><span class="pre">ActiveWarps</span></code> reduces the <code class="docutils literal notranslate"><span class="pre">WarpSize</span></code>. In cases where the partial result count isn’t a divisor of <code class="docutils literal notranslate"><span class="pre">ActiveWarps</span></code> and you need to launch an extra warp, use <code class="docutils literal notranslate"><span class="pre">tmp::divide_ceil</span></code>, which always rounds to positive infinity. The tertiary <code class="docutils literal notranslate"><span class="pre">tmp::select</span></code> is required because such division never reaches <code class="docutils literal notranslate"><span class="pre">0</span></code>, so you must terminate the loop after the last warp concludes.</p>
<p>In each iteration, if the warp is active, which means it has at least a single valid input, it carries out a pass of warp reduction and writes output based on warp ID. Reading is carried out based on thread ID. Global output continues to be based on block ID.</p>
</section>
<section id="amortize-bookkeeping-variable-overhead">
<h3>Amortize bookkeeping variable overhead<a class="headerlink" href="#amortize-bookkeeping-variable-overhead" title="Link to this heading">#</a></h3>
<p>The previous sections explained how to reduce register usage to improve occupancy. This allows more blocks to execute in parallel on all multiprocessors, leading to more global store/load latency to be hidden. Reducing the number of kernels in flight while still carrying out the same workload reduces the wastage of registers while loading and maintaining bookkeeping variables such as kernel indices.</p>
<p>An example of this optimization is performing one binary <code class="docutils literal notranslate"><span class="pre">op</span></code> while loading input from global. Even though the operation is said to be carried out “in flight”, the two values are loaded into local memory (registers) before <code class="docutils literal notranslate"><span class="pre">op</span></code> is called.</p>
<p>A more general form of this optimization is wrapping most kernel logic in loops that carry out the workload of multiple kernel instances but require storing only a single instance of most of the bookkeeping logic. In code, this multiplicity factor is referred to via the <code class="docutils literal notranslate"><span class="pre">ItemsPerThread</span></code> compile-time constant, which is supplied by a template argument to allow for loop unrolling.</p>
<p>This kernel variant utilizes another generally applicable utility known as <code class="docutils literal notranslate"><span class="pre">hip::static_array</span></code>, which is a more restrictive wrapper over the builtin array than <code class="docutils literal notranslate"><span class="pre">std::array</span></code>, as it allows indexing only compile-time constants using the usual tuple-like <code class="docutils literal notranslate"><span class="pre">template</span> <span class="pre">&lt;size_t</span> <span class="pre">I&gt;</span> <span class="pre">auto</span> <span class="pre">get&lt;I&gt;(...)</span></code> interface.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>On a GPU, there is no stack, and the local memory is provisioned from the register file. This provisioning takes place statically. To paraphrase, the address range of a thread’s local memory is determined at compile-time. When an array is defined and used in the local storage, the compiler can only maintain its storage in the register file as long as all accesses to the array are computable by the compiler at compile-time. It doesn’t need to be a compile-time constant as long as the compiler can resolve the addresses of the accesses through constant folding or some other means. If the compiler fails to do so, the array will be backed by global memory, which is indicated by allocating a non-zero number of spill registers observable using static analysis tools. However, this is slower by the magnitude of multiple order. <code class="docutils literal notranslate"><span class="pre">hip::static_array</span></code> via its <code class="docutils literal notranslate"><span class="pre">hip::get&lt;&gt;</span></code> interface ensures that no such spills occur.</p>
</div>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="k">template</span><span class="o">&lt;</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">BlockSize</span><span class="p">,</span><span class="w"> </span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">WarpSize</span><span class="p">,</span><span class="w"> </span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">ItemsPerThread</span><span class="o">&gt;</span>
<span class="n">__global__</span><span class="w"> </span><span class="k">static</span><span class="w"> </span><span class="n">__launch_bounds__</span><span class="p">(</span><span class="n">BlockSize</span><span class="p">)</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernel</span><span class="p">(...)</span>
</pre></div>
</div>
<p>The kernel now has three compile-time configurable parameters. The only part of the kernel that changes depends on how you load data from global and perform the binary operation on those loaded values. So, the following step to read input from front buffer to global is now split into two steps: <a class="reference internal" href="#reading-items"><span class="std std-ref">Reading ItemsPerThread</span></a> and <a class="reference internal" href="#processing-items"><span class="std std-ref">Processing ItemsPerThread</span></a> .</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="c1">// Read input from front buffer to local</span>
<span class="n">T</span><span class="w"> </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">op</span><span class="p">(</span><span class="n">read_global_safe</span><span class="p">(</span><span class="n">gid</span><span class="p">),</span><span class="w"> </span><span class="n">read_global_safe</span><span class="p">(</span><span class="n">gid</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="p">));</span>
</pre></div>
</div>
<section id="reading-itemsperthread">
<span id="reading-items"></span><h4>Reading <code class="docutils literal notranslate"><span class="pre">ItemsPerThread</span></code><a class="headerlink" href="#reading-itemsperthread" title="Link to this heading">#</a></h4>
<p>The change to reading happens inside <cite>read_global_safe</cite>:</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="k">auto</span><span class="w"> </span><span class="n">read_global_safe</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="o">&amp;</span><span class="p">](</span><span class="k">const</span><span class="w"> </span><span class="kt">int32_t</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">hip</span><span class="o">::</span><span class="n">static_array</span><span class="o">&lt;</span><span class="n">T</span><span class="p">,</span><span class="w"> </span><span class="n">ItemsPerThread</span><span class="o">&gt;</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="p">[</span><span class="o">&amp;</span><span class="p">]</span><span class="o">&lt;</span><span class="kt">int32_t</span><span class="p">...</span><span class="w"> </span><span class="n">I</span><span class="o">&gt;</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">integer_sequence</span><span class="o">&lt;</span><span class="kt">int32_t</span><span class="p">,</span><span class="w"> </span><span class="n">I</span><span class="p">...</span><span class="o">&gt;</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">ItemsPerThread</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">front_size</span><span class="p">)</span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="n">hip</span><span class="o">::</span><span class="n">static_array</span><span class="o">&lt;</span><span class="n">T</span><span class="p">,</span><span class="w"> </span><span class="n">ItemsPerThread</span><span class="o">&gt;</span><span class="p">{</span>
<span class="w">                </span><span class="n">front</span><span class="p">[</span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">I</span><span class="p">]...</span>
<span class="w">            </span><span class="p">};</span>
<span class="w">        </span><span class="k">else</span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="n">hip</span><span class="o">::</span><span class="n">static_array</span><span class="o">&lt;</span><span class="n">T</span><span class="p">,</span><span class="w"> </span><span class="n">ItemsPerThread</span><span class="o">&gt;</span><span class="p">{</span>
<span class="w">                </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">I</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">front_size</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="n">front</span><span class="p">[</span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">I</span><span class="p">]</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">zero_elem</span><span class="p">)...</span>
<span class="w">            </span><span class="p">};</span>
<span class="w">    </span><span class="p">}(</span><span class="n">std</span><span class="o">::</span><span class="n">make_integer_sequence</span><span class="o">&lt;</span><span class="kt">int32_t</span><span class="p">,</span><span class="w"> </span><span class="n">ItemsPerThread</span><span class="o">&gt;</span><span class="p">());</span>
<span class="p">};</span>
</pre></div>
</div>
<p>Note that each array element is being loaded consecutively without the flexibility of a configurable <code class="docutils literal notranslate"><span class="pre">ItemsPerThread</span></code> property. This is morally equivalent to:</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="n">T</span><span class="w"> </span><span class="n">arr</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">front</span><span class="p">[</span><span class="n">gid</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">0</span><span class="p">],</span>
<span class="w">    </span><span class="n">front</span><span class="p">[</span><span class="n">gid</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="p">],</span>
<span class="w">    </span><span class="n">front</span><span class="p">[</span><span class="n">gid</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">2</span><span class="p">],</span>
<span class="w">    </span><span class="n">front</span><span class="p">[</span><span class="n">gid</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">3</span><span class="p">]</span>
<span class="p">}</span>
</pre></div>
</div>
<p>This is exactly what’s happening in the <code class="docutils literal notranslate"><span class="pre">front[i</span> <span class="pre">+</span> <span class="pre">I]...</span></code> fold-expression. However, this can only be issued if the entire read operates on real input without padding using <code class="docutils literal notranslate"><span class="pre">zero_elem</span></code>. If some reads over-index the input, the read turns into:</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="n">T</span><span class="w"> </span><span class="n">arr</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">0</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">front_size</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="n">front</span><span class="p">[</span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">zero_elem</span><span class="p">,</span>
<span class="w">    </span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">front_size</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="n">front</span><span class="p">[</span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="p">]</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">zero_elem</span><span class="p">,</span>
<span class="w">    </span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">2</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">front_size</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="n">front</span><span class="p">[</span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">2</span><span class="p">]</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">zero_elem</span><span class="p">,</span>
<span class="w">    </span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">3</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">front_size</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="n">front</span><span class="p">[</span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">3</span><span class="p">]</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">zero_elem</span>
<span class="p">}</span>
</pre></div>
</div>
<p>This makes it easier for the compiler to recognize vector loads from global. As the performance at large is dominated by how you move the data, it’s only natural to utilize dedicated instructions to move more data with less binary. This is evident by the huge performance improvement when loading two values per thread. For more information, see <a class="reference external" href="https://godbolt.org/z/b36Eea69q">the compiler explorer</a> to learn how loading for AMD (both RDNA and CDNA) compiles to <code class="docutils literal notranslate"><span class="pre">global_load_dwordx4</span></code>, where <code class="docutils literal notranslate"><span class="pre">x4</span></code> denotes the 4-vector variant of the instruction.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Note that <code class="docutils literal notranslate"><span class="pre">read_global_safe</span></code>, which used to take an <code class="docutils literal notranslate"><span class="pre">uint32_t</span></code> as the index type, now takes a signed integer. When indexing an array with unsigned integers, the compiler has to handle integer overflows, as the C/C++ standards defined them. It might happen that some part of the vector load indices overflow, thus resulting in a non-contiguous read. If you change the previously linked code to use an unsigned integer as the thread ID, the compiler won’t emit a vector load. Signed integer overflow is an undefined behavior, and hence, unknown to the optimizer. To convey the absence of overflow to the compiler with unsigned indices, add <code class="docutils literal notranslate"><span class="pre">__builtin_assume(gid</span> <span class="pre">+</span> <span class="pre">4</span> <span class="pre">&gt;</span> <span class="pre">gid)</span></code>, or the more portable <code class="docutils literal notranslate"><span class="pre">[[assume]](gid</span> <span class="pre">+</span> <span class="pre">4</span> <span class="pre">&gt;</span> <span class="pre">gid)</span></code>, once <code class="docutils literal notranslate"><span class="pre">amdclang++</span></code> supports it.</p>
</div>
<p><code class="docutils literal notranslate"><span class="pre">read_global_safe</span></code> implementation is an Immediately Invoked Lambda Expression (IILE), because <code class="docutils literal notranslate"><span class="pre">ItemsPerThread</span></code> is an integer value, while you need a compile-time <code class="docutils literal notranslate"><span class="pre">iota</span></code>-like sequence of integers as a pack for the fold-expressions to expand on. This can only occur as part of template argument deduction on the IILE.</p>
</section>
<section id="processing-itemsperthread">
<span id="processing-items"></span><h4>Processing <code class="docutils literal notranslate"><span class="pre">ItemsPerThread</span></code><a class="headerlink" href="#processing-itemsperthread" title="Link to this heading">#</a></h4>
<p>Once the kernel reads <code class="docutils literal notranslate"><span class="pre">ItemsPerThread</span></code> number of inputs to local, it immediately reduces them to a scalar. There is no reason to propagate the input element multiplicity to the warp reduction phase.</p>
<div class="highlight-C++ notranslate"><div class="highlight"><pre><span></span><span class="n">T</span><span class="w"> </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="o">&amp;</span><span class="p">]()</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// Read input from front buffer to local</span>
<span class="w">    </span><span class="n">hip</span><span class="o">::</span><span class="n">static_array</span><span class="o">&lt;</span><span class="n">T</span><span class="p">,</span><span class="w"> </span><span class="n">ItemsPerThread</span><span class="o">&gt;</span><span class="w"> </span><span class="n">arr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">read_global_safe</span><span class="p">(</span><span class="n">gid</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Reduce ItemsPerThread to scalar</span>
<span class="w">    </span><span class="n">tmp</span><span class="o">::</span><span class="n">static_for</span><span class="o">&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">tmp</span><span class="o">::</span><span class="n">less_than</span><span class="o">&lt;</span><span class="n">ItemsPerThread</span><span class="o">&gt;</span><span class="p">,</span><span class="w"> </span><span class="n">tmp</span><span class="o">::</span><span class="n">increment</span><span class="o">&lt;</span><span class="mi">1</span><span class="o">&gt;&gt;</span><span class="p">([</span><span class="o">&amp;</span><span class="p">]</span><span class="o">&lt;</span><span class="kt">int</span><span class="w"> </span><span class="n">I</span><span class="o">&gt;</span><span class="p">()</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">get</span><span class="o">&lt;</span><span class="mi">0</span><span class="o">&gt;</span><span class="p">(</span><span class="n">arr</span><span class="p">)</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">op</span><span class="p">(</span><span class="n">get</span><span class="o">&lt;</span><span class="mi">0</span><span class="o">&gt;</span><span class="p">(</span><span class="n">arr</span><span class="p">),</span><span class="w"> </span><span class="n">get</span><span class="o">&lt;</span><span class="n">I</span><span class="o">&gt;</span><span class="p">(</span><span class="n">arr</span><span class="p">));</span>
<span class="w">    </span><span class="p">});</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">get</span><span class="o">&lt;</span><span class="mi">0</span><span class="o">&gt;</span><span class="p">(</span><span class="n">arr</span><span class="p">);</span>
<span class="p">}();</span>
</pre></div>
</div>
</section>
</section>
<section id="two-pass-reduction">
<h3>Two-pass reduction<a class="headerlink" href="#two-pass-reduction" title="Link to this heading">#</a></h3>
<p>Alter kernel launch and input fetching such that no more blocks are launched than what a subsequent kernel launch’s single block can conveniently reduce, while performing multiple passes of input reading from global and combining their results before engaging in the end game tree-like reduction.</p>
<p>With this method, you can save at least one to two kernel launches for large inputs.</p>
</section>
<section id="global-data-share">
<h3>Global data share<a class="headerlink" href="#global-data-share" title="Link to this heading">#</a></h3>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This modification can only be executed on AMD hardware.</p>
</div>
<p>Perform the first step of the two-pass reduction, but in the end, instead of writing to global and reading it back in a subsequent kernel, write the partial results to the Global Data Share (GDS). This is an <code class="docutils literal notranslate"><span class="pre">N+1</span></code> th shared memory that is accessed by all multiprocessors and is also on-chip memory.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The API doesn’t guarantee the order in which blocks are scheduled even though all GPUs schedule them in the same monotonically increasing order of block ids. Relying on this implicitly, the last block of a grid is in the optimal position to observe the side effects of all other blocks (using spinlocks or other methods) without occupying a multiprocessor for longer than necessary.</p>
</div>
<p>Without launching a second kernel, you can make the last block collect the results of all other blocks from GDS by implicitly exploiting the scheduling behavior or relying on another AMD-specific feature called Global Wave Sync (GWS) to merge them for a final tree-like reduction.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>GDS and GWS are reserved runtime features that the HIP API doesn’t cover. Invoking these functionalities requires inline AMDGCN assembly. Moreover, the fact that the runtime doesn’t virtualize the GDS, imposes further restrictions on concurrent scheduling of other kernels.</p>
</div>
</section>
</section>
<section id="conclusion">
<h2>Conclusion<a class="headerlink" href="#conclusion" title="Link to this heading">#</a></h2>
<p>Optimizing code on GPUs, like on any other architecture, requires careful consideration and balancing of resources and costs of various operations to obtain optimal performance. This document explored optimizing reductions much beyond the territory of diminishing returns. This approach introduced multiple optimization techniques and discussed opportunities.</p>
<p>The document focused on reductions when an entire device participates in it. Still, the choice of optimal compile-time constants or even the algorithm itself might not be optimal when its multiple blocks participate in multiple parallel reductions or when each thread performs its reduction. However, when multiple devices participate in the same reduction, other aspects must be considered.</p>
<p>Most solutions, including the ones covered in this document, are given to the end users in a turnkey fashion via algorithm primitive libraries. These solutions might not be the fastest in all cases, but they are close to being the gold standard for carrying out certain operations as reasonably as possible.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="programming-patterns/multikernel_bfs.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Multi-kernel programming: breadth-first search tutorial</p>
      </div>
    </a>
    <a class="right-next"
       href="cooperative_groups_tutorial.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Cooperative groups</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#the-algorithm">The algorithm</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#reduction-on-gpus">Reduction on GPUs</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#naive-shared-reduction">Naive shared reduction</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#reducing-thread-divergence">Reducing thread divergence</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#resolving-bank-conflicts">Resolving bank conflicts</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#utilize-upper-half-of-the-block">Utilize upper half of the block</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#unroll-all-loops">Unroll all loops</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#communicate-using-warp-collective-functions">Communicate using warp-collective functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#prefer-warp-communication-over-shared">Prefer warp communication over shared</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amortize-bookkeeping-variable-overhead">Amortize bookkeeping variable overhead</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#reading-itemsperthread">Reading <code class="docutils literal notranslate"><span class="pre">ItemsPerThread</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#processing-itemsperthread">Processing <code class="docutils literal notranslate"><span class="pre">ItemsPerThread</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#two-pass-reduction">Two-pass reduction</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#global-data-share">Global data share</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#conclusion">Conclusion</a></li>
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
