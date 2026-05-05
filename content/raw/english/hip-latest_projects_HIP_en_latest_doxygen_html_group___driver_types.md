---
title: "HIP Runtime API Reference: Driver Types &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___driver_types.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:46.824643+00:00
content_hash: "6500a3da49dfe06e"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>HIP Runtime API Reference: Driver Types &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/html/group___driver_types';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="Data Structures" href="annotated.html" />
    <link rel="prev" title="Global enum and defines" href="group___global_defs.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/group___driver_types.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l3"><a class="reference internal" href="group___global_defs.html">Global enum and defines</a></li>
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Driver Types</a></li>
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
    <h1>Driver Types</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="driver-types">
<h1>Driver Types<a class="headerlink" href="#driver-types" title="Link to this heading">#</a></h1>
<div class="doxygen-content docutils container">
<!-- HTML header for doxygen 1.9.6-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>HIP Runtime API Reference: Driver Types</title>
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
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/group___driver_types.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
<a href="#nested-classes">Data Structures</a> &#124;
<a href="#define-members">Macros</a> &#124;
<a href="#typedef-members">Typedefs</a> &#124;
<a href="#enum-members">Enumerations</a>  </div>
  <div class="headertitle"><div class="title">Driver Types</div></div>
</div><!--header-->
<div class="contents">
<table class="memberdecls">
<tr class="heading"><td colspan="2"><h2 class="groupheader"><a id="nested-classes" name="nested-classes"></a>
Data Structures</h2></td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_channel_format_desc.html">hipChannelFormatDesc</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="struct_h_i_p___a_r_r_a_y___d_e_s_c_r_i_p_t_o_r.html">HIP_ARRAY_DESCRIPTOR</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="struct_h_i_p___a_r_r_a_y3_d___d_e_s_c_r_i_p_t_o_r.html">HIP_ARRAY3D_DESCRIPTOR</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip___memcpy2_d.html">hip_Memcpy2D</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_mipmapped_array.html">hipMipmappedArray_t</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="struct_h_i_p___t_e_x_t_u_r_e___d_e_s_c.html">HIP_TEXTURE_DESC</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_resource_desc.html">hipResourceDesc</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="struct_h_i_p___r_e_s_o_u_r_c_e___d_e_s_c.html">HIP_RESOURCE_DESC</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_resource_view_desc.html">hipResourceViewDesc</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="struct_h_i_p___r_e_s_o_u_r_c_e___v_i_e_w___d_e_s_c.html">HIP_RESOURCE_VIEW_DESC</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_pitched_ptr.html">hipPitchedPtr</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_extent.html">hipExtent</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_pos.html">hipPos</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_memcpy3_d_parms.html">hipMemcpy3DParms</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="struct_h_i_p___m_e_m_c_p_y3_d.html">HIP_MEMCPY3D</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_mem_location.html">hipMemLocation</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_memcpy_attributes.html">hipMemcpyAttributes</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_offset3_d.html">hipOffset3D</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_memcpy3_d_operand.html">hipMemcpy3DOperand</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_memcpy3_d_batch_op.html">hipMemcpy3DBatchOp</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:"><td class="memItemLeft" align="right" valign="top">struct &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="structhip_memcpy3_d_peer_parms.html">hipMemcpy3DPeerParms</a></td></tr>
<tr class="separator:"><td class="memSeparator" colspan="2">&#160;</td></tr>
</table><table class="memberdecls">
<tr class="heading"><td colspan="2"><h2 class="groupheader"><a id="define-members" name="define-members"></a>
Macros</h2></td></tr>
<tr class="memitem:gaa284fe33b3b20a94c0fb7ce06cbd284a" id="r_gaa284fe33b3b20a94c0fb7ce06cbd284a"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#gaa284fe33b3b20a94c0fb7ce06cbd284a">HIP_TRSA_OVERRIDE_FORMAT</a>&#160;&#160;&#160;0x01</td></tr>
<tr class="memdesc:gaa284fe33b3b20a94c0fb7ce06cbd284a"><td class="mdescLeft">&#160;</td><td class="mdescRight">The hipTexRefSetArray function flags parameter override format value.  <br /></td></tr>
<tr class="separator:gaa284fe33b3b20a94c0fb7ce06cbd284a"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga76401f44a9502e5811f92516c78a99fa" id="r_ga76401f44a9502e5811f92516c78a99fa"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga76401f44a9502e5811f92516c78a99fa">HIP_TRSF_READ_AS_INTEGER</a>&#160;&#160;&#160;0x01</td></tr>
<tr class="memdesc:ga76401f44a9502e5811f92516c78a99fa"><td class="mdescLeft">&#160;</td><td class="mdescRight">The hipTexRefSetFlags function flags parameter read as integer value.  <br /></td></tr>
<tr class="separator:ga76401f44a9502e5811f92516c78a99fa"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gab89fdd3c5ebe4eeaf6a19b98dfdeae63" id="r_gab89fdd3c5ebe4eeaf6a19b98dfdeae63"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#gab89fdd3c5ebe4eeaf6a19b98dfdeae63">HIP_TRSF_NORMALIZED_COORDINATES</a>&#160;&#160;&#160;0x02</td></tr>
<tr class="memdesc:gab89fdd3c5ebe4eeaf6a19b98dfdeae63"><td class="mdescLeft">&#160;</td><td class="mdescRight">The hipTexRefSetFlags function flags parameter normalized coordinate value.  <br /></td></tr>
<tr class="separator:gab89fdd3c5ebe4eeaf6a19b98dfdeae63"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gab0d1233f549d2208e76508e105473a45" id="r_gab0d1233f549d2208e76508e105473a45"><td class="memItemLeft" align="right" valign="top">#define&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#gab0d1233f549d2208e76508e105473a45">HIP_TRSF_SRGB</a>&#160;&#160;&#160;0x10</td></tr>
<tr class="memdesc:gab0d1233f549d2208e76508e105473a45"><td class="mdescLeft">&#160;</td><td class="mdescRight">The hipTexRefSetFlags function flags parameter srgb value.  <br /></td></tr>
<tr class="separator:gab0d1233f549d2208e76508e105473a45"><td class="memSeparator" colspan="2">&#160;</td></tr>
</table><table class="memberdecls">
<tr class="heading"><td colspan="2"><h2 class="groupheader"><a id="typedef-members" name="typedef-members"></a>
Typedefs</h2></td></tr>
<tr class="memitem:ga618e4f089dc1e59056b0cb992f7aaae9" id="r_ga618e4f089dc1e59056b0cb992f7aaae9"><td class="memItemLeft" align="right" valign="top">typedef void *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga618e4f089dc1e59056b0cb992f7aaae9">hipDeviceptr_t</a></td></tr>
<tr class="separator:ga618e4f089dc1e59056b0cb992f7aaae9"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga489732842b8866d0af94040a296299a6" id="r_ga489732842b8866d0af94040a296299a6"><td class="memItemLeft" align="right" valign="top">typedef struct hipArray *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga489732842b8866d0af94040a296299a6">hipArray_t</a></td></tr>
<tr class="separator:ga489732842b8866d0af94040a296299a6"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga9f60656acb28958101d89192f365babc" id="r_ga9f60656acb28958101d89192f365babc"><td class="memItemLeft" align="right" valign="top">typedef const struct hipArray *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga9f60656acb28958101d89192f365babc">hipArray_const_t</a></td></tr>
<tr class="separator:ga9f60656acb28958101d89192f365babc"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga490778e2da44ddb3f1a127f0d17c8e5b" id="r_ga490778e2da44ddb3f1a127f0d17c8e5b"><td class="memItemLeft" align="right" valign="top">typedef hipMipmappedArray_t&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga490778e2da44ddb3f1a127f0d17c8e5b">hipmipmappedArray</a></td></tr>
<tr class="separator:ga490778e2da44ddb3f1a127f0d17c8e5b"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gad3a2249d04845db4cddf271c474058f6" id="r_gad3a2249d04845db4cddf271c474058f6"><td class="memItemLeft" align="right" valign="top">typedef const struct <a class="el" href="structhip_mipmapped_array.html">hipMipmappedArray</a> *&#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#gad3a2249d04845db4cddf271c474058f6">hipMipmappedArray_const_t</a></td></tr>
<tr class="separator:gad3a2249d04845db4cddf271c474058f6"><td class="memSeparator" colspan="2">&#160;</td></tr>
</table><table class="memberdecls">
<tr class="heading"><td colspan="2"><h2 class="groupheader"><a id="enum-members" name="enum-members"></a>
Enumerations</h2></td></tr>
<tr class="memitem:ga098cc20d3d4d7491e6fd551b92ddfe13" id="r_ga098cc20d3d4d7491e6fd551b92ddfe13"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga098cc20d3d4d7491e6fd551b92ddfe13">hipChannelFormatKind</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga098cc20d3d4d7491e6fd551b92ddfe13ab02387829e0e6ba8ecfe50ff48bb01ed">hipChannelFormatKindSigned</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga098cc20d3d4d7491e6fd551b92ddfe13aaaa9627a55441642dc6b979eea7a5aac">hipChannelFormatKindUnsigned</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga098cc20d3d4d7491e6fd551b92ddfe13a3e7aa403938413ba94916c95c505e18f">hipChannelFormatKindFloat</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga098cc20d3d4d7491e6fd551b92ddfe13a6c3c97c39f7019c1625cdc185cb3a1e0">hipChannelFormatKindNone</a> = 3
<br />
 }</td></tr>
<tr class="separator:ga098cc20d3d4d7491e6fd551b92ddfe13"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gabdf845d253f69e8e30230222c757ea00" id="r_gabdf845d253f69e8e30230222c757ea00"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#gabdf845d253f69e8e30230222c757ea00">hipArray_Format</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggabdf845d253f69e8e30230222c757ea00a52dbf377a1ffb064a876da381375774d">HIP_AD_FORMAT_UNSIGNED_INT8</a> = 0x01
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggabdf845d253f69e8e30230222c757ea00a0f95f2b5739bb056295a56c2fea57643">HIP_AD_FORMAT_UNSIGNED_INT16</a> = 0x02
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggabdf845d253f69e8e30230222c757ea00a372c9193990708f356a9db791bccadc7">HIP_AD_FORMAT_UNSIGNED_INT32</a> = 0x03
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggabdf845d253f69e8e30230222c757ea00a5aa8e6092c8db4d9e4eb782126b2fb8c">HIP_AD_FORMAT_SIGNED_INT8</a> = 0x08
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggabdf845d253f69e8e30230222c757ea00aa1ca13303f4ecaf87f8d679de5dae027">HIP_AD_FORMAT_SIGNED_INT16</a> = 0x09
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggabdf845d253f69e8e30230222c757ea00a5fc8dde617c05e4ceeaf14e26042e9fc">HIP_AD_FORMAT_SIGNED_INT32</a> = 0x0a
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggabdf845d253f69e8e30230222c757ea00a27a5bd952e593fbf4be3ad8e27a16a20">HIP_AD_FORMAT_HALF</a> = 0x10
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggabdf845d253f69e8e30230222c757ea00af99a0a987ff42a8909c484fdb183c2a7">HIP_AD_FORMAT_FLOAT</a> = 0x20
<br />
 }</td></tr>
<tr class="separator:gabdf845d253f69e8e30230222c757ea00"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gac4a2d283d15bd706ec2fce745e5cf7ac" id="r_gac4a2d283d15bd706ec2fce745e5cf7ac"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#gac4a2d283d15bd706ec2fce745e5cf7ac">hipResourceType</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggac4a2d283d15bd706ec2fce745e5cf7aca0589eb56f5887c95e50c97bb3afd618c">hipResourceTypeArray</a> = 0x00
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggac4a2d283d15bd706ec2fce745e5cf7aca67c0cdae37af35df9a56c09a2ec806a9">hipResourceTypeMipmappedArray</a> = 0x01
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggac4a2d283d15bd706ec2fce745e5cf7acabfbb200e565b7d76cecf8f13e3c282e5">hipResourceTypeLinear</a> = 0x02
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggac4a2d283d15bd706ec2fce745e5cf7acab79b496f361dd19e423382fc5aea7729">hipResourceTypePitch2D</a> = 0x03
<br />
 }</td></tr>
