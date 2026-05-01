---
title: "Atomic operations: Histogram tutorial &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/programming-patterns/atomic_operations_histogram.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:12.055962+00:00
content_hash: "e0e5c8c64a3906f0"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="HIP atomic operations histogram tutorial" name="description" />
<meta content="AMD, ROCm, HIP, atomic operations, GPU programming, histogram, synchronization primitives" name="keywords" />

    <title>Atomic operations: Histogram tutorial &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>window.MathJax = {"options": {"processHtmlClass": "tex2jax_process|mathjax_process|math|output_area"}}</script>
    <script defer="defer" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'tutorial/programming-patterns/atomic_operations_histogram';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="CPU-GPU cooperative computing: K-means clustering tutorial" href="cpu_gpu_kmeans.html" />
    <link rel="prev" title="Two-dimensional kernels: Matrix multiplication tutorial" href="matrix_multiplication.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/tutorial/programming-patterns/atomic_operations_histogram.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../../reference/hip_runtime_api_reference.html">HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
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
<li class="toctree-l2 has-children"><a class="reference internal" href="../../reference/hip_runtime_api/global_defines_enums_structs_files.html">Global defines, enums, structs and files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../doxygen/html/group___global_defs.html">Global enum and defines</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../doxygen/html/group___driver_types.html">Driver Types</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../doxygen/html/annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../doxygen/html/files.html">File List</a></li>
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
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic">HIP basic examples</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples">HIP examples</a></li>
<li class="toctree-l1"><a class="reference internal" href="../saxpy.html">SAXPY - Hello, HIP</a></li>
<li class="toctree-l1 current active has-children"><a class="reference internal" href="../programming-patterns.html">GPU programming patterns</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2"><a class="reference internal" href="matrix_multiplication.html">Two-dimensional kernels: Matrix multiplication tutorial</a></li>
<li class="toctree-l2 current active"><a class="current reference internal" href="#">Atomic operations: Histogram tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="cpu_gpu_kmeans.html">CPU-GPU cooperative computing: K-means clustering tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="stencil_operations.html">Stencil operations: Image convolution tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="multikernel_bfs.html">Multi-kernel programming: breadth-first search tutorial</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../reduction.html">Reduction</a></li>
<li class="toctree-l1"><a class="reference internal" href="../cooperative_groups_tutorial.html">Cooperative groups</a></li>
<li class="toctree-l1"><a class="reference internal" href="../graph_api.html">HIP Graph API Tutorial</a></li>
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
    
    <li class="breadcrumb-item"><a href="../programming-patterns.html" class="nav-link">GPU programming patterns</a></li>
    
    <li class="breadcrumb-item active" aria-current="page">Atomic...</li>
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
    <h1>Atomic operations: Histogram tutorial</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#prerequisites">Prerequisites</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#race-condition">Race condition</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#histogram">Histogram</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#the-challenge-in-parallel-context">The Challenge in parallel context</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#atomic-operations">Atomic operations</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#mechanics">Mechanics</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#atomic-functions">Atomic functions</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#image-brightness-histogram">Image brightness histogram</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-implementation">Kernel implementation</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#thread-identification">Thread identification</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#brightness-computation">Brightness computation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#safe-histogram-update">Safe histogram update</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#performance-characteristics">Performance characteristics</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#benefits">Benefits</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#limitations">Limitations</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#best-practices">Best practices</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#conclusion">Conclusion</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="atomic-operations-histogram-tutorial">
