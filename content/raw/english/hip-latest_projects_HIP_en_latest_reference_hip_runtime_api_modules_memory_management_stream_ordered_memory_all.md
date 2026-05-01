---
title: "Stream ordered memory allocator &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:50.534728+00:00
content_hash: "62050af4c50bf3e1"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="The stream ordered memory allocator reference page." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, stream ordered memory allocator" name="keywords" />

    <title>Stream ordered memory allocator &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
  <script data-cfasync="false">
    document.documentElement.dataset.mode = localStorage.getItem("mode") || "";
    document.documentElement.dataset.theme = localStorage.getItem("theme") || "";
  </script>
  
  <!-- Loaded before other Sphinx assets -->
  <link href="../../../../_static/styles/theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../../../../_static/styles/bootstrap.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../../../../_static/styles/pydata-sphinx-theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />

  
  <link href="../../../../_static/vendor/fontawesome/6.5.2/css/all.min.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
  <link rel="preload" as="font" type="font/woff2" crossorigin href="../../../../_static/vendor/fontawesome/6.5.2/webfonts/fa-solid-900.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../../../_static/vendor/fontawesome/6.5.2/webfonts/fa-brands-400.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../../../_static/vendor/fontawesome/6.5.2/webfonts/fa-regular-400.woff2" />

    <link rel="stylesheet" type="text/css" href="../../../../_static/pygments.css?v=a746c00c" />
    <link rel="stylesheet" type="text/css" href="../../../../_static/styles/sphinx-book-theme.css?v=a3416100" />
    <link rel="stylesheet" type="text/css" href="../../../../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
    <link rel="stylesheet" type="text/css" href="../../../../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../../../../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../../../../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../../../../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../../../../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../../../../_static/sphinx-design.min.css?v=95c83b7e" />
    <link rel="stylesheet" type="text/css" href="../../../../_static/rocm_custom.css?v=35d74aab" />
  
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../../../../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b" />
<link rel="preload" as="script" href="../../../../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b" />
  <script src="../../../../_static/vendor/fontawesome/6.5.2/js/all.min.js?digest=dfe6caa3a7d634c4db9b"></script>

    <script src="../../../../_static/documentation_options.js?v=75144bb1"></script>
    <script src="../../../../_static/doctools.js?v=9a2dae69"></script>
    <script src="../../../../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../../../../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../../../../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../../../../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../../../../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../../../../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../../../../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../../../../_static/search.js?v=90a4452c"></script>
    <script src="../../../../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
    <script src="../../../../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../../genindex.html" />
    <link rel="search" title="Search" href="../../../../search.html" />
    <link rel="next" title="Managed memory" href="unified_memory_reference.html" />
    <link rel="prev" title="External resource interoperability" href="external_resource_interoperability.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
      action="../../../../search.html"
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
                    <img src="../../../../_static/images/amd-header-logo.svg" alt="AMD Logo" title="AMD Logo" width="90" class="d-inline-block align-text-top hover-opacity"/>
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

  
    
  

