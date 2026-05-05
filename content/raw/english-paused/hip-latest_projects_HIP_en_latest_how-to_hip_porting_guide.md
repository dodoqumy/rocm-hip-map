---
title: "Porting CUDA code to HIP &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_porting_guide.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:05:31.512853+00:00
content_hash: "9811b78c83dc3d7b"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="This chapter presents how to port CUDA source code to HIP" name="description" />
<meta content="AMD, ROCm, HIP, CUDA, driver API, porting, port" name="keywords" />

    <title>Porting CUDA code to HIP &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/hip_porting_guide';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Programming for HIP runtime compiler (RTC)" href="hip_rtc.html" />
    <link rel="prev" title="Kernel language C++ support" href="kernel_language_cpp_support.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/hip_porting_guide.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1"><a class="reference internal" href="../understand/programming_model.html">Introduction to the HIP programming model</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/performance_optimization.html">Understanding GPU performance</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/hardware_implementation.html">Hardware implementation</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/compilers.html">HIP compilers</a></li>
<li class="toctree-l1"><a class="reference internal" href="performance_guidelines.html">Performance guidelines</a></li>
<li class="toctree-l1"><a class="reference internal" href="debugging.html">Debugging with HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="logging.html">Logging HIP activity</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="hip_runtime_api.html">Using HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/initialization.html">Initialization</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="hip_runtime_api/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/memory_management/host_memory.html">Host memory</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="hip_runtime_api/memory_management/device_memory.html">Device memory</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/memory_management/device_memory/texture_fetching.html">Texture fetching</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/memory_management/coherence_control.html">Coherence control</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/memory_management/unified_memory.html">Unified memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/memory_management/virtual_memory.html">Virtual memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/memory_management/stream_ordered_allocator.html">Stream Ordered Memory Allocator</a></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/error_handling.html">Error handling</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/call_stack.html">Call stack</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/asynchronous.html">Asynchronous concurrent execution</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/hipgraph.html">HIP graphs</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/cooperative_groups.html">Cooperative groups</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/multi_device.html">Multi-device management</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/opengl_interop.html">OpenGL interoperability</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/external_interop.html">External resource interoperability</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="hip_cpp_language_extensions.html">HIP C++ language extensions</a></li>
<li class="toctree-l1"><a class="reference internal" href="kernel_language_cpp_support.html">Kernel language C++ support</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Porting CUDA code to HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="hip_rtc.html">Programming for HIP runtime compiler (RTC)</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">Porting...</li>
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
    <h1>Porting CUDA code to HIP</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#porting-a-cuda-project">Porting a CUDA project</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#general-tips">General tips</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#using-hipify">Using HIPIFY</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-copy-functions">Memory copy functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#address-spaces">Address spaces</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#context-stack-behavior-differences">Context stack behavior differences</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#scanning-cuda-source-to-scope-the-translation">Scanning CUDA source to scope the translation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#automatically-converting-a-cuda-project">Automatically converting a CUDA project</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#library-and-driver-equivalents">Library and driver equivalents</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#cumodule-and-hipmodule">cuModule and hipModule</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#using-hipmodulelaunchkernel">Using hipModuleLaunchKernel</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#cuctx-and-hipctx">cuCtx and hipCtx</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#compilation">Compilation</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-headers">HIP Headers</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-a-standard-c-compiler">Using a Standard C++ Compiler</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#compiler-defines-for-hip">Compiler defines for HIP</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#identifying-compiler-target">Identifying host or device compilation pass</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-clang-implementation-notes">HIP-Clang implementation notes</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#initialization-and-termination-functions">Initialization and termination functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-launching">Kernel launching</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#compilation-options-for-hipmoduleloaddataex">Compilation options for hipModuleLoadDataEx</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#identifying-device-architecture-features">Identifying device architecture and features</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#device-code-feature-identification">Device code feature identification</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#host-code-feature-identification">Host code feature identification</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#feature-macros-and-properties">Feature macros and properties</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#warpsize">warpSize</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#lane-masks-bit-shift">Lane masks bit-shift</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#porting-from-cuda-launch-bounds">Porting from CUDA __launch_bounds__</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#maxregcount">maxregcount</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#driver-entry-point-access">Driver entry point access</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#address-retrieval">Address retrieval</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#per-thread-default-stream-version-request">Per-thread default stream version request</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#accessing-hip-features-with-a-newer-driver">Accessing HIP features with a newer driver</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-type-identification">Memory type identification</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="porting-cuda-code-to-hip">
<span id="porting-cuda-code"></span><h1>Porting CUDA code to HIP<a class="headerlink" href="#porting-cuda-code-to-hip" title="Link to this heading">#</a></h1>
<p>HIP is a C++ runtime API and kernel language for AMD GPUs. It allows developers to convert
existing NVIDIA CUDA code to run on AMD GPUs. This topic describes the available tools and
provides practical suggestions for porting your CUDA code and working through common issues.</p>
<p>CUDA provides separate driver and runtime APIs, while HIP mostly uses a single API.
The two CUDA APIs generally provide similar functionality and are mostly interchangeable.
However, the CUDA driver API provides fine-grained control over kernel-level
initialization, contexts, and module management, while the runtime API automatically
manages contexts and modules. The driver API is suitable for applications that require
tight integration with other systems or advanced control over GPU resources.</p>
<ul class="simple">
<li><p>Driver API calls begin with the prefix <code class="docutils literal notranslate"><span class="pre">cu</span></code>, while runtime API calls begin
with the prefix <code class="docutils literal notranslate"><span class="pre">cuda</span></code>. For example, the driver API contains
<code class="docutils literal notranslate"><span class="pre">cuEventCreate</span></code>, while the runtime API contains <code class="docutils literal notranslate"><span class="pre">cudaEventCreate</span></code>, which
has similar functionality.</p></li>
<li><p>The driver API offers two additional low-level functionalities not exposed by
the runtime API: module management <code class="docutils literal notranslate"><span class="pre">cuModule*</span></code> and context management
<code class="docutils literal notranslate"><span class="pre">cuCtx*</span></code> APIs.</p></li>
</ul>
<p>The HIP runtime API includes corresponding functions for both the CUDA driver and
the CUDA runtime API. The module and context functionality are available with the
<code class="docutils literal notranslate"><span class="pre">hipModule</span></code> and <code class="docutils literal notranslate"><span class="pre">hipCtx</span></code> prefixes, and driver API functions are usually
prefixed with <code class="docutils literal notranslate"><span class="pre">hipDrv</span></code>.</p>
<section id="porting-a-cuda-project">
<h2>Porting a CUDA project<a class="headerlink" href="#porting-a-cuda-project" title="Link to this heading">#</a></h2>
<p>HIP provides a runtime API for AMD GPUs that closely mirrors CUDA, making it
straightforward to port existing CUDA applications. To compile HIP code for AMD platforms,
you can use <code class="docutils literal notranslate"><span class="pre">amdclang++</span></code>, also called HIP-Clang, or you can use <code class="docutils literal notranslate"><span class="pre">hipcc</span></code> which offers
a higher-level compiler interface.</p>
<section id="general-tips">
<h3>General tips<a class="headerlink" href="#general-tips" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p>Use the <a class="reference external" href="https://github.com/ROCm/HIPIFY">HIPIFY</a> tools to automatically
convert CUDA code to HIP, as described in the following section.</p></li>
<li><p>Start with a working CUDA codebase before beginning the porting process.</p></li>
<li><p>Port the application incrementally and test each section as you convert it.</p></li>
<li><p>HIP code runs on AMD GPUs and takes advantage of the ROCm software stack for both
performance and tooling support.</p></li>
</ul>
</section>
</section>
<section id="using-hipify">
<h2>Using HIPIFY<a class="headerlink" href="#using-hipify" title="Link to this heading">#</a></h2>
<p><a class="reference external" href="https://rocm.docs.amd.com/projects/HIPIFY/en/latest/index.html" title="(in HIPIFY Documentation)"><span class="xref std std-doc">HIPIFY</span></a> is a collection of tools that automatically
translate CUDA code to HIP code. For example, <code class="docutils literal notranslate"><span class="pre">cuEventCreate</span></code> is translated to
<a class="reference internal" href="../reference/hip_runtime_api/modules/event_management.html#_CPPv414hipEventCreateP10hipEvent_t" title="hipEventCreate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipEventCreate()</span></code></a>. HIPIFY tools also convert error codes from the
driver namespace and coding conventions to the equivalent HIP error code.
HIP unifies the APIs for these common functions.</p>
<p>There are two types of HIPIFY available:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://rocm.docs.amd.com/projects/HIPIFY/en/latest/how-to/hipify-clang.html" title="(in HIPIFY Documentation)"><span class="xref std std-doc">hipify-clang</span></a> is a Clang-based tool that parses code,
translates it into an Abstract Syntax Tree, and generates the HIP source. For this,
<code class="docutils literal notranslate"><span class="pre">hipify-clang</span></code> needs to be able to actually compile the code, so the CUDA code needs
to be correct, and a CUDA install with all necessary headers must be provided.</p></li>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/projects/HIPIFY/en/latest/how-to/hipify-perl.html" title="(in HIPIFY Documentation)"><span class="xref std std-doc">hipify-perl</span></a> uses pattern matching, to translate the
CUDA code to HIP. It does not require a working CUDA installation, and can also
convert CUDA code, that is not syntactically correct. It is therefore easier to
set up and use, but is not as powerful as <code class="docutils literal notranslate"><span class="pre">hipify-clang</span></code>.</p></li>
</ul>
<section id="memory-copy-functions">
<h3>Memory copy functions<a class="headerlink" href="#memory-copy-functions" title="Link to this heading">#</a></h3>
<p>When copying memory, the CUDA driver includes the memory direction in the name of
the API (<code class="docutils literal notranslate"><span class="pre">cuMemcpyHtoD</span></code>), while the CUDA runtime API provides a single memory
copy API with a parameter that specifies the direction. It also supports a
default direction where the runtime determines the direction automatically.</p>
<p>HIP provides both versions, for example, <a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html#_CPPv413hipMemcpyHtoD14hipDeviceptr_tPKv6size_t" title="hipMemcpyHtoD"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpyHtoD()</span></code></a> as well as
<a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind" title="hipMemcpy"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpy()</span></code></a>. The first version might be faster in some cases because
it avoids any host overhead to detect the direction of the memory copy.</p>
</section>
<section id="address-spaces">
<h3>Address spaces<a class="headerlink" href="#address-spaces" title="Link to this heading">#</a></h3>
<p>HIP-Clang defines a process-wide address space where
the CPU and all devices allocate addresses from a single unified pool.
This means addresses can be shared between contexts. A new context
does not create a new address space for the device.</p>
</section>
<section id="context-stack-behavior-differences">
<h3>Context stack behavior differences<a class="headerlink" href="#context-stack-behavior-differences" title="Link to this heading">#</a></h3>
<p>HIP-Clang creates a primary context when the HIP API is first invoked. It then
pushes this primary context onto the context stack if the stack is empty.
This behavior differs from the CUDA driver API, where contexts often need to
be managed explicitly.</p>
</section>
<section id="scanning-cuda-source-to-scope-the-translation">
<h3>Scanning CUDA source to scope the translation<a class="headerlink" href="#scanning-cuda-source-to-scope-the-translation" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">--examine</span></code> option, tells the hipify tools to do a test-run without changing
the source files, but instead scanning the files to determine which files contain CUDA code and
how much of that code can automatically be hipified.</p>
<p>There also are <code class="docutils literal notranslate"><span class="pre">hipexamine-perl.sh</span></code> or <code class="docutils literal notranslate"><span class="pre">hipexamine.sh</span></code> (for
<code class="docutils literal notranslate"><span class="pre">hipify-clang</span></code>) scripts to automatically scan directories.</p>
<p>For example, the following is a scan of one of the <code class="docutils literal notranslate"><span class="pre">convolutionSeparable</span></code> sample
from <a class="reference external" href="https://github.com/NVIDIA/cuda-samples">cuda-samples</a>:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>&gt;<span class="w"> </span><span class="nb">cd</span><span class="w"> </span>Samples/2_Concepts_and_Techniques/convolutionSeparable/
&gt;<span class="w"> </span>hipexamine-perl.sh
<span class="o">[</span>HIPIFY<span class="o">]</span><span class="w"> </span>info:<span class="w"> </span>file<span class="w"> </span><span class="s1">&#39;./convolutionSeparable.cu&#39;</span><span class="w"> </span>statistics:
<span class="w">  </span>CONVERTED<span class="w"> </span>refs<span class="w"> </span>count:<span class="w"> </span><span class="m">2</span>
<span class="w">  </span>TOTAL<span class="w"> </span>lines<span class="w"> </span>of<span class="w"> </span>code:<span class="w"> </span><span class="m">214</span>
<span class="w">  </span>WARNINGS:<span class="w"> </span><span class="m">0</span>
<span class="o">[</span>HIPIFY<span class="o">]</span><span class="w"> </span>info:<span class="w"> </span>CONVERTED<span class="w"> </span>refs<span class="w"> </span>by<span class="w"> </span>names:
<span class="w">  </span>cooperative_groups.h<span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hip/hip_cooperative_groups.h:<span class="w"> </span><span class="m">1</span>
<span class="w">  </span><span class="nv">cudaMemcpyToSymbol</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipMemcpyToSymbol:<span class="w"> </span><span class="m">1</span>

