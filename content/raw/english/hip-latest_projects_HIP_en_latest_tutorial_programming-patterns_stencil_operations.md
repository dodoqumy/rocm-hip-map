---
title: "Stencil operations: Image convolution tutorial &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/programming-patterns/stencil_operations.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:08:00.455233+00:00
content_hash: "85547e909a015670"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Image convolution tutorial using HIP on AMD GPUs" name="description" />
<meta content="AMD, ROCm, HIP, stencil operations, image convolution, GPU programming, data parallelism" name="keywords" />

    <title>Stencil operations: Image convolution tutorial &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'tutorial/programming-patterns/stencil_operations';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="Multi-kernel programming: breadth-first search tutorial" href="multikernel_bfs.html" />
    <link rel="prev" title="CPU-GPU cooperative computing: K-means clustering tutorial" href="cpu_gpu_kmeans.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/tutorial/programming-patterns/stencil_operations.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l2"><a class="reference internal" href="atomic_operations_histogram.html">Atomic operations: Histogram tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="cpu_gpu_kmeans.html">CPU-GPU cooperative computing: K-means clustering tutorial</a></li>
<li class="toctree-l2 current active"><a class="current reference internal" href="#">Stencil operations: Image convolution tutorial</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">Stencil...</li>
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
    <h1>Stencil operations: Image convolution tutorial</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#prerequisites">Prerequisites</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#applications-of-stencil-operations">Applications of stencil operations</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#image-convolution">Image convolution</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#dimensionality-of-stencils">Dimensionality of stencils</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#the-smoothing-operation">The smoothing operation</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#two-dimensional-grid-architecture">Two-dimensional grid architecture</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#grid-configuration">Grid configuration</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#complete-implementation">Complete implementation</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#header-and-setup">Header and setup</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#the-convolution-kernel">The convolution kernel</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#thread-identification-in-2d">Thread identification in 2D</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#boundary-checking">Boundary checking</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#mask-application-loop">Mask application loop</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#coordinate-calculation">Coordinate calculation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#edge-handling">Edge handling</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#accumulation">Accumulation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#writing-the-result">Writing the result</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#host-code-implementation">Host code implementation</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#main-function-setup">Main function setup</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#mask-initialization">Mask initialization</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-allocation-and-data-transfer">Memory allocation and data transfer</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#grid-configuration-and-kernel-launch">Grid configuration and kernel launch</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#retrieving-results-and-cleanup">Retrieving results and cleanup</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#performance-considerations">Performance considerations</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-access-patterns">Memory access patterns</a></li>
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
                  
  <section id="stencil-operations-image-convolution-tutorial">
