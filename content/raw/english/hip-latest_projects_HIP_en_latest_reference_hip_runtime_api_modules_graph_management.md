---
title: "Graph management &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/graph_management.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:05:44.471486+00:00
content_hash: "b1a1d7f30a12d8c9"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="The graph management reference page." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, graph management, graph" name="keywords" />

    <title>Graph management &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
  <script data-cfasync="false">
    document.documentElement.dataset.mode = localStorage.getItem("mode") || "";
    document.documentElement.dataset.theme = localStorage.getItem("theme") || "";
  </script>
  
  <!-- Loaded before other Sphinx assets -->
  <link href="../../../_static/styles/theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../../../_static/styles/bootstrap.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../../../_static/styles/pydata-sphinx-theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />

  
  <link href="../../../_static/vendor/fontawesome/6.5.2/css/all.min.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
  <link rel="preload" as="font" type="font/woff2" crossorigin href="../../../_static/vendor/fontawesome/6.5.2/webfonts/fa-solid-900.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../../_static/vendor/fontawesome/6.5.2/webfonts/fa-brands-400.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../../_static/vendor/fontawesome/6.5.2/webfonts/fa-regular-400.woff2" />

    <link rel="stylesheet" type="text/css" href="../../../_static/pygments.css?v=a746c00c" />
    <link rel="stylesheet" type="text/css" href="../../../_static/styles/sphinx-book-theme.css?v=a3416100" />
    <link rel="stylesheet" type="text/css" href="../../../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
    <link rel="stylesheet" type="text/css" href="../../../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../../../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../../../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../../../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../../../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../../../_static/sphinx-design.min.css?v=95c83b7e" />
    <link rel="stylesheet" type="text/css" href="../../../_static/rocm_custom.css?v=35d74aab" />
  
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../../../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b" />
<link rel="preload" as="script" href="../../../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b" />
  <script src="../../../_static/vendor/fontawesome/6.5.2/js/all.min.js?digest=dfe6caa3a7d634c4db9b"></script>

    <script src="../../../_static/documentation_options.js?v=75144bb1"></script>
    <script src="../../../_static/doctools.js?v=9a2dae69"></script>
    <script src="../../../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../../../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../../../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../../../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../../../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../../../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../../../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../../../_static/search.js?v=90a4452c"></script>
    <script src="../../../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
    <script src="../../../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/hip_runtime_api/modules/graph_management';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Graphics interoperability" href="graphics_interoperability.html" />
    <link rel="prev" title="Callback activity APIs" href="callback_activity_apis.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/hip_runtime_api/modules/graph_management.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
      action="../../../search.html"
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
                    <img src="../../../_static/images/amd-header-logo.svg" alt="AMD Logo" title="AMD Logo" width="90" class="d-inline-block align-text-top hover-opacity"/>
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

  
    
  

<a class="navbar-brand logo" href="../../../index.html">
  
  
  
  
  
  
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
<li class="toctree-l1"><a class="reference internal" href="../../../what_is_hip.html">What is HIP?</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../hip-7-changes.html">HIP API 7.0 changes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../faq.html">Frequently asked questions</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../install/install.html">Installing HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../install/build.html">Building HIP from source</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Programming guide</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../understand/programming_model.html">Introduction to the HIP programming model</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../understand/performance_optimization.html">Understanding GPU performance</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../understand/hardware_implementation.html">Hardware implementation</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../understand/compilers.html">HIP compilers</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/performance_guidelines.html">Performance guidelines</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/debugging.html">Debugging with HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/logging.html">Logging HIP activity</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../../../how-to/hip_runtime_api.html">Using HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../../../how-to/hip_runtime_api/initialization.html">Initialization</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../../../how-to/hip_runtime_api/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../../how-to/hip_runtime_api/memory_management/host_memory.html">Host memory</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../../../how-to/hip_runtime_api/memory_management/device_memory.html">Device memory</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../../../how-to/hip_runtime_api/memory_management/device_memory/texture_fetching.html">Texture fetching</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="../../../how-to/hip_runtime_api/memory_management/coherence_control.html">Coherence control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../how-to/hip_runtime_api/memory_management/unified_memory.html">Unified memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../how-to/hip_runtime_api/memory_management/virtual_memory.html">Virtual memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../how-to/hip_runtime_api/memory_management/stream_ordered_allocator.html">Stream Ordered Memory Allocator</a></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="../../../how-to/hip_runtime_api/error_handling.html">Error handling</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../how-to/hip_runtime_api/call_stack.html">Call stack</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../how-to/hip_runtime_api/asynchronous.html">Asynchronous concurrent execution</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../how-to/hip_runtime_api/hipgraph.html">HIP graphs</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../how-to/hip_runtime_api/cooperative_groups.html">Cooperative groups</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../how-to/hip_runtime_api/multi_device.html">Multi-device management</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../how-to/hip_runtime_api/opengl_interop.html">OpenGL interoperability</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../how-to/hip_runtime_api/external_interop.html">External resource interoperability</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/hip_cpp_language_extensions.html">HIP C++ language extensions</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/kernel_language_cpp_support.html">Kernel language C++ support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/hip_porting_guide.html">Porting CUDA code to HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../how-to/hip_rtc.html">Programming for HIP runtime compiler (RTC)</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../understand/amd_clr.html">AMD compute language runtimes (CLR)</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active has-children"><a class="reference internal" href="../../hip_runtime_api_reference.html">HIP runtime API</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2 current active has-children"><a class="reference internal" href="../modules.html">Modules</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l3"><a class="reference internal" href="initialization_and_version.html">Initialization and version</a></li>
<li class="toctree-l3"><a class="reference internal" href="device_management.html">Device management</a></li>
<li class="toctree-l3"><a class="reference internal" href="execution_control.html">Execution control</a></li>
<li class="toctree-l3"><a class="reference internal" href="error_handling.html">Error handling</a></li>
<li class="toctree-l3"><a class="reference internal" href="stream_management.html">Stream management</a></li>
<li class="toctree-l3"><a class="reference internal" href="stream_memory_operations.html">Stream memory operations</a></li>
<li class="toctree-l3"><a class="reference internal" href="event_management.html">Event management</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="memory_management/memory_management_deprecated.html">Memory management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="memory_management/external_resource_interoperability.html">External resource interoperability</a></li>
<li class="toctree-l4"><a class="reference internal" href="memory_management/stream_ordered_memory_allocator.html">Stream ordered memory allocator</a></li>
<li class="toctree-l4"><a class="reference internal" href="memory_management/unified_memory_reference.html">Managed memory</a></li>
<li class="toctree-l4"><a class="reference internal" href="memory_management/virtual_memory_reference.html">Virtual memory management</a></li>
<li class="toctree-l4"><a class="reference internal" href="memory_management/texture_management.html">Texture management</a></li>
<li class="toctree-l4"><a class="reference internal" href="memory_management/texture_management_deprecated.html">Texture management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="memory_management/surface_object.html">Surface object</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="peer_to_peer_device_memory_access.html">Peer to peer device memory access</a></li>
<li class="toctree-l3"><a class="reference internal" href="context_management.html">Context management [deprecated]</a></li>
<li class="toctree-l3"><a class="reference internal" href="module_management.html">Module management</a></li>
<li class="toctree-l3"><a class="reference internal" href="occupancy.html">Occupancy</a></li>
<li class="toctree-l3"><a class="reference internal" href="profiler_control.html">Profiler control</a></li>
<li class="toctree-l3"><a class="reference internal" href="launch_api.html">Launch API</a></li>
<li class="toctree-l3"><a class="reference internal" href="runtime_compilation.html">Runtime compilation</a></li>
<li class="toctree-l3"><a class="reference internal" href="callback_activity_apis.html">Callback activity APIs</a></li>
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Graph management</a></li>
<li class="toctree-l3"><a class="reference internal" href="graphics_interoperability.html">Graphics interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="opengl_interoperability.html">OpenGL interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="cooperative_groups_reference.html">Cooperative groups</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../global_defines_enums_structs_files.html">Global defines, enums, structs and files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../../doxygen/html/group___global_defs.html">Global enum and defines</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../doxygen/html/group___driver_types.html">Driver Types</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../doxygen/html/annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../doxygen/html/files.html">File List</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../math_api.html">HIP math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../complex_math_api.html">HIP complex math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../env_variables.html">HIP environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../error_codes.html">HIP error codes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../api_syntax.html">CUDA to HIP API Function Comparison</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../deprecated_api_list.html">List of deprecated APIs</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../low_fp_types.html">Low Precision Floating Point Types</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../hardware_features.html">Hardware features</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Tutorials</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic">HIP basic examples</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples">HIP examples</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../tutorial/saxpy.html">SAXPY - Hello, HIP</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../../../tutorial/programming-patterns.html">GPU programming patterns</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../../../tutorial/programming-patterns/matrix_multiplication.html">Two-dimensional kernels: Matrix multiplication tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../tutorial/programming-patterns/atomic_operations_histogram.html">Atomic operations: Histogram tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../tutorial/programming-patterns/cpu_gpu_kmeans.html">CPU-GPU cooperative computing: K-means clustering tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../tutorial/programming-patterns/stencil_operations.html">Stencil operations: Image convolution tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../tutorial/programming-patterns/multikernel_bfs.html">Multi-kernel programming: breadth-first search tutorial</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../../tutorial/reduction.html">Reduction</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../tutorial/cooperative_groups_tutorial.html">Cooperative groups</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../tutorial/graph_api.html">HIP Graph API Tutorial</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">About</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../license.html">License</a></li>
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
      <a href="../../../index.html" class="nav-link" aria-label="Home">
        <i class="fa-solid fa-home"></i>
      </a>
    </li>
    
    <li class="breadcrumb-item"><a href="../../hip_runtime_api_reference.html" class="nav-link">HIP runtime API</a></li>
    
    
    <li class="breadcrumb-item"><a href="../modules.html" class="nav-link">Modules</a></li>
    
    <li class="breadcrumb-item active" aria-current="page">Graph management</li>
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
    <h1>Graph management</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode"><code class="docutils literal notranslate"><span class="pre">hipStreamBeginCapture()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipStreamBeginCaptureToGraph11hipStream_t10hipGraph_tPK14hipGraphNode_tPK16hipGraphEdgeData6size_t20hipStreamCaptureMode"><code class="docutils literal notranslate"><span class="pre">hipStreamBeginCaptureToGraph()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipStreamEndCapture11hipStream_tP10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipStreamEndCapture()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipStreamGetCaptureInfo11hipStream_tP22hipStreamCaptureStatusPy"><code class="docutils literal notranslate"><span class="pre">hipStreamGetCaptureInfo()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipStreamGetCaptureInfo_v211hipStream_tP22hipStreamCaptureStatusPyP10hipGraph_tPPK14hipGraphNode_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipStreamGetCaptureInfo_v2()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipStreamIsCapturing11hipStream_tP22hipStreamCaptureStatus"><code class="docutils literal notranslate"><span class="pre">hipStreamIsCapturing()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv434hipStreamUpdateCaptureDependencies11hipStream_tP14hipGraphNode_t6size_tj"><code class="docutils literal notranslate"><span class="pre">hipStreamUpdateCaptureDependencies()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv434hipThreadExchangeStreamCaptureModeP20hipStreamCaptureMode"><code class="docutils literal notranslate"><span class="pre">hipThreadExchangeStreamCaptureMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipGraphCreateP10hipGraph_tj"><code class="docutils literal notranslate"><span class="pre">hipGraphCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipGraphDestroy10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipGraphDestroy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipGraphAddDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphAddDependencies()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipGraphRemoveDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphRemoveDependencies()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipGraphGetEdges10hipGraph_tP14hipGraphNode_tP14hipGraphNode_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphGetEdges()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipGraphGetNodes10hipGraph_tP14hipGraphNode_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphGetNodes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipGraphGetRootNodes10hipGraph_tP14hipGraphNode_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphGetRootNodes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphNodeGetDependencies14hipGraphNode_tP14hipGraphNode_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeGetDependencies()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphNodeGetDependentNodes14hipGraphNode_tP14hipGraphNode_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeGetDependentNodes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipGraphNodeGetType14hipGraphNode_tP16hipGraphNodeType"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeGetType()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipGraphDestroyNode14hipGraphNode_t"><code class="docutils literal notranslate"><span class="pre">hipGraphDestroyNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipGraphCloneP10hipGraph_t10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipGraphClone()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipGraphNodeFindInCloneP14hipGraphNode_t14hipGraphNode_t10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeFindInClone()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipGraphInstantiateP14hipGraphExec_t10hipGraph_tP14hipGraphNode_tPc6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphInstantiate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipGraphInstantiateWithFlagsP14hipGraphExec_t10hipGraph_ty"><code class="docutils literal notranslate"><span class="pre">hipGraphInstantiateWithFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphInstantiateWithParamsP14hipGraphExec_t10hipGraph_tP25hipGraphInstantiateParams"><code class="docutils literal notranslate"><span class="pre">hipGraphInstantiateWithParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipGraphLaunch14hipGraphExec_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipGraphLaunch()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipGraphUpload14hipGraphExec_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipGraphUpload()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipGraphAddNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tP18hipGraphNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipGraphExecGetFlags14hipGraphExec_tPy"><code class="docutils literal notranslate"><span class="pre">hipGraphExecGetFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipGraphNodeSetParams14hipGraphNode_tP18hipGraphNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipGraphExecNodeSetParams14hipGraphExec_t14hipGraphNode_tP18hipGraphNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExecNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipGraphExecDestroy14hipGraphExec_t"><code class="docutils literal notranslate"><span class="pre">hipGraphExecDestroy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipGraphExecUpdate14hipGraphExec_t10hipGraph_tP14hipGraphNode_tP24hipGraphExecUpdateResult"><code class="docutils literal notranslate"><span class="pre">hipGraphExecUpdate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipGraphAddKernelNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK19hipKernelNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddKernelNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphKernelNodeGetParams14hipGraphNode_tP19hipKernelNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphKernelNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphKernelNodeSetParams14hipGraphNode_tPK19hipKernelNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphKernelNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431hipGraphExecKernelNodeSetParams14hipGraphExec_t14hipGraphNode_tPK19hipKernelNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExecKernelNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipDrvGraphAddMemcpyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK12HIP_MEMCPY3D8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphAddMemcpyNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipGraphAddMemcpyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK16hipMemcpy3DParms"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemcpyNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphMemcpyNodeGetParams14hipGraphNode_tP16hipMemcpy3DParms"><code class="docutils literal notranslate"><span class="pre">hipGraphMemcpyNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphMemcpyNodeSetParams14hipGraphNode_tPK16hipMemcpy3DParms"><code class="docutils literal notranslate"><span class="pre">hipGraphMemcpyNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipGraphKernelNodeSetAttribute14hipGraphNode_t19hipKernelNodeAttrIDPK22hipKernelNodeAttrValue"><code class="docutils literal notranslate"><span class="pre">hipGraphKernelNodeSetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipGraphKernelNodeGetAttribute14hipGraphNode_t19hipKernelNodeAttrIDP22hipKernelNodeAttrValue"><code class="docutils literal notranslate"><span class="pre">hipGraphKernelNodeGetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431hipGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tP16hipMemcpy3DParms"><code class="docutils literal notranslate"><span class="pre">hipGraphExecMemcpyNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipGraphAddMemcpyNode1DP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPvPKv6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemcpyNode1D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphMemcpyNodeSetParams1D14hipGraphNode_tPvPKv6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphMemcpyNodeSetParams1D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv433hipGraphExecMemcpyNodeSetParams1D14hipGraphExec_t14hipGraphNode_tPvPKv6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphExecMemcpyNodeSetParams1D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431hipGraphAddMemcpyNodeFromSymbolP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemcpyNodeFromSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv437hipGraphMemcpyNodeSetParamsFromSymbol14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphMemcpyNodeSetParamsFromSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv441hipGraphExecMemcpyNodeSetParamsFromSymbol14hipGraphExec_t14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphExecMemcpyNodeSetParamsFromSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphAddMemcpyNodeToSymbolP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPKvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemcpyNodeToSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv435hipGraphMemcpyNodeSetParamsToSymbol14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphMemcpyNodeSetParamsToSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv439hipGraphExecMemcpyNodeSetParamsToSymbol14hipGraphExec_t14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphExecMemcpyNodeSetParamsToSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipGraphAddMemsetNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK15hipMemsetParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemsetNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphMemsetNodeGetParams14hipGraphNode_tP15hipMemsetParams"><code class="docutils literal notranslate"><span class="pre">hipGraphMemsetNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphMemsetNodeSetParams14hipGraphNode_tPK15hipMemsetParams"><code class="docutils literal notranslate"><span class="pre">hipGraphMemsetNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431hipGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExecMemsetNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipGraphAddHostNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK17hipHostNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddHostNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipGraphHostNodeGetParams14hipGraphNode_tP17hipHostNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphHostNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipGraphHostNodeSetParams14hipGraphNode_tPK17hipHostNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphHostNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphExecHostNodeSetParams14hipGraphExec_t14hipGraphNode_tPK17hipHostNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExecHostNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipGraphAddChildGraphNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipGraphAddChildGraphNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipGraphChildGraphNodeGetGraph14hipGraphNode_tP10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipGraphChildGraphNodeGetGraph()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv435hipGraphExecChildGraphNodeSetParams14hipGraphExec_t14hipGraphNode_t10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipGraphExecChildGraphNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipGraphAddEmptyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphAddEmptyNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipGraphAddEventRecordNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphAddEventRecordNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431hipGraphEventRecordNodeGetEvent14hipGraphNode_tP10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphEventRecordNodeGetEvent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431hipGraphEventRecordNodeSetEvent14hipGraphNode_t10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphEventRecordNodeSetEvent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv435hipGraphExecEventRecordNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphExecEventRecordNodeSetEvent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipGraphAddEventWaitNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphAddEventWaitNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphEventWaitNodeGetEvent14hipGraphNode_tP10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphEventWaitNodeGetEvent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphEventWaitNodeSetEvent14hipGraphNode_t10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphEventWaitNodeSetEvent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv433hipGraphExecEventWaitNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphExecEventWaitNodeSetEvent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipGraphAddMemAllocNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tP21hipMemAllocNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemAllocNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphMemAllocNodeGetParams14hipGraphNode_tP21hipMemAllocNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphMemAllocNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipGraphAddMemFreeNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPv"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemFreeNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipGraphMemFreeNodeGetParams14hipGraphNode_tPv"><code class="docutils literal notranslate"><span class="pre">hipGraphMemFreeNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipDeviceGetGraphMemAttributei24hipGraphMemAttributeTypePv"><code class="docutils literal notranslate"><span class="pre">hipDeviceGetGraphMemAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipDeviceSetGraphMemAttributei24hipGraphMemAttributeTypePv"><code class="docutils literal notranslate"><span class="pre">hipDeviceSetGraphMemAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipDeviceGraphMemTrimi"><code class="docutils literal notranslate"><span class="pre">hipDeviceGraphMemTrim()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipUserObjectCreateP15hipUserObject_tPv11hipHostFn_tjj"><code class="docutils literal notranslate"><span class="pre">hipUserObjectCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipUserObjectRelease15hipUserObject_tj"><code class="docutils literal notranslate"><span class="pre">hipUserObjectRelease()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipUserObjectRetain15hipUserObject_tj"><code class="docutils literal notranslate"><span class="pre">hipUserObjectRetain()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipGraphRetainUserObject10hipGraph_t15hipUserObject_tjj"><code class="docutils literal notranslate"><span class="pre">hipGraphRetainUserObject()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipGraphReleaseUserObject10hipGraph_t15hipUserObject_tj"><code class="docutils literal notranslate"><span class="pre">hipGraphReleaseUserObject()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipGraphDebugDotPrint10hipGraph_tPKcj"><code class="docutils literal notranslate"><span class="pre">hipGraphDebugDotPrint()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv432hipGraphKernelNodeCopyAttributes14hipGraphNode_t14hipGraphNode_t"><code class="docutils literal notranslate"><span class="pre">hipGraphKernelNodeCopyAttributes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipGraphNodeSetEnabled14hipGraphExec_t14hipGraphNode_tj"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeSetEnabled()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipGraphNodeGetEnabled14hipGraphExec_t14hipGraphNode_tPj"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeGetEnabled()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv437hipGraphAddExternalSemaphoresWaitNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK34hipExternalSemaphoreWaitNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddExternalSemaphoresWaitNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv439hipGraphAddExternalSemaphoresSignalNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK36hipExternalSemaphoreSignalNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddExternalSemaphoresSignalNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv445hipGraphExternalSemaphoresSignalNodeSetParams14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExternalSemaphoresSignalNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv443hipGraphExternalSemaphoresWaitNodeSetParams14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExternalSemaphoresWaitNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv445hipGraphExternalSemaphoresSignalNodeGetParams14hipGraphNode_tP36hipExternalSemaphoreSignalNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExternalSemaphoresSignalNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv443hipGraphExternalSemaphoresWaitNodeGetParams14hipGraphNode_tP34hipExternalSemaphoreWaitNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExternalSemaphoresWaitNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv449hipGraphExecExternalSemaphoresSignalNodeSetParams14hipGraphExec_t14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExecExternalSemaphoresSignalNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv447hipGraphExecExternalSemaphoresWaitNodeSetParams14hipGraphExec_t14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExecExternalSemaphoresWaitNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipDrvGraphMemcpyNodeGetParams14hipGraphNode_tP12HIP_MEMCPY3D"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphMemcpyNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipDrvGraphMemcpyNodeSetParams14hipGraphNode_tPK12HIP_MEMCPY3D"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphMemcpyNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipDrvGraphAddMemsetNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK15hipMemsetParams8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphAddMemsetNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipDrvGraphAddMemFreeNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t14hipDeviceptr_t"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphAddMemFreeNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv434hipDrvGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tPK12HIP_MEMCPY3D8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphExecMemcpyNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv434hipDrvGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphExecMemsetNodeSetParams()</span></code></a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="graph-management">