<tr class="separator:gac4a2d283d15bd706ec2fce745e5cf7ac"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga1d01da29fc699617c37f9bcdfbffa58e" id="r_ga1d01da29fc699617c37f9bcdfbffa58e"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga1d01da29fc699617c37f9bcdfbffa58e">hipResourcetype</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga1d01da29fc699617c37f9bcdfbffa58ea05b57e567f221b411deb80223a5ef77a">HIP_RESOURCE_TYPE_ARRAY</a> = 0x00
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga1d01da29fc699617c37f9bcdfbffa58ea71a6755e1536d31217ca8401cc70e0f1">HIP_RESOURCE_TYPE_MIPMAPPED_ARRAY</a> = 0x01
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga1d01da29fc699617c37f9bcdfbffa58ea7f86a0f731402eb6a70342294dc2f216">HIP_RESOURCE_TYPE_LINEAR</a> = 0x02
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga1d01da29fc699617c37f9bcdfbffa58ea1eb726cd957c3e446a2425d58875e456">HIP_RESOURCE_TYPE_PITCH2D</a> = 0x03
<br />
 }</td></tr>
<tr class="separator:ga1d01da29fc699617c37f9bcdfbffa58e"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gada6b505b00e83d66542c91a1b2307bf2" id="r_gada6b505b00e83d66542c91a1b2307bf2"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#gada6b505b00e83d66542c91a1b2307bf2">HIPaddress_mode</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggada6b505b00e83d66542c91a1b2307bf2a3eed307e0deb1f4520e93a94fbc1ee19">HIP_TR_ADDRESS_MODE_WRAP</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggada6b505b00e83d66542c91a1b2307bf2afaabb2d8d3f102b22886c78255f02739">HIP_TR_ADDRESS_MODE_CLAMP</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggada6b505b00e83d66542c91a1b2307bf2a8c3b7372c2ad54d6487a6c0ad42a3f8a">HIP_TR_ADDRESS_MODE_MIRROR</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggada6b505b00e83d66542c91a1b2307bf2a7ec57430ccc83aa203bb4f26ff9f319d">HIP_TR_ADDRESS_MODE_BORDER</a> = 3
<br />
 }</td></tr>
<tr class="separator:gada6b505b00e83d66542c91a1b2307bf2"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga1f77a6108eb4b1424cbcc1dc09eaaa6e" id="r_ga1f77a6108eb4b1424cbcc1dc09eaaa6e"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga1f77a6108eb4b1424cbcc1dc09eaaa6e">HIPfilter_mode</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga1f77a6108eb4b1424cbcc1dc09eaaa6ea4089ec9391134b86fb5d2e81387eac86">HIP_TR_FILTER_MODE_POINT</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga1f77a6108eb4b1424cbcc1dc09eaaa6eabe656f5e6d23d18d05cf8b20cd0589aa">HIP_TR_FILTER_MODE_LINEAR</a> = 1
<br />
 }</td></tr>
<tr class="separator:ga1f77a6108eb4b1424cbcc1dc09eaaa6e"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaa0ce0df88178c3157b1a56ae9adb96ce" id="r_gaa0ce0df88178c3157b1a56ae9adb96ce"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#gaa0ce0df88178c3157b1a56ae9adb96ce">hipResourceViewFormat</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea2063974b7c63fe5cc30608eee63c7614">hipResViewFormatNone</a> = 0x00
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceae24b50913e9a821ec8f8c577d047bb75">hipResViewFormatUnsignedChar1</a> = 0x01
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea2638d20534e10404e014f99b447603bd">hipResViewFormatUnsignedChar2</a> = 0x02
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea77ca99a2f486070fe859d714d3b62a57">hipResViewFormatUnsignedChar4</a> = 0x03
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceae3d8d4b36e2c4a25de5208513fbf751b">hipResViewFormatSignedChar1</a> = 0x04
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceabce1650eb85d3ef6db11513caaaf08be">hipResViewFormatSignedChar2</a> = 0x05
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea041b834a894dd458994afd3fb17f2dcf">hipResViewFormatSignedChar4</a> = 0x06
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceab1ec6b2b7587f5a7505df1518bc4e2cf">hipResViewFormatUnsignedShort1</a> = 0x07
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceaf1f818268859b5db38129200e9c1535a">hipResViewFormatUnsignedShort2</a> = 0x08
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceafb6ec538c67bcd6944a682263b7a6b39">hipResViewFormatUnsignedShort4</a> = 0x09
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceaeebafd1f78ec8590ff32a81a1268f0e5">hipResViewFormatSignedShort1</a> = 0x0a
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea55ccc4ec1afb1a023aeed517cffaccc2">hipResViewFormatSignedShort2</a> = 0x0b
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea37a0212e13a615f6a972834d661c5edb">hipResViewFormatSignedShort4</a> = 0x0c
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea74327a9fbc40fad62352d54248a106fb">hipResViewFormatUnsignedInt1</a> = 0x0d
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea4cd9e01ef72096fdd9c1f844b879ed95">hipResViewFormatUnsignedInt2</a> = 0x0e
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea7c253bb1e7c25cd51a9bcbe8a88106ab">hipResViewFormatUnsignedInt4</a> = 0x0f
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceafe8ce539aced89efc110cbd0f862bfa9">hipResViewFormatSignedInt1</a> = 0x10
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea03a89ff79e27e25450d2c02cbca60412">hipResViewFormatSignedInt2</a> = 0x11
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea49b56a0bc812ada92ff2199f29d42698">hipResViewFormatSignedInt4</a> = 0x12
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceab5d4e7c0bb19afd3e2c1b7006fa6bc43">hipResViewFormatHalf1</a> = 0x13
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceaad2ea80ee12541c78c8c14a020406233">hipResViewFormatHalf2</a> = 0x14
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea5e59ef9588077f8b7514582bf6b4bc76">hipResViewFormatHalf4</a> = 0x15
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea0b724b833c3350e7fa709b8d4c1b3908">hipResViewFormatFloat1</a> = 0x16
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceace7ed35d1f9e472b12434ef15d622f52">hipResViewFormatFloat2</a> = 0x17
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea63014d0f5b494259309ce97e2084828a">hipResViewFormatFloat4</a> = 0x18
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea72d644a4603a5f50e28219cca0dbc63a">hipResViewFormatUnsignedBlockCompressed1</a> = 0x19
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea8d3723df9d15fd0f7d948405074c4645">hipResViewFormatUnsignedBlockCompressed2</a> = 0x1a
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceadc93cc8950df637929fec0833091d843">hipResViewFormatUnsignedBlockCompressed3</a> = 0x1b
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea37b93313fdc9e6d4345c9f62e8ffacc3">hipResViewFormatUnsignedBlockCompressed4</a> = 0x1c
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceab2b2d0d8eeb42f5e0bd36742ddf5c32d">hipResViewFormatSignedBlockCompressed4</a> = 0x1d
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea2022710f743fb58bfc48b22520e95386">hipResViewFormatUnsignedBlockCompressed5</a> = 0x1e
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceab216c662063865156e5c064ce5156991">hipResViewFormatSignedBlockCompressed5</a> = 0x1f
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceae445c47c26608ab53a073b61b2495c84">hipResViewFormatUnsignedBlockCompressed6H</a> = 0x20
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96cea89fa2e14d9d41c48d01c34594728456f">hipResViewFormatSignedBlockCompressed6H</a> = 0x21
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaa0ce0df88178c3157b1a56ae9adb96ceaecae7d40367785c319d4af27f11d1cf7">hipResViewFormatUnsignedBlockCompressed7</a> = 0x22
<br />
 }</td></tr>
<tr class="separator:gaa0ce0df88178c3157b1a56ae9adb96ce"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga38e942dc4952156f08c4ba5232f20ec9" id="r_ga38e942dc4952156f08c4ba5232f20ec9"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga38e942dc4952156f08c4ba5232f20ec9">HIPresourceViewFormat</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a5577990d7926d3534c6cded3558d9721">HIP_RES_VIEW_FORMAT_NONE</a> = 0x00
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a130866b96a283c9ae7ed888e8b409bf2">HIP_RES_VIEW_FORMAT_UINT_1X8</a> = 0x01
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a42934e6b68903f070cee9de0cefb1618">HIP_RES_VIEW_FORMAT_UINT_2X8</a> = 0x02
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a4d00bad266d3b744bcfb9aca03ad5371">HIP_RES_VIEW_FORMAT_UINT_4X8</a> = 0x03
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a971f037b327889d81aec1d4471e5747e">HIP_RES_VIEW_FORMAT_SINT_1X8</a> = 0x04
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a335a6b14bb95049d62a22c636062dfe9">HIP_RES_VIEW_FORMAT_SINT_2X8</a> = 0x05
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a6a07d1b58e83f112e51577a71db4064e">HIP_RES_VIEW_FORMAT_SINT_4X8</a> = 0x06
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a1ff8d7bd5c9283225b5f1491422821f5">HIP_RES_VIEW_FORMAT_UINT_1X16</a> = 0x07
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a2550a8c0d339d4340d59c75b568fbef6">HIP_RES_VIEW_FORMAT_UINT_2X16</a> = 0x08
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a889f1abd7fbbecad885ffe99e09377a7">HIP_RES_VIEW_FORMAT_UINT_4X16</a> = 0x09
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9aaf61ce87edb24595b7087aa5392676c2">HIP_RES_VIEW_FORMAT_SINT_1X16</a> = 0x0a
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a292aee6051c9e3fb35d7e90df84bc5db">HIP_RES_VIEW_FORMAT_SINT_2X16</a> = 0x0b
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a3b002e409a851bf3010339887b51ec4c">HIP_RES_VIEW_FORMAT_SINT_4X16</a> = 0x0c
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a1c1c947c4444f9b5c064e2642a08d5ee">HIP_RES_VIEW_FORMAT_UINT_1X32</a> = 0x0d
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9ad9209dc87b0b30f348715ec8c3b6bc6e">HIP_RES_VIEW_FORMAT_UINT_2X32</a> = 0x0e
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9ac3cad7107de9afe19a83e1c92ec7d071">HIP_RES_VIEW_FORMAT_UINT_4X32</a> = 0x0f
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a52e0cc75079546b896608ed1fa0b2964">HIP_RES_VIEW_FORMAT_SINT_1X32</a> = 0x10
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a68f080c50ced45d092395ca51b0f4ff2">HIP_RES_VIEW_FORMAT_SINT_2X32</a> = 0x11
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9ac8f4750cfb1a60bba7e095c30246f6af">HIP_RES_VIEW_FORMAT_SINT_4X32</a> = 0x12
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9ac4e033ffcddac858422b7043f452926c">HIP_RES_VIEW_FORMAT_FLOAT_1X16</a> = 0x13
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9ab0b187f3471a77f1d722dde3ab9b73a7">HIP_RES_VIEW_FORMAT_FLOAT_2X16</a> = 0x14
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a8a61a8e88f7f76830071987d19f21ae5">HIP_RES_VIEW_FORMAT_FLOAT_4X16</a> = 0x15
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9af59a8dec7304f4d8261d4a3603595098">HIP_RES_VIEW_FORMAT_FLOAT_1X32</a> = 0x16
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9aa0df1d7cf39a6b3d488b43565d6fa1ee">HIP_RES_VIEW_FORMAT_FLOAT_2X32</a> = 0x17
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a180b648c21563572942b2448840a5c2e">HIP_RES_VIEW_FORMAT_FLOAT_4X32</a> = 0x18
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a0e4452d2d91fb43fcdc3aa265478a171">HIP_RES_VIEW_FORMAT_UNSIGNED_BC1</a> = 0x19
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9afb4fbc1ed1ef7c5965c9a5d80a50a0bb">HIP_RES_VIEW_FORMAT_UNSIGNED_BC2</a> = 0x1a
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9ae01c8d3950c053eef6a0ada98901ad72">HIP_RES_VIEW_FORMAT_UNSIGNED_BC3</a> = 0x1b
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a87572f3856c0b8efe1ec2472a3bae8e7">HIP_RES_VIEW_FORMAT_UNSIGNED_BC4</a> = 0x1c
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a6bcabc7788897c6ec43942f5bdc951ef">HIP_RES_VIEW_FORMAT_SIGNED_BC4</a> = 0x1d
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9abe53bcc8a9b200c3e4ceb1f758f79a7d">HIP_RES_VIEW_FORMAT_UNSIGNED_BC5</a> = 0x1e
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a972c526013a903d0bbf321231de69a06">HIP_RES_VIEW_FORMAT_SIGNED_BC5</a> = 0x1f
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a3a69f57d94eacd6d4dfe618b27e17ab7">HIP_RES_VIEW_FORMAT_UNSIGNED_BC6H</a> = 0x20
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a7a951a5566a5e075566f3f4ed4b1a491">HIP_RES_VIEW_FORMAT_SIGNED_BC6H</a> = 0x21
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga38e942dc4952156f08c4ba5232f20ec9a707b7c4445769c7a33929f284c92e088">HIP_RES_VIEW_FORMAT_UNSIGNED_BC7</a> = 0x22
<br />
 }</td></tr>
