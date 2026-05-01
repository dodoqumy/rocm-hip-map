---
title: "Texture management (deprecated) &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/memory_management/texture_management_deprecated.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:04.222003+00:00
content_hash: "0e2d9a68361ba48e"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="The deprecated texture management reference page." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, deprecated texture management" name="keywords" />

    <title>Texture management (deprecated) &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/hip_runtime_api/modules/memory_management/texture_management_deprecated';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../../genindex.html" />
    <link rel="search" title="Search" href="../../../../search.html" />
    <link rel="next" title="Surface object" href="surface_object.html" />
    <link rel="prev" title="Texture management" href="texture_management.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/hip_runtime_api/modules/memory_management/texture_management_deprecated.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l4"><a class="reference internal" href="stream_ordered_memory_allocator.html">Stream ordered memory allocator</a></li>
<li class="toctree-l4"><a class="reference internal" href="unified_memory_reference.html">Managed memory</a></li>
<li class="toctree-l4"><a class="reference internal" href="virtual_memory_reference.html">Virtual memory management</a></li>
<li class="toctree-l4"><a class="reference internal" href="texture_management.html">Texture management</a></li>
<li class="toctree-l4 current active"><a class="current reference internal" href="#">Texture management (deprecated)</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">Texture...</li>
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
    <h1>Texture management (deprecated)</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipBindTextureToMipmappedArrayPK16textureReference25hipMipmappedArray_const_tPK20hipChannelFormatDesc"><code class="docutils literal notranslate"><span class="pre">hipBindTextureToMipmappedArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipGetTextureReferencePPK16textureReferencePKv"><code class="docutils literal notranslate"><span class="pre">hipGetTextureReference()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipTexRefGetBorderColorPfPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetBorderColor()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipTexRefGetArrayP10hipArray_tPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipTexRefSetAddressModeP16textureReferencei21hipTextureAddressMode"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetAddressMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipTexRefSetArrayP16textureReference16hipArray_const_tj"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipTexRefSetFilterModeP16textureReference20hipTextureFilterMode"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetFilterMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipTexRefSetFlagsP16textureReferencej"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipTexRefSetFormatP16textureReference15hipArray_Formati"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetFormat()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipBindTextureP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t"><code class="docutils literal notranslate"><span class="pre">hipBindTexture()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipBindTexture2DP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipBindTexture2D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipBindTextureToArrayPK16textureReference16hipArray_const_tPK20hipChannelFormatDesc"><code class="docutils literal notranslate"><span class="pre">hipBindTextureToArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipGetTextureAlignmentOffsetP6size_tPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipGetTextureAlignmentOffset()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipUnbindTexturePK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipUnbindTexture()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipTexRefGetAddressP14hipDeviceptr_tPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetAddress()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipTexRefGetAddressModeP21hipTextureAddressModePK16textureReferencei"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetAddressMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipTexRefGetFilterModeP20hipTextureFilterModePK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetFilterMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipTexRefGetFlagsPjPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipTexRefGetFormatP15hipArray_FormatPiPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetFormat()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipTexRefGetMaxAnisotropyPiPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetMaxAnisotropy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipTexRefGetMipmapFilterModeP20hipTextureFilterModePK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetMipmapFilterMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipTexRefGetMipmapLevelBiasPfPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetMipmapLevelBias()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipTexRefGetMipmapLevelClampPfPfPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetMipmapLevelClamp()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipTexRefGetMipMappedArrayP19hipMipmappedArray_tPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetMipMappedArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipTexRefSetAddressP6size_tP16textureReference14hipDeviceptr_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetAddress()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipTexRefSetAddress2DP16textureReferencePK20HIP_ARRAY_DESCRIPTOR14hipDeviceptr_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetAddress2D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipTexRefSetMaxAnisotropyP16textureReferencej"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetMaxAnisotropy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipTexRefSetBorderColorP16textureReferencePf"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetBorderColor()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipTexRefSetMipmapFilterModeP16textureReference20hipTextureFilterMode"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetMipmapFilterMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipTexRefSetMipmapLevelBiasP16textureReferencef"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetMipmapLevelBias()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipTexRefSetMipmapLevelClampP16textureReferenceff"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetMipmapLevelClamp()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipTexRefSetMipmappedArrayP16textureReferenceP17hipMipmappedArrayj"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetMipmappedArray()</span></code></a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="texture-management-deprecated">
