---
title: "HIP compilers &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/understand/compilers.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:07:01.169576+00:00
content_hash: "83c093af86f9163e"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Compilation workflow of the HIP compilers." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, HIP runtime API" name="keywords" />

    <title>HIP compilers &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'understand/compilers';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Performance guidelines" href="../how-to/performance_guidelines.html" />
    <link rel="prev" title="Hardware implementation" href="hardware_implementation.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/understand/compilers.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="programming_model.html">Introduction to the HIP programming model</a></li>
<li class="toctree-l1"><a class="reference internal" href="performance_optimization.html">Understanding GPU performance</a></li>
<li class="toctree-l1"><a class="reference internal" href="hardware_implementation.html">Hardware implementation</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">HIP compilers</a></li>
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
<li class="toctree-l1"><a class="reference internal" href="amd_clr.html">AMD compute language runtimes (CLR)</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">HIP compilers</li>
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
    <h1>HIP compilers</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#compilation-workflow">Compilation workflow</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#offline-compilation">Offline compilation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#runtime-compilation">Runtime compilation</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#target-gpu-architectures-gfx-ip">Target GPU architectures (GFX IP)</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#amdgpu-assembly">AMDGPU assembly</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#amdgpu-intermediate-representation">AMDGPU intermediate representation</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-binary-utilities">ROCm binary utilities</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#static-libraries">Static libraries</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="hip-compilers">
