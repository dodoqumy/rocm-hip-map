---
title: "CPU-GPU cooperative computing: K-means clustering tutorial &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/programming-patterns/cpu_gpu_kmeans.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:05:29.681153+00:00
content_hash: "bb93a7c393f38c7c"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="CPU-GPU cooperative computing at K-means clustering" name="description" />
<meta content="AMD, ROCm, HIP, CPU-GPU cooperative computing, K-means, clustering, K-means clustering" name="keywords" />

    <title>CPU-GPU cooperative computing: K-means clustering tutorial &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'tutorial/programming-patterns/cpu_gpu_kmeans';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="Stencil operations: Image convolution tutorial" href="stencil_operations.html" />
    <link rel="prev" title="Atomic operations: Histogram tutorial" href="atomic_operations_histogram.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/tutorial/programming-patterns/cpu_gpu_kmeans.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l2 current active"><a class="current reference internal" href="#">CPU-GPU cooperative computing: K-means clustering tutorial</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">CPU-GPU...</li>
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
    <h1>CPU-GPU cooperative computing: K-means clustering tutorial</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#prerequisites">Prerequisites</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cpugpu-cooperative-computing">CPU–GPU cooperative computing</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#k-means-clustering">K-means clustering</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#algorithm">Algorithm</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#iterative-procedure">Iterative procedure</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#initialization">Initialization</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#assignment">Assignment</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#update">Update</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#convergence">Convergence</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#summary-of-cooperative-execution">Summary of cooperative execution</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#implementation">Implementation</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#data-structures">Data Structures</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#main-loop">Main Loop</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#gpu-membership-update-function">GPU membership update function</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-1-gpu-memory-allocation">Step 1: GPU memory allocation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-2-data-transfer-to-gpu">Step 2: Data transfer to GPU</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-3-kernel-configuration">Step 3: Kernel configuration</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-4-kernel-launch">Step 4: Kernel launch</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-5-retrieve-results">Step 5: Retrieve results</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-6-count-changes">Step 6: Count changes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-7-cleanup">Step 7: Cleanup</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-implementation">Kernel implementation</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#cpu-centroid-update">CPU centroid update</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#data-transfer-considerations">Data transfer considerations</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#best-practices">Best practices</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#design-principles">Design principles</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-strategy">Memory strategy</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#performance-considerations">Performance Considerations</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#when-to-use-cpu-gpu-cooperation">When to use CPU-GPU cooperation</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#when-to-avoid-cpu-gpu-cooperation">When to avoid CPU-GPU cooperation</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#conclusion">Conclusion</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="cpu-gpu-cooperative-computing-k-means-clustering-tutorial">