<span class="o">[</span>HIPIFY<span class="o">]</span><span class="w"> </span>info:<span class="w"> </span>file<span class="w"> </span><span class="s1">&#39;./main.cpp&#39;</span><span class="w"> </span>statistics:
<span class="w">  </span>CONVERTED<span class="w"> </span>refs<span class="w"> </span>count:<span class="w"> </span><span class="m">13</span>
<span class="w">  </span>TOTAL<span class="w"> </span>lines<span class="w"> </span>of<span class="w"> </span>code:<span class="w"> </span><span class="m">174</span>
<span class="w">  </span>WARNINGS:<span class="w"> </span><span class="m">0</span>
<span class="o">[</span>HIPIFY<span class="o">]</span><span class="w"> </span>info:<span class="w"> </span>CONVERTED<span class="w"> </span>refs<span class="w"> </span>by<span class="w"> </span>names:
<span class="w">  </span><span class="nv">cudaDeviceSynchronize</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipDeviceSynchronize:<span class="w"> </span><span class="m">2</span>
<span class="w">  </span><span class="nv">cudaFree</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipFree:<span class="w"> </span><span class="m">3</span>
<span class="w">  </span><span class="nv">cudaMalloc</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipMalloc:<span class="w"> </span><span class="m">3</span>
<span class="w">  </span><span class="nv">cudaMemcpy</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipMemcpy:<span class="w"> </span><span class="m">2</span>
<span class="w">  </span><span class="nv">cudaMemcpyDeviceToHost</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipMemcpyDeviceToHost:<span class="w"> </span><span class="m">1</span>
<span class="w">  </span><span class="nv">cudaMemcpyHostToDevice</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipMemcpyHostToDevice:<span class="w"> </span><span class="m">1</span>
<span class="w">  </span>cuda_runtime.h<span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hip/hip_runtime.h:<span class="w"> </span><span class="m">1</span>