<h1>Stencil operations: Image convolution tutorial<a class="headerlink" href="#stencil-operations-image-convolution-tutorial" title="Link to this heading">#</a></h1>
<p>Stencil operations represent an important class of <strong>embarrassingly parallel</strong>
algorithms that are ideally suited for GPU acceleration. A stencil algorithm
iteratively updates data in an array based on a data item’s adjacent cells,
making it a fundamental technique in various computational domains.</p>
<section id="prerequisites">
<h2>Prerequisites<a class="headerlink" href="#prerequisites" title="Link to this heading">#</a></h2>
<p>To follow this tutorial, you’ll need installed drivers and a HIP compiler
toolchain to compile your code. HIP supports compiling and running on Linux and
Windows with AMD GPUs, the combination of install instructions is more than
worth covering as part of this tutorial. For more information about installing
HIP development packages, see <a class="reference internal" href="../../install/install.html"><span class="doc">Install HIP</span></a>.</p>
</section>
<section id="applications-of-stencil-operations">
<h2>Applications of stencil operations<a class="headerlink" href="#applications-of-stencil-operations" title="Link to this heading">#</a></h2>
<p>Stencil algorithms are commonly used in:</p>
<ul class="simple">
<li><p><strong>Physics simulations</strong>: Modeling heat transfer, fluid dynamics, and wave
propagation</p></li>
<li><p><strong>Partial differential equations</strong>: Numerical solutions to scientific
computing problems</p></li>
<li><p><strong>Image processing</strong>: Convolutional operations for smoothing, sharpening, and
edge detection</p></li>
<li><p><strong>Convolutional Neural Networks</strong>: A major building block in modern
deep learning</p></li>
</ul>
<p>By applying different image convolution kernels (not to be confused with GPU
kernels), these algorithms can smooth and sharpen image features and detect
edges effectively.</p>
</section>
<section id="image-convolution">
<h2>Image convolution<a class="headerlink" href="#image-convolution" title="Link to this heading">#</a></h2>
<p>An image convolution applies a small matrix (the <strong>mask</strong> or <strong>filter kernel</strong>)
to an input image. For each pixel <span class="math notranslate nohighlight">\((x, y)\)</span>, the output is computed as:</p>
<div class="math notranslate nohighlight">
\[I'(x, y) = \sum_{i=-r}^{r} \sum_{j=-r}^{r} M(i, j) \cdot I(x + i, y + j)\]</div>
<p>where <span class="math notranslate nohighlight">\(M(i, j)\)</span> is the mask coefficient, and <span class="math notranslate nohighlight">\(r\)</span> is half the mask
width (assuming a square kernel).</p>
<p>Step by step description of the equation:</p>
<ol class="arabic simple">
<li><p>Center the mask over the current pixel</p></li>
<li><p>Multiply each mask value by the corresponding image pixel</p></li>
<li><p>Sum all the products</p></li>
<li><p>Store the result as the new pixel value</p></li>
</ol>
<section id="dimensionality-of-stencils">
<h3>Dimensionality of stencils<a class="headerlink" href="#dimensionality-of-stencils" title="Link to this heading">#</a></h3>
<p>Stencil computations extend beyond 2D image grids:</p>
<ul class="simple">
<li><p><strong>1D:</strong> Signal filtering, time series processing</p></li>
<li><p><strong>2D:</strong> Image processing, texture analysis</p></li>
<li><p><strong>3D:</strong> Volume data, fluid flow, and physical field simulation</p></li>
</ul>
<p>This tutorial focuses on <strong>2D image convolution</strong>, the most common stencil
operation in visual and scientific computing.</p>
</section>
<section id="the-smoothing-operation">
<h3>The smoothing operation<a class="headerlink" href="#the-smoothing-operation" title="Link to this heading">#</a></h3>
<p>The tutorial implements a <strong>box blur</strong> (uniform smoothing filter). Each
pixel’s new value is the average of its local neighborhood. This operation:</p>
<ul class="simple">
<li><p>Reduces noise by averaging local intensity variations.</p></li>
<li><p>Acts as a low-pass filter, attenuating high-frequency components.</p></li>
<li><p>Provides an ideal example of a stencil computation with uniform weights.</p></li>
</ul>
</section>
</section>
<section id="two-dimensional-grid-architecture">
<h2>Two-dimensional grid architecture<a class="headerlink" href="#two-dimensional-grid-architecture" title="Link to this heading">#</a></h2>
<p>The tutorial uses a two-dimensional grid that maps to the shape of the image, significantly
simplifying the implementation. This approach:</p>
<ul class="simple">
<li><p>Maps threads directly to pixel positions</p></li>
<li><p>Simplifies coordinate calculations</p></li>
<li><p>Enables intuitive spatial reasoning</p></li>
<li><p>Aligns with the natural structure of images</p></li>
</ul>
<section id="grid-configuration">
<h3>Grid configuration<a class="headerlink" href="#grid-configuration" title="Link to this heading">#</a></h3>
<p>Rather than using a single integer to represent the size of the grid, the tutorial uses a
<code class="docutils literal notranslate"><span class="pre">dim3</span></code> object containing three values to represent the number of block-based
work items per dimension:</p>
<ul class="simple">
<li><p><strong>x dimension</strong>: Width of the image</p></li>
<li><p><strong>y dimension</strong>: Height of the image</p></li>
<li><p><strong>z dimension</strong>: Set to 1 for 2D problems</p></li>
</ul>
</section>
</section>
<section id="complete-implementation">
<h2>Complete implementation<a class="headerlink" href="#complete-implementation" title="Link to this heading">#</a></h2>
<section id="header-and-setup">
<h3>Header and setup<a class="headerlink" href="#header-and-setup" title="Link to this heading">#</a></h3>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&quot;image.h&quot;</span>
</pre></div>
</div>
</section>
<section id="the-convolution-kernel">
<h3>The convolution kernel<a class="headerlink" href="#the-convolution-kernel" title="Link to this heading">#</a></h3>
<p>Here’s the complete 2D convolution kernel for image smoothing:</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">conv2d</span><span class="p">(</span><span class="kt">uint8_t</span><span class="w"> </span><span class="o">*</span><span class="n">image</span><span class="p">,</span><span class="w"> </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">image_width</span><span class="p">,</span>
<span class="w">                      </span><span class="kt">int</span><span class="w"> </span><span class="n">image_height</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">mask_width</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">mask_height</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">y</span><span class="p">;</span>

<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="n">image_width</span><span class="w"> </span><span class="o">||</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="n">image_height</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">return</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="n">sum</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">mask_width</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">mask_height</span><span class="p">;</span><span class="w"> </span><span class="n">j</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="c1">// Calculate the coordinate of the pixel to read.</span>
<span class="w">            </span><span class="kt">int</span><span class="w"> </span><span class="n">image_x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">mask_width</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>
<span class="w">            </span><span class="kt">int</span><span class="w"> </span><span class="n">image_y</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">mask_height</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>

<span class="w">            </span><span class="c1">// Do not read outside the image.</span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">image_x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">0</span><span class="w"> </span><span class="o">||</span><span class="w"> </span><span class="n">image_x</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="n">image_width</span><span class="w"> </span><span class="o">||</span>
<span class="w">                </span><span class="n">image_y</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">0</span><span class="w"> </span><span class="o">||</span><span class="w"> </span><span class="n">image_y</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="n">image_height</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="k">continue</span><span class="p">;</span>
<span class="w">            </span><span class="p">}</span>

