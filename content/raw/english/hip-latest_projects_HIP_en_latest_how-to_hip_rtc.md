---
title: "Programming for HIP runtime compiler (RTC) &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_rtc.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:24.020074+00:00
content_hash: "7063ce41c50777d5"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="HIP runtime compiler (RTC)" name="description" />
<meta content="AMD, ROCm, HIP, CUDA, RTC, HIP runtime compiler" name="keywords" />

    <title>Programming for HIP runtime compiler (RTC) &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/hip_rtc';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="AMD compute language runtimes (CLR)" href="../understand/amd_clr.html" />
    <link rel="prev" title="Porting CUDA code to HIP" href="hip_porting_guide.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/hip_rtc.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l1"><a class="reference internal" href="hip_porting_guide.html">Porting CUDA code to HIP</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Programming for HIP runtime compiler (RTC)</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">Programming...</li>
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
    <h1>Programming for HIP runtime compiler (RTC)</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#compilation-apis">Compilation APIs</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hiprtc-specific-options">HIPRTC specific options</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#bitcode">Bitcode</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#cu-mode-vs-wgp-mode">CU mode vs WGP mode</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#linker-apis">Linker APIs</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#example">Example</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#input-types">Input Types</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#backward-compatibility-of-llvm-bitcode-ir">Backward Compatibility of LLVM Bitcode/IR</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#link-options">Link Options</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#error-handling">Error Handling</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hiprtc-general-apis">HIPRTC General APIs</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#lowered-names-mangled-names">Lowered Names (Mangled Names)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">Example</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#versioning">Versioning</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-header-support">HIP header support</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#deprecation-notice">Deprecation notice</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="programming-for-hip-runtime-compiler-rtc">
<span id="hip-runtime-compiler-how-to"></span><h1>Programming for HIP runtime compiler (RTC)<a class="headerlink" href="#programming-for-hip-runtime-compiler-rtc" title="Link to this heading">#</a></h1>
<p>HIP supports the kernels compilation at runtime with the <code class="docutils literal notranslate"><span class="pre">hiprtc*</span></code> APIs.
Kernels can be stored as a text string and can be passed to HIPRTC APIs
alongside options to guide the compilation.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p>Device code compilation via HIPRTC uses the <code class="docutils literal notranslate"><span class="pre">__hip_internal</span></code> namespace instead
of the <code class="docutils literal notranslate"><span class="pre">std</span></code> namespace to avoid namespace collision.</p></li>
<li><p>This library can be used for compilation on systems without AMD GPU drivers
installed (offline compilation). However, running the compiled code still
requires both the HIP runtime library and GPU drivers on the target system.</p></li>
<li><p>Developers can bundle this library with their application.</p></li>
<li><p>HIPRTC leverages AMD’s Code Object Manager API (<code class="docutils literal notranslate"><span class="pre">Comgr</span></code>) internally, which
is designed to simplify linking, compiling, and inspecting code objects. For
more information, see the <a class="reference external" href="https://github.com/ROCm/llvm-project/blob/amd-staging/amd/comgr/README.md">llvm-project/amd/comgr/README</a>.</p></li>
<li><p>Comgr may cache HIPRTC compilations. To force full recompilation for each HIPRTC API invocation, set AMD_COMGR_CACHE=0.</p>
<ul>
<li><p>When viewing the <em>README</em> in the Comgr GitHub repository you should look at a
specific branch of interest, such as <code class="docutils literal notranslate"><span class="pre">docs/6.3.0</span></code> or <code class="docutils literal notranslate"><span class="pre">docs/6.4.1</span></code>, rather than the default branch.</p></li>
</ul>
</li>
</ul>
</div>
<section id="compilation-apis">
<h2>Compilation APIs<a class="headerlink" href="#compilation-apis" title="Link to this heading">#</a></h2>
<p>To use HIPRTC functionality the header needs to be included:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hiprtc.h&gt;</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Prior to the 7.0 release, the HIP runtime included the hipRTC library. With the 7.0
release, the library is separate and must be specifically included as shown above.</p>
</div>
<p>Kernels can be stored in a string:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">static</span><span class="w"> </span><span class="k">constexpr</span><span class="w"> </span><span class="k">auto</span><span class="w"> </span><span class="n">kernel_source</span><span class="w"> </span><span class="p">{</span>
<span class="sa">R</span><span class="s">&quot;</span><span class="dl">(</span>
<span class="s">    extern &quot;C&quot;</span>
<span class="s">    __global__ void vector_add(float* output, float* input1, float* input2, size_t size) {</span>
<span class="s">      int i = threadIdx.x;</span>
<span class="s">      if (i &lt; size) {</span>
<span class="s">        output[i] = input1[i] + input2[i];</span>
<span class="s">      }</span>
<span class="s">    }</span>
<span class="dl">)</span><span class="s">&quot;</span><span class="p">};</span>
</pre></div>
</div>
<p>To compile this kernel, it needs to be associated with
<code class="xref cpp cpp-struct docutils literal notranslate"><span class="pre">hiprtcProgram</span></code> type, which is done by declaring <code class="code docutils literal notranslate"><span class="pre">hiprtcProgram</span> <span class="pre">prog;</span></code>
and associating the string of kernel with this program:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hiprtcCreateProgram</span><span class="p">(</span><span class="o">&amp;</span><span class="n">prog</span><span class="p">,</span><span class="w">                 </span><span class="c1">// HIPRTC program handle</span>
<span class="w">                    </span><span class="n">kernel_source</span><span class="p">,</span><span class="w">         </span><span class="c1">// HIP kernel source string</span>
<span class="w">                    </span><span class="s">&quot;vector_add.cpp&quot;</span><span class="p">,</span><span class="w">      </span><span class="c1">// Name of the HIP program, can be null or an empty string</span>
<span class="w">                    </span><span class="mi">0</span><span class="p">,</span><span class="w">                     </span><span class="c1">// Number of headers</span>
<span class="w">                    </span><span class="nb">NULL</span><span class="p">,</span><span class="w">                  </span><span class="c1">// Header sources</span>
<span class="w">                    </span><span class="nb">NULL</span><span class="p">);</span><span class="w">                 </span><span class="c1">// Name of header files</span>
</pre></div>
</div>
<p><a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv419hiprtcCreateProgramP13hiprtcProgramPKcPKciPPCKcPPCKc" title="hiprtcCreateProgram"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcCreateProgram()</span></code></a> API also allows you to add headers which can be
included in your RTC program. For online compilation, the compiler pre-defines
HIP device API functions, HIP specific types and macros for device compilation,
but doesn’t include standard C/C++ headers by default. Users can only include
header files provided to <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv419hiprtcCreateProgramP13hiprtcProgramPKcPKciPPCKcPPCKc" title="hiprtcCreateProgram"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcCreateProgram()</span></code></a>.</p>
<p>After associating the kernel string with <code class="xref cpp cpp-struct docutils literal notranslate"><span class="pre">hiprtcProgram</span></code>, you can
now compile this program using:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hiprtcCompileProgram</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w">     </span><span class="c1">// hiprtcProgram</span>
<span class="w">                    </span><span class="mi">0</span><span class="p">,</span><span class="w">         </span><span class="c1">// Number of options</span>
<span class="w">                    </span><span class="n">options</span><span class="p">);</span><span class="w">  </span><span class="c1">// Clang Options [Supported Clang Options](clang_options.md)</span>
</pre></div>
</div>
<p><a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcCompileProgram13hiprtcProgramiPPCKc" title="hiprtcCompileProgram"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcCompileProgram()</span></code></a> returns a status value which can be converted
to string via <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcGetErrorString12hiprtcResult" title="hiprtcGetErrorString"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcGetErrorString()</span></code></a>. If compilation is successful,
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcCompileProgram13hiprtcProgramiPPCKc" title="hiprtcCompileProgram"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcCompileProgram()</span></code></a> will return <code class="docutils literal notranslate"><span class="pre">HIPRTC_SUCCESS</span></code>.</p>
<p>if the compilation fails or produces warnings, you can look up the logs via:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">size_t</span><span class="w"> </span><span class="n">logSize</span><span class="p">;</span>
<span class="n">hiprtcGetProgramLogSize</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">logSize</span><span class="p">);</span>

