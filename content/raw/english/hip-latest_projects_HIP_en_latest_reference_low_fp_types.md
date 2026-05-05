---
title: "Low precision floating point types &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/low_fp_types.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:07:37.402109+00:00
content_hash: "317c4e3fce7a5613"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="This page describes the FP8 and FP16 types present in HIP." name="description" />
<meta content="AMD, ROCm, HIP, fp8, fnuz, ocp" name="keywords" />

    <title>Low precision floating point types &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/low_fp_types';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Hardware features" href="hardware_features.html" />
    <link rel="prev" title="HIP deprecated runtime API functions" href="deprecated_api_list.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/low_fp_types.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<ul class="current nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="hip_runtime_api_reference.html">HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2 has-children"><a class="reference internal" href="hip_runtime_api/modules.html">Modules</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/initialization_and_version.html">Initialization and version</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/device_management.html">Device management</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/execution_control.html">Execution control</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/error_handling.html">Error handling</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/stream_management.html">Stream management</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/stream_memory_operations.html">Stream memory operations</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/event_management.html">Event management</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="hip_runtime_api/modules/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/memory_management_deprecated.html">Memory management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/external_resource_interoperability.html">External resource interoperability</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html">Stream ordered memory allocator</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/unified_memory_reference.html">Managed memory</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/virtual_memory_reference.html">Virtual memory management</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/texture_management.html">Texture management</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/texture_management_deprecated.html">Texture management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/surface_object.html">Surface object</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/peer_to_peer_device_memory_access.html">Peer to peer device memory access</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/context_management.html">Context management [deprecated]</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/module_management.html">Module management</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/occupancy.html">Occupancy</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/profiler_control.html">Profiler control</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/launch_api.html">Launch API</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/runtime_compilation.html">Runtime compilation</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/callback_activity_apis.html">Callback activity APIs</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/graph_management.html">Graph management</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/graphics_interoperability.html">Graphics interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/opengl_interoperability.html">OpenGL interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/cooperative_groups_reference.html">Cooperative groups</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="hip_runtime_api/global_defines_enums_structs_files.html">Global defines, enums, structs and files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/group___global_defs.html">Global enum and defines</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/group___driver_types.html">Driver Types</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/files.html">File List</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="math_api.html">HIP math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="complex_math_api.html">HIP complex math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="env_variables.html">HIP environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="error_codes.html">HIP error codes</a></li>
<li class="toctree-l1"><a class="reference internal" href="api_syntax.html">CUDA to HIP API Function Comparison</a></li>
<li class="toctree-l1"><a class="reference internal" href="deprecated_api_list.html">List of deprecated APIs</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Low Precision Floating Point Types</a></li>
<li class="toctree-l1"><a class="reference internal" href="hardware_features.html">Hardware features</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Tutorials</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic">HIP basic examples</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples">HIP examples</a></li>
<li class="toctree-l1"><a class="reference internal" href="../tutorial/saxpy.html">SAXPY - Hello, HIP</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../tutorial/programming-patterns.html">GPU programming patterns</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../tutorial/programming-patterns/matrix_multiplication.html">Two-dimensional kernels: Matrix multiplication tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../tutorial/programming-patterns/atomic_operations_histogram.html">Atomic operations: Histogram tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../tutorial/programming-patterns/cpu_gpu_kmeans.html">CPU-GPU cooperative computing: K-means clustering tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../tutorial/programming-patterns/stencil_operations.html">Stencil operations: Image convolution tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../tutorial/programming-patterns/multikernel_bfs.html">Multi-kernel programming: breadth-first search tutorial</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../tutorial/reduction.html">Reduction</a></li>
<li class="toctree-l1"><a class="reference internal" href="../tutorial/cooperative_groups_tutorial.html">Cooperative groups</a></li>
<li class="toctree-l1"><a class="reference internal" href="../tutorial/graph_api.html">HIP Graph API Tutorial</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">Low...</li>
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
    <h1>Low precision floating point types</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#fp4-4-bit-precision">FP4 (4-bit Precision)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-header">HIP Header</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#device-compatibility">Device Compatibility</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-fp4-numbers-in-hip-programs">Using FP4 Numbers in HIP Programs</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#fp6-6-bit-precision">FP6 (6-bit Precision)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">HIP Header</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id2">Device Compatibility</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-fp6-numbers-in-hip-programs">Using FP6 Numbers in HIP Programs</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#fp8-quarter-precision">FP8 (Quarter Precision)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id3">HIP Header</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id4">Device Compatibility</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-fp8-numbers-in-hip-programs">Using FP8 Numbers in HIP Programs</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#float16-half-precision">Float16 (Half Precision)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#float16-format">Float16 Format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id5">HIP Header</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id6">Device Compatibility</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-float16-numbers-in-hip-programs">Using Float16 Numbers in HIP Programs</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#c-style-classes">C++ Style Classes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#vector-support">Vector Support</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#bfloat16-brain-float-16-bit-precision">BFloat16 (Brain float 16-bit precision)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#bfloat16-format">BFloat16 Format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id7">HIP Header</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id8">Device Compatibility</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-bfloat16-numbers-in-hip-programs">Using <code class="docutils literal notranslate"><span class="pre">bfloat16</span></code> Numbers in HIP Programs</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id9">C++ Style Classes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id10">Vector Support</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-extensions">HIP Extensions</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hipext-types">hipExt Types</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#c-apis">C-APIs</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-ext-c-api">HIP EXT C++ API</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="low-precision-floating-point-types">