<span class="w">            </span><span class="c1">// Accumulate the value of the pixel.</span>
<span class="w">            </span><span class="kt">int</span><span class="w"> </span><span class="n">image_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">image_y</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">image_width</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">image_x</span><span class="p">;</span>
<span class="w">            </span><span class="kt">int</span><span class="w"> </span><span class="n">mask_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">mask_width</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">;</span>
<span class="w">            </span><span class="n">sum</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">image</span><span class="p">[</span><span class="n">image_index</span><span class="p">]</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mf">255.0f</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">mask</span><span class="p">[</span><span class="n">mask_index</span><span class="p">];</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">image_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">image_width</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="n">image</span><span class="p">[</span><span class="n">image_index</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">sum</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">255</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<section id="thread-identification-in-2d">
<h4>Thread identification in 2D<a class="headerlink" href="#thread-identification-in-2d" title="Link to this heading">#</a></h4>
<p>To obtain thread IDs in both x and y dimensions:</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">y</span><span class="p">;</span>
</pre></div>
</div>
<p>This calculation combines:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">threadIdx.x</span></code> and <code class="docutils literal notranslate"><span class="pre">threadIdx.y</span></code>: Local thread coordinates within a block</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">blockIdx.x</span></code> and <code class="docutils literal notranslate"><span class="pre">blockIdx.y</span></code>: Block coordinates within the grid</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">blockDim.x</span></code> and <code class="docutils literal notranslate"><span class="pre">blockDim.y</span></code>: Block dimensions</p></li>
</ul>
</section>
<section id="boundary-checking">
<h4>Boundary checking<a class="headerlink" href="#boundary-checking" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="n">image_width</span><span class="w"> </span><span class="o">||</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="n">image_height</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">return</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>This ensures threads don’t process pixels outside the image bounds. Threads that
exceed the image dimensions simply return without doing work.</p>
</section>
<section id="mask-application-loop">
<h4>Mask application loop<a class="headerlink" href="#mask-application-loop" title="Link to this heading">#</a></h4>
<p>The nested loops iterate over the mask dimensions:</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">mask_width</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">mask_height</span><span class="p">;</span><span class="w"> </span><span class="n">j</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="c1">// Process each mask element</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="coordinate-calculation">
<h4>Coordinate calculation<a class="headerlink" href="#coordinate-calculation" title="Link to this heading">#</a></h4>
<p>For each position in the mask, calculate the corresponding image coordinate:</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">image_x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">mask_width</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">image_y</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">mask_height</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>
</pre></div>
</div>
<p>The <code class="docutils literal notranslate"><span class="pre">-</span> <span class="pre">mask_width</span> <span class="pre">/</span> <span class="pre">2</span></code> and <code class="docutils literal notranslate"><span class="pre">-</span> <span class="pre">mask_height</span> <span class="pre">/</span> <span class="pre">2</span></code> center the mask over the
current pixel.</p>
</section>
<section id="edge-handling">
<h4>Edge handling<a class="headerlink" href="#edge-handling" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">image_x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">0</span><span class="w"> </span><span class="o">||</span><span class="w"> </span><span class="n">image_x</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="n">image_width</span><span class="w"> </span><span class="o">||</span>
<span class="w">    </span><span class="n">image_y</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">0</span><span class="w"> </span><span class="o">||</span><span class="w"> </span><span class="n">image_y</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="n">image_height</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">continue</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>This prevents reading outside the image boundaries. When the mask extends beyond
the image edge, the code simply skips those pixels (continue to the next
iteration).</p>
</section>
<section id="accumulation">
<h4>Accumulation<a class="headerlink" href="#accumulation" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">image_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">image_y</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">image_width</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">image_x</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">mask_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">mask_width</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">;</span>
<span class="n">sum</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">image</span><span class="p">[</span><span class="n">image_index</span><span class="p">]</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mf">255.0f</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">mask</span><span class="p">[</span><span class="n">mask_index</span><span class="p">];</span>
</pre></div>
</div>
<p>For each mask position:</p>
<ol class="arabic simple">
<li><p>Calculate the flattened array index for the image pixel</p></li>
<li><p>Calculate the flattened array index for the mask value</p></li>
<li><p>Normalize the pixel value (divide by 255 to get 0-1 range)</p></li>
<li><p>Multiply by the mask weight and accumulate</p></li>
</ol>
</section>
<section id="writing-the-result">
<h4>Writing the result<a class="headerlink" href="#writing-the-result" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">image_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">image_width</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">x</span><span class="p">;</span>
<span class="n">image</span><span class="p">[</span><span class="n">image_index</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">sum</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">255</span><span class="p">;</span>
</pre></div>
</div>
<p>After processing all mask positions, write the accumulated result back to the
output image, scaling back to the 0-255 range.</p>
</section>
</section>
<section id="host-code-implementation">
<h3>Host code implementation<a class="headerlink" href="#host-code-implementation" title="Link to this heading">#</a></h3>
<section id="main-function-setup">
<h4>Main function setup<a class="headerlink" href="#main-function-setup" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">width</span><span class="p">,</span><span class="w"> </span><span class="n">height</span><span class="p">,</span><span class="w"> </span><span class="n">channels</span><span class="p">;</span>
<span class="w">    </span><span class="k">static</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">maskWidth</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">200</span><span class="p">;</span>
<span class="w">    </span><span class="k">static</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">maskHeight</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">200</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">mask</span><span class="p">(</span><span class="n">maskWidth</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">maskHeight</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">channels</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Initialize mask with uniform averaging weights</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">maskWidth</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">maskHeight</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">mask</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">1.0f</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">maskWidth</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">maskHeight</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">channels</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Load an image from disk (implementation not shown)</span>
</pre></div>
</div>
</section>
<section id="mask-initialization">
<h4>Mask initialization<a class="headerlink" href="#mask-initialization" title="Link to this heading">#</a></h4>
<p>The mask is initialized with uniform weights that sum to 1.0:</p>
<ul class="simple">
<li><p>Each element is <code class="docutils literal notranslate"><span class="pre">1.0</span> <span class="pre">/</span> <span class="pre">(maskWidth</span> <span class="pre">*</span> <span class="pre">maskHeight</span> <span class="pre">*</span> <span class="pre">channels)</span></code></p></li>
<li><p>This creates an averaging filter</p></li>
<li><p>When applied, it produces a smoothing (blurring) effect</p></li>
</ul>
</section>
<section id="memory-allocation-and-data-transfer">
<h4>Memory allocation and data transfer<a class="headerlink" href="#memory-allocation-and-data-transfer" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="c1">// Allocate GPU memory and copy data to the GPU.</span>
<span class="kt">uint8_t</span><span class="w"> </span><span class="o">*</span><span class="n">d_image</span><span class="p">;</span>
<span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">d_mask</span><span class="p">;</span>
<span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_image</span><span class="p">,</span><span class="w"> </span><span class="n">width</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">height</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">channels</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">uint8_t</span><span class="p">));</span>
<span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_mask</span><span class="p">,</span><span class="w"> </span><span class="n">maskWidth</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">maskHeight</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">channels</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">));</span>

<span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_image</span><span class="p">,</span><span class="w"> </span><span class="n">image</span><span class="p">,</span><span class="w"> </span><span class="n">width</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">height</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">channels</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">uint8_t</span><span class="p">),</span>
<span class="w">          </span><span class="n">hipMemcpyHostToDevice</span><span class="p">);</span>
<span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_mask</span><span class="p">,</span><span class="w"> </span><span class="n">mask</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span>
<span class="w">          </span><span class="n">maskWidth</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">maskHeight</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">channels</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">),</span>
<span class="w">          </span><span class="n">hipMemcpyHostToDevice</span><span class="p">);</span>
</pre></div>
</div>
</section>
<section id="grid-configuration-and-kernel-launch">
<h4>Grid configuration and kernel launch<a class="headerlink" href="#grid-configuration-and-kernel-launch" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="c1">// Calculate grid size and launch the kernel.</span>
<span class="n">dim3</span><span class="w"> </span><span class="n">block_size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="mi">16</span><span class="p">,</span><span class="w"> </span><span class="mi">16</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">};</span>
<span class="n">dim3</span><span class="w"> </span><span class="n">grid_size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{(</span><span class="n">width</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">block_size</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="mi">1</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">block_size</span><span class="p">.</span><span class="n">x</span><span class="p">,</span>
<span class="w">                 </span><span class="p">(</span><span class="n">height</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">block_size</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="mi">1</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">block_size</span><span class="p">.</span><span class="n">y</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">};</span>

<span class="n">conv2d</span><span class="o">&lt;&lt;&lt;</span><span class="n">grid_size</span><span class="p">,</span><span class="w"> </span><span class="n">block_size</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_image</span><span class="p">,</span><span class="w"> </span><span class="n">d_mask</span><span class="p">,</span><span class="w"> </span><span class="n">width</span><span class="p">,</span><span class="w"> </span><span class="n">height</span><span class="p">,</span>
<span class="w">                                  </span><span class="n">maskWidth</span><span class="p">,</span><span class="w"> </span><span class="n">maskHeight</span><span class="p">);</span>
<span class="n">hipDeviceSynchronize</span><span class="p">();</span>
</pre></div>
</div>
<p><strong>Grid size calculation:</strong></p>
<ul class="simple">
<li><p><code class="code docutils literal notranslate"><span class="pre">block_size</span></code>: 16 × 16 threads per block (256 threads total).</p></li>
<li><p><code class="code docutils literal notranslate"><span class="pre">grid_size</span></code>: Calculated to cover the entire image.</p></li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">(width</span> <span class="pre">+</span> <span class="pre">block_size.x</span> <span class="pre">-</span> <span class="pre">1)</span> <span class="pre">/</span> <span class="pre">block_size.x</span></code> formula ensures there are
enough blocks to cover all pixels, rounding up.</p></li>
</ul>
</section>
<section id="retrieving-results-and-cleanup">
<h4>Retrieving results and cleanup<a class="headerlink" href="#retrieving-results-and-cleanup" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="w">    </span><span class="c1">// Copy the data back to the host.</span>
<span class="w">    </span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">image</span><span class="p">,</span><span class="w"> </span><span class="n">d_image</span><span class="p">,</span><span class="w"> </span><span class="n">width</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">height</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">channels</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">uint8_t</span><span class="p">),</span>
<span class="w">              </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Store the image to disk (implementation not shown)</span>

<span class="w">    </span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_image</span><span class="p">);</span>
<span class="w">    </span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_mask</span><span class="p">);</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
</section>
</section>
<section id="performance-considerations">
<h2>Performance considerations<a class="headerlink" href="#performance-considerations" title="Link to this heading">#</a></h2>
<p>For high-resolution images for example 4096×4096 pixels, the GPU acceleration
provides:</p>
<ul class="simple">
<li><p><strong>Massive parallelism:</strong> Tens of thousands of concurrent threads.</p></li>
<li><p><strong>High throughput:</strong> Leveraging GPU memory bandwidth and computational density.</p></li>
<li><p><strong>Scalability:</strong> Linear speedup with increased SM occupancy.</p></li>
</ul>
<p>Typical speedups over CPU implementations range from <strong>10× to 100×</strong>, depending
on image size, mask complexity, and GPU architecture.</p>
<section id="memory-access-patterns">
<h3>Memory access patterns<a class="headerlink" href="#memory-access-patterns" title="Link to this heading">#</a></h3>
<p>Image convolution requires repeated access to neighboring pixels, leading to
non-coalesced memory transactions. Optimizing memory access is essential:</p>
<ul class="simple">
<li><p>Non-coalesced memory accesses (not all accesses are contiguous).</p></li>
<li><p>Repeated reads of the same pixels by adjacent threads.</p></li>
<li><p>Potential for optimization using shared memory (advanced technique).</p></li>
</ul>
</section>
</section>
<section id="best-practices">
<h2>Best practices<a class="headerlink" href="#best-practices" title="Link to this heading">#</a></h2>
<ol class="arabic">
<li><p><strong>Handle boundaries carefully</strong></p>
<p>Conditional branches in edge regions can cause wavefronts or warps to execute
serially. Prefer approaches that avoid per-thread branching, including:</p>
<blockquote>
<div><ul class="simple">
<li><p>Pre-clamping coordinates to valid index ranges</p></li>
<li><p>Padding or haloing input images so all threads operate on valid data</p></li>
<li><p>Using hardware boundary modes (such as texture sampling modes on RDNA) to
offload boundary handling</p></li>
</ul>
</div></blockquote>
<p>These techniques help maintain high SIMD lane utilization across the entire
grid.</p>
</li>
<li><p><strong>Center your stencil properly</strong></p>
<p>Compute the stencil origin using mask_width / 2 (or the equivalent for
rectangular masks) to ensure correct alignment between the input data and the
mask coefficients. This prevents off-by-one misalignment that can propagate
as spatial artifacts.</p>
</li>
<li><p><strong>Select mask sizes based on compute–memory tradeoffs</strong></p>
<p>Larger kernels increase arithmetic intensity but also expand the set of
neighbor loads per output element. Balance mask dimensions with available
bandwidth, register pressure, and shared-memory capacity, particularly when
implementing separable or multi-pass stencils.</p>
</li>
<li><p><strong>Normalize properly</strong></p>
<p>Ensure mask weights sum to the intended normalization constant, commonly 1.0
for averaging operations. When using integer or half-precision paths, verify
scaling behavior to avoid overflow or unintended bias.</p>
</li>
<li><p><strong>Consider edge strategies</strong></p>
<p>Adopt a clear policy for pixels whose neighborhoods extend outside the valid
domain. Options include skipping output generation, clamping to the nearest
valid coordinate, wrapping coordinates, or mirroring.</p>
</li>
</ol>
</section>
<section id="conclusion">
<h2>Conclusion<a class="headerlink" href="#conclusion" title="Link to this heading">#</a></h2>
<p>Stencil operations are a fundamental pattern in GPU computing that enables
efficient parallel processing of spatially-dependent data. The 2D convolution
example demonstrates:</p>
<ul class="simple">
<li><p>How to structure kernels for stencil patterns</p></li>
<li><p>Proper boundary handling for neighborhood operations</p></li>
<li><p>Effective use of 2D thread grids that map naturally to image structure</p></li>
<li><p>Memory access patterns for adjacent data elements</p></li>
</ul>
<p>By understanding stencil operations, developers can implement a wide range of
image processing algorithms, scientific simulations, and deep learning
operations on GPUs. The patterns demonstrated here extend beyond image
processing to any computational problem involving spatial relationships in
multi-dimensional data.</p>
<p>The key to successful stencil implementations is carefully managing boundary
conditions, ensuring correct coordinate calculations, and leveraging the GPU’s
parallel architecture to process many independent stencil operations
simultaneously.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="cpu_gpu_kmeans.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">CPU-GPU cooperative computing: K-means clustering tutorial</p>
      </div>
    </a>
    <a class="right-next"
       href="multikernel_bfs.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Multi-kernel programming: breadth-first search tutorial</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#applications-of-stencil-operations">Applications of stencil operations</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#image-convolution">Image convolution</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#dimensionality-of-stencils">Dimensionality of stencils</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#the-smoothing-operation">The smoothing operation</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#two-dimensional-grid-architecture">Two-dimensional grid architecture</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#grid-configuration">Grid configuration</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#complete-implementation">Complete implementation</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#header-and-setup">Header and setup</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#the-convolution-kernel">The convolution kernel</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#thread-identification-in-2d">Thread identification in 2D</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#boundary-checking">Boundary checking</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#mask-application-loop">Mask application loop</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#coordinate-calculation">Coordinate calculation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#edge-handling">Edge handling</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#accumulation">Accumulation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#writing-the-result">Writing the result</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#host-code-implementation">Host code implementation</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#main-function-setup">Main function setup</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#mask-initialization">Mask initialization</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-allocation-and-data-transfer">Memory allocation and data transfer</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#grid-configuration-and-kernel-launch">Grid configuration and kernel launch</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#retrieving-results-and-cleanup">Retrieving results and cleanup</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#performance-considerations">Performance considerations</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-access-patterns">Memory access patterns</a></li>
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
