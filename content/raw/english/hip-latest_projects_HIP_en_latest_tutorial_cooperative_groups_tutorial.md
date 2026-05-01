---
title: "Cooperative groups &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/cooperative_groups_tutorial.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:39.384359+00:00
content_hash: "22979156508d7376"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="HIP cooperative groups tutorial" name="description" />
<meta content="AMD, ROCm, HIP, cooperative groups, tutorial" name="keywords" />

    <title>Cooperative groups &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'tutorial/cooperative_groups_tutorial';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="HIP Graph API Tutorial" href="graph_api.html" />
    <link rel="prev" title="Reduction" href="reduction.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/tutorial/cooperative_groups_tutorial.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Cooperative groups</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">Cooperative groups</li>
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
    <h1>Cooperative groups</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#prerequisites">Prerequisites</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#simple-hip-code">Simple HIP Code</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#tiled-partition">Tiled partition</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#device-side-code">Device-side code</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#initialization-of-the-reduction-function-variables">1. Initialization of the reduction function variables</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#the-reduction-of-thread-block">2. The reduction of thread block</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#the-reduction-of-custom-partition">3. The reduction of custom partition</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#host-side-code">Host-side code</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#confirm-the-cooperative-group-support-on-amd-gpus">1. Confirm the cooperative group support on AMD GPUs</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#initialize-the-cooperative-group-configuration">2. Initialize the cooperative group configuration</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#launch-the-kernel">4. Launch the kernel</a></li>
</ul>
</li>
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
                  
  <section id="cooperative-groups">
<h1>Cooperative groups<a class="headerlink" href="#cooperative-groups" title="Link to this heading">#</a></h1>
<p>This tutorial demonstrates the basic concepts of cooperative groups in the HIP (Heterogeneous-computing Interface for Portability) programming model and the most essential tooling supporting it. This topic also reviews the commonalities of heterogeneous APIs. Familiarity with the C/C++ compilation model and the language is assumed.</p>
<section id="prerequisites">
<h2>Prerequisites<a class="headerlink" href="#prerequisites" title="Link to this heading">#</a></h2>
<p>To follow this tutorial, you’ll need properly installed drivers and a HIP compiler toolchain to compile your code. Because ROCm HIP supports compiling and running on Linux and Microsoft Windows with AMD GPUs, review the HIP development package installation before starting this tutorial. For more information, see <a class="reference internal" href="../install/install.html"><span class="doc">Install HIP</span></a>.</p>
</section>
<section id="simple-hip-code">
<h2>Simple HIP Code<a class="headerlink" href="#simple-hip-code" title="Link to this heading">#</a></h2>
<p>To become familiar with heterogeneous programming, review the <a class="reference internal" href="saxpy.html"><span class="doc">SAXPY tutorial</span></a> and the first HIP code subsection. Compiling is also described in that tutorial.</p>
</section>
<section id="tiled-partition">
<h2>Tiled partition<a class="headerlink" href="#tiled-partition" title="Link to this heading">#</a></h2>
<p>You can use tiled partition to calculate the sum of <code class="docutils literal notranslate"><span class="pre">partition_size</span></code> length sequences and the sum of <code class="docutils literal notranslate"><span class="pre">result_size</span></code>/ <code class="docutils literal notranslate"><span class="pre">BlockSize</span></code> length sequences. The host-side reference implementation is the following:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Host-side function to perform the same reductions as executed on the GPU</span>
<span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="o">&gt;</span><span class="w"> </span><span class="n">ref_reduced</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w">        </span><span class="n">partition_size</span><span class="p">,</span>
<span class="w">                                      </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="o">&gt;</span><span class="w"> </span><span class="n">input</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w">        </span><span class="n">input_size</span><span class="w">  </span><span class="o">=</span><span class="w"> </span><span class="n">input</span><span class="p">.</span><span class="n">size</span><span class="p">();</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w">        </span><span class="n">result_size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">input_size</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">partition_size</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="o">&gt;</span><span class="w"> </span><span class="n">result</span><span class="p">(</span><span class="n">result_size</span><span class="p">);</span>

