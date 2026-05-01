---
title: "Memory management &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/memory_management.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:07:21.182897+00:00
content_hash: "32883c9c2016242c"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="The memory management reference page." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, memory management, memory" name="keywords" />

    <title>Memory management &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/hip_runtime_api/modules/memory_management';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Memory management (deprecated)" href="memory_management/memory_management_deprecated.html" />
    <link rel="prev" title="Event management" href="event_management.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/hip_runtime_api/modules/memory_management.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l3 current active has-children"><a class="current reference internal" href="#">Memory management</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
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
    
    <li class="breadcrumb-item active" aria-current="page">Memory management</li>
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
    <h1>Memory management</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipPointerSetAttributePKv20hipPointer_attribute14hipDeviceptr_t"><code class="docutils literal notranslate"><span class="pre">hipPointerSetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipPointerGetAttributesP21hipPointerAttribute_tPKv"><code class="docutils literal notranslate"><span class="pre">hipPointerGetAttributes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipPointerGetAttributePv20hipPointer_attribute14hipDeviceptr_t"><code class="docutils literal notranslate"><span class="pre">hipPointerGetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipDrvPointerGetAttributesjP20hipPointer_attributePPv14hipDeviceptr_t"><code class="docutils literal notranslate"><span class="pre">hipDrvPointerGetAttributes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49hipMallocPPv6size_t"><code class="docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipExtMallocWithFlagsPPv6size_tj"><code class="docutils literal notranslate"><span class="pre">hipExtMallocWithFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipHostMallocPPv6size_tj"><code class="docutils literal notranslate"><span class="pre">hipHostMalloc()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipHostAllocPPv6size_tj"><code class="docutils literal notranslate"><span class="pre">hipHostAlloc()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipHostGetDevicePointerPPvPvj"><code class="docutils literal notranslate"><span class="pre">hipHostGetDevicePointer()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipHostGetFlagsPjPv"><code class="docutils literal notranslate"><span class="pre">hipHostGetFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipHostRegisterPv6size_tj"><code class="docutils literal notranslate"><span class="pre">hipHostRegister()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipHostUnregisterPv"><code class="docutils literal notranslate"><span class="pre">hipHostUnregister()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMallocPitchPPvP6size_t6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMallocPitch()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemAllocPitchP14hipDeviceptr_tP6size_t6size_t6size_tj"><code class="docutils literal notranslate"><span class="pre">hipMemAllocPitch()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47hipFreePv"><code class="docutils literal notranslate"><span class="pre">hipFree()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipFreeHostPv"><code class="docutils literal notranslate"><span class="pre">hipFreeHost()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemcpyWithStreamPvPKv6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyWithStream()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyHtoD14hipDeviceptr_tPKv6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyHtoD()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyDtoHPv14hipDeviceptr_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyDtoH()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyDtoD14hipDeviceptr_t14hipDeviceptr_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyDtoD()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyAtoD14hipDeviceptr_t10hipArray_t6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyAtoD()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyDtoA10hipArray_t6size_t14hipDeviceptr_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyDtoA()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyAtoA10hipArray_t6size_t10hipArray_t6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyAtoA()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemcpyHtoDAsync14hipDeviceptr_tPKv6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyHtoDAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemcpyDtoHAsyncPv14hipDeviceptr_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyDtoHAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemcpyDtoDAsync14hipDeviceptr_t14hipDeviceptr_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyDtoDAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemcpyAtoHAsyncPv10hipArray_t6size_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyAtoHAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemcpyHtoAAsync10hipArray_t6size_tPKv6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyHtoAAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipGetSymbolAddressPPvPKv"><code class="docutils literal notranslate"><span class="pre">hipGetSymbolAddress()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipGetSymbolSizeP6size_tPKv"><code class="docutils literal notranslate"><span class="pre">hipGetSymbolSize()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipGetProcAddressPKcPPvi8uint64_tP31hipDriverProcAddressQueryResult"><code class="docutils literal notranslate"><span class="pre">hipGetProcAddress()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipMemcpyToSymbolPKvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpyToSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipMemcpyToSymbolAsyncPKvPKv6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyToSymbolAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemcpyFromSymbolPvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpyFromSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipMemcpyFromSymbolAsyncPvPKv6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyFromSymbolAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMemcpyAsyncPvPKv6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49hipMemsetPvi6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemset()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipMemsetD814hipDeviceptr_th6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD8()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemsetD8Async14hipDeviceptr_th6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD8Async()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipMemsetD1614hipDeviceptr_tt6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD16()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipMemsetD16Async14hipDeviceptr_tt6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD16Async()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipMemsetD3214hipDeviceptr_ti6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD32()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMemsetAsyncPvi6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipMemsetD32Async14hipDeviceptr_ti6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD32Async()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipMemset2DPv6size_ti6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemset2D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemset2DAsyncPv6size_ti6size_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemset2DAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipMemset3D13hipPitchedPtri9hipExtent"><code class="docutils literal notranslate"><span class="pre">hipMemset3D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemset3DAsync13hipPitchedPtri9hipExtent11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemset3DAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemsetD2D814hipDeviceptr_t6size_th6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD2D8()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemsetD2D8Async14hipDeviceptr_t6size_th6size_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD2D8Async()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMemsetD2D1614hipDeviceptr_t6size_tt6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD2D16()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemsetD2D16Async14hipDeviceptr_t6size_tt6size_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD2D16Async()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMemsetD2D3214hipDeviceptr_t6size_tj6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD2D32()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemsetD2D32Async14hipDeviceptr_t6size_tj6size_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD2D32Async()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemGetInfoP6size_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemGetInfo()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemPtrGetInfoPvP6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemPtrGetInfo()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMallocArrayP10hipArray_tPK20hipChannelFormatDesc6size_t6size_tj"><code class="docutils literal notranslate"><span class="pre">hipMallocArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipArrayCreateP10hipArray_tPK20HIP_ARRAY_DESCRIPTOR"><code class="docutils literal notranslate"><span class="pre">hipArrayCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipArrayDestroy10hipArray_t"><code class="docutils literal notranslate"><span class="pre">hipArrayDestroy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipArray3DCreateP10hipArray_tPK22HIP_ARRAY3D_DESCRIPTOR"><code class="docutils literal notranslate"><span class="pre">hipArray3DCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipMalloc3DP13hipPitchedPtr9hipExtent"><code class="docutils literal notranslate"><span class="pre">hipMalloc3D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipFreeArray10hipArray_t"><code class="docutils literal notranslate"><span class="pre">hipFreeArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMalloc3DArrayP10hipArray_tPK20hipChannelFormatDesc9hipExtentj"><code class="docutils literal notranslate"><span class="pre">hipMalloc3DArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipArrayGetInfoP20hipChannelFormatDescP9hipExtentPj10hipArray_t"><code class="docutils literal notranslate"><span class="pre">hipArrayGetInfo()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipArrayGetDescriptorP20HIP_ARRAY_DESCRIPTOR10hipArray_t"><code class="docutils literal notranslate"><span class="pre">hipArrayGetDescriptor()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipArray3DGetDescriptorP22HIP_ARRAY3D_DESCRIPTOR10hipArray_t"><code class="docutils literal notranslate"><span class="pre">hipArray3DGetDescriptor()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipMemcpy2DPv6size_tPKv6size_t6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemcpyParam2DPK12hip_Memcpy2D"><code class="docutils literal notranslate"><span class="pre">hipMemcpyParam2D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipMemcpyParam2DAsyncPK12hip_Memcpy2D11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyParam2DAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemcpy2DAsyncPv6size_tPKv6size_t6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2DAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemcpy2DToArray10hipArray_t6size_t6size_tPKv6size_t6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2DToArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipMemcpy2DToArrayAsync10hipArray_t6size_t6size_tPKv6size_t6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2DToArrayAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipMemcpy2DArrayToArray10hipArray_t6size_t6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2DArrayToArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipMemcpy2DFromArrayPv6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2DFromArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipMemcpy2DFromArrayAsyncPv6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2DFromArrayAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyAtoHPv10hipArray_t6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyAtoH()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyHtoA10hipArray_t6size_tPKv6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyHtoA()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipMemcpy3DPK16hipMemcpy3DParms"><code class="docutils literal notranslate"><span class="pre">hipMemcpy3D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemcpy3DAsyncPK16hipMemcpy3DParms11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpy3DAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipDrvMemcpy3DPK12HIP_MEMCPY3D"><code class="docutils literal notranslate"><span class="pre">hipDrvMemcpy3D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipDrvMemcpy3DAsyncPK12HIP_MEMCPY3D11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipDrvMemcpy3DAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipMemGetAddressRangeP14hipDeviceptr_tP6size_t14hipDeviceptr_t"><code class="docutils literal notranslate"><span class="pre">hipMemGetAddressRange()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemcpyBatchAsyncPPvPPvP6size_t6size_tP19hipMemcpyAttributesP6size_t6size_tP6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyBatchAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipMemcpy3DBatchAsync6size_tP18hipMemcpy3DBatchOpP6size_ty11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpy3DBatchAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipMemcpy3DPeerP20hipMemcpy3DPeerParms"><code class="docutils literal notranslate"><span class="pre">hipMemcpy3DPeer()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipMemcpy3DPeerAsyncP20hipMemcpy3DPeerParms11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpy3DPeerAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E19hipGetSymbolAddress10hipError_tPPvRK1T"><code class="docutils literal notranslate"><span class="pre">hipGetSymbolAddress()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E16hipGetSymbolSize10hipError_tP6size_tRK1T"><code class="docutils literal notranslate"><span class="pre">hipGetSymbolSize()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E17hipMemcpyToSymbol10hipError_tRK1TPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpyToSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E22hipMemcpyToSymbolAsync10hipError_tRK1TPKv6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyToSymbolAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E19hipMemcpyFromSymbol10hipError_tPvRK1T6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpyFromSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E24hipMemcpyFromSymbolAsync10hipError_tPvRK1T6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyFromSymbolAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E9hipMalloc10hipError_tPP1T6size_t"><code class="docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E14hipMallocPitch10hipError_tPP1TP6size_t6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMallocPitch()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E13hipHostMalloc10hipError_tPP1T6size_tj"><code class="docutils literal notranslate"><span class="pre">hipHostMalloc()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E12hipHostAlloc10hipError_tPP1T6size_tj"><code class="docutils literal notranslate"><span class="pre">hipHostAlloc()</span></code></a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="memory-management">