<span id="graph-management-reference"></span><h1>Graph management<a class="headerlink" href="#graph-management" title="Link to this heading">#</a></h1>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode">
<span id="_CPPv321hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode"></span><span id="_CPPv221hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode"></span><span id="hipStreamBeginCapture__hipStream_t.hipStreamCaptureMode"></span><span class="target" id="group___graph_1ga826596fabd1d7657721cc3abfb476b10"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipStreamBeginCapture</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span>, <span class="n"><span class="pre">hipStreamCaptureMode</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mode</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode" title="Link to this definition">#</a><br /></dt>
<dd><p>Begins graph capture on a stream. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stream</strong> – <strong>[in]</strong> - Stream to initiate capture. </p></li>
<li><p><strong>mode</strong> – <strong>[in]</strong> - Controls the interaction of this capture sequence with other API calls that are not safe.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv428hipStreamBeginCaptureToGraph11hipStream_t10hipGraph_tPK14hipGraphNode_tPK16hipGraphEdgeData6size_t20hipStreamCaptureMode">
<span id="_CPPv328hipStreamBeginCaptureToGraph11hipStream_t10hipGraph_tPK14hipGraphNode_tPK16hipGraphEdgeData6size_t20hipStreamCaptureMode"></span><span id="_CPPv228hipStreamBeginCaptureToGraph11hipStream_t10hipGraph_tPK14hipGraphNode_tPK16hipGraphEdgeData6size_t20hipStreamCaptureMode"></span><span id="hipStreamBeginCaptureToGraph__hipStream_t.hipGraph_t.hipGraphNode_tCP.hipGraphEdgeDataCP.s.hipStreamCaptureMode"></span><span class="target" id="group___graph_1gabf4070df86154abb92cfc371658d9378"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipStreamBeginCaptureToGraph</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dependencies</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphEdgeData</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dependencyData</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="n"><span class="pre">hipStreamCaptureMode</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mode</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv428hipStreamBeginCaptureToGraph11hipStream_t10hipGraph_tPK14hipGraphNode_tPK16hipGraphEdgeData6size_t20hipStreamCaptureMode" title="Link to this definition">#</a><br /></dt>
<dd><p>Begins graph capture on a stream to an existing graph. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>param “const hipGraphEdgeData* dependencyData” is currently not supported and has to be passed as nullptr. This API is marked as beta, meaning, while this is feature complete, it is still open to changes and may have outstanding issues. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stream</strong> – <strong>[in]</strong> - Stream to initiate capture. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Graph to capture into. </p></li>
<li><p><strong>dependencies</strong> – <strong>[in]</strong> - Dependencies of the first node captured in the stream. Can be NULL if numDependencies is 0. </p></li>
<li><p><strong>dependencyData</strong> – <strong>[in]</strong> - Optional array of data associated with each dependency. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - Number of dependencies. </p></li>
<li><p><strong>mode</strong> – <strong>[in]</strong> - Controls the interaction of this capture sequence with other API calls that are not safe.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipStreamEndCapture11hipStream_tP10hipGraph_t">
<span id="_CPPv319hipStreamEndCapture11hipStream_tP10hipGraph_t"></span><span id="_CPPv219hipStreamEndCapture11hipStream_tP10hipGraph_t"></span><span id="hipStreamEndCapture__hipStream_t.hipGraph_tP"></span><span class="target" id="group___graph_1ga83fc036ee874fbfe066c0fe4fce816b3"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipStreamEndCapture</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraph</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipStreamEndCapture11hipStream_tP10hipGraph_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Ends capture on a stream, returning the captured graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stream</strong> – <strong>[in]</strong> - Stream to end capture. </p></li>
<li><p><strong>pGraph</strong> – <strong>[out]</strong> - Captured graph.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipStreamGetCaptureInfo11hipStream_tP22hipStreamCaptureStatusPy">
<span id="_CPPv323hipStreamGetCaptureInfo11hipStream_tP22hipStreamCaptureStatusPy"></span><span id="_CPPv223hipStreamGetCaptureInfo11hipStream_tP22hipStreamCaptureStatusPy"></span><span id="hipStreamGetCaptureInfo__hipStream_t.hipStreamCaptureStatusP.unsigned-l-lP"></span><span class="target" id="group___graph_1ga5343379e3f86d39aa8527fe0e68abf14"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipStreamGetCaptureInfo</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span>, <span class="n"><span class="pre">hipStreamCaptureStatus</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pCaptureStatus</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pId</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipStreamGetCaptureInfo11hipStream_tP22hipStreamCaptureStatusPy" title="Link to this definition">#</a><br /></dt>
<dd><p>Get capture status of a stream. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stream</strong> – <strong>[in]</strong> - Stream of which to get capture status from. </p></li>
<li><p><strong>pCaptureStatus</strong> – <strong>[out]</strong> - Returns current capture status. </p></li>
<li><p><strong>pId</strong> – <strong>[out]</strong> - Unique capture ID.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorStreamCaptureImplicit</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426hipStreamGetCaptureInfo_v211hipStream_tP22hipStreamCaptureStatusPyP10hipGraph_tPPK14hipGraphNode_tP6size_t">
<span id="_CPPv326hipStreamGetCaptureInfo_v211hipStream_tP22hipStreamCaptureStatusPyP10hipGraph_tPPK14hipGraphNode_tP6size_t"></span><span id="_CPPv226hipStreamGetCaptureInfo_v211hipStream_tP22hipStreamCaptureStatusPyP10hipGraph_tPPK14hipGraphNode_tP6size_t"></span><span id="hipStreamGetCaptureInfo_v2__hipStream_t.hipStreamCaptureStatusP.unsigned-l-lP.hipGraph_tP.hipGraphNode_tCPP.sP"></span><span class="target" id="group___graph_1gab794bda84f171bcd1834dd40ed0949b5"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipStreamGetCaptureInfo_v2</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span>, <span class="n"><span class="pre">hipStreamCaptureStatus</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">captureStatus_out</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">id_out</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">graph_out</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dependencies_out</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">numDependencies_out</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426hipStreamGetCaptureInfo_v211hipStream_tP22hipStreamCaptureStatusPyP10hipGraph_tPPK14hipGraphNode_tP6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Get stream’s capture state. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stream</strong> – <strong>[in]</strong> - Stream of which to get capture status from. </p></li>
<li><p><strong>captureStatus_out</strong> – <strong>[out]</strong> - Returns current capture status. </p></li>
<li><p><strong>id_out</strong> – <strong>[out]</strong> - Unique capture ID. </p></li>
<li><p><strong>graph_out</strong> – <strong>[out]</strong> - Returns the graph being captured into. </p></li>
<li><p><strong>dependencies_out</strong> – <strong>[out]</strong> - Pointer to an array of nodes representing the graphs dependencies. </p></li>
<li><p><strong>numDependencies_out</strong> – <strong>[out]</strong> - Returns size of the array returned in dependencies_out.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorStreamCaptureImplicit</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hipStreamIsCapturing11hipStream_tP22hipStreamCaptureStatus">
<span id="_CPPv320hipStreamIsCapturing11hipStream_tP22hipStreamCaptureStatus"></span><span id="_CPPv220hipStreamIsCapturing11hipStream_tP22hipStreamCaptureStatus"></span><span id="hipStreamIsCapturing__hipStream_t.hipStreamCaptureStatusP"></span><span class="target" id="group___graph_1ga1e6353035e74630a13ad7effd44e3263"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipStreamIsCapturing</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span>, <span class="n"><span class="pre">hipStreamCaptureStatus</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pCaptureStatus</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hipStreamIsCapturing11hipStream_tP22hipStreamCaptureStatus" title="Link to this definition">#</a><br /></dt>
<dd><p>Get stream’s capture state. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stream</strong> – <strong>[in]</strong> - Stream of which to get capture status from. </p></li>
<li><p><strong>pCaptureStatus</strong> – <strong>[out]</strong> - Returns current capture status.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorStreamCaptureImplicit</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv434hipStreamUpdateCaptureDependencies11hipStream_tP14hipGraphNode_t6size_tj">
<span id="_CPPv334hipStreamUpdateCaptureDependencies11hipStream_tP14hipGraphNode_t6size_tj"></span><span id="_CPPv234hipStreamUpdateCaptureDependencies11hipStream_tP14hipGraphNode_t6size_tj"></span><span id="hipStreamUpdateCaptureDependencies__hipStream_t.hipGraphNode_tP.s.unsigned-i"></span><span class="target" id="group___graph_1gaf40ec47e46b07252d36204482ab47c02"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipStreamUpdateCaptureDependencies</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv434hipStreamUpdateCaptureDependencies11hipStream_tP14hipGraphNode_t6size_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Update the set of dependencies in a capturing stream. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream that is being captured. </p></li>
<li><p><strong>dependencies</strong> – <strong>[in]</strong> Pointer to an array of nodes to add/replace. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> Size of the dependencies array. </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Flag to update dependency set. Should be one of the values in enum hipStreamUpdateCaptureDependenciesFlags. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorIllegalState</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv434hipThreadExchangeStreamCaptureModeP20hipStreamCaptureMode">
<span id="_CPPv334hipThreadExchangeStreamCaptureModeP20hipStreamCaptureMode"></span><span id="_CPPv234hipThreadExchangeStreamCaptureModeP20hipStreamCaptureMode"></span><span id="hipThreadExchangeStreamCaptureMode__hipStreamCaptureModeP"></span><span class="target" id="group___graph_1gaa5d692f2f09cad68b7534917e76d8c7f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipThreadExchangeStreamCaptureMode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipStreamCaptureMode</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">mode</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv434hipThreadExchangeStreamCaptureModeP20hipStreamCaptureMode" title="Link to this definition">#</a><br /></dt>
<dd><p>Swaps the stream capture mode of a thread. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>mode</strong> – <strong>[in]</strong> - Pointer to mode value to swap with the current mode. </p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipGraphCreateP10hipGraph_tj">
<span id="_CPPv314hipGraphCreateP10hipGraph_tj"></span><span id="_CPPv214hipGraphCreateP10hipGraph_tj"></span><span id="hipGraphCreate__hipGraph_tP.unsigned-i"></span><span class="target" id="group___graph_1ga0569a00583e14be02790df5531e905d6"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphCreate</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraph</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipGraphCreateP10hipGraph_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraph</strong> – <strong>[out]</strong> - pointer to graph to create. </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> - flags for graph creation, must be 0.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorMemoryAllocation</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415hipGraphDestroy10hipGraph_t">
<span id="_CPPv315hipGraphDestroy10hipGraph_t"></span><span id="_CPPv215hipGraphDestroy10hipGraph_t"></span><span id="hipGraphDestroy__hipGraph_t"></span><span class="target" id="group___graph_1gadf21ff5ddbe98084e0fe3db592290ca7"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphDestroy</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415hipGraphDestroy10hipGraph_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Destroys a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>graph</strong> – <strong>[in]</strong> - instance of graph to destroy.</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipGraphAddDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t">
<span id="_CPPv323hipGraphAddDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t"></span><span id="_CPPv223hipGraphAddDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t"></span><span id="hipGraphAddDependencies__hipGraph_t.hipGraphNode_tCP.hipGraphNode_tCP.s"></span><span class="target" id="group___graph_1ga55de501ca624e30d33a58722b97ab119"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddDependencies</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">from</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">to</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipGraphAddDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Adds dependency edges to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of the graph to add dependencies to. </p></li>
<li><p><strong>from</strong> – <strong>[in]</strong> - Pointer to the graph nodes with dependencies to add from. </p></li>
<li><p><strong>to</strong> – <strong>[in]</strong> - Pointer to the graph nodes to add dependencies to. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - Number of dependencies to add. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426hipGraphRemoveDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t">
<span id="_CPPv326hipGraphRemoveDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t"></span><span id="_CPPv226hipGraphRemoveDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t"></span><span id="hipGraphRemoveDependencies__hipGraph_t.hipGraphNode_tCP.hipGraphNode_tCP.s"></span><span class="target" id="group___graph_1ga3a97f18f0c27e7cd58b404532e940dc6"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphRemoveDependencies</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">from</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">to</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426hipGraphRemoveDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Removes dependency edges from a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of the graph to remove dependencies from. </p></li>
<li><p><strong>from</strong> – <strong>[in]</strong> - Array of nodes that provide the dependencies. </p></li>
<li><p><strong>to</strong> – <strong>[in]</strong> - Array of dependent nodes. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - Number of dependencies to remove. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipGraphGetEdges10hipGraph_tP14hipGraphNode_tP14hipGraphNode_tP6size_t">
<span id="_CPPv316hipGraphGetEdges10hipGraph_tP14hipGraphNode_tP14hipGraphNode_tP6size_t"></span><span id="_CPPv216hipGraphGetEdges10hipGraph_tP14hipGraphNode_tP14hipGraphNode_tP6size_t"></span><span id="hipGraphGetEdges__hipGraph_t.hipGraphNode_tP.hipGraphNode_tP.sP"></span><span class="target" id="group___graph_1gab44fc541c62279d674436289d8f504b1"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphGetEdges</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">from</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">to</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">numEdges</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipGraphGetEdges10hipGraph_tP14hipGraphNode_tP14hipGraphNode_tP6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a graph’s dependency edges. </p>
<p>
from and to may both be NULL, in which case this function only returns the number of edges in numEdges. Otherwise, numEdges entries will be filled in. If numEdges is higher than the actual number of edges, the remaining entries in from and to will be set to NULL, and the number of edges actually returned will be written to numEdges. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of the graph to get the edges from. </p></li>
<li><p><strong>from</strong> – <strong>[out]</strong> - Pointer to the graph nodes to return edge endpoints. </p></li>
<li><p><strong>to</strong> – <strong>[out]</strong> - Pointer to the graph nodes to return edge endpoints. </p></li>
<li><p><strong>numEdges</strong> – <strong>[out]</strong> - Returns number of edges. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipGraphGetNodes10hipGraph_tP14hipGraphNode_tP6size_t">
<span id="_CPPv316hipGraphGetNodes10hipGraph_tP14hipGraphNode_tP6size_t"></span><span id="_CPPv216hipGraphGetNodes10hipGraph_tP14hipGraphNode_tP6size_t"></span><span id="hipGraphGetNodes__hipGraph_t.hipGraphNode_tP.sP"></span><span class="target" id="group___graph_1gaf006701d98164ed3492755bbb19bab83"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphGetNodes</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">nodes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">numNodes</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipGraphGetNodes10hipGraph_tP14hipGraphNode_tP6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a graph’s nodes. </p>
<p>
nodes may be NULL, in which case this function will return the number of nodes in numNodes. Otherwise, numNodes entries will be filled in. If numNodes is higher than the actual number of nodes, the remaining entries in nodes will be set to NULL, and the number of nodes actually obtained will be returned in numNodes. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of graph to get the nodes from. </p></li>
<li><p><strong>nodes</strong> – <strong>[out]</strong> - Pointer to return the graph nodes. </p></li>
<li><p><strong>numNodes</strong> – <strong>[out]</strong> - Returns the number of graph nodes. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hipGraphGetRootNodes10hipGraph_tP14hipGraphNode_tP6size_t">
<span id="_CPPv320hipGraphGetRootNodes10hipGraph_tP14hipGraphNode_tP6size_t"></span><span id="_CPPv220hipGraphGetRootNodes10hipGraph_tP14hipGraphNode_tP6size_t"></span><span id="hipGraphGetRootNodes__hipGraph_t.hipGraphNode_tP.sP"></span><span class="target" id="group___graph_1gafc3f79160be0a919644835388258bd87"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphGetRootNodes</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pRootNodes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNumRootNodes</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hipGraphGetRootNodes10hipGraph_tP14hipGraphNode_tP6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a graph’s root nodes. </p>
<p>
pRootNodes may be NULL, in which case this function will return the number of root nodes in pNumRootNodes. Otherwise, pNumRootNodes entries will be filled in. If pNumRootNodes is higher than the actual number of root nodes, the remaining entries in pRootNodes will be set to NULL, and the number of nodes actually obtained will be returned in pNumRootNodes. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of the graph to get the nodes from. </p></li>
<li><p><strong>pRootNodes</strong> – <strong>[out]</strong> - Pointer to return the graph’s root nodes. </p></li>
<li><p><strong>pNumRootNodes</strong> – <strong>[out]</strong> - Returns the number of graph’s root nodes. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv427hipGraphNodeGetDependencies14hipGraphNode_tP14hipGraphNode_tP6size_t">
<span id="_CPPv327hipGraphNodeGetDependencies14hipGraphNode_tP14hipGraphNode_tP6size_t"></span><span id="_CPPv227hipGraphNodeGetDependencies14hipGraphNode_tP14hipGraphNode_tP6size_t"></span><span id="hipGraphNodeGetDependencies__hipGraphNode_t.hipGraphNode_tP.sP"></span><span class="target" id="group___graph_1ga03f5231946f3e850de44120b3fffd58b"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphNodeGetDependencies</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNumDependencies</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv427hipGraphNodeGetDependencies14hipGraphNode_tP14hipGraphNode_tP6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a node’s dependencies. </p>
<p>
pDependencies may be NULL, in which case this function will return the number of dependencies in pNumDependencies. Otherwise, pNumDependencies entries will be filled in. If pNumDependencies is higher than the actual number of dependencies, the remaining entries in pDependencies will be set to NULL, and the number of nodes actually obtained will be returned in pNumDependencies. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Graph node to get the dependencies from. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[out]</strong> - Pointer to return the dependencies. </p></li>
<li><p><strong>pNumDependencies</strong> – <strong>[out]</strong> - Returns the number of graph node dependencies. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv429hipGraphNodeGetDependentNodes14hipGraphNode_tP14hipGraphNode_tP6size_t">
<span id="_CPPv329hipGraphNodeGetDependentNodes14hipGraphNode_tP14hipGraphNode_tP6size_t"></span><span id="_CPPv229hipGraphNodeGetDependentNodes14hipGraphNode_tP14hipGraphNode_tP6size_t"></span><span id="hipGraphNodeGetDependentNodes__hipGraphNode_t.hipGraphNode_tP.sP"></span><span class="target" id="group___graph_1ga5ca0eedf026ec470d3e7d10724b08253"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphNodeGetDependentNodes</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependentNodes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNumDependentNodes</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv429hipGraphNodeGetDependentNodes14hipGraphNode_tP14hipGraphNode_tP6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a node’s dependent nodes. </p>
<p>
pDependentNodes may be NULL, in which case this function will return the number of dependent nodes in pNumDependentNodes. Otherwise, pNumDependentNodes entries will be filled in. If pNumDependentNodes is higher than the actual number of dependent nodes, the remaining entries in pDependentNodes will be set to NULL, and the number of nodes actually obtained will be returned in pNumDependentNodes. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Graph node to get the dependent nodes from. </p></li>
<li><p><strong>pDependentNodes</strong> – <strong>[out]</strong> - Pointer to return the graph dependent nodes. </p></li>
<li><p><strong>pNumDependentNodes</strong> – <strong>[out]</strong> - Returns the number of graph node dependent nodes. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipGraphNodeGetType14hipGraphNode_tP16hipGraphNodeType">
<span id="_CPPv319hipGraphNodeGetType14hipGraphNode_tP16hipGraphNodeType"></span><span id="_CPPv219hipGraphNodeGetType14hipGraphNode_tP16hipGraphNodeType"></span><span id="hipGraphNodeGetType__hipGraphNode_t.hipGraphNodeTypeP"></span><span class="target" id="group___graph_1ga87c68ae9408a6438d4a1101560ceea11"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphNodeGetType</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipGraphNodeType</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pType</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipGraphNodeGetType14hipGraphNode_tP16hipGraphNodeType" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a node’s type. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Node to get type of. </p></li>
<li><p><strong>pType</strong> – <strong>[out]</strong> - Returns the node’s type. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipGraphDestroyNode14hipGraphNode_t">
<span id="_CPPv319hipGraphDestroyNode14hipGraphNode_t"></span><span id="_CPPv219hipGraphDestroyNode14hipGraphNode_t"></span><span id="hipGraphDestroyNode__hipGraphNode_t"></span><span class="target" id="group___graph_1ga29ce4a5ca318996445984df02b036f01"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphDestroyNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipGraphDestroyNode14hipGraphNode_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Remove a node from the graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>node</strong> – <strong>[in]</strong> - graph node to remove </p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipGraphCloneP10hipGraph_t10hipGraph_t">
<span id="_CPPv313hipGraphCloneP10hipGraph_t10hipGraph_t"></span><span id="_CPPv213hipGraphCloneP10hipGraph_t10hipGraph_t"></span><span id="hipGraphClone__hipGraph_tP.hipGraph_t"></span><span class="target" id="group___graph_1gaf9eec67b896029a35ee31055c247cc77"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphClone</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphClone</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">originalGraph</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipGraphCloneP10hipGraph_t10hipGraph_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Clones a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphClone</strong> – <strong>[out]</strong> - Returns newly created cloned graph. </p></li>
<li><p><strong>originalGraph</strong> – <strong>[in]</strong> - original graph to clone from. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorMemoryAllocation</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipGraphNodeFindInCloneP14hipGraphNode_t14hipGraphNode_t10hipGraph_t">
<span id="_CPPv323hipGraphNodeFindInCloneP14hipGraphNode_t14hipGraphNode_t10hipGraph_t"></span><span id="_CPPv223hipGraphNodeFindInCloneP14hipGraphNode_t14hipGraphNode_t10hipGraph_t"></span><span id="hipGraphNodeFindInClone__hipGraphNode_tP.hipGraphNode_t.hipGraph_t"></span><span class="target" id="group___graph_1ga14d9f4cc7967a4cb06aca0631025495d"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphNodeFindInClone</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNode</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">originalNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">clonedGraph</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipGraphNodeFindInCloneP14hipGraphNode_t14hipGraphNode_t10hipGraph_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Finds a cloned version of a node. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pNode</strong> – <strong>[out]</strong> - Returns the cloned node. </p></li>
<li><p><strong>originalNode</strong> – <strong>[in]</strong> - original node handle. </p></li>
<li><p><strong>clonedGraph</strong> – <strong>[in]</strong> - Cloned graph to query. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipGraphInstantiateP14hipGraphExec_t10hipGraph_tP14hipGraphNode_tPc6size_t">
<span id="_CPPv319hipGraphInstantiateP14hipGraphExec_t10hipGraph_tP14hipGraphNode_tPc6size_t"></span><span id="_CPPv219hipGraphInstantiateP14hipGraphExec_t10hipGraph_tP14hipGraphNode_tPc6size_t"></span><span id="hipGraphInstantiate__hipGraphExec_tP.hipGraph_t.hipGraphNode_tP.cP.s"></span><span class="target" id="group___graph_1gaf5ede92050539e795805f4e2705e6b59"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphInstantiate</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphExec</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pErrorNode</span></span>, <span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pLogBuffer</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">bufferSize</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipGraphInstantiateP14hipGraphExec_t10hipGraph_tP14hipGraphNode_tPc6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates an executable graph from a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphExec</strong> – <strong>[out]</strong> - Pointer to instantiated executable graph. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of graph to instantiate. </p></li>
<li><p><strong>pErrorNode</strong> – <strong>[out]</strong> - Pointer to error node. In case an error occured during graph instantiation, it could modify the corresponding node. </p></li>
<li><p><strong>pLogBuffer</strong> – <strong>[out]</strong> - Pointer to log buffer. </p></li>
<li><p><strong>bufferSize</strong> – <strong>[out]</strong> - Size of the log buffer.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorOutOfMemory</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv428hipGraphInstantiateWithFlagsP14hipGraphExec_t10hipGraph_ty">
<span id="_CPPv328hipGraphInstantiateWithFlagsP14hipGraphExec_t10hipGraph_ty"></span><span id="_CPPv228hipGraphInstantiateWithFlagsP14hipGraphExec_t10hipGraph_ty"></span><span id="hipGraphInstantiateWithFlags__hipGraphExec_tP.hipGraph_t.unsigned-l-l"></span><span class="target" id="group___graph_1ga5f8c8f7c3cf2db57908891b715759028"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphInstantiateWithFlags</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphExec</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv428hipGraphInstantiateWithFlagsP14hipGraphExec_t10hipGraph_ty" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates an executable graph from a graph. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API does not support any of flag and is behaving as hipGraphInstantiate. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphExec</strong> – <strong>[out]</strong> - Pointer to instantiated executable graph. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of graph to instantiate. </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> - Flags to control instantiation. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv429hipGraphInstantiateWithParamsP14hipGraphExec_t10hipGraph_tP25hipGraphInstantiateParams">
<span id="_CPPv329hipGraphInstantiateWithParamsP14hipGraphExec_t10hipGraph_tP25hipGraphInstantiateParams"></span><span id="_CPPv229hipGraphInstantiateWithParamsP14hipGraphExec_t10hipGraph_tP25hipGraphInstantiateParams"></span><span id="hipGraphInstantiateWithParams__hipGraphExec_tP.hipGraph_t.hipGraphInstantiateParamsP"></span><span class="target" id="group___graph_1ga97772b87ae4396a8100890df46890c8c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphInstantiateWithParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphExec</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="n"><span class="pre">hipGraphInstantiateParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">instantiateParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv429hipGraphInstantiateWithParamsP14hipGraphExec_t10hipGraph_tP25hipGraphInstantiateParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates an executable graph from a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphExec</strong> – <strong>[out]</strong> - Pointer to instantiated executable graph. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of graph to instantiate. </p></li>
<li><p><strong>instantiateParams</strong> – <strong>[in]</strong> - Graph instantiation Params </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipGraphLaunch14hipGraphExec_t11hipStream_t">
<span id="_CPPv314hipGraphLaunch14hipGraphExec_t11hipStream_t"></span><span id="_CPPv214hipGraphLaunch14hipGraphExec_t11hipStream_t"></span><span id="hipGraphLaunch__hipGraphExec_t.hipStream_t"></span><span class="target" id="group___graph_1gaa7e8979d0977ded7d554ae272ad557ff"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphLaunch</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graphExec</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipGraphLaunch14hipGraphExec_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Launches an executable graph in the specified stream. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>graphExec</strong> – <strong>[in]</strong> - Instance of executable graph to launch. </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> - Instance of stream in which to launch executable graph. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipGraphUpload14hipGraphExec_t11hipStream_t">
<span id="_CPPv314hipGraphUpload14hipGraphExec_t11hipStream_t"></span><span id="_CPPv214hipGraphUpload14hipGraphExec_t11hipStream_t"></span><span id="hipGraphUpload__hipGraphExec_t.hipStream_t"></span><span class="target" id="group___graph_1ga6626b6ab9daa6358b0c2067272c449ff"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphUpload</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graphExec</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipGraphUpload14hipGraphExec_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Uploads an executable graph to a stream. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>graphExec</strong> – <strong>[in]</strong> - Instance of executable graph to be uploaded. </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> - Instance of stream to which the executable graph is uploaded to. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415hipGraphAddNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tP18hipGraphNodeParams">
<span id="_CPPv315hipGraphAddNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tP18hipGraphNodeParams"></span><span id="_CPPv215hipGraphAddNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tP18hipGraphNodeParams"></span><span id="hipGraphAddNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipGraphNodeParamsP"></span><span class="target" id="group___graph_1gaefab3caa775470618527796774eae6f9"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="n"><span class="pre">hipGraphNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">nodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415hipGraphAddNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tP18hipGraphNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a kernel execution node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to kernel graph node that is created. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of graph to add the created node to. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - Pointer to the dependencies on the kernel execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - Number of dependencies. </p></li>
<li><p><strong>nodeParams</strong> – <strong>[in]</strong> - Pointer to the node parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hipGraphExecGetFlags14hipGraphExec_tPy">
<span id="_CPPv320hipGraphExecGetFlags14hipGraphExec_tPy"></span><span id="_CPPv220hipGraphExecGetFlags14hipGraphExec_tPy"></span><span id="hipGraphExecGetFlags__hipGraphExec_t.unsigned-l-lP"></span><span class="target" id="group___graph_1ga87384379d402af7a44f1464419f65d46"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecGetFlags</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graphExec</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hipGraphExecGetFlags14hipGraphExec_tPy" title="Link to this definition">#</a><br /></dt>
<dd><p>Return the flags of an executable graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>graphExec</strong> – <strong>[in]</strong> - Executable graph to get the flags from. </p></li>
<li><p><strong>flags</strong> – <strong>[out]</strong> - Flags used to instantiate this executable graph. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipGraphNodeSetParams14hipGraphNode_tP18hipGraphNodeParams">
<span id="_CPPv321hipGraphNodeSetParams14hipGraphNode_tP18hipGraphNodeParams"></span><span id="_CPPv221hipGraphNodeSetParams14hipGraphNode_tP18hipGraphNodeParams"></span><span id="hipGraphNodeSetParams__hipGraphNode_t.hipGraphNodeParamsP"></span><span class="target" id="group___graph_1ga74265124259dae4cd413b635e1f33901"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipGraphNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">nodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipGraphNodeSetParams14hipGraphNode_tP18hipGraphNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates parameters of a graph’s node. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters for. </p></li>
<li><p><strong>nodeParams</strong> – <strong>[in]</strong> - Pointer to the parameters to be set. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidDeviceFunction, hipErrorNotSupported. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425hipGraphExecNodeSetParams14hipGraphExec_t14hipGraphNode_tP18hipGraphNodeParams">
<span id="_CPPv325hipGraphExecNodeSetParams14hipGraphExec_t14hipGraphNode_tP18hipGraphNodeParams"></span><span id="_CPPv225hipGraphExecNodeSetParams14hipGraphExec_t14hipGraphNode_tP18hipGraphNodeParams"></span><span id="hipGraphExecNodeSetParams__hipGraphExec_t.hipGraphNode_t.hipGraphNodeParamsP"></span><span class="target" id="group___graph_1ga8bc17629df369e20c61f8fba26b59a23"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipGraphNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">nodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425hipGraphExecNodeSetParams14hipGraphExec_t14hipGraphNode_tP18hipGraphNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates parameters of an executable graph’s node. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>graphExec</strong> – <strong>[in]</strong> - Instance of the executable graph. </p></li>
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters to. </p></li>
<li><p><strong>nodeParams</strong> – <strong>[in]</strong> - Pointer to the parameters to be set. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidDeviceFunction, hipErrorNotSupported. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipGraphExecDestroy14hipGraphExec_t">
<span id="_CPPv319hipGraphExecDestroy14hipGraphExec_t"></span><span id="_CPPv219hipGraphExecDestroy14hipGraphExec_t"></span><span id="hipGraphExecDestroy__hipGraphExec_t"></span><span class="target" id="group___graph_1ga4786c0e6cc8c1cd96a346e0d82177a35"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecDestroy</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graphExec</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipGraphExecDestroy14hipGraphExec_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Destroys an executable graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>graphExec</strong> – <strong>[in]</strong> - Instance of executable graph to destroy.</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipGraphExecUpdate14hipGraphExec_t10hipGraph_tP14hipGraphNode_tP24hipGraphExecUpdateResult">
<span id="_CPPv318hipGraphExecUpdate14hipGraphExec_t10hipGraph_tP14hipGraphNode_tP24hipGraphExecUpdateResult"></span><span id="_CPPv218hipGraphExecUpdate14hipGraphExec_t10hipGraph_tP14hipGraphNode_tP24hipGraphExecUpdateResult"></span><span id="hipGraphExecUpdate__hipGraphExec_t.hipGraph_t.hipGraphNode_tP.hipGraphExecUpdateResultP"></span><span class="target" id="group___graph_1ga0fb2ea2d5d6348888b074a7e44738b98"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecUpdate</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraph</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">hErrorNode_out</span></span>, <span class="n"><span class="pre">hipGraphExecUpdateResult</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">updateResult_out</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipGraphExecUpdate14hipGraphExec_t10hipGraph_tP14hipGraphNode_tP24hipGraphExecUpdateResult" title="Link to this definition">#</a><br /></dt>
<dd><p>Check whether an executable graph can be updated with a graph and perform the update if * possible. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - instance of executable graph to update. </p></li>
<li><p><strong>hGraph</strong> – <strong>[in]</strong> - graph that contains the updated parameters. </p></li>
<li><p><strong>hErrorNode_out</strong> – <strong>[in]</strong> - node which caused the permissibility check to forbid the update. </p></li>
<li><p><strong>updateResult_out</strong> – <strong>[in]</strong> - Return code whether the graph update was performed. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorGraphExecUpdateFailure</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipGraphAddKernelNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK19hipKernelNodeParams">
<span id="_CPPv321hipGraphAddKernelNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK19hipKernelNodeParams"></span><span id="_CPPv221hipGraphAddKernelNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK19hipKernelNodeParams"></span><span id="hipGraphAddKernelNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipKernelNodeParamsCP"></span><span class="target" id="group___graph_1gab5d1eebec77853325f9f9884698b1a67"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddKernelNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipKernelNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipGraphAddKernelNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK19hipKernelNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a kernel execution node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to graph node that is created </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of graph to add the created node to. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - Pointer to the dependencies of the kernel execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - The number of the dependencies. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[in]</strong> - Pointer to the parameters of the kernel execution node. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidDeviceFunction</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv427hipGraphKernelNodeGetParams14hipGraphNode_tP19hipKernelNodeParams">
<span id="_CPPv327hipGraphKernelNodeGetParams14hipGraphNode_tP19hipKernelNodeParams"></span><span id="_CPPv227hipGraphKernelNodeGetParams14hipGraphNode_tP19hipKernelNodeParams"></span><span id="hipGraphKernelNodeGetParams__hipGraphNode_t.hipKernelNodeParamsP"></span><span class="target" id="group___graph_1ga6d46df5efcbfebb98d7b9bfaba4d81b6"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphKernelNodeGetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipKernelNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv427hipGraphKernelNodeGetParams14hipGraphNode_tP19hipKernelNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets kernel node’s parameters. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - instance of the node to get parameters from. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[out]</strong> - pointer to the parameters </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv427hipGraphKernelNodeSetParams14hipGraphNode_tPK19hipKernelNodeParams">
<span id="_CPPv327hipGraphKernelNodeSetParams14hipGraphNode_tPK19hipKernelNodeParams"></span><span id="_CPPv227hipGraphKernelNodeSetParams14hipGraphNode_tPK19hipKernelNodeParams"></span><span id="hipGraphKernelNodeSetParams__hipGraphNode_t.hipKernelNodeParamsCP"></span><span class="target" id="group___graph_1ga00c58e917faec3f6d71cbef95336105b"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphKernelNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipKernelNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv427hipGraphKernelNodeSetParams14hipGraphNode_tPK19hipKernelNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets a kernel node’s parameters. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[in]</strong> - const pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv431hipGraphExecKernelNodeSetParams14hipGraphExec_t14hipGraphNode_tPK19hipKernelNodeParams">
<span id="_CPPv331hipGraphExecKernelNodeSetParams14hipGraphExec_t14hipGraphNode_tPK19hipKernelNodeParams"></span><span id="_CPPv231hipGraphExecKernelNodeSetParams14hipGraphExec_t14hipGraphNode_tPK19hipKernelNodeParams"></span><span id="hipGraphExecKernelNodeSetParams__hipGraphExec_t.hipGraphNode_t.hipKernelNodeParamsCP"></span><span class="target" id="group___graph_1ga5b1918dae65224863b7370e6d4ad3f2a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecKernelNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipKernelNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv431hipGraphExecKernelNodeSetParams14hipGraphExec_t14hipGraphNode_tPK19hipKernelNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the parameters for a kernel node in the given graphExec. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - Instance of the executable graph with the node. </p></li>
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[in]</strong> - const pointer to the kernel node parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424hipDrvGraphAddMemcpyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK12HIP_MEMCPY3D8hipCtx_t">
<span id="_CPPv324hipDrvGraphAddMemcpyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK12HIP_MEMCPY3D8hipCtx_t"></span><span id="_CPPv224hipDrvGraphAddMemcpyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK12HIP_MEMCPY3D8hipCtx_t"></span><span id="hipDrvGraphAddMemcpyNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.HIP_MEMCPY3DCP.hipCtx_t"></span><span class="target" id="group___graph_1ga33aff03ac42d5ccf4bc39d78b91d1397"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDrvGraphAddMemcpyNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">phGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">HIP_MEMCPY3D</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">copyParams</span></span>, <span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ctx</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424hipDrvGraphAddMemcpyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK12HIP_MEMCPY3D8hipCtx_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a memcpy node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>phGraphNode</strong> – <strong>[out]</strong> - Pointer to graph node that is created. </p></li>
<li><p><strong>hGraph</strong> – <strong>[in]</strong> - Instance of graph to add the created node to. </p></li>
<li><p><strong>dependencies</strong> – <strong>[in]</strong> - const pointer to the dependencies of the memcpy execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - The number of dependencies. </p></li>
<li><p><strong>copyParams</strong> – <strong>[in]</strong> - const pointer to the parameters for the memory copy. </p></li>
<li><p><strong>ctx</strong> – <strong>[in]</strong> - context related to current device. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipGraphAddMemcpyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK16hipMemcpy3DParms">
<span id="_CPPv321hipGraphAddMemcpyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK16hipMemcpy3DParms"></span><span id="_CPPv221hipGraphAddMemcpyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK16hipMemcpy3DParms"></span><span id="hipGraphAddMemcpyNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipMemcpy3DParmsCP"></span><span class="target" id="group___graph_1gafc4759560bef7b96ca3eefccde8dd550"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddMemcpyNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemcpy3DParms</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pCopyParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipGraphAddMemcpyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK16hipMemcpy3DParms" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a memcpy node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to graph node that is created. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of graph to add the created node to. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - const pointer to the dependencies of the memcpy execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - The number of dependencies. </p></li>
<li><p><strong>pCopyParams</strong> – <strong>[in]</strong> - const pointer to the parameters for the memory copy. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv427hipGraphMemcpyNodeGetParams14hipGraphNode_tP16hipMemcpy3DParms">
<span id="_CPPv327hipGraphMemcpyNodeGetParams14hipGraphNode_tP16hipMemcpy3DParms"></span><span id="_CPPv227hipGraphMemcpyNodeGetParams14hipGraphNode_tP16hipMemcpy3DParms"></span><span id="hipGraphMemcpyNodeGetParams__hipGraphNode_t.hipMemcpy3DParmsP"></span><span class="target" id="group___graph_1ga72fec822464281fa91a6a3b19556f17d"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphMemcpyNodeGetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipMemcpy3DParms</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv427hipGraphMemcpyNodeGetParams14hipGraphNode_tP16hipMemcpy3DParms" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets a memcpy node’s parameters. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - instance of the node to get parameters from. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[out]</strong> - pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv427hipGraphMemcpyNodeSetParams14hipGraphNode_tPK16hipMemcpy3DParms">
<span id="_CPPv327hipGraphMemcpyNodeSetParams14hipGraphNode_tPK16hipMemcpy3DParms"></span><span id="_CPPv227hipGraphMemcpyNodeSetParams14hipGraphNode_tPK16hipMemcpy3DParms"></span><span id="hipGraphMemcpyNodeSetParams__hipGraphNode_t.hipMemcpy3DParmsCP"></span><span class="target" id="group___graph_1ga098c63fb0fbb57e8d9ee6da0fbfccc70"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphMemcpyNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemcpy3DParms</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv427hipGraphMemcpyNodeSetParams14hipGraphNode_tPK16hipMemcpy3DParms" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets a memcpy node’s parameters. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - instance of the node to set parameters to. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[in]</strong> - const pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv430hipGraphKernelNodeSetAttribute14hipGraphNode_t19hipKernelNodeAttrIDPK22hipKernelNodeAttrValue">
<span id="_CPPv330hipGraphKernelNodeSetAttribute14hipGraphNode_t19hipKernelNodeAttrIDPK22hipKernelNodeAttrValue"></span><span id="_CPPv230hipGraphKernelNodeSetAttribute14hipGraphNode_t19hipKernelNodeAttrIDPK22hipKernelNodeAttrValue"></span><span id="hipGraphKernelNodeSetAttribute__hipGraphNode_t.hipKernelNodeAttrID.hipKernelNodeAttrValueCP"></span><span class="target" id="group___graph_1gacfa93a3e229d03215c3da71f44d70d56"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphKernelNodeSetAttribute</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="n"><span class="pre">hipKernelNodeAttrID</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">attr</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipKernelNodeAttrValue</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">value</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv430hipGraphKernelNodeSetAttribute14hipGraphNode_t19hipKernelNodeAttrIDPK22hipKernelNodeAttrValue" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets a node’s attribute. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hNode</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>attr</strong> – <strong>[in]</strong> - The attribute type to be set. </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> - const pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv430hipGraphKernelNodeGetAttribute14hipGraphNode_t19hipKernelNodeAttrIDP22hipKernelNodeAttrValue">
<span id="_CPPv330hipGraphKernelNodeGetAttribute14hipGraphNode_t19hipKernelNodeAttrIDP22hipKernelNodeAttrValue"></span><span id="_CPPv230hipGraphKernelNodeGetAttribute14hipGraphNode_t19hipKernelNodeAttrIDP22hipKernelNodeAttrValue"></span><span id="hipGraphKernelNodeGetAttribute__hipGraphNode_t.hipKernelNodeAttrID.hipKernelNodeAttrValueP"></span><span class="target" id="group___graph_1gaa3d0f64875d84bea5ddf11b94364d598"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphKernelNodeGetAttribute</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="n"><span class="pre">hipKernelNodeAttrID</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">attr</span></span>, <span class="n"><span class="pre">hipKernelNodeAttrValue</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">value</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv430hipGraphKernelNodeGetAttribute14hipGraphNode_t19hipKernelNodeAttrIDP22hipKernelNodeAttrValue" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets a node’s attribute. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hNode</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>attr</strong> – <strong>[in]</strong> - The attribute type to be set. </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> - const pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv431hipGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tP16hipMemcpy3DParms">
<span id="_CPPv331hipGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tP16hipMemcpy3DParms"></span><span id="_CPPv231hipGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tP16hipMemcpy3DParms"></span><span id="hipGraphExecMemcpyNodeSetParams__hipGraphExec_t.hipGraphNode_t.hipMemcpy3DParmsP"></span><span class="target" id="group___graph_1ga8b2a9b3158e565a1266269fed5f658ae"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecMemcpyNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipMemcpy3DParms</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv431hipGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tP16hipMemcpy3DParms" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the parameters of a memcpy node in the given graphExec. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - Instance of the executable graph with the node. </p></li>
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[in]</strong> - const pointer to the kernel node parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipGraphAddMemcpyNode1DP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPvPKv6size_t13hipMemcpyKind">
<span id="_CPPv323hipGraphAddMemcpyNode1DP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPvPKv6size_t13hipMemcpyKind"></span><span id="_CPPv223hipGraphAddMemcpyNode1DP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPvPKv6size_t13hipMemcpyKind"></span><span id="hipGraphAddMemcpyNode1D__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.voidP.voidCP.s.hipMemcpyKind"></span><span class="target" id="group___graph_1ga05e51a4f490804536f16f5dc83459ca1"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddMemcpyNode1D</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipGraphAddMemcpyNode1DP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPvPKv6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a 1D memcpy node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to graph node that is created. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of graph to add the created node to. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - const pointer to the dependencies of the memcpy execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - The number of dependencies. </p></li>
<li><p><strong>dst</strong> – <strong>[in]</strong> - Pointer to memory address of the destination. </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> - Pointer to memory address of the source. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - Size of the memory to copy. </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> - Type of memory copy. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv429hipGraphMemcpyNodeSetParams1D14hipGraphNode_tPvPKv6size_t13hipMemcpyKind">
<span id="_CPPv329hipGraphMemcpyNodeSetParams1D14hipGraphNode_tPvPKv6size_t13hipMemcpyKind"></span><span id="_CPPv229hipGraphMemcpyNodeSetParams1D14hipGraphNode_tPvPKv6size_t13hipMemcpyKind"></span><span id="hipGraphMemcpyNodeSetParams1D__hipGraphNode_t.voidP.voidCP.s.hipMemcpyKind"></span><span class="target" id="group___graph_1ga3c7686dca4a405d9ec5a8a89615d33a7"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphMemcpyNodeSetParams1D</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv429hipGraphMemcpyNodeSetParams1D14hipGraphNode_tPvPKv6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets a memcpy node’s parameters to perform a 1-dimensional copy. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>dst</strong> – <strong>[in]</strong> - Pointer to memory address of the destination. </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> - Pointer to memory address of the source. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - Size of the memory to copy. </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> - Type of memory copy. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv433hipGraphExecMemcpyNodeSetParams1D14hipGraphExec_t14hipGraphNode_tPvPKv6size_t13hipMemcpyKind">
<span id="_CPPv333hipGraphExecMemcpyNodeSetParams1D14hipGraphExec_t14hipGraphNode_tPvPKv6size_t13hipMemcpyKind"></span><span id="_CPPv233hipGraphExecMemcpyNodeSetParams1D14hipGraphExec_t14hipGraphNode_tPvPKv6size_t13hipMemcpyKind"></span><span id="hipGraphExecMemcpyNodeSetParams1D__hipGraphExec_t.hipGraphNode_t.voidP.voidCP.s.hipMemcpyKind"></span><span class="target" id="group___graph_1ga456ee94786d7923e4e7968dc19a03563"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecMemcpyNodeSetParams1D</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv433hipGraphExecMemcpyNodeSetParams1D14hipGraphExec_t14hipGraphNode_tPvPKv6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the parameters for a memcpy node in the given graphExec to perform a 1-dimensional copy. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - Instance of the executable graph with the node. </p></li>
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>dst</strong> – <strong>[in]</strong> - Pointer to memory address of the destination. </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> - Pointer to memory address of the source. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - Size of the memory to copy. </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> - Type of memory copy. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv431hipGraphAddMemcpyNodeFromSymbolP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPvPKv6size_t6size_t13hipMemcpyKind">
<span id="_CPPv331hipGraphAddMemcpyNodeFromSymbolP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPvPKv6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv231hipGraphAddMemcpyNodeFromSymbolP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPvPKv6size_t6size_t13hipMemcpyKind"></span><span id="hipGraphAddMemcpyNodeFromSymbol__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.voidP.voidCP.s.s.hipMemcpyKind"></span><span class="target" id="group___graph_1ga6f3c6ac9b90264dd297f9ee45fdb5a1c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddMemcpyNodeFromSymbol</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv431hipGraphAddMemcpyNodeFromSymbolP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPvPKv6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a memcpy node to copy from a symbol on the device and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to graph node that is created. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of graph to add the created node to. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - const pointer to the dependencies of the memcpy execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - Number of the dependencies. </p></li>
<li><p><strong>dst</strong> – <strong>[in]</strong> - Pointer to memory address of the destination. </p></li>
<li><p><strong>symbol</strong> – <strong>[in]</strong> - Device symbol address. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - Size of the memory to copy. </p></li>
<li><p><strong>offset</strong> – <strong>[in]</strong> - Offset from start of symbol in bytes. </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> - Type of memory copy. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv437hipGraphMemcpyNodeSetParamsFromSymbol14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind">
<span id="_CPPv337hipGraphMemcpyNodeSetParamsFromSymbol14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv237hipGraphMemcpyNodeSetParamsFromSymbol14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind"></span><span id="hipGraphMemcpyNodeSetParamsFromSymbol__hipGraphNode_t.voidP.voidCP.s.s.hipMemcpyKind"></span><span class="target" id="group___graph_1ga2d8fb8cff71140a7183b488dfd5c5642"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphMemcpyNodeSetParamsFromSymbol</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv437hipGraphMemcpyNodeSetParamsFromSymbol14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets a memcpy node’s parameters to copy from a symbol on the device. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>dst</strong> – <strong>[in]</strong> - Pointer to memory address of the destination. </p></li>
<li><p><strong>symbol</strong> – <strong>[in]</strong> - Device symbol address. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - Size of the memory to copy. </p></li>
<li><p><strong>offset</strong> – <strong>[in]</strong> - Offset from start of symbol in bytes. </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> - Type of memory copy. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv441hipGraphExecMemcpyNodeSetParamsFromSymbol14hipGraphExec_t14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind">
<span id="_CPPv341hipGraphExecMemcpyNodeSetParamsFromSymbol14hipGraphExec_t14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv241hipGraphExecMemcpyNodeSetParamsFromSymbol14hipGraphExec_t14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind"></span><span id="hipGraphExecMemcpyNodeSetParamsFromSymbol__hipGraphExec_t.hipGraphNode_t.voidP.voidCP.s.s.hipMemcpyKind"></span><span class="target" id="group___graph_1gae4d2ca401e05487ff9e9a094abccf792"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecMemcpyNodeSetParamsFromSymbol</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv441hipGraphExecMemcpyNodeSetParamsFromSymbol14hipGraphExec_t14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the parameters for a memcpy node in the given graphExec to copy from a symbol on the. </p>
<p><ul class="simple">
<li><p>device.</p></li>
</ul>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - Instance of the executable graph with the node. </p></li>
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>dst</strong> – <strong>[in]</strong> - Pointer to memory address of the destination. </p></li>
<li><p><strong>symbol</strong> – <strong>[in]</strong> - Device symbol address. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - Size of the memory to copy. </p></li>
<li><p><strong>offset</strong> – <strong>[in]</strong> - Offset from start of symbol in bytes. </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> - Type of memory copy. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv429hipGraphAddMemcpyNodeToSymbolP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPKvPKv6size_t6size_t13hipMemcpyKind">
<span id="_CPPv329hipGraphAddMemcpyNodeToSymbolP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPKvPKv6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv229hipGraphAddMemcpyNodeToSymbolP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPKvPKv6size_t6size_t13hipMemcpyKind"></span><span id="hipGraphAddMemcpyNodeToSymbol__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.voidCP.voidCP.s.s.hipMemcpyKind"></span><span class="target" id="group___graph_1gadc76882339279fa8c70f9666d2088435"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddMemcpyNodeToSymbol</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv429hipGraphAddMemcpyNodeToSymbolP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPKvPKv6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a memcpy node to copy to a symbol on the device and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to graph node that is created. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of graph to add the created node to. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - const pointer to the dependencies on the memcpy execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - Number of dependencies. </p></li>
<li><p><strong>symbol</strong> – <strong>[in]</strong> - Device symbol address. </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> - Pointer to memory address of the src. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - Size of the memory to copy. </p></li>
<li><p><strong>offset</strong> – <strong>[in]</strong> - Offset from start of symbol in bytes. </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> - Type of memory copy. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv435hipGraphMemcpyNodeSetParamsToSymbol14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind">
<span id="_CPPv335hipGraphMemcpyNodeSetParamsToSymbol14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv235hipGraphMemcpyNodeSetParamsToSymbol14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind"></span><span id="hipGraphMemcpyNodeSetParamsToSymbol__hipGraphNode_t.voidCP.voidCP.s.s.hipMemcpyKind"></span><span class="target" id="group___graph_1ga1993d843a450078b3a91f82ff4e0ac02"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphMemcpyNodeSetParamsToSymbol</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv435hipGraphMemcpyNodeSetParamsToSymbol14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets a memcpy node’s parameters to copy to a symbol on the device. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>symbol</strong> – <strong>[in]</strong> - Device symbol address. </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> - Pointer to memory address of the src. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - Size of the memory to copy. </p></li>
<li><p><strong>offset</strong> – <strong>[in]</strong> - Offset from start of symbol in bytes. </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> - Type of memory copy. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv439hipGraphExecMemcpyNodeSetParamsToSymbol14hipGraphExec_t14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind">
<span id="_CPPv339hipGraphExecMemcpyNodeSetParamsToSymbol14hipGraphExec_t14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv239hipGraphExecMemcpyNodeSetParamsToSymbol14hipGraphExec_t14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind"></span><span id="hipGraphExecMemcpyNodeSetParamsToSymbol__hipGraphExec_t.hipGraphNode_t.voidCP.voidCP.s.s.hipMemcpyKind"></span><span class="target" id="group___graph_1ga698fb0f0bd392e4f383ee62e9a61d1e0"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecMemcpyNodeSetParamsToSymbol</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv439hipGraphExecMemcpyNodeSetParamsToSymbol14hipGraphExec_t14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the parameters for a memcpy node in the given graphExec to copy to a symbol on the device. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - Instance of the executable graph with the node. </p></li>
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>symbol</strong> – <strong>[in]</strong> - Device symbol address. </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> - Pointer to memory address of the src. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - Size of the memory to copy. </p></li>
<li><p><strong>offset</strong> – <strong>[in]</strong> - Offset from start of symbol in bytes. </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> - Type of memory copy. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipGraphAddMemsetNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK15hipMemsetParams">
<span id="_CPPv321hipGraphAddMemsetNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK15hipMemsetParams"></span><span id="_CPPv221hipGraphAddMemsetNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK15hipMemsetParams"></span><span id="hipGraphAddMemsetNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipMemsetParamsCP"></span><span class="target" id="group___graph_1gaf195e543467f8b1d313dfb997cb38c58"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddMemsetNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemsetParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pMemsetParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipGraphAddMemsetNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK15hipMemsetParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a memset node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to graph node that is created. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of the graph to add the created node to. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - const pointer to the dependencies on the memset execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - Number of dependencies. </p></li>
<li><p><strong>pMemsetParams</strong> – <strong>[in]</strong> - const pointer to the parameters for the memory set. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv427hipGraphMemsetNodeGetParams14hipGraphNode_tP15hipMemsetParams">
<span id="_CPPv327hipGraphMemsetNodeGetParams14hipGraphNode_tP15hipMemsetParams"></span><span id="_CPPv227hipGraphMemsetNodeGetParams14hipGraphNode_tP15hipMemsetParams"></span><span id="hipGraphMemsetNodeGetParams__hipGraphNode_t.hipMemsetParamsP"></span><span class="target" id="group___graph_1ga9d41c500748b2b774aecb54d7ede5bbd"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphMemsetNodeGetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipMemsetParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv427hipGraphMemsetNodeGetParams14hipGraphNode_tP15hipMemsetParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets a memset node’s parameters. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to get parameters of. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[out]</strong> - Pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv427hipGraphMemsetNodeSetParams14hipGraphNode_tPK15hipMemsetParams">
<span id="_CPPv327hipGraphMemsetNodeSetParams14hipGraphNode_tPK15hipMemsetParams"></span><span id="_CPPv227hipGraphMemsetNodeSetParams14hipGraphNode_tPK15hipMemsetParams"></span><span id="hipGraphMemsetNodeSetParams__hipGraphNode_t.hipMemsetParamsCP"></span><span class="target" id="group___graph_1gad5ab6dd1f9d88c3bc662c271c8aff1a3"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphMemsetNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemsetParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv427hipGraphMemsetNodeSetParams14hipGraphNode_tPK15hipMemsetParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets a memset node’s parameters. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[in]</strong> - Pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv431hipGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams">
<span id="_CPPv331hipGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams"></span><span id="_CPPv231hipGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams"></span><span id="hipGraphExecMemsetNodeSetParams__hipGraphExec_t.hipGraphNode_t.hipMemsetParamsCP"></span><span class="target" id="group___graph_1gaaea31b879fa5eed6a2e12e156020f467"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecMemsetNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemsetParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv431hipGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the parameters for a memset node in the given graphExec. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - Instance of the executable graph with the node. </p></li>
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[in]</strong> - Pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipGraphAddHostNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK17hipHostNodeParams">
<span id="_CPPv319hipGraphAddHostNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK17hipHostNodeParams"></span><span id="_CPPv219hipGraphAddHostNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK17hipHostNodeParams"></span><span id="hipGraphAddHostNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipHostNodeParamsCP"></span><span class="target" id="group___graph_1gaeb6a31dddbc88f6c565edf541de788fa"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddHostNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipHostNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipGraphAddHostNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK17hipHostNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a host execution node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to graph node that is created. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of the graph to add the created node to. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - const pointer to the dependencies of the memset execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - Number of dependencies. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[in]</strong> - Pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425hipGraphHostNodeGetParams14hipGraphNode_tP17hipHostNodeParams">
<span id="_CPPv325hipGraphHostNodeGetParams14hipGraphNode_tP17hipHostNodeParams"></span><span id="_CPPv225hipGraphHostNodeGetParams14hipGraphNode_tP17hipHostNodeParams"></span><span id="hipGraphHostNodeGetParams__hipGraphNode_t.hipHostNodeParamsP"></span><span class="target" id="group___graph_1ga5ee553eb113a3cf55afc9f279b231989"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphHostNodeGetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipHostNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425hipGraphHostNodeGetParams14hipGraphNode_tP17hipHostNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a host node’s parameters. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to get parameters of. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[out]</strong> - Pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425hipGraphHostNodeSetParams14hipGraphNode_tPK17hipHostNodeParams">
<span id="_CPPv325hipGraphHostNodeSetParams14hipGraphNode_tPK17hipHostNodeParams"></span><span id="_CPPv225hipGraphHostNodeSetParams14hipGraphNode_tPK17hipHostNodeParams"></span><span id="hipGraphHostNodeSetParams__hipGraphNode_t.hipHostNodeParamsCP"></span><span class="target" id="group___graph_1ga8e51945beaf0b3b27c3b79a0decd3b80"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphHostNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipHostNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425hipGraphHostNodeSetParams14hipGraphNode_tPK17hipHostNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets a host node’s parameters. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[in]</strong> - Pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv429hipGraphExecHostNodeSetParams14hipGraphExec_t14hipGraphNode_tPK17hipHostNodeParams">
<span id="_CPPv329hipGraphExecHostNodeSetParams14hipGraphExec_t14hipGraphNode_tPK17hipHostNodeParams"></span><span id="_CPPv229hipGraphExecHostNodeSetParams14hipGraphExec_t14hipGraphNode_tPK17hipHostNodeParams"></span><span id="hipGraphExecHostNodeSetParams__hipGraphExec_t.hipGraphNode_t.hipHostNodeParamsCP"></span><span class="target" id="group___graph_1ga4a6f01ac80a51ba37ff0beac10588e61"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecHostNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipHostNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv429hipGraphExecHostNodeSetParams14hipGraphExec_t14hipGraphNode_tPK17hipHostNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the parameters for a host node in the given graphExec. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - Instance of the executable graph with the node. </p></li>
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set parameters of. </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[in]</strong> - Pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425hipGraphAddChildGraphNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipGraph_t">
<span id="_CPPv325hipGraphAddChildGraphNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipGraph_t"></span><span id="_CPPv225hipGraphAddChildGraphNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipGraph_t"></span><span id="hipGraphAddChildGraphNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipGraph_t"></span><span class="target" id="group___graph_1ga215a83cccf00cc4b6a6e43415b68bf4a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddChildGraphNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">childGraph</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425hipGraphAddChildGraphNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipGraph_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a child graph node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to graph node that is created. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of the graph to add the created node. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - const pointer to the dependencies of the memset execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - Number of dependencies. </p></li>
<li><p><strong>childGraph</strong> – <strong>[in]</strong> - Graph to clone into this node </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv430hipGraphChildGraphNodeGetGraph14hipGraphNode_tP10hipGraph_t">
<span id="_CPPv330hipGraphChildGraphNodeGetGraph14hipGraphNode_tP10hipGraph_t"></span><span id="_CPPv230hipGraphChildGraphNodeGetGraph14hipGraphNode_tP10hipGraph_t"></span><span id="hipGraphChildGraphNodeGetGraph__hipGraphNode_t.hipGraph_tP"></span><span class="target" id="group___graph_1gaa3a045ef7065eb0dbaaf0c65cdec8565"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphChildGraphNodeGetGraph</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraph</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv430hipGraphChildGraphNodeGetGraph14hipGraphNode_tP10hipGraph_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets a handle to the embedded graph of a child graph node. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to get child graph of. </p></li>
<li><p><strong>pGraph</strong> – <strong>[out]</strong> - Pointer to get the graph. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv435hipGraphExecChildGraphNodeSetParams14hipGraphExec_t14hipGraphNode_t10hipGraph_t">
<span id="_CPPv335hipGraphExecChildGraphNodeSetParams14hipGraphExec_t14hipGraphNode_t10hipGraph_t"></span><span id="_CPPv235hipGraphExecChildGraphNodeSetParams14hipGraphExec_t14hipGraphNode_t10hipGraph_t"></span><span id="hipGraphExecChildGraphNodeSetParams__hipGraphExec_t.hipGraphNode_t.hipGraph_t"></span><span class="target" id="group___graph_1ga532a7a3b938fc5eed6a5d63d409e60a2"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecChildGraphNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">childGraph</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv435hipGraphExecChildGraphNodeSetParams14hipGraphExec_t14hipGraphNode_t10hipGraph_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates node parameters in the child graph node in the given graphExec. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - instance of the executable graph with the node. </p></li>
<li><p><strong>node</strong> – <strong>[in]</strong> - node from the graph which was used to instantiate graphExec. </p></li>
<li><p><strong>childGraph</strong> – <strong>[in]</strong> - child graph with updated parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hipGraphAddEmptyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t">
<span id="_CPPv320hipGraphAddEmptyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t"></span><span id="_CPPv220hipGraphAddEmptyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t"></span><span id="hipGraphAddEmptyNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s"></span><span class="target" id="group___graph_1gadb06da0ec43f0dd73672d9dcd351df61"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddEmptyNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hipGraphAddEmptyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates an empty node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to graph node that is created. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of the graph the node is added to. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - const pointer to the node dependencies. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - Number of dependencies. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426hipGraphAddEventRecordNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipEvent_t">
<span id="_CPPv326hipGraphAddEventRecordNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipEvent_t"></span><span id="_CPPv226hipGraphAddEventRecordNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipEvent_t"></span><span id="hipGraphAddEventRecordNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipEvent_t"></span><span class="target" id="group___graph_1ga74dca46f970bafa279ec9af41ceca7a9"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddEventRecordNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="n"><span class="pre">hipEvent_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">event</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426hipGraphAddEventRecordNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipEvent_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates an event record node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to graph node that is created. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of the graph the node is added to. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - const pointer to the node dependencies. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - Number of dependencies. </p></li>
<li><p><strong>event</strong> – <strong>[in]</strong> - Event of the node. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv431hipGraphEventRecordNodeGetEvent14hipGraphNode_tP10hipEvent_t">
<span id="_CPPv331hipGraphEventRecordNodeGetEvent14hipGraphNode_tP10hipEvent_t"></span><span id="_CPPv231hipGraphEventRecordNodeGetEvent14hipGraphNode_tP10hipEvent_t"></span><span id="hipGraphEventRecordNodeGetEvent__hipGraphNode_t.hipEvent_tP"></span><span class="target" id="group___graph_1gad5cf984b5b764ca5d715a6673cc5d6cb"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphEventRecordNodeGetEvent</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipEvent_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">event_out</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv431hipGraphEventRecordNodeGetEvent14hipGraphNode_tP10hipEvent_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns the event associated with an event record node. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to get event of. </p></li>
<li><p><strong>event_out</strong> – <strong>[out]</strong> - Pointer to return the event. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv431hipGraphEventRecordNodeSetEvent14hipGraphNode_t10hipEvent_t">
<span id="_CPPv331hipGraphEventRecordNodeSetEvent14hipGraphNode_t10hipEvent_t"></span><span id="_CPPv231hipGraphEventRecordNodeSetEvent14hipGraphNode_t10hipEvent_t"></span><span id="hipGraphEventRecordNodeSetEvent__hipGraphNode_t.hipEvent_t"></span><span class="target" id="group___graph_1gac91ec8eb7a374eb1f7cec45e172efe8c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphEventRecordNodeSetEvent</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipEvent_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">event</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv431hipGraphEventRecordNodeSetEvent14hipGraphNode_t10hipEvent_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets an event record node’s event. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set event to. </p></li>
<li><p><strong>event</strong> – <strong>[in]</strong> - Pointer to the event. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv435hipGraphExecEventRecordNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t">
<span id="_CPPv335hipGraphExecEventRecordNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t"></span><span id="_CPPv235hipGraphExecEventRecordNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t"></span><span id="hipGraphExecEventRecordNodeSetEvent__hipGraphExec_t.hipGraphNode_t.hipEvent_t"></span><span class="target" id="group___graph_1ga9778c1957d72d7ed372a8c2820536066"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecEventRecordNodeSetEvent</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="n"><span class="pre">hipEvent_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">event</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv435hipGraphExecEventRecordNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the event for an event record node in the given graphExec. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - instance of the executable graph with the node. </p></li>
<li><p><strong>hNode</strong> – <strong>[in]</strong> - node from the graph which was used to instantiate graphExec. </p></li>
<li><p><strong>event</strong> – <strong>[in]</strong> - pointer to the event. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424hipGraphAddEventWaitNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipEvent_t">
<span id="_CPPv324hipGraphAddEventWaitNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipEvent_t"></span><span id="_CPPv224hipGraphAddEventWaitNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipEvent_t"></span><span id="hipGraphAddEventWaitNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipEvent_t"></span><span class="target" id="group___graph_1ga1756a144a9ca0b596f81773befdcbc67"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddEventWaitNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="n"><span class="pre">hipEvent_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">event</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424hipGraphAddEventWaitNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipEvent_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates an event wait node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to graph node that is created. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of the graph the node to be added. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - const pointer to the node dependencies. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - Number of dependencies. </p></li>
<li><p><strong>event</strong> – <strong>[in]</strong> - Event for the node. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv429hipGraphEventWaitNodeGetEvent14hipGraphNode_tP10hipEvent_t">
<span id="_CPPv329hipGraphEventWaitNodeGetEvent14hipGraphNode_tP10hipEvent_t"></span><span id="_CPPv229hipGraphEventWaitNodeGetEvent14hipGraphNode_tP10hipEvent_t"></span><span id="hipGraphEventWaitNodeGetEvent__hipGraphNode_t.hipEvent_tP"></span><span class="target" id="group___graph_1gaccfa3e841e4af4a1897b52f47d75a43d"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphEventWaitNodeGetEvent</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipEvent_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">event_out</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv429hipGraphEventWaitNodeGetEvent14hipGraphNode_tP10hipEvent_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns the event associated with an event wait node. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to get event of. </p></li>
<li><p><strong>event_out</strong> – <strong>[out]</strong> - Pointer to return the event. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv429hipGraphEventWaitNodeSetEvent14hipGraphNode_t10hipEvent_t">
<span id="_CPPv329hipGraphEventWaitNodeSetEvent14hipGraphNode_t10hipEvent_t"></span><span id="_CPPv229hipGraphEventWaitNodeSetEvent14hipGraphNode_t10hipEvent_t"></span><span id="hipGraphEventWaitNodeSetEvent__hipGraphNode_t.hipEvent_t"></span><span class="target" id="group___graph_1gac802549bd73126ed736833af7a8c6863"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphEventWaitNodeSetEvent</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipEvent_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">event</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv429hipGraphEventWaitNodeSetEvent14hipGraphNode_t10hipEvent_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets an event wait node’s event. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Instance of the node to set event of. </p></li>
<li><p><strong>event</strong> – <strong>[in]</strong> - Pointer to the event. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv433hipGraphExecEventWaitNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t">
<span id="_CPPv333hipGraphExecEventWaitNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t"></span><span id="_CPPv233hipGraphExecEventWaitNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t"></span><span id="hipGraphExecEventWaitNodeSetEvent__hipGraphExec_t.hipGraphNode_t.hipEvent_t"></span><span class="target" id="group___graph_1gab7649d14c214d61f24e143c1599be9f0"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecEventWaitNodeSetEvent</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="n"><span class="pre">hipEvent_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">event</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv433hipGraphExecEventWaitNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the event for an event record node in the given graphExec. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - instance of the executable graph with the node. </p></li>
<li><p><strong>hNode</strong> – <strong>[in]</strong> - node from the graph which was used to instantiate graphExec. </p></li>
<li><p><strong>event</strong> – <strong>[in]</strong> - pointer to the event. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipGraphAddMemAllocNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tP21hipMemAllocNodeParams">
<span id="_CPPv323hipGraphAddMemAllocNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tP21hipMemAllocNodeParams"></span><span id="_CPPv223hipGraphAddMemAllocNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tP21hipMemAllocNodeParams"></span><span id="hipGraphAddMemAllocNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipMemAllocNodeParamsP"></span><span class="target" id="group___graph_1gae9ea0d05ebde492309f77ba0a23b81a9"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddMemAllocNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="n"><span class="pre">hipMemAllocNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipGraphAddMemAllocNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tP21hipMemAllocNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a memory allocation node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to the graph node to create and add to the graph </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of the graph node to be added </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - Const pointer to the node dependencies </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - The number of dependencies </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[inout]</strong> - Node parameters for memory allocation, returns a pointer to the allocated memory. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv429hipGraphMemAllocNodeGetParams14hipGraphNode_tP21hipMemAllocNodeParams">
<span id="_CPPv329hipGraphMemAllocNodeGetParams14hipGraphNode_tP21hipMemAllocNodeParams"></span><span id="_CPPv229hipGraphMemAllocNodeGetParams14hipGraphNode_tP21hipMemAllocNodeParams"></span><span id="hipGraphMemAllocNodeGetParams__hipGraphNode_t.hipMemAllocNodeParamsP"></span><span class="target" id="group___graph_1ga8fbf788fab0247056ab27ce6eccfb20e"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphMemAllocNodeGetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="n"><span class="pre">hipMemAllocNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv429hipGraphMemAllocNodeGetParams14hipGraphNode_tP21hipMemAllocNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns parameters for memory allocation node. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Memory allocation node to query </p></li>
<li><p><strong>pNodeParams</strong> – <strong>[out]</strong> - Parameters for the specified memory allocation node </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipGraphAddMemFreeNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPv">
<span id="_CPPv322hipGraphAddMemFreeNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPv"></span><span id="_CPPv222hipGraphAddMemFreeNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPv"></span><span id="hipGraphAddMemFreeNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.voidP"></span><span class="target" id="group___graph_1ga70f6f4924c404883cbc0d7cb6ac38100"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddMemFreeNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipGraphAddMemFreeNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPv" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a memory free node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - Pointer to the graph node to create and add to the graph </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - Instance of the graph node to be added </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - Const pointer to the node dependencies </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - The number of dependencies </p></li>
<li><p><strong>dev_ptr</strong> – <strong>[in]</strong> - Pointer to the memory to be freed </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv428hipGraphMemFreeNodeGetParams14hipGraphNode_tPv">
<span id="_CPPv328hipGraphMemFreeNodeGetParams14hipGraphNode_tPv"></span><span id="_CPPv228hipGraphMemFreeNodeGetParams14hipGraphNode_tPv"></span><span id="hipGraphMemFreeNodeGetParams__hipGraphNode_t.voidP"></span><span class="target" id="group___graph_1ga0173b789bbf238185d90733fe36d9a07"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphMemFreeNodeGetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">node</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv428hipGraphMemFreeNodeGetParams14hipGraphNode_tPv" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns parameters for memory free node. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>node</strong> – <strong>[in]</strong> - Memory free node to query </p></li>
<li><p><strong>dev_ptr</strong> – <strong>[out]</strong> - Device pointer of the specified memory free node </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv429hipDeviceGetGraphMemAttributei24hipGraphMemAttributeTypePv">
<span id="_CPPv329hipDeviceGetGraphMemAttributei24hipGraphMemAttributeTypePv"></span><span id="_CPPv229hipDeviceGetGraphMemAttributei24hipGraphMemAttributeTypePv"></span><span id="hipDeviceGetGraphMemAttribute__i.hipGraphMemAttributeType.voidP"></span><span class="target" id="group___graph_1ga5eb353becf0e5a38a376dd7aa13677c0"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDeviceGetGraphMemAttribute</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">device</span></span>, <span class="n"><span class="pre">hipGraphMemAttributeType</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">attr</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">value</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv429hipDeviceGetGraphMemAttributei24hipGraphMemAttributeTypePv" title="Link to this definition">#</a><br /></dt>
<dd><p>Get the mem attribute for graphs. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>device</strong> – <strong>[in]</strong> - Device to get attributes from </p></li>
<li><p><strong>attr</strong> – <strong>[in]</strong> - Attribute type to be queried </p></li>
<li><p><strong>value</strong> – <strong>[out]</strong> - Value of the queried attribute </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidDevice</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv429hipDeviceSetGraphMemAttributei24hipGraphMemAttributeTypePv">
<span id="_CPPv329hipDeviceSetGraphMemAttributei24hipGraphMemAttributeTypePv"></span><span id="_CPPv229hipDeviceSetGraphMemAttributei24hipGraphMemAttributeTypePv"></span><span id="hipDeviceSetGraphMemAttribute__i.hipGraphMemAttributeType.voidP"></span><span class="target" id="group___graph_1ga0921c547b41f9124bb4aec6d5f7dab46"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDeviceSetGraphMemAttribute</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">device</span></span>, <span class="n"><span class="pre">hipGraphMemAttributeType</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">attr</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">value</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv429hipDeviceSetGraphMemAttributei24hipGraphMemAttributeTypePv" title="Link to this definition">#</a><br /></dt>
<dd><p>Set the mem attribute for graphs. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>device</strong> – <strong>[in]</strong> - Device to set attribute of. </p></li>
<li><p><strong>attr</strong> – <strong>[in]</strong> - Attribute type to be set. </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> - Value of the attribute. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidDevice</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipDeviceGraphMemTrimi">
<span id="_CPPv321hipDeviceGraphMemTrimi"></span><span id="_CPPv221hipDeviceGraphMemTrimi"></span><span id="hipDeviceGraphMemTrim__i"></span><span class="target" id="group___graph_1gaf637d203d43c5df6d44a1c509bd43f4d"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDeviceGraphMemTrim</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">device</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipDeviceGraphMemTrimi" title="Link to this definition">#</a><br /></dt>
<dd><p>Free unused memory reserved for graphs on a specific device and return it back to the OS. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>device</strong> – <strong>[in]</strong> - Device for which memory should be trimmed </p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidDevice</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipUserObjectCreateP15hipUserObject_tPv11hipHostFn_tjj">
<span id="_CPPv319hipUserObjectCreateP15hipUserObject_tPv11hipHostFn_tjj"></span><span id="_CPPv219hipUserObjectCreateP15hipUserObject_tPv11hipHostFn_tjj"></span><span id="hipUserObjectCreate__hipUserObject_tP.voidP.hipHostFn_t.unsigned-i.unsigned-i"></span><span class="target" id="group___graph_1ga0c464e200034254c80cdfb9277a55cb5"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipUserObjectCreate</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipUserObject_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">object_out</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ptr</span></span>, <span class="n"><span class="pre">hipHostFn_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">destroy</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">initialRefcount</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipUserObjectCreateP15hipUserObject_tPv11hipHostFn_tjj" title="Link to this definition">#</a><br /></dt>
<dd><p>Create an instance of userObject to manage lifetime of a resource. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>object_out</strong> – <strong>[out]</strong> - pointer to instace of userobj. </p></li>
<li><p><strong>ptr</strong> – <strong>[in]</strong> - pointer to pass to destroy function. </p></li>
<li><p><strong>destroy</strong> – <strong>[in]</strong> - destroy callback to remove resource. </p></li>
<li><p><strong>initialRefcount</strong> – <strong>[in]</strong> - reference to resource. </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> - flags passed to API. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hipUserObjectRelease15hipUserObject_tj">
<span id="_CPPv320hipUserObjectRelease15hipUserObject_tj"></span><span id="_CPPv220hipUserObjectRelease15hipUserObject_tj"></span><span id="hipUserObjectRelease__hipUserObject_t.unsigned-i"></span><span class="target" id="group___graph_1ga6b15f4e7a77f9dbda0d4e3a3febedff5"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipUserObjectRelease</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipUserObject_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">object</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hipUserObjectRelease15hipUserObject_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Release number of references to resource. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>object</strong> – <strong>[in]</strong> - pointer to instace of userobj. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - reference to resource to be retained. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipUserObjectRetain15hipUserObject_tj">
<span id="_CPPv319hipUserObjectRetain15hipUserObject_tj"></span><span id="_CPPv219hipUserObjectRetain15hipUserObject_tj"></span><span id="hipUserObjectRetain__hipUserObject_t.unsigned-i"></span><span class="target" id="group___graph_1ga87b191d080e9b6c9d1ec1bc7990e405d"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipUserObjectRetain</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipUserObject_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">object</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipUserObjectRetain15hipUserObject_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Retain number of references to resource. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>object</strong> – <strong>[in]</strong> - pointer to instace of userobj. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - reference to resource to be retained. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424hipGraphRetainUserObject10hipGraph_t15hipUserObject_tjj">
<span id="_CPPv324hipGraphRetainUserObject10hipGraph_t15hipUserObject_tjj"></span><span id="_CPPv224hipGraphRetainUserObject10hipGraph_t15hipUserObject_tjj"></span><span id="hipGraphRetainUserObject__hipGraph_t.hipUserObject_t.unsigned-i.unsigned-i"></span><span class="target" id="group___graph_1gae158b791c4bb11d2389fc8876aea4a8f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphRetainUserObject</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="n"><span class="pre">hipUserObject_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">object</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424hipGraphRetainUserObject10hipGraph_t15hipUserObject_tjj" title="Link to this definition">#</a><br /></dt>
<dd><p>Retain user object for graphs. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>graph</strong> – <strong>[in]</strong> - pointer to graph to retain the user object for. </p></li>
<li><p><strong>object</strong> – <strong>[in]</strong> - pointer to instace of userobj. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - reference to resource to be retained. </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> - flags passed to API. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425hipGraphReleaseUserObject10hipGraph_t15hipUserObject_tj">
<span id="_CPPv325hipGraphReleaseUserObject10hipGraph_t15hipUserObject_tj"></span><span id="_CPPv225hipGraphReleaseUserObject10hipGraph_t15hipUserObject_tj"></span><span id="hipGraphReleaseUserObject__hipGraph_t.hipUserObject_t.unsigned-i"></span><span class="target" id="group___graph_1ga3287f181e8e0999c6774ac37ba04ee8f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphReleaseUserObject</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="n"><span class="pre">hipUserObject_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">object</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425hipGraphReleaseUserObject10hipGraph_t15hipUserObject_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Release user object from graphs. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>graph</strong> – <strong>[in]</strong> - pointer to graph to retain the user object for. </p></li>
<li><p><strong>object</strong> – <strong>[in]</strong> - pointer to instace of userobj. </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - reference to resource to be retained. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipGraphDebugDotPrint10hipGraph_tPKcj">
<span id="_CPPv321hipGraphDebugDotPrint10hipGraph_tPKcj"></span><span id="_CPPv221hipGraphDebugDotPrint10hipGraph_tPKcj"></span><span id="hipGraphDebugDotPrint__hipGraph_t.cCP.unsigned-i"></span><span class="target" id="group___graph_1gaad520a916f418e08e0ca9078a21e244f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphDebugDotPrint</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">path</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipGraphDebugDotPrint10hipGraph_tPKcj" title="Link to this definition">#</a><br /></dt>
<dd><p>Write a DOT file describing graph structure. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>graph</strong> – <strong>[in]</strong> - graph object for which DOT file has to be generated. </p></li>
<li><p><strong>path</strong> – <strong>[in]</strong> - path to write the DOT file. </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> - Flags from hipGraphDebugDotFlags to get additional node information. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorOperatingSystem</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv432hipGraphKernelNodeCopyAttributes14hipGraphNode_t14hipGraphNode_t">
<span id="_CPPv332hipGraphKernelNodeCopyAttributes14hipGraphNode_t14hipGraphNode_t"></span><span id="_CPPv232hipGraphKernelNodeCopyAttributes14hipGraphNode_t14hipGraphNode_t"></span><span id="hipGraphKernelNodeCopyAttributes__hipGraphNode_t.hipGraphNode_t"></span><span class="target" id="group___graph_1ga6fd9af1ec50bc34c6500fe276d05946f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphKernelNodeCopyAttributes</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hSrc</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hDst</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv432hipGraphKernelNodeCopyAttributes14hipGraphNode_t14hipGraphNode_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies attributes from source node to destination node. </p>
<p>Copies attributes from source node to destination node. Both node must have the same context.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hDst</strong> – <strong>[out]</strong> - Destination node. </p></li>
<li><p><strong>hSrc</strong> – <strong>[in]</strong> - Source node. For list of attributes see hipKernelNodeAttrID.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidContext</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipGraphNodeSetEnabled14hipGraphExec_t14hipGraphNode_tj">
<span id="_CPPv322hipGraphNodeSetEnabled14hipGraphExec_t14hipGraphNode_tj"></span><span id="_CPPv222hipGraphNodeSetEnabled14hipGraphExec_t14hipGraphNode_tj"></span><span id="hipGraphNodeSetEnabled__hipGraphExec_t.hipGraphNode_t.unsigned-i"></span><span class="target" id="group___graph_1ga8902200d9fed1df7644fc7a51c4d327b"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphNodeSetEnabled</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">isEnabled</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipGraphNodeSetEnabled14hipGraphExec_t14hipGraphNode_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Enables or disables the specified node in the given graphExec. </p>
<p>Sets hNode to be either enabled or disabled. Disabled nodes are functionally equivalent to empty nodes until they are reenabled. Existing node parameters are not affected by disabling/enabling the node.</p>
<p>The node is identified by the corresponding hNode in the non-executable graph, from which the executable graph was instantiated.</p>
<p>hNode must not have been removed from the original graph.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Currently only kernel, memset and memcpy nodes are supported.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - The executable graph in which to set the specified node. </p></li>
<li><p><strong>hNode</strong> – <strong>[in]</strong> - Node from the graph from which graphExec was instantiated. </p></li>
<li><p><strong>isEnabled</strong> – <strong>[in]</strong> - Node is enabled if != 0, otherwise the node is disabled.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipGraphNodeGetEnabled14hipGraphExec_t14hipGraphNode_tPj">
<span id="_CPPv322hipGraphNodeGetEnabled14hipGraphExec_t14hipGraphNode_tPj"></span><span id="_CPPv222hipGraphNodeGetEnabled14hipGraphExec_t14hipGraphNode_tPj"></span><span id="hipGraphNodeGetEnabled__hipGraphExec_t.hipGraphNode_t.unsigned-iP"></span><span class="target" id="group___graph_1ga207d60e261a723f81dd573423602239c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphNodeGetEnabled</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">isEnabled</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipGraphNodeGetEnabled14hipGraphExec_t14hipGraphNode_tPj" title="Link to this definition">#</a><br /></dt>
<dd><p>Query whether a node in the given graphExec is enabled. </p>
<p>Sets isEnabled to 1 if hNode is enabled, or 0 if it is disabled.</p>
<p>The node is identified by the corresponding node in the non-executable graph, from which the executable graph was instantiated.</p>
<p>hNode must not have been removed from the original graph.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Currently only kernel, memset and memcpy nodes are supported.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - The executable graph in which to set the specified node. </p></li>
<li><p><strong>hNode</strong> – <strong>[in]</strong> - Node from the graph from which graphExec was instantiated. </p></li>
<li><p><strong>isEnabled</strong> – <strong>[out]</strong> - Location to return the enabled status of the node.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv437hipGraphAddExternalSemaphoresWaitNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK34hipExternalSemaphoreWaitNodeParams">
<span id="_CPPv337hipGraphAddExternalSemaphoresWaitNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK34hipExternalSemaphoreWaitNodeParams"></span><span id="_CPPv237hipGraphAddExternalSemaphoresWaitNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK34hipExternalSemaphoreWaitNodeParams"></span><span id="hipGraphAddExternalSemaphoresWaitNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipExternalSemaphoreWaitNodeParamsCP"></span><span class="target" id="group___graph_1gac086da9e2ee7561a7b47ce4f7276faf2"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddExternalSemaphoresWaitNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipExternalSemaphoreWaitNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">nodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv437hipGraphAddExternalSemaphoresWaitNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK34hipExternalSemaphoreWaitNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a external semaphor wait node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - pointer to the graph node to create. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - instance of the graph to add the created node. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - const pointer to the dependencies on the memset execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - the number of the dependencies. </p></li>
<li><p><strong>nodeParams</strong> – <strong>[in]</strong> -pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv439hipGraphAddExternalSemaphoresSignalNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK36hipExternalSemaphoreSignalNodeParams">
<span id="_CPPv339hipGraphAddExternalSemaphoresSignalNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK36hipExternalSemaphoreSignalNodeParams"></span><span id="_CPPv239hipGraphAddExternalSemaphoresSignalNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK36hipExternalSemaphoreSignalNodeParams"></span><span id="hipGraphAddExternalSemaphoresSignalNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipExternalSemaphoreSignalNodeParamsCP"></span><span class="target" id="group___graph_1ga49886f3a676840be5b5eea99af87d4bf"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphAddExternalSemaphoresSignalNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">graph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pDependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipExternalSemaphoreSignalNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">nodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv439hipGraphAddExternalSemaphoresSignalNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK36hipExternalSemaphoreSignalNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a external semaphor signal node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pGraphNode</strong> – <strong>[out]</strong> - pointer to the graph node to create. </p></li>
<li><p><strong>graph</strong> – <strong>[in]</strong> - instance of the graph to add the created node. </p></li>
<li><p><strong>pDependencies</strong> – <strong>[in]</strong> - const pointer to the dependencies on the memset execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - the number of the dependencies. </p></li>
<li><p><strong>nodeParams</strong> – <strong>[in]</strong> -pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv445hipGraphExternalSemaphoresSignalNodeSetParams14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams">
<span id="_CPPv345hipGraphExternalSemaphoresSignalNodeSetParams14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams"></span><span id="_CPPv245hipGraphExternalSemaphoresSignalNodeSetParams14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams"></span><span id="hipGraphExternalSemaphoresSignalNodeSetParams__hipGraphNode_t.hipExternalSemaphoreSignalNodeParamsCP"></span><span class="target" id="group___graph_1ga25d077916d21a34bf5bfb7f7cc13eaf8"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExternalSemaphoresSignalNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipExternalSemaphoreSignalNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">nodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv445hipGraphExternalSemaphoresSignalNodeSetParams14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates node parameters in the external semaphore signal node. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hNode</strong> – <strong>[in]</strong> - Node from the graph from which graphExec was instantiated. </p></li>
<li><p><strong>nodeParams</strong> – <strong>[in]</strong> - Pointer to the params to be set. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv443hipGraphExternalSemaphoresWaitNodeSetParams14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams">
<span id="_CPPv343hipGraphExternalSemaphoresWaitNodeSetParams14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams"></span><span id="_CPPv243hipGraphExternalSemaphoresWaitNodeSetParams14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams"></span><span id="hipGraphExternalSemaphoresWaitNodeSetParams__hipGraphNode_t.hipExternalSemaphoreWaitNodeParamsCP"></span><span class="target" id="group___graph_1ga993155e50b96e92f383bdcf62aa2d099"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExternalSemaphoresWaitNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipExternalSemaphoreWaitNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">nodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv443hipGraphExternalSemaphoresWaitNodeSetParams14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates node parameters in the external semaphore wait node. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hNode</strong> – <strong>[in]</strong> - Node from the graph from which graphExec was instantiated. </p></li>
<li><p><strong>nodeParams</strong> – <strong>[in]</strong> - Pointer to the params to be set. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv445hipGraphExternalSemaphoresSignalNodeGetParams14hipGraphNode_tP36hipExternalSemaphoreSignalNodeParams">
<span id="_CPPv345hipGraphExternalSemaphoresSignalNodeGetParams14hipGraphNode_tP36hipExternalSemaphoreSignalNodeParams"></span><span id="_CPPv245hipGraphExternalSemaphoresSignalNodeGetParams14hipGraphNode_tP36hipExternalSemaphoreSignalNodeParams"></span><span id="hipGraphExternalSemaphoresSignalNodeGetParams__hipGraphNode_t.hipExternalSemaphoreSignalNodeParamsP"></span><span class="target" id="group___graph_1ga5fce7651a7e9333ea23687f346d70c7f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExternalSemaphoresSignalNodeGetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="n"><span class="pre">hipExternalSemaphoreSignalNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">params_out</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv445hipGraphExternalSemaphoresSignalNodeGetParams14hipGraphNode_tP36hipExternalSemaphoreSignalNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns external semaphore signal node params. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hNode</strong> – <strong>[in]</strong> - Node from the graph from which graphExec was instantiated. </p></li>
<li><p><strong>params_out</strong> – <strong>[out]</strong> - Pointer to params. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv443hipGraphExternalSemaphoresWaitNodeGetParams14hipGraphNode_tP34hipExternalSemaphoreWaitNodeParams">
<span id="_CPPv343hipGraphExternalSemaphoresWaitNodeGetParams14hipGraphNode_tP34hipExternalSemaphoreWaitNodeParams"></span><span id="_CPPv243hipGraphExternalSemaphoresWaitNodeGetParams14hipGraphNode_tP34hipExternalSemaphoreWaitNodeParams"></span><span id="hipGraphExternalSemaphoresWaitNodeGetParams__hipGraphNode_t.hipExternalSemaphoreWaitNodeParamsP"></span><span class="target" id="group___graph_1gaf6e73d6a19ca850f395febf4adb46ce7"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExternalSemaphoresWaitNodeGetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="n"><span class="pre">hipExternalSemaphoreWaitNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">params_out</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv443hipGraphExternalSemaphoresWaitNodeGetParams14hipGraphNode_tP34hipExternalSemaphoreWaitNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns external semaphore wait node params. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hNode</strong> – <strong>[in]</strong> - Node from the graph from which graphExec was instantiated. </p></li>
<li><p><strong>params_out</strong> – <strong>[out]</strong> - Pointer to params. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv449hipGraphExecExternalSemaphoresSignalNodeSetParams14hipGraphExec_t14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams">
<span id="_CPPv349hipGraphExecExternalSemaphoresSignalNodeSetParams14hipGraphExec_t14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams"></span><span id="_CPPv249hipGraphExecExternalSemaphoresSignalNodeSetParams14hipGraphExec_t14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams"></span><span id="hipGraphExecExternalSemaphoresSignalNodeSetParams__hipGraphExec_t.hipGraphNode_t.hipExternalSemaphoreSignalNodeParamsCP"></span><span class="target" id="group___graph_1ga69757fcf41c1939bb698f3e31913803b"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecExternalSemaphoresSignalNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipExternalSemaphoreSignalNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">nodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv449hipGraphExecExternalSemaphoresSignalNodeSetParams14hipGraphExec_t14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates node parameters in the external semaphore signal node in the given graphExec. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - The executable graph in which to set the specified node. </p></li>
<li><p><strong>hNode</strong> – <strong>[in]</strong> - Node from the graph from which graphExec was instantiated. </p></li>
<li><p><strong>nodeParams</strong> – <strong>[in]</strong> - Pointer to the params to be set. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv447hipGraphExecExternalSemaphoresWaitNodeSetParams14hipGraphExec_t14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams">
<span id="_CPPv347hipGraphExecExternalSemaphoresWaitNodeSetParams14hipGraphExec_t14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams"></span><span id="_CPPv247hipGraphExecExternalSemaphoresWaitNodeSetParams14hipGraphExec_t14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams"></span><span id="hipGraphExecExternalSemaphoresWaitNodeSetParams__hipGraphExec_t.hipGraphNode_t.hipExternalSemaphoreWaitNodeParamsCP"></span><span class="target" id="group___graph_1ga4a2826775ca03a0302005e81587a634f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGraphExecExternalSemaphoresWaitNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipExternalSemaphoreWaitNodeParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">nodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv447hipGraphExecExternalSemaphoresWaitNodeSetParams14hipGraphExec_t14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams" title="Link to this definition">#</a><br /></dt>
<dd><p>Updates node parameters in the external semaphore wait node in the given graphExec. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - The executable graph in which to set the specified node. </p></li>
<li><p><strong>hNode</strong> – <strong>[in]</strong> - Node from the graph from which graphExec was instantiated. </p></li>
<li><p><strong>nodeParams</strong> – <strong>[in]</strong> - Pointer to the params to be set. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv430hipDrvGraphMemcpyNodeGetParams14hipGraphNode_tP12HIP_MEMCPY3D">
<span id="_CPPv330hipDrvGraphMemcpyNodeGetParams14hipGraphNode_tP12HIP_MEMCPY3D"></span><span id="_CPPv230hipDrvGraphMemcpyNodeGetParams14hipGraphNode_tP12HIP_MEMCPY3D"></span><span id="hipDrvGraphMemcpyNodeGetParams__hipGraphNode_t.HIP_MEMCPY3DP"></span><span class="target" id="group___graph_1ga08610f43c866c43ec03a62075f9f05b4"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDrvGraphMemcpyNodeGetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="n"><span class="pre">HIP_MEMCPY3D</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">nodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv430hipDrvGraphMemcpyNodeGetParams14hipGraphNode_tP12HIP_MEMCPY3D" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets a memcpy node’s parameters. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hNode</strong> – <strong>[in]</strong> - instance of the node to get parameters from. </p></li>
<li><p><strong>nodeParams</strong> – <strong>[out]</strong> - pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv430hipDrvGraphMemcpyNodeSetParams14hipGraphNode_tPK12HIP_MEMCPY3D">
<span id="_CPPv330hipDrvGraphMemcpyNodeSetParams14hipGraphNode_tPK12HIP_MEMCPY3D"></span><span id="_CPPv230hipDrvGraphMemcpyNodeSetParams14hipGraphNode_tPK12HIP_MEMCPY3D"></span><span id="hipDrvGraphMemcpyNodeSetParams__hipGraphNode_t.HIP_MEMCPY3DCP"></span><span class="target" id="group___graph_1ga71199fde02ca746f24c73ed224a5cefb"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDrvGraphMemcpyNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">HIP_MEMCPY3D</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">nodeParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv430hipDrvGraphMemcpyNodeSetParams14hipGraphNode_tPK12HIP_MEMCPY3D" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets a memcpy node’s parameters. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hNode</strong> – <strong>[in]</strong> - instance of the node to Set parameters for. </p></li>
<li><p><strong>nodeParams</strong> – <strong>[out]</strong> - pointer to the parameters. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424hipDrvGraphAddMemsetNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK15hipMemsetParams8hipCtx_t">
<span id="_CPPv324hipDrvGraphAddMemsetNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK15hipMemsetParams8hipCtx_t"></span><span id="_CPPv224hipDrvGraphAddMemsetNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK15hipMemsetParams8hipCtx_t"></span><span id="hipDrvGraphAddMemsetNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipMemsetParamsCP.hipCtx_t"></span><span class="target" id="group___graph_1ga66548119eaa99f46d32073955239b2f2"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDrvGraphAddMemsetNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">phGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemsetParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">memsetParams</span></span>, <span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ctx</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424hipDrvGraphAddMemsetNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK15hipMemsetParams8hipCtx_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a memset node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>phGraphNode</strong> – <strong>[out]</strong> - pointer to graph node to create. </p></li>
<li><p><strong>hGraph</strong> – <strong>[in]</strong> - instance of graph to add the created node to. </p></li>
<li><p><strong>dependencies</strong> – <strong>[in]</strong> - const pointer to the dependencies on the memset execution node. </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - number of the dependencies. </p></li>
<li><p><strong>memsetParams</strong> – <strong>[in]</strong> - const pointer to the parameters for the memory set. </p></li>
<li><p><strong>ctx</strong> – <strong>[in]</strong> - cotext related to current device. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425hipDrvGraphAddMemFreeNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t14hipDeviceptr_t">
<span id="_CPPv325hipDrvGraphAddMemFreeNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t14hipDeviceptr_t"></span><span id="_CPPv225hipDrvGraphAddMemFreeNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t14hipDeviceptr_t"></span><span id="hipDrvGraphAddMemFreeNode__hipGraphNode_tP.hipGraph_t.hipGraphNode_tCP.s.hipDeviceptr_t"></span><span class="target" id="group___graph_1ga55f78947cfc9b1844672f11d197ddeed"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDrvGraphAddMemFreeNode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">phGraphNode</span></span>, <span class="n"><span class="pre">hipGraph_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraph</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dependencies</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDependencies</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dptr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425hipDrvGraphAddMemFreeNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t14hipDeviceptr_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a memory free node and adds it to a graph. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>phGraphNode</strong> – <strong>[out]</strong> - Pointer to the graph node to create and add to the graph </p></li>
<li><p><strong>hGraph</strong> – <strong>[in]</strong> - Instance of the graph the node to be added </p></li>
<li><p><strong>dependencies</strong> – <strong>[in]</strong> - Const pointer to the node dependencies </p></li>
<li><p><strong>numDependencies</strong> – <strong>[in]</strong> - The number of dependencies </p></li>
<li><p><strong>dptr</strong> – <strong>[in]</strong> - Pointer to the memory to be freed </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv434hipDrvGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tPK12HIP_MEMCPY3D8hipCtx_t">
<span id="_CPPv334hipDrvGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tPK12HIP_MEMCPY3D8hipCtx_t"></span><span id="_CPPv234hipDrvGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tPK12HIP_MEMCPY3D8hipCtx_t"></span><span id="hipDrvGraphExecMemcpyNodeSetParams__hipGraphExec_t.hipGraphNode_t.HIP_MEMCPY3DCP.hipCtx_t"></span><span class="target" id="group___graph_1ga8173e6bad29de6ac5eab05463dda127c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDrvGraphExecMemcpyNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">HIP_MEMCPY3D</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">copyParams</span></span>, <span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ctx</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv434hipDrvGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tPK12HIP_MEMCPY3D8hipCtx_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the parameters for a memcpy node in the given graphExec. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - instance of the executable graph with the node. </p></li>
<li><p><strong>hNode</strong> – <strong>[in]</strong> - instance of the node to set parameters to. </p></li>
<li><p><strong>copyParams</strong> – <strong>[in]</strong> - const pointer to the memcpy node params. </p></li>
<li><p><strong>ctx</strong> – <strong>[in]</strong> - cotext related to current device. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv434hipDrvGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams8hipCtx_t">
<span id="_CPPv334hipDrvGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams8hipCtx_t"></span><span id="_CPPv234hipDrvGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams8hipCtx_t"></span><span id="hipDrvGraphExecMemsetNodeSetParams__hipGraphExec_t.hipGraphNode_t.hipMemsetParamsCP.hipCtx_t"></span><span class="target" id="group___graph_1ga037dcdd56f1ebe098380f2ba0b88e539"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDrvGraphExecMemsetNodeSetParams</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipGraphExec_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hGraphExec</span></span>, <span class="n"><span class="pre">hipGraphNode_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hNode</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemsetParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">memsetParams</span></span>, <span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ctx</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv434hipDrvGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams8hipCtx_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the parameters for a memset node in the given graphExec. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hGraphExec</strong> – <strong>[in]</strong> - instance of the executable graph with the node. </p></li>
<li><p><strong>hNode</strong> – <strong>[in]</strong> - instance of the node to set parameters to. </p></li>
<li><p><strong>memsetParams</strong> – <strong>[in]</strong> - pointer to the parameters. </p></li>
<li><p><strong>ctx</strong> – <strong>[in]</strong> - cotext related to current device. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="callback_activity_apis.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Callback activity APIs</p>
      </div>
    </a>
    <a class="right-next"
       href="graphics_interoperability.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Graphics interoperability</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode"><code class="docutils literal notranslate"><span class="pre">hipStreamBeginCapture()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipStreamBeginCaptureToGraph11hipStream_t10hipGraph_tPK14hipGraphNode_tPK16hipGraphEdgeData6size_t20hipStreamCaptureMode"><code class="docutils literal notranslate"><span class="pre">hipStreamBeginCaptureToGraph()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipStreamEndCapture11hipStream_tP10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipStreamEndCapture()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipStreamGetCaptureInfo11hipStream_tP22hipStreamCaptureStatusPy"><code class="docutils literal notranslate"><span class="pre">hipStreamGetCaptureInfo()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipStreamGetCaptureInfo_v211hipStream_tP22hipStreamCaptureStatusPyP10hipGraph_tPPK14hipGraphNode_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipStreamGetCaptureInfo_v2()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipStreamIsCapturing11hipStream_tP22hipStreamCaptureStatus"><code class="docutils literal notranslate"><span class="pre">hipStreamIsCapturing()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv434hipStreamUpdateCaptureDependencies11hipStream_tP14hipGraphNode_t6size_tj"><code class="docutils literal notranslate"><span class="pre">hipStreamUpdateCaptureDependencies()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv434hipThreadExchangeStreamCaptureModeP20hipStreamCaptureMode"><code class="docutils literal notranslate"><span class="pre">hipThreadExchangeStreamCaptureMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipGraphCreateP10hipGraph_tj"><code class="docutils literal notranslate"><span class="pre">hipGraphCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipGraphDestroy10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipGraphDestroy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipGraphAddDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphAddDependencies()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipGraphRemoveDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphRemoveDependencies()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipGraphGetEdges10hipGraph_tP14hipGraphNode_tP14hipGraphNode_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphGetEdges()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipGraphGetNodes10hipGraph_tP14hipGraphNode_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphGetNodes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipGraphGetRootNodes10hipGraph_tP14hipGraphNode_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphGetRootNodes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphNodeGetDependencies14hipGraphNode_tP14hipGraphNode_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeGetDependencies()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphNodeGetDependentNodes14hipGraphNode_tP14hipGraphNode_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeGetDependentNodes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipGraphNodeGetType14hipGraphNode_tP16hipGraphNodeType"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeGetType()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipGraphDestroyNode14hipGraphNode_t"><code class="docutils literal notranslate"><span class="pre">hipGraphDestroyNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipGraphCloneP10hipGraph_t10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipGraphClone()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipGraphNodeFindInCloneP14hipGraphNode_t14hipGraphNode_t10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeFindInClone()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipGraphInstantiateP14hipGraphExec_t10hipGraph_tP14hipGraphNode_tPc6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphInstantiate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipGraphInstantiateWithFlagsP14hipGraphExec_t10hipGraph_ty"><code class="docutils literal notranslate"><span class="pre">hipGraphInstantiateWithFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphInstantiateWithParamsP14hipGraphExec_t10hipGraph_tP25hipGraphInstantiateParams"><code class="docutils literal notranslate"><span class="pre">hipGraphInstantiateWithParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipGraphLaunch14hipGraphExec_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipGraphLaunch()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipGraphUpload14hipGraphExec_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipGraphUpload()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipGraphAddNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tP18hipGraphNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipGraphExecGetFlags14hipGraphExec_tPy"><code class="docutils literal notranslate"><span class="pre">hipGraphExecGetFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipGraphNodeSetParams14hipGraphNode_tP18hipGraphNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipGraphExecNodeSetParams14hipGraphExec_t14hipGraphNode_tP18hipGraphNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExecNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipGraphExecDestroy14hipGraphExec_t"><code class="docutils literal notranslate"><span class="pre">hipGraphExecDestroy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipGraphExecUpdate14hipGraphExec_t10hipGraph_tP14hipGraphNode_tP24hipGraphExecUpdateResult"><code class="docutils literal notranslate"><span class="pre">hipGraphExecUpdate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipGraphAddKernelNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK19hipKernelNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddKernelNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphKernelNodeGetParams14hipGraphNode_tP19hipKernelNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphKernelNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphKernelNodeSetParams14hipGraphNode_tPK19hipKernelNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphKernelNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431hipGraphExecKernelNodeSetParams14hipGraphExec_t14hipGraphNode_tPK19hipKernelNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExecKernelNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipDrvGraphAddMemcpyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK12HIP_MEMCPY3D8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphAddMemcpyNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipGraphAddMemcpyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK16hipMemcpy3DParms"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemcpyNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphMemcpyNodeGetParams14hipGraphNode_tP16hipMemcpy3DParms"><code class="docutils literal notranslate"><span class="pre">hipGraphMemcpyNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphMemcpyNodeSetParams14hipGraphNode_tPK16hipMemcpy3DParms"><code class="docutils literal notranslate"><span class="pre">hipGraphMemcpyNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipGraphKernelNodeSetAttribute14hipGraphNode_t19hipKernelNodeAttrIDPK22hipKernelNodeAttrValue"><code class="docutils literal notranslate"><span class="pre">hipGraphKernelNodeSetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipGraphKernelNodeGetAttribute14hipGraphNode_t19hipKernelNodeAttrIDP22hipKernelNodeAttrValue"><code class="docutils literal notranslate"><span class="pre">hipGraphKernelNodeGetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431hipGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tP16hipMemcpy3DParms"><code class="docutils literal notranslate"><span class="pre">hipGraphExecMemcpyNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipGraphAddMemcpyNode1DP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPvPKv6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemcpyNode1D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphMemcpyNodeSetParams1D14hipGraphNode_tPvPKv6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphMemcpyNodeSetParams1D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv433hipGraphExecMemcpyNodeSetParams1D14hipGraphExec_t14hipGraphNode_tPvPKv6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphExecMemcpyNodeSetParams1D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431hipGraphAddMemcpyNodeFromSymbolP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemcpyNodeFromSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv437hipGraphMemcpyNodeSetParamsFromSymbol14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphMemcpyNodeSetParamsFromSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv441hipGraphExecMemcpyNodeSetParamsFromSymbol14hipGraphExec_t14hipGraphNode_tPvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphExecMemcpyNodeSetParamsFromSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphAddMemcpyNodeToSymbolP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPKvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemcpyNodeToSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv435hipGraphMemcpyNodeSetParamsToSymbol14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphMemcpyNodeSetParamsToSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv439hipGraphExecMemcpyNodeSetParamsToSymbol14hipGraphExec_t14hipGraphNode_tPKvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipGraphExecMemcpyNodeSetParamsToSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipGraphAddMemsetNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK15hipMemsetParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemsetNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphMemsetNodeGetParams14hipGraphNode_tP15hipMemsetParams"><code class="docutils literal notranslate"><span class="pre">hipGraphMemsetNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipGraphMemsetNodeSetParams14hipGraphNode_tPK15hipMemsetParams"><code class="docutils literal notranslate"><span class="pre">hipGraphMemsetNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431hipGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExecMemsetNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipGraphAddHostNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK17hipHostNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddHostNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipGraphHostNodeGetParams14hipGraphNode_tP17hipHostNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphHostNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipGraphHostNodeSetParams14hipGraphNode_tPK17hipHostNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphHostNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphExecHostNodeSetParams14hipGraphExec_t14hipGraphNode_tPK17hipHostNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExecHostNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipGraphAddChildGraphNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipGraphAddChildGraphNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipGraphChildGraphNodeGetGraph14hipGraphNode_tP10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipGraphChildGraphNodeGetGraph()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv435hipGraphExecChildGraphNodeSetParams14hipGraphExec_t14hipGraphNode_t10hipGraph_t"><code class="docutils literal notranslate"><span class="pre">hipGraphExecChildGraphNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipGraphAddEmptyNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipGraphAddEmptyNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipGraphAddEventRecordNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphAddEventRecordNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431hipGraphEventRecordNodeGetEvent14hipGraphNode_tP10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphEventRecordNodeGetEvent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv431hipGraphEventRecordNodeSetEvent14hipGraphNode_t10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphEventRecordNodeSetEvent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv435hipGraphExecEventRecordNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphExecEventRecordNodeSetEvent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipGraphAddEventWaitNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphAddEventWaitNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphEventWaitNodeGetEvent14hipGraphNode_tP10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphEventWaitNodeGetEvent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphEventWaitNodeSetEvent14hipGraphNode_t10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphEventWaitNodeSetEvent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv433hipGraphExecEventWaitNodeSetEvent14hipGraphExec_t14hipGraphNode_t10hipEvent_t"><code class="docutils literal notranslate"><span class="pre">hipGraphExecEventWaitNodeSetEvent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipGraphAddMemAllocNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tP21hipMemAllocNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemAllocNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipGraphMemAllocNodeGetParams14hipGraphNode_tP21hipMemAllocNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphMemAllocNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipGraphAddMemFreeNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPv"><code class="docutils literal notranslate"><span class="pre">hipGraphAddMemFreeNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipGraphMemFreeNodeGetParams14hipGraphNode_tPv"><code class="docutils literal notranslate"><span class="pre">hipGraphMemFreeNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipDeviceGetGraphMemAttributei24hipGraphMemAttributeTypePv"><code class="docutils literal notranslate"><span class="pre">hipDeviceGetGraphMemAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv429hipDeviceSetGraphMemAttributei24hipGraphMemAttributeTypePv"><code class="docutils literal notranslate"><span class="pre">hipDeviceSetGraphMemAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipDeviceGraphMemTrimi"><code class="docutils literal notranslate"><span class="pre">hipDeviceGraphMemTrim()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipUserObjectCreateP15hipUserObject_tPv11hipHostFn_tjj"><code class="docutils literal notranslate"><span class="pre">hipUserObjectCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipUserObjectRelease15hipUserObject_tj"><code class="docutils literal notranslate"><span class="pre">hipUserObjectRelease()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipUserObjectRetain15hipUserObject_tj"><code class="docutils literal notranslate"><span class="pre">hipUserObjectRetain()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipGraphRetainUserObject10hipGraph_t15hipUserObject_tjj"><code class="docutils literal notranslate"><span class="pre">hipGraphRetainUserObject()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipGraphReleaseUserObject10hipGraph_t15hipUserObject_tj"><code class="docutils literal notranslate"><span class="pre">hipGraphReleaseUserObject()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipGraphDebugDotPrint10hipGraph_tPKcj"><code class="docutils literal notranslate"><span class="pre">hipGraphDebugDotPrint()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv432hipGraphKernelNodeCopyAttributes14hipGraphNode_t14hipGraphNode_t"><code class="docutils literal notranslate"><span class="pre">hipGraphKernelNodeCopyAttributes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipGraphNodeSetEnabled14hipGraphExec_t14hipGraphNode_tj"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeSetEnabled()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipGraphNodeGetEnabled14hipGraphExec_t14hipGraphNode_tPj"><code class="docutils literal notranslate"><span class="pre">hipGraphNodeGetEnabled()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv437hipGraphAddExternalSemaphoresWaitNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK34hipExternalSemaphoreWaitNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddExternalSemaphoresWaitNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv439hipGraphAddExternalSemaphoresSignalNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK36hipExternalSemaphoreSignalNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphAddExternalSemaphoresSignalNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv445hipGraphExternalSemaphoresSignalNodeSetParams14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExternalSemaphoresSignalNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv443hipGraphExternalSemaphoresWaitNodeSetParams14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExternalSemaphoresWaitNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv445hipGraphExternalSemaphoresSignalNodeGetParams14hipGraphNode_tP36hipExternalSemaphoreSignalNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExternalSemaphoresSignalNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv443hipGraphExternalSemaphoresWaitNodeGetParams14hipGraphNode_tP34hipExternalSemaphoreWaitNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExternalSemaphoresWaitNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv449hipGraphExecExternalSemaphoresSignalNodeSetParams14hipGraphExec_t14hipGraphNode_tPK36hipExternalSemaphoreSignalNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExecExternalSemaphoresSignalNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv447hipGraphExecExternalSemaphoresWaitNodeSetParams14hipGraphExec_t14hipGraphNode_tPK34hipExternalSemaphoreWaitNodeParams"><code class="docutils literal notranslate"><span class="pre">hipGraphExecExternalSemaphoresWaitNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipDrvGraphMemcpyNodeGetParams14hipGraphNode_tP12HIP_MEMCPY3D"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphMemcpyNodeGetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipDrvGraphMemcpyNodeSetParams14hipGraphNode_tPK12HIP_MEMCPY3D"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphMemcpyNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipDrvGraphAddMemsetNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK15hipMemsetParams8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphAddMemsetNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipDrvGraphAddMemFreeNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_t14hipDeviceptr_t"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphAddMemFreeNode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv434hipDrvGraphExecMemcpyNodeSetParams14hipGraphExec_t14hipGraphNode_tPK12HIP_MEMCPY3D8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphExecMemcpyNodeSetParams()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv434hipDrvGraphExecMemsetNodeSetParams14hipGraphExec_t14hipGraphNode_tPK15hipMemsetParams8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipDrvGraphExecMemsetNodeSetParams()</span></code></a></li>
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
  <script src="../../../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b"></script>
<script src="../../../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b"></script>

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
    <img id="rdc-watermark" src="../../../_static/images/alpha-watermark.svg" alt="DRAFT watermark"/>
</div> -->
  </body>
</html>
