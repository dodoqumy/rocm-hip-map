---
title: "Context management [deprecated] &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/context_management.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:08.224365+00:00
content_hash: "480174175440f1c1"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="The context management reference page." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, context management, context" name="keywords" />

    <title>Context management [deprecated] &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/hip_runtime_api/modules/context_management';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Module management" href="module_management.html" />
    <link rel="prev" title="Peer to peer device memory access" href="peer_to_peer_device_memory_access.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/hip_runtime_api/modules/context_management.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Context management [deprecated]</a></li>
<li class="toctree-l3"><a class="reference internal" href="module_management.html">Module management</a></li>
<li class="toctree-l3"><a class="reference internal" href="occupancy.html">Occupancy</a></li>
<li class="toctree-l3"><a class="reference internal" href="profiler_control.html">Profiler control</a></li>
<li class="toctree-l3"><a class="reference internal" href="launch_api.html">Launch API</a></li>
<li class="toctree-l3"><a class="reference internal" href="runtime_compilation.html">Runtime compilation</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">Context...</li>
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
    <h1>Context management [deprecated]</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipCtxCreateP8hipCtx_tj11hipDevice_t"><code class="docutils literal notranslate"><span class="pre">hipCtxCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipCtxDestroy8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipCtxDestroy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipCtxPopCurrentP8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipCtxPopCurrent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipCtxPushCurrent8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipCtxPushCurrent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipCtxSetCurrent8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipCtxSetCurrent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipCtxGetCurrentP8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipCtxGetCurrent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipCtxGetDeviceP11hipDevice_t"><code class="docutils literal notranslate"><span class="pre">hipCtxGetDevice()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipCtxGetApiVersion8hipCtx_tPj"><code class="docutils literal notranslate"><span class="pre">hipCtxGetApiVersion()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipCtxGetCacheConfigP14hipFuncCache_t"><code class="docutils literal notranslate"><span class="pre">hipCtxGetCacheConfig()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipCtxSetCacheConfig14hipFuncCache_t"><code class="docutils literal notranslate"><span class="pre">hipCtxSetCacheConfig()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipCtxSetSharedMemConfig18hipSharedMemConfig"><code class="docutils literal notranslate"><span class="pre">hipCtxSetSharedMemConfig()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipCtxGetSharedMemConfigP18hipSharedMemConfig"><code class="docutils literal notranslate"><span class="pre">hipCtxGetSharedMemConfig()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipCtxSynchronizev"><code class="docutils literal notranslate"><span class="pre">hipCtxSynchronize()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipCtxGetFlagsPj"><code class="docutils literal notranslate"><span class="pre">hipCtxGetFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipCtxEnablePeerAccess8hipCtx_tj"><code class="docutils literal notranslate"><span class="pre">hipCtxEnablePeerAccess()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipCtxDisablePeerAccess8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipCtxDisablePeerAccess()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipDevicePrimaryCtxGetState11hipDevice_tPjPi"><code class="docutils literal notranslate"><span class="pre">hipDevicePrimaryCtxGetState()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipDevicePrimaryCtxRelease11hipDevice_t"><code class="docutils literal notranslate"><span class="pre">hipDevicePrimaryCtxRelease()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipDevicePrimaryCtxRetainP8hipCtx_t11hipDevice_t"><code class="docutils literal notranslate"><span class="pre">hipDevicePrimaryCtxRetain()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipDevicePrimaryCtxReset11hipDevice_t"><code class="docutils literal notranslate"><span class="pre">hipDevicePrimaryCtxReset()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipDevicePrimaryCtxSetFlags11hipDevice_tj"><code class="docutils literal notranslate"><span class="pre">hipDevicePrimaryCtxSetFlags()</span></code></a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="context-management-deprecated">