<span class="o">[</span>HIPIFY<span class="o">]</span><span class="w"> </span>info:<span class="w"> </span>file<span class="w"> </span><span class="s1">&#39;GLOBAL&#39;</span><span class="w"> </span>statistics:
<span class="w">  </span>CONVERTED<span class="w"> </span>refs<span class="w"> </span>count:<span class="w"> </span><span class="m">15</span>
<span class="w">  </span>TOTAL<span class="w"> </span>lines<span class="w"> </span>of<span class="w"> </span>code:<span class="w"> </span><span class="m">512</span>
<span class="w">  </span>WARNINGS:<span class="w"> </span><span class="m">0</span>
<span class="o">[</span>HIPIFY<span class="o">]</span><span class="w"> </span>info:<span class="w"> </span>CONVERTED<span class="w"> </span>refs<span class="w"> </span>by<span class="w"> </span>names:
<span class="w">  </span>cooperative_groups.h<span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hip/hip_cooperative_groups.h:<span class="w"> </span><span class="m">1</span>
<span class="w">  </span><span class="nv">cudaDeviceSynchronize</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipDeviceSynchronize:<span class="w"> </span><span class="m">2</span>
<span class="w">  </span><span class="nv">cudaFree</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipFree:<span class="w"> </span><span class="m">3</span>
<span class="w">  </span><span class="nv">cudaMalloc</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipMalloc:<span class="w"> </span><span class="m">3</span>
<span class="w">  </span><span class="nv">cudaMemcpy</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipMemcpy:<span class="w"> </span><span class="m">2</span>
<span class="w">  </span><span class="nv">cudaMemcpyDeviceToHost</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipMemcpyDeviceToHost:<span class="w"> </span><span class="m">1</span>
<span class="w">  </span><span class="nv">cudaMemcpyHostToDevice</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipMemcpyHostToDevice:<span class="w"> </span><span class="m">1</span>
<span class="w">  </span><span class="nv">cudaMemcpyToSymbol</span><span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hipMemcpyToSymbol:<span class="w"> </span><span class="m">1</span>
<span class="w">  </span>cuda_runtime.h<span class="w"> </span><span class="o">=</span>&gt;<span class="w"> </span>hip/hip_runtime.h:<span class="w"> </span><span class="m">1</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">hipexamine-perl.sh</span></code> reports how many CUDA calls are going to be converted to
HIP (e.g. <code class="docutils literal notranslate"><span class="pre">CONVERTED</span> <span class="pre">refs</span> <span class="pre">count:</span> <span class="pre">2</span></code>), and lists them by name together with
their corresponding HIP-version (see the lines following <code class="docutils literal notranslate"><span class="pre">[HIPIFY]</span> <span class="pre">info:</span>
<span class="pre">CONVERTED</span> <span class="pre">refs</span> <span class="pre">by</span> <span class="pre">names:</span></code>). It also lists the total lines of code for the file
and potential warnings. In the end it prints a summary for all files.</p>
</section>
<section id="automatically-converting-a-cuda-project">
<h3>Automatically converting a CUDA project<a class="headerlink" href="#automatically-converting-a-cuda-project" title="Link to this heading">#</a></h3>
<p>To directly replace the files, the <code class="docutils literal notranslate"><span class="pre">--inplace</span></code> option of <code class="docutils literal notranslate"><span class="pre">hipify-perl</span></code> or
<code class="docutils literal notranslate"><span class="pre">hipify-clang</span></code> can be used. This creates a backup of the original files in a
<code class="docutils literal notranslate"><span class="pre">&lt;filename&gt;.prehip</span></code> file and overwrites the existing files, keeping their file
endings. If the <code class="docutils literal notranslate"><span class="pre">--inplace</span></code> option is not given, the scripts print the
hipified code to <code class="docutils literal notranslate"><span class="pre">stdout</span></code>.</p>
<p><code class="docutils literal notranslate"><span class="pre">hipconvertinplace.sh</span></code> or <code class="docutils literal notranslate"><span class="pre">hipconvertinplace-perl.sh</span></code> operate on whole
directories.</p>
</section>
</section>
<section id="library-and-driver-equivalents">
<h2>Library and driver equivalents<a class="headerlink" href="#library-and-driver-equivalents" title="Link to this heading">#</a></h2>
<p>ROCm provides libraries to ease porting of code relying on CUDA libraries or the CUDA driver API.
Most CUDA libraries have a corresponding HIP library. For more information,
see either <a class="reference external" href="https://rocm.docs.amd.com/en/latest/reference/api-libraries.html" title="(in ROCm Documentation v7.2.2)"><span class="xref std std-doc">ROCm libraries</span></a> or <a class="reference external" href="https://rocm.docs.amd.com/projects/HIPIFY/en/latest/reference/supported_apis.html" title="(in HIPIFY Documentation)"><span class="xref std std-doc">HIPIFY CUDA compatible libraries</span></a>.</p>
<p>ROCm provides two categories of libraries: those prefixed with <code class="docutils literal notranslate"><span class="pre">hip</span></code> and those prefixed
with <code class="docutils literal notranslate"><span class="pre">roc</span></code>. While both are implemented using HIP, the <code class="docutils literal notranslate"><span class="pre">roc</span></code> libraries are optimized
specifically for AMD GPUs and may use AMD-specific features to deliver the best performance.</p>
<p>In the case where a library provides both <code class="docutils literal notranslate"><span class="pre">roc</span></code> and <code class="docutils literal notranslate"><span class="pre">hip</span></code> versions, such as
<code class="docutils literal notranslate"><span class="pre">hipSparse</span></code> and <code class="docutils literal notranslate"><span class="pre">rocSparse</span></code>, it is recommended to use the <code class="docutils literal notranslate"><span class="pre">roc</span></code> version
for applications running on AMD GPUs, as they are optimized for AMD architectures.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>For applications running on AMD GPUs, it is recommended to use
the <code class="docutils literal notranslate"><span class="pre">roc</span></code>-libraries. In hipify tools, this can be accomplished using the <code class="docutils literal notranslate"><span class="pre">--roc</span></code> option.</p>
</div>
<section id="cumodule-and-hipmodule">
<h3>cuModule and hipModule<a class="headerlink" href="#cumodule-and-hipmodule" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">cuModule</span></code> feature of the driver API provides additional control over how and
when accelerator code objects are loaded. For example, the driver API enables
code objects to be loaded from files or memory pointers. Symbols for kernels or
global data are extracted from the loaded code objects. In contrast, the runtime
API loads automatically and, if necessary, compiles all the kernels from an
executable binary when it runs.</p>
<p>The Module features are useful in an environment that generates the code objects
directly, such as a new accelerator language front end. Other environments have
many kernels and don’t want all of them to be loaded automatically. The Module
functions load the generated code objects and launch kernels.</p>
<p>Like the <code class="docutils literal notranslate"><span class="pre">cuModule</span></code> API, the <code class="docutils literal notranslate"><span class="pre">hipModule</span></code> API provides additional control
over code object management, including options to load code from files or from
in-memory pointers.</p>
<p>HIP-Clang uses the <code class="docutils literal notranslate"><span class="pre">hsaco</span></code> format for code objects. The following table
summarizes the formats used:</p>
<div class="pst-scrollable-table-container"><table class="table" id="id1">
<caption><span class="caption-text">Module formats</span><a class="headerlink" href="#id1" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Format</p></th>
<th class="head"><p>APIs</p></th>
<th class="head"><p>HIP-CLANG</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Code object</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hipModuleLoad</span></code>, <code class="docutils literal notranslate"><span class="pre">hipModuleLoadData</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">.hsaco</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>Fat binary</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hipModuleLoadFatBin</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">.hip_fatbin</span></code></p></td>
</tr>
</tbody>
</table>
</div>
<p><code class="docutils literal notranslate"><span class="pre">hipcc</span></code> uses HIP-Clang to compile host code. The compiler can
embed code objects into the final executable. These code objects are automatically
loaded when the application starts. The <code class="docutils literal notranslate"><span class="pre">hipModule</span></code> API can be used to load
additional code objects. When used this way, it extends the capability of the
automatically loaded code objects. HIP-Clang enables both of these capabilities to
be used together. Of course, it is possible to create a program with no kernels and
no automatic loading.</p>
<p>For <code class="docutils literal notranslate"><span class="pre">hipModule</span></code> API reference content, see <a class="reference internal" href="../reference/hip_runtime_api/modules/module_management.html#module-management-reference"><span class="std std-ref">Module management</span></a>.</p>
<section id="using-hipmodulelaunchkernel">
<h4>Using hipModuleLaunchKernel<a class="headerlink" href="#using-hipmodulelaunchkernel" title="Link to this heading">#</a></h4>
<p>Both CUDA driver and runtime APIs define a function for launching kernels,
called <code class="docutils literal notranslate"><span class="pre">cuLaunchKernel</span></code> or <code class="docutils literal notranslate"><span class="pre">cudaLaunchKernel</span></code>. The equivalent API in HIP is
<a class="reference internal" href="../reference/hip_runtime_api/modules/execution_control.html#_CPPv421hipModuleLaunchKernel13hipFunction_tjjjjjjj11hipStream_tPPvPPv" title="hipModuleLaunchKernel"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipModuleLaunchKernel()</span></code></a>. The kernel arguments and the execution
configuration (grid dimensions, group dimensions, dynamic shared memory, and
stream) are passed as arguments to the launch function.</p>
<p>The HIP runtime API additionally supports the triple chevron (<code class="docutils literal notranslate"><span class="pre">&lt;&lt;&lt;</span> <span class="pre">&gt;&gt;&gt;</span></code>) syntax for launching
kernels, which resembles a special function call and is easier to use than the
explicit launch API, especially when handling kernel arguments.</p>
</section>
</section>
<section id="cuctx-and-hipctx">
<span id="context-driver-api"></span><h3>cuCtx and hipCtx<a class="headerlink" href="#cuctx-and-hipctx" title="Link to this heading">#</a></h3>
<p>The CUDA driver API defines “Context” and “Devices” as separate entities.
Contexts contain a single device, and a device can theoretically have multiple contexts.
Each context contains a set of streams and events specific to the context.
The <code class="docutils literal notranslate"><span class="pre">cuCtx</span></code> API also provide a mechanism to switch between devices, which enables a
single CPU thread to send commands to different GPUs. HIP and recent versions of the
CUDA Runtime provide other mechanisms to accomplish this, such as using streams or <code class="docutils literal notranslate"><span class="pre">cudaSetDevice</span></code>.</p>
<p>On the other hand, the CUDA runtime API unifies the Context API with the Device API. This simplifies the
APIs and has little loss of functionality because each context can contain a
single device, and the benefits of multiple contexts have been replaced with other interfaces.</p>
<p>HIP provides a Context API as a thin layer over the existing device functions to facilitate
easy porting from existing driver API code. The <code class="docutils literal notranslate"><span class="pre">hipCtx</span></code> functions largely provide an
alternate syntax for changing the active device. The <code class="docutils literal notranslate"><span class="pre">hipCtx</span></code> API can be used to set the
current context or to query properties of the device associated with the context. The current
context is implicitly used by other APIs, such as <code class="docutils literal notranslate"><span class="pre">hipStreamCreate</span></code>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The <code class="docutils literal notranslate"><span class="pre">hipCtx</span></code> API is <strong>deprecated</strong> and its use is discouraged. Most new applications use
<code class="docutils literal notranslate"><span class="pre">hipSetDevice</span></code> or the <code class="docutils literal notranslate"><span class="pre">hipStream</span></code> APIs. For more details on deprecated APIs, see <a class="reference internal" href="../reference/deprecated_api_list.html"><span class="doc">HIP deprecated runtime API functions</span></a>.</p>
</div>
</section>
</section>
<section id="compilation">
<span id="compilation-platform"></span><h2>Compilation<a class="headerlink" href="#compilation" title="Link to this heading">#</a></h2>
<p>HIP code must be compiled for a specific AMD GPU architecture, and the resulting binaries
contain code tailored to that target architecture.</p>
<p><code class="docutils literal notranslate"><span class="pre">hipcc</span></code> is a compiler driver that invokes <code class="docutils literal notranslate"><span class="pre">amdclang++</span></code> (HIP-Clang) and passes the
required options to it. Tools that rely on <code class="docutils literal notranslate"><span class="pre">hipcc</span></code> must ensure that the compiler flags
they provide are appropriate for the underlying compiler.</p>
<p><code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> is a helpful tool for identifying the current system’s platform,
compiler and runtime. It can also help set options appropriately. As an example,
<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> can provide a path to HIP, in Makefiles:</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>HIP_PATH<span class="w"> </span>?<span class="o">=</span><span class="w"> </span><span class="k">$(</span>shell<span class="w"> </span>hipconfig<span class="w"> </span>--path<span class="k">)</span>
</pre></div>
</div>
<section id="hip-headers">
<h3>HIP Headers<a class="headerlink" href="#hip-headers" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">hip_runtime.h</span></code> headers define all the necessary types, functions, macros,
etc., needed to compile a HIP program, this includes host as well as device
code. <code class="docutils literal notranslate"><span class="pre">hip_runtime_api.h</span></code> is a subset of <code class="docutils literal notranslate"><span class="pre">hip_runtime.h</span></code>.</p>
<p>CUDA has slightly different contents for these two files. In some cases you might
need to convert hipified code to include the richer <code class="docutils literal notranslate"><span class="pre">hip_runtime.h</span></code> instead of
<code class="docutils literal notranslate"><span class="pre">hip_runtime_api.h</span></code>.</p>
</section>
<section id="using-a-standard-c-compiler">
<h3>Using a Standard C++ Compiler<a class="headerlink" href="#using-a-standard-c-compiler" title="Link to this heading">#</a></h3>
<p>A source file that is only calling HIP APIs but neither defines nor launches
any kernels can be compiled with a standard C or C++ compiler (GCC or MSVC for example)
even when <code class="docutils literal notranslate"><span class="pre">hip_runtime_api.h</span></code> or <code class="docutils literal notranslate"><span class="pre">hip_runtime.h</span></code> are included. The HIP include
paths and platform macros (<code class="docutils literal notranslate"><span class="pre">__HIP_PLATFORM_AMD__</span></code>) must be passed to the compiler.</p>
<p><code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> can help define the necessary options, for example on an AMD
platform:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>hipconfig<span class="w"> </span>--cpp_config
<span class="w"> </span>-D__HIP_PLATFORM_AMD__<span class="o">=</span><span class="w"> </span>-I/opt/rocm/include
</pre></div>
</div>
<p>HIP-Clang does not include default headers, and instead you must explicitly
include all required files.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The <code class="docutils literal notranslate"><span class="pre">hipify</span></code> tool automatically converts <code class="docutils literal notranslate"><span class="pre">cuda_runtime.h</span></code> to <code class="docutils literal notranslate"><span class="pre">hip_runtime.h</span></code>,
and it converts <code class="docutils literal notranslate"><span class="pre">cuda_runtime_api.h</span></code> to <code class="docutils literal notranslate"><span class="pre">hip_runtime_api.h</span></code>, but it may
miss nested headers or macros.</p>
</div>
</section>
<section id="compiler-defines-for-hip">
<h3>Compiler defines for HIP<a class="headerlink" href="#compiler-defines-for-hip" title="Link to this heading">#</a></h3>
<p>C++ macros are defined by the HIP compilers and APIs. This section lists macros
that are available when compiling HIP code and the compiler combinations that
define them.</p>
<p>The following table lists the macros that can be used when compiling HIP. Most
of these macros are not directly defined by the compilers, but in
<code class="docutils literal notranslate"><span class="pre">hip_common.h</span></code>, which is included by <code class="docutils literal notranslate"><span class="pre">hip_runtime.h</span></code>.</p>
<div class="pst-scrollable-table-container"><table class="table" id="id2">
<caption><span class="caption-text">HIP-related defines</span><a class="headerlink" href="#id2" title="Link to this table">#</a></caption>
<thead>
<tr class="row-odd"><th class="head"><p>Macro</p></th>
<th class="head"><p><code class="docutils literal notranslate"><span class="pre">amdclang++</span></code></p></th>
<th class="head"><p>Other (GCC, MSVC, Clang, etc.)</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_PLATFORM_AMD__</span></code></p></td>
<td><p>Defined</p></td>
<td><p>Undefined, needs to be set explicitly</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__HIPCC__</span></code></p></td>
<td><p>Defined when compiling <code class="docutils literal notranslate"><span class="pre">.hip</span></code> files or specifying <code class="docutils literal notranslate"><span class="pre">-x</span> <span class="pre">hip</span></code></p></td>
<td><p>Undefined</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_DEVICE_COMPILE__</span></code></p></td>
<td><p>1 if compiling for device, undefined if compiling for host</p></td>
<td><p>Undefined</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_&lt;FEATURE&gt;__</span></code></p></td>
<td><p>0 or 1 depending on feature support of targeted hardware (see <a class="reference internal" href="#identifying-device-architecture-features"><span class="std std-ref">Identifying device architecture and features</span></a>)</p></td>
<td><p>0</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP__</span></code></p></td>
<td><p>Defined when compiling <code class="docutils literal notranslate"><span class="pre">.hip</span></code> files or specifying <code class="docutils literal notranslate"><span class="pre">-x</span> <span class="pre">hip</span></code></p></td>
<td><p>Undefined</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="identifying-compiler-target">
<span id="identifying-host-or-device-compilation-pass"></span><h3>Identifying host or device compilation pass<a class="headerlink" href="#identifying-compiler-target" title="Link to this heading">#</a></h3>
<p><code class="docutils literal notranslate"><span class="pre">amdclang++</span></code> makes multiple passes over the code: one pass for the host code, and
for the device code one pass for each GPU architecture to be compiled for.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">__HIP_DEVICE_COMPILE__</span></code> macro is defined when the compiler is compiling
for the device. This macro can be used to replace the <code class="docutils literal notranslate"><span class="pre">__CUDA_ARCH__</span></code> macro
when porting from CUDA.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&quot;hip/hip_runtime.h&quot;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="n">__host__</span><span class="w"> </span><span class="n">__device__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">call_func</span><span class="p">(){</span>
<span class="w">  </span><span class="cp">#ifdef __HIP_DEVICE_COMPILE__</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">&quot;device</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">);</span>
<span class="w">  </span><span class="cp">#else</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;host&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">  </span><span class="cp">#endif</span>
<span class="p">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">test_kernel</span><span class="p">(){</span>
<span class="w">  </span><span class="n">call_func</span><span class="p">();</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">argc</span><span class="p">,</span><span class="w"> </span><span class="kt">char</span><span class="o">**</span><span class="w"> </span><span class="n">argv</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">test_kernel</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="o">&gt;&gt;&gt;</span><span class="p">();</span>