<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">logSize</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">string</span><span class="w"> </span><span class="n">log</span><span class="p">(</span><span class="n">logSize</span><span class="p">,</span><span class="w"> </span><span class="sc">&#39;\0&#39;</span><span class="p">);</span>
<span class="w">  </span><span class="n">hiprtcGetProgramLog</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">log</span><span class="p">[</span><span class="mi">0</span><span class="p">]);</span>
<span class="w">  </span><span class="c1">// Corrective action with logs</span>
<span class="p">}</span>
</pre></div>
</div>
<p>If the compilation is successful, you can load the compiled binary in a local
variable.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">size_t</span><span class="w"> </span><span class="n">codeSize</span><span class="p">;</span>
<span class="n">hiprtcGetCodeSize</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">codeSize</span><span class="p">);</span>

<span class="n">vector</span><span class="o">&lt;</span><span class="kt">char</span><span class="o">&gt;</span><span class="w"> </span><span class="n">kernel_binary</span><span class="p">(</span><span class="n">codeSize</span><span class="p">);</span>
<span class="n">hiprtcGetCode</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="n">kernel_binary</span><span class="p">.</span><span class="n">data</span><span class="p">());</span>
</pre></div>
</div>
<p>After loading the binary, <code class="xref cpp cpp-struct docutils literal notranslate"><span class="pre">hiprtcProgram</span></code> can be destroyed.
<code class="code docutils literal notranslate"><span class="pre">hiprtcDestroyProgram(&amp;prog);</span></code></p>
<p>The binary present in <code class="docutils literal notranslate"><span class="pre">kernel_binary</span></code> can now be loaded via
<a class="reference internal" href="../reference/hip_runtime_api/modules/module_management.html#_CPPv417hipModuleLoadDataP11hipModule_tPKv" title="hipModuleLoadData"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipModuleLoadData()</span></code></a> API.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipModule_t</span><span class="w"> </span><span class="k">module</span><span class="p">;</span>
<span class="n">hipFunction_t</span><span class="w"> </span><span class="n">kernel</span><span class="p">;</span>

<span class="n">hipModuleLoadData</span><span class="p">(</span><span class="o">&amp;</span><span class="k">module</span><span class="p">,</span><span class="w"> </span><span class="n">kernel_binary</span><span class="p">.</span><span class="n">data</span><span class="p">());</span>
<span class="n">hipModuleGetFunction</span><span class="p">(</span><span class="o">&amp;</span><span class="n">kernel</span><span class="p">,</span><span class="w"> </span><span class="k">module</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;vector_add&quot;</span><span class="p">);</span>
</pre></div>
</div>
<p>And now this kernel can be launched via <code class="docutils literal notranslate"><span class="pre">hipModule</span></code> APIs.</p>
<p>The full example is below:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hiprtc.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;string&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>

<span class="cp">#define CHECK_RET_CODE(call, ret_code)                                                             \</span>
<span class="cp">  {                                                                                                \</span>
<span class="cp">    if ((call) != ret_code) {                                                                      \</span>
<span class="cp">      std::cout &lt;&lt; &quot;Failed in call: &quot; &lt;&lt; #call &lt;&lt; std::endl;                                       \</span>
<span class="cp">      std::abort();                                                                                \</span>
<span class="cp">    }                                                                                              \</span>
<span class="cp">  }</span>
<span class="cp">#define HIP_CHECK(call) CHECK_RET_CODE(call, hipSuccess)</span>
<span class="cp">#define HIPRTC_CHECK(call) CHECK_RET_CODE(call, HIPRTC_SUCCESS)</span>

<span class="c1">// source code for hiprtc</span>
<span class="k">static</span><span class="w"> </span><span class="k">constexpr</span><span class="w"> </span><span class="k">auto</span><span class="w"> </span><span class="n">kernel_source</span><span class="p">{</span>
<span class="w">    </span><span class="sa">R</span><span class="s">&quot;</span><span class="dl">(</span>
<span class="s">    extern &quot;C&quot;</span>
<span class="s">    __global__ void vector_add(float* output, float* input1, float* input2, size_t size) {</span>
<span class="s">      int i = threadIdx.x;</span>
<span class="s">      if (i &lt; size) {</span>
<span class="s">        output[i] = input1[i] + input2[i];</span>
<span class="s">      }</span>
<span class="s">    }</span>
<span class="dl">)</span><span class="s">&quot;</span><span class="p">};</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">hiprtcProgram</span><span class="w"> </span><span class="n">prog</span><span class="p">;</span>
<span class="w">  </span><span class="k">auto</span><span class="w"> </span><span class="n">rtc_ret_code</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hiprtcCreateProgram</span><span class="p">(</span><span class="o">&amp;</span><span class="n">prog</span><span class="p">,</span><span class="w">            </span><span class="c1">// HIPRTC program handle</span>
<span class="w">                                          </span><span class="n">kernel_source</span><span class="p">,</span><span class="w">    </span><span class="c1">// kernel source string</span>
<span class="w">                                          </span><span class="s">&quot;vector_add.cpp&quot;</span><span class="p">,</span><span class="w"> </span><span class="c1">// Name of the file</span>
<span class="w">                                          </span><span class="mi">0</span><span class="p">,</span><span class="w">                </span><span class="c1">// Number of headers</span>
<span class="w">                                          </span><span class="nb">NULL</span><span class="p">,</span><span class="w">             </span><span class="c1">// Header sources</span>
<span class="w">                                          </span><span class="nb">NULL</span><span class="p">);</span><span class="w">            </span><span class="c1">// Name of header file</span>

<span class="w">  </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rtc_ret_code</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">HIPRTC_SUCCESS</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failed to create program&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">abort</span><span class="p">();</span>
<span class="w">  </span><span class="p">}</span>

<span class="w">  </span><span class="n">hipDeviceProp_t</span><span class="w"> </span><span class="n">props</span><span class="p">;</span>
<span class="w">  </span><span class="kt">int</span><span class="w"> </span><span class="n">device</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDeviceProperties</span><span class="p">(</span><span class="o">&amp;</span><span class="n">props</span><span class="p">,</span><span class="w"> </span><span class="n">device</span><span class="p">));</span>
<span class="w">  </span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="w"> </span><span class="n">sarg</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="p">(</span><span class="s">&quot;--gpu-architecture=&quot;</span><span class="p">)</span><span class="w"> </span><span class="o">+</span>
<span class="w">      </span><span class="n">props</span><span class="p">.</span><span class="n">gcnArchName</span><span class="p">;</span><span class="w">  </span><span class="c1">// device for which binary is to be generated</span>

<span class="w">  </span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">*</span><span class="w"> </span><span class="n">options</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="n">sarg</span><span class="p">.</span><span class="n">c_str</span><span class="p">()};</span>

<span class="w">  </span><span class="n">rtc_ret_code</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hiprtcCompileProgram</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w">      </span><span class="c1">// hiprtcProgram</span>
<span class="w">                                      </span><span class="mi">0</span><span class="p">,</span><span class="w">         </span><span class="c1">// Number of options</span>
<span class="w">                                      </span><span class="n">options</span><span class="p">);</span><span class="w">  </span><span class="c1">// Clang Options</span>
<span class="w">  </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rtc_ret_code</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">HIPRTC_SUCCESS</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failed to create program&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">abort</span><span class="p">();</span>
<span class="w">  </span><span class="p">}</span>