<h1>CPU-GPU cooperative computing: K-means clustering tutorial<a class="headerlink" href="#cpu-gpu-cooperative-computing-k-means-clustering-tutorial" title="Link to this heading">#</a></h1>
<p>Modern heterogeneous systems combine CPUs and GPUs to maximize computational
throughput. GPUs provide massive data-parallel performance, whereas CPUs excel
at complex control logic, and latency-sensitive serial tasks. Many real-world
algorithms—including unsupervised clustering—contain both parallelizable and
inherently sequential components.</p>
<p>This tutorial demonstrates a hybrid CPU–GPU cooperative execution model using
the K-means clustering algorithm, showcasing partitioned workload distribution,
memory management, and performance optimization strategies in heterogeneous
architectures.</p>
<section id="prerequisites">
<h2>Prerequisites<a class="headerlink" href="#prerequisites" title="Link to this heading">#</a></h2>
<p>To follow this tutorial, you’ll need installed drivers and a HIP compiler
toolchain to compile your code. HIP supports compiling and running on Linux and
Windows with AMD GPUs, the combination of install instructions is more than
worth covering as part of this tutorial. For more information about installing
HIP development packages, see <a class="reference internal" href="../../install/install.html"><span class="doc">Install HIP</span></a>.</p>
</section>
<section id="cpugpu-cooperative-computing">
<h2>CPU–GPU cooperative computing<a class="headerlink" href="#cpugpu-cooperative-computing" title="Link to this heading">#</a></h2>
<p>Modern computing platforms integrate <strong>central processing units (CPUs)</strong> and
<strong>graphics processing units (GPUs)</strong> into unified heterogeneous systems.
Each processor type offers distinct architectural strengths:</p>
<ul class="simple">
<li><p><strong>CPUs</strong> feature a small number of complex cores optimized for sequential
execution, branching, and latency-sensitive control flow.</p></li>
<li><p><strong>GPUs</strong> consist of thousands of simpler cores optimized for throughput and
massive data-level parallelism.</p></li>
</ul>
<p><strong>Cooperative computing</strong> refers to a programming paradigm that combines these
capabilities in a coordinated execution model, where both CPU and GPU perform
complementary portions of a workload. Rather than treating the GPU as a passive
accelerator, this approach distributes computation dynamically between devices
to maximize total system utilization.</p>
</section>
<section id="k-means-clustering">
<h2>K-means clustering<a class="headerlink" href="#k-means-clustering" title="Link to this heading">#</a></h2>
<p>K-means is an unsupervised machine learning algorithm that partitions a dataset
into <span class="math notranslate nohighlight">\(k\)</span> clusters (groups of similar data points) by minimizing
intra-cluster variance. It iteratively refines cluster assignments and centroid
(center point of a cluster) locations until convergence.</p>
<p>The optimization objective is defined as:</p>
<div class="math notranslate nohighlight">
\[\min_{C_1, \dots, C_k} \sum_{i=1}^{k} \sum_{x_j \in C_i} \|x_j - \mu_i\|^2\]</div>
<p>where <span class="math notranslate nohighlight">\(\mu_i\)</span> is the centroid of cluster <span class="math notranslate nohighlight">\(C_i\)</span>.</p>
<p>K-means is frequently used in:</p>
<ul class="simple">
<li><p><strong>Customer segmentation</strong>: Grouping customers by behavior patterns</p></li>
<li><p><strong>Image compression</strong>: Reducing color palette by clustering similar colors</p></li>
<li><p><strong>Anomaly detection</strong>: Identifying outliers that don’t fit clusters</p></li>
<li><p><strong>Document clustering</strong>: Organizing similar documents together</p></li>
<li><p><strong>Feature engineering</strong>: Creating new features based on cluster membership</p></li>
</ul>
</section>
<section id="algorithm">
<h2>Algorithm<a class="headerlink" href="#algorithm" title="Link to this heading">#</a></h2>
<p>The K-means algorithm iteratively refines a partition of a dataset into
<span class="math notranslate nohighlight">\(k\)</span> clusters by alternating between two primary computational phases:
<strong>assignment</strong> and <strong>update</strong>. Each iteration minimizes the total within-cluster
variance, driving the system toward convergence where centroid movement or
membership changes fall below a defined threshold.</p>
<section id="iterative-procedure">
<h3>Iterative procedure<a class="headerlink" href="#iterative-procedure" title="Link to this heading">#</a></h3>
<ol class="arabic simple">
<li><p><strong>Initialization</strong>: Select initial centroids (random or via K-means++).</p></li>
<li><p><strong>Assignment</strong>: Assign each data point to the nearest centroid.</p></li>
<li><p><strong>Update</strong>: Recalculate each centroid as the mean of its assigned members.</p></li>
<li><p><strong>Convergence</strong>: Repeat until centroids stabilize or a maximum iteration
limit is reached.</p></li>
</ol>
<p>These phases alternate until the solution converges or a maximum iteration count
is reached.</p>
<section id="initialization">
<h4>Initialization<a class="headerlink" href="#initialization" title="Link to this heading">#</a></h4>
<p>The algorithm begins by selecting initial centroid positions. This step
significantly influences both convergence rate and clustering quality.</p>
<ul class="simple">
<li><p><strong>Random initialization</strong>: centroids are randomly chosen from the dataset.</p></li>
<li><p><strong>K-means++</strong>: probabilistic seeding to spread centroids across data space.</p></li>
<li><p><strong>Domain-specific heuristics</strong>: custom initializations for structured data.</p></li>
</ul>
<p>Initial centroid diversity reduces the likelihood of poor local minima and
improves overall stability.</p>
</section>
<section id="assignment">
<h4>Assignment<a class="headerlink" href="#assignment" title="Link to this heading">#</a></h4>
<p>For each data point <span class="math notranslate nohighlight">\(x_i\)</span>, the algorithm computes the Euclidean distance
to each centroid <span class="math notranslate nohighlight">\(\mu_j\)</span> and assigns the point to the nearest cluster:</p>
<div class="math notranslate nohighlight">
\[C_i = \arg \min_j \|x_i - \mu_j\|^2\]</div>
<ul class="simple">
<li><p>Each point–centroid distance calculation is independent.</p></li>
<li><p>Ideal for SIMD/SIMT architectures (GPU execution).</p></li>
<li><p>Dominated by dense floating-point arithmetic and memory bandwidth utilization.</p></li>
</ul>
<p>This phase represents the <strong>embarrassingly parallel</strong> portion of the algorithm
and provides the largest opportunity for GPU acceleration.</p>
</section>
<section id="update">
<h4>Update<a class="headerlink" href="#update" title="Link to this heading">#</a></h4>
<p>Once all data points are assigned, new centroid positions are computed as the
mean of their corresponding cluster members:</p>
<div class="math notranslate nohighlight">
\[\mu_j = \frac{1}{|C_j|} \sum_{x_i \in C_j} x_i\]</div>
<ul class="simple">
<li><p>Requires aggregation and division per cluster.</p></li>
<li><p>Involves variable membership counts across clusters.</p></li>
<li><p>Reduction-heavy and branch-divergent.</p></li>
</ul>
<p>Although reduction can be implemented on GPUs, small <span class="math notranslate nohighlight">\(k\)</span> values and
irregular membership sizes typically make the CPU more efficient for this phase,
given its superior cache hierarchy and flexible control flow.</p>
</section>
<section id="convergence">
<h4>Convergence<a class="headerlink" href="#convergence" title="Link to this heading">#</a></h4>
<p>After the update phase, convergence is evaluated using one of the following
criteria:</p>
<ul class="simple">
<li><p>No change in point memberships.</p></li>
<li><p>Centroid displacement below a user-defined threshold.</p></li>
<li><p>Iteration count exceeds maximum limit.</p></li>
</ul>
<p>If the convergence condition is not met, the assignment and update phases
repeat.</p>
</section>
</section>
<section id="summary-of-cooperative-execution">
<h3>Summary of cooperative execution<a class="headerlink" href="#summary-of-cooperative-execution" title="Link to this heading">#</a></h3>
<ol class="arabic simple">
<li><p><strong>GPU:</strong> performs parallel distance evaluations and membership assignments.</p></li>
<li><p><strong>CPU:</strong> executes centroid averaging and convergence checks.</p></li>
<li><p><strong>Synchronization:</strong> only essential data (centroids and membership
arrays) is exchanged per iteration.</p></li>
</ol>
<p>This division of labor minimizes data movement and maximizes hardware
utilization. The resulting hybrid implementation combines GPU throughput for
massive data-parallel operations with CPU efficiency for aggregation and control
tasks, enabling scalable clustering performance on heterogeneous systems.</p>
</section>
</section>
<section id="implementation">
<h2>Implementation<a class="headerlink" href="#implementation" title="Link to this heading">#</a></h2>
<p>This implementation follows a hybrid CPU/GPU design to accelerate the most
computationally expensive phase of K-means: assigning each data point to its
nearest centroid. The GPU performs distance calculations in parallel, while the
CPU handles the centroid recomputation, where sequential reductions are
efficient and data sizes are small. The algorithm iterates between GPU-based
membership updates and CPU-based centroid averaging until convergence or a
maximum iteration count is reached.</p>
<section id="data-structures">
<h3>Data Structures<a class="headerlink" href="#data-structures" title="Link to this heading">#</a></h3>
<p>The implementation stores all data in simple, contiguous arrays for efficient
memory access on both CPU and GPU. Data points and centroids are represented as
flattened <code class="docutils literal notranslate"><span class="pre">std::vector&lt;float&gt;</span></code> arrays, while cluster assignments are stored as
<code class="docutils literal notranslate"><span class="pre">std::vector&lt;int&gt;</span></code>.</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="c1">// length: Number of data points to cluster</span>
<span class="c1">// dimension: Number of features per data point</span>
<span class="c1">// k: Number of clusters</span>