<span class="w">  </span><span class="n">call_func</span><span class="p">();</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
</section>
<section id="hip-clang-implementation-notes">
<h2>HIP-Clang implementation notes<a class="headerlink" href="#hip-clang-implementation-notes" title="Link to this heading">#</a></h2>
<p>HIP-Clang links device code from different translation units together. For each
device target, it generates a code object. <code class="docutils literal notranslate"><span class="pre">clang-offload-bundler</span></code> bundles
code objects for different device targets into one fat binary, which is embedded
as the global symbol <code class="docutils literal notranslate"><span class="pre">__hip_fatbin</span></code> in the <code class="docutils literal notranslate"><span class="pre">.hip_fatbin</span></code> section of the ELF
file of the executable or shared object.</p>
<section id="initialization-and-termination-functions">
<h3>Initialization and termination functions<a class="headerlink" href="#initialization-and-termination-functions" title="Link to this heading">#</a></h3>
<p>HIP-Clang generates initialization and termination functions for each
translation unit for host code compilation. The initialization functions call
<code class="docutils literal notranslate"><span class="pre">__hipRegisterFatBinary</span></code> to register the fat binary embedded in the ELF file.
They also call <code class="docutils literal notranslate"><span class="pre">__hipRegisterFunction</span></code> and <code class="docutils literal notranslate"><span class="pre">__hipRegisterVar</span></code> to register
kernel functions and device-side global variables. The termination functions
call <code class="docutils literal notranslate"><span class="pre">__hipUnregisterFatBinary</span></code>.</p>
<p>HIP-Clang emits a global variable <code class="docutils literal notranslate"><span class="pre">__hip_gpubin_handle</span></code> of type <code class="docutils literal notranslate"><span class="pre">void**</span></code>
with <code class="docutils literal notranslate"><span class="pre">linkonce</span></code> linkage and an initial value of 0 for each host translation
unit. Each initialization function checks <code class="docutils literal notranslate"><span class="pre">__hip_gpubin_handle</span></code> and registers
the fat binary only if <code class="docutils literal notranslate"><span class="pre">__hip_gpubin_handle</span></code> is 0. It saves the return value
of <code class="docutils literal notranslate"><span class="pre">__hip_gpubin_handle</span></code> to <code class="docutils literal notranslate"><span class="pre">__hip_gpubin_handle</span></code>. This ensures that the fat
binary is registered once. A similar check is performed in the termination
functions.</p>
</section>
<section id="kernel-launching">
<h3>Kernel launching<a class="headerlink" href="#kernel-launching" title="Link to this heading">#</a></h3>
<p>HIP-Clang supports kernel launching using either the triple chevron (<code class="docutils literal notranslate"><span class="pre">&lt;&lt;&lt;&gt;&gt;&gt;</span></code>) syntax,
<a class="reference internal" href="../reference/hip_runtime_api/modules/launch_api.html#_CPPv415hipLaunchKernelPKv4dim34dim3PPv6size_t11hipStream_t" title="hipLaunchKernel"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipLaunchKernel()</span></code></a>, or <code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipLaunchKernelGGL()</span></code>. The last option is a macro that
expands to the <code class="docutils literal notranslate"><span class="pre">&lt;&lt;&lt;&gt;&gt;&gt;</span></code> syntax by default. It can also be turned into a template by
defining <code class="docutils literal notranslate"><span class="pre">HIP_TEMPLATE_KERNEL_LAUNCH</span></code>.</p>
<p>When the executable or shared library is loaded by the dynamic linker, the
initialization functions are called. In the initialization functions, the code
objects containing all kernels are loaded when <code class="docutils literal notranslate"><span class="pre">__hipRegisterFatBinary</span></code> is
called. When <code class="docutils literal notranslate"><span class="pre">__hipRegisterFunction</span></code> is called, the stub functions are
associated with the corresponding kernels in the code objects.</p>
<p>HIP-Clang implements two sets of APIs for launching kernels.
By default, when HIP-Clang encounters the <code class="docutils literal notranslate"><span class="pre">&lt;&lt;&lt;&gt;&gt;&gt;</span></code> statement in the host code,
it first calls <a class="reference internal" href="../reference/hip_runtime_api/modules/launch_api.html#_CPPv416hipConfigureCall4dim34dim36size_t11hipStream_t" title="hipConfigureCall"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipConfigureCall()</span></code></a> to set up the threads and grids. It then
calls the stub function with the given arguments. The stub function calls
<a class="reference internal" href="../reference/hip_runtime_api/modules/launch_api.html#_CPPv416hipSetupArgumentPKv6size_t6size_t" title="hipSetupArgument"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipSetupArgument()</span></code></a> for each kernel argument, then calls <a class="reference internal" href="../reference/hip_runtime_api/modules/launch_api.html#_CPPv414hipLaunchByPtrPKv" title="hipLaunchByPtr"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipLaunchByPtr()</span></code></a>
with a function pointer to the stub function. In <code class="docutils literal notranslate"><span class="pre">hipLaunchByPtr</span></code>, the actual
kernel associated with the stub function is launched.</p>
</section>
<section id="compilation-options-for-hipmoduleloaddataex">
<h3>Compilation options for hipModuleLoadDataEx<a class="headerlink" href="#compilation-options-for-hipmoduleloaddataex" title="Link to this heading">#</a></h3>
<p>The <code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipModule_t</span></code> interface provides <a class="reference internal" href="../reference/hip_runtime_api/modules/module_management.html#_CPPv419hipModuleLoadDataExP11hipModule_tPKvjP12hipJitOptionPPv" title="hipModuleLoadDataEx"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipModuleLoadDataEx()</span></code></a>
for loading code modules. HIP-Clang code objects contain fully compiled code
for a device-specific instruction set and don’t require additional compilation
as a part of the load step. Therefore, <a class="reference internal" href="../reference/hip_runtime_api/modules/module_management.html#_CPPv419hipModuleLoadDataExP11hipModule_tPKvjP12hipJitOptionPPv" title="hipModuleLoadDataEx"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipModuleLoadDataEx()</span></code></a> behaves
like <a class="reference internal" href="../reference/hip_runtime_api/modules/module_management.html#_CPPv417hipModuleLoadDataP11hipModule_tPKv" title="hipModuleLoadData"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipModuleLoadData()</span></code></a> on HIP-Clang (where compilation options are
not used).</p>
<p>For example:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipModule_t</span><span class="w"> </span><span class="k">module</span><span class="p">;</span>
<span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">imagePtr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">...;</span><span class="w"> </span><span class="c1">// Somehow populate data pointer with code object</span>