<span class="w">  </span><span class="kt">size_t</span><span class="w"> </span><span class="n">logSize</span><span class="p">;</span>
<span class="w">  </span><span class="n">HIPRTC_CHECK</span><span class="p">(</span><span class="n">hiprtcGetProgramLogSize</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">logSize</span><span class="p">));</span>

<span class="w">  </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">logSize</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="w"> </span><span class="n">log</span><span class="p">(</span><span class="n">logSize</span><span class="p">,</span><span class="w"> </span><span class="sc">&#39;\0&#39;</span><span class="p">);</span>
<span class="w">    </span><span class="n">HIPRTC_CHECK</span><span class="p">(</span><span class="n">hiprtcGetProgramLog</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">log</span><span class="p">[</span><span class="mi">0</span><span class="p">]));</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Compilation failed or produced warnings: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">log</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">abort</span><span class="p">();</span>
<span class="w">  </span><span class="p">}</span>

<span class="w">  </span><span class="kt">size_t</span><span class="w"> </span><span class="n">codeSize</span><span class="p">;</span>
<span class="w">  </span><span class="n">HIPRTC_CHECK</span><span class="p">(</span><span class="n">hiprtcGetCodeSize</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">codeSize</span><span class="p">));</span>

<span class="w">  </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">char</span><span class="o">&gt;</span><span class="w"> </span><span class="n">kernel_binary</span><span class="p">(</span><span class="n">codeSize</span><span class="p">);</span>
<span class="w">  </span><span class="n">HIPRTC_CHECK</span><span class="p">(</span><span class="n">hiprtcGetCode</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="n">kernel_binary</span><span class="p">.</span><span class="n">data</span><span class="p">()));</span>

<span class="w">  </span><span class="n">HIPRTC_CHECK</span><span class="p">(</span><span class="n">hiprtcDestroyProgram</span><span class="p">(</span><span class="o">&amp;</span><span class="n">prog</span><span class="p">));</span>

<span class="w">  </span><span class="n">hipModule_t</span><span class="w"> </span><span class="k">module</span><span class="p">;</span>
<span class="w">  </span><span class="n">hipFunction_t</span><span class="w"> </span><span class="n">kernel</span><span class="p">;</span>

<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipModuleLoadData</span><span class="p">(</span><span class="o">&amp;</span><span class="k">module</span><span class="p">,</span><span class="w"> </span><span class="n">kernel_binary</span><span class="p">.</span><span class="n">data</span><span class="p">()));</span>
<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipModuleGetFunction</span><span class="p">(</span><span class="o">&amp;</span><span class="n">kernel</span><span class="p">,</span><span class="w"> </span><span class="k">module</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;vector_add&quot;</span><span class="p">));</span>

<span class="w">  </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">ele_size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">256</span><span class="p">;</span><span class="w">  </span><span class="c1">// total number of items to add</span>
<span class="w">  </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">hinput</span><span class="p">,</span><span class="w"> </span><span class="n">output</span><span class="p">;</span>
<span class="w">  </span><span class="n">hinput</span><span class="p">.</span><span class="n">reserve</span><span class="p">(</span><span class="n">ele_size</span><span class="p">);</span>
<span class="w">  </span><span class="n">output</span><span class="p">.</span><span class="n">reserve</span><span class="p">(</span><span class="n">ele_size</span><span class="p">);</span>
<span class="w">  </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">ele_size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">hinput</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="k">static_cast</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="p">));</span>
<span class="w">    </span><span class="n">output</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="mf">0.0f</span><span class="p">);</span>
<span class="w">  </span><span class="p">}</span>

<span class="w">  </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">dinput1</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">dinput2</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">doutput</span><span class="p">;</span>
<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">dinput1</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">ele_size</span><span class="p">));</span>
<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">dinput2</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">ele_size</span><span class="p">));</span>
<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">doutput</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">ele_size</span><span class="p">));</span>

<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">dinput1</span><span class="p">,</span><span class="w"> </span><span class="n">hinput</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">ele_size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>
<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">dinput2</span><span class="p">,</span><span class="w"> </span><span class="n">hinput</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">ele_size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>

<span class="w">  </span><span class="k">struct</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">output</span><span class="p">;</span>
<span class="w">    </span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">input1</span><span class="p">;</span>
<span class="w">    </span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">input2</span><span class="p">;</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">;</span>
<span class="w">  </span><span class="p">}</span><span class="w"> </span><span class="n">args</span><span class="p">{</span><span class="n">doutput</span><span class="p">,</span><span class="w"> </span><span class="n">dinput1</span><span class="p">,</span><span class="w"> </span><span class="n">dinput2</span><span class="p">,</span><span class="w"> </span><span class="n">ele_size</span><span class="p">};</span>

<span class="w">  </span><span class="k">auto</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">args</span><span class="p">);</span>
<span class="w">  </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">config</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="n">HIP_LAUNCH_PARAM_BUFFER_POINTER</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">args</span><span class="p">,</span><span class="w"> </span><span class="n">HIP_LAUNCH_PARAM_BUFFER_SIZE</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">size</span><span class="p">,</span>
<span class="w">                    </span><span class="n">HIP_LAUNCH_PARAM_END</span><span class="p">};</span>

