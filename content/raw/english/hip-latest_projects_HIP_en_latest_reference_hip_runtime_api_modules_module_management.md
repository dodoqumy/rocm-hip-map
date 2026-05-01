---
title: "Module management &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/module_management.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:07:23.080200+00:00
content_hash: "3c770e3b2c54d190"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="The module management reference page." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, module management, module" name="keywords" />

    <title>Module management &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/hip_runtime_api/modules/module_management';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Occupancy" href="occupancy.html" />
    <link rel="prev" title="Context management [deprecated]" href="context_management.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/hip_runtime_api/modules/module_management.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Module management</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">Module management</li>
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
    <h1>Module management</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipModuleGetGlobalP14hipDeviceptr_tP6size_t11hipModule_tPKc"><code class="docutils literal notranslate"><span class="pre">hipModuleGetGlobal()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipModuleLoadFatBinaryP11hipModule_tPKv"><code class="docutils literal notranslate"><span class="pre">hipModuleLoadFatBinary()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipModuleLoadP11hipModule_tPKc"><code class="docutils literal notranslate"><span class="pre">hipModuleLoad()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipModuleUnload11hipModule_t"><code class="docutils literal notranslate"><span class="pre">hipModuleUnload()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipModuleGetFunctionP13hipFunction_t11hipModule_tPKc"><code class="docutils literal notranslate"><span class="pre">hipModuleGetFunction()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipModuleGetFunctionCountPj11hipModule_t"><code class="docutils literal notranslate"><span class="pre">hipModuleGetFunctionCount()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipLibraryLoadDataP12hipLibrary_tPKvP12hipJitOptionPPvjP16hipLibraryOptionPPvj"><code class="docutils literal notranslate"><span class="pre">hipLibraryLoadData()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipLibraryLoadFromFileP12hipLibrary_tPKcP12hipJitOptionPPvjP16hipLibraryOptionPPvj"><code class="docutils literal notranslate"><span class="pre">hipLibraryLoadFromFile()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipLibraryUnload12hipLibrary_t"><code class="docutils literal notranslate"><span class="pre">hipLibraryUnload()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipLibraryGetKernelP11hipKernel_t12hipLibrary_tPKc"><code class="docutils literal notranslate"><span class="pre">hipLibraryGetKernel()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipLibraryGetKernelCountPj12hipLibrary_t"><code class="docutils literal notranslate"><span class="pre">hipLibraryGetKernelCount()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipLibraryEnumerateKernelsP11hipKernel_tj12hipLibrary_t"><code class="docutils literal notranslate"><span class="pre">hipLibraryEnumerateKernels()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipKernelGetLibraryP12hipLibrary_t11hipKernel_t"><code class="docutils literal notranslate"><span class="pre">hipKernelGetLibrary()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipKernelGetNamePPKc11hipKernel_t"><code class="docutils literal notranslate"><span class="pre">hipKernelGetName()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipGetFuncBySymbolP13hipFunction_tPKv"><code class="docutils literal notranslate"><span class="pre">hipGetFuncBySymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipGetDriverEntryPointPKcPPvyP30hipDriverEntryPointQueryResult"><code class="docutils literal notranslate"><span class="pre">hipGetDriverEntryPoint()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipModuleGetTexRefPP16textureReference11hipModule_tPKc"><code class="docutils literal notranslate"><span class="pre">hipModuleGetTexRef()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipModuleLoadDataP11hipModule_tPKv"><code class="docutils literal notranslate"><span class="pre">hipModuleLoadData()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipModuleLoadDataExP11hipModule_tPKvjP12hipJitOptionPPv"><code class="docutils literal notranslate"><span class="pre">hipModuleLoadDataEx()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipLinkAddData14hipLinkState_t15hipJitInputTypePv6size_tPKcjP12hipJitOptionPPv"><code class="docutils literal notranslate"><span class="pre">hipLinkAddData()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipLinkAddFile14hipLinkState_t15hipJitInputTypePKcjP12hipJitOptionPPv"><code class="docutils literal notranslate"><span class="pre">hipLinkAddFile()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipLinkComplete14hipLinkState_tPPvP6size_t"><code class="docutils literal notranslate"><span class="pre">hipLinkComplete()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipLinkCreatejP12hipJitOptionPPvP14hipLinkState_t"><code class="docutils literal notranslate"><span class="pre">hipLinkCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipLinkDestroy14hipLinkState_t"><code class="docutils literal notranslate"><span class="pre">hipLinkDestroy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipMemGetHandleForAddressRangePv14hipDeviceptr_t6size_t21hipMemRangeHandleTypey"><code class="docutils literal notranslate"><span class="pre">hipMemGetHandleForAddressRange()</span></code></a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="module-management">