<span id="id1"></span><h1>HIP compilers<a class="headerlink" href="#hip-compilers" title="Link to this heading">#</a></h1>
<p>ROCm provides tools for compiling HIP applications for use on
AMD GPUs. The compilers set up the default libraries, and include paths for the
HIP and ROCm libraries, along with required environment variables. For more
information, see the <a class="reference external" href="https://rocm.docs.amd.com/projects/llvm-project/en/latest/reference/rocmcc.html" title="(in llvm-project Documentation v22.0.0)"><span class="xref std std-doc">ROCm compiler reference</span></a>.</p>
<section id="compilation-workflow">
<h2>Compilation workflow<a class="headerlink" href="#compilation-workflow" title="Link to this heading">#</a></h2>
<p>HIP provides a flexible compilation workflow that supports both offline
compilation and runtime or just-in-time (JIT) compilation. Each approach has
advantages depending on the use case, target architecture, and performance
needs.</p>
<p>The offline compilation is ideal for production environments, where the
performance is critical, and the target GPU architecture is known in advance.</p>
<p>The runtime compilation is useful in development environments or when
distributing software that must run on a wide range of hardware without the
knowledge of the GPU in advance. It provides flexibility at the cost of some
The runtime compilation is useful in development environments or when
distributing software that must run on a wide range of hardware without prior
knowledge of the GPU. It provides flexibility at the cost of some
performance overhead.</p>
<section id="offline-compilation">
<h3>Offline compilation<a class="headerlink" href="#offline-compilation" title="Link to this heading">#</a></h3>
<p>Offline compilation is performed in two steps: host and  device code
compilation.</p>
<ul class="simple">
<li><p>Host-code compilation: On the host side, <code class="docutils literal notranslate"><span class="pre">amdclang++</span></code> or <code class="docutils literal notranslate"><span class="pre">hipcc</span></code> can
compile the host code in one step without other C++ compilers.</p></li>
<li><p>Device-code compilation: The compiled device code is embedded into the
host object file. Depending on the platform, the device code can be compiled
into assembly or binary.</p></li>
</ul>
<p>For an example on how to compile HIP from the command line, see <a class="reference internal" href="../tutorial/saxpy.html#compiling-on-the-command-line"><span class="std std-ref">SAXPY
tutorial</span></a> .</p>
</section>
<section id="runtime-compilation">
<h3>Runtime compilation<a class="headerlink" href="#runtime-compilation" title="Link to this heading">#</a></h3>
<p>HIP allows you to compile kernels at runtime using the <code class="docutils literal notranslate"><span class="pre">hiprtc*</span></code> API. Kernels
are stored as a text string, which is passed to HIPRTC alongside options to
guide the compilation.</p>
<p>For more information, see <a class="reference internal" href="../how-to/hip_rtc.html"><span class="doc">HIP runtime compiler</span></a>.</p>
</section>
</section>
<section id="target-gpu-architectures-gfx-ip">
<span id="gfx-ip"></span><h2>Target GPU architectures (GFX IP)<a class="headerlink" href="#target-gpu-architectures-gfx-ip" title="Link to this heading">#</a></h2>
<p>Instructions in the AMDGPU instruction set architecture (ISA) are compatible
only with certain physical GPU architectures. The versioning system that
abstracts hardware details from compilers and software is called the GFX IP
version. Each AMD GPU family, such as RDNA or CDNA, defines its own GFX IP
identifiers. These identifiers specify which instruction formats, memory
models, and compute features are supported by that generation of hardware.</p>
<p>A GFX version is expressed as a short string, for example:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gfx90a</span></code> — CDNA2 (MI250 series)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gfx942</span></code> — CDNA3 (MI300 series)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gfx1100</span></code> — RDNA3 (RX 7900 series)</p></li>
</ul>
<p>Most GFX IP versions are composed of three numerical fields, which act roughly
like a major-minor-subminor versioning system:</p>
<ul class="simple">
<li><p>The major version corresponds to the architectural family (for example,
CDNA3 versus RDNA3).</p></li>
<li><p>The minor version encodes core feature updates within that family (for
example, new <a class="reference internal" href="hardware_implementation.html#mfma-units"><span class="std std-ref">MFMA</span></a> or <a class="reference internal" href="hardware_implementation.html#lds"><span class="std std-ref">LDS</span></a> capabilities).</p></li>
<li><p>The subminor version may specify packaging or stepping differences (for
example, MI300A versus MI300X).</p></li>
</ul>
<p>Each new generation introduces additional hardware features, for example,
mixed-precision MFMA instructions, asynchronous data movement engines, and
updated cache hierarchies, while maintaining broad forward compatibility for
code compiled at the intermediate representation (IR) level. When compiling GPU
programs with <code class="docutils literal notranslate"><span class="pre">amdclang++</span></code>, the target GFX architecture determines the ISA
and hardware features available to the kernel.</p>
<p>For example, compiling for the MI300X would use:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>amdclang++<span class="w"> </span>--offload-arch<span class="o">=</span>gfx942<span class="w"> </span>kernel.cpp<span class="w"> </span>-o<span class="w"> </span>kernel.out
</pre></div>
</div>
<p>The compiler uses this flag to emit optimized machine code for that GPU’s
<a class="reference internal" href="hardware_implementation.html#compute-unit"><span class="std std-ref">compute units</span></a>, <a class="reference internal" href="hardware_implementation.html#mfma-units"><span class="std std-ref">matrix cores</span></a>, and
memory subsystem. The GFX IP acts as a virtual hardware target, decoupling
high-level programming models (HIP, OpenMP, OpenCL) from the underlying physical
GPU design.</p>
<p>While AMD does not explicitly name its compatibility model as “onion-layered,”
the GFX IP system follows a similar principle: newer architectures generally
extend, rather than break, existing instruction sets.</p>
<p>Thus, code compiled for an older architecture (for example, <code class="docutils literal notranslate"><span class="pre">gfx90a</span></code>) can
often be re-optimized or recompiled for a newer one (<code class="docutils literal notranslate"><span class="pre">gfx942</span></code>) with minimal
modification. However, compatibility is not guaranteed across major GFX
families, since those may introduce fundamentally new pipelines or execution
semantics.</p>
</section>
<section id="amdgpu-assembly">
<span id="id2"></span><h2>AMDGPU assembly<a class="headerlink" href="#amdgpu-assembly" title="Link to this heading">#</a></h2>
<p>AMDGPU assembly, sometimes called GFX ISA (Instruction Set Architecture), is
the low-level assembly format for programs running directly on AMD GPUs. It is
the lowest-level human-readable representation of GPU instructions, typically
generated by the ROCm compiler toolchain and converted into binary microcode
for execution on the device.</p>
<p>Each AMD GPU architecture family, such as RDNA or CDNA, defines its own GFX ISA
version. For example:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gfx90a</span></code> corresponds to CDNA2 (MI250 series)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gfx942</span></code> corresponds to CDNA3 (MI300 series)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gfx1100</span></code> corresponds to RDNA3 consumer GPUs</p></li>
</ul>
<p>Each version defines its unique instruction encodings, supported data types,
and pipeline behavior. Compiled GPU kernels must target a specific <a class="reference internal" href="#gfx-ip"><span class="std std-ref">GFX
architecture</span></a> to ensure instruction compatibility and optimal
scheduling.</p>
<p>AMDGPU assembly is rich and expressive, exposing every level of GPU behavior:
scalar operations, vector math, memory access, synchronization, and
matrix-multiply instructions. A few examples of instructions from the
<code class="docutils literal notranslate"><span class="pre">gfx942</span></code> architecture include:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">v_add_f32</span> <span class="pre">v0,</span> <span class="pre">v1,</span> <span class="pre">v2</span></code> — add 32-bit floats in vector registers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s_mov_b32</span> <span class="pre">s4,</span> <span class="pre">0x3f800000</span></code> — move immediate value (1.0f) into a scalar
register</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">v_mfma_f32_16x16x4f16</span> <span class="pre">v[0:15],</span> <span class="pre">v[16:31],</span> <span class="pre">v[32:47],</span> <span class="pre">v[0:15]</span></code> — perform a
16×16×4 matrix fused multiply-add</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s_barrier</span></code> — synchronize all warps in the work-group</p></li>
</ul>
<p>In this syntax:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">v_</span></code> instructions operate on vector registers (VGPRs) per thread.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">s_</span></code> instructions operate on scalar registers (SGPRs) shared by the warp.</p></li>
<li><p>Specialized matrix instructions (<code class="docutils literal notranslate"><span class="pre">v_mfma_*</span></code>) invoke the <a class="reference internal" href="hardware_implementation.html#mfma-units"><span class="std std-ref">Matrix Core
(MFMA) hardware units</span></a>.</p></li>
</ul>
<p>Although AMDGPU assembly can be written by hand, this is uncommon. Developers typically inspect compiler‑generated assembly when optimizing kernels, diagnosing register pressure, or tuning memory‑access patterns</p>
<p>The ROCm disassembler (<code class="docutils literal notranslate"><span class="pre">llvm-objdump</span></code>) and ROCm profiler (<code class="docutils literal notranslate"><span class="pre">rocprofv3</span></code>)
allow inspection of generated GFX ISA alongside high-level HIP or OpenMP source
code. Because the instruction semantics and binary encodings are publicly
documented by AMD, the GFX ISA is a fully open, compiler-targetable standard.</p>
<p>This openness allows tool developers, performance engineers, and researchers to
reason about GPU behavior at the instruction level, bridging the gap
between hardware and high-level kernel code.</p>
</section>
<section id="amdgpu-intermediate-representation">
<span id="amdgpu-ir"></span><h2>AMDGPU intermediate representation<a class="headerlink" href="#amdgpu-intermediate-representation" title="Link to this heading">#</a></h2>
<p>AMDGPU intermediate representation (AMDGPU IR) is an intermediate
representation for code that runs on AMD GPUs and other parallel processors. It
is one of the key outputs of the ROCm compiler toolchain, produced by
<code class="docutils literal notranslate"><span class="pre">amdclang++</span></code> before being translated into architecture-specific GPU assembly
(<a class="reference internal" href="#amdgpu-assembly"><span class="std std-ref">GFX ISA</span></a>).</p>
<p>AMD documentation refers to this layer as both a virtual instruction set and
a target-specific dialect of LLVM IR. From a programmer’s perspective, AMDGPU
IR defines a virtual machine model for parallel thread execution: compilers and
optimizers emit this IR with the expectation that it will execute with consistent semantics
across multiple generations of AMD hardware, including future architectures not
yet released.</p>
<p>This makes AMDGPU IR a “narrow waist” between software and hardware,
abstracting the details of the physical <a class="reference internal" href="hardware_implementation.html#compute-unit"><span class="std std-ref">compute units</span></a>,
<a class="reference internal" href="programming_model.html#wavefront"><span class="std std-ref">warp</span></a> schedulers, and memory hierarchies, while still
providing explicit control over threads, registers, and memory spaces.</p>
<p>Unlike traditional CPU ISAs, AMDGPU IR is not executed directly. Instead, it is
further compiled (either just‑in‑time or ahead‑of‑time) into GFX ISA, the
device-specific binary that runs on a given GPU architecture (for example,
<code class="docutils literal notranslate"><span class="pre">gfx942</span></code> for CDNA3 MI300X or <code class="docutils literal notranslate"><span class="pre">gfx1200</span></code> for RDNA3). This multi-stage
compilation allows forward compatibility: kernels compiled for one generation
can often be re-optimized and executed efficiently on newer hardware through
updated ROCm runtimes and drivers. Some exemplary fragments of AMDGPU IR:</p>
<div class="highlight-llvm notranslate"><div class="highlight"><pre><span></span><span class="c">; declare usage of 64 vector registers</span>
<span class="nv">!amdgpu.num_vgpr</span><span class="w"> </span><span class="p">=</span><span class="w"> </span><span class="p">!{</span><span class="kt">i32</span><span class="w"> </span><span class="m">64</span><span class="p">}</span>