<span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">data</span><span class="p">;</span><span class="w">           </span><span class="c1">// Data points (length * dimension)</span>
<span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">centroids</span><span class="p">;</span><span class="w">      </span><span class="c1">// Centroid positions (k * dimension)</span>
<span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="w"> </span><span class="n">memberships</span><span class="p">;</span><span class="w">      </span><span class="c1">// Cluster assignments (length)</span>
</pre></div>
</div>
</section>
<section id="main-loop">
<h3>Main Loop<a class="headerlink" href="#main-loop" title="Link to this heading">#</a></h3>
<p>The core K-means iteration:</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="c1">// length is an integer for the number of entries to be clustered.</span>
<span class="c1">// dimension is an integer for the number of properties of each entry.</span>
<span class="c1">// k is an integer that determines the number of clusters.</span>

<span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">centroids</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">initializeCentroids</span><span class="p">(</span><span class="n">length</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">dimension</span><span class="p">,</span><span class="w"> </span><span class="n">k</span><span class="p">);</span>
<span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="w"> </span><span class="n">memberships</span><span class="p">(</span><span class="n">length</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>

<span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">iteration</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">iteration</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">maxIterations</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">iteration</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// Determine the cluster that each entry belongs to.</span>
<span class="w">    </span><span class="c1">// The function returns how many entries changed membership.</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">membershipChanges</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">updateMembership</span><span class="p">(</span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="n">centroids</span><span class="p">,</span><span class="w"> </span><span class="n">memberships</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Converge checking.</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">membershipChanges</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">break</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Calculate new centroids.</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">Point</span><span class="o">&gt;</span><span class="w"> </span><span class="n">newCentroids</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">centroids</span><span class="p">;</span>
<span class="w">    </span><span class="n">updateCentroid</span><span class="p">(</span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="n">newCentroids</span><span class="p">,</span><span class="w"> </span><span class="n">memberships</span><span class="p">);</span>
<span class="w">    </span><span class="n">centroids</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">newCentroids</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>Loop structure:</strong></p>
<ol class="arabic simple">
<li><p>Update memberships using GPU</p></li>
<li><p>Check for convergence (no changes)</p></li>
<li><p>Update centroids using CPU</p></li>
<li><p>Repeat until convergence or max iterations</p></li>
</ol>
</section>
<section id="gpu-membership-update-function">
<h3>GPU membership update function<a class="headerlink" href="#gpu-membership-update-function" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">updateMembership</span></code> function serves as the interface between CPU and GPU:</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="nf">updateMembership</span><span class="p">(</span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">centroids</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">membership</span><span class="p">,</span>
<span class="w">                    </span><span class="kt">int</span><span class="w"> </span><span class="n">dataSize</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">dimension</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">k</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// gpuData is allocated and copied to the GPU earlier.</span>

<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">gpuCentroids</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">gpuMembership</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Allocate GPU memory</span>
<span class="w">    </span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">gpuCentroids</span><span class="p">,</span><span class="w"> </span><span class="n">k</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">));</span>
<span class="w">    </span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">gpuMembership</span><span class="p">,</span><span class="w"> </span><span class="n">dataSize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Copy data from CPU to GPU</span>
<span class="w">    </span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">gpuCentroids</span><span class="p">,</span><span class="w"> </span><span class="n">centroids</span><span class="p">,</span><span class="w"> </span><span class="n">k</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">),</span>
<span class="w">              </span><span class="n">hipMemcpyHostToDevice</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Calculate the sizes for the kernel launch</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">localSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">256</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">globalSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="n">dataSize</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">localSize</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="mi">1</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">localSize</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Launch the kernel</span>
<span class="w">    </span><span class="n">updateMembershipGPU</span><span class="o">&lt;&lt;&lt;</span><span class="n">globalSize</span><span class="p">,</span><span class="w"> </span><span class="n">localSize</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span>
<span class="w">        </span><span class="n">gpuData</span><span class="p">,</span><span class="w"> </span><span class="n">gpuCentroids</span><span class="p">,</span><span class="w"> </span><span class="n">gpuMembership</span><span class="p">,</span><span class="w"> </span><span class="n">dataSize</span><span class="p">,</span><span class="w"> </span><span class="n">dimension</span><span class="p">,</span><span class="w"> </span><span class="n">k</span><span class="p">);</span>
<span class="w">    </span><span class="n">hipDeviceSynchronize</span><span class="p">();</span>