<a class="navbar-brand logo" href="../../../../index.html">
  
  
  
  
  
  
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
<li class="toctree-l1"><a class="reference internal" href="../../../../what_is_hip.html">What is HIP?</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../hip-7-changes.html">HIP API 7.0 changes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../faq.html">Frequently asked questions</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../../install/install.html">Installing HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../install/build.html">Building HIP from source</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Programming guide</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../../understand/programming_model.html">Introduction to the HIP programming model</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../understand/performance_optimization.html">Understanding GPU performance</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../understand/hardware_implementation.html">Hardware implementation</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../understand/compilers.html">HIP compilers</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../how-to/performance_guidelines.html">Performance guidelines</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../how-to/debugging.html">Debugging with HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../how-to/logging.html">Logging HIP activity</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../../../../how-to/hip_runtime_api.html">Using HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../../../../how-to/hip_runtime_api/initialization.html">Initialization</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../../../../how-to/hip_runtime_api/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../../../how-to/hip_runtime_api/memory_management/host_memory.html">Host memory</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../../../../how-to/hip_runtime_api/memory_management/device_memory.html">Device memory</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../../../../how-to/hip_runtime_api/memory_management/device_memory/texture_fetching.html">Texture fetching</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="../../../../how-to/hip_runtime_api/memory_management/coherence_control.html">Coherence control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../../how-to/hip_runtime_api/memory_management/unified_memory.html">Unified memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../../how-to/hip_runtime_api/memory_management/virtual_memory.html">Virtual memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../../how-to/hip_runtime_api/memory_management/stream_ordered_allocator.html">Stream Ordered Memory Allocator</a></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="../../../../how-to/hip_runtime_api/error_handling.html">Error handling</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../../how-to/hip_runtime_api/call_stack.html">Call stack</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../../how-to/hip_runtime_api/asynchronous.html">Asynchronous concurrent execution</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../../how-to/hip_runtime_api/hipgraph.html">HIP graphs</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../../how-to/hip_runtime_api/cooperative_groups.html">Cooperative groups</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../../how-to/hip_runtime_api/multi_device.html">Multi-device management</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../../how-to/hip_runtime_api/opengl_interop.html">OpenGL interoperability</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../../how-to/hip_runtime_api/external_interop.html">External resource interoperability</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../how-to/hip_cpp_language_extensions.html">HIP C++ language extensions</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../how-to/kernel_language_cpp_support.html">Kernel language C++ support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../how-to/hip_porting_guide.html">Porting CUDA code to HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../how-to/hip_rtc.html">Programming for HIP runtime compiler (RTC)</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../understand/amd_clr.html">AMD compute language runtimes (CLR)</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active has-children"><a class="reference internal" href="../../../hip_runtime_api_reference.html">HIP runtime API</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2 current active has-children"><a class="reference internal" href="../../modules.html">Modules</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l3"><a class="reference internal" href="../initialization_and_version.html">Initialization and version</a></li>
<li class="toctree-l3"><a class="reference internal" href="../device_management.html">Device management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../execution_control.html">Execution control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../error_handling.html">Error handling</a></li>
<li class="toctree-l3"><a class="reference internal" href="../stream_management.html">Stream management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../stream_memory_operations.html">Stream memory operations</a></li>
<li class="toctree-l3"><a class="reference internal" href="../event_management.html">Event management</a></li>
<li class="toctree-l3 current active has-children"><a class="reference internal" href="../memory_management.html">Memory management</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l4"><a class="reference internal" href="memory_management_deprecated.html">Memory management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="external_resource_interoperability.html">External resource interoperability</a></li>
<li class="toctree-l4 current active"><a class="current reference internal" href="#">Stream ordered memory allocator</a></li>
<li class="toctree-l4"><a class="reference internal" href="unified_memory_reference.html">Managed memory</a></li>
<li class="toctree-l4"><a class="reference internal" href="virtual_memory_reference.html">Virtual memory management</a></li>
<li class="toctree-l4"><a class="reference internal" href="texture_management.html">Texture management</a></li>
<li class="toctree-l4"><a class="reference internal" href="texture_management_deprecated.html">Texture management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="surface_object.html">Surface object</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="../peer_to_peer_device_memory_access.html">Peer to peer device memory access</a></li>
<li class="toctree-l3"><a class="reference internal" href="../context_management.html">Context management [deprecated]</a></li>
<li class="toctree-l3"><a class="reference internal" href="../module_management.html">Module management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../occupancy.html">Occupancy</a></li>
<li class="toctree-l3"><a class="reference internal" href="../profiler_control.html">Profiler control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../launch_api.html">Launch API</a></li>
<li class="toctree-l3"><a class="reference internal" href="../runtime_compilation.html">Runtime compilation</a></li>
<li class="toctree-l3"><a class="reference internal" href="../callback_activity_apis.html">Callback activity APIs</a></li>
<li class="toctree-l3"><a class="reference internal" href="../graph_management.html">Graph management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../graphics_interoperability.html">Graphics interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="../opengl_interoperability.html">OpenGL interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="../cooperative_groups_reference.html">Cooperative groups</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../../global_defines_enums_structs_files.html">Global defines, enums, structs and files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../../../doxygen/html/group___global_defs.html">Global enum and defines</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../../doxygen/html/group___driver_types.html">Driver Types</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../../doxygen/html/annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../../doxygen/html/files.html">File List</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../../math_api.html">HIP math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../complex_math_api.html">HIP complex math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../env_variables.html">HIP environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../error_codes.html">HIP error codes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../api_syntax.html">CUDA to HIP API Function Comparison</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../deprecated_api_list.html">List of deprecated APIs</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../low_fp_types.html">Low Precision Floating Point Types</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../hardware_features.html">Hardware features</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Tutorials</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic">HIP basic examples</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples">HIP examples</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../tutorial/saxpy.html">SAXPY - Hello, HIP</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../../../../tutorial/programming-patterns.html">GPU programming patterns</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../../../../tutorial/programming-patterns/matrix_multiplication.html">Two-dimensional kernels: Matrix multiplication tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../../tutorial/programming-patterns/atomic_operations_histogram.html">Atomic operations: Histogram tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../../tutorial/programming-patterns/cpu_gpu_kmeans.html">CPU-GPU cooperative computing: K-means clustering tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../../tutorial/programming-patterns/stencil_operations.html">Stencil operations: Image convolution tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../../../tutorial/programming-patterns/multikernel_bfs.html">Multi-kernel programming: breadth-first search tutorial</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../tutorial/reduction.html">Reduction</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../tutorial/cooperative_groups_tutorial.html">Cooperative groups</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../../tutorial/graph_api.html">HIP Graph API Tutorial</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">About</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../../license.html">License</a></li>
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
      <a href="../../../../index.html" class="nav-link" aria-label="Home">
        <i class="fa-solid fa-home"></i>
      </a>
    </li>
    
    <li class="breadcrumb-item"><a href="../../../hip_runtime_api_reference.html" class="nav-link">HIP runtime API</a></li>
    
    
    <li class="breadcrumb-item"><i class="fa-solid fa-ellipsis"></i></li>
    
    
    <li class="breadcrumb-item"><a href="../memory_management.html" class="nav-link">Memory management</a></li>
    
    <li class="breadcrumb-item active" aria-current="page">Stream...</li>
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
    <h1>Stream ordered memory allocator</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMallocAsyncPPv6size_t12hipMemPool_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E14hipMallocAsync10hipError_tPP1T6size_t12hipMemPool_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E14hipMallocAsync10hipError_tPP1T6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E22hipMallocFromPoolAsync10hipError_tPP1T6size_t12hipMemPool_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMallocFromPoolAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4IDpDpE17hipLaunchKernelEx10hipError_tPK17hipLaunchConfig_tPFvDp10KernelArgsEDpRR6Params"><code class="docutils literal notranslate"><span class="pre">hipLaunchKernelEx()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMallocAsyncPPv6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipFreeAsyncPv11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipFreeAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemPoolTrimTo12hipMemPool_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemPoolTrimTo()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipMemPoolSetAttribute12hipMemPool_t14hipMemPoolAttrPv"><code class="docutils literal notranslate"><span class="pre">hipMemPoolSetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipMemPoolGetAttribute12hipMemPool_t14hipMemPoolAttrPv"><code class="docutils literal notranslate"><span class="pre">hipMemPoolGetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemPoolSetAccess12hipMemPool_tPK16hipMemAccessDesc6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemPoolSetAccess()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemPoolGetAccessP17hipMemAccessFlags12hipMemPool_tP14hipMemLocation"><code class="docutils literal notranslate"><span class="pre">hipMemPoolGetAccess()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemPoolCreateP12hipMemPool_tPK15hipMemPoolProps"><code class="docutils literal notranslate"><span class="pre">hipMemPoolCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipMemPoolDestroy12hipMemPool_t"><code class="docutils literal notranslate"><span class="pre">hipMemPoolDestroy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipMallocFromPoolAsyncPPv6size_t12hipMemPool_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMallocFromPoolAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv433hipMemPoolExportToShareableHandlePv12hipMemPool_t26hipMemAllocationHandleTypej"><code class="docutils literal notranslate"><span class="pre">hipMemPoolExportToShareableHandle()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv435hipMemPoolImportFromShareableHandleP12hipMemPool_tPv26hipMemAllocationHandleTypej"><code class="docutils literal notranslate"><span class="pre">hipMemPoolImportFromShareableHandle()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipMemPoolExportPointerP23hipMemPoolPtrExportDataPv"><code class="docutils literal notranslate"><span class="pre">hipMemPoolExportPointer()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipMemPoolImportPointerPPv12hipMemPool_tP23hipMemPoolPtrExportData"><code class="docutils literal notranslate"><span class="pre">hipMemPoolImportPointer()</span></code></a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="stream-ordered-memory-allocator">