<span id="module-management-reference"></span><h1>Module management<a class="headerlink" href="#module-management" title="Link to this heading">#</a></h1>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipModuleGetGlobalP14hipDeviceptr_tP6size_t11hipModule_tPKc">
<span id="_CPPv318hipModuleGetGlobalP14hipDeviceptr_tP6size_t11hipModule_tPKc"></span><span id="_CPPv218hipModuleGetGlobalP14hipDeviceptr_tP6size_t11hipModule_tPKc"></span><span id="hipModuleGetGlobal__hipDeviceptr_tP.sP.hipModule_t.cCP"></span><span class="target" id="group___module_1ga3e425a680285f495e776f096e9632c89"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipModuleGetGlobal</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">bytes</span></span>, <span class="n"><span class="pre">hipModule_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hmod</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">name</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipModuleGetGlobalP14hipDeviceptr_tP6size_t11hipModule_tPKc" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a global pointer from a module. </p>
<p>Returns in *dptr and *bytes the pointer and size of the global of name name located in module hmod. If no variable of that name exists, it returns hipErrorNotFound. Both parameters dptr and bytes are optional. If one of them is NULL, it is ignored and hipSuccess is returned.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dptr</strong> – <strong>[out]</strong> Returns global device pointer </p></li>
<li><p><strong>bytes</strong> – <strong>[out]</strong> Returns global size in bytes </p></li>
<li><p><strong>hmod</strong> – <strong>[in]</strong> Module to retrieve global from </p></li>
<li><p><strong>name</strong> – <strong>[in]</strong> Name of global to retrieve</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotFound, hipErrorInvalidContext</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipModuleLoadFatBinaryP11hipModule_tPKv">
<span id="_CPPv322hipModuleLoadFatBinaryP11hipModule_tPKv"></span><span id="_CPPv222hipModuleLoadFatBinaryP11hipModule_tPKv"></span><span id="hipModuleLoadFatBinary__hipModule_tP.voidCP"></span><span class="target" id="group___module_1gadd464c89066b98fda5c7e0dfe20557e5"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipModuleLoadFatBinary</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipModule_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">module</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">fatbin</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipModuleLoadFatBinaryP11hipModule_tPKv" title="Link to this definition">#</a><br /></dt>
<dd><p>Loads fatbin object. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>fatbin</strong> – <strong>[in]</strong> fatbin to be loaded as a module </p></li>
<li><p><strong>module</strong> – <strong>[out]</strong> Module</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidContext, hipErrorFileNotFound, hipErrorOutOfMemory, hipErrorSharedObjectInitFailed, hipErrorNotInitialized</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipModuleLoadP11hipModule_tPKc">
<span id="_CPPv313hipModuleLoadP11hipModule_tPKc"></span><span id="_CPPv213hipModuleLoadP11hipModule_tPKc"></span><span id="hipModuleLoad__hipModule_tP.cCP"></span><span class="target" id="group___module_1ga31d806d976e91d36bd990ae3004d8760"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipModuleLoad</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipModule_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">module</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">fname</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipModuleLoadP11hipModule_tPKc" title="Link to this definition">#</a><br /></dt>
<dd><p>Loads code object from file into a module the currrent context. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>File/memory resources allocated in this function are released only in hipModuleUnload.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>fname</strong> – <strong>[in]</strong> Filename of code object to load</p></li>
<li><p><strong>module</strong> – <strong>[out]</strong> Module</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidContext, hipErrorFileNotFound, hipErrorOutOfMemory, hipErrorSharedObjectInitFailed, hipErrorNotInitialized</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415hipModuleUnload11hipModule_t">
<span id="_CPPv315hipModuleUnload11hipModule_t"></span><span id="_CPPv215hipModuleUnload11hipModule_t"></span><span id="hipModuleUnload__hipModule_t"></span><span class="target" id="group___module_1gae58e345f55bb3ec13dca80d2df88e0ed"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipModuleUnload</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipModule_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">module</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415hipModuleUnload11hipModule_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Frees the module. </p>
<p>
The module is freed, and the code objects associated with it are destroyed. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>module</strong> – <strong>[in]</strong> Module to free</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidResourceHandle</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv420hipModuleGetFunctionP13hipFunction_t11hipModule_tPKc">
<span id="_CPPv320hipModuleGetFunctionP13hipFunction_t11hipModule_tPKc"></span><span id="_CPPv220hipModuleGetFunctionP13hipFunction_t11hipModule_tPKc"></span><span id="hipModuleGetFunction__hipFunction_tP.hipModule_t.cCP"></span><span class="target" id="group___module_1ga9648b457bb837838cb936b417b56a65d"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipModuleGetFunction</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipFunction_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">function</span></span>, <span class="n"><span class="pre">hipModule_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">module</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">kname</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv420hipModuleGetFunctionP13hipFunction_t11hipModule_tPKc" title="Link to this definition">#</a><br /></dt>
<dd><p>Function with kname will be extracted if present in module. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>module</strong> – <strong>[in]</strong> Module to get function from </p></li>
<li><p><strong>kname</strong> – <strong>[in]</strong> Pointer to the name of function </p></li>
<li><p><strong>function</strong> – <strong>[out]</strong> Pointer to function handle</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidContext, hipErrorNotInitialized, hipErrorNotFound, </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425hipModuleGetFunctionCountPj11hipModule_t">
<span id="_CPPv325hipModuleGetFunctionCountPj11hipModule_t"></span><span id="_CPPv225hipModuleGetFunctionCountPj11hipModule_t"></span><span id="hipModuleGetFunctionCount__unsigned-iP.hipModule_t"></span><span class="target" id="group___module_1ga309efccad8ae2a17c8fb7454707904b7"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipModuleGetFunctionCount</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">hipModule_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mod</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425hipModuleGetFunctionCountPj11hipModule_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns the number of functions within a module. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>mod</strong> – <strong>[in]</strong> Module to get function count from </p></li>
<li><p><strong>count</strong> – <strong>[out]</strong> function count from module</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidContext, hipErrorNotInitialized, hipErrorNotFound, </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipLibraryLoadDataP12hipLibrary_tPKvP12hipJitOptionPPvjP16hipLibraryOptionPPvj">
<span id="_CPPv318hipLibraryLoadDataP12hipLibrary_tPKvP12hipJitOptionPPvjP16hipLibraryOptionPPvj"></span><span id="_CPPv218hipLibraryLoadDataP12hipLibrary_tPKvP12hipJitOptionPPvjP16hipLibraryOptionPPvj"></span><span id="hipLibraryLoadData__hipLibrary_tP.voidCP.hipJitOptionP.voidPP.unsigned-i.hipLibraryOptionP.voidPP.unsigned-i"></span><span class="target" id="group___module_1gae417a022a086597d3e1f672c9015f4d5"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLibraryLoadData</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipLibrary_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">library</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">code</span></span>, <span class="n"><span class="pre">hipJitOption</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">jitOptions</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">jitOptionsValues</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numJitOptions</span></span>, <span class="n"><span class="pre">hipLibraryOption</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">libraryOptions</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">libraryOptionValues</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numLibraryOptions</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipLibraryLoadDataP12hipLibrary_tPKvP12hipJitOptionPPvjP16hipLibraryOptionPPvj" title="Link to this definition">#</a><br /></dt>
<dd><p>Load hip Library from inmemory object. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>library</strong> – <strong>[out]</strong> Output Library </p></li>
<li><p><strong>code</strong> – <strong>[in]</strong> In memory object </p></li>
<li><p><strong>jitOptions</strong> – <strong>[in]</strong> JIT options, CUDA only </p></li>
<li><p><strong>jitOptionsValues</strong> – <strong>[in]</strong> JIT options values, CUDA only </p></li>
<li><p><strong>numJitOptions</strong> – <strong>[in]</strong> Number of JIT options </p></li>
<li><p><strong>libraryOptions</strong> – <strong>[in]</strong> Library options </p></li>
<li><p><strong>libraryOptionValues</strong> – <strong>[in]</strong> Library options values </p></li>
<li><p><strong>numLibraryOptions</strong> – <strong>[in]</strong> Number of library options </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipLibraryLoadFromFileP12hipLibrary_tPKcP12hipJitOptionPPvjP16hipLibraryOptionPPvj">
<span id="_CPPv322hipLibraryLoadFromFileP12hipLibrary_tPKcP12hipJitOptionPPvjP16hipLibraryOptionPPvj"></span><span id="_CPPv222hipLibraryLoadFromFileP12hipLibrary_tPKcP12hipJitOptionPPvjP16hipLibraryOptionPPvj"></span><span id="hipLibraryLoadFromFile__hipLibrary_tP.cCP.hipJitOptionP.voidPP.unsigned-i.hipLibraryOptionP.voidPP.unsigned-i"></span><span class="target" id="group___module_1ga5dff638bef38052c410ef3fa06fa1795"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLibraryLoadFromFile</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipLibrary_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">library</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">fileName</span></span>, <span class="n"><span class="pre">hipJitOption</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">jitOptions</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">jitOptionsValues</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numJitOptions</span></span>, <span class="n"><span class="pre">hipLibraryOption</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">libraryOptions</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">libraryOptionValues</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numLibraryOptions</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipLibraryLoadFromFileP12hipLibrary_tPKcP12hipJitOptionPPvjP16hipLibraryOptionPPvj" title="Link to this definition">#</a><br /></dt>
<dd><p>Load hip Library from file. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>library</strong> – <strong>[out]</strong> Output Library </p></li>
<li><p><strong>fileName</strong> – <strong>[in]</strong> file which contains code object </p></li>
<li><p><strong>jitOptions</strong> – <strong>[in]</strong> JIT options, CUDA only </p></li>
<li><p><strong>jitOptionsValues</strong> – <strong>[in]</strong> JIT options values, CUDA only </p></li>
<li><p><strong>numJitOptions</strong> – <strong>[in]</strong> Number of JIT options </p></li>
<li><p><strong>libraryOptions</strong> – <strong>[in]</strong> Library options </p></li>
<li><p><strong>libraryOptionValues</strong> – <strong>[in]</strong> Library options values </p></li>
<li><p><strong>numLibraryOptions</strong> – <strong>[in]</strong> Number of library options </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipLibraryUnload12hipLibrary_t">
<span id="_CPPv316hipLibraryUnload12hipLibrary_t"></span><span id="_CPPv216hipLibraryUnload12hipLibrary_t"></span><span id="hipLibraryUnload__hipLibrary_t"></span><span class="target" id="group___module_1ga3fd2267120accdaf3aa0c6cc684d7e1d"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLibraryUnload</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipLibrary_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">library</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipLibraryUnload12hipLibrary_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Unload HIP Library. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>library</strong> – <strong>[in]</strong> Input created hip library </p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipLibraryGetKernelP11hipKernel_t12hipLibrary_tPKc">
<span id="_CPPv319hipLibraryGetKernelP11hipKernel_t12hipLibrary_tPKc"></span><span id="_CPPv219hipLibraryGetKernelP11hipKernel_t12hipLibrary_tPKc"></span><span id="hipLibraryGetKernel__hipKernel_tP.hipLibrary_t.cCP"></span><span class="target" id="group___module_1ga8802b7f1757161e47238dc32cceb9283"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLibraryGetKernel</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipKernel_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pKernel</span></span>, <span class="n"><span class="pre">hipLibrary_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">library</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">name</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipLibraryGetKernelP11hipKernel_t12hipLibrary_tPKc" title="Link to this definition">#</a><br /></dt>
<dd><p>Get Kernel object from library. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pKernel</strong> – <strong>[out]</strong> Output kernel object </p></li>
<li><p><strong>library</strong> – <strong>[in]</strong> Input hip library </p></li>
<li><p><strong>name</strong> – <strong>[in]</strong> kernel name to be searched for </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424hipLibraryGetKernelCountPj12hipLibrary_t">
<span id="_CPPv324hipLibraryGetKernelCountPj12hipLibrary_t"></span><span id="_CPPv224hipLibraryGetKernelCountPj12hipLibrary_t"></span><span id="hipLibraryGetKernelCount__unsigned-iP.hipLibrary_t"></span><span class="target" id="group___module_1gab6cc7286ee4ab0094878f41a43dfeb6a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLibraryGetKernelCount</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">hipLibrary_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">library</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424hipLibraryGetKernelCountPj12hipLibrary_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Get Kernel count in library. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>count</strong> – <strong>[out]</strong> Count of kernels in library </p></li>
<li><p><strong>library</strong> – <strong>[in]</strong> Input created hip library </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426hipLibraryEnumerateKernelsP11hipKernel_tj12hipLibrary_t">
<span id="_CPPv326hipLibraryEnumerateKernelsP11hipKernel_tj12hipLibrary_t"></span><span id="_CPPv226hipLibraryEnumerateKernelsP11hipKernel_tj12hipLibrary_t"></span><span id="hipLibraryEnumerateKernels__hipKernel_tP.unsigned-i.hipLibrary_t"></span><span class="target" id="group___module_1ga698bf2365bcb3ab7380bc81dd8033667"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLibraryEnumerateKernels</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipKernel_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">kernels</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numKernels</span></span>, <span class="n"><span class="pre">hipLibrary_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">library</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426hipLibraryEnumerateKernelsP11hipKernel_tj12hipLibrary_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Retrieve kernel handles within a library. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>kernels</strong> – <strong>[out]</strong> Buffer for kernel handles </p></li>
<li><p><strong>numKernels</strong> – <strong>[in]</strong> Maximum number of kernel handles to return to buffer &#64;oaram [in] library Library handle to query from </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipKernelGetLibraryP12hipLibrary_t11hipKernel_t">
<span id="_CPPv319hipKernelGetLibraryP12hipLibrary_t11hipKernel_t"></span><span id="_CPPv219hipKernelGetLibraryP12hipLibrary_t11hipKernel_t"></span><span id="hipKernelGetLibrary__hipLibrary_tP.hipKernel_t"></span><span class="target" id="group___module_1gaeb1746abcfcbde455628f541c86f70fd"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipKernelGetLibrary</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipLibrary_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">library</span></span>, <span class="n"><span class="pre">hipKernel_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kernel</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipKernelGetLibraryP12hipLibrary_t11hipKernel_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Library Handle. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>library</strong> – <strong>[out]</strong> Returned Library handle </p></li>
<li><p><strong>kernel</strong> – <strong>[in]</strong> Kernel to retrieve library Handle </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipKernelGetNamePPKc11hipKernel_t">
<span id="_CPPv316hipKernelGetNamePPKc11hipKernel_t"></span><span id="_CPPv216hipKernelGetNamePPKc11hipKernel_t"></span><span id="hipKernelGetName__cCPP.hipKernel_t"></span><span class="target" id="group___module_1ga8fba95e5de4ae981e7218d619ee245bf"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipKernelGetName</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">name</span></span>, <span class="n"><span class="pre">hipKernel_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">kernel</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipKernelGetNamePPKc11hipKernel_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a Kernel Name. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> – <strong>[out]</strong> Returned Kernel Name </p></li>
<li><p><strong>kernel</strong> – <strong>[in]</strong> Kernel handle to retrieve name </p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipGetFuncBySymbolP13hipFunction_tPKv">
<span id="_CPPv318hipGetFuncBySymbolP13hipFunction_tPKv"></span><span id="_CPPv218hipGetFuncBySymbolP13hipFunction_tPKv"></span><span id="hipGetFuncBySymbol__hipFunction_tP.voidCP"></span><span class="target" id="group___module_1ga4adaac7b90f84ec13b0274df72245547"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGetFuncBySymbol</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipFunction_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">functionPtr</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbolPtr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipGetFuncBySymbolP13hipFunction_tPKv" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets pointer to device entry function that matches entry function symbolPtr. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>functionPtr</strong> – <strong>[out]</strong> Device entry function </p></li>
<li><p><strong>symbolPtr</strong> – <strong>[in]</strong> Pointer to device entry function to search for</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidDeviceFunction</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipGetDriverEntryPointPKcPPvyP30hipDriverEntryPointQueryResult">
<span id="_CPPv322hipGetDriverEntryPointPKcPPvyP30hipDriverEntryPointQueryResult"></span><span id="_CPPv222hipGetDriverEntryPointPKcPPvyP30hipDriverEntryPointQueryResult"></span><span id="hipGetDriverEntryPoint__cCP.voidPP.unsigned-l-l.hipDriverEntryPointQueryResultP"></span><span class="target" id="group___module_1gaa711b3fea8483aecf71e0a1c13af4684"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGetDriverEntryPoint</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">funcPtr</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span>, <span class="n"><span class="pre">hipDriverEntryPointQueryResult</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">driverStatus</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipGetDriverEntryPointPKcPPvyP30hipDriverEntryPointQueryResult" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets function pointer of a requested HIP API. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>symbol</strong> – <strong>[in]</strong> The API base name </p></li>
<li><p><strong>funcPtr</strong> – <strong>[out]</strong> Pointer to the requested function </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Flags for the search </p></li>
<li><p><strong>driverStatus</strong> – <strong>[out]</strong> Optional returned status of the search</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipModuleGetTexRefPP16textureReference11hipModule_tPKc">
<span id="_CPPv318hipModuleGetTexRefPP16textureReference11hipModule_tPKc"></span><span id="_CPPv218hipModuleGetTexRefPP16textureReference11hipModule_tPKc"></span><span id="hipModuleGetTexRef__textureReferencePP.hipModule_t.cCP"></span><span class="target" id="group___module_1ga1ceb20d084d571c28282ee2fd052264c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipModuleGetTexRef</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="n"><span class="pre">hipModule_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">hmod</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">name</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipModuleGetTexRefPP16textureReference11hipModule_tPKc" title="Link to this definition">#</a><br /></dt>
<dd><p>returns the handle of the texture reference with the name from the module. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hmod</strong> – <strong>[in]</strong> Module </p></li>
<li><p><strong>name</strong> – <strong>[in]</strong> Pointer of name of texture reference </p></li>
<li><p><strong>texRef</strong> – <strong>[out]</strong> Pointer of texture reference</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorNotInitialized, hipErrorNotFound, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipModuleLoadDataP11hipModule_tPKv">
<span id="_CPPv317hipModuleLoadDataP11hipModule_tPKv"></span><span id="_CPPv217hipModuleLoadDataP11hipModule_tPKv"></span><span id="hipModuleLoadData__hipModule_tP.voidCP"></span><span class="target" id="group___module_1gaabdbd73e952a741e861d01109c4790f3"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipModuleLoadData</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipModule_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">module</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">image</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipModuleLoadDataP11hipModule_tPKv" title="Link to this definition">#</a><br /></dt>
<dd><p>builds module from code object data which resides in host memory. </p>
<p>The “image” is a pointer to the location of code object data. This data can be either a single code object or a fat binary (fatbin), which serves as the entry point for loading and launching device-specific kernel executions.</p>
<p>By default, the following command generates a fatbin:</p>
<p>“amdclang++ -O3 -c –offload-device-only –offload-arch=&lt;GPU_ARCH&gt; &lt;input_file&gt; -o &lt;output_file&gt;”</p>
<p>For more details, refer to: <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/kernel_language_cpp_support.html#kernel-compilation">Kernel Compilation</a> in the HIP kernel language C++ support, or <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_rtc.html">HIP runtime compilation (HIP RTC)</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>image</strong> – <strong>[in]</strong> The pointer to the location of data </p></li>
<li><p><strong>module</strong> – <strong>[out]</strong> Retuned module</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorNotInitialized, hipErrorOutOfMemory, hipErrorNotInitialized </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipModuleLoadDataExP11hipModule_tPKvjP12hipJitOptionPPv">
<span id="_CPPv319hipModuleLoadDataExP11hipModule_tPKvjP12hipJitOptionPPv"></span><span id="_CPPv219hipModuleLoadDataExP11hipModule_tPKvjP12hipJitOptionPPv"></span><span id="hipModuleLoadDataEx__hipModule_tP.voidCP.unsigned-i.hipJitOptionP.voidPP"></span><span class="target" id="group___module_1ga3e70722338894f48540c7be9a136af79"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipModuleLoadDataEx</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipModule_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">module</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">image</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numOptions</span></span>, <span class="n"><span class="pre">hipJitOption</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">options</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">optionValues</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipModuleLoadDataExP11hipModule_tPKvjP12hipJitOptionPPv" title="Link to this definition">#</a><br /></dt>
<dd><p>builds module from code object which resides in host memory. Image is pointer to that location. Options are not used. hipModuleLoadData is called. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>image</strong> – <strong>[in]</strong> The pointer to the location of data </p></li>
<li><p><strong>module</strong> – <strong>[out]</strong> Retuned module </p></li>
<li><p><strong>numOptions</strong> – <strong>[in]</strong> Number of options </p></li>
<li><p><strong>options</strong> – <strong>[in]</strong> Options for JIT </p></li>
<li><p><strong>optionValues</strong> – <strong>[in]</strong> Option values for JIT</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorNotInitialized, hipErrorOutOfMemory, hipErrorNotInitialized </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipLinkAddData14hipLinkState_t15hipJitInputTypePv6size_tPKcjP12hipJitOptionPPv">
<span id="_CPPv314hipLinkAddData14hipLinkState_t15hipJitInputTypePv6size_tPKcjP12hipJitOptionPPv"></span><span id="_CPPv214hipLinkAddData14hipLinkState_t15hipJitInputTypePv6size_tPKcjP12hipJitOptionPPv"></span><span id="hipLinkAddData__hipLinkState_t.hipJitInputType.voidP.s.cCP.unsigned-i.hipJitOptionP.voidPP"></span><span class="target" id="group___module_1gaf3bda16dabe443ea621212c39a0573f2"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLinkAddData</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipLinkState_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">state</span></span>, <span class="n"><span class="pre">hipJitInputType</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">type</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">name</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numOptions</span></span>, <span class="n"><span class="pre">hipJitOption</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">options</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">optionValues</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipLinkAddData14hipLinkState_t15hipJitInputTypePv6size_tPKcjP12hipJitOptionPPv" title="Link to this definition">#</a><br /></dt>
<dd><p>Adds bitcode data to be linked with options. </p>
<p>
If adding the file fails, it will <div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hipError_t</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – <strong>[in]</strong> hip link state </p></li>
<li><p><strong>type</strong> – <strong>[in]</strong> Type of the input data or bitcode </p></li>
<li><p><strong>data</strong> – <strong>[in]</strong> Input data which is null terminated </p></li>
<li><p><strong>size</strong> – <strong>[in]</strong> Size of the input data </p></li>
<li><p><strong>name</strong> – <strong>[in]</strong> Optional name for this input </p></li>
<li><p><strong>numOptions</strong> – <strong>[in]</strong> Size of the options </p></li>
<li><p><strong>options</strong> – <strong>[in]</strong> Array of options applied to this input </p></li>
<li><p><strong>optionValues</strong> – <strong>[in]</strong> Array of option values cast to void*</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorInvalidHandle</p>
</dd>
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>hipErrorInvalidConfiguration</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipLinkAddFile14hipLinkState_t15hipJitInputTypePKcjP12hipJitOptionPPv">
<span id="_CPPv314hipLinkAddFile14hipLinkState_t15hipJitInputTypePKcjP12hipJitOptionPPv"></span><span id="_CPPv214hipLinkAddFile14hipLinkState_t15hipJitInputTypePKcjP12hipJitOptionPPv"></span><span id="hipLinkAddFile__hipLinkState_t.hipJitInputType.cCP.unsigned-i.hipJitOptionP.voidPP"></span><span class="target" id="group___module_1ga4060b26dae6d689b859b047649bcc3a4"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLinkAddFile</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipLinkState_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">state</span></span>, <span class="n"><span class="pre">hipJitInputType</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">type</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">char</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">path</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numOptions</span></span>, <span class="n"><span class="pre">hipJitOption</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">options</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">optionValues</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipLinkAddFile14hipLinkState_t15hipJitInputTypePKcjP12hipJitOptionPPv" title="Link to this definition">#</a><br /></dt>
<dd><p>Adds a file with bitcode to be linked with options. </p>
<p>
If adding the file fails, it will <div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hipError_t</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – <strong>[in]</strong> hip link state </p></li>
<li><p><strong>type</strong> – <strong>[in]</strong> Type of the input data or bitcode </p></li>
<li><p><strong>path</strong> – <strong>[in]</strong> Path to the input file where bitcode is present </p></li>
<li><p><strong>numOptions</strong> – <strong>[in]</strong> Size of the options </p></li>
<li><p><strong>options</strong> – <strong>[in]</strong> Array of options applied to this input </p></li>
<li><p><strong>optionValues</strong> – <strong>[in]</strong> Array of option values cast to void*</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>hipErrorInvalidConfiguration</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415hipLinkComplete14hipLinkState_tPPvP6size_t">
<span id="_CPPv315hipLinkComplete14hipLinkState_tPPvP6size_t"></span><span id="_CPPv215hipLinkComplete14hipLinkState_tPPvP6size_t"></span><span id="hipLinkComplete__hipLinkState_t.voidPP.sP"></span><span class="target" id="group___module_1ga2bb425497d49cd8245aee333b8024270"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLinkComplete</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipLinkState_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">state</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">hipBinOut</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">sizeOut</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415hipLinkComplete14hipLinkState_tPPvP6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Completes the linking of the given program. </p>
<p>
If adding the data fails, it will <div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hipError_t</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>state</strong> – <strong>[in]</strong> hip link state </p></li>
<li><p><strong>hipBinOut</strong> – <strong>[out]</strong> Upon success, points to the output binary </p></li>
<li><p><strong>sizeOut</strong> – <strong>[out]</strong> Size of the binary is stored (optional)</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess hipErrorInvalidValue</p>
</dd>
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>hipErrorInvalidConfiguration</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv413hipLinkCreatejP12hipJitOptionPPvP14hipLinkState_t">
<span id="_CPPv313hipLinkCreatejP12hipJitOptionPPvP14hipLinkState_t"></span><span id="_CPPv213hipLinkCreatejP12hipJitOptionPPvP14hipLinkState_t"></span><span id="hipLinkCreate__unsigned-i.hipJitOptionP.voidPP.hipLinkState_tP"></span><span class="target" id="group___module_1ga9883986f6bfe2d83f97c7823bae484bd"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLinkCreate</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numOptions</span></span>, <span class="n"><span class="pre">hipJitOption</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">options</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">optionValues</span></span>, <span class="n"><span class="pre">hipLinkState_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">stateOut</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv413hipLinkCreatejP12hipJitOptionPPvP14hipLinkState_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a linker instance with options. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hipSuccess</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>numOptions</strong> – <strong>[in]</strong> Number of options </p></li>
<li><p><strong>options</strong> – <strong>[in]</strong> Array of options </p></li>
<li><p><strong>optionValues</strong> – <strong>[in]</strong> Array of option values cast to void* </p></li>
<li><p><strong>stateOut</strong> – <strong>[out]</strong> hip link state created upon success</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess hipErrorInvalidValue hipErrorInvalidConfiguration</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipLinkDestroy14hipLinkState_t">
<span id="_CPPv314hipLinkDestroy14hipLinkState_t"></span><span id="_CPPv214hipLinkDestroy14hipLinkState_t"></span><span id="hipLinkDestroy__hipLinkState_t"></span><span class="target" id="group___module_1ga5aad9536fafac972e38efd1efe2c29b9"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLinkDestroy</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipLinkState_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">state</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipLinkDestroy14hipLinkState_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Deletes the linker instance. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p>hipSuccess</p>
</div>
</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>state</strong> – <strong>[in]</strong> link state instance</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv430hipMemGetHandleForAddressRangePv14hipDeviceptr_t6size_t21hipMemRangeHandleTypey">
<span id="_CPPv330hipMemGetHandleForAddressRangePv14hipDeviceptr_t6size_t21hipMemRangeHandleTypey"></span><span id="_CPPv230hipMemGetHandleForAddressRangePv14hipDeviceptr_t6size_t21hipMemRangeHandleTypey"></span><span id="hipMemGetHandleForAddressRange__voidP.hipDeviceptr_t.s.hipMemRangeHandleType.unsigned-l-l"></span><span class="target" id="group___module_1ga641bf30f80c5483db4c13eda7b37cb5d"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemGetHandleForAddressRange</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">handle</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="n"><span class="pre">hipMemRangeHandleType</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">handleType</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv430hipMemGetHandleForAddressRangePv14hipDeviceptr_t6size_t21hipMemRangeHandleTypey" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns a handle for the address range requested. </p>
<p>This function returns a handle to a device pointer created using either hipMalloc set of APIs or through hipMemAddressReserve (as long as the ptr is mapped).</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>handle</strong> – <strong>[out]</strong> Ptr to the handle where the fd or other types will be returned. </p></li>
<li><p><strong>dptr</strong> – <strong>[in]</strong> Device ptr for which we get the handle. </p></li>
<li><p><strong>size</strong> – <strong>[in]</strong> Size of the address range. </p></li>
<li><p><strong>handleType</strong> – <strong>[in]</strong> Type of the handle requested for the address range. </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Any flags set regarding the handle requested.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess if the kernel is launched successfully, otherwise an appropriate error code. </p>
</dd>
</dl>
</dd></dl>