<span class="w">    </span><span class="c1">// Create CPU Data to hold the results</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="w"> </span><span class="n">cpuNewMembership</span><span class="p">(</span><span class="n">dataSize</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Copy GPU data back to CPU</span>
<span class="w">    </span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">cpuNewMembership</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">gpuMembership</span><span class="p">,</span>
<span class="w">              </span><span class="n">dataSize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Count membership updates</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">membershipUpdate</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">dataSize</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">membership</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">cpuNewMembership</span><span class="p">[</span><span class="n">i</span><span class="p">])</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">membershipUpdate</span><span class="o">++</span><span class="p">;</span>
<span class="w">            </span><span class="n">membership</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">cpuNewMembership</span><span class="p">[</span><span class="n">i</span><span class="p">];</span><span class="w"> </span><span class="c1">// Update the original</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Free GPU memory</span>
<span class="w">    </span><span class="n">hipFree</span><span class="p">(</span><span class="n">gpuCentroids</span><span class="p">);</span>
<span class="w">    </span><span class="n">hipFree</span><span class="p">(</span><span class="n">gpuMembership</span><span class="p">);</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">membershipUpdate</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<section id="step-1-gpu-memory-allocation">
<h4>Step 1: GPU memory allocation<a class="headerlink" href="#step-1-gpu-memory-allocation" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">gpuCentroids</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">gpuMembership</span><span class="p">;</span>
<span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">gpuCentroids</span><span class="p">,</span><span class="w"> </span><span class="n">k</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">));</span>
<span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">gpuMembership</span><span class="p">,</span><span class="w"> </span><span class="n">dataSize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">));</span>
</pre></div>
</div>
<p>Allocate space on the GPU for:</p>
<ul class="simple">
<li><p><strong>Centroids</strong>: <span class="math notranslate nohighlight">\(k\)</span> centroids, each with dimension features</p></li>
<li><p><strong>Membership assignments</strong>: One cluster ID per data point</p></li>
</ul>
</section>
<section id="step-2-data-transfer-to-gpu">
<h4>Step 2: Data transfer to GPU<a class="headerlink" href="#step-2-data-transfer-to-gpu" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">gpuCentroids</span><span class="p">,</span><span class="w"> </span><span class="n">centroids</span><span class="p">,</span><span class="w"> </span><span class="n">k</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">float</span><span class="p">),</span>
<span class="w">          </span><span class="n">hipMemcpyHostToDevice</span><span class="p">);</span>
</pre></div>
</div>
<p>Transfer the current centroid positions from CPU to GPU. Note that the data
points (<code class="docutils literal notranslate"><span class="pre">gpuData</span></code>) are already on the GPU from earlier initialization.</p>
</section>
<section id="step-3-kernel-configuration">
<h4>Step 3: Kernel configuration<a class="headerlink" href="#step-3-kernel-configuration" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">localSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">256</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">globalSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="n">dataSize</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">localSize</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="mi">1</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">localSize</span><span class="p">;</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">localSize</span></code>: 256 threads per block (common choice)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">globalSize</span></code>: Number of blocks needed to cover all data points</p></li>
<li><p>Rounding up ensures we process all data points</p></li>
</ul>
</section>
<section id="step-4-kernel-launch">
<h4>Step 4: Kernel launch<a class="headerlink" href="#step-4-kernel-launch" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="n">updateMembershipGPU</span><span class="o">&lt;&lt;&lt;</span><span class="n">globalSize</span><span class="p">,</span><span class="w"> </span><span class="n">localSize</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span>
<span class="w">    </span><span class="n">gpuData</span><span class="p">,</span><span class="w"> </span><span class="n">gpuCentroids</span><span class="p">,</span><span class="w"> </span><span class="n">gpuMembership</span><span class="p">,</span><span class="w"> </span><span class="n">dataSize</span><span class="p">,</span><span class="w"> </span><span class="n">dimension</span><span class="p">,</span><span class="w"> </span><span class="n">k</span><span class="p">);</span>
<span class="n">hipDeviceSynchronize</span><span class="p">();</span>
</pre></div>
</div>
<p>Launch the GPU kernel to compute cluster assignments in parallel, then wait for
completion.</p>
</section>
<section id="step-5-retrieve-results">
<h4>Step 5: Retrieve results<a class="headerlink" href="#step-5-retrieve-results" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="w"> </span><span class="n">cpuNewMembership</span><span class="p">(</span><span class="n">dataSize</span><span class="p">);</span>
<span class="n">hipMemcpy</span><span class="p">(</span><span class="n">cpuNewMembership</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">gpuMembership</span><span class="p">,</span>
<span class="w">          </span><span class="n">dataSize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">);</span>
</pre></div>
</div>
<p>Copy the new membership assignments back from GPU to CPU.</p>
</section>
<section id="step-6-count-changes">
<h4>Step 6: Count changes<a class="headerlink" href="#step-6-count-changes" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">membershipUpdate</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">dataSize</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">membership</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">cpuNewMembership</span><span class="p">[</span><span class="n">i</span><span class="p">])</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">membershipUpdate</span><span class="o">++</span><span class="p">;</span>
<span class="w">        </span><span class="n">membership</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">cpuNewMembership</span><span class="p">[</span><span class="n">i</span><span class="p">];</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>
<p>Count how many data points changed clusters. This value determines if the algorithm has converged.</p>
</section>
<section id="step-7-cleanup">
<h4>Step 7: Cleanup<a class="headerlink" href="#step-7-cleanup" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="n">hipFree</span><span class="p">(</span><span class="n">gpuCentroids</span><span class="p">);</span>
<span class="n">hipFree</span><span class="p">(</span><span class="n">gpuMembership</span><span class="p">);</span>
<span class="k">return</span><span class="w"> </span><span class="n">membershipUpdate</span><span class="p">;</span>
</pre></div>
</div>
<p>Free temporary GPU memory and return the change count.</p>
</section>
<section id="kernel-implementation">
<h4>Kernel implementation<a class="headerlink" href="#kernel-implementation" title="Link to this heading">#</a></h4>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">updateMembershipGPU</span><span class="p">(</span>
<span class="w">    </span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">centroids</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">membership</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">dataSize</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">dimension</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">k</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>