<tr class="separator:ga38e942dc4952156f08c4ba5232f20ec9"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga232e222db36b1fc672ba98054d036a18" id="r_ga232e222db36b1fc672ba98054d036a18"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga232e222db36b1fc672ba98054d036a18">hipMemcpyKind</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga232e222db36b1fc672ba98054d036a18a9d66b705aa85a9c83f0f533cef70d0af">hipMemcpyHostToHost</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga232e222db36b1fc672ba98054d036a18aff32175ecb0c7113200286eff8211008">hipMemcpyHostToDevice</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga232e222db36b1fc672ba98054d036a18aba2505e9ce1e5382f17730bc670917d1">hipMemcpyDeviceToHost</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga232e222db36b1fc672ba98054d036a18abd05a09d3105e0ce25b34dd91cf83f88">hipMemcpyDeviceToDevice</a> = 3
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga232e222db36b1fc672ba98054d036a18a4e37107e416f79a2edf2b6534163c823">hipMemcpyDefault</a> = 4
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga232e222db36b1fc672ba98054d036a18a43a2409dc0d09645418a5855ab0c0f1c">hipMemcpyDeviceToDeviceNoCU</a> = 1024
<br />
 }</td></tr>
<tr class="separator:ga232e222db36b1fc672ba98054d036a18"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gaee88a54f9376456dcabf3fdcf9b9810f" id="r_gaee88a54f9376456dcabf3fdcf9b9810f"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#gaee88a54f9376456dcabf3fdcf9b9810f">hipMemLocationType</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaee88a54f9376456dcabf3fdcf9b9810fa5403e1e0771ce147fc29edfb2c3e84a3">hipMemLocationTypeInvalid</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaee88a54f9376456dcabf3fdcf9b9810fa895e0e72b22e15f6e5808b034587a1ae">hipMemLocationTypeNone</a> = 0
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaee88a54f9376456dcabf3fdcf9b9810fa7dd18d5d22a3ab95b64f2daa8e3b33de">hipMemLocationTypeDevice</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaee88a54f9376456dcabf3fdcf9b9810fa5fc26b0761e2a06ded14048ea9f2cdd3">hipMemLocationTypeHost</a> = 2
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaee88a54f9376456dcabf3fdcf9b9810fa3ccc587f519942cbbdb869e205054e5e">hipMemLocationTypeHostNuma</a> = 3
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggaee88a54f9376456dcabf3fdcf9b9810fa2ea10c636002fc4f4a817fbdeaeb4c0a">hipMemLocationTypeHostNumaCurrent</a>
<br />
 }</td></tr>
<tr class="separator:gaee88a54f9376456dcabf3fdcf9b9810f"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gabbc7d80e011c3a40173a7b763cc0ac99" id="r_gabbc7d80e011c3a40173a7b763cc0ac99"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#gabbc7d80e011c3a40173a7b763cc0ac99">hipMemcpyFlags</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggabbc7d80e011c3a40173a7b763cc0ac99af3ad2864dfb025aea5b10a87bc9b07e3">hipMemcpyFlagDefault</a> = 0x0
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggabbc7d80e011c3a40173a7b763cc0ac99a7b4d87aef3c4a41cf9711b10670d9120">hipMemcpyFlagPreferOverlapWithCompute</a> = 0x1
<br />
 }</td></tr>
<tr class="separator:gabbc7d80e011c3a40173a7b763cc0ac99"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga3298f79d98abcbdf71e53f718cdec254" id="r_ga3298f79d98abcbdf71e53f718cdec254"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga3298f79d98abcbdf71e53f718cdec254">hipMemcpySrcAccessOrder</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga3298f79d98abcbdf71e53f718cdec254a7fb93c9ebb930b4a87f0d199a5c61627">hipMemcpySrcAccessOrderInvalid</a> = 0x0
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga3298f79d98abcbdf71e53f718cdec254ae7af12ad5ca4a82f1f2baad3adfcf3f7">hipMemcpySrcAccessOrderStream</a> = 0x1
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga3298f79d98abcbdf71e53f718cdec254a9e2fc56667605febb5f6245866534b2f">hipMemcpySrcAccessOrderDuringApiCall</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga3298f79d98abcbdf71e53f718cdec254ad10477ca5a7a85d28731ff3565a234e2">hipMemcpySrcAccessOrderAny</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga3298f79d98abcbdf71e53f718cdec254a958bb9acf191ab6c24e65901bd7515f4">hipMemcpySrcAccessOrderMax</a> = 0x7FFFFFFF
<br />
 }</td></tr>
<tr class="separator:ga3298f79d98abcbdf71e53f718cdec254"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:gadb3e6d03d988754d5ae4f7260373089e" id="r_gadb3e6d03d988754d5ae4f7260373089e"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#gadb3e6d03d988754d5ae4f7260373089e">hipMemcpy3DOperandType</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggadb3e6d03d988754d5ae4f7260373089ea93f9ada3ed1066ffee214747f40f7512">hipMemcpyOperandTypePointer</a> = 0x1
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggadb3e6d03d988754d5ae4f7260373089ea0b6d41595e311461e28b5cfdbd8e7198">hipMemcpyOperandTypeArray</a> = 0x2
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#ggadb3e6d03d988754d5ae4f7260373089ea6762a84f9d14a56f24d794f2fffc2799">hipMemcpyOperandTypeMax</a> = 0x7FFFFFFF
<br />
 }</td></tr>
<tr class="separator:gadb3e6d03d988754d5ae4f7260373089e"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga8951f1475533fcd35b4a7a9aeb41272f" id="r_ga8951f1475533fcd35b4a7a9aeb41272f"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga8951f1475533fcd35b4a7a9aeb41272f">hipFunction_attribute</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga8951f1475533fcd35b4a7a9aeb41272fa2b3276e86efaf46c92c4cb2c6cde047c">HIP_FUNC_ATTRIBUTE_MAX_THREADS_PER_BLOCK</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga8951f1475533fcd35b4a7a9aeb41272fab82448e3b734ca5662b14793c60d4eab">HIP_FUNC_ATTRIBUTE_SHARED_SIZE_BYTES</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga8951f1475533fcd35b4a7a9aeb41272fadebb80a22231c94fe055e2d29ce2af18">HIP_FUNC_ATTRIBUTE_CONST_SIZE_BYTES</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga8951f1475533fcd35b4a7a9aeb41272fa3aeed307844d1aaa793e914365622a8c">HIP_FUNC_ATTRIBUTE_LOCAL_SIZE_BYTES</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga8951f1475533fcd35b4a7a9aeb41272fad881275205999e13b6006589d3253e09">HIP_FUNC_ATTRIBUTE_NUM_REGS</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga8951f1475533fcd35b4a7a9aeb41272faefaa35608ff8b9049d7bad0c22b62a67">HIP_FUNC_ATTRIBUTE_PTX_VERSION</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga8951f1475533fcd35b4a7a9aeb41272fa16863fccec7c1453e7ad30f7484ba60a">HIP_FUNC_ATTRIBUTE_BINARY_VERSION</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga8951f1475533fcd35b4a7a9aeb41272fa2de0385b6d314acdacd178fabe5094e0">HIP_FUNC_ATTRIBUTE_CACHE_MODE_CA</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga8951f1475533fcd35b4a7a9aeb41272faf2c3f8f7994af78193b2692e497c777c">HIP_FUNC_ATTRIBUTE_MAX_DYNAMIC_SHARED_SIZE_BYTES</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga8951f1475533fcd35b4a7a9aeb41272fa2e7d7259e292793f35b0b71735debdce">HIP_FUNC_ATTRIBUTE_PREFERRED_SHARED_MEMORY_CARVEOUT</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga8951f1475533fcd35b4a7a9aeb41272fa1369da7f0ad27875636a0525f67a5bd4">HIP_FUNC_ATTRIBUTE_MAX</a>
<br />
 }</td></tr>
<tr class="separator:ga8951f1475533fcd35b4a7a9aeb41272f"><td class="memSeparator" colspan="2">&#160;</td></tr>
<tr class="memitem:ga44f13516fbfca2d20cc2594b7f633cf1" id="r_ga44f13516fbfca2d20cc2594b7f633cf1"><td class="memItemLeft" align="right" valign="top">enum &#160;</td><td class="memItemRight" valign="bottom"><a class="el" href="group___driver_types.html#ga44f13516fbfca2d20cc2594b7f633cf1">hipPointer_attribute</a> { <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1a351f4be735a13e2788c0c74abf7cb0e0">HIP_POINTER_ATTRIBUTE_CONTEXT</a> = 1
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1adb8735d707be3d31dd64a46271069237">HIP_POINTER_ATTRIBUTE_MEMORY_TYPE</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1a24c68927c9881c8ffbcbb0ecc04b0a31">HIP_POINTER_ATTRIBUTE_DEVICE_POINTER</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1a639ebcef2880cd4cb020dfa7fecd5119">HIP_POINTER_ATTRIBUTE_HOST_POINTER</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1ab05bd233393c51d2db1dfbb7ae8d70c9">HIP_POINTER_ATTRIBUTE_P2P_TOKENS</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1a9a587bd4cc33f9a58961cb5801c5489d">HIP_POINTER_ATTRIBUTE_SYNC_MEMOPS</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1a264f5f3d40fe591e880eaf73c37d569a">HIP_POINTER_ATTRIBUTE_BUFFER_ID</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1ad3ca9bfc093449926c90734900334fac">HIP_POINTER_ATTRIBUTE_IS_MANAGED</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1a0cab1da1255a8b4d62d87d7c83806296">HIP_POINTER_ATTRIBUTE_DEVICE_ORDINAL</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1a15544939ec22c928e579c514293d9412">HIP_POINTER_ATTRIBUTE_IS_LEGACY_HIP_IPC_CAPABLE</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1ae82b2f8de6a3238aa5d65cc40e1d0368">HIP_POINTER_ATTRIBUTE_RANGE_START_ADDR</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1a160ddae557035db47837e507f595825e">HIP_POINTER_ATTRIBUTE_RANGE_SIZE</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1a2d96a7dd4e9cf031b94fc3cd1309d723">HIP_POINTER_ATTRIBUTE_MAPPED</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1afc43c9bb83f3b15b20e3c85e42ab1acb">HIP_POINTER_ATTRIBUTE_ALLOWED_HANDLE_TYPES</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1a64ff1f6b7144501cb01c153b1ccbb51e">HIP_POINTER_ATTRIBUTE_IS_GPU_DIRECT_RDMA_CAPABLE</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1ac81cd9e2ec4fed70a14a0576ff18cc05">HIP_POINTER_ATTRIBUTE_ACCESS_FLAGS</a>
, <br />
&#160;&#160;<a class="el" href="group___driver_types.html#gga44f13516fbfca2d20cc2594b7f633cf1a337d6dd0cdfad646bb635cafcb78c44c">HIP_POINTER_ATTRIBUTE_MEMPOOL_HANDLE</a>
<br />
 }</td></tr>
<tr class="separator:ga44f13516fbfca2d20cc2594b7f633cf1"><td class="memSeparator" colspan="2">&#160;</td></tr>
</table>
<a name="details" id="details"></a><h2 class="groupheader">Detailed Description</h2>
<p>This section describes the driver data types. </p>
<h2 class="groupheader">Macro Definition Documentation</h2>
<a id="gaa284fe33b3b20a94c0fb7ce06cbd284a" name="gaa284fe33b3b20a94c0fb7ce06cbd284a"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaa284fe33b3b20a94c0fb7ce06cbd284a">&#9670;&#160;</a></span>HIP_TRSA_OVERRIDE_FORMAT</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIP_TRSA_OVERRIDE_FORMAT&#160;&#160;&#160;0x01</td>
        </tr>
      </table>