<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipModuleLaunchKernel</span><span class="p">(</span><span class="n">kernel</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">ele_size</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="n">config</span><span class="p">));</span>

<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">output</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">doutput</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">ele_size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">  </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">ele_size</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">((</span><span class="n">hinput</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">hinput</span><span class="p">[</span><span class="n">i</span><span class="p">])</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">output</span><span class="p">[</span><span class="n">i</span><span class="p">])</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failed in validation: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="p">(</span><span class="n">hinput</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">hinput</span><span class="p">[</span><span class="n">i</span><span class="p">])</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; - &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">output</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
<span class="w">                </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">      </span><span class="n">std</span><span class="o">::</span><span class="n">abort</span><span class="p">();</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}</span>
<span class="w">  </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Passed&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">dinput1</span><span class="p">));</span>
<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">dinput2</span><span class="p">));</span>
<span class="w">  </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">doutput</span><span class="p">));</span>
<span class="p">}</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Some applications define datatypes such as <code class="docutils literal notranslate"><span class="pre">int64_t</span></code>, <code class="docutils literal notranslate"><span class="pre">uint64_t</span></code>, <code class="docutils literal notranslate"><span class="pre">int32_t</span></code>, and <code class="docutils literal notranslate"><span class="pre">uint32_t</span></code>
that could lead to conflicts when integrating with <code class="docutils literal notranslate"><span class="pre">hipRTC</span></code>. To resolve these conflicts, these
datatypes are replaced with HIP-specific internal datatypes prefixed with <code class="docutils literal notranslate"><span class="pre">__hip</span></code>. For example,
<code class="docutils literal notranslate"><span class="pre">int64_t</span></code> is replaced by <code class="docutils literal notranslate"><span class="pre">__hip_int64_t</span></code>.</p>
</div>
</section>
<section id="hiprtc-specific-options">
<h2>HIPRTC specific options<a class="headerlink" href="#hiprtc-specific-options" title="Link to this heading">#</a></h2>
<p>HIPRTC provides a few HIPRTC specific flags:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">--gpu-architecture</span></code> : This flag can guide the code object generation for a
specific GPU architecture. Example:
<code class="docutils literal notranslate"><span class="pre">--gpu-architecture=gfx906:sramecc+:xnack-</span></code>, its equivalent to
<code class="docutils literal notranslate"><span class="pre">--offload-arch</span></code>.</p>
<ul>
<li><p>This option is compulsory if compilation is done on a system without AMD
GPUs supported by HIP runtime.</p></li>
<li><p>Otherwise, HIPRTC will load the hip runtime and gather the current device
and its architecture info and use it as option.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">-fgpu-rdc</span></code> : This flag when provided during the
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv419hiprtcCreateProgramP13hiprtcProgramPKcPKciPPCKcPPCKc" title="hiprtcCreateProgram"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcCreateProgram()</span></code></a> generates the bitcode (HIPRTC doesn’t convert
this bitcode into ISA and binary). This bitcode can later be fetched using
<code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcGetBitcode()</span></code> and <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcGetBitcodeSize13hiprtcProgramP6size_t" title="hiprtcGetBitcodeSize"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcGetBitcodeSize()</span></code></a> APIs.</p></li>
</ul>
<section id="bitcode">
<h3>Bitcode<a class="headerlink" href="#bitcode" title="Link to this heading">#</a></h3>
<p>In the usual scenario, the kernel associated with <code class="xref cpp cpp-struct docutils literal notranslate"><span class="pre">hiprtcProgram</span></code> is
compiled into the binary which can be loaded and run. However, if <code class="docutils literal notranslate"><span class="pre">-fgpu-rdc</span></code>
option is provided in the compile options, HIPRTC calls comgr and generates only
the LLVM bitcode. It doesn’t convert this bitcode to ISA and generate the final
binary.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="w"> </span><span class="n">sarg</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="p">(</span><span class="s">&quot;-fgpu-rdc&quot;</span><span class="p">);</span>
<span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">*</span><span class="w"> </span><span class="n">options</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">sarg</span><span class="p">.</span><span class="n">c_str</span><span class="p">()</span><span class="w"> </span><span class="p">};</span>
<span class="n">hiprtcCompileProgram</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="c1">// hiprtcProgram</span>
<span class="w">                     </span><span class="mi">1</span><span class="p">,</span><span class="w">    </span><span class="c1">// Number of options</span>
<span class="w">                     </span><span class="n">options</span><span class="p">);</span>
</pre></div>
</div>
<p>If the compilation is successful, one can load the bitcode in a local variable
using the bitcode APIs provided by HIPRTC.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">size_t</span><span class="w"> </span><span class="n">bitCodeSize</span><span class="p">;</span>
<span class="n">hiprtcGetBitcodeSize</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">bitCodeSize</span><span class="p">);</span>

