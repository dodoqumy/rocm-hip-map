---
title: "Runtime compilation &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/runtime_compilation.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:07:15.328749+00:00
content_hash: "c2949870303ac1d5"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="The runtime compilation reference page." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, runtime compilation" name="keywords" />

    <title>Runtime compilation &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/hip_runtime_api/modules/runtime_compilation';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Callback activity APIs" href="callback_activity_apis.html" />
    <link rel="prev" title="Launch API" href="launch_api.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/hip_runtime_api/modules/runtime_compilation.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Runtime compilation</a></li>
<li class="toctree-l3"><a class="reference internal" href="callback_activity_apis.html">Callback activity APIs</a></li>
<li class="toctree-l3"><a class="reference internal" href="graph_management.html">Graph management</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">Runtime compilation</li>
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
    <h1>Runtime compilation</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hiprtcGetErrorString12hiprtcResult"><code class="docutils literal notranslate"><span class="pre">hiprtcGetErrorString()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hiprtcVersionPiPi"><code class="docutils literal notranslate"><span class="pre">hiprtcVersion()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hiprtcAddNameExpression13hiprtcProgramPKc"><code class="docutils literal notranslate"><span class="pre">hiprtcAddNameExpression()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hiprtcCompileProgram13hiprtcProgramiPPCKc"><code class="docutils literal notranslate"><span class="pre">hiprtcCompileProgram()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hiprtcCreateProgramP13hiprtcProgramPKcPKciPPCKcPPCKc"><code class="docutils literal notranslate"><span class="pre">hiprtcCreateProgram()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hiprtcDestroyProgramP13hiprtcProgram"><code class="docutils literal notranslate"><span class="pre">hiprtcDestroyProgram()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hiprtcGetLoweredName13hiprtcProgramPKcPPKc"><code class="docutils literal notranslate"><span class="pre">hiprtcGetLoweredName()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hiprtcGetProgramLog13hiprtcProgramPc"><code class="docutils literal notranslate"><span class="pre">hiprtcGetProgramLog()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hiprtcGetCode13hiprtcProgramPc"><code class="docutils literal notranslate"><span class="pre">hiprtcGetCode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hiprtcGetCodeSize13hiprtcProgramP6size_t"><code class="docutils literal notranslate"><span class="pre">hiprtcGetCodeSize()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hiprtcGetBitcodeSize13hiprtcProgramP6size_t"><code class="docutils literal notranslate"><span class="pre">hiprtcGetBitcodeSize()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hiprtcLinkCreatejP16hiprtcJIT_optionPPvP15hiprtcLinkState"><code class="docutils literal notranslate"><span class="pre">hiprtcLinkCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hiprtcLinkAddFile15hiprtcLinkState18hiprtcJITInputTypePKcjP16hiprtcJIT_optionPPv"><code class="docutils literal notranslate"><span class="pre">hiprtcLinkAddFile()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hiprtcLinkAddData15hiprtcLinkState18hiprtcJITInputTypePv6size_tPKcjP16hiprtcJIT_optionPPv"><code class="docutils literal notranslate"><span class="pre">hiprtcLinkAddData()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hiprtcLinkComplete15hiprtcLinkStatePPvP6size_t"><code class="docutils literal notranslate"><span class="pre">hiprtcLinkComplete()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hiprtcLinkDestroy15hiprtcLinkState"><code class="docutils literal notranslate"><span class="pre">hiprtcLinkDestroy()</span></code></a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="runtime-compilation">