</div><div class="memdoc">

<p>The hipTexRefSetArray function flags parameter override format value. </p>

</div>
</div>
<a id="gab89fdd3c5ebe4eeaf6a19b98dfdeae63" name="gab89fdd3c5ebe4eeaf6a19b98dfdeae63"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gab89fdd3c5ebe4eeaf6a19b98dfdeae63">&#9670;&#160;</a></span>HIP_TRSF_NORMALIZED_COORDINATES</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIP_TRSF_NORMALIZED_COORDINATES&#160;&#160;&#160;0x02</td>
        </tr>
      </table>
</div><div class="memdoc">

<p>The hipTexRefSetFlags function flags parameter normalized coordinate value. </p>

</div>
</div>
<a id="ga76401f44a9502e5811f92516c78a99fa" name="ga76401f44a9502e5811f92516c78a99fa"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga76401f44a9502e5811f92516c78a99fa">&#9670;&#160;</a></span>HIP_TRSF_READ_AS_INTEGER</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIP_TRSF_READ_AS_INTEGER&#160;&#160;&#160;0x01</td>
        </tr>
      </table>
</div><div class="memdoc">

<p>The hipTexRefSetFlags function flags parameter read as integer value. </p>

</div>
</div>
<a id="gab0d1233f549d2208e76508e105473a45" name="gab0d1233f549d2208e76508e105473a45"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gab0d1233f549d2208e76508e105473a45">&#9670;&#160;</a></span>HIP_TRSF_SRGB</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">#define HIP_TRSF_SRGB&#160;&#160;&#160;0x10</td>
        </tr>
      </table>
</div><div class="memdoc">

<p>The hipTexRefSetFlags function flags parameter srgb value. </p>

</div>
</div>
<h2 class="groupheader">Typedef Documentation</h2>
<a id="ga9f60656acb28958101d89192f365babc" name="ga9f60656acb28958101d89192f365babc"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga9f60656acb28958101d89192f365babc">&#9670;&#160;</a></span>hipArray_const_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef const struct hipArray* <a class="el" href="group___driver_types.html#ga9f60656acb28958101d89192f365babc">hipArray_const_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga489732842b8866d0af94040a296299a6" name="ga489732842b8866d0af94040a296299a6"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga489732842b8866d0af94040a296299a6">&#9670;&#160;</a></span>hipArray_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef struct hipArray* <a class="el" href="group___driver_types.html#ga489732842b8866d0af94040a296299a6">hipArray_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga618e4f089dc1e59056b0cb992f7aaae9" name="ga618e4f089dc1e59056b0cb992f7aaae9"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga618e4f089dc1e59056b0cb992f7aaae9">&#9670;&#160;</a></span>hipDeviceptr_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef void* <a class="el" href="group___driver_types.html#ga618e4f089dc1e59056b0cb992f7aaae9">hipDeviceptr_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="ga490778e2da44ddb3f1a127f0d17c8e5b" name="ga490778e2da44ddb3f1a127f0d17c8e5b"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga490778e2da44ddb3f1a127f0d17c8e5b">&#9670;&#160;</a></span>hipmipmappedArray</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef hipMipmappedArray_t <a class="el" href="group___driver_types.html#ga490778e2da44ddb3f1a127f0d17c8e5b">hipmipmappedArray</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<a id="gad3a2249d04845db4cddf271c474058f6" name="gad3a2249d04845db4cddf271c474058f6"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gad3a2249d04845db4cddf271c474058f6">&#9670;&#160;</a></span>hipMipmappedArray_const_t</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">typedef const struct <a class="el" href="structhip_mipmapped_array.html">hipMipmappedArray</a>* <a class="el" href="group___driver_types.html#gad3a2249d04845db4cddf271c474058f6">hipMipmappedArray_const_t</a></td>
        </tr>
      </table>
</div><div class="memdoc">

</div>
</div>
<h2 class="groupheader">Enumeration Type Documentation</h2>
<a id="gada6b505b00e83d66542c91a1b2307bf2" name="gada6b505b00e83d66542c91a1b2307bf2"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gada6b505b00e83d66542c91a1b2307bf2">&#9670;&#160;</a></span>HIPaddress_mode</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#gada6b505b00e83d66542c91a1b2307bf2">HIPaddress_mode</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP texture address modes </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggada6b505b00e83d66542c91a1b2307bf2a3eed307e0deb1f4520e93a94fbc1ee19" name="ggada6b505b00e83d66542c91a1b2307bf2a3eed307e0deb1f4520e93a94fbc1ee19"></a>HIP_TR_ADDRESS_MODE_WRAP&#160;</td><td class="fielddoc"><p>Wrap address mode. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggada6b505b00e83d66542c91a1b2307bf2afaabb2d8d3f102b22886c78255f02739" name="ggada6b505b00e83d66542c91a1b2307bf2afaabb2d8d3f102b22886c78255f02739"></a>HIP_TR_ADDRESS_MODE_CLAMP&#160;</td><td class="fielddoc"><p>Clamp address mode. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggada6b505b00e83d66542c91a1b2307bf2a8c3b7372c2ad54d6487a6c0ad42a3f8a" name="ggada6b505b00e83d66542c91a1b2307bf2a8c3b7372c2ad54d6487a6c0ad42a3f8a"></a>HIP_TR_ADDRESS_MODE_MIRROR&#160;</td><td class="fielddoc"><p>Mirror address mode. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggada6b505b00e83d66542c91a1b2307bf2a7ec57430ccc83aa203bb4f26ff9f319d" name="ggada6b505b00e83d66542c91a1b2307bf2a7ec57430ccc83aa203bb4f26ff9f319d"></a>HIP_TR_ADDRESS_MODE_BORDER&#160;</td><td class="fielddoc"><p>Border address mode. </p>
</td></tr>
</table>