<span class="n">vector</span><span class="o">&lt;</span><span class="kt">char</span><span class="o">&gt;</span><span class="w"> </span><span class="n">kernel_bitcode</span><span class="p">(</span><span class="n">bitCodeSize</span><span class="p">);</span>
<span class="n">hiprtcGetBitcode</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="n">kernel_bitcode</span><span class="p">.</span><span class="n">data</span><span class="p">());</span>
</pre></div>
</div>
</section>
<section id="cu-mode-vs-wgp-mode">
<h3>CU mode vs WGP mode<a class="headerlink" href="#cu-mode-vs-wgp-mode" title="Link to this heading">#</a></h3>
<p>All <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html" title="(in ROCm installation on Linux v7.2.2)"><span class="xref std std-doc">supported AMD GPUs</span></a> are built around a data-parallel
processor (DPP) array.</p>
<p>On CDNA GPUs, the DPP is organized as a set of compute unit (CU) pipelines, with each CU containing four SIMD64
units. Each CU has its own low-latency memory space called local data share (LDS), which threads from a warp running on
the CU can access.</p>
<p>On RDNA GPUs, the DPP is organized as a set of workgroup processor (WGP) pipelines. Each WGP contains two CUs, and each
CU contains two SIMD32 units. The LDS is attached to the WGP, so threads from different warps can access the same LDS if
they run on CUs within the same WGP.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Because CDNA GPUs do not use workgroup processors and have a different CU layout, the following information applies
only to RDNA GPUs.</p>
</div>
<p>Warps are dispatched in one of two modes. These control whether warps are distributed across two SIMD32s (<strong>CU mode</strong>)
or across all four SIMD32s within a WGP (<strong>WGP mode</strong>).</p>
<p>CU mode executes two warps per block on a single CU and provides only half the LDS to those warps. Independence between
CUs can improve performance for workloads avoiding inter-warp communication, but LDS capacity per CU is limited.</p>
<p>WGP mode executes four warps per block on a WGP with a shared LDS. It can increase occupancy and improve performance
for workloads without heavy inter-warp communication, but it can degrade performance for programs relying on atomics or
extensive inter-warp communication.</p>
<p>For more information on the differences between CU and WGP modes, please refer to the appropriate ISA reference under
<a class="reference external" href="https://gpuopen.com/amd-gpu-architecture-programming-documentation/">AMD RDNA architecture</a>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>HIPRTC assumes <strong>WGP mode by default</strong> for RDNA GPUs. This can be overridden by passing <code class="docutils literal notranslate"><span class="pre">-mcumode</span></code> as a compile
option in <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcCompileProgram13hiprtcProgramiPPCKc" title="hiprtcCompileProgram"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcCompileProgram()</span></code></a>.</p>
</div>
</section>
</section>
<section id="linker-apis">
<h2>Linker APIs<a class="headerlink" href="#linker-apis" title="Link to this heading">#</a></h2>
<p>The bitcode generated using the HIPRTC Bitcode APIs can be loaded using
<code class="docutils literal notranslate"><span class="pre">hipModule</span></code> APIs and also can be linked with other generated bitcodes with
appropriate linker flags using the HIPRTC linker APIs. This also provides more
flexibility and optimizations to the applications who want to generate the
binary dynamically according to their needs. The input bitcodes can be generated
only for a specific architecture or it can be a bundled bitcode which is
generated for multiple architectures.</p>
<section id="example">
<h3>Example<a class="headerlink" href="#example" title="Link to this heading">#</a></h3>
<p>Firstly, HIPRTC link instance or a pending linker invocation must be created
using <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv416hiprtcLinkCreatejP16hiprtcJIT_optionPPvP15hiprtcLinkState" title="hiprtcLinkCreate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcLinkCreate()</span></code></a>, with the appropriate linker options
provided.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hiprtcLinkCreate</span><span class="p">(</span><span class="w"> </span><span class="n">num_options</span><span class="p">,</span><span class="w">           </span><span class="c1">// number of options</span>
<span class="w">                  </span><span class="n">options</span><span class="p">,</span><span class="w">               </span><span class="c1">// Array of options</span>
<span class="w">                  </span><span class="n">option_vals</span><span class="p">,</span><span class="w">           </span><span class="c1">// Array of option values cast to void*</span>
<span class="w">                  </span><span class="o">&amp;</span><span class="n">rtc_link_state</span><span class="w"> </span><span class="p">);</span><span class="w">     </span><span class="c1">// HIPRTC link state created upon success</span>
</pre></div>
</div>
<p>Following which, the bitcode data can be added to this link instance via
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv417hiprtcLinkAddData15hiprtcLinkState18hiprtcJITInputTypePv6size_tPKcjP16hiprtcJIT_optionPPv" title="hiprtcLinkAddData"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcLinkAddData()</span></code></a> (if the data is present as a string) or
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv417hiprtcLinkAddFile15hiprtcLinkState18hiprtcJITInputTypePKcjP16hiprtcJIT_optionPPv" title="hiprtcLinkAddFile"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcLinkAddFile()</span></code></a> (if the data is present as a file) with the
appropriate input type according to the data or the bitcode used.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hiprtcLinkAddData</span><span class="p">(</span><span class="n">rtc_link_state</span><span class="p">,</span><span class="w">        </span><span class="c1">// HIPRTC link state</span>
<span class="w">                  </span><span class="n">input_type</span><span class="p">,</span><span class="w">            </span><span class="c1">// type of the input data or bitcode</span>
<span class="w">                  </span><span class="n">bit_code_ptr</span><span class="p">,</span><span class="w">          </span><span class="c1">// input data which is null terminated</span>
<span class="w">                  </span><span class="n">bit_code_size</span><span class="p">,</span><span class="w">         </span><span class="c1">// size of the input data</span>
<span class="w">                  </span><span class="s">&quot;a&quot;</span><span class="p">,</span><span class="w">                   </span><span class="c1">// optional name for this input</span>
<span class="w">                  </span><span class="mi">0</span><span class="p">,</span><span class="w">                     </span><span class="c1">// size of the options</span>
<span class="w">                  </span><span class="mi">0</span><span class="p">,</span><span class="w">                     </span><span class="c1">// Array of options applied to this input</span>
<span class="w">                  </span><span class="mi">0</span><span class="p">);</span><span class="w">                    </span><span class="c1">// Array of option values cast to void*</span>
</pre></div>
</div>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hiprtcLinkAddFile</span><span class="p">(</span><span class="n">rtc_link_state</span><span class="p">,</span><span class="w">        </span><span class="c1">// HIPRTC link state</span>
<span class="w">                  </span><span class="n">input_type</span><span class="p">,</span><span class="w">            </span><span class="c1">// type of the input data or bitcode</span>
<span class="w">                  </span><span class="n">bc_file_path</span><span class="p">.</span><span class="n">c_str</span><span class="p">(),</span><span class="w">  </span><span class="c1">// path to the input file where bitcode is present</span>
<span class="w">                  </span><span class="mi">0</span><span class="p">,</span><span class="w">                     </span><span class="c1">// size of the options</span>
<span class="w">                  </span><span class="mi">0</span><span class="p">,</span><span class="w">                     </span><span class="c1">// Array of options applied to this input</span>
<span class="w">                  </span><span class="mi">0</span><span class="p">);</span><span class="w">                    </span><span class="c1">// Array of option values cast to void*</span>
</pre></div>
</div>
<p>Once the bitcodes for multiple architectures are added to the link instance, the
linking of the device code must be completed using <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv418hiprtcLinkComplete15hiprtcLinkStatePPvP6size_t" title="hiprtcLinkComplete"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcLinkComplete()</span></code></a>
which generates the final binary.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hiprtcLinkComplete</span><span class="p">(</span><span class="n">rtc_link_state</span><span class="p">,</span><span class="w">       </span><span class="c1">// HIPRTC link state</span>
<span class="w">                   </span><span class="o">&amp;</span><span class="n">binary</span><span class="p">,</span><span class="w">              </span><span class="c1">// upon success, points to the output binary</span>
<span class="w">                   </span><span class="o">&amp;</span><span class="n">binarySize</span><span class="p">);</span><span class="w">         </span><span class="c1">// size of the binary is stored (optional)</span>
</pre></div>
</div>
<p>If the <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv418hiprtcLinkComplete15hiprtcLinkStatePPvP6size_t" title="hiprtcLinkComplete"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcLinkComplete()</span></code></a> returns successfully, the generated binary
can be loaded and run using the <code class="docutils literal notranslate"><span class="pre">hipModule*</span></code> APIs.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipModuleLoadData</span><span class="p">(</span><span class="o">&amp;</span><span class="k">module</span><span class="p">,</span><span class="w"> </span><span class="n">binary</span><span class="p">);</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul>
<li><p>The compiled binary must be loaded before HIPRTC link instance is destroyed
using the <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv417hiprtcLinkDestroy15hiprtcLinkState" title="hiprtcLinkDestroy"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcLinkDestroy()</span></code></a> API.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hiprtcLinkDestroy</span><span class="p">(</span><span class="n">rtc_link_state</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>The correct sequence of calls is : <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv416hiprtcLinkCreatejP16hiprtcJIT_optionPPvP15hiprtcLinkState" title="hiprtcLinkCreate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcLinkCreate()</span></code></a>,
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv417hiprtcLinkAddData15hiprtcLinkState18hiprtcJITInputTypePv6size_tPKcjP16hiprtcJIT_optionPPv" title="hiprtcLinkAddData"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcLinkAddData()</span></code></a> or <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv417hiprtcLinkAddFile15hiprtcLinkState18hiprtcJITInputTypePKcjP16hiprtcJIT_optionPPv" title="hiprtcLinkAddFile"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcLinkAddFile()</span></code></a>,
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv418hiprtcLinkComplete15hiprtcLinkStatePPvP6size_t" title="hiprtcLinkComplete"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcLinkComplete()</span></code></a>, <a class="reference internal" href="../reference/hip_runtime_api/modules/module_management.html#_CPPv417hipModuleLoadDataP11hipModule_tPKv" title="hipModuleLoadData"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipModuleLoadData()</span></code></a>,
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv417hiprtcLinkDestroy15hiprtcLinkState" title="hiprtcLinkDestroy"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcLinkDestroy()</span></code></a>.</p></li>
</ul>
</div>
</section>
<section id="input-types">
<h3>Input Types<a class="headerlink" href="#input-types" title="Link to this heading">#</a></h3>
<p>HIPRTC provides <code class="docutils literal notranslate"><span class="pre">hiprtcJITInputType</span></code> enumeration type which defines the input
types accepted by the Linker APIs. Here are the <code class="docutils literal notranslate"><span class="pre">enum</span></code> values of
<code class="docutils literal notranslate"><span class="pre">hiprtcJITInputType</span></code>. However only the input types
<code class="docutils literal notranslate"><span class="pre">HIPRTC_JIT_INPUT_LLVM_BITCODE</span></code>, <code class="docutils literal notranslate"><span class="pre">HIPRTC_JIT_INPUT_LLVM_BUNDLED_BITCODE</span></code> and
<code class="docutils literal notranslate"><span class="pre">HIPRTC_JIT_INPUT_LLVM_ARCHIVES_OF_BUNDLED_BITCODE</span></code> are supported currently.</p>
<p><code class="docutils literal notranslate"><span class="pre">HIPRTC_JIT_INPUT_LLVM_BITCODE</span></code> can be used to load both LLVM bitcode or LLVM
IR assembly code. However, <code class="docutils literal notranslate"><span class="pre">HIPRTC_JIT_INPUT_LLVM_BUNDLED_BITCODE</span></code> and
<code class="docutils literal notranslate"><span class="pre">HIPRTC_JIT_INPUT_LLVM_ARCHIVES_OF_BUNDLED_BITCODE</span></code> are only for bundled
bitcode and archive of bundled bitcode.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">HIPRTC_JIT_INPUT_CUBIN</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="n">HIPRTC_JIT_INPUT_PTX</span><span class="p">,</span>
<span class="n">HIPRTC_JIT_INPUT_FATBINARY</span><span class="p">,</span>
<span class="n">HIPRTC_JIT_INPUT_OBJECT</span><span class="p">,</span>
<span class="n">HIPRTC_JIT_INPUT_LIBRARY</span><span class="p">,</span>
<span class="n">HIPRTC_JIT_INPUT_NVVM</span><span class="p">,</span>
<span class="n">HIPRTC_JIT_NUM_LEGACY_INPUT_TYPES</span><span class="p">,</span>
<span class="n">HIPRTC_JIT_INPUT_LLVM_BITCODE</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">100</span><span class="p">,</span>
<span class="n">HIPRTC_JIT_INPUT_LLVM_BUNDLED_BITCODE</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">101</span><span class="p">,</span>
<span class="n">HIPRTC_JIT_INPUT_LLVM_ARCHIVES_OF_BUNDLED_BITCODE</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">102</span><span class="p">,</span>
<span class="n">HIPRTC_JIT_NUM_INPUT_TYPES</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="n">HIPRTC_JIT_NUM_LEGACY_INPUT_TYPES</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">3</span><span class="p">)</span>
</pre></div>
</div>
</section>
<section id="backward-compatibility-of-llvm-bitcode-ir">
<h3>Backward Compatibility of LLVM Bitcode/IR<a class="headerlink" href="#backward-compatibility-of-llvm-bitcode-ir" title="Link to this heading">#</a></h3>
<p>For HIP applications utilizing HIPRTC to compile LLVM bitcode/IR, compatibility
is assured only when the ROCm or HIP SDK version used for generating the LLVM
bitcode/IR matches the version used during the runtime compilation. When an
application requires the ingestion of bitcode/IR not derived from the currently
installed AMD compiler, it must run with HIPRTC and comgr dynamic libraries that
are compatible with the version of the bitcode/IR.</p>
<p><a class="reference external" href="https://github.com/ROCm/llvm-project/tree/amd-staging/amd/comgr/README.md">Comgr</a> is a
shared library that incorporates the LLVM/Clang compiler that HIPRTC relies on.
To identify the bitcode/IR version that comgr is compatible with, one can
execute “clang -v” using the clang binary from the same ROCm or HIP SDK package.
For instance, if compiling bitcode/IR version 14, the HIPRTC and comgr libraries
released by AMD around mid 2022 would be the best choice, assuming the
LLVM/Clang version included in the package is also version 14.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>When viewing the <em>README</em> in the Comgr GitHub repository you should look at a
specific branch of interest, such as <code class="docutils literal notranslate"><span class="pre">docs/6.3.0</span></code> or <code class="docutils literal notranslate"><span class="pre">docs/6.4.1</span></code>, rather than the default branch.</p>
</div>
<p>To ensure smooth operation and compatibility, an application may choose to ship
the specific versions of HIPRTC and comgr dynamic libraries, or it may opt to
clearly specify the version requirements and dependencies. This approach
guarantees that the application can correctly compile the specified version of
bitcode/IR.</p>
</section>
<section id="link-options">
<h3>Link Options<a class="headerlink" href="#link-options" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">HIPRTC_JIT_IR_TO_ISA_OPT_EXT</span></code> - AMD Only. Options to be passed on to link
step of compiler by <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv416hiprtcLinkCreatejP16hiprtcJIT_optionPPvP15hiprtcLinkState" title="hiprtcLinkCreate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcLinkCreate()</span></code></a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIPRTC_JIT_IR_TO_ISA_OPT_COUNT_EXT</span></code> - AMD Only. Count of options passed on
to link step of compiler.</p></li>
</ul>
<p>Example:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">*</span><span class="w"> </span><span class="n">isaopts</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="s">&quot;-mllvm&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;-inline-threshold=1&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;-mllvm&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;-inlinehint-threshold=1&quot;</span><span class="p">};</span>
<span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">hiprtcJIT_option</span><span class="o">&gt;</span><span class="w"> </span><span class="n">jit_options</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="n">HIPRTC_JIT_IR_TO_ISA_OPT_EXT</span><span class="p">,</span>
<span class="w">                                            </span><span class="n">HIPRTC_JIT_IR_TO_ISA_OPT_COUNT_EXT</span><span class="p">};</span>
<span class="kt">size_t</span><span class="w"> </span><span class="n">isaoptssize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">4</span><span class="p">;</span>
<span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">lopts</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{(</span><span class="kt">void</span><span class="o">*</span><span class="p">)</span><span class="n">isaopts</span><span class="p">,</span><span class="w"> </span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="p">)(</span><span class="n">isaoptssize</span><span class="p">)};</span>
<span class="n">hiprtcLinkState</span><span class="w"> </span><span class="n">linkstate</span><span class="p">;</span>
<span class="n">hiprtcLinkCreate</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="n">jit_options</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="p">(</span><span class="kt">void</span><span class="o">**</span><span class="p">)</span><span class="n">lopts</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">linkstate</span><span class="p">);</span>
</pre></div>
</div>
</section>
</section>
<section id="error-handling">
<h2>Error Handling<a class="headerlink" href="#error-handling" title="Link to this heading">#</a></h2>
<p>HIPRTC defines the <code class="docutils literal notranslate"><span class="pre">hiprtcResult</span></code> enumeration type and a function
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcGetErrorString12hiprtcResult" title="hiprtcGetErrorString"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcGetErrorString()</span></code></a> for API call error handling. <code class="docutils literal notranslate"><span class="pre">hiprtcResult</span></code>
<code class="docutils literal notranslate"><span class="pre">enum</span></code> defines the API result codes. HIPRTC APIs return <code class="docutils literal notranslate"><span class="pre">hiprtcResult</span></code> to
indicate the call result. <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcGetErrorString12hiprtcResult" title="hiprtcGetErrorString"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcGetErrorString()</span></code></a> function returns a
string describing the given <code class="docutils literal notranslate"><span class="pre">hiprtcResult</span></code> code, for example HIPRTC_SUCCESS to
“HIPRTC_SUCCESS”. For unrecognized enumeration values, it returns
“Invalid HIPRTC error code”.</p>
<p><code class="docutils literal notranslate"><span class="pre">hiprtcResult</span></code> <code class="docutils literal notranslate"><span class="pre">enum</span></code> supported values and the
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcGetErrorString12hiprtcResult" title="hiprtcGetErrorString"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcGetErrorString()</span></code></a> usage are mentioned below.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">HIPRTC_SUCCESS</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="n">HIPRTC_ERROR_OUT_OF_MEMORY</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
<span class="n">HIPRTC_ERROR_PROGRAM_CREATION_FAILURE</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span>
<span class="n">HIPRTC_ERROR_INVALID_INPUT</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span>
<span class="n">HIPRTC_ERROR_INVALID_PROGRAM</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">4</span><span class="p">,</span>
<span class="n">HIPRTC_ERROR_INVALID_OPTION</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">5</span><span class="p">,</span>
<span class="n">HIPRTC_ERROR_COMPILATION</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">6</span><span class="p">,</span>
<span class="n">HIPRTC_ERROR_LINKING</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">7</span><span class="p">,</span>
<span class="n">HIPRTC_ERROR_BUILTIN_OPERATION_FAILURE</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">8</span><span class="p">,</span>
<span class="n">HIPRTC_ERROR_NO_NAME_EXPRESSIONS_AFTER_COMPILATION</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">9</span><span class="p">,</span>
<span class="n">HIPRTC_ERROR_NO_LOWERED_NAMES_BEFORE_COMPILATION</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">10</span><span class="p">,</span>
<span class="n">HIPRTC_ERROR_NAME_EXPRESSION_NOT_VALID</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">11</span><span class="p">,</span>
<span class="n">HIPRTC_ERROR_INTERNAL_ERROR</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">12</span>
</pre></div>
</div>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hiprtcResult</span><span class="w"> </span><span class="n">result</span><span class="p">;</span>
<span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hiprtcCompileProgram</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">opts</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">result</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">HIPRTC_SUCCESS</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;hiprtcCompileProgram fails with error &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hiprtcGetErrorString</span><span class="p">(</span><span class="n">result</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="hiprtc-general-apis">
<h2>HIPRTC General APIs<a class="headerlink" href="#hiprtc-general-apis" title="Link to this heading">#</a></h2>
<p>HIPRTC provides <code class="docutils literal notranslate"><span class="pre">hiprtcVersion(int*</span> <span class="pre">major,</span> <span class="pre">int*</span> <span class="pre">minor)</span></code> for querying the
version. This sets the output parameters major and minor with the HIP Runtime
compilation major version and minor version number respectively.</p>
<p>Currently, it returns hardcoded values. This should be implemented to return HIP
runtime major and minor version in the future releases.</p>
</section>
<section id="lowered-names-mangled-names">
<h2>Lowered Names (Mangled Names)<a class="headerlink" href="#lowered-names-mangled-names" title="Link to this heading">#</a></h2>
<p>HIPRTC mangles the <code class="docutils literal notranslate"><span class="pre">__global__</span></code> function names and names of <code class="docutils literal notranslate"><span class="pre">__device__</span></code> and
<code class="docutils literal notranslate"><span class="pre">__constant__</span></code> variables. If the generated binary is being loaded using the
HIP Runtime API, the kernel function or <code class="docutils literal notranslate"><span class="pre">__device__/__constant__</span></code> variable
must be looked up by name, but this is very hard when the name has been mangled.
To overcome this, HIPRTC provides API functions that map <code class="docutils literal notranslate"><span class="pre">__global__</span></code> function
or <code class="docutils literal notranslate"><span class="pre">__device__/__constant__</span></code> variable names in the source to the mangled names
present in the generated binary.</p>
<p>The two APIs <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv423hiprtcAddNameExpression13hiprtcProgramPKc" title="hiprtcAddNameExpression"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcAddNameExpression()</span></code></a> and
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcGetLoweredName13hiprtcProgramPKcPPKc" title="hiprtcGetLoweredName"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcGetLoweredName()</span></code></a> provide this functionality. First, a ‘name
expression’ string denoting the address for the <code class="docutils literal notranslate"><span class="pre">__global__</span></code> function or
<code class="docutils literal notranslate"><span class="pre">__device__/__constant__</span></code> variable is provided to
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv423hiprtcAddNameExpression13hiprtcProgramPKc" title="hiprtcAddNameExpression"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcAddNameExpression()</span></code></a>. Then, the program is compiled with
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv419hiprtcCreateProgramP13hiprtcProgramPKcPKciPPCKcPPCKc" title="hiprtcCreateProgram"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcCreateProgram()</span></code></a>. During compilation, HIPRTC will parse the name
expression string as a C++ constant expression at the end of the user program.
Finally, the function <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcGetLoweredName13hiprtcProgramPKcPPKc" title="hiprtcGetLoweredName"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcGetLoweredName()</span></code></a> is called with the
original name expression and it returns a pointer to the lowered name. The
lowered name can be used to refer to the kernel or variable in the HIP Runtime
API.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p>The identical name expression string must be provided on a subsequent call
to <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcGetLoweredName13hiprtcProgramPKcPPKc" title="hiprtcGetLoweredName"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcGetLoweredName()</span></code></a> to extract the lowered name.</p></li>
<li><p>The correct sequence of calls is : <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv423hiprtcAddNameExpression13hiprtcProgramPKc" title="hiprtcAddNameExpression"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcAddNameExpression()</span></code></a>,
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv419hiprtcCreateProgramP13hiprtcProgramPKcPKciPPCKcPPCKc" title="hiprtcCreateProgram"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcCreateProgram()</span></code></a>, <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcGetLoweredName13hiprtcProgramPKcPPKc" title="hiprtcGetLoweredName"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcGetLoweredName()</span></code></a>,
<a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcDestroyProgramP13hiprtcProgram" title="hiprtcDestroyProgram"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcDestroyProgram()</span></code></a>.</p></li>
<li><p>The lowered names must be fetched using <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcGetLoweredName13hiprtcProgramPKcPPKc" title="hiprtcGetLoweredName"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcGetLoweredName()</span></code></a>
only after the HIPRTC program has been compiled, and before it has been
destroyed.</p></li>
</ul>
</div>
<section id="id1">
<h3>Example<a class="headerlink" href="#id1" title="Link to this heading">#</a></h3>
<p>Kernel containing various definitions <code class="docutils literal notranslate"><span class="pre">__global__</span></code> functions/function
templates and <code class="docutils literal notranslate"><span class="pre">__device__/__constant__</span></code> variables can be stored in a string.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">static</span><span class="w"> </span><span class="k">constexpr</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="w"> </span><span class="n">gpu_program</span><span class="p">[]</span><span class="w"> </span><span class="p">{</span>
<span class="sa">R</span><span class="s">&quot;</span><span class="dl">(</span>
<span class="s">__device__ int V1; // set from host code</span>
<span class="s">static __global__ void f1(int *result) { *result = V1 + 10; }</span>
<span class="s">namespace N1 {</span>
<span class="s">namespace N2 {</span>
<span class="s">__constant__ int V2; // set from host code</span>
<span class="s">__global__ void f2(int *result) { *result = V2 + 20; }</span>
<span class="s">}</span>
<span class="s">}</span>
<span class="s">template&lt;typename T&gt;</span>
<span class="s">__global__ void f3(int *result) { *result = sizeof(T); }</span>
<span class="dl">)</span><span class="s">&quot;</span><span class="p">};</span>
</pre></div>
</div>
<p><a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv423hiprtcAddNameExpression13hiprtcProgramPKc" title="hiprtcAddNameExpression"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcAddNameExpression()</span></code></a> is called with various name expressions
referring to the address of <code class="docutils literal notranslate"><span class="pre">__global__</span></code> functions and
<code class="docutils literal notranslate"><span class="pre">__device__/__constant__</span></code> variables.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">kernel_name_vec</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="s">&quot;&amp;f1&quot;</span><span class="p">);</span>
<span class="n">kernel_name_vec</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="s">&quot;N1::N2::f2&quot;</span><span class="p">);</span>
<span class="n">kernel_name_vec</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="s">&quot;f3&lt;int&gt;&quot;</span><span class="p">);</span>
<span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="k">auto</span><span class="o">&amp;&amp;</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">kernel_name_vec</span><span class="p">)</span><span class="w"> </span><span class="n">hiprtcAddNameExpression</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="n">x</span><span class="p">.</span><span class="n">c_str</span><span class="p">());</span>
<span class="n">variable_name_vec</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="s">&quot;&amp;V1&quot;</span><span class="p">);</span>
<span class="n">variable_name_vec</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="s">&quot;&amp;N1::N2::V2&quot;</span><span class="p">);</span>
<span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="k">auto</span><span class="o">&amp;&amp;</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="n">variable_name_vec</span><span class="p">)</span><span class="w"> </span><span class="n">hiprtcAddNameExpression</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="n">x</span><span class="p">.</span><span class="n">c_str</span><span class="p">());</span>
</pre></div>
</div>
<p>After which, the program is compiled using <a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html#_CPPv420hiprtcCompileProgram13hiprtcProgramiPPCKc" title="hiprtcCompileProgram"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hiprtcCompileProgram()</span></code></a>, the
generated binary is loaded using <a class="reference internal" href="../reference/hip_runtime_api/modules/module_management.html#_CPPv417hipModuleLoadDataP11hipModule_tPKv" title="hipModuleLoadData"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipModuleLoadData()</span></code></a>, and the mangled
names can be fetched using <code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hirtcGetLoweredName()</span></code>.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="k">decltype</span><span class="p">(</span><span class="n">variable_name_vec</span><span class="p">.</span><span class="n">size</span><span class="p">())</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">variable_name_vec</span><span class="p">.</span><span class="n">size</span><span class="p">();</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">*</span><span class="w"> </span><span class="n">name</span><span class="p">;</span>
<span class="w">  </span><span class="n">hiprtcGetLoweredName</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="n">variable_name_vec</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">c_str</span><span class="p">(),</span><span class="w"> </span><span class="o">&amp;</span><span class="n">name</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="k">decltype</span><span class="p">(</span><span class="n">kernel_name_vec</span><span class="p">.</span><span class="n">size</span><span class="p">())</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">kernel_name_vec</span><span class="p">.</span><span class="n">size</span><span class="p">();</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">*</span><span class="w"> </span><span class="n">name</span><span class="p">;</span>
<span class="w">  </span><span class="n">hiprtcGetLoweredName</span><span class="p">(</span><span class="n">prog</span><span class="p">,</span><span class="w"> </span><span class="n">kernel_name_vec</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">c_str</span><span class="p">(),</span><span class="w"> </span><span class="o">&amp;</span><span class="n">name</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p>The mangled name of the variables are used to look up the variable in the module
and update its value.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipDeviceptr_t</span><span class="w"> </span><span class="n">variable_addr</span><span class="p">;</span>
<span class="kt">size_t</span><span class="w"> </span><span class="n">bytes</span><span class="p">{};</span>
<span class="n">hipModuleGetGlobal</span><span class="p">(</span><span class="o">&amp;</span><span class="n">variable_addr</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">bytes</span><span class="p">,</span><span class="w"> </span><span class="k">module</span><span class="p">,</span><span class="w"> </span><span class="n">name</span><span class="p">);</span>
<span class="n">hipMemcpyHtoD</span><span class="p">(</span><span class="n">variable_addr</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">initial_value</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">initial_value</span><span class="p">));</span>
</pre></div>
</div>
<p>Finally, the mangled name of the kernel is used to launch it using the
<code class="docutils literal notranslate"><span class="pre">hipModule</span></code> APIs.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipFunction_t</span><span class="w"> </span><span class="n">kernel</span><span class="p">;</span>
<span class="n">hipModuleGetFunction</span><span class="p">(</span><span class="o">&amp;</span><span class="n">kernel</span><span class="p">,</span><span class="w"> </span><span class="k">module</span><span class="p">,</span><span class="w"> </span><span class="n">name</span><span class="p">);</span>
<span class="n">hipModuleLaunchKernel</span><span class="p">(</span><span class="n">kernel</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="n">config</span><span class="p">);</span>
</pre></div>
</div>
<p>For a detailed example, refer to <a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/amd-staging/HIP-Doc/Programming-Guide/Programming-for-HIP-Runtime-Compiler/lowered_names">lowered_names</a> in <a class="reference external" href="https://github.com/ROCm/rocm-examples">rocm_examples</a>.</p>
</section>
</section>
<section id="versioning">
<h2>Versioning<a class="headerlink" href="#versioning" title="Link to this heading">#</a></h2>
<p>HIPRTC uses the following versioning:</p>
<ul class="simple">
<li><p>Linux</p>
<ul>
<li><p>HIPRTC follows the same versioning as HIP runtime library.</p></li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">so</span></code> name field for the shared library is set to MAJOR version. For
example, for HIP 5.3 the <code class="docutils literal notranslate"><span class="pre">so</span></code> name is set to 5 (<code class="docutils literal notranslate"><span class="pre">hiprtc.so.5</span></code>).</p></li>
</ul>
</li>
<li><p>Windows</p>
<ul>
<li><p>HIPRTC dll is named as <code class="docutils literal notranslate"><span class="pre">hiprtcXXYY.dll</span></code> where <code class="docutils literal notranslate"><span class="pre">XX</span></code> is MAJOR version and
<code class="docutils literal notranslate"><span class="pre">YY</span></code> is MINOR version. For example, for HIP 5.3 the name is
<code class="docutils literal notranslate"><span class="pre">hiprtc0503.dll</span></code>.</p></li>
</ul>
</li>
</ul>
</section>
<section id="hip-header-support">
<h2>HIP header support<a class="headerlink" href="#hip-header-support" title="Link to this heading">#</a></h2>
<p>Added HIPRTC support for all the hip common header files such as
<code class="docutils literal notranslate"><span class="pre">library_types.h</span></code>, <code class="docutils literal notranslate"><span class="pre">hip_math_constants.h</span></code>, <code class="docutils literal notranslate"><span class="pre">hip_complex.h</span></code>,
<code class="docutils literal notranslate"><span class="pre">math_functions.h</span></code>, <code class="docutils literal notranslate"><span class="pre">surface_types.h</span></code> etc. from 6.1. HIPRTC users need not
include any HIP macros or constants explicitly in their header files. All of
these should get included via HIPRTC builtins when the app links to HIPRTC
library.</p>
</section>
<section id="deprecation-notice">
<h2>Deprecation notice<a class="headerlink" href="#deprecation-notice" title="Link to this heading">#</a></h2>
<ul class="simple">
<li><p>Currently HIPRTC APIs are separated from HIP APIs and HIPRTC is available as a
separate library <code class="docutils literal notranslate"><span class="pre">libhiprtc.so</span></code>/ <code class="docutils literal notranslate"><span class="pre">libhiprtc.dll</span></code>. But on Linux, HIPRTC
symbols are also present in <code class="docutils literal notranslate"><span class="pre">libamdhip64.so</span></code> in order to support the
existing applications. Gradually, these symbols will be removed from HIP
library and applications using HIPRTC will be required to explicitly link to
HIPRTC library. However, on Windows <code class="docutils literal notranslate"><span class="pre">hiprtc.dll</span></code> must be used as the
<code class="docutils literal notranslate"><span class="pre">amdhip64.dll</span></code> doesn’t contain the HIPRTC symbols.</p></li>
<li><p>Data types such as <code class="docutils literal notranslate"><span class="pre">uint32_t</span></code>, <code class="docutils literal notranslate"><span class="pre">uint64_t</span></code>, <code class="docutils literal notranslate"><span class="pre">int32_t</span></code>, <code class="docutils literal notranslate"><span class="pre">int64_t</span></code>
defined in std namespace in HIPRTC are deprecated earlier and are being
removed from ROCm release 6.1 since these can conflict with the standard
C++ data types. These data types are now prefixed with <code class="docutils literal notranslate"><span class="pre">__hip__</span></code>, for example
<code class="docutils literal notranslate"><span class="pre">__hip_uint32_t</span></code>. Applications previously using <code class="docutils literal notranslate"><span class="pre">std::uint32_t</span></code> or similar
types can use <code class="docutils literal notranslate"><span class="pre">__hip_</span></code> prefixed types to avoid conflicts with standard std
namespace or application can have their own definitions for these types. Also,
type_traits templates previously defined in std namespace are moved to
<code class="docutils literal notranslate"><span class="pre">__hip_internal</span></code> namespace as implementation details.</p></li>
</ul>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="hip_porting_guide.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Porting CUDA code to HIP</p>
      </div>
    </a>
    <a class="right-next"
       href="../understand/amd_clr.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">AMD compute language runtimes (CLR)</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#compilation-apis">Compilation APIs</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hiprtc-specific-options">HIPRTC specific options</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#bitcode">Bitcode</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#cu-mode-vs-wgp-mode">CU mode vs WGP mode</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#linker-apis">Linker APIs</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#example">Example</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#input-types">Input Types</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#backward-compatibility-of-llvm-bitcode-ir">Backward Compatibility of LLVM Bitcode/IR</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#link-options">Link Options</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#error-handling">Error Handling</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hiprtc-general-apis">HIPRTC General APIs</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#lowered-names-mangled-names">Lowered Names (Mangled Names)</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">Example</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#versioning">Versioning</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-header-support">HIP header support</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#deprecation-notice">Deprecation notice</a></li>
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