<span id="runtime-compilation-reference"></span><h1>Runtime compilation<a class="headerlink" href="#runtime-compilation" title="Link to this heading">#</a></h1>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hiprtcGetErrorString12hiprtcResult">
<span id="_CPPv320hiprtcGetErrorString12hiprtcResult"></span><span id="_CPPv220hiprtcGetErrorString12hiprtcResult"></span><span id="hiprtcGetErrorString__hiprtcResult"></span><span class="target" id="group___runtime_1ga27bebf4ed3e810ca627cbbfc34880be1"></span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcGetErrorString</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">result</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hiprtcGetErrorString12hiprtcResult" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns text string message to explain the error which occurred. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>In HIP, this function returns the name of the error, if the hiprtc result is defined, it will return “Invalid HIPRTC error code”</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>result</strong> – <strong>[in]</strong> code to convert to string. </p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>const char pointer to the NULL-terminated error string</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hiprtcVersionPiPi">
<span id="_CPPv313hiprtcVersionPiPi"></span><span id="_CPPv213hiprtcVersionPiPi"></span><span id="hiprtcVersion__iP.iP"></span><span class="target" id="group___runtime_1gaef1b2a666014e32bb1ced53729e7f8a6"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcVersion</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">major</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">minor</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hiprtcVersionPiPi" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the parameters as major and minor version. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>major</strong> – <strong>[out]</strong> HIP Runtime Compilation major version. </p></li>
<li><p><strong>minor</strong> – <strong>[out]</strong> HIP Runtime Compilation minor version.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_ERROR_INVALID_INPUT, HIPRTC_SUCCESS</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hiprtcAddNameExpression13hiprtcProgramPKc">
<span id="_CPPv323hiprtcAddNameExpression13hiprtcProgramPKc"></span><span id="_CPPv223hiprtcAddNameExpression13hiprtcProgramPKc"></span><span id="hiprtcAddNameExpression__hiprtcProgram.cCP"></span><span class="target" id="group___runtime_1ga050d3a66e5a6fc90284857af3760b142"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcAddNameExpression</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcProgram</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">prog</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">name_expression</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hiprtcAddNameExpression13hiprtcProgramPKc" title="Link to this definition">#</a><br /></dt>
<dd><p>Adds the given name exprssion to the runtime compilation program. </p>
<p>
If const char pointer is NULL, it will return HIPRTC_ERROR_INVALID_INPUT.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>prog</strong> – <strong>[in]</strong> runtime compilation program instance. </p></li>
<li><p><strong>name_expression</strong> – <strong>[in]</strong> const char pointer to the name expression. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hiprtcCompileProgram13hiprtcProgramiPPCKc">
<span id="_CPPv320hiprtcCompileProgram13hiprtcProgramiPPCKc"></span><span id="_CPPv220hiprtcCompileProgram13hiprtcProgramiPPCKc"></span><span id="hiprtcCompileProgram__hiprtcProgram.i.cCPCP"></span><span class="target" id="group___runtime_1ga7f44ccee23232dbc3e73dbedd4d3f2ad"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcCompileProgram</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcProgram</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">prog</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numOptions</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">options</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hiprtcCompileProgram13hiprtcProgramiPPCKc" title="Link to this definition">#</a><br /></dt>
<dd><p>Compiles the given runtime compilation program. </p>
<p>
If the compiler failed to build the runtime compilation program, it will return HIPRTC_ERROR_COMPILATION.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>prog</strong> – <strong>[in]</strong> runtime compilation program instance. </p></li>
<li><p><strong>numOptions</strong> – <strong>[in]</strong> number of compiler options. </p></li>
<li><p><strong>options</strong> – <strong>[in]</strong> compiler options as const array of strins. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hiprtcCreateProgramP13hiprtcProgramPKcPKciPPCKcPPCKc">
<span id="_CPPv319hiprtcCreateProgramP13hiprtcProgramPKcPKciPPCKcPPCKc"></span><span id="_CPPv219hiprtcCreateProgramP13hiprtcProgramPKcPKciPPCKcPPCKc"></span><span id="hiprtcCreateProgram__hiprtcProgramP.cCP.cCP.i.cCPCP.cCPCP"></span><span class="target" id="group___runtime_1gae7ab5939a3f85ef3b7dcad3314f3067c"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcCreateProgram</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcProgram</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">prog</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">name</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numHeaders</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">headers</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">includeNames</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hiprtcCreateProgramP13hiprtcProgramPKcPKciPPCKcPPCKc" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates an instance of hiprtcProgram with the given input parameters, and sets the output hiprtcProgram prog with it. </p>
<p>
Any invalide input parameter, it will return HIPRTC_ERROR_INVALID_INPUT or HIPRTC_ERROR_INVALID_PROGRAM.</p>
<p>If failed to create the program, it will return HIPRTC_ERROR_PROGRAM_CREATION_FAILURE.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>prog</strong> – <strong>[inout]</strong> runtime compilation program instance. </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> const char pointer to the program source. </p></li>
<li><p><strong>name</strong> – <strong>[in]</strong> const char pointer to the program name. </p></li>
<li><p><strong>numHeaders</strong> – <strong>[in]</strong> number of headers. </p></li>
<li><p><strong>headers</strong> – <strong>[in]</strong> array of strings pointing to headers. </p></li>
<li><p><strong>includeNames</strong> – <strong>[in]</strong> array of strings pointing to names included in program source. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hiprtcDestroyProgramP13hiprtcProgram">
<span id="_CPPv320hiprtcDestroyProgramP13hiprtcProgram"></span><span id="_CPPv220hiprtcDestroyProgramP13hiprtcProgram"></span><span id="hiprtcDestroyProgram__hiprtcProgramP"></span><span class="target" id="group___runtime_1gaaf03e08e317ee3e50e3af04aade84787"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcDestroyProgram</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcProgram</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">prog</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hiprtcDestroyProgramP13hiprtcProgram" title="Link to this definition">#</a><br /></dt>
<dd><p>Destroys an instance of given hiprtcProgram. </p>
<p>
If prog is NULL, it will return HIPRTC_ERROR_INVALID_INPUT.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>prog</strong> – <strong>[in]</strong> runtime compilation program instance. </p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hiprtcGetLoweredName13hiprtcProgramPKcPPKc">
<span id="_CPPv320hiprtcGetLoweredName13hiprtcProgramPKcPPKc"></span><span id="_CPPv220hiprtcGetLoweredName13hiprtcProgramPKcPPKc"></span><span id="hiprtcGetLoweredName__hiprtcProgram.cCP.cCPP"></span><span class="target" id="group___runtime_1ga1e890947c8786af8f3a3eeda2280a5cc"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcGetLoweredName</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcProgram</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">prog</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">name_expression</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">lowered_name</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hiprtcGetLoweredName13hiprtcProgramPKcPPKc" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the lowered (mangled) name from an instance of hiprtcProgram with the given input parameters, and sets the output lowered_name with it. </p>
<p>
If any invalide nullptr input parameters, it will return HIPRTC_ERROR_INVALID_INPUT</p>
<p>If name_expression is not found, it will return HIPRTC_ERROR_NAME_EXPRESSION_NOT_VALID</p>
<p>If failed to get lowered_name from the program, it will return HIPRTC_ERROR_COMPILATION.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>prog</strong> – <strong>[in]</strong> runtime compilation program instance. </p></li>
<li><p><strong>name_expression</strong> – <strong>[in]</strong> const char pointer to the name expression. </p></li>
<li><p><strong>lowered_name</strong> – <strong>[inout]</strong> const char array to the lowered (mangled) name. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hiprtcGetProgramLog13hiprtcProgramPc">
<span id="_CPPv319hiprtcGetProgramLog13hiprtcProgramPc"></span><span id="_CPPv219hiprtcGetProgramLog13hiprtcProgramPc"></span><span id="hiprtcGetProgramLog__hiprtcProgram.cP"></span><span class="target" id="group___runtime_1ga60a18885be6dab83e09d0d340b5003d3"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcGetProgramLog</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcProgram</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">prog</span></span>, <span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">log</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hiprtcGetProgramLog13hiprtcProgramPc" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the log generated by the runtime compilation program instance. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>prog</strong> – <strong>[in]</strong> runtime compilation program instance. </p></li>
<li><p><strong>log</strong> – <strong>[out]</strong> memory pointer to the generated log. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hiprtcGetCode13hiprtcProgramPc">
<span id="_CPPv313hiprtcGetCode13hiprtcProgramPc"></span><span id="_CPPv213hiprtcGetCode13hiprtcProgramPc"></span><span id="hiprtcGetCode__hiprtcProgram.cP"></span><span class="target" id="group___runtime_1gac80b2c9cf7d3635e82c3b7aea35ca82f"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcGetCode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcProgram</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">prog</span></span>, <span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">code</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hiprtcGetCode13hiprtcProgramPc" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the pointer of compilation binary by the runtime compilation program instance. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>prog</strong> – <strong>[in]</strong> runtime compilation program instance. </p></li>
<li><p><strong>code</strong> – <strong>[out]</strong> char pointer to binary. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hiprtcGetCodeSize13hiprtcProgramP6size_t">
<span id="_CPPv317hiprtcGetCodeSize13hiprtcProgramP6size_t"></span><span id="_CPPv217hiprtcGetCodeSize13hiprtcProgramP6size_t"></span><span id="hiprtcGetCodeSize__hiprtcProgram.sP"></span><span class="target" id="group___runtime_1ga3dce3c4183d7a09c9ffffd763f744ecb"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcGetCodeSize</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcProgram</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">prog</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">codeSizeRet</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hiprtcGetCodeSize13hiprtcProgramP6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the size of compilation binary by the runtime compilation program instance. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>prog</strong> – <strong>[in]</strong> runtime compilation program instance. </p></li>
<li><p><strong>codeSizeRet</strong> – <strong>[out]</strong> the size of binary. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hiprtcGetBitcodeSize13hiprtcProgramP6size_t">
<span id="_CPPv320hiprtcGetBitcodeSize13hiprtcProgramP6size_t"></span><span id="_CPPv220hiprtcGetBitcodeSize13hiprtcProgramP6size_t"></span><span id="hiprtcGetBitcodeSize__hiprtcProgram.sP"></span><span class="target" id="group___runtime_1ga775e1e9a7a23c169913eaa8eb874f2d6"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcGetBitcodeSize</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcProgram</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">prog</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">bitcode_size</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hiprtcGetBitcodeSize13hiprtcProgramP6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the size of compiled bitcode by the runtime compilation program instance. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>prog</strong> – <strong>[in]</strong> runtime compilation program instance. </p></li>
<li><p><strong>bitcode_size</strong> – <strong>[out]</strong> the size of bitcode. </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hiprtcLinkCreatejP16hiprtcJIT_optionPPvP15hiprtcLinkState">
<span id="_CPPv316hiprtcLinkCreatejP16hiprtcJIT_optionPPvP15hiprtcLinkState"></span><span id="_CPPv216hiprtcLinkCreatejP16hiprtcJIT_optionPPvP15hiprtcLinkState"></span><span id="hiprtcLinkCreate__unsigned-i.hiprtcJIT_optionP.voidPP.hiprtcLinkStateP"></span><span class="target" id="group___runtime_1ga39f7dee1fb248b9b3977b53c18deea8d"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcLinkCreate</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">num_options</span></span>, <span class="n"><span class="pre">hiprtcJIT_option</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">option_ptr</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">option_vals_pptr</span></span>, <span class="n"><span class="pre">hiprtcLinkState</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">hip_link_state_ptr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hiprtcLinkCreatejP16hiprtcJIT_optionPPvP15hiprtcLinkState" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates the link instance via hiprtc APIs. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>num_options</strong> – <strong>[in]</strong> Number of options </p></li>
<li><p><strong>option_ptr</strong> – <strong>[in]</strong> Array of options </p></li>
<li><p><strong>option_vals_pptr</strong> – <strong>[in]</strong> Array of option values cast to void* </p></li>
<li><p><strong>hip_link_state_ptr</strong> – <strong>[out]</strong> hiprtc link state created upon success</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS, HIPRTC_ERROR_INVALID_INPUT, HIPRTC_ERROR_INVALID_OPTION</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hiprtcLinkAddFile15hiprtcLinkState18hiprtcJITInputTypePKcjP16hiprtcJIT_optionPPv">
<span id="_CPPv317hiprtcLinkAddFile15hiprtcLinkState18hiprtcJITInputTypePKcjP16hiprtcJIT_optionPPv"></span><span id="_CPPv217hiprtcLinkAddFile15hiprtcLinkState18hiprtcJITInputTypePKcjP16hiprtcJIT_optionPPv"></span><span id="hiprtcLinkAddFile__hiprtcLinkState.hiprtcJITInputType.cCP.unsigned-i.hiprtcJIT_optionP.voidPP"></span><span class="target" id="group___runtime_1ga1b0f89907c20e8fd1d7e47cbecb80a4b"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcLinkAddFile</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcLinkState</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hip_link_state</span></span>, <span class="n"><span class="pre">hiprtcJITInputType</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">input_type</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">file_path</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">num_options</span></span>, <span class="n"><span class="pre">hiprtcJIT_option</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">options_ptr</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">option_values</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hiprtcLinkAddFile15hiprtcLinkState18hiprtcJITInputTypePKcjP16hiprtcJIT_optionPPv" title="Link to this definition">#</a><br /></dt>
<dd><p>Adds a file with bit code to be linked with options. </p>
<p>
If input values are invalid, it will <div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hip_link_state</strong> – <strong>[in]</strong> hiprtc link state </p></li>
<li><p><strong>input_type</strong> – <strong>[in]</strong> Type of the input data or bitcode </p></li>
<li><p><strong>file_path</strong> – <strong>[in]</strong> Path to the input file where bitcode is present </p></li>
<li><p><strong>num_options</strong> – <strong>[in]</strong> Size of the options </p></li>
<li><p><strong>options_ptr</strong> – <strong>[in]</strong> Array of options applied to this input </p></li>
<li><p><strong>option_values</strong> – <strong>[in]</strong> Array of option values cast to void*</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS</p>
</dd>
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>HIPRTC_ERROR_INVALID_INPUT</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hiprtcLinkAddData15hiprtcLinkState18hiprtcJITInputTypePv6size_tPKcjP16hiprtcJIT_optionPPv">
<span id="_CPPv317hiprtcLinkAddData15hiprtcLinkState18hiprtcJITInputTypePv6size_tPKcjP16hiprtcJIT_optionPPv"></span><span id="_CPPv217hiprtcLinkAddData15hiprtcLinkState18hiprtcJITInputTypePv6size_tPKcjP16hiprtcJIT_optionPPv"></span><span id="hiprtcLinkAddData__hiprtcLinkState.hiprtcJITInputType.voidP.s.cCP.unsigned-i.hiprtcJIT_optionP.voidPP"></span><span class="target" id="group___runtime_1ga772b8b360f0a1e891ca55fdc32e7e74e"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcLinkAddData</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcLinkState</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hip_link_state</span></span>, <span class="n"><span class="pre">hiprtcJITInputType</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">input_type</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">image</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">image_size</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">name</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">num_options</span></span>, <span class="n"><span class="pre">hiprtcJIT_option</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">options_ptr</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">option_values</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hiprtcLinkAddData15hiprtcLinkState18hiprtcJITInputTypePv6size_tPKcjP16hiprtcJIT_optionPPv" title="Link to this definition">#</a><br /></dt>
<dd><p>Completes the linking of the given program. </p>
<p>
If adding the file fails, it will <div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hip_link_state</strong> – <strong>[in]</strong> hiprtc link state </p></li>
<li><p><strong>input_type</strong> – <strong>[in]</strong> Type of the input data or bitcode </p></li>
<li><p><strong>image</strong> – <strong>[in]</strong> Input data which is null terminated </p></li>
<li><p><strong>image_size</strong> – <strong>[in]</strong> Size of the input data </p></li>
<li><p><strong>name</strong> – <strong>[in]</strong> Optional name for this input </p></li>
<li><p><strong>num_options</strong> – <strong>[in]</strong> Size of the options </p></li>
<li><p><strong>options_ptr</strong> – <strong>[in]</strong> Array of options applied to this input </p></li>
<li><p><strong>option_values</strong> – <strong>[in]</strong> Array of option values cast to void*</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS, HIPRTC_ERROR_INVALID_INPUT</p>
</dd>
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>HIPRTC_ERROR_PROGRAM_CREATION_FAILURE</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hiprtcLinkComplete15hiprtcLinkStatePPvP6size_t">
<span id="_CPPv318hiprtcLinkComplete15hiprtcLinkStatePPvP6size_t"></span><span id="_CPPv218hiprtcLinkComplete15hiprtcLinkStatePPvP6size_t"></span><span id="hiprtcLinkComplete__hiprtcLinkState.voidPP.sP"></span><span class="target" id="group___runtime_1ga1479cebdfe7986b909531d2ee37714b2"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcLinkComplete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcLinkState</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hip_link_state</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">bin_out</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">size_out</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hiprtcLinkComplete15hiprtcLinkStatePPvP6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Completes the linking of the given program. </p>
<p>
If adding the data fails, it will <div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hip_link_state</strong> – <strong>[in]</strong> hiprtc link state </p></li>
<li><p><strong>bin_out</strong> – <strong>[out]</strong> Upon success, points to the output binary </p></li>
<li><p><strong>size_out</strong> – <strong>[out]</strong> Size of the binary is stored (optional)</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS</p>
</dd>
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>HIPRTC_ERROR_LINKING</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hiprtcLinkDestroy15hiprtcLinkState">
<span id="_CPPv317hiprtcLinkDestroy15hiprtcLinkState"></span><span id="_CPPv217hiprtcLinkDestroy15hiprtcLinkState"></span><span id="hiprtcLinkDestroy__hiprtcLinkState"></span><span class="target" id="group___runtime_1ga472583d0d93fa14458171969ae726c24"></span><span class="n"><span class="pre">hiprtcResult</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hiprtcLinkDestroy</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hiprtcLinkState</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hip_link_state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hiprtcLinkDestroy15hiprtcLinkState" title="Link to this definition">#</a><br /></dt>
<dd><p>Deletes the link instance via hiprtc APIs. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hiprtcResult</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>hip_link_state</strong> – <strong>[in]</strong> link state instance</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>HIPRTC_SUCCESS</p>
</dd>
</dl>
</dd></dl>