</div>
</div>
<a id="gabdf845d253f69e8e30230222c757ea00" name="gabdf845d253f69e8e30230222c757ea00"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gabdf845d253f69e8e30230222c757ea00">&#9670;&#160;</a></span>hipArray_Format</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#gabdf845d253f69e8e30230222c757ea00">hipArray_Format</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP array format </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggabdf845d253f69e8e30230222c757ea00a52dbf377a1ffb064a876da381375774d" name="ggabdf845d253f69e8e30230222c757ea00a52dbf377a1ffb064a876da381375774d"></a>HIP_AD_FORMAT_UNSIGNED_INT8&#160;</td><td class="fielddoc"><p>Unsigned 8-bit array format. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggabdf845d253f69e8e30230222c757ea00a0f95f2b5739bb056295a56c2fea57643" name="ggabdf845d253f69e8e30230222c757ea00a0f95f2b5739bb056295a56c2fea57643"></a>HIP_AD_FORMAT_UNSIGNED_INT16&#160;</td><td class="fielddoc"><p>Unsigned 16-bit array format. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggabdf845d253f69e8e30230222c757ea00a372c9193990708f356a9db791bccadc7" name="ggabdf845d253f69e8e30230222c757ea00a372c9193990708f356a9db791bccadc7"></a>HIP_AD_FORMAT_UNSIGNED_INT32&#160;</td><td class="fielddoc"><p>Unsigned 32-bit array format. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggabdf845d253f69e8e30230222c757ea00a5aa8e6092c8db4d9e4eb782126b2fb8c" name="ggabdf845d253f69e8e30230222c757ea00a5aa8e6092c8db4d9e4eb782126b2fb8c"></a>HIP_AD_FORMAT_SIGNED_INT8&#160;</td><td class="fielddoc"><p>Signed 8-bit array format. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggabdf845d253f69e8e30230222c757ea00aa1ca13303f4ecaf87f8d679de5dae027" name="ggabdf845d253f69e8e30230222c757ea00aa1ca13303f4ecaf87f8d679de5dae027"></a>HIP_AD_FORMAT_SIGNED_INT16&#160;</td><td class="fielddoc"><p>Signed 16-bit array format. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggabdf845d253f69e8e30230222c757ea00a5fc8dde617c05e4ceeaf14e26042e9fc" name="ggabdf845d253f69e8e30230222c757ea00a5fc8dde617c05e4ceeaf14e26042e9fc"></a>HIP_AD_FORMAT_SIGNED_INT32&#160;</td><td class="fielddoc"><p>Signed 32-bit array format. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggabdf845d253f69e8e30230222c757ea00a27a5bd952e593fbf4be3ad8e27a16a20" name="ggabdf845d253f69e8e30230222c757ea00a27a5bd952e593fbf4be3ad8e27a16a20"></a>HIP_AD_FORMAT_HALF&#160;</td><td class="fielddoc"><p>Half array format. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggabdf845d253f69e8e30230222c757ea00af99a0a987ff42a8909c484fdb183c2a7" name="ggabdf845d253f69e8e30230222c757ea00af99a0a987ff42a8909c484fdb183c2a7"></a>HIP_AD_FORMAT_FLOAT&#160;</td><td class="fielddoc"><p>Float array format. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga098cc20d3d4d7491e6fd551b92ddfe13" name="ga098cc20d3d4d7491e6fd551b92ddfe13"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga098cc20d3d4d7491e6fd551b92ddfe13">&#9670;&#160;</a></span>hipChannelFormatKind</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#ga098cc20d3d4d7491e6fd551b92ddfe13">hipChannelFormatKind</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP channel format kinds </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga098cc20d3d4d7491e6fd551b92ddfe13ab02387829e0e6ba8ecfe50ff48bb01ed" name="gga098cc20d3d4d7491e6fd551b92ddfe13ab02387829e0e6ba8ecfe50ff48bb01ed"></a>hipChannelFormatKindSigned&#160;</td><td class="fielddoc"><p>Signed channel format. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga098cc20d3d4d7491e6fd551b92ddfe13aaaa9627a55441642dc6b979eea7a5aac" name="gga098cc20d3d4d7491e6fd551b92ddfe13aaaa9627a55441642dc6b979eea7a5aac"></a>hipChannelFormatKindUnsigned&#160;</td><td class="fielddoc"><p>Unsigned channel format. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga098cc20d3d4d7491e6fd551b92ddfe13a3e7aa403938413ba94916c95c505e18f" name="gga098cc20d3d4d7491e6fd551b92ddfe13a3e7aa403938413ba94916c95c505e18f"></a>hipChannelFormatKindFloat&#160;</td><td class="fielddoc"><p>Float channel format. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga098cc20d3d4d7491e6fd551b92ddfe13a6c3c97c39f7019c1625cdc185cb3a1e0" name="gga098cc20d3d4d7491e6fd551b92ddfe13a6c3c97c39f7019c1625cdc185cb3a1e0"></a>hipChannelFormatKindNone&#160;</td><td class="fielddoc"><p>No channel format. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga1f77a6108eb4b1424cbcc1dc09eaaa6e" name="ga1f77a6108eb4b1424cbcc1dc09eaaa6e"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga1f77a6108eb4b1424cbcc1dc09eaaa6e">&#9670;&#160;</a></span>HIPfilter_mode</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#ga1f77a6108eb4b1424cbcc1dc09eaaa6e">HIPfilter_mode</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP filter modes </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga1f77a6108eb4b1424cbcc1dc09eaaa6ea4089ec9391134b86fb5d2e81387eac86" name="gga1f77a6108eb4b1424cbcc1dc09eaaa6ea4089ec9391134b86fb5d2e81387eac86"></a>HIP_TR_FILTER_MODE_POINT&#160;</td><td class="fielddoc"><p>Filter mode point. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga1f77a6108eb4b1424cbcc1dc09eaaa6eabe656f5e6d23d18d05cf8b20cd0589aa" name="gga1f77a6108eb4b1424cbcc1dc09eaaa6eabe656f5e6d23d18d05cf8b20cd0589aa"></a>HIP_TR_FILTER_MODE_LINEAR&#160;</td><td class="fielddoc"><p>Filter mode linear. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga8951f1475533fcd35b4a7a9aeb41272f" name="ga8951f1475533fcd35b4a7a9aeb41272f"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga8951f1475533fcd35b4a7a9aeb41272f">&#9670;&#160;</a></span>hipFunction_attribute</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#ga8951f1475533fcd35b4a7a9aeb41272f">hipFunction_attribute</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga8951f1475533fcd35b4a7a9aeb41272fa2b3276e86efaf46c92c4cb2c6cde047c" name="gga8951f1475533fcd35b4a7a9aeb41272fa2b3276e86efaf46c92c4cb2c6cde047c"></a>HIP_FUNC_ATTRIBUTE_MAX_THREADS_PER_BLOCK&#160;</td><td class="fielddoc"><p>The maximum number of threads per block. Depends on function and device. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga8951f1475533fcd35b4a7a9aeb41272fab82448e3b734ca5662b14793c60d4eab" name="gga8951f1475533fcd35b4a7a9aeb41272fab82448e3b734ca5662b14793c60d4eab"></a>HIP_FUNC_ATTRIBUTE_SHARED_SIZE_BYTES&#160;</td><td class="fielddoc"><p>The statically allocated shared memory size in bytes per block required by the function. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga8951f1475533fcd35b4a7a9aeb41272fadebb80a22231c94fe055e2d29ce2af18" name="gga8951f1475533fcd35b4a7a9aeb41272fadebb80a22231c94fe055e2d29ce2af18"></a>HIP_FUNC_ATTRIBUTE_CONST_SIZE_BYTES&#160;</td><td class="fielddoc"><p>The user-allocated constant memory by the function in bytes. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga8951f1475533fcd35b4a7a9aeb41272fa3aeed307844d1aaa793e914365622a8c" name="gga8951f1475533fcd35b4a7a9aeb41272fa3aeed307844d1aaa793e914365622a8c"></a>HIP_FUNC_ATTRIBUTE_LOCAL_SIZE_BYTES&#160;</td><td class="fielddoc"><p>The local memory usage of each thread by this function in bytes. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga8951f1475533fcd35b4a7a9aeb41272fad881275205999e13b6006589d3253e09" name="gga8951f1475533fcd35b4a7a9aeb41272fad881275205999e13b6006589d3253e09"></a>HIP_FUNC_ATTRIBUTE_NUM_REGS&#160;</td><td class="fielddoc"><p>The number of registers used by each thread of this function. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga8951f1475533fcd35b4a7a9aeb41272faefaa35608ff8b9049d7bad0c22b62a67" name="gga8951f1475533fcd35b4a7a9aeb41272faefaa35608ff8b9049d7bad0c22b62a67"></a>HIP_FUNC_ATTRIBUTE_PTX_VERSION&#160;</td><td class="fielddoc"><p>PTX version. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga8951f1475533fcd35b4a7a9aeb41272fa16863fccec7c1453e7ad30f7484ba60a" name="gga8951f1475533fcd35b4a7a9aeb41272fa16863fccec7c1453e7ad30f7484ba60a"></a>HIP_FUNC_ATTRIBUTE_BINARY_VERSION&#160;</td><td class="fielddoc"><p>Binary version. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga8951f1475533fcd35b4a7a9aeb41272fa2de0385b6d314acdacd178fabe5094e0" name="gga8951f1475533fcd35b4a7a9aeb41272fa2de0385b6d314acdacd178fabe5094e0"></a>HIP_FUNC_ATTRIBUTE_CACHE_MODE_CA&#160;</td><td class="fielddoc"><p>Cache mode. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga8951f1475533fcd35b4a7a9aeb41272faf2c3f8f7994af78193b2692e497c777c" name="gga8951f1475533fcd35b4a7a9aeb41272faf2c3f8f7994af78193b2692e497c777c"></a>HIP_FUNC_ATTRIBUTE_MAX_DYNAMIC_SHARED_SIZE_BYTES&#160;</td><td class="fielddoc"><p>The maximum dynamic shared memory per block for this function in bytes. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga8951f1475533fcd35b4a7a9aeb41272fa2e7d7259e292793f35b0b71735debdce" name="gga8951f1475533fcd35b4a7a9aeb41272fa2e7d7259e292793f35b0b71735debdce"></a>HIP_FUNC_ATTRIBUTE_PREFERRED_SHARED_MEMORY_CARVEOUT&#160;</td><td class="fielddoc"><p>The shared memory carveout preference in percent of the maximum shared memory. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga8951f1475533fcd35b4a7a9aeb41272fa1369da7f0ad27875636a0525f67a5bd4" name="gga8951f1475533fcd35b4a7a9aeb41272fa1369da7f0ad27875636a0525f67a5bd4"></a>HIP_FUNC_ATTRIBUTE_MAX&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="gadb3e6d03d988754d5ae4f7260373089e" name="gadb3e6d03d988754d5ae4f7260373089e"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gadb3e6d03d988754d5ae4f7260373089e">&#9670;&#160;</a></span>hipMemcpy3DOperandType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#gadb3e6d03d988754d5ae4f7260373089e">hipMemcpy3DOperandType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Operand types for individual copies within a batch </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggadb3e6d03d988754d5ae4f7260373089ea93f9ada3ed1066ffee214747f40f7512" name="ggadb3e6d03d988754d5ae4f7260373089ea93f9ada3ed1066ffee214747f40f7512"></a>hipMemcpyOperandTypePointer&#160;</td><td class="fielddoc"><p>Mempcy operand is a valid pointer. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggadb3e6d03d988754d5ae4f7260373089ea0b6d41595e311461e28b5cfdbd8e7198" name="ggadb3e6d03d988754d5ae4f7260373089ea0b6d41595e311461e28b5cfdbd8e7198"></a>hipMemcpyOperandTypeArray&#160;</td><td class="fielddoc"><p>Memcpy operand is a valid hipArray. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggadb3e6d03d988754d5ae4f7260373089ea6762a84f9d14a56f24d794f2fffc2799" name="ggadb3e6d03d988754d5ae4f7260373089ea6762a84f9d14a56f24d794f2fffc2799"></a>hipMemcpyOperandTypeMax&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="gabbc7d80e011c3a40173a7b763cc0ac99" name="gabbc7d80e011c3a40173a7b763cc0ac99"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gabbc7d80e011c3a40173a7b763cc0ac99">&#9670;&#160;</a></span>hipMemcpyFlags</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#gabbc7d80e011c3a40173a7b763cc0ac99">hipMemcpyFlags</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Flags to specify for copies within a batch. Used with hipMemcpyBatchAsync </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggabbc7d80e011c3a40173a7b763cc0ac99af3ad2864dfb025aea5b10a87bc9b07e3" name="ggabbc7d80e011c3a40173a7b763cc0ac99af3ad2864dfb025aea5b10a87bc9b07e3"></a>hipMemcpyFlagDefault&#160;</td><td class="fielddoc"><p>Default flag. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggabbc7d80e011c3a40173a7b763cc0ac99a7b4d87aef3c4a41cf9711b10670d9120" name="ggabbc7d80e011c3a40173a7b763cc0ac99a7b4d87aef3c4a41cf9711b10670d9120"></a>hipMemcpyFlagPreferOverlapWithCompute&#160;</td><td class="fielddoc"><p>Tries to overlap copy with compute work. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga232e222db36b1fc672ba98054d036a18" name="ga232e222db36b1fc672ba98054d036a18"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga232e222db36b1fc672ba98054d036a18">&#9670;&#160;</a></span>hipMemcpyKind</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#ga232e222db36b1fc672ba98054d036a18">hipMemcpyKind</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Memory copy types </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga232e222db36b1fc672ba98054d036a18a9d66b705aa85a9c83f0f533cef70d0af" name="gga232e222db36b1fc672ba98054d036a18a9d66b705aa85a9c83f0f533cef70d0af"></a>hipMemcpyHostToHost&#160;</td><td class="fielddoc"><p>Host-to-Host Copy. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga232e222db36b1fc672ba98054d036a18aff32175ecb0c7113200286eff8211008" name="gga232e222db36b1fc672ba98054d036a18aff32175ecb0c7113200286eff8211008"></a>hipMemcpyHostToDevice&#160;</td><td class="fielddoc"><p>Host-to-Device Copy. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga232e222db36b1fc672ba98054d036a18aba2505e9ce1e5382f17730bc670917d1" name="gga232e222db36b1fc672ba98054d036a18aba2505e9ce1e5382f17730bc670917d1"></a>hipMemcpyDeviceToHost&#160;</td><td class="fielddoc"><p>Device-to-Host Copy. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga232e222db36b1fc672ba98054d036a18abd05a09d3105e0ce25b34dd91cf83f88" name="gga232e222db36b1fc672ba98054d036a18abd05a09d3105e0ce25b34dd91cf83f88"></a>hipMemcpyDeviceToDevice&#160;</td><td class="fielddoc"><p>Device-to-Device Copy. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga232e222db36b1fc672ba98054d036a18a4e37107e416f79a2edf2b6534163c823" name="gga232e222db36b1fc672ba98054d036a18a4e37107e416f79a2edf2b6534163c823"></a>hipMemcpyDefault&#160;</td><td class="fielddoc"><p>Runtime will automatically determine copy-kind based on virtual addresses. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga232e222db36b1fc672ba98054d036a18a43a2409dc0d09645418a5855ab0c0f1c" name="gga232e222db36b1fc672ba98054d036a18a43a2409dc0d09645418a5855ab0c0f1c"></a>hipMemcpyDeviceToDeviceNoCU&#160;</td><td class="fielddoc"><p>Device-to-Device Copy without using compute units. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga3298f79d98abcbdf71e53f718cdec254" name="ga3298f79d98abcbdf71e53f718cdec254"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga3298f79d98abcbdf71e53f718cdec254">&#9670;&#160;</a></span>hipMemcpySrcAccessOrder</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#ga3298f79d98abcbdf71e53f718cdec254">hipMemcpySrcAccessOrder</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Flags to specify order in which source pointer is accessed by Batch memcpy </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga3298f79d98abcbdf71e53f718cdec254a7fb93c9ebb930b4a87f0d199a5c61627" name="gga3298f79d98abcbdf71e53f718cdec254a7fb93c9ebb930b4a87f0d199a5c61627"></a>hipMemcpySrcAccessOrderInvalid&#160;</td><td class="fielddoc"><p>Default Invalid. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga3298f79d98abcbdf71e53f718cdec254ae7af12ad5ca4a82f1f2baad3adfcf3f7" name="gga3298f79d98abcbdf71e53f718cdec254ae7af12ad5ca4a82f1f2baad3adfcf3f7"></a>hipMemcpySrcAccessOrderStream&#160;</td><td class="fielddoc"><p>Access to source pointer must be in stream order. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga3298f79d98abcbdf71e53f718cdec254a9e2fc56667605febb5f6245866534b2f" name="gga3298f79d98abcbdf71e53f718cdec254a9e2fc56667605febb5f6245866534b2f"></a>hipMemcpySrcAccessOrderDuringApiCall&#160;</td><td class="fielddoc"><p>Access to source pointer can be out of stream order and all accesses must be complete before API call returns. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga3298f79d98abcbdf71e53f718cdec254ad10477ca5a7a85d28731ff3565a234e2" name="gga3298f79d98abcbdf71e53f718cdec254ad10477ca5a7a85d28731ff3565a234e2"></a>hipMemcpySrcAccessOrderAny&#160;</td><td class="fielddoc"><p>Access to the source pointer can be out of stream order and the accesses can happen even after the API call return. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga3298f79d98abcbdf71e53f718cdec254a958bb9acf191ab6c24e65901bd7515f4" name="gga3298f79d98abcbdf71e53f718cdec254a958bb9acf191ab6c24e65901bd7515f4"></a>hipMemcpySrcAccessOrderMax&#160;</td><td class="fielddoc"></td></tr>
</table>