<span id="texture-management-deprecated-reference"></span><h1>Texture management (deprecated)<a class="headerlink" href="#texture-management-deprecated" title="Link to this heading">#</a></h1>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv430hipBindTextureToMipmappedArrayPK16textureReference25hipMipmappedArray_const_tPK20hipChannelFormatDesc">
<span id="_CPPv330hipBindTextureToMipmappedArrayPK16textureReference25hipMipmappedArray_const_tPK20hipChannelFormatDesc"></span><span id="_CPPv230hipBindTextureToMipmappedArrayPK16textureReference25hipMipmappedArray_const_tPK20hipChannelFormatDesc"></span><span id="hipBindTextureToMipmappedArray__textureReferenceCP.hipMipmappedArray_const_t.hipChannelFormatDescCP"></span><span class="target" id="group___texture_d_1ga1c182e356b3796fc11a6064685a4f29c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipBindTextureToMipmappedArray</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">tex</span></span>, <span class="n"><span class="pre">hipMipmappedArray_const_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">mipmappedArray</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipChannelFormatDesc</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">desc</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv430hipBindTextureToMipmappedArrayPK16textureReference25hipMipmappedArray_const_tPK20hipChannelFormatDesc" title="Link to this definition">#</a><br /></dt>
<dd><p>Binds a mipmapped array to a texture [Deprecated]. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>tex</strong> – <strong>[in]</strong> pointer to the texture reference to bind </p></li>
<li><p><strong>mipmappedArray</strong> – <strong>[in]</strong> memory mipmapped array on the device </p></li>
<li><p><strong>desc</strong> – <strong>[in]</strong> opointer to the channel format</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipGetTextureReferencePPK16textureReferencePKv">
<span id="_CPPv322hipGetTextureReferencePPK16textureReferencePKv"></span><span id="_CPPv222hipGetTextureReferencePPK16textureReferencePKv"></span><span id="hipGetTextureReference__textureReferenceCPP.voidCP"></span><span class="target" id="group___texture_d_1gaec97b7e9649423af9198a13ac73dcdd4"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGetTextureReference</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texref</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">symbol</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipGetTextureReferencePPK16textureReferencePKv" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the texture reference related with the symbol [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>texref</strong> – <strong>[out]</strong> texture reference </p></li>
<li><p><strong>symbol</strong> – <strong>[in]</strong> pointer to the symbol related with the texture for the reference</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipTexRefGetBorderColorPfPK16textureReference">
<span id="_CPPv323hipTexRefGetBorderColorPfPK16textureReference"></span><span id="_CPPv223hipTexRefGetBorderColorPfPK16textureReference"></span><span id="hipTexRefGetBorderColor__floatP.textureReferenceCP"></span><span class="target" id="group___texture_d_1ga68ae56351534358e74ef7d9e24efeab9"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefGetBorderColor</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pBorderColor</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipTexRefGetBorderColorPfPK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the border color used by a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pBorderColor</strong> – <strong>[out]</strong> Returned Type and Value of RGBA color. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> Texture reference.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipTexRefGetArrayP10hipArray_tPK16textureReference">
<span id="_CPPv317hipTexRefGetArrayP10hipArray_tPK16textureReference"></span><span id="_CPPv217hipTexRefGetArrayP10hipArray_tPK16textureReference"></span><span id="hipTexRefGetArray__hipArray_tP.textureReferenceCP"></span><span class="target" id="group___texture_d_1ga9041baa58925270638c3035c65f5ce77"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefGetArray</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pArray</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipTexRefGetArrayP10hipArray_tPK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the array bound to a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pArray</strong> – <strong>[in]</strong> Returned array. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> texture reference.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipTexRefSetAddressModeP16textureReferencei21hipTextureAddressMode">
<span id="_CPPv323hipTexRefSetAddressModeP16textureReferencei21hipTextureAddressMode"></span><span id="_CPPv223hipTexRefSetAddressModeP16textureReferencei21hipTextureAddressMode"></span><span id="hipTexRefSetAddressMode__textureReferenceP.i.hipTextureAddressMode"></span><span class="target" id="group___texture_d_1ga9c70e94c59c441a3903411256213a963"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetAddressMode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dim</span></span>, <span class="k"><span class="pre">enum</span></span><span class="w"> </span><span class="n"><span class="pre">hipTextureAddressMode</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">am</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipTexRefSetAddressModeP16textureReferencei21hipTextureAddressMode" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets address mode for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>texRef</strong> – <strong>[in]</strong> texture reference. </p></li>
<li><p><strong>dim</strong> – <strong>[in]</strong> Dimension of the texture. </p></li>
<li><p><strong>am</strong> – <strong>[in]</strong> Value of the texture address mode.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipTexRefSetArrayP16textureReference16hipArray_const_tj">
<span id="_CPPv317hipTexRefSetArrayP16textureReference16hipArray_const_tj"></span><span id="_CPPv217hipTexRefSetArrayP16textureReference16hipArray_const_tj"></span><span id="hipTexRefSetArray__textureReferenceP.hipArray_const_t.unsigned-i"></span><span class="target" id="group___texture_d_1gad3c3a2a7797c96b9f53b4eab7b27b0c6"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetArray</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">tex</span></span>, <span class="n"><span class="pre">hipArray_const_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">array</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipTexRefSetArrayP16textureReference16hipArray_const_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Binds an array as a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>tex</strong> – <strong>[in]</strong> Pointer texture reference. </p></li>
<li><p><strong>array</strong> – <strong>[in]</strong> Array to bind. </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Flags should be set as HIP_TRSA_OVERRIDE_FORMAT, as a valid value.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipTexRefSetFilterModeP16textureReference20hipTextureFilterMode">
<span id="_CPPv322hipTexRefSetFilterModeP16textureReference20hipTextureFilterMode"></span><span id="_CPPv222hipTexRefSetFilterModeP16textureReference20hipTextureFilterMode"></span><span id="hipTexRefSetFilterMode__textureReferenceP.hipTextureFilterMode"></span><span class="target" id="group___texture_d_1ga3f05947e0dc31a7861ee27002b9aa6a8"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetFilterMode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="k"><span class="pre">enum</span></span><span class="w"> </span><span class="n"><span class="pre">hipTextureFilterMode</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">fm</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipTexRefSetFilterModeP16textureReference20hipTextureFilterMode" title="Link to this definition">#</a><br /></dt>
<dd><p>Set filter mode for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer texture reference. </p></li>
<li><p><strong>fm</strong> – <strong>[in]</strong> Value of texture filter mode.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipTexRefSetFlagsP16textureReferencej">
<span id="_CPPv317hipTexRefSetFlagsP16textureReferencej"></span><span id="_CPPv217hipTexRefSetFlagsP16textureReferencej"></span><span id="hipTexRefSetFlags__textureReferenceP.unsigned-i"></span><span class="target" id="group___texture_d_1ga939238805ce9e7dca127927147058ada"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetFlags</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">Flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipTexRefSetFlagsP16textureReferencej" title="Link to this definition">#</a><br /></dt>
<dd><p>Set flags for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer texture reference. </p></li>
<li><p><strong>Flags</strong> – <strong>[in]</strong> Value of flags.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipTexRefSetFormatP16textureReference15hipArray_Formati">
<span id="_CPPv318hipTexRefSetFormatP16textureReference15hipArray_Formati"></span><span id="_CPPv218hipTexRefSetFormatP16textureReference15hipArray_Formati"></span><span id="hipTexRefSetFormat__textureReferenceP.hipArray_Format.i"></span><span class="target" id="group___texture_d_1ga6d207019c4165bcee452508d7451ca41"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetFormat</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="n"><span class="pre">hipArray_Format</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">fmt</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">NumPackedComponents</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipTexRefSetFormatP16textureReference15hipArray_Formati" title="Link to this definition">#</a><br /></dt>
<dd><p>Set format for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer texture reference. </p></li>
<li><p><strong>fmt</strong> – <strong>[in]</strong> Value of format. </p></li>
<li><p><strong>NumPackedComponents</strong> – <strong>[in]</strong> Number of components per array.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv414hipBindTextureP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t">
<span id="_CPPv314hipBindTextureP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t"></span><span id="_CPPv214hipBindTextureP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t"></span><span id="hipBindTexture__sP.textureReferenceCP.voidCP.hipChannelFormatDescCP.s"></span><span class="target" id="group___texture_d_1ga5e5e058031ab88c41cf662fd29f491ac"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipBindTexture</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">tex</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">devPtr</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipChannelFormatDesc</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">desc</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv414hipBindTextureP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Binds a memory area to a texture [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – <strong>[in]</strong> Offset in bytes. </p></li>
<li><p><strong>tex</strong> – <strong>[in]</strong> Texture to bind. </p></li>
<li><p><strong>devPtr</strong> – <strong>[in]</strong> Pointer of memory on the device. </p></li>
<li><p><strong>desc</strong> – <strong>[in]</strong> Pointer of channel format descriptor. </p></li>
<li><p><strong>size</strong> – <strong>[in]</strong> Size of memory in bites.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipBindTexture2DP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t6size_t6size_t">
<span id="_CPPv316hipBindTexture2DP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t6size_t6size_t"></span><span id="_CPPv216hipBindTexture2DP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t6size_t6size_t"></span><span id="hipBindTexture2D__sP.textureReferenceCP.voidCP.hipChannelFormatDescCP.s.s.s"></span><span class="target" id="group___texture_d_1ga5a2db1f1c95fa9d31ba5240a3a88d4cd"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipBindTexture2D</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">tex</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">devPtr</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipChannelFormatDesc</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">desc</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">width</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">height</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">pitch</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipBindTexture2DP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t6size_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Binds a 2D memory area to a texture [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – <strong>[in]</strong> Offset in bytes. </p></li>
<li><p><strong>tex</strong> – <strong>[in]</strong> Texture to bind. </p></li>
<li><p><strong>devPtr</strong> – <strong>[in]</strong> Pointer of 2D memory area on the device. </p></li>
<li><p><strong>desc</strong> – <strong>[in]</strong> Pointer of channel format descriptor. </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width in texel units. </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Height in texel units. </p></li>
<li><p><strong>pitch</strong> – <strong>[in]</strong> Pitch in bytes.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipBindTextureToArrayPK16textureReference16hipArray_const_tPK20hipChannelFormatDesc">
<span id="_CPPv321hipBindTextureToArrayPK16textureReference16hipArray_const_tPK20hipChannelFormatDesc"></span><span id="_CPPv221hipBindTextureToArrayPK16textureReference16hipArray_const_tPK20hipChannelFormatDesc"></span><span id="hipBindTextureToArray__textureReferenceCP.hipArray_const_t.hipChannelFormatDescCP"></span><span class="target" id="group___texture_d_1gaddd135091fa603870fd34d04b0a59c58"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipBindTextureToArray</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">tex</span></span>, <span class="n"><span class="pre">hipArray_const_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">array</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">hipChannelFormatDesc</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">desc</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipBindTextureToArrayPK16textureReference16hipArray_const_tPK20hipChannelFormatDesc" title="Link to this definition">#</a><br /></dt>
<dd><p>Binds a memory area to a texture [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>tex</strong> – <strong>[in]</strong> Pointer of texture reference. </p></li>
<li><p><strong>array</strong> – <strong>[in]</strong> Array to bind. </p></li>
<li><p><strong>desc</strong> – <strong>[in]</strong> Pointer of channel format descriptor.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv428hipGetTextureAlignmentOffsetP6size_tPK16textureReference">
<span id="_CPPv328hipGetTextureAlignmentOffsetP6size_tPK16textureReference"></span><span id="_CPPv228hipGetTextureAlignmentOffsetP6size_tPK16textureReference"></span><span id="hipGetTextureAlignmentOffset__sP.textureReferenceCP"></span><span class="target" id="group___texture_d_1ga53edad6565b3244b8713f6aee42d9c9f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipGetTextureAlignmentOffset</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">offset</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texref</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv428hipGetTextureAlignmentOffsetP6size_tPK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Get the offset of the alignment in a texture [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – <strong>[in]</strong> Offset in bytes. </p></li>
<li><p><strong>texref</strong> – <strong>[in]</strong> Pointer of texture reference.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipUnbindTexturePK16textureReference">
<span id="_CPPv316hipUnbindTexturePK16textureReference"></span><span id="_CPPv216hipUnbindTexturePK16textureReference"></span><span id="hipUnbindTexture__textureReferenceCP"></span><span class="target" id="group___texture_d_1ga6082a76377229793500a21caf249794f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipUnbindTexture</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">tex</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipUnbindTexturePK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Unbinds a texture [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>tex</strong> – <strong>[in]</strong> Texture to unbind.</p>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipTexRefGetAddressP14hipDeviceptr_tPK16textureReference">
<span id="_CPPv319hipTexRefGetAddressP14hipDeviceptr_tPK16textureReference"></span><span id="_CPPv219hipTexRefGetAddressP14hipDeviceptr_tPK16textureReference"></span><span id="hipTexRefGetAddress__hipDeviceptr_tP.textureReferenceCP"></span><span class="target" id="group___texture_d_1ga8f58bdd1cbbeee60fba3ec4bfcd74515"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefGetAddress</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipTexRefGetAddressP14hipDeviceptr_tPK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the address for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dev_ptr</strong> – <strong>[out]</strong> Pointer of device address. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipTexRefGetAddressModeP21hipTextureAddressModePK16textureReferencei">
<span id="_CPPv323hipTexRefGetAddressModeP21hipTextureAddressModePK16textureReferencei"></span><span id="_CPPv223hipTexRefGetAddressModeP21hipTextureAddressModePK16textureReferencei"></span><span id="hipTexRefGetAddressMode__hipTextureAddressModeP.textureReferenceCP.i"></span><span class="target" id="group___texture_d_1ga28e2b18b9fa55bab5983e88ad62a4c9f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefGetAddressMode</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">enum</span></span><span class="w"> </span><span class="n"><span class="pre">hipTextureAddressMode</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pam</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dim</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipTexRefGetAddressModeP21hipTextureAddressModePK16textureReferencei" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the address mode for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pam</strong> – <strong>[out]</strong> Pointer of address mode. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference. </p></li>
<li><p><strong>dim</strong> – <strong>[in]</strong> Dimension.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipTexRefGetFilterModeP20hipTextureFilterModePK16textureReference">
<span id="_CPPv322hipTexRefGetFilterModeP20hipTextureFilterModePK16textureReference"></span><span id="_CPPv222hipTexRefGetFilterModeP20hipTextureFilterModePK16textureReference"></span><span id="hipTexRefGetFilterMode__hipTextureFilterModeP.textureReferenceCP"></span><span class="target" id="group___texture_d_1ga07d91c8480153c3b38ca6d02a03980b8"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefGetFilterMode</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">enum</span></span><span class="w"> </span><span class="n"><span class="pre">hipTextureFilterMode</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pfm</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipTexRefGetFilterModeP20hipTextureFilterModePK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets filter mode for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pfm</strong> – <strong>[out]</strong> Pointer of filter mode. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417hipTexRefGetFlagsPjPK16textureReference">
<span id="_CPPv317hipTexRefGetFlagsPjPK16textureReference"></span><span id="_CPPv217hipTexRefGetFlagsPjPK16textureReference"></span><span id="hipTexRefGetFlags__unsigned-iP.textureReferenceCP"></span><span class="target" id="group___texture_d_1ga29eca0fa3db8bc4cdcceac1aebf47c9a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefGetFlags</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pFlags</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417hipTexRefGetFlagsPjPK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets flags for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pFlags</strong> – <strong>[out]</strong> Pointer of flags. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv418hipTexRefGetFormatP15hipArray_FormatPiPK16textureReference">
<span id="_CPPv318hipTexRefGetFormatP15hipArray_FormatPiPK16textureReference"></span><span id="_CPPv218hipTexRefGetFormatP15hipArray_FormatPiPK16textureReference"></span><span id="hipTexRefGetFormat__hipArray_FormatP.iP.textureReferenceCP"></span><span class="target" id="group___texture_d_1gaf7221d495964939f7dd1eea0b133efcc"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefGetFormat</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipArray_Format</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pFormat</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pNumChannels</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv418hipTexRefGetFormatP15hipArray_FormatPiPK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets texture format for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pFormat</strong> – <strong>[out]</strong> Pointer of the format. </p></li>
<li><p><strong>pNumChannels</strong> – <strong>[out]</strong> Pointer of number of channels. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425hipTexRefGetMaxAnisotropyPiPK16textureReference">
<span id="_CPPv325hipTexRefGetMaxAnisotropyPiPK16textureReference"></span><span id="_CPPv225hipTexRefGetMaxAnisotropyPiPK16textureReference"></span><span id="hipTexRefGetMaxAnisotropy__iP.textureReferenceCP"></span><span class="target" id="group___texture_d_1ga5b8f516d89303a5ade97dd885f373bf6"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefGetMaxAnisotropy</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pmaxAnsio</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425hipTexRefGetMaxAnisotropyPiPK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the maximum anisotropy for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pmaxAnsio</strong> – <strong>[out]</strong> Pointer of the maximum anisotropy. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv428hipTexRefGetMipmapFilterModeP20hipTextureFilterModePK16textureReference">
<span id="_CPPv328hipTexRefGetMipmapFilterModeP20hipTextureFilterModePK16textureReference"></span><span id="_CPPv228hipTexRefGetMipmapFilterModeP20hipTextureFilterModePK16textureReference"></span><span id="hipTexRefGetMipmapFilterMode__hipTextureFilterModeP.textureReferenceCP"></span><span class="target" id="group___texture_d_1ga471218ad91920133054b83d6273bee14"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefGetMipmapFilterMode</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">enum</span></span><span class="w"> </span><span class="n"><span class="pre">hipTextureFilterMode</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pfm</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv428hipTexRefGetMipmapFilterModeP20hipTextureFilterModePK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the mipmap filter mode for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pfm</strong> – <strong>[out]</strong> Pointer of the mipmap filter mode. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv427hipTexRefGetMipmapLevelBiasPfPK16textureReference">
<span id="_CPPv327hipTexRefGetMipmapLevelBiasPfPK16textureReference"></span><span id="_CPPv227hipTexRefGetMipmapLevelBiasPfPK16textureReference"></span><span id="hipTexRefGetMipmapLevelBias__floatP.textureReferenceCP"></span><span class="target" id="group___texture_d_1gadd1c0a0ec8edc555f477642546e0bd3a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefGetMipmapLevelBias</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pbias</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv427hipTexRefGetMipmapLevelBiasPfPK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the mipmap level bias for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pbias</strong> – <strong>[out]</strong> Pointer of the mipmap level bias. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv428hipTexRefGetMipmapLevelClampPfPfPK16textureReference">
<span id="_CPPv328hipTexRefGetMipmapLevelClampPfPfPK16textureReference"></span><span id="_CPPv228hipTexRefGetMipmapLevelClampPfPfPK16textureReference"></span><span id="hipTexRefGetMipmapLevelClamp__floatP.floatP.textureReferenceCP"></span><span class="target" id="group___texture_d_1ga21cb9dcdc8829ab01f40ee0a3b59ddb0"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefGetMipmapLevelClamp</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pminMipmapLevelClamp</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pmaxMipmapLevelClamp</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv428hipTexRefGetMipmapLevelClampPfPfPK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the minimum and maximum mipmap level clamps for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pminMipmapLevelClamp</strong> – <strong>[out]</strong> Pointer of the minimum mipmap level clamp. </p></li>
<li><p><strong>pmaxMipmapLevelClamp</strong> – <strong>[out]</strong> Pointer of the maximum mipmap level clamp. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426hipTexRefGetMipMappedArrayP19hipMipmappedArray_tPK16textureReference">
<span id="_CPPv326hipTexRefGetMipMappedArrayP19hipMipmappedArray_tPK16textureReference"></span><span id="_CPPv226hipTexRefGetMipMappedArrayP19hipMipmappedArray_tPK16textureReference"></span><span id="hipTexRefGetMipMappedArray__hipMipmappedArray_tP.textureReferenceCP"></span><span class="target" id="group___texture_d_1gaa0d2ebbb5c3b7e1e71a4b449936da801"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefGetMipMappedArray</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipMipmappedArray_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pArray</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426hipTexRefGetMipMappedArrayP19hipMipmappedArray_tPK16textureReference" title="Link to this definition">#</a><br /></dt>
<dd><p>Gets the mipmapped array bound to a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>pArray</strong> – <strong>[out]</strong> Pointer of the mipmapped array. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipTexRefSetAddressP6size_tP16textureReference14hipDeviceptr_t6size_t">
<span id="_CPPv319hipTexRefSetAddressP6size_tP16textureReference14hipDeviceptr_t6size_t"></span><span id="_CPPv219hipTexRefSetAddressP6size_tP16textureReference14hipDeviceptr_t6size_t"></span><span id="hipTexRefSetAddress__sP.textureReferenceP.hipDeviceptr_t.s"></span><span class="target" id="group___texture_d_1ga39e9dac1975f1007f173c00454ceaf87"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetAddress</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">ByteOffset</span></span>, <span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">bytes</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipTexRefSetAddressP6size_tP16textureReference14hipDeviceptr_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets an bound address for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ByteOffset</strong> – <strong>[out]</strong> Pointer of the offset in bytes. </p></li>
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference. </p></li>
<li><p><strong>dptr</strong> – <strong>[in]</strong> Pointer of device address to bind. </p></li>
<li><p><strong>bytes</strong> – <strong>[in]</strong> Size in bytes.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv421hipTexRefSetAddress2DP16textureReferencePK20HIP_ARRAY_DESCRIPTOR14hipDeviceptr_t6size_t">
<span id="_CPPv321hipTexRefSetAddress2DP16textureReferencePK20HIP_ARRAY_DESCRIPTOR14hipDeviceptr_t6size_t"></span><span id="_CPPv221hipTexRefSetAddress2DP16textureReferencePK20HIP_ARRAY_DESCRIPTOR14hipDeviceptr_t6size_t"></span><span id="hipTexRefSetAddress2D__textureReferenceP.HIP_ARRAY_DESCRIPTORCP.hipDeviceptr_t.s"></span><span class="target" id="group___texture_d_1gaf24188ec011b0cb0cd4194f8ef60808c"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetAddress2D</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">HIP_ARRAY_DESCRIPTOR</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">desc</span></span>, <span class="n"><span class="pre">hipDeviceptr_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">dptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">Pitch</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv421hipTexRefSetAddress2DP16textureReferencePK20HIP_ARRAY_DESCRIPTOR14hipDeviceptr_t6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Set a bind an address as a 2D texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference. </p></li>
<li><p><strong>desc</strong> – <strong>[in]</strong> Pointer of array descriptor. </p></li>
<li><p><strong>dptr</strong> – <strong>[in]</strong> Pointer of device address to bind. </p></li>
<li><p><strong>Pitch</strong> – <strong>[in]</strong> Pitch in bytes.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv425hipTexRefSetMaxAnisotropyP16textureReferencej">
<span id="_CPPv325hipTexRefSetMaxAnisotropyP16textureReferencej"></span><span id="_CPPv225hipTexRefSetMaxAnisotropyP16textureReferencej"></span><span id="hipTexRefSetMaxAnisotropy__textureReferenceP.unsigned-i"></span><span class="target" id="group___texture_d_1gabeb3f31407bb518ccda9b0183bc6c03f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetMaxAnisotropy</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">maxAniso</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv425hipTexRefSetMaxAnisotropyP16textureReferencej" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets the maximum anisotropy for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference. </p></li>
<li><p><strong>maxAniso</strong> – <strong>[out]</strong> Value of the maximum anisotropy.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipTexRefSetBorderColorP16textureReferencePf">
<span id="_CPPv323hipTexRefSetBorderColorP16textureReferencePf"></span><span id="_CPPv223hipTexRefSetBorderColorP16textureReferencePf"></span><span id="hipTexRefSetBorderColor__textureReferenceP.floatP"></span><span class="target" id="group___texture_d_1gad021c81371c1596e16cf28390799e8f5"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetBorderColor</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">pBorderColor</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipTexRefSetBorderColorP16textureReferencePf" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets border color for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference. </p></li>
<li><p><strong>pBorderColor</strong> – <strong>[in]</strong> Pointer of border color.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv428hipTexRefSetMipmapFilterModeP16textureReference20hipTextureFilterMode">
<span id="_CPPv328hipTexRefSetMipmapFilterModeP16textureReference20hipTextureFilterMode"></span><span id="_CPPv228hipTexRefSetMipmapFilterModeP16textureReference20hipTextureFilterMode"></span><span id="hipTexRefSetMipmapFilterMode__textureReferenceP.hipTextureFilterMode"></span><span class="target" id="group___texture_d_1gaf3b8771e6dac8d8c0284a546e550c24e"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetMipmapFilterMode</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="k"><span class="pre">enum</span></span><span class="w"> </span><span class="n"><span class="pre">hipTextureFilterMode</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">fm</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv428hipTexRefSetMipmapFilterModeP16textureReference20hipTextureFilterMode" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets mipmap filter mode for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference. </p></li>
<li><p><strong>fm</strong> – <strong>[in]</strong> Value of filter mode.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv427hipTexRefSetMipmapLevelBiasP16textureReferencef">
<span id="_CPPv327hipTexRefSetMipmapLevelBiasP16textureReferencef"></span><span id="_CPPv227hipTexRefSetMipmapLevelBiasP16textureReferencef"></span><span id="hipTexRefSetMipmapLevelBias__textureReferenceP.float"></span><span class="target" id="group___texture_d_1gad81d7049385e4031a4b2f1167e880950"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetMipmapLevelBias</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">bias</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv427hipTexRefSetMipmapLevelBiasP16textureReferencef" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets mipmap level bias for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference. </p></li>
<li><p><strong>bias</strong> – <strong>[in]</strong> Value of mipmap bias.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv428hipTexRefSetMipmapLevelClampP16textureReferenceff">
<span id="_CPPv328hipTexRefSetMipmapLevelClampP16textureReferenceff"></span><span id="_CPPv228hipTexRefSetMipmapLevelClampP16textureReferenceff"></span><span id="hipTexRefSetMipmapLevelClamp__textureReferenceP.float.float"></span><span class="target" id="group___texture_d_1gac5b5f689eacd90c7a638c7e3c955d722"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetMipmapLevelClamp</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">minMipMapLevelClamp</span></span>, <span class="kt"><span class="pre">float</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">maxMipMapLevelClamp</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv428hipTexRefSetMipmapLevelClampP16textureReferenceff" title="Link to this definition">#</a><br /></dt>
<dd><p>Sets mipmap level clamp for a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference. </p></li>
<li><p><strong>minMipMapLevelClamp</strong> – <strong>[in]</strong> Value of minimum mipmap level clamp. </p></li>
<li><p><strong>maxMipMapLevelClamp</strong> – <strong>[in]</strong> Value of maximum mipmap level clamp.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue, hipErrorNotSupported</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426hipTexRefSetMipmappedArrayP16textureReferenceP17hipMipmappedArrayj">
<span id="_CPPv326hipTexRefSetMipmappedArrayP16textureReferenceP17hipMipmappedArrayj"></span><span id="_CPPv226hipTexRefSetMipmappedArrayP16textureReferenceP17hipMipmappedArrayj"></span><span id="hipTexRefSetMipmappedArray__textureReferenceP.hipMipmappedArrayP.unsigned-i"></span><span class="target" id="group___texture_d_1ga43f9441244f526a4552852040a28e0ef"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipTexRefSetMipmappedArray</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">textureReference</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">texRef</span></span>, <span class="k"><span class="pre">struct</span></span><span class="w"> </span><span class="n"><span class="pre">hipMipmappedArray</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">mipmappedArray</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">Flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426hipTexRefSetMipmappedArrayP16textureReferenceP17hipMipmappedArrayj" title="Link to this definition">#</a><br /></dt>
<dd><p>Binds mipmapped array to a texture reference [Deprecated]. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>texRef</strong> – <strong>[in]</strong> Pointer of texture reference to bind. </p></li>
<li><p><strong>mipmappedArray</strong> – <strong>[in]</strong> Pointer of mipmapped array to bind. </p></li>
<li><p><strong>Flags</strong> – <strong>[in]</strong> Flags should be set as HIP_TRSA_OVERRIDE_FORMAT, as a valid value.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp">
<span class="target" id="group___texture_d_1gad98dbffaac39bf4aa58d153e25a2bf2b"></span><span class="sig-name descname"><span class="pre">template&lt;class</span> <span class="pre">T,</span> <span class="pre">int</span> <span class="pre">dim,</span> <span class="pre">enum</span> <span class="pre">hipTextureReadMode</span> <span class="pre">readMode&gt;</span>&#160; <span class="pre">HIP_DEPRECATED</span> <span class="pre">(HIP_DEPRECATED_MSG)</span> <span class="pre">static</span> <span class="pre">inline</span> <span class="pre">hipError_t</span> <span class="pre">hipBindTexture(size_t</span> <span class="pre">*offset</span></span></dt>
<dd><p>Binds a memory area to a texture [Deprecated]. </p>
<p>Unbinds a texture [Depreacated].</p>
<p>Binds a mipmapped array to a texture [Deprecated].</p>
<p>Binds an array to a texture [Deprecated].</p>
<p>Binds a 2D memory area to a texture [Deprecated].</p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated.</p>
</div>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is deprecated. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>offset</strong> – <strong>[in]</strong> Offset in bytes. </p></li>
<li><p><strong>tex</strong> – <strong>[in]</strong> Texture to bind. </p></li>
<li><p><strong>devPtr</strong> – <strong>[in]</strong> Pointer of memory on the device. </p></li>
<li><p><strong>size</strong> – <strong>[in]</strong> Size of memory in bites.</p></li>
<li><p><strong>offset</strong> – <strong>[in]</strong> Offset in bytes. </p></li>
<li><p><strong>tex</strong> – <strong>[in]</strong> Texture to bind. </p></li>
<li><p><strong>devPtr</strong> – <strong>[in]</strong> Pointer of 2D memory area on the device. </p></li>
<li><p><strong>desc</strong> – <strong>[in]</strong> Texture channel format. </p></li>
<li><p><strong>width</strong> – <strong>[in]</strong> Width in texel units. </p></li>
<li><p><strong>height</strong> – <strong>[in]</strong> Height in texel units. </p></li>
<li><p><strong>pitch</strong> – <strong>[in]</strong> Pitch in bytes.</p></li>
<li><p><strong>tex</strong> – <strong>[in]</strong> Texture to bind. </p></li>
<li><p><strong>array</strong> – <strong>[in]</strong> Array of memory on the device.</p></li>
<li><p><strong>tex</strong> – <strong>[in]</strong> Texture to bind. </p></li>
<li><p><strong>array</strong> – <strong>[in]</strong> Array of memory on the device. </p></li>
<li><p><strong>desc</strong> – <strong>[in]</strong> Texture channel format.</p></li>
<li><p><strong>tex</strong> – <strong>[in]</strong> Texture to bind. </p></li>
<li><p><strong>mipmappedArray</strong> – <strong>[in]</strong> Mipmapped Array of memory on the device.</p></li>
<li><p><strong>tex</strong> – <strong>[in]</strong> Texture to bind. </p></li>
<li><p><strong>mipmappedArray</strong> – <strong>[in]</strong> Mipmapped Array of memory on the device. </p></li>
<li><p><strong>desc</strong> – <strong>[in]</strong> Texture channel format.</p></li>
<li><p><strong>tex</strong> – <strong>[in]</strong> Texture to unbind.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="texture_management.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Texture management</p>
      </div>
    </a>
    <a class="right-next"
       href="surface_object.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Surface object</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv430hipBindTextureToMipmappedArrayPK16textureReference25hipMipmappedArray_const_tPK20hipChannelFormatDesc"><code class="docutils literal notranslate"><span class="pre">hipBindTextureToMipmappedArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipGetTextureReferencePPK16textureReferencePKv"><code class="docutils literal notranslate"><span class="pre">hipGetTextureReference()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipTexRefGetBorderColorPfPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetBorderColor()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipTexRefGetArrayP10hipArray_tPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipTexRefSetAddressModeP16textureReferencei21hipTextureAddressMode"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetAddressMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipTexRefSetArrayP16textureReference16hipArray_const_tj"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipTexRefSetFilterModeP16textureReference20hipTextureFilterMode"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetFilterMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipTexRefSetFlagsP16textureReferencej"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipTexRefSetFormatP16textureReference15hipArray_Formati"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetFormat()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv414hipBindTextureP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t"><code class="docutils literal notranslate"><span class="pre">hipBindTexture()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipBindTexture2DP6size_tPK16textureReferencePKvPK20hipChannelFormatDesc6size_t6size_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipBindTexture2D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipBindTextureToArrayPK16textureReference16hipArray_const_tPK20hipChannelFormatDesc"><code class="docutils literal notranslate"><span class="pre">hipBindTextureToArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipGetTextureAlignmentOffsetP6size_tPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipGetTextureAlignmentOffset()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipUnbindTexturePK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipUnbindTexture()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipTexRefGetAddressP14hipDeviceptr_tPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetAddress()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipTexRefGetAddressModeP21hipTextureAddressModePK16textureReferencei"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetAddressMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipTexRefGetFilterModeP20hipTextureFilterModePK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetFilterMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417hipTexRefGetFlagsPjPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetFlags()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv418hipTexRefGetFormatP15hipArray_FormatPiPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetFormat()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipTexRefGetMaxAnisotropyPiPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetMaxAnisotropy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipTexRefGetMipmapFilterModeP20hipTextureFilterModePK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetMipmapFilterMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipTexRefGetMipmapLevelBiasPfPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetMipmapLevelBias()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipTexRefGetMipmapLevelClampPfPfPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetMipmapLevelClamp()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipTexRefGetMipMappedArrayP19hipMipmappedArray_tPK16textureReference"><code class="docutils literal notranslate"><span class="pre">hipTexRefGetMipMappedArray()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipTexRefSetAddressP6size_tP16textureReference14hipDeviceptr_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetAddress()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv421hipTexRefSetAddress2DP16textureReferencePK20HIP_ARRAY_DESCRIPTOR14hipDeviceptr_t6size_t"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetAddress2D()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv425hipTexRefSetMaxAnisotropyP16textureReferencej"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetMaxAnisotropy()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipTexRefSetBorderColorP16textureReferencePf"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetBorderColor()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipTexRefSetMipmapFilterModeP16textureReference20hipTextureFilterMode"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetMipmapFilterMode()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv427hipTexRefSetMipmapLevelBiasP16textureReferencef"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetMipmapLevelBias()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv428hipTexRefSetMipmapLevelClampP16textureReferenceff"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetMipmapLevelClamp()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipTexRefSetMipmappedArrayP16textureReferenceP17hipMipmappedArrayj"><code class="docutils literal notranslate"><span class="pre">hipTexRefSetMipmappedArray()</span></code></a></li>
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