<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">dataSize</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="kt">float</span><span class="w"> </span><span class="n">minDistance</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">INFINITY</span><span class="p">;</span>
<span class="w">        </span><span class="kt">int</span><span class="w"> </span><span class="n">bestCluster</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>

<span class="w">        </span><span class="c1">// Find nearest centroid</span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">cluster</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">cluster</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">k</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">cluster</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="kt">float</span><span class="w"> </span><span class="n">distance</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0.0f</span><span class="p">;</span>

<span class="w">            </span><span class="c1">// Calculate Euclidean distance</span>
<span class="w">            </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">d</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">d</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">dimension</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">d</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="kt">float</span><span class="w"> </span><span class="n">diff</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">data</span><span class="p">[</span><span class="n">tid</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">d</span><span class="p">]</span><span class="w"> </span><span class="o">-</span>
<span class="w">                            </span><span class="n">centroids</span><span class="p">[</span><span class="n">cluster</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">d</span><span class="p">];</span>
<span class="w">                </span><span class="n">distance</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">diff</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">diff</span><span class="p">;</span>
<span class="w">            </span><span class="p">}</span>

<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">distance</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">minDistance</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="n">minDistance</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">distance</span><span class="p">;</span>
<span class="w">                </span><span class="n">bestCluster</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">cluster</span><span class="p">;</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">        </span><span class="p">}</span>