</div>
</div>
<a id="gaee88a54f9376456dcabf3fdcf9b9810f" name="gaee88a54f9376456dcabf3fdcf9b9810f"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaee88a54f9376456dcabf3fdcf9b9810f">&#9670;&#160;</a></span>hipMemLocationType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#gaee88a54f9376456dcabf3fdcf9b9810f">hipMemLocationType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>Specifies the type of location </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggaee88a54f9376456dcabf3fdcf9b9810fa5403e1e0771ce147fc29edfb2c3e84a3" name="ggaee88a54f9376456dcabf3fdcf9b9810fa5403e1e0771ce147fc29edfb2c3e84a3"></a>hipMemLocationTypeInvalid&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="ggaee88a54f9376456dcabf3fdcf9b9810fa895e0e72b22e15f6e5808b034587a1ae" name="ggaee88a54f9376456dcabf3fdcf9b9810fa895e0e72b22e15f6e5808b034587a1ae"></a>hipMemLocationTypeNone&#160;</td><td class="fielddoc"></td></tr>
<tr><td class="fieldname"><a id="ggaee88a54f9376456dcabf3fdcf9b9810fa7dd18d5d22a3ab95b64f2daa8e3b33de" name="ggaee88a54f9376456dcabf3fdcf9b9810fa7dd18d5d22a3ab95b64f2daa8e3b33de"></a>hipMemLocationTypeDevice&#160;</td><td class="fielddoc"><p>Device location, thus it's HIP device ID. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaee88a54f9376456dcabf3fdcf9b9810fa5fc26b0761e2a06ded14048ea9f2cdd3" name="ggaee88a54f9376456dcabf3fdcf9b9810fa5fc26b0761e2a06ded14048ea9f2cdd3"></a>hipMemLocationTypeHost&#160;</td><td class="fielddoc"><p>Host location, id is ignored. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaee88a54f9376456dcabf3fdcf9b9810fa3ccc587f519942cbbdb869e205054e5e" name="ggaee88a54f9376456dcabf3fdcf9b9810fa3ccc587f519942cbbdb869e205054e5e"></a>hipMemLocationTypeHostNuma&#160;</td><td class="fielddoc"><p>Host NUMA node location, id is host NUMA node id. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaee88a54f9376456dcabf3fdcf9b9810fa2ea10c636002fc4f4a817fbdeaeb4c0a" name="ggaee88a54f9376456dcabf3fdcf9b9810fa2ea10c636002fc4f4a817fbdeaeb4c0a"></a>hipMemLocationTypeHostNumaCurrent&#160;</td><td class="fielddoc"><p>Host NUMA node closest to current thread’s CPU, id is ignored. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga44f13516fbfca2d20cc2594b7f633cf1" name="ga44f13516fbfca2d20cc2594b7f633cf1"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga44f13516fbfca2d20cc2594b7f633cf1">&#9670;&#160;</a></span>hipPointer_attribute</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#ga44f13516fbfca2d20cc2594b7f633cf1">hipPointer_attribute</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1a351f4be735a13e2788c0c74abf7cb0e0" name="gga44f13516fbfca2d20cc2594b7f633cf1a351f4be735a13e2788c0c74abf7cb0e0"></a>HIP_POINTER_ATTRIBUTE_CONTEXT&#160;</td><td class="fielddoc"><p>The context on which a pointer was allocated </p><dl class="section warning"><dt>Warning</dt><dd>This attribute is not supported in HIP </dd></dl>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1adb8735d707be3d31dd64a46271069237" name="gga44f13516fbfca2d20cc2594b7f633cf1adb8735d707be3d31dd64a46271069237"></a>HIP_POINTER_ATTRIBUTE_MEMORY_TYPE&#160;</td><td class="fielddoc"><p>memory type describing the location of a pointer </p>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1a24c68927c9881c8ffbcbb0ecc04b0a31" name="gga44f13516fbfca2d20cc2594b7f633cf1a24c68927c9881c8ffbcbb0ecc04b0a31"></a>HIP_POINTER_ATTRIBUTE_DEVICE_POINTER&#160;</td><td class="fielddoc"><p>address at which the pointer is allocated on the device </p>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1a639ebcef2880cd4cb020dfa7fecd5119" name="gga44f13516fbfca2d20cc2594b7f633cf1a639ebcef2880cd4cb020dfa7fecd5119"></a>HIP_POINTER_ATTRIBUTE_HOST_POINTER&#160;</td><td class="fielddoc"><p>address at which the pointer is allocated on the host </p>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1ab05bd233393c51d2db1dfbb7ae8d70c9" name="gga44f13516fbfca2d20cc2594b7f633cf1ab05bd233393c51d2db1dfbb7ae8d70c9"></a>HIP_POINTER_ATTRIBUTE_P2P_TOKENS&#160;</td><td class="fielddoc"><p>A pair of tokens for use with Linux kernel interface </p><dl class="section warning"><dt>Warning</dt><dd>This attribute is not supported in HIP </dd></dl>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1a9a587bd4cc33f9a58961cb5801c5489d" name="gga44f13516fbfca2d20cc2594b7f633cf1a9a587bd4cc33f9a58961cb5801c5489d"></a>HIP_POINTER_ATTRIBUTE_SYNC_MEMOPS&#160;</td><td class="fielddoc"><p>Synchronize every synchronous memory operation initiated on this region </p>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1a264f5f3d40fe591e880eaf73c37d569a" name="gga44f13516fbfca2d20cc2594b7f633cf1a264f5f3d40fe591e880eaf73c37d569a"></a>HIP_POINTER_ATTRIBUTE_BUFFER_ID&#160;</td><td class="fielddoc"><p>Unique ID for an allocated memory region. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1ad3ca9bfc093449926c90734900334fac" name="gga44f13516fbfca2d20cc2594b7f633cf1ad3ca9bfc093449926c90734900334fac"></a>HIP_POINTER_ATTRIBUTE_IS_MANAGED&#160;</td><td class="fielddoc"><p>Indicates if the pointer points to managed memory. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1a0cab1da1255a8b4d62d87d7c83806296" name="gga44f13516fbfca2d20cc2594b7f633cf1a0cab1da1255a8b4d62d87d7c83806296"></a>HIP_POINTER_ATTRIBUTE_DEVICE_ORDINAL&#160;</td><td class="fielddoc"><p>device ordinal of a device on which a pointer was allocated or registered </p>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1a15544939ec22c928e579c514293d9412" name="gga44f13516fbfca2d20cc2594b7f633cf1a15544939ec22c928e579c514293d9412"></a>HIP_POINTER_ATTRIBUTE_IS_LEGACY_HIP_IPC_CAPABLE&#160;</td><td class="fielddoc"><p>if this pointer maps to an allocation that is suitable for hipIpcGetMemHandle </p><dl class="section warning"><dt>Warning</dt><dd>This attribute is not supported in HIP </dd></dl>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1ae82b2f8de6a3238aa5d65cc40e1d0368" name="gga44f13516fbfca2d20cc2594b7f633cf1ae82b2f8de6a3238aa5d65cc40e1d0368"></a>HIP_POINTER_ATTRIBUTE_RANGE_START_ADDR&#160;</td><td class="fielddoc"><p>Starting address for this requested pointer. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1a160ddae557035db47837e507f595825e" name="gga44f13516fbfca2d20cc2594b7f633cf1a160ddae557035db47837e507f595825e"></a>HIP_POINTER_ATTRIBUTE_RANGE_SIZE&#160;</td><td class="fielddoc"><p>Size of the address range for this requested pointer. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1a2d96a7dd4e9cf031b94fc3cd1309d723" name="gga44f13516fbfca2d20cc2594b7f633cf1a2d96a7dd4e9cf031b94fc3cd1309d723"></a>HIP_POINTER_ATTRIBUTE_MAPPED&#160;</td><td class="fielddoc"><p>tells if this pointer is in a valid address range that is mapped to a backing allocation </p>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1afc43c9bb83f3b15b20e3c85e42ab1acb" name="gga44f13516fbfca2d20cc2594b7f633cf1afc43c9bb83f3b15b20e3c85e42ab1acb"></a>HIP_POINTER_ATTRIBUTE_ALLOWED_HANDLE_TYPES&#160;</td><td class="fielddoc"><p>Bitmask of allowed hipmemAllocationHandleType for this allocation </p><dl class="section warning"><dt>Warning</dt><dd>This attribute is not supported in HIP </dd></dl>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1a64ff1f6b7144501cb01c153b1ccbb51e" name="gga44f13516fbfca2d20cc2594b7f633cf1a64ff1f6b7144501cb01c153b1ccbb51e"></a>HIP_POINTER_ATTRIBUTE_IS_GPU_DIRECT_RDMA_CAPABLE&#160;</td><td class="fielddoc"><p>returns if the memory referenced by this pointer can be used with the GPUDirect RDMA API </p><dl class="section warning"><dt>Warning</dt><dd>This attribute is not supported in HIP </dd></dl>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1ac81cd9e2ec4fed70a14a0576ff18cc05" name="gga44f13516fbfca2d20cc2594b7f633cf1ac81cd9e2ec4fed70a14a0576ff18cc05"></a>HIP_POINTER_ATTRIBUTE_ACCESS_FLAGS&#160;</td><td class="fielddoc"><p>Returns the access flags the device associated with for the corresponding memory referenced by the ptr </p>
</td></tr>
<tr><td class="fieldname"><a id="gga44f13516fbfca2d20cc2594b7f633cf1a337d6dd0cdfad646bb635cafcb78c44c" name="gga44f13516fbfca2d20cc2594b7f633cf1a337d6dd0cdfad646bb635cafcb78c44c"></a>HIP_POINTER_ATTRIBUTE_MEMPOOL_HANDLE&#160;</td><td class="fielddoc"><p>Returns the mempool handle for the allocation if it was allocated from a mempool </p><dl class="section warning"><dt>Warning</dt><dd>This attribute is not supported in HIP </dd></dl>
</td></tr>
</table>

</div>
</div>
<a id="gac4a2d283d15bd706ec2fce745e5cf7ac" name="gac4a2d283d15bd706ec2fce745e5cf7ac"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gac4a2d283d15bd706ec2fce745e5cf7ac">&#9670;&#160;</a></span>hipResourceType</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#gac4a2d283d15bd706ec2fce745e5cf7ac">hipResourceType</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP resource types </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggac4a2d283d15bd706ec2fce745e5cf7aca0589eb56f5887c95e50c97bb3afd618c" name="ggac4a2d283d15bd706ec2fce745e5cf7aca0589eb56f5887c95e50c97bb3afd618c"></a>hipResourceTypeArray&#160;</td><td class="fielddoc"><p>Array resource. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac4a2d283d15bd706ec2fce745e5cf7aca67c0cdae37af35df9a56c09a2ec806a9" name="ggac4a2d283d15bd706ec2fce745e5cf7aca67c0cdae37af35df9a56c09a2ec806a9"></a>hipResourceTypeMipmappedArray&#160;</td><td class="fielddoc"><p>Mipmapped array resource. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac4a2d283d15bd706ec2fce745e5cf7acabfbb200e565b7d76cecf8f13e3c282e5" name="ggac4a2d283d15bd706ec2fce745e5cf7acabfbb200e565b7d76cecf8f13e3c282e5"></a>hipResourceTypeLinear&#160;</td><td class="fielddoc"><p>Linear resource. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggac4a2d283d15bd706ec2fce745e5cf7acab79b496f361dd19e423382fc5aea7729" name="ggac4a2d283d15bd706ec2fce745e5cf7acab79b496f361dd19e423382fc5aea7729"></a>hipResourceTypePitch2D&#160;</td><td class="fielddoc"><p>Pitch 2D resource. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga1d01da29fc699617c37f9bcdfbffa58e" name="ga1d01da29fc699617c37f9bcdfbffa58e"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga1d01da29fc699617c37f9bcdfbffa58e">&#9670;&#160;</a></span>hipResourcetype</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#ga1d01da29fc699617c37f9bcdfbffa58e">hipResourcetype</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga1d01da29fc699617c37f9bcdfbffa58ea05b57e567f221b411deb80223a5ef77a" name="gga1d01da29fc699617c37f9bcdfbffa58ea05b57e567f221b411deb80223a5ef77a"></a>HIP_RESOURCE_TYPE_ARRAY&#160;</td><td class="fielddoc"><p>Array resource. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga1d01da29fc699617c37f9bcdfbffa58ea71a6755e1536d31217ca8401cc70e0f1" name="gga1d01da29fc699617c37f9bcdfbffa58ea71a6755e1536d31217ca8401cc70e0f1"></a>HIP_RESOURCE_TYPE_MIPMAPPED_ARRAY&#160;</td><td class="fielddoc"><p>Mipmapped array resource. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga1d01da29fc699617c37f9bcdfbffa58ea7f86a0f731402eb6a70342294dc2f216" name="gga1d01da29fc699617c37f9bcdfbffa58ea7f86a0f731402eb6a70342294dc2f216"></a>HIP_RESOURCE_TYPE_LINEAR&#160;</td><td class="fielddoc"><p>Linear resource. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga1d01da29fc699617c37f9bcdfbffa58ea1eb726cd957c3e446a2425d58875e456" name="gga1d01da29fc699617c37f9bcdfbffa58ea1eb726cd957c3e446a2425d58875e456"></a>HIP_RESOURCE_TYPE_PITCH2D&#160;</td><td class="fielddoc"><p>Pitch 2D resource. </p>
</td></tr>
</table>