<h1>Low precision floating point types<a class="headerlink" href="#low-precision-floating-point-types" title="Link to this heading">#</a></h1>
<p>Modern computing tasks often require balancing numerical precision against hardware resources
and processing speed. Low precision floating point number formats in HIP include FP8 (Quarter Precision)
and FP16 (Half Precision), which reduce memory and bandwidth requirements compared to traditional
32-bit or 64-bit formats. The following sections detail their specifications, variants, and provide
practical guidance for implementation in HIP.</p>
<section id="fp4-4-bit-precision">
<h2>FP4 (4-bit Precision)<a class="headerlink" href="#fp4-4-bit-precision" title="Link to this heading">#</a></h2>
<p>FP4 (Floating Point 4-bit) numbers represent the current extreme in low-precision formats,
pushing the boundaries of memory optimization for specialized AI workloads. This ultra-compact
format is designed for scenarios where model size and computational efficiency are paramount
constraints, even at the cost of significant precision reduction.</p>
<p>FP4 is particularly valuable in weight storage for large language models (LLMs) and vision
transformers, where aggressive quantization can dramatically reduce model size while
maintaining acceptable inference quality. By reducing memory footprint to a quarter of FP16,
FP4 enables deployment of larger models in memory-constrained environments or higher throughput
in existing hardware.</p>
<p>The supported FP4 format is:</p>
<ul class="simple">
<li><p><strong>E2M1 Format</strong></p>
<ul>
<li><p>Sign: 1 bit</p></li>
<li><p>Exponent: 2 bits</p></li>
<li><p>Mantissa: 1 bit</p></li>
</ul>
</li>
</ul>
<p>The E2M1 format offers a balance between minimal precision and a reasonable dynamic range,
optimized for weight storage in neural network applications.</p>
<section id="hip-header">
<h3>HIP Header<a class="headerlink" href="#hip-header" title="Link to this heading">#</a></h3>
<p>The <a class="reference external" href="https://github.com/ROCm/clr/blob/amd-staging/hipamd/include/hip/amd_detail/amd_hip_fp4.h">HIP FP4 header</a>
defines the FP4 numbers.</p>
</section>
<section id="device-compatibility">
<h3>Device Compatibility<a class="headerlink" href="#device-compatibility" title="Link to this heading">#</a></h3>
<p>The following table shows hardware support for this precision format by GPU architecture. “Yes”
indicates native hardware acceleration is available, while “No” indicates hardware acceleration
is not available.</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Device Type</p></th>
<th class="head"><p>E2M1</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>CDNA1</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-odd"><td><p>CDNA2</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-even"><td><p>CDNA3</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-odd"><td><p>CDNA4</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="row-even"><td><p>RDNA2</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-odd"><td><p>RDNA3</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-even"><td><p>RDNA4</p></td>
<td><p>No</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="using-fp4-numbers-in-hip-programs">
<h3>Using FP4 Numbers in HIP Programs<a class="headerlink" href="#using-fp4-numbers-in-hip-programs" title="Link to this heading">#</a></h3>
<p>To use the FP4 numbers inside HIP programs:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_fp4.h&gt;</span>
</pre></div>
</div>
<p>FP4 numbers can be used on CPU side:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__hip_fp4_storage_t</span><span class="w"> </span><span class="nf">convert_float_to_fp4</span><span class="p">(</span>
<span class="w">  </span><span class="kt">float</span><span class="w"> </span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="cm">/* Input val */</span>
<span class="w">  </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="w"> </span><span class="cm">/* Saturation behavior */</span>
<span class="w">  </span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="k">return</span><span class="w"> </span><span class="n">__hip_cvt_float_to_fp4</span><span class="p">(</span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="n">__HIP_E2M1</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p>The same can be done in kernels as well:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__device__</span><span class="w"> </span><span class="n">__hip_fp4_storage_t</span><span class="w"> </span><span class="n">d_convert_float_to_fp4</span><span class="p">(</span>
<span class="w">  </span><span class="kt">float</span><span class="w"> </span><span class="n">in</span><span class="p">,</span>
<span class="w">  </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="k">return</span><span class="w"> </span><span class="n">__hip_cvt_float_to_fp4</span><span class="p">(</span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="n">__HIP_E2M1</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p>The following code example demonstrates a simple roundtrip conversion using FP4 types:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_fp4.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>

<span class="cp">#define hip_check(hip_call)                                                    \</span>
<span class="cp">{                                                                              \</span>
<span class="cp">    auto hip_res = hip_call;                                                   \</span>
<span class="cp">    if (hip_res != hipSuccess) {                                               \</span>
<span class="cp">      std::cerr &lt;&lt; &quot;Failed in HIP call: &quot; &lt;&lt; #hip_call \</span>
<span class="cp">                &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot; &lt;&lt; __LINE__ \</span>
<span class="cp">                &lt;&lt; &quot; with error: &quot; &lt;&lt; hipGetErrorString(hip_res) &lt;&lt; std::endl; \</span>
<span class="cp">      std::abort();                                                            \</span>
<span class="cp">    }                                                                          \</span>
<span class="cp">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">float_to_fp4_to_float</span><span class="p">(</span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">in</span><span class="p">,</span>
<span class="w">                                    </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="p">,</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">out</span><span class="p">,</span>
<span class="w">                                    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">auto</span><span class="w"> </span><span class="n">fp4</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__hip_cvt_float_to_fp4</span><span class="p">(</span><span class="n">in</span><span class="p">[</span><span class="n">i</span><span class="p">],</span><span class="w"> </span><span class="n">__HIP_E2M1</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">);</span>
<span class="w">        </span><span class="n">out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__hip_cvt_fp4_to_halfraw</span><span class="p">(</span><span class="n">fp4</span><span class="p">,</span><span class="w"> </span><span class="n">__HIP_E2M1</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">16</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipDeviceProp_t</span><span class="w"> </span><span class="n">prop</span><span class="p">;</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipGetDeviceProperties</span><span class="p">(</span><span class="o">&amp;</span><span class="n">prop</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">is_supported</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="p">(</span><span class="n">prop</span><span class="p">.</span><span class="n">gcnArchName</span><span class="p">).</span><span class="n">find</span><span class="p">(</span><span class="s">&quot;gfx950&quot;</span><span class="p">)</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="o">::</span><span class="n">npos</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="o">!</span><span class="n">is_supported</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Need gfx950, but found: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">prop</span><span class="p">.</span><span class="n">gcnArchName</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Device conversions are not supported on this hardware.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">-1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__HIP_SATFINITE</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Create test data</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">in</span><span class="p">;</span>
<span class="w">    </span><span class="n">in</span><span class="p">.</span><span class="n">reserve</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">in</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mf">0.5f</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Allocate device memory</span>
<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">d_out</span><span class="p">;</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="n">in</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Run conversion kernel</span>
<span class="w">    </span><span class="n">float_to_fp4_to_float</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">,</span><span class="w"> </span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Get results</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">result</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">result</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Clean up</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_in</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_out</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Display results</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;FP4 Roundtrip Results:&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Original: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">in</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; -&gt; FP4 roundtrip: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">result</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>There are C++ style classes available as well:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__hip_fp4_e2m1</span><span class="w"> </span><span class="nf">fp4_val</span><span class="p">(</span><span class="mf">1.0f</span><span class="p">);</span>
</pre></div>
</div>
<p>FP4 type has its own class:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp4_e2m1</span></code></p></li>
</ul>
<p>There is support of vector of FP4 types:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp4x2_e2m1</span></code>: holds 2 values of FP4 e2m1 numbers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp4x4_e2m1</span></code>: holds 4 values of FP4 e2m1 numbers</p></li>
</ul>
</section>
</section>
<section id="fp6-6-bit-precision">
<h2>FP6 (6-bit Precision)<a class="headerlink" href="#fp6-6-bit-precision" title="Link to this heading">#</a></h2>
<p>FP6 (Floating Point 6-bit) numbers represent an even more aggressive memory optimization
compared to FP8, designed specifically for ultra-efficient deep learning inference and
specialized AI applications. This extremely compact format delivers significant memory
and bandwidth savings at the cost of reduced dynamic range and precision.</p>
<p>The primary advantage of FP6 is enabling higher computational throughput in
hardware-constrained environments, particularly for AI model deployment on edge devices
and applications where model size is a critical constraint. While offering less precision
than FP8, FP6 maintains sufficient accuracy for many inference tasks, especially when
used with carefully quantized models.</p>
<p>There are two primary FP6 formats:</p>
<ul class="simple">
<li><p><strong>E3M2 Format</strong></p>
<ul>
<li><p>Sign: 1 bit</p></li>
<li><p>Exponent: 3 bits</p></li>
<li><p>Mantissa: 2 bits</p></li>
</ul>
</li>
<li><p><strong>E2M3 Format</strong></p>
<ul>
<li><p>Sign: 1 bit</p></li>
<li><p>Exponent: 2 bits</p></li>
<li><p>Mantissa: 3 bits</p></li>
</ul>
</li>
</ul>
<p>The E3M2 format provides a wider numeric range with less precision, while the E2M3 format
offers higher precision within a narrower range.</p>
<section id="id1">
<h3>HIP Header<a class="headerlink" href="#id1" title="Link to this heading">#</a></h3>
<p>The <a class="reference external" href="https://github.com/ROCm/clr/blob/amd-staging/hipamd/include/hip/amd_detail/amd_hip_fp6.h">HIP FP6 header</a>
defines the FP6 numbers.</p>
</section>
<section id="id2">
<h3>Device Compatibility<a class="headerlink" href="#id2" title="Link to this heading">#</a></h3>
<p>The following table shows hardware support for this precision format by GPU architecture. “Yes”
indicates native hardware acceleration is available, while “No” indicates hardware acceleration
is not available.</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Device Type</p></th>
<th class="head"><p>E3M2</p></th>
<th class="head"><p>E2M3</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>CDNA1</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-odd"><td><p>CDNA2</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-even"><td><p>CDNA3</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-odd"><td><p>CDNA4</p></td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="row-even"><td><p>RDNA2</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-odd"><td><p>RDNA3</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-even"><td><p>RDNA4</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="using-fp6-numbers-in-hip-programs">
<h3>Using FP6 Numbers in HIP Programs<a class="headerlink" href="#using-fp6-numbers-in-hip-programs" title="Link to this heading">#</a></h3>
<p>To use the FP6 numbers inside HIP programs:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_fp6.h&gt;</span>
</pre></div>
</div>
<p>FP6 numbers can be used on CPU side:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__hip_fp6_storage_t</span><span class="w"> </span><span class="nf">convert_float_to_fp6</span><span class="p">(</span>
<span class="w">  </span><span class="kt">float</span><span class="w"> </span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="cm">/* Input val */</span>
<span class="w">  </span><span class="n">__hip_fp6_interpretation_t</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span><span class="w"> </span><span class="cm">/* interpretation of number E3M2/E2M3 */</span>
<span class="w">  </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="w"> </span><span class="cm">/* Saturation behavior */</span>
<span class="w">  </span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="k">return</span><span class="w"> </span><span class="n">__hip_cvt_float_to_fp6</span><span class="p">(</span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p>The same can be done in kernels as well:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__device__</span><span class="w"> </span><span class="n">__hip_fp6_storage_t</span><span class="w"> </span><span class="n">d_convert_float_to_fp6</span><span class="p">(</span>
<span class="w">  </span><span class="kt">float</span><span class="w"> </span><span class="n">in</span><span class="p">,</span>
<span class="w">  </span><span class="n">__hip_fp6_interpretation_t</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span>
<span class="w">  </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="k">return</span><span class="w"> </span><span class="n">__hip_cvt_float_to_fp6</span><span class="p">(</span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p>The following code example demonstrates a roundtrip conversion using FP6 types:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_fp6.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>

<span class="cp">#define hip_check(hip_call)                                                    \</span>
<span class="cp">{                                                                              \</span>
<span class="cp">    auto hip_res = hip_call;                                                   \</span>
<span class="cp">    if (hip_res != hipSuccess) {                                               \</span>
<span class="cp">      std::cerr &lt;&lt; &quot;Failed in HIP call: &quot; &lt;&lt; #hip_call \</span>
<span class="cp">                &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot; &lt;&lt; __LINE__ \</span>
<span class="cp">                &lt;&lt; &quot; with error: &quot; &lt;&lt; hipGetErrorString(hip_res) &lt;&lt; std::endl; \</span>
<span class="cp">      std::abort();                                                            \</span>
<span class="cp">    }                                                                          \</span>
<span class="cp">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">float_to_fp6_to_float</span><span class="p">(</span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">in</span><span class="p">,</span>
<span class="w">                                    </span><span class="n">__hip_fp6_interpretation_t</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span>
<span class="w">                                    </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="p">,</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">out</span><span class="p">,</span>
<span class="w">                                    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">auto</span><span class="w"> </span><span class="n">fp6</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__hip_cvt_float_to_fp6</span><span class="p">(</span><span class="n">in</span><span class="p">[</span><span class="n">i</span><span class="p">],</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">);</span>
<span class="w">        </span><span class="n">out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__hip_cvt_fp6_to_halfraw</span><span class="p">(</span><span class="n">fp6</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">16</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipDeviceProp_t</span><span class="w"> </span><span class="n">prop</span><span class="p">;</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipGetDeviceProperties</span><span class="p">(</span><span class="o">&amp;</span><span class="n">prop</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">is_supported</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="p">(</span><span class="n">prop</span><span class="p">.</span><span class="n">gcnArchName</span><span class="p">).</span><span class="n">find</span><span class="p">(</span><span class="s">&quot;gfx950&quot;</span><span class="p">)</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="o">::</span><span class="n">npos</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="o">!</span><span class="n">is_supported</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Need gfx950, but found: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">prop</span><span class="p">.</span><span class="n">gcnArchName</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Device conversions are not supported on this hardware.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">-1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Test both formats</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__HIP_SATFINITE</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Create test vectors</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">in</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">in</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mf">0.5f</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">out_e2m3</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">out_e3m2</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Allocate device memory</span>
<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">d_out</span><span class="p">;</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="n">in</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Test E2M3 format</span>
<span class="w">    </span><span class="n">float_to_fp6_to_float</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="n">__HIP_E2M3</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">,</span><span class="w"> </span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">out_e2m3</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Test E3M2 format</span>
<span class="w">    </span><span class="n">float_to_fp6_to_float</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="n">__HIP_E3M2</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">,</span><span class="w"> </span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">out_e3m2</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Display results</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;FP6 Roundtrip Results:&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Original: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">in</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
<span class="w">                  </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; -&gt; E2M3: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">out_e2m3</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
<span class="w">                  </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; -&gt; E3M2: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">out_e3m2</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Clean up</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_in</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_out</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>There are C++ style classes available as well:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__hip_fp6_e2m3</span><span class="w"> </span><span class="nf">fp6_val_e2m3</span><span class="p">(</span><span class="mf">1.1f</span><span class="p">);</span>
<span class="n">__hip_fp6_e3m2</span><span class="w"> </span><span class="nf">fp6_val_e3m2</span><span class="p">(</span><span class="mf">1.1f</span><span class="p">);</span>
</pre></div>
</div>
<p>Each type of FP6 number has its own class:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp6_e2m3</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp6_e3m2</span></code></p></li>
</ul>
<p>There is support of vector of FP6 types:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp6x2_e2m3</span></code>: holds 2 values of FP6 e2m3 numbers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp6x4_e2m3</span></code>: holds 4 values of FP6 e2m3 numbers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp6x2_e3m2</span></code>: holds 2 values of FP6 e3m2 numbers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp6x4_e3m2</span></code>: holds 4 values of FP6 e3m2 numbers</p></li>
</ul>
</section>
</section>
<section id="fp8-quarter-precision">
<h2>FP8 (Quarter Precision)<a class="headerlink" href="#fp8-quarter-precision" title="Link to this heading">#</a></h2>
<p><a class="reference external" href="https://arxiv.org/pdf/2209.05433">FP8 (Floating Point 8-bit) numbers</a> were introduced
as a compact numerical format specifically tailored for deep learning inference. By reducing
precision while maintaining computational effectiveness, FP8 allows for significant memory
savings and improved processing speed. This makes it particularly beneficial for deploying
large-scale models with strict efficiency constraints.</p>
<p>Unlike traditional floating-point formats such as FP32 or even FP16, FP8 further optimizes
performance by enabling a higher volume of matrix operations per second. Its reduced bit-width
minimizes bandwidth requirements, making it an attractive choice for hardware accelerators
in deep learning applications.</p>
<p>There are two primary FP8 formats:</p>
<ul class="simple">
<li><p><strong>E4M3 Format</strong></p>
<ul>
<li><p>Sign: 1 bit</p></li>
<li><p>Exponent: 4 bits</p></li>
<li><p>Mantissa: 3 bits</p></li>
</ul>
</li>
<li><p><strong>E5M2 Format</strong></p>
<ul>
<li><p>Sign: 1 bit</p></li>
<li><p>Exponent: 5 bits</p></li>
<li><p>Mantissa: 2 bits</p></li>
</ul>
</li>
</ul>
<p>The E4M3 format offers higher precision with a narrower range, while the E5M2 format provides
a wider range at the cost of some precision.</p>
<p>Additionally, FP8 numbers have two representations:</p>
<ul class="simple">
<li><p><strong>FP8-OCP (Open Compute Project)</strong></p>
<ul>
<li><p><a class="reference external" href="https://www.opencompute.org/documents/ocp-8-bit-floating-point-specification-ofp8-revision-1-0-2023-12-01-pdf-1">This</a>
is a standardized format developed by the Open Compute Project to ensure compatibility
across various hardware and software implementations.</p></li>
</ul>
</li>
<li><p><strong>FP8-FNUZ (Finite and NaN Only)</strong></p>
<ul>
<li><p>A specialized format optimized for specific computations, supporting only finite and NaN values
(no Inf support).</p></li>
<li><p>This provides one extra value of exponent and adds to the range of supported FP8 numbers.</p></li>
<li><p><strong>NaN Definition</strong>: When the sign bit is set, and all other exponent and mantissa bits are zero.</p></li>
</ul>
</li>
</ul>
<p>The FNUZ representation provides an extra exponent value, expanding the range of representable
numbers compared to standard FP8 formats.</p>
<section id="id3">
<h3>HIP Header<a class="headerlink" href="#id3" title="Link to this heading">#</a></h3>
<p>The <a class="reference external" href="https://github.com/ROCm/clr/blob/amd-staging/hipamd/include/hip/amd_detail/amd_hip_fp8.h">HIP FP8 header</a>
defines the FP8 ocp/fnuz numbers.</p>
</section>
<section id="id4">
<h3>Device Compatibility<a class="headerlink" href="#id4" title="Link to this heading">#</a></h3>
<p>The following table shows hardware support for this precision format by GPU architecture. “Yes”
indicates native hardware acceleration is available, while “No” indicates hardware acceleration
is not available.</p>
<div class="pst-scrollable-table-container"><table class="table" id="id11">
<caption><span class="caption-text">Supported devices for fp8 numbers</span><a class="headerlink" href="#id11" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Device Type</p></th>
<th class="head"><p>FNUZ FP8</p></th>
<th class="head"><p>OCP FP8</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>CDNA1</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-odd"><td><p>CDNA2</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-even"><td><p>CDNA3</p></td>
<td><p>Yes</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-odd"><td><p>CDNA4</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="row-even"><td><p>RDNA2</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-odd"><td><p>RDNA3</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-even"><td><p>RDNA4</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="using-fp8-numbers-in-hip-programs">
<h3>Using FP8 Numbers in HIP Programs<a class="headerlink" href="#using-fp8-numbers-in-hip-programs" title="Link to this heading">#</a></h3>
<p>To use the FP8 numbers inside HIP programs.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_fp8.h&gt;</span>
</pre></div>
</div>
<p>FP8 numbers can be used on CPU side:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__hip_fp8_storage_t</span><span class="w"> </span><span class="nf">convert_float_to_fp8</span><span class="p">(</span>
<span class="w">  </span><span class="kt">float</span><span class="w"> </span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="cm">/* Input val */</span>
<span class="w">  </span><span class="n">__hip_fp8_interpretation_t</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span><span class="w"> </span><span class="cm">/* interpretation of number E4M3/E5M2 */</span>
<span class="w">  </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="w"> </span><span class="cm">/* Saturation behavior */</span>
<span class="w">  </span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="k">return</span><span class="w"> </span><span class="n">__hip_cvt_float_to_fp8</span><span class="p">(</span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p>The same can be done in kernels as well.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__device__</span><span class="w"> </span><span class="n">__hip_fp8_storage_t</span><span class="w"> </span><span class="n">d_convert_float_to_fp8</span><span class="p">(</span>
<span class="w">  </span><span class="kt">float</span><span class="w"> </span><span class="n">in</span><span class="p">,</span>
<span class="w">  </span><span class="n">__hip_fp8_interpretation_t</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span>
<span class="w">  </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="k">return</span><span class="w"> </span><span class="n">__hip_cvt_float_to_fp8</span><span class="p">(</span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p>Note: On a gfx94x GPU, the type will default to the fnuz type.</p>
<p>The following code example does roundtrip FP8 conversions on both the CPU and GPU and compares the results.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_fp8.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>

<span class="cp">#define hip_check(hip_call)                                                    \</span>
<span class="cp">{                                                                              \</span>
<span class="cp">    auto hip_res = hip_call;                                                   \</span>
<span class="cp">    if (hip_res != hipSuccess) {                                               \</span>
<span class="cp">      std::cerr &lt;&lt; &quot;Failed in HIP call: &quot; &lt;&lt; #hip_call \</span>
<span class="cp">                &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot; &lt;&lt; __LINE__ \</span>
<span class="cp">                &lt;&lt; &quot; with error: &quot; &lt;&lt; hipGetErrorString(hip_res) &lt;&lt; std::endl; \</span>
<span class="cp">      std::abort();                                                            \</span>
<span class="cp">    }                                                                          \</span>
<span class="cp">}</span>

<span class="n">__device__</span><span class="w"> </span><span class="n">__hip_fp8_storage_t</span><span class="w"> </span><span class="n">d_convert_float_to_fp8</span><span class="p">(</span>
<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="n">__hip_fp8_interpretation_t</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span><span class="w"> </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">__hip_cvt_float_to_fp8</span><span class="p">(</span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">);</span>
<span class="p">}</span>

<span class="n">__device__</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="n">d_convert_fp8_to_float</span><span class="p">(</span><span class="kt">float</span><span class="w"> </span><span class="n">in</span><span class="p">,</span>
<span class="w">                                        </span><span class="n">__hip_fp8_interpretation_t</span><span class="w"> </span><span class="n">interpret</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="n">hf</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__hip_cvt_fp8_to_float</span><span class="p">(</span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">);</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">hf</span><span class="p">;</span>
<span class="p">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">float_to_fp8_to_float</span><span class="p">(</span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">in</span><span class="p">,</span>
<span class="w">                                    </span><span class="n">__hip_fp8_interpretation_t</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span>
<span class="w">                                    </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="p">,</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">out</span><span class="p">,</span>
<span class="w">                                    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">auto</span><span class="w"> </span><span class="n">fp8</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">d_convert_float_to_fp8</span><span class="p">(</span><span class="n">in</span><span class="p">[</span><span class="n">i</span><span class="p">],</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">);</span>
<span class="w">        </span><span class="n">out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">d_convert_fp8_to_float</span><span class="p">(</span><span class="n">fp8</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="n">__hip_fp8_storage_t</span>
<span class="n">convert_float_to_fp8</span><span class="p">(</span><span class="kt">float</span><span class="w"> </span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="cm">/* Input val */</span>
<span class="w">                    </span><span class="n">__hip_fp8_interpretation_t</span>
<span class="w">                        </span><span class="n">interpret</span><span class="p">,</span><span class="w"> </span><span class="cm">/* interpretation of number E4M3/E5M2 */</span>
<span class="w">                    </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="w"> </span><span class="cm">/* Saturation behavior */</span>
<span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">__hip_cvt_float_to_fp8</span><span class="p">(</span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">);</span>
<span class="p">}</span>

<span class="kt">float</span><span class="w"> </span><span class="n">convert_fp8_to_float</span><span class="p">(</span>
<span class="w">    </span><span class="n">__hip_fp8_storage_t</span><span class="w"> </span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="cm">/* Input val */</span>
<span class="w">    </span><span class="n">__hip_fp8_interpretation_t</span>
<span class="w">        </span><span class="n">interpret</span><span class="w"> </span><span class="cm">/* interpretation of number E4M3/E5M2 */</span>
<span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">__half</span><span class="w"> </span><span class="n">hf</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__hip_cvt_fp8_to_halfraw</span><span class="p">(</span><span class="n">in</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">);</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">hf</span><span class="p">;</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">32</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipDeviceProp_t</span><span class="w"> </span><span class="n">prop</span><span class="p">;</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipGetDeviceProperties</span><span class="p">(</span><span class="o">&amp;</span><span class="n">prop</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">is_supported</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="p">(</span><span class="n">prop</span><span class="p">.</span><span class="n">gcnArchName</span><span class="p">).</span><span class="n">find</span><span class="p">(</span><span class="s">&quot;gfx94&quot;</span><span class="p">)</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="o">::</span><span class="n">npos</span><span class="p">)</span>
<span class="w">                        </span><span class="o">||</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="p">(</span><span class="n">prop</span><span class="p">.</span><span class="n">gcnArchName</span><span class="p">).</span><span class="n">find</span><span class="p">(</span><span class="s">&quot;gfx950&quot;</span><span class="p">)</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="o">::</span><span class="n">npos</span><span class="p">)</span>
<span class="w">                        </span><span class="o">||</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="p">(</span><span class="n">prop</span><span class="p">.</span><span class="n">gcnArchName</span><span class="p">).</span><span class="n">find</span><span class="p">(</span><span class="s">&quot;gfx12&quot;</span><span class="p">)</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="o">::</span><span class="n">npos</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="o">!</span><span class="n">is_supported</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Need a gfx94x, gfx950 or gfx12xx, but found: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">prop</span><span class="p">.</span><span class="n">gcnArchName</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;No device conversions are supported, only host conversions are supported.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">-1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">__hip_fp8_interpretation_t</span><span class="w"> </span><span class="n">interpret</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="p">(</span><span class="n">prop</span><span class="p">.</span><span class="n">gcnArchName</span><span class="p">).</span><span class="n">find</span><span class="p">(</span><span class="s">&quot;gfx94&quot;</span><span class="p">)</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="o">::</span><span class="n">npos</span><span class="p">)</span>
<span class="w">                                                    </span><span class="o">?</span><span class="w"> </span><span class="n">__HIP_E4M3_FNUZ</span><span class="w"> </span><span class="c1">// gfx94x</span>
<span class="w">                                                    </span><span class="o">:</span><span class="w"> </span><span class="n">__HIP_E4M3</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">__hip_saturation_t</span><span class="w"> </span><span class="n">sat</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__HIP_SATFINITE</span><span class="p">;</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">in</span><span class="p">;</span>
<span class="w">    </span><span class="n">in</span><span class="p">.</span><span class="n">reserve</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">in</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mf">1.1f</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Converting float to fp8 and back...&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// CPU convert</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">cpu_out</span><span class="p">;</span>
<span class="w">    </span><span class="n">cpu_out</span><span class="p">.</span><span class="n">reserve</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="k">auto</span><span class="w"> </span><span class="o">&amp;</span><span class="n">fval</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">in</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">auto</span><span class="w"> </span><span class="n">fp8</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">convert_float_to_fp8</span><span class="p">(</span><span class="n">fval</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">);</span>
<span class="w">        </span><span class="n">cpu_out</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="n">convert_fp8_to_float</span><span class="p">(</span><span class="n">fp8</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">));</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// GPU convert</span>
<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">d_out</span><span class="p">;</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>

<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="n">in</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">in</span><span class="p">.</span><span class="n">size</span><span class="p">(),</span>
<span class="w">                        </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>

<span class="w">    </span><span class="n">float_to_fp8_to_float</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_in</span><span class="p">,</span><span class="w"> </span><span class="n">interpret</span><span class="p">,</span><span class="w"> </span><span class="n">sat</span><span class="p">,</span><span class="w"> </span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">gpu_out</span><span class="p">(</span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="mf">0.0f</span><span class="p">);</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">gpu_out</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">gpu_out</span><span class="p">.</span><span class="n">size</span><span class="p">(),</span>
<span class="w">                        </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_in</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_out</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Validation</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">cpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">gpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">])</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;cpu round trip result: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">cpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
<span class="w">                      </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; - gpu round trip result: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">gpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">abort</span><span class="p">();</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;...CPU and GPU round trip convert matches.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>There are C++ style classes available as well.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__hip_fp8_e4m3_fnuz</span><span class="w"> </span><span class="nf">fp8_val</span><span class="p">(</span><span class="mf">1.1f</span><span class="p">);</span><span class="w"> </span><span class="c1">// gfx94x</span>
<span class="n">__hip_fp8_e4m3</span><span class="w"> </span><span class="nf">fp8_val</span><span class="p">(</span><span class="mf">1.1f</span><span class="p">);</span>
</pre></div>
</div>
<p>Each type of FP8 number has its own class:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp8_e4m3</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp8_e5m2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp8_e4m3_fnuz</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp8_e5m2_fnuz</span></code></p></li>
</ul>
<p>There is support of vector of FP8 types.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp8x2_e4m3</span></code>:      holds 2 values of OCP FP8 e4m3 numbers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp8x4_e4m3</span></code>:      holds 4 values of OCP FP8 e4m3 numbers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp8x2_e5m2</span></code>:      holds 2 values of OCP FP8 e5m2 numbers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp8x4_e5m2</span></code>:      holds 4 values of OCP FP8 e5m2 numbers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp8x2_e4m3_fnuz</span></code>: holds 2 values of FP8 fnuz e4m3 numbers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp8x4_e4m3_fnuz</span></code>: holds 4 values of FP8 fnuz e4m3 numbers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp8x2_e5m2_fnuz</span></code>: holds 2 values of FP8 fnuz e5m2 numbers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_fp8x4_e5m2_fnuz</span></code>: holds 4 values of FP8 fnuz e5m2 numbers</p></li>
</ul>
<p>FNUZ extensions will be available on gfx94x only.</p>
</section>
</section>
<section id="float16-half-precision">
<h2>Float16 (Half Precision)<a class="headerlink" href="#float16-half-precision" title="Link to this heading">#</a></h2>
<p><code class="docutils literal notranslate"><span class="pre">float16</span></code> (Floating Point 16-bit) numbers offer a balance between precision and
efficiency, making them a widely adopted standard for accelerating deep learning
inference. With higher precision than FP8 but lower memory requirements than FP32,
<code class="docutils literal notranslate"><span class="pre">float16</span></code> enables faster computations while preserving model accuracy.</p>
<p>Deep learning workloads often involve massive datasets and complex calculations,
making FP32 computationally expensive. <code class="docutils literal notranslate"><span class="pre">float16</span></code> helps mitigate these costs by reducing
storage and bandwidth demands, allowing for increased throughput without significant
loss of numerical stability. This format is particularly useful for training and
inference in GPUs and TPUs optimized for half-precision arithmetic.</p>
<section id="float16-format">
<h3>Float16 Format<a class="headerlink" href="#float16-format" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">float16</span></code> format uses the following bit allocation:</p>
<ul class="simple">
<li><p><strong>Sign</strong>: 1 bit</p></li>
<li><p><strong>Exponent</strong>: 5 bits</p></li>
<li><p><strong>Mantissa</strong>: 10 bits</p></li>
</ul>
<p>This format offers higher precision with a narrower range compared to <code class="docutils literal notranslate"><span class="pre">bfloat16</span></code>.</p>
</section>
<section id="id5">
<h3>HIP Header<a class="headerlink" href="#id5" title="Link to this heading">#</a></h3>
<p>The <a class="reference external" href="https://github.com/ROCm/clr/blob/amd-staging/hipamd/include/hip/amd_detail/amd_hip_fp16.h">HIP FP16 header</a>
defines the <code class="docutils literal notranslate"><span class="pre">float16</span></code> format.</p>
</section>
<section id="id6">
<h3>Device Compatibility<a class="headerlink" href="#id6" title="Link to this heading">#</a></h3>
<p>This precision format is supported across all GPU architectures. The HIP types and functions
are available for use in both host and device code, with implementation handled by the
compiler and device libraries.</p>
</section>
<section id="using-float16-numbers-in-hip-programs">
<h3>Using Float16 Numbers in HIP Programs<a class="headerlink" href="#using-float16-numbers-in-hip-programs" title="Link to this heading">#</a></h3>
<p>To use <code class="docutils literal notranslate"><span class="pre">float16</span></code> numbers inside HIP programs:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_fp16.h&gt;</span><span class="c1"> // for float16</span>
</pre></div>
</div>
<p>The following code example adds two <code class="docutils literal notranslate"><span class="pre">float16</span></code> values on the GPU and compares the results
against summed float values on the CPU.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_fp16.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>

<span class="cp">#define hip_check(hip_call)                                                    \</span>
<span class="cp">{                                                                              \</span>
<span class="cp">    auto hip_res = hip_call;                                                   \</span>
<span class="cp">    if (hip_res != hipSuccess) {                                               \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;Failed in HIP call: &quot; &lt;&lt; #hip_call \</span>
<span class="cp">                  &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot; &lt;&lt; __LINE__ \</span>
<span class="cp">                  &lt;&lt; &quot; with error: &quot; &lt;&lt; hipGetErrorString(hip_res) &lt;&lt; std::endl; \</span>
<span class="cp">        std::abort();                                                            \</span>
<span class="cp">    }                                                                          \</span>
<span class="cp">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">add_half_precision</span><span class="p">(</span><span class="n">__half</span><span class="o">*</span><span class="w"> </span><span class="n">in1</span><span class="p">,</span><span class="w"> </span><span class="n">__half</span><span class="o">*</span><span class="w"> </span><span class="n">in2</span><span class="p">,</span><span class="w"> </span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">out</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">idx</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="c1">// Load as half, perform addition in float, store as float</span>
<span class="w">        </span><span class="n">__half</span><span class="w"> </span><span class="n">sum</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">in1</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">in2</span><span class="p">[</span><span class="n">idx</span><span class="p">];</span>
<span class="w">        </span><span class="n">out</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__half2float</span><span class="p">(</span><span class="n">sum</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">32</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="n">tolerance</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">1e-1f</span><span class="p">;</span><span class="w">  </span><span class="c1">// Allowable numerical difference</span>

<span class="w">    </span><span class="c1">// Initialize input vectors as floats</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">in1</span><span class="p">(</span><span class="n">size</span><span class="p">),</span><span class="w"> </span><span class="n">in2</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">in1</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mf">0.5f</span><span class="p">;</span>
<span class="w">        </span><span class="n">in2</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mf">0.5f</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Compute expected results in full precision on CPU</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">cpu_out</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">cpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">in1</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">in2</span><span class="p">[</span><span class="n">i</span><span class="p">];</span><span class="w">  </span><span class="c1">// Direct float addition</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Allocate device memory (store input as half, output as float)</span>
<span class="w">    </span><span class="n">__half</span><span class="w"> </span><span class="o">*</span><span class="n">d_in1</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">d_in2</span><span class="p">;</span>
<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">d_out</span><span class="p">;</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_in1</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">__half</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_in2</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">__half</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Convert input to half and copy to device</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">__half</span><span class="o">&gt;</span><span class="w"> </span><span class="n">in1_half</span><span class="p">(</span><span class="n">size</span><span class="p">),</span><span class="w"> </span><span class="n">in2_half</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">in1_half</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__float2half</span><span class="p">(</span><span class="n">in1</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">        </span><span class="n">in2_half</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__float2half</span><span class="p">(</span><span class="n">in2</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_in1</span><span class="p">,</span><span class="w"> </span><span class="n">in1_half</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">__half</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_in2</span><span class="p">,</span><span class="w"> </span><span class="n">in2_half</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">__half</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Launch kernel</span>
<span class="w">    </span><span class="n">add_half_precision</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_in1</span><span class="p">,</span><span class="w"> </span><span class="n">d_in2</span><span class="p">,</span><span class="w"> </span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Copy result back to host</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">gpu_out</span><span class="p">(</span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="mf">0.0f</span><span class="p">);</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">gpu_out</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Free device memory</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_in1</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_in2</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_out</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Validation with tolerance</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">fabs</span><span class="p">(</span><span class="n">cpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">gpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">])</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="n">tolerance</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Mismatch at index &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;: CPU result = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">cpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
<span class="w">                      </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;, GPU result = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">gpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">abort</span><span class="p">();</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Success: CPU and GPU half-precision addition match within tolerance!&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="c-style-classes">
<h3>C++ Style Classes<a class="headerlink" href="#c-style-classes" title="Link to this heading">#</a></h3>
<p>Float16 numbers can be used with C++ style classes:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__half</span><span class="w"> </span><span class="nf">fp16_val</span><span class="p">(</span><span class="mf">1.1f</span><span class="p">);</span><span class="w">           </span><span class="c1">// float16</span>
</pre></div>
</div>
</section>
<section id="vector-support">
<h3>Vector Support<a class="headerlink" href="#vector-support" title="Link to this heading">#</a></h3>
<p>There is support for vectors of float16 types:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">__half2</span></code>: holds 2 values of float16 numbers</p></li>
</ul>
</section>
</section>
<section id="bfloat16-brain-float-16-bit-precision">
<h2>BFloat16 (Brain float 16-bit precision)<a class="headerlink" href="#bfloat16-brain-float-16-bit-precision" title="Link to this heading">#</a></h2>
<p><code class="docutils literal notranslate"><span class="pre">bfloat16</span></code> (Brain Floating Point 16-bit) is a truncated version of the 32-bit IEEE 754
single-precision floating-point format. Originally developed by Google for machine
learning applications, <code class="docutils literal notranslate"><span class="pre">bfloat16</span></code> provides a good balance between range and precision
for neural network computations.</p>
<p><code class="docutils literal notranslate"><span class="pre">bfloat16</span></code> is particularly well-suited for deep learning workloads because it maintains
the same exponent range as FP32, making it less prone to overflow and underflow issues
during training. This format sacrifices some precision compared to float16 but offers
better numerical stability for many AI applications.</p>
<section id="bfloat16-format">
<h3>BFloat16 Format<a class="headerlink" href="#bfloat16-format" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">bfloat16</span></code> format uses the following bit allocation:</p>
<ul class="simple">
<li><p><strong>Sign</strong>: 1 bit</p></li>
<li><p><strong>Exponent</strong>: 8 bits</p></li>
<li><p><strong>Mantissa</strong>: 7 bits</p></li>
</ul>
<p>This format provides a wider range at the cost of some precision compared to <code class="docutils literal notranslate"><span class="pre">float16</span></code>.</p>
</section>
<section id="id7">
<h3>HIP Header<a class="headerlink" href="#id7" title="Link to this heading">#</a></h3>
<p>The <a class="reference external" href="https://github.com/ROCm/clr/blob/amd-staging/hipamd/include/hip/amd_detail/amd_hip_bf16.h">HIP BF16 header</a>
defines the <code class="docutils literal notranslate"><span class="pre">bfloat16</span></code> format.</p>
</section>
<section id="id8">
<h3>Device Compatibility<a class="headerlink" href="#id8" title="Link to this heading">#</a></h3>
<p>This precision format is supported across all GPU architectures. The HIP types and functions
are available for use in both host and device code, with implementation handled by the
compiler and device libraries.</p>
</section>
<section id="using-bfloat16-numbers-in-hip-programs">
<h3>Using <code class="docutils literal notranslate"><span class="pre">bfloat16</span></code> Numbers in HIP Programs<a class="headerlink" href="#using-bfloat16-numbers-in-hip-programs" title="Link to this heading">#</a></h3>
<p>To use <code class="docutils literal notranslate"><span class="pre">bfloat16</span></code> numbers inside HIP programs:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_bf16.h&gt;</span><span class="c1"> // for bfloat16</span>
</pre></div>
</div>
<p>The following code example demonstrates basic <code class="docutils literal notranslate"><span class="pre">bfloat16</span></code> operations:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_bf16.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>

<span class="cp">#define hip_check(hip_call)                                                    \</span>
<span class="cp">{                                                                              \</span>
<span class="cp">    auto hip_res = hip_call;                                                   \</span>
<span class="cp">    if (hip_res != hipSuccess) {                                               \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;Failed in HIP call: &quot; &lt;&lt; #hip_call \</span>
<span class="cp">                  &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot; &lt;&lt; __LINE__ \</span>
<span class="cp">                  &lt;&lt; &quot; with error: &quot; &lt;&lt; hipGetErrorString(hip_res) &lt;&lt; std::endl; \</span>
<span class="cp">        std::abort();                                                            \</span>
<span class="cp">    }                                                                          \</span>
<span class="cp">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">add_bfloat16</span><span class="p">(</span><span class="n">__hip_bfloat16</span><span class="o">*</span><span class="w"> </span><span class="n">in1</span><span class="p">,</span><span class="w"> </span><span class="n">__hip_bfloat16</span><span class="o">*</span><span class="w"> </span><span class="n">in2</span><span class="p">,</span><span class="w"> </span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">out</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">idx</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="c1">// Load as bfloat16, perform addition, convert to float for output</span>
<span class="w">        </span><span class="n">__hip_bfloat16</span><span class="w"> </span><span class="n">sum</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">in1</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">in2</span><span class="p">[</span><span class="n">idx</span><span class="p">];</span>
<span class="w">        </span><span class="n">out</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__bfloat162float</span><span class="p">(</span><span class="n">sum</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">32</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="n">tolerance</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">1e-1f</span><span class="p">;</span><span class="w">  </span><span class="c1">// Allowable numerical difference</span>

<span class="w">    </span><span class="c1">// Initialize input vectors as floats</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">in1</span><span class="p">(</span><span class="n">size</span><span class="p">),</span><span class="w"> </span><span class="n">in2</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">in1</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mf">0.5f</span><span class="p">;</span>
<span class="w">        </span><span class="n">in2</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mf">0.5f</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Compute expected results in full precision on CPU</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">cpu_out</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">cpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">in1</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">in2</span><span class="p">[</span><span class="n">i</span><span class="p">];</span><span class="w">  </span><span class="c1">// Direct float addition</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Allocate device memory (store input as bfloat16, output as float)</span>
<span class="w">    </span><span class="n">__hip_bfloat16</span><span class="w"> </span><span class="o">*</span><span class="n">d_in1</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">d_in2</span><span class="p">;</span>
<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">d_out</span><span class="p">;</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_in1</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">__hip_bfloat16</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_in2</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">__hip_bfloat16</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Convert input to bfloat16 and copy to device</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">__hip_bfloat16</span><span class="o">&gt;</span><span class="w"> </span><span class="n">in1_bf16</span><span class="p">(</span><span class="n">size</span><span class="p">),</span><span class="w"> </span><span class="n">in2_bf16</span><span class="p">(</span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">in1_bf16</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__float2bfloat16</span><span class="p">(</span><span class="n">in1</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">        </span><span class="n">in2_bf16</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__float2bfloat16</span><span class="p">(</span><span class="n">in2</span><span class="p">[</span><span class="n">i</span><span class="p">]);</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_in1</span><span class="p">,</span><span class="w"> </span><span class="n">in1_bf16</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">__hip_bfloat16</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_in2</span><span class="p">,</span><span class="w"> </span><span class="n">in2_bf16</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">__hip_bfloat16</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Launch kernel</span>
<span class="w">    </span><span class="n">add_bfloat16</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_in1</span><span class="p">,</span><span class="w"> </span><span class="n">d_in2</span><span class="p">,</span><span class="w"> </span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Copy result back to host</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">gpu_out</span><span class="p">(</span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="mf">0.0f</span><span class="p">);</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">gpu_out</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_out</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Free device memory</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_in1</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_in2</span><span class="p">));</span>
<span class="w">    </span><span class="n">hip_check</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_out</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Validation with tolerance</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="n">fabs</span><span class="p">(</span><span class="n">cpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">gpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">])</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="n">tolerance</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Mismatch at index &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;: CPU result = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">cpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
<span class="w">                      </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;, GPU result = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">gpu_out</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">abort</span><span class="p">();</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Success: CPU and GPU bfloat16 addition match within tolerance!&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="id9">
<h3>C++ Style Classes<a class="headerlink" href="#id9" title="Link to this heading">#</a></h3>
<p><code class="docutils literal notranslate"><span class="pre">bfloat16</span></code> numbers can be used with C++ style classes:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__hip_bfloat16</span><span class="w"> </span><span class="nf">bf16_val</span><span class="p">(</span><span class="mf">1.1f</span><span class="p">);</span><span class="w">   </span><span class="c1">// bfloat16</span>
</pre></div>
</div>
</section>
<section id="id10">
<h3>Vector Support<a class="headerlink" href="#id10" title="Link to this heading">#</a></h3>
<p>There is support for vectors of bfloat16 types:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">__hip_bfloat162</span></code>: holds 2 values of bfloat16 numbers</p></li>
</ul>
</section>
</section>
<section id="hip-extensions">
<h2>HIP Extensions<a class="headerlink" href="#hip-extensions" title="Link to this heading">#</a></h2>
<p>HIP also provides some extensions APIs for microscaling formats. These are supported on AMD
GPUs. <code class="docutils literal notranslate"><span class="pre">gfx950</span></code> provides hardware acceleration for hip extensions. In fact most APIs are 1 to 1
mapping of hardware instruction.</p>
<p>Scale is also an input to the APIs. Scale is defined as type <code class="docutils literal notranslate"><span class="pre">__amd_scale_t</span></code> and is of format E8M0.</p>
</section>
<section id="hipext-types">
<h2>hipExt Types<a class="headerlink" href="#hipext-types" title="Link to this heading">#</a></h2>
<p>hipExt microscaling APIs introduce a bunch of types which are used throughout the set of APIs.</p>
<div class="pst-scrollable-table-container"><table class="table" id="id12">
<caption><span class="caption-text">Types</span><a class="headerlink" href="#id12" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Types</p></th>
<th class="head"><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_scale_t</span></code></p></td>
<td><p>Store scale type which stores a value of E8M0.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8_storage_t</span></code></p></td>
<td><p>Store a single fp8 value.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x2_storage_t</span></code></p></td>
<td><p>Store 2 packed fp8 value.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x8_storage_t</span></code></p></td>
<td><p>Store 8 packed fp8 value.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x2_storage_t</span></code></p></td>
<td><p>Store 2 packed fp4 value.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x8_storage_t</span></code></p></td>
<td><p>Store 8 packed fp4 value.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16_storage_t</span></code></p></td>
<td><p>Store a single bf16 value.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16x2_storage_t</span></code></p></td>
<td><p>Store 2 packed bf16 value.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16x8_storage_t</span></code></p></td>
<td><p>Store 8 packed bf16 value.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16x32_storage_t</span></code></p></td>
<td><p>Store 32 packed bf16 value.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16_storage_t</span></code></p></td>
<td><p>Store a single fp16 value.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16x2_storage_t</span></code></p></td>
<td><p>Store 2 packed fp16 value.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16x8_storage_t</span></code></p></td>
<td><p>Store 8 packed fp16 value.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16x32_storage_t</span></code></p></td>
<td><p>Store 32 packed fp16 value.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_floatx2_storage_t</span></code></p></td>
<td><p>Store 2 packed float value.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_floatx8_storage_t</span></code></p></td>
<td><p>Store 8 packed float value.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_floatx16_storage_t</span></code></p></td>
<td><p>Store 16 packed float value.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_floatx32_storage_t</span></code></p></td>
<td><p>Store 32 packed float value.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp6x32_storage_t</span></code></p></td>
<td><p>Store 32 packed fp6 value.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_shortx2_storage_t</span></code></p></td>
<td><p>Store 2 packed short value.</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="c-apis">
<h2>C-APIs<a class="headerlink" href="#c-apis" title="Link to this heading">#</a></h2>
<p>The naming style of C API is as follows:</p>
<p>All APIs start with <code class="docutils literal notranslate"><span class="pre">__amd</span></code>.
<code class="docutils literal notranslate"><span class="pre">_</span></code>: is used as a separator.
<code class="docutils literal notranslate"><span class="pre">cvt</span></code>: means convert i.e. convert from one format to another.
<code class="docutils literal notranslate"><span class="pre">sr</span></code>: if an API name has <strong>sr</strong> in it, means it will do stochastic rounding and will expect an input as seed.
<code class="docutils literal notranslate"><span class="pre">scale</span></code>: if an API has scale in it, means it will scale the values based on the <code class="docutils literal notranslate"><span class="pre">__amd_scale_t</span></code> input.</p>
<p><code class="docutils literal notranslate"><span class="pre">create</span></code>: The following APIs will be used to create composite types from smaller values
<code class="docutils literal notranslate"><span class="pre">extract</span></code>: The following set of APIs will extract out individual values from a composite type.</p>
<p>Example:
<code class="docutils literal notranslate"><span class="pre">__amd_cvt_fp8x8_to_bf16x8_scale</span></code> : this API converts 8-packed fp8 values to 8 packed bf16. This will also accept input of scale to do the conversion.</p>
<p><code class="docutils literal notranslate"><span class="pre">__amd_extract_fp8x2</span></code> : this API will extract out a 2 packed fp8 value from 8 packed fp8 value based on index. Example of 8-packed fp8: <code class="docutils literal notranslate"><span class="pre">{a:{fp8,</span> <span class="pre">fp8},</span> <span class="pre">b:{fp8,</span> <span class="pre">fp8},</span> <span class="pre">c:{fp8,</span> <span class="pre">fp8},</span> <span class="pre">d:{fp8,</span> <span class="pre">fp8}}</span></code> based on index 0, 1, 2 or 3 the API will return <code class="docutils literal notranslate"><span class="pre">a</span></code>, <code class="docutils literal notranslate"><span class="pre">b</span></code>, <code class="docutils literal notranslate"><span class="pre">c</span></code> or <code class="docutils literal notranslate"><span class="pre">d</span></code> respectively.
<code class="docutils literal notranslate"><span class="pre">__amd_create_fp8x8</span></code> : this API will create 8 packed fp8 value from 4 inputs of 2 packed fp8 values.</p>
<div class="pst-scrollable-table-container"><table class="table" id="id13">
<caption><span class="caption-text">C APIs</span><a class="headerlink" href="#id13" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>API</p></th>
<th class="head"><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">float</span> <span class="pre">__amd_cvt_fp8_to_float(const</span> <span class="pre">__amd_fp8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t)</span></code></p></td>
<td><p>Convert a fp8 value to float.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8_storage_t</span> <span class="pre">__amd_cvt_float_to_fp8_sr(const</span> <span class="pre">float,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int</span> <span class="pre">/*</span> <span class="pre">sr</span> <span class="pre">seed</span> <span class="pre">*/)</span></code></p></td>
<td><p>Convert a float to fp8 value with stochastic rounding, seed is passed as unsigned int argument.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">float</span> <span class="pre">__amd_cvt_fp8_to_float_scale(const</span> <span class="pre">__amd_fp8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert a fp8 value to float with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">float</span> <span class="pre">__amd_cvt_fp8_to_float_scale(const</span> <span class="pre">__amd_fp8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert a fp8 value to float with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_floatx2_storage_t</span> <span class="pre">__amd_cvt_fp8x2_to_floatx2(const</span> <span class="pre">__amd_fp8x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t)</span></code></p></td>
<td><p>Convert 2 packed fp8 value to 2 packed float.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x2_storage_t</span> <span class="pre">__amd_cvt_floatx2_to_fp8x2(const</span> <span class="pre">__amd_floatx2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t)</span></code></p></td>
<td><p>Convert 2 packed float value to 2 packed fp8.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x2_storage_t</span> <span class="pre">__amd_cvt_floatx2_to_fp4x2_sr_scale(const</span> <span class="pre">__amd_floatx2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int</span> <span class="pre">/*</span> <span class="pre">sr</span> <span class="pre">seed</span> <span class="pre">*/,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed float value to 2 packed fp4 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_floatx2_storage_t</span> <span class="pre">__amd_cvt_fp4x2_to_floatx2_scale(const</span> <span class="pre">__amd_fp4x2_storage_t</span> <span class="pre">,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed fp4 value to 2 packed float with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x2_storage_t</span> <span class="pre">__amd_cvt_floatx2_to_fp4x2_scale(const</span> <span class="pre">__amd_floatx2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed float value to 2 packed fp4 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_floatx2_storage_t</span> <span class="pre">__amd_cvt_fp8x2_to_floatx2_scale(const</span> <span class="pre">__amd_fp8x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed fp8 value to 2 packed float with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x2_storage_t</span> <span class="pre">__amd_cvt_floatx2_to_fp8x2_scale(const</span> <span class="pre">__amd_floatx2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed float value to 2 packed fp8 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp6x32_storage_t</span> <span class="pre">__amd_cvt_bf16x32_to_fp6x32_scale(const</span> <span class="pre">__amd_bf16x32_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp6_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 32 packed bf16 value to 32 packed fp6 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp6x32_storage_t</span> <span class="pre">__amd_cvt_fp16x32_to_fp6x32_scale(const</span> <span class="pre">__amd_fp16x32_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp6_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 32 packed fp16 value to 32 packed fp6 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16x2_storage_t</span> <span class="pre">__amd_cvt_fp8x2_to_fp16x2_scale(const</span> <span class="pre">__amd_fp8x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed fp8 value to 2 packed fp16 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16x8_storage_t</span> <span class="pre">__amd_cvt_fp8x8_to_fp16x8_scale(const</span> <span class="pre">__amd_fp8x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed fp8 value to 8 packed fp16 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16x2_storage_t</span> <span class="pre">__amd_cvt_fp8x2_to_bf16x2_scale(const</span> <span class="pre">__amd_fp8x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed fp8 value to 2 packed bf16 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16x2_storage_t</span> <span class="pre">__amd_cvt_fp8x2_to_bf16x2_scale(const</span> <span class="pre">__amd_fp8x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed fp8 value to 2 packed bf16 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16x8_storage_t</span> <span class="pre">__amd_cvt_fp8x8_to_bf16x8_scale(const</span> <span class="pre">__amd_fp8x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed fp8 value to 8 packed bf16 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16x32_storage_t</span> <span class="pre">__amd_cvt_fp6x32_to_fp16x32_scale(const</span> <span class="pre">__amd_fp6x32_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp6_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 32 packed fp6 value to 32 packed fp16 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16x32_storage_t</span> <span class="pre">__amd_cvt_fp6x32_to_bf16x32_scale(const</span> <span class="pre">__amd_fp6x32_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp6_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 32 packed fp6 value to 32 packed bf16 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_floatx32_storage_t</span> <span class="pre">__amd_cvt_fp6x32_to_floatx32_scale(const</span> <span class="pre">__amd_fp6x32_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp6_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 32 packed fp6 value to 32 packed float with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16x2_storage_t</span> <span class="pre">__amd_cvt_fp4x2_to_fp16x2_scale(const</span> <span class="pre">__amd_fp4x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed fp4 value to 2 packed fp16 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16x8_storage_t</span> <span class="pre">__amd_cvt_fp4x8_to_fp16x8_scale(const</span> <span class="pre">__amd_fp4x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed fp4 value to 8 packed fp16 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16x2_storage_t</span> <span class="pre">__amd_cvt_fp4x2_to_bf16x2_scale(const</span> <span class="pre">__amd_fp4x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed fp4 value to 2 packed bf16 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16x8_storage_t</span> <span class="pre">__amd_cvt_fp4x8_to_bf16x8_scale(const</span> <span class="pre">__amd_fp4x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed fp4 value to 8 packed bf16 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_floatx8_storage_t</span> <span class="pre">__amd_cvt_fp4x8_to_floatx8_scale(const</span> <span class="pre">__amd_fp4x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed fp4 value to 8 packed float with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x8_storage_t</span> <span class="pre">__amd_cvt_floatx8_to_fp4x8_scale(const</span> <span class="pre">__amd_floatx8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed float value to 8 packed fp4 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x2_storage_t</span> <span class="pre">__amd_cvt_fp16x2_to_fp8x2_scale(const</span> <span class="pre">__amd_fp16x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed fp16 value to 2 packed fp8 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x2_storage_t</span> <span class="pre">__amd_cvt_bf16x2_to_fp8x2_scale(const</span> <span class="pre">__amd_bf16x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed bf16 value to 2 packed fp8 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x8_storage_t</span> <span class="pre">__amd_cvt_bf16x8_to_fp8x8_scale(const</span> <span class="pre">__amd_bf16x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed bf16 value to 8 packed fp8 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_floatx8_storage_t</span> <span class="pre">__amd_cvt_fp8x8_to_floatx8_scale(const</span> <span class="pre">__amd_fp8x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed fp8 value to 8 packed float with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16_storage_t</span> <span class="pre">__amd_cvt_fp8_to_fp16_scale(const</span> <span class="pre">__amd_fp8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert a fp8 value to fp16 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16_storage_t</span> <span class="pre">__amd_cvt_fp8_to_bf16_scale(const</span> <span class="pre">__amd_fp8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert a fp8 value to bf16 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp6x32_storage_t</span> <span class="pre">__amd_cvt_floatx16_floatx16_to_fp6x32_scale(const</span> <span class="pre">__amd_floatx16_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_floatx16_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp6_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 inputs of 16-packed float values to 32 packed fp6 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp6x32_storage_t</span> <span class="pre">__amd_cvt_floatx32_to_fp6x32_scale(const</span> <span class="pre">__amd_floatx32_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp6_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 32 packed float values to 32 packed fp6 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp6x32_storage_t</span> <span class="pre">__amd_cvt_floatx32_to_fp6x32_sr_scale(const</span> <span class="pre">__amd_floatx32_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp6_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 32 packed float values to 32 packed fp6 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16_storage_t</span> <span class="pre">__amd_cvt_float_to_fp16_sr(const</span> <span class="pre">float,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int)</span></code></p></td>
<td><p>Convert a float value to fp16 with stochastic rounding.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16x2_storage_t</span> <span class="pre">__amd_cvt_float_float_to_fp16x2_sr(const</span> <span class="pre">float,</span> <span class="pre">const</span> <span class="pre">float,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int)</span></code></p></td>
<td><p>Convert two inputs of float to 2 packed fp16 with stochastic rounding.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16_storage_t</span> <span class="pre">__amd_cvt_float_to_bf16_sr(const</span> <span class="pre">float,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int)</span></code></p></td>
<td><p>Convert a float value to bf16 with stochastic rounding.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp6x32_storage_t</span> <span class="pre">__amd_cvt_fp16x32_to_fp6x32_sr_scale(const</span> <span class="pre">__amd_fp16x32_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp6_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 32 packed fp16 values to 32 packed fp6 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp6x32_storage_t</span> <span class="pre">__amd_cvt_bf16x32_to_fp6x32_sr_scale(const</span> <span class="pre">__amd_bf16x32_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp6_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 32 packed bf16 values to 32 packed fp6 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x2_storage_t</span> <span class="pre">__amd_cvt_bf16x2_to_fp4x2_scale(const</span> <span class="pre">__amd_bf16x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed bf16 value to 2 packed fp4 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x8_storage_t</span> <span class="pre">__amd_cvt_bf16x8_to_fp4x8_scale(const</span> <span class="pre">__amd_bf16x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed bf16 value to 8 packed fp4 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x2_storage_t</span> <span class="pre">__amd_cvt_fp16x2_to_fp4x2_scale(const</span> <span class="pre">__amd_fp16x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed fp16 value to 2 packed fp4 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x8_storage_t</span> <span class="pre">__amd_cvt_fp16x8_to_fp4x8_scale(const</span> <span class="pre">__amd_fp16x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed fp16 value to 8 packed fp4 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x8_storage_t</span> <span class="pre">__amd_cvt_floatx8_to_fp4x8_sr_scale(const</span> <span class="pre">__amd_floatx8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed float values to 8 packed fp4 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x2_storage_t</span> <span class="pre">__amd_cvt_bf16x2_to_fp4x2_sr_scale(const</span> <span class="pre">__amd_bf16x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed bf16 value to 2 packed fp4 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x8_storage_t</span> <span class="pre">__amd_cvt_bf16x8_to_fp4x8_sr_scale(const</span> <span class="pre">__amd_bf16x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed bf16 value to 8 packed fp4 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x2_storage_t</span> <span class="pre">__amd_cvt_fp16x2_to_fp4x2_sr_scale(const</span> <span class="pre">__amd_fp16x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 2 packed fp16 value to 2 packed fp4 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp4x8_storage_t</span> <span class="pre">__amd_cvt_fp16x8_to_fp4x8_sr_scale(const</span> <span class="pre">__amd_fp16x8_storage_t</span> <span class="pre">,</span> <span class="pre">const</span> <span class="pre">__amd_fp4_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed fp16 values to 8 packed fp4 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x8_storage_t</span> <span class="pre">__amd_cvt_floatx8_to_fp8x8_sr_scale(const</span> <span class="pre">__amd_floatx8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed float values to 8 packed fp8 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8_storage_t</span> <span class="pre">__amd_cvt_fp16_to_fp8_sr_scale(const</span> <span class="pre">__amd_fp16_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert a fp16 value to fp8 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x8_storage_t</span> <span class="pre">__amd_cvt_fp16x8_to_fp8x8_sr_scale(const</span> <span class="pre">__amd_fp16x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed fp16 values to 8 packed fp8 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8_storage_t</span> <span class="pre">__amd_cvt_bf16_to_fp8_sr_scale(const</span> <span class="pre">__amd_bf16_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert a bf16 value to fp8 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x8_storage_t</span> <span class="pre">__amd_cvt_bf16x8_to_fp8x8_sr_scale(const</span> <span class="pre">__amd_bf16x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">unsigned</span> <span class="pre">int,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed bf16 values to 8 packed fp8 with stochastic rounding and scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16_storage_t</span> <span class="pre">__amd_cvt_fp8_to_fp16(const</span> <span class="pre">__amd_fp8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t)</span></code></p></td>
<td><p>Convert a fp8 value to fp16.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16x2_storage_t</span> <span class="pre">__amd_cvt_fp8x2_to_fp16x2(const</span> <span class="pre">__amd_fp8x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t)</span></code></p></td>
<td><p>Convert 2 packed fp8 value to 2 packed fp16.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x2_storage_t</span> <span class="pre">__amd_cvt_fp16x2_to_fp8x2(const</span> <span class="pre">__amd_fp16x2_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t)</span></code></p></td>
<td><p>Convert 2 packed fp16 value to 2 packed fp8.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x8_storage_t</span> <span class="pre">__amd_cvt_fp16x8_to_fp8x8_scale(const</span> <span class="pre">__amd_fp16x8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed fp16 values to 8 packed fp8 with scale.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8x8_storage_t</span> <span class="pre">__amd_cvt_floatx8_to_fp8x8_scale(const</span> <span class="pre">__amd_floatx8_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">__amd_scale_t)</span></code></p></td>
<td><p>Convert 8 packed float values to 8 packed fp8 with scale.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp8_storage_t</span> <span class="pre">__amd_cvt_fp16_to_fp8_sr(const</span> <span class="pre">__amd_fp16_storage_t,</span> <span class="pre">const</span> <span class="pre">__amd_fp8_interpretation_t,</span> <span class="pre">const</span> <span class="pre">short)</span></code></p></td>
<td><p>Convert a fp16 value to fp8 with stochastic rounding.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">float2</span> <span class="pre">__amd_cvt_floatx2_to_float2(const</span> <span class="pre">__amd_floatx2_storage_t)</span></code></p></td>
<td><p>Convert 2 packed float value to hip’s float2 type.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__half</span> <span class="pre">__amd_cvt_fp16_to_half(const</span> <span class="pre">__amd_fp16_storage_t)</span></code></p></td>
<td><p>Convert fp16 type to hip’s __half type.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__half2</span> <span class="pre">__amd_cvt_fp16x2_to_half2(const</span> <span class="pre">__amd_fp16x2_storage_t)</span></code></p></td>
<td><p>Convert 2 packed fp16 type to hip’s __half2 type.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16_storage_t</span> <span class="pre">__amd_cvt_half_to_fp16(const</span> <span class="pre">__half)</span></code></p></td>
<td><p>Convert hip’s __half type to fp16 type.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_fp16x2_storage_t</span> <span class="pre">__amd_cvt_half2_to_fp16x2(const</span> <span class="pre">__half2)</span></code></p></td>
<td><p>Convert hip’s __half2 type to 2 packed fp16.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__hip_bfloat16</span> <span class="pre">__amd_cvt_bf16_to_hipbf16(const</span> <span class="pre">__amd_bf16_storage_t)</span></code></p></td>
<td><p>Convert bf16 type to __hip_bfloat16 type.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__hip_bfloat162</span> <span class="pre">__amd_cvt_bf16x2_to_hipbf162(const</span> <span class="pre">__amd_bf16x2_storage_t)</span></code></p></td>
<td><p>Convert 2 packed bf16 type to __hip_bfloat162 type.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16_storage_t</span> <span class="pre">__amd_cvt_hipbf16_to_bf16(const</span> <span class="pre">__hip_bfloat16)</span></code></p></td>
<td><p>Convert __hip_bfloat16 to bf16 type.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__amd_bf16x2_storage_t</span> <span class="pre">__amd_cvt_hipbf162_to_bf16x2(const</span> <span class="pre">__hip_bfloat162)</span></code></p></td>
<td><p>Convert __hip_bfloat162 to 2 packed bf16 type.</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="hip-ext-c-api">
<h2>HIP EXT C++ API<a class="headerlink" href="#hip-ext-c-api" title="Link to this heading">#</a></h2>
<p>There are C++ data structures also available. These are different from one in <code class="docutils literal notranslate"><span class="pre">&lt;hip/hip_fp8.h&gt;</span></code> header. These APIs expose a wider capability set which are exclusive to <code class="docutils literal notranslate"><span class="pre">gfx950</span></code>.</p>
<p>HIP EXT FP8 E4M3:</p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="k">struct</span><span class="w"> </span><span class="nc">__hipext_ocp_fp8_e4m3</span><span class="w">  </span><span class="p">{</span>
<span class="w">  </span><span class="c1">// Constructor</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8_e4m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8 e4m3 from float</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8_e4m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* sr seed */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8 e4m3 from float with stochastic rounding</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8_e4m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* sr seed */</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8 e4m3 from float with stochastic rounding and scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8_e4m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_fp16_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* sr seed */</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8 e4m3 from fp16 with scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8_e4m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_bf16_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* sr seed */</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8 e4m3 from bf16 with scale</span>

<span class="w">  </span><span class="c1">// Getters</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_fp16_storage_t</span><span class="w"> </span><span class="n">get_scaled_fp16</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// get scaled fp16 value</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_bf16_storage_t</span><span class="w"> </span><span class="n">get_scaled_bf16</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// get scaled bf16 value</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="n">get_scaled_float</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// get scaled float value</span>

<span class="w">  </span><span class="c1">// Operators</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">operator</span><span class="w"> </span><span class="kt">float</span><span class="p">()</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// get a float value</span>
<span class="p">};</span>
</pre></div>
</div>
<p>HIP EXT FP8 E5M2:</p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="k">struct</span><span class="w"> </span><span class="nc">__hipext_ocp_fp8_e5m2</span><span class="w">  </span><span class="p">{</span>
<span class="w">  </span><span class="c1">// Constructor</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8_e5m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8 e4m3 from float</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8_e5m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* sr seed */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8 e4m3 from float with stochastic rounding</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8_e5m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* sr seed */</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8 e4m3 from float with stochastic rounding and scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8_e5m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_fp16_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* sr seed */</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8 e4m3 from fp16 with scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8_e5m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_bf16_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* sr seed */</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8 e4m3 from bf16 with scale</span>

<span class="w">  </span><span class="c1">// Getters</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_fp16_storage_t</span><span class="w"> </span><span class="n">get_scaled_fp16</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// get scaled fp16 value</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_bf16_storage_t</span><span class="w"> </span><span class="n">get_scaled_bf16</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// get scaled bf16 value</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="n">get_scaled_float</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// get scaled float value</span>

<span class="w">  </span><span class="c1">// Operators</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">operator</span><span class="w"> </span><span class="kt">float</span><span class="p">()</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// get a float value</span>
<span class="p">};</span>
</pre></div>
</div>
<p>HIP EXT 2 Packed FP8 E4M3</p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="k">struct</span><span class="w"> </span><span class="nc">__hipext_ocp_fp8x2_e4m3</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8x2_e4m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8x2 from two floats</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8x2_e4m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_floatx2_storage_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8x2 from 2 packed floats</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8x2_e4m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_floatx2_storage_t</span><span class="p">,</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8x2 from 2 packed floats with scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8x2_e4m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_fp16x2_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8x2 from 2 packed fp16 with scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8x2_e4m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_bf16x2_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8x2 from 2 packed bf16 with scale</span>

<span class="w">  </span><span class="c1">// Getters</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_fp16x2_storage_t</span><span class="w"> </span><span class="n">get_scaled_fp16x2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get scaled 2 packed fp16</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_bf16x2_storage_t</span><span class="w"> </span><span class="n">get_scaled_fp16x2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get scaled 2 packed fp16</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_floatx2_storage_t</span><span class="w"> </span><span class="n">get_scaled_floatx2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="n">scale</span><span class="p">)</span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get scaled 2 packed float</span>

<span class="w">  </span><span class="c1">// Operators</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">operator</span><span class="w"> </span><span class="n">__amd_floatx2_storage_t</span><span class="p">()</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get 2 packed float</span>
<span class="p">};</span>
</pre></div>
</div>
<p>HIP EXT 2 Packed FP8 E5M2</p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="k">struct</span><span class="w"> </span><span class="nc">__hipext_ocp_fp8x2_e5m2</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8x2_e5m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8x2 from two floats</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8x2_e5m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_floatx2_storage_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8x2 from 2 packed floats</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8x2_e5m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_floatx2_storage_t</span><span class="p">,</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8x2 from 2 packed floats with scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8x2_e5m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_fp16x2_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8x2 from 2 packed fp16 with scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp8x2_e5m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_bf16x2_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="cm">/* scale */</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp8x2 from 2 packed bf16 with scale</span>

<span class="w">  </span><span class="c1">// Getters</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_fp16x2_storage_t</span><span class="w"> </span><span class="n">get_scaled_fp16x2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get scaled 2 packed fp16</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_bf16x2_storage_t</span><span class="w"> </span><span class="n">get_scaled_fp16x2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get scaled 2 packed fp16</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_floatx2_storage_t</span><span class="w"> </span><span class="n">get_scaled_floatx2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="w"> </span><span class="n">scale</span><span class="p">)</span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get scaled 2 packed float</span>

<span class="w">  </span><span class="c1">// Operators</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">operator</span><span class="w"> </span><span class="n">__amd_floatx2_storage_t</span><span class="p">()</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get 2 packed float</span>
<span class="p">};</span>
</pre></div>
</div>
<p>HIP EXT 32 packed FP6 E2M3</p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="k">struct</span><span class="w"> </span><span class="nc">__hipext_ocp_fp6x32_e2m3</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp6x32_e2m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_floatx16_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_floatx16_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp6x32 from two floatx16 with scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp6x32_e2m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_floatx32_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* seed */</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp6x32 from two floatx32 with stochastic rounding and scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp6x32_e2m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_fp16x32_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* seed */</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp6x32 from two fp16x32 with stochastic rounding and scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp6x32_e2m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_fp16x32_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp6x32 from two fp16x32 with scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp6x32_e2m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_bf16x32_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* seed */</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp6x32 from two bf16x32 with stochastic rounding and scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp6x32_e2m3</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_bf16x32_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp6x32 from two bf16x32 with scale</span>

<span class="w">  </span><span class="c1">// Getters</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_floatx32_storage_t</span><span class="w"> </span><span class="n">get_scaled_floatx32</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get Scaled floatx32</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_fp16x32_storage_t</span><span class="w"> </span><span class="n">get_scaled_fp16x32</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get Scaled fp16x32</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_bf16x32_storage_t</span><span class="w"> </span><span class="n">get_scaled_bf16x32</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get Scaled bf16x32</span>
<span class="p">};</span>
</pre></div>
</div>
<p>HIP EXT 32 packed FP6 E3M2</p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="k">struct</span><span class="w"> </span><span class="nc">__hipext_ocp_fp6x32_e3m2</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp6x32_e3m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_floatx16_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_floatx16_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp6x32 from two floatx16 with scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp6x32_e3m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_floatx32_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* seed */</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp6x32 from two floatx32 with stochastic rounding and scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp6x32_e3m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_fp16x32_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* seed */</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp6x32 from two fp16x32 with stochastic rounding and scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp6x32_e3m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_fp16x32_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp6x32 from two fp16x32 with scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp6x32_e3m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_bf16x32_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="cm">/* seed */</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp6x32 from two bf16x32 with stochastic rounding and scale</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp6x32_e3m2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_bf16x32_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create fp6x32 from two bf16x32 with scale</span>

<span class="w">  </span><span class="c1">// Getters</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_floatx32_storage_t</span><span class="w"> </span><span class="n">get_scaled_floatx32</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get Scaled floatx32</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_fp16x32_storage_t</span><span class="w"> </span><span class="n">get_scaled_fp16x32</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get Scaled fp16x32</span>
<span class="w">  </span><span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_bf16x32_storage_t</span><span class="w"> </span><span class="n">get_scaled_bf16x32</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get Scaled bf16x32</span>
<span class="p">};</span>
</pre></div>
</div>
<p>HIP EXT 2 packed FP4</p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="k">struct</span><span class="w"> </span><span class="nc">__hipext_ocp_fp4x2_e2m1</span><span class="w"> </span><span class="p">{</span>
<span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp4x2_e2m1</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">float</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create FP4x2 from two floats with scale</span>
<span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp4x2_e2m1</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_floatx2_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create FP4x2 from floatx2 with scale</span>
<span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp4x2_e2m1</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_bf16x2_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create FP4x2 from bf16x2 with scale</span>
<span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp4x2_e2m1</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_fp16x2_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create FP4x2 from fp16x2 with scale</span>
<span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp4x2_e2m1</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_floatx2_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create FP4x2 from floatx2 with stochastic rounding and scale</span>
<span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp4x2_e2m1</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_bf16x2_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create FP4x2 from bf16x2 with stochastic rounding and scale</span>
<span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__hipext_ocp_fp4x2_e2m1</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_fp16x2_storage_t</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">);</span><span class="w"> </span><span class="c1">// Create FP4x2 from fp16x2 with stochastic rounding and scale</span>

<span class="c1">// Getters</span>
<span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_floatx2_storage_t</span><span class="w"> </span><span class="n">get_scaled_floatx2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// get scaled floatx2</span>
<span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_fp16x2_storage_t</span><span class="w"> </span><span class="n">get_scaled_fp16x2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get scaled fp16x2</span>
<span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="n">__amd_bf16x2_storage_t</span><span class="w"> </span><span class="n">get_scaled_bf16x2</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="n">__amd_scale_t</span><span class="p">)</span><span class="w"> </span><span class="k">const</span><span class="p">;</span><span class="w"> </span><span class="c1">// Get scaled bf16x2</span>
<span class="p">};</span>
</pre></div>
</div>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="deprecated_api_list.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">HIP deprecated runtime API functions</p>
      </div>
    </a>
    <a class="right-next"
       href="hardware_features.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Hardware features</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#fp4-4-bit-precision">FP4 (4-bit Precision)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-header">HIP Header</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#device-compatibility">Device Compatibility</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-fp4-numbers-in-hip-programs">Using FP4 Numbers in HIP Programs</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#fp6-6-bit-precision">FP6 (6-bit Precision)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">HIP Header</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id2">Device Compatibility</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-fp6-numbers-in-hip-programs">Using FP6 Numbers in HIP Programs</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#fp8-quarter-precision">FP8 (Quarter Precision)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id3">HIP Header</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id4">Device Compatibility</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-fp8-numbers-in-hip-programs">Using FP8 Numbers in HIP Programs</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#float16-half-precision">Float16 (Half Precision)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#float16-format">Float16 Format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id5">HIP Header</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id6">Device Compatibility</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-float16-numbers-in-hip-programs">Using Float16 Numbers in HIP Programs</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#c-style-classes">C++ Style Classes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#vector-support">Vector Support</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#bfloat16-brain-float-16-bit-precision">BFloat16 (Brain float 16-bit precision)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#bfloat16-format">BFloat16 Format</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id7">HIP Header</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id8">Device Compatibility</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-bfloat16-numbers-in-hip-programs">Using <code class="docutils literal notranslate"><span class="pre">bfloat16</span></code> Numbers in HIP Programs</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id9">C++ Style Classes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id10">Vector Support</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-extensions">HIP Extensions</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hipext-types">hipExt Types</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#c-apis">C-APIs</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-ext-c-api">HIP EXT C++ API</a></li>
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