<span id="context-management-reference"></span><h1>Context management [deprecated]<a class="headerlink" href="#context-management-deprecated" title="Link to this heading">#</a></h1>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412hipCtxCreateP8hipCtx_tj11hipDevice_t">
<span id="_CPPv312hipCtxCreateP8hipCtx_tj11hipDevice_t"></span><span id="_CPPv212hipCtxCreateP8hipCtx_tj11hipDevice_t"></span><span id="hipCtxCreate__hipCtx_tP.unsigned-i.hipDevice_t"></span><span class="target" id="group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxCreate</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ctx</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span>, <span class="n"><span class="pre">hipDevice_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">device</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412hipCtxCreateP8hipCtx_tj11hipDevice_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Create a context and set it as current/default context. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ctx</strong> – <strong>[out]</strong> Context to create </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Context creation flags </p></li>
<li><p><strong>device</strong> – <strong>[in]</strong> device handle</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipCtxDestroy8hipCtx_t">
<span id="_CPPv313hipCtxDestroy8hipCtx_t"></span><span id="_CPPv213hipCtxDestroy8hipCtx_t"></span><span id="hipCtxDestroy__hipCtx_t"></span><span class="target" id="group___context_1ga9a65fe43238ef303a6d97826c05fd14e"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxDestroy</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ctx</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipCtxDestroy8hipCtx_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Destroy a HIP context [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>,<a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a> , <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>ctx</strong> – <strong>[in]</strong> Context to destroy</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipCtxPopCurrentP8hipCtx_t">
<span id="_CPPv316hipCtxPopCurrentP8hipCtx_t"></span><span id="_CPPv216hipCtxPopCurrentP8hipCtx_t"></span><span id="hipCtxPopCurrent__hipCtx_tP"></span><span class="target" id="group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxPopCurrent</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ctx</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipCtxPopCurrentP8hipCtx_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Pop the current/default context and return the popped context [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>ctx</strong> – <strong>[out]</strong> The current context to pop</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidContext</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipCtxPushCurrent8hipCtx_t">
<span id="_CPPv317hipCtxPushCurrent8hipCtx_t"></span><span id="_CPPv217hipCtxPushCurrent8hipCtx_t"></span><span id="hipCtxPushCurrent__hipCtx_t"></span><span class="target" id="group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxPushCurrent</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ctx</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipCtxPushCurrent8hipCtx_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Push the context to be set as current/ default context [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a> , <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>ctx</strong> – <strong>[in]</strong> The current context to push</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidContext</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipCtxSetCurrent8hipCtx_t">
<span id="_CPPv316hipCtxSetCurrent8hipCtx_t"></span><span id="_CPPv216hipCtxSetCurrent8hipCtx_t"></span><span id="hipCtxSetCurrent__hipCtx_t"></span><span class="target" id="group___context_1ga834a192f70c2bfc0269c309436776feb"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxSetCurrent</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ctx</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipCtxSetCurrent8hipCtx_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Set the passed context as current/default [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a> , <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>ctx</strong> – <strong>[in]</strong> The context to set as current</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidContext</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipCtxGetCurrentP8hipCtx_t">
<span id="_CPPv316hipCtxGetCurrentP8hipCtx_t"></span><span id="_CPPv216hipCtxGetCurrentP8hipCtx_t"></span><span id="hipCtxGetCurrent__hipCtx_tP"></span><span class="target" id="group___context_1ga741786101d348fdbfa1f64546860357a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxGetCurrent</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ctx</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipCtxGetCurrentP8hipCtx_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Get the handle of the current/ default context [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>ctx</strong> – <strong>[out]</strong> The context to get as current</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidContext</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415hipCtxGetDeviceP11hipDevice_t">
<span id="_CPPv315hipCtxGetDeviceP11hipDevice_t"></span><span id="_CPPv215hipCtxGetDeviceP11hipDevice_t"></span><span id="hipCtxGetDevice__hipDevice_tP"></span><span class="target" id="group___context_1ga8aa32cf64272da929f23ecbafefefcee"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxGetDevice</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDevice_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">device</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415hipCtxGetDeviceP11hipDevice_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Get the handle of the device associated with current/default context [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>device</strong> – <strong>[out]</strong> The device from the current context</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidContext</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipCtxGetApiVersion8hipCtx_tPj">
<span id="_CPPv319hipCtxGetApiVersion8hipCtx_tPj"></span><span id="_CPPv219hipCtxGetApiVersion8hipCtx_tPj"></span><span id="hipCtxGetApiVersion__hipCtx_t.unsigned-iP"></span><span class="target" id="group___context_1ga16acb41a83574a7e7431811aa3421c21"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxGetApiVersion</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ctx</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">apiVersion</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipCtxGetApiVersion8hipCtx_tPj" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns the approximate HIP api version. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>The HIP feature set does not correspond to an exact CUDA SDK api revision. This function always set *apiVersion to 4 as an approximation though HIP supports some features which were introduced in later CUDA SDK revisions. HIP apps code should not rely on the api revision number here and should use arch feature flags to test device capabilities or conditional compilation.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ctx</strong> – <strong>[in]</strong> Context to check [Deprecated] </p></li>
<li><p><strong>apiVersion</strong> – <strong>[out]</strong> API version to get</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hipCtxGetCacheConfigP14hipFuncCache_t">
<span id="_CPPv320hipCtxGetCacheConfigP14hipFuncCache_t"></span><span id="_CPPv220hipCtxGetCacheConfigP14hipFuncCache_t"></span><span id="hipCtxGetCacheConfig__hipFuncCache_tP"></span><span class="target" id="group___context_1gab10373068faafd3042c9003e2e6d905a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxGetCacheConfig</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipFuncCache_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">cacheConfig</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hipCtxGetCacheConfigP14hipFuncCache_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Get Cache configuration for a specific function [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>AMD devices and some Nvidia GPUS do not support reconfigurable cache. This hint is ignored on those architectures.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>cacheConfig</strong> – <strong>[out]</strong> Cache configuration</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hipCtxSetCacheConfig14hipFuncCache_t">
<span id="_CPPv320hipCtxSetCacheConfig14hipFuncCache_t"></span><span id="_CPPv220hipCtxSetCacheConfig14hipFuncCache_t"></span><span id="hipCtxSetCacheConfig__hipFuncCache_t"></span><span class="target" id="group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxSetCacheConfig</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipFuncCache_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">cacheConfig</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hipCtxSetCacheConfig14hipFuncCache_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Set L1/Shared cache partition [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>AMD devices and some Nvidia GPUS do not support reconfigurable cache. This hint is ignored on those architectures.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>cacheConfig</strong> – <strong>[in]</strong> Cache configuration to set</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424hipCtxSetSharedMemConfig18hipSharedMemConfig">
<span id="_CPPv324hipCtxSetSharedMemConfig18hipSharedMemConfig"></span><span id="_CPPv224hipCtxSetSharedMemConfig18hipSharedMemConfig"></span><span id="hipCtxSetSharedMemConfig__hipSharedMemConfig"></span><span class="target" id="group___context_1gad5c1d4ced27f584a74ed550dd002fa5a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxSetSharedMemConfig</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipSharedMemConfig</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">config</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424hipCtxSetSharedMemConfig18hipSharedMemConfig" title="Link to this definition">#</a><br /></dt>
<dd><p>Set Shared memory bank configuration [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>AMD devices and some Nvidia GPUS do not support shared cache banking, and the hint is ignored on those architectures.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>config</strong> – <strong>[in]</strong> Shared memory configuration to set</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424hipCtxGetSharedMemConfigP18hipSharedMemConfig">
<span id="_CPPv324hipCtxGetSharedMemConfigP18hipSharedMemConfig"></span><span id="_CPPv224hipCtxGetSharedMemConfigP18hipSharedMemConfig"></span><span id="hipCtxGetSharedMemConfig__hipSharedMemConfigP"></span><span class="target" id="group___context_1ga3c78b22dd03435a7ca88621a45409565"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxGetSharedMemConfig</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipSharedMemConfig</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pConfig</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424hipCtxGetSharedMemConfigP18hipSharedMemConfig" title="Link to this definition">#</a><br /></dt>
<dd><p>Get Shared memory bank configuration [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>AMD devices and some Nvidia GPUS do not support shared cache banking, and the hint is ignored on those architectures.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>pConfig</strong> – <strong>[out]</strong> Pointer of shared memory configuration</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipCtxSynchronizev">
<span id="_CPPv317hipCtxSynchronizev"></span><span id="_CPPv217hipCtxSynchronizev"></span><span id="hipCtxSynchronize__void"></span><span class="target" id="group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxSynchronize</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipCtxSynchronizev" title="Link to this definition">#</a><br /></dt>
<dd><p>Blocks until the default context has completed all preceding requested tasks [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This function waits for all streams on the default context to complete execution, and then returns.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>hipSuccess</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipCtxGetFlagsPj">
<span id="_CPPv314hipCtxGetFlagsPj"></span><span id="_CPPv214hipCtxGetFlagsPj"></span><span id="hipCtxGetFlags__unsigned-iP"></span><span class="target" id="group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxGetFlags</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipCtxGetFlagsPj" title="Link to this definition">#</a><br /></dt>
<dd><p>Return flags used for creating default context [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>flags</strong> – <strong>[out]</strong> Pointer of flags</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipCtxEnablePeerAccess8hipCtx_tj">
<span id="_CPPv322hipCtxEnablePeerAccess8hipCtx_tj"></span><span id="_CPPv222hipCtxEnablePeerAccess8hipCtx_tj"></span><span id="hipCtxEnablePeerAccess__hipCtx_t.unsigned-i"></span><span class="target" id="group___context_1ga834dfd99d72082fe8770142fa30b30e2"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxEnablePeerAccess</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">peerCtx</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipCtxEnablePeerAccess8hipCtx_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Enables direct access to memory allocations in a peer context [Deprecated]. </p>
<p>Memory which already allocated on peer device will be mapped into the address space of the current device. In addition, all future memory allocations on peerDeviceId will be mapped into the address space of the current device when the memory is allocated. The peer memory remains accessible from the current device until a call to hipDeviceDisablePeerAccess or hipDeviceReset.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>PeerToPeer support is experimental.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>peerCtx</strong> – <strong>[in]</strong> Peer context </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> flags, need to set as 0</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidDevice, hipErrorInvalidValue, hipErrorPeerAccessAlreadyEnabled</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipCtxDisablePeerAccess8hipCtx_t">
<span id="_CPPv323hipCtxDisablePeerAccess8hipCtx_t"></span><span id="_CPPv223hipCtxDisablePeerAccess8hipCtx_t"></span><span id="hipCtxDisablePeerAccess__hipCtx_t"></span><span class="target" id="group___context_1gaf48e4e9c3b6bbad5deaeff10d2e28b31"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipCtxDisablePeerAccess</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">peerCtx</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipCtxDisablePeerAccess8hipCtx_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Disable direct access from current context’s virtual address space to memory allocations physically located on a peer context.Disables direct access to memory allocations in a peer context and unregisters any registered allocations [Deprecated]. </p>
<p>Returns hipErrorPeerAccessNotEnabled if direct access to memory on peerDevice has not yet been enabled from the current device.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>PeerToPeer support is experimental.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent cuCtx driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>peerCtx</strong> – <strong>[in]</strong> Peer context to be disabled</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorPeerAccessNotEnabled</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv427hipDevicePrimaryCtxGetState11hipDevice_tPjPi">
<span id="_CPPv327hipDevicePrimaryCtxGetState11hipDevice_tPjPi"></span><span id="_CPPv227hipDevicePrimaryCtxGetState11hipDevice_tPjPi"></span><span id="hipDevicePrimaryCtxGetState__hipDevice_t.unsigned-iP.iP"></span><span class="target" id="group___context_1ga60d31f744991c6c568ec3027cf1fb8ab"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDevicePrimaryCtxGetState</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDevice_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dev</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">flags</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">active</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv427hipDevicePrimaryCtxGetState11hipDevice_tPjPi" title="Link to this definition">#</a><br /></dt>
<dd><p>Get the state of the primary context [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dev</strong> – <strong>[in]</strong> Device to get primary context flags for </p></li>
<li><p><strong>flags</strong> – <strong>[out]</strong> Pointer to store flags </p></li>
<li><p><strong>active</strong> – <strong>[out]</strong> Pointer to store context state; 0 = inactive, 1 = active</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426hipDevicePrimaryCtxRelease11hipDevice_t">
<span id="_CPPv326hipDevicePrimaryCtxRelease11hipDevice_t"></span><span id="_CPPv226hipDevicePrimaryCtxRelease11hipDevice_t"></span><span id="hipDevicePrimaryCtxRelease__hipDevice_t"></span><span class="target" id="group___context_1ga7bbe8905908168909ddecd98cd34c1e8"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDevicePrimaryCtxRelease</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDevice_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426hipDevicePrimaryCtxRelease11hipDevice_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Release the primary context on the GPU. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This function return hipSuccess though doesn’t release the primaryCtx by design on HIP/HIP-CLANG path.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>dev</strong> – <strong>[in]</strong> Device which primary context is released [Deprecated]</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425hipDevicePrimaryCtxRetainP8hipCtx_t11hipDevice_t">
<span id="_CPPv325hipDevicePrimaryCtxRetainP8hipCtx_t11hipDevice_t"></span><span id="_CPPv225hipDevicePrimaryCtxRetainP8hipCtx_t11hipDevice_t"></span><span id="hipDevicePrimaryCtxRetain__hipCtx_tP.hipDevice_t"></span><span class="target" id="group___context_1gab6e1014e9a4dbe281b84e38d89ff2409"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDevicePrimaryCtxRetain</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipCtx_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pctx</span></span>, <span class="n"><span class="pre">hipDevice_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425hipDevicePrimaryCtxRetainP8hipCtx_t11hipDevice_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Retain the primary context on the GPU [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pctx</strong> – <strong>[out]</strong> Returned context handle of the new context </p></li>
<li><p><strong>dev</strong> – <strong>[in]</strong> Device which primary context is released</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424hipDevicePrimaryCtxReset11hipDevice_t">
<span id="_CPPv324hipDevicePrimaryCtxReset11hipDevice_t"></span><span id="_CPPv224hipDevicePrimaryCtxReset11hipDevice_t"></span><span id="hipDevicePrimaryCtxReset__hipDevice_t"></span><span class="target" id="group___context_1gac2ca146e5d67b28d870dadd9dc3fc04e"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDevicePrimaryCtxReset</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDevice_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dev</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424hipDevicePrimaryCtxReset11hipDevice_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Resets the primary context on the GPU [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>dev</strong> – <strong>[in]</strong> Device which primary context is reset</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv427hipDevicePrimaryCtxSetFlags11hipDevice_tj">
<span id="_CPPv327hipDevicePrimaryCtxSetFlags11hipDevice_tj"></span><span id="_CPPv227hipDevicePrimaryCtxSetFlags11hipDevice_tj"></span><span id="hipDevicePrimaryCtxSetFlags__hipDevice_t.unsigned-i"></span><span class="target" id="group___context_1ga5cd8ba188e628274142dd44d39780436"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDevicePrimaryCtxSetFlags</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDevice_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dev</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv427hipDevicePrimaryCtxSetFlags11hipDevice_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Set flags for the primary context [Deprecated]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated on the AMD platform, only for equivalent driver API on the NVIDIA platform. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dev</strong> – <strong>[in]</strong> Device for which the primary context flags are set </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> New flags for the device</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorContextAlreadyInUse</p>
</dd>
</dl>
</dd></dl>

</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="peer_to_peer_device_memory_access.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Peer to peer device memory access</p>
      </div>
    </a>
    <a class="right-next"
       href="module_management.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Module management</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipCtxCreateP8hipCtx_tj11hipDevice_t"><code class="docutils literal notranslate"><span class="pre">hipCtxCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipCtxDestroy8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipCtxDestroy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipCtxPopCurrentP8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipCtxPopCurrent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipCtxPushCurrent8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipCtxPushCurrent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipCtxSetCurrent8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipCtxSetCurrent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipCtxGetCurrentP8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipCtxGetCurrent()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipCtxGetDeviceP11hipDevice_t"><code class="docutils literal notranslate"><span class="pre">hipCtxGetDevice()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipCtxGetApiVersion8hipCtx_tPj"><code class="docutils literal notranslate"><span class="pre">hipCtxGetApiVersion()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipCtxGetCacheConfigP14hipFuncCache_t"><code class="docutils literal notranslate"><span class="pre">hipCtxGetCacheConfig()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipCtxSetCacheConfig14hipFuncCache_t"><code class="docutils literal notranslate"><span class="pre">hipCtxSetCacheConfig()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipCtxSetSharedMemConfig18hipSharedMemConfig"><code class="docutils literal notranslate"><span class="pre">hipCtxSetSharedMemConfig()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipCtxGetSharedMemConfigP18hipSharedMemConfig"><code class="docutils literal notranslate"><span class="pre">hipCtxGetSharedMemConfig()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipCtxSynchronizev"><code class="docutils literal notranslate"><span class="pre">hipCtxSynchronize()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipCtxGetFlagsPj"><code class="docutils literal notranslate"><span class="pre">hipCtxGetFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipCtxEnablePeerAccess8hipCtx_tj"><code class="docutils literal notranslate"><span class="pre">hipCtxEnablePeerAccess()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipCtxDisablePeerAccess8hipCtx_t"><code class="docutils literal notranslate"><span class="pre">hipCtxDisablePeerAccess()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipDevicePrimaryCtxGetState11hipDevice_tPjPi"><code class="docutils literal notranslate"><span class="pre">hipDevicePrimaryCtxGetState()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipDevicePrimaryCtxRelease11hipDevice_t"><code class="docutils literal notranslate"><span class="pre">hipDevicePrimaryCtxRelease()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipDevicePrimaryCtxRetainP8hipCtx_t11hipDevice_t"><code class="docutils literal notranslate"><span class="pre">hipDevicePrimaryCtxRetain()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipDevicePrimaryCtxReset11hipDevice_t"><code class="docutils literal notranslate"><span class="pre">hipDevicePrimaryCtxReset()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipDevicePrimaryCtxSetFlags11hipDevice_tj"><code class="docutils literal notranslate"><span class="pre">hipDevicePrimaryCtxSetFlags()</span></code></a></li>
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