</div>
</div>
<a id="gaa0ce0df88178c3157b1a56ae9adb96ce" name="gaa0ce0df88178c3157b1a56ae9adb96ce"></a>
<h2 class="memtitle"><span class="permalink"><a href="#gaa0ce0df88178c3157b1a56ae9adb96ce">&#9670;&#160;</a></span>hipResourceViewFormat</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#gaa0ce0df88178c3157b1a56ae9adb96ce">hipResourceViewFormat</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP texture resource view formats </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea2063974b7c63fe5cc30608eee63c7614" name="ggaa0ce0df88178c3157b1a56ae9adb96cea2063974b7c63fe5cc30608eee63c7614"></a>hipResViewFormatNone&#160;</td><td class="fielddoc"><p>No resource view format (use underlying resource format) </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceae24b50913e9a821ec8f8c577d047bb75" name="ggaa0ce0df88178c3157b1a56ae9adb96ceae24b50913e9a821ec8f8c577d047bb75"></a>hipResViewFormatUnsignedChar1&#160;</td><td class="fielddoc"><p>1 channel, unsigned 8-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea2638d20534e10404e014f99b447603bd" name="ggaa0ce0df88178c3157b1a56ae9adb96cea2638d20534e10404e014f99b447603bd"></a>hipResViewFormatUnsignedChar2&#160;</td><td class="fielddoc"><p>2 channels, unsigned 8-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea77ca99a2f486070fe859d714d3b62a57" name="ggaa0ce0df88178c3157b1a56ae9adb96cea77ca99a2f486070fe859d714d3b62a57"></a>hipResViewFormatUnsignedChar4&#160;</td><td class="fielddoc"><p>4 channels, unsigned 8-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceae3d8d4b36e2c4a25de5208513fbf751b" name="ggaa0ce0df88178c3157b1a56ae9adb96ceae3d8d4b36e2c4a25de5208513fbf751b"></a>hipResViewFormatSignedChar1&#160;</td><td class="fielddoc"><p>1 channel, signed 8-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceabce1650eb85d3ef6db11513caaaf08be" name="ggaa0ce0df88178c3157b1a56ae9adb96ceabce1650eb85d3ef6db11513caaaf08be"></a>hipResViewFormatSignedChar2&#160;</td><td class="fielddoc"><p>2 channels, signed 8-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea041b834a894dd458994afd3fb17f2dcf" name="ggaa0ce0df88178c3157b1a56ae9adb96cea041b834a894dd458994afd3fb17f2dcf"></a>hipResViewFormatSignedChar4&#160;</td><td class="fielddoc"><p>4 channels, signed 8-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceab1ec6b2b7587f5a7505df1518bc4e2cf" name="ggaa0ce0df88178c3157b1a56ae9adb96ceab1ec6b2b7587f5a7505df1518bc4e2cf"></a>hipResViewFormatUnsignedShort1&#160;</td><td class="fielddoc"><p>1 channel, unsigned 16-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceaf1f818268859b5db38129200e9c1535a" name="ggaa0ce0df88178c3157b1a56ae9adb96ceaf1f818268859b5db38129200e9c1535a"></a>hipResViewFormatUnsignedShort2&#160;</td><td class="fielddoc"><p>2 channels, unsigned 16-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceafb6ec538c67bcd6944a682263b7a6b39" name="ggaa0ce0df88178c3157b1a56ae9adb96ceafb6ec538c67bcd6944a682263b7a6b39"></a>hipResViewFormatUnsignedShort4&#160;</td><td class="fielddoc"><p>4 channels, unsigned 16-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceaeebafd1f78ec8590ff32a81a1268f0e5" name="ggaa0ce0df88178c3157b1a56ae9adb96ceaeebafd1f78ec8590ff32a81a1268f0e5"></a>hipResViewFormatSignedShort1&#160;</td><td class="fielddoc"><p>1 channel, signed 16-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea55ccc4ec1afb1a023aeed517cffaccc2" name="ggaa0ce0df88178c3157b1a56ae9adb96cea55ccc4ec1afb1a023aeed517cffaccc2"></a>hipResViewFormatSignedShort2&#160;</td><td class="fielddoc"><p>2 channels, signed 16-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea37a0212e13a615f6a972834d661c5edb" name="ggaa0ce0df88178c3157b1a56ae9adb96cea37a0212e13a615f6a972834d661c5edb"></a>hipResViewFormatSignedShort4&#160;</td><td class="fielddoc"><p>4 channels, signed 16-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea74327a9fbc40fad62352d54248a106fb" name="ggaa0ce0df88178c3157b1a56ae9adb96cea74327a9fbc40fad62352d54248a106fb"></a>hipResViewFormatUnsignedInt1&#160;</td><td class="fielddoc"><p>1 channel, unsigned 32-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea4cd9e01ef72096fdd9c1f844b879ed95" name="ggaa0ce0df88178c3157b1a56ae9adb96cea4cd9e01ef72096fdd9c1f844b879ed95"></a>hipResViewFormatUnsignedInt2&#160;</td><td class="fielddoc"><p>2 channels, unsigned 32-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea7c253bb1e7c25cd51a9bcbe8a88106ab" name="ggaa0ce0df88178c3157b1a56ae9adb96cea7c253bb1e7c25cd51a9bcbe8a88106ab"></a>hipResViewFormatUnsignedInt4&#160;</td><td class="fielddoc"><p>4 channels, unsigned 32-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceafe8ce539aced89efc110cbd0f862bfa9" name="ggaa0ce0df88178c3157b1a56ae9adb96ceafe8ce539aced89efc110cbd0f862bfa9"></a>hipResViewFormatSignedInt1&#160;</td><td class="fielddoc"><p>1 channel, signed 32-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea03a89ff79e27e25450d2c02cbca60412" name="ggaa0ce0df88178c3157b1a56ae9adb96cea03a89ff79e27e25450d2c02cbca60412"></a>hipResViewFormatSignedInt2&#160;</td><td class="fielddoc"><p>2 channels, signed 32-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea49b56a0bc812ada92ff2199f29d42698" name="ggaa0ce0df88178c3157b1a56ae9adb96cea49b56a0bc812ada92ff2199f29d42698"></a>hipResViewFormatSignedInt4&#160;</td><td class="fielddoc"><p>4 channels, signed 32-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceab5d4e7c0bb19afd3e2c1b7006fa6bc43" name="ggaa0ce0df88178c3157b1a56ae9adb96ceab5d4e7c0bb19afd3e2c1b7006fa6bc43"></a>hipResViewFormatHalf1&#160;</td><td class="fielddoc"><p>1 channel, 16-bit floating point </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceaad2ea80ee12541c78c8c14a020406233" name="ggaa0ce0df88178c3157b1a56ae9adb96ceaad2ea80ee12541c78c8c14a020406233"></a>hipResViewFormatHalf2&#160;</td><td class="fielddoc"><p>2 channels, 16-bit floating point </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea5e59ef9588077f8b7514582bf6b4bc76" name="ggaa0ce0df88178c3157b1a56ae9adb96cea5e59ef9588077f8b7514582bf6b4bc76"></a>hipResViewFormatHalf4&#160;</td><td class="fielddoc"><p>4 channels, 16-bit floating point </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea0b724b833c3350e7fa709b8d4c1b3908" name="ggaa0ce0df88178c3157b1a56ae9adb96cea0b724b833c3350e7fa709b8d4c1b3908"></a>hipResViewFormatFloat1&#160;</td><td class="fielddoc"><p>1 channel, 32-bit floating point </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceace7ed35d1f9e472b12434ef15d622f52" name="ggaa0ce0df88178c3157b1a56ae9adb96ceace7ed35d1f9e472b12434ef15d622f52"></a>hipResViewFormatFloat2&#160;</td><td class="fielddoc"><p>2 channels, 32-bit floating point </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea63014d0f5b494259309ce97e2084828a" name="ggaa0ce0df88178c3157b1a56ae9adb96cea63014d0f5b494259309ce97e2084828a"></a>hipResViewFormatFloat4&#160;</td><td class="fielddoc"><p>4 channels, 32-bit floating point </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea72d644a4603a5f50e28219cca0dbc63a" name="ggaa0ce0df88178c3157b1a56ae9adb96cea72d644a4603a5f50e28219cca0dbc63a"></a>hipResViewFormatUnsignedBlockCompressed1&#160;</td><td class="fielddoc"><p>Block-compressed 1. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea8d3723df9d15fd0f7d948405074c4645" name="ggaa0ce0df88178c3157b1a56ae9adb96cea8d3723df9d15fd0f7d948405074c4645"></a>hipResViewFormatUnsignedBlockCompressed2&#160;</td><td class="fielddoc"><p>Block-compressed 2. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceadc93cc8950df637929fec0833091d843" name="ggaa0ce0df88178c3157b1a56ae9adb96ceadc93cc8950df637929fec0833091d843"></a>hipResViewFormatUnsignedBlockCompressed3&#160;</td><td class="fielddoc"><p>Block-compressed 3. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea37b93313fdc9e6d4345c9f62e8ffacc3" name="ggaa0ce0df88178c3157b1a56ae9adb96cea37b93313fdc9e6d4345c9f62e8ffacc3"></a>hipResViewFormatUnsignedBlockCompressed4&#160;</td><td class="fielddoc"><p>Block-compressed 4 unsigned. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceab2b2d0d8eeb42f5e0bd36742ddf5c32d" name="ggaa0ce0df88178c3157b1a56ae9adb96ceab2b2d0d8eeb42f5e0bd36742ddf5c32d"></a>hipResViewFormatSignedBlockCompressed4&#160;</td><td class="fielddoc"><p>Block-compressed 4 signed. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea2022710f743fb58bfc48b22520e95386" name="ggaa0ce0df88178c3157b1a56ae9adb96cea2022710f743fb58bfc48b22520e95386"></a>hipResViewFormatUnsignedBlockCompressed5&#160;</td><td class="fielddoc"><p>Block-compressed 5 unsigned. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceab216c662063865156e5c064ce5156991" name="ggaa0ce0df88178c3157b1a56ae9adb96ceab216c662063865156e5c064ce5156991"></a>hipResViewFormatSignedBlockCompressed5&#160;</td><td class="fielddoc"><p>Block-compressed 5 signed. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceae445c47c26608ab53a073b61b2495c84" name="ggaa0ce0df88178c3157b1a56ae9adb96ceae445c47c26608ab53a073b61b2495c84"></a>hipResViewFormatUnsignedBlockCompressed6H&#160;</td><td class="fielddoc"><p>Block-compressed 6 unsigned half-float. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96cea89fa2e14d9d41c48d01c34594728456f" name="ggaa0ce0df88178c3157b1a56ae9adb96cea89fa2e14d9d41c48d01c34594728456f"></a>hipResViewFormatSignedBlockCompressed6H&#160;</td><td class="fielddoc"><p>Block-compressed 6 signed half-float. </p>
</td></tr>
<tr><td class="fieldname"><a id="ggaa0ce0df88178c3157b1a56ae9adb96ceaecae7d40367785c319d4af27f11d1cf7" name="ggaa0ce0df88178c3157b1a56ae9adb96ceaecae7d40367785c319d4af27f11d1cf7"></a>hipResViewFormatUnsignedBlockCompressed7&#160;</td><td class="fielddoc"><p>Block-compressed 7. </p>
</td></tr>
</table>

</div>
</div>
<a id="ga38e942dc4952156f08c4ba5232f20ec9" name="ga38e942dc4952156f08c4ba5232f20ec9"></a>
<h2 class="memtitle"><span class="permalink"><a href="#ga38e942dc4952156f08c4ba5232f20ec9">&#9670;&#160;</a></span>HIPresourceViewFormat</h2>