<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">result_size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">partition_result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">        </span><span class="k">for</span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">partition_size</span><span class="p">;</span><span class="w"> </span><span class="n">j</span><span class="o">++</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="n">partition_result</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">input</span><span class="p">[</span><span class="n">partition_size</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">j</span><span class="p">];</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="n">result</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">partition_result</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">result</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<section id="device-side-code">
<h3>Device-side code<a class="headerlink" href="#device-side-code" title="Link to this heading">#</a></h3>
<p>To calculate the sum of the sets of numbers, the tutorial uses the shared memory-based reduction on the device side. The warp level intrinsics usage is not covered in this tutorial, unlike in the <a class="reference internal" href="reduction.html"><span class="doc">reduction tutorial.</span></a> <code class="docutils literal notranslate"><span class="pre">x</span></code> input variable is a shared pointer, which needs to be synchronized after every value change. The <code class="docutils literal notranslate"><span class="pre">thread_group</span></code> input parameter can be <code class="docutils literal notranslate"><span class="pre">thread_block_tile</span></code> or <code class="docutils literal notranslate"><span class="pre">thread_block</span></code> because the <code class="docutils literal notranslate"><span class="pre">thread_group</span></code> is the parent class of these types. The <code class="docutils literal notranslate"><span class="pre">val</span></code> are the numbers to calculate the sum of. The returned results of this function return the final results of the reduction on thread ID 0 of the <code class="docutils literal notranslate"><span class="pre">thread_group</span></code>, and for every other thread, the function results are 0.</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">/// \brief Summation of `unsigned int val`&#39;s in `thread_group g` using shared memory `x`</span>
<span class="kt">__device__</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">reduce_sum</span><span class="p">(</span><span class="n">thread_group</span><span class="w"> </span><span class="n">g</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">x</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">val</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// Rank of this thread in the group</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">group_thread_id</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">g</span><span class="p">.</span><span class="n">thread_rank</span><span class="p">();</span>