</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="launch_api.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Launch API</p>
      </div>
    </a>
    <a class="right-next"
       href="callback_activity_apis.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Callback activity APIs</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hiprtcGetErrorString12hiprtcResult"><code class="docutils literal notranslate"><span class="pre">hiprtcGetErrorString()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hiprtcVersionPiPi"><code class="docutils literal notranslate"><span class="pre">hiprtcVersion()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hiprtcAddNameExpression13hiprtcProgramPKc"><code class="docutils literal notranslate"><span class="pre">hiprtcAddNameExpression()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hiprtcCompileProgram13hiprtcProgramiPPCKc"><code class="docutils literal notranslate"><span class="pre">hiprtcCompileProgram()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hiprtcCreateProgramP13hiprtcProgramPKcPKciPPCKcPPCKc"><code class="docutils literal notranslate"><span class="pre">hiprtcCreateProgram()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hiprtcDestroyProgramP13hiprtcProgram"><code class="docutils literal notranslate"><span class="pre">hiprtcDestroyProgram()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hiprtcGetLoweredName13hiprtcProgramPKcPPKc"><code class="docutils literal notranslate"><span class="pre">hiprtcGetLoweredName()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hiprtcGetProgramLog13hiprtcProgramPc"><code class="docutils literal notranslate"><span class="pre">hiprtcGetProgramLog()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hiprtcGetCode13hiprtcProgramPc"><code class="docutils literal notranslate"><span class="pre">hiprtcGetCode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hiprtcGetCodeSize13hiprtcProgramP6size_t"><code class="docutils literal notranslate"><span class="pre">hiprtcGetCodeSize()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hiprtcGetBitcodeSize13hiprtcProgramP6size_t"><code class="docutils literal notranslate"><span class="pre">hiprtcGetBitcodeSize()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hiprtcLinkCreatejP16hiprtcJIT_optionPPvP15hiprtcLinkState"><code class="docutils literal notranslate"><span class="pre">hiprtcLinkCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hiprtcLinkAddFile15hiprtcLinkState18hiprtcJITInputTypePKcjP16hiprtcJIT_optionPPv"><code class="docutils literal notranslate"><span class="pre">hiprtcLinkAddFile()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hiprtcLinkAddData15hiprtcLinkState18hiprtcJITInputTypePv6size_tPKcjP16hiprtcJIT_optionPPv"><code class="docutils literal notranslate"><span class="pre">hiprtcLinkAddData()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hiprtcLinkComplete15hiprtcLinkStatePPvP6size_t"><code class="docutils literal notranslate"><span class="pre">hiprtcLinkComplete()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hiprtcLinkDestroy15hiprtcLinkState"><code class="docutils literal notranslate"><span class="pre">hiprtcLinkDestroy()</span></code></a></li>
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