<span class="w">        </span><span class="n">membership</span><span class="p">[</span><span class="n">tid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">bestCluster</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>Kernel operation:</strong></p>
<ol class="arabic simple">
<li><p>Each thread processes one data point</p></li>
<li><p>Calculates distance to all <span class="math notranslate nohighlight">\(k\)</span> centroids</p></li>
<li><p>Assigns point to nearest centroid</p></li>
<li><p>Stores result in membership array</p></li>
</ol>
</section>
</section>
<section id="cpu-centroid-update">
<h3>CPU centroid update<a class="headerlink" href="#cpu-centroid-update" title="Link to this heading">#</a></h3>
<p>The CPU handles the averaging operation:</p>
<div class="highlight-c++ notranslate"><div class="highlight"><pre><span></span><span class="kt">void</span><span class="w"> </span><span class="nf">updateCentroid</span><span class="p">(</span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="kt">float</span><span class="o">*</span><span class="w"> </span><span class="n">centroids</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">membership</span><span class="p">,</span>
<span class="w">                   </span><span class="kt">int</span><span class="w"> </span><span class="n">dataSize</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">dimension</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">k</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="w"> </span><span class="n">counts</span><span class="p">(</span><span class="n">k</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">sums</span><span class="p">(</span><span class="n">k</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">dimension</span><span class="p">,</span><span class="w"> </span><span class="mf">0.0f</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Accumulate sums for each cluster</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">dataSize</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="kt">int</span><span class="w"> </span><span class="n">cluster</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">membership</span><span class="p">[</span><span class="n">i</span><span class="p">];</span>
<span class="w">        </span><span class="n">counts</span><span class="p">[</span><span class="n">cluster</span><span class="p">]</span><span class="o">++</span><span class="p">;</span>

<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">d</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">d</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">dimension</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">d</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">sums</span><span class="p">[</span><span class="n">cluster</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">d</span><span class="p">]</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">data</span><span class="p">[</span><span class="n">i</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">d</span><span class="p">];</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Calculate averages (new centroids)</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">cluster</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">cluster</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">k</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">cluster</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">counts</span><span class="p">[</span><span class="n">cluster</span><span class="p">]</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">d</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">d</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">dimension</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">d</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="n">centroids</span><span class="p">[</span><span class="n">cluster</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">d</span><span class="p">]</span><span class="w"> </span><span class="o">=</span>
<span class="w">                    </span><span class="n">sums</span><span class="p">[</span><span class="n">cluster</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">d</span><span class="p">]</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">counts</span><span class="p">[</span><span class="n">cluster</span><span class="p">];</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>
<p>The centroid update requires:</p>
<ol class="arabic simple">
<li><p><strong>Reduction operation</strong>: Sum all points in each cluster.</p></li>
<li><p><strong>Variable-sized groups</strong>: Clusters have different numbers of points.</p></li>
<li><p><strong>Division</strong>: Calculate average (not easily parallelized).</p></li>
</ol>
<p>While GPUs can perform reductions, for this workload:</p>
<ul class="simple">
<li><p>The number of clusters (<span class="math notranslate nohighlight">\(k\)</span>) is typically small (&lt; 100).</p></li>
<li><p>The CPU can efficiently handle this sequential aggregation.</p></li>
<li><p>Avoiding GPU complexity keeps code simpler.</p></li>
</ul>
<section id="data-transfer-considerations">
<h4>Data transfer considerations<a class="headerlink" href="#data-transfer-considerations" title="Link to this heading">#</a></h4>
<p><strong>Data already on CPU:</strong></p>
<ul class="simple">
<li><p>Membership array was just copied back.</p></li>
<li><p>Data points can be kept on CPU for small datasets.</p></li>
<li><p>Centroids are small (k × dimension values).</p></li>
</ul>
<p><strong>Transfer costs:</strong></p>
<ul class="simple">
<li><p>Only centroids need to copy back to GPU.</p></li>
<li><p>Much smaller than the full dataset.</p></li>
<li><p>Overhead justified by parallel speedup in assignment phase.</p></li>
</ul>
</section>
</section>
</section>
<section id="best-practices">
<h2>Best practices<a class="headerlink" href="#best-practices" title="Link to this heading">#</a></h2>
<p>This section outlines recommended practices for implementing an efficient
GPU-accelerated Breadth-First Search (BFS). It highlights design principles,
memory-management strategies, and debugging techniques that help ensure
correctness, maintainability, and high performance when mapping BFS onto modern
GPU architectures.</p>
<section id="design-principles">
<h3>Design principles<a class="headerlink" href="#design-principles" title="Link to this heading">#</a></h3>
<ol class="arabic">
<li><p><strong>Identify parallelism</strong></p>
<p>Decompose the K-means workflow into independent, data-parallel kernels such
as distance computation. Minimize sequential dependencies in assignment and
reduction steps.</p>
</li>
<li><p><strong>Minimize host–device data movement</strong></p>
<p>Maintain dataset and intermediate buffers resident on the GPU across
iterations. Transfer only convergence metrics or centroids when absolutely
necessary.</p>
</li>
<li><p><strong>Batch and fuse operations</strong></p>
<p>Combine smaller kernels such as distance computation and assignment, or
process multiple mini-batches per kernel launch to reduce kernel invocation
and PCIe transfer overhead.</p>
</li>
<li><p><strong>Overlap communication with computation</strong></p>
<p>Utilize asynchronous HIP streams to overlap host–device memory transfers with
GPU kernel execution. Employ pinned (page-locked) memory for faster DMA
transfers.</p>
</li>
</ol>
</section>
<section id="memory-strategy">
<h3>Memory strategy<a class="headerlink" href="#memory-strategy" title="Link to this heading">#</a></h3>
<ol class="arabic">
<li><p><strong>Persistent device allocations</strong></p>
<p>Allocate GPU memory once before iterative processing. Reuse buffers such as
those for centroids, assignments, and temporary reductions to avoid the
overhead of repeated <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a> and <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html#_CPPv47hipFreePv" title="hipFree"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipFree()</span></code></a> calls.</p>
</li>
<li><p><strong>Data locality optimization</strong></p>
<p>Co-locate data structures according to access frequency:</p>
<ul class="simple">
<li><p>Store high-throughput arrays (points, centroids) in global memory with
coalesced access.</p></li>
<li><p>Cache small, frequently reused values in shared memory or registers.</p></li>
</ul>
</li>
<li><p><strong>Transfer scheduling</strong></p>
<p>Schedule host–device transfers asynchronously while the GPU executes kernels.
Use HIP events or streams to synchronize only when necessary.</p>
</li>
<li><p><strong>Memory pooling and reuse</strong></p>
<p>Use memory pools such as <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html#_CPPv414hipMallocAsyncPPv6size_t12hipMemPool_t11hipStream_t" title="hipMallocAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code></a>,
<a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html#_CPPv4I0E22hipMallocFromPoolAsync10hipError_tPP1T6size_t12hipMemPool_t11hipStream_t" title="hipMallocFromPoolAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMallocFromPoolAsync()</span></code></a>, or custom allocators to mitigate
fragmentation and reduce allocation latency, especially in iterative or
batched workloads.</p>
</li>
</ol>
</section>
<section id="performance-considerations">
<h3>Performance Considerations<a class="headerlink" href="#performance-considerations" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 30.0%" />
<col style="width: 70.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Aspect</p></th>
<th class="head"><p>Recommendation</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>Large datasets</strong></p></td>
<td><p>GPU acceleration scales linearly with dataset size. Prioritize keeping
data on GPU to avoid PCIe bottlenecks.</p></td>
</tr>
<tr class="row-odd"><td><p><strong>Many iterations</strong></p></td>
<td><p>Use persistent buffers and asynchronous reduction to minimize
per-iteration synchronization overhead.</p></td>
</tr>
<tr class="row-even"><td><p><strong>Small number of clusters (k)</strong></p></td>
<td><p>Kernel execution may be underutilized. CPU execution or hybrid scheduling
may be more efficient.</p></td>
</tr>
<tr class="row-odd"><td><p><strong>High-dimensional data</strong></p></td>
<td><p>Distance computation dominates cost. Leverage GPU shared memory for
centroid caching and ensure memory coalescing for point vectors.</p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<section id="when-to-use-cpu-gpu-cooperation">
<h2>When to use CPU-GPU cooperation<a class="headerlink" href="#when-to-use-cpu-gpu-cooperation" title="Link to this heading">#</a></h2>
<ul>
<li><p><strong>Hybrid computational structure</strong></p>
<p>The algorithm exhibits a clear division between compute-intensive,
data-parallel kernels such as distance computation in K-means and lightweight,
control-heavy serial stages such as centroid updates or convergence checks.</p>
</li>
<li><p><strong>High arithmetic intensity in parallel regions</strong></p>
<p>The GPU-executed portion performs substantial arithmetic operations per memory
access, ensuring efficient utilization of GPU cores and minimizing the impact
of memory latency.</p>
</li>
<li><p><strong>Low-complexity reduction or synchronization on CPU</strong></p>
<p>The CPU phase primarily aggregates results or performs decision logic that
does not justify GPU kernel execution overhead.</p>
</li>
<li><p><strong>Large-scale data processing</strong></p>
<p>Dataset size exceeds the threshold where PCIe transfer costs can be amortized,
enabling sustained GPU throughput and effective memory reuse.</p>
</li>
<li><p><strong>Iterative or streaming workloads</strong></p>
<p>Algorithms involving multiple iterations benefit from persistent GPU memory
allocations and overlapped data transfer, significantly reducing
per-iteration latency.</p>
</li>
</ul>
</section>
<section id="when-to-avoid-cpu-gpu-cooperation">
<h2>When to avoid CPU-GPU cooperation<a class="headerlink" href="#when-to-avoid-cpu-gpu-cooperation" title="Link to this heading">#</a></h2>
<ul>
<li><p><strong>Fully parallelizable workloads</strong></p>
<p>Algorithms with uniform, independent computations across all data points are
better suited for GPU-only execution without CPU coordination overhead.</p>
</li>
<li><p><strong>Low computational density per element</strong></p>
<p>If each data element requires few operations relative to transfer cost,
CPU–GPU communication latency will dominate, leading to suboptimal
performance.</p>
</li>
<li><p><strong>High inter-phase data dependency</strong></p>
<p>Frequent synchronization or data exchange between CPU and GPU phases prevents
effective pipeline overlap and leads to idle compute units.</p>
</li>
<li><p><strong>Small problem sizes</strong></p>
<p>When datasets fit comfortably in CPU cache or system memory, the GPU launch
overhead and transfer latency outweigh any computational gains from
offloading.</p>
</li>
</ul>
</section>
<section id="conclusion">
<h2>Conclusion<a class="headerlink" href="#conclusion" title="Link to this heading">#</a></h2>
<p>The K-means implementation illustrates <strong>heterogeneous workload partitioning</strong>
between CPU and GPU. By mapping compute-intensive, data-parallel operations to
the GPU and reduction-heavy serial logic to the CPU, total runtime is minimized
while code complexity remains manageable.</p>
<p>This CPU–GPU cooperative execution paradigm generalizes to many algorithms
combining reduction, aggregation, and distance-based computation—enabling
scalable, efficient utilization of modern heterogeneous hardware.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="atomic_operations_histogram.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Atomic operations: Histogram tutorial</p>
      </div>
    </a>
    <a class="right-next"
       href="stencil_operations.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Stencil operations: Image convolution tutorial</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cpugpu-cooperative-computing">CPU–GPU cooperative computing</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#k-means-clustering">K-means clustering</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#algorithm">Algorithm</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#iterative-procedure">Iterative procedure</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#initialization">Initialization</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#assignment">Assignment</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#update">Update</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#convergence">Convergence</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#summary-of-cooperative-execution">Summary of cooperative execution</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#implementation">Implementation</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#data-structures">Data Structures</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#main-loop">Main Loop</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#gpu-membership-update-function">GPU membership update function</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-1-gpu-memory-allocation">Step 1: GPU memory allocation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-2-data-transfer-to-gpu">Step 2: Data transfer to GPU</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-3-kernel-configuration">Step 3: Kernel configuration</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-4-kernel-launch">Step 4: Kernel launch</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-5-retrieve-results">Step 5: Retrieve results</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-6-count-changes">Step 6: Count changes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#step-7-cleanup">Step 7: Cleanup</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-implementation">Kernel implementation</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#cpu-centroid-update">CPU centroid update</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#data-transfer-considerations">Data transfer considerations</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#best-practices">Best practices</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#design-principles">Design principles</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-strategy">Memory strategy</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#performance-considerations">Performance Considerations</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#when-to-use-cpu-gpu-cooperation">When to use CPU-GPU cooperation</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#when-to-avoid-cpu-gpu-cooperation">When to avoid CPU-GPU cooperation</a></li>
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