</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="context_management.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Context management [deprecated]</p>
      </div>
    </a>
    <a class="right-next"
       href="occupancy.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Occupancy</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipModuleGetGlobalP14hipDeviceptr_tP6size_t11hipModule_tPKc"><code class="docutils literal notranslate"><span class="pre">hipModuleGetGlobal()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipModuleLoadFatBinaryP11hipModule_tPKv"><code class="docutils literal notranslate"><span class="pre">hipModuleLoadFatBinary()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipModuleLoadP11hipModule_tPKc"><code class="docutils literal notranslate"><span class="pre">hipModuleLoad()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipModuleUnload11hipModule_t"><code class="docutils literal notranslate"><span class="pre">hipModuleUnload()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv420hipModuleGetFunctionP13hipFunction_t11hipModule_tPKc"><code class="docutils literal notranslate"><span class="pre">hipModuleGetFunction()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipModuleGetFunctionCountPj11hipModule_t"><code class="docutils literal notranslate"><span class="pre">hipModuleGetFunctionCount()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipLibraryLoadDataP12hipLibrary_tPKvP12hipJitOptionPPvjP16hipLibraryOptionPPvj"><code class="docutils literal notranslate"><span class="pre">hipLibraryLoadData()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipLibraryLoadFromFileP12hipLibrary_tPKcP12hipJitOptionPPvjP16hipLibraryOptionPPvj"><code class="docutils literal notranslate"><span class="pre">hipLibraryLoadFromFile()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipLibraryUnload12hipLibrary_t"><code class="docutils literal notranslate"><span class="pre">hipLibraryUnload()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipLibraryGetKernelP11hipKernel_t12hipLibrary_tPKc"><code class="docutils literal notranslate"><span class="pre">hipLibraryGetKernel()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipLibraryGetKernelCountPj12hipLibrary_t"><code class="docutils literal notranslate"><span class="pre">hipLibraryGetKernelCount()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipLibraryEnumerateKernelsP11hipKernel_tj12hipLibrary_t"><code class="docutils literal notranslate"><span class="pre">hipLibraryEnumerateKernels()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipKernelGetLibraryP12hipLibrary_t11hipKernel_t"><code class="docutils literal notranslate"><span class="pre">hipKernelGetLibrary()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipKernelGetNamePPKc11hipKernel_t"><code class="docutils literal notranslate"><span class="pre">hipKernelGetName()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipGetFuncBySymbolP13hipFunction_tPKv"><code class="docutils literal notranslate"><span class="pre">hipGetFuncBySymbol()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipGetDriverEntryPointPKcPPvyP30hipDriverEntryPointQueryResult"><code class="docutils literal notranslate"><span class="pre">hipGetDriverEntryPoint()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipModuleGetTexRefPP16textureReference11hipModule_tPKc"><code class="docutils literal notranslate"><span class="pre">hipModuleGetTexRef()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipModuleLoadDataP11hipModule_tPKv"><code class="docutils literal notranslate"><span class="pre">hipModuleLoadData()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipModuleLoadDataExP11hipModule_tPKvjP12hipJitOptionPPv"><code class="docutils literal notranslate"><span class="pre">hipModuleLoadDataEx()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipLinkAddData14hipLinkState_t15hipJitInputTypePv6size_tPKcjP12hipJitOptionPPv"><code class="docutils literal notranslate"><span class="pre">hipLinkAddData()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipLinkAddFile14hipLinkState_t15hipJitInputTypePKcjP12hipJitOptionPPv"><code class="docutils literal notranslate"><span class="pre">hipLinkAddFile()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipLinkComplete14hipLinkState_tPPvP6size_t"><code class="docutils literal notranslate"><span class="pre">hipLinkComplete()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv413hipLinkCreatejP12hipJitOptionPPvP14hipLinkState_t"><code class="docutils literal notranslate"><span class="pre">hipLinkCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipLinkDestroy14hipLinkState_t"><code class="docutils literal notranslate"><span class="pre">hipLinkDestroy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipMemGetHandleForAddressRangePv14hipDeviceptr_t6size_t21hipMemRangeHandleTypey"><code class="docutils literal notranslate"><span class="pre">hipMemGetHandleForAddressRange()</span></code></a></li>
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