<span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">numOptions</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">hipJitOption</span><span class="w"> </span><span class="n">options</span><span class="p">[</span><span class="n">numOptions</span><span class="p">];</span>
<span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">optionValues</span><span class="p">[</span><span class="n">numOptions</span><span class="p">];</span>

<span class="n">options</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipJitOptionMaxRegisters</span><span class="p">;</span>
<span class="kt">unsigned</span><span class="w"> </span><span class="n">maxRegs</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">15</span><span class="p">;</span>
<span class="n">optionValues</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="p">)(</span><span class="o">&amp;</span><span class="n">maxRegs</span><span class="p">);</span>

<span class="c1">// hipModuleLoadData(module, imagePtr) will be called, JIT options will not be used</span>
<span class="n">hipModuleLoadDataEx</span><span class="p">(</span><span class="k">module</span><span class="p">,</span><span class="w"> </span><span class="n">imagePtr</span><span class="p">,</span><span class="w"> </span><span class="n">numOptions</span><span class="p">,</span><span class="w"> </span><span class="n">options</span><span class="p">,</span><span class="w"> </span><span class="n">optionValues</span><span class="p">);</span>

<span class="n">hipFunction_t</span><span class="w"> </span><span class="n">k</span><span class="p">;</span>
<span class="n">hipModuleGetFunction</span><span class="p">(</span><span class="o">&amp;</span><span class="n">k</span><span class="p">,</span><span class="w"> </span><span class="k">module</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;myKernel&quot;</span><span class="p">);</span>
</pre></div>
</div>
<p>The sample below shows how to use :cpp:func:<code class="docutils literal notranslate"><span class="pre">hipModuleGetFunction</span></code>.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime_api.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>

<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">elements</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">64</span><span class="o">*</span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size_bytes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">elements</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">);</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">A</span><span class="p">(</span><span class="n">elements</span><span class="p">),</span><span class="w"> </span><span class="n">B</span><span class="p">(</span><span class="n">elements</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Allocate device memory</span>
<span class="w">    </span><span class="n">hipDeviceptr_t</span><span class="w"> </span><span class="n">d_A</span><span class="p">,</span><span class="w"> </span><span class="n">d_B</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_A</span><span class="p">,</span><span class="w"> </span><span class="n">size_bytes</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_B</span><span class="p">,</span><span class="w"> </span><span class="n">size_bytes</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Copy data to device</span>
<span class="w">    </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipMemcpyHtoD</span><span class="p">(</span><span class="n">d_A</span><span class="p">,</span><span class="w"> </span><span class="n">A</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">size_bytes</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipMemcpyHtoD</span><span class="p">(</span><span class="n">d_B</span><span class="p">,</span><span class="w"> </span><span class="n">B</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">size_bytes</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Load module</span>
<span class="w">    </span><span class="n">hipModule_t</span><span class="w"> </span><span class="n">Module</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// The module file must contain architecture specific object code (.hsaco)</span>
<span class="w">    </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipModuleLoad</span><span class="p">(</span><span class="o">&amp;</span><span class="n">Module</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;vcpy_isa.co&quot;</span><span class="p">));</span>
<span class="w">    </span><span class="c1">// Get kernel function from the module via its name</span>
<span class="w">    </span><span class="n">hipFunction_t</span><span class="w"> </span><span class="n">Function</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipModuleGetFunction</span><span class="p">(</span><span class="o">&amp;</span><span class="n">Function</span><span class="p">,</span><span class="w"> </span><span class="n">Module</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;hello_world&quot;</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Create buffer for kernel arguments</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="w"> </span><span class="n">argBuffer</span><span class="p">{</span><span class="o">&amp;</span><span class="n">d_A</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">d_B</span><span class="p">};</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">arg_size_bytes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">argBuffer</span><span class="p">.</span><span class="n">size</span><span class="p">()</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Create configuration passed to the kernel as arguments</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">config</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="n">HIP_LAUNCH_PARAM_BUFFER_POINTER</span><span class="p">,</span><span class="w"> </span><span class="n">argBuffer</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span>
<span class="w">                      </span><span class="n">HIP_LAUNCH_PARAM_BUFFER_SIZE</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">arg_size_bytes</span><span class="p">,</span><span class="w"> </span><span class="n">HIP_LAUNCH_PARAM_END</span><span class="p">};</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">threads_per_block</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">128</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">blocks</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="n">elements</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threads_per_block</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="mi">1</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">threads_per_block</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Actually launch kernel</span>
<span class="w">    </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipModuleLaunchKernel</span><span class="p">(</span><span class="n">Function</span><span class="p">,</span><span class="w"> </span><span class="n">blocks</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">threads_per_block</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="nb">NULL</span><span class="p">,</span><span class="w"> </span><span class="n">config</span><span class="p">));</span>

<span class="w">    </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipMemcpyDtoH</span><span class="p">(</span><span class="n">A</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_A</span><span class="p">,</span><span class="w"> </span><span class="n">elements</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipMemcpyDtoH</span><span class="p">(</span><span class="n">B</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_B</span><span class="p">,</span><span class="w"> </span><span class="n">elements</span><span class="p">));</span>

<span class="w">    </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_A</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_B</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
</section>
<section id="identifying-device-architecture-features">
<span id="identifying-device-architecture-and-features"></span><h2>Identifying device architecture and features<a class="headerlink" href="#identifying-device-architecture-features" title="Link to this heading">#</a></h2>
<p>GPUs of different generations and architectures do not provide the same
level of <a class="reference internal" href="../reference/hardware_features.html"><span class="doc">hardware feature support</span></a>. To
guard device code that uses architecture-dependent features, the
<code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_&lt;FEATURE&gt;__</span></code> C++-macros can be used, as described below.</p>
<section id="device-code-feature-identification">
<h3>Device code feature identification<a class="headerlink" href="#device-code-feature-identification" title="Link to this heading">#</a></h3>
<p>Some CUDA code tests <code class="docutils literal notranslate"><span class="pre">__CUDA_ARCH__</span></code> for a specific value to determine whether
the GPU supports a certain architectural feature, depending on its compute
capability. This requires knowledge about what <code class="docutils literal notranslate"><span class="pre">__CUDA_ARCH__</span></code> supports what
feature set.</p>
<p>HIP simplifies this, by replacing these macros with feature-specific macros, not
architecture specific.</p>
<p>For instance,</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">//#if __CUDA_ARCH__ &gt;= 130 // does not properly specify what feature is required</span>
<span class="cp">#if __HIP_ARCH_HAS_DOUBLES__ == 1 </span><span class="c1">// explicitly specifies what feature is required</span>
<span class="w">  </span><span class="c1">// device code</span>
<span class="cp">#endif</span>
</pre></div>
</div>
<p>For host code, the <code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_&lt;FEATURE&gt;__</span></code> defines are set to 0, if
<code class="docutils literal notranslate"><span class="pre">hip_runtime.h</span></code> is included, and undefined otherwise. It should not be relied
upon in host code.</p>
</section>
<section id="host-code-feature-identification">
<h3>Host code feature identification<a class="headerlink" href="#host-code-feature-identification" title="Link to this heading">#</a></h3>
<p>The host code must not rely on the <code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_&lt;FEATURE&gt;__</span></code> macros, because the
GPUs available to a system are not known during compile time, and their
architectural features differ. Alternatively, the host code can query architecture
feature flags during runtime by using <a class="reference internal" href="../reference/hip_runtime_api/modules/device_management.html#_CPPv422hipGetDevicePropertiesP15hipDeviceProp_ti" title="hipGetDeviceProperties"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGetDeviceProperties()</span></code></a>
or <a class="reference internal" href="../reference/hip_runtime_api/modules/device_management.html#_CPPv421hipDeviceGetAttributePi20hipDeviceAttribute_ti" title="hipDeviceGetAttribute"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipDeviceGetAttribute()</span></code></a>.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstdlib&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression) {                           \</span>
<span class="cp">  const hipError_t err = expression;                      \</span>
<span class="cp">  if (err != hipSuccess){                                 \</span>
<span class="cp">    std::cout &lt;&lt; &quot;HIP Error: &quot; &lt;&lt; hipGetErrorString(err)) \</span>
<span class="cp">              &lt;&lt; &quot; at line &quot; &lt;&lt; __LINE__ &lt;&lt; std::endl;    \</span>
<span class="cp">    std::exit(EXIT_FAILURE);                              \</span>
<span class="cp">  }                                                       \</span>
<span class="cp">}</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">(){</span>
<span class="w">  </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceCount</span><span class="p">;</span>
<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDeviceCount</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceCount</span><span class="p">));</span>