<h1>Atomic operations: Histogram tutorial<a class="headerlink" href="#atomic-operations-histogram-tutorial" title="Link to this heading">#</a></h1>
<p>In GPU programming, a core design principle is to <strong>avoid simultaneous writes to
the same memory address by multiple threads</strong>. When multiple threads write to
the same location without proper synchronization, this creates a
<strong>race condition</strong>, where the final result depends on unpredictable thread
execution order.</p>
<p>Unlike CPUs, GPUs are designed for high-throughput parallel execution with
relaxed memory consistency models and limited cache coherence mechanisms. This
architectural choice maximizes bandwidth and scalability but introduces
challenges when multiple threads need to safely update shared state.</p>
<p>This tutorial demonstrates how to safely handle <strong>concurrent memory updates</strong>
using <strong>atomic operations</strong>, illustrated through the practical example of
computing an image brightness histogram on the GPU.</p>
<section id="prerequisites">
<h2>Prerequisites<a class="headerlink" href="#prerequisites" title="Link to this heading">#</a></h2>
<p>To follow this tutorial, you’ll need installed drivers and a HIP compiler
toolchain to compile your code. HIP supports compiling and running on Linux and
Windows with AMD GPUs, the combination of install instructions is more than
worth covering as part of this tutorial. For more information about installing
HIP development packages, see <a class="reference internal" href="../../install/install.html"><span class="doc">Install HIP</span></a>.</p>
</section>
<section id="race-condition">
<h2>Race condition<a class="headerlink" href="#race-condition" title="Link to this heading">#</a></h2>
<p>A <strong>race condition</strong> occurs when two or more threads attempt to
read-modify-write the same memory location concurrently without proper
synchronization. Because GPU threads execute asynchronously across multiple
cores (compute units), concurrent writes can interleave unpredictably,
leading to incorrect results.</p>
<p>For example, if two threads simultaneously attempt:</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="n">histogram</span><span class="p">[</span><span class="n">bin</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">histogram</span><span class="p">[</span><span class="n">bin</span><span class="p">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
</pre></div>
</div>
<p>both may read the same old value before either writes back,
resulting in only one increment being reflected. This results in <strong>lost updates</strong>
and <strong>nondeterministic output</strong>, which must be avoided.</p>
</section>
<section id="histogram">
<h2>Histogram<a class="headerlink" href="#histogram" title="Link to this heading">#</a></h2>
<p>A <strong>histogram</strong> partitions continuous data into discrete intervals called
<strong>bins</strong> and counts how many data points fall into each bin. In image processing,
a histogram typically represents the <strong>distribution of pixel intensities</strong> for
example brightness or color channel values.</p>
<p>The histogram algorithm can be expressed as:</p>
<div class="math notranslate nohighlight">
\[H[b] = \sum_{i=1}^{N} \delta(b - \lfloor f(x_i) \rfloor)\]</div>
<p>where <span class="math notranslate nohighlight">\(f(x_i)\)</span> maps each data value to its corresponding bin index
<span class="math notranslate nohighlight">\(b\)</span>, and <span class="math notranslate nohighlight">\(\delta()\)</span> is 1 when the value belongs to bin <span class="math notranslate nohighlight">\(b\)</span> and
0 otherwise.</p>
<p>The basic computational steps are:</p>
<ol class="arabic simple">
<li><p>Iterate through all pixels (or data points).</p></li>
<li><p>Determine the appropriate bin for each value.</p></li>
<li><p>Increment that bin’s count.</p></li>
</ol>
<p>In a serial CPU program, this is straightforward. On a GPU, thousands of threads
may attempt to increment the same bin concurrently, leading to <strong>race
conditions</strong> unless atomic synchronization is used.</p>
<section id="the-challenge-in-parallel-context">
<h3>The Challenge in parallel context<a class="headerlink" href="#the-challenge-in-parallel-context" title="Link to this heading">#</a></h3>
<p>When multiple threads attempt to increment the same bin:</p>
<ul class="simple">
<li><p>One thread’s update can overwrite another’s pending increment.</p></li>
<li><p>Memory coherence cannot guarantee ordered visibility across thread blocks.</p></li>
<li><p>The final result may be inconsistent or incorrect.</p></li>
</ul>
<p>This necessitates synchronization mechanisms to ensure that updates occur in a
<strong>mutually exclusive</strong> manner without introducing high overhead.</p>
</section>
</section>
<section id="atomic-operations">
<h2>Atomic operations<a class="headerlink" href="#atomic-operations" title="Link to this heading">#</a></h2>
<p>An <strong>atomic operation</strong> ensures that a compound operation — typically a
read-modify-write sequence — executes as an <strong>indivisible unit</strong>. From the
programmer’s perspective, atomicity guarantees that no other thread can observe
a partially completed operation.</p>
<p>Formally, an operation <span class="math notranslate nohighlight">\(O(x)\)</span> on shared variable <span class="math notranslate nohighlight">\(x\)</span> is <strong>atomic</strong>
if its execution satisfies:</p>
<div class="math notranslate nohighlight">
\[\forall T_i, T_j, \text{ the effects of } O(x) \text{ appear serializable.}\]</div>
<p>That is, all threads observe results as if operations occurred in a single,
sequential order.</p>
<section id="mechanics">
<h3>Mechanics<a class="headerlink" href="#mechanics" title="Link to this heading">#</a></h3>
<p>Atomic operations on GPUs are implemented in hardware through a <strong>memory
arbitration unit</strong> that locks a cache line, performs the modification, and
releases the lock. This ensures correctness even under massive parallelism.</p>
<p>When a thread performs an atomic operation:</p>
<ol class="arabic simple">
<li><p>The target memory location is temporarily locked.</p></li>
<li><p>The value is fetched and updated.</p></li>
<li><p>The update is written back, and the lock is released.</p></li>
</ol>
<p>No other thread can modify the same memory location during this sequence.</p>
</section>
<section id="atomic-functions">
<h3>Atomic functions<a class="headerlink" href="#atomic-functions" title="Link to this heading">#</a></h3>
<p>HIP provides a wide set of atomic primitives to synchronize updates to shared
memory or global memory locations:</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 20.0%" />
<col style="width: 80.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Operation</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">atomicAdd</span></code></p></td>
<td><p>Atomically adds a value to a memory location and returns the old value.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">atomicSub</span></code></p></td>
<td><p>Atomically subtracts a value.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">atomicExch</span></code></p></td>
<td><p>Atomically exchanges values between a register and memory.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">atomicCAS</span></code></p></td>
<td><p>Performs an atomic compare-and-swap; fundamental for implementing locks.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">atomicMax</span></code> / <code class="docutils literal notranslate"><span class="pre">atomicMin</span></code></p></td>
<td><p>Updates to the maximum or minimum of two values.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">atomicInc</span></code> / <code class="docutils literal notranslate"><span class="pre">atomicDec</span></code></p></td>
<td><p>Atomically increments or decrements a counter, wrapping at a boundary.</p></td>
</tr>
</tbody>
</table>
</div>
<p>Atomic operations in kernels can operate on block scope (shared memory),
device scope (global memory), or system scope (system memory), depending on
<a class="reference external" href="https://rocm.docs.amd.com/en/latest/reference/gpu-atomics-operation.html" title="(in ROCm Documentation v7.2.2)"><span class="xref std std-doc">hardware support</span></a>.</p>
<p>For more information, please check <a class="reference internal" href="../../how-to/hip_cpp_language_extensions.html#atomic-functions"><span class="std std-ref">atomic functions</span></a>.</p>
</section>
</section>
<section id="image-brightness-histogram">
<h2>Image brightness histogram<a class="headerlink" href="#image-brightness-histogram" title="Link to this heading">#</a></h2>
<p>We will compute a histogram that captures the <strong>distribution of pixel
brightness</strong> in an RGB image. The algorithm:</p>
<ol class="arabic simple">
<li><p>Reads image data in <strong>channel-height-width</strong> format.</p></li>
<li><p>Converts RGB values to grayscale brightness.</p></li>
<li><p>Maps brightness to a histogram bin.</p></li>
<li><p>Atomically increments the corresponding bin counter.</p></li>
</ol>
<section id="kernel-implementation">
<h3>Kernel implementation<a class="headerlink" href="#kernel-implementation" title="Link to this heading">#</a></h3>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">calculateHistogram</span><span class="p">(</span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">imageData</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">histogram</span><span class="p">,</span>
<span class="w">                                   </span><span class="kt">int</span><span class="w"> </span><span class="n">width</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">height</span><span class="p">,</span>
<span class="w">                                   </span><span class="kt">int</span><span class="w"> </span><span class="n">channels</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">numBins</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">y</span><span class="p">;</span>

<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="n">width</span><span class="w"> </span><span class="o">||</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="n">height</span><span class="p">)</span>
<span class="w">        </span><span class="k">return</span><span class="p">;</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="n">y</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">width</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">x</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">channels</span><span class="p">;</span>
<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="n">brightness</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0.0f</span><span class="p">;</span>