<span class="w">    </span><span class="c1">// We start with half the group size as active threads</span>
<span class="w">    </span><span class="c1">// Every iteration the number of active threads halves, until we processed all values</span>
<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">g</span><span class="p">.</span><span class="n">size</span><span class="p">()</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">/=</span><span class="w"> </span><span class="mi">2</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="c1">// Store value for this thread in a shared, temporary array</span>
<span class="w">        </span><span class="n">x</span><span class="p">[</span><span class="n">group_thread_id</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">val</span><span class="p">;</span>

<span class="w">        </span><span class="c1">// Synchronize all threads in the group</span>
<span class="w">        </span><span class="n">g</span><span class="p">.</span><span class="n">sync</span><span class="p">();</span>

<span class="w">        </span><span class="c1">// If our thread is still active, sum with its counterpart in the other half</span>
<span class="w">        </span><span class="k">if</span><span class="p">(</span><span class="n">group_thread_id</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">i</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="n">val</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">x</span><span class="p">[</span><span class="n">group_thread_id</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">];</span>
<span class="w">        </span><span class="p">}</span>

<span class="w">        </span><span class="c1">// Synchronize all threads in the group</span>
<span class="w">        </span><span class="n">g</span><span class="p">.</span><span class="n">sync</span><span class="p">();</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Only the first thread returns a valid value</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">g</span><span class="p">.</span><span class="n">thread_rank</span><span class="p">()</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">val</span><span class="p">;</span>
<span class="w">    </span><span class="k">else</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>The <code class="docutils literal notranslate"><span class="pre">reduce_sum</span></code> device function is reused to calculate the block and custom
partition sum of the input numbers. The kernel has three sections:</p>
<ol class="arabic simple">
<li><p>Initialization of the reduction function variables.</p></li>
<li><p>The reduction of thread block and store the results in global memory.</p></li>
<li><p>The reduction of custom partition and store the results in global memory.</p></li>
</ol>
<section id="initialization-of-the-reduction-function-variables">
<h4>1. Initialization of the reduction function variables<a class="headerlink" href="#initialization-of-the-reduction-function-variables" title="Link to this heading">#</a></h4>
<p>In this code section, the shared memory is declared, the thread_block_group and
custom_partition are defined, and the input variables are loaded from global
memory.</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// threadBlockGroup consists of all threads in the block</span>
<span class="n">thread_block</span><span class="w"> </span><span class="n">thread_block_group</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">this_thread_block</span><span class="p">();</span>

<span class="c1">// Workspace array in shared memory required for reduction</span>
<span class="kt">__shared__</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">workspace</span><span class="p">[</span><span class="mi">2048</span><span class="p">];</span>

<span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">output</span><span class="p">;</span>

<span class="c1">// Input to reduce</span>
<span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">input</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">d_vector</span><span class="p">[</span><span class="n">thread_block_group</span><span class="p">.</span><span class="n">thread_rank</span><span class="p">()];</span>

<span class="c1">// ...</span>

<span class="c1">// Every custom_partition group consists of 16 threads</span>
<span class="n">thread_block_tile</span><span class="o">&lt;</span><span class="n">PartitionSize</span><span class="o">&gt;</span><span class="w"> </span><span class="n">custom_partition</span>
<span class="w">        </span><span class="o">=</span><span class="w"> </span><span class="n">tiled_partition</span><span class="o">&lt;</span><span class="n">PartitionSize</span><span class="o">&gt;</span><span class="p">(</span><span class="n">thread_block_group</span><span class="p">);</span>
</pre></div>
</div>
</section>
<section id="the-reduction-of-thread-block">
<h4>2. The reduction of thread block<a class="headerlink" href="#the-reduction-of-thread-block" title="Link to this heading">#</a></h4>
<p>In this code section, the sum is calculated on <code class="docutils literal notranslate"><span class="pre">thread_block_group</span></code> level, then the results are stored in global memory.</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Perform reduction</span>
<span class="n">output</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">reduce_sum</span><span class="p">(</span><span class="n">thread_block_group</span><span class="p">,</span><span class="w"> </span><span class="n">workspace</span><span class="p">,</span><span class="w"> </span><span class="n">input</span><span class="p">);</span>

<span class="c1">// Only the first thread returns a valid value</span>
<span class="k">if</span><span class="p">(</span><span class="n">thread_block_group</span><span class="p">.</span><span class="n">thread_rank</span><span class="p">()</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">d_block_reduced_vector</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">output</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="the-reduction-of-custom-partition">
<h4>3. The reduction of custom partition<a class="headerlink" href="#the-reduction-of-custom-partition" title="Link to this heading">#</a></h4>
<p>In this code section, the sum is calculated on the custom partition level, then the results are stored in global memory. The custom partition is a partial block of the thread block, it means the reduction calculates on a shorter sequence of input numbers than at the <code class="docutils literal notranslate"><span class="pre">thread_block_group</span></code> case.</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="c1">// Perform reduction</span>
<span class="n">output</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">reduce_sum</span><span class="p">(</span><span class="n">custom_partition</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">workspace</span><span class="p">[</span><span class="n">group_offset</span><span class="p">],</span><span class="w"> </span><span class="n">input</span><span class="p">);</span>

<span class="c1">// Only the first thread in each partition returns a valid value</span>
<span class="k">if</span><span class="p">(</span><span class="n">custom_partition</span><span class="p">.</span><span class="n">thread_rank</span><span class="p">()</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">partition_id</span><span class="w">          </span><span class="o">=</span><span class="w"> </span><span class="n">thread_block_group</span><span class="p">.</span><span class="n">thread_rank</span><span class="p">()</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">PartitionSize</span><span class="p">;</span>
<span class="w">    </span><span class="n">d_partition_reduced_vector</span><span class="p">[</span><span class="n">partition_id</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">output</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
</section>
<section id="host-side-code">
<h3>Host-side code<a class="headerlink" href="#host-side-code" title="Link to this heading">#</a></h3>
<p>On the host-side, the following steps are done in the example:</p>
<ol class="arabic simple">
<li><p>Confirm the cooperative group support on AMD GPUs.</p></li>
<li><p>Initialize the cooperative group configuration.</p></li>
<li><p>Allocate and copy input to global memory.</p></li>
<li><p>Launch the cooperative kernel.</p></li>
<li><p>Save the results from global memory.</p></li>
<li><p>Free the global memory.</p></li>
</ol>
<p>Only the first, second and fourth steps are important from the cooperative groups aspect, that’s why those steps are detailed further.</p>
<section id="confirm-the-cooperative-group-support-on-amd-gpus">
<h4>1. Confirm the cooperative group support on AMD GPUs<a class="headerlink" href="#confirm-the-cooperative-group-support-on-amd-gpus" title="Link to this heading">#</a></h4>
<p>Not all AMD GPUs support cooperative groups. You can confirm support with the following code:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#ifdef __HIP_PLATFORM_AMD__</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">device</span><span class="w">               </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">supports_coop_launch</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// Check support</span>
<span class="w">    </span><span class="c1">// Use hipDeviceAttributeCooperativeMultiDeviceLaunch when launching across multiple devices</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDevice</span><span class="p">(</span><span class="o">&amp;</span><span class="n">device</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span>
<span class="w">        </span><span class="n">hipDeviceGetAttribute</span><span class="p">(</span><span class="o">&amp;</span><span class="n">supports_coop_launch</span><span class="p">,</span><span class="w"> </span><span class="n">hipDeviceAttributeCooperativeLaunch</span><span class="p">,</span><span class="w"> </span><span class="n">device</span><span class="p">));</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="o">!</span><span class="n">supports_coop_launch</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Skipping, device &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">device</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; does not support cooperative groups&quot;</span>
<span class="w">                  </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="cp">#endif</span>
</pre></div>
</div>
</section>
<section id="initialize-the-cooperative-group-configuration">
<h4>2. Initialize the cooperative group configuration<a class="headerlink" href="#initialize-the-cooperative-group-configuration" title="Link to this heading">#</a></h4>
<p>In the example, there is only one block in the grid, and the <code class="docutils literal notranslate"><span class="pre">threads_per_block</span></code> must be dividable with <code class="docutils literal notranslate"><span class="pre">partition_size</span></code>.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Number of blocks to launch.</span>
<span class="k">constexpr</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">num_blocks</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>

<span class="c1">// Number of threads in each kernel block.</span>
<span class="k">constexpr</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">threads_per_block</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">64</span><span class="p">;</span>

<span class="c1">// Total element count of the input vector.</span>
<span class="k">constexpr</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">num_blocks</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">threads_per_block</span><span class="p">;</span>

<span class="c1">// Total elements count of a tiled_partition.</span>
<span class="k">constexpr</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">partition_size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">16</span><span class="p">;</span>

<span class="c1">// Total size (in bytes) of the input vector.</span>
<span class="k">constexpr</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size_bytes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">size</span><span class="p">;</span>

<span class="k">static_assert</span><span class="p">(</span><span class="n">threads_per_block</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="n">partition_size</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">              </span><span class="s">&quot;threads_per_block must be a multiple of partition_size&quot;</span><span class="p">);</span>
</pre></div>
</div>
</section>
<section id="launch-the-kernel">
<h4>4. Launch the kernel<a class="headerlink" href="#launch-the-kernel" title="Link to this heading">#</a></h4>
<p>The kernel launch is done with the <code class="docutils literal notranslate"><span class="pre">hipLaunchCooperativeKernel</span></code> of the  cooperative groups API.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">params</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="o">&amp;</span><span class="n">d_vector</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">d_block_reduced</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">d_partition_reduced</span><span class="p">};</span>
<span class="c1">// Launching kernel from host.</span>
<span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipLaunchCooperativeKernel</span><span class="p">(</span><span class="n">vector_reduce_kernel</span><span class="o">&lt;</span><span class="n">partition_size</span><span class="o">&gt;</span><span class="p">,</span>
<span class="w">                                     </span><span class="n">dim3</span><span class="p">(</span><span class="n">num_blocks</span><span class="p">),</span>
<span class="w">                                     </span><span class="n">dim3</span><span class="p">(</span><span class="n">threads_per_block</span><span class="p">),</span>
<span class="w">                                     </span><span class="n">params</span><span class="p">,</span>
<span class="w">                                     </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                                     </span><span class="n">hipStreamDefault</span><span class="p">));</span>\

<span class="c1">// Check if the kernel launch was successful.</span>
<span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetLastError</span><span class="p">());</span>
</pre></div>
</div>
</section>
</section>
</section>
<section id="conclusion">
<h2>Conclusion<a class="headerlink" href="#conclusion" title="Link to this heading">#</a></h2>
<p>With cooperative groups, you can easily use custom partitions to create custom tiles for custom solutions. You can find the complete code at <a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic/cooperative_groups">cooperative groups ROCm example.</a></p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="reduction.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Reduction</p>
      </div>
    </a>
    <a class="right-next"
       href="graph_api.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">HIP Graph API Tutorial</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#prerequisites">Prerequisites</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#simple-hip-code">Simple HIP Code</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#tiled-partition">Tiled partition</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#device-side-code">Device-side code</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#initialization-of-the-reduction-function-variables">1. Initialization of the reduction function variables</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#the-reduction-of-thread-block">2. The reduction of thread block</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#the-reduction-of-custom-partition">3. The reduction of custom partition</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#host-side-code">Host-side code</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#confirm-the-cooperative-group-support-on-amd-gpus">1. Confirm the cooperative group support on AMD GPUs</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#initialize-the-cooperative-group-configuration">2. Initialize the cooperative group configuration</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#launch-the-kernel">4. Launch the kernel</a></li>
</ul>
</li>
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