<span class="c">; perform fused multiply-add</span>
<span class="nv">%f5</span><span class="w"> </span><span class="p">=</span><span class="w"> </span><span class="k">call</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="vg">@llvm.fma.f32</span><span class="p">(</span><span class="kt">float</span><span class="w"> </span><span class="nv">%f3</span><span class="p">,</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="nv">%f4</span><span class="p">,</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="m">1.5</span><span class="p">)</span>

<span class="c">; read thread and workgroup indices</span>
<span class="nv">%tid</span><span class="w">  </span><span class="p">=</span><span class="w"> </span><span class="k">call</span><span class="w"> </span><span class="kt">i32</span><span class="w"> </span><span class="vg">@llvm.amdgcn.workitem.id.x</span><span class="p">()</span>
<span class="nv">%wgid</span><span class="w"> </span><span class="p">=</span><span class="w"> </span><span class="k">call</span><span class="w"> </span><span class="kt">i32</span><span class="w"> </span><span class="vg">@llvm.amdgcn.workgroup.id.x</span><span class="p">()</span>
</pre></div>
</div>
<p>These instructions represent operations in the virtual machine model:</p>
<ul class="simple">
<li><p>Registers are virtual VGPRs/SGPRs dynamically mapped to physical hardware
registers by the compiler.</p></li>
<li><p>Arithmetic and memory intrinsics (<code class="docutils literal notranslate"><span class="pre">llvm.fma</span></code>, <code class="docutils literal notranslate"><span class="pre">llvm.amdgcn.buffer.load</span></code>)
map one-to-one to GPU instructions.</p></li>
<li><p>Built-in functions like <code class="docutils literal notranslate"><span class="pre">llvm.amdgcn.workitem.id.x()</span></code> access special
per-thread state, such as the current thread or
<a class="reference internal" href="programming_model.html#inherent-thread-hierarchy-block"><span class="std std-ref">block</span></a> index.</p></li>
</ul>
<p>The AMDGPU IR machine model reflects the hardware reality of AMD GPUs: a single
instruction stream drives a <a class="reference internal" href="programming_model.html#wavefront"><span class="std std-ref">wavefront</span></a> of 64 threads that
execute in lockstep on the SIMD pipelines, each maintaining its own register
state while sharing program flow and <a class="reference internal" href="hardware_implementation.html#lds"><span class="std std-ref">local memory</span></a>.
Warps cooperate through the <a class="reference internal" href="hardware_implementation.html#lds"><span class="std std-ref">Local Data Share (LDS)</span></a> and synchronize
via barriers, the same abstractions exposed in the high-level ROCm programming
model.</p>
<p>Since AMDGPU IR is integrated with the open-source LLVM compiler
infrastructure, its syntax and semantics are well-documented and publicly
accessible. Developers can inspect, modify, or emit AMDGPU IR directly for
performance analysis, research, or custom toolchains.</p>
</section>
<section id="rocm-binary-utilities">
<span id="binary-utilities"></span><h2>ROCm binary utilities<a class="headerlink" href="#rocm-binary-utilities" title="Link to this heading">#</a></h2>
<p>The ROCm binary utilities are a collection of command-line tools for examining
and manipulating GPU binaries produced by <code class="docutils literal notranslate"><span class="pre">amdclang++</span></code> or other ROCm build
tools. These utilities allow developers to inspect, disassemble, and analyze
AMDGPU code objects, the compiled GPU kernels embedded in host executables or
distributed as standalone <code class="docutils literal notranslate"><span class="pre">.hsaco</span></code> files.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">llvm-objdump</span></code> utility provides multiple capabilities for analyzing GPU
binaries. With the <code class="docutils literal notranslate"><span class="pre">--offloading</span></code> flag, it can list and extract information
from the contents of ROCm binaries, including code object metadata, kernel
symbols, target architectures (for example, <code class="docutils literal notranslate"><span class="pre">gfx90a</span></code>, <code class="docutils literal notranslate"><span class="pre">gfx1100</span></code>), and
linkage details. It supports both standalone <code class="docutils literal notranslate"><span class="pre">.hsaco</span></code> files and “fat
binaries” embedded within host executables. With the <code class="docutils literal notranslate"><span class="pre">--triple=amdgcn</span></code> flag,
it can disassemble GPU kernels into human-readable AMDGPU ISA, allowing
inspection of instruction sequences, register allocation, and control flow.
These capabilities are essential for performance debugging, code verification,
and low-level kernel analysis, for example, when tuning <a class="reference internal" href="hardware_implementation.html#mfma-units"><span class="std std-ref">MFMA</span></a> instructions or checking compiler optimizations.</p>
<p>Together, these utilities provide developers with insight into how HIP C++ code
is compiled, optimized, and mapped to GPU hardware. They complement profiling
tools like <code class="docutils literal notranslate"><span class="pre">rocprofv3</span></code> by exposing the static structure of compiled GPU
binaries.</p>
</section>
<section id="static-libraries">
<h2>Static libraries<a class="headerlink" href="#static-libraries" title="Link to this heading">#</a></h2>
<p><code class="docutils literal notranslate"><span class="pre">amdclang++</span></code> supports generating two types of static libraries.</p>
<ul>
<li><p>The first type of static library only exports and launches host functions
within the same library and not the device functions. This library type
offers the ability to link with another compiler such as <code class="docutils literal notranslate"><span class="pre">gcc</span></code>.
Additionally, this library type contains host objects with device code
embedded as fat binaries. This library type is generated using the flag
<code class="docutils literal notranslate"><span class="pre">--emit-static-lib</span></code>:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>amdclang++<span class="w"> </span>hipOptLibrary.cpp<span class="w"> </span>--emit-static-lib<span class="w"> </span>-fPIC<span class="w"> </span>-o<span class="w"> </span>libHipOptLibrary.a
gcc<span class="w"> </span>test.cpp<span class="w"> </span>-L.<span class="w"> </span>-lhipOptLibrary<span class="w"> </span>-L/path/to/hip/lib<span class="w"> </span>-lamdhip64<span class="w"> </span>-o<span class="w"> </span>test.out
</pre></div>
</div>
</li>
<li><p>The second type of static library exports device functions to be linked by
other code objects by using <code class="docutils literal notranslate"><span class="pre">amdclang++</span></code> as the linker. This library type
contains relocatable device objects and is generated using
<code class="docutils literal notranslate"><span class="pre">ar</span></code>:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>amdclang++<span class="w"> </span>hipDevice.cpp<span class="w"> </span>-c<span class="w"> </span>-fgpu-rdc<span class="w"> </span>-o<span class="w"> </span>hipDevice.o
ar<span class="w"> </span>rcsD<span class="w"> </span>libHipDevice.a<span class="w"> </span>hipDevice.o
amdclang++<span class="w"> </span>libHipDevice.a<span class="w"> </span>test.cpp<span class="w"> </span>-fgpu-rdc<span class="w"> </span>-o<span class="w"> </span>test.out
</pre></div>
</div>
</li>
</ul>
<p>Examples of this can be found in <a class="reference external" href="https://github.com/ROCm/rocm-examples">rocm-examples</a> under <a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic/static_host_library">static host libraries</a>
or <a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic/static_device_library">static device libraries</a>.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="hardware_implementation.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Hardware implementation</p>
      </div>
    </a>
    <a class="right-next"
       href="../how-to/performance_guidelines.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Performance guidelines</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#compilation-workflow">Compilation workflow</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#offline-compilation">Offline compilation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#runtime-compilation">Runtime compilation</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#target-gpu-architectures-gfx-ip">Target GPU architectures (GFX IP)</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#amdgpu-assembly">AMDGPU assembly</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#amdgpu-intermediate-representation">AMDGPU intermediate representation</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-binary-utilities">ROCm binary utilities</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#static-libraries">Static libraries</a></li>
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