<span class="w">  </span><span class="kt">int</span><span class="w"> </span><span class="n">device</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="c1">// Query first available GPU. Can be replaced with any</span>
<span class="w">                  </span><span class="c1">// integer up to, not including, deviceCount</span>
<span class="w">  </span><span class="n">hipDeviceProp_t</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">;</span>
<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDeviceProperties</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceProp</span><span class="p">,</span><span class="w"> </span><span class="n">device</span><span class="p">));</span>

<span class="w">  </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;The queried device &quot;</span><span class="p">;</span>
<span class="w">  </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">deviceProp</span><span class="p">.</span><span class="n">arch</span><span class="p">.</span><span class="n">hasSharedInt32Atomics</span><span class="p">)</span><span class="w"> </span><span class="c1">// HIP feature query</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;supports&quot;</span><span class="p">;</span>
<span class="w">  </span><span class="k">else</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;does not support&quot;</span><span class="p">;</span>
<span class="w">  </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; shared int32 atomic operations&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="feature-macros-and-properties">
<h3>Feature macros and properties<a class="headerlink" href="#feature-macros-and-properties" title="Link to this heading">#</a></h3>
<p>The following table lists the feature macros that HIP supports,
alongside corresponding device properties that can be queried from the host code.</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Macro (for device code)</p></th>
<th class="head"><p>Device property (for host runtime query)</p></th>
<th class="head"><p>Comment</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_GLOBAL_INT32_ATOMICS__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasGlobalInt32Atomics</span></code></p></td>
<td><p>32-bit integer atomics for global memory</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_GLOBAL_FLOAT_ATOMIC_EXCH__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasGlobalFloatAtomicExch</span></code></p></td>
<td><p>32-bit float atomic exchange for global memory</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_SHARED_INT32_ATOMICS__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasSharedInt32Atomics</span></code></p></td>
<td><p>32-bit integer atomics for shared memory</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_SHARED_FLOAT_ATOMIC_EXCH__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasSharedFloatAtomicExch</span></code></p></td>
<td><p>32-bit float atomic exchange for shared memory</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_FLOAT_ATOMIC_ADD__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasFloatAtomicAdd</span></code></p></td>
<td><p>32-bit float atomic add in global and shared memory</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_GLOBAL_INT64_ATOMICS__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasGlobalInt64Atomics</span></code></p></td>
<td><p>64-bit integer atomics for global memory</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_SHARED_INT64_ATOMICS__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasSharedInt64Atomics</span></code></p></td>
<td><p>64-bit integer atomics for shared memory</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_DOUBLES__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasDoubles</span></code></p></td>
<td><p>Double-precision floating-point operations</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_WARP_VOTE__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasWarpVote</span></code></p></td>
<td><p>Warp vote instructions (<code class="docutils literal notranslate"><span class="pre">any</span></code>, <code class="docutils literal notranslate"><span class="pre">all</span></code>)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_WARP_BALLOT__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasWarpBallot</span></code></p></td>
<td><p>Warp ballot instructions</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_WARP_SHUFFLE__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasWarpShuffle</span></code></p></td>
<td><p>Warp shuffle operations (<code class="docutils literal notranslate"><span class="pre">shfl_*</span></code>)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_WARP_FUNNEL_SHIFT__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasFunnelShift</span></code></p></td>
<td><p>Funnel shift two input words into one</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_THREAD_FENCE_SYSTEM__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasThreadFenceSystem</span></code></p></td>
<td><p><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">threadfence_system()</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_SYNC_THREAD_EXT__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasSyncThreadsExt</span></code></p></td>
<td><p><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">syncthreads_count()</span></code>, <code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">syncthreads_and()</span></code>, <code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">syncthreads_or()</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_SURFACE_FUNCS__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasSurfaceFuncs</span></code></p></td>
<td><p>Supports <a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/surface_object.html#surface-object-reference"><span class="std std-ref">surface functions</span></a>.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_3DGRID__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">has3dGrid</span></code></p></td>
<td><p>Grids and groups are 3D</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">__HIP_ARCH_HAS_DYNAMIC_PARALLEL__</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">hasDynamicParallelism</span></code></p></td>
<td><p>Ability to launch a kernel from within a kernel</p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<section id="warpsize">
<h2>warpSize<a class="headerlink" href="#warpsize" title="Link to this heading">#</a></h2>
<p>Code should not assume a warp size of 32 or 64, as AMD GPU architectures have different
warp sizes. The <code class="docutils literal notranslate"><span class="pre">warpSize</span></code> built-in should be used in device code, while the host can
query it during runtime via the device properties. See the <a class="reference internal" href="hip_cpp_language_extensions.html#warp-size"><span class="std std-ref">HIP language extension for warpSize</span></a>
for information on how to write warpSize-aware code.</p>
</section>
<section id="lane-masks-bit-shift">
<h2>Lane masks bit-shift<a class="headerlink" href="#lane-masks-bit-shift" title="Link to this heading">#</a></h2>
<p>A thread in a warp is also called a lane, and a lane mask is a bitmask where
each bit corresponds to a thread in a warp. A bit is 1 if the thread is active,
0 if it’s inactive. Bit-shift operations are typically used to create lane masks
and on AMD GPUs the <code class="docutils literal notranslate"><span class="pre">warpSize</span></code> can differ between different architectures,
that’s why it’s essential to use correct bitmask type, when porting code.</p>
<p>Example:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Get the thread&#39;s position in the warp</span>
<span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">laneId</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="n">warpSize</span><span class="p">;</span>

<span class="c1">// Use lane ID for bit-shift</span>
<span class="n">val</span><span class="w"> </span><span class="o">&amp;</span><span class="w"> </span><span class="p">((</span><span class="mi">1</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="p">(</span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="n">warpSize</span><span class="p">)</span><span class="w"> </span><span class="p">)</span><span class="mi">-1</span><span class="w"> </span><span class="p">);</span>