<span id="memory-management-reference"></span><h1>Memory management<a class="headerlink" href="#memory-management" title="Link to this heading">#</a></h1>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipPointerSetAttributePKv20hipPointer_attribute14hipDeviceptr_t">
<span id="_CPPv322hipPointerSetAttributePKv20hipPointer_attribute14hipDeviceptr_t"></span><span id="_CPPv222hipPointerSetAttributePKv20hipPointer_attribute14hipDeviceptr_t"></span><span id="hipPointerSetAttribute__voidCP.hipPointer_attribute.hipDeviceptr_t"></span><span class="target" id="group___memory_1gad35dd7d821d5a4d32693e3eada647177"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipPointerSetAttribute</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">hipPointer_attribute</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">attribute</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ptr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipPointerSetAttributePKv20hipPointer_attribute14hipDeviceptr_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets information on the specified pointer.[BETA]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>value</strong> – <strong>[in]</strong> Sets pointer attribute value </p></li>
<li><p><strong>attribute</strong> – <strong>[in]</strong> Attribute to set </p></li>
<li><p><strong>ptr</strong> – <strong>[in]</strong> Pointer to set attributes for</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidDevice, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipPointerGetAttributesP21hipPointerAttribute_tPKv">
<span id="_CPPv323hipPointerGetAttributesP21hipPointerAttribute_tPKv"></span><span id="_CPPv223hipPointerGetAttributesP21hipPointerAttribute_tPKv"></span><span id="hipPointerGetAttributes__hipPointerAttribute_tP.voidCP"></span><span class="target" id="group___memory_1ga7c3e8663feebb7be9fd3a1e5139bcefc"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipPointerGetAttributes</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipPointerAttribute_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">attributes</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ptr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipPointerGetAttributesP21hipPointerAttribute_tPKv" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns attributes for the specified pointer. </p>
<p>
The output parameter ‘attributes’ has a member named ‘type’ that describes what memory the pointer is associated with, such as device memory, host memory, managed memory, and others. Otherwise, the API cannot handle the pointer and returns hipErrorInvalidValue.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gaf147601f5094423a9810db112ef8ef07"><span class="std std-ref">hipPointerGetAttribute</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The unrecognized memory type is unsupported to keep the HIP functionality backward compatibility due to hipMemoryType enum values.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The current behavior of this HIP API corresponds to the CUDA API before version 11.0.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>attributes</strong> – <strong>[out]</strong> attributes for the specified pointer </p></li>
<li><p><strong>ptr</strong> – <strong>[in]</strong> pointer to get attributes for</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidDevice, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipPointerGetAttributePv20hipPointer_attribute14hipDeviceptr_t">
<span id="_CPPv322hipPointerGetAttributePv20hipPointer_attribute14hipDeviceptr_t"></span><span id="_CPPv222hipPointerGetAttributePv20hipPointer_attribute14hipDeviceptr_t"></span><span id="hipPointerGetAttribute__voidP.hipPointer_attribute.hipDeviceptr_t"></span><span class="target" id="group___memory_1gaf147601f5094423a9810db112ef8ef07"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipPointerGetAttribute</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">data</span></span>, <span class="n"><span class="pre">hipPointer_attribute</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">attribute</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ptr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipPointerGetAttributePv20hipPointer_attribute14hipDeviceptr_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns information about the specified pointer.[BETA]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga7c3e8663feebb7be9fd3a1e5139bcefc"><span class="std std-ref">hipPointerGetAttributes</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>data</strong> – <strong>[inout]</strong> Returned pointer attribute value </p></li>
<li><p><strong>attribute</strong> – <strong>[in]</strong> Attribute to query for </p></li>
<li><p><strong>ptr</strong> – <strong>[in]</strong> Pointer to get attributes for</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidDevice, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426hipDrvPointerGetAttributesjP20hipPointer_attributePPv14hipDeviceptr_t">
<span id="_CPPv326hipDrvPointerGetAttributesjP20hipPointer_attributePPv14hipDeviceptr_t"></span><span id="_CPPv226hipDrvPointerGetAttributesjP20hipPointer_attributePPv14hipDeviceptr_t"></span><span id="hipDrvPointerGetAttributes__unsigned-i.hipPointer_attributeP.voidPP.hipDeviceptr_t"></span><span class="target" id="group___memory_1gad0d11c0ccac6e262c147e5b47642cf1d"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDrvPointerGetAttributes</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numAttributes</span></span>, <span class="n"><span class="pre">hipPointer_attribute</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">attributes</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">data</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ptr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426hipDrvPointerGetAttributesjP20hipPointer_attributePPv14hipDeviceptr_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns information about the specified pointer.[BETA]. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gaf147601f5094423a9810db112ef8ef07"><span class="std std-ref">hipPointerGetAttribute</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>numAttributes</strong> – <strong>[in]</strong> number of attributes to query for </p></li>
<li><p><strong>attributes</strong> – <strong>[in]</strong> attributes to query for </p></li>
<li><p><strong>data</strong> – <strong>[inout]</strong> a two-dimensional containing pointers to memory locations where the result of each attribute query will be written to </p></li>
<li><p><strong>ptr</strong> – <strong>[in]</strong> pointer to get attributes for</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidDevice, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49hipMallocPPv6size_t">
<span id="_CPPv39hipMallocPPv6size_t"></span><span id="_CPPv29hipMallocPPv6size_t"></span><span id="hipMalloc__voidPP.s"></span><span class="target" id="group___memory_1ga4c6fcfe80010069d2792780d00dcead2"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMalloc</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49hipMallocPPv6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Allocate memory on the default accelerator. </p>
<p>
If size is 0, no memory is allocated, *ptr returns nullptr, and hipSuccess is returned.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga805c7320498926e444616fe090c727ee"><span class="std std-ref">hipMallocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga740d08da65cae1441ba32f8fedb863d1"><span class="std std-ref">hipFree</span></a>, <a class="reference internal" href="#group___memory_1ga8376a0644463118cd96432365bb470e3"><span class="std std-ref">hipMallocArray</span></a>, <a class="reference internal" href="#group___memory_1gad6c25b3106fb47a2a75285ff2bd8cb29"><span class="std std-ref">hipFreeArray</span></a>, <a class="reference internal" href="#group___memory_1gad12f684263bbc92690553af2aa918fd9"><span class="std std-ref">hipMalloc3D</span></a>, <a class="reference internal" href="#group___memory_1ga3be2acb8c75857958ddd1ab949ed4476"><span class="std std-ref">hipMalloc3DArray</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga2e543f58ee4544e317cd695d6d82e0a3"><span class="std std-ref">hipHostFree</span></a>, <a class="reference internal" href="#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1"><span class="std std-ref">hipHostMalloc</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ptr</strong> – <strong>[out]</strong> Pointer to the allocated memory </p></li>
<li><p><strong>size</strong> – <strong>[in]</strong> Requested memory size</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorOutOfMemory, hipErrorInvalidValue (bad context, null *ptr)</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipExtMallocWithFlagsPPv6size_tj">
<span id="_CPPv321hipExtMallocWithFlagsPPv6size_tj"></span><span id="_CPPv221hipExtMallocWithFlagsPPv6size_tj"></span><span id="hipExtMallocWithFlags__voidPP.s.unsigned-i"></span><span class="target" id="group___memory_1ga3529b96082582c65b645085491e91309"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipExtMallocWithFlags</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipExtMallocWithFlagsPPv6size_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Allocate memory on the default accelerator. </p>
<p>
If requested memory size is 0, no memory is allocated, *ptr returns nullptr, and hipSuccess is returned.</p>
<p>The memory allocation flag should be either hipDeviceMallocDefault, hipDeviceMallocFinegrained, hipDeviceMallocUncached, or hipMallocSignalMemory. If the flag is any other value, the API returns hipErrorInvalidValue.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga805c7320498926e444616fe090c727ee"><span class="std std-ref">hipMallocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga740d08da65cae1441ba32f8fedb863d1"><span class="std std-ref">hipFree</span></a>, <a class="reference internal" href="#group___memory_1ga8376a0644463118cd96432365bb470e3"><span class="std std-ref">hipMallocArray</span></a>, <a class="reference internal" href="#group___memory_1gad6c25b3106fb47a2a75285ff2bd8cb29"><span class="std std-ref">hipFreeArray</span></a>, <a class="reference internal" href="#group___memory_1gad12f684263bbc92690553af2aa918fd9"><span class="std std-ref">hipMalloc3D</span></a>, <a class="reference internal" href="#group___memory_1ga3be2acb8c75857958ddd1ab949ed4476"><span class="std std-ref">hipMalloc3DArray</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga2e543f58ee4544e317cd695d6d82e0a3"><span class="std std-ref">hipHostFree</span></a>, hiHostMalloc </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ptr</strong> – <strong>[out]</strong> Pointer to the allocated memory </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Requested memory size </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Type of memory allocation</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorOutOfMemory, hipErrorInvalidValue (bad context, null *ptr)</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipHostMallocPPv6size_tj">
<span id="_CPPv313hipHostMallocPPv6size_tj"></span><span id="_CPPv213hipHostMallocPPv6size_tj"></span><span id="hipHostMalloc__voidPP.s.unsigned-i"></span><span class="target" id="group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipHostMalloc</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipHostMallocPPv6size_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Allocates device accessible page locked (pinned) host memory. </p>
<p>This API allocates pinned host memory which is mapped into the address space of all GPUs in the system, the memory can be accessed directly by the GPU device, and can be read or written with much higher bandwidth than pageable memory obtained with functions such as malloc().</p>
<p>Using the pinned host memory, applications can implement faster data transfers for HostToDevice and DeviceToHost. The runtime tracks the hipHostMalloc allocations and can avoid some of the setup required for regular unpinned memory.</p>
<p>When the memory accesses are infrequent, zero-copy memory can be a good choice, for coherent allocation. GPU can directly access the host memory over the CPU/GPU interconnect, without need to copy the data.</p>
<p>Currently the allocation granularity is 4KB for the API.</p>
<p>Developers need to choose proper allocation flag with consideration of synchronization.</p>
<p>
If no input for flags, it will be the default pinned memory allocation on the host.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="device_management.html#group___device_1ga6e54db382768827e84725632018307aa"><span class="std std-ref">hipSetDeviceFlags</span></a>, hiptHostFree </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ptr</strong> – <strong>[out]</strong> Pointer to the allocated host pinned memory </p></li>
<li><p><strong>size</strong> – <strong>[in]</strong> Requested memory size in bytes If size is 0, no memory is allocated, *ptr returns nullptr, and hipSuccess is returned. </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Type of host memory allocation. See the description of flags in hipSetDeviceFlags.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorOutOfMemory</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412hipHostAllocPPv6size_tj">
<span id="_CPPv312hipHostAllocPPv6size_tj"></span><span id="_CPPv212hipHostAllocPPv6size_tj"></span><span id="hipHostAlloc__voidPP.s.unsigned-i"></span><span class="target" id="group___memory_1ga0e35f3397f6ea9c3f47a17461ae01231"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipHostAlloc</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412hipHostAllocPPv6size_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Allocate device accessible page locked host memory. </p>
<p>
If size is 0, no memory is allocated, *ptr returns nullptr, and hipSuccess is returned.</p>
<p>Flags:<ul class="simple">
<li><p>hipHostAllocDefault Default pinned memory allocation on the host.</p></li>
<li><p>hipHostAllocPortable Memory is considered allocated by all contexts.</p></li>
<li><p>hipHostAllocMapped Map the allocation into the address space for the current device.</p></li>
<li><p>hipHostAllocWriteCombined Allocates the memory as write-combined.</p></li>
<li><p>hipHostAllocUncached Allocate the host memory on extended fine grained access system memory pool</p></li>
</ul>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ptr</strong> – <strong>[out]</strong> Pointer to the allocated host pinned memory </p></li>
<li><p><strong>size</strong> – <strong>[in]</strong> Requested memory size in bytes </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Type of host memory allocation see below</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorOutOfMemory, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipHostGetDevicePointerPPvPvj">
<span id="_CPPv323hipHostGetDevicePointerPPvPvj"></span><span id="_CPPv223hipHostGetDevicePointerPPvPvj"></span><span id="hipHostGetDevicePointer__voidPP.voidP.unsigned-i"></span><span class="target" id="group___memory_1ga8fa7a0478020b835a24785cd6bb89725"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipHostGetDevicePointer</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">devPtr</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">hstPtr</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipHostGetDevicePointerPPvPvj" title="Link to this definition">#</a><br /></dt>
<dd><p>Get Device pointer from Host Pointer allocated through hipHostMalloc. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="device_management.html#group___device_1ga6e54db382768827e84725632018307aa"><span class="std std-ref">hipSetDeviceFlags</span></a>, <a class="reference internal" href="#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1"><span class="std std-ref">hipHostMalloc</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>devPtr</strong> – <strong>[out]</strong> Device Pointer mapped to passed host pointer </p></li>
<li><p><strong>hstPtr</strong> – <strong>[in]</strong> Host Pointer allocated through hipHostMalloc </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Flags to be passed for extension</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorOutOfMemory</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415hipHostGetFlagsPjPv">
<span id="_CPPv315hipHostGetFlagsPjPv"></span><span id="_CPPv215hipHostGetFlagsPjPv"></span><span id="hipHostGetFlags__unsigned-iP.voidP"></span><span class="target" id="group___memory_1ga4d26915873b3e3534ceb4dc310f8709a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipHostGetFlags</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">flagsPtr</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">hostPtr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415hipHostGetFlagsPjPv" title="Link to this definition">#</a><br /></dt>
<dd><p>Return flags associated with host pointer. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1"><span class="std std-ref">hipHostMalloc</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>flagsPtr</strong> – <strong>[out]</strong> Memory location to store flags </p></li>
<li><p><strong>hostPtr</strong> – <strong>[in]</strong> Host Pointer allocated through hipHostMalloc </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415hipHostRegisterPv6size_tj">
<span id="_CPPv315hipHostRegisterPv6size_tj"></span><span id="_CPPv215hipHostRegisterPv6size_tj"></span><span id="hipHostRegister__voidP.s.unsigned-i"></span><span class="target" id="group___memory_1gab8258f051e1a1f7385f794a15300e674"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipHostRegister</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">hostPtr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415hipHostRegisterPv6size_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Register host memory so it can be accessed from the current device. </p>
<p>
Flags:<ul class="simple">
<li><p>hipHostRegisterDefault Memory is Mapped and Portable</p></li>
<li><p>hipHostRegisterPortable Memory is considered registered by all contexts. HIP only supports one context so this is always assumed true.</p></li>
<li><p>hipHostRegisterMapped Map the allocation into the address space for the current device. The device pointer can be obtained with <a class="reference internal" href="#group___memory_1ga8fa7a0478020b835a24785cd6bb89725"><span class="std std-ref">hipHostGetDevicePointer</span></a>.</p></li>
<li><p>hipExtHostRegisterUncached Map the host memory onto extended fine grained access system memory pool.</p></li>
</ul>
</p>
<p>After registering the memory, use <a class="reference internal" href="#group___memory_1ga8fa7a0478020b835a24785cd6bb89725"><span class="std std-ref">hipHostGetDevicePointer</span></a> to obtain the mapped device pointer. On many systems, the mapped device pointer will have a different value than the mapped host pointer. Applications must use the device pointer in device code, and the host pointer in host code.</p>
<p>On some systems, registered memory is pinned. On some systems, registered memory may not be actually be pinned but uses OS or hardware facilities to all GPU access to the host memory.</p>
<p>Developers are strongly encouraged to register memory blocks which are aligned to the host cache-line size. (typically 64-bytes but can be obtains from the CPUID instruction).</p>
<p>If registering non-aligned pointers, the application must take care when register pointers from the same cache line on different devices. HIP’s coarse-grained synchronization model does not guarantee correct results if different devices write to different parts of the same cache block - typically one of the writes will “win” and overwrite data from the other registered memory region.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga4c9e1810b9f5858d36c4d28c91c86924"><span class="std std-ref">hipHostUnregister</span></a>, <a class="reference internal" href="#group___memory_1ga4d26915873b3e3534ceb4dc310f8709a"><span class="std std-ref">hipHostGetFlags</span></a>, <a class="reference internal" href="#group___memory_1ga8fa7a0478020b835a24785cd6bb89725"><span class="std std-ref">hipHostGetDevicePointer</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hostPtr</strong> – <strong>[out]</strong> Pointer to host memory to be registered. </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Size of the host memory </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> See below.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorOutOfMemory</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipHostUnregisterPv">
<span id="_CPPv317hipHostUnregisterPv"></span><span id="_CPPv217hipHostUnregisterPv"></span><span id="hipHostUnregister__voidP"></span><span class="target" id="group___memory_1ga4c9e1810b9f5858d36c4d28c91c86924"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipHostUnregister</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">hostPtr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipHostUnregisterPv" title="Link to this definition">#</a><br /></dt>
<dd><p>Un-register host pointer. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gab8258f051e1a1f7385f794a15300e674"><span class="std std-ref">hipHostRegister</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>hostPtr</strong> – <strong>[in]</strong> Host pointer previously registered with <a class="reference internal" href="#group___memory_1gab8258f051e1a1f7385f794a15300e674"><span class="std std-ref">hipHostRegister</span></a></p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Error code</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipMallocPitchPPvP6size_t6size_t6size_t">
<span id="_CPPv314hipMallocPitchPPvP6size_t6size_t6size_t"></span><span id="_CPPv214hipMallocPitchPPvP6size_t6size_t6size_t"></span><span id="hipMallocPitch__voidPP.sP.s.s"></span><span class="target" id="group___memory_1ga805c7320498926e444616fe090c727ee"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMallocPitch</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pitch</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipMallocPitchPPvP6size_t6size_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Allocates at least width (in bytes) * height bytes of linear memory Padding may occur to ensure alighnment requirements are met for the given row The change in width size due to padding will be returned in *pitch. Currently the alignment is set to 128 bytes</p>
<p>
If size is 0, no memory is allocated, *ptr returns nullptr, and hipSuccess is returned.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga4c6fcfe80010069d2792780d00dcead2"><span class="std std-ref">hipMalloc</span></a>, <a class="reference internal" href="#group___memory_1ga740d08da65cae1441ba32f8fedb863d1"><span class="std std-ref">hipFree</span></a>, <a class="reference internal" href="#group___memory_1ga8376a0644463118cd96432365bb470e3"><span class="std std-ref">hipMallocArray</span></a>, <a class="reference internal" href="#group___memory_1gad6c25b3106fb47a2a75285ff2bd8cb29"><span class="std std-ref">hipFreeArray</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga2e543f58ee4544e317cd695d6d82e0a3"><span class="std std-ref">hipHostFree</span></a>, <a class="reference internal" href="#group___memory_1gad12f684263bbc92690553af2aa918fd9"><span class="std std-ref">hipMalloc3D</span></a>, <a class="reference internal" href="#group___memory_1ga3be2acb8c75857958ddd1ab949ed4476"><span class="std std-ref">hipMalloc3DArray</span></a>, <a class="reference internal" href="#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1"><span class="std std-ref">hipHostMalloc</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ptr</strong> – <strong>[out]</strong> Pointer to the allocated device memory </p></li>
<li><p><strong>pitch</strong> – <strong>[out]</strong> Pitch for allocation (in bytes) </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Requested pitched allocation width (in bytes) </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Requested pitched allocation height</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Error code</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipMemAllocPitchP14hipDeviceptr_tP6size_t6size_t6size_tj">
<span id="_CPPv316hipMemAllocPitchP14hipDeviceptr_tP6size_t6size_t6size_tj"></span><span id="_CPPv216hipMemAllocPitchP14hipDeviceptr_tP6size_t6size_t6size_tj"></span><span id="hipMemAllocPitch__hipDeviceptr_tP.sP.s.s.unsigned-i"></span><span class="target" id="group___memory_1gad44d400532df8e67a6db45027cd05405"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemAllocPitch</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pitch</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">widthInBytes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">elementSizeBytes</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipMemAllocPitchP14hipDeviceptr_tP6size_t6size_t6size_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Allocates at least width (in bytes) * height bytes of linear memory Padding may occur to ensure alighnment requirements are met for the given row The change in width size due to padding will be returned in *pitch. Currently the alignment is set to 128 bytes</p>
<p>
If size is 0, no memory is allocated, <em>ptr returns nullptr, and hipSuccess is returned. The intended usage of pitch is as a separate parameter of the allocation, used to compute addresses within the 2D array. Given the row and column of an array element of type T, the address is computed as: T</em> pElement = (T*)((char*)BaseAddress + Row * Pitch) + Column;</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga4c6fcfe80010069d2792780d00dcead2"><span class="std std-ref">hipMalloc</span></a>, <a class="reference internal" href="#group___memory_1ga740d08da65cae1441ba32f8fedb863d1"><span class="std std-ref">hipFree</span></a>, <a class="reference internal" href="#group___memory_1ga8376a0644463118cd96432365bb470e3"><span class="std std-ref">hipMallocArray</span></a>, <a class="reference internal" href="#group___memory_1gad6c25b3106fb47a2a75285ff2bd8cb29"><span class="std std-ref">hipFreeArray</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga2e543f58ee4544e317cd695d6d82e0a3"><span class="std std-ref">hipHostFree</span></a>, <a class="reference internal" href="#group___memory_1gad12f684263bbc92690553af2aa918fd9"><span class="std std-ref">hipMalloc3D</span></a>, <a class="reference internal" href="#group___memory_1ga3be2acb8c75857958ddd1ab949ed4476"><span class="std std-ref">hipMalloc3DArray</span></a>, <a class="reference internal" href="#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1"><span class="std std-ref">hipHostMalloc</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dptr</strong> – <strong>[out]</strong> Pointer to the allocated device memory </p></li>
<li><p><strong>pitch</strong> – <strong>[out]</strong> Pitch for allocation (in bytes) </p></li>
<li><p><strong>widthInBytes</strong> – <strong>[in]</strong> Requested pitched allocation width (in bytes) </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Requested pitched allocation height </p></li>
<li><p><strong>elementSizeBytes</strong> – <strong>[in]</strong> The size of element bytes, should be 4, 8 or 16</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>Error code</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv47hipFreePv">
<span id="_CPPv37hipFreePv"></span><span id="_CPPv27hipFreePv"></span><span id="hipFree__voidP"></span><span class="target" id="group___memory_1ga740d08da65cae1441ba32f8fedb863d1"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipFree</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ptr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv47hipFreePv" title="Link to this definition">#</a><br /></dt>
<dd><p>Free memory allocated by the HIP-Clang hip memory allocation API. This API performs an implicit <a class="reference internal" href="device_management.html#group___device_1gaefdc2847fb1d6c3fb1354e827a191ebd"><span class="std std-ref">hipDeviceSynchronize()</span></a> call. If pointer is NULL, the hip runtime is initialized and hipSuccess is returned. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga4c6fcfe80010069d2792780d00dcead2"><span class="std std-ref">hipMalloc</span></a>, <a class="reference internal" href="#group___memory_1ga805c7320498926e444616fe090c727ee"><span class="std std-ref">hipMallocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8376a0644463118cd96432365bb470e3"><span class="std std-ref">hipMallocArray</span></a>, <a class="reference internal" href="#group___memory_1gad6c25b3106fb47a2a75285ff2bd8cb29"><span class="std std-ref">hipFreeArray</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga2e543f58ee4544e317cd695d6d82e0a3"><span class="std std-ref">hipHostFree</span></a>, <a class="reference internal" href="#group___memory_1gad12f684263bbc92690553af2aa918fd9"><span class="std std-ref">hipMalloc3D</span></a>, <a class="reference internal" href="#group___memory_1ga3be2acb8c75857958ddd1ab949ed4476"><span class="std std-ref">hipMalloc3DArray</span></a>, <a class="reference internal" href="#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1"><span class="std std-ref">hipHostMalloc</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>ptr</strong> – <strong>[in]</strong> Pointer to memory to be freed </p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess</p>
</dd>
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>hipErrorInvalidDevicePointer (if pointer is invalid, including host pointers allocated with hipHostMalloc)</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv411hipFreeHostPv">
<span id="_CPPv311hipFreeHostPv"></span><span id="_CPPv211hipFreeHostPv"></span><span id="hipFreeHost__voidP"></span><span class="target" id="group___memory_1ga28d7d92836116dfadeb62e416ee887d3"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipFreeHost</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ptr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv411hipFreeHostPv" title="Link to this definition">#</a><br /></dt>
<dd><p>Frees page-locked memory This API performs an implicit <a class="reference internal" href="device_management.html#group___device_1gaefdc2847fb1d6c3fb1354e827a191ebd"><span class="std std-ref">hipDeviceSynchronize()</span></a> call. If pointer is NULL, the hip runtime is initialized and hipSuccess is returned. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>ptr</strong> – <strong>[in]</strong> Pointer to memory to be freed </p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue (if pointer is invalid, including device pointers allocated with hipMalloc) </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind">
<span id="_CPPv39hipMemcpyPvPKv6size_t13hipMemcpyKind"></span><span id="_CPPv29hipMemcpyPvPKv6size_t13hipMemcpyKind"></span><span id="hipMemcpy__voidP.voidCP.s.hipMemcpyKind"></span><span class="target" id="group___memory_1gac1a055d288302edd641c6d7416858e1e"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Copy data from src to dst. </p>
<p>It supports memory from host to device, device to host, device to device and host to host The src and dst must not overlap.</p>
<p>For hipMemcpy, the copy is always performed by the current device (set by hipSetDevice). For multi-gpu or peer-to-peer configurations, it is recommended to set the current device to the device where the src data is physically located. For optimal peer-to-peer copies, the copy device must be able to access the src and dst pointers (by calling hipDeviceEnablePeerAccess with copy agent as the current device and src/dst as the peerDevice argument. if this is not done, the hipMemcpy will still work, but will perform the copy using a staging buffer on the host. Calling hipMemcpy with dst and src pointers that do not match the hipMemcpyKind results in undefined behavior.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Data being copy to </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Data being copy from </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Data size in bytes </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> Kind of transfer </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorUnknown</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipMemcpyWithStreamPvPKv6size_t13hipMemcpyKind11hipStream_t">
<span id="_CPPv319hipMemcpyWithStreamPvPKv6size_t13hipMemcpyKind11hipStream_t"></span><span id="_CPPv219hipMemcpyWithStreamPvPKv6size_t13hipMemcpyKind11hipStream_t"></span><span id="hipMemcpyWithStream__voidP.voidCP.s.hipMemcpyKind.hipStream_t"></span><span class="target" id="group___memory_1gae9ba7e2beacec0bd9d606ec8d241da37"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyWithStream</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipMemcpyWithStreamPvPKv6size_t13hipMemcpyKind11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Memory copy on the stream. It allows single or multiple devices to do memory copy on single or multiple streams. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="stream_management.html#group___stream_1gaff5b62d6e9502d80879f7176f4d03102"><span class="std std-ref">hipStreamCreate</span></a>, <a class="reference internal" href="stream_management.html#group___stream_1gabbfb9f573a6ebe8c478605ecb5504a74"><span class="std std-ref">hipStreamSynchronize</span></a>, <a class="reference internal" href="stream_management.html#group___stream_1ga3076a3499ed2c7821311006100bb95ec"><span class="std std-ref">hipStreamDestroy</span></a>, <a class="reference internal" href="device_management.html#group___device_1ga43c1e7f15925eeb762195ccb5e063eae"><span class="std std-ref">hipSetDevice</span></a>, hipLaunchKernelGGL </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Data being copy to </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Data being copy from </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Data size in bytes </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> Kind of transfer </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Valid stream </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorUnknown, hipErrorContextIsDestroyed</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipMemcpyHtoD14hipDeviceptr_tPKv6size_t">
<span id="_CPPv313hipMemcpyHtoD14hipDeviceptr_tPKv6size_t"></span><span id="_CPPv213hipMemcpyHtoD14hipDeviceptr_tPKv6size_t"></span><span id="hipMemcpyHtoD__hipDeviceptr_t.voidCP.s"></span><span class="target" id="group___memory_1gad9b6077f129d2694cda5e8c24b4bed0f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyHtoD</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipMemcpyHtoD14hipDeviceptr_tPKv6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copy data from Host to Device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Data being copy to </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Data being copy from </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Data size in bytes</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipMemcpyDtoHPv14hipDeviceptr_t6size_t">
<span id="_CPPv313hipMemcpyDtoHPv14hipDeviceptr_t6size_t"></span><span id="_CPPv213hipMemcpyDtoHPv14hipDeviceptr_t6size_t"></span><span id="hipMemcpyDtoH__voidP.hipDeviceptr_t.s"></span><span class="target" id="group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyDtoH</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipMemcpyDtoHPv14hipDeviceptr_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copy data from Device to Host. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Data being copy to </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Data being copy from </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Data size in bytes</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipMemcpyDtoD14hipDeviceptr_t14hipDeviceptr_t6size_t">
<span id="_CPPv313hipMemcpyDtoD14hipDeviceptr_t14hipDeviceptr_t6size_t"></span><span id="_CPPv213hipMemcpyDtoD14hipDeviceptr_t14hipDeviceptr_t6size_t"></span><span id="hipMemcpyDtoD__hipDeviceptr_t.hipDeviceptr_t.s"></span><span class="target" id="group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyDtoD</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipMemcpyDtoD14hipDeviceptr_t14hipDeviceptr_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copy data from Device to Device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Data being copy to </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Data being copy from </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Data size in bytes</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipMemcpyAtoD14hipDeviceptr_t10hipArray_t6size_t6size_t">
<span id="_CPPv313hipMemcpyAtoD14hipDeviceptr_t10hipArray_t6size_t6size_t"></span><span id="_CPPv213hipMemcpyAtoD14hipDeviceptr_t10hipArray_t6size_t6size_t"></span><span id="hipMemcpyAtoD__hipDeviceptr_t.hipArray_t.s.s"></span><span class="target" id="group___memory_1ga46d002bcd57e00d01615a118f2b230c3"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyAtoD</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstDevice</span></span>, <span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">srcArray</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">srcOffset</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ByteCount</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipMemcpyAtoD14hipDeviceptr_t10hipArray_t6size_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies from one 1D array to device memory. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dstDevice</strong> – <strong>[out]</strong> Destination device pointer </p></li>
<li><p><strong>srcArray</strong> – <strong>[in]</strong> Source array </p></li>
<li><p><strong>srcOffset</strong> – <strong>[in]</strong> Offset in bytes of source array </p></li>
<li><p><strong>ByteCount</strong> – <strong>[in]</strong> Size of memory copy in bytes</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipMemcpyDtoA10hipArray_t6size_t14hipDeviceptr_t6size_t">
<span id="_CPPv313hipMemcpyDtoA10hipArray_t6size_t14hipDeviceptr_t6size_t"></span><span id="_CPPv213hipMemcpyDtoA10hipArray_t6size_t14hipDeviceptr_t6size_t"></span><span id="hipMemcpyDtoA__hipArray_t.s.hipDeviceptr_t.s"></span><span class="target" id="group___memory_1ga91e920637e005ddec51610ef38b55285"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyDtoA</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstArray</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstOffset</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">srcDevice</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ByteCount</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipMemcpyDtoA10hipArray_t6size_t14hipDeviceptr_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies from device memory to a 1D array. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dstArray</strong> – <strong>[out]</strong> Destination array </p></li>
<li><p><strong>dstOffset</strong> – <strong>[in]</strong> Offset in bytes of destination array </p></li>
<li><p><strong>srcDevice</strong> – <strong>[in]</strong> Source device pointer </p></li>
<li><p><strong>ByteCount</strong> – <strong>[in]</strong> Size of memory copy in bytes</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipMemcpyAtoA10hipArray_t6size_t10hipArray_t6size_t6size_t">
<span id="_CPPv313hipMemcpyAtoA10hipArray_t6size_t10hipArray_t6size_t6size_t"></span><span id="_CPPv213hipMemcpyAtoA10hipArray_t6size_t10hipArray_t6size_t6size_t"></span><span id="hipMemcpyAtoA__hipArray_t.s.hipArray_t.s.s"></span><span class="target" id="group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyAtoA</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstArray</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstOffset</span></span>, <span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">srcArray</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">srcOffset</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ByteCount</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipMemcpyAtoA10hipArray_t6size_t10hipArray_t6size_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies from one 1D array to another. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dstArray</strong> – <strong>[out]</strong> Destination array </p></li>
<li><p><strong>dstOffset</strong> – <strong>[in]</strong> Offset in bytes of destination array </p></li>
<li><p><strong>srcArray</strong> – <strong>[in]</strong> Source array </p></li>
<li><p><strong>srcOffset</strong> – <strong>[in]</strong> Offset in bytes of source array </p></li>
<li><p><strong>ByteCount</strong> – <strong>[in]</strong> Size of memory copy in bytes</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipMemcpyHtoDAsync14hipDeviceptr_tPKv6size_t11hipStream_t">
<span id="_CPPv318hipMemcpyHtoDAsync14hipDeviceptr_tPKv6size_t11hipStream_t"></span><span id="_CPPv218hipMemcpyHtoDAsync14hipDeviceptr_tPKv6size_t11hipStream_t"></span><span id="hipMemcpyHtoDAsync__hipDeviceptr_t.voidCP.s.hipStream_t"></span><span class="target" id="group___memory_1gae6d39bd67777d55d555b24de221206b3"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyHtoDAsync</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipMemcpyHtoDAsync14hipDeviceptr_tPKv6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copy data from Host to Device asynchronously. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Data being copy to </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Data being copy from </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Data size in bytes </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream identifier</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipMemcpyDtoHAsyncPv14hipDeviceptr_t6size_t11hipStream_t">
<span id="_CPPv318hipMemcpyDtoHAsyncPv14hipDeviceptr_t6size_t11hipStream_t"></span><span id="_CPPv218hipMemcpyDtoHAsyncPv14hipDeviceptr_t6size_t11hipStream_t"></span><span id="hipMemcpyDtoHAsync__voidP.hipDeviceptr_t.s.hipStream_t"></span><span class="target" id="group___memory_1gad69da1994a646b843fb1fa465dbeb623"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyDtoHAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipMemcpyDtoHAsyncPv14hipDeviceptr_t6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copy data from Device to Host asynchronously. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Data being copy to </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Data being copy from </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Data size in bytes </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream identifier</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipMemcpyDtoDAsync14hipDeviceptr_t14hipDeviceptr_t6size_t11hipStream_t">
<span id="_CPPv318hipMemcpyDtoDAsync14hipDeviceptr_t14hipDeviceptr_t6size_t11hipStream_t"></span><span id="_CPPv218hipMemcpyDtoDAsync14hipDeviceptr_t14hipDeviceptr_t6size_t11hipStream_t"></span><span id="hipMemcpyDtoDAsync__hipDeviceptr_t.hipDeviceptr_t.s.hipStream_t"></span><span class="target" id="group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyDtoDAsync</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipMemcpyDtoDAsync14hipDeviceptr_t14hipDeviceptr_t6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copy data from Device to Device asynchronously. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Data being copy to </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Data being copy from </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Data size in bytes </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream identifier</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipMemcpyAtoHAsyncPv10hipArray_t6size_t6size_t11hipStream_t">
<span id="_CPPv318hipMemcpyAtoHAsyncPv10hipArray_t6size_t6size_t11hipStream_t"></span><span id="_CPPv218hipMemcpyAtoHAsyncPv10hipArray_t6size_t6size_t11hipStream_t"></span><span id="hipMemcpyAtoHAsync__voidP.hipArray_t.s.s.hipStream_t"></span><span class="target" id="group___memory_1ga25614799894ee316c4ce832a57a29741"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyAtoHAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dstHost</span></span>, <span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">srcArray</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">srcOffset</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ByteCount</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipMemcpyAtoHAsyncPv10hipArray_t6size_t6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies from one 1D array to host memory. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dstHost</strong> – <strong>[out]</strong> Destination pointer </p></li>
<li><p><strong>srcArray</strong> – <strong>[in]</strong> Source array </p></li>
<li><p><strong>srcOffset</strong> – <strong>[in]</strong> Offset in bytes of source array </p></li>
<li><p><strong>ByteCount</strong> – <strong>[in]</strong> Size of memory copy in bytes </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream identifier</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipMemcpyHtoAAsync10hipArray_t6size_tPKv6size_t11hipStream_t">
<span id="_CPPv318hipMemcpyHtoAAsync10hipArray_t6size_tPKv6size_t11hipStream_t"></span><span id="_CPPv218hipMemcpyHtoAAsync10hipArray_t6size_tPKv6size_t11hipStream_t"></span><span id="hipMemcpyHtoAAsync__hipArray_t.s.voidCP.s.hipStream_t"></span><span class="target" id="group___memory_1ga7458d07076c60e26707ea0522da8e694"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyHtoAAsync</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstArray</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstOffset</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">srcHost</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">ByteCount</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipMemcpyHtoAAsync10hipArray_t6size_tPKv6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies from host memory to a 1D array. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer </p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dstArray</strong> – <strong>[out]</strong> Destination array </p></li>
<li><p><strong>dstOffset</strong> – <strong>[in]</strong> Offset in bytes of destination array </p></li>
<li><p><strong>srcHost</strong> – <strong>[in]</strong> Source host pointer </p></li>
<li><p><strong>ByteCount</strong> – <strong>[in]</strong> Size of memory copy in bytes </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream identifier</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipGetSymbolAddressPPvPKv">
<span id="_CPPv319hipGetSymbolAddressPPvPKv"></span><span id="_CPPv219hipGetSymbolAddressPPvPKv"></span><span id="hipGetSymbolAddress__voidPP.voidCP"></span><span class="target" id="group___memory_1gaecac468bcedcfb139058df2d83d38987"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGetSymbolAddress</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">devPtr</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipGetSymbolAddressPPvPKv" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets device pointer associated with symbol on the device. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>devPtr</strong> – <strong>[out]</strong> pointer to the device associated the symbole </p></li>
<li><p><strong>symbol</strong> – <strong>[in]</strong> pointer to the symbole of the device</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipGetSymbolSizeP6size_tPKv">
<span id="_CPPv316hipGetSymbolSizeP6size_tPKv"></span><span id="_CPPv216hipGetSymbolSizeP6size_tPKv"></span><span id="hipGetSymbolSize__sP.voidCP"></span><span class="target" id="group___memory_1gae61bb9a71f0fe9b3eee29336d6b83d97"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGetSymbolSize</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">size</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipGetSymbolSizeP6size_tPKv" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the size of the given symbol on the device. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>symbol</strong> – <strong>[in]</strong> pointer to the device symbole </p></li>
<li><p><strong>size</strong> – <strong>[out]</strong> pointer to the size</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipGetProcAddressPKcPPvi8uint64_tP31hipDriverProcAddressQueryResult">
<span id="_CPPv317hipGetProcAddressPKcPPvi8uint64_tP31hipDriverProcAddressQueryResult"></span><span id="_CPPv217hipGetProcAddressPKcPPvi8uint64_tP31hipDriverProcAddressQueryResult"></span><span id="hipGetProcAddress__cCP.voidPP.i.uint64_t.hipDriverProcAddressQueryResultP"></span><span class="target" id="group___memory_1ga7823a32f9f6f133612c6288a0932bbc2"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGetProcAddress</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pfn</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hipVersion</span></span>, <span class="n"><span class="pre">uint64_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span>, <span class="n"><span class="pre">hipDriverProcAddressQueryResult</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbolStatus</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipGetProcAddressPKcPPvi8uint64_tP31hipDriverProcAddressQueryResult" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the pointer of requested HIP driver function. </p>
<p>
Returns hipSuccess if the returned pfn is addressed to the pointer of found driver function.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>symbol</strong> – <strong>[in]</strong> The Symbol name of the driver function to request. </p></li>
<li><p><strong>pfn</strong> – <strong>[out]</strong> Output pointer to the requested driver function. </p></li>
<li><p><strong>hipVersion</strong> – <strong>[in]</strong> The HIP version for the requested driver function symbol. HIP version is defined as 100*version_major + version_minor. For example, in HIP 6.1, the hipversion is 601, for the symbol function “hipGetDeviceProperties”, the specified hipVersion 601 is greater or equal to the version 600, the symbol function will be handle properly as backend compatible function.</p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Currently only default flag is suppported. </p></li>
<li><p><strong>symbolStatus</strong> – <strong>[out]</strong> Optional enumeration for returned status of searching for symbol driver function based on the input hipVersion.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipMemcpyToSymbolPKvPKv6size_t6size_t13hipMemcpyKind">
<span id="_CPPv317hipMemcpyToSymbolPKvPKv6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv217hipMemcpyToSymbolPKvPKv6size_t6size_t13hipMemcpyKind"></span><span id="hipMemcpyToSymbol__voidCP.voidCP.s.s.hipMemcpyKind"></span><span class="target" id="group___memory_1gac0d988981c8535af1712f1f57436869b"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyToSymbol</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipMemcpyToSymbolPKvPKv6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data to the given symbol on the device. Symbol HIP APIs allow a kernel to define a device-side data symbol which can be accessed on the host side. The symbol can be in __constant or device space. Note that the symbol name needs to be encased in the HIP_SYMBOL macro. This also applies to hipMemcpyFromSymbol, hipGetSymbolAddress, and hipGetSymbolSize. For detailed usage, see the <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_porting_guide.html#memcpytosymbol">memcpyToSymbol example</a> in the HIP Porting Guide. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>symbol</strong> – <strong>[out]</strong> pointer to the device symbole </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> pointer to the source address </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> size in bytes to copy </p></li>
<li><p><strong>offset</strong> – <strong>[in]</strong> offset in bytes from start of symbole </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> type of memory transfer</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipMemcpyToSymbolAsyncPKvPKv6size_t6size_t13hipMemcpyKind11hipStream_t">
<span id="_CPPv322hipMemcpyToSymbolAsyncPKvPKv6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span id="_CPPv222hipMemcpyToSymbolAsyncPKvPKv6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span id="hipMemcpyToSymbolAsync__voidCP.voidCP.s.s.hipMemcpyKind.hipStream_t"></span><span class="target" id="group___memory_1gaaceb6e89fb822d3a8e387b526b718478"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyToSymbolAsync</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipMemcpyToSymbolAsyncPKvPKv6size_t6size_t13hipMemcpyKind11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data to the given symbol on the device asynchronously. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>symbol</strong> – <strong>[out]</strong> pointer to the device symbole </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> pointer to the source address </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> size in bytes to copy </p></li>
<li><p><strong>offset</strong> – <strong>[in]</strong> offset in bytes from start of symbole </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> type of memory transfer </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> stream identifier</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipMemcpyFromSymbolPvPKv6size_t6size_t13hipMemcpyKind">
<span id="_CPPv319hipMemcpyFromSymbolPvPKv6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv219hipMemcpyFromSymbolPvPKv6size_t6size_t13hipMemcpyKind"></span><span id="hipMemcpyFromSymbol__voidP.voidCP.s.s.hipMemcpyKind"></span><span class="target" id="group___memory_1ga5e06c171bb33ac109bf9e642bea57314"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyFromSymbol</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipMemcpyFromSymbolPvPKv6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data from the given symbol on the device. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Returns pointer to destinition memory address </p></li>
<li><p><strong>symbol</strong> – <strong>[in]</strong> Pointer to the symbole address on the device </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Size in bytes to copy </p></li>
<li><p><strong>offset</strong> – <strong>[in]</strong> Offset in bytes from the start of symbole </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> Type of memory transfer</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424hipMemcpyFromSymbolAsyncPvPKv6size_t6size_t13hipMemcpyKind11hipStream_t">
<span id="_CPPv324hipMemcpyFromSymbolAsyncPvPKv6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span id="_CPPv224hipMemcpyFromSymbolAsyncPvPKv6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span id="hipMemcpyFromSymbolAsync__voidP.voidCP.s.s.hipMemcpyKind.hipStream_t"></span><span class="target" id="group___memory_1ga50a9366e07b89172e140203a744a80c5"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyFromSymbolAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424hipMemcpyFromSymbolAsyncPvPKv6size_t6size_t13hipMemcpyKind11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data from the given symbol on the device asynchronously. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Returns pointer to destinition memory address </p></li>
<li><p><strong>symbol</strong> – <strong>[in]</strong> pointer to the symbole address on the device </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> size in bytes to copy </p></li>
<li><p><strong>offset</strong> – <strong>[in]</strong> offset in bytes from the start of symbole </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> type of memory transfer </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> stream identifier</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipMemcpyAsyncPvPKv6size_t13hipMemcpyKind11hipStream_t">
<span id="_CPPv314hipMemcpyAsyncPvPKv6size_t13hipMemcpyKind11hipStream_t"></span><span id="_CPPv214hipMemcpyAsyncPvPKv6size_t13hipMemcpyKind11hipStream_t"></span><span id="hipMemcpyAsync__voidP.voidCP.s.hipMemcpyKind.hipStream_t"></span><span class="target" id="group___memory_1gad55fa9f5980b711bc93c52820149ba18"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipMemcpyAsyncPvPKv6size_t13hipMemcpyKind11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data from src to dst asynchronously. </p>
<p>The copy is always performed by the device associated with the specified stream.</p>
<p>For multi-gpu or peer-to-peer configurations, it is recommended to use a stream which is attached to the device where the src data is physically located. For optimal peer-to-peer copies, the copy device must be able to access the src and dst pointers (by calling hipDeviceEnablePeerAccess) with copy agent as the current device and src/dest as the peerDevice argument. If enabling device peer access is not done, the memory copy will still work, but will perform the copy using a staging buffer on the host.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga835954048fd6cf0b4de065ada300d8ef"><span class="std std-ref">hipMemcpyToArray</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1ga9c5763233c9803b8e964881487fc4e60"><span class="std std-ref">hipMemcpy2DFromArray</span></a>, hipMemcpyArrayToArray, <a class="reference internal" href="#group___memory_1ga11a0bead0f40a85a212f8a686b72b243"><span class="std std-ref">hipMemcpy2DArrayToArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1ga5e06c171bb33ac109bf9e642bea57314"><span class="std std-ref">hipMemcpyFromSymbol</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpyToArrayAsync, <a class="reference internal" href="#group___memory_1gab6953ee5f575d0324c19ffc51a72f8fb"><span class="std std-ref">hipMemcpy2DToArrayAsync</span></a>, hipMemcpyFromArrayAsync, <a class="reference internal" href="#group___memory_1ga946fe29e78ce1580cb95fa2210389263"><span class="std std-ref">hipMemcpy2DFromArrayAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaceb6e89fb822d3a8e387b526b718478"><span class="std std-ref">hipMemcpyToSymbolAsync</span></a>, <a class="reference internal" href="#group___memory_1ga50a9366e07b89172e140203a744a80c5"><span class="std std-ref">hipMemcpyFromSymbolAsync</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If host or dst are not pinned, the memory copy will be performed synchronously. For best performance, use hipHostMalloc to allocate host memory that is transferred asynchronously.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Data being copy to </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Data being copy from </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Data size in bytes </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> Type of memory transfer </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream identifier </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorUnknown</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49hipMemsetPvi6size_t">
<span id="_CPPv39hipMemsetPvi6size_t"></span><span id="_CPPv29hipMemsetPvi6size_t"></span><span id="hipMemset__voidP.i.s"></span><span class="target" id="group___memory_1gac7441e74affcce4b8b69dba996c5ebc4"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemset</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49hipMemsetPvi6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills the first sizeBytes bytes of the memory area pointed to by dest with the constant byte value value. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Data being filled </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Value to be set </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Data size in bytes </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv411hipMemsetD814hipDeviceptr_th6size_t">
<span id="_CPPv311hipMemsetD814hipDeviceptr_th6size_t"></span><span id="_CPPv211hipMemsetD814hipDeviceptr_th6size_t"></span><span id="hipMemsetD8__hipDeviceptr_t.unsigned-c.s"></span><span class="target" id="group___memory_1gad484d4b0a7e178d1d180498625b6122f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetD8</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dest</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv411hipMemsetD814hipDeviceptr_th6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills the first sizeBytes bytes of the memory area pointed to by dest with the constant byte value value. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dest</strong> – <strong>[out]</strong> Data ptr to be filled </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Value to be set </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> Number of values to be set </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipMemsetD8Async14hipDeviceptr_th6size_t11hipStream_t">
<span id="_CPPv316hipMemsetD8Async14hipDeviceptr_th6size_t11hipStream_t"></span><span id="_CPPv216hipMemsetD8Async14hipDeviceptr_th6size_t11hipStream_t"></span><span id="hipMemsetD8Async__hipDeviceptr_t.unsigned-c.s.hipStream_t"></span><span class="target" id="group___memory_1ga11b214a1af7b60f85694331802dd557c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetD8Async</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dest</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipMemsetD8Async14hipDeviceptr_th6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills the first sizeBytes bytes of the memory area pointed to by dest with the constant byte value value. </p>
<p><a class="reference internal" href="#group___memory_1ga11b214a1af7b60f85694331802dd557c"><span class="std std-ref">hipMemsetD8Async()</span></a> is asynchronous with respect to the host, so the call may return before the memset is complete. The operation can optionally be associated to a stream by passing a non-zero stream argument. If stream is non-zero, the operation may overlap with operations in other streams.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dest</strong> – <strong>[out]</strong> Data ptr to be filled </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Constant value to be set </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> Number of values to be set </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream identifier </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412hipMemsetD1614hipDeviceptr_tt6size_t">
<span id="_CPPv312hipMemsetD1614hipDeviceptr_tt6size_t"></span><span id="_CPPv212hipMemsetD1614hipDeviceptr_tt6size_t"></span><span id="hipMemsetD16__hipDeviceptr_t.unsigned-short.s"></span><span class="target" id="group___memory_1ga3ee39cf8737f4a5d0e1e8c9eb870f02f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetD16</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dest</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">short</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412hipMemsetD1614hipDeviceptr_tt6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills the first sizeBytes bytes of the memory area pointed to by dest with the constant short value value. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dest</strong> – <strong>[out]</strong> Data ptr to be filled </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Constant value to be set </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> Number of values to be set </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipMemsetD16Async14hipDeviceptr_tt6size_t11hipStream_t">
<span id="_CPPv317hipMemsetD16Async14hipDeviceptr_tt6size_t11hipStream_t"></span><span id="_CPPv217hipMemsetD16Async14hipDeviceptr_tt6size_t11hipStream_t"></span><span id="hipMemsetD16Async__hipDeviceptr_t.unsigned-short.s.hipStream_t"></span><span class="target" id="group___memory_1ga76cf7b34d3d8dad2fb5c4959cfd1a988"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetD16Async</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dest</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">short</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipMemsetD16Async14hipDeviceptr_tt6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills the first sizeBytes bytes of the memory area pointed to by dest with the constant short value value. </p>
<p><a class="reference internal" href="#group___memory_1ga76cf7b34d3d8dad2fb5c4959cfd1a988"><span class="std std-ref">hipMemsetD16Async()</span></a> is asynchronous with respect to the host, so the call may return before the memset is complete. The operation can optionally be associated to a stream by passing a non-zero stream argument. If stream is non-zero, the operation may overlap with operations in other streams.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dest</strong> – <strong>[out]</strong> Data ptr to be filled </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Constant value to be set </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> Number of values to be set </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream identifier </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412hipMemsetD3214hipDeviceptr_ti6size_t">
<span id="_CPPv312hipMemsetD3214hipDeviceptr_ti6size_t"></span><span id="_CPPv212hipMemsetD3214hipDeviceptr_ti6size_t"></span><span id="hipMemsetD32__hipDeviceptr_t.i.s"></span><span class="target" id="group___memory_1ga54b16e2fd8d6230c22193ae11b58486b"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetD32</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dest</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412hipMemsetD3214hipDeviceptr_ti6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills the memory area pointed to by dest with the constant integer value for specified number of times. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dest</strong> – <strong>[out]</strong> Data being filled </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Constant value to be set </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> Number of values to be set </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipMemsetAsyncPvi6size_t11hipStream_t">
<span id="_CPPv314hipMemsetAsyncPvi6size_t11hipStream_t"></span><span id="_CPPv214hipMemsetAsyncPvi6size_t11hipStream_t"></span><span id="hipMemsetAsync__voidP.i.s.hipStream_t"></span><span class="target" id="group___memory_1gae7d90e14c387e49f10db597f12915c54"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipMemsetAsyncPvi6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills the first sizeBytes bytes of the memory area pointed to by dev with the constant byte value value. </p>
<p><a class="reference internal" href="#group___memory_1gae7d90e14c387e49f10db597f12915c54"><span class="std std-ref">hipMemsetAsync()</span></a> is asynchronous with respect to the host, so the call may return before the memset is complete. The operation can optionally be associated to a stream by passing a non-zero stream argument. If stream is non-zero, the operation may overlap with operations in other streams.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Pointer to device memory </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Value to set for each byte of specified memory </p></li>
<li><p><strong>sizeBytes</strong> – <strong>[in]</strong> Size in bytes to set </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream identifier </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipMemsetD32Async14hipDeviceptr_ti6size_t11hipStream_t">
<span id="_CPPv317hipMemsetD32Async14hipDeviceptr_ti6size_t11hipStream_t"></span><span id="_CPPv217hipMemsetD32Async14hipDeviceptr_ti6size_t11hipStream_t"></span><span id="hipMemsetD32Async__hipDeviceptr_t.i.s.hipStream_t"></span><span class="target" id="group___memory_1gae0e29827e32436fc6f0431b865e32244"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetD32Async</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipMemsetD32Async14hipDeviceptr_ti6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills the memory area pointed to by dev with the constant integer value for specified number of times. </p>
<p><a class="reference internal" href="#group___memory_1gae0e29827e32436fc6f0431b865e32244"><span class="std std-ref">hipMemsetD32Async()</span></a> is asynchronous with respect to the host, so the call may return before the memset is complete. The operation can optionally be associated to a stream by passing a non-zero stream argument. If stream is non-zero, the operation may overlap with operations in other streams.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Pointer to device memory </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Value to set for each byte of specified memory </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> Number of values to be set </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream identifier </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv411hipMemset2DPv6size_ti6size_t6size_t">
<span id="_CPPv311hipMemset2DPv6size_ti6size_t6size_t"></span><span id="_CPPv211hipMemset2DPv6size_ti6size_t6size_t"></span><span id="hipMemset2D__voidP.s.i.s.s"></span><span class="target" id="group___memory_1gae1e7b4c740cc02611ea8122bec376201"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemset2D</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">pitch</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv411hipMemset2DPv6size_ti6size_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills the memory area pointed to by dst with the constant value. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[out]</strong> Pointer to 2D device memory </p></li>
<li><p><strong>pitch</strong> – <strong>[in]</strong> Pitch size in bytes of 2D device memory, unused if height equals 1 </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Constant value to set for each byte of specified memory </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width size in bytes in 2D memory </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Height size in bytes in 2D memory </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipMemset2DAsyncPv6size_ti6size_t6size_t11hipStream_t">
<span id="_CPPv316hipMemset2DAsyncPv6size_ti6size_t6size_t11hipStream_t"></span><span id="_CPPv216hipMemset2DAsyncPv6size_ti6size_t6size_t11hipStream_t"></span><span id="hipMemset2DAsync__voidP.s.i.s.s.hipStream_t"></span><span class="target" id="group___memory_1ga2bac47006b553a69424431c0445f8e95"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemset2DAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">pitch</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipMemset2DAsyncPv6size_ti6size_t6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills asynchronously the memory area pointed to by dst with the constant value. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Pointer to 2D device memory </p></li>
<li><p><strong>pitch</strong> – <strong>[in]</strong> Pitch size in bytes of 2D device memory, unused if height equals 1 </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Value to set for each byte of specified memory </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width size in bytes in 2D memory </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Height size in bytes in 2D memory </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream identifier </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv411hipMemset3D13hipPitchedPtri9hipExtent">
<span id="_CPPv311hipMemset3D13hipPitchedPtri9hipExtent"></span><span id="_CPPv211hipMemset3D13hipPitchedPtri9hipExtent"></span><span id="hipMemset3D__hipPitchedPtr.i.hipExtent"></span><span class="target" id="group___memory_1ga3c04a21c9de9c55b3e47d8c87a0b0593"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemset3D</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipPitchedPtr</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">pitchedDevPtr</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">hipExtent</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">extent</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv411hipMemset3D13hipPitchedPtri9hipExtent" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills synchronously the memory area pointed to by pitchedDevPtr with the constant value. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pitchedDevPtr</strong> – <strong>[in]</strong> Pointer to pitched device memory </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Value to set for each byte of specified memory </p></li>
<li><p><strong>extent</strong> – <strong>[in]</strong> Size parameters for width field in bytes in device memory </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipMemset3DAsync13hipPitchedPtri9hipExtent11hipStream_t">
<span id="_CPPv316hipMemset3DAsync13hipPitchedPtri9hipExtent11hipStream_t"></span><span id="_CPPv216hipMemset3DAsync13hipPitchedPtri9hipExtent11hipStream_t"></span><span id="hipMemset3DAsync__hipPitchedPtr.i.hipExtent.hipStream_t"></span><span class="target" id="group___memory_1ga5565cddc90c7ebd0f8b081d5440b3166"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemset3DAsync</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipPitchedPtr</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">pitchedDevPtr</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">hipExtent</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">extent</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipMemset3DAsync13hipPitchedPtri9hipExtent11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills asynchronously the memory area pointed to by pitchedDevPtr with the constant value. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pitchedDevPtr</strong> – <strong>[in]</strong> Pointer to pitched device memory </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Value to set for each byte of specified memory </p></li>
<li><p><strong>extent</strong> – <strong>[in]</strong> Size parameters for width field in bytes in device memory </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream identifier </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipMemsetD2D814hipDeviceptr_t6size_th6size_t6size_t">
<span id="_CPPv313hipMemsetD2D814hipDeviceptr_t6size_th6size_t6size_t"></span><span id="_CPPv213hipMemsetD2D814hipDeviceptr_t6size_th6size_t6size_t"></span><span id="hipMemsetD2D8__hipDeviceptr_t.s.unsigned-c.s.s"></span><span class="target" id="group___memory_1gab5d49a6cc5782f99a9453e174c3b127c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetD2D8</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstPitch</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipMemsetD2D814hipDeviceptr_t6size_th6size_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills 2D memory range of ‘width’ 8-bit values synchronously to the specified char value. Height specifies numbers of rows to set and dstPitch speicifies the number of bytes between each row. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Pointer to device memory </p></li>
<li><p><strong>dstPitch</strong> – <strong>[in]</strong> Pitch of dst device pointer </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> value to set </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width of row </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Number of rows </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipMemsetD2D8Async14hipDeviceptr_t6size_th6size_t6size_t11hipStream_t">
<span id="_CPPv318hipMemsetD2D8Async14hipDeviceptr_t6size_th6size_t6size_t11hipStream_t"></span><span id="_CPPv218hipMemsetD2D8Async14hipDeviceptr_t6size_th6size_t6size_t11hipStream_t"></span><span id="hipMemsetD2D8Async__hipDeviceptr_t.s.unsigned-c.s.s.hipStream_t"></span><span class="target" id="group___memory_1gaf2751a9fd31589c76761787d96bbb3f9"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetD2D8Async</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstPitch</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipMemsetD2D8Async14hipDeviceptr_t6size_th6size_t6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills 2D memory range of ‘width’ 8-bit values asynchronously to the specified char value. Height specifies numbers of rows to set and dstPitch speicifies the number of bytes between each row. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Pointer to device memory </p></li>
<li><p><strong>dstPitch</strong> – <strong>[in]</strong> Pitch of dst device pointer </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> value to set </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width of row </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Number of rows </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream Identifier </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipMemsetD2D1614hipDeviceptr_t6size_tt6size_t6size_t">
<span id="_CPPv314hipMemsetD2D1614hipDeviceptr_t6size_tt6size_t6size_t"></span><span id="_CPPv214hipMemsetD2D1614hipDeviceptr_t6size_tt6size_t6size_t"></span><span id="hipMemsetD2D16__hipDeviceptr_t.s.unsigned-short.s.s"></span><span class="target" id="group___memory_1gabbdd160d602e9ec0f749ff20b461a0ff"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetD2D16</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstPitch</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">short</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipMemsetD2D1614hipDeviceptr_t6size_tt6size_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills 2D memory range of ‘width’ 16-bit values synchronously to the specified short value. Height specifies numbers of rows to set and dstPitch speicifies the number of bytes between each row. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Pointer to device memory </p></li>
<li><p><strong>dstPitch</strong> – <strong>[in]</strong> Pitch of dst device pointer </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> value to set </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width of row </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Number of rows </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipMemsetD2D16Async14hipDeviceptr_t6size_tt6size_t6size_t11hipStream_t">
<span id="_CPPv319hipMemsetD2D16Async14hipDeviceptr_t6size_tt6size_t6size_t11hipStream_t"></span><span id="_CPPv219hipMemsetD2D16Async14hipDeviceptr_t6size_tt6size_t6size_t11hipStream_t"></span><span id="hipMemsetD2D16Async__hipDeviceptr_t.s.unsigned-short.s.s.hipStream_t"></span><span class="target" id="group___memory_1ga99fbda39f6b7823a98ce240a9806347c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetD2D16Async</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstPitch</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">short</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipMemsetD2D16Async14hipDeviceptr_t6size_tt6size_t6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills 2D memory range of ‘width’ 16-bit values asynchronously to the specified short value. Height specifies numbers of rows to set and dstPitch speicifies the number of bytes between each row. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Pointer to device memory </p></li>
<li><p><strong>dstPitch</strong> – <strong>[in]</strong> Pitch of dst device pointer </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> value to set </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width of row </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Number of rows </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream Identifier </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipMemsetD2D3214hipDeviceptr_t6size_tj6size_t6size_t">
<span id="_CPPv314hipMemsetD2D3214hipDeviceptr_t6size_tj6size_t6size_t"></span><span id="_CPPv214hipMemsetD2D3214hipDeviceptr_t6size_tj6size_t6size_t"></span><span id="hipMemsetD2D32__hipDeviceptr_t.s.unsigned-i.s.s"></span><span class="target" id="group___memory_1ga522627ea02f657f4235376f5ed9ace4c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetD2D32</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstPitch</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipMemsetD2D3214hipDeviceptr_t6size_tj6size_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills 2D memory range of ‘width’ 32-bit values synchronously to the specified int value. Height specifies numbers of rows to set and dstPitch speicifies the number of bytes between each row. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Pointer to device memory </p></li>
<li><p><strong>dstPitch</strong> – <strong>[in]</strong> Pitch of dst device pointer </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> value to set </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width of row </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Number of rows </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipMemsetD2D32Async14hipDeviceptr_t6size_tj6size_t6size_t11hipStream_t">
<span id="_CPPv319hipMemsetD2D32Async14hipDeviceptr_t6size_tj6size_t6size_t11hipStream_t"></span><span id="_CPPv219hipMemsetD2D32Async14hipDeviceptr_t6size_tj6size_t6size_t11hipStream_t"></span><span id="hipMemsetD2D32Async__hipDeviceptr_t.s.unsigned-i.s.s.hipStream_t"></span><span class="target" id="group___memory_1ga675985ebfe6611556955dc88195937d6"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemsetD2D32Async</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstPitch</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipMemsetD2D32Async14hipDeviceptr_t6size_tj6size_t6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Fills 2D memory range of ‘width’ 32-bit values asynchronously to the specified int value. Height specifies numbers of rows to set and dstPitch speicifies the number of bytes between each row. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Pointer to device memory </p></li>
<li><p><strong>dstPitch</strong> – <strong>[in]</strong> Pitch of dst device pointer </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> value to set </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width of row </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Number of rows </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream Identifier </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipMemGetInfoP6size_tP6size_t">
<span id="_CPPv313hipMemGetInfoP6size_tP6size_t"></span><span id="_CPPv213hipMemGetInfoP6size_tP6size_t"></span><span id="hipMemGetInfo__sP.sP"></span><span class="target" id="group___memory_1ga311c3e246a21590de14478b8bd063be2"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemGetInfo</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">free</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">total</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipMemGetInfoP6size_tP6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Query memory info. </p>
<p>On ROCM, this function gets the actual free memory left on the current device, so supports the cases while running multi-workload (such as multiple processes, multiple threads, and multiple GPUs).</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>On Windows, the free memory only accounts for memory allocated by this process and may be optimistic.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>free</strong> – <strong>[out]</strong> Returns free memory on the current device in bytes </p></li>
<li><p><strong>total</strong> – <strong>[out]</strong> Returns total allocatable memory on the current device in bytes</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidDevice, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipMemPtrGetInfoPvP6size_t">
<span id="_CPPv316hipMemPtrGetInfoPvP6size_t"></span><span id="_CPPv216hipMemPtrGetInfoPvP6size_t"></span><span id="hipMemPtrGetInfo__voidP.sP"></span><span class="target" id="group___memory_1gaf7e9522b8fd7bae6cc1bf2e3238fd20f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPtrGetInfo</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">size</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipMemPtrGetInfoPvP6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Get allocated memory size via memory pointer. </p>
<p>This function gets the allocated shared virtual memory size from memory pointer.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ptr</strong> – <strong>[in]</strong> Pointer to allocated memory </p></li>
<li><p><strong>size</strong> – <strong>[out]</strong> Returns the allocated memory size in bytes</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipMallocArrayP10hipArray_tPK20hipChannelFormatDesc6size_t6size_tj">
<span id="_CPPv314hipMallocArrayP10hipArray_tPK20hipChannelFormatDesc6size_t6size_tj"></span><span id="_CPPv214hipMallocArrayP10hipArray_tPK20hipChannelFormatDesc6size_t6size_tj"></span><span id="hipMallocArray__hipArray_tP.hipChannelFormatDescCP.s.s.unsigned-i"></span><span class="target" id="group___memory_1ga8376a0644463118cd96432365bb470e3"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMallocArray</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">array</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipChannelFormatDesc</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">desc</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipMallocArrayP10hipArray_tPK20hipChannelFormatDesc6size_t6size_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Allocate an array on the device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga4c6fcfe80010069d2792780d00dcead2"><span class="std std-ref">hipMalloc</span></a>, <a class="reference internal" href="#group___memory_1ga805c7320498926e444616fe090c727ee"><span class="std std-ref">hipMallocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga740d08da65cae1441ba32f8fedb863d1"><span class="std std-ref">hipFree</span></a>, <a class="reference internal" href="#group___memory_1gad6c25b3106fb47a2a75285ff2bd8cb29"><span class="std std-ref">hipFreeArray</span></a>, <a class="reference internal" href="#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1"><span class="std std-ref">hipHostMalloc</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga2e543f58ee4544e317cd695d6d82e0a3"><span class="std std-ref">hipHostFree</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>array</strong> – <strong>[out]</strong> Pointer to allocated array in device memory </p></li>
<li><p><strong>desc</strong> – <strong>[in]</strong> Requested channel format </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Requested array allocation width </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Requested array allocation height </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Requested properties of allocated array </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorOutOfMemory</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipArrayCreateP10hipArray_tPK20HIP_ARRAY_DESCRIPTOR">
<span id="_CPPv314hipArrayCreateP10hipArray_tPK20HIP_ARRAY_DESCRIPTOR"></span><span id="_CPPv214hipArrayCreateP10hipArray_tPK20HIP_ARRAY_DESCRIPTOR"></span><span id="hipArrayCreate__hipArray_tP.HIP_ARRAY_DESCRIPTORCP"></span><span class="target" id="group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipArrayCreate</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pHandle</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">HIP_ARRAY_DESCRIPTOR</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pAllocateArray</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipArrayCreateP10hipArray_tPK20HIP_ARRAY_DESCRIPTOR" title="Link to this definition">#</a><br /></dt>
<dd><p>Create an array memory pointer on the device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga8376a0644463118cd96432365bb470e3"><span class="std std-ref">hipMallocArray</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1gad6c25b3106fb47a2a75285ff2bd8cb29"><span class="std std-ref">hipFreeArray</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pHandle</strong> – <strong>[out]</strong> Pointer to the array memory </p></li>
<li><p><strong>pAllocateArray</strong> – <strong>[in]</strong> Requested array desciptor</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415hipArrayDestroy10hipArray_t">
<span id="_CPPv315hipArrayDestroy10hipArray_t"></span><span id="_CPPv215hipArrayDestroy10hipArray_t"></span><span id="hipArrayDestroy__hipArray_t"></span><span class="target" id="group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipArrayDestroy</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">array</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415hipArrayDestroy10hipArray_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Destroy an array memory pointer on the device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1gad6c25b3106fb47a2a75285ff2bd8cb29"><span class="std std-ref">hipFreeArray</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>array</strong> – <strong>[in]</strong> Pointer to the array memory</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipArray3DCreateP10hipArray_tPK22HIP_ARRAY3D_DESCRIPTOR">
<span id="_CPPv316hipArray3DCreateP10hipArray_tPK22HIP_ARRAY3D_DESCRIPTOR"></span><span id="_CPPv216hipArray3DCreateP10hipArray_tPK22HIP_ARRAY3D_DESCRIPTOR"></span><span id="hipArray3DCreate__hipArray_tP.HIP_ARRAY3D_DESCRIPTORCP"></span><span class="target" id="group___memory_1ga9dc08dfcd1078227106d9a4a3fe77d25"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipArray3DCreate</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">array</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">HIP_ARRAY3D_DESCRIPTOR</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pAllocateArray</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipArray3DCreateP10hipArray_tPK22HIP_ARRAY3D_DESCRIPTOR" title="Link to this definition">#</a><br /></dt>
<dd><p>Create a 3D array memory pointer on the device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga8376a0644463118cd96432365bb470e3"><span class="std std-ref">hipMallocArray</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1gad6c25b3106fb47a2a75285ff2bd8cb29"><span class="std std-ref">hipFreeArray</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>array</strong> – <strong>[out]</strong> Pointer to the 3D array memory </p></li>
<li><p><strong>pAllocateArray</strong> – <strong>[in]</strong> Requested array desciptor</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv411hipMalloc3DP13hipPitchedPtr9hipExtent">
<span id="_CPPv311hipMalloc3DP13hipPitchedPtr9hipExtent"></span><span id="_CPPv211hipMalloc3DP13hipPitchedPtr9hipExtent"></span><span id="hipMalloc3D__hipPitchedPtrP.hipExtent"></span><span class="target" id="group___memory_1gad12f684263bbc92690553af2aa918fd9"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMalloc3D</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipPitchedPtr</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pitchedDevPtr</span></span>, <span class="n"><span class="pre">hipExtent</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">extent</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv411hipMalloc3DP13hipPitchedPtr9hipExtent" title="Link to this definition">#</a><br /></dt>
<dd><p>Create a 3D memory pointer on the device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga805c7320498926e444616fe090c727ee"><span class="std std-ref">hipMallocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, <a class="reference internal" href="#group___memory_1ga740d08da65cae1441ba32f8fedb863d1"><span class="std std-ref">hipFree</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pitchedDevPtr</strong> – <strong>[out]</strong> Pointer to the 3D memory </p></li>
<li><p><strong>extent</strong> – <strong>[in]</strong> Requested extent</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412hipFreeArray10hipArray_t">
<span id="_CPPv312hipFreeArray10hipArray_t"></span><span id="_CPPv212hipFreeArray10hipArray_t"></span><span id="hipFreeArray__hipArray_t"></span><span class="target" id="group___memory_1gad6c25b3106fb47a2a75285ff2bd8cb29"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipFreeArray</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">array</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412hipFreeArray10hipArray_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Frees an array on the device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga4c6fcfe80010069d2792780d00dcead2"><span class="std std-ref">hipMalloc</span></a>, <a class="reference internal" href="#group___memory_1ga805c7320498926e444616fe090c727ee"><span class="std std-ref">hipMallocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga740d08da65cae1441ba32f8fedb863d1"><span class="std std-ref">hipFree</span></a>, <a class="reference internal" href="#group___memory_1ga8376a0644463118cd96432365bb470e3"><span class="std std-ref">hipMallocArray</span></a>, <a class="reference internal" href="#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1"><span class="std std-ref">hipHostMalloc</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga2e543f58ee4544e317cd695d6d82e0a3"><span class="std std-ref">hipHostFree</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>array</strong> – <strong>[in]</strong> Pointer to array to free </p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipMalloc3DArrayP10hipArray_tPK20hipChannelFormatDesc9hipExtentj">
<span id="_CPPv316hipMalloc3DArrayP10hipArray_tPK20hipChannelFormatDesc9hipExtentj"></span><span id="_CPPv216hipMalloc3DArrayP10hipArray_tPK20hipChannelFormatDesc9hipExtentj"></span><span id="hipMalloc3DArray__hipArray_tP.hipChannelFormatDescCP.hipExtent.unsigned-i"></span><span class="target" id="group___memory_1ga3be2acb8c75857958ddd1ab949ed4476"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMalloc3DArray</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">array</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="k"><span class="pre">struct</span></span><span class="w"> </span><span class="n"><span class="pre">hipChannelFormatDesc</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">desc</span></span>, <span class="k"><span class="pre">struct</span></span><span class="w"> </span><span class="n"><span class="pre">hipExtent</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">extent</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipMalloc3DArrayP10hipArray_tPK20hipChannelFormatDesc9hipExtentj" title="Link to this definition">#</a><br /></dt>
<dd><p>Allocate an array on the device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga4c6fcfe80010069d2792780d00dcead2"><span class="std std-ref">hipMalloc</span></a>, <a class="reference internal" href="#group___memory_1ga805c7320498926e444616fe090c727ee"><span class="std std-ref">hipMallocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga740d08da65cae1441ba32f8fedb863d1"><span class="std std-ref">hipFree</span></a>, <a class="reference internal" href="#group___memory_1gad6c25b3106fb47a2a75285ff2bd8cb29"><span class="std std-ref">hipFreeArray</span></a>, <a class="reference internal" href="#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1"><span class="std std-ref">hipHostMalloc</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga2e543f58ee4544e317cd695d6d82e0a3"><span class="std std-ref">hipHostFree</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>array</strong> – <strong>[out]</strong> Pointer to allocated array in device memory </p></li>
<li><p><strong>desc</strong> – <strong>[in]</strong> Requested channel format </p></li>
<li><p><strong>extent</strong> – <strong>[in]</strong> Requested array allocation width, height and depth </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Requested properties of allocated array </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorOutOfMemory</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415hipArrayGetInfoP20hipChannelFormatDescP9hipExtentPj10hipArray_t">
<span id="_CPPv315hipArrayGetInfoP20hipChannelFormatDescP9hipExtentPj10hipArray_t"></span><span id="_CPPv215hipArrayGetInfoP20hipChannelFormatDescP9hipExtentPj10hipArray_t"></span><span id="hipArrayGetInfo__hipChannelFormatDescP.hipExtentP.unsigned-iP.hipArray_t"></span><span class="target" id="group___memory_1ga9f67e594f3d410393b312ade84044597"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipArrayGetInfo</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipChannelFormatDesc</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">desc</span></span>, <span class="n"><span class="pre">hipExtent</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">extent</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">flags</span></span>, <span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">array</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415hipArrayGetInfoP20hipChannelFormatDescP9hipExtentPj10hipArray_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets info about the specified array. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, <a class="reference internal" href="#group___memory_1ga68d59254ab8994d3f61063bb57bf5498"><span class="std std-ref">hipArray3DGetDescriptor</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>desc</strong> – <strong>[out]</strong> - Returned array type </p></li>
<li><p><strong>extent</strong> – <strong>[out]</strong> - Returned array shape. 2D arrays will have depth of zero </p></li>
<li><p><strong>flags</strong> – <strong>[out]</strong> - Returned array flags </p></li>
<li><p><strong>array</strong> – <strong>[in]</strong> - The HIP array to get info for</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue hipErrorInvalidHandle</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipArrayGetDescriptorP20HIP_ARRAY_DESCRIPTOR10hipArray_t">
<span id="_CPPv321hipArrayGetDescriptorP20HIP_ARRAY_DESCRIPTOR10hipArray_t"></span><span id="_CPPv221hipArrayGetDescriptorP20HIP_ARRAY_DESCRIPTOR10hipArray_t"></span><span id="hipArrayGetDescriptor__HIP_ARRAY_DESCRIPTORP.hipArray_t"></span><span class="target" id="group___memory_1ga6e64255c46778f5839711fe730cc7abc"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipArrayGetDescriptor</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">HIP_ARRAY_DESCRIPTOR</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pArrayDescriptor</span></span>, <span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">array</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipArrayGetDescriptorP20HIP_ARRAY_DESCRIPTOR10hipArray_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets a 1D or 2D array descriptor. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga9dc08dfcd1078227106d9a4a3fe77d25"><span class="std std-ref">hipArray3DCreate</span></a>, <a class="reference internal" href="#group___memory_1ga68d59254ab8994d3f61063bb57bf5498"><span class="std std-ref">hipArray3DGetDescriptor</span></a>, <a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga38facb98eb1ae8206376c3c48bf5c444"><span class="std std-ref">hipMemcpy3D</span></a>, <a class="reference internal" href="#group___memory_1ga9c638fd577a3a0b80daffeede136063a"><span class="std std-ref">hipMemcpy3DAsync</span></a>, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gad9b6077f129d2694cda5e8c24b4bed0f"><span class="std std-ref">hipMemcpyHtoD</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer, <a class="reference internal" href="#group___memory_1gad484d4b0a7e178d1d180498625b6122f"><span class="std std-ref">hipMemsetD8</span></a>, <a class="reference internal" href="#group___memory_1ga3ee39cf8737f4a5d0e1e8c9eb870f02f"><span class="std std-ref">hipMemsetD16</span></a>, <a class="reference internal" href="#group___memory_1ga54b16e2fd8d6230c22193ae11b58486b"><span class="std std-ref">hipMemsetD32</span></a>, <a class="reference internal" href="#group___memory_1ga9f67e594f3d410393b312ade84044597"><span class="std std-ref">hipArrayGetInfo</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pArrayDescriptor</strong> – <strong>[out]</strong> - Returned array descriptor </p></li>
<li><p><strong>array</strong> – <strong>[in]</strong> - Array to get descriptor of</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue hipErrorInvalidHandle</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipArray3DGetDescriptorP22HIP_ARRAY3D_DESCRIPTOR10hipArray_t">
<span id="_CPPv323hipArray3DGetDescriptorP22HIP_ARRAY3D_DESCRIPTOR10hipArray_t"></span><span id="_CPPv223hipArray3DGetDescriptorP22HIP_ARRAY3D_DESCRIPTOR10hipArray_t"></span><span id="hipArray3DGetDescriptor__HIP_ARRAY3D_DESCRIPTORP.hipArray_t"></span><span class="target" id="group___memory_1ga68d59254ab8994d3f61063bb57bf5498"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipArray3DGetDescriptor</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">HIP_ARRAY3D_DESCRIPTOR</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pArrayDescriptor</span></span>, <span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">array</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipArray3DGetDescriptorP22HIP_ARRAY3D_DESCRIPTOR10hipArray_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets a 3D array descriptor. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga9dc08dfcd1078227106d9a4a3fe77d25"><span class="std std-ref">hipArray3DCreate</span></a>, <a class="reference internal" href="#group___memory_1ga3befa5c6aee5b18728e2d96ebc1374b8"><span class="std std-ref">hipArrayCreate</span></a>, <a class="reference internal" href="#group___memory_1gafeb20479f2c8bd50f311b0bdc8869b24"><span class="std std-ref">hipArrayDestroy</span></a>, <a class="reference internal" href="#group___memory_1ga6e64255c46778f5839711fe730cc7abc"><span class="std std-ref">hipArrayGetDescriptor</span></a>, hipMemAlloc, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1gaefab023bb8ec9b13a95b5362ab7c62d2"><span class="std std-ref">hipMemAllocHost</span></a>, <a class="reference internal" href="#group___memory_1gad44d400532df8e67a6db45027cd05405"><span class="std std-ref">hipMemAllocPitch</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="#group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"><span class="std std-ref">hipMemcpy2DAsync</span></a>, hipMemcpy2DUnaligned, <a class="reference internal" href="#group___memory_1ga38facb98eb1ae8206376c3c48bf5c444"><span class="std std-ref">hipMemcpy3D</span></a>, <a class="reference internal" href="#group___memory_1ga9c638fd577a3a0b80daffeede136063a"><span class="std std-ref">hipMemcpy3DAsync</span></a>, <a class="reference internal" href="#group___memory_1ga0a714ba192b400688a1ccdd2b3359a9f"><span class="std std-ref">hipMemcpyAtoA</span></a>, <a class="reference internal" href="#group___memory_1ga46d002bcd57e00d01615a118f2b230c3"><span class="std std-ref">hipMemcpyAtoD</span></a>, <a class="reference internal" href="#group___memory_1gabf833a230a7883199514e3fe7face896"><span class="std std-ref">hipMemcpyAtoH</span></a>, <a class="reference internal" href="#group___memory_1ga25614799894ee316c4ce832a57a29741"><span class="std std-ref">hipMemcpyAtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1ga91e920637e005ddec51610ef38b55285"><span class="std std-ref">hipMemcpyDtoA</span></a>, <a class="reference internal" href="#group___memory_1ga814f245b8918f173c1f2f8c1480f7f93"><span class="std std-ref">hipMemcpyDtoD</span></a>, <a class="reference internal" href="#group___memory_1gad3bba6016cba62f0e933cdfb4c312d27"><span class="std std-ref">hipMemcpyDtoDAsync</span></a>, <a class="reference internal" href="#group___memory_1gae61f4e35ff1b9643c6328bc45d091c3f"><span class="std std-ref">hipMemcpyDtoH</span></a>, <a class="reference internal" href="#group___memory_1gad69da1994a646b843fb1fa465dbeb623"><span class="std std-ref">hipMemcpyDtoHAsync</span></a>, <a class="reference internal" href="#group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"><span class="std std-ref">hipMemcpyHtoA</span></a>, <a class="reference internal" href="#group___memory_1ga7458d07076c60e26707ea0522da8e694"><span class="std std-ref">hipMemcpyHtoAAsync</span></a>, <a class="reference internal" href="#group___memory_1gad9b6077f129d2694cda5e8c24b4bed0f"><span class="std std-ref">hipMemcpyHtoD</span></a>, <a class="reference internal" href="#group___memory_1gae6d39bd67777d55d555b24de221206b3"><span class="std std-ref">hipMemcpyHtoDAsync</span></a>, hipMemFree, hipMemFreeHost, <a class="reference internal" href="#group___memory_1gac7d9132f6e3d102e9b512020e5654f38"><span class="std std-ref">hipMemGetAddressRange</span></a>, <a class="reference internal" href="#group___memory_1ga311c3e246a21590de14478b8bd063be2"><span class="std std-ref">hipMemGetInfo</span></a>, hipMemHostAlloc, hipMemHostGetDevicePointer, <a class="reference internal" href="#group___memory_1gad484d4b0a7e178d1d180498625b6122f"><span class="std std-ref">hipMemsetD8</span></a>, <a class="reference internal" href="#group___memory_1ga3ee39cf8737f4a5d0e1e8c9eb870f02f"><span class="std std-ref">hipMemsetD16</span></a>, <a class="reference internal" href="#group___memory_1ga54b16e2fd8d6230c22193ae11b58486b"><span class="std std-ref">hipMemsetD32</span></a>, <a class="reference internal" href="#group___memory_1ga9f67e594f3d410393b312ade84044597"><span class="std std-ref">hipArrayGetInfo</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pArrayDescriptor</strong> – <strong>[out]</strong> - Returned 3D array descriptor </p></li>
<li><p><strong>array</strong> – <strong>[in]</strong> - 3D array to get descriptor of</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidValue hipErrorInvalidHandle, hipErrorContextIsDestroyed</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv411hipMemcpy2DPv6size_tPKv6size_t6size_t6size_t13hipMemcpyKind">
<span id="_CPPv311hipMemcpy2DPv6size_tPKv6size_t6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv211hipMemcpy2DPv6size_tPKv6size_t6size_t6size_t13hipMemcpyKind"></span><span id="hipMemcpy2D__voidP.s.voidCP.s.s.s.hipMemcpyKind"></span><span class="target" id="group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy2D</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dpitch</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">spitch</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv411hipMemcpy2DPv6size_tPKv6size_t6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device. </p>
<p>hipMemcpy2D supports memory matrix copy from the pointed area src to the pointed area dst. The copy direction is defined by kind which must be one of hipMemcpyHostToDevice, hipMemcpyHostToDevice, hipMemcpyDeviceToHost hipMemcpyDeviceToDevice or hipMemcpyDefault. Device to Device copies don’t need to wait for host synchronization. The copy is executed on the default null tream. The src and dst must not overlap. dpitch and spitch are the widths in bytes in memory matrix, width cannot exceed dpitch or spitch.</p>
<p>For hipMemcpy2D, the copy is always performed by the current device (set by hipSetDevice). For multi-gpu or peer-to-peer configurations, it is recommended to set the current device to the device where the src data is physically located. For optimal peer-to-peer copies, the copy device must be able to access the src and dst pointers (by calling hipDeviceEnablePeerAccess with copy agent as the current device and src/dst as the peerDevice argument. if this is not done, the hipMemcpy2D will still work, but will perform the copy using a staging buffer on the host.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga835954048fd6cf0b4de065ada300d8ef"><span class="std std-ref">hipMemcpyToArray</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>Calling hipMemcpy2D with dst and src pointers that do not match the hipMemcpyKind results in undefined behavior.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Destination memory address </p></li>
<li><p><strong>dpitch</strong> – <strong>[in]</strong> Pitch size in bytes of destination memory </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Source memory address </p></li>
<li><p><strong>spitch</strong> – <strong>[in]</strong> Pitch size in bytes of source memory </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width size in bytes of matrix transfer (columns) </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Height size in bytes of matrix transfer (rows) </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> Type of transfer </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipMemcpyParam2DPK12hip_Memcpy2D">
<span id="_CPPv316hipMemcpyParam2DPK12hip_Memcpy2D"></span><span id="_CPPv216hipMemcpyParam2DPK12hip_Memcpy2D"></span><span id="hipMemcpyParam2D__hip_Memcpy2DCP"></span><span class="target" id="group___memory_1gaa6913c5738f524d8fd043ab6f2c0e5ed"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyParam2D</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hip_Memcpy2D</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pCopy</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipMemcpyParam2DPK12hip_Memcpy2D" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies memory for 2D arrays. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga835954048fd6cf0b4de065ada300d8ef"><span class="std std-ref">hipMemcpyToArray</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>pCopy</strong> – <strong>[in]</strong> Parameters for the memory copy </p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipMemcpyParam2DAsyncPK12hip_Memcpy2D11hipStream_t">
<span id="_CPPv321hipMemcpyParam2DAsyncPK12hip_Memcpy2D11hipStream_t"></span><span id="_CPPv221hipMemcpyParam2DAsyncPK12hip_Memcpy2D11hipStream_t"></span><span id="hipMemcpyParam2DAsync__hip_Memcpy2DCP.hipStream_t"></span><span class="target" id="group___memory_1gad0068c52b6f5c2ed758ec2f68db8751b"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyParam2DAsync</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hip_Memcpy2D</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pCopy</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipMemcpyParam2DAsyncPK12hip_Memcpy2D11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies memory for 2D arrays. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga835954048fd6cf0b4de065ada300d8ef"><span class="std std-ref">hipMemcpyToArray</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pCopy</strong> – <strong>[in]</strong> Parameters for the memory copy </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream to use </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipMemcpy2DAsyncPv6size_tPKv6size_t6size_t6size_t13hipMemcpyKind11hipStream_t">
<span id="_CPPv316hipMemcpy2DAsyncPv6size_tPKv6size_t6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span id="_CPPv216hipMemcpy2DAsyncPv6size_tPKv6size_t6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span id="hipMemcpy2DAsync__voidP.s.voidCP.s.s.s.hipMemcpyKind.hipStream_t"></span><span class="target" id="group___memory_1ga6b9eaa58bc332346cb8ed956f8b590ac"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy2DAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dpitch</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">spitch</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipMemcpy2DAsyncPv6size_tPKv6size_t6size_t6size_t13hipMemcpyKind11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device asynchronously. </p>
<p>hipMemcpy2DAsync supports memory matrix copy from the pointed area src to the pointed area dst. The copy direction is defined by kind which must be one of hipMemcpyHostToDevice, hipMemcpyDeviceToHost, hipMemcpyDeviceToDevice or hipMemcpyDefault. dpitch and spitch are the widths in bytes for memory matrix corresponds to dst and src. width cannot exceed dpitch or spitch.</p>
<p>The copy is always performed by the device associated with the specified stream. The API is asynchronous with respect to the host, so the call may return before the copy is complete. The copy can optionally be excuted in a specific stream by passing a non-zero stream argument, for HostToDevice or DeviceToHost copies, the copy can overlap with operations in other streams.</p>
<p>For multi-gpu or peer-to-peer configurations, it is recommended to use a stream which is attached to the device where the src data is physically located.</p>
<p>For optimal peer-to-peer copies, the copy device must be able to access the src and dst pointers (by calling hipDeviceEnablePeerAccess) with copy agent as the current device and src/dst as the peerDevice argument. If enabling device peer access is not done, the API will still work, but will perform the copy using a staging buffer on the host.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga835954048fd6cf0b4de065ada300d8ef"><span class="std std-ref">hipMemcpyToArray</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If host or dst are not pinned, the memory copy will be performed synchronously. For best performance, use hipHostMalloc to allocate host memory that is transferred asynchronously.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Pointer to destination memory address </p></li>
<li><p><strong>dpitch</strong> – <strong>[in]</strong> Pitch size in bytes of destination memory </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Pointer to source memory address </p></li>
<li><p><strong>spitch</strong> – <strong>[in]</strong> Pitch size in bytes of source memory </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width of matrix transfer (columns in bytes) </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Height of matrix transfer (rows) </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> Type of transfer </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream to use </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipMemcpy2DToArray10hipArray_t6size_t6size_tPKv6size_t6size_t6size_t13hipMemcpyKind">
<span id="_CPPv318hipMemcpy2DToArray10hipArray_t6size_t6size_tPKv6size_t6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv218hipMemcpy2DToArray10hipArray_t6size_t6size_tPKv6size_t6size_t6size_t13hipMemcpyKind"></span><span id="hipMemcpy2DToArray__hipArray_t.s.s.voidCP.s.s.s.hipMemcpyKind"></span><span class="target" id="group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy2DToArray</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">wOffset</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hOffset</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">spitch</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipMemcpy2DToArray10hipArray_t6size_t6size_tPKv6size_t6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga835954048fd6cf0b4de065ada300d8ef"><span class="std std-ref">hipMemcpyToArray</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Destination memory address </p></li>
<li><p><strong>wOffset</strong> – <strong>[in]</strong> Destination starting X offset </p></li>
<li><p><strong>hOffset</strong> – <strong>[in]</strong> Destination starting Y offset </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Source memory address </p></li>
<li><p><strong>spitch</strong> – <strong>[in]</strong> Pitch of source memory </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width of matrix transfer (columns in bytes) </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Height of matrix transfer (rows) </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> Type of transfer </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipMemcpy2DToArrayAsync10hipArray_t6size_t6size_tPKv6size_t6size_t6size_t13hipMemcpyKind11hipStream_t">
<span id="_CPPv323hipMemcpy2DToArrayAsync10hipArray_t6size_t6size_tPKv6size_t6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span id="_CPPv223hipMemcpy2DToArrayAsync10hipArray_t6size_t6size_tPKv6size_t6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span id="hipMemcpy2DToArrayAsync__hipArray_t.s.s.voidCP.s.s.s.hipMemcpyKind.hipStream_t"></span><span class="target" id="group___memory_1gab6953ee5f575d0324c19ffc51a72f8fb"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy2DToArrayAsync</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">wOffset</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hOffset</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">spitch</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipMemcpy2DToArrayAsync10hipArray_t6size_t6size_tPKv6size_t6size_t6size_t13hipMemcpyKind11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga835954048fd6cf0b4de065ada300d8ef"><span class="std std-ref">hipMemcpyToArray</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Destination memory address </p></li>
<li><p><strong>wOffset</strong> – <strong>[in]</strong> Destination starting X offset </p></li>
<li><p><strong>hOffset</strong> – <strong>[in]</strong> Destination starting Y offset </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Source memory address </p></li>
<li><p><strong>spitch</strong> – <strong>[in]</strong> Pitch of source memory </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width of matrix transfer (columns in bytes) </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Height of matrix transfer (rows) </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> Type of transfer </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Accelerator view which the copy is being enqueued </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipMemcpy2DArrayToArray10hipArray_t6size_t6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind">
<span id="_CPPv323hipMemcpy2DArrayToArray10hipArray_t6size_t6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv223hipMemcpy2DArrayToArray10hipArray_t6size_t6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind"></span><span id="hipMemcpy2DArrayToArray__hipArray_t.s.s.hipArray_const_t.s.s.s.s.hipMemcpyKind"></span><span class="target" id="group___memory_1ga11a0bead0f40a85a212f8a686b72b243"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy2DArrayToArray</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">wOffsetDst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hOffsetDst</span></span>, <span class="n"><span class="pre">hipArray_const_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">wOffsetSrc</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hOffsetSrc</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipMemcpy2DArrayToArray10hipArray_t6size_t6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga835954048fd6cf0b4de065ada300d8ef"><span class="std std-ref">hipMemcpyToArray</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Destination memory address </p></li>
<li><p><strong>wOffsetDst</strong> – <strong>[in]</strong> Destination starting X offset </p></li>
<li><p><strong>hOffsetDst</strong> – <strong>[in]</strong> Destination starting Y offset </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Source memory address </p></li>
<li><p><strong>wOffsetSrc</strong> – <strong>[in]</strong> Source starting X offset </p></li>
<li><p><strong>hOffsetSrc</strong> – <strong>[in]</strong> Source starting Y offset (columns in bytes) </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width of matrix transfer (columns in bytes) </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Height of matrix transfer (rows) </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> Type of transfer</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hipMemcpy2DFromArrayPv6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind">
<span id="_CPPv320hipMemcpy2DFromArrayPv6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv220hipMemcpy2DFromArrayPv6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind"></span><span id="hipMemcpy2DFromArray__voidP.s.hipArray_const_t.s.s.s.s.hipMemcpyKind"></span><span class="target" id="group___memory_1ga9c5763233c9803b8e964881487fc4e60"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy2DFromArray</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dpitch</span></span>, <span class="n"><span class="pre">hipArray_const_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">wOffset</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hOffset</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hipMemcpy2DFromArrayPv6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Destination memory address </p></li>
<li><p><strong>dpitch</strong> – <strong>[in]</strong> Pitch of destination memory </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Source memory address </p></li>
<li><p><strong>wOffset</strong> – <strong>[in]</strong> Source starting X offset </p></li>
<li><p><strong>hOffset</strong> – <strong>[in]</strong> Source starting Y offset </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width of matrix transfer (columns in bytes) </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Height of matrix transfer (rows) </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> Type of transfer </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425hipMemcpy2DFromArrayAsyncPv6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind11hipStream_t">
<span id="_CPPv325hipMemcpy2DFromArrayAsyncPv6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span id="_CPPv225hipMemcpy2DFromArrayAsyncPv6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span id="hipMemcpy2DFromArrayAsync__voidP.s.hipArray_const_t.s.s.s.s.hipMemcpyKind.hipStream_t"></span><span class="target" id="group___memory_1ga946fe29e78ce1580cb95fa2210389263"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy2DFromArrayAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dpitch</span></span>, <span class="n"><span class="pre">hipArray_const_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">wOffset</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hOffset</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425hipMemcpy2DFromArrayAsyncPv6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device asynchronously. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Destination memory address </p></li>
<li><p><strong>dpitch</strong> – <strong>[in]</strong> Pitch of destination memory </p></li>
<li><p><strong>src</strong> – <strong>[in]</strong> Source memory address </p></li>
<li><p><strong>wOffset</strong> – <strong>[in]</strong> Source starting X offset </p></li>
<li><p><strong>hOffset</strong> – <strong>[in]</strong> Source starting Y offset </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width of matrix transfer (columns in bytes) </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Height of matrix transfer (rows) </p></li>
<li><p><strong>kind</strong> – <strong>[in]</strong> Type of transfer </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Accelerator view which the copy is being enqueued </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipMemcpyAtoHPv10hipArray_t6size_t6size_t">
<span id="_CPPv313hipMemcpyAtoHPv10hipArray_t6size_t6size_t"></span><span id="_CPPv213hipMemcpyAtoHPv10hipArray_t6size_t6size_t"></span><span id="hipMemcpyAtoH__voidP.hipArray_t.s.s"></span><span class="target" id="group___memory_1gabf833a230a7883199514e3fe7face896"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyAtoH</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">srcArray</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">srcOffset</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipMemcpyAtoHPv10hipArray_t6size_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dst</strong> – <strong>[in]</strong> Destination memory address </p></li>
<li><p><strong>srcArray</strong> – <strong>[in]</strong> Source array </p></li>
<li><p><strong>srcOffset</strong> – <strong>[in]</strong> Offset in bytes of source array </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> Size of memory copy in bytes </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipMemcpyHtoA10hipArray_t6size_tPKv6size_t">
<span id="_CPPv313hipMemcpyHtoA10hipArray_t6size_tPKv6size_t"></span><span id="_CPPv213hipMemcpyHtoA10hipArray_t6size_tPKv6size_t"></span><span id="hipMemcpyHtoA__hipArray_t.s.voidCP.s"></span><span class="target" id="group___memory_1gaaa6b5a61fa58239bb36344b219ed7e2c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyHtoA</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstArray</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dstOffset</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">srcHost</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipMemcpyHtoA10hipArray_t6size_tPKv6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dstArray</strong> – <strong>[in]</strong> Destination memory address </p></li>
<li><p><strong>dstOffset</strong> – <strong>[in]</strong> Offset in bytes of destination array </p></li>
<li><p><strong>srcHost</strong> – <strong>[in]</strong> Source host pointer </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> Size of memory copy in bytes </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv411hipMemcpy3DPK16hipMemcpy3DParms">
<span id="_CPPv311hipMemcpy3DPK16hipMemcpy3DParms"></span><span id="_CPPv211hipMemcpy3DPK16hipMemcpy3DParms"></span><span id="hipMemcpy3D__hipMemcpy3DParmsCP"></span><span class="target" id="group___memory_1ga38facb98eb1ae8206376c3c48bf5c444"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy3D</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="k"><span class="pre">struct</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemcpy3DParms</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">p</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv411hipMemcpy3DPK16hipMemcpy3DParms" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>p</strong> – <strong>[in]</strong> 3D memory copy parameters </p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipMemcpy3DAsyncPK16hipMemcpy3DParms11hipStream_t">
<span id="_CPPv316hipMemcpy3DAsyncPK16hipMemcpy3DParms11hipStream_t"></span><span id="_CPPv216hipMemcpy3DAsyncPK16hipMemcpy3DParms11hipStream_t"></span><span id="hipMemcpy3DAsync__hipMemcpy3DParmsCP.hipStream_t"></span><span class="target" id="group___memory_1ga9c638fd577a3a0b80daffeede136063a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy3DAsync</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="k"><span class="pre">struct</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemcpy3DParms</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">p</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipMemcpy3DAsyncPK16hipMemcpy3DParms11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device asynchronously. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>p</strong> – <strong>[in]</strong> 3D memory copy parameters </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream to use </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipDrvMemcpy3DPK12HIP_MEMCPY3D">
<span id="_CPPv314hipDrvMemcpy3DPK12HIP_MEMCPY3D"></span><span id="_CPPv214hipDrvMemcpy3DPK12HIP_MEMCPY3D"></span><span id="hipDrvMemcpy3D__HIP_MEMCPY3DCP"></span><span class="target" id="group___memory_1gaa385d7b1d0f0d941224abd9549ea9494"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDrvMemcpy3D</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">HIP_MEMCPY3D</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pCopy</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipDrvMemcpy3DPK12HIP_MEMCPY3D" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>pCopy</strong> – <strong>[in]</strong> 3D memory copy parameters </p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipDrvMemcpy3DAsyncPK12HIP_MEMCPY3D11hipStream_t">
<span id="_CPPv319hipDrvMemcpy3DAsyncPK12HIP_MEMCPY3D11hipStream_t"></span><span id="_CPPv219hipDrvMemcpy3DAsyncPK12HIP_MEMCPY3D11hipStream_t"></span><span id="hipDrvMemcpy3DAsync__HIP_MEMCPY3DCP.hipStream_t"></span><span class="target" id="group___memory_1ga6141790316fdb3c85ce34cf94c721c20"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipDrvMemcpy3DAsync</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">HIP_MEMCPY3D</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pCopy</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipDrvMemcpy3DAsyncPK12HIP_MEMCPY3D11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data between host and device asynchronously. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac1a055d288302edd641c6d7416858e1e"><span class="std std-ref">hipMemcpy</span></a>, <a class="reference internal" href="#group___memory_1gaccf359cb35ce1887e6250c09e115e9a2"><span class="std std-ref">hipMemcpy2DToArray</span></a>, <a class="reference internal" href="#group___memory_1ga8af4597ff0cd17247d8a857c4d8bfa8a"><span class="std std-ref">hipMemcpy2D</span></a>, <a class="reference internal" href="memory_management/memory_management_deprecated.html#group___memory_d_1ga8c39c67c4ba098c6e6e116a9a4839a24"><span class="std std-ref">hipMemcpyFromArray</span></a>, <a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a>, <a class="reference internal" href="#group___memory_1gad55fa9f5980b711bc93c52820149ba18"><span class="std std-ref">hipMemcpyAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pCopy</strong> – <strong>[in]</strong> 3D memory copy parameters </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream to use </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidPitchValue, hipErrorInvalidDevicePointer, hipErrorInvalidMemcpyDirection</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipMemGetAddressRangeP14hipDeviceptr_tP6size_t14hipDeviceptr_t">
<span id="_CPPv321hipMemGetAddressRangeP14hipDeviceptr_tP6size_t14hipDeviceptr_t"></span><span id="_CPPv221hipMemGetAddressRangeP14hipDeviceptr_tP6size_t14hipDeviceptr_t"></span><span id="hipMemGetAddressRange__hipDeviceptr_tP.sP.hipDeviceptr_t"></span><span class="target" id="group___memory_1gac7d9132f6e3d102e9b512020e5654f38"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemGetAddressRange</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pbase</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">psize</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dptr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipMemGetAddressRangeP14hipDeviceptr_tP6size_t14hipDeviceptr_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Get information on memory allocations. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="context_management.html#group___context_1gab6dbcff5c5b1249a5ac5cf39ae9d08bc"><span class="std std-ref">hipCtxCreate</span></a>, <a class="reference internal" href="context_management.html#group___context_1ga9a65fe43238ef303a6d97826c05fd14e"><span class="std std-ref">hipCtxDestroy</span></a>, <a class="reference internal" href="context_management.html#group___context_1ga12a7a993e10f775fbf61a0b14288ed1b"><span class="std std-ref">hipCtxGetFlags</span></a>, <a class="reference internal" href="context_management.html#group___context_1ga2cc4ea5a6b78d9d7990a88a7863467d4"><span class="std std-ref">hipCtxPopCurrent</span></a>, <a class="reference internal" href="context_management.html#group___context_1ga741786101d348fdbfa1f64546860357a"><span class="std std-ref">hipCtxGetCurrent</span></a>, <a class="reference internal" href="context_management.html#group___context_1ga834a192f70c2bfc0269c309436776feb"><span class="std std-ref">hipCtxSetCurrent</span></a>, <a class="reference internal" href="context_management.html#group___context_1ga9c9d92f29d68cacdea4c062c97e50a8a"><span class="std std-ref">hipCtxPushCurrent</span></a>, <a class="reference internal" href="context_management.html#group___context_1ga7eacc656f1d1b6f5a683bea31be67a2f"><span class="std std-ref">hipCtxSetCacheConfig</span></a>, <a class="reference internal" href="context_management.html#group___context_1gad45cd968e8e3dcfd24ef050cab2f41c8"><span class="std std-ref">hipCtxSynchronize</span></a>, <a class="reference internal" href="context_management.html#group___context_1ga8aa32cf64272da929f23ecbafefefcee"><span class="std std-ref">hipCtxGetDevice</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pbase</strong> – <strong>[out]</strong> - BAse pointer address </p></li>
<li><p><strong>psize</strong> – <strong>[out]</strong> - Size of allocation </p></li>
<li><p><strong>dptr-</strong> – <strong>[in]</strong> Device Pointer</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorNotFound</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipMemcpyBatchAsyncPPvPPvP6size_t6size_tP19hipMemcpyAttributesP6size_t6size_tP6size_t11hipStream_t">
<span id="_CPPv319hipMemcpyBatchAsyncPPvPPvP6size_t6size_tP19hipMemcpyAttributesP6size_t6size_tP6size_t11hipStream_t"></span><span id="_CPPv219hipMemcpyBatchAsyncPPvPPvP6size_t6size_tP19hipMemcpyAttributesP6size_t6size_tP6size_t11hipStream_t"></span><span id="hipMemcpyBatchAsync__voidPP.voidPP.sP.s.hipMemcpyAttributesP.sP.s.sP.hipStream_t"></span><span class="target" id="group___memory_1gabd45a88bbd984d686e677d922072f619"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyBatchAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dsts</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">srcs</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">sizes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">hipMemcpyAttributes</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">attrs</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">attrsIdxs</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numAttrs</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">failIdx</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipMemcpyBatchAsyncPPvPPvP6size_t6size_tP19hipMemcpyAttributesP6size_t6size_tP6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Perform Batch of 1D copies. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dsts</strong> – <strong>[in]</strong> - Array of destination pointers </p></li>
<li><p><strong>srcs</strong> – <strong>[in]</strong> - Array of source pointers. </p></li>
<li><p><strong>sizes</strong> – <strong>[in]</strong> - Array of sizes for memcpy operations </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> - Size of dsts, srcs and sizes arrays </p></li>
<li><p><strong>attrs</strong> – <strong>[in]</strong> - Array of memcpy attributes (not supported) </p></li>
<li><p><strong>attrsIdxs</strong> – <strong>[in]</strong> - Array of indices to map attrs to copies (not supported) </p></li>
<li><p><strong>numAttrs</strong> – <strong>[in]</strong> - Size of attrs and attrsIdxs arrays (not supported) </p></li>
<li><p><strong>failIdx</strong> – <strong>[in]</strong> - Pointer to a location to return failure index inside the batch </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> - stream used to enqueue operations in.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipMemcpy3DBatchAsync6size_tP18hipMemcpy3DBatchOpP6size_ty11hipStream_t">
<span id="_CPPv321hipMemcpy3DBatchAsync6size_tP18hipMemcpy3DBatchOpP6size_ty11hipStream_t"></span><span id="_CPPv221hipMemcpy3DBatchAsync6size_tP18hipMemcpy3DBatchOpP6size_ty11hipStream_t"></span><span id="hipMemcpy3DBatchAsync__s.hipMemcpy3DBatchOpP.sP.unsigned-l-l.hipStream_t"></span><span class="target" id="group___memory_1ga0e387e19da9b076424123fcbd4070fb2"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy3DBatchAsync</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numOps</span></span>, <span class="k"><span class="pre">struct</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemcpy3DBatchOp</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">opList</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">failIdx</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipMemcpy3DBatchAsync6size_tP18hipMemcpy3DBatchOpP6size_ty11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Perform Batch of 3D copies. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>numOps</strong> – <strong>[in]</strong> - Total number of memcpy operations. </p></li>
<li><p><strong>opList</strong> – <strong>[in]</strong> - Array of size numOps containing the actual memcpy operations. </p></li>
<li><p><strong>failIdx</strong> – <strong>[in]</strong> - Pointer to a location to return the index of the copy where a failure<ul>
<li><p>was encountered. </p></li>
</ul>
</p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> - Flags for future use, must be zero now. </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> - The stream to enqueue the operations in.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415hipMemcpy3DPeerP20hipMemcpy3DPeerParms">
<span id="_CPPv315hipMemcpy3DPeerP20hipMemcpy3DPeerParms"></span><span id="_CPPv215hipMemcpy3DPeerP20hipMemcpy3DPeerParms"></span><span id="hipMemcpy3DPeer__hipMemcpy3DPeerParmsP"></span><span class="target" id="group___memory_1ga80d9b368037c9e80b4d5a6704580f652"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy3DPeer</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipMemcpy3DPeerParms</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">p</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415hipMemcpy3DPeerP20hipMemcpy3DPeerParms" title="Link to this definition">#</a><br /></dt>
<dd><p>Performs 3D memory copies between devices This API is asynchronous with respect to host. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>p</strong> – <strong>[in]</strong> - Parameters for memory copy</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidDevice </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hipMemcpy3DPeerAsyncP20hipMemcpy3DPeerParms11hipStream_t">
<span id="_CPPv320hipMemcpy3DPeerAsyncP20hipMemcpy3DPeerParms11hipStream_t"></span><span id="_CPPv220hipMemcpy3DPeerAsyncP20hipMemcpy3DPeerParms11hipStream_t"></span><span id="hipMemcpy3DPeerAsync__hipMemcpy3DPeerParmsP.hipStream_t"></span><span class="target" id="group___memory_1gaf51d7f03f7945454ea5d15ac7c7ca402"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpy3DPeerAsync</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipMemcpy3DPeerParms</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">p</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hipMemcpy3DPeerAsyncP20hipMemcpy3DPeerParms11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Performs 3D memory copies between devices asynchronously. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>p</strong> – <strong>[in]</strong> - Parameters for memory copy </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> - Stream to enqueue operation in.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidDevice </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E19hipGetSymbolAddress10hipError_tPPvRK1T">
<span id="_CPPv3I0E19hipGetSymbolAddressPPvRK1T"></span><span id="_CPPv2I0E19hipGetSymbolAddressPPvRK1T"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">typename</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___memory_1ga4cbd54bd4fae852ab09b253d5ad1efa5"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGetSymbolAddress</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">devPtr</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv4I0E19hipGetSymbolAddress10hipError_tPPvRK1T" title="hipGetSymbolAddress::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">symbol</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E19hipGetSymbolAddress10hipError_tPPvRK1T" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the address of a symbol. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>devPtr</strong> – <strong>[out]</strong> - Returns device pointer associated with symbol. </p></li>
<li><p><strong>symbol</strong> – <strong>[in]</strong> - Device symbol.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E16hipGetSymbolSize10hipError_tP6size_tRK1T">
<span id="_CPPv3I0E16hipGetSymbolSizeP6size_tRK1T"></span><span id="_CPPv2I0E16hipGetSymbolSizeP6size_tRK1T"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">typename</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___memory_1gaffeda0524b62974431ad5e4ef1bed534"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGetSymbolSize</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">size</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv4I0E16hipGetSymbolSize10hipError_tP6size_tRK1T" title="hipGetSymbolSize::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">symbol</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E16hipGetSymbolSize10hipError_tP6size_tRK1T" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the size of a symbol. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>size</strong> – <strong>[out]</strong> - Returns the size of a symbol. </p></li>
<li><p><strong>symbol</strong> – <strong>[in]</strong> - Device symbol address.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E17hipMemcpyToSymbol10hipError_tRK1TPKv6size_t6size_t13hipMemcpyKind">
<span id="_CPPv3I0E17hipMemcpyToSymbolRK1TPKv6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv2I0E17hipMemcpyToSymbolRK1TPKv6size_t6size_t13hipMemcpyKind"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">typename</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___memory_1gafbc947cdd26a84f521e071647f74a32e"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyToSymbol</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv4I0E17hipMemcpyToSymbol10hipError_tRK1TPKv6size_t6size_t13hipMemcpyKind" title="hipMemcpyToSymbol::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E17hipMemcpyToSymbol10hipError_tRK1TPKv6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data to the given symbol on the device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gac0d988981c8535af1712f1f57436869b"><span class="std std-ref">hipMemcpyToSymbol</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>hipSuccess, hipErrorInvalidMemcpyDirection, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E22hipMemcpyToSymbolAsync10hipError_tRK1TPKv6size_t6size_t13hipMemcpyKind11hipStream_t">
<span id="_CPPv3I0E22hipMemcpyToSymbolAsyncRK1TPKv6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span id="_CPPv2I0E22hipMemcpyToSymbolAsyncRK1TPKv6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">typename</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___memory_1ga0aa5122b72f11142b40c36152e8b484c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyToSymbolAsync</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv4I0E22hipMemcpyToSymbolAsync10hipError_tRK1TPKv6size_t6size_t13hipMemcpyKind11hipStream_t" title="hipMemcpyToSymbolAsync::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">src</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E22hipMemcpyToSymbolAsync10hipError_tRK1TPKv6size_t6size_t13hipMemcpyKind11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data to the given symbol on the device asynchronously on the stream. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gaaceb6e89fb822d3a8e387b526b718478"><span class="std std-ref">hipMemcpyToSymbolAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>hipSuccess, hipErrorInvalidMemcpyDirection, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E19hipMemcpyFromSymbol10hipError_tPvRK1T6size_t6size_t13hipMemcpyKind">
<span id="_CPPv3I0E19hipMemcpyFromSymbolPvRK1T6size_t6size_t13hipMemcpyKind"></span><span id="_CPPv2I0E19hipMemcpyFromSymbolPvRK1T6size_t6size_t13hipMemcpyKind"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">typename</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___memory_1ga70a4f961f82146aa297b121dc0be570d"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyFromSymbol</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv4I0E19hipMemcpyFromSymbol10hipError_tPvRK1T6size_t6size_t13hipMemcpyKind" title="hipMemcpyFromSymbol::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E19hipMemcpyFromSymbol10hipError_tPvRK1T6size_t6size_t13hipMemcpyKind" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data from the given symbol on the device. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga5e06c171bb33ac109bf9e642bea57314"><span class="std std-ref">hipMemcpyFromSymbol</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>hipSuccess, hipErrorInvalidMemcpyDirection, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E24hipMemcpyFromSymbolAsync10hipError_tPvRK1T6size_t6size_t13hipMemcpyKind11hipStream_t">
<span id="_CPPv3I0E24hipMemcpyFromSymbolAsyncPvRK1T6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span id="_CPPv2I0E24hipMemcpyFromSymbolAsyncPvRK1T6size_t6size_t13hipMemcpyKind11hipStream_t"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">typename</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___memory_1gaf9db17bdee8354dad2e973cb1ebafdf6"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemcpyFromSymbolAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dst</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv4I0E24hipMemcpyFromSymbolAsync10hipError_tPvRK1T6size_t6size_t13hipMemcpyKind11hipStream_t" title="hipMemcpyFromSymbolAsync::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sizeBytes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="n"><span class="pre">hipMemcpyKind</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kind</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E24hipMemcpyFromSymbolAsync10hipError_tPvRK1T6size_t6size_t13hipMemcpyKind11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Copies data from the given symbol on the device asynchronously on the stream. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga50a9366e07b89172e140203a744a80c5"><span class="std std-ref">hipMemcpyFromSymbolAsync</span></a></p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>hipSuccess, hipErrorInvalidMemcpyDirection, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E9hipMalloc10hipError_tPP1T6size_t">
<span id="_CPPv3I0E9hipMallocPP1T6size_t"></span><span id="_CPPv2I0E9hipMallocPP1T6size_t"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___memory_1ga5a399f019a2951241ff58ea69dd64c8a"></span><span class="k"><span class="pre">static</span></span><span class="w"> </span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMalloc</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E9hipMalloc10hipError_tPP1T6size_t" title="hipMalloc::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">devPtr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E9hipMalloc10hipError_tPP1T6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>: C++ wrapper for hipMalloc</p>
<p>Perform automatic type conversion to eliminate the need for excessive typecasting (ie void**) </p>
<p><strong>HIP_DISABLE_CPP_FUNCTIONS</strong> macro can be defined to suppress these wrappers. It is useful for applications which need to obtain decltypes of HIP runtime APIs.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga4c6fcfe80010069d2792780d00dcead2"><span class="std std-ref">hipMalloc</span></a></p>
</div>
</p>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E14hipMallocPitch10hipError_tPP1TP6size_t6size_t6size_t">
<span id="_CPPv3I0E14hipMallocPitchPP1TP6size_t6size_t6size_t"></span><span id="_CPPv2I0E14hipMallocPitchPP1TP6size_t6size_t6size_t"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___memory_1ga164e50fe14aec73710f248333be521b6"></span><span class="k"><span class="pre">static</span></span><span class="w"> </span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMallocPitch</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E14hipMallocPitch10hipError_tPP1TP6size_t6size_t6size_t" title="hipMallocPitch::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">devPtr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pitch</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E14hipMallocPitch10hipError_tPP1TP6size_t6size_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>: C++ wrapper for hipMallocPitch</p>
<p>Perform automatic type conversion to eliminate the need for excessive typecasting (ie void**) </p>
<p><strong>HIP_DISABLE_CPP_FUNCTIONS</strong> macro can be defined to suppress these wrappers. It is useful for applications which need to obtain decltypes of HIP runtime APIs.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga805c7320498926e444616fe090c727ee"><span class="std std-ref">hipMallocPitch</span></a></p>
</div>
</p>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E13hipHostMalloc10hipError_tPP1T6size_tj">
<span id="_CPPv3I0E13hipHostMallocPP1T6size_tj"></span><span id="_CPPv2I0E13hipHostMallocPP1T6size_tj"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___memory_1ga402d2f8293c5eed65e4d6a8d960f2e9b"></span><span class="k"><span class="pre">static</span></span><span class="w"> </span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipHostMalloc</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E13hipHostMalloc10hipError_tPP1T6size_tj" title="hipHostMalloc::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="n"><span class="pre">hipHostMallocDefault</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E13hipHostMalloc10hipError_tPP1T6size_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>: C++ wrapper for hipHostMalloc</p>
<p>Provide an override to automatically typecast the pointer type from void**, and also provide a default for the flags. </p>
<p><strong>HIP_DISABLE_CPP_FUNCTIONS</strong> macro can be defined to suppress these wrappers. It is useful for applications which need to obtain decltypes of HIP runtime APIs.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1gaad40bc7d97ccc799403ef5a9a8c246e1"><span class="std std-ref">hipHostMalloc</span></a></p>
</div>
</p>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E12hipHostAlloc10hipError_tPP1T6size_tj">
<span id="_CPPv3I0E12hipHostAllocPP1T6size_tj"></span><span id="_CPPv2I0E12hipHostAllocPP1T6size_tj"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___memory_1ga61c8bed28e3f58956e52e3f39010a504"></span><span class="k"><span class="pre">static</span></span><span class="w"> </span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipHostAlloc</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E12hipHostAlloc10hipError_tPP1T6size_tj" title="hipHostAlloc::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="n"><span class="pre">hipHostAllocDefault</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E12hipHostAlloc10hipError_tPP1T6size_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>: C++ wrapper for hipHostAlloc</p>
<p>Provide an override to automatically typecast the pointer type from void**, and also provide a default for the flags. </p>
<p><strong>HIP_DISABLE_CPP_FUNCTIONS</strong> macro can be defined to suppress these wrappers. It is useful for applications which need to obtain decltypes of HIP runtime APIs.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_1ga0e35f3397f6ea9c3f47a17461ae01231"><span class="std std-ref">hipHostAlloc</span></a></p>
</div>
</p>
</dd></dl>

<div class="toctree-wrapper compound">
</div>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="event_management.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Event management</p>
      </div>
    </a>
    <a class="right-next"
       href="memory_management/memory_management_deprecated.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Memory management (deprecated)</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipPointerSetAttributePKv20hipPointer_attribute14hipDeviceptr_t"><code class="docutils literal notranslate"><span class="pre">hipPointerSetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipPointerGetAttributesP21hipPointerAttribute_tPKv"><code class="docutils literal notranslate"><span class="pre">hipPointerGetAttributes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipPointerGetAttributePv20hipPointer_attribute14hipDeviceptr_t"><code class="docutils literal notranslate"><span class="pre">hipPointerGetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipDrvPointerGetAttributesjP20hipPointer_attributePPv14hipDeviceptr_t"><code class="docutils literal notranslate"><span class="pre">hipDrvPointerGetAttributes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49hipMallocPPv6size_t"><code class="docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipExtMallocWithFlagsPPv6size_tj"><code class="docutils literal notranslate"><span class="pre">hipExtMallocWithFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipHostMallocPPv6size_tj"><code class="docutils literal notranslate"><span class="pre">hipHostMalloc()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipHostAllocPPv6size_tj"><code class="docutils literal notranslate"><span class="pre">hipHostAlloc()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipHostGetDevicePointerPPvPvj"><code class="docutils literal notranslate"><span class="pre">hipHostGetDevicePointer()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipHostGetFlagsPjPv"><code class="docutils literal notranslate"><span class="pre">hipHostGetFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipHostRegisterPv6size_tj"><code class="docutils literal notranslate"><span class="pre">hipHostRegister()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipHostUnregisterPv"><code class="docutils literal notranslate"><span class="pre">hipHostUnregister()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMallocPitchPPvP6size_t6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMallocPitch()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemAllocPitchP14hipDeviceptr_tP6size_t6size_t6size_tj"><code class="docutils literal notranslate"><span class="pre">hipMemAllocPitch()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv47hipFreePv"><code class="docutils literal notranslate"><span class="pre">hipFree()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipFreeHostPv"><code class="docutils literal notranslate"><span class="pre">hipFreeHost()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemcpyWithStreamPvPKv6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyWithStream()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyHtoD14hipDeviceptr_tPKv6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyHtoD()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyDtoHPv14hipDeviceptr_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyDtoH()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyDtoD14hipDeviceptr_t14hipDeviceptr_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyDtoD()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyAtoD14hipDeviceptr_t10hipArray_t6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyAtoD()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyDtoA10hipArray_t6size_t14hipDeviceptr_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyDtoA()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyAtoA10hipArray_t6size_t10hipArray_t6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyAtoA()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemcpyHtoDAsync14hipDeviceptr_tPKv6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyHtoDAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemcpyDtoHAsyncPv14hipDeviceptr_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyDtoHAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemcpyDtoDAsync14hipDeviceptr_t14hipDeviceptr_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyDtoDAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemcpyAtoHAsyncPv10hipArray_t6size_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyAtoHAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemcpyHtoAAsync10hipArray_t6size_tPKv6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyHtoAAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipGetSymbolAddressPPvPKv"><code class="docutils literal notranslate"><span class="pre">hipGetSymbolAddress()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipGetSymbolSizeP6size_tPKv"><code class="docutils literal notranslate"><span class="pre">hipGetSymbolSize()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipGetProcAddressPKcPPvi8uint64_tP31hipDriverProcAddressQueryResult"><code class="docutils literal notranslate"><span class="pre">hipGetProcAddress()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipMemcpyToSymbolPKvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpyToSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipMemcpyToSymbolAsyncPKvPKv6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyToSymbolAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemcpyFromSymbolPvPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpyFromSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipMemcpyFromSymbolAsyncPvPKv6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyFromSymbolAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMemcpyAsyncPvPKv6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49hipMemsetPvi6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemset()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipMemsetD814hipDeviceptr_th6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD8()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemsetD8Async14hipDeviceptr_th6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD8Async()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipMemsetD1614hipDeviceptr_tt6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD16()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipMemsetD16Async14hipDeviceptr_tt6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD16Async()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipMemsetD3214hipDeviceptr_ti6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD32()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMemsetAsyncPvi6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipMemsetD32Async14hipDeviceptr_ti6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD32Async()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipMemset2DPv6size_ti6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemset2D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemset2DAsyncPv6size_ti6size_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemset2DAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipMemset3D13hipPitchedPtri9hipExtent"><code class="docutils literal notranslate"><span class="pre">hipMemset3D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemset3DAsync13hipPitchedPtri9hipExtent11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemset3DAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemsetD2D814hipDeviceptr_t6size_th6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD2D8()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemsetD2D8Async14hipDeviceptr_t6size_th6size_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD2D8Async()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMemsetD2D1614hipDeviceptr_t6size_tt6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD2D16()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemsetD2D16Async14hipDeviceptr_t6size_tt6size_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD2D16Async()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMemsetD2D3214hipDeviceptr_t6size_tj6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD2D32()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemsetD2D32Async14hipDeviceptr_t6size_tj6size_t6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemsetD2D32Async()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemGetInfoP6size_tP6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemGetInfo()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemPtrGetInfoPvP6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemPtrGetInfo()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMallocArrayP10hipArray_tPK20hipChannelFormatDesc6size_t6size_tj"><code class="docutils literal notranslate"><span class="pre">hipMallocArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipArrayCreateP10hipArray_tPK20HIP_ARRAY_DESCRIPTOR"><code class="docutils literal notranslate"><span class="pre">hipArrayCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipArrayDestroy10hipArray_t"><code class="docutils literal notranslate"><span class="pre">hipArrayDestroy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipArray3DCreateP10hipArray_tPK22HIP_ARRAY3D_DESCRIPTOR"><code class="docutils literal notranslate"><span class="pre">hipArray3DCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipMalloc3DP13hipPitchedPtr9hipExtent"><code class="docutils literal notranslate"><span class="pre">hipMalloc3D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipFreeArray10hipArray_t"><code class="docutils literal notranslate"><span class="pre">hipFreeArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMalloc3DArrayP10hipArray_tPK20hipChannelFormatDesc9hipExtentj"><code class="docutils literal notranslate"><span class="pre">hipMalloc3DArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipArrayGetInfoP20hipChannelFormatDescP9hipExtentPj10hipArray_t"><code class="docutils literal notranslate"><span class="pre">hipArrayGetInfo()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipArrayGetDescriptorP20HIP_ARRAY_DESCRIPTOR10hipArray_t"><code class="docutils literal notranslate"><span class="pre">hipArrayGetDescriptor()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipArray3DGetDescriptorP22HIP_ARRAY3D_DESCRIPTOR10hipArray_t"><code class="docutils literal notranslate"><span class="pre">hipArray3DGetDescriptor()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipMemcpy2DPv6size_tPKv6size_t6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemcpyParam2DPK12hip_Memcpy2D"><code class="docutils literal notranslate"><span class="pre">hipMemcpyParam2D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipMemcpyParam2DAsyncPK12hip_Memcpy2D11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyParam2DAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemcpy2DAsyncPv6size_tPKv6size_t6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2DAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipMemcpy2DToArray10hipArray_t6size_t6size_tPKv6size_t6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2DToArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipMemcpy2DToArrayAsync10hipArray_t6size_t6size_tPKv6size_t6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2DToArrayAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipMemcpy2DArrayToArray10hipArray_t6size_t6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2DArrayToArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipMemcpy2DFromArrayPv6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2DFromArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipMemcpy2DFromArrayAsyncPv6size_t16hipArray_const_t6size_t6size_t6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpy2DFromArrayAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyAtoHPv10hipArray_t6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyAtoH()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipMemcpyHtoA10hipArray_t6size_tPKv6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyHtoA()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv411hipMemcpy3DPK16hipMemcpy3DParms"><code class="docutils literal notranslate"><span class="pre">hipMemcpy3D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemcpy3DAsyncPK16hipMemcpy3DParms11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpy3DAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipDrvMemcpy3DPK12HIP_MEMCPY3D"><code class="docutils literal notranslate"><span class="pre">hipDrvMemcpy3D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipDrvMemcpy3DAsyncPK12HIP_MEMCPY3D11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipDrvMemcpy3DAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipMemGetAddressRangeP14hipDeviceptr_tP6size_t14hipDeviceptr_t"><code class="docutils literal notranslate"><span class="pre">hipMemGetAddressRange()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemcpyBatchAsyncPPvPPvP6size_t6size_tP19hipMemcpyAttributesP6size_t6size_tP6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyBatchAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipMemcpy3DBatchAsync6size_tP18hipMemcpy3DBatchOpP6size_ty11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpy3DBatchAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipMemcpy3DPeerP20hipMemcpy3DPeerParms"><code class="docutils literal notranslate"><span class="pre">hipMemcpy3DPeer()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipMemcpy3DPeerAsyncP20hipMemcpy3DPeerParms11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpy3DPeerAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E19hipGetSymbolAddress10hipError_tPPvRK1T"><code class="docutils literal notranslate"><span class="pre">hipGetSymbolAddress()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E16hipGetSymbolSize10hipError_tP6size_tRK1T"><code class="docutils literal notranslate"><span class="pre">hipGetSymbolSize()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E17hipMemcpyToSymbol10hipError_tRK1TPKv6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpyToSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E22hipMemcpyToSymbolAsync10hipError_tRK1TPKv6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyToSymbolAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E19hipMemcpyFromSymbol10hipError_tPvRK1T6size_t6size_t13hipMemcpyKind"><code class="docutils literal notranslate"><span class="pre">hipMemcpyFromSymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E24hipMemcpyFromSymbolAsync10hipError_tPvRK1T6size_t6size_t13hipMemcpyKind11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemcpyFromSymbolAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E9hipMalloc10hipError_tPP1T6size_t"><code class="docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E14hipMallocPitch10hipError_tPP1TP6size_t6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMallocPitch()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E13hipHostMalloc10hipError_tPP1T6size_tj"><code class="docutils literal notranslate"><span class="pre">hipHostMalloc()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E12hipHostAlloc10hipError_tPP1T6size_tj"><code class="docutils literal notranslate"><span class="pre">hipHostAlloc()</span></code></a></li>
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