<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">c</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">c</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">channels</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">c</span><span class="p">)</span>
<span class="w">        </span><span class="n">brightness</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">imageData</span><span class="p">[</span><span class="n">idx</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">c</span><span class="p">];</span>

<span class="w">    </span><span class="n">brightness</span><span class="w"> </span><span class="o">/=</span><span class="w"> </span><span class="n">channels</span><span class="p">;</span><span class="w"> </span><span class="c1">// Normalize to [0, 1]</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">bin</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">static_cast</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="n">brightness</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">numBins</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Atomic increment to avoid race conditions</span>
<span class="w">    </span><span class="n">atomicAdd</span><span class="p">(</span><span class="o">&amp;</span><span class="n">histogram</span><span class="p">[</span><span class="n">bin</span><span class="p">],</span><span class="w"> </span><span class="mi">1</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<section id="thread-identification">
<h4>Thread identification<a class="headerlink" href="#thread-identification" title="Link to this heading">#</a></h4>
<p>Each thread computes one pixel’s contribution using its 2D thread and block
indices:</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">y</span><span class="p">;</span>
</pre></div>
</div>
<p>This mapping provides a 1:1 correspondence between threads and pixels, making
the computation naturally parallel.</p>
</section>
<section id="brightness-computation">
<h4>Brightness computation<a class="headerlink" href="#brightness-computation" title="Link to this heading">#</a></h4>
<p>Each pixel’s brightness is computed as the arithmetic mean of its RGB channels:</p>
<div class="math notranslate nohighlight">
\[
I'(x, y) = \frac{R + G + B}{3}
\]</div><p>This value is then normalized to [0, 1] and mapped to one of <cite>numBins</cite>
histogram intervals.</p>
</section>
<section id="safe-histogram-update">
<h4>Safe histogram update<a class="headerlink" href="#safe-histogram-update" title="Link to this heading">#</a></h4>
<p>The key step is:</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="n">atomicAdd</span><span class="p">(</span><span class="o">&amp;</span><span class="n">histogram</span><span class="p">[</span><span class="n">bin</span><span class="p">],</span><span class="w"> </span><span class="mi">1</span><span class="p">);</span>
</pre></div>
</div>
<p>This ensures that even if thousands of threads map to the same bin, each
increment is serialized correctly, maintaining an accurate bin count.</p>
</section>
</section>
</section>
<section id="performance-characteristics">
<h2>Performance characteristics<a class="headerlink" href="#performance-characteristics" title="Link to this heading">#</a></h2>
<section id="benefits">
<h3>Benefits<a class="headerlink" href="#benefits" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p><strong>Correctness under parallel updates:</strong> Ensures race-free accumulation.</p></li>
<li><p><strong>Simplified synchronization:</strong> No explicit locks or barriers needed.</p></li>
<li><p><strong>Hardware-level efficiency:</strong> Implemented directly in the GPU memory
subsystem.</p></li>
</ul>
</section>
<section id="limitations">
<h3>Limitations<a class="headerlink" href="#limitations" title="Link to this heading">#</a></h3>
<p>While atomic operations guarantee correctness, they can <strong>serialize execution</strong>
when multiple threads target the same memory address. This causes contention and
reduces effective parallelism.</p>
<p>Typical performance degradation sources include:</p>
<ul class="simple">
<li><p><strong>Hot bins:</strong> When many pixels fall into a small subset of bins.</p></li>
<li><p><strong>Global memory atomics:</strong> Global memory atomics are slower than shared memory
atomics due to higher access latency.</p></li>
<li><p><strong>Warp serialization:</strong> Threads within a warp waiting for the same atomic
target serialize.</p></li>
</ul>
</section>
</section>
<section id="best-practices">
<h2>Best practices<a class="headerlink" href="#best-practices" title="Link to this heading">#</a></h2>
<ol class="arabic">
<li><p><strong>Apply atomic operations only where necessary</strong></p>
<p>Atomic instructions serialize access to a memory location and use can
diminish SIMT parallel efficiency and increase warp stalls. Restrict atomic
usage to code paths where data races cannot be eliminated through algorithmic
restructuring.</p>
</li>
<li><p><strong>Minimize contention</strong></p>
<p>High contention on a single address or a small set of addresses leads to
serialization. Distribute writes across independent memory locations.</p>
</li>
<li><p><strong>Leverage shared memory</strong></p>
<p>Use fast, low-latency shared memory to aggregate partial results within a
block before issuing a single atomic update to global memory.</p>
</li>
<li><p><strong>Validate correctness</strong></p>
<p>Validate the numerical and logical correctness of GPU kernels by comparing
against single-threaded or deterministic multi-threaded CPU baselines.</p>
</li>
<li><p><strong>Profile regularly</strong></p>
<p>GPU performance is highly sensitive to thread divergence, memory-access
patterns, and workload distribution. Regularly use profiling tools such as
<a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3.html" title="(in Rocprofiler SDK v1.1.0)"><span class="xref std std-doc">rocprofv3</span></a> or
<a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/how-to/profile/mode.html" title="(in ROCm Compute Profiler v3.4.0)"><span class="xref std std-doc">ROCm compute profiler</span></a> to
examine warp-level execution efficiency, memory-coalescing behavior,
occupancy, and atomic throughput bottlenecks.</p>
</li>
</ol>
</section>
<section id="conclusion">
<h2>Conclusion<a class="headerlink" href="#conclusion" title="Link to this heading">#</a></h2>
<p>Atomic operations provide a low-level synchronization mechanism that allows
correct and deterministic parallel updates to shared data structures. In the
histogram example, <code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">atomicAdd()</span></code> ensures that all threads safely
contribute to their corresponding bins, preventing race conditions.</p>
<p>While atomics incur some serialization overhead, they are indispensable for
algorithms that require concurrent accumulation or counting. By applying
techniques like privatization and reduction, developers can achieve both
<strong>correctness</strong> and <strong>high performance</strong> on modern GPUs.</p>
<p>Atomic operations form the foundation for more advanced synchronization
patterns, including parallel reductions, prefix sums, and graph traversal, and
are essential for developing scalable, data-parallel GPU algorithms.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="matrix_multiplication.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Two-dimensional kernels: Matrix multiplication tutorial</p>
      </div>
    </a>
    <a class="right-next"
       href="cpu_gpu_kmeans.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">CPU-GPU cooperative computing: K-means clustering tutorial</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#race-condition">Race condition</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#histogram">Histogram</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#the-challenge-in-parallel-context">The Challenge in parallel context</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#atomic-operations">Atomic operations</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#mechanics">Mechanics</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#atomic-functions">Atomic functions</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#image-brightness-histogram">Image brightness histogram</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-implementation">Kernel implementation</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#thread-identification">Thread identification</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#brightness-computation">Brightness computation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#safe-histogram-update">Safe histogram update</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#performance-characteristics">Performance characteristics</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#benefits">Benefits</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#limitations">Limitations</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#best-practices">Best practices</a></li>
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