<div class="memitem">
<div class="memproto">
      <table class="memname">
        <tr>
          <td class="memname">enum <a class="el" href="group___driver_types.html#ga38e942dc4952156f08c4ba5232f20ec9">HIPresourceViewFormat</a></td>
        </tr>
      </table>
</div><div class="memdoc">
<p>HIP texture resource view formats </p>
<table class="fieldtable">
<tr><th colspan="2">Enumerator</th></tr><tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a5577990d7926d3534c6cded3558d9721" name="gga38e942dc4952156f08c4ba5232f20ec9a5577990d7926d3534c6cded3558d9721"></a>HIP_RES_VIEW_FORMAT_NONE&#160;</td><td class="fielddoc"><p>No resource view format (use underlying resource format) </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a130866b96a283c9ae7ed888e8b409bf2" name="gga38e942dc4952156f08c4ba5232f20ec9a130866b96a283c9ae7ed888e8b409bf2"></a>HIP_RES_VIEW_FORMAT_UINT_1X8&#160;</td><td class="fielddoc"><p>1 channel, unsigned 8-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a42934e6b68903f070cee9de0cefb1618" name="gga38e942dc4952156f08c4ba5232f20ec9a42934e6b68903f070cee9de0cefb1618"></a>HIP_RES_VIEW_FORMAT_UINT_2X8&#160;</td><td class="fielddoc"><p>2 channels, unsigned 8-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a4d00bad266d3b744bcfb9aca03ad5371" name="gga38e942dc4952156f08c4ba5232f20ec9a4d00bad266d3b744bcfb9aca03ad5371"></a>HIP_RES_VIEW_FORMAT_UINT_4X8&#160;</td><td class="fielddoc"><p>4 channels, unsigned 8-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a971f037b327889d81aec1d4471e5747e" name="gga38e942dc4952156f08c4ba5232f20ec9a971f037b327889d81aec1d4471e5747e"></a>HIP_RES_VIEW_FORMAT_SINT_1X8&#160;</td><td class="fielddoc"><p>1 channel, signed 8-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a335a6b14bb95049d62a22c636062dfe9" name="gga38e942dc4952156f08c4ba5232f20ec9a335a6b14bb95049d62a22c636062dfe9"></a>HIP_RES_VIEW_FORMAT_SINT_2X8&#160;</td><td class="fielddoc"><p>2 channels, signed 8-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a6a07d1b58e83f112e51577a71db4064e" name="gga38e942dc4952156f08c4ba5232f20ec9a6a07d1b58e83f112e51577a71db4064e"></a>HIP_RES_VIEW_FORMAT_SINT_4X8&#160;</td><td class="fielddoc"><p>4 channels, signed 8-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a1ff8d7bd5c9283225b5f1491422821f5" name="gga38e942dc4952156f08c4ba5232f20ec9a1ff8d7bd5c9283225b5f1491422821f5"></a>HIP_RES_VIEW_FORMAT_UINT_1X16&#160;</td><td class="fielddoc"><p>1 channel, unsigned 16-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a2550a8c0d339d4340d59c75b568fbef6" name="gga38e942dc4952156f08c4ba5232f20ec9a2550a8c0d339d4340d59c75b568fbef6"></a>HIP_RES_VIEW_FORMAT_UINT_2X16&#160;</td><td class="fielddoc"><p>2 channels, unsigned 16-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a889f1abd7fbbecad885ffe99e09377a7" name="gga38e942dc4952156f08c4ba5232f20ec9a889f1abd7fbbecad885ffe99e09377a7"></a>HIP_RES_VIEW_FORMAT_UINT_4X16&#160;</td><td class="fielddoc"><p>4 channels, unsigned 16-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9aaf61ce87edb24595b7087aa5392676c2" name="gga38e942dc4952156f08c4ba5232f20ec9aaf61ce87edb24595b7087aa5392676c2"></a>HIP_RES_VIEW_FORMAT_SINT_1X16&#160;</td><td class="fielddoc"><p>1 channel, signed 16-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a292aee6051c9e3fb35d7e90df84bc5db" name="gga38e942dc4952156f08c4ba5232f20ec9a292aee6051c9e3fb35d7e90df84bc5db"></a>HIP_RES_VIEW_FORMAT_SINT_2X16&#160;</td><td class="fielddoc"><p>2 channels, signed 16-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a3b002e409a851bf3010339887b51ec4c" name="gga38e942dc4952156f08c4ba5232f20ec9a3b002e409a851bf3010339887b51ec4c"></a>HIP_RES_VIEW_FORMAT_SINT_4X16&#160;</td><td class="fielddoc"><p>4 channels, signed 16-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a1c1c947c4444f9b5c064e2642a08d5ee" name="gga38e942dc4952156f08c4ba5232f20ec9a1c1c947c4444f9b5c064e2642a08d5ee"></a>HIP_RES_VIEW_FORMAT_UINT_1X32&#160;</td><td class="fielddoc"><p>1 channel, unsigned 32-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9ad9209dc87b0b30f348715ec8c3b6bc6e" name="gga38e942dc4952156f08c4ba5232f20ec9ad9209dc87b0b30f348715ec8c3b6bc6e"></a>HIP_RES_VIEW_FORMAT_UINT_2X32&#160;</td><td class="fielddoc"><p>2 channels, unsigned 32-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9ac3cad7107de9afe19a83e1c92ec7d071" name="gga38e942dc4952156f08c4ba5232f20ec9ac3cad7107de9afe19a83e1c92ec7d071"></a>HIP_RES_VIEW_FORMAT_UINT_4X32&#160;</td><td class="fielddoc"><p>4 channels, unsigned 32-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a52e0cc75079546b896608ed1fa0b2964" name="gga38e942dc4952156f08c4ba5232f20ec9a52e0cc75079546b896608ed1fa0b2964"></a>HIP_RES_VIEW_FORMAT_SINT_1X32&#160;</td><td class="fielddoc"><p>1 channel, signed 32-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a68f080c50ced45d092395ca51b0f4ff2" name="gga38e942dc4952156f08c4ba5232f20ec9a68f080c50ced45d092395ca51b0f4ff2"></a>HIP_RES_VIEW_FORMAT_SINT_2X32&#160;</td><td class="fielddoc"><p>2 channels, signed 32-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9ac8f4750cfb1a60bba7e095c30246f6af" name="gga38e942dc4952156f08c4ba5232f20ec9ac8f4750cfb1a60bba7e095c30246f6af"></a>HIP_RES_VIEW_FORMAT_SINT_4X32&#160;</td><td class="fielddoc"><p>4 channels, signed 32-bit integers </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9ac4e033ffcddac858422b7043f452926c" name="gga38e942dc4952156f08c4ba5232f20ec9ac4e033ffcddac858422b7043f452926c"></a>HIP_RES_VIEW_FORMAT_FLOAT_1X16&#160;</td><td class="fielddoc"><p>1 channel, 16-bit floating point </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9ab0b187f3471a77f1d722dde3ab9b73a7" name="gga38e942dc4952156f08c4ba5232f20ec9ab0b187f3471a77f1d722dde3ab9b73a7"></a>HIP_RES_VIEW_FORMAT_FLOAT_2X16&#160;</td><td class="fielddoc"><p>2 channels, 16-bit floating point </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a8a61a8e88f7f76830071987d19f21ae5" name="gga38e942dc4952156f08c4ba5232f20ec9a8a61a8e88f7f76830071987d19f21ae5"></a>HIP_RES_VIEW_FORMAT_FLOAT_4X16&#160;</td><td class="fielddoc"><p>4 channels, 16-bit floating point </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9af59a8dec7304f4d8261d4a3603595098" name="gga38e942dc4952156f08c4ba5232f20ec9af59a8dec7304f4d8261d4a3603595098"></a>HIP_RES_VIEW_FORMAT_FLOAT_1X32&#160;</td><td class="fielddoc"><p>1 channel, 32-bit floating point </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9aa0df1d7cf39a6b3d488b43565d6fa1ee" name="gga38e942dc4952156f08c4ba5232f20ec9aa0df1d7cf39a6b3d488b43565d6fa1ee"></a>HIP_RES_VIEW_FORMAT_FLOAT_2X32&#160;</td><td class="fielddoc"><p>2 channels, 32-bit floating point </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a180b648c21563572942b2448840a5c2e" name="gga38e942dc4952156f08c4ba5232f20ec9a180b648c21563572942b2448840a5c2e"></a>HIP_RES_VIEW_FORMAT_FLOAT_4X32&#160;</td><td class="fielddoc"><p>4 channels, 32-bit floating point </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a0e4452d2d91fb43fcdc3aa265478a171" name="gga38e942dc4952156f08c4ba5232f20ec9a0e4452d2d91fb43fcdc3aa265478a171"></a>HIP_RES_VIEW_FORMAT_UNSIGNED_BC1&#160;</td><td class="fielddoc"><p>Block-compressed 1. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9afb4fbc1ed1ef7c5965c9a5d80a50a0bb" name="gga38e942dc4952156f08c4ba5232f20ec9afb4fbc1ed1ef7c5965c9a5d80a50a0bb"></a>HIP_RES_VIEW_FORMAT_UNSIGNED_BC2&#160;</td><td class="fielddoc"><p>Block-compressed 2. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9ae01c8d3950c053eef6a0ada98901ad72" name="gga38e942dc4952156f08c4ba5232f20ec9ae01c8d3950c053eef6a0ada98901ad72"></a>HIP_RES_VIEW_FORMAT_UNSIGNED_BC3&#160;</td><td class="fielddoc"><p>Block-compressed 3. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a87572f3856c0b8efe1ec2472a3bae8e7" name="gga38e942dc4952156f08c4ba5232f20ec9a87572f3856c0b8efe1ec2472a3bae8e7"></a>HIP_RES_VIEW_FORMAT_UNSIGNED_BC4&#160;</td><td class="fielddoc"><p>Block-compressed 4 unsigned. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a6bcabc7788897c6ec43942f5bdc951ef" name="gga38e942dc4952156f08c4ba5232f20ec9a6bcabc7788897c6ec43942f5bdc951ef"></a>HIP_RES_VIEW_FORMAT_SIGNED_BC4&#160;</td><td class="fielddoc"><p>Block-compressed 4 signed. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9abe53bcc8a9b200c3e4ceb1f758f79a7d" name="gga38e942dc4952156f08c4ba5232f20ec9abe53bcc8a9b200c3e4ceb1f758f79a7d"></a>HIP_RES_VIEW_FORMAT_UNSIGNED_BC5&#160;</td><td class="fielddoc"><p>Block-compressed 5 unsigned. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a972c526013a903d0bbf321231de69a06" name="gga38e942dc4952156f08c4ba5232f20ec9a972c526013a903d0bbf321231de69a06"></a>HIP_RES_VIEW_FORMAT_SIGNED_BC5&#160;</td><td class="fielddoc"><p>Block-compressed 5 signed. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a3a69f57d94eacd6d4dfe618b27e17ab7" name="gga38e942dc4952156f08c4ba5232f20ec9a3a69f57d94eacd6d4dfe618b27e17ab7"></a>HIP_RES_VIEW_FORMAT_UNSIGNED_BC6H&#160;</td><td class="fielddoc"><p>Block-compressed 6 unsigned half-float. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a7a951a5566a5e075566f3f4ed4b1a491" name="gga38e942dc4952156f08c4ba5232f20ec9a7a951a5566a5e075566f3f4ed4b1a491"></a>HIP_RES_VIEW_FORMAT_SIGNED_BC6H&#160;</td><td class="fielddoc"><p>Block-compressed 6 signed half-float. </p>
</td></tr>
<tr><td class="fieldname"><a id="gga38e942dc4952156f08c4ba5232f20ec9a707b7c4445769c7a33929f284c92e088" name="gga38e942dc4952156f08c4ba5232f20ec9a707b7c4445769c7a33929f284c92e088"></a>HIP_RES_VIEW_FORMAT_UNSIGNED_BC7&#160;</td><td class="fielddoc"><p>Block-compressed 7. </p>
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
       href="group___global_defs.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Global enum and defines</p>
      </div>
    </a>
    <a class="right-next"
       href="annotated.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Data Structures</p>
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