<span class="c1">// Shift 32 bit integer with val variable</span>
<span class="n">WarpReduce</span><span class="o">::</span><span class="n">sum</span><span class="p">(</span><span class="w"> </span><span class="p">(</span><span class="n">val</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">warpSize</span><span class="p">)</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="p">(</span><span class="mi">1</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">val</span><span class="p">)</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
</pre></div>
</div>
<p>Lane masks are 32-bit integer types as this is the integer precision that C
assigns to such constants by default. GCN/CDNA architectures have a warp size of
64, <code class="code docutils literal notranslate"><span class="pre">threadIdx.x</span> <span class="pre">%</span> <span class="pre">warpSize</span></code> and <code class="code docutils literal notranslate"><span class="pre">val</span></code> in the example may obtain
values greater than 31. Consequently, shifting by such values would clear the
32-bit register to which the shift operation is applied. For AMD
architectures, a straightforward fix could look as follows:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Get the thread&#39;s position in the warp</span>
<span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">laneId</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="n">warpSize</span><span class="p">;</span>

<span class="c1">// Use lane ID for bit-shift</span>
<span class="n">val</span><span class="w"> </span><span class="o">&amp;</span><span class="w"> </span><span class="p">((</span><span class="mi">1ull</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="p">(</span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="n">warpSize</span><span class="p">)</span><span class="w"> </span><span class="p">)</span><span class="mi">-1</span><span class="w"> </span><span class="p">);</span>

<span class="c1">// Shift 64 bit integer with val variable</span>
<span class="n">WarpReduce</span><span class="o">::</span><span class="n">sum</span><span class="p">(</span><span class="w"> </span><span class="p">(</span><span class="n">val</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">warpSize</span><span class="p">)</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="p">(</span><span class="mi">1ull</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">val</span><span class="p">)</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
</pre></div>
</div>
<p>To handle different AMD GPU architectures, it is better to introduce appropriately
typed placeholders as shown below:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#if defined(__GFX8__) || defined(__GFX9__)</span>
<span class="k">typedef</span><span class="w"> </span><span class="kt">uint64_t</span><span class="w"> </span><span class="n">lane_mask_t</span><span class="p">;</span>
<span class="cp">#else</span>
<span class="k">typedef</span><span class="w"> </span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">lane_mask_t</span><span class="p">;</span>
<span class="cp">#endif</span>
</pre></div>
</div>
<p>The use of <code class="code docutils literal notranslate"><span class="pre">lane_mask_t</span></code> with the previous example:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Get the thread&#39;s position in the warp</span>
<span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">laneId</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="n">warpSize</span><span class="p">;</span>

<span class="c1">// Use lane ID for bit-shift</span>
<span class="n">val</span><span class="w"> </span><span class="o">&amp;</span><span class="w"> </span><span class="p">((</span><span class="n">lane_mask_t</span><span class="p">{</span><span class="mi">1</span><span class="p">}</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="p">(</span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="n">warpSize</span><span class="p">)</span><span class="w"> </span><span class="p">)</span><span class="mi">-1</span><span class="w"> </span><span class="p">);</span>

<span class="c1">// Shift 32 or 64 bit integer with val variable</span>
<span class="n">WarpReduce</span><span class="o">::</span><span class="n">sum</span><span class="p">(</span><span class="w"> </span><span class="p">(</span><span class="n">val</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">warpSize</span><span class="p">)</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="p">(</span><span class="n">lane_mask_t</span><span class="p">{</span><span class="mi">1</span><span class="p">}</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">val</span><span class="p">)</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
</pre></div>
</div>
</section>
<section id="porting-from-cuda-launch-bounds">
<h2>Porting from CUDA __launch_bounds__<a class="headerlink" href="#porting-from-cuda-launch-bounds" title="Link to this heading">#</a></h2>
<p>CUDA defines a <code class="docutils literal notranslate"><span class="pre">__launch_bounds__</span></code> qualifier which works similarly to the HIP
implementation, however, it uses different parameters:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__launch_bounds__</span><span class="p">(</span><span class="n">MAX_THREADS_PER_BLOCK</span><span class="p">,</span><span class="w"> </span><span class="n">MIN_BLOCKS_PER_MULTIPROCESSOR</span><span class="p">)</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">MAX_THREADS_PER_BLOCK</span></code> is the same in CUDA and in HIP. However, <code class="docutils literal notranslate"><span class="pre">MIN_BLOCKS_PER_MULTIPROCESSOR</span></code> in CUDA
must  be converted to <code class="docutils literal notranslate"><span class="pre">MIN_WARPS_PER_EXECUTION_UNIT</span></code> in HIP, which uses warps and execution units
rather than blocks and multiprocessors. This conversion can be done manually with the equation
considering the GPU’s configuration mode.</p>
<ul class="simple">
<li><p>In Compute Unit (CU) mode, typical of CDNA:</p></li>
</ul>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">MIN_WARPS_PER_EXECUTION_UNIT</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="n">MIN_BLOCKS_PER_MULTIPROCESSOR</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">MAX_THREADS_PER_BLOCK</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="p">(</span><span class="n">warpSize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">2</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p>In Workgroup Processor (WGP) mode, a feature of RDNA:</p></li>
</ul>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">MIN_WARPS_PER_EXECUTION_UNIT</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="n">MIN_BLOCKS_PER_MULTIPROCESSOR</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">MAX_THREADS_PER_BLOCK</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="p">(</span><span class="n">warpSize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">4</span><span class="p">)</span>
</pre></div>
</div>
<p>Directly controlling the warps per execution unit makes it easier to reason about the occupancy,
unlike with blocks, where the occupancy depends on the block size.</p>
<p>The use of execution units rather than multiprocessors also provides support for
architectures with multiple execution units per multiprocessor. For example, the
AMD GCN architecture has 4 execution units per multiprocessor.</p>
<section id="maxregcount">
<h3>maxregcount<a class="headerlink" href="#maxregcount" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">nvcc</span></code> compiler will predict the number of registers per thread based on the launch bounds calculation.
<code class="docutils literal notranslate"><span class="pre">--maxregcount</span> <span class="pre">X</span></code> can be used to override the compiler’s decision by enforcing a hard number of registers
(<code class="docutils literal notranslate"><span class="pre">X</span></code>) that the compiler must not exceed. If the compiler is unable to meet this requirement, it will place
additional “registers” into memory instead of using hardware registers.</p>
<p>Unlike <code class="docutils literal notranslate"><span class="pre">nvcc</span></code>, <code class="docutils literal notranslate"><span class="pre">amdclang++</span></code> does not support the <code class="docutils literal notranslate"><span class="pre">--maxregcount</span></code> option. You are encouraged to use
the <code class="docutils literal notranslate"><span class="pre">__launch_bounds__</span></code> directive since the parameters are more intuitive than micro-architecture
details like registers. The directive allows per-kernel control.</p>
</section>
</section>
<section id="driver-entry-point-access">
<h2>Driver entry point access<a class="headerlink" href="#driver-entry-point-access" title="Link to this heading">#</a></h2>
<p>The HIP runtime provides driver entry point access functionality. This feature lets
developers interact directly with the HIP driver API, providing more control over GPU
operations.</p>
<p>Driver entry point access provides several features:</p>
<ul class="simple">
<li><p>Retrieving the address of a runtime function</p></li>
<li><p>Requesting the default stream version on a per-thread basis</p></li>
<li><p>Accessing HIP features on older toolkits with a newer driver</p></li>
</ul>
<p>For more information on driver entry point access, see <a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html#_CPPv417hipGetProcAddressPKcPPvi8uint64_tP31hipDriverProcAddressQueryResult" title="hipGetProcAddress"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGetProcAddress()</span></code></a>.</p>
<section id="address-retrieval">
<h3>Address retrieval<a class="headerlink" href="#address-retrieval" title="Link to this heading">#</a></h3>
<p>The <a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html#_CPPv417hipGetProcAddressPKcPPvi8uint64_tP31hipDriverProcAddressQueryResult" title="hipGetProcAddress"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGetProcAddress()</span></code></a> function can be used to obtain the address of
a runtime function. This is demonstrated in the following example:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime_api.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="k">typedef</span><span class="w"> </span><span class="n">hipError_t</span><span class="w"> </span><span class="p">(</span><span class="o">*</span><span class="n">hipInit_t</span><span class="p">)(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="p">);</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// Initialize the HIP runtime</span>
<span class="w">    </span><span class="n">hipError_t</span><span class="w"> </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipInit</span><span class="p">(</span><span class="mi">0</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">res</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failed to initialize HIP runtime.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Get the address of the hipInit function</span>
<span class="w">    </span><span class="n">hipInit_t</span><span class="w"> </span><span class="n">hipInitFunc</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">hipVersion</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">HIP_VERSION</span><span class="p">;</span><span class="w"> </span><span class="c1">// Use the HIP version defined in hip_runtime_api.h</span>
<span class="w">    </span><span class="kt">uint64_t</span><span class="w"> </span><span class="n">flags</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="c1">// No special flags</span>
<span class="w">    </span><span class="n">hipDriverProcAddressQueryResult</span><span class="w"> </span><span class="n">symbolStatus</span><span class="p">;</span>

<span class="w">    </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipGetProcAddress</span><span class="p">(</span><span class="s">&quot;hipInit&quot;</span><span class="p">,</span><span class="w"> </span><span class="p">(</span><span class="kt">void</span><span class="o">**</span><span class="p">)</span><span class="o">&amp;</span><span class="n">hipInitFunc</span><span class="p">,</span><span class="w"> </span><span class="n">hipVersion</span><span class="p">,</span><span class="w"> </span><span class="n">flags</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">symbolStatus</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">res</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failed to get address of hipInit().&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Call the hipInit function using the obtained address</span>
<span class="w">    </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipInitFunc</span><span class="p">(</span><span class="mi">0</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">res</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;HIP runtime initialized successfully using hipGetProcAddress().&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failed to initialize HIP runtime using hipGetProcAddress().&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="per-thread-default-stream-version-request">
<h3>Per-thread default stream version request<a class="headerlink" href="#per-thread-default-stream-version-request" title="Link to this heading">#</a></h3>
<p>HIP offers functionality for managing streams on a per-thread basis. By using
<code class="docutils literal notranslate"><span class="pre">hipStreamPerThread</span></code>, each thread can independently manage its default stream,
simplifying operations. The following example demonstrates how this feature
enhances performance by reducing contention and improving efficiency.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// Initialize the HIP runtime</span>
<span class="w">    </span><span class="n">hipError_t</span><span class="w"> </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipInit</span><span class="p">(</span><span class="mi">0</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">res</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failed to initialize HIP runtime.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Get the per-thread default stream</span>
<span class="w">    </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">stream</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipStreamPerThread</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Use the stream for some operation</span>
<span class="w">    </span><span class="c1">// For example, allocate memory on the device</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">d_ptr</span><span class="p">;</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_ptr</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">res</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failed to allocate memory.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Perform some operation using the stream</span>
<span class="w">    </span><span class="c1">// For example, set memory on the device</span>
<span class="w">    </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemsetAsync</span><span class="p">(</span><span class="n">d_ptr</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">res</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failed to set memory.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Synchronize the stream</span>
<span class="w">    </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipStreamSynchronize</span><span class="p">(</span><span class="n">stream</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">res</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failed to synchronize stream.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Operation completed successfully using per-thread default stream.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Free the allocated memory</span>
<span class="w">    </span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_ptr</span><span class="p">);</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="accessing-hip-features-with-a-newer-driver">
<h3>Accessing HIP features with a newer driver<a class="headerlink" href="#accessing-hip-features-with-a-newer-driver" title="Link to this heading">#</a></h3>
<p>HIP is forward compatible, allowing newer features to be utilized
with older toolkits, provided a compatible driver is present. Feature support
can be verified through runtime API functions and version checks. This approach
ensures that applications can benefit from new features and improvements in the
HIP runtime without requiring recompilation with a newer toolkit. The function
<a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html#_CPPv417hipGetProcAddressPKcPPvi8uint64_tP31hipDriverProcAddressQueryResult" title="hipGetProcAddress"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGetProcAddress()</span></code></a> enables dynamic querying and the use of newer
functions offered by the HIP runtime, even if the application was built with an
older toolkit.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>:cpp:func:<code class="docutils literal notranslate"><span class="pre">hipGetProcAddress</span></code> is limited to HIP driver API function calls.
For HIP runtime API calls, the corresponding function is :cpp:func:<code class="docutils literal notranslate"><span class="pre">hipGetDriverEntryPoint</span></code>.</p>
</div>
<p>An example is provided for a hypothetical <code class="docutils literal notranslate"><span class="pre">foo()</span></code> function.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Get the address of the foo function</span>
<span class="n">foo_t</span><span class="w"> </span><span class="n">fooFunc</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">hipVersion</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">60300000</span><span class="p">;</span><span class="w"> </span><span class="c1">// HIP version number (e.g. 6.3.0)</span>
<span class="kt">uint64_t</span><span class="w"> </span><span class="n">flags</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="c1">// No special flags</span>
<span class="n">hipDriverProcAddressQueryResult</span><span class="w"> </span><span class="n">symbolStatus</span><span class="p">;</span>

<span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipGetProcAddress</span><span class="p">(</span><span class="s">&quot;foo&quot;</span><span class="p">,</span><span class="w"> </span><span class="p">(</span><span class="kt">void</span><span class="o">**</span><span class="p">)</span><span class="o">&amp;</span><span class="n">fooFunc</span><span class="p">,</span><span class="w"> </span><span class="n">hipVersion</span><span class="p">,</span><span class="w"> </span><span class="n">flags</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">symbolStatus</span><span class="p">);</span>
</pre></div>
</div>
<p>The HIP version number is defined as an integer:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">HIP_VERSION</span><span class="o">=</span><span class="n">HIP_VERSION_MAJOR</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">10000000</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">HIP_VERSION_MINOR</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">100000</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">HIP_VERSION_PATCH</span>
</pre></div>
</div>
</section>
</section>
<section id="memory-type-identification">
<h2>Memory type identification<a class="headerlink" href="#memory-type-identification" title="Link to this heading">#</a></h2>
<p>To return the pointer’s memory type in HIP, developers should use <a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html#_CPPv423hipPointerGetAttributesP21hipPointerAttribute_tPKv" title="hipPointerGetAttributes"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipPointerGetAttributes()</span></code></a>.
The first parameter of the function is <cite>hipPointerAttribute_t</cite>. Its <code class="docutils literal notranslate"><span class="pre">type</span></code> member variable indicates
whether the memory pointed to is allocated on the device or the host. For example:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">ptr</span><span class="p">;</span>
<span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">ptr</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">double</span><span class="p">));</span>
<span class="n">hipPointerAttribute_t</span><span class="w"> </span><span class="n">attr</span><span class="p">;</span>
<span class="n">hipPointerGetAttributes</span><span class="p">(</span><span class="o">&amp;</span><span class="n">attr</span><span class="p">,</span><span class="w"> </span><span class="n">ptr</span><span class="p">);</span><span class="w"> </span><span class="cm">/*attr.type is hipMemoryTypeDevice*/</span>
<span class="k">if</span><span class="p">(</span><span class="n">attr</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">hipMemoryTypeDevice</span><span class="p">)</span>
<span class="w">  </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;ptr is of type hipMemoryTypeDevice&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">ptrHost</span><span class="p">;</span>
<span class="n">hipHostMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">ptrHost</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">double</span><span class="p">));</span>
<span class="n">hipPointerAttribute_t</span><span class="w"> </span><span class="n">attr</span><span class="p">;</span>
<span class="n">hipPointerGetAttributes</span><span class="p">(</span><span class="o">&amp;</span><span class="n">attr</span><span class="p">,</span><span class="w"> </span><span class="n">ptrHost</span><span class="p">);</span><span class="w"> </span><span class="cm">/*attr.type is hipMemoryTypeHost*/</span>
<span class="k">if</span><span class="p">(</span><span class="n">attr</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">hipMemoryTypeHost</span><span class="p">)</span>
<span class="w">  </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;ptrHost is of type hipMemoryTypeHost&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
</pre></div>
</div>
<p>Note that <code class="docutils literal notranslate"><span class="pre">hipMemoryType</span></code> enum values are different from the
<code class="docutils literal notranslate"><span class="pre">cudaMemoryType</span></code> enum values.</p>
<p><code class="docutils literal notranslate"><span class="pre">hipMemoryType</span></code> is defined in <code class="docutils literal notranslate"><span class="pre">hip_runtime_api.h</span></code>:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">typedef</span><span class="w"> </span><span class="k">enum</span><span class="w"> </span><span class="nc">hipMemoryType</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">hipMemoryTypeHost</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w">    </span><span class="c1">///&lt; Memory is physically located on host</span>
<span class="w">    </span><span class="n">hipMemoryTypeDevice</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w">  </span><span class="c1">///&lt; Memory is physically located on device. (see deviceId for specific device)</span>
<span class="w">    </span><span class="n">hipMemoryTypeArray</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w">   </span><span class="c1">///&lt; Array memory, physically located on device. (see deviceId for specific device)</span>
<span class="w">    </span><span class="n">hipMemoryTypeUnified</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span><span class="w"> </span><span class="c1">///&lt; Not used currently</span>
<span class="w">    </span><span class="n">hipMemoryTypeManaged</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">4</span><span class="w">  </span><span class="c1">///&lt; Managed memory, automaticallly managed by the unified memory system</span>
<span class="p">}</span><span class="w"> </span><span class="n">hipMemoryType</span><span class="p">;</span>
</pre></div>
</div>
<p>In the CUDA toolkit, the <code class="docutils literal notranslate"><span class="pre">cudaMemoryType</span></code> is defined as following:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">enum</span><span class="w"> </span><span class="nc">cudaMemoryType</span>
<span class="p">{</span>
<span class="w">  </span><span class="n">cudaMemoryTypeUnregistered</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="c1">// Unregistered memory.</span>
<span class="w">  </span><span class="n">cudaMemoryTypeHost</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="c1">// Host memory.</span>
<span class="w">  </span><span class="n">cudaMemoryTypeDevice</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="c1">// Device memory.</span>
<span class="w">  </span><span class="n">cudaMemoryTypeManaged</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span><span class="w"> </span><span class="c1">// Managed memory</span>
<span class="p">}</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><code class="docutils literal notranslate"><span class="pre">cudaMemoryTypeUnregistered</span></code> is currently not supported as <code class="docutils literal notranslate"><span class="pre">hipMemoryType</span></code> enum,
due to HIP functionality backward compatibility.</p>
</div>
<p>When porting applications that use memory type APIs, ensure that you map the
CUDA memory types to the corresponding HIP memory types appropriately.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="kernel_language_cpp_support.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Kernel language C++ support</p>
      </div>
    </a>
    <a class="right-next"
       href="hip_rtc.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Programming for HIP runtime compiler (RTC)</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#porting-a-cuda-project">Porting a CUDA project</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#general-tips">General tips</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#using-hipify">Using HIPIFY</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-copy-functions">Memory copy functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#address-spaces">Address spaces</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#context-stack-behavior-differences">Context stack behavior differences</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#scanning-cuda-source-to-scope-the-translation">Scanning CUDA source to scope the translation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#automatically-converting-a-cuda-project">Automatically converting a CUDA project</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#library-and-driver-equivalents">Library and driver equivalents</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#cumodule-and-hipmodule">cuModule and hipModule</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#using-hipmodulelaunchkernel">Using hipModuleLaunchKernel</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#cuctx-and-hipctx">cuCtx and hipCtx</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#compilation">Compilation</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-headers">HIP Headers</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-a-standard-c-compiler">Using a Standard C++ Compiler</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#compiler-defines-for-hip">Compiler defines for HIP</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#identifying-compiler-target">Identifying host or device compilation pass</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-clang-implementation-notes">HIP-Clang implementation notes</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#initialization-and-termination-functions">Initialization and termination functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-launching">Kernel launching</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#compilation-options-for-hipmoduleloaddataex">Compilation options for hipModuleLoadDataEx</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#identifying-device-architecture-features">Identifying device architecture and features</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#device-code-feature-identification">Device code feature identification</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#host-code-feature-identification">Host code feature identification</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#feature-macros-and-properties">Feature macros and properties</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#warpsize">warpSize</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#lane-masks-bit-shift">Lane masks bit-shift</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#porting-from-cuda-launch-bounds">Porting from CUDA __launch_bounds__</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#maxregcount">maxregcount</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#driver-entry-point-access">Driver entry point access</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#address-retrieval">Address retrieval</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#per-thread-default-stream-version-request">Per-thread default stream version request</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#accessing-hip-features-with-a-newer-driver">Accessing HIP features with a newer driver</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-type-identification">Memory type identification</a></li>
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