<span id="stream-ordered-memory-allocator-reference"></span><h1>Stream ordered memory allocator<a class="headerlink" href="#stream-ordered-memory-allocator" title="Link to this heading">#</a></h1>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipMallocAsyncPPv6size_t12hipMemPool_t11hipStream_t">
<span id="_CPPv314hipMallocAsyncPPv6size_t12hipMemPool_t11hipStream_t"></span><span id="_CPPv214hipMallocAsyncPPv6size_t12hipMemPool_t11hipStream_t"></span><span id="hipMallocAsync__voidPP.s.hipMemPool_t.hipStream_t"></span><span class="target" id="group___stream_o_1ga33aeff38cbb30d503cec8989d172e1a8"></span><span class="k"><span class="pre">static</span></span><span class="w"> </span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMallocAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipMallocAsyncPPv6size_t12hipMemPool_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>C++ wrappers for allocations from a memory pool. </p>
<p>This section describes wrappers for stream Ordered allocation from memory pool functions of HIP runtime API.</p>
<p>
This is an alternate C++ calls for <code class="docutils literal notranslate"><span class="pre">hipMallocFromPoolAsync</span></code> made available through function overloading.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>APIs in this section are implemented on Linux, under development on Windows. </p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E14hipMallocAsync10hipError_tPP1T6size_t12hipMemPool_t11hipStream_t">
<span id="_CPPv3I0E14hipMallocAsyncPP1T6size_t12hipMemPool_t11hipStream_t"></span><span id="_CPPv2I0E14hipMallocAsyncPP1T6size_t12hipMemPool_t11hipStream_t"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___stream_o_1ga9411c8f11d47cbd69c7ca29e866aa591"></span><span class="k"><span class="pre">static</span></span><span class="w"> </span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMallocAsync</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E14hipMallocAsync10hipError_tPP1T6size_t12hipMemPool_t11hipStream_t" title="hipMallocAsync::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E14hipMallocAsync10hipError_tPP1T6size_t12hipMemPool_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>C++ wrappers for allocations from a memory pool on the stream. </p>
<p>This is an alternate C++ calls for <code class="docutils literal notranslate"><span class="pre">hipMallocFromPoolAsync</span></code> made available through function overloading.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E14hipMallocAsync10hipError_tPP1T6size_t11hipStream_t">
<span id="_CPPv3I0E14hipMallocAsyncPP1T6size_t11hipStream_t"></span><span id="_CPPv2I0E14hipMallocAsyncPP1T6size_t11hipStream_t"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___stream_o_1ga4ef904c789d99002c682fbc9656e7d7a"></span><span class="k"><span class="pre">static</span></span><span class="w"> </span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMallocAsync</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E14hipMallocAsync10hipError_tPP1T6size_t11hipStream_t" title="hipMallocAsync::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E14hipMallocAsync10hipError_tPP1T6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>C++ wrappers for allocations from a memory pool. </p>
<p>This is an alternate C++ calls for <code class="docutils literal notranslate"><span class="pre">hipMallocFromPoolAsync</span></code> made available through function overloading.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E22hipMallocFromPoolAsync10hipError_tPP1T6size_t12hipMemPool_t11hipStream_t">
<span id="_CPPv3I0E22hipMallocFromPoolAsyncPP1T6size_t12hipMemPool_t11hipStream_t"></span><span id="_CPPv2I0E22hipMallocFromPoolAsyncPP1T6size_t12hipMemPool_t11hipStream_t"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___stream_o_1ga78b307a383328566731df8d7873a1d6a"></span><span class="k"><span class="pre">static</span></span><span class="w"> </span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMallocFromPoolAsync</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E22hipMallocFromPoolAsync10hipError_tPP1T6size_t12hipMemPool_t11hipStream_t" title="hipMallocFromPoolAsync::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E22hipMallocFromPoolAsync10hipError_tPP1T6size_t12hipMemPool_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>C++ wrappers for allocations from a memory pool. </p>
<p>This is an alternate C++ calls for <code class="docutils literal notranslate"><span class="pre">hipMallocFromPoolAsync</span></code> made available through function overloading.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4IDpDpE17hipLaunchKernelEx10hipError_tPK17hipLaunchConfig_tPFvDp10KernelArgsEDpRR6Params">
<span id="_CPPv3IDpDpE17hipLaunchKernelExPK17hipLaunchConfig_tPFvDp10KernelArgsEDpRR6Params"></span><span id="_CPPv2IDpDpE17hipLaunchKernelExPK17hipLaunchConfig_tPFvDp10KernelArgsEDpRR6Params"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">typename</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="sig-name descname"><span class="n"><span class="pre">KernelArgs</span></span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="k"><span class="pre">typename</span></span><span class="w"> </span><span class="p"><span class="pre">...</span></span><span class="sig-name descname"><span class="n"><span class="pre">Params</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___stream_o_1gab99b8d6fca7d769c7063de1d4acbb37e"></span><span class="k"><span class="pre">static</span></span><span class="w"> </span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLaunchKernelEx</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipLaunchConfig_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">config</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">(</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">kernel</span></span><span class="p"><span class="pre">)</span></span><span class="p"><span class="pre">(</span></span><a class="reference internal" href="../execution_control.html#_CPPv4IDpDpE17hipLaunchKernelEx10hipError_tPK17hipLaunchConfig_tPFvDp10KernelArgsEDpRR6Params" title="hipLaunchKernelEx::KernelArgs"><span class="n"><span class="pre">KernelArgs</span></span></a><span class="p"><span class="pre">...</span></span><span class="p"><span class="pre">)</span></span>, <a class="reference internal" href="../execution_control.html#_CPPv4IDpDpE17hipLaunchKernelEx10hipError_tPK17hipLaunchConfig_tPFvDp10KernelArgsEDpRR6Params" title="hipLaunchKernelEx::Params"><span class="n"><span class="pre">Params</span></span></a><span class="p"><span class="pre">&amp;</span></span><span class="p"><span class="pre">&amp;</span></span><span class="p"><span class="pre">...</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">args</span></span><span class="sig-paren">)</span><br /></dt>
<dd><p>Launches a HIP kernel using the specified configuration. </p>
<p>This function dispatches the provided kernel with the given launch configuration and forwards the kernel arguments.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>config</strong> – <strong>[in]</strong> Pointer to the kernel launch configuration structure. </p></li>
<li><p><strong>kernel</strong> – <strong>[in]</strong> Pointer to the device kernel function to be launched. </p></li>
<li><p><strong>args</strong> – <strong>[in]</strong> Variadic list of arguments to be passed to the kernel.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess if the kernel is launched successfully, otherwise an appropriate error code. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipMallocAsyncPPv6size_t11hipStream_t">
<span id="_CPPv314hipMallocAsyncPPv6size_t11hipStream_t"></span><span id="_CPPv214hipMallocAsyncPPv6size_t11hipStream_t"></span><span id="hipMallocAsync__voidPP.s.hipStream_t"></span><span class="target" id="group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMallocAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipMallocAsyncPPv6size_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Allocates memory with stream ordered semantics. </p>
<p>Inserts a memory allocation operation into <code class="docutils literal notranslate"><span class="pre">stream</span></code>. A pointer to the allocated memory is returned immediately in *dptr. The allocation must not be accessed until the allocation operation completes. The allocation comes from the memory pool associated with the stream’s device.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga42543ee2625b87cfd4f6ec29ae11c3d8"><span class="std std-ref">hipFreeAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga4cd76526312084a115c6007d41ba9b96"><span class="std std-ref">hipMemPoolTrimTo</span></a>, <a class="reference internal" href="#group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136"><span class="std std-ref">hipMemPoolGetAttribute</span></a>, <a class="reference internal" href="../device_management.html#group___device_1ga29fd231db3cb31fde8f776d5b073e407"><span class="std std-ref">hipDeviceSetMemPool</span></a>, <a class="reference internal" href="#group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf"><span class="std std-ref">hipMemPoolSetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c"><span class="std std-ref">hipMemPoolSetAccess</span></a>, <a class="reference internal" href="#group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6"><span class="std std-ref">hipMemPoolGetAccess</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The default memory pool of a device contains device memory from that device. </p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Basic stream ordering allows future work submitted into the same stream to use the allocation. Stream query, stream synchronize, and HIP events can be used to guarantee that the allocation operation completes before work submitted in a separate stream runs. </p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>During stream capture, this function results in the creation of an allocation node. In this case, the allocation is owned by the graph instead of the memory pool. The memory pool’s properties are used to set the node’s creation parameters.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dev_ptr</strong> – <strong>[out]</strong> Returned device pointer of memory allocation </p></li>
<li><p><strong>size</strong> – <strong>[in]</strong> Number of bytes to allocate </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> The stream establishing the stream ordering contract and the memory pool to allocate from</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported, hipErrorOutOfMemory</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412hipFreeAsyncPv11hipStream_t">
<span id="_CPPv312hipFreeAsyncPv11hipStream_t"></span><span id="_CPPv212hipFreeAsyncPv11hipStream_t"></span><span id="hipFreeAsync__voidP.hipStream_t"></span><span class="target" id="group___stream_o_1ga42543ee2625b87cfd4f6ec29ae11c3d8"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipFreeAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412hipFreeAsyncPv11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Frees memory with stream ordered semantics. </p>
<p>Inserts a free operation into <code class="docutils literal notranslate"><span class="pre">stream</span></code>. The allocation must not be used after stream execution reaches the free. After this API returns, accessing the memory from any subsequent work launched on the GPU or querying its pointer attributes results in undefined behavior.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a>, <a class="reference internal" href="#group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f"><span class="std std-ref">hipMallocAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga4cd76526312084a115c6007d41ba9b96"><span class="std std-ref">hipMemPoolTrimTo</span></a>, <a class="reference internal" href="#group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136"><span class="std std-ref">hipMemPoolGetAttribute</span></a>, <a class="reference internal" href="../device_management.html#group___device_1ga29fd231db3cb31fde8f776d5b073e407"><span class="std std-ref">hipDeviceSetMemPool</span></a>, <a class="reference internal" href="#group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf"><span class="std std-ref">hipMemPoolSetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c"><span class="std std-ref">hipMemPoolSetAccess</span></a>, <a class="reference internal" href="#group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6"><span class="std std-ref">hipMemPoolGetAccess</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>During stream capture, this function results in the creation of a free node and must therefore be passed the address of a graph allocation.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dev_ptr</strong> – <strong>[in]</strong> Pointer to device memory to free </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> The stream, where the destruciton will occur according to the execution order</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipMemPoolTrimTo12hipMemPool_t6size_t">
<span id="_CPPv316hipMemPoolTrimTo12hipMemPool_t6size_t"></span><span id="_CPPv216hipMemPoolTrimTo12hipMemPool_t6size_t"></span><span id="hipMemPoolTrimTo__hipMemPool_t.s"></span><span class="target" id="group___stream_o_1ga4cd76526312084a115c6007d41ba9b96"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPoolTrimTo</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">min_bytes_to_hold</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipMemPoolTrimTo12hipMemPool_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Releases freed memory back to the OS. </p>
<p>Releases memory back to the OS until the pool contains fewer than <code class="docutils literal notranslate"><span class="pre">min_bytes_to_keep</span></code> reserved bytes, or there is no more memory that the allocator can safely release. The allocator cannot release OS allocations that back outstanding asynchronous allocations. The OS allocations may happen at different granularity from the user allocations.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a>, <a class="reference internal" href="#group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f"><span class="std std-ref">hipMallocAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga42543ee2625b87cfd4f6ec29ae11c3d8"><span class="std std-ref">hipFreeAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136"><span class="std std-ref">hipMemPoolGetAttribute</span></a>, <a class="reference internal" href="../device_management.html#group___device_1ga29fd231db3cb31fde8f776d5b073e407"><span class="std std-ref">hipDeviceSetMemPool</span></a>, <a class="reference internal" href="#group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf"><span class="std std-ref">hipMemPoolSetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c"><span class="std std-ref">hipMemPoolSetAccess</span></a>, <a class="reference internal" href="#group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6"><span class="std std-ref">hipMemPoolGetAccess</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Allocations that have not been freed count as outstanding. </p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Allocations that have been asynchronously freed but whose completion has not been observed on the host (eg. by a synchronize) can count as outstanding.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>mem_pool</strong> – <strong>[in]</strong> The memory pool to trim allocations </p></li>
<li><p><strong>min_bytes_to_hold</strong> – <strong>[in]</strong> If the pool has less than min_bytes_to_hold reserved, then the TrimTo operation is a no-op. Otherwise the memory pool will contain at least min_bytes_to_hold bytes reserved after the operation.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipMemPoolSetAttribute12hipMemPool_t14hipMemPoolAttrPv">
<span id="_CPPv322hipMemPoolSetAttribute12hipMemPool_t14hipMemPoolAttrPv"></span><span id="_CPPv222hipMemPoolSetAttribute12hipMemPool_t14hipMemPoolAttrPv"></span><span id="hipMemPoolSetAttribute__hipMemPool_t.hipMemPoolAttr.voidP"></span><span class="target" id="group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPoolSetAttribute</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="n"><span class="pre">hipMemPoolAttr</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">attr</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">value</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipMemPoolSetAttribute12hipMemPool_t14hipMemPoolAttrPv" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets attributes of a memory pool. </p>
<p>Supported attributes are:<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolAttrReleaseThreshold:</span></code> (value type = cuuint64_t) Amount of reserved memory in bytes to hold onto before trying to release memory back to the OS. When more than the release threshold bytes of memory are held by the memory pool, the allocator will try to release memory back to the OS on the next call to stream, event or context synchronize. (default 0)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolReuseFollowEventDependencies:</span></code> (value type = int) Allow <code class="docutils literal notranslate"><span class="pre">hipMallocAsync</span></code> to use memory asynchronously freed in another stream as long as a stream ordering dependency of the allocating stream on the free action exists. HIP events and null stream interactions can create the required stream ordered dependencies. (default enabled)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolReuseAllowOpportunistic:</span></code> (value type = int) Allow reuse of already completed frees when there is no dependency between the free and allocation. (default enabled)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolReuseAllowInternalDependencies:</span></code> (value type = int) Allow <code class="docutils literal notranslate"><span class="pre">hipMallocAsync</span></code> to insert new stream dependencies in order to establish the stream ordering required to reuse a piece of memory released by <code class="docutils literal notranslate"><span class="pre">hipFreeAsync</span></code> (default enabled).</p></li>
</ul>
</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a>, <a class="reference internal" href="#group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f"><span class="std std-ref">hipMallocAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga42543ee2625b87cfd4f6ec29ae11c3d8"><span class="std std-ref">hipFreeAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136"><span class="std std-ref">hipMemPoolGetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga4cd76526312084a115c6007d41ba9b96"><span class="std std-ref">hipMemPoolTrimTo</span></a>, <a class="reference internal" href="../device_management.html#group___device_1ga29fd231db3cb31fde8f776d5b073e407"><span class="std std-ref">hipDeviceSetMemPool</span></a>, <a class="reference internal" href="#group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c"><span class="std std-ref">hipMemPoolSetAccess</span></a>, <a class="reference internal" href="#group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6"><span class="std std-ref">hipMemPoolGetAccess</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>mem_pool</strong> – <strong>[in]</strong> The memory pool to modify </p></li>
<li><p><strong>attr</strong> – <strong>[in]</strong> The attribute to modify </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Pointer to the value to assign</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipMemPoolGetAttribute12hipMemPool_t14hipMemPoolAttrPv">
<span id="_CPPv322hipMemPoolGetAttribute12hipMemPool_t14hipMemPoolAttrPv"></span><span id="_CPPv222hipMemPoolGetAttribute12hipMemPool_t14hipMemPoolAttrPv"></span><span id="hipMemPoolGetAttribute__hipMemPool_t.hipMemPoolAttr.voidP"></span><span class="target" id="group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPoolGetAttribute</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="n"><span class="pre">hipMemPoolAttr</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">attr</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">value</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipMemPoolGetAttribute12hipMemPool_t14hipMemPoolAttrPv" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets attributes of a memory pool. </p>
<p>Supported attributes are:<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolAttrReleaseThreshold:</span></code> (value type = cuuint64_t) Amount of reserved memory in bytes to hold onto before trying to release memory back to the OS. When more than the release threshold bytes of memory are held by the memory pool, the allocator will try to release memory back to the OS on the next call to stream, event or context synchronize. (default 0)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolReuseFollowEventDependencies:</span></code> (value type = int) Allow <code class="docutils literal notranslate"><span class="pre">hipMallocAsync</span></code> to use memory asynchronously freed in another stream as long as a stream ordering dependency of the allocating stream on the free action exists. HIP events and null stream interactions can create the required stream ordered dependencies. (default enabled)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolReuseAllowOpportunistic:</span></code> (value type = int) Allow reuse of already completed frees when there is no dependency between the free and allocation. (default enabled)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolReuseAllowInternalDependencies:</span></code> (value type = int) Allow <code class="docutils literal notranslate"><span class="pre">hipMallocAsync</span></code> to insert new stream dependencies in order to establish the stream ordering required to reuse a piece of memory released by <code class="docutils literal notranslate"><span class="pre">hipFreeAsync</span></code> (default enabled).</p></li>
</ul>
</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a>, <a class="reference internal" href="#group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f"><span class="std std-ref">hipMallocAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga42543ee2625b87cfd4f6ec29ae11c3d8"><span class="std std-ref">hipFreeAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga4cd76526312084a115c6007d41ba9b96"><span class="std std-ref">hipMemPoolTrimTo</span></a>, <a class="reference internal" href="../device_management.html#group___device_1ga29fd231db3cb31fde8f776d5b073e407"><span class="std std-ref">hipDeviceSetMemPool</span></a>, <a class="reference internal" href="#group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf"><span class="std std-ref">hipMemPoolSetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c"><span class="std std-ref">hipMemPoolSetAccess</span></a>, <a class="reference internal" href="#group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6"><span class="std std-ref">hipMemPoolGetAccess</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>mem_pool</strong> – <strong>[in]</strong> The memory pool to get attributes of </p></li>
<li><p><strong>attr</strong> – <strong>[in]</strong> The attribute to get </p></li>
<li><p><strong>value</strong> – <strong>[in]</strong> Retrieved value</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipMemPoolSetAccess12hipMemPool_tPK16hipMemAccessDesc6size_t">
<span id="_CPPv319hipMemPoolSetAccess12hipMemPool_tPK16hipMemAccessDesc6size_t"></span><span id="_CPPv219hipMemPoolSetAccess12hipMemPool_tPK16hipMemAccessDesc6size_t"></span><span id="hipMemPoolSetAccess__hipMemPool_t.hipMemAccessDescCP.s"></span><span class="target" id="group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPoolSetAccess</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemAccessDesc</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">desc_list</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipMemPoolSetAccess12hipMemPool_tPK16hipMemAccessDesc6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Controls visibility of the specified pool between devices. </p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a>, <a class="reference internal" href="#group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f"><span class="std std-ref">hipMallocAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga42543ee2625b87cfd4f6ec29ae11c3d8"><span class="std std-ref">hipFreeAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136"><span class="std std-ref">hipMemPoolGetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga4cd76526312084a115c6007d41ba9b96"><span class="std std-ref">hipMemPoolTrimTo</span></a>, <a class="reference internal" href="../device_management.html#group___device_1ga29fd231db3cb31fde8f776d5b073e407"><span class="std std-ref">hipDeviceSetMemPool</span></a>, <a class="reference internal" href="#group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf"><span class="std std-ref">hipMemPoolSetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6"><span class="std std-ref">hipMemPoolGetAccess</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>mem_pool</strong> – <strong>[in]</strong> Memory pool for acccess change </p></li>
<li><p><strong>desc_list</strong> – <strong>[in]</strong> Array of access descriptors. Each descriptor instructs the access to enable for a single gpu </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> Number of descriptors in the map array.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipMemPoolGetAccessP17hipMemAccessFlags12hipMemPool_tP14hipMemLocation">
<span id="_CPPv319hipMemPoolGetAccessP17hipMemAccessFlags12hipMemPool_tP14hipMemLocation"></span><span id="_CPPv219hipMemPoolGetAccessP17hipMemAccessFlags12hipMemPool_tP14hipMemLocation"></span><span id="hipMemPoolGetAccess__hipMemAccessFlagsP.hipMemPool_t.hipMemLocationP"></span><span class="target" id="group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPoolGetAccess</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipMemAccessFlags</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">flags</span></span>, <span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="n"><span class="pre">hipMemLocation</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">location</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipMemPoolGetAccessP17hipMemAccessFlags12hipMemPool_tP14hipMemLocation" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns the accessibility of a pool from a device. </p>
<p>Returns the accessibility of the pool’s memory from the specified location.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a>, <a class="reference internal" href="#group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f"><span class="std std-ref">hipMallocAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga42543ee2625b87cfd4f6ec29ae11c3d8"><span class="std std-ref">hipFreeAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136"><span class="std std-ref">hipMemPoolGetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga4cd76526312084a115c6007d41ba9b96"><span class="std std-ref">hipMemPoolTrimTo</span></a>, <a class="reference internal" href="../device_management.html#group___device_1ga29fd231db3cb31fde8f776d5b073e407"><span class="std std-ref">hipDeviceSetMemPool</span></a>, <a class="reference internal" href="#group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf"><span class="std std-ref">hipMemPoolSetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c"><span class="std std-ref">hipMemPoolSetAccess</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>flags</strong> – <strong>[out]</strong> Accessibility of the memory pool from the specified location/device </p></li>
<li><p><strong>mem_pool</strong> – <strong>[in]</strong> Memory pool being queried </p></li>
<li><p><strong>location</strong> – <strong>[in]</strong> Location/device for memory pool access</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipMemPoolCreateP12hipMemPool_tPK15hipMemPoolProps">
<span id="_CPPv316hipMemPoolCreateP12hipMemPool_tPK15hipMemPoolProps"></span><span id="_CPPv216hipMemPoolCreateP12hipMemPool_tPK15hipMemPoolProps"></span><span id="hipMemPoolCreate__hipMemPool_tP.hipMemPoolPropsCP"></span><span class="target" id="group___stream_o_1ga58beb2a7c65ecfaede1029844920f429"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPoolCreate</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemPoolProps</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pool_props</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipMemPoolCreateP12hipMemPool_tPK15hipMemPoolProps" title="Link to this definition">#</a><br /></dt>
<dd><p>Creates a memory pool. </p>
<p>Creates a HIP memory pool and returns the handle in <code class="docutils literal notranslate"><span class="pre">mem_pool</span></code>. The <code class="docutils literal notranslate"><span class="pre">pool_props</span></code> determines the properties of the pool such as the backing device and IPC capabilities.</p>
<p>By default, the memory pool will be accessible from the device it is allocated on.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a>, <a class="reference internal" href="#group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f"><span class="std std-ref">hipMallocAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga42543ee2625b87cfd4f6ec29ae11c3d8"><span class="std std-ref">hipFreeAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136"><span class="std std-ref">hipMemPoolGetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga80b27ec04a2c1884bb8faf882cd9298e"><span class="std std-ref">hipMemPoolDestroy</span></a>, <a class="reference internal" href="#group___stream_o_1ga4cd76526312084a115c6007d41ba9b96"><span class="std std-ref">hipMemPoolTrimTo</span></a>, <a class="reference internal" href="../device_management.html#group___device_1ga29fd231db3cb31fde8f776d5b073e407"><span class="std std-ref">hipDeviceSetMemPool</span></a>, <a class="reference internal" href="#group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf"><span class="std std-ref">hipMemPoolSetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c"><span class="std std-ref">hipMemPoolSetAccess</span></a>, <a class="reference internal" href="#group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6"><span class="std std-ref">hipMemPoolGetAccess</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Specifying hipMemHandleTypeNone creates a memory pool that will not support IPC.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>mem_pool</strong> – <strong>[out]</strong> Contains createed memory pool </p></li>
<li><p><strong>pool_props</strong> – <strong>[in]</strong> Memory pool properties</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipMemPoolDestroy12hipMemPool_t">
<span id="_CPPv317hipMemPoolDestroy12hipMemPool_t"></span><span id="_CPPv217hipMemPoolDestroy12hipMemPool_t"></span><span id="hipMemPoolDestroy__hipMemPool_t"></span><span class="target" id="group___stream_o_1ga80b27ec04a2c1884bb8faf882cd9298e"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPoolDestroy</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mem_pool</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipMemPoolDestroy12hipMemPool_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Destroys the specified memory pool. </p>
<p>If any pointers obtained from this pool haven’t been freed or the pool has free operations that haven’t completed when <code class="docutils literal notranslate"><span class="pre">hipMemPoolDestroy</span></code> is invoked, the function will return immediately and the resources associated with the pool will be released automatically once there are no more outstanding allocations.</p>
<p>Destroying the current mempool of a device sets the default mempool of that device as the current mempool for that device.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"><span class="std std-ref">hipMallocFromPoolAsync</span></a>, <a class="reference internal" href="#group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f"><span class="std std-ref">hipMallocAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga42543ee2625b87cfd4f6ec29ae11c3d8"><span class="std std-ref">hipFreeAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136"><span class="std std-ref">hipMemPoolGetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga58beb2a7c65ecfaede1029844920f429"><span class="std std-ref">hipMemPoolCreate</span></a> <a class="reference internal" href="#group___stream_o_1ga4cd76526312084a115c6007d41ba9b96"><span class="std std-ref">hipMemPoolTrimTo</span></a>, <a class="reference internal" href="../device_management.html#group___device_1ga29fd231db3cb31fde8f776d5b073e407"><span class="std std-ref">hipDeviceSetMemPool</span></a>, <a class="reference internal" href="#group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf"><span class="std std-ref">hipMemPoolSetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c"><span class="std std-ref">hipMemPoolSetAccess</span></a>, <a class="reference internal" href="#group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6"><span class="std std-ref">hipMemPoolGetAccess</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>A device’s default memory pool cannot be destroyed.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>mem_pool</strong> – <strong>[in]</strong> Memory pool for destruction</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipMallocFromPoolAsyncPPv6size_t12hipMemPool_t11hipStream_t">
<span id="_CPPv322hipMallocFromPoolAsyncPPv6size_t12hipMemPool_t11hipStream_t"></span><span id="_CPPv222hipMallocFromPoolAsyncPPv6size_t12hipMemPool_t11hipStream_t"></span><span id="hipMallocFromPoolAsync__voidPP.s.hipMemPool_t.hipStream_t"></span><span class="target" id="group___stream_o_1ga24cab3e20805d8df79a06db1bb0d9938"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMallocFromPoolAsync</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipMallocFromPoolAsyncPPv6size_t12hipMemPool_t11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Allocates memory from a specified pool with stream ordered semantics. </p>
<p>Inserts an allocation operation into <code class="docutils literal notranslate"><span class="pre">stream</span></code>. A pointer to the allocated memory is returned immediately in <code class="docutils literal notranslate"><span class="pre">dev_ptr</span></code>. The allocation must not be accessed until the allocation operation completes. The allocation comes from the specified memory pool.</p>
<p>
Basic stream ordering allows future work submitted into the same stream to use the allocation. Stream query, stream synchronize, and HIP events can be used to guarantee that the allocation operation completes before work submitted in a separate stream runs.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1gab9b9031bb65f8f9e54487ff8b726591f"><span class="std std-ref">hipMallocAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga42543ee2625b87cfd4f6ec29ae11c3d8"><span class="std std-ref">hipFreeAsync</span></a>, <a class="reference internal" href="#group___stream_o_1ga8ac80ed79a85f4e7a9ce33abfbd8f136"><span class="std std-ref">hipMemPoolGetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga58beb2a7c65ecfaede1029844920f429"><span class="std std-ref">hipMemPoolCreate</span></a> <a class="reference internal" href="#group___stream_o_1ga4cd76526312084a115c6007d41ba9b96"><span class="std std-ref">hipMemPoolTrimTo</span></a>, <a class="reference internal" href="../device_management.html#group___device_1ga29fd231db3cb31fde8f776d5b073e407"><span class="std std-ref">hipDeviceSetMemPool</span></a>, <a class="reference internal" href="#group___stream_o_1ga89006d354ee6e0428a432d6f2e76c8bf"><span class="std std-ref">hipMemPoolSetAttribute</span></a>, <a class="reference internal" href="#group___stream_o_1ga6198235d5ae856c21f8507fc218e5c0c"><span class="std std-ref">hipMemPoolSetAccess</span></a>, <a class="reference internal" href="#group___stream_o_1gabefabb7f014dac6b6f646a517c8dd0a6"><span class="std std-ref">hipMemPoolGetAccess</span></a>,</p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The specified memory pool may be from a device different than that of the specified <code class="docutils literal notranslate"><span class="pre">stream</span></code>.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>During stream capture, this function results in the creation of an allocation node. In this case, the allocation is owned by the graph instead of the memory pool. The memory pool’s properties are used to set the node’s creation parameters.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dev_ptr</strong> – <strong>[out]</strong> Returned device pointer </p></li>
<li><p><strong>size</strong> – <strong>[in]</strong> Number of bytes to allocate </p></li>
<li><p><strong>mem_pool</strong> – <strong>[in]</strong> The pool to allocate from </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> The stream establishing the stream ordering semantic</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported, hipErrorOutOfMemory</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv433hipMemPoolExportToShareableHandlePv12hipMemPool_t26hipMemAllocationHandleTypej">
<span id="_CPPv333hipMemPoolExportToShareableHandlePv12hipMemPool_t26hipMemAllocationHandleTypej"></span><span id="_CPPv233hipMemPoolExportToShareableHandlePv12hipMemPool_t26hipMemAllocationHandleTypej"></span><span id="hipMemPoolExportToShareableHandle__voidP.hipMemPool_t.hipMemAllocationHandleType.unsigned-i"></span><span class="target" id="group___stream_o_1ga929b2b894b051dec2d5df7fbad157a1f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPoolExportToShareableHandle</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">shared_handle</span></span>, <span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="n"><span class="pre">hipMemAllocationHandleType</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">handle_type</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv433hipMemPoolExportToShareableHandlePv12hipMemPool_t26hipMemAllocationHandleTypej" title="Link to this definition">#</a><br /></dt>
<dd><p>Exports a memory pool to the requested handle type. </p>
<p>Given an IPC capable mempool, create an OS handle to share the pool with another process. A recipient process can convert the shareable handle into a mempool with <code class="docutils literal notranslate"><span class="pre">hipMemPoolImportFromShareableHandle</span></code>. Individual pointers can then be shared with the <code class="docutils literal notranslate"><span class="pre">hipMemPoolExportPointer</span></code> and <code class="docutils literal notranslate"><span class="pre">hipMemPoolImportPointer</span></code> APIs. The implementation of what the shareable handle is and how it can be transferred is defined by the requested handle type.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga2008b5a98ecec44ecebb3618692aa894"><span class="std std-ref">hipMemPoolImportFromShareableHandle</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>To create an IPC capable mempool, create a mempool with a <code class="docutils literal notranslate"><span class="pre">hipMemAllocationHandleType</span></code> other than <code class="docutils literal notranslate"><span class="pre">hipMemHandleTypeNone</span></code>.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>shared_handle</strong> – <strong>[out]</strong> Pointer to the location in which to store the requested handle </p></li>
<li><p><strong>mem_pool</strong> – <strong>[in]</strong> Pool to export </p></li>
<li><p><strong>handle_type</strong> – <strong>[in]</strong> The type of handle to create </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Must be 0</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorOutOfMemory</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv435hipMemPoolImportFromShareableHandleP12hipMemPool_tPv26hipMemAllocationHandleTypej">
<span id="_CPPv335hipMemPoolImportFromShareableHandleP12hipMemPool_tPv26hipMemAllocationHandleTypej"></span><span id="_CPPv235hipMemPoolImportFromShareableHandleP12hipMemPool_tPv26hipMemAllocationHandleTypej"></span><span id="hipMemPoolImportFromShareableHandle__hipMemPool_tP.voidP.hipMemAllocationHandleType.unsigned-i"></span><span class="target" id="group___stream_o_1ga2008b5a98ecec44ecebb3618692aa894"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPoolImportFromShareableHandle</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">shared_handle</span></span>, <span class="n"><span class="pre">hipMemAllocationHandleType</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">handle_type</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv435hipMemPoolImportFromShareableHandleP12hipMemPool_tPv26hipMemAllocationHandleTypej" title="Link to this definition">#</a><br /></dt>
<dd><p>Imports a memory pool from a shared handle. </p>
<p>Specific allocations can be imported from the imported pool with <code class="docutils literal notranslate"><span class="pre">hipMemPoolImportPointer</span></code>.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga929b2b894b051dec2d5df7fbad157a1f"><span class="std std-ref">hipMemPoolExportToShareableHandle</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Imported memory pools do not support creating new allocations. As such imported memory pools may not be used in <code class="docutils literal notranslate"><span class="pre">hipDeviceSetMemPool</span></code> or <code class="docutils literal notranslate"><span class="pre">hipMallocFromPoolAsync</span></code> calls.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>mem_pool</strong> – <strong>[out]</strong> Returned memory pool </p></li>
<li><p><strong>shared_handle</strong> – <strong>[in]</strong> OS handle of the pool to open </p></li>
<li><p><strong>handle_type</strong> – <strong>[in]</strong> The type of handle being imported </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Must be 0</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorOutOfMemory</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipMemPoolExportPointerP23hipMemPoolPtrExportDataPv">
<span id="_CPPv323hipMemPoolExportPointerP23hipMemPoolPtrExportDataPv"></span><span id="_CPPv223hipMemPoolExportPointerP23hipMemPoolPtrExportDataPv"></span><span id="hipMemPoolExportPointer__hipMemPoolPtrExportDataP.voidP"></span><span class="target" id="group___stream_o_1gaafb76a90d8609a1736e9b1944ef09090"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPoolExportPointer</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipMemPoolPtrExportData</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">export_data</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipMemPoolExportPointerP23hipMemPoolPtrExportDataPv" title="Link to this definition">#</a><br /></dt>
<dd><p>Export data to share a memory pool allocation between processes. </p>
<p>Constructs <code class="docutils literal notranslate"><span class="pre">export_data</span></code> for sharing a specific allocation from an already shared memory pool. The recipient process can import the allocation with the <code class="docutils literal notranslate"><span class="pre">hipMemPoolImportPointer</span></code> api. The data is not a handle and may be shared through any IPC mechanism.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1ga1fdd9ab4e5d5bac53d96d053697ddc33"><span class="std std-ref">hipMemPoolImportPointer</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>export_data</strong> – <strong>[out]</strong> Returned export data </p></li>
<li><p><strong>dev_ptr</strong> – <strong>[in]</strong> Pointer to memory being exported</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorOutOfMemory</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipMemPoolImportPointerPPv12hipMemPool_tP23hipMemPoolPtrExportData">
<span id="_CPPv323hipMemPoolImportPointerPPv12hipMemPool_tP23hipMemPoolPtrExportData"></span><span id="_CPPv223hipMemPoolImportPointerPPv12hipMemPool_tP23hipMemPoolPtrExportData"></span><span id="hipMemPoolImportPointer__voidPP.hipMemPool_t.hipMemPoolPtrExportDataP"></span><span class="target" id="group___stream_o_1ga1fdd9ab4e5d5bac53d96d053697ddc33"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPoolImportPointer</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">hipMemPool_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mem_pool</span></span>, <span class="n"><span class="pre">hipMemPoolPtrExportData</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">export_data</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipMemPoolImportPointerPPv12hipMemPool_tP23hipMemPoolPtrExportData" title="Link to this definition">#</a><br /></dt>
<dd><p>Import a memory pool allocation from another process. </p>
<p>Returns in <code class="docutils literal notranslate"><span class="pre">dev_ptr</span></code> a pointer to the imported memory. The imported memory must not be accessed before the allocation operation completes in the exporting process. The imported memory must be freed from all importing processes before being freed in the exporting process. The pointer may be freed with <code class="docutils literal notranslate"><span class="pre">hipFree</span></code> or <code class="docutils literal notranslate"><span class="pre">hipFreeAsync</span></code>. If <code class="docutils literal notranslate"><span class="pre">hipFreeAsync</span></code> is used, the free must be completed on the importing process before the free operation on the exporting process.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___stream_o_1gaafb76a90d8609a1736e9b1944ef09090"><span class="std std-ref">hipMemPoolExportPointer</span></a></p>
</div>
</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The <code class="docutils literal notranslate"><span class="pre">hipFreeAsync</span></code> api may be used in the exporting process before the <code class="docutils literal notranslate"><span class="pre">hipFreeAsync</span></code> operation completes in its stream as long as the <code class="docutils literal notranslate"><span class="pre">hipFreeAsync</span></code> in the exporting process specifies a stream with a stream dependency on the importing process’s <code class="docutils literal notranslate"><span class="pre">hipFreeAsync</span></code>.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is marked as Beta. While this feature is complete, it can change and might have outstanding issues.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dev_ptr</strong> – <strong>[out]</strong> Pointer to imported memory </p></li>
<li><p><strong>mem_pool</strong> – <strong>[in]</strong> Memory pool from which to import a pointer </p></li>
<li><p><strong>export_data</strong> – <strong>[in]</strong> Data specifying the memory to import</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotInitialized, hipErrorOutOfMemory</p>
</dd>
</dl>
</dd></dl>

</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="external_resource_interoperability.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">External resource interoperability</p>
      </div>
    </a>
    <a class="right-next"
       href="unified_memory_reference.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Managed memory</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMallocAsyncPPv6size_t12hipMemPool_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E14hipMallocAsync10hipError_tPP1T6size_t12hipMemPool_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E14hipMallocAsync10hipError_tPP1T6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E22hipMallocFromPoolAsync10hipError_tPP1T6size_t12hipMemPool_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMallocFromPoolAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4IDpDpE17hipLaunchKernelEx10hipError_tPK17hipLaunchConfig_tPFvDp10KernelArgsEDpRR6Params"><code class="docutils literal notranslate"><span class="pre">hipLaunchKernelEx()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipMallocAsyncPPv6size_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipFreeAsyncPv11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipFreeAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemPoolTrimTo12hipMemPool_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemPoolTrimTo()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipMemPoolSetAttribute12hipMemPool_t14hipMemPoolAttrPv"><code class="docutils literal notranslate"><span class="pre">hipMemPoolSetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipMemPoolGetAttribute12hipMemPool_t14hipMemPoolAttrPv"><code class="docutils literal notranslate"><span class="pre">hipMemPoolGetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemPoolSetAccess12hipMemPool_tPK16hipMemAccessDesc6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemPoolSetAccess()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemPoolGetAccessP17hipMemAccessFlags12hipMemPool_tP14hipMemLocation"><code class="docutils literal notranslate"><span class="pre">hipMemPoolGetAccess()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMemPoolCreateP12hipMemPool_tPK15hipMemPoolProps"><code class="docutils literal notranslate"><span class="pre">hipMemPoolCreate()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipMemPoolDestroy12hipMemPool_t"><code class="docutils literal notranslate"><span class="pre">hipMemPoolDestroy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipMallocFromPoolAsyncPPv6size_t12hipMemPool_t11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMallocFromPoolAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv433hipMemPoolExportToShareableHandlePv12hipMemPool_t26hipMemAllocationHandleTypej"><code class="docutils literal notranslate"><span class="pre">hipMemPoolExportToShareableHandle()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv435hipMemPoolImportFromShareableHandleP12hipMemPool_tPv26hipMemAllocationHandleTypej"><code class="docutils literal notranslate"><span class="pre">hipMemPoolImportFromShareableHandle()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipMemPoolExportPointerP23hipMemPoolPtrExportDataPv"><code class="docutils literal notranslate"><span class="pre">hipMemPoolExportPointer()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipMemPoolImportPointerPPv12hipMemPool_tP23hipMemPoolPtrExportData"><code class="docutils literal notranslate"><span class="pre">hipMemPoolImportPointer()</span></code></a></li>
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
  <script src="../../../../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b"></script>
<script src="../../../../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b"></script>

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
    <img id="rdc-watermark" src="../../../../_static/images/alpha-watermark.svg" alt="DRAFT watermark"/>
</div> -->
  </body>
</html>
