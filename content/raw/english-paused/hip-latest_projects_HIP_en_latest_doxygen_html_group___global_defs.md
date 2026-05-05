---
title: "HIP Runtime API Reference: Global enum and defines &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___global_defs.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:05.596205+00:00
content_hash: "ff9ab2011cd6e9f7"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>HIP Runtime API Reference: Global enum and defines &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
  <script data-cfasync="false">
    document.documentElement.dataset.mode = localStorage.getItem("mode") || "";
    document.documentElement.dataset.theme = localStorage.getItem("theme") || "";
  </script>
  
  <!-- Loaded before other Sphinx assets -->
  <link href="../../_static/styles/theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../../_static/styles/bootstrap.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../../_static/styles/pydata-sphinx-theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />

  
  <link href="../../_static/vendor/fontawesome/6.5.2/css/all.min.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
  <link rel="preload" as="font" type="font/woff2" crossorigin href="../../_static/vendor/fontawesome/6.5.2/webfonts/fa-solid-900.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../_static/vendor/fontawesome/6.5.2/webfonts/fa-brands-400.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../_static/vendor/fontawesome/6.5.2/webfonts/fa-regular-400.woff2" />

    <link rel="stylesheet" type="text/css" href="../../_static/pygments.css?v=a746c00c" />
    <link rel="stylesheet" type="text/css" href="../../_static/styles/sphinx-book-theme.css?v=a3416100" />
    <link rel="stylesheet" type="text/css" href="../../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
    <link rel="stylesheet" type="text/css" href="../../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../../_static/sphinx-design.min.css?v=95c83b7e" />
    <link rel="stylesheet" type="text/css" href="../../_static/rocm_custom.css?v=35d74aab" />
  
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b" />
<link rel="preload" as="script" href="../../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b" />
  <script src="../../_static/vendor/fontawesome/6.5.2/js/all.min.js?digest=dfe6caa3a7d634c4db9b"></script>

    <script src="../../_static/documentation_options.js?v=75144bb1"></script>
    <script src="../../_static/doctools.js?v=9a2dae69"></script>
    <script src="../../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../../_static/search.js?v=90a4452c"></script>
    <script src="../../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
    <script src="../../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/html/group___global_defs';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="Driver Types" href="group___driver_types.html" />
    <link rel="prev" title="Global defines, enums, structs and files" href="../../reference/hip_runtime_api/global_defines_enums_structs_files.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/group___global_defs.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
      action="../../search.html"
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
                    <img src="../../_static/images/amd-header-logo.svg" alt="AMD Logo" title="AMD Logo" width="90" class="d-inline-block align-text-top hover-opacity"/>
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

  
    
  

<a class="navbar-brand logo" href="../../index.html">
  
  
  
  
  
  
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
<li class="toctree-l1"><a class="reference internal" href="../../what_is_hip.html">What is HIP?</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../hip-7-changes.html">HIP API 7.0 changes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../faq.html">Frequently asked questions</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../install/install.html">Installing HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../install/build.html">Building HIP from source</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Programming guide</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../understand/programming_model.html">Introduction to the HIP programming model</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../understand/performance_optimization.html">Understanding GPU performance</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../understand/hardware_implementation.html">Hardware implementation</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../understand/compilers.html">HIP compilers</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../how-to/performance_guidelines.html">Performance guidelines</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../how-to/debugging.html">Debugging with HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../how-to/logging.html">Logging HIP activity</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../../how-to/hip_runtime_api.html">Using HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../../how-to/hip_runtime_api/initialization.html">Initialization</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../../how-to/hip_runtime_api/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../how-to/hip_runtime_api/memory_management/host_memory.html">Host memory</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../../how-to/hip_runtime_api/memory_management/device_memory.html">Device memory</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../../how-to/hip_runtime_api/memory_management/device_memory/texture_fetching.html">Texture fetching</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="../../how-to/hip_runtime_api/memory_management/coherence_control.html">Coherence control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../how-to/hip_runtime_api/memory_management/unified_memory.html">Unified memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../how-to/hip_runtime_api/memory_management/virtual_memory.html">Virtual memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../how-to/hip_runtime_api/memory_management/stream_ordered_allocator.html">Stream Ordered Memory Allocator</a></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="../../how-to/hip_runtime_api/error_handling.html">Error handling</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../how-to/hip_runtime_api/call_stack.html">Call stack</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../how-to/hip_runtime_api/asynchronous.html">Asynchronous concurrent execution</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../how-to/hip_runtime_api/hipgraph.html">HIP graphs</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../how-to/hip_runtime_api/cooperative_groups.html">Cooperative groups</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../how-to/hip_runtime_api/multi_device.html">Multi-device management</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../how-to/hip_runtime_api/opengl_interop.html">OpenGL interoperability</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../how-to/hip_runtime_api/external_interop.html">External resource interoperability</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../how-to/hip_cpp_language_extensions.html">HIP C++ language extensions</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../how-to/kernel_language_cpp_support.html">Kernel language C++ support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../how-to/hip_porting_guide.html">Porting CUDA code to HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../how-to/hip_rtc.html">Programming for HIP runtime compiler (RTC)</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../understand/amd_clr.html">AMD compute language runtimes (CLR)</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active has-children"><a class="reference internal" href="../../reference/hip_runtime_api_reference.html">HIP runtime API</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2 has-children"><a class="reference internal" href="../../reference/hip_runtime_api/modules.html">Modules</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/initialization_and_version.html">Initialization and version</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/device_management.html">Device management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/execution_control.html">Execution control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/error_handling.html">Error handling</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/stream_management.html">Stream management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/stream_memory_operations.html">Stream memory operations</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/event_management.html">Event management</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/memory_management_deprecated.html">Memory management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/external_resource_interoperability.html">External resource interoperability</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html">Stream ordered memory allocator</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html">Managed memory</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html">Virtual memory management</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/texture_management.html">Texture management</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/texture_management_deprecated.html">Texture management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/surface_object.html">Surface object</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/peer_to_peer_device_memory_access.html">Peer to peer device memory access</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/context_management.html">Context management [deprecated]</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/module_management.html">Module management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/occupancy.html">Occupancy</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/profiler_control.html">Profiler control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/launch_api.html">Launch API</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/runtime_compilation.html">Runtime compilation</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/callback_activity_apis.html">Callback activity APIs</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html">Graph management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/graphics_interoperability.html">Graphics interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/opengl_interoperability.html">OpenGL interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/cooperative_groups_reference.html">Cooperative groups</a></li>
</ul>
</details></li>
<li class="toctree-l2 current active has-children"><a class="reference internal" href="../../reference/hip_runtime_api/global_defines_enums_structs_files.html">Global defines, enums, structs and files</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Global enum and defines</a></li>
<li class="toctree-l3"><a class="reference internal" href="group___driver_types.html">Driver Types</a></li>
<li class="toctree-l3"><a class="reference internal" href="annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="files.html">File List</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/math_api.html">HIP math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/complex_math_api.html">HIP complex math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/env_variables.html">HIP environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/error_codes.html">HIP error codes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/api_syntax.html">CUDA to HIP API Function Comparison</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/deprecated_api_list.html">List of deprecated APIs</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/low_fp_types.html">Low Precision Floating Point Types</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/hardware_features.html">Hardware features</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Tutorials</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic">HIP basic examples</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples">HIP examples</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../tutorial/saxpy.html">SAXPY - Hello, HIP</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../../tutorial/programming-patterns.html">GPU programming patterns</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../../tutorial/programming-patterns/matrix_multiplication.html">Two-dimensional kernels: Matrix multiplication tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../tutorial/programming-patterns/atomic_operations_histogram.html">Atomic operations: Histogram tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../tutorial/programming-patterns/cpu_gpu_kmeans.html">CPU-GPU cooperative computing: K-means clustering tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../tutorial/programming-patterns/stencil_operations.html">Stencil operations: Image convolution tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../tutorial/programming-patterns/multikernel_bfs.html">Multi-kernel programming: breadth-first search tutorial</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../tutorial/reduction.html">Reduction</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../tutorial/cooperative_groups_tutorial.html">Cooperative groups</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../tutorial/graph_api.html">HIP Graph API Tutorial</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">About</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../license.html">License</a></li>
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
      <a href="../../index.html" class="nav-link" aria-label="Home">
        <i class="fa-solid fa-home"></i>
      </a>
    </li>
    
    <li class="breadcrumb-item"><a href="../../reference/hip_runtime_api_reference.html" class="nav-link">HIP runtime API</a></li>
    
    
    <li class="breadcrumb-item"><a href="../../reference/hip_runtime_api/global_defines_enums_structs_files.html" class="nav-link">Global defines, enums, structs and files</a></li>
    
    <li class="breadcrumb-item active" aria-current="page">HIP Runtime...</li>
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
    <h1>Global enum and defines</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="global-enum-and-defines">
<h1>Global enum and defines<a class="headerlink" href="#global-enum-and-defines" title="Link to this heading">#</a></h1>
<div class="doxygen-content docutils container">
<!-- HTML header for doxygen 1.9.6-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>HIP Runtime API Reference: Global enum and defines</title>
<link href="tabs.css" rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="dynsections.js"></script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  extensions: ["tex2jax.js"],
  jax: ["input/TeX","output/HTML-CSS"],
});
</script>
<script type="text/javascript" async="async" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js"></script>
<link href="doxygen.css" rel="stylesheet" type="text/css" />
<link href="extra_stylesheet.css" rel="stylesheet" type="text/css"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/group___global_defs.html" /><meta name="readthedocs-http-status" content="200" /></head>
<body>
<div id="top"><!-- do not remove this div, it is closed by doxygen! -->
<!-- Generated by Doxygen 1.9.8 -->
<script type="text/javascript" src="menudata.js"></script>
<script type="text/javascript" src="menu.js"></script>
<script type="text/javascript">
/* @license magnet:?xt=urn:btih:d3d9a9a6595521f9666a5e94cc830dab83b65699&amp;dn=expat.txt MIT */
$(function() {
  initMenu('',false,false,'search.php','Search');
});
/* @license-end */
</script>
<div id="main-nav"></div>
</div><!-- top -->
<div class="header">
  <div class="summary">
<a href="#namespaces">Namespaces</a> &#124;
<a href="#nested-classes">Data Structures</a> &#124;
<a href="#define-members">Macros</a> &#124;
<a href="#typedef-members">Typedefs</a> &#124;
<a href="#enum-members">Enumerations</a>  </div>
  <div class="headertitle"><div class="title">Global enum and defines</div></div>
</div><!--header-->
<div class="contents">
<table class="memberdecls">
<tr class="heading"><td colspan="2"><h2 class="groupheader"><a id="namespaces" name="namespaces"></a>
Namespaces</h2></td></tr>
<tr class="memitem:namespacehip__impl" id="r_namespacehip__impl"><td class="memItemLeft" align="right" valign="top">namespace &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="namespacehip__impl.html">hip_impl</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
</table><table class="memberdecls">
<tr class="heading"><td colspan="2"><h2 class="groupheader"><a id="nested-classes" name="nested-classes"></a>
Data Structures</h2></td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_device_arch__t.html">hipDeviceArch_t</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_u_u_i_d.html">hipUUID</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_device_prop__t.html">hipDeviceProp_t</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_pointer_attribute__t.html">hipPointerAttribute_t</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_ipc_mem_handle__t.html">hipIpcMemHandle_t</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_ipc_event_handle__t.html">hipIpcEventHandle_t</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_func_attributes.html">hipFuncAttributes</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">union &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="unionhip_stream_batch_mem_op_params.html">hipStreamBatchMemOpParams</a></td></tr>
<tr class="memdesc:"><td class="mdescLeft">&#160;</td><td class="mdescRight">Union representing batch memory operation parameters for HIP streams.  <a href="unionhip_stream_batch_mem_op_params.html#details">More...</a><br /></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_batch_mem_op_node_params.html">hipBatchMemOpNodeParams</a></td></tr>
<tr class="memdesc:"><td class="mdescLeft">&#160;</td><td class="mdescRight">Structure representing node parameters for batch memory operations in HIP graphs.  <a href="structhip_batch_mem_op_node_params.html#details">More...</a><br /></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_mem_access_desc.html">hipMemAccessDesc</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_mem_pool_props.html">hipMemPoolProps</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_mem_pool_ptr_export_data.html">hipMemPoolPtrExportData</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structdim3.html">dim3</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_launch_params.html">hipLaunchParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_function_launch_params.html">hipFunctionLaunchParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_external_memory_handle_desc.html">hipExternalMemoryHandleDesc</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_external_memory_buffer_desc.html">hipExternalMemoryBufferDesc</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_external_memory_mipmapped_array_desc.html">hipExternalMemoryMipmappedArrayDesc</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_external_semaphore_handle_desc.html">hipExternalSemaphoreHandleDesc</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_external_semaphore_signal_params.html">hipExternalSemaphoreSignalParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_external_semaphore_wait_params.html">hipExternalSemaphoreWaitParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_host_node_params.html">hipHostNodeParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_kernel_node_params.html">hipKernelNodeParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_memset_params.html">hipMemsetParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_mem_alloc_node_params.html">hipMemAllocNodeParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_access_policy_window.html">hipAccessPolicyWindow</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_launch_mem_sync_domain_map.html">hipLaunchMemSyncDomainMap</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">union &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="unionhip_launch_attribute_value.html">hipLaunchAttributeValue</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_graph_instantiate_params.html">hipGraphInstantiateParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_mem_allocation_prop.html">hipMemAllocationProp</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_external_semaphore_signal_node_params.html">hipExternalSemaphoreSignalNodeParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_external_semaphore_wait_node_params.html">hipExternalSemaphoreWaitNodeParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_array_map_info.html">hipArrayMapInfo</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_memcpy_node_params.html">hipMemcpyNodeParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_child_graph_node_params.html">hipChildGraphNodeParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_event_wait_node_params.html">hipEventWaitNodeParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_event_record_node_params.html">hipEventRecordNodeParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_mem_free_node_params.html">hipMemFreeNodeParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_graph_node_params.html">hipGraphNodeParams</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_graph_edge_data.html">hipGraphEdgeData</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_launch_attribute.html">hipLaunchAttribute</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_launch_config__t.html">hipLaunchConfig_t</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="struct_h_i_p___l_a_u_n_c_h___c_o_n_f_i_g.html">HIP_LAUNCH_CONFIG</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
</table><table class="memberdecls">
<tr class="heading"><td colspan="2"><h2 class="groupheader"><a id="define-members" name="define-members"></a>
Macros</h2></td></tr>
<tr class="memitem:gacf5d42474f220210d9769beacd060720" id="r_gacf5d42474f220210d9769beacd060720"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gacf5d42474f220210d9769beacd060720">hipGetDeviceProperties</a>&#160;&#160;&#160;hipGetDevicePropertiesR0600</td></tr>
<tr class="separator:gacf5d42474f220210d9769beacd060720"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaa00e004b6ede756d50d4eae0ca2b0330" id="r_gaa00e004b6ede756d50d4eae0ca2b0330"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaa00e004b6ede756d50d4eae0ca2b0330">hipDeviceProp_t</a>&#160;&#160;&#160;hipDeviceProp_tR0600</td></tr>
<tr class="separator:gaa00e004b6ede756d50d4eae0ca2b0330"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga77ce8fe6c05ed444d6a7fc769917dc93" id="r_ga77ce8fe6c05ed444d6a7fc769917dc93"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga77ce8fe6c05ed444d6a7fc769917dc93">hipChooseDevice</a>&#160;&#160;&#160;hipChooseDeviceR0600</td></tr>
<tr class="separator:ga77ce8fe6c05ed444d6a7fc769917dc93"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga89716f0e21b750a51ceb081208a84b33" id="r_ga89716f0e21b750a51ceb081208a84b33"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga89716f0e21b750a51ceb081208a84b33">__HIP_NODISCARD</a></td></tr>
<tr class="separator:ga89716f0e21b750a51ceb081208a84b33"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga9a93afd2ec3f43ce2612feb962c67ced" id="r_ga9a93afd2ec3f43ce2612feb962c67ced"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga9a93afd2ec3f43ce2612feb962c67ced">GENERIC_GRID_LAUNCH</a>&#160;&#160;&#160;1</td></tr>
<tr class="separator:ga9a93afd2ec3f43ce2612feb962c67ced"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gad6f100bd2ecab24ac448506698cba686" id="r_gad6f100bd2ecab24ac448506698cba686"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gad6f100bd2ecab24ac448506698cba686">HIP_DEPRECATED</a>(msg)&#160;&#160;&#160;__attribute__((deprecated(msg)))</td></tr>
<tr class="separator:gad6f100bd2ecab24ac448506698cba686"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga3f6fb51f33c412366ee1c42e34e71a05" id="r_ga3f6fb51f33c412366ee1c42e34e71a05"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga3f6fb51f33c412366ee1c42e34e71a05">HIP_DEPRECATED_MSG</a></td></tr>
<tr class="separator:ga3f6fb51f33c412366ee1c42e34e71a05"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gab78d63242f906b6d92cf766bd88a1898" id="r_gab78d63242f906b6d92cf766bd88a1898"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gab78d63242f906b6d92cf766bd88a1898">HIP_LAUNCH_PARAM_BUFFER_POINTER</a>&#160;&#160;&#160;((void*)0x01)</td></tr>
<tr class="separator:gab78d63242f906b6d92cf766bd88a1898"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga529edcc8dc562e3f6f6c6d17bf868f03" id="r_ga529edcc8dc562e3f6f6c6d17bf868f03"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga529edcc8dc562e3f6f6c6d17bf868f03">HIP_LAUNCH_PARAM_BUFFER_SIZE</a>&#160;&#160;&#160;((void*)0x02)</td></tr>
<tr class="separator:ga529edcc8dc562e3f6f6c6d17bf868f03"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga86cd80c0b352a6679a7fac89e026f0f7" id="r_ga86cd80c0b352a6679a7fac89e026f0f7"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga86cd80c0b352a6679a7fac89e026f0f7">HIP_LAUNCH_PARAM_END</a>&#160;&#160;&#160;((void*)0x03)</td></tr>
<tr class="separator:ga86cd80c0b352a6679a7fac89e026f0f7"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga0f49b614c87c5d703133fbc52fc68670" id="r_ga0f49b614c87c5d703133fbc52fc68670"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga0f49b614c87c5d703133fbc52fc68670">__dparm</a>(x)&#160;&#160;&#160;= x</td></tr>
<tr class="separator:ga0f49b614c87c5d703133fbc52fc68670"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaa6226e5fe180a7a8da048f53a5baaf45" id="r_gaa6226e5fe180a7a8da048f53a5baaf45"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaa6226e5fe180a7a8da048f53a5baaf45">hipIpcMemLazyEnablePeerAccess</a>&#160;&#160;&#160;0x01</td></tr>
<tr class="separator:gaa6226e5fe180a7a8da048f53a5baaf45"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaf095c042450b241001894e1578d71acd" id="r_gaf095c042450b241001894e1578d71acd"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaf095c042450b241001894e1578d71acd">HIP_IPC_HANDLE_SIZE</a>&#160;&#160;&#160;64</td></tr>
<tr class="separator:gaf095c042450b241001894e1578d71acd"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga6df5f70eb976836ab3598cacf0ffcdf9" id="r_ga6df5f70eb976836ab3598cacf0ffcdf9"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga6df5f70eb976836ab3598cacf0ffcdf9">hipStreamDefault</a>&#160;&#160;&#160;0x00</td></tr>
<tr class="separator:ga6df5f70eb976836ab3598cacf0ffcdf9"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaaba9ae995d9b43b7d1ee70c6fa12c57d" id="r_gaaba9ae995d9b43b7d1ee70c6fa12c57d"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaaba9ae995d9b43b7d1ee70c6fa12c57d">hipStreamNonBlocking</a>&#160;&#160;&#160;0x01</td></tr>
<tr class="separator:gaaba9ae995d9b43b7d1ee70c6fa12c57d"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga122a5853359eba97cf047ddd153740f0" id="r_ga122a5853359eba97cf047ddd153740f0"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga122a5853359eba97cf047ddd153740f0">hipEventDefault</a>&#160;&#160;&#160;0x0</td></tr>
<tr class="separator:ga122a5853359eba97cf047ddd153740f0"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gafa1c076a5b991763a98695063f1ea11d" id="r_gafa1c076a5b991763a98695063f1ea11d"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gafa1c076a5b991763a98695063f1ea11d">hipEventBlockingSync</a>&#160;&#160;&#160;0x1</td></tr>
<tr class="separator:gafa1c076a5b991763a98695063f1ea11d"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga3c0f44a85e36a4c67671da6bcdad0351" id="r_ga3c0f44a85e36a4c67671da6bcdad0351"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga3c0f44a85e36a4c67671da6bcdad0351">hipEventDisableTiming</a>&#160;&#160;&#160;0x2</td></tr>
<tr class="separator:ga3c0f44a85e36a4c67671da6bcdad0351"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga0f01d74059baa704e42aeff8222166bb" id="r_ga0f01d74059baa704e42aeff8222166bb"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga0f01d74059baa704e42aeff8222166bb">hipEventInterprocess</a>&#160;&#160;&#160;0x4</td></tr>
<tr class="separator:ga0f01d74059baa704e42aeff8222166bb"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga89c797f8db87adb1cba32b2ecd4cd10a" id="r_ga89c797f8db87adb1cba32b2ecd4cd10a"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga89c797f8db87adb1cba32b2ecd4cd10a">hipEventRecordDefault</a>&#160;&#160;&#160;0x00</td></tr>
<tr class="separator:ga89c797f8db87adb1cba32b2ecd4cd10a"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga4ba32143914d35954ebc5d1c9aea1240" id="r_ga4ba32143914d35954ebc5d1c9aea1240"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga4ba32143914d35954ebc5d1c9aea1240">hipEventRecordExternal</a>&#160;&#160;&#160;0x01</td></tr>
<tr class="separator:ga4ba32143914d35954ebc5d1c9aea1240"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga6f2ee7919aec28aba79174d4a507a845" id="r_ga6f2ee7919aec28aba79174d4a507a845"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga6f2ee7919aec28aba79174d4a507a845">hipEventWaitDefault</a>&#160;&#160;&#160;0x00</td></tr>
<tr class="separator:ga6f2ee7919aec28aba79174d4a507a845"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gad255a5b010e6cde0d04de5a1ebe9191c" id="r_gad255a5b010e6cde0d04de5a1ebe9191c"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gad255a5b010e6cde0d04de5a1ebe9191c">hipEventWaitExternal</a>&#160;&#160;&#160;0x01</td></tr>
<tr class="separator:gad255a5b010e6cde0d04de5a1ebe9191c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga0e9ec830fe53ed7a24a8b96da15f4f12" id="r_ga0e9ec830fe53ed7a24a8b96da15f4f12"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga0e9ec830fe53ed7a24a8b96da15f4f12">hipEventDisableSystemFence</a>&#160;&#160;&#160;0x20000000</td></tr>
<tr class="separator:ga0e9ec830fe53ed7a24a8b96da15f4f12"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gae0909af811a68136a82c970d4e607133" id="r_gae0909af811a68136a82c970d4e607133"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gae0909af811a68136a82c970d4e607133">hipEventReleaseToDevice</a>&#160;&#160;&#160;0x40000000</td></tr>
<tr class="separator:gae0909af811a68136a82c970d4e607133"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gab89a2c35618cc9e3e9e2308216c9fc45" id="r_gab89a2c35618cc9e3e9e2308216c9fc45"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gab89a2c35618cc9e3e9e2308216c9fc45">hipEventReleaseToSystem</a>&#160;&#160;&#160;0x80000000</td></tr>
<tr class="separator:gab89a2c35618cc9e3e9e2308216c9fc45"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga572208e4a28453f2073d2c8e557584c4" id="r_ga572208e4a28453f2073d2c8e557584c4"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga572208e4a28453f2073d2c8e557584c4">hipEnableDefault</a>&#160;&#160;&#160;0x0</td></tr>
<tr class="separator:ga572208e4a28453f2073d2c8e557584c4"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaa78bc2a6e22c64dc8410710e6a976c58" id="r_gaa78bc2a6e22c64dc8410710e6a976c58"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaa78bc2a6e22c64dc8410710e6a976c58">hipEnableLegacyStream</a>&#160;&#160;&#160;0x1</td></tr>
<tr class="separator:gaa78bc2a6e22c64dc8410710e6a976c58"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gabc39fb84f3390dfe4a69c10303c1340d" id="r_gabc39fb84f3390dfe4a69c10303c1340d"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gabc39fb84f3390dfe4a69c10303c1340d">hipEnablePerThreadDefaultStream</a>&#160;&#160;&#160;0x2</td></tr>
<tr class="separator:gabc39fb84f3390dfe4a69c10303c1340d"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga68a61bd968eb98b6cc6365e760722617" id="r_ga68a61bd968eb98b6cc6365e760722617"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga68a61bd968eb98b6cc6365e760722617">hipHostAllocDefault</a>&#160;&#160;&#160;0x0</td></tr>
<tr class="separator:ga68a61bd968eb98b6cc6365e760722617"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gad594ec51cb5b5e946c1e354bf80bddc7" id="r_gad594ec51cb5b5e946c1e354bf80bddc7"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gad594ec51cb5b5e946c1e354bf80bddc7">hipHostMallocDefault</a>&#160;&#160;&#160;0x0</td></tr>
<tr class="separator:gad594ec51cb5b5e946c1e354bf80bddc7"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga39cedce84d521c99c0e6565f02d15c06" id="r_ga39cedce84d521c99c0e6565f02d15c06"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga39cedce84d521c99c0e6565f02d15c06">hipHostAllocPortable</a>&#160;&#160;&#160;0x1</td></tr>
<tr class="separator:ga39cedce84d521c99c0e6565f02d15c06"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga99b7c2b08a834b4736bfdc24893a6bc5" id="r_ga99b7c2b08a834b4736bfdc24893a6bc5"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga99b7c2b08a834b4736bfdc24893a6bc5">hipHostMallocPortable</a>&#160;&#160;&#160;0x1</td></tr>
<tr class="separator:ga99b7c2b08a834b4736bfdc24893a6bc5"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga15e14750b538f56dda0836ddaab2b8c8" id="r_ga15e14750b538f56dda0836ddaab2b8c8"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga15e14750b538f56dda0836ddaab2b8c8">hipHostAllocMapped</a>&#160;&#160;&#160;0x2</td></tr>
<tr class="separator:ga15e14750b538f56dda0836ddaab2b8c8"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaf6e07be144bb1031bfcf9816335906cc" id="r_gaf6e07be144bb1031bfcf9816335906cc"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaf6e07be144bb1031bfcf9816335906cc">hipHostMallocMapped</a>&#160;&#160;&#160;0x2</td></tr>
<tr class="separator:gaf6e07be144bb1031bfcf9816335906cc"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga4d6740835ee5071aac5cdb9c69238135" id="r_ga4d6740835ee5071aac5cdb9c69238135"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga4d6740835ee5071aac5cdb9c69238135">hipHostAllocWriteCombined</a>&#160;&#160;&#160;0x4</td></tr>
<tr class="separator:ga4d6740835ee5071aac5cdb9c69238135"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga21beb95617644dbefaffaacdc0f0a35c" id="r_ga21beb95617644dbefaffaacdc0f0a35c"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga21beb95617644dbefaffaacdc0f0a35c">hipHostMallocWriteCombined</a>&#160;&#160;&#160;0x4</td></tr>
<tr class="separator:ga21beb95617644dbefaffaacdc0f0a35c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaa4c1aba392606f075e6fea9ed3cf0ccb" id="r_gaa4c1aba392606f075e6fea9ed3cf0ccb"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaa4c1aba392606f075e6fea9ed3cf0ccb">hipHostMallocUncached</a>&#160;&#160;&#160;0x10000000</td></tr>
<tr class="separator:gaa4c1aba392606f075e6fea9ed3cf0ccb"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga213497e00c458747d94d7afd21907cdf" id="r_ga213497e00c458747d94d7afd21907cdf"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga213497e00c458747d94d7afd21907cdf">hipHostAllocUncached</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gaa4c1aba392606f075e6fea9ed3cf0ccb">hipHostMallocUncached</a></td></tr>
<tr class="separator:ga213497e00c458747d94d7afd21907cdf"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga1d7d6413d3c528fcaa7b5eb808da75d9" id="r_ga1d7d6413d3c528fcaa7b5eb808da75d9"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga1d7d6413d3c528fcaa7b5eb808da75d9">hipHostMallocNumaUser</a>&#160;&#160;&#160;0x20000000</td></tr>
<tr class="separator:ga1d7d6413d3c528fcaa7b5eb808da75d9"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gac726701ac143539b0893c506377f44ee" id="r_gac726701ac143539b0893c506377f44ee"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gac726701ac143539b0893c506377f44ee">hipHostMallocCoherent</a>&#160;&#160;&#160;0x40000000</td></tr>
<tr class="separator:gac726701ac143539b0893c506377f44ee"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaeec0b563ac9d02f45ed02ceab771a472" id="r_gaeec0b563ac9d02f45ed02ceab771a472"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaeec0b563ac9d02f45ed02ceab771a472">hipHostMallocNonCoherent</a>&#160;&#160;&#160;0x80000000</td></tr>
<tr class="separator:gaeec0b563ac9d02f45ed02ceab771a472"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga48891a93744bc494ce1b1841f756694b" id="r_ga48891a93744bc494ce1b1841f756694b"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga48891a93744bc494ce1b1841f756694b">hipMemAttachGlobal</a>&#160;&#160;&#160;0x01</td></tr>
<tr class="separator:ga48891a93744bc494ce1b1841f756694b"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga93325b413b2dc1e01be5e7d2f6d8947f" id="r_ga93325b413b2dc1e01be5e7d2f6d8947f"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga93325b413b2dc1e01be5e7d2f6d8947f">hipMemAttachHost</a>&#160;&#160;&#160;0x02</td></tr>
<tr class="separator:ga93325b413b2dc1e01be5e7d2f6d8947f"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga21e33b9b7f3a1a7deebc8718d5bb5e01" id="r_ga21e33b9b7f3a1a7deebc8718d5bb5e01"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga21e33b9b7f3a1a7deebc8718d5bb5e01">hipMemAttachSingle</a>&#160;&#160;&#160;0x04</td></tr>
<tr class="separator:ga21e33b9b7f3a1a7deebc8718d5bb5e01"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaa4247e48df3515377a4190d9d5eef26f" id="r_gaa4247e48df3515377a4190d9d5eef26f"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaa4247e48df3515377a4190d9d5eef26f">hipDeviceMallocDefault</a>&#160;&#160;&#160;0x0</td></tr>
<tr class="separator:gaa4247e48df3515377a4190d9d5eef26f"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gabf06f7f184187487343b027b04c13173" id="r_gabf06f7f184187487343b027b04c13173"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gabf06f7f184187487343b027b04c13173">hipDeviceMallocFinegrained</a>&#160;&#160;&#160;0x1</td></tr>
<tr class="separator:gabf06f7f184187487343b027b04c13173"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga9c7b267b119306ca08402b6df91d101b" id="r_ga9c7b267b119306ca08402b6df91d101b"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga9c7b267b119306ca08402b6df91d101b">hipMallocSignalMemory</a>&#160;&#160;&#160;0x2</td></tr>
<tr class="separator:ga9c7b267b119306ca08402b6df91d101b"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga7e54931e846bc5815b2ffdc4c26bc841" id="r_ga7e54931e846bc5815b2ffdc4c26bc841"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga7e54931e846bc5815b2ffdc4c26bc841">hipDeviceMallocUncached</a>&#160;&#160;&#160;0x3</td></tr>
<tr class="separator:ga7e54931e846bc5815b2ffdc4c26bc841"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gad01f4c969ca352edd8330774fa416e5b" id="r_gad01f4c969ca352edd8330774fa416e5b"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gad01f4c969ca352edd8330774fa416e5b">hipDeviceMallocContiguous</a>&#160;&#160;&#160;0x4</td></tr>
<tr class="separator:gad01f4c969ca352edd8330774fa416e5b"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gac7c100d241ff84ad10109bb00b7b25dc" id="r_gac7c100d241ff84ad10109bb00b7b25dc"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gac7c100d241ff84ad10109bb00b7b25dc">hipHostRegisterDefault</a>&#160;&#160;&#160;0x0</td></tr>
<tr class="separator:gac7c100d241ff84ad10109bb00b7b25dc"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga2db444f2315d412d3c7ba80ec6049583" id="r_ga2db444f2315d412d3c7ba80ec6049583"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga2db444f2315d412d3c7ba80ec6049583">hipHostRegisterPortable</a>&#160;&#160;&#160;0x1</td></tr>
<tr class="separator:ga2db444f2315d412d3c7ba80ec6049583"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gacfa4edcfcb39fc61bff6bdecb14d7618" id="r_gacfa4edcfcb39fc61bff6bdecb14d7618"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gacfa4edcfcb39fc61bff6bdecb14d7618">hipHostRegisterMapped</a>&#160;&#160;&#160;0x2</td></tr>
<tr class="separator:gacfa4edcfcb39fc61bff6bdecb14d7618"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaefa79f1b4481d6a1d1091c14b24f33d0" id="r_gaefa79f1b4481d6a1d1091c14b24f33d0"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaefa79f1b4481d6a1d1091c14b24f33d0">hipHostRegisterIoMemory</a>&#160;&#160;&#160;0x4</td></tr>
<tr class="separator:gaefa79f1b4481d6a1d1091c14b24f33d0"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga4fa1d9b68702b4705b0a2aaa96c58774" id="r_ga4fa1d9b68702b4705b0a2aaa96c58774"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga4fa1d9b68702b4705b0a2aaa96c58774">hipHostRegisterReadOnly</a>&#160;&#160;&#160;0x08</td></tr>
<tr class="separator:ga4fa1d9b68702b4705b0a2aaa96c58774"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gad01a491a6d1ab26ee10280aa1360b2a5" id="r_gad01a491a6d1ab26ee10280aa1360b2a5"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gad01a491a6d1ab26ee10280aa1360b2a5">hipExtHostRegisterCoarseGrained</a>&#160;&#160;&#160;0x8</td></tr>
<tr class="separator:gad01a491a6d1ab26ee10280aa1360b2a5"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga0de3ebe88623693c81a7eea6afee29fc" id="r_ga0de3ebe88623693c81a7eea6afee29fc"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga0de3ebe88623693c81a7eea6afee29fc">hipExtHostRegisterUncached</a>&#160;&#160;&#160;0x80000000</td></tr>
<tr class="separator:ga0de3ebe88623693c81a7eea6afee29fc"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga9032d35eb7383948828ee48e1e19f5fd" id="r_ga9032d35eb7383948828ee48e1e19f5fd"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga9032d35eb7383948828ee48e1e19f5fd">hipDeviceScheduleAuto</a>&#160;&#160;&#160;0x0</td></tr>
<tr class="separator:ga9032d35eb7383948828ee48e1e19f5fd"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga713d962bafb7758dc1ff0675e4239453" id="r_ga713d962bafb7758dc1ff0675e4239453"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga713d962bafb7758dc1ff0675e4239453">hipDeviceScheduleSpin</a>&#160;&#160;&#160;0x1</td></tr>
<tr class="separator:ga713d962bafb7758dc1ff0675e4239453"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaaf1e2706430c06601aa12a8af2a0ba5a" id="r_gaaf1e2706430c06601aa12a8af2a0ba5a"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaaf1e2706430c06601aa12a8af2a0ba5a">hipDeviceScheduleYield</a>&#160;&#160;&#160;0x2</td></tr>
<tr class="separator:gaaf1e2706430c06601aa12a8af2a0ba5a"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gac9480926da806dfe7241e3c8fa0bd060" id="r_gac9480926da806dfe7241e3c8fa0bd060"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gac9480926da806dfe7241e3c8fa0bd060">hipDeviceScheduleBlockingSync</a>&#160;&#160;&#160;0x4</td></tr>
<tr class="separator:gac9480926da806dfe7241e3c8fa0bd060"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gad0ee225558955549785dc0bf37e53554" id="r_gad0ee225558955549785dc0bf37e53554"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gad0ee225558955549785dc0bf37e53554">hipDeviceScheduleMask</a>&#160;&#160;&#160;0x7</td></tr>
<tr class="separator:gad0ee225558955549785dc0bf37e53554"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga0b7ffad8d7cfcbf9d3c863d30ef651ae" id="r_ga0b7ffad8d7cfcbf9d3c863d30ef651ae"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga0b7ffad8d7cfcbf9d3c863d30ef651ae">hipDeviceMapHost</a>&#160;&#160;&#160;0x8</td></tr>
<tr class="separator:ga0b7ffad8d7cfcbf9d3c863d30ef651ae"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gad1c4f8c9fab30ce95f59e2cc404f4d96" id="r_gad1c4f8c9fab30ce95f59e2cc404f4d96"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gad1c4f8c9fab30ce95f59e2cc404f4d96">hipDeviceLmemResizeToMax</a>&#160;&#160;&#160;0x10</td></tr>
<tr class="separator:gad1c4f8c9fab30ce95f59e2cc404f4d96"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga2cae862086a89539b3cf6906a458190c" id="r_ga2cae862086a89539b3cf6906a458190c"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga2cae862086a89539b3cf6906a458190c">hipArrayDefault</a>&#160;&#160;&#160;0x00</td></tr>
<tr class="separator:ga2cae862086a89539b3cf6906a458190c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga7b5573cd703c789c35edb588fb973588" id="r_ga7b5573cd703c789c35edb588fb973588"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga7b5573cd703c789c35edb588fb973588">hipArrayLayered</a>&#160;&#160;&#160;0x01</td></tr>
<tr class="separator:ga7b5573cd703c789c35edb588fb973588"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gadb552c0ab451ab238fccd142e975a840" id="r_gadb552c0ab451ab238fccd142e975a840"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gadb552c0ab451ab238fccd142e975a840">hipArraySurfaceLoadStore</a>&#160;&#160;&#160;0x02</td></tr>
<tr class="separator:gadb552c0ab451ab238fccd142e975a840"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga59685fdad42a844747214758c05f333c" id="r_ga59685fdad42a844747214758c05f333c"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga59685fdad42a844747214758c05f333c">hipArrayCubemap</a>&#160;&#160;&#160;0x04</td></tr>
<tr class="separator:ga59685fdad42a844747214758c05f333c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga62bc9f85553dbe4eea819ae35f8baaac" id="r_ga62bc9f85553dbe4eea819ae35f8baaac"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga62bc9f85553dbe4eea819ae35f8baaac">hipArrayTextureGather</a>&#160;&#160;&#160;0x08</td></tr>
<tr class="separator:ga62bc9f85553dbe4eea819ae35f8baaac"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga6b6e50d4535e432ffd219008e751bf2d" id="r_ga6b6e50d4535e432ffd219008e751bf2d"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga6b6e50d4535e432ffd219008e751bf2d">hipOccupancyDefault</a>&#160;&#160;&#160;0x00</td></tr>
<tr class="separator:ga6b6e50d4535e432ffd219008e751bf2d"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gadad1d47116853cf8fb1cd34db61b66dc" id="r_gadad1d47116853cf8fb1cd34db61b66dc"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gadad1d47116853cf8fb1cd34db61b66dc">hipOccupancyDisableCachingOverride</a>&#160;&#160;&#160;0x01</td></tr>
<tr class="separator:gadad1d47116853cf8fb1cd34db61b66dc"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaac01b6324c1a7bcdde41d3349e0cf330" id="r_gaac01b6324c1a7bcdde41d3349e0cf330"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaac01b6324c1a7bcdde41d3349e0cf330">hipCooperativeLaunchMultiDeviceNoPreSync</a>&#160;&#160;&#160;0x01</td></tr>
<tr class="separator:gaac01b6324c1a7bcdde41d3349e0cf330"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga719dca27c00095d1348ffcfc96bea187" id="r_ga719dca27c00095d1348ffcfc96bea187"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga719dca27c00095d1348ffcfc96bea187">hipCooperativeLaunchMultiDeviceNoPostSync</a>&#160;&#160;&#160;0x02</td></tr>
<tr class="separator:ga719dca27c00095d1348ffcfc96bea187"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga3ebb587bf795d68d18ba0679a2b41fc8" id="r_ga3ebb587bf795d68d18ba0679a2b41fc8"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga3ebb587bf795d68d18ba0679a2b41fc8">hipCpuDeviceId</a>&#160;&#160;&#160;((int)-1)</td></tr>
<tr class="separator:ga3ebb587bf795d68d18ba0679a2b41fc8"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga142b1b5268b4d18fe34050d5c9d9907d" id="r_ga142b1b5268b4d18fe34050d5c9d9907d"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga142b1b5268b4d18fe34050d5c9d9907d">hipInvalidDeviceId</a>&#160;&#160;&#160;((int)-2)</td></tr>
<tr class="separator:ga142b1b5268b4d18fe34050d5c9d9907d"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga06df407ca5682aeed76186e15c050a98" id="r_ga06df407ca5682aeed76186e15c050a98"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga06df407ca5682aeed76186e15c050a98">hipExtAnyOrderLaunch</a>&#160;&#160;&#160;0x01</td></tr>
<tr class="separator:ga06df407ca5682aeed76186e15c050a98"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gab6d87965bf388c229dffa70fea11e772" id="r_gab6d87965bf388c229dffa70fea11e772"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gab6d87965bf388c229dffa70fea11e772">hipStreamWaitValueGte</a>&#160;&#160;&#160;0x0</td></tr>
<tr class="separator:gab6d87965bf388c229dffa70fea11e772"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga3cf15c65c047827a251f1c42d2a8c4d4" id="r_ga3cf15c65c047827a251f1c42d2a8c4d4"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga3cf15c65c047827a251f1c42d2a8c4d4">hipStreamWaitValueEq</a>&#160;&#160;&#160;0x1</td></tr>
<tr class="separator:ga3cf15c65c047827a251f1c42d2a8c4d4"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaeaac19269c1ef4f10630ecb683302fed" id="r_gaeaac19269c1ef4f10630ecb683302fed"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaeaac19269c1ef4f10630ecb683302fed">hipStreamWaitValueAnd</a>&#160;&#160;&#160;0x2</td></tr>
<tr class="separator:gaeaac19269c1ef4f10630ecb683302fed"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga4c3e4c6c5147a927d84d239da5754845" id="r_ga4c3e4c6c5147a927d84d239da5754845"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga4c3e4c6c5147a927d84d239da5754845">hipStreamWaitValueNor</a>&#160;&#160;&#160;0x3</td></tr>
<tr class="separator:ga4c3e4c6c5147a927d84d239da5754845"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga69981e17c0b9cf4cd562c8103724e2cf" id="r_ga69981e17c0b9cf4cd562c8103724e2cf"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga69981e17c0b9cf4cd562c8103724e2cf">hipStreamPerThread</a>&#160;&#160;&#160;((<a class="el" href="group___global_defs.html#ga0fc4326b345ac109cb72b90a22a1cb29">hipStream_t</a>)2)</td></tr>
<tr class="separator:ga69981e17c0b9cf4cd562c8103724e2cf"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga7f5bb5340726842f8967cd66337361d7" id="r_ga7f5bb5340726842f8967cd66337361d7"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga7f5bb5340726842f8967cd66337361d7">hipStreamLegacy</a>&#160;&#160;&#160;((<a class="el" href="group___global_defs.html#ga0fc4326b345ac109cb72b90a22a1cb29">hipStream_t</a>)1)</td></tr>
<tr class="separator:ga7f5bb5340726842f8967cd66337361d7"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gab99642079d3d09533b3f8f27920309fc" id="r_gab99642079d3d09533b3f8f27920309fc"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gab99642079d3d09533b3f8f27920309fc">hipExternalMemoryDedicated</a>&#160;&#160;&#160;0x1</td></tr>
<tr class="separator:gab99642079d3d09533b3f8f27920309fc"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga64f6b888b51ac73a4a442e8c7986bcfe" id="r_ga64f6b888b51ac73a4a442e8c7986bcfe"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga64f6b888b51ac73a4a442e8c7986bcfe">hipStreamAttrID</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#ga4026e9ccca8bb88888ad739e0f7586b4">hipLaunchAttributeID</a></td></tr>
<tr class="separator:ga64f6b888b51ac73a4a442e8c7986bcfe"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaf67922ae5820e7e5a949b75a90cc12e3" id="r_gaf67922ae5820e7e5a949b75a90cc12e3"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaf67922ae5820e7e5a949b75a90cc12e3">hipStreamAttributeAccessPolicyWindow</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4ae9c06559f2a188eb87818348cefc4171">hipLaunchAttributeAccessPolicyWindow</a></td></tr>
<tr class="separator:gaf67922ae5820e7e5a949b75a90cc12e3"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga10af2df66d201920bdd860164e45c3b4" id="r_ga10af2df66d201920bdd860164e45c3b4"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga10af2df66d201920bdd860164e45c3b4">hipStreamAttributeSynchronizationPolicy</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4aac7011b4266fc8e091a1048326da38b7">hipLaunchAttributeSynchronizationPolicy</a></td></tr>
<tr class="separator:ga10af2df66d201920bdd860164e45c3b4"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gae628261a328822c59e70741b44a15765" id="r_gae628261a328822c59e70741b44a15765"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gae628261a328822c59e70741b44a15765">hipStreamAttributeMemSyncDomainMap</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4a9229ce145edcc4442002d8ee2d156cc3">hipLaunchAttributeMemSyncDomainMap</a></td></tr>
<tr class="separator:gae628261a328822c59e70741b44a15765"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga867c605c43bdaec3d8d9fd6e68833795" id="r_ga867c605c43bdaec3d8d9fd6e68833795"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga867c605c43bdaec3d8d9fd6e68833795">hipStreamAttributeMemSyncDomain</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4a71ab9ea6aef993bbcaac9798a1445023">hipLaunchAttributeMemSyncDomain</a></td></tr>
<tr class="separator:ga867c605c43bdaec3d8d9fd6e68833795"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga9f499f227eb07651976dd2bca91b5a32" id="r_ga9f499f227eb07651976dd2bca91b5a32"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga9f499f227eb07651976dd2bca91b5a32">hipStreamAttributePriority</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4a358f69dfec66d2cfe93b25f44845bcc1">hipLaunchAttributePriority</a></td></tr>
<tr class="separator:ga9f499f227eb07651976dd2bca91b5a32"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gabc501f050b998117cf3519d57967721d" id="r_gabc501f050b998117cf3519d57967721d"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gabc501f050b998117cf3519d57967721d">hipStreamAttrValue</a>&#160;&#160;&#160;<a class="el" href="unionhip_launch_attribute_value.html">hipLaunchAttributeValue</a></td></tr>
<tr class="separator:gabc501f050b998117cf3519d57967721d"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gac88b62d1b19899d8611f8b0d81c8aefc" id="r_gac88b62d1b19899d8611f8b0d81c8aefc"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gac88b62d1b19899d8611f8b0d81c8aefc">hipKernelNodeAttrID</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#ga4026e9ccca8bb88888ad739e0f7586b4">hipLaunchAttributeID</a></td></tr>
<tr class="separator:gac88b62d1b19899d8611f8b0d81c8aefc"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaaca6dcdbf6d07ebd1929ef4317ee767b" id="r_gaaca6dcdbf6d07ebd1929ef4317ee767b"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaaca6dcdbf6d07ebd1929ef4317ee767b">hipKernelNodeAttributeAccessPolicyWindow</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4ae9c06559f2a188eb87818348cefc4171">hipLaunchAttributeAccessPolicyWindow</a></td></tr>
<tr class="separator:gaaca6dcdbf6d07ebd1929ef4317ee767b"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaded41d67a369cba6502677aa00ac000e" id="r_gaded41d67a369cba6502677aa00ac000e"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaded41d67a369cba6502677aa00ac000e">hipKernelNodeAttributeCooperative</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4af2e2bdbec3458fd4810e9d18b9e527af">hipLaunchAttributeCooperative</a></td></tr>
<tr class="separator:gaded41d67a369cba6502677aa00ac000e"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gace8baff75db3919346fdcb7e5cf1b7ec" id="r_gace8baff75db3919346fdcb7e5cf1b7ec"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gace8baff75db3919346fdcb7e5cf1b7ec">hipKernelNodeAttributePriority</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4a358f69dfec66d2cfe93b25f44845bcc1">hipLaunchAttributePriority</a></td></tr>
<tr class="separator:gace8baff75db3919346fdcb7e5cf1b7ec"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga34eb9fa298c10a891ed61bea24ed6c19" id="r_ga34eb9fa298c10a891ed61bea24ed6c19"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga34eb9fa298c10a891ed61bea24ed6c19">hipKernelNodeAttrValue</a>&#160;&#160;&#160;<a class="el" href="unionhip_launch_attribute_value.html">hipLaunchAttributeValue</a></td></tr>
<tr class="separator:ga34eb9fa298c10a891ed61bea24ed6c19"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga8862cae1ca655975e89f6a49f85fdb6d" id="r_ga8862cae1ca655975e89f6a49f85fdb6d"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga8862cae1ca655975e89f6a49f85fdb6d">hipDrvLaunchAttributeCooperative</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4af2e2bdbec3458fd4810e9d18b9e527af">hipLaunchAttributeCooperative</a></td></tr>
<tr class="separator:ga8862cae1ca655975e89f6a49f85fdb6d"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaef10fd11055b9bd60594621763e06b8c" id="r_gaef10fd11055b9bd60594621763e06b8c"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaef10fd11055b9bd60594621763e06b8c">hipDrvLaunchAttributeID</a>&#160;&#160;&#160;<a class="el" href="group___global_defs.html#ga4026e9ccca8bb88888ad739e0f7586b4">hipLaunchAttributeID</a></td></tr>
<tr class="separator:gaef10fd11055b9bd60594621763e06b8c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaaab4f9f146f99b0c285a50e3a25c2f4a" id="r_gaaab4f9f146f99b0c285a50e3a25c2f4a"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaaab4f9f146f99b0c285a50e3a25c2f4a">hipDrvLaunchAttributeValue</a>&#160;&#160;&#160;<a class="el" href="unionhip_launch_attribute_value.html">hipLaunchAttributeValue</a></td></tr>
<tr class="separator:gaaab4f9f146f99b0c285a50e3a25c2f4a"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga50ec239992eb3d9adec2342f4ef55d58" id="r_ga50ec239992eb3d9adec2342f4ef55d58"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga50ec239992eb3d9adec2342f4ef55d58">hipDrvLaunchAttribute</a>&#160;&#160;&#160;<a class="el" href="structhip_launch_attribute.html">hipLaunchAttribute</a></td></tr>
<tr class="separator:ga50ec239992eb3d9adec2342f4ef55d58"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gadc2b418c7ddb2a925668c93e2b09d283" id="r_gadc2b418c7ddb2a925668c93e2b09d283"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gadc2b418c7ddb2a925668c93e2b09d283">hipGraphKernelNodePortDefault</a>&#160;&#160;&#160;0</td></tr>
<tr class="separator:gadc2b418c7ddb2a925668c93e2b09d283"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gafa17b53c9077021a57c4226282df5c5f" id="r_gafa17b53c9077021a57c4226282df5c5f"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gafa17b53c9077021a57c4226282df5c5f">hipGraphKernelNodePortLaunchCompletion</a>&#160;&#160;&#160;2</td></tr>
<tr class="separator:gafa17b53c9077021a57c4226282df5c5f"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gad58b559f9d55b1a9d75f7c0b0ec09eef" id="r_gad58b559f9d55b1a9d75f7c0b0ec09eef"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gad58b559f9d55b1a9d75f7c0b0ec09eef">hipGraphKernelNodePortProgrammatic</a>&#160;&#160;&#160;1</td></tr>
<tr class="separator:gad58b559f9d55b1a9d75f7c0b0ec09eef"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga4648625dd84e67665d6e81eca7ac38b2" id="r_ga4648625dd84e67665d6e81eca7ac38b2"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga4648625dd84e67665d6e81eca7ac38b2">hiprtcJIT_option</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#ga54cbbb7697c63cf9b13383b49819d500">hipJitOption</a></td></tr>
<tr class="separator:ga4648625dd84e67665d6e81eca7ac38b2"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga844dd731acf15ad2f5234c3952525077" id="r_ga844dd731acf15ad2f5234c3952525077"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga844dd731acf15ad2f5234c3952525077">HIPRTC_JIT_MAX_REGISTERS</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500adb9370990a4403b1e5e03724031b4ecb">hipJitOptionMaxRegisters</a></td></tr>
<tr class="separator:ga844dd731acf15ad2f5234c3952525077"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaf17433edc5e16beeea7ecc1771480a3c" id="r_gaf17433edc5e16beeea7ecc1771480a3c"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaf17433edc5e16beeea7ecc1771480a3c">HIPRTC_JIT_THREADS_PER_BLOCK</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a5c9a55072a6f4ed3ca61604ef66a4a86">hipJitOptionThreadsPerBlock</a></td></tr>
<tr class="memdesc:gaf17433edc5e16beeea7ecc1771480a3c"><td class="mdescLeft">&#160;</td><td class="mdescRight">CUDA Only Number of thread per block/*#end#*&zwj;/.  <br /></td></tr>
<tr class="separator:gaf17433edc5e16beeea7ecc1771480a3c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga116d5f8bab368a95f67e5aa271b3ceb1" id="r_ga116d5f8bab368a95f67e5aa271b3ceb1"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga116d5f8bab368a95f67e5aa271b3ceb1">HIPRTC_JIT_WALL_TIME</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a8ee4752e49439cb2fbecdf1dcc69871e">hipJitOptionWallTime</a></td></tr>
<tr class="memdesc:ga116d5f8bab368a95f67e5aa271b3ceb1"><td class="mdescLeft">&#160;</td><td class="mdescRight">CUDA Only Value for total wall clock time.  <br /></td></tr>
<tr class="separator:ga116d5f8bab368a95f67e5aa271b3ceb1"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga8a548b1d92ae8663fb68b2c2279dc90f" id="r_ga8a548b1d92ae8663fb68b2c2279dc90f"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga8a548b1d92ae8663fb68b2c2279dc90f">HIPRTC_JIT_INFO_LOG_BUFFER</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a144aa71e24aa20fb4162e9978d6c66d1">hipJitOptionInfoLogBuffer</a></td></tr>
<tr class="separator:ga8a548b1d92ae8663fb68b2c2279dc90f"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga492c32e4fd482ee995e7036df57037ad" id="r_ga492c32e4fd482ee995e7036df57037ad"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga492c32e4fd482ee995e7036df57037ad">HIPRTC_JIT_INFO_LOG_BUFFER_SIZE_BYTES</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a9692ed236671843b99de1dbfc7aadb8f">hipJitOptionInfoLogBufferSizeBytes</a></td></tr>
<tr class="separator:ga492c32e4fd482ee995e7036df57037ad"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga2b42afcded55988c4a9a97002720cb48" id="r_ga2b42afcded55988c4a9a97002720cb48"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga2b42afcded55988c4a9a97002720cb48">HIPRTC_JIT_ERROR_LOG_BUFFER</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a160e81f3788646e12f4526027c4c8e77">hipJitOptionErrorLogBuffer</a></td></tr>
<tr class="separator:ga2b42afcded55988c4a9a97002720cb48"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga42abe8807ad975df375d68643620d329" id="r_ga42abe8807ad975df375d68643620d329"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga42abe8807ad975df375d68643620d329">HIPRTC_JIT_ERROR_LOG_BUFFER_SIZE_BYTES</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a85c04bedf8aaf7a55628301a9672dd71">hipJitOptionErrorLogBufferSizeBytes</a></td></tr>
<tr class="separator:ga42abe8807ad975df375d68643620d329"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaf088a48ea211084071c1cacceb7c6105" id="r_gaf088a48ea211084071c1cacceb7c6105"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaf088a48ea211084071c1cacceb7c6105">HIPRTC_JIT_OPTIMIZATION_LEVEL</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a853499616f10eaa99df134371f0ed075">hipJitOptionOptimizationLevel</a></td></tr>
<tr class="separator:gaf088a48ea211084071c1cacceb7c6105"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga13c5257e0f3a67d068a57de9bd10210a" id="r_ga13c5257e0f3a67d068a57de9bd10210a"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga13c5257e0f3a67d068a57de9bd10210a">HIPRTC_JIT_TARGET_FROM_HIPCONTEXT</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500ab8e971a00aa557a668791e3403aafeca">hipJitOptionTargetFromContext</a></td></tr>
<tr class="separator:ga13c5257e0f3a67d068a57de9bd10210a"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga097ccbfbb1d9a1b80f6955f4a30d81b9" id="r_ga097ccbfbb1d9a1b80f6955f4a30d81b9"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga097ccbfbb1d9a1b80f6955f4a30d81b9">HIPRTC_JIT_TARGET</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a4c83761657de80ef98f0a34d1d22f323">hipJitOptionTarget</a></td></tr>
<tr class="memdesc:ga097ccbfbb1d9a1b80f6955f4a30d81b9"><td class="mdescLeft">&#160;</td><td class="mdescRight">CUDA Only JIT target.  <br /></td></tr>
<tr class="separator:ga097ccbfbb1d9a1b80f6955f4a30d81b9"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga0677386224c6d2b7f88252ea367f6603" id="r_ga0677386224c6d2b7f88252ea367f6603"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga0677386224c6d2b7f88252ea367f6603">HIPRTC_JIT_FALLBACK_STRATEGY</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500af0117529faba4b00c265add35d44c71c">hipJitOptionFallbackStrategy</a></td></tr>
<tr class="memdesc:ga0677386224c6d2b7f88252ea367f6603"><td class="mdescLeft">&#160;</td><td class="mdescRight">CUDA Only Fallback strategy.  <br /></td></tr>
<tr class="separator:ga0677386224c6d2b7f88252ea367f6603"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga891c9e74a0424511c658bb3c21a65538" id="r_ga891c9e74a0424511c658bb3c21a65538"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga891c9e74a0424511c658bb3c21a65538">HIPRTC_JIT_GENERATE_DEBUG_INFO</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500accc9993c7598bdcbfe2c7738fc2dc2a6">hipJitOptionGenerateDebugInfo</a></td></tr>
<tr class="memdesc:ga891c9e74a0424511c658bb3c21a65538"><td class="mdescLeft">&#160;</td><td class="mdescRight">CUDA Only Generate debug information/*#end#*&zwj;/.  <br /></td></tr>
<tr class="separator:ga891c9e74a0424511c658bb3c21a65538"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga4858108f706063c48145b701a3eefd5c" id="r_ga4858108f706063c48145b701a3eefd5c"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga4858108f706063c48145b701a3eefd5c">HIPRTC_JIT_LOG_VERBOSE</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500ad42abb970a18154f23e359e097d5aa89">hipJitOptionLogVerbose</a></td></tr>
<tr class="memdesc:ga4858108f706063c48145b701a3eefd5c"><td class="mdescLeft">&#160;</td><td class="mdescRight">CUDA Only Generate log verbose.  <br /></td></tr>
<tr class="separator:ga4858108f706063c48145b701a3eefd5c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gae1be684de97e8598bfe7005e9eee833e" id="r_gae1be684de97e8598bfe7005e9eee833e"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gae1be684de97e8598bfe7005e9eee833e">HIPRTC_JIT_GENERATE_LINE_INFO</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a75f073079cf61c48325633878532ab01">hipJitOptionGenerateLineInfo</a></td></tr>
<tr class="memdesc:gae1be684de97e8598bfe7005e9eee833e"><td class="mdescLeft">&#160;</td><td class="mdescRight">CUDA Only Generate line number information/*#end#*&zwj;/.  <br /></td></tr>
<tr class="separator:gae1be684de97e8598bfe7005e9eee833e"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga1fa7fb4d31414111eddcf33066ee72c8" id="r_ga1fa7fb4d31414111eddcf33066ee72c8"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga1fa7fb4d31414111eddcf33066ee72c8">HIPRTC_JIT_CACHE_MODE</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a03909311a4e24160a3b04796cddb5772">hipJitOptionCacheMode</a></td></tr>
<tr class="memdesc:ga1fa7fb4d31414111eddcf33066ee72c8"><td class="mdescLeft">&#160;</td><td class="mdescRight">CUDA Only Set cache mode.  <br /></td></tr>
<tr class="separator:ga1fa7fb4d31414111eddcf33066ee72c8"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga98ead031f321c8c55081d9d522ac6f64" id="r_ga98ead031f321c8c55081d9d522ac6f64"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga98ead031f321c8c55081d9d522ac6f64">HIPRTC_JIT_NEW_SM3X_OPT</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500ae942560c8927000dc8933aff96f4ed9e">hipJitOptionSm3xOpt</a></td></tr>
<tr class="separator:ga98ead031f321c8c55081d9d522ac6f64"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga6b6db66d400302dcefac95cfa824143c" id="r_ga6b6db66d400302dcefac95cfa824143c"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga6b6db66d400302dcefac95cfa824143c">HIPRTC_JIT_FAST_COMPILE</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a10b1271048a9a8adc55aebcfad56b5b2">hipJitOptionFastCompile</a></td></tr>
<tr class="memdesc:ga6b6db66d400302dcefac95cfa824143c"><td class="mdescLeft">&#160;</td><td class="mdescRight">CUDA Only Set fast compile.  <br /></td></tr>
<tr class="separator:ga6b6db66d400302dcefac95cfa824143c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga55bc69a5e022e095458550b05947750d" id="r_ga55bc69a5e022e095458550b05947750d"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga55bc69a5e022e095458550b05947750d">HIPRTC_JIT_GLOBAL_SYMBOL_NAMES</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a8cd7f84c16128c39d422cc94d6180d47">hipJitOptionGlobalSymbolNames</a></td></tr>
<tr class="separator:ga55bc69a5e022e095458550b05947750d"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga73cc3a267ecdef3675ac545f371bcdf0" id="r_ga73cc3a267ecdef3675ac545f371bcdf0"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga73cc3a267ecdef3675ac545f371bcdf0">HIPRTC_JIT_GLOBAL_SYMBOL_ADDRESS</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a92882f96099e9a265d1f24d20698dc28">hipJitOptionGlobalSymbolAddresses</a></td></tr>
<tr class="separator:ga73cc3a267ecdef3675ac545f371bcdf0"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga69b8fd1b666286ab6c4e03094b0e510b" id="r_ga69b8fd1b666286ab6c4e03094b0e510b"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga69b8fd1b666286ab6c4e03094b0e510b">HIPRTC_JIT_GLOBAL_SYMBOL_COUNT</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500aa428196b5654c717bb67583c808491f3">hipJitOptionGlobalSymbolCount</a></td></tr>
<tr class="memdesc:ga69b8fd1b666286ab6c4e03094b0e510b"><td class="mdescLeft">&#160;</td><td class="mdescRight">CUDA Only Number of symbol count./*#end#*&zwj;/.  <br /></td></tr>
<tr class="separator:ga69b8fd1b666286ab6c4e03094b0e510b"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga9bc86db1f4761801010ea682c5e1ed68" id="r_ga9bc86db1f4761801010ea682c5e1ed68"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga9bc86db1f4761801010ea682c5e1ed68">HIPRTC_JIT_LTO</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a0c4487f8639e8edd0790699f3f068cb3">hipJitOptionLto</a></td></tr>
<tr class="separator:ga9bc86db1f4761801010ea682c5e1ed68"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga68d7b895512edf7c793ea28ac521544b" id="r_ga68d7b895512edf7c793ea28ac521544b"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga68d7b895512edf7c793ea28ac521544b">HIPRTC_JIT_FTZ</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a77c8b8d337c2eb98e6f910e0a43c9115">hipJitOptionFtz</a></td></tr>
<tr class="separator:ga68d7b895512edf7c793ea28ac521544b"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaa0931c6a36ca739e1161774fccaf96fd" id="r_gaa0931c6a36ca739e1161774fccaf96fd"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaa0931c6a36ca739e1161774fccaf96fd">HIPRTC_JIT_PREC_DIV</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a4652bd7280b345cf90a785a8abba3230">hipJitOptionPrecDiv</a></td></tr>
<tr class="separator:gaa0931c6a36ca739e1161774fccaf96fd"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga8982f3e9dfdb66107ad2eb79e83373bd" id="r_ga8982f3e9dfdb66107ad2eb79e83373bd"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga8982f3e9dfdb66107ad2eb79e83373bd">HIPRTC_JIT_PREC_SQRT</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500ad49317eb710a0ab90b3678eaa28edf5c">hipJitOptionPrecSqrt</a></td></tr>
<tr class="separator:ga8982f3e9dfdb66107ad2eb79e83373bd"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga3b5d2d104996cf777ffe65d45beace13" id="r_ga3b5d2d104996cf777ffe65d45beace13"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga3b5d2d104996cf777ffe65d45beace13">HIPRTC_JIT_FMA</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a88b8360e9c3031625e14c7bab84ba8ec">hipJitOptionFma</a></td></tr>
<tr class="separator:ga3b5d2d104996cf777ffe65d45beace13"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gae52eeb4f069ce82ec2e3bca87ff29f78" id="r_gae52eeb4f069ce82ec2e3bca87ff29f78"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gae52eeb4f069ce82ec2e3bca87ff29f78">HIPRTC_JIT_POSITION_INDEPENDENT_CODE</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a069d8f3795d50848cc7d36a12e658c66">hipJitOptionPositionIndependentCode</a></td></tr>
<tr class="separator:gae52eeb4f069ce82ec2e3bca87ff29f78"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaf2d771a2f74ede0e89e6d52b2f7390c3" id="r_gaf2d771a2f74ede0e89e6d52b2f7390c3"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaf2d771a2f74ede0e89e6d52b2f7390c3">HIPRTC_JIT_MIN_CTA_PER_SM</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500ac17c5d8cb8bf1417cffa84ae37bd647a">hipJitOptionMinCTAPerSM</a></td></tr>
<tr class="separator:gaf2d771a2f74ede0e89e6d52b2f7390c3"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga57b1691eeb7a979112805a5670c6a419" id="r_ga57b1691eeb7a979112805a5670c6a419"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga57b1691eeb7a979112805a5670c6a419">HIPRTC_JIT_MAX_THREADS_PER_BLOCK</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500af3eb46de12b9aa7759fcbac5841705e8">hipJitOptionMaxThreadsPerBlock</a></td></tr>
<tr class="separator:ga57b1691eeb7a979112805a5670c6a419"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gacaf02527aac7f508983866c34ad136ab" id="r_gacaf02527aac7f508983866c34ad136ab"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gacaf02527aac7f508983866c34ad136ab">HIPRTC_JIT_OVERRIDE_DIRECT_VALUES</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a7186206beec45797e629016e91fe60c9">hipJitOptionOverrideDirectiveValues</a></td></tr>
<tr class="separator:gacaf02527aac7f508983866c34ad136ab"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gae2744cea3199352529c2f9a330cb885d" id="r_gae2744cea3199352529c2f9a330cb885d"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gae2744cea3199352529c2f9a330cb885d">HIPRTC_JIT_NUM_OPTIONS</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a639edb73879171ee5c22ce54d7d5b1d5">hipJitOptionNumOptions</a></td></tr>
<tr class="memdesc:gae2744cea3199352529c2f9a330cb885d"><td class="mdescLeft">&#160;</td><td class="mdescRight">Number of options.  <br /></td></tr>
<tr class="separator:gae2744cea3199352529c2f9a330cb885d"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga03b492a096a92af33ad0256fc26704be" id="r_ga03b492a096a92af33ad0256fc26704be"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga03b492a096a92af33ad0256fc26704be">HIPRTC_JIT_IR_TO_ISA_OPT_EXT</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500afcdd8a22dbc9216c754eab0924900f03">hipJitOptionIRtoISAOptExt</a></td></tr>
<tr class="separator:ga03b492a096a92af33ad0256fc26704be"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga8c505a9bef8629a7688e4a7347905f0e" id="r_ga8c505a9bef8629a7688e4a7347905f0e"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga8c505a9bef8629a7688e4a7347905f0e">HIPRTC_JIT_IR_TO_ISA_OPT_COUNT_EXT</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a01af3ae03c48fdb37a6307f2890600d9">hipJitOptionIRtoISAOptCountExt</a></td></tr>
<tr class="separator:ga8c505a9bef8629a7688e4a7347905f0e"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga6aef618fbe4bb34d63c218c8de8e5631" id="r_ga6aef618fbe4bb34d63c218c8de8e5631"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga6aef618fbe4bb34d63c218c8de8e5631">hiprtcJITInputType</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gad0680b9556a66070daae617025a8137b">hipJitInputType</a></td></tr>
<tr class="separator:ga6aef618fbe4bb34d63c218c8de8e5631"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaa5f10291ec491a9b44d423c8cf40e9a2" id="r_gaa5f10291ec491a9b44d423c8cf40e9a2"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaa5f10291ec491a9b44d423c8cf40e9a2">HIPRTC_JIT_INPUT_CUBIN</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137ba45010991b618ba1d7256a59375f97933">hipJitInputCubin</a></td></tr>
<tr class="memdesc:gaa5f10291ec491a9b44d423c8cf40e9a2"><td class="mdescLeft">&#160;</td><td class="mdescRight">Cuda only Input Cubin.  <br /></td></tr>
<tr class="separator:gaa5f10291ec491a9b44d423c8cf40e9a2"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gabfe56d29fc90e8372ee9f1d6a418829c" id="r_gabfe56d29fc90e8372ee9f1d6a418829c"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gabfe56d29fc90e8372ee9f1d6a418829c">HIPRTC_JIT_INPUT_PTX</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137bac42cc2efd148b2504642178cc1f6fd93">hipJitInputPtx</a></td></tr>
<tr class="memdesc:gabfe56d29fc90e8372ee9f1d6a418829c"><td class="mdescLeft">&#160;</td><td class="mdescRight">Cuda only Input PTX.  <br /></td></tr>
<tr class="separator:gabfe56d29fc90e8372ee9f1d6a418829c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaa19ce08a4953c057acba59fd0b9af60b" id="r_gaa19ce08a4953c057acba59fd0b9af60b"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaa19ce08a4953c057acba59fd0b9af60b">HIPRTC_JIT_INPUT_FATBINARY</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137baa404072040c12d06ebbf06ac518f1acc">hipJitInputFatBinary</a></td></tr>
<tr class="memdesc:gaa19ce08a4953c057acba59fd0b9af60b"><td class="mdescLeft">&#160;</td><td class="mdescRight">Cuda Only Input FAT Binary.  <br /></td></tr>
<tr class="separator:gaa19ce08a4953c057acba59fd0b9af60b"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga2f76899d2ecd435a61d0c9e5a8e944bb" id="r_ga2f76899d2ecd435a61d0c9e5a8e944bb"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga2f76899d2ecd435a61d0c9e5a8e944bb">HIPRTC_JIT_INPUT_OBJECT</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137ba885b8c1b34c4e922f1d6c9812791043b">hipJitInputObject</a></td></tr>
<tr class="memdesc:ga2f76899d2ecd435a61d0c9e5a8e944bb"><td class="mdescLeft">&#160;</td><td class="mdescRight">Cuda Only Host Object with embedded device code/*#end#*&zwj;/.  <br /></td></tr>
<tr class="separator:ga2f76899d2ecd435a61d0c9e5a8e944bb"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga9b4744b6ade1b83051e2923822a8efc8" id="r_ga9b4744b6ade1b83051e2923822a8efc8"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga9b4744b6ade1b83051e2923822a8efc8">HIPRTC_JIT_INPUT_LIBRARY</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137ba5fa416edd513fc5763e34f86166e8508">hipJitInputLibrary</a></td></tr>
<tr class="memdesc:ga9b4744b6ade1b83051e2923822a8efc8"><td class="mdescLeft">&#160;</td><td class="mdescRight">Cuda Only Archive of Host Objects with embedded device code/*#end#*&zwj;/.  <br /></td></tr>
<tr class="separator:ga9b4744b6ade1b83051e2923822a8efc8"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga88176f9b8fb9c09d294507bce0aae982" id="r_ga88176f9b8fb9c09d294507bce0aae982"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga88176f9b8fb9c09d294507bce0aae982">HIPRTC_JIT_INPUT_NVVM</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137baf94b48b3e589b922d6638a6eadfe0046">hipJitInputNvvm</a></td></tr>
<tr class="separator:ga88176f9b8fb9c09d294507bce0aae982"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga6eaf11642f9f91cd7b4bb5756aa59733" id="r_ga6eaf11642f9f91cd7b4bb5756aa59733"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga6eaf11642f9f91cd7b4bb5756aa59733">HIPRTC_JIT_NUM_LEGACY_INPUT_TYPES</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137ba3f3daa2b9d22468f9d46402a5a6823e2">hipJitNumLegacyInputTypes</a></td></tr>
<tr class="memdesc:ga6eaf11642f9f91cd7b4bb5756aa59733"><td class="mdescLeft">&#160;</td><td class="mdescRight">Count of Legacy Input Types/*#end#*&zwj;/.  <br /></td></tr>
<tr class="separator:ga6eaf11642f9f91cd7b4bb5756aa59733"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga69edd89282dedef12b5ece9672a8b972" id="r_ga69edd89282dedef12b5ece9672a8b972"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga69edd89282dedef12b5ece9672a8b972">HIPRTC_JIT_INPUT_LLVM_BITCODE</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137babc39a8964fe113cf0c00deebb8675d23">hipJitInputLLVMBitcode</a></td></tr>
<tr class="memdesc:ga69edd89282dedef12b5ece9672a8b972"><td class="mdescLeft">&#160;</td><td class="mdescRight">HIP Only LLVM Bitcode or IR assembly/*#end#*&zwj;/.  <br /></td></tr>
<tr class="separator:ga69edd89282dedef12b5ece9672a8b972"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga9a18c8cd0929f6ffaeb93ab1236e545c" id="r_ga9a18c8cd0929f6ffaeb93ab1236e545c"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga9a18c8cd0929f6ffaeb93ab1236e545c">HIPRTC_JIT_INPUT_LLVM_BUNDLED_BITCODE</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137baed006f1254cb797a67f3cd20eb15fd90">hipJitInputLLVMBundledBitcode</a></td></tr>
<tr class="memdesc:ga9a18c8cd0929f6ffaeb93ab1236e545c"><td class="mdescLeft">&#160;</td><td class="mdescRight">HIP Only LLVM Clang Bundled Code/*#end#*&zwj;/.  <br /></td></tr>
<tr class="separator:ga9a18c8cd0929f6ffaeb93ab1236e545c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga9bfd9789fcb79200ebb50cf7e0b862b2" id="r_ga9bfd9789fcb79200ebb50cf7e0b862b2"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga9bfd9789fcb79200ebb50cf7e0b862b2">HIPRTC_JIT_INPUT_LLVM_ARCHIVES_OF_BUNDLED_BITCODE</a>&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137ba3a1fcd77531ad7ba59d817966c9ff3a7">hipJitInputLLVMArchivesOfBundledBitcode</a></td></tr>
<tr class="separator:ga9bfd9789fcb79200ebb50cf7e0b862b2"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga9c4afbdb17545bab451e30889674e911" id="r_ga9c4afbdb17545bab451e30889674e911"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga9c4afbdb17545bab451e30889674e911">HIPRTC_JIT_INPUT_SPIRV</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137bae7607245bf34f44146dfa10778a103e9">hipJitInputSpirv</a></td></tr>
<tr class="memdesc:ga9c4afbdb17545bab451e30889674e911"><td class="mdescLeft">&#160;</td><td class="mdescRight">HIP Only SPIRV Code Object.  <br /></td></tr>
<tr class="separator:ga9c4afbdb17545bab451e30889674e911"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga645de3f1f485789503c15f9b3f03212c" id="r_ga645de3f1f485789503c15f9b3f03212c"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga645de3f1f485789503c15f9b3f03212c">HIPRTC_JIT_NUM_INPUT_TYPES</a>&#160;&#160;&#160;<a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137ba658d253cd7fceb446c97553544eb81ec">hipJitNumInputTypes</a></td></tr>
<tr class="memdesc:ga645de3f1f485789503c15f9b3f03212c"><td class="mdescLeft">&#160;</td><td class="mdescRight">Count of Input Types.  <br /></td></tr>
<tr class="separator:ga645de3f1f485789503c15f9b3f03212c"><td class="memSeparator" colspan="2">&#160;</td></tr>
</table><table class="memberdecls">
<tr class="heading"><td colspan="2"><h2 class="groupheader"><a id="typedef-members" name="typedef-members"></a>
Typedefs</h2></td></tr>
<tr class="memitem:ga6742b54e2b83c1a5d6861ede4825aafe" id="r_ga6742b54e2b83c1a5d6861ede4825aafe"><td class="memItemLeft" align="right" valign="top">typedef enum <a class="el" href="group___global_defs.html#ga89716f0e21b750a51ceb081208a84b33">__HIP_NODISCARD</a> <a class="el" href="group___global_defs.html#ga6742b54e2b83c1a5d6861ede4825aafe">hipError_t</a>&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga6742b54e2b83c1a5d6861ede4825aafe">hipError_t</a></td></tr>
<tr class="separator:ga6742b54e2b83c1a5d6861ede4825aafe"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga0ebbb61a275c1adb950de995aadd22bf" id="r_ga0ebbb61a275c1adb950de995aadd22bf"><td class="memItemLeft" align="right" valign="top">typedef struct ihipCtx_t *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga0ebbb61a275c1adb950de995aadd22bf">hipCtx_t</a></td></tr>
<tr class="separator:ga0ebbb61a275c1adb950de995aadd22bf"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga181a06ca0d50ffdd6e019c87ffe02fb4" id="r_ga181a06ca0d50ffdd6e019c87ffe02fb4"><td class="memItemLeft" align="right" valign="top">typedef int&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga181a06ca0d50ffdd6e019c87ffe02fb4">hipDevice_t</a></td></tr>
<tr class="separator:ga181a06ca0d50ffdd6e019c87ffe02fb4"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga0fc4326b345ac109cb72b90a22a1cb29" id="r_ga0fc4326b345ac109cb72b90a22a1cb29"><td class="memItemLeft" align="right" valign="top">typedef struct ihipStream_t *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga0fc4326b345ac109cb72b90a22a1cb29">hipStream_t</a></td></tr>
<tr class="separator:ga0fc4326b345ac109cb72b90a22a1cb29"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gab0b1dd6ce7ee1720c2970552c20173e8" id="r_gab0b1dd6ce7ee1720c2970552c20173e8"><td class="memItemLeft" align="right" valign="top">typedef struct ihipModule_t *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gab0b1dd6ce7ee1720c2970552c20173e8">hipModule_t</a></td></tr>
<tr class="separator:gab0b1dd6ce7ee1720c2970552c20173e8"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gac7ab0ad556b5e1b3461e450fd2c7da3b" id="r_gac7ab0ad556b5e1b3461e450fd2c7da3b"><td class="memItemLeft" align="right" valign="top">typedef struct ihipModuleSymbol_t *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gac7ab0ad556b5e1b3461e450fd2c7da3b">hipFunction_t</a></td></tr>
<tr class="separator:gac7ab0ad556b5e1b3461e450fd2c7da3b"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga1d7d9b2f511df4d4841c6f30ff01fbd8" id="r_ga1d7d9b2f511df4d4841c6f30ff01fbd8"><td class="memItemLeft" align="right" valign="top">typedef struct ihipLinkState_t *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga1d7d9b2f511df4d4841c6f30ff01fbd8">hipLinkState_t</a></td></tr>
<tr class="separator:ga1d7d9b2f511df4d4841c6f30ff01fbd8"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga494ada27be8218d3181e6d88f3196b79" id="r_ga494ada27be8218d3181e6d88f3196b79"><td class="memItemLeft" align="right" valign="top">typedef struct ihipLibrary_t *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga494ada27be8218d3181e6d88f3196b79">hipLibrary_t</a></td></tr>
<tr class="separator:ga494ada27be8218d3181e6d88f3196b79"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga457ed655bd58ace1a3b11b4bd19da8e9" id="r_ga457ed655bd58ace1a3b11b4bd19da8e9"><td class="memItemLeft" align="right" valign="top">typedef struct ihipKernel_t *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga457ed655bd58ace1a3b11b4bd19da8e9">hipKernel_t</a></td></tr>
<tr class="separator:ga457ed655bd58ace1a3b11b4bd19da8e9"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaf61ebfa5ef0825fb2a763ae42daa20f0" id="r_gaf61ebfa5ef0825fb2a763ae42daa20f0"><td class="memItemLeft" align="right" valign="top">typedef struct ihipMemPoolHandle_t *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaf61ebfa5ef0825fb2a763ae42daa20f0">hipMemPool_t</a></td></tr>
<tr class="separator:gaf61ebfa5ef0825fb2a763ae42daa20f0"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga3640952e23c028a87a7db564443948ea" id="r_ga3640952e23c028a87a7db564443948ea"><td class="memItemLeft" align="right" valign="top">typedef struct ihipEvent_t *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga3640952e23c028a87a7db564443948ea">hipEvent_t</a></td></tr>
<tr class="separator:ga3640952e23c028a87a7db564443948ea"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gacad4902ef0f6115cb225c6eadc08c0ed" id="r_gacad4902ef0f6115cb225c6eadc08c0ed"><td class="memItemLeft" align="right" valign="top">typedef void *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gacad4902ef0f6115cb225c6eadc08c0ed">hipExternalMemory_t</a></td></tr>
<tr class="separator:gacad4902ef0f6115cb225c6eadc08c0ed"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gabac0a28e2e38f93c46743f629efac5c5" id="r_gabac0a28e2e38f93c46743f629efac5c5"><td class="memItemLeft" align="right" valign="top">typedef void *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gabac0a28e2e38f93c46743f629efac5c5">hipExternalSemaphore_t</a></td></tr>
<tr class="separator:gabac0a28e2e38f93c46743f629efac5c5"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gad96ccb9b8a16edff6513bdc22745a832" id="r_gad96ccb9b8a16edff6513bdc22745a832"><td class="memItemLeft" align="right" valign="top">typedef struct _hipGraphicsResource&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gad96ccb9b8a16edff6513bdc22745a832">hipGraphicsResource</a></td></tr>
<tr class="separator:gad96ccb9b8a16edff6513bdc22745a832"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga0844c3ebc78e5c8d91dca7379b3e0930" id="r_ga0844c3ebc78e5c8d91dca7379b3e0930"><td class="memItemLeft" align="right" valign="top">typedef <a class="el" href="group___global_defs.html#gad96ccb9b8a16edff6513bdc22745a832">hipGraphicsResource</a> *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga0844c3ebc78e5c8d91dca7379b3e0930">hipGraphicsResource_t</a></td></tr>
<tr class="separator:ga0844c3ebc78e5c8d91dca7379b3e0930"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga76cd3d33523dd0544c9031fcccc95eec" id="r_ga76cd3d33523dd0544c9031fcccc95eec"><td class="memItemLeft" align="right" valign="top">typedef struct ihipGraph *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga76cd3d33523dd0544c9031fcccc95eec">hipGraph_t</a></td></tr>
<tr class="separator:ga76cd3d33523dd0544c9031fcccc95eec"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gae127ef09c4eec55642394658ec3433ec" id="r_gae127ef09c4eec55642394658ec3433ec"><td class="memItemLeft" align="right" valign="top">typedef struct hipGraphNode *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gae127ef09c4eec55642394658ec3433ec">hipGraphNode_t</a></td></tr>
<tr class="separator:gae127ef09c4eec55642394658ec3433ec"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gac6cdb648ca4cdd1f61d82c0c0644a065" id="r_gac6cdb648ca4cdd1f61d82c0c0644a065"><td class="memItemLeft" align="right" valign="top">typedef struct hipGraphExec *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gac6cdb648ca4cdd1f61d82c0c0644a065">hipGraphExec_t</a></td></tr>
<tr class="separator:gac6cdb648ca4cdd1f61d82c0c0644a065"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gab5b072cf29fa8e0a61cbad91e3798565" id="r_gab5b072cf29fa8e0a61cbad91e3798565"><td class="memItemLeft" align="right" valign="top">typedef struct hipUserObject *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gab5b072cf29fa8e0a61cbad91e3798565">hipUserObject_t</a></td></tr>
<tr class="separator:gab5b072cf29fa8e0a61cbad91e3798565"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga6b1ea90b2fea2d4c62eb351e1ed44f93" id="r_ga6b1ea90b2fea2d4c62eb351e1ed44f93"><td class="memItemLeft" align="right" valign="top">typedef void(*&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga6b1ea90b2fea2d4c62eb351e1ed44f93">hipHostFn_t</a>) (void *userData)</td></tr>
<tr class="separator:ga6b1ea90b2fea2d4c62eb351e1ed44f93"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gae466e78534ea3eef06973cd06aea9840" id="r_gae466e78534ea3eef06973cd06aea9840"><td class="memItemLeft" align="right" valign="top">typedef struct ihipMemGenericAllocationHandle *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gae466e78534ea3eef06973cd06aea9840">hipMemGenericAllocationHandle_t</a></td></tr>
<tr class="separator:gae466e78534ea3eef06973cd06aea9840"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaa311c7f0d6ec4f1a33f9235c3651b86b" id="r_gaa311c7f0d6ec4f1a33f9235c3651b86b"><td class="memItemLeft" align="right" valign="top">typedef unsigned int&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaa311c7f0d6ec4f1a33f9235c3651b86b">GLuint</a></td></tr>
<tr class="separator:gaa311c7f0d6ec4f1a33f9235c3651b86b"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga7efd7809e1632cdae75603fd1fee61c0" id="r_ga7efd7809e1632cdae75603fd1fee61c0"><td class="memItemLeft" align="right" valign="top">typedef unsigned int&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga7efd7809e1632cdae75603fd1fee61c0">GLenum</a></td></tr>
<tr class="separator:ga7efd7809e1632cdae75603fd1fee61c0"><td class="memSeparator" colspan="2">&#160;</td></tr>
</table><table class="memberdecls">
<tr class="heading"><td colspan="2"><h2 class="groupheader"><a id="enum-members" name="enum-members"></a>
Enumerations</h2></td></tr>
<tr class="memitem:gaea86e91d3cd65992d787b39b218435a3" id="r_gaea86e91d3cd65992d787b39b218435a3"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaea86e91d3cd65992d787b39b218435a3">hipMemoryType</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaea86e91d3cd65992d787b39b218435a3ab07106e9139657fd73adbbe5f0109bc1">hipMemoryTypeUnregistered</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaea86e91d3cd65992d787b39b218435a3a5c5c99ed85b2599362089aa089cdad77">hipMemoryTypeHost</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaea86e91d3cd65992d787b39b218435a3a0e5f84f5565ba2a011ef3a9df2584a7a">hipMemoryTypeDevice</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaea86e91d3cd65992d787b39b218435a3ac567ef3faeb55edfc965fd8f1dbccf4c">hipMemoryTypeManaged</a> = 3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaea86e91d3cd65992d787b39b218435a3abbd7b93a87068c9dbb8d841ff0f3a366">hipMemoryTypeArray</a> = 10
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaea86e91d3cd65992d787b39b218435a3aceb68d38418e0a54dd9f7c8e113a4ec4">hipMemoryTypeUnified</a> = 11
<br />
 }</td></tr>
<tr class="separator:gaea86e91d3cd65992d787b39b218435a3"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gacc0acd7b9bda126c6bb3dfd6e2796d7c" id="r_gacc0acd7b9bda126c6bb3dfd6e2796d7c"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gacc0acd7b9bda126c6bb3dfd6e2796d7c">hipDeviceAttribute_t</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cad6f798685ee7e3c0c598b768deed019e">hipDeviceAttributeCudaCompatibleBegin</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca52fa8868e3d06d6ceed35072946c4500">hipDeviceAttributeEccEnabled</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca3453c7d157ca16c6a94c312205c3ae86">hipDeviceAttributeAccessPolicyMaxWindowSize</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca773d2f74a90f647fcfec39ba19aa7b9e">hipDeviceAttributeAsyncEngineCount</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca9753ae75a27d737cb02c3ef762275106">hipDeviceAttributeCanMapHostMemory</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca56a8b8ee9b1165461ea6c1ee7d56e90d">hipDeviceAttributeCanUseHostPointerForRegisteredMem</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca2300e077e020e7967592065561373b00">hipDeviceAttributeClockRate</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4d0369a6ef7bd7890fdcabc16ed3385d">hipDeviceAttributeComputeMode</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8af4079129030527721246176198f75d">hipDeviceAttributeComputePreemptionSupported</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cad9f45254d0d048677f560032532d5504">hipDeviceAttributeConcurrentKernels</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca9e5af4761458152e645d2e1312767514">hipDeviceAttributeConcurrentManagedAccess</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6ffb0a3933411c136ea1f9d154fab5cc">hipDeviceAttributeCooperativeLaunch</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5169c438b4ba17f8588d744bf56d87e4">hipDeviceAttributeCooperativeMultiDeviceLaunch</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca41202a4affefb5cf099beb8c8bf70bbf">hipDeviceAttributeDeviceOverlap</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca0037b357264179e4093c551a80a2a21c">hipDeviceAttributeDirectManagedMemAccessFromHost</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca28029ba35569753cbdbd777b21eab37b">hipDeviceAttributeGlobalL1CacheSupported</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca1421bb450fe736fda9605a607be69836">hipDeviceAttributeHostNativeAtomicSupported</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caa384485d5fe1ac26746d817af1aa669b">hipDeviceAttributeIntegrated</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6129311200a17dcc5fa8d2256874ae3d">hipDeviceAttributeIsMultiGpuBoard</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca58434135137ef3af09567698829810f1">hipDeviceAttributeKernelExecTimeout</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca582ae5a26a7148504878890028e4b64c">hipDeviceAttributeL2CacheSize</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca7d251fb7e063e4703489eddbc41a440d">hipDeviceAttributeLocalL1CacheSupported</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cada0ca948530460469095f6a63729219a">hipDeviceAttributeLuid</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caea6c84c14d2539fc9abcdfb0f940acbe">hipDeviceAttributeLuidDeviceNodeMask</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca2735739cf977b7d303266f6781131e8d">hipDeviceAttributeComputeCapabilityMajor</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caa1a9b27307b3dda43201bfaead8458c5">hipDeviceAttributeManagedMemory</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caae53485511cc012addc523e602ef9b98">hipDeviceAttributeMaxBlocksPerMultiProcessor</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cac1e4ac589db0d8adbbc241e3d0fcd594">hipDeviceAttributeMaxBlockDimX</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca187dbffe12db09a56c0f75c340d879c9">hipDeviceAttributeMaxBlockDimY</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caf811f51e03d1ffb025d80ac1da088675">hipDeviceAttributeMaxBlockDimZ</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca03db8df0e7a9fbdaae683d97e8ac9c87">hipDeviceAttributeMaxGridDimX</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5b5cc49972679c5ccf62b79425ee99df">hipDeviceAttributeMaxGridDimY</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6c206ac083999caf4640e5d91dae24f7">hipDeviceAttributeMaxGridDimZ</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8d9538aecd5fa764b6b13dd9ae05a1cf">hipDeviceAttributeMaxSurface1D</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca48c9f35454f5c329718bec08b54e8928">hipDeviceAttributeMaxSurface1DLayered</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca45e5f8d0e1b6b8ba58cf4b0f00b793b0">hipDeviceAttributeMaxSurface2D</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca63f784bd3a09ed4b9c1feb3628410bbe">hipDeviceAttributeMaxSurface2DLayered</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca09c1178054d1e7eda20fd5bd5dd17175">hipDeviceAttributeMaxSurface3D</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca1a76a9768fb8e98c4f437e3f7962027f">hipDeviceAttributeMaxSurfaceCubemap</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca08a044c95db3574e2c89ca856adcf4df">hipDeviceAttributeMaxSurfaceCubemapLayered</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca9ca92f0db9775c913bc681d87449bf1a">hipDeviceAttributeMaxTexture1DWidth</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cacc59d7cf69f95371c8e8d7fbccf13e73">hipDeviceAttributeMaxTexture1DLayered</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca929925869c0fee0db630b4fd08f87b3a">hipDeviceAttributeMaxTexture1DLinear</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca2428066c6ecb425d5b61c7532042bedf">hipDeviceAttributeMaxTexture1DMipmap</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caba995e4cf2e8e3cf99dbca7c5adf4342">hipDeviceAttributeMaxTexture2DWidth</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca523ab7684ddf2fd7ad7e7b9123e49163">hipDeviceAttributeMaxTexture2DHeight</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca92b064e8b236f1d06b528056ce6fddae">hipDeviceAttributeMaxTexture2DGather</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caa4d2c06274d024a40fc0e4b797a5a3a2">hipDeviceAttributeMaxTexture2DLayered</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca45b44857785bff4085506a56022fbf0f">hipDeviceAttributeMaxTexture2DLinear</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caf1b78e548e4cd729f0e0be4ab7736c62">hipDeviceAttributeMaxTexture2DMipmap</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cac38a9aec2fba4d56ad90a0bd76c26380">hipDeviceAttributeMaxTexture3DWidth</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca36a3b206969474f65c0d5ad4831c1ba8">hipDeviceAttributeMaxTexture3DHeight</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caa7be0131e8f44109c377ca1b7d634ce7">hipDeviceAttributeMaxTexture3DDepth</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca90020ecaeb108308c5b13a335d5c9130">hipDeviceAttributeMaxTexture3DAlt</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca3b576766317055e3bf321761fe5d84fd">hipDeviceAttributeMaxTextureCubemap</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caeab620ddac9e5520e0411fda9f6a5fb1">hipDeviceAttributeMaxTextureCubemapLayered</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5a4d13aaac8710b1d078306125f24e25">hipDeviceAttributeMaxThreadsDim</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8327aa23782d9c994bdef33a6d62e02e">hipDeviceAttributeMaxThreadsPerBlock</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caddc08922b491eb1f6a583833cbf4e2f0">hipDeviceAttributeMaxThreadsPerMultiProcessor</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca0b3f58899744df724961b664061afd54">hipDeviceAttributeMaxPitch</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca848c1396fab6f20463c6aefb828b0870">hipDeviceAttributeMemoryBusWidth</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6b68deafd65f036b30dc8051573eb000">hipDeviceAttributeMemoryClockRate</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca38edc4fcae456e47160d349da3249b85">hipDeviceAttributeComputeCapabilityMinor</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca7770672185967b47674798253cb7f47d">hipDeviceAttributeMultiGpuBoardGroupID</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5c1519870733ccf0b83f722678240e5f">hipDeviceAttributeMultiprocessorCount</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8dcc079d3099aadfd6d37c9614f91407">hipDeviceAttributeUnused1</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca21e422662a09d4894c8ebc60473384ff">hipDeviceAttributePageableMemoryAccess</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca14dff2a1b8c0ba131b06a6685bb052f3">hipDeviceAttributePageableMemoryAccessUsesHostPageTables</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca572b29c44f1322aa7657fdd784832f88">hipDeviceAttributePciBusId</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca955d90286e87be9e3528f0b817ab32ff">hipDeviceAttributePciDeviceId</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca83b77edfc8ef6044cc602af64969518c">hipDeviceAttributePciDomainId</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cadb8cdb8c1f1e140ae5340cf9fbe8aa8e">hipDeviceAttributePciDomainID</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca52d3c74a3d94c02ebfda31b32a0cd75a">hipDeviceAttributePersistingL2CacheMaxSize</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca82289b170192b6ea742be0efc6f95107">hipDeviceAttributeMaxRegistersPerBlock</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5f366458f31c0dc0f3faa0a11446ada4">hipDeviceAttributeMaxRegistersPerMultiprocessor</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cad612849d153747b7be03b0e697a2aead">hipDeviceAttributeReservedSharedMemPerBlock</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca7bca3aa18b26d40eba043ae93e15c7e5">hipDeviceAttributeMaxSharedMemoryPerBlock</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6299fb9b996d154c456d1622d447fe47">hipDeviceAttributeSharedMemPerBlockOptin</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cae88a51d68a16de43c9036bd1c555e0c9">hipDeviceAttributeSharedMemPerMultiprocessor</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5aa88c2c66ab8d71bb5b3177da16eecd">hipDeviceAttributeSingleToDoublePrecisionPerfRatio</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca7ace06929e3bb30616db62f966ad50db">hipDeviceAttributeStreamPrioritiesSupported</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca02af979ebb5db7921872c8eff4d667bd">hipDeviceAttributeSurfaceAlignment</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca0eb1b68cd4148e015736be9dc965caa4">hipDeviceAttributeTccDriver</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cac72b2427df2ba58dbbee2e1399b3e135">hipDeviceAttributeTextureAlignment</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cae044c1754ea66c8f9f7b420a2f14671e">hipDeviceAttributeTexturePitchAlignment</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cac6089ac3a0f9c77cc382fb0eaa73ae9c">hipDeviceAttributeTotalConstantMemory</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caad0e1bd8d5bb28ae8e0c710fd70bea29">hipDeviceAttributeTotalGlobalMem</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca72a250028cf4eac11a83410a86de83a4">hipDeviceAttributeUnifiedAddressing</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6d7bf28444bf5fe676c4260333e2da7c">hipDeviceAttributeUnused2</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caffd94133e823247a6f1215343232f6ec">hipDeviceAttributeWarpSize</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caef1d9fb1d5d0c6129903d93ddae8c4ca">hipDeviceAttributeMemoryPoolsSupported</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caecdccc51c9b30e22a154839d5827a615">hipDeviceAttributeVirtualMemoryManagementSupported</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cae7fc4b89d3474089f40e2206866f658a">hipDeviceAttributeHostRegisterSupported</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca85d831cf51005e06956c389c37d071bb">hipDeviceAttributeMemoryPoolSupportedHandleTypes</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caa360d503e92d5dfc48b373e863547441">hipDeviceAttributeHostNumaId</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca23a769372f05b3d4b1bf28a9fd46991a">hipDeviceAttributeCudaCompatibleEnd</a> = 9999
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5f195e2a51f8fb6fa40dbe443d2b0279">hipDeviceAttributeAmdSpecificBegin</a> = 10000
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caefd7213ecdc587ca7e74822d2ca97309">hipDeviceAttributeClockInstructionRate</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cac4750f9f64dfe4455e58c2ba7e073f87">hipDeviceAttributeUnused3</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cad3e7f3d01533b32e12211172fcf410ba">hipDeviceAttributeMaxSharedMemoryPerMultiprocessor</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4ff9d7bb9ee05b2ae28caa535a81dcf0">hipDeviceAttributeUnused4</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca1694fee46a4b2befda6ecb7e058f53fc">hipDeviceAttributeUnused5</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6c9f83e4239d19aa000dd13cbcfc00dd">hipDeviceAttributeHdpMemFlushCntl</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca49f4f8395025ba1ebe1a0a7eff0f24ed">hipDeviceAttributeHdpRegFlushCntl</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4d791a8a67ad0c89d413a67ce184be5d">hipDeviceAttributeCooperativeMultiDeviceUnmatchedFunc</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caa5679987f35a74bfcbb1d3ac36db73cb">hipDeviceAttributeCooperativeMultiDeviceUnmatchedGridDim</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caeb7c0c783e1f88a0675726bf2da6424b">hipDeviceAttributeCooperativeMultiDeviceUnmatchedBlockDim</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca3295f0728fc8152a98556d89ba81216f">hipDeviceAttributeCooperativeMultiDeviceUnmatchedSharedMem</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cab980fc82595b70b6338b9dd2b913ec26">hipDeviceAttributeIsLargeBar</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4e443d1d515e56a1f8cee4a9f3a7a546">hipDeviceAttributeAsicRevision</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8179e5c1507831eaeb4690513e618913">hipDeviceAttributeCanUseStreamWaitValue</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caaca61f2bab5521294fe5657fc7e6548c">hipDeviceAttributeImageSupport</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7cae5ef640fe3203e10381d220b0c46be66">hipDeviceAttributePhysicalMultiProcessorCount</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6f1528b1afa5f1a70cd47680b353f96d">hipDeviceAttributeFineGrainSupport</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca949a6be673b95e4af2c13f2003078e44">hipDeviceAttributeWallClockRate</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca3ac50041beb59111a5c76edf03da0898">hipDeviceAttributeNumberOfXccs</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4a50a99d2921accb565746e4a17dd669">hipDeviceAttributeMaxAvailableVgprsPerThread</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7caaaa98b5dee05f0ea04d08f61b0bddda9">hipDeviceAttributePciChipId</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca652aba6828121b90705663532992a059">hipDeviceAttributeAmdSpecificEnd</a> = 19999
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacc0acd7b9bda126c6bb3dfd6e2796d7ca9e5ce28ccb762bfb010dc35f4487d619">hipDeviceAttributeVendorSpecificBegin</a> = 20000
<br />
 }</td></tr>
<tr class="separator:gacc0acd7b9bda126c6bb3dfd6e2796d7c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga3e30b1faa389b4565cae7af03d5d3e76" id="r_ga3e30b1faa389b4565cae7af03d5d3e76"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga3e30b1faa389b4565cae7af03d5d3e76">hipDriverProcAddressQueryResult</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga3e30b1faa389b4565cae7af03d5d3e76a796004dd82889d925351ca710fd65d96">HIP_GET_PROC_ADDRESS_SUCCESS</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga3e30b1faa389b4565cae7af03d5d3e76a2575b187974521a7ac3a6ec0c4b1aad8">HIP_GET_PROC_ADDRESS_SYMBOL_NOT_FOUND</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga3e30b1faa389b4565cae7af03d5d3e76ab22f8a48ad16cbfa5c27e9ebba363723">HIP_GET_PROC_ADDRESS_VERSION_NOT_SUFFICIENT</a> = 2
<br />
 }</td></tr>
<tr class="separator:ga3e30b1faa389b4565cae7af03d5d3e76"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga35133e080ad8aecd57ec2c5387e3a376" id="r_ga35133e080ad8aecd57ec2c5387e3a376"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga35133e080ad8aecd57ec2c5387e3a376">hipComputeMode</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga35133e080ad8aecd57ec2c5387e3a376a9565a36ccb87755b51f42e1cf150bba6">hipComputeModeDefault</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga35133e080ad8aecd57ec2c5387e3a376a92d8c4babfb6cdce4c7db31d420f72ca">hipComputeModeExclusive</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga35133e080ad8aecd57ec2c5387e3a376a41e725f5f69f23e23eff05c4c64cfe8d">hipComputeModeProhibited</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga35133e080ad8aecd57ec2c5387e3a376a9d39a96ce69f00a1fd859a436ef6e060">hipComputeModeExclusiveProcess</a> = 3
<br />
 }</td></tr>
<tr class="separator:ga35133e080ad8aecd57ec2c5387e3a376"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga7f21ab1d42258d4f479a3bc4f420ac26" id="r_ga7f21ab1d42258d4f479a3bc4f420ac26"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga7f21ab1d42258d4f479a3bc4f420ac26">hipFlushGPUDirectRDMAWritesOptions</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga7f21ab1d42258d4f479a3bc4f420ac26a7ea9cfe68bb86afe0d797bb4ea9a7cd2">hipFlushGPUDirectRDMAWritesOptionHost</a> = 1 &lt;&lt; 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga7f21ab1d42258d4f479a3bc4f420ac26aa8e4e696581d4b8c3b2993ee5c4c472a">hipFlushGPUDirectRDMAWritesOptionMemOps</a> = 1 &lt;&lt; 1
<br />
 }</td></tr>
<tr class="separator:ga7f21ab1d42258d4f479a3bc4f420ac26"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaccd4ecfca4d2a5bfdad59e1f3953f665" id="r_gaccd4ecfca4d2a5bfdad59e1f3953f665"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaccd4ecfca4d2a5bfdad59e1f3953f665">hipGPUDirectRDMAWritesOrdering</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaccd4ecfca4d2a5bfdad59e1f3953f665a4c8affda770fec6151516a0a599958a5">hipGPUDirectRDMAWritesOrderingNone</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaccd4ecfca4d2a5bfdad59e1f3953f665a02317af92580a65cb1ed5f4958af9268">hipGPUDirectRDMAWritesOrderingOwner</a> = 100
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaccd4ecfca4d2a5bfdad59e1f3953f665a78519e9864647bcc6fdd4fbb0e4aeeb4">hipGPUDirectRDMAWritesOrderingAllDevices</a> = 200
<br />
 }</td></tr>
<tr class="separator:gaccd4ecfca4d2a5bfdad59e1f3953f665"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga5582537cfebefc286383a3abeb71f4d1" id="r_ga5582537cfebefc286383a3abeb71f4d1"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga5582537cfebefc286383a3abeb71f4d1">hipDeviceP2PAttr</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5582537cfebefc286383a3abeb71f4d1acda359cb54b8cc6654ccd470d2ae85b3">hipDevP2PAttrPerformanceRank</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5582537cfebefc286383a3abeb71f4d1a3ce64b7f78e8f5d2088a085182bdd703">hipDevP2PAttrAccessSupported</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5582537cfebefc286383a3abeb71f4d1a74da118b7d5fada7d20bade38a684fe8">hipDevP2PAttrNativeAtomicSupported</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5582537cfebefc286383a3abeb71f4d1a6e15f73f41e1c10fef0de092243d8a52">hipDevP2PAttrHipArrayAccessSupported</a>
<br />
 }</td></tr>
<tr class="separator:ga5582537cfebefc286383a3abeb71f4d1"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga991ce0e0446fc74c393cb35d788402ac" id="r_ga991ce0e0446fc74c393cb35d788402ac"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga991ce0e0446fc74c393cb35d788402ac">hipDriverEntryPointQueryResult</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga991ce0e0446fc74c393cb35d788402aca2e36ffb87a366a31ef49a0be950172eb">hipDriverEntryPointSuccess</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga991ce0e0446fc74c393cb35d788402aca88a1895e1ad3e3478a2e5f3ee52dfcd4">hipDriverEntryPointSymbolNotFound</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga991ce0e0446fc74c393cb35d788402acaa97575c9d073709455a2b2712b24b6dc">hipDriverEntryPointVersionNotSufficent</a> = 2
<br />
 }</td></tr>
<tr class="separator:ga991ce0e0446fc74c393cb35d788402ac"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga02ceb1513c852c4dd1ecf3cc459fda70" id="r_ga02ceb1513c852c4dd1ecf3cc459fda70"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga02ceb1513c852c4dd1ecf3cc459fda70">hipLimit_t</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga02ceb1513c852c4dd1ecf3cc459fda70a30214f21a523ab016abc833abde96486">hipLimitStackSize</a> = 0x0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga02ceb1513c852c4dd1ecf3cc459fda70a76d41da5f9a43671718a72237e783273">hipLimitPrintfFifoSize</a> = 0x01
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga02ceb1513c852c4dd1ecf3cc459fda70a1ec17519ca7e1fa12dde48d3a919d210">hipLimitMallocHeapSize</a> = 0x02
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga02ceb1513c852c4dd1ecf3cc459fda70a03fe8a1c0d40535160ee2fca6c38a7de">hipExtLimitScratchMin</a> = 0x1000
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga02ceb1513c852c4dd1ecf3cc459fda70a95da197cb0b890663d14c041c0f2f98d">hipExtLimitScratchMax</a> = 0x1001
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga02ceb1513c852c4dd1ecf3cc459fda70ac39843ab7052effa3c1be92dd4a6af6b">hipExtLimitScratchCurrent</a> = 0x1002
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga02ceb1513c852c4dd1ecf3cc459fda70a62987c6383927c7dbbbb02a770b71eb5">hipLimitRange</a>
<br />
 }</td></tr>
<tr class="separator:ga02ceb1513c852c4dd1ecf3cc459fda70"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga3cb603dcc7b6a7884fec90988149b72a" id="r_ga3cb603dcc7b6a7884fec90988149b72a"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga3cb603dcc7b6a7884fec90988149b72a">hipStreamBatchMemOpType</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga3cb603dcc7b6a7884fec90988149b72aaeb04b51c0497b95ee2d9fc7895fad4bc">hipStreamMemOpWaitValue32</a> = 0x1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga3cb603dcc7b6a7884fec90988149b72aad6a2b610d5d8fdea795be97991bc1db6">hipStreamMemOpWriteValue32</a> = 0x2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga3cb603dcc7b6a7884fec90988149b72aaec21f22ffacf0e874b31516438693aad">hipStreamMemOpWaitValue64</a> = 0x4
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga3cb603dcc7b6a7884fec90988149b72aa38a237828c1bbcce28a5338f09ad4ebf">hipStreamMemOpWriteValue64</a> = 0x5
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga3cb603dcc7b6a7884fec90988149b72aa690b461a80f7b48b111d7b94d18356af">hipStreamMemOpBarrier</a> = 0x6
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga3cb603dcc7b6a7884fec90988149b72aaed825058fa9b15a5f5e305f6fb8fe7b1">hipStreamMemOpFlushRemoteWrites</a> = 0x3
<br />
 }</td></tr>
<tr class="separator:ga3cb603dcc7b6a7884fec90988149b72a"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga2757323c1ac94b1d71f699fcbd5bdc2f" id="r_ga2757323c1ac94b1d71f699fcbd5bdc2f"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga2757323c1ac94b1d71f699fcbd5bdc2f">hipMemoryAdvise</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga2757323c1ac94b1d71f699fcbd5bdc2fafaeec0b64516ce7134b9ae80c2b7a3f5">hipMemAdviseSetReadMostly</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga2757323c1ac94b1d71f699fcbd5bdc2fafd2ae0ca621c454f44551ec654a29cf6">hipMemAdviseUnsetReadMostly</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga2757323c1ac94b1d71f699fcbd5bdc2facd018663520b26a64c6201a3efae1f15">hipMemAdviseSetPreferredLocation</a> = 3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga2757323c1ac94b1d71f699fcbd5bdc2fa6801ff205e3837d679aced24eb71e370">hipMemAdviseUnsetPreferredLocation</a> = 4
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga2757323c1ac94b1d71f699fcbd5bdc2fab516731448e70a8a48ada9314a869549">hipMemAdviseSetAccessedBy</a> = 5
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga2757323c1ac94b1d71f699fcbd5bdc2fa025ece7c72ff19784e1fe9fdb07e7e56">hipMemAdviseUnsetAccessedBy</a> = 6
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga2757323c1ac94b1d71f699fcbd5bdc2fa56145fb5a178f26cc758cbbaa17b8d86">hipMemAdviseSetCoarseGrain</a> = 100
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga2757323c1ac94b1d71f699fcbd5bdc2fa24256a97d088ab9a13e2ae2af21751c6">hipMemAdviseUnsetCoarseGrain</a> = 101
<br />
 }</td></tr>
<tr class="separator:ga2757323c1ac94b1d71f699fcbd5bdc2f"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gac1e4b99211365977c2a7a9d054b59765" id="r_gac1e4b99211365977c2a7a9d054b59765"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gac1e4b99211365977c2a7a9d054b59765">hipMemRangeCoherencyMode</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac1e4b99211365977c2a7a9d054b59765a300a479362ae193c4c51bc64fa411304">hipMemRangeCoherencyModeFineGrain</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac1e4b99211365977c2a7a9d054b59765af508599624e76d1a13bb23a9e6359834">hipMemRangeCoherencyModeCoarseGrain</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac1e4b99211365977c2a7a9d054b59765ad7e3bd29e10dbbfca7b550c97a034687">hipMemRangeCoherencyModeIndeterminate</a> = 2
<br />
 }</td></tr>
<tr class="separator:gac1e4b99211365977c2a7a9d054b59765"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga1e8d4a7cf5d1844fa34e4f9ac3bfcc63" id="r_ga1e8d4a7cf5d1844fa34e4f9ac3bfcc63"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga1e8d4a7cf5d1844fa34e4f9ac3bfcc63">hipMemRangeAttribute</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63a94a4c175d01932cf90eff033a302528c">hipMemRangeAttributeReadMostly</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63a135eda185c450dd8add5580c23bf37b8">hipMemRangeAttributePreferredLocation</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63a666534e4e8298c8d694dc745d9afe6ae">hipMemRangeAttributeAccessedBy</a> = 3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63a12c0540067c44b9f126da23edc523484">hipMemRangeAttributeLastPrefetchLocation</a> = 4
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63ad00a2b439bae60733943da9b27de4f08">hipMemRangeAttributeCoherencyMode</a> = 100
<br />
 }</td></tr>
<tr class="separator:ga1e8d4a7cf5d1844fa34e4f9ac3bfcc63"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga987c8e7a7e8171832a6647150854ca2e" id="r_ga987c8e7a7e8171832a6647150854ca2e"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga987c8e7a7e8171832a6647150854ca2e">hipMemPoolAttr</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga987c8e7a7e8171832a6647150854ca2eac0b660a866fc6c3ee87a8230d384532f">hipMemPoolReuseFollowEventDependencies</a> = 0x1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga987c8e7a7e8171832a6647150854ca2ead1da20661bcf84605088d3e20120b653">hipMemPoolReuseAllowOpportunistic</a> = 0x2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga987c8e7a7e8171832a6647150854ca2eaa1fa58a079f0a1b31aef2baf543a8dd7">hipMemPoolReuseAllowInternalDependencies</a> = 0x3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga987c8e7a7e8171832a6647150854ca2ea601b937cbdd057d30d4e136360e11220">hipMemPoolAttrReleaseThreshold</a> = 0x4
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga987c8e7a7e8171832a6647150854ca2ea4e4e69ffb29a939c6970467312bad712">hipMemPoolAttrReservedMemCurrent</a> = 0x5
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga987c8e7a7e8171832a6647150854ca2ea30c968e449328135ef9610f12e740582">hipMemPoolAttrReservedMemHigh</a> = 0x6
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga987c8e7a7e8171832a6647150854ca2ea0574c734ba2b79ba156a8e94739f07e5">hipMemPoolAttrUsedMemCurrent</a> = 0x7
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga987c8e7a7e8171832a6647150854ca2ea7d0d0e5e6ce19fdaaef2674a305930d0">hipMemPoolAttrUsedMemHigh</a> = 0x8
<br />
 }</td></tr>
<tr class="separator:ga987c8e7a7e8171832a6647150854ca2e"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gac20e3511da42142b23285e557e43facd" id="r_gac20e3511da42142b23285e557e43facd"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gac20e3511da42142b23285e557e43facd">hipMemAccessFlags</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac20e3511da42142b23285e557e43facda3fed6a3f2f6435894c1a9b0cc707bbaa">hipMemAccessFlagsProtNone</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac20e3511da42142b23285e557e43facda1246e2630cabcfdf92292952395b3bca">hipMemAccessFlagsProtRead</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac20e3511da42142b23285e557e43facda6c92304d286d8c38614e2b6b76b36734">hipMemAccessFlagsProtReadWrite</a> = 3
<br />
 }</td></tr>
<tr class="separator:gac20e3511da42142b23285e557e43facd"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gadefdae0569c5be4538c065396ed758f5" id="r_gadefdae0569c5be4538c065396ed758f5"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gadefdae0569c5be4538c065396ed758f5">hipMemAllocationType</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggadefdae0569c5be4538c065396ed758f5ab500eee492813b9c90ade2a8c852a3ae">hipMemAllocationTypeInvalid</a> = 0x0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggadefdae0569c5be4538c065396ed758f5a8b9b2a4595b9ff034a6a5d053c95c227">hipMemAllocationTypePinned</a> = 0x1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggadefdae0569c5be4538c065396ed758f5aab0b9e7ca7208f5d82e549346305410a">hipMemAllocationTypeUncached</a> = 0x40000000
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggadefdae0569c5be4538c065396ed758f5a7827526b3897c596109b6024bf38502a">hipMemAllocationTypeMax</a> = 0x7FFFFFFF
<br />
 }</td></tr>
<tr class="separator:gadefdae0569c5be4538c065396ed758f5"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga07b4aea600602a99d135dd2ca87faa92" id="r_ga07b4aea600602a99d135dd2ca87faa92"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga07b4aea600602a99d135dd2ca87faa92">hipMemAllocationHandleType</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga07b4aea600602a99d135dd2ca87faa92a72c5024a4f58cb4de197d6314e4c66a9">hipMemHandleTypeNone</a> = 0x0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga07b4aea600602a99d135dd2ca87faa92a9f261aad3214093c5b1aa2838b157d66">hipMemHandleTypePosixFileDescriptor</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga07b4aea600602a99d135dd2ca87faa92a3b7ddb718292009167abee4779fe03c8">hipMemHandleTypeWin32</a> = 0x2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga07b4aea600602a99d135dd2ca87faa92a54d89168742fee74bb05e02d3b699f46">hipMemHandleTypeWin32Kmt</a> = 0x4
<br />
 }</td></tr>
<tr class="separator:ga07b4aea600602a99d135dd2ca87faa92"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga4a800faf1ce60529b4f052a30ef10b85" id="r_ga4a800faf1ce60529b4f052a30ef10b85"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga4a800faf1ce60529b4f052a30ef10b85">hipFuncAttribute</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4a800faf1ce60529b4f052a30ef10b85a77db750682af411fb1aaef6b916e65ad">hipFuncAttributeMaxDynamicSharedMemorySize</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4a800faf1ce60529b4f052a30ef10b85a492a0ab1879358bbb039545bd899d527">hipFuncAttributePreferredSharedMemoryCarveout</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4a800faf1ce60529b4f052a30ef10b85a78119858f4a6a22782ce980b8ce4fb95">hipFuncAttributeMax</a>
<br />
 }</td></tr>
<tr class="separator:ga4a800faf1ce60529b4f052a30ef10b85"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga86e5c5692645963a9a673e1aa88ba6ca" id="r_ga86e5c5692645963a9a673e1aa88ba6ca"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga86e5c5692645963a9a673e1aa88ba6ca">hipFuncCache_t</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga86e5c5692645963a9a673e1aa88ba6caa0813fbaa008ce1231ff9fed3911eb3af">hipFuncCachePreferNone</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga86e5c5692645963a9a673e1aa88ba6caa9b34337dfbadba25ed2aa270bbcabc43">hipFuncCachePreferShared</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga86e5c5692645963a9a673e1aa88ba6caa636a3c140db6b9d4a8bf7d5a61c398c5">hipFuncCachePreferL1</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga86e5c5692645963a9a673e1aa88ba6caa0ddab0e840107634a152033103be44d7">hipFuncCachePreferEqual</a>
<br />
 }</td></tr>
<tr class="separator:ga86e5c5692645963a9a673e1aa88ba6ca"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga2e17b71d94ac350f2ccd914fd49d104e" id="r_ga2e17b71d94ac350f2ccd914fd49d104e"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga2e17b71d94ac350f2ccd914fd49d104e">hipSharedMemConfig</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga2e17b71d94ac350f2ccd914fd49d104eaf5b325c9b7bde878913f768eaba5014d">hipSharedMemBankSizeDefault</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga2e17b71d94ac350f2ccd914fd49d104ea0a95a6e0c33106c42d66ab9476ff954a">hipSharedMemBankSizeFourByte</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga2e17b71d94ac350f2ccd914fd49d104ea64518b4f5a25f536c883330167e79258">hipSharedMemBankSizeEightByte</a>
<br />
 }</td></tr>
<tr class="separator:ga2e17b71d94ac350f2ccd914fd49d104e"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga47a3a9058e535f2a43a20982c39031bb" id="r_ga47a3a9058e535f2a43a20982c39031bb"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga47a3a9058e535f2a43a20982c39031bb">hipExternalMemoryHandleType</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga47a3a9058e535f2a43a20982c39031bba754a120bc60fcfbf5f5290967c2bd299">hipExternalMemoryHandleTypeOpaqueFd</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga47a3a9058e535f2a43a20982c39031bbab289071d76ed3fa028b0b72d6fe57863">hipExternalMemoryHandleTypeOpaqueWin32</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga47a3a9058e535f2a43a20982c39031bbaa6231ff4442f793dc4472c406373909b">hipExternalMemoryHandleTypeOpaqueWin32Kmt</a> = 3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga47a3a9058e535f2a43a20982c39031bba84a3c0206a80b99170a9d9196d28d6d4">hipExternalMemoryHandleTypeD3D12Heap</a> = 4
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga47a3a9058e535f2a43a20982c39031bba2e2c241fcec7b8fcf092e271df4d900f">hipExternalMemoryHandleTypeD3D12Resource</a> = 5
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga47a3a9058e535f2a43a20982c39031bba07b9b9bd3833c3f66bae6d13f66c7f67">hipExternalMemoryHandleTypeD3D11Resource</a> = 6
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga47a3a9058e535f2a43a20982c39031bbad703b9b79a0f0d36eb8530ec81c0c4a0">hipExternalMemoryHandleTypeD3D11ResourceKmt</a> = 7
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga47a3a9058e535f2a43a20982c39031bba45c9deab844e97f375ea28bec2877312">hipExternalMemoryHandleTypeNvSciBuf</a> = 8
<br />
 }</td></tr>
<tr class="separator:ga47a3a9058e535f2a43a20982c39031bb"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga4ea2e2748bf8cefee1d1cc3c800c10d5" id="r_ga4ea2e2748bf8cefee1d1cc3c800c10d5"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga4ea2e2748bf8cefee1d1cc3c800c10d5">hipExternalSemaphoreHandleType</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4ea2e2748bf8cefee1d1cc3c800c10d5acb2af352ae589486b706635b5f273911">hipExternalSemaphoreHandleTypeOpaqueFd</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4ea2e2748bf8cefee1d1cc3c800c10d5aeb0d35bd0276f67e86091dc3969355ac">hipExternalSemaphoreHandleTypeOpaqueWin32</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4ea2e2748bf8cefee1d1cc3c800c10d5a44c1a257f0e2605f6efd44741851e8d7">hipExternalSemaphoreHandleTypeOpaqueWin32Kmt</a> = 3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4ea2e2748bf8cefee1d1cc3c800c10d5afff89d172e5aad8afea7021c55fa4fc1">hipExternalSemaphoreHandleTypeD3D12Fence</a> = 4
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4ea2e2748bf8cefee1d1cc3c800c10d5aa8d81456306ed714fb2ff92026a27dbe">hipExternalSemaphoreHandleTypeD3D11Fence</a> = 5
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4ea2e2748bf8cefee1d1cc3c800c10d5a317541984f3cd4af445918d4ac63ea64">hipExternalSemaphoreHandleTypeNvSciSync</a> = 6
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4ea2e2748bf8cefee1d1cc3c800c10d5a4e869593fe59e351dd981d7a4de95ec5">hipExternalSemaphoreHandleTypeKeyedMutex</a> = 7
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4ea2e2748bf8cefee1d1cc3c800c10d5a3c536b1ed5fdfd7618738ee61633e7a0">hipExternalSemaphoreHandleTypeKeyedMutexKmt</a> = 8
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4ea2e2748bf8cefee1d1cc3c800c10d5aef4e7167a49308a989588fcef88fbefe">hipExternalSemaphoreHandleTypeTimelineSemaphoreFd</a> = 9
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4ea2e2748bf8cefee1d1cc3c800c10d5aca482a93b49594fcc837429db03d96f1">hipExternalSemaphoreHandleTypeTimelineSemaphoreWin32</a> = 10
<br />
 }</td></tr>
<tr class="separator:ga4ea2e2748bf8cefee1d1cc3c800c10d5"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gabb8a4ae6dc64f7315c302c5b3b6e1c59" id="r_gabb8a4ae6dc64f7315c302c5b3b6e1c59"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gabb8a4ae6dc64f7315c302c5b3b6e1c59">hipGraphicsRegisterFlags</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggabb8a4ae6dc64f7315c302c5b3b6e1c59aadea95241fb75cc9ce058b8a42007734">hipGraphicsRegisterFlagsNone</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggabb8a4ae6dc64f7315c302c5b3b6e1c59a16e70253402db71a1c1b073755494a03">hipGraphicsRegisterFlagsReadOnly</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggabb8a4ae6dc64f7315c302c5b3b6e1c59a5d3ee9600bd812fd1f1c26f66c77e881">hipGraphicsRegisterFlagsWriteDiscard</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggabb8a4ae6dc64f7315c302c5b3b6e1c59af1e660943886c56aef11ed34c8ee86f0">hipGraphicsRegisterFlagsSurfaceLoadStore</a> = 4
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggabb8a4ae6dc64f7315c302c5b3b6e1c59a4f30ff3c46b068f0e5d138c3d9bfff11">hipGraphicsRegisterFlagsTextureGather</a>
<br />
 }</td></tr>
<tr class="separator:gabb8a4ae6dc64f7315c302c5b3b6e1c59"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga4727d20b89566832c74b762f987b9728" id="r_ga4727d20b89566832c74b762f987b9728"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga4727d20b89566832c74b762f987b9728">hipGraphNodeType</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728a9949391db00445f7a4a0b0465d093e36">hipGraphNodeTypeKernel</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728a635989252eae22c3002a001d63e1cb27">hipGraphNodeTypeMemcpy</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728a3cbfa0e34c1665922fab5abc77c213a1">hipGraphNodeTypeMemset</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728aada6f6582063a8a1db454d4950d05f1f">hipGraphNodeTypeHost</a> = 3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728a3c0d48ee17536fa328c7f688cea29341">hipGraphNodeTypeGraph</a> = 4
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728ad4f074d6484c61be503b22addd170f5d">hipGraphNodeTypeEmpty</a> = 5
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728a6ecc1f3e6df39acdb8fd75ee6c7596f4">hipGraphNodeTypeWaitEvent</a> = 6
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728a40f8dc14f77efa8409c763d9014f2f79">hipGraphNodeTypeEventRecord</a> = 7
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728a5cfa4c3858247a14c618e2c648ed1c3d">hipGraphNodeTypeExtSemaphoreSignal</a> = 8
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728adde9842fa2d0f9eccc94058f6d40c69f">hipGraphNodeTypeExtSemaphoreWait</a> = 9
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728ab2f8761e77c317de516ee923db962229">hipGraphNodeTypeMemAlloc</a> = 10
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728ac8264d54af4199cd9194611932db6883">hipGraphNodeTypeMemFree</a> = 11
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728ad1dfcaa91d4817fae0940b911ea74460">hipGraphNodeTypeMemcpyFromSymbol</a> = 12
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728ad1e85c6612c6e59fb9188c9ca87fb64f">hipGraphNodeTypeMemcpyToSymbol</a> = 13
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728a0d03f67f5d3e19c0fc343818cc60f693">hipGraphNodeTypeBatchMemOp</a> = 14
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4727d20b89566832c74b762f987b9728a8669923fef17da304f3f5189615b054f">hipGraphNodeTypeCount</a>
<br />
 }</td></tr>
<tr class="separator:ga4727d20b89566832c74b762f987b9728"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga193abcc67d55b127bc5c0bc3625de907" id="r_ga193abcc67d55b127bc5c0bc3625de907"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga193abcc67d55b127bc5c0bc3625de907">hipAccessProperty</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga193abcc67d55b127bc5c0bc3625de907a5e691c3d2417d1fabbd2eb753829db97">hipAccessPropertyNormal</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga193abcc67d55b127bc5c0bc3625de907ac4b5d4099632e30e4c21c77490290319">hipAccessPropertyStreaming</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga193abcc67d55b127bc5c0bc3625de907aa1a91b8045c860f890f8741de827f92f">hipAccessPropertyPersisting</a> = 2
<br />
 }</td></tr>
<tr class="separator:ga193abcc67d55b127bc5c0bc3625de907"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga503fd3aecee14969a1e48a41bc8b16c1" id="r_ga503fd3aecee14969a1e48a41bc8b16c1"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga503fd3aecee14969a1e48a41bc8b16c1">hipLaunchMemSyncDomain</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga503fd3aecee14969a1e48a41bc8b16c1a6d069ee68549d463bc7b873b1f3631d5">hipLaunchMemSyncDomainDefault</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga503fd3aecee14969a1e48a41bc8b16c1a20b07e28748e19c3aacdeadd53860a02">hipLaunchMemSyncDomainRemote</a> = 1
<br />
 }</td></tr>
<tr class="separator:ga503fd3aecee14969a1e48a41bc8b16c1"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga46aec5b8c6c0302e179d82693f3b1243" id="r_ga46aec5b8c6c0302e179d82693f3b1243"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga46aec5b8c6c0302e179d82693f3b1243">hipSynchronizationPolicy</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga46aec5b8c6c0302e179d82693f3b1243aadc2aeaed10849c3a75b818b593afdf9">hipSyncPolicyAuto</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga46aec5b8c6c0302e179d82693f3b1243af0cd9e0cdc6c920c7bac2e545f2a7e8b">hipSyncPolicySpin</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga46aec5b8c6c0302e179d82693f3b1243a287d7e82eb8904eb707bd46c65a697f3">hipSyncPolicyYield</a> = 3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga46aec5b8c6c0302e179d82693f3b1243aacf44cd40fb89bdd37d313f2739e918e">hipSyncPolicyBlockingSync</a> = 4
<br />
 }</td></tr>
<tr class="separator:ga46aec5b8c6c0302e179d82693f3b1243"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga4026e9ccca8bb88888ad739e0f7586b4" id="r_ga4026e9ccca8bb88888ad739e0f7586b4"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga4026e9ccca8bb88888ad739e0f7586b4">hipLaunchAttributeID</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4ae9c06559f2a188eb87818348cefc4171">hipLaunchAttributeAccessPolicyWindow</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4af2e2bdbec3458fd4810e9d18b9e527af">hipLaunchAttributeCooperative</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4aac7011b4266fc8e091a1048326da38b7">hipLaunchAttributeSynchronizationPolicy</a> = 3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4a358f69dfec66d2cfe93b25f44845bcc1">hipLaunchAttributePriority</a> = 8
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4a9229ce145edcc4442002d8ee2d156cc3">hipLaunchAttributeMemSyncDomainMap</a> = 9
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4a71ab9ea6aef993bbcaac9798a1445023">hipLaunchAttributeMemSyncDomain</a> = 10
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4a3942a0c67db2d9b4ddd1f6fbc04d59ea">hipLaunchAttributeMax</a>
<br />
 }</td></tr>
<tr class="separator:ga4026e9ccca8bb88888ad739e0f7586b4"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gac79a2b2c0f83ae81c9325978c044892e" id="r_gac79a2b2c0f83ae81c9325978c044892e"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gac79a2b2c0f83ae81c9325978c044892e">hipGraphExecUpdateResult</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac79a2b2c0f83ae81c9325978c044892eac1f2b2a324b22bbca94f6c4f21039d8f">hipGraphExecUpdateSuccess</a> = 0x0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac79a2b2c0f83ae81c9325978c044892ea67878e33ef3ec61463a920f149e082fe">hipGraphExecUpdateError</a> = 0x1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac79a2b2c0f83ae81c9325978c044892ea25d787d82ab0b453c931b676272ba75b">hipGraphExecUpdateErrorTopologyChanged</a> = 0x2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac79a2b2c0f83ae81c9325978c044892ea1f13abf8d4c8b14e7db99a224cc1620b">hipGraphExecUpdateErrorNodeTypeChanged</a> = 0x3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac79a2b2c0f83ae81c9325978c044892eaa1c53ed0892dc10db16e4e229ff784e9">hipGraphExecUpdateErrorFunctionChanged</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac79a2b2c0f83ae81c9325978c044892eaddd407406093becb360f4f971e672d47">hipGraphExecUpdateErrorParametersChanged</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac79a2b2c0f83ae81c9325978c044892ea0445beac1f3c3235e7f4ed315e17fba0">hipGraphExecUpdateErrorNotSupported</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac79a2b2c0f83ae81c9325978c044892ea2cdf6a53a1434e4773cdc54a4d312a17">hipGraphExecUpdateErrorUnsupportedFunctionChange</a> = 0x7
<br />
 }</td></tr>
<tr class="separator:gac79a2b2c0f83ae81c9325978c044892e"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga3ae2cd03e623963eba9e0064d270ce4c" id="r_ga3ae2cd03e623963eba9e0064d270ce4c"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga3ae2cd03e623963eba9e0064d270ce4c">hipStreamCaptureMode</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga3ae2cd03e623963eba9e0064d270ce4ca8e07e28586b1178e96e310f983c4a5d2">hipStreamCaptureModeGlobal</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga3ae2cd03e623963eba9e0064d270ce4ca42813de2ec53c9ada7ff8b6f3961bf6e">hipStreamCaptureModeThreadLocal</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga3ae2cd03e623963eba9e0064d270ce4ca0b1aab61f226d1c7e40ba090f7fca255">hipStreamCaptureModeRelaxed</a>
<br />
 }</td></tr>
<tr class="separator:ga3ae2cd03e623963eba9e0064d270ce4c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gacb066bac5e39dd1b82926e02db1756a7" id="r_gacb066bac5e39dd1b82926e02db1756a7"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gacb066bac5e39dd1b82926e02db1756a7">hipStreamCaptureStatus</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacb066bac5e39dd1b82926e02db1756a7a8c4ef8104913161030ff321b1454d4c3">hipStreamCaptureStatusNone</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacb066bac5e39dd1b82926e02db1756a7abf89793c47e573fd8da9afad98d442d9">hipStreamCaptureStatusActive</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggacb066bac5e39dd1b82926e02db1756a7a0d6ad4c0e0e50ddab3cf3b87ac7f38ce">hipStreamCaptureStatusInvalidated</a>
<br />
 }</td></tr>
<tr class="separator:gacb066bac5e39dd1b82926e02db1756a7"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga76c22e13ab588b0a551814adca12e91a" id="r_ga76c22e13ab588b0a551814adca12e91a"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga76c22e13ab588b0a551814adca12e91a">hipStreamUpdateCaptureDependenciesFlags</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga76c22e13ab588b0a551814adca12e91aa46f516525ec015f5075adae5b9796187">hipStreamAddCaptureDependencies</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga76c22e13ab588b0a551814adca12e91aab0016a2fc2ce71f217ddc2717e9433aa">hipStreamSetCaptureDependencies</a>
<br />
 }</td></tr>
<tr class="separator:ga76c22e13ab588b0a551814adca12e91a"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga920ab2073b2ff77f37ae672d376ffe7e" id="r_ga920ab2073b2ff77f37ae672d376ffe7e"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga920ab2073b2ff77f37ae672d376ffe7e">hipGraphMemAttributeType</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga920ab2073b2ff77f37ae672d376ffe7ea4a7f157d4ca32bf67d3cb8760692e44b">hipGraphMemAttrUsedMemCurrent</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga920ab2073b2ff77f37ae672d376ffe7ea9bed75ed79b9d7f7baa9432c162be774">hipGraphMemAttrUsedMemHigh</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga920ab2073b2ff77f37ae672d376ffe7ead23bfe68f6bda084c491303c36fdd278">hipGraphMemAttrReservedMemCurrent</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga920ab2073b2ff77f37ae672d376ffe7ea333e093c34ad2272c53f96efe3cb9717">hipGraphMemAttrReservedMemHigh</a>
<br />
 }</td></tr>
<tr class="separator:ga920ab2073b2ff77f37ae672d376ffe7e"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga87db9f321bad9b03ff2859f4509791f2" id="r_ga87db9f321bad9b03ff2859f4509791f2"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga87db9f321bad9b03ff2859f4509791f2">hipUserObjectFlags</a> { <a class="el" href="group___global_defs.html#gga87db9f321bad9b03ff2859f4509791f2a027010c7f334c1d21b77da618b20928b">hipUserObjectNoDestructorSync</a> = 0x1
 }</td></tr>
<tr class="separator:ga87db9f321bad9b03ff2859f4509791f2"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga614792f2c22f324d4125f616ceb5afda" id="r_ga614792f2c22f324d4125f616ceb5afda"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga614792f2c22f324d4125f616ceb5afda">hipUserObjectRetainFlags</a> { <a class="el" href="group___global_defs.html#gga614792f2c22f324d4125f616ceb5afdaaf3e94cc868dccc75612acfafc23b86de">hipGraphUserObjectMove</a> = 0x1
 }</td></tr>
<tr class="separator:ga614792f2c22f324d4125f616ceb5afda"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaedc0107efcf1bd34d95e42cc04fa28f4" id="r_gaedc0107efcf1bd34d95e42cc04fa28f4"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaedc0107efcf1bd34d95e42cc04fa28f4">hipGraphInstantiateFlags</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaedc0107efcf1bd34d95e42cc04fa28f4a5db4094d6829b599d4c47c25cd4dfb87">hipGraphInstantiateFlagAutoFreeOnLaunch</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaedc0107efcf1bd34d95e42cc04fa28f4a9df2be596a2520102068529ab4477c8a">hipGraphInstantiateFlagUpload</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaedc0107efcf1bd34d95e42cc04fa28f4ab1bf70c734aea099510b9157914a6515">hipGraphInstantiateFlagDeviceLaunch</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaedc0107efcf1bd34d95e42cc04fa28f4a8f535452f119e17823fb674d9b9f693f">hipGraphInstantiateFlagUseNodePriority</a>
<br />
 }</td></tr>
<tr class="separator:gaedc0107efcf1bd34d95e42cc04fa28f4"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga5f0b6b05428bbd208a4adba36bbf3036" id="r_ga5f0b6b05428bbd208a4adba36bbf3036"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga5f0b6b05428bbd208a4adba36bbf3036">hipGraphDebugDotFlags</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5f0b6b05428bbd208a4adba36bbf3036af0c573ee94c6758b5eabf5f4f13d408f">hipGraphDebugDotFlagsVerbose</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5f0b6b05428bbd208a4adba36bbf3036a5180492c462e92a98fabcb0454f69aef">hipGraphDebugDotFlagsKernelNodeParams</a> = 1 &lt;&lt; 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5f0b6b05428bbd208a4adba36bbf3036af643dcafad92388a9532e94dd671ecf9">hipGraphDebugDotFlagsMemcpyNodeParams</a> = 1 &lt;&lt; 3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5f0b6b05428bbd208a4adba36bbf3036a162e1cc37582c814278a8a257f65255e">hipGraphDebugDotFlagsMemsetNodeParams</a> = 1 &lt;&lt; 4
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5f0b6b05428bbd208a4adba36bbf3036ac3530926183d0cef94a74b6bd94ea07f">hipGraphDebugDotFlagsHostNodeParams</a> = 1 &lt;&lt; 5
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5f0b6b05428bbd208a4adba36bbf3036ad9104a8ce1454c6d536e363724e18dad">hipGraphDebugDotFlagsEventNodeParams</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5f0b6b05428bbd208a4adba36bbf3036ab3497ea43f2e47877d8e96a0e97b7225">hipGraphDebugDotFlagsExtSemasSignalNodeParams</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5f0b6b05428bbd208a4adba36bbf3036a7669e2948dd9b9ce1b18144b2dacce66">hipGraphDebugDotFlagsExtSemasWaitNodeParams</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5f0b6b05428bbd208a4adba36bbf3036a0acef45295f4817dce9f90e70aacfe9e">hipGraphDebugDotFlagsKernelNodeAttributes</a>
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga5f0b6b05428bbd208a4adba36bbf3036a9f0cd5093721d6ee605d48074f110c65">hipGraphDebugDotFlagsHandles</a>
<br />
 }</td></tr>
<tr class="separator:ga5f0b6b05428bbd208a4adba36bbf3036"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga1275741e4687f414904caae01fecfd2f" id="r_ga1275741e4687f414904caae01fecfd2f"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga1275741e4687f414904caae01fecfd2f">hipGraphInstantiateResult</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga1275741e4687f414904caae01fecfd2fabcf7aafc228a6c17c7405160d0e32e70">hipGraphInstantiateSuccess</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga1275741e4687f414904caae01fecfd2fa93eaf8955b0c17e270bc2231c7dfeaa2">hipGraphInstantiateError</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga1275741e4687f414904caae01fecfd2fa961222f2a70390abbf60f71ed878cf65">hipGraphInstantiateInvalidStructure</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga1275741e4687f414904caae01fecfd2fa3c30667e32eb738974b1455d3f23b7c6">hipGraphInstantiateNodeOperationNotSupported</a> = 3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga1275741e4687f414904caae01fecfd2fa4ec62027dbfb29cbd365e9c94f5f325e">hipGraphInstantiateMultipleDevicesNotSupported</a> = 4
<br />
 }</td></tr>
<tr class="separator:ga1275741e4687f414904caae01fecfd2f"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gac339d242785822f679962c10b45037c8" id="r_gac339d242785822f679962c10b45037c8"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gac339d242785822f679962c10b45037c8">hipMemAllocationGranularity_flags</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac339d242785822f679962c10b45037c8abdb60c08374a9bdf35b86ae3d6650597">hipMemAllocationGranularityMinimum</a> = 0x0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggac339d242785822f679962c10b45037c8ae21e3d97d84b2c61d2aee2b2a9293c34">hipMemAllocationGranularityRecommended</a> = 0x1
<br />
 }</td></tr>
<tr class="separator:gac339d242785822f679962c10b45037c8"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga7a1387fab190ef8404d955871eeaa7fa" id="r_ga7a1387fab190ef8404d955871eeaa7fa"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga7a1387fab190ef8404d955871eeaa7fa">hipMemHandleType</a> { <a class="el" href="group___global_defs.html#gga7a1387fab190ef8404d955871eeaa7faad503b171c92fc9e224ed41f49ab5fef7">hipMemHandleTypeGeneric</a> = 0x0
 }</td></tr>
<tr class="separator:ga7a1387fab190ef8404d955871eeaa7fa"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gab6a581b72da85bebd9a6e02a27e22d49" id="r_gab6a581b72da85bebd9a6e02a27e22d49"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gab6a581b72da85bebd9a6e02a27e22d49">hipMemOperationType</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggab6a581b72da85bebd9a6e02a27e22d49a003c437dbe8ae98e1cb7ad0837b1d489">hipMemOperationTypeMap</a> = 0x1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggab6a581b72da85bebd9a6e02a27e22d49a341e660cc0facbb2576d70817eed0fc5">hipMemOperationTypeUnmap</a> = 0x2
<br />
 }</td></tr>
<tr class="separator:gab6a581b72da85bebd9a6e02a27e22d49"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gafd065a07554c87b025803c4b0bb98c0c" id="r_gafd065a07554c87b025803c4b0bb98c0c"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gafd065a07554c87b025803c4b0bb98c0c">hipArraySparseSubresourceType</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggafd065a07554c87b025803c4b0bb98c0ca4950320e5bdbe31969dbf76b1112023c">hipArraySparseSubresourceTypeSparseLevel</a> = 0x0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggafd065a07554c87b025803c4b0bb98c0ca662c94e0dc0635529c2c003cf64d3bdf">hipArraySparseSubresourceTypeMiptail</a> = 0x1
<br />
 }</td></tr>
<tr class="separator:gafd065a07554c87b025803c4b0bb98c0c"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga1dae8774d48cdf98a0bcf4b0d7a3aafb" id="r_ga1dae8774d48cdf98a0bcf4b0d7a3aafb"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga1dae8774d48cdf98a0bcf4b0d7a3aafb">hipGraphDependencyType</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga1dae8774d48cdf98a0bcf4b0d7a3aafba3c323771897c596a9340f72e451109c0">hipGraphDependencyTypeDefault</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga1dae8774d48cdf98a0bcf4b0d7a3aafbaa85b51c1b1c8c38b3db3ea11b9e406ce">hipGraphDependencyTypeProgrammatic</a> = 1
<br />
 }</td></tr>
<tr class="separator:ga1dae8774d48cdf98a0bcf4b0d7a3aafb"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga04d1e286b2c0a6bd0fcb0c8a0840782e" id="r_ga04d1e286b2c0a6bd0fcb0c8a0840782e"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga04d1e286b2c0a6bd0fcb0c8a0840782e">hipMemRangeHandleType</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga04d1e286b2c0a6bd0fcb0c8a0840782eac1dfb4123f249838b37110a6ff1e2f8d">hipMemRangeHandleTypeDmaBufFd</a> = 0x1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga04d1e286b2c0a6bd0fcb0c8a0840782eaba654afb15049bffda6169071a3d9ab6">hipMemRangeHandleTypeMax</a> = 0x7fffffff
<br />
 }</td></tr>
<tr class="separator:ga04d1e286b2c0a6bd0fcb0c8a0840782e"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga9e9efb47c0fd633ee7a25cbc18d16cf3" id="r_ga9e9efb47c0fd633ee7a25cbc18d16cf3"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga9e9efb47c0fd633ee7a25cbc18d16cf3">hipMemRangeFlags</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga9e9efb47c0fd633ee7a25cbc18d16cf3aca415bce635dee749a0cf90afee5492c">hipMemRangeFlagDmaBufMappingTypePcie</a> = 0x1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga9e9efb47c0fd633ee7a25cbc18d16cf3a16f93156ec0e7c102d809ec69f1a39bc">hipMemRangeFlagsMax</a> = 0x7fffffff
<br />
 }</td></tr>
<tr class="separator:ga9e9efb47c0fd633ee7a25cbc18d16cf3"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaaab4f1f28ef296fc6218b1ca8d21a6e9" id="r_gaaab4f1f28ef296fc6218b1ca8d21a6e9"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#gaaab4f1f28ef296fc6218b1ca8d21a6e9">hiprtcResult</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9ab81164860f4404a742c0972867e178e2">HIPRTC_SUCCESS</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9ad9863c0cdec84a87cb37fbe071ff8f0a">HIPRTC_ERROR_OUT_OF_MEMORY</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9a0d31deb90b120cbf8a94c30e6be27718">HIPRTC_ERROR_PROGRAM_CREATION_FAILURE</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9a8af2964e85221c54309e50ea4a0dd79e">HIPRTC_ERROR_INVALID_INPUT</a> = 3
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9a37d841d4dd1bae0e5e2cd1df2c24e795">HIPRTC_ERROR_INVALID_PROGRAM</a> = 4
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9a83af982bfeefbef92066ecf652131256">HIPRTC_ERROR_INVALID_OPTION</a> = 5
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9ad2b17befbe962616ab95250d40c8e62b">HIPRTC_ERROR_COMPILATION</a> = 6
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9abe35c9e3a6ced42320085125bf400480">HIPRTC_ERROR_BUILTIN_OPERATION_FAILURE</a> = 7
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9a40cdc896c8f49fe4d13f2df51f09aaa3">HIPRTC_ERROR_NO_NAME_EXPRESSIONS_AFTER_COMPILATION</a> = 8
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9ab5b7de5fc47672db6541f3973f3bf7b2">HIPRTC_ERROR_NO_LOWERED_NAMES_BEFORE_COMPILATION</a> = 9
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9a8fcdce6a190a32526947d5285f16faf9">HIPRTC_ERROR_NAME_EXPRESSION_NOT_VALID</a> = 10
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9ac8e5161c2d09c3757b1e4609e2b99313">HIPRTC_ERROR_INTERNAL_ERROR</a> = 11
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#ggaaab4f1f28ef296fc6218b1ca8d21a6e9ade69dfa707075ad89d45c79d31825cba">HIPRTC_ERROR_LINKING</a> = 100
<br />
 }</td></tr>
<tr class="separator:gaaab4f1f28ef296fc6218b1ca8d21a6e9"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga10719d9de09329f1a8947796b87f5844" id="r_ga10719d9de09329f1a8947796b87f5844"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___global_defs.html#ga10719d9de09329f1a8947796b87f5844">hipGLDeviceList</a> { <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga10719d9de09329f1a8947796b87f5844a0b709df4695dc4daed5577437411ea75">hipGLDeviceListAll</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga10719d9de09329f1a8947796b87f5844a71f10703a8678c6fc465e734ab8428a5">hipGLDeviceListCurrentFrame</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___global_defs.html#gga10719d9de09329f1a8947796b87f5844a00eef2e8d4116eabbd5d241ba782fed8">hipGLDeviceListNextFrame</a> = 3
<br />
 }</td></tr>
<tr class="separator:ga10719d9de09329f1a8947796b87f5844"><td class="memSeparator" colspan="2">&#160;</td></tr>
</table>
<a name="details" id="details"></a><h2 class="groupheader">Detailed Description</h2>
<h2 class="groupheader">Macro Definition Documentation</h2>
<a id="ga0f49b614c87c5d703133fbc52fc68670" name="ga0f49b614c87c5d703133fbc52fc68670"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga0f49b614c87c5d703133fbc52fc68670">&#9670;&#160;</a></span>__dparm</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define __dparm</td>
          <td>(</td>
          <td class="paramtype">&#160;</td>
          <td class="paramname">x</td><td>)</td>
          <td>&#160;&#160;&#160;= x</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga89716f0e21b750a51ceb081208a84b33" name="ga89716f0e21b750a51ceb081208a84b33"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga89716f0e21b750a51ceb081208a84b33">&#9670;&#160;</a></span>__HIP_NODISCARD</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define __HIP_NODISCARD</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga9a93afd2ec3f43ce2612feb962c67ced" name="ga9a93afd2ec3f43ce2612feb962c67ced"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga9a93afd2ec3f43ce2612feb962c67ced">&#9670;&#160;</a></span>GENERIC_GRID_LAUNCH</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define GENERIC_GRID_LAUNCH&#160;&#160;&#160;1</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gad6f100bd2ecab24ac448506698cba686" name="gad6f100bd2ecab24ac448506698cba686"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gad6f100bd2ecab24ac448506698cba686">&#9670;&#160;</a></span>HIP_DEPRECATED</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIP_DEPRECATED</td>
          <td>(</td>
          <td class="paramtype">&#160;</td>
          <td class="paramname">msg</td><td>)</td>
          <td>&#160;&#160;&#160;__attribute__((deprecated(msg)))</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga3f6fb51f33c412366ee1c42e34e71a05" name="ga3f6fb51f33c412366ee1c42e34e71a05"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga3f6fb51f33c412366ee1c42e34e71a05">&#9670;&#160;</a></span>HIP_DEPRECATED_MSG</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIP_DEPRECATED_MSG</td>
        </tr>
      </table>
</div><div class="memdoc">
<b>Value:</b><div class="fragment"><div class="line">  <span class="stringliteral">&quot;This API is marked as deprecated and might not be supported in future releases. For more &quot;</span>      \</div>
<div class="line">  <span class="stringliteral">&quot;details please refer &quot;</span>                                                                          \</div>
<div class="line">  <span class="stringliteral">&quot;https://github.com/ROCm/HIP/blob/develop/docs/reference/deprecated_api_list.md&quot;</span></div>
</div><!-- fragment -->
</div>
</div>
<a id="gaf095c042450b241001894e1578d71acd" name="gaf095c042450b241001894e1578d71acd"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaf095c042450b241001894e1578d71acd">&#9670;&#160;</a></span>HIP_IPC_HANDLE_SIZE</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIP_IPC_HANDLE_SIZE&#160;&#160;&#160;64</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gab78d63242f906b6d92cf766bd88a1898" name="gab78d63242f906b6d92cf766bd88a1898"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gab78d63242f906b6d92cf766bd88a1898">&#9670;&#160;</a></span>HIP_LAUNCH_PARAM_BUFFER_POINTER</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIP_LAUNCH_PARAM_BUFFER_POINTER&#160;&#160;&#160;((void*)0x01)</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga529edcc8dc562e3f6f6c6d17bf868f03" name="ga529edcc8dc562e3f6f6c6d17bf868f03"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga529edcc8dc562e3f6f6c6d17bf868f03">&#9670;&#160;</a></span>HIP_LAUNCH_PARAM_BUFFER_SIZE</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIP_LAUNCH_PARAM_BUFFER_SIZE&#160;&#160;&#160;((void*)0x02)</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga86cd80c0b352a6679a7fac89e026f0f7" name="ga86cd80c0b352a6679a7fac89e026f0f7"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga86cd80c0b352a6679a7fac89e026f0f7">&#9670;&#160;</a></span>HIP_LAUNCH_PARAM_END</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIP_LAUNCH_PARAM_END&#160;&#160;&#160;((void*)0x03)</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga59685fdad42a844747214758c05f333c" name="ga59685fdad42a844747214758c05f333c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga59685fdad42a844747214758c05f333c">&#9670;&#160;</a></span>hipArrayCubemap</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipArrayCubemap&#160;&#160;&#160;0x04</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga2cae862086a89539b3cf6906a458190c" name="ga2cae862086a89539b3cf6906a458190c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga2cae862086a89539b3cf6906a458190c">&#9670;&#160;</a></span>hipArrayDefault</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipArrayDefault&#160;&#160;&#160;0x00</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Default HIP array allocation flag. </p>

</div>
</div>
<a id="ga7b5573cd703c789c35edb588fb973588" name="ga7b5573cd703c789c35edb588fb973588"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga7b5573cd703c789c35edb588fb973588">&#9670;&#160;</a></span>hipArrayLayered</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipArrayLayered&#160;&#160;&#160;0x01</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gadb552c0ab451ab238fccd142e975a840" name="gadb552c0ab451ab238fccd142e975a840"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gadb552c0ab451ab238fccd142e975a840">&#9670;&#160;</a></span>hipArraySurfaceLoadStore</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipArraySurfaceLoadStore&#160;&#160;&#160;0x02</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga62bc9f85553dbe4eea819ae35f8baaac" name="ga62bc9f85553dbe4eea819ae35f8baaac"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga62bc9f85553dbe4eea819ae35f8baaac">&#9670;&#160;</a></span>hipArrayTextureGather</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipArrayTextureGather&#160;&#160;&#160;0x08</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga77ce8fe6c05ed444d6a7fc769917dc93" name="ga77ce8fe6c05ed444d6a7fc769917dc93"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga77ce8fe6c05ed444d6a7fc769917dc93">&#9670;&#160;</a></span>hipChooseDevice</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipChooseDevice&#160;&#160;&#160;hipChooseDeviceR0600</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga719dca27c00095d1348ffcfc96bea187" name="ga719dca27c00095d1348ffcfc96bea187"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga719dca27c00095d1348ffcfc96bea187">&#9670;&#160;</a></span>hipCooperativeLaunchMultiDeviceNoPostSync</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipCooperativeLaunchMultiDeviceNoPostSync&#160;&#160;&#160;0x02</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gaac01b6324c1a7bcdde41d3349e0cf330" name="gaac01b6324c1a7bcdde41d3349e0cf330"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaac01b6324c1a7bcdde41d3349e0cf330">&#9670;&#160;</a></span>hipCooperativeLaunchMultiDeviceNoPreSync</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipCooperativeLaunchMultiDeviceNoPreSync&#160;&#160;&#160;0x01</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga3ebb587bf795d68d18ba0679a2b41fc8" name="ga3ebb587bf795d68d18ba0679a2b41fc8"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga3ebb587bf795d68d18ba0679a2b41fc8">&#9670;&#160;</a></span>hipCpuDeviceId</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipCpuDeviceId&#160;&#160;&#160;((int)-1)</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gad1c4f8c9fab30ce95f59e2cc404f4d96" name="gad1c4f8c9fab30ce95f59e2cc404f4d96"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gad1c4f8c9fab30ce95f59e2cc404f4d96">&#9670;&#160;</a></span>hipDeviceLmemResizeToMax</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDeviceLmemResizeToMax&#160;&#160;&#160;0x10</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gad01f4c969ca352edd8330774fa416e5b" name="gad01f4c969ca352edd8330774fa416e5b"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gad01f4c969ca352edd8330774fa416e5b">&#9670;&#160;</a></span>hipDeviceMallocContiguous</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDeviceMallocContiguous&#160;&#160;&#160;0x4</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory allocated will be contiguous. </p>

</div>
</div>
<a id="gaa4247e48df3515377a4190d9d5eef26f" name="gaa4247e48df3515377a4190d9d5eef26f"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaa4247e48df3515377a4190d9d5eef26f">&#9670;&#160;</a></span>hipDeviceMallocDefault</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDeviceMallocDefault&#160;&#160;&#160;0x0</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gabf06f7f184187487343b027b04c13173" name="gabf06f7f184187487343b027b04c13173"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gabf06f7f184187487343b027b04c13173">&#9670;&#160;</a></span>hipDeviceMallocFinegrained</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDeviceMallocFinegrained&#160;&#160;&#160;0x1</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory is allocated in fine grained region of device. </p>

</div>
</div>
<a id="ga7e54931e846bc5815b2ffdc4c26bc841" name="ga7e54931e846bc5815b2ffdc4c26bc841"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga7e54931e846bc5815b2ffdc4c26bc841">&#9670;&#160;</a></span>hipDeviceMallocUncached</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDeviceMallocUncached&#160;&#160;&#160;0x3</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory allocated will be uncached. </p>

</div>
</div>
<a id="ga0b7ffad8d7cfcbf9d3c863d30ef651ae" name="ga0b7ffad8d7cfcbf9d3c863d30ef651ae"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga0b7ffad8d7cfcbf9d3c863d30ef651ae">&#9670;&#160;</a></span>hipDeviceMapHost</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDeviceMapHost&#160;&#160;&#160;0x8</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gaa00e004b6ede756d50d4eae0ca2b0330" name="gaa00e004b6ede756d50d4eae0ca2b0330"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaa00e004b6ede756d50d4eae0ca2b0330">&#9670;&#160;</a></span>hipDeviceProp_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define <a class="el" href="structhip_device_prop__t.html">hipDeviceProp_t</a>&#160;&#160;&#160;hipDeviceProp_tR0600</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga9032d35eb7383948828ee48e1e19f5fd" name="ga9032d35eb7383948828ee48e1e19f5fd"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga9032d35eb7383948828ee48e1e19f5fd">&#9670;&#160;</a></span>hipDeviceScheduleAuto</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDeviceScheduleAuto&#160;&#160;&#160;0x0</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Automatically select between Spin and Yield. </p>

</div>
</div>
<a id="gac9480926da806dfe7241e3c8fa0bd060" name="gac9480926da806dfe7241e3c8fa0bd060"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gac9480926da806dfe7241e3c8fa0bd060">&#9670;&#160;</a></span>hipDeviceScheduleBlockingSync</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDeviceScheduleBlockingSync&#160;&#160;&#160;0x4</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gad0ee225558955549785dc0bf37e53554" name="gad0ee225558955549785dc0bf37e53554"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gad0ee225558955549785dc0bf37e53554">&#9670;&#160;</a></span>hipDeviceScheduleMask</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDeviceScheduleMask&#160;&#160;&#160;0x7</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga713d962bafb7758dc1ff0675e4239453" name="ga713d962bafb7758dc1ff0675e4239453"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga713d962bafb7758dc1ff0675e4239453">&#9670;&#160;</a></span>hipDeviceScheduleSpin</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDeviceScheduleSpin&#160;&#160;&#160;0x1</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Dedicate a CPU core to spin-wait. Provides lowest latency, but burns a CPU core and may consume more power. </p>

</div>
</div>
<a id="gaaf1e2706430c06601aa12a8af2a0ba5a" name="gaaf1e2706430c06601aa12a8af2a0ba5a"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaaf1e2706430c06601aa12a8af2a0ba5a">&#9670;&#160;</a></span>hipDeviceScheduleYield</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDeviceScheduleYield&#160;&#160;&#160;0x2</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Yield the CPU to the operating system when waiting. May increase latency, but lowers power and is friendlier to other threads in the system. </p>

</div>
</div>
<a id="ga50ec239992eb3d9adec2342f4ef55d58" name="ga50ec239992eb3d9adec2342f4ef55d58"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga50ec239992eb3d9adec2342f4ef55d58">&#9670;&#160;</a></span>hipDrvLaunchAttribute</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDrvLaunchAttribute&#160;&#160;&#160;<a class="el" href="structhip_launch_attribute.html">hipLaunchAttribute</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga8862cae1ca655975e89f6a49f85fdb6d" name="ga8862cae1ca655975e89f6a49f85fdb6d"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga8862cae1ca655975e89f6a49f85fdb6d">&#9670;&#160;</a></span>hipDrvLaunchAttributeCooperative</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDrvLaunchAttributeCooperative&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4af2e2bdbec3458fd4810e9d18b9e527af">hipLaunchAttributeCooperative</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>hip Drv attributes </p>

</div>
</div>
<a id="gaef10fd11055b9bd60594621763e06b8c" name="gaef10fd11055b9bd60594621763e06b8c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaef10fd11055b9bd60594621763e06b8c">&#9670;&#160;</a></span>hipDrvLaunchAttributeID</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDrvLaunchAttributeID&#160;&#160;&#160;<a class="el" href="group___global_defs.html#ga4026e9ccca8bb88888ad739e0f7586b4">hipLaunchAttributeID</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gaaab4f9f146f99b0c285a50e3a25c2f4a" name="gaaab4f9f146f99b0c285a50e3a25c2f4a"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaaab4f9f146f99b0c285a50e3a25c2f4a">&#9670;&#160;</a></span>hipDrvLaunchAttributeValue</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipDrvLaunchAttributeValue&#160;&#160;&#160;<a class="el" href="unionhip_launch_attribute_value.html">hipLaunchAttributeValue</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga572208e4a28453f2073d2c8e557584c4" name="ga572208e4a28453f2073d2c8e557584c4"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga572208e4a28453f2073d2c8e557584c4">&#9670;&#160;</a></span>hipEnableDefault</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEnableDefault&#160;&#160;&#160;0x0</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Default flag. Equivalent to hipEnablePerThreadDefaultStream if compiled with -fgpu-default-stream=per-thread flag or HIP_API_PER_THREAD_DEFAULT_STREAM macro is defined. </p>

</div>
</div>
<a id="gaa78bc2a6e22c64dc8410710e6a976c58" name="gaa78bc2a6e22c64dc8410710e6a976c58"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaa78bc2a6e22c64dc8410710e6a976c58">&#9670;&#160;</a></span>hipEnableLegacyStream</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEnableLegacyStream&#160;&#160;&#160;0x1</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Search for all symbols except the corresponding per-thread versions. </p>

</div>
</div>
<a id="gabc39fb84f3390dfe4a69c10303c1340d" name="gabc39fb84f3390dfe4a69c10303c1340d"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gabc39fb84f3390dfe4a69c10303c1340d">&#9670;&#160;</a></span>hipEnablePerThreadDefaultStream</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEnablePerThreadDefaultStream&#160;&#160;&#160;0x2</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Search for all symbols including the per-thread versions. If a per-thread version cannot be found, returns the legacy version. </p>

</div>
</div>
<a id="gafa1c076a5b991763a98695063f1ea11d" name="gafa1c076a5b991763a98695063f1ea11d"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gafa1c076a5b991763a98695063f1ea11d">&#9670;&#160;</a></span>hipEventBlockingSync</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEventBlockingSync&#160;&#160;&#160;0x1</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Waiting will yield CPU. Power-friendly and usage-friendly but may increase latency. </p>

</div>
</div>
<a id="ga122a5853359eba97cf047ddd153740f0" name="ga122a5853359eba97cf047ddd153740f0"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga122a5853359eba97cf047ddd153740f0">&#9670;&#160;</a></span>hipEventDefault</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEventDefault&#160;&#160;&#160;0x0</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Default flags. </p>

</div>
</div>
<a id="ga0e9ec830fe53ed7a24a8b96da15f4f12" name="ga0e9ec830fe53ed7a24a8b96da15f4f12"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga0e9ec830fe53ed7a24a8b96da15f4f12">&#9670;&#160;</a></span>hipEventDisableSystemFence</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEventDisableSystemFence&#160;&#160;&#160;0x20000000</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Disable performing a system scope sequentially consistent memory fence when the event transitions from recording to recorded. This can be used for events that are only being used to measure timing, and do not require the event inspection operations (see <a class="el" href="group___event.html#ga1f72d98ba5d6f7dc3da54e0c41fe38b1" title="Wait for an event to complete.">hipEventSynchronize</a>, <a class="el" href="group___event.html#ga5d12d7b798b5ceb5932d1ac21f5ac776" title="Query event status.">hipEventQuery</a>, and <a class="el" href="group___event.html#gad4128b815cb475c8e13c7e66ff6250b7" title="Return the elapsed time between two events.">hipEventElapsedTime</a>) to synchronize-with the work on which the recorded event (see <a class="el" href="group___event.html#gace88ebd8c7ec42a6c2cebda2e8b0cb38" title="Record an event in the specified stream.">hipEventRecord</a>) is waiting. On some AMD GPU devices this can improve the accuracy of timing measurements by avoiding the cost of cache writeback and invalidation, and the performance impact of those actions on the execution of following work. </p>

</div>
</div>
<a id="ga3c0f44a85e36a4c67671da6bcdad0351" name="ga3c0f44a85e36a4c67671da6bcdad0351"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga3c0f44a85e36a4c67671da6bcdad0351">&#9670;&#160;</a></span>hipEventDisableTiming</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEventDisableTiming&#160;&#160;&#160;0x2</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Disable event's capability to record timing information. May improve performance. </p>

</div>
</div>
<a id="ga0f01d74059baa704e42aeff8222166bb" name="ga0f01d74059baa704e42aeff8222166bb"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga0f01d74059baa704e42aeff8222166bb">&#9670;&#160;</a></span>hipEventInterprocess</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEventInterprocess&#160;&#160;&#160;0x4</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Event can support IPC. hipEventDisableTiming also must be set. </p>

</div>
</div>
<a id="ga89c797f8db87adb1cba32b2ecd4cd10a" name="ga89c797f8db87adb1cba32b2ecd4cd10a"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga89c797f8db87adb1cba32b2ecd4cd10a">&#9670;&#160;</a></span>hipEventRecordDefault</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEventRecordDefault&#160;&#160;&#160;0x00</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Default flag. </p>

</div>
</div>
<a id="ga4ba32143914d35954ebc5d1c9aea1240" name="ga4ba32143914d35954ebc5d1c9aea1240"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga4ba32143914d35954ebc5d1c9aea1240">&#9670;&#160;</a></span>hipEventRecordExternal</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEventRecordExternal&#160;&#160;&#160;0x01</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Event is captured in the graph as an external event node when performing stream capture. </p>

</div>
</div>
<a id="gae0909af811a68136a82c970d4e607133" name="gae0909af811a68136a82c970d4e607133"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gae0909af811a68136a82c970d4e607133">&#9670;&#160;</a></span>hipEventReleaseToDevice</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEventReleaseToDevice&#160;&#160;&#160;0x40000000</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Use a device-scope release when recording this event. This flag is useful to obtain more precise timings of commands between events. The flag is a no-op on CUDA platforms. </p>

</div>
</div>
<a id="gab89a2c35618cc9e3e9e2308216c9fc45" name="gab89a2c35618cc9e3e9e2308216c9fc45"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gab89a2c35618cc9e3e9e2308216c9fc45">&#9670;&#160;</a></span>hipEventReleaseToSystem</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEventReleaseToSystem&#160;&#160;&#160;0x80000000</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Use a system-scope release when recording this event. This flag is useful to make non-coherent host memory visible to the host. The flag is a no-op on CUDA platforms. </p>

</div>
</div>
<a id="ga6f2ee7919aec28aba79174d4a507a845" name="ga6f2ee7919aec28aba79174d4a507a845"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga6f2ee7919aec28aba79174d4a507a845">&#9670;&#160;</a></span>hipEventWaitDefault</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEventWaitDefault&#160;&#160;&#160;0x00</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Default flag. </p>

</div>
</div>
<a id="gad255a5b010e6cde0d04de5a1ebe9191c" name="gad255a5b010e6cde0d04de5a1ebe9191c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gad255a5b010e6cde0d04de5a1ebe9191c">&#9670;&#160;</a></span>hipEventWaitExternal</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipEventWaitExternal&#160;&#160;&#160;0x01</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Wait is captured in the graph as an external event node when performing stream capture. </p>

</div>
</div>
<a id="ga06df407ca5682aeed76186e15c050a98" name="ga06df407ca5682aeed76186e15c050a98"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga06df407ca5682aeed76186e15c050a98">&#9670;&#160;</a></span>hipExtAnyOrderLaunch</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipExtAnyOrderLaunch&#160;&#160;&#160;0x01</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>AnyOrderLaunch of kernels. </p>

</div>
</div>
<a id="gab99642079d3d09533b3f8f27920309fc" name="gab99642079d3d09533b3f8f27920309fc"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gab99642079d3d09533b3f8f27920309fc">&#9670;&#160;</a></span>hipExternalMemoryDedicated</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipExternalMemoryDedicated&#160;&#160;&#160;0x1</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gad01a491a6d1ab26ee10280aa1360b2a5" name="gad01a491a6d1ab26ee10280aa1360b2a5"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gad01a491a6d1ab26ee10280aa1360b2a5">&#9670;&#160;</a></span>hipExtHostRegisterCoarseGrained</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipExtHostRegisterCoarseGrained&#160;&#160;&#160;0x8</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Coarse Grained host memory lock. </p>

</div>
</div>
<a id="ga0de3ebe88623693c81a7eea6afee29fc" name="ga0de3ebe88623693c81a7eea6afee29fc"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga0de3ebe88623693c81a7eea6afee29fc">&#9670;&#160;</a></span>hipExtHostRegisterUncached</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipExtHostRegisterUncached&#160;&#160;&#160;0x80000000</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Map host memory onto extended fine grained access host memory pool when enabled. It is applicable on AMD devices, except for Navi4X, in Linux only. </p>

</div>
</div>
<a id="gacf5d42474f220210d9769beacd060720" name="gacf5d42474f220210d9769beacd060720"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gacf5d42474f220210d9769beacd060720">&#9670;&#160;</a></span>hipGetDeviceProperties</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipGetDeviceProperties&#160;&#160;&#160;hipGetDevicePropertiesR0600</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gadc2b418c7ddb2a925668c93e2b09d283" name="gadc2b418c7ddb2a925668c93e2b09d283"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gadc2b418c7ddb2a925668c93e2b09d283">&#9670;&#160;</a></span>hipGraphKernelNodePortDefault</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipGraphKernelNodePortDefault&#160;&#160;&#160;0</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>This port activates when the kernel has finished executing. </p>

</div>
</div>
<a id="gafa17b53c9077021a57c4226282df5c5f" name="gafa17b53c9077021a57c4226282df5c5f"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gafa17b53c9077021a57c4226282df5c5f">&#9670;&#160;</a></span>hipGraphKernelNodePortLaunchCompletion</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipGraphKernelNodePortLaunchCompletion&#160;&#160;&#160;2</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>This port activates when all blocks of the kernel have begun execution. </p>

</div>
</div>
<a id="gad58b559f9d55b1a9d75f7c0b0ec09eef" name="gad58b559f9d55b1a9d75f7c0b0ec09eef"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gad58b559f9d55b1a9d75f7c0b0ec09eef">&#9670;&#160;</a></span>hipGraphKernelNodePortProgrammatic</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipGraphKernelNodePortProgrammatic&#160;&#160;&#160;1</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>This port activates when all blocks of the kernel have performed hipTriggerProgrammaticLaunchCompletion() or have terminated. It must be used with edge type hipGraphDependencyTypeProgrammatic. </p>

</div>
</div>
<a id="ga68a61bd968eb98b6cc6365e760722617" name="ga68a61bd968eb98b6cc6365e760722617"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga68a61bd968eb98b6cc6365e760722617">&#9670;&#160;</a></span>hipHostAllocDefault</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostAllocDefault&#160;&#160;&#160;0x0</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Default pinned memory allocation on the host. </p>

</div>
</div>
<a id="ga15e14750b538f56dda0836ddaab2b8c8" name="ga15e14750b538f56dda0836ddaab2b8c8"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga15e14750b538f56dda0836ddaab2b8c8">&#9670;&#160;</a></span>hipHostAllocMapped</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostAllocMapped&#160;&#160;&#160;0x2</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Map the allocation into the address space for the current device. The device pointer can be obtained with <a class="el" href="group___memory.html#ga8fa7a0478020b835a24785cd6bb89725" title="Get Device pointer from Host Pointer allocated through hipHostMalloc.">hipHostGetDevicePointer</a>. </p>

</div>
</div>
<a id="ga39cedce84d521c99c0e6565f02d15c06" name="ga39cedce84d521c99c0e6565f02d15c06"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga39cedce84d521c99c0e6565f02d15c06">&#9670;&#160;</a></span>hipHostAllocPortable</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostAllocPortable&#160;&#160;&#160;0x1</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory is considered allocated by all contexts. </p>

</div>
</div>
<a id="ga213497e00c458747d94d7afd21907cdf" name="ga213497e00c458747d94d7afd21907cdf"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga213497e00c458747d94d7afd21907cdf">&#9670;&#160;</a></span>hipHostAllocUncached</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostAllocUncached&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gaa4c1aba392606f075e6fea9ed3cf0ccb">hipHostMallocUncached</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga4d6740835ee5071aac5cdb9c69238135" name="ga4d6740835ee5071aac5cdb9c69238135"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga4d6740835ee5071aac5cdb9c69238135">&#9670;&#160;</a></span>hipHostAllocWriteCombined</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostAllocWriteCombined&#160;&#160;&#160;0x4</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Allocates the memory as write-combined. On some system configurations, write-combined allocation may be transferred faster across the PCI Express bus, however, could have low read efficiency by most CPUs. It's a good option for data transfer from host to device via mapped pinned memory. </p><dl class="section note"><dt>Note</dt><dd>This flag is only for CUDA source compatibility but not functional within HIP runtime, because the allocation path is currently not supported on the AMD platform. </dd></dl>

</div>
</div>
<a id="gac726701ac143539b0893c506377f44ee" name="gac726701ac143539b0893c506377f44ee"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gac726701ac143539b0893c506377f44ee">&#9670;&#160;</a></span>hipHostMallocCoherent</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostMallocCoherent&#160;&#160;&#160;0x40000000</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Allocate coherent memory. Overrides HIP_HOST_COHERENT for specific allocation. </p>

</div>
</div>
<a id="gad594ec51cb5b5e946c1e354bf80bddc7" name="gad594ec51cb5b5e946c1e354bf80bddc7"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gad594ec51cb5b5e946c1e354bf80bddc7">&#9670;&#160;</a></span>hipHostMallocDefault</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostMallocDefault&#160;&#160;&#160;0x0</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Default pinned memory allocation on the host. </p><dl class="section note"><dt>Note</dt><dd>This is the same definition as <a class="el" href="group___global_defs.html#ga39cedce84d521c99c0e6565f02d15c06">hipHostAllocPortable</a>. </dd></dl>

</div>
</div>
<a id="gaf6e07be144bb1031bfcf9816335906cc" name="gaf6e07be144bb1031bfcf9816335906cc"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaf6e07be144bb1031bfcf9816335906cc">&#9670;&#160;</a></span>hipHostMallocMapped</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostMallocMapped&#160;&#160;&#160;0x2</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Map the allocation into the address space for the current device. The device pointer can be obtained with <a class="el" href="group___memory.html#ga8fa7a0478020b835a24785cd6bb89725" title="Get Device pointer from Host Pointer allocated through hipHostMalloc.">hipHostGetDevicePointer</a>. </p><dl class="section note"><dt>Note</dt><dd>This is the same <a class="el" href="group___global_defs.html#gaf6e07be144bb1031bfcf9816335906cc">hipHostMallocMapped</a>. </dd></dl>

</div>
</div>
<a id="gaeec0b563ac9d02f45ed02ceab771a472" name="gaeec0b563ac9d02f45ed02ceab771a472"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaeec0b563ac9d02f45ed02ceab771a472">&#9670;&#160;</a></span>hipHostMallocNonCoherent</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostMallocNonCoherent&#160;&#160;&#160;0x80000000</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Allocate non-coherent memory. Overrides HIP_HOST_COHERENT for specific allocation. </p>

</div>
</div>
<a id="ga1d7d6413d3c528fcaa7b5eb808da75d9" name="ga1d7d6413d3c528fcaa7b5eb808da75d9"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga1d7d6413d3c528fcaa7b5eb808da75d9">&#9670;&#160;</a></span>hipHostMallocNumaUser</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostMallocNumaUser&#160;&#160;&#160;0x20000000</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Host memory allocation will follow numa policy set by user. </p><dl class="section note"><dt>Note</dt><dd>This numa allocation flag is applicable on Linux, under development on Windows. </dd></dl>

</div>
</div>
<a id="ga99b7c2b08a834b4736bfdc24893a6bc5" name="ga99b7c2b08a834b4736bfdc24893a6bc5"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga99b7c2b08a834b4736bfdc24893a6bc5">&#9670;&#160;</a></span>hipHostMallocPortable</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostMallocPortable&#160;&#160;&#160;0x1</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory is considered allocated by all contexts. </p><dl class="section note"><dt>Note</dt><dd>This is the same definition as <a class="el" href="group___global_defs.html#ga39cedce84d521c99c0e6565f02d15c06">hipHostAllocPortable</a>. </dd></dl>

</div>
</div>
<a id="gaa4c1aba392606f075e6fea9ed3cf0ccb" name="gaa4c1aba392606f075e6fea9ed3cf0ccb"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaa4c1aba392606f075e6fea9ed3cf0ccb">&#9670;&#160;</a></span>hipHostMallocUncached</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostMallocUncached&#160;&#160;&#160;0x10000000</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Host memory will be forcedly allocated on extended fine grained system memory pool which is with MTYPE_UC. </p><dl class="section note"><dt>Note</dt><dd>This allocation flag is applicable on AMD devices, except for Navi4X, in Linux only. </dd></dl>

</div>
</div>
<a id="ga21beb95617644dbefaffaacdc0f0a35c" name="ga21beb95617644dbefaffaacdc0f0a35c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga21beb95617644dbefaffaacdc0f0a35c">&#9670;&#160;</a></span>hipHostMallocWriteCombined</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostMallocWriteCombined&#160;&#160;&#160;0x4</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Allocates the memory as write-combined. On some system configurations, write-combined allocation may be transferred faster across the PCI Express bus, however, could have low read efficiency by most CPUs. It's a good option for data transfer from host to device via mapped pinned memory. </p><dl class="section note"><dt>Note</dt><dd>This flag is the same definition as <a class="el" href="group___global_defs.html#ga4d6740835ee5071aac5cdb9c69238135">hipHostAllocWriteCombined</a> which is equivalent to cudaHostAllocWriteCombined. It is only for CUDA source compatibility but not functional within HIP runtime, because the allocation path is currently not supported on the AMD platform. </dd></dl>

</div>
</div>
<a id="gac7c100d241ff84ad10109bb00b7b25dc" name="gac7c100d241ff84ad10109bb00b7b25dc"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gac7c100d241ff84ad10109bb00b7b25dc">&#9670;&#160;</a></span>hipHostRegisterDefault</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostRegisterDefault&#160;&#160;&#160;0x0</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory is Mapped and Portable. </p>

</div>
</div>
<a id="gaefa79f1b4481d6a1d1091c14b24f33d0" name="gaefa79f1b4481d6a1d1091c14b24f33d0"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaefa79f1b4481d6a1d1091c14b24f33d0">&#9670;&#160;</a></span>hipHostRegisterIoMemory</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostRegisterIoMemory&#160;&#160;&#160;0x4</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>The passed memory pointer is treated as pointing to some memory-mapped I/O space, e.g. belonging to a third-party PCIe device, and it will be marked as non cache-coherent and contiguous. </p>

</div>
</div>
<a id="gacfa4edcfcb39fc61bff6bdecb14d7618" name="gacfa4edcfcb39fc61bff6bdecb14d7618"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gacfa4edcfcb39fc61bff6bdecb14d7618">&#9670;&#160;</a></span>hipHostRegisterMapped</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostRegisterMapped&#160;&#160;&#160;0x2</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Map the allocation into the address space for the current device. The device pointer can be obtained with <a class="el" href="group___memory.html#ga8fa7a0478020b835a24785cd6bb89725" title="Get Device pointer from Host Pointer allocated through hipHostMalloc.">hipHostGetDevicePointer</a>. </p>

</div>
</div>
<a id="ga2db444f2315d412d3c7ba80ec6049583" name="ga2db444f2315d412d3c7ba80ec6049583"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga2db444f2315d412d3c7ba80ec6049583">&#9670;&#160;</a></span>hipHostRegisterPortable</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostRegisterPortable&#160;&#160;&#160;0x1</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory is considered registered by all contexts. </p>

</div>
</div>
<a id="ga4fa1d9b68702b4705b0a2aaa96c58774" name="ga4fa1d9b68702b4705b0a2aaa96c58774"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga4fa1d9b68702b4705b0a2aaa96c58774">&#9670;&#160;</a></span>hipHostRegisterReadOnly</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipHostRegisterReadOnly&#160;&#160;&#160;0x08</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>This flag is ignored On AMD devices. </p>

</div>
</div>
<a id="ga142b1b5268b4d18fe34050d5c9d9907d" name="ga142b1b5268b4d18fe34050d5c9d9907d"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga142b1b5268b4d18fe34050d5c9d9907d">&#9670;&#160;</a></span>hipInvalidDeviceId</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipInvalidDeviceId&#160;&#160;&#160;((int)-2)</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gaa6226e5fe180a7a8da048f53a5baaf45" name="gaa6226e5fe180a7a8da048f53a5baaf45"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaa6226e5fe180a7a8da048f53a5baaf45">&#9670;&#160;</a></span>hipIpcMemLazyEnablePeerAccess</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipIpcMemLazyEnablePeerAccess&#160;&#160;&#160;0x01</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gaaca6dcdbf6d07ebd1929ef4317ee767b" name="gaaca6dcdbf6d07ebd1929ef4317ee767b"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaaca6dcdbf6d07ebd1929ef4317ee767b">&#9670;&#160;</a></span>hipKernelNodeAttributeAccessPolicyWindow</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipKernelNodeAttributeAccessPolicyWindow&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4ae9c06559f2a188eb87818348cefc4171">hipLaunchAttributeAccessPolicyWindow</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gaded41d67a369cba6502677aa00ac000e" name="gaded41d67a369cba6502677aa00ac000e"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaded41d67a369cba6502677aa00ac000e">&#9670;&#160;</a></span>hipKernelNodeAttributeCooperative</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipKernelNodeAttributeCooperative&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4af2e2bdbec3458fd4810e9d18b9e527af">hipLaunchAttributeCooperative</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gace8baff75db3919346fdcb7e5cf1b7ec" name="gace8baff75db3919346fdcb7e5cf1b7ec"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gace8baff75db3919346fdcb7e5cf1b7ec">&#9670;&#160;</a></span>hipKernelNodeAttributePriority</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipKernelNodeAttributePriority&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4a358f69dfec66d2cfe93b25f44845bcc1">hipLaunchAttributePriority</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gac88b62d1b19899d8611f8b0d81c8aefc" name="gac88b62d1b19899d8611f8b0d81c8aefc"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gac88b62d1b19899d8611f8b0d81c8aefc">&#9670;&#160;</a></span>hipKernelNodeAttrID</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipKernelNodeAttrID&#160;&#160;&#160;<a class="el" href="group___global_defs.html#ga4026e9ccca8bb88888ad739e0f7586b4">hipLaunchAttributeID</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Kernel node attributeID </p>

</div>
</div>
<a id="ga34eb9fa298c10a891ed61bea24ed6c19" name="ga34eb9fa298c10a891ed61bea24ed6c19"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga34eb9fa298c10a891ed61bea24ed6c19">&#9670;&#160;</a></span>hipKernelNodeAttrValue</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipKernelNodeAttrValue&#160;&#160;&#160;<a class="el" href="unionhip_launch_attribute_value.html">hipLaunchAttributeValue</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Kernel node attribute value </p>

</div>
</div>
<a id="ga9c7b267b119306ca08402b6df91d101b" name="ga9c7b267b119306ca08402b6df91d101b"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga9c7b267b119306ca08402b6df91d101b">&#9670;&#160;</a></span>hipMallocSignalMemory</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipMallocSignalMemory&#160;&#160;&#160;0x2</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory represents a HSA signal. </p>

</div>
</div>
<a id="ga48891a93744bc494ce1b1841f756694b" name="ga48891a93744bc494ce1b1841f756694b"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga48891a93744bc494ce1b1841f756694b">&#9670;&#160;</a></span>hipMemAttachGlobal</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipMemAttachGlobal&#160;&#160;&#160;0x01</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory can be accessed by any stream on any device </p>

</div>
</div>
<a id="ga93325b413b2dc1e01be5e7d2f6d8947f" name="ga93325b413b2dc1e01be5e7d2f6d8947f"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga93325b413b2dc1e01be5e7d2f6d8947f">&#9670;&#160;</a></span>hipMemAttachHost</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipMemAttachHost&#160;&#160;&#160;0x02</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory cannot be accessed by any stream on any device. </p>

</div>
</div>
<a id="ga21e33b9b7f3a1a7deebc8718d5bb5e01" name="ga21e33b9b7f3a1a7deebc8718d5bb5e01"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga21e33b9b7f3a1a7deebc8718d5bb5e01">&#9670;&#160;</a></span>hipMemAttachSingle</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipMemAttachSingle&#160;&#160;&#160;0x04</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory can only be accessed by a single stream on the associated device. </p>

</div>
</div>
<a id="ga6b6e50d4535e432ffd219008e751bf2d" name="ga6b6e50d4535e432ffd219008e751bf2d"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga6b6e50d4535e432ffd219008e751bf2d">&#9670;&#160;</a></span>hipOccupancyDefault</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipOccupancyDefault&#160;&#160;&#160;0x00</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gadad1d47116853cf8fb1cd34db61b66dc" name="gadad1d47116853cf8fb1cd34db61b66dc"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gadad1d47116853cf8fb1cd34db61b66dc">&#9670;&#160;</a></span>hipOccupancyDisableCachingOverride</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipOccupancyDisableCachingOverride&#160;&#160;&#160;0x01</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga1fa7fb4d31414111eddcf33066ee72c8" name="ga1fa7fb4d31414111eddcf33066ee72c8"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga1fa7fb4d31414111eddcf33066ee72c8">&#9670;&#160;</a></span>HIPRTC_JIT_CACHE_MODE</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_CACHE_MODE&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a03909311a4e24160a3b04796cddb5772">hipJitOptionCacheMode</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>CUDA Only Set cache mode. </p>

</div>
</div>
<a id="ga2b42afcded55988c4a9a97002720cb48" name="ga2b42afcded55988c4a9a97002720cb48"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga2b42afcded55988c4a9a97002720cb48">&#9670;&#160;</a></span>HIPRTC_JIT_ERROR_LOG_BUFFER</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_ERROR_LOG_BUFFER&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a160e81f3788646e12f4526027c4c8e77">hipJitOptionErrorLogBuffer</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>CUDA Only Pointer to the buffer/*#end#*&zwj;/ with logged error(s) </p>

</div>
</div>
<a id="ga42abe8807ad975df375d68643620d329" name="ga42abe8807ad975df375d68643620d329"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga42abe8807ad975df375d68643620d329">&#9670;&#160;</a></span>HIPRTC_JIT_ERROR_LOG_BUFFER_SIZE_BYTES</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_ERROR_LOG_BUFFER_SIZE_BYTES&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a85c04bedf8aaf7a55628301a9672dd71">hipJitOptionErrorLogBufferSizeBytes</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>CUDA Only Size of the buffer in/*#end#*&zwj;/ bytes for logged error(s) </p>

</div>
</div>
<a id="ga0677386224c6d2b7f88252ea367f6603" name="ga0677386224c6d2b7f88252ea367f6603"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga0677386224c6d2b7f88252ea367f6603">&#9670;&#160;</a></span>HIPRTC_JIT_FALLBACK_STRATEGY</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_FALLBACK_STRATEGY&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500af0117529faba4b00c265add35d44c71c">hipJitOptionFallbackStrategy</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>CUDA Only Fallback strategy. </p>

</div>
</div>
<a id="ga6b6db66d400302dcefac95cfa824143c" name="ga6b6db66d400302dcefac95cfa824143c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga6b6db66d400302dcefac95cfa824143c">&#9670;&#160;</a></span>HIPRTC_JIT_FAST_COMPILE</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_FAST_COMPILE&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a10b1271048a9a8adc55aebcfad56b5b2">hipJitOptionFastCompile</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>CUDA Only Set fast compile. </p>

</div>
</div>
<a id="ga3b5d2d104996cf777ffe65d45beace13" name="ga3b5d2d104996cf777ffe65d45beace13"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga3b5d2d104996cf777ffe65d45beace13">&#9670;&#160;</a></span>HIPRTC_JIT_FMA</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_FMA&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a88b8360e9c3031625e14c7bab84ba8ec">hipJitOptionFma</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<dl class="deprecated"><dt><b><a class="el" href="deprecated.html#_deprecated000006">Deprecated:</a></b></dt><dd>CUDA Only Enable/*#end#*&zwj;/ floating-point multiplies and adds/subtracts operations </dd></dl>

</div>
</div>
<a id="ga68d7b895512edf7c793ea28ac521544b" name="ga68d7b895512edf7c793ea28ac521544b"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga68d7b895512edf7c793ea28ac521544b">&#9670;&#160;</a></span>HIPRTC_JIT_FTZ</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_FTZ&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a77c8b8d337c2eb98e6f910e0a43c9115">hipJitOptionFtz</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<dl class="deprecated"><dt><b><a class="el" href="deprecated.html#_deprecated000003">Deprecated:</a></b></dt><dd>CUDA Only Set/*#end#*&zwj;/ single-precision denormals. </dd></dl>

</div>
</div>
<a id="ga891c9e74a0424511c658bb3c21a65538" name="ga891c9e74a0424511c658bb3c21a65538"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga891c9e74a0424511c658bb3c21a65538">&#9670;&#160;</a></span>HIPRTC_JIT_GENERATE_DEBUG_INFO</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_GENERATE_DEBUG_INFO&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500accc9993c7598bdcbfe2c7738fc2dc2a6">hipJitOptionGenerateDebugInfo</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>CUDA Only Generate debug information/*#end#*&zwj;/. </p>

</div>
</div>
<a id="gae1be684de97e8598bfe7005e9eee833e" name="gae1be684de97e8598bfe7005e9eee833e"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gae1be684de97e8598bfe7005e9eee833e">&#9670;&#160;</a></span>HIPRTC_JIT_GENERATE_LINE_INFO</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_GENERATE_LINE_INFO&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a75f073079cf61c48325633878532ab01">hipJitOptionGenerateLineInfo</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>CUDA Only Generate line number information/*#end#*&zwj;/. </p>

</div>
</div>
<a id="ga73cc3a267ecdef3675ac545f371bcdf0" name="ga73cc3a267ecdef3675ac545f371bcdf0"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga73cc3a267ecdef3675ac545f371bcdf0">&#9670;&#160;</a></span>HIPRTC_JIT_GLOBAL_SYMBOL_ADDRESS</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_GLOBAL_SYMBOL_ADDRESS&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a92882f96099e9a265d1f24d20698dc28">hipJitOptionGlobalSymbolAddresses</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>CUDA Only Array of host addresses to be/*#end#*&zwj;/ relocated to the device </p>

</div>
</div>
<a id="ga69b8fd1b666286ab6c4e03094b0e510b" name="ga69b8fd1b666286ab6c4e03094b0e510b"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga69b8fd1b666286ab6c4e03094b0e510b">&#9670;&#160;</a></span>HIPRTC_JIT_GLOBAL_SYMBOL_COUNT</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_GLOBAL_SYMBOL_COUNT&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500aa428196b5654c717bb67583c808491f3">hipJitOptionGlobalSymbolCount</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>CUDA Only Number of symbol count./*#end#*&zwj;/. </p>

</div>
</div>
<a id="ga55bc69a5e022e095458550b05947750d" name="ga55bc69a5e022e095458550b05947750d"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga55bc69a5e022e095458550b05947750d">&#9670;&#160;</a></span>HIPRTC_JIT_GLOBAL_SYMBOL_NAMES</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_GLOBAL_SYMBOL_NAMES&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a8cd7f84c16128c39d422cc94d6180d47">hipJitOptionGlobalSymbolNames</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>CUDA Only Array of device symbol names to be/*#end#*&zwj;/ relocated to the host </p>

</div>
</div>
<a id="ga8a548b1d92ae8663fb68b2c2279dc90f" name="ga8a548b1d92ae8663fb68b2c2279dc90f"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga8a548b1d92ae8663fb68b2c2279dc90f">&#9670;&#160;</a></span>HIPRTC_JIT_INFO_LOG_BUFFER</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_INFO_LOG_BUFFER&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a144aa71e24aa20fb4162e9978d6c66d1">hipJitOptionInfoLogBuffer</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>CUDA Only Pointer to the buffer with/*#end#*&zwj;/ logged information </p>

</div>
</div>
<a id="ga492c32e4fd482ee995e7036df57037ad" name="ga492c32e4fd482ee995e7036df57037ad"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga492c32e4fd482ee995e7036df57037ad">&#9670;&#160;</a></span>HIPRTC_JIT_INFO_LOG_BUFFER_SIZE_BYTES</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_INFO_LOG_BUFFER_SIZE_BYTES&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a9692ed236671843b99de1dbfc7aadb8f">hipJitOptionInfoLogBufferSizeBytes</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>CUDA Only Size of the buffer/*#end#*&zwj;/ in bytes for logged info </p>

</div>
</div>
<a id="gaa5f10291ec491a9b44d423c8cf40e9a2" name="gaa5f10291ec491a9b44d423c8cf40e9a2"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaa5f10291ec491a9b44d423c8cf40e9a2">&#9670;&#160;</a></span>HIPRTC_JIT_INPUT_CUBIN</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_INPUT_CUBIN&#160;&#160;&#160;<a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137ba45010991b618ba1d7256a59375f97933">hipJitInputCubin</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>Cuda only Input Cubin. </p>

</div>
</div>
<a id="gaa19ce08a4953c057acba59fd0b9af60b" name="gaa19ce08a4953c057acba59fd0b9af60b"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaa19ce08a4953c057acba59fd0b9af60b">&#9670;&#160;</a></span>HIPRTC_JIT_INPUT_FATBINARY</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_INPUT_FATBINARY&#160;&#160;&#160;<a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137baa404072040c12d06ebbf06ac518f1acc">hipJitInputFatBinary</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>Cuda Only Input FAT Binary. </p>

</div>
</div>
<a id="ga9b4744b6ade1b83051e2923822a8efc8" name="ga9b4744b6ade1b83051e2923822a8efc8"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga9b4744b6ade1b83051e2923822a8efc8">&#9670;&#160;</a></span>HIPRTC_JIT_INPUT_LIBRARY</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_INPUT_LIBRARY&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137ba5fa416edd513fc5763e34f86166e8508">hipJitInputLibrary</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>Cuda Only Archive of Host Objects with embedded device code/*#end#*&zwj;/. </p>

</div>
</div>
<a id="ga9bfd9789fcb79200ebb50cf7e0b862b2" name="ga9bfd9789fcb79200ebb50cf7e0b862b2"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga9bfd9789fcb79200ebb50cf7e0b862b2">&#9670;&#160;</a></span>HIPRTC_JIT_INPUT_LLVM_ARCHIVES_OF_BUNDLED_BITCODE</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_INPUT_LLVM_ARCHIVES_OF_BUNDLED_BITCODE&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137ba3a1fcd77531ad7ba59d817966c9ff3a7">hipJitInputLLVMArchivesOfBundledBitcode</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP Only LLVM/*#end#*&zwj;/ Archives of Bundled Bitcode </p>

</div>
</div>
<a id="ga69edd89282dedef12b5ece9672a8b972" name="ga69edd89282dedef12b5ece9672a8b972"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga69edd89282dedef12b5ece9672a8b972">&#9670;&#160;</a></span>HIPRTC_JIT_INPUT_LLVM_BITCODE</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_INPUT_LLVM_BITCODE&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137babc39a8964fe113cf0c00deebb8675d23">hipJitInputLLVMBitcode</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>HIP Only LLVM Bitcode or IR assembly/*#end#*&zwj;/. </p>

</div>
</div>
<a id="ga9a18c8cd0929f6ffaeb93ab1236e545c" name="ga9a18c8cd0929f6ffaeb93ab1236e545c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga9a18c8cd0929f6ffaeb93ab1236e545c">&#9670;&#160;</a></span>HIPRTC_JIT_INPUT_LLVM_BUNDLED_BITCODE</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_INPUT_LLVM_BUNDLED_BITCODE&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137baed006f1254cb797a67f3cd20eb15fd90">hipJitInputLLVMBundledBitcode</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>HIP Only LLVM Clang Bundled Code/*#end#*&zwj;/. </p>

</div>
</div>
<a id="ga88176f9b8fb9c09d294507bce0aae982" name="ga88176f9b8fb9c09d294507bce0aae982"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga88176f9b8fb9c09d294507bce0aae982">&#9670;&#160;</a></span>HIPRTC_JIT_INPUT_NVVM</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_INPUT_NVVM&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137baf94b48b3e589b922d6638a6eadfe0046">hipJitInputNvvm</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<dl class="deprecated"><dt><b><a class="el" href="deprecated.html#_deprecated000007">Deprecated:</a></b></dt><dd>CUDA only High Level intermediate code for LTO/*#end#*&zwj;/ </dd></dl>

</div>
</div>
<a id="ga2f76899d2ecd435a61d0c9e5a8e944bb" name="ga2f76899d2ecd435a61d0c9e5a8e944bb"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga2f76899d2ecd435a61d0c9e5a8e944bb">&#9670;&#160;</a></span>HIPRTC_JIT_INPUT_OBJECT</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_INPUT_OBJECT&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137ba885b8c1b34c4e922f1d6c9812791043b">hipJitInputObject</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>Cuda Only Host Object with embedded device code/*#end#*&zwj;/. </p>

</div>
</div>
<a id="gabfe56d29fc90e8372ee9f1d6a418829c" name="gabfe56d29fc90e8372ee9f1d6a418829c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gabfe56d29fc90e8372ee9f1d6a418829c">&#9670;&#160;</a></span>HIPRTC_JIT_INPUT_PTX</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_INPUT_PTX&#160;&#160;&#160;<a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137bac42cc2efd148b2504642178cc1f6fd93">hipJitInputPtx</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>Cuda only Input PTX. </p>

</div>
</div>
<a id="ga9c4afbdb17545bab451e30889674e911" name="ga9c4afbdb17545bab451e30889674e911"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga9c4afbdb17545bab451e30889674e911">&#9670;&#160;</a></span>HIPRTC_JIT_INPUT_SPIRV</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_INPUT_SPIRV&#160;&#160;&#160;<a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137bae7607245bf34f44146dfa10778a103e9">hipJitInputSpirv</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>HIP Only SPIRV Code Object. </p>

</div>
</div>
<a id="ga8c505a9bef8629a7688e4a7347905f0e" name="ga8c505a9bef8629a7688e4a7347905f0e"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga8c505a9bef8629a7688e4a7347905f0e">&#9670;&#160;</a></span>HIPRTC_JIT_IR_TO_ISA_OPT_COUNT_EXT</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_IR_TO_ISA_OPT_COUNT_EXT&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a01af3ae03c48fdb37a6307f2890600d9">hipJitOptionIRtoISAOptCountExt</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP Only Count of linker options/*#end#*&zwj;/ to be passed on to </p>

</div>
</div>
<a id="ga03b492a096a92af33ad0256fc26704be" name="ga03b492a096a92af33ad0256fc26704be"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga03b492a096a92af33ad0256fc26704be">&#9670;&#160;</a></span>HIPRTC_JIT_IR_TO_ISA_OPT_EXT</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_IR_TO_ISA_OPT_EXT&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500afcdd8a22dbc9216c754eab0924900f03">hipJitOptionIRtoISAOptExt</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP Only Linker options to be/*#end#*&zwj;/ passed on to compiler </p>

</div>
</div>
<a id="ga4858108f706063c48145b701a3eefd5c" name="ga4858108f706063c48145b701a3eefd5c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga4858108f706063c48145b701a3eefd5c">&#9670;&#160;</a></span>HIPRTC_JIT_LOG_VERBOSE</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_LOG_VERBOSE&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500ad42abb970a18154f23e359e097d5aa89">hipJitOptionLogVerbose</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>CUDA Only Generate log verbose. </p>

</div>
</div>
<a id="ga9bc86db1f4761801010ea682c5e1ed68" name="ga9bc86db1f4761801010ea682c5e1ed68"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga9bc86db1f4761801010ea682c5e1ed68">&#9670;&#160;</a></span>HIPRTC_JIT_LTO</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_LTO&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a0c4487f8639e8edd0790699f3f068cb3">hipJitOptionLto</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<dl class="deprecated"><dt><b><a class="el" href="deprecated.html#_deprecated000002">Deprecated:</a></b></dt><dd>CUDA Only Enable link-time/*#end#*&zwj;/ optimization for device code </dd></dl>

</div>
</div>
<a id="ga844dd731acf15ad2f5234c3952525077" name="ga844dd731acf15ad2f5234c3952525077"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga844dd731acf15ad2f5234c3952525077">&#9670;&#160;</a></span>HIPRTC_JIT_MAX_REGISTERS</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_MAX_REGISTERS&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500adb9370990a4403b1e5e03724031b4ecb">hipJitOptionMaxRegisters</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>CUDA Only Maximum registers may be used in a/*#end#*&zwj;/ thread, passed to compiler </p>

</div>
</div>
<a id="ga57b1691eeb7a979112805a5670c6a419" name="ga57b1691eeb7a979112805a5670c6a419"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga57b1691eeb7a979112805a5670c6a419">&#9670;&#160;</a></span>HIPRTC_JIT_MAX_THREADS_PER_BLOCK</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_MAX_THREADS_PER_BLOCK&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500af3eb46de12b9aa7759fcbac5841705e8">hipJitOptionMaxThreadsPerBlock</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>CUDA only Maximum number of/*#end#*&zwj;/ threads in a thread block </p>

</div>
</div>
<a id="gaf2d771a2f74ede0e89e6d52b2f7390c3" name="gaf2d771a2f74ede0e89e6d52b2f7390c3"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaf2d771a2f74ede0e89e6d52b2f7390c3">&#9670;&#160;</a></span>HIPRTC_JIT_MIN_CTA_PER_SM</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_MIN_CTA_PER_SM&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500ac17c5d8cb8bf1417cffa84ae37bd647a">hipJitOptionMinCTAPerSM</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>CUDA Only Hints to JIT compiler/*#end#*&zwj;/ the minimum number of CTAs frin kernel's grid to be mapped to SM </p>

</div>
</div>
<a id="ga98ead031f321c8c55081d9d522ac6f64" name="ga98ead031f321c8c55081d9d522ac6f64"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga98ead031f321c8c55081d9d522ac6f64">&#9670;&#160;</a></span>HIPRTC_JIT_NEW_SM3X_OPT</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_NEW_SM3X_OPT&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500ae942560c8927000dc8933aff96f4ed9e">hipJitOptionSm3xOpt</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<dl class="deprecated"><dt><b><a class="el" href="deprecated.html#_deprecated000001">Deprecated:</a></b></dt><dd>CUDA Only New SM3X option. </dd></dl>

</div>
</div>
<a id="ga645de3f1f485789503c15f9b3f03212c" name="ga645de3f1f485789503c15f9b3f03212c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga645de3f1f485789503c15f9b3f03212c">&#9670;&#160;</a></span>HIPRTC_JIT_NUM_INPUT_TYPES</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_NUM_INPUT_TYPES&#160;&#160;&#160;<a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137ba658d253cd7fceb446c97553544eb81ec">hipJitNumInputTypes</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>Count of Input Types. </p>

</div>
</div>
<a id="ga6eaf11642f9f91cd7b4bb5756aa59733" name="ga6eaf11642f9f91cd7b4bb5756aa59733"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga6eaf11642f9f91cd7b4bb5756aa59733">&#9670;&#160;</a></span>HIPRTC_JIT_NUM_LEGACY_INPUT_TYPES</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_NUM_LEGACY_INPUT_TYPES&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#ggad0680b9556a66070daae617025a8137ba3f3daa2b9d22468f9d46402a5a6823e2">hipJitNumLegacyInputTypes</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>Count of Legacy Input Types/*#end#*&zwj;/. </p>

</div>
</div>
<a id="gae2744cea3199352529c2f9a330cb885d" name="gae2744cea3199352529c2f9a330cb885d"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gae2744cea3199352529c2f9a330cb885d">&#9670;&#160;</a></span>HIPRTC_JIT_NUM_OPTIONS</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_NUM_OPTIONS&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a639edb73879171ee5c22ce54d7d5b1d5">hipJitOptionNumOptions</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>Number of options. </p>

</div>
</div>
<a id="gaf088a48ea211084071c1cacceb7c6105" name="gaf088a48ea211084071c1cacceb7c6105"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaf088a48ea211084071c1cacceb7c6105">&#9670;&#160;</a></span>HIPRTC_JIT_OPTIMIZATION_LEVEL</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_OPTIMIZATION_LEVEL&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a853499616f10eaa99df134371f0ed075">hipJitOptionOptimizationLevel</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Value of optimization level for/*#end#*&zwj;/ generated codes, acceptable options -O0, -O1, -O2, -O3 </p>

</div>
</div>
<a id="gacaf02527aac7f508983866c34ad136ab" name="gacaf02527aac7f508983866c34ad136ab"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gacaf02527aac7f508983866c34ad136ab">&#9670;&#160;</a></span>HIPRTC_JIT_OVERRIDE_DIRECT_VALUES</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_OVERRIDE_DIRECT_VALUES&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a7186206beec45797e629016e91fe60c9">hipJitOptionOverrideDirectiveValues</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>CUDA only Override Directive/*#end#*&zwj;/ Values </p>

</div>
</div>
<a id="gae52eeb4f069ce82ec2e3bca87ff29f78" name="gae52eeb4f069ce82ec2e3bca87ff29f78"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gae52eeb4f069ce82ec2e3bca87ff29f78">&#9670;&#160;</a></span>HIPRTC_JIT_POSITION_INDEPENDENT_CODE</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_POSITION_INDEPENDENT_CODE&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a069d8f3795d50848cc7d36a12e658c66">hipJitOptionPositionIndependentCode</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>CUDA Only Generates/*#end#*&zwj;/ Position Independent code </p>

</div>
</div>
<a id="gaa0931c6a36ca739e1161774fccaf96fd" name="gaa0931c6a36ca739e1161774fccaf96fd"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaa0931c6a36ca739e1161774fccaf96fd">&#9670;&#160;</a></span>HIPRTC_JIT_PREC_DIV</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_PREC_DIV&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a4652bd7280b345cf90a785a8abba3230">hipJitOptionPrecDiv</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<dl class="deprecated"><dt><b><a class="el" href="deprecated.html#_deprecated000004">Deprecated:</a></b></dt><dd>CUDA Only Set/*#end#*&zwj;/ single-precision floating-point division and reciprocals </dd></dl>

</div>
</div>
<a id="ga8982f3e9dfdb66107ad2eb79e83373bd" name="ga8982f3e9dfdb66107ad2eb79e83373bd"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga8982f3e9dfdb66107ad2eb79e83373bd">&#9670;&#160;</a></span>HIPRTC_JIT_PREC_SQRT</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_PREC_SQRT&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500ad49317eb710a0ab90b3678eaa28edf5c">hipJitOptionPrecSqrt</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<dl class="deprecated"><dt><b><a class="el" href="deprecated.html#_deprecated000005">Deprecated:</a></b></dt><dd>CUDA Only Set/*#end#*&zwj;/ single-precision floating-point square root </dd></dl>

</div>
</div>
<a id="ga097ccbfbb1d9a1b80f6955f4a30d81b9" name="ga097ccbfbb1d9a1b80f6955f4a30d81b9"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga097ccbfbb1d9a1b80f6955f4a30d81b9">&#9670;&#160;</a></span>HIPRTC_JIT_TARGET</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_TARGET&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a4c83761657de80ef98f0a34d1d22f323">hipJitOptionTarget</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>CUDA Only JIT target. </p>

</div>
</div>
<a id="ga13c5257e0f3a67d068a57de9bd10210a" name="ga13c5257e0f3a67d068a57de9bd10210a"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga13c5257e0f3a67d068a57de9bd10210a">&#9670;&#160;</a></span>HIPRTC_JIT_TARGET_FROM_HIPCONTEXT</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_TARGET_FROM_HIPCONTEXT&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500ab8e971a00aa557a668791e3403aafeca">hipJitOptionTargetFromContext</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>CUDA Only The target context,/*#end#*&zwj;/ which is the default </p>

</div>
</div>
<a id="gaf17433edc5e16beeea7ecc1771480a3c" name="gaf17433edc5e16beeea7ecc1771480a3c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaf17433edc5e16beeea7ecc1771480a3c">&#9670;&#160;</a></span>HIPRTC_JIT_THREADS_PER_BLOCK</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_THREADS_PER_BLOCK&#160;&#160;&#160;  <a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a5c9a55072a6f4ed3ca61604ef66a4a86">hipJitOptionThreadsPerBlock</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>CUDA Only Number of thread per block/*#end#*&zwj;/. </p>

</div>
</div>
<a id="ga116d5f8bab368a95f67e5aa271b3ceb1" name="ga116d5f8bab368a95f67e5aa271b3ceb1"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga116d5f8bab368a95f67e5aa271b3ceb1">&#9670;&#160;</a></span>HIPRTC_JIT_WALL_TIME</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIPRTC_JIT_WALL_TIME&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gga54cbbb7697c63cf9b13383b49819d500a8ee4752e49439cb2fbecdf1dcc69871e">hipJitOptionWallTime</a></td>
        </tr>
      </table>
</div><div class="memdoc">

<p>CUDA Only Value for total wall clock time. </p>

</div>
</div>
<a id="ga4648625dd84e67665d6e81eca7ac38b2" name="ga4648625dd84e67665d6e81eca7ac38b2"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga4648625dd84e67665d6e81eca7ac38b2">&#9670;&#160;</a></span>hiprtcJIT_option</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hiprtcJIT_option&#160;&#160;&#160;<a class="el" href="group___linker_types.html#ga54cbbb7697c63cf9b13383b49819d500">hipJitOption</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>hiprtc JIT option </p>

</div>
</div>
<a id="ga6aef618fbe4bb34d63c218c8de8e5631" name="ga6aef618fbe4bb34d63c218c8de8e5631"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga6aef618fbe4bb34d63c218c8de8e5631">&#9670;&#160;</a></span>hiprtcJITInputType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hiprtcJITInputType&#160;&#160;&#160;<a class="el" href="group___linker_types.html#gad0680b9556a66070daae617025a8137b">hipJitInputType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>hiprtc JIT input type </p>

</div>
</div>
<a id="gaf67922ae5820e7e5a949b75a90cc12e3" name="gaf67922ae5820e7e5a949b75a90cc12e3"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaf67922ae5820e7e5a949b75a90cc12e3">&#9670;&#160;</a></span>hipStreamAttributeAccessPolicyWindow</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamAttributeAccessPolicyWindow&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4ae9c06559f2a188eb87818348cefc4171">hipLaunchAttributeAccessPolicyWindow</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga867c605c43bdaec3d8d9fd6e68833795" name="ga867c605c43bdaec3d8d9fd6e68833795"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga867c605c43bdaec3d8d9fd6e68833795">&#9670;&#160;</a></span>hipStreamAttributeMemSyncDomain</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamAttributeMemSyncDomain&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4a71ab9ea6aef993bbcaac9798a1445023">hipLaunchAttributeMemSyncDomain</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gae628261a328822c59e70741b44a15765" name="gae628261a328822c59e70741b44a15765"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gae628261a328822c59e70741b44a15765">&#9670;&#160;</a></span>hipStreamAttributeMemSyncDomainMap</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamAttributeMemSyncDomainMap&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4a9229ce145edcc4442002d8ee2d156cc3">hipLaunchAttributeMemSyncDomainMap</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga9f499f227eb07651976dd2bca91b5a32" name="ga9f499f227eb07651976dd2bca91b5a32"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga9f499f227eb07651976dd2bca91b5a32">&#9670;&#160;</a></span>hipStreamAttributePriority</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamAttributePriority&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4a358f69dfec66d2cfe93b25f44845bcc1">hipLaunchAttributePriority</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga10af2df66d201920bdd860164e45c3b4" name="ga10af2df66d201920bdd860164e45c3b4"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga10af2df66d201920bdd860164e45c3b4">&#9670;&#160;</a></span>hipStreamAttributeSynchronizationPolicy</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamAttributeSynchronizationPolicy&#160;&#160;&#160;<a class="el" href="group___global_defs.html#gga4026e9ccca8bb88888ad739e0f7586b4aac7011b4266fc8e091a1048326da38b7">hipLaunchAttributeSynchronizationPolicy</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga64f6b888b51ac73a4a442e8c7986bcfe" name="ga64f6b888b51ac73a4a442e8c7986bcfe"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga64f6b888b51ac73a4a442e8c7986bcfe">&#9670;&#160;</a></span>hipStreamAttrID</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamAttrID&#160;&#160;&#160;<a class="el" href="group___global_defs.html#ga4026e9ccca8bb88888ad739e0f7586b4">hipLaunchAttributeID</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Stream attributes </p>

</div>
</div>
<a id="gabc501f050b998117cf3519d57967721d" name="gabc501f050b998117cf3519d57967721d"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gabc501f050b998117cf3519d57967721d">&#9670;&#160;</a></span>hipStreamAttrValue</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamAttrValue&#160;&#160;&#160;<a class="el" href="unionhip_launch_attribute_value.html">hipLaunchAttributeValue</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga6df5f70eb976836ab3598cacf0ffcdf9" name="ga6df5f70eb976836ab3598cacf0ffcdf9"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga6df5f70eb976836ab3598cacf0ffcdf9">&#9670;&#160;</a></span>hipStreamDefault</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamDefault&#160;&#160;&#160;0x00</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Flags that can be used with hipStreamCreateWithFlags. Default stream creation flags. These are used with <a class="el" href="group___stream.html#gaff5b62d6e9502d80879f7176f4d03102" title="Creates an asynchronous stream.">hipStreamCreate()</a>. </p>

</div>
</div>
<a id="ga7f5bb5340726842f8967cd66337361d7" name="ga7f5bb5340726842f8967cd66337361d7"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga7f5bb5340726842f8967cd66337361d7">&#9670;&#160;</a></span>hipStreamLegacy</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamLegacy&#160;&#160;&#160;((<a class="el" href="group___global_defs.html#ga0fc4326b345ac109cb72b90a22a1cb29">hipStream_t</a>)1)</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gaaba9ae995d9b43b7d1ee70c6fa12c57d" name="gaaba9ae995d9b43b7d1ee70c6fa12c57d"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaaba9ae995d9b43b7d1ee70c6fa12c57d">&#9670;&#160;</a></span>hipStreamNonBlocking</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamNonBlocking&#160;&#160;&#160;0x01</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Stream does not implicitly synchronize with null stream. </p>

</div>
</div>
<a id="ga69981e17c0b9cf4cd562c8103724e2cf" name="ga69981e17c0b9cf4cd562c8103724e2cf"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga69981e17c0b9cf4cd562c8103724e2cf">&#9670;&#160;</a></span>hipStreamPerThread</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamPerThread&#160;&#160;&#160;((<a class="el" href="group___global_defs.html#ga0fc4326b345ac109cb72b90a22a1cb29">hipStream_t</a>)2)</td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Implicit stream per application thread. </p>

</div>
</div>
<a id="gaeaac19269c1ef4f10630ecb683302fed" name="gaeaac19269c1ef4f10630ecb683302fed"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaeaac19269c1ef4f10630ecb683302fed">&#9670;&#160;</a></span>hipStreamWaitValueAnd</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamWaitValueAnd&#160;&#160;&#160;0x2</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga3cf15c65c047827a251f1c42d2a8c4d4" name="ga3cf15c65c047827a251f1c42d2a8c4d4"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga3cf15c65c047827a251f1c42d2a8c4d4">&#9670;&#160;</a></span>hipStreamWaitValueEq</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamWaitValueEq&#160;&#160;&#160;0x1</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gab6d87965bf388c229dffa70fea11e772" name="gab6d87965bf388c229dffa70fea11e772"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gab6d87965bf388c229dffa70fea11e772">&#9670;&#160;</a></span>hipStreamWaitValueGte</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamWaitValueGte&#160;&#160;&#160;0x0</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga4c3e4c6c5147a927d84d239da5754845" name="ga4c3e4c6c5147a927d84d239da5754845"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga4c3e4c6c5147a927d84d239da5754845">&#9670;&#160;</a></span>hipStreamWaitValueNor</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define hipStreamWaitValueNor&#160;&#160;&#160;0x3</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<h2 class="groupheader">Typedef Documentation</h2>
<a id="ga7efd7809e1632cdae75603fd1fee61c0" name="ga7efd7809e1632cdae75603fd1fee61c0"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga7efd7809e1632cdae75603fd1fee61c0">&#9670;&#160;</a></span>GLenum</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef unsigned int <a class="el" href="group___global_defs.html#ga7efd7809e1632cdae75603fd1fee61c0">GLenum</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>GLenum as uint. </p>

</div>
</div>
<a id="gaa311c7f0d6ec4f1a33f9235c3651b86b" name="gaa311c7f0d6ec4f1a33f9235c3651b86b"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaa311c7f0d6ec4f1a33f9235c3651b86b">&#9670;&#160;</a></span>GLuint</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef unsigned int <a class="el" href="group___global_defs.html#gaa311c7f0d6ec4f1a33f9235c3651b86b">GLuint</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>GLuint as uint. </p>

</div>
</div>
<a id="ga0ebbb61a275c1adb950de995aadd22bf" name="ga0ebbb61a275c1adb950de995aadd22bf"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga0ebbb61a275c1adb950de995aadd22bf">&#9670;&#160;</a></span>hipCtx_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct ihipCtx_t* <a class="el" href="group___global_defs.html#ga0ebbb61a275c1adb950de995aadd22bf">hipCtx_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga181a06ca0d50ffdd6e019c87ffe02fb4" name="ga181a06ca0d50ffdd6e019c87ffe02fb4"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga181a06ca0d50ffdd6e019c87ffe02fb4">&#9670;&#160;</a></span>hipDevice_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef int <a class="el" href="group___global_defs.html#ga181a06ca0d50ffdd6e019c87ffe02fb4">hipDevice_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga6742b54e2b83c1a5d6861ede4825aafe" name="ga6742b54e2b83c1a5d6861ede4825aafe"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga6742b54e2b83c1a5d6861ede4825aafe">&#9670;&#160;</a></span>hipError_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga89716f0e21b750a51ceb081208a84b33">__HIP_NODISCARD</a> <a class="el" href="group___global_defs.html#ga6742b54e2b83c1a5d6861ede4825aafe">hipError_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP error type </p>

</div>
</div>
<a id="ga3640952e23c028a87a7db564443948ea" name="ga3640952e23c028a87a7db564443948ea"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga3640952e23c028a87a7db564443948ea">&#9670;&#160;</a></span>hipEvent_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct ihipEvent_t* <a class="el" href="group___global_defs.html#ga3640952e23c028a87a7db564443948ea">hipEvent_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gacad4902ef0f6115cb225c6eadc08c0ed" name="gacad4902ef0f6115cb225c6eadc08c0ed"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gacad4902ef0f6115cb225c6eadc08c0ed">&#9670;&#160;</a></span>hipExternalMemory_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef void* <a class="el" href="group___global_defs.html#gacad4902ef0f6115cb225c6eadc08c0ed">hipExternalMemory_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gabac0a28e2e38f93c46743f629efac5c5" name="gabac0a28e2e38f93c46743f629efac5c5"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gabac0a28e2e38f93c46743f629efac5c5">&#9670;&#160;</a></span>hipExternalSemaphore_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef void* <a class="el" href="group___global_defs.html#gabac0a28e2e38f93c46743f629efac5c5">hipExternalSemaphore_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gac7ab0ad556b5e1b3461e450fd2c7da3b" name="gac7ab0ad556b5e1b3461e450fd2c7da3b"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gac7ab0ad556b5e1b3461e450fd2c7da3b">&#9670;&#160;</a></span>hipFunction_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct ihipModuleSymbol_t* <a class="el" href="group___global_defs.html#gac7ab0ad556b5e1b3461e450fd2c7da3b">hipFunction_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga76cd3d33523dd0544c9031fcccc95eec" name="ga76cd3d33523dd0544c9031fcccc95eec"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga76cd3d33523dd0544c9031fcccc95eec">&#9670;&#160;</a></span>hipGraph_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct ihipGraph* <a class="el" href="group___global_defs.html#ga76cd3d33523dd0544c9031fcccc95eec">hipGraph_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>An opaque value that represents a hip graph </p>

</div>
</div>
<a id="gac6cdb648ca4cdd1f61d82c0c0644a065" name="gac6cdb648ca4cdd1f61d82c0c0644a065"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gac6cdb648ca4cdd1f61d82c0c0644a065">&#9670;&#160;</a></span>hipGraphExec_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct hipGraphExec* <a class="el" href="group___global_defs.html#gac6cdb648ca4cdd1f61d82c0c0644a065">hipGraphExec_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>An opaque value that represents a hip graph Exec </p>

</div>
</div>
<a id="gad96ccb9b8a16edff6513bdc22745a832" name="gad96ccb9b8a16edff6513bdc22745a832"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gad96ccb9b8a16edff6513bdc22745a832">&#9670;&#160;</a></span>hipGraphicsResource</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct _hipGraphicsResource <a class="el" href="group___global_defs.html#gad96ccb9b8a16edff6513bdc22745a832">hipGraphicsResource</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga0844c3ebc78e5c8d91dca7379b3e0930" name="ga0844c3ebc78e5c8d91dca7379b3e0930"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga0844c3ebc78e5c8d91dca7379b3e0930">&#9670;&#160;</a></span>hipGraphicsResource_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef <a class="el" href="group___global_defs.html#gad96ccb9b8a16edff6513bdc22745a832">hipGraphicsResource</a>* <a class="el" href="group___global_defs.html#ga0844c3ebc78e5c8d91dca7379b3e0930">hipGraphicsResource_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gae127ef09c4eec55642394658ec3433ec" name="gae127ef09c4eec55642394658ec3433ec"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gae127ef09c4eec55642394658ec3433ec">&#9670;&#160;</a></span>hipGraphNode_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct hipGraphNode* <a class="el" href="group___global_defs.html#gae127ef09c4eec55642394658ec3433ec">hipGraphNode_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>An opaque value that represents a hip graph node </p>

</div>
</div>
<a id="ga6b1ea90b2fea2d4c62eb351e1ed44f93" name="ga6b1ea90b2fea2d4c62eb351e1ed44f93"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga6b1ea90b2fea2d4c62eb351e1ed44f93">&#9670;&#160;</a></span>hipHostFn_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef void(* hipHostFn_t) (void *userData)</td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga457ed655bd58ace1a3b11b4bd19da8e9" name="ga457ed655bd58ace1a3b11b4bd19da8e9"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga457ed655bd58ace1a3b11b4bd19da8e9">&#9670;&#160;</a></span>hipKernel_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct ihipKernel_t* <a class="el" href="group___global_defs.html#ga457ed655bd58ace1a3b11b4bd19da8e9">hipKernel_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga494ada27be8218d3181e6d88f3196b79" name="ga494ada27be8218d3181e6d88f3196b79"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga494ada27be8218d3181e6d88f3196b79">&#9670;&#160;</a></span>hipLibrary_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct ihipLibrary_t* <a class="el" href="group___global_defs.html#ga494ada27be8218d3181e6d88f3196b79">hipLibrary_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga1d7d9b2f511df4d4841c6f30ff01fbd8" name="ga1d7d9b2f511df4d4841c6f30ff01fbd8"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga1d7d9b2f511df4d4841c6f30ff01fbd8">&#9670;&#160;</a></span>hipLinkState_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct ihipLinkState_t* <a class="el" href="group___global_defs.html#ga1d7d9b2f511df4d4841c6f30ff01fbd8">hipLinkState_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gae466e78534ea3eef06973cd06aea9840" name="gae466e78534ea3eef06973cd06aea9840"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gae466e78534ea3eef06973cd06aea9840">&#9670;&#160;</a></span>hipMemGenericAllocationHandle_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct ihipMemGenericAllocationHandle* <a class="el" href="group___global_defs.html#gae466e78534ea3eef06973cd06aea9840">hipMemGenericAllocationHandle_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Generic handle for memory allocation </p>

</div>
</div>
<a id="gaf61ebfa5ef0825fb2a763ae42daa20f0" name="gaf61ebfa5ef0825fb2a763ae42daa20f0"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaf61ebfa5ef0825fb2a763ae42daa20f0">&#9670;&#160;</a></span>hipMemPool_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct ihipMemPoolHandle_t* <a class="el" href="group___global_defs.html#gaf61ebfa5ef0825fb2a763ae42daa20f0">hipMemPool_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP memory pool </p>

</div>
</div>
<a id="gab0b1dd6ce7ee1720c2970552c20173e8" name="gab0b1dd6ce7ee1720c2970552c20173e8"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gab0b1dd6ce7ee1720c2970552c20173e8">&#9670;&#160;</a></span>hipModule_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct ihipModule_t* <a class="el" href="group___global_defs.html#gab0b1dd6ce7ee1720c2970552c20173e8">hipModule_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga0fc4326b345ac109cb72b90a22a1cb29" name="ga0fc4326b345ac109cb72b90a22a1cb29"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga0fc4326b345ac109cb72b90a22a1cb29">&#9670;&#160;</a></span>hipStream_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct ihipStream_t* <a class="el" href="group___global_defs.html#ga0fc4326b345ac109cb72b90a22a1cb29">hipStream_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gab5b072cf29fa8e0a61cbad91e3798565" name="gab5b072cf29fa8e0a61cbad91e3798565"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gab5b072cf29fa8e0a61cbad91e3798565">&#9670;&#160;</a></span>hipUserObject_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct hipUserObject* <a class="el" href="group___global_defs.html#gab5b072cf29fa8e0a61cbad91e3798565">hipUserObject_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>An opaque value that represents a user obj </p>

</div>
</div>
<h2 class="groupheader">Enumeration Type Documentation</h2>
<a id="ga193abcc67d55b127bc5c0bc3625de907" name="ga193abcc67d55b127bc5c0bc3625de907"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga193abcc67d55b127bc5c0bc3625de907">&#9670;&#160;</a></span>hipAccessProperty</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga193abcc67d55b127bc5c0bc3625de907">hipAccessProperty</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Specifies performance hint with <a class="el" href="structhip_access_policy_window.html">hipAccessPolicyWindow</a> </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga193abcc67d55b127bc5c0bc3625de907a5e691c3d2417d1fabbd2eb753829db97" name="gga193abcc67d55b127bc5c0bc3625de907a5e691c3d2417d1fabbd2eb753829db97"></a>hipAccessPropertyNormal&#160;</td><td class="fielddoc"><p>Normal cache persistence. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga193abcc67d55b127bc5c0bc3625de907ac4b5d4099632e30e4c21c77490290319" name="gga193abcc67d55b127bc5c0bc3625de907ac4b5d4099632e30e4c21c77490290319"></a>hipAccessPropertyStreaming&#160;</td><td class="fielddoc"><p>Streaming access is less likely to persist from cache. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga193abcc67d55b127bc5c0bc3625de907aa1a91b8045c860f890f8741de827f92f" name="gga193abcc67d55b127bc5c0bc3625de907aa1a91b8045c860f890f8741de827f92f"></a>hipAccessPropertyPersisting&#160;</td><td class="fielddoc"><p>Persisting access is more likely to persist in cache. </p>
</td></tr>
</table>

</div>
</div>
<a id="gafd065a07554c87b025803c4b0bb98c0c" name="gafd065a07554c87b025803c4b0bb98c0c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gafd065a07554c87b025803c4b0bb98c0c">&#9670;&#160;</a></span>hipArraySparseSubresourceType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gafd065a07554c87b025803c4b0bb98c0c">hipArraySparseSubresourceType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Subresource types for sparse arrays </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggafd065a07554c87b025803c4b0bb98c0ca4950320e5bdbe31969dbf76b1112023c" name="ggafd065a07554c87b025803c4b0bb98c0ca4950320e5bdbe31969dbf76b1112023c"></a>hipArraySparseSubresourceTypeSparseLevel&#160;</td><td class="fielddoc"><p>Sparse level. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggafd065a07554c87b025803c4b0bb98c0ca662c94e0dc0635529c2c003cf64d3bdf" name="ggafd065a07554c87b025803c4b0bb98c0ca662c94e0dc0635529c2c003cf64d3bdf"></a>hipArraySparseSubresourceTypeMiptail&#160;</td><td class="fielddoc"><p>Miptail. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga35133e080ad8aecd57ec2c5387e3a376" name="ga35133e080ad8aecd57ec2c5387e3a376"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga35133e080ad8aecd57ec2c5387e3a376">&#9670;&#160;</a></span>hipComputeMode</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga35133e080ad8aecd57ec2c5387e3a376">hipComputeMode</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga35133e080ad8aecd57ec2c5387e3a376a9565a36ccb87755b51f42e1cf150bba6" name="gga35133e080ad8aecd57ec2c5387e3a376a9565a36ccb87755b51f42e1cf150bba6"></a>hipComputeModeDefault&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga35133e080ad8aecd57ec2c5387e3a376a92d8c4babfb6cdce4c7db31d420f72ca" name="gga35133e080ad8aecd57ec2c5387e3a376a92d8c4babfb6cdce4c7db31d420f72ca"></a>hipComputeModeExclusive&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga35133e080ad8aecd57ec2c5387e3a376a41e725f5f69f23e23eff05c4c64cfe8d" name="gga35133e080ad8aecd57ec2c5387e3a376a41e725f5f69f23e23eff05c4c64cfe8d"></a>hipComputeModeProhibited&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga35133e080ad8aecd57ec2c5387e3a376a9d39a96ce69f00a1fd859a436ef6e060" name="gga35133e080ad8aecd57ec2c5387e3a376a9d39a96ce69f00a1fd859a436ef6e060"></a>hipComputeModeExclusiveProcess&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="gacc0acd7b9bda126c6bb3dfd6e2796d7c" name="gacc0acd7b9bda126c6bb3dfd6e2796d7c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gacc0acd7b9bda126c6bb3dfd6e2796d7c">&#9670;&#160;</a></span>hipDeviceAttribute_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gacc0acd7b9bda126c6bb3dfd6e2796d7c">hipDeviceAttribute_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>hipDeviceAttribute_t hipDeviceAttributeUnused number: 5 </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cad6f798685ee7e3c0c598b768deed019e" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cad6f798685ee7e3c0c598b768deed019e"></a>hipDeviceAttributeCudaCompatibleBegin&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca52fa8868e3d06d6ceed35072946c4500" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca52fa8868e3d06d6ceed35072946c4500"></a>hipDeviceAttributeEccEnabled&#160;</td><td class="fielddoc"><p>Whether ECC support is enabled. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca3453c7d157ca16c6a94c312205c3ae86" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca3453c7d157ca16c6a94c312205c3ae86"></a>hipDeviceAttributeAccessPolicyMaxWindowSize&#160;</td><td class="fielddoc"><p>Cuda only. The maximum size of the window policy in bytes. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca773d2f74a90f647fcfec39ba19aa7b9e" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca773d2f74a90f647fcfec39ba19aa7b9e"></a>hipDeviceAttributeAsyncEngineCount&#160;</td><td class="fielddoc"><p>Asynchronous engines number. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca9753ae75a27d737cb02c3ef762275106" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca9753ae75a27d737cb02c3ef762275106"></a>hipDeviceAttributeCanMapHostMemory&#160;</td><td class="fielddoc"><p>Whether host memory can be mapped into device address space </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca56a8b8ee9b1165461ea6c1ee7d56e90d" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca56a8b8ee9b1165461ea6c1ee7d56e90d"></a>hipDeviceAttributeCanUseHostPointerForRegisteredMem&#160;</td><td class="fielddoc"><p>Device can access host registered memory at the same virtual address as the CPU </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca2300e077e020e7967592065561373b00" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca2300e077e020e7967592065561373b00"></a>hipDeviceAttributeClockRate&#160;</td><td class="fielddoc"><p>Peak clock frequency in kilohertz. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4d0369a6ef7bd7890fdcabc16ed3385d" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4d0369a6ef7bd7890fdcabc16ed3385d"></a>hipDeviceAttributeComputeMode&#160;</td><td class="fielddoc"><p>Compute mode that device is currently in. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8af4079129030527721246176198f75d" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8af4079129030527721246176198f75d"></a>hipDeviceAttributeComputePreemptionSupported&#160;</td><td class="fielddoc"><p>Device supports Compute Preemption. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cad9f45254d0d048677f560032532d5504" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cad9f45254d0d048677f560032532d5504"></a>hipDeviceAttributeConcurrentKernels&#160;</td><td class="fielddoc"><p>Device can possibly execute multiple kernels concurrently. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca9e5af4761458152e645d2e1312767514" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca9e5af4761458152e645d2e1312767514"></a>hipDeviceAttributeConcurrentManagedAccess&#160;</td><td class="fielddoc"><p>Device can coherently access managed memory concurrently with the CPU </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6ffb0a3933411c136ea1f9d154fab5cc" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6ffb0a3933411c136ea1f9d154fab5cc"></a>hipDeviceAttributeCooperativeLaunch&#160;</td><td class="fielddoc"><p>Support cooperative launch. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5169c438b4ba17f8588d744bf56d87e4" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5169c438b4ba17f8588d744bf56d87e4"></a>hipDeviceAttributeCooperativeMultiDeviceLaunch&#160;</td><td class="fielddoc"><p>Support cooperative launch on multiple devices </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca41202a4affefb5cf099beb8c8bf70bbf" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca41202a4affefb5cf099beb8c8bf70bbf"></a>hipDeviceAttributeDeviceOverlap&#160;</td><td class="fielddoc"><p>Device can concurrently copy memory and execute a kernel. Deprecated. Use instead asyncEngineCount. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca0037b357264179e4093c551a80a2a21c" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca0037b357264179e4093c551a80a2a21c"></a>hipDeviceAttributeDirectManagedMemAccessFromHost&#160;</td><td class="fielddoc"><p>Host can directly access managed memory on the device without migration </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca28029ba35569753cbdbd777b21eab37b" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca28029ba35569753cbdbd777b21eab37b"></a>hipDeviceAttributeGlobalL1CacheSupported&#160;</td><td class="fielddoc"><p>Device supports caching globals in L1. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca1421bb450fe736fda9605a607be69836" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca1421bb450fe736fda9605a607be69836"></a>hipDeviceAttributeHostNativeAtomicSupported&#160;</td><td class="fielddoc"><p>Link between the device and the host supports native atomic operations </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caa384485d5fe1ac26746d817af1aa669b" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caa384485d5fe1ac26746d817af1aa669b"></a>hipDeviceAttributeIntegrated&#160;</td><td class="fielddoc"><p>Device is integrated GPU. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6129311200a17dcc5fa8d2256874ae3d" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6129311200a17dcc5fa8d2256874ae3d"></a>hipDeviceAttributeIsMultiGpuBoard&#160;</td><td class="fielddoc"><p>Multiple GPU devices. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca58434135137ef3af09567698829810f1" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca58434135137ef3af09567698829810f1"></a>hipDeviceAttributeKernelExecTimeout&#160;</td><td class="fielddoc"><p>Run time limit for kernels executed on the device. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca582ae5a26a7148504878890028e4b64c" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca582ae5a26a7148504878890028e4b64c"></a>hipDeviceAttributeL2CacheSize&#160;</td><td class="fielddoc"><p>Size of L2 cache in bytes. 0 if the device doesn't have L2 cache. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca7d251fb7e063e4703489eddbc41a440d" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca7d251fb7e063e4703489eddbc41a440d"></a>hipDeviceAttributeLocalL1CacheSupported&#160;</td><td class="fielddoc"><p>caching locals in L1 is supported </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cada0ca948530460469095f6a63729219a" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cada0ca948530460469095f6a63729219a"></a>hipDeviceAttributeLuid&#160;</td><td class="fielddoc"><p>8-byte locally unique identifier in 8 bytes. Undefined on TCC and non-Windows platforms </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caea6c84c14d2539fc9abcdfb0f940acbe" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caea6c84c14d2539fc9abcdfb0f940acbe"></a>hipDeviceAttributeLuidDeviceNodeMask&#160;</td><td class="fielddoc"><p>Luid device node mask. Undefined on TCC and non-Windows platforms </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca2735739cf977b7d303266f6781131e8d" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca2735739cf977b7d303266f6781131e8d"></a>hipDeviceAttributeComputeCapabilityMajor&#160;</td><td class="fielddoc"><p>Major compute capability version number. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caa1a9b27307b3dda43201bfaead8458c5" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caa1a9b27307b3dda43201bfaead8458c5"></a>hipDeviceAttributeManagedMemory&#160;</td><td class="fielddoc"><p>Device supports allocating managed memory on this system. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caae53485511cc012addc523e602ef9b98" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caae53485511cc012addc523e602ef9b98"></a>hipDeviceAttributeMaxBlocksPerMultiProcessor&#160;</td><td class="fielddoc"><p>Max block size per multiprocessor. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cac1e4ac589db0d8adbbc241e3d0fcd594" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cac1e4ac589db0d8adbbc241e3d0fcd594"></a>hipDeviceAttributeMaxBlockDimX&#160;</td><td class="fielddoc"><p>Max block size in width. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca187dbffe12db09a56c0f75c340d879c9" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca187dbffe12db09a56c0f75c340d879c9"></a>hipDeviceAttributeMaxBlockDimY&#160;</td><td class="fielddoc"><p>Max block size in height. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caf811f51e03d1ffb025d80ac1da088675" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caf811f51e03d1ffb025d80ac1da088675"></a>hipDeviceAttributeMaxBlockDimZ&#160;</td><td class="fielddoc"><p>Max block size in depth. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca03db8df0e7a9fbdaae683d97e8ac9c87" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca03db8df0e7a9fbdaae683d97e8ac9c87"></a>hipDeviceAttributeMaxGridDimX&#160;</td><td class="fielddoc"><p>Max grid size in width. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5b5cc49972679c5ccf62b79425ee99df" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5b5cc49972679c5ccf62b79425ee99df"></a>hipDeviceAttributeMaxGridDimY&#160;</td><td class="fielddoc"><p>Max grid size in height. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6c206ac083999caf4640e5d91dae24f7" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6c206ac083999caf4640e5d91dae24f7"></a>hipDeviceAttributeMaxGridDimZ&#160;</td><td class="fielddoc"><p>Max grid size in depth. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8d9538aecd5fa764b6b13dd9ae05a1cf" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8d9538aecd5fa764b6b13dd9ae05a1cf"></a>hipDeviceAttributeMaxSurface1D&#160;</td><td class="fielddoc"><p>Maximum size of 1D surface. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca48c9f35454f5c329718bec08b54e8928" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca48c9f35454f5c329718bec08b54e8928"></a>hipDeviceAttributeMaxSurface1DLayered&#160;</td><td class="fielddoc"><p>Cuda only. Maximum dimensions of 1D layered surface. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca45e5f8d0e1b6b8ba58cf4b0f00b793b0" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca45e5f8d0e1b6b8ba58cf4b0f00b793b0"></a>hipDeviceAttributeMaxSurface2D&#160;</td><td class="fielddoc"><p>Maximum dimension (width, height) of 2D surface. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca63f784bd3a09ed4b9c1feb3628410bbe" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca63f784bd3a09ed4b9c1feb3628410bbe"></a>hipDeviceAttributeMaxSurface2DLayered&#160;</td><td class="fielddoc"><p>Cuda only. Maximum dimensions of 2D layered surface. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca09c1178054d1e7eda20fd5bd5dd17175" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca09c1178054d1e7eda20fd5bd5dd17175"></a>hipDeviceAttributeMaxSurface3D&#160;</td><td class="fielddoc"><p>Maximum dimension (width, height, depth) of 3D surface. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca1a76a9768fb8e98c4f437e3f7962027f" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca1a76a9768fb8e98c4f437e3f7962027f"></a>hipDeviceAttributeMaxSurfaceCubemap&#160;</td><td class="fielddoc"><p>Cuda only. Maximum dimensions of Cubemap surface. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca08a044c95db3574e2c89ca856adcf4df" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca08a044c95db3574e2c89ca856adcf4df"></a>hipDeviceAttributeMaxSurfaceCubemapLayered&#160;</td><td class="fielddoc"><p>Cuda only. Maximum dimension of Cubemap layered surface. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca9ca92f0db9775c913bc681d87449bf1a" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca9ca92f0db9775c913bc681d87449bf1a"></a>hipDeviceAttributeMaxTexture1DWidth&#160;</td><td class="fielddoc"><p>Maximum size of 1D texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cacc59d7cf69f95371c8e8d7fbccf13e73" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cacc59d7cf69f95371c8e8d7fbccf13e73"></a>hipDeviceAttributeMaxTexture1DLayered&#160;</td><td class="fielddoc"><p>Maximum dimensions of 1D layered texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca929925869c0fee0db630b4fd08f87b3a" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca929925869c0fee0db630b4fd08f87b3a"></a>hipDeviceAttributeMaxTexture1DLinear&#160;</td><td class="fielddoc"><p>Maximum number of elements allocatable in a 1D linear texture. Use cudaDeviceGetTexture1DLinearMaxWidth() instead on Cuda. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca2428066c6ecb425d5b61c7532042bedf" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca2428066c6ecb425d5b61c7532042bedf"></a>hipDeviceAttributeMaxTexture1DMipmap&#160;</td><td class="fielddoc"><p>Maximum size of 1D mipmapped texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caba995e4cf2e8e3cf99dbca7c5adf4342" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caba995e4cf2e8e3cf99dbca7c5adf4342"></a>hipDeviceAttributeMaxTexture2DWidth&#160;</td><td class="fielddoc"><p>Maximum dimension width of 2D texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca523ab7684ddf2fd7ad7e7b9123e49163" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca523ab7684ddf2fd7ad7e7b9123e49163"></a>hipDeviceAttributeMaxTexture2DHeight&#160;</td><td class="fielddoc"><p>Maximum dimension hight of 2D texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca92b064e8b236f1d06b528056ce6fddae" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca92b064e8b236f1d06b528056ce6fddae"></a>hipDeviceAttributeMaxTexture2DGather&#160;</td><td class="fielddoc"><p>Maximum dimensions of 2D texture if gather operations performed. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caa4d2c06274d024a40fc0e4b797a5a3a2" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caa4d2c06274d024a40fc0e4b797a5a3a2"></a>hipDeviceAttributeMaxTexture2DLayered&#160;</td><td class="fielddoc"><p>Maximum dimensions of 2D layered texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca45b44857785bff4085506a56022fbf0f" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca45b44857785bff4085506a56022fbf0f"></a>hipDeviceAttributeMaxTexture2DLinear&#160;</td><td class="fielddoc"><p>Maximum dimensions (width, height, pitch) of 2D textures bound to pitched memory. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caf1b78e548e4cd729f0e0be4ab7736c62" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caf1b78e548e4cd729f0e0be4ab7736c62"></a>hipDeviceAttributeMaxTexture2DMipmap&#160;</td><td class="fielddoc"><p>Maximum dimensions of 2D mipmapped texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cac38a9aec2fba4d56ad90a0bd76c26380" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cac38a9aec2fba4d56ad90a0bd76c26380"></a>hipDeviceAttributeMaxTexture3DWidth&#160;</td><td class="fielddoc"><p>Maximum dimension width of 3D texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca36a3b206969474f65c0d5ad4831c1ba8" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca36a3b206969474f65c0d5ad4831c1ba8"></a>hipDeviceAttributeMaxTexture3DHeight&#160;</td><td class="fielddoc"><p>Maximum dimension height of 3D texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caa7be0131e8f44109c377ca1b7d634ce7" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caa7be0131e8f44109c377ca1b7d634ce7"></a>hipDeviceAttributeMaxTexture3DDepth&#160;</td><td class="fielddoc"><p>Maximum dimension depth of 3D texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca90020ecaeb108308c5b13a335d5c9130" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca90020ecaeb108308c5b13a335d5c9130"></a>hipDeviceAttributeMaxTexture3DAlt&#160;</td><td class="fielddoc"><p>Maximum dimensions of alternate 3D texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca3b576766317055e3bf321761fe5d84fd" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca3b576766317055e3bf321761fe5d84fd"></a>hipDeviceAttributeMaxTextureCubemap&#160;</td><td class="fielddoc"><p>Maximum dimensions of Cubemap texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caeab620ddac9e5520e0411fda9f6a5fb1" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caeab620ddac9e5520e0411fda9f6a5fb1"></a>hipDeviceAttributeMaxTextureCubemapLayered&#160;</td><td class="fielddoc"><p>Maximum dimensions of Cubemap layered texture. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5a4d13aaac8710b1d078306125f24e25" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5a4d13aaac8710b1d078306125f24e25"></a>hipDeviceAttributeMaxThreadsDim&#160;</td><td class="fielddoc"><p>Maximum dimension of a block. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8327aa23782d9c994bdef33a6d62e02e" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8327aa23782d9c994bdef33a6d62e02e"></a>hipDeviceAttributeMaxThreadsPerBlock&#160;</td><td class="fielddoc"><p>Maximum number of threads per block. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caddc08922b491eb1f6a583833cbf4e2f0" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caddc08922b491eb1f6a583833cbf4e2f0"></a>hipDeviceAttributeMaxThreadsPerMultiProcessor&#160;</td><td class="fielddoc"><p>Maximum resident threads per multiprocessor. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca0b3f58899744df724961b664061afd54" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca0b3f58899744df724961b664061afd54"></a>hipDeviceAttributeMaxPitch&#160;</td><td class="fielddoc"><p>Maximum pitch in bytes allowed by memory copies. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca848c1396fab6f20463c6aefb828b0870" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca848c1396fab6f20463c6aefb828b0870"></a>hipDeviceAttributeMemoryBusWidth&#160;</td><td class="fielddoc"><p>Global memory bus width in bits. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6b68deafd65f036b30dc8051573eb000" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6b68deafd65f036b30dc8051573eb000"></a>hipDeviceAttributeMemoryClockRate&#160;</td><td class="fielddoc"><p>Peak memory clock frequency in kilohertz. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca38edc4fcae456e47160d349da3249b85" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca38edc4fcae456e47160d349da3249b85"></a>hipDeviceAttributeComputeCapabilityMinor&#160;</td><td class="fielddoc"><p>Minor compute capability version number. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca7770672185967b47674798253cb7f47d" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca7770672185967b47674798253cb7f47d"></a>hipDeviceAttributeMultiGpuBoardGroupID&#160;</td><td class="fielddoc"><p>Unique ID of device group on the same multi-GPU board </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5c1519870733ccf0b83f722678240e5f" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5c1519870733ccf0b83f722678240e5f"></a>hipDeviceAttributeMultiprocessorCount&#160;</td><td class="fielddoc"><p>Number of multi-processors. When the GPU works in Compute Unit (CU) mode, this value equals the number of CUs; when in Workgroup Processor (WGP) mode, this value equels half of CUs, because a single WGP contains two CUs. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8dcc079d3099aadfd6d37c9614f91407" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8dcc079d3099aadfd6d37c9614f91407"></a>hipDeviceAttributeUnused1&#160;</td><td class="fielddoc"><p>Previously hipDeviceAttributeName. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca21e422662a09d4894c8ebc60473384ff" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca21e422662a09d4894c8ebc60473384ff"></a>hipDeviceAttributePageableMemoryAccess&#160;</td><td class="fielddoc"><p>Device supports coherently accessing pageable memory without calling hipHostRegister on it </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca14dff2a1b8c0ba131b06a6685bb052f3" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca14dff2a1b8c0ba131b06a6685bb052f3"></a>hipDeviceAttributePageableMemoryAccessUsesHostPageTables&#160;</td><td class="fielddoc"><p>Device accesses pageable memory via the host's page tables </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca572b29c44f1322aa7657fdd784832f88" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca572b29c44f1322aa7657fdd784832f88"></a>hipDeviceAttributePciBusId&#160;</td><td class="fielddoc"><p>PCI Bus ID. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca955d90286e87be9e3528f0b817ab32ff" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca955d90286e87be9e3528f0b817ab32ff"></a>hipDeviceAttributePciDeviceId&#160;</td><td class="fielddoc"><p>PCI Device ID. Returns pcie slot id. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca83b77edfc8ef6044cc602af64969518c" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca83b77edfc8ef6044cc602af64969518c"></a>hipDeviceAttributePciDomainId&#160;</td><td class="fielddoc"><p>PCI Domain Id. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cadb8cdb8c1f1e140ae5340cf9fbe8aa8e" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cadb8cdb8c1f1e140ae5340cf9fbe8aa8e"></a>hipDeviceAttributePciDomainID&#160;</td><td class="fielddoc"><p>PCI Domain ID, for backward compatibility. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca52d3c74a3d94c02ebfda31b32a0cd75a" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca52d3c74a3d94c02ebfda31b32a0cd75a"></a>hipDeviceAttributePersistingL2CacheMaxSize&#160;</td><td class="fielddoc"><p>Maximum l2 persisting lines capacity in bytes. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca82289b170192b6ea742be0efc6f95107" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca82289b170192b6ea742be0efc6f95107"></a>hipDeviceAttributeMaxRegistersPerBlock&#160;</td><td class="fielddoc"><p>32-bit registers available to a thread block. This number is shared by all thread blocks simultaneously resident on a multiprocessor. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5f366458f31c0dc0f3faa0a11446ada4" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5f366458f31c0dc0f3faa0a11446ada4"></a>hipDeviceAttributeMaxRegistersPerMultiprocessor&#160;</td><td class="fielddoc"><p>32-bit registers available per block. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cad612849d153747b7be03b0e697a2aead" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cad612849d153747b7be03b0e697a2aead"></a>hipDeviceAttributeReservedSharedMemPerBlock&#160;</td><td class="fielddoc"><p>Shared memory reserved by CUDA driver per block. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca7bca3aa18b26d40eba043ae93e15c7e5" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca7bca3aa18b26d40eba043ae93e15c7e5"></a>hipDeviceAttributeMaxSharedMemoryPerBlock&#160;</td><td class="fielddoc"><p>Maximum shared memory available per block in bytes. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6299fb9b996d154c456d1622d447fe47" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6299fb9b996d154c456d1622d447fe47"></a>hipDeviceAttributeSharedMemPerBlockOptin&#160;</td><td class="fielddoc"><p>Maximum shared memory per block usable by special opt in. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cae88a51d68a16de43c9036bd1c555e0c9" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cae88a51d68a16de43c9036bd1c555e0c9"></a>hipDeviceAttributeSharedMemPerMultiprocessor&#160;</td><td class="fielddoc"><p>Shared memory available per multiprocessor. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5aa88c2c66ab8d71bb5b3177da16eecd" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5aa88c2c66ab8d71bb5b3177da16eecd"></a>hipDeviceAttributeSingleToDoublePrecisionPerfRatio&#160;</td><td class="fielddoc"><p>Cuda only. Performance ratio of single precision to double precision. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca7ace06929e3bb30616db62f966ad50db" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca7ace06929e3bb30616db62f966ad50db"></a>hipDeviceAttributeStreamPrioritiesSupported&#160;</td><td class="fielddoc"><p>Whether to support stream priorities. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca02af979ebb5db7921872c8eff4d667bd" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca02af979ebb5db7921872c8eff4d667bd"></a>hipDeviceAttributeSurfaceAlignment&#160;</td><td class="fielddoc"><p>Alignment requirement for surfaces. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca0eb1b68cd4148e015736be9dc965caa4" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca0eb1b68cd4148e015736be9dc965caa4"></a>hipDeviceAttributeTccDriver&#160;</td><td class="fielddoc"><p>Cuda only. Whether device is a Tesla device using TCC driver. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cac72b2427df2ba58dbbee2e1399b3e135" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cac72b2427df2ba58dbbee2e1399b3e135"></a>hipDeviceAttributeTextureAlignment&#160;</td><td class="fielddoc"><p>Alignment requirement for textures. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cae044c1754ea66c8f9f7b420a2f14671e" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cae044c1754ea66c8f9f7b420a2f14671e"></a>hipDeviceAttributeTexturePitchAlignment&#160;</td><td class="fielddoc"><p>Pitch alignment requirement for 2D texture references bound to pitched memory; </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cac6089ac3a0f9c77cc382fb0eaa73ae9c" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cac6089ac3a0f9c77cc382fb0eaa73ae9c"></a>hipDeviceAttributeTotalConstantMemory&#160;</td><td class="fielddoc"><p>Constant memory size in bytes. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caad0e1bd8d5bb28ae8e0c710fd70bea29" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caad0e1bd8d5bb28ae8e0c710fd70bea29"></a>hipDeviceAttributeTotalGlobalMem&#160;</td><td class="fielddoc"><p>Global memory available on devicice. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca72a250028cf4eac11a83410a86de83a4" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca72a250028cf4eac11a83410a86de83a4"></a>hipDeviceAttributeUnifiedAddressing&#160;</td><td class="fielddoc"><p>Cuda only. An unified address space shared with the host. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6d7bf28444bf5fe676c4260333e2da7c" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6d7bf28444bf5fe676c4260333e2da7c"></a>hipDeviceAttributeUnused2&#160;</td><td class="fielddoc"><p>Previously hipDeviceAttributeUuid. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caffd94133e823247a6f1215343232f6ec" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caffd94133e823247a6f1215343232f6ec"></a>hipDeviceAttributeWarpSize&#160;</td><td class="fielddoc"><p>Warp size in threads. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caef1d9fb1d5d0c6129903d93ddae8c4ca" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caef1d9fb1d5d0c6129903d93ddae8c4ca"></a>hipDeviceAttributeMemoryPoolsSupported&#160;</td><td class="fielddoc"><p>Device supports HIP Stream Ordered Memory Allocator. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caecdccc51c9b30e22a154839d5827a615" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caecdccc51c9b30e22a154839d5827a615"></a>hipDeviceAttributeVirtualMemoryManagementSupported&#160;</td><td class="fielddoc"><p>Device supports HIP virtual memory management </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cae7fc4b89d3474089f40e2206866f658a" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cae7fc4b89d3474089f40e2206866f658a"></a>hipDeviceAttributeHostRegisterSupported&#160;</td><td class="fielddoc"><p>Can device support host memory registration via hipHostRegister </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca85d831cf51005e06956c389c37d071bb" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca85d831cf51005e06956c389c37d071bb"></a>hipDeviceAttributeMemoryPoolSupportedHandleTypes&#160;</td><td class="fielddoc"><p>Supported handle mask for HIP Stream Ordered Memory Allocator </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caa360d503e92d5dfc48b373e863547441" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caa360d503e92d5dfc48b373e863547441"></a>hipDeviceAttributeHostNumaId&#160;</td><td class="fielddoc"><p>NUMA ID of the cpu node closest to the device, or -1 when NUMA isn't supported </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca23a769372f05b3d4b1bf28a9fd46991a" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca23a769372f05b3d4b1bf28a9fd46991a"></a>hipDeviceAttributeCudaCompatibleEnd&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5f195e2a51f8fb6fa40dbe443d2b0279" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca5f195e2a51f8fb6fa40dbe443d2b0279"></a>hipDeviceAttributeAmdSpecificBegin&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caefd7213ecdc587ca7e74822d2ca97309" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caefd7213ecdc587ca7e74822d2ca97309"></a>hipDeviceAttributeClockInstructionRate&#160;</td><td class="fielddoc"><p>Frequency in khz of the timer used by the device-side "clock*" </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cac4750f9f64dfe4455e58c2ba7e073f87" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cac4750f9f64dfe4455e58c2ba7e073f87"></a>hipDeviceAttributeUnused3&#160;</td><td class="fielddoc"><p>Previously hipDeviceAttributeArch. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cad3e7f3d01533b32e12211172fcf410ba" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cad3e7f3d01533b32e12211172fcf410ba"></a>hipDeviceAttributeMaxSharedMemoryPerMultiprocessor&#160;</td><td class="fielddoc"><p>Maximum Shared Memory PerMultiprocessor. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4ff9d7bb9ee05b2ae28caa535a81dcf0" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4ff9d7bb9ee05b2ae28caa535a81dcf0"></a>hipDeviceAttributeUnused4&#160;</td><td class="fielddoc"><p>Previously hipDeviceAttributeGcnArch. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca1694fee46a4b2befda6ecb7e058f53fc" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca1694fee46a4b2befda6ecb7e058f53fc"></a>hipDeviceAttributeUnused5&#160;</td><td class="fielddoc"><p>Previously hipDeviceAttributeGcnArchName. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6c9f83e4239d19aa000dd13cbcfc00dd" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6c9f83e4239d19aa000dd13cbcfc00dd"></a>hipDeviceAttributeHdpMemFlushCntl&#160;</td><td class="fielddoc"><p>Address of the HDP_MEM_COHERENCY_FLUSH_CNTL register. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca49f4f8395025ba1ebe1a0a7eff0f24ed" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca49f4f8395025ba1ebe1a0a7eff0f24ed"></a>hipDeviceAttributeHdpRegFlushCntl&#160;</td><td class="fielddoc"><p>Address of the HDP_REG_COHERENCY_FLUSH_CNTL register. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4d791a8a67ad0c89d413a67ce184be5d" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4d791a8a67ad0c89d413a67ce184be5d"></a>hipDeviceAttributeCooperativeMultiDeviceUnmatchedFunc&#160;</td><td class="fielddoc"><p>Supports cooperative launch on multiple devices with unmatched functions </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caa5679987f35a74bfcbb1d3ac36db73cb" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caa5679987f35a74bfcbb1d3ac36db73cb"></a>hipDeviceAttributeCooperativeMultiDeviceUnmatchedGridDim&#160;</td><td class="fielddoc"><p>Supports cooperative launch on multiple devices with unmatched grid dimensions </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caeb7c0c783e1f88a0675726bf2da6424b" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caeb7c0c783e1f88a0675726bf2da6424b"></a>hipDeviceAttributeCooperativeMultiDeviceUnmatchedBlockDim&#160;</td><td class="fielddoc"><p>Supports cooperative launch on multiple devices with unmatched block dimensions </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca3295f0728fc8152a98556d89ba81216f" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca3295f0728fc8152a98556d89ba81216f"></a>hipDeviceAttributeCooperativeMultiDeviceUnmatchedSharedMem&#160;</td><td class="fielddoc"><p>Supports cooperative launch on multiple devices with unmatched shared memories </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cab980fc82595b70b6338b9dd2b913ec26" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cab980fc82595b70b6338b9dd2b913ec26"></a>hipDeviceAttributeIsLargeBar&#160;</td><td class="fielddoc"><p>Whether it is LargeBar. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4e443d1d515e56a1f8cee4a9f3a7a546" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4e443d1d515e56a1f8cee4a9f3a7a546"></a>hipDeviceAttributeAsicRevision&#160;</td><td class="fielddoc"><p>Revision of the GPU in this device. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8179e5c1507831eaeb4690513e618913" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca8179e5c1507831eaeb4690513e618913"></a>hipDeviceAttributeCanUseStreamWaitValue&#160;</td><td class="fielddoc"><p>'1' if Device supports <a class="el" href="group___stream_m.html#gafade0b118c7ed28e1dae21cd4df0a9d6" title="Enqueues a wait command to the stream.[BETA].">hipStreamWaitValue32()</a> and <a class="el" href="group___stream_m.html#ga9ef06d564d19ef9afc11d60d20c9c541" title="Enqueues a wait command to the stream.[BETA].">hipStreamWaitValue64()</a>, '0' otherwise. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caaca61f2bab5521294fe5657fc7e6548c" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caaca61f2bab5521294fe5657fc7e6548c"></a>hipDeviceAttributeImageSupport&#160;</td><td class="fielddoc"><p>'1' if Device supports image, '0' otherwise. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7cae5ef640fe3203e10381d220b0c46be66" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7cae5ef640fe3203e10381d220b0c46be66"></a>hipDeviceAttributePhysicalMultiProcessorCount&#160;</td><td class="fielddoc"><p>All available physical compute units for the device </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6f1528b1afa5f1a70cd47680b353f96d" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca6f1528b1afa5f1a70cd47680b353f96d"></a>hipDeviceAttributeFineGrainSupport&#160;</td><td class="fielddoc"><p>'1' if Device supports fine grain, '0' otherwise </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca949a6be673b95e4af2c13f2003078e44" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca949a6be673b95e4af2c13f2003078e44"></a>hipDeviceAttributeWallClockRate&#160;</td><td class="fielddoc"><p>Constant frequency of wall clock in kilohertz. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca3ac50041beb59111a5c76edf03da0898" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca3ac50041beb59111a5c76edf03da0898"></a>hipDeviceAttributeNumberOfXccs&#160;</td><td class="fielddoc"><p>The number of XCC(s) on the device. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4a50a99d2921accb565746e4a17dd669" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca4a50a99d2921accb565746e4a17dd669"></a>hipDeviceAttributeMaxAvailableVgprsPerThread&#160;</td><td class="fielddoc"><p>Max number of available (directly or indirectly addressable) VGPRs per thread in DWORDs. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7caaaa98b5dee05f0ea04d08f61b0bddda9" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7caaaa98b5dee05f0ea04d08f61b0bddda9"></a>hipDeviceAttributePciChipId&#160;</td><td class="fielddoc"><p>GPU Manufacturer device id. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca652aba6828121b90705663532992a059" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca652aba6828121b90705663532992a059"></a>hipDeviceAttributeAmdSpecificEnd&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca9e5ce28ccb762bfb010dc35f4487d619" name="ggacc0acd7b9bda126c6bb3dfd6e2796d7ca9e5ce28ccb762bfb010dc35f4487d619"></a>hipDeviceAttributeVendorSpecificBegin&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga5582537cfebefc286383a3abeb71f4d1" name="ga5582537cfebefc286383a3abeb71f4d1"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga5582537cfebefc286383a3abeb71f4d1">&#9670;&#160;</a></span>hipDeviceP2PAttr</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga5582537cfebefc286383a3abeb71f4d1">hipDeviceP2PAttr</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga5582537cfebefc286383a3abeb71f4d1acda359cb54b8cc6654ccd470d2ae85b3" name="gga5582537cfebefc286383a3abeb71f4d1acda359cb54b8cc6654ccd470d2ae85b3"></a>hipDevP2PAttrPerformanceRank&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga5582537cfebefc286383a3abeb71f4d1a3ce64b7f78e8f5d2088a085182bdd703" name="gga5582537cfebefc286383a3abeb71f4d1a3ce64b7f78e8f5d2088a085182bdd703"></a>hipDevP2PAttrAccessSupported&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga5582537cfebefc286383a3abeb71f4d1a74da118b7d5fada7d20bade38a684fe8" name="gga5582537cfebefc286383a3abeb71f4d1a74da118b7d5fada7d20bade38a684fe8"></a>hipDevP2PAttrNativeAtomicSupported&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga5582537cfebefc286383a3abeb71f4d1a6e15f73f41e1c10fef0de092243d8a52" name="gga5582537cfebefc286383a3abeb71f4d1a6e15f73f41e1c10fef0de092243d8a52"></a>hipDevP2PAttrHipArrayAccessSupported&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga991ce0e0446fc74c393cb35d788402ac" name="ga991ce0e0446fc74c393cb35d788402ac"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga991ce0e0446fc74c393cb35d788402ac">&#9670;&#160;</a></span>hipDriverEntryPointQueryResult</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga991ce0e0446fc74c393cb35d788402ac">hipDriverEntryPointQueryResult</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga991ce0e0446fc74c393cb35d788402aca2e36ffb87a366a31ef49a0be950172eb" name="gga991ce0e0446fc74c393cb35d788402aca2e36ffb87a366a31ef49a0be950172eb"></a>hipDriverEntryPointSuccess&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga991ce0e0446fc74c393cb35d788402aca88a1895e1ad3e3478a2e5f3ee52dfcd4" name="gga991ce0e0446fc74c393cb35d788402aca88a1895e1ad3e3478a2e5f3ee52dfcd4"></a>hipDriverEntryPointSymbolNotFound&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga991ce0e0446fc74c393cb35d788402acaa97575c9d073709455a2b2712b24b6dc" name="gga991ce0e0446fc74c393cb35d788402acaa97575c9d073709455a2b2712b24b6dc"></a>hipDriverEntryPointVersionNotSufficent&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga3e30b1faa389b4565cae7af03d5d3e76" name="ga3e30b1faa389b4565cae7af03d5d3e76"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga3e30b1faa389b4565cae7af03d5d3e76">&#9670;&#160;</a></span>hipDriverProcAddressQueryResult</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga3e30b1faa389b4565cae7af03d5d3e76">hipDriverProcAddressQueryResult</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga3e30b1faa389b4565cae7af03d5d3e76a796004dd82889d925351ca710fd65d96" name="gga3e30b1faa389b4565cae7af03d5d3e76a796004dd82889d925351ca710fd65d96"></a>HIP_GET_PROC_ADDRESS_SUCCESS&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga3e30b1faa389b4565cae7af03d5d3e76a2575b187974521a7ac3a6ec0c4b1aad8" name="gga3e30b1faa389b4565cae7af03d5d3e76a2575b187974521a7ac3a6ec0c4b1aad8"></a>HIP_GET_PROC_ADDRESS_SYMBOL_NOT_FOUND&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga3e30b1faa389b4565cae7af03d5d3e76ab22f8a48ad16cbfa5c27e9ebba363723" name="gga3e30b1faa389b4565cae7af03d5d3e76ab22f8a48ad16cbfa5c27e9ebba363723"></a>HIP_GET_PROC_ADDRESS_VERSION_NOT_SUFFICIENT&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga47a3a9058e535f2a43a20982c39031bb" name="ga47a3a9058e535f2a43a20982c39031bb"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga47a3a9058e535f2a43a20982c39031bb">&#9670;&#160;</a></span>hipExternalMemoryHandleType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga47a3a9058e535f2a43a20982c39031bb">hipExternalMemoryHandleType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga47a3a9058e535f2a43a20982c39031bba754a120bc60fcfbf5f5290967c2bd299" name="gga47a3a9058e535f2a43a20982c39031bba754a120bc60fcfbf5f5290967c2bd299"></a>hipExternalMemoryHandleTypeOpaqueFd&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga47a3a9058e535f2a43a20982c39031bbab289071d76ed3fa028b0b72d6fe57863" name="gga47a3a9058e535f2a43a20982c39031bbab289071d76ed3fa028b0b72d6fe57863"></a>hipExternalMemoryHandleTypeOpaqueWin32&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga47a3a9058e535f2a43a20982c39031bbaa6231ff4442f793dc4472c406373909b" name="gga47a3a9058e535f2a43a20982c39031bbaa6231ff4442f793dc4472c406373909b"></a>hipExternalMemoryHandleTypeOpaqueWin32Kmt&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga47a3a9058e535f2a43a20982c39031bba84a3c0206a80b99170a9d9196d28d6d4" name="gga47a3a9058e535f2a43a20982c39031bba84a3c0206a80b99170a9d9196d28d6d4"></a>hipExternalMemoryHandleTypeD3D12Heap&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga47a3a9058e535f2a43a20982c39031bba2e2c241fcec7b8fcf092e271df4d900f" name="gga47a3a9058e535f2a43a20982c39031bba2e2c241fcec7b8fcf092e271df4d900f"></a>hipExternalMemoryHandleTypeD3D12Resource&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga47a3a9058e535f2a43a20982c39031bba07b9b9bd3833c3f66bae6d13f66c7f67" name="gga47a3a9058e535f2a43a20982c39031bba07b9b9bd3833c3f66bae6d13f66c7f67"></a>hipExternalMemoryHandleTypeD3D11Resource&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga47a3a9058e535f2a43a20982c39031bbad703b9b79a0f0d36eb8530ec81c0c4a0" name="gga47a3a9058e535f2a43a20982c39031bbad703b9b79a0f0d36eb8530ec81c0c4a0"></a>hipExternalMemoryHandleTypeD3D11ResourceKmt&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga47a3a9058e535f2a43a20982c39031bba45c9deab844e97f375ea28bec2877312" name="gga47a3a9058e535f2a43a20982c39031bba45c9deab844e97f375ea28bec2877312"></a>hipExternalMemoryHandleTypeNvSciBuf&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga4ea2e2748bf8cefee1d1cc3c800c10d5" name="ga4ea2e2748bf8cefee1d1cc3c800c10d5"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga4ea2e2748bf8cefee1d1cc3c800c10d5">&#9670;&#160;</a></span>hipExternalSemaphoreHandleType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga4ea2e2748bf8cefee1d1cc3c800c10d5">hipExternalSemaphoreHandleType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga4ea2e2748bf8cefee1d1cc3c800c10d5acb2af352ae589486b706635b5f273911" name="gga4ea2e2748bf8cefee1d1cc3c800c10d5acb2af352ae589486b706635b5f273911"></a>hipExternalSemaphoreHandleTypeOpaqueFd&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga4ea2e2748bf8cefee1d1cc3c800c10d5aeb0d35bd0276f67e86091dc3969355ac" name="gga4ea2e2748bf8cefee1d1cc3c800c10d5aeb0d35bd0276f67e86091dc3969355ac"></a>hipExternalSemaphoreHandleTypeOpaqueWin32&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga4ea2e2748bf8cefee1d1cc3c800c10d5a44c1a257f0e2605f6efd44741851e8d7" name="gga4ea2e2748bf8cefee1d1cc3c800c10d5a44c1a257f0e2605f6efd44741851e8d7"></a>hipExternalSemaphoreHandleTypeOpaqueWin32Kmt&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga4ea2e2748bf8cefee1d1cc3c800c10d5afff89d172e5aad8afea7021c55fa4fc1" name="gga4ea2e2748bf8cefee1d1cc3c800c10d5afff89d172e5aad8afea7021c55fa4fc1"></a>hipExternalSemaphoreHandleTypeD3D12Fence&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga4ea2e2748bf8cefee1d1cc3c800c10d5aa8d81456306ed714fb2ff92026a27dbe" name="gga4ea2e2748bf8cefee1d1cc3c800c10d5aa8d81456306ed714fb2ff92026a27dbe"></a>hipExternalSemaphoreHandleTypeD3D11Fence&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga4ea2e2748bf8cefee1d1cc3c800c10d5a317541984f3cd4af445918d4ac63ea64" name="gga4ea2e2748bf8cefee1d1cc3c800c10d5a317541984f3cd4af445918d4ac63ea64"></a>hipExternalSemaphoreHandleTypeNvSciSync&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga4ea2e2748bf8cefee1d1cc3c800c10d5a4e869593fe59e351dd981d7a4de95ec5" name="gga4ea2e2748bf8cefee1d1cc3c800c10d5a4e869593fe59e351dd981d7a4de95ec5"></a>hipExternalSemaphoreHandleTypeKeyedMutex&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga4ea2e2748bf8cefee1d1cc3c800c10d5a3c536b1ed5fdfd7618738ee61633e7a0" name="gga4ea2e2748bf8cefee1d1cc3c800c10d5a3c536b1ed5fdfd7618738ee61633e7a0"></a>hipExternalSemaphoreHandleTypeKeyedMutexKmt&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga4ea2e2748bf8cefee1d1cc3c800c10d5aef4e7167a49308a989588fcef88fbefe" name="gga4ea2e2748bf8cefee1d1cc3c800c10d5aef4e7167a49308a989588fcef88fbefe"></a>hipExternalSemaphoreHandleTypeTimelineSemaphoreFd&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga4ea2e2748bf8cefee1d1cc3c800c10d5aca482a93b49594fcc837429db03d96f1" name="gga4ea2e2748bf8cefee1d1cc3c800c10d5aca482a93b49594fcc837429db03d96f1"></a>hipExternalSemaphoreHandleTypeTimelineSemaphoreWin32&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga7f21ab1d42258d4f479a3bc4f420ac26" name="ga7f21ab1d42258d4f479a3bc4f420ac26"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga7f21ab1d42258d4f479a3bc4f420ac26">&#9670;&#160;</a></span>hipFlushGPUDirectRDMAWritesOptions</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga7f21ab1d42258d4f479a3bc4f420ac26">hipFlushGPUDirectRDMAWritesOptions</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga7f21ab1d42258d4f479a3bc4f420ac26a7ea9cfe68bb86afe0d797bb4ea9a7cd2" name="gga7f21ab1d42258d4f479a3bc4f420ac26a7ea9cfe68bb86afe0d797bb4ea9a7cd2"></a>hipFlushGPUDirectRDMAWritesOptionHost&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga7f21ab1d42258d4f479a3bc4f420ac26aa8e4e696581d4b8c3b2993ee5c4c472a" name="gga7f21ab1d42258d4f479a3bc4f420ac26aa8e4e696581d4b8c3b2993ee5c4c472a"></a>hipFlushGPUDirectRDMAWritesOptionMemOps&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga4a800faf1ce60529b4f052a30ef10b85" name="ga4a800faf1ce60529b4f052a30ef10b85"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga4a800faf1ce60529b4f052a30ef10b85">&#9670;&#160;</a></span>hipFuncAttribute</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga4a800faf1ce60529b4f052a30ef10b85">hipFuncAttribute</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<dl class="section warning"><dt>Warning</dt><dd>On AMD devices and some Nvidia devices, these hints and controls are ignored. </dd></dl>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga4a800faf1ce60529b4f052a30ef10b85a77db750682af411fb1aaef6b916e65ad" name="gga4a800faf1ce60529b4f052a30ef10b85a77db750682af411fb1aaef6b916e65ad"></a>hipFuncAttributeMaxDynamicSharedMemorySize&#160;</td><td class="fielddoc"><p>The maximum number of bytes requested for dynamically allocated shared memory. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4a800faf1ce60529b4f052a30ef10b85a492a0ab1879358bbb039545bd899d527" name="gga4a800faf1ce60529b4f052a30ef10b85a492a0ab1879358bbb039545bd899d527"></a>hipFuncAttributePreferredSharedMemoryCarveout&#160;</td><td class="fielddoc"><p>Sets the percentage of total shared memory allocated as the shared memory carveout. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4a800faf1ce60529b4f052a30ef10b85a78119858f4a6a22782ce980b8ce4fb95" name="gga4a800faf1ce60529b4f052a30ef10b85a78119858f4a6a22782ce980b8ce4fb95"></a>hipFuncAttributeMax&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga86e5c5692645963a9a673e1aa88ba6ca" name="ga86e5c5692645963a9a673e1aa88ba6ca"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga86e5c5692645963a9a673e1aa88ba6ca">&#9670;&#160;</a></span>hipFuncCache_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga86e5c5692645963a9a673e1aa88ba6ca">hipFuncCache_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<dl class="section warning"><dt>Warning</dt><dd>On AMD devices and some Nvidia devices, these hints and controls are ignored. </dd></dl>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga86e5c5692645963a9a673e1aa88ba6caa0813fbaa008ce1231ff9fed3911eb3af" name="gga86e5c5692645963a9a673e1aa88ba6caa0813fbaa008ce1231ff9fed3911eb3af"></a>hipFuncCachePreferNone&#160;</td><td class="fielddoc"><p>no preference for shared memory or L1 (default) </p>
</td></tr>
<tr><td class="fieldname"><a id="gga86e5c5692645963a9a673e1aa88ba6caa9b34337dfbadba25ed2aa270bbcabc43" name="gga86e5c5692645963a9a673e1aa88ba6caa9b34337dfbadba25ed2aa270bbcabc43"></a>hipFuncCachePreferShared&#160;</td><td class="fielddoc"><p>prefer larger shared memory and smaller L1 cache </p>
</td></tr>
<tr><td class="fieldname"><a id="gga86e5c5692645963a9a673e1aa88ba6caa636a3c140db6b9d4a8bf7d5a61c398c5" name="gga86e5c5692645963a9a673e1aa88ba6caa636a3c140db6b9d4a8bf7d5a61c398c5"></a>hipFuncCachePreferL1&#160;</td><td class="fielddoc"><p>prefer larger L1 cache and smaller shared memory </p>
</td></tr>
<tr><td class="fieldname"><a id="gga86e5c5692645963a9a673e1aa88ba6caa0ddab0e840107634a152033103be44d7" name="gga86e5c5692645963a9a673e1aa88ba6caa0ddab0e840107634a152033103be44d7"></a>hipFuncCachePreferEqual&#160;</td><td class="fielddoc"><p>prefer equal size L1 cache and shared memory </p>
</td></tr>
</table>

</div>
</div>
<a id="ga10719d9de09329f1a8947796b87f5844" name="ga10719d9de09329f1a8947796b87f5844"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga10719d9de09329f1a8947796b87f5844">&#9670;&#160;</a></span>hipGLDeviceList</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga10719d9de09329f1a8947796b87f5844">hipGLDeviceList</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP Devices used by current OpenGL Context. </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga10719d9de09329f1a8947796b87f5844a0b709df4695dc4daed5577437411ea75" name="gga10719d9de09329f1a8947796b87f5844a0b709df4695dc4daed5577437411ea75"></a>hipGLDeviceListAll&#160;</td><td class="fielddoc"><p>All hip devices used by current OpenGL context. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga10719d9de09329f1a8947796b87f5844a71f10703a8678c6fc465e734ab8428a5" name="gga10719d9de09329f1a8947796b87f5844a71f10703a8678c6fc465e734ab8428a5"></a>hipGLDeviceListCurrentFrame&#160;</td><td class="fielddoc"><p>Hip devices used by current OpenGL context in current frame </p>
</td></tr>
<tr><td class="fieldname"><a id="gga10719d9de09329f1a8947796b87f5844a00eef2e8d4116eabbd5d241ba782fed8" name="gga10719d9de09329f1a8947796b87f5844a00eef2e8d4116eabbd5d241ba782fed8"></a>hipGLDeviceListNextFrame&#160;</td><td class="fielddoc"><p>Hip devices used by current OpenGL context in next frame. </p>
</td></tr>
</table>

</div>
</div>
<a id="gaccd4ecfca4d2a5bfdad59e1f3953f665" name="gaccd4ecfca4d2a5bfdad59e1f3953f665"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaccd4ecfca4d2a5bfdad59e1f3953f665">&#9670;&#160;</a></span>hipGPUDirectRDMAWritesOrdering</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gaccd4ecfca4d2a5bfdad59e1f3953f665">hipGPUDirectRDMAWritesOrdering</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggaccd4ecfca4d2a5bfdad59e1f3953f665a4c8affda770fec6151516a0a599958a5" name="ggaccd4ecfca4d2a5bfdad59e1f3953f665a4c8affda770fec6151516a0a599958a5"></a>hipGPUDirectRDMAWritesOrderingNone&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="ggaccd4ecfca4d2a5bfdad59e1f3953f665a02317af92580a65cb1ed5f4958af9268" name="ggaccd4ecfca4d2a5bfdad59e1f3953f665a02317af92580a65cb1ed5f4958af9268"></a>hipGPUDirectRDMAWritesOrderingOwner&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="ggaccd4ecfca4d2a5bfdad59e1f3953f665a78519e9864647bcc6fdd4fbb0e4aeeb4" name="ggaccd4ecfca4d2a5bfdad59e1f3953f665a78519e9864647bcc6fdd4fbb0e4aeeb4"></a>hipGPUDirectRDMAWritesOrderingAllDevices&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga5f0b6b05428bbd208a4adba36bbf3036" name="ga5f0b6b05428bbd208a4adba36bbf3036"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga5f0b6b05428bbd208a4adba36bbf3036">&#9670;&#160;</a></span>hipGraphDebugDotFlags</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga5f0b6b05428bbd208a4adba36bbf3036">hipGraphDebugDotFlags</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga5f0b6b05428bbd208a4adba36bbf3036af0c573ee94c6758b5eabf5f4f13d408f" name="gga5f0b6b05428bbd208a4adba36bbf3036af0c573ee94c6758b5eabf5f4f13d408f"></a>hipGraphDebugDotFlagsVerbose&#160;</td><td class="fielddoc"><p>Output all debug data as if every debug flag is enabled </p>
</td></tr>
<tr><td class="fieldname"><a id="gga5f0b6b05428bbd208a4adba36bbf3036a5180492c462e92a98fabcb0454f69aef" name="gga5f0b6b05428bbd208a4adba36bbf3036a5180492c462e92a98fabcb0454f69aef"></a>hipGraphDebugDotFlagsKernelNodeParams&#160;</td><td class="fielddoc"><p>Adds <a class="el" href="structhip_kernel_node_params.html">hipKernelNodeParams</a> to output </p>
</td></tr>
<tr><td class="fieldname"><a id="gga5f0b6b05428bbd208a4adba36bbf3036af643dcafad92388a9532e94dd671ecf9" name="gga5f0b6b05428bbd208a4adba36bbf3036af643dcafad92388a9532e94dd671ecf9"></a>hipGraphDebugDotFlagsMemcpyNodeParams&#160;</td><td class="fielddoc"><p>Adds <a class="el" href="structhip_memcpy3_d_parms.html">hipMemcpy3DParms</a> to output </p>
</td></tr>
<tr><td class="fieldname"><a id="gga5f0b6b05428bbd208a4adba36bbf3036a162e1cc37582c814278a8a257f65255e" name="gga5f0b6b05428bbd208a4adba36bbf3036a162e1cc37582c814278a8a257f65255e"></a>hipGraphDebugDotFlagsMemsetNodeParams&#160;</td><td class="fielddoc"><p>Adds <a class="el" href="structhip_memset_params.html">hipMemsetParams</a> to output </p>
</td></tr>
<tr><td class="fieldname"><a id="gga5f0b6b05428bbd208a4adba36bbf3036ac3530926183d0cef94a74b6bd94ea07f" name="gga5f0b6b05428bbd208a4adba36bbf3036ac3530926183d0cef94a74b6bd94ea07f"></a>hipGraphDebugDotFlagsHostNodeParams&#160;</td><td class="fielddoc"><p>Adds <a class="el" href="structhip_host_node_params.html">hipHostNodeParams</a> to output </p>
</td></tr>
<tr><td class="fieldname"><a id="gga5f0b6b05428bbd208a4adba36bbf3036ad9104a8ce1454c6d536e363724e18dad" name="gga5f0b6b05428bbd208a4adba36bbf3036ad9104a8ce1454c6d536e363724e18dad"></a>hipGraphDebugDotFlagsEventNodeParams&#160;</td><td class="fielddoc"><p>Adds hipEvent_t handle from record and wait nodes to output </p>
</td></tr>
<tr><td class="fieldname"><a id="gga5f0b6b05428bbd208a4adba36bbf3036ab3497ea43f2e47877d8e96a0e97b7225" name="gga5f0b6b05428bbd208a4adba36bbf3036ab3497ea43f2e47877d8e96a0e97b7225"></a>hipGraphDebugDotFlagsExtSemasSignalNodeParams&#160;</td><td class="fielddoc"><p>Adds <a class="el" href="structhip_external_semaphore_signal_node_params.html">hipExternalSemaphoreSignalNodeParams</a> values to output </p>
</td></tr>
<tr><td class="fieldname"><a id="gga5f0b6b05428bbd208a4adba36bbf3036a7669e2948dd9b9ce1b18144b2dacce66" name="gga5f0b6b05428bbd208a4adba36bbf3036a7669e2948dd9b9ce1b18144b2dacce66"></a>hipGraphDebugDotFlagsExtSemasWaitNodeParams&#160;</td><td class="fielddoc"><p>Adds <a class="el" href="structhip_external_semaphore_wait_node_params.html">hipExternalSemaphoreWaitNodeParams</a> to output </p>
</td></tr>
<tr><td class="fieldname"><a id="gga5f0b6b05428bbd208a4adba36bbf3036a0acef45295f4817dce9f90e70aacfe9e" name="gga5f0b6b05428bbd208a4adba36bbf3036a0acef45295f4817dce9f90e70aacfe9e"></a>hipGraphDebugDotFlagsKernelNodeAttributes&#160;</td><td class="fielddoc"><p>Adds hipKernelNodeAttrID values to output </p>
</td></tr>
<tr><td class="fieldname"><a id="gga5f0b6b05428bbd208a4adba36bbf3036a9f0cd5093721d6ee605d48074f110c65" name="gga5f0b6b05428bbd208a4adba36bbf3036a9f0cd5093721d6ee605d48074f110c65"></a>hipGraphDebugDotFlagsHandles&#160;</td><td class="fielddoc"><p>Adds node handles and every kernel function handle to output </p>
</td></tr>
</table>

</div>
</div>
<a id="ga1dae8774d48cdf98a0bcf4b0d7a3aafb" name="ga1dae8774d48cdf98a0bcf4b0d7a3aafb"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga1dae8774d48cdf98a0bcf4b0d7a3aafb">&#9670;&#160;</a></span>hipGraphDependencyType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga1dae8774d48cdf98a0bcf4b0d7a3aafb">hipGraphDependencyType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga1dae8774d48cdf98a0bcf4b0d7a3aafba3c323771897c596a9340f72e451109c0" name="gga1dae8774d48cdf98a0bcf4b0d7a3aafba3c323771897c596a9340f72e451109c0"></a>hipGraphDependencyTypeDefault&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga1dae8774d48cdf98a0bcf4b0d7a3aafbaa85b51c1b1c8c38b3db3ea11b9e406ce" name="gga1dae8774d48cdf98a0bcf4b0d7a3aafbaa85b51c1b1c8c38b3db3ea11b9e406ce"></a>hipGraphDependencyTypeProgrammatic&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="gac79a2b2c0f83ae81c9325978c044892e" name="gac79a2b2c0f83ae81c9325978c044892e"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gac79a2b2c0f83ae81c9325978c044892e">&#9670;&#160;</a></span>hipGraphExecUpdateResult</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gac79a2b2c0f83ae81c9325978c044892e">hipGraphExecUpdateResult</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Graph execution update result </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggac79a2b2c0f83ae81c9325978c044892eac1f2b2a324b22bbca94f6c4f21039d8f" name="ggac79a2b2c0f83ae81c9325978c044892eac1f2b2a324b22bbca94f6c4f21039d8f"></a>hipGraphExecUpdateSuccess&#160;</td><td class="fielddoc"><p>The update succeeded. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac79a2b2c0f83ae81c9325978c044892ea67878e33ef3ec61463a920f149e082fe" name="ggac79a2b2c0f83ae81c9325978c044892ea67878e33ef3ec61463a920f149e082fe"></a>hipGraphExecUpdateError&#160;</td><td class="fielddoc"><p>The update failed for an unexpected reason which is described in the return value of the function </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac79a2b2c0f83ae81c9325978c044892ea25d787d82ab0b453c931b676272ba75b" name="ggac79a2b2c0f83ae81c9325978c044892ea25d787d82ab0b453c931b676272ba75b"></a>hipGraphExecUpdateErrorTopologyChanged&#160;</td><td class="fielddoc"><p>The update failed because the topology changed. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac79a2b2c0f83ae81c9325978c044892ea1f13abf8d4c8b14e7db99a224cc1620b" name="ggac79a2b2c0f83ae81c9325978c044892ea1f13abf8d4c8b14e7db99a224cc1620b"></a>hipGraphExecUpdateErrorNodeTypeChanged&#160;</td><td class="fielddoc"><p>The update failed because a node type changed. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac79a2b2c0f83ae81c9325978c044892eaa1c53ed0892dc10db16e4e229ff784e9" name="ggac79a2b2c0f83ae81c9325978c044892eaa1c53ed0892dc10db16e4e229ff784e9"></a>hipGraphExecUpdateErrorFunctionChanged&#160;</td><td class="fielddoc"><p>The update failed because the function of a kernel node changed. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac79a2b2c0f83ae81c9325978c044892eaddd407406093becb360f4f971e672d47" name="ggac79a2b2c0f83ae81c9325978c044892eaddd407406093becb360f4f971e672d47"></a>hipGraphExecUpdateErrorParametersChanged&#160;</td><td class="fielddoc"><p>The update failed because the parameters changed in a way that is not supported. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac79a2b2c0f83ae81c9325978c044892ea0445beac1f3c3235e7f4ed315e17fba0" name="ggac79a2b2c0f83ae81c9325978c044892ea0445beac1f3c3235e7f4ed315e17fba0"></a>hipGraphExecUpdateErrorNotSupported&#160;</td><td class="fielddoc"><p>The update failed because something about the node is not supported. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac79a2b2c0f83ae81c9325978c044892ea2cdf6a53a1434e4773cdc54a4d312a17" name="ggac79a2b2c0f83ae81c9325978c044892ea2cdf6a53a1434e4773cdc54a4d312a17"></a>hipGraphExecUpdateErrorUnsupportedFunctionChange&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="gabb8a4ae6dc64f7315c302c5b3b6e1c59" name="gabb8a4ae6dc64f7315c302c5b3b6e1c59"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gabb8a4ae6dc64f7315c302c5b3b6e1c59">&#9670;&#160;</a></span>hipGraphicsRegisterFlags</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gabb8a4ae6dc64f7315c302c5b3b6e1c59">hipGraphicsRegisterFlags</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP Access falgs for Interop resources. </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggabb8a4ae6dc64f7315c302c5b3b6e1c59aadea95241fb75cc9ce058b8a42007734" name="ggabb8a4ae6dc64f7315c302c5b3b6e1c59aadea95241fb75cc9ce058b8a42007734"></a>hipGraphicsRegisterFlagsNone&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="ggabb8a4ae6dc64f7315c302c5b3b6e1c59a16e70253402db71a1c1b073755494a03" name="ggabb8a4ae6dc64f7315c302c5b3b6e1c59a16e70253402db71a1c1b073755494a03"></a>hipGraphicsRegisterFlagsReadOnly&#160;</td><td class="fielddoc"><p>HIP will not write to this registered resource, read only. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggabb8a4ae6dc64f7315c302c5b3b6e1c59a5d3ee9600bd812fd1f1c26f66c77e881" name="ggabb8a4ae6dc64f7315c302c5b3b6e1c59a5d3ee9600bd812fd1f1c26f66c77e881"></a>hipGraphicsRegisterFlagsWriteDiscard&#160;</td><td class="fielddoc"><p>HIP will only write and will not read from this registered resource, write only. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggabb8a4ae6dc64f7315c302c5b3b6e1c59af1e660943886c56aef11ed34c8ee86f0" name="ggabb8a4ae6dc64f7315c302c5b3b6e1c59af1e660943886c56aef11ed34c8ee86f0"></a>hipGraphicsRegisterFlagsSurfaceLoadStore&#160;</td><td class="fielddoc"><p>HIP will bind this resource to a surface, read and write. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggabb8a4ae6dc64f7315c302c5b3b6e1c59a4f30ff3c46b068f0e5d138c3d9bfff11" name="ggabb8a4ae6dc64f7315c302c5b3b6e1c59a4f30ff3c46b068f0e5d138c3d9bfff11"></a>hipGraphicsRegisterFlagsTextureGather&#160;</td><td class="fielddoc"><p>HIP will perform texture gather operations on this registered resource, read and write or read only. </p>
</td></tr>
</table>

</div>
</div>
<a id="gaedc0107efcf1bd34d95e42cc04fa28f4" name="gaedc0107efcf1bd34d95e42cc04fa28f4"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaedc0107efcf1bd34d95e42cc04fa28f4">&#9670;&#160;</a></span>hipGraphInstantiateFlags</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gaedc0107efcf1bd34d95e42cc04fa28f4">hipGraphInstantiateFlags</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggaedc0107efcf1bd34d95e42cc04fa28f4a5db4094d6829b599d4c47c25cd4dfb87" name="ggaedc0107efcf1bd34d95e42cc04fa28f4a5db4094d6829b599d4c47c25cd4dfb87"></a>hipGraphInstantiateFlagAutoFreeOnLaunch&#160;</td><td class="fielddoc"><p>Automatically free memory allocated in a graph before relaunching. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaedc0107efcf1bd34d95e42cc04fa28f4a9df2be596a2520102068529ab4477c8a" name="ggaedc0107efcf1bd34d95e42cc04fa28f4a9df2be596a2520102068529ab4477c8a"></a>hipGraphInstantiateFlagUpload&#160;</td><td class="fielddoc"><p>Automatically upload the graph after instantiation. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaedc0107efcf1bd34d95e42cc04fa28f4ab1bf70c734aea099510b9157914a6515" name="ggaedc0107efcf1bd34d95e42cc04fa28f4ab1bf70c734aea099510b9157914a6515"></a>hipGraphInstantiateFlagDeviceLaunch&#160;</td><td class="fielddoc"><p>Instantiate the graph to be launched from the device. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaedc0107efcf1bd34d95e42cc04fa28f4a8f535452f119e17823fb674d9b9f693f" name="ggaedc0107efcf1bd34d95e42cc04fa28f4a8f535452f119e17823fb674d9b9f693f"></a>hipGraphInstantiateFlagUseNodePriority&#160;</td><td class="fielddoc"><p>Run the graph using the per-node priority attributes rather than the priority of the stream it is launched into. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga1275741e4687f414904caae01fecfd2f" name="ga1275741e4687f414904caae01fecfd2f"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga1275741e4687f414904caae01fecfd2f">&#9670;&#160;</a></span>hipGraphInstantiateResult</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga1275741e4687f414904caae01fecfd2f">hipGraphInstantiateResult</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>hipGraphInstantiateWithParams results </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga1275741e4687f414904caae01fecfd2fabcf7aafc228a6c17c7405160d0e32e70" name="gga1275741e4687f414904caae01fecfd2fabcf7aafc228a6c17c7405160d0e32e70"></a>hipGraphInstantiateSuccess&#160;</td><td class="fielddoc"><p>Instantiation Success </p>
</td></tr>
<tr><td class="fieldname"><a id="gga1275741e4687f414904caae01fecfd2fa93eaf8955b0c17e270bc2231c7dfeaa2" name="gga1275741e4687f414904caae01fecfd2fa93eaf8955b0c17e270bc2231c7dfeaa2"></a>hipGraphInstantiateError&#160;</td><td class="fielddoc"><p>Instantiation failed for an unexpected reason which is described in the return value of the function </p>
</td></tr>
<tr><td class="fieldname"><a id="gga1275741e4687f414904caae01fecfd2fa961222f2a70390abbf60f71ed878cf65" name="gga1275741e4687f414904caae01fecfd2fa961222f2a70390abbf60f71ed878cf65"></a>hipGraphInstantiateInvalidStructure&#160;</td><td class="fielddoc"><p>Instantiation failed due to invalid structure, such as cycles </p>
</td></tr>
<tr><td class="fieldname"><a id="gga1275741e4687f414904caae01fecfd2fa3c30667e32eb738974b1455d3f23b7c6" name="gga1275741e4687f414904caae01fecfd2fa3c30667e32eb738974b1455d3f23b7c6"></a>hipGraphInstantiateNodeOperationNotSupported&#160;</td><td class="fielddoc"><p>Instantiation for device launch failed because the graph contained an unsupported operation </p>
</td></tr>
<tr><td class="fieldname"><a id="gga1275741e4687f414904caae01fecfd2fa4ec62027dbfb29cbd365e9c94f5f325e" name="gga1275741e4687f414904caae01fecfd2fa4ec62027dbfb29cbd365e9c94f5f325e"></a>hipGraphInstantiateMultipleDevicesNotSupported&#160;</td><td class="fielddoc"><p>Instantiation for device launch failed due to the nodes belonging to different contexts </p>
</td></tr>
</table>

</div>
</div>
<a id="ga920ab2073b2ff77f37ae672d376ffe7e" name="ga920ab2073b2ff77f37ae672d376ffe7e"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga920ab2073b2ff77f37ae672d376ffe7e">&#9670;&#160;</a></span>hipGraphMemAttributeType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga920ab2073b2ff77f37ae672d376ffe7e">hipGraphMemAttributeType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga920ab2073b2ff77f37ae672d376ffe7ea4a7f157d4ca32bf67d3cb8760692e44b" name="gga920ab2073b2ff77f37ae672d376ffe7ea4a7f157d4ca32bf67d3cb8760692e44b"></a>hipGraphMemAttrUsedMemCurrent&#160;</td><td class="fielddoc"><p>Amount of memory, in bytes, currently associated with graphs. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga920ab2073b2ff77f37ae672d376ffe7ea9bed75ed79b9d7f7baa9432c162be774" name="gga920ab2073b2ff77f37ae672d376ffe7ea9bed75ed79b9d7f7baa9432c162be774"></a>hipGraphMemAttrUsedMemHigh&#160;</td><td class="fielddoc"><p>High watermark of memory, in bytes, associated with graphs since the last time. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga920ab2073b2ff77f37ae672d376ffe7ead23bfe68f6bda084c491303c36fdd278" name="gga920ab2073b2ff77f37ae672d376ffe7ead23bfe68f6bda084c491303c36fdd278"></a>hipGraphMemAttrReservedMemCurrent&#160;</td><td class="fielddoc"><p>Amount of memory, in bytes, currently allocated for graphs. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga920ab2073b2ff77f37ae672d376ffe7ea333e093c34ad2272c53f96efe3cb9717" name="gga920ab2073b2ff77f37ae672d376ffe7ea333e093c34ad2272c53f96efe3cb9717"></a>hipGraphMemAttrReservedMemHigh&#160;</td><td class="fielddoc"><p>High watermark of memory, in bytes, currently allocated for graphs </p>
</td></tr>
</table>

</div>
</div>
<a id="ga4727d20b89566832c74b762f987b9728" name="ga4727d20b89566832c74b762f987b9728"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga4727d20b89566832c74b762f987b9728">&#9670;&#160;</a></span>hipGraphNodeType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga4727d20b89566832c74b762f987b9728">hipGraphNodeType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>hipGraphNodeType </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728a9949391db00445f7a4a0b0465d093e36" name="gga4727d20b89566832c74b762f987b9728a9949391db00445f7a4a0b0465d093e36"></a>hipGraphNodeTypeKernel&#160;</td><td class="fielddoc"><p>GPU kernel node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728a635989252eae22c3002a001d63e1cb27" name="gga4727d20b89566832c74b762f987b9728a635989252eae22c3002a001d63e1cb27"></a>hipGraphNodeTypeMemcpy&#160;</td><td class="fielddoc"><p>Memcpy node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728a3cbfa0e34c1665922fab5abc77c213a1" name="gga4727d20b89566832c74b762f987b9728a3cbfa0e34c1665922fab5abc77c213a1"></a>hipGraphNodeTypeMemset&#160;</td><td class="fielddoc"><p>Memset node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728aada6f6582063a8a1db454d4950d05f1f" name="gga4727d20b89566832c74b762f987b9728aada6f6582063a8a1db454d4950d05f1f"></a>hipGraphNodeTypeHost&#160;</td><td class="fielddoc"><p>Host (executable) node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728a3c0d48ee17536fa328c7f688cea29341" name="gga4727d20b89566832c74b762f987b9728a3c0d48ee17536fa328c7f688cea29341"></a>hipGraphNodeTypeGraph&#160;</td><td class="fielddoc"><p>Node which executes an embedded graph. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728ad4f074d6484c61be503b22addd170f5d" name="gga4727d20b89566832c74b762f987b9728ad4f074d6484c61be503b22addd170f5d"></a>hipGraphNodeTypeEmpty&#160;</td><td class="fielddoc"><p>Empty (no-op) node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728a6ecc1f3e6df39acdb8fd75ee6c7596f4" name="gga4727d20b89566832c74b762f987b9728a6ecc1f3e6df39acdb8fd75ee6c7596f4"></a>hipGraphNodeTypeWaitEvent&#160;</td><td class="fielddoc"><p>External event wait node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728a40f8dc14f77efa8409c763d9014f2f79" name="gga4727d20b89566832c74b762f987b9728a40f8dc14f77efa8409c763d9014f2f79"></a>hipGraphNodeTypeEventRecord&#160;</td><td class="fielddoc"><p>External event record node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728a5cfa4c3858247a14c618e2c648ed1c3d" name="gga4727d20b89566832c74b762f987b9728a5cfa4c3858247a14c618e2c648ed1c3d"></a>hipGraphNodeTypeExtSemaphoreSignal&#160;</td><td class="fielddoc"><p>External Semaphore signal node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728adde9842fa2d0f9eccc94058f6d40c69f" name="gga4727d20b89566832c74b762f987b9728adde9842fa2d0f9eccc94058f6d40c69f"></a>hipGraphNodeTypeExtSemaphoreWait&#160;</td><td class="fielddoc"><p>External Semaphore wait node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728ab2f8761e77c317de516ee923db962229" name="gga4727d20b89566832c74b762f987b9728ab2f8761e77c317de516ee923db962229"></a>hipGraphNodeTypeMemAlloc&#160;</td><td class="fielddoc"><p>Memory alloc node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728ac8264d54af4199cd9194611932db6883" name="gga4727d20b89566832c74b762f987b9728ac8264d54af4199cd9194611932db6883"></a>hipGraphNodeTypeMemFree&#160;</td><td class="fielddoc"><p>Memory free node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728ad1dfcaa91d4817fae0940b911ea74460" name="gga4727d20b89566832c74b762f987b9728ad1dfcaa91d4817fae0940b911ea74460"></a>hipGraphNodeTypeMemcpyFromSymbol&#160;</td><td class="fielddoc"><p>MemcpyFromSymbol node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728ad1e85c6612c6e59fb9188c9ca87fb64f" name="gga4727d20b89566832c74b762f987b9728ad1e85c6612c6e59fb9188c9ca87fb64f"></a>hipGraphNodeTypeMemcpyToSymbol&#160;</td><td class="fielddoc"><p>MemcpyToSymbol node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728a0d03f67f5d3e19c0fc343818cc60f693" name="gga4727d20b89566832c74b762f987b9728a0d03f67f5d3e19c0fc343818cc60f693"></a>hipGraphNodeTypeBatchMemOp&#160;</td><td class="fielddoc"><p>BatchMemOp node. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4727d20b89566832c74b762f987b9728a8669923fef17da304f3f5189615b054f" name="gga4727d20b89566832c74b762f987b9728a8669923fef17da304f3f5189615b054f"></a>hipGraphNodeTypeCount&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga4026e9ccca8bb88888ad739e0f7586b4" name="ga4026e9ccca8bb88888ad739e0f7586b4"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga4026e9ccca8bb88888ad739e0f7586b4">&#9670;&#160;</a></span>hipLaunchAttributeID</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga4026e9ccca8bb88888ad739e0f7586b4">hipLaunchAttributeID</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Launch Attribute ID </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga4026e9ccca8bb88888ad739e0f7586b4ae9c06559f2a188eb87818348cefc4171" name="gga4026e9ccca8bb88888ad739e0f7586b4ae9c06559f2a188eb87818348cefc4171"></a>hipLaunchAttributeAccessPolicyWindow&#160;</td><td class="fielddoc"><p>Valid for Streams, graph nodes, launches. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4026e9ccca8bb88888ad739e0f7586b4af2e2bdbec3458fd4810e9d18b9e527af" name="gga4026e9ccca8bb88888ad739e0f7586b4af2e2bdbec3458fd4810e9d18b9e527af"></a>hipLaunchAttributeCooperative&#160;</td><td class="fielddoc"><p>Valid for graph nodes, launches. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4026e9ccca8bb88888ad739e0f7586b4aac7011b4266fc8e091a1048326da38b7" name="gga4026e9ccca8bb88888ad739e0f7586b4aac7011b4266fc8e091a1048326da38b7"></a>hipLaunchAttributeSynchronizationPolicy&#160;</td><td class="fielddoc"><p>Valid for streams. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4026e9ccca8bb88888ad739e0f7586b4a358f69dfec66d2cfe93b25f44845bcc1" name="gga4026e9ccca8bb88888ad739e0f7586b4a358f69dfec66d2cfe93b25f44845bcc1"></a>hipLaunchAttributePriority&#160;</td><td class="fielddoc"><p>Valid for graph node, streams, launches. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4026e9ccca8bb88888ad739e0f7586b4a9229ce145edcc4442002d8ee2d156cc3" name="gga4026e9ccca8bb88888ad739e0f7586b4a9229ce145edcc4442002d8ee2d156cc3"></a>hipLaunchAttributeMemSyncDomainMap&#160;</td><td class="fielddoc"><p>Valid for streams, graph nodes, launches. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4026e9ccca8bb88888ad739e0f7586b4a71ab9ea6aef993bbcaac9798a1445023" name="gga4026e9ccca8bb88888ad739e0f7586b4a71ab9ea6aef993bbcaac9798a1445023"></a>hipLaunchAttributeMemSyncDomain&#160;</td><td class="fielddoc"><p>Valid for streams, graph nodes, launches. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga4026e9ccca8bb88888ad739e0f7586b4a3942a0c67db2d9b4ddd1f6fbc04d59ea" name="gga4026e9ccca8bb88888ad739e0f7586b4a3942a0c67db2d9b4ddd1f6fbc04d59ea"></a>hipLaunchAttributeMax&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga503fd3aecee14969a1e48a41bc8b16c1" name="ga503fd3aecee14969a1e48a41bc8b16c1"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga503fd3aecee14969a1e48a41bc8b16c1">&#9670;&#160;</a></span>hipLaunchMemSyncDomain</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga503fd3aecee14969a1e48a41bc8b16c1">hipLaunchMemSyncDomain</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory Synchronization Domain </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga503fd3aecee14969a1e48a41bc8b16c1a6d069ee68549d463bc7b873b1f3631d5" name="gga503fd3aecee14969a1e48a41bc8b16c1a6d069ee68549d463bc7b873b1f3631d5"></a>hipLaunchMemSyncDomainDefault&#160;</td><td class="fielddoc"><p>Launch kernels in the default domain </p>
</td></tr>
<tr><td class="fieldname"><a id="gga503fd3aecee14969a1e48a41bc8b16c1a20b07e28748e19c3aacdeadd53860a02" name="gga503fd3aecee14969a1e48a41bc8b16c1a20b07e28748e19c3aacdeadd53860a02"></a>hipLaunchMemSyncDomainRemote&#160;</td><td class="fielddoc"><p>Launch kernels in the remote domain </p>
</td></tr>
</table>

</div>
</div>
<a id="ga02ceb1513c852c4dd1ecf3cc459fda70" name="ga02ceb1513c852c4dd1ecf3cc459fda70"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga02ceb1513c852c4dd1ecf3cc459fda70">&#9670;&#160;</a></span>hipLimit_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga02ceb1513c852c4dd1ecf3cc459fda70">hipLimit_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>hipLimit</p>
<dl class="section note"><dt>Note</dt><dd>In HIP device limit-related APIs, any input limit value other than those defined in the enum is treated as "UnsupportedLimit" by default. </dd></dl>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga02ceb1513c852c4dd1ecf3cc459fda70a30214f21a523ab016abc833abde96486" name="gga02ceb1513c852c4dd1ecf3cc459fda70a30214f21a523ab016abc833abde96486"></a>hipLimitStackSize&#160;</td><td class="fielddoc"><p>Limit of stack size in bytes on the current device, per thread. The size is in units of 256 dwords, up to the limit of (128K - 16) </p>
</td></tr>
<tr><td class="fieldname"><a id="gga02ceb1513c852c4dd1ecf3cc459fda70a76d41da5f9a43671718a72237e783273" name="gga02ceb1513c852c4dd1ecf3cc459fda70a76d41da5f9a43671718a72237e783273"></a>hipLimitPrintfFifoSize&#160;</td><td class="fielddoc"><p>Size limit in bytes of fifo used by printf call on the device. Currently not supported </p>
</td></tr>
<tr><td class="fieldname"><a id="gga02ceb1513c852c4dd1ecf3cc459fda70a1ec17519ca7e1fa12dde48d3a919d210" name="gga02ceb1513c852c4dd1ecf3cc459fda70a1ec17519ca7e1fa12dde48d3a919d210"></a>hipLimitMallocHeapSize&#160;</td><td class="fielddoc"><p>Limit of heap size in bytes on the current device, should be less than the global memory size on the device </p>
</td></tr>
<tr><td class="fieldname"><a id="gga02ceb1513c852c4dd1ecf3cc459fda70a03fe8a1c0d40535160ee2fca6c38a7de" name="gga02ceb1513c852c4dd1ecf3cc459fda70a03fe8a1c0d40535160ee2fca6c38a7de"></a>hipExtLimitScratchMin&#160;</td><td class="fielddoc"><p>Minimum allowed value in bytes for scratch limit on this device. Valid only on Rocm device. This is read only. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga02ceb1513c852c4dd1ecf3cc459fda70a95da197cb0b890663d14c041c0f2f98d" name="gga02ceb1513c852c4dd1ecf3cc459fda70a95da197cb0b890663d14c041c0f2f98d"></a>hipExtLimitScratchMax&#160;</td><td class="fielddoc"><p>Maximum allowed value in bytes for scratch limit on this device. Valid only on Rocm device. This is read only. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga02ceb1513c852c4dd1ecf3cc459fda70ac39843ab7052effa3c1be92dd4a6af6b" name="gga02ceb1513c852c4dd1ecf3cc459fda70ac39843ab7052effa3c1be92dd4a6af6b"></a>hipExtLimitScratchCurrent&#160;</td><td class="fielddoc"><p>Current scratch limit threshold in bytes on this device. Must be between hipExtLimitScratchMin and hipExtLimitScratchMaxValid values. Valid only on Rocm device. This can be modified. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga02ceb1513c852c4dd1ecf3cc459fda70a62987c6383927c7dbbbb02a770b71eb5" name="gga02ceb1513c852c4dd1ecf3cc459fda70a62987c6383927c7dbbbb02a770b71eb5"></a>hipLimitRange&#160;</td><td class="fielddoc"><p>Supported limit range. </p>
</td></tr>
</table>

</div>
</div>
<a id="gac20e3511da42142b23285e557e43facd" name="gac20e3511da42142b23285e557e43facd"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gac20e3511da42142b23285e557e43facd">&#9670;&#160;</a></span>hipMemAccessFlags</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gac20e3511da42142b23285e557e43facd">hipMemAccessFlags</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Specifies the memory protection flags for mapping </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggac20e3511da42142b23285e557e43facda3fed6a3f2f6435894c1a9b0cc707bbaa" name="ggac20e3511da42142b23285e557e43facda3fed6a3f2f6435894c1a9b0cc707bbaa"></a>hipMemAccessFlagsProtNone&#160;</td><td class="fielddoc"><p>Default, make the address range not accessible. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac20e3511da42142b23285e557e43facda1246e2630cabcfdf92292952395b3bca" name="ggac20e3511da42142b23285e557e43facda1246e2630cabcfdf92292952395b3bca"></a>hipMemAccessFlagsProtRead&#160;</td><td class="fielddoc"><p>Set the address range read accessible. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac20e3511da42142b23285e557e43facda6c92304d286d8c38614e2b6b76b36734" name="ggac20e3511da42142b23285e557e43facda6c92304d286d8c38614e2b6b76b36734"></a>hipMemAccessFlagsProtReadWrite&#160;</td><td class="fielddoc"><p>Set the address range read-write accessible. </p>
</td></tr>
</table>

</div>
</div>
<a id="gac339d242785822f679962c10b45037c8" name="gac339d242785822f679962c10b45037c8"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gac339d242785822f679962c10b45037c8">&#9670;&#160;</a></span>hipMemAllocationGranularity_flags</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gac339d242785822f679962c10b45037c8">hipMemAllocationGranularity_flags</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Flags for granularity </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggac339d242785822f679962c10b45037c8abdb60c08374a9bdf35b86ae3d6650597" name="ggac339d242785822f679962c10b45037c8abdb60c08374a9bdf35b86ae3d6650597"></a>hipMemAllocationGranularityMinimum&#160;</td><td class="fielddoc"><p>Minimum granularity. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac339d242785822f679962c10b45037c8ae21e3d97d84b2c61d2aee2b2a9293c34" name="ggac339d242785822f679962c10b45037c8ae21e3d97d84b2c61d2aee2b2a9293c34"></a>hipMemAllocationGranularityRecommended&#160;</td><td class="fielddoc"><p>Recommended granularity for performance. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga07b4aea600602a99d135dd2ca87faa92" name="ga07b4aea600602a99d135dd2ca87faa92"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga07b4aea600602a99d135dd2ca87faa92">&#9670;&#160;</a></span>hipMemAllocationHandleType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga07b4aea600602a99d135dd2ca87faa92">hipMemAllocationHandleType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Flags for specifying handle types for memory pool allocations </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga07b4aea600602a99d135dd2ca87faa92a72c5024a4f58cb4de197d6314e4c66a9" name="gga07b4aea600602a99d135dd2ca87faa92a72c5024a4f58cb4de197d6314e4c66a9"></a>hipMemHandleTypeNone&#160;</td><td class="fielddoc"><p>Does not allow any export mechanism. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga07b4aea600602a99d135dd2ca87faa92a9f261aad3214093c5b1aa2838b157d66" name="gga07b4aea600602a99d135dd2ca87faa92a9f261aad3214093c5b1aa2838b157d66"></a>hipMemHandleTypePosixFileDescriptor&#160;</td><td class="fielddoc"><p>Allows a file descriptor for exporting. Permitted only on POSIX systems. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga07b4aea600602a99d135dd2ca87faa92a3b7ddb718292009167abee4779fe03c8" name="gga07b4aea600602a99d135dd2ca87faa92a3b7ddb718292009167abee4779fe03c8"></a>hipMemHandleTypeWin32&#160;</td><td class="fielddoc"><p>Allows a Win32 NT handle for exporting. (HANDLE) </p>
</td></tr>
<tr><td class="fieldname"><a id="gga07b4aea600602a99d135dd2ca87faa92a54d89168742fee74bb05e02d3b699f46" name="gga07b4aea600602a99d135dd2ca87faa92a54d89168742fee74bb05e02d3b699f46"></a>hipMemHandleTypeWin32Kmt&#160;</td><td class="fielddoc"><p>Allows a Win32 KMT handle for exporting. (D3DKMT_HANDLE) </p>
</td></tr>
</table>

</div>
</div>
<a id="gadefdae0569c5be4538c065396ed758f5" name="gadefdae0569c5be4538c065396ed758f5"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gadefdae0569c5be4538c065396ed758f5">&#9670;&#160;</a></span>hipMemAllocationType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gadefdae0569c5be4538c065396ed758f5">hipMemAllocationType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Defines the allocation types </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggadefdae0569c5be4538c065396ed758f5ab500eee492813b9c90ade2a8c852a3ae" name="ggadefdae0569c5be4538c065396ed758f5ab500eee492813b9c90ade2a8c852a3ae"></a>hipMemAllocationTypeInvalid&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="ggadefdae0569c5be4538c065396ed758f5a8b9b2a4595b9ff034a6a5d053c95c227" name="ggadefdae0569c5be4538c065396ed758f5a8b9b2a4595b9ff034a6a5d053c95c227"></a>hipMemAllocationTypePinned&#160;</td><td class="fielddoc"><p>This allocation type is 'pinned', i.e. cannot migrate from its current location while the application is actively using it </p>
</td></tr>
<tr><td class="fieldname"><a id="ggadefdae0569c5be4538c065396ed758f5aab0b9e7ca7208f5d82e549346305410a" name="ggadefdae0569c5be4538c065396ed758f5aab0b9e7ca7208f5d82e549346305410a"></a>hipMemAllocationTypeUncached&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="ggadefdae0569c5be4538c065396ed758f5a7827526b3897c596109b6024bf38502a" name="ggadefdae0569c5be4538c065396ed758f5a7827526b3897c596109b6024bf38502a"></a>hipMemAllocationTypeMax&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga7a1387fab190ef8404d955871eeaa7fa" name="ga7a1387fab190ef8404d955871eeaa7fa"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga7a1387fab190ef8404d955871eeaa7fa">&#9670;&#160;</a></span>hipMemHandleType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga7a1387fab190ef8404d955871eeaa7fa">hipMemHandleType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory handle type </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga7a1387fab190ef8404d955871eeaa7faad503b171c92fc9e224ed41f49ab5fef7" name="gga7a1387fab190ef8404d955871eeaa7faad503b171c92fc9e224ed41f49ab5fef7"></a>hipMemHandleTypeGeneric&#160;</td><td class="fielddoc"><p>Generic handle type. </p>
</td></tr>
</table>

</div>
</div>
<a id="gab6a581b72da85bebd9a6e02a27e22d49" name="gab6a581b72da85bebd9a6e02a27e22d49"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gab6a581b72da85bebd9a6e02a27e22d49">&#9670;&#160;</a></span>hipMemOperationType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gab6a581b72da85bebd9a6e02a27e22d49">hipMemOperationType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory operation types </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggab6a581b72da85bebd9a6e02a27e22d49a003c437dbe8ae98e1cb7ad0837b1d489" name="ggab6a581b72da85bebd9a6e02a27e22d49a003c437dbe8ae98e1cb7ad0837b1d489"></a>hipMemOperationTypeMap&#160;</td><td class="fielddoc"><p>Map operation. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggab6a581b72da85bebd9a6e02a27e22d49a341e660cc0facbb2576d70817eed0fc5" name="ggab6a581b72da85bebd9a6e02a27e22d49a341e660cc0facbb2576d70817eed0fc5"></a>hipMemOperationTypeUnmap&#160;</td><td class="fielddoc"><p>Unmap operation. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga2757323c1ac94b1d71f699fcbd5bdc2f" name="ga2757323c1ac94b1d71f699fcbd5bdc2f"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga2757323c1ac94b1d71f699fcbd5bdc2f">&#9670;&#160;</a></span>hipMemoryAdvise</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga2757323c1ac94b1d71f699fcbd5bdc2f">hipMemoryAdvise</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP Memory Advise values</p>
<dl class="section note"><dt>Note</dt><dd>This memory advise enumeration is used on Linux, not Windows. </dd></dl>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga2757323c1ac94b1d71f699fcbd5bdc2fafaeec0b64516ce7134b9ae80c2b7a3f5" name="gga2757323c1ac94b1d71f699fcbd5bdc2fafaeec0b64516ce7134b9ae80c2b7a3f5"></a>hipMemAdviseSetReadMostly&#160;</td><td class="fielddoc"><p>Data will mostly be read and only occassionally be written to </p>
</td></tr>
<tr><td class="fieldname"><a id="gga2757323c1ac94b1d71f699fcbd5bdc2fafd2ae0ca621c454f44551ec654a29cf6" name="gga2757323c1ac94b1d71f699fcbd5bdc2fafd2ae0ca621c454f44551ec654a29cf6"></a>hipMemAdviseUnsetReadMostly&#160;</td><td class="fielddoc"><p>Undo the effect of hipMemAdviseSetReadMostly. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga2757323c1ac94b1d71f699fcbd5bdc2facd018663520b26a64c6201a3efae1f15" name="gga2757323c1ac94b1d71f699fcbd5bdc2facd018663520b26a64c6201a3efae1f15"></a>hipMemAdviseSetPreferredLocation&#160;</td><td class="fielddoc"><p>Set the preferred location for the data as the specified device </p>
</td></tr>
<tr><td class="fieldname"><a id="gga2757323c1ac94b1d71f699fcbd5bdc2fa6801ff205e3837d679aced24eb71e370" name="gga2757323c1ac94b1d71f699fcbd5bdc2fa6801ff205e3837d679aced24eb71e370"></a>hipMemAdviseUnsetPreferredLocation&#160;</td><td class="fielddoc"><p>Clear the preferred location for the data. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga2757323c1ac94b1d71f699fcbd5bdc2fab516731448e70a8a48ada9314a869549" name="gga2757323c1ac94b1d71f699fcbd5bdc2fab516731448e70a8a48ada9314a869549"></a>hipMemAdviseSetAccessedBy&#160;</td><td class="fielddoc"><p>Data will be accessed by the specified device so prevent page faults as much as possible </p>
</td></tr>
<tr><td class="fieldname"><a id="gga2757323c1ac94b1d71f699fcbd5bdc2fa025ece7c72ff19784e1fe9fdb07e7e56" name="gga2757323c1ac94b1d71f699fcbd5bdc2fa025ece7c72ff19784e1fe9fdb07e7e56"></a>hipMemAdviseUnsetAccessedBy&#160;</td><td class="fielddoc"><p>Let HIP to decide on the page faulting policy for the specified device </p>
</td></tr>
<tr><td class="fieldname"><a id="gga2757323c1ac94b1d71f699fcbd5bdc2fa56145fb5a178f26cc758cbbaa17b8d86" name="gga2757323c1ac94b1d71f699fcbd5bdc2fa56145fb5a178f26cc758cbbaa17b8d86"></a>hipMemAdviseSetCoarseGrain&#160;</td><td class="fielddoc"><p>The default memory model is fine-grain. That allows coherent operations between host and device, while executing kernels. The coarse-grain can be used for data that only needs to be coherent at dispatch boundaries for better performance </p>
</td></tr>
<tr><td class="fieldname"><a id="gga2757323c1ac94b1d71f699fcbd5bdc2fa24256a97d088ab9a13e2ae2af21751c6" name="gga2757323c1ac94b1d71f699fcbd5bdc2fa24256a97d088ab9a13e2ae2af21751c6"></a>hipMemAdviseUnsetCoarseGrain&#160;</td><td class="fielddoc"><p>Restores cache coherency policy back to fine-grain. </p>
</td></tr>
</table>

</div>
</div>
<a id="gaea86e91d3cd65992d787b39b218435a3" name="gaea86e91d3cd65992d787b39b218435a3"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaea86e91d3cd65992d787b39b218435a3">&#9670;&#160;</a></span>hipMemoryType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gaea86e91d3cd65992d787b39b218435a3">hipMemoryType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>hipMemoryType (for pointer attributes)</p>
<dl class="section note"><dt>Note</dt><dd>hipMemoryType enum values are combination of cudaMemoryType and cuMemoryType and AMD specific enum values. </dd></dl>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggaea86e91d3cd65992d787b39b218435a3ab07106e9139657fd73adbbe5f0109bc1" name="ggaea86e91d3cd65992d787b39b218435a3ab07106e9139657fd73adbbe5f0109bc1"></a>hipMemoryTypeUnregistered&#160;</td><td class="fielddoc"><p>Unregistered memory. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaea86e91d3cd65992d787b39b218435a3a5c5c99ed85b2599362089aa089cdad77" name="ggaea86e91d3cd65992d787b39b218435a3a5c5c99ed85b2599362089aa089cdad77"></a>hipMemoryTypeHost&#160;</td><td class="fielddoc"><p>Memory is physically located on host. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaea86e91d3cd65992d787b39b218435a3a0e5f84f5565ba2a011ef3a9df2584a7a" name="ggaea86e91d3cd65992d787b39b218435a3a0e5f84f5565ba2a011ef3a9df2584a7a"></a>hipMemoryTypeDevice&#160;</td><td class="fielddoc"><p>Memory is physically located on device. (see deviceId for specific device) </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaea86e91d3cd65992d787b39b218435a3ac567ef3faeb55edfc965fd8f1dbccf4c" name="ggaea86e91d3cd65992d787b39b218435a3ac567ef3faeb55edfc965fd8f1dbccf4c"></a>hipMemoryTypeManaged&#160;</td><td class="fielddoc"><p>Managed memory, automaticallly managed by the unified memory system place holder for new values. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaea86e91d3cd65992d787b39b218435a3abbd7b93a87068c9dbb8d841ff0f3a366" name="ggaea86e91d3cd65992d787b39b218435a3abbd7b93a87068c9dbb8d841ff0f3a366"></a>hipMemoryTypeArray&#160;</td><td class="fielddoc"><p>Array memory, physically located on device. (see deviceId for specific device) </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaea86e91d3cd65992d787b39b218435a3aceb68d38418e0a54dd9f7c8e113a4ec4" name="ggaea86e91d3cd65992d787b39b218435a3aceb68d38418e0a54dd9f7c8e113a4ec4"></a>hipMemoryTypeUnified&#160;</td><td class="fielddoc"><p>unified address space </p>
</td></tr>
</table>

</div>
</div>
<a id="ga987c8e7a7e8171832a6647150854ca2e" name="ga987c8e7a7e8171832a6647150854ca2e"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga987c8e7a7e8171832a6647150854ca2e">&#9670;&#160;</a></span>hipMemPoolAttr</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga987c8e7a7e8171832a6647150854ca2e">hipMemPoolAttr</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP memory pool attributes </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga987c8e7a7e8171832a6647150854ca2eac0b660a866fc6c3ee87a8230d384532f" name="gga987c8e7a7e8171832a6647150854ca2eac0b660a866fc6c3ee87a8230d384532f"></a>hipMemPoolReuseFollowEventDependencies&#160;</td><td class="fielddoc"><p>(value type = int) Allow <code>hipMemAllocAsync</code> to use memory asynchronously freed in another streams as long as a stream ordering dependency of the allocating stream on the free action exists. hip events and null stream interactions can create the required stream ordered dependencies. (default enabled) </p>
</td></tr>
<tr><td class="fieldname"><a id="gga987c8e7a7e8171832a6647150854ca2ead1da20661bcf84605088d3e20120b653" name="gga987c8e7a7e8171832a6647150854ca2ead1da20661bcf84605088d3e20120b653"></a>hipMemPoolReuseAllowOpportunistic&#160;</td><td class="fielddoc"><p>(value type = int) Allow reuse of already completed frees when there is no dependency between the free and allocation. (default enabled) </p>
</td></tr>
<tr><td class="fieldname"><a id="gga987c8e7a7e8171832a6647150854ca2eaa1fa58a079f0a1b31aef2baf543a8dd7" name="gga987c8e7a7e8171832a6647150854ca2eaa1fa58a079f0a1b31aef2baf543a8dd7"></a>hipMemPoolReuseAllowInternalDependencies&#160;</td><td class="fielddoc"><p>(value type = int) Allow <code>hipMemAllocAsync</code> to insert new stream dependencies in order to establish the stream ordering required to reuse a piece of memory released by cuFreeAsync (default enabled). </p>
</td></tr>
<tr><td class="fieldname"><a id="gga987c8e7a7e8171832a6647150854ca2ea601b937cbdd057d30d4e136360e11220" name="gga987c8e7a7e8171832a6647150854ca2ea601b937cbdd057d30d4e136360e11220"></a>hipMemPoolAttrReleaseThreshold&#160;</td><td class="fielddoc"><p>(value type = uint64_t) Amount of reserved memory in bytes to hold onto before trying to release memory back to the OS. When more than the release threshold bytes of memory are held by the memory pool, the allocator will try to release memory back to the OS on the next call to stream, event or context synchronize. (default 0) </p>
</td></tr>
<tr><td class="fieldname"><a id="gga987c8e7a7e8171832a6647150854ca2ea4e4e69ffb29a939c6970467312bad712" name="gga987c8e7a7e8171832a6647150854ca2ea4e4e69ffb29a939c6970467312bad712"></a>hipMemPoolAttrReservedMemCurrent&#160;</td><td class="fielddoc"><p>(value type = uint64_t) Amount of backing memory currently allocated for the mempool. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga987c8e7a7e8171832a6647150854ca2ea30c968e449328135ef9610f12e740582" name="gga987c8e7a7e8171832a6647150854ca2ea30c968e449328135ef9610f12e740582"></a>hipMemPoolAttrReservedMemHigh&#160;</td><td class="fielddoc"><p>(value type = uint64_t) High watermark of backing memory allocated for the mempool since the last time it was reset. High watermark can only be reset to zero. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga987c8e7a7e8171832a6647150854ca2ea0574c734ba2b79ba156a8e94739f07e5" name="gga987c8e7a7e8171832a6647150854ca2ea0574c734ba2b79ba156a8e94739f07e5"></a>hipMemPoolAttrUsedMemCurrent&#160;</td><td class="fielddoc"><p>(value type = uint64_t) Amount of memory from the pool that is currently in use by the application. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga987c8e7a7e8171832a6647150854ca2ea7d0d0e5e6ce19fdaaef2674a305930d0" name="gga987c8e7a7e8171832a6647150854ca2ea7d0d0e5e6ce19fdaaef2674a305930d0"></a>hipMemPoolAttrUsedMemHigh&#160;</td><td class="fielddoc"><p>(value type = uint64_t) High watermark of the amount of memory from the pool that was in use by the application since the last time it was reset. High watermark can only be reset to zero. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga1e8d4a7cf5d1844fa34e4f9ac3bfcc63" name="ga1e8d4a7cf5d1844fa34e4f9ac3bfcc63"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga1e8d4a7cf5d1844fa34e4f9ac3bfcc63">&#9670;&#160;</a></span>hipMemRangeAttribute</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga1e8d4a7cf5d1844fa34e4f9ac3bfcc63">hipMemRangeAttribute</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP range attributes </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63a94a4c175d01932cf90eff033a302528c" name="gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63a94a4c175d01932cf90eff033a302528c"></a>hipMemRangeAttributeReadMostly&#160;</td><td class="fielddoc"><p>Whether the range will mostly be read and only occassionally be written to </p>
</td></tr>
<tr><td class="fieldname"><a id="gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63a135eda185c450dd8add5580c23bf37b8" name="gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63a135eda185c450dd8add5580c23bf37b8"></a>hipMemRangeAttributePreferredLocation&#160;</td><td class="fielddoc"><p>The preferred location of the range. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63a666534e4e8298c8d694dc745d9afe6ae" name="gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63a666534e4e8298c8d694dc745d9afe6ae"></a>hipMemRangeAttributeAccessedBy&#160;</td><td class="fielddoc"><p>Memory range has hipMemAdviseSetAccessedBy set for the specified device </p>
</td></tr>
<tr><td class="fieldname"><a id="gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63a12c0540067c44b9f126da23edc523484" name="gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63a12c0540067c44b9f126da23edc523484"></a>hipMemRangeAttributeLastPrefetchLocation&#160;</td><td class="fielddoc"><p>The last location to where the range was prefetched </p>
</td></tr>
<tr><td class="fieldname"><a id="gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63ad00a2b439bae60733943da9b27de4f08" name="gga1e8d4a7cf5d1844fa34e4f9ac3bfcc63ad00a2b439bae60733943da9b27de4f08"></a>hipMemRangeAttributeCoherencyMode&#160;</td><td class="fielddoc"><p>Returns coherency mode <a class="el" href="group___global_defs.html#gac1e4b99211365977c2a7a9d054b59765">hipMemRangeCoherencyMode</a> for the range </p>
</td></tr>
</table>

</div>
</div>
<a id="gac1e4b99211365977c2a7a9d054b59765" name="gac1e4b99211365977c2a7a9d054b59765"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gac1e4b99211365977c2a7a9d054b59765">&#9670;&#160;</a></span>hipMemRangeCoherencyMode</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gac1e4b99211365977c2a7a9d054b59765">hipMemRangeCoherencyMode</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP Coherency Mode </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggac1e4b99211365977c2a7a9d054b59765a300a479362ae193c4c51bc64fa411304" name="ggac1e4b99211365977c2a7a9d054b59765a300a479362ae193c4c51bc64fa411304"></a>hipMemRangeCoherencyModeFineGrain&#160;</td><td class="fielddoc"><p>Updates to memory with this attribute can be done coherently from all devices </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac1e4b99211365977c2a7a9d054b59765af508599624e76d1a13bb23a9e6359834" name="ggac1e4b99211365977c2a7a9d054b59765af508599624e76d1a13bb23a9e6359834"></a>hipMemRangeCoherencyModeCoarseGrain&#160;</td><td class="fielddoc"><p>Writes to memory with this attribute can be performed by a single device at a time </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac1e4b99211365977c2a7a9d054b59765ad7e3bd29e10dbbfca7b550c97a034687" name="ggac1e4b99211365977c2a7a9d054b59765ad7e3bd29e10dbbfca7b550c97a034687"></a>hipMemRangeCoherencyModeIndeterminate&#160;</td><td class="fielddoc"><p>Memory region queried contains subregions with both hipMemRangeCoherencyModeFineGrain and hipMemRangeCoherencyModeCoarseGrain attributes </p>
</td></tr>
</table>

</div>
</div>
<a id="ga9e9efb47c0fd633ee7a25cbc18d16cf3" name="ga9e9efb47c0fd633ee7a25cbc18d16cf3"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga9e9efb47c0fd633ee7a25cbc18d16cf3">&#9670;&#160;</a></span>hipMemRangeFlags</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga9e9efb47c0fd633ee7a25cbc18d16cf3">hipMemRangeFlags</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Mem Range Flags used in hipMemGetHandleForAddressRange. </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga9e9efb47c0fd633ee7a25cbc18d16cf3aca415bce635dee749a0cf90afee5492c" name="gga9e9efb47c0fd633ee7a25cbc18d16cf3aca415bce635dee749a0cf90afee5492c"></a>hipMemRangeFlagDmaBufMappingTypePcie&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga9e9efb47c0fd633ee7a25cbc18d16cf3a16f93156ec0e7c102d809ec69f1a39bc" name="gga9e9efb47c0fd633ee7a25cbc18d16cf3a16f93156ec0e7c102d809ec69f1a39bc"></a>hipMemRangeFlagsMax&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="ga04d1e286b2c0a6bd0fcb0c8a0840782e" name="ga04d1e286b2c0a6bd0fcb0c8a0840782e"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga04d1e286b2c0a6bd0fcb0c8a0840782e">&#9670;&#160;</a></span>hipMemRangeHandleType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga04d1e286b2c0a6bd0fcb0c8a0840782e">hipMemRangeHandleType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Requested handle type for address range. </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga04d1e286b2c0a6bd0fcb0c8a0840782eac1dfb4123f249838b37110a6ff1e2f8d" name="gga04d1e286b2c0a6bd0fcb0c8a0840782eac1dfb4123f249838b37110a6ff1e2f8d"></a>hipMemRangeHandleTypeDmaBufFd&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga04d1e286b2c0a6bd0fcb0c8a0840782eaba654afb15049bffda6169071a3d9ab6" name="gga04d1e286b2c0a6bd0fcb0c8a0840782eaba654afb15049bffda6169071a3d9ab6"></a>hipMemRangeHandleTypeMax&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="gaaab4f1f28ef296fc6218b1ca8d21a6e9" name="gaaab4f1f28ef296fc6218b1ca8d21a6e9"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaaab4f1f28ef296fc6218b1ca8d21a6e9">&#9670;&#160;</a></span>hiprtcResult</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gaaab4f1f28ef296fc6218b1ca8d21a6e9">hiprtcResult</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>hiprtc error code </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9ab81164860f4404a742c0972867e178e2" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9ab81164860f4404a742c0972867e178e2"></a>HIPRTC_SUCCESS&#160;</td><td class="fielddoc"><p>Success. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9ad9863c0cdec84a87cb37fbe071ff8f0a" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9ad9863c0cdec84a87cb37fbe071ff8f0a"></a>HIPRTC_ERROR_OUT_OF_MEMORY&#160;</td><td class="fielddoc"><p>Out of memory. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9a0d31deb90b120cbf8a94c30e6be27718" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9a0d31deb90b120cbf8a94c30e6be27718"></a>HIPRTC_ERROR_PROGRAM_CREATION_FAILURE&#160;</td><td class="fielddoc"><p>Failed to create program. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9a8af2964e85221c54309e50ea4a0dd79e" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9a8af2964e85221c54309e50ea4a0dd79e"></a>HIPRTC_ERROR_INVALID_INPUT&#160;</td><td class="fielddoc"><p>Invalid input. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9a37d841d4dd1bae0e5e2cd1df2c24e795" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9a37d841d4dd1bae0e5e2cd1df2c24e795"></a>HIPRTC_ERROR_INVALID_PROGRAM&#160;</td><td class="fielddoc"><p>Invalid program. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9a83af982bfeefbef92066ecf652131256" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9a83af982bfeefbef92066ecf652131256"></a>HIPRTC_ERROR_INVALID_OPTION&#160;</td><td class="fielddoc"><p>Invalid option. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9ad2b17befbe962616ab95250d40c8e62b" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9ad2b17befbe962616ab95250d40c8e62b"></a>HIPRTC_ERROR_COMPILATION&#160;</td><td class="fielddoc"><p>Compilation error. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9abe35c9e3a6ced42320085125bf400480" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9abe35c9e3a6ced42320085125bf400480"></a>HIPRTC_ERROR_BUILTIN_OPERATION_FAILURE&#160;</td><td class="fielddoc"><p>Failed in builtin operation. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9a40cdc896c8f49fe4d13f2df51f09aaa3" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9a40cdc896c8f49fe4d13f2df51f09aaa3"></a>HIPRTC_ERROR_NO_NAME_EXPRESSIONS_AFTER_COMPILATION&#160;</td><td class="fielddoc"><p>No name expression after compilation. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9ab5b7de5fc47672db6541f3973f3bf7b2" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9ab5b7de5fc47672db6541f3973f3bf7b2"></a>HIPRTC_ERROR_NO_LOWERED_NAMES_BEFORE_COMPILATION&#160;</td><td class="fielddoc"><p>No lowered names before compilation. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9a8fcdce6a190a32526947d5285f16faf9" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9a8fcdce6a190a32526947d5285f16faf9"></a>HIPRTC_ERROR_NAME_EXPRESSION_NOT_VALID&#160;</td><td class="fielddoc"><p>Invalid name expression. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9ac8e5161c2d09c3757b1e4609e2b99313" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9ac8e5161c2d09c3757b1e4609e2b99313"></a>HIPRTC_ERROR_INTERNAL_ERROR&#160;</td><td class="fielddoc"><p>Internal error. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaaab4f1f28ef296fc6218b1ca8d21a6e9ade69dfa707075ad89d45c79d31825cba" name="ggaaab4f1f28ef296fc6218b1ca8d21a6e9ade69dfa707075ad89d45c79d31825cba"></a>HIPRTC_ERROR_LINKING&#160;</td><td class="fielddoc"><p>Error in linking. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga2e17b71d94ac350f2ccd914fd49d104e" name="ga2e17b71d94ac350f2ccd914fd49d104e"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga2e17b71d94ac350f2ccd914fd49d104e">&#9670;&#160;</a></span>hipSharedMemConfig</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga2e17b71d94ac350f2ccd914fd49d104e">hipSharedMemConfig</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<dl class="section warning"><dt>Warning</dt><dd>On AMD devices and some Nvidia devices, these hints and controls are ignored. </dd></dl>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga2e17b71d94ac350f2ccd914fd49d104eaf5b325c9b7bde878913f768eaba5014d" name="gga2e17b71d94ac350f2ccd914fd49d104eaf5b325c9b7bde878913f768eaba5014d"></a>hipSharedMemBankSizeDefault&#160;</td><td class="fielddoc"><p>The compiler selects a device-specific value for the banking. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga2e17b71d94ac350f2ccd914fd49d104ea0a95a6e0c33106c42d66ab9476ff954a" name="gga2e17b71d94ac350f2ccd914fd49d104ea0a95a6e0c33106c42d66ab9476ff954a"></a>hipSharedMemBankSizeFourByte&#160;</td><td class="fielddoc"><p>Shared mem is banked at 4-bytes intervals and performs best when adjacent threads access data 4 bytes apart. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga2e17b71d94ac350f2ccd914fd49d104ea64518b4f5a25f536c883330167e79258" name="gga2e17b71d94ac350f2ccd914fd49d104ea64518b4f5a25f536c883330167e79258"></a>hipSharedMemBankSizeEightByte&#160;</td><td class="fielddoc"><p>Shared mem is banked at 8-byte intervals and performs best when adjacent threads access data 4 bytes apart. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga3cb603dcc7b6a7884fec90988149b72a" name="ga3cb603dcc7b6a7884fec90988149b72a"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga3cb603dcc7b6a7884fec90988149b72a">&#9670;&#160;</a></span>hipStreamBatchMemOpType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga3cb603dcc7b6a7884fec90988149b72a">hipStreamBatchMemOpType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Operations for hipStreamBatchMemOp </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga3cb603dcc7b6a7884fec90988149b72aaeb04b51c0497b95ee2d9fc7895fad4bc" name="gga3cb603dcc7b6a7884fec90988149b72aaeb04b51c0497b95ee2d9fc7895fad4bc"></a>hipStreamMemOpWaitValue32&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga3cb603dcc7b6a7884fec90988149b72aad6a2b610d5d8fdea795be97991bc1db6" name="gga3cb603dcc7b6a7884fec90988149b72aad6a2b610d5d8fdea795be97991bc1db6"></a>hipStreamMemOpWriteValue32&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga3cb603dcc7b6a7884fec90988149b72aaec21f22ffacf0e874b31516438693aad" name="gga3cb603dcc7b6a7884fec90988149b72aaec21f22ffacf0e874b31516438693aad"></a>hipStreamMemOpWaitValue64&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga3cb603dcc7b6a7884fec90988149b72aa38a237828c1bbcce28a5338f09ad4ebf" name="gga3cb603dcc7b6a7884fec90988149b72aa38a237828c1bbcce28a5338f09ad4ebf"></a>hipStreamMemOpWriteValue64&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga3cb603dcc7b6a7884fec90988149b72aa690b461a80f7b48b111d7b94d18356af" name="gga3cb603dcc7b6a7884fec90988149b72aa690b461a80f7b48b111d7b94d18356af"></a>hipStreamMemOpBarrier&#160;</td><td class="fielddoc"><p>Currently not supported. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga3cb603dcc7b6a7884fec90988149b72aaed825058fa9b15a5f5e305f6fb8fe7b1" name="gga3cb603dcc7b6a7884fec90988149b72aaed825058fa9b15a5f5e305f6fb8fe7b1"></a>hipStreamMemOpFlushRemoteWrites&#160;</td><td class="fielddoc"><p>Currently not supported. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga3ae2cd03e623963eba9e0064d270ce4c" name="ga3ae2cd03e623963eba9e0064d270ce4c"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga3ae2cd03e623963eba9e0064d270ce4c">&#9670;&#160;</a></span>hipStreamCaptureMode</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga3ae2cd03e623963eba9e0064d270ce4c">hipStreamCaptureMode</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga3ae2cd03e623963eba9e0064d270ce4ca8e07e28586b1178e96e310f983c4a5d2" name="gga3ae2cd03e623963eba9e0064d270ce4ca8e07e28586b1178e96e310f983c4a5d2"></a>hipStreamCaptureModeGlobal&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga3ae2cd03e623963eba9e0064d270ce4ca42813de2ec53c9ada7ff8b6f3961bf6e" name="gga3ae2cd03e623963eba9e0064d270ce4ca42813de2ec53c9ada7ff8b6f3961bf6e"></a>hipStreamCaptureModeThreadLocal&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="gga3ae2cd03e623963eba9e0064d270ce4ca0b1aab61f226d1c7e40ba090f7fca255" name="gga3ae2cd03e623963eba9e0064d270ce4ca0b1aab61f226d1c7e40ba090f7fca255"></a>hipStreamCaptureModeRelaxed&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="gacb066bac5e39dd1b82926e02db1756a7" name="gacb066bac5e39dd1b82926e02db1756a7"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gacb066bac5e39dd1b82926e02db1756a7">&#9670;&#160;</a></span>hipStreamCaptureStatus</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#gacb066bac5e39dd1b82926e02db1756a7">hipStreamCaptureStatus</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggacb066bac5e39dd1b82926e02db1756a7a8c4ef8104913161030ff321b1454d4c3" name="ggacb066bac5e39dd1b82926e02db1756a7a8c4ef8104913161030ff321b1454d4c3"></a>hipStreamCaptureStatusNone&#160;</td><td class="fielddoc"><p>Stream is not capturing. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacb066bac5e39dd1b82926e02db1756a7abf89793c47e573fd8da9afad98d442d9" name="ggacb066bac5e39dd1b82926e02db1756a7abf89793c47e573fd8da9afad98d442d9"></a>hipStreamCaptureStatusActive&#160;</td><td class="fielddoc"><p>Stream is actively capturing. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggacb066bac5e39dd1b82926e02db1756a7a0d6ad4c0e0e50ddab3cf3b87ac7f38ce" name="ggacb066bac5e39dd1b82926e02db1756a7a0d6ad4c0e0e50ddab3cf3b87ac7f38ce"></a>hipStreamCaptureStatusInvalidated&#160;</td><td class="fielddoc"><p>Stream is part of a capture sequence that has been invalidated, but not terminated </p>
</td></tr>
</table>

</div>
</div>
<a id="ga76c22e13ab588b0a551814adca12e91a" name="ga76c22e13ab588b0a551814adca12e91a"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga76c22e13ab588b0a551814adca12e91a">&#9670;&#160;</a></span>hipStreamUpdateCaptureDependenciesFlags</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga76c22e13ab588b0a551814adca12e91a">hipStreamUpdateCaptureDependenciesFlags</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga76c22e13ab588b0a551814adca12e91aa46f516525ec015f5075adae5b9796187" name="gga76c22e13ab588b0a551814adca12e91aa46f516525ec015f5075adae5b9796187"></a>hipStreamAddCaptureDependencies&#160;</td><td class="fielddoc"><p>Add new nodes to the dependency set. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga76c22e13ab588b0a551814adca12e91aab0016a2fc2ce71f217ddc2717e9433aa" name="gga76c22e13ab588b0a551814adca12e91aab0016a2fc2ce71f217ddc2717e9433aa"></a>hipStreamSetCaptureDependencies&#160;</td><td class="fielddoc"><p>Replace the dependency set with the new nodes. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga46aec5b8c6c0302e179d82693f3b1243" name="ga46aec5b8c6c0302e179d82693f3b1243"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga46aec5b8c6c0302e179d82693f3b1243">&#9670;&#160;</a></span>hipSynchronizationPolicy</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga46aec5b8c6c0302e179d82693f3b1243">hipSynchronizationPolicy</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Stream Synchronization Policy. Can be set with hipStreamSetAttribute </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga46aec5b8c6c0302e179d82693f3b1243aadc2aeaed10849c3a75b818b593afdf9" name="gga46aec5b8c6c0302e179d82693f3b1243aadc2aeaed10849c3a75b818b593afdf9"></a>hipSyncPolicyAuto&#160;</td><td class="fielddoc"><p>Default Synchronization Policy. Host thread waits actively </p>
</td></tr>
<tr><td class="fieldname"><a id="gga46aec5b8c6c0302e179d82693f3b1243af0cd9e0cdc6c920c7bac2e545f2a7e8b" name="gga46aec5b8c6c0302e179d82693f3b1243af0cd9e0cdc6c920c7bac2e545f2a7e8b"></a>hipSyncPolicySpin&#160;</td><td class="fielddoc"><p>Host thread spins in tight loop waiting for completition </p>
</td></tr>
<tr><td class="fieldname"><a id="gga46aec5b8c6c0302e179d82693f3b1243a287d7e82eb8904eb707bd46c65a697f3" name="gga46aec5b8c6c0302e179d82693f3b1243a287d7e82eb8904eb707bd46c65a697f3"></a>hipSyncPolicyYield&#160;</td><td class="fielddoc"><p>Host spins but yields to other threads, reducing CPU usage </p>
</td></tr>
<tr><td class="fieldname"><a id="gga46aec5b8c6c0302e179d82693f3b1243aacf44cd40fb89bdd37d313f2739e918e" name="gga46aec5b8c6c0302e179d82693f3b1243aacf44cd40fb89bdd37d313f2739e918e"></a>hipSyncPolicyBlockingSync&#160;</td><td class="fielddoc"><p>Host thread blocks (sleeps) until the stream completes </p>
</td></tr>
</table>

</div>
</div>
<a id="ga87db9f321bad9b03ff2859f4509791f2" name="ga87db9f321bad9b03ff2859f4509791f2"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga87db9f321bad9b03ff2859f4509791f2">&#9670;&#160;</a></span>hipUserObjectFlags</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga87db9f321bad9b03ff2859f4509791f2">hipUserObjectFlags</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga87db9f321bad9b03ff2859f4509791f2a027010c7f334c1d21b77da618b20928b" name="gga87db9f321bad9b03ff2859f4509791f2a027010c7f334c1d21b77da618b20928b"></a>hipUserObjectNoDestructorSync&#160;</td><td class="fielddoc"><p>Destructor execution is not synchronized. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga614792f2c22f324d4125f616ceb5afda" name="ga614792f2c22f324d4125f616ceb5afda"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga614792f2c22f324d4125f616ceb5afda">&#9670;&#160;</a></span>hipUserObjectRetainFlags</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___global_defs.html#ga614792f2c22f324d4125f616ceb5afda">hipUserObjectRetainFlags</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga614792f2c22f324d4125f616ceb5afdaaf3e94cc868dccc75612acfafc23b86de" name="gga614792f2c22f324d4125f616ceb5afdaaf3e94cc868dccc75612acfafc23b86de"></a>hipGraphUserObjectMove&#160;</td><td class="fielddoc"><p>Add new reference or retain. </p>
</td></tr>
</table>

</div>
</div>
</div><!-- contents -->
<!-- HTML footer for doxygen 1.9.6-->
<!-- start footer part -->
</div>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../../reference/hip_runtime_api/global_defines_enums_structs_files.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Global defines, enums, structs and files</p>
      </div>
    </a>
    <a class="right-next"
       href="group___driver_types.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Driver Types</p>
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
  <script src="../../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b"></script>
<script src="../../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b"></script>

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
    <img id="rdc-watermark" src="../../_static/images/alpha-watermark.svg" alt="DRAFT watermark"/>
</div> -->
  </body>
</html>
