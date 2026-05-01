---
title: "HIP Runtime API Reference: Data Structures &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/annotated.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:20.241973+00:00
content_hash: "fd8227ddb7008468"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>HIP Runtime API Reference: Data Structures &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'doxygen/html/annotated';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="File List" href="files.html" />
    <link rel="prev" title="Driver Types" href="group___driver_types.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/annotated.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l3"><a class="reference internal" href="group___driver_types.html">Driver Types</a></li>
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Data Structures</a></li>
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
    <h1>Data Structures</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="data-structures">
<h1>Data Structures<a class="headerlink" href="#data-structures" title="Link to this heading">#</a></h1>
<div class="doxygen-content docutils container">
<!-- HTML header for doxygen 1.9.6-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US">
<head>
<meta http-equiv="Content-Type" content="text/xhtml;charset=UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=11"/>
<meta name="generator" content="Doxygen 1.9.8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>HIP Runtime API Reference: Data Structures</title>
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
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/doxygen/html/annotated.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
  <div class="headertitle"><div class="title">Data Structures</div></div>
</div><!--header-->
<div class="contents">
<div class="textblock">Here are the data structures with brief descriptions:</div><div class="directory">
<div class="levels">[detail level <span onclick="javascript:toggleLevel(1);">1</span><span onclick="javascript:toggleLevel(2);">2</span><span onclick="javascript:toggleLevel(3);">3</span>]</div><table class="directory">
<tr id="row_0_" class="even"><td class="entry"><span style="width:0px;display:inline-block;">&#160;</span><span id="arr_0_" class="arrow" onclick="toggleFolder('0_')">&#9660;</span><span class="icona"><span class="icon">N</span></span><a class="el" href="namespacecooperative__groups.html" target="_self">cooperative_groups</a></td><td class="desc"></td></tr>
<tr id="row_0_0_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span id="arr_0_0_" class="arrow" onclick="toggleFolder('0_0_')">&#9660;</span><span class="icona"><span class="icon">N</span></span><a class="el" href="namespacecooperative__groups_1_1impl.html" target="_self">impl</a></td><td class="desc"></td></tr>
<tr id="row_0_0_0_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1impl_1_1thread__block__tile__internal.html" target="_self">thread_block_tile_internal</a></td><td class="desc"></td></tr>
<tr id="row_0_0_1_" class="odd"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structcooperative__groups_1_1impl_1_1tiled__partition__internal.html" target="_self">tiled_partition_internal</a></td><td class="desc"></td></tr>
<tr id="row_0_0_2_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structcooperative__groups_1_1impl_1_1tiled__partition__internal_3_01size_00_01thread__block_01_4.html" target="_self">tiled_partition_internal&lt; size, thread_block &gt;</a></td><td class="desc"></td></tr>
<tr id="row_0_0_3_" class="odd"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structcooperative__groups_1_1impl_1_1tiled__partition__internal_3_01size_00_01thread__block__til84038521549bf31d2e74513f3af1fa36.html" target="_self">tiled_partition_internal&lt; size, thread_block_tile&lt; ParentSize, GrandParentCGTy &gt; &gt;</a></td><td class="desc"></td></tr>
<tr id="row_0_1_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1coalesced__group.html" target="_self">coalesced_group</a></td><td class="desc">The <a class="el" href="classcooperative__groups_1_1coalesced__group.html" title="The coalesced_group cooperative group type.">coalesced_group</a> cooperative group type </td></tr>
<tr id="row_0_2_" class="odd"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1grid__group.html" target="_self">grid_group</a></td><td class="desc">The grid cooperative group type </td></tr>
<tr id="row_0_3_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1multi__grid__group.html" target="_self">multi_grid_group</a></td><td class="desc">The multi-grid cooperative group type </td></tr>
<tr id="row_0_4_" class="odd"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1parent__group__info.html" target="_self">parent_group_info</a></td><td class="desc">User exposed API that captures the state of the parent group pre-partition </td></tr>
<tr id="row_0_5_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1thread__block.html" target="_self">thread_block</a></td><td class="desc">The workgroup (thread-block in CUDA terminology) cooperative group type </td></tr>
<tr id="row_0_6_" class="odd"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1thread__block__tile.html" target="_self">thread_block_tile</a></td><td class="desc">Group type - <a class="el" href="classcooperative__groups_1_1thread__block__tile.html" title="Group type - thread_block_tile.">thread_block_tile</a> </td></tr>
<tr id="row_0_7_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1thread__block__tile_3_01size_00_01void_01_4.html" target="_self">thread_block_tile&lt; size, void &gt;</a></td><td class="desc"></td></tr>
<tr id="row_0_8_" class="odd"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1thread__block__tile__base.html" target="_self">thread_block_tile_base</a></td><td class="desc"></td></tr>
<tr id="row_0_9_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1thread__block__tile__type.html" target="_self">thread_block_tile_type</a></td><td class="desc">Group type - <a class="el" href="classcooperative__groups_1_1thread__block__tile.html" title="Group type - thread_block_tile.">thread_block_tile</a> </td></tr>
<tr id="row_0_10_" class="odd"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1thread__block__tile__type_3_01tile_size_00_01void_01_4.html" target="_self">thread_block_tile_type&lt; tileSize, void &gt;</a></td><td class="desc"></td></tr>
<tr id="row_0_11_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span id="arr_0_11_" class="arrow" onclick="toggleFolder('0_11_')">&#9660;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1thread__group.html" target="_self">thread_group</a></td><td class="desc">The base type of all cooperative group types </td></tr>
<tr id="row_0_11_0_" class="odd"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structcooperative__groups_1_1thread__group_1_1__coalesced__info.html" target="_self">_coalesced_info</a></td><td class="desc"></td></tr>
<tr id="row_0_11_1_" class="even"><td class="entry"><span style="width:48px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structcooperative__groups_1_1thread__group_1_1__tiled__info.html" target="_self">_tiled_info</a></td><td class="desc"></td></tr>
<tr id="row_0_12_" class="odd"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1tile__base.html" target="_self">tile_base</a></td><td class="desc"></td></tr>
<tr id="row_0_13_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="classcooperative__groups_1_1tiled__group.html" target="_self">tiled_group</a></td><td class="desc">The <a class="el" href="classcooperative__groups_1_1tiled__group.html" title="The tiled_group cooperative group type.">tiled_group</a> cooperative group type </td></tr>
<tr id="row_1_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structdim3.html" target="_self">dim3</a></td><td class="desc"></td></tr>
<tr id="row_2_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="struct_h_i_p___a_r_r_a_y3_d___d_e_s_c_r_i_p_t_o_r.html" target="_self">HIP_ARRAY3D_DESCRIPTOR</a></td><td class="desc"></td></tr>
<tr id="row_3_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="struct_h_i_p___a_r_r_a_y___d_e_s_c_r_i_p_t_o_r.html" target="_self">HIP_ARRAY_DESCRIPTOR</a></td><td class="desc"></td></tr>
<tr id="row_4_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="struct_h_i_p___l_a_u_n_c_h___c_o_n_f_i_g.html" target="_self">HIP_LAUNCH_CONFIG</a></td><td class="desc"></td></tr>
<tr id="row_5_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip___memcpy2_d.html" target="_self">hip_Memcpy2D</a></td><td class="desc"></td></tr>
<tr id="row_6_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="struct_h_i_p___m_e_m_c_p_y3_d.html" target="_self">HIP_MEMCPY3D</a></td><td class="desc"></td></tr>
<tr id="row_7_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="struct_h_i_p___r_e_s_o_u_r_c_e___d_e_s_c.html" target="_self">HIP_RESOURCE_DESC</a></td><td class="desc"></td></tr>
<tr id="row_8_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="struct_h_i_p___r_e_s_o_u_r_c_e___v_i_e_w___d_e_s_c.html" target="_self">HIP_RESOURCE_VIEW_DESC</a></td><td class="desc"></td></tr>
<tr id="row_9_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="struct_h_i_p___t_e_x_t_u_r_e___d_e_s_c.html" target="_self">HIP_TEXTURE_DESC</a></td><td class="desc"></td></tr>
<tr id="row_10_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_access_policy_window.html" target="_self">hipAccessPolicyWindow</a></td><td class="desc"></td></tr>
<tr id="row_11_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_array_map_info.html" target="_self">hipArrayMapInfo</a></td><td class="desc"></td></tr>
<tr id="row_12_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_batch_mem_op_node_params.html" target="_self">hipBatchMemOpNodeParams</a></td><td class="desc">Structure representing node parameters for batch memory operations in HIP graphs </td></tr>
<tr id="row_13_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_channel_format_desc.html" target="_self">hipChannelFormatDesc</a></td><td class="desc"></td></tr>
<tr id="row_14_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_child_graph_node_params.html" target="_self">hipChildGraphNodeParams</a></td><td class="desc"></td></tr>
<tr id="row_15_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_device_arch__t.html" target="_self">hipDeviceArch_t</a></td><td class="desc"></td></tr>
<tr id="row_16_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_device_prop__t.html" target="_self">hipDeviceProp_t</a></td><td class="desc"></td></tr>
<tr id="row_17_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_device_prop__t_r0000.html" target="_self">hipDeviceProp_tR0000</a></td><td class="desc"></td></tr>
<tr id="row_18_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_event_record_node_params.html" target="_self">hipEventRecordNodeParams</a></td><td class="desc"></td></tr>
<tr id="row_19_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_event_wait_node_params.html" target="_self">hipEventWaitNodeParams</a></td><td class="desc"></td></tr>
<tr id="row_20_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_extent.html" target="_self">hipExtent</a></td><td class="desc"></td></tr>
<tr id="row_21_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_external_memory_buffer_desc.html" target="_self">hipExternalMemoryBufferDesc</a></td><td class="desc"></td></tr>
<tr id="row_22_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_external_memory_handle_desc.html" target="_self">hipExternalMemoryHandleDesc</a></td><td class="desc"></td></tr>
<tr id="row_23_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_external_memory_mipmapped_array_desc.html" target="_self">hipExternalMemoryMipmappedArrayDesc</a></td><td class="desc"></td></tr>
<tr id="row_24_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_external_semaphore_handle_desc.html" target="_self">hipExternalSemaphoreHandleDesc</a></td><td class="desc"></td></tr>
<tr id="row_25_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_external_semaphore_signal_node_params.html" target="_self">hipExternalSemaphoreSignalNodeParams</a></td><td class="desc"></td></tr>
<tr id="row_26_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_external_semaphore_signal_params.html" target="_self">hipExternalSemaphoreSignalParams</a></td><td class="desc"></td></tr>
<tr id="row_27_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_external_semaphore_wait_node_params.html" target="_self">hipExternalSemaphoreWaitNodeParams</a></td><td class="desc"></td></tr>
<tr id="row_28_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_external_semaphore_wait_params.html" target="_self">hipExternalSemaphoreWaitParams</a></td><td class="desc"></td></tr>
<tr id="row_29_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_func_attributes.html" target="_self">hipFuncAttributes</a></td><td class="desc"></td></tr>
<tr id="row_30_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_function_launch_params.html" target="_self">hipFunctionLaunchParams</a></td><td class="desc"></td></tr>
<tr id="row_31_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_graph_edge_data.html" target="_self">hipGraphEdgeData</a></td><td class="desc"></td></tr>
<tr id="row_32_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_graph_instantiate_params.html" target="_self">hipGraphInstantiateParams</a></td><td class="desc"></td></tr>
<tr id="row_33_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_graph_node_params.html" target="_self">hipGraphNodeParams</a></td><td class="desc"></td></tr>
<tr id="row_34_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_host_node_params.html" target="_self">hipHostNodeParams</a></td><td class="desc"></td></tr>
<tr id="row_35_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_ipc_event_handle__t.html" target="_self">hipIpcEventHandle_t</a></td><td class="desc"></td></tr>
<tr id="row_36_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_ipc_mem_handle__t.html" target="_self">hipIpcMemHandle_t</a></td><td class="desc"></td></tr>
<tr id="row_37_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_kernel_node_params.html" target="_self">hipKernelNodeParams</a></td><td class="desc"></td></tr>
<tr id="row_38_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_launch_attribute.html" target="_self">hipLaunchAttribute</a></td><td class="desc"></td></tr>
<tr id="row_39_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="unionhip_launch_attribute_value.html" target="_self">hipLaunchAttributeValue</a></td><td class="desc"></td></tr>
<tr id="row_40_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_launch_config__t.html" target="_self">hipLaunchConfig_t</a></td><td class="desc"></td></tr>
<tr id="row_41_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_launch_mem_sync_domain_map.html" target="_self">hipLaunchMemSyncDomainMap</a></td><td class="desc"></td></tr>
<tr id="row_42_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_launch_params.html" target="_self">hipLaunchParams</a></td><td class="desc"></td></tr>
<tr id="row_43_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_mem_access_desc.html" target="_self">hipMemAccessDesc</a></td><td class="desc"></td></tr>
<tr id="row_44_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_mem_allocation_prop.html" target="_self">hipMemAllocationProp</a></td><td class="desc"></td></tr>
<tr id="row_45_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_mem_alloc_node_params.html" target="_self">hipMemAllocNodeParams</a></td><td class="desc"></td></tr>
<tr id="row_46_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_memcpy3_d_batch_op.html" target="_self">hipMemcpy3DBatchOp</a></td><td class="desc"></td></tr>
<tr id="row_47_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_memcpy3_d_operand.html" target="_self">hipMemcpy3DOperand</a></td><td class="desc"></td></tr>
<tr id="row_48_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_memcpy3_d_parms.html" target="_self">hipMemcpy3DParms</a></td><td class="desc"></td></tr>
<tr id="row_49_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_memcpy3_d_peer_parms.html" target="_self">hipMemcpy3DPeerParms</a></td><td class="desc"></td></tr>
<tr id="row_50_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_memcpy_attributes.html" target="_self">hipMemcpyAttributes</a></td><td class="desc"></td></tr>
<tr id="row_51_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_memcpy_node_params.html" target="_self">hipMemcpyNodeParams</a></td><td class="desc"></td></tr>
<tr id="row_52_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_mem_free_node_params.html" target="_self">hipMemFreeNodeParams</a></td><td class="desc"></td></tr>
<tr id="row_53_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_mem_location.html" target="_self">hipMemLocation</a></td><td class="desc"></td></tr>
<tr id="row_54_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_mem_pool_props.html" target="_self">hipMemPoolProps</a></td><td class="desc"></td></tr>
<tr id="row_55_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_mem_pool_ptr_export_data.html" target="_self">hipMemPoolPtrExportData</a></td><td class="desc"></td></tr>
<tr id="row_56_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_memset_params.html" target="_self">hipMemsetParams</a></td><td class="desc"></td></tr>
<tr id="row_57_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_mipmapped_array.html" target="_self">hipMipmappedArray_t</a></td><td class="desc"></td></tr>
<tr id="row_58_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_offset3_d.html" target="_self">hipOffset3D</a></td><td class="desc"></td></tr>
<tr id="row_59_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_pitched_ptr.html" target="_self">hipPitchedPtr</a></td><td class="desc"></td></tr>
<tr id="row_60_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_pointer_attribute__t.html" target="_self">hipPointerAttribute_t</a></td><td class="desc"></td></tr>
<tr id="row_61_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_pos.html" target="_self">hipPos</a></td><td class="desc"></td></tr>
<tr id="row_62_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_resource_desc.html" target="_self">hipResourceDesc</a></td><td class="desc"></td></tr>
<tr id="row_63_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_resource_view_desc.html" target="_self">hipResourceViewDesc</a></td><td class="desc"></td></tr>
<tr id="row_64_" class="even"><td class="entry"><span style="width:0px;display:inline-block;">&#160;</span><span id="arr_64_" class="arrow" onclick="toggleFolder('64_')">&#9660;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="unionhip_stream_batch_mem_op_params.html" target="_self">hipStreamBatchMemOpParams</a></td><td class="desc">Union representing batch memory operation parameters for HIP streams </td></tr>
<tr id="row_64_0_" class="odd"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_stream_batch_mem_op_params_1_1hip_stream_mem_op_flush_remote_writes_params__t.html" target="_self">hipStreamMemOpFlushRemoteWritesParams_t</a></td><td class="desc"></td></tr>
<tr id="row_64_1_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_stream_batch_mem_op_params_1_1hip_stream_mem_op_memory_barrier_params__t.html" target="_self">hipStreamMemOpMemoryBarrierParams_t</a></td><td class="desc"></td></tr>
<tr id="row_64_2_" class="odd"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_stream_batch_mem_op_params_1_1hip_stream_mem_op_wait_value_params__t.html" target="_self">hipStreamMemOpWaitValueParams_t</a></td><td class="desc"></td></tr>
<tr id="row_64_3_" class="even"><td class="entry"><span style="width:32px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_stream_batch_mem_op_params_1_1hip_stream_mem_op_write_value_params__t.html" target="_self">hipStreamMemOpWriteValueParams_t</a></td><td class="desc"></td></tr>
<tr id="row_65_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_texture_desc.html" target="_self">hipTextureDesc</a></td><td class="desc"></td></tr>
<tr id="row_66_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structhip_u_u_i_d.html" target="_self">hipUUID</a></td><td class="desc"></td></tr>
<tr id="row_67_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structsurface_reference.html" target="_self">surfaceReference</a></td><td class="desc"></td></tr>
<tr id="row_68_" class="even"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structtexture.html" target="_self">texture</a></td><td class="desc"></td></tr>
<tr id="row_69_" class="odd"><td class="entry"><span style="width:16px;display:inline-block;">&#160;</span><span class="icona"><span class="icon">C</span></span><a class="el" href="structtexture_reference.html" target="_self">textureReference</a></td><td class="desc"></td></tr>
</table>
</div><!-- directory -->
</div><!-- contents -->
<!-- HTML footer for doxygen 1.9.6-->
<!-- start footer part -->
</div>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="group___driver_types.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Driver Types</p>
      </div>
    </a>
    <a class="right-next"
       href="files.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">File List</p>
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
