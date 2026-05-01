---
title: "Managed memory &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:57.811816+00:00
content_hash: "ebbc4273f95877f0"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="The managed memory reference page." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, unified memory, unified, memory, UM, APU" name="keywords" />

    <title>Managed memory &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/hip_runtime_api/modules/memory_management/unified_memory_reference';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../../genindex.html" />
    <link rel="search" title="Search" href="../../../../search.html" />
    <link rel="next" title="Virtual memory management" href="virtual_memory_reference.html" />
    <link rel="prev" title="Stream ordered memory allocator" href="stream_ordered_memory_allocator.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l4 current active"><a class="current reference internal" href="#">Managed memory</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">Managed memory</li>
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
    <h1>Managed memory</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMallocManagedPPv6size_tj"><code class="docutils literal notranslate"><span class="pre">hipMallocManaged()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemPrefetchAsyncPKv6size_ti11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemPrefetchAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipMemPrefetchAsync_v2PKv6size_t14hipMemLocationj11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemPrefetchAsync_v2()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipMemAdvisePKv6size_t15hipMemoryAdvisei"><code class="docutils literal notranslate"><span class="pre">hipMemAdvise()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipMemAdvise_v2PKv6size_t15hipMemoryAdvise14hipMemLocation"><code class="docutils literal notranslate"><span class="pre">hipMemAdvise_v2()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipMemRangeGetAttributePv6size_t20hipMemRangeAttributePKv6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemRangeGetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipMemRangeGetAttributesPPvP6size_tP20hipMemRangeAttribute6size_tPKv6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemRangeGetAttributes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipStreamAttachMemAsync11hipStream_tPv6size_tj"><code class="docutils literal notranslate"><span class="pre">hipStreamAttachMemAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E16hipMallocManaged10hipError_tPP1T6size_tj"><code class="docutils literal notranslate"><span class="pre">hipMallocManaged()</span></code></a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="managed-memory">
<span id="unified-memory-reference"></span><h1>Managed memory<a class="headerlink" href="#managed-memory" title="Link to this heading">#</a></h1>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416hipMallocManagedPPv6size_tj">
<span id="_CPPv316hipMallocManagedPPv6size_tj"></span><span id="_CPPv216hipMallocManagedPPv6size_tj"></span><span id="hipMallocManaged__voidPP.s.unsigned-i"></span><span class="target" id="group___memory_m_1gaadf4780d920bb6f5cc755880740ef7dc"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMallocManaged</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416hipMallocManagedPPv6size_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Allocates memory that will be automatically managed by HIP. </p>
<p>This API is used for managed memory, allows data be shared and accessible to both CPU and GPU using a single pointer.</p>
<p>The API returns the allocation pointer, managed by HMM, can be used further to execute kernels on device and fetch data between the host and device as needed.</p>
<p>If HMM is not supported, the function behaves the same as <code class="docutils literal notranslate"><span class="pre">hipMallocHost</span></code> .</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>It is recommend to do the capability check before call this API.</p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dev_ptr</strong> – <strong>[out]</strong> - pointer to allocated device memory </p></li>
<li><p><strong>size</strong> – <strong>[in]</strong> - requested allocation size in bytes, it should be granularity of 4KB </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> - must be either hipMemAttachGlobal or hipMemAttachHost (defaults to hipMemAttachGlobal)</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorMemoryAllocation, hipErrorNotSupported, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv419hipMemPrefetchAsyncPKv6size_ti11hipStream_t">
<span id="_CPPv319hipMemPrefetchAsyncPKv6size_ti11hipStream_t"></span><span id="_CPPv219hipMemPrefetchAsyncPKv6size_ti11hipStream_t"></span><span id="hipMemPrefetchAsync__voidCP.s.i.hipStream_t"></span><span class="target" id="group___memory_m_1ga08ca029eec15591f680c7b19b0fb1d1a"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPrefetchAsync</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">device</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv419hipMemPrefetchAsyncPKv6size_ti11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Prefetches memory to the specified destination device using HIP. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dev_ptr</strong> – <strong>[in]</strong> pointer to be prefetched </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> size in bytes for prefetching </p></li>
<li><p><strong>device</strong> – <strong>[in]</strong> destination device to prefetch to </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> stream to enqueue prefetch operation</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv422hipMemPrefetchAsync_v2PKv6size_t14hipMemLocationj11hipStream_t">
<span id="_CPPv322hipMemPrefetchAsync_v2PKv6size_t14hipMemLocationj11hipStream_t"></span><span id="_CPPv222hipMemPrefetchAsync_v2PKv6size_t14hipMemLocationj11hipStream_t"></span><span id="hipMemPrefetchAsync_v2__voidCP.s.hipMemLocation.unsigned-i.hipStream_t"></span><span class="target" id="group___memory_m_1ga224d823750aa1d3076cb6d03643501e1"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemPrefetchAsync_v2</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">hipMemLocation</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">location</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv422hipMemPrefetchAsync_v2PKv6size_t14hipMemLocationj11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Prefetches memory to the specified destination device using HIP. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dev_ptr</strong> – <strong>[in]</strong> pointer to be prefetched </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> size in bytes for prefetching </p></li>
<li><p><strong>location</strong> – <strong>[in]</strong> destination location to prefetch to </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> flags for future use, must be zero now. </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> stream to enqueue prefetch operation</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv412hipMemAdvisePKv6size_t15hipMemoryAdvisei">
<span id="_CPPv312hipMemAdvisePKv6size_t15hipMemoryAdvisei"></span><span id="_CPPv212hipMemAdvisePKv6size_t15hipMemoryAdvisei"></span><span id="hipMemAdvise__voidCP.s.hipMemoryAdvise.i"></span><span class="target" id="group___memory_m_1ga5c8a3ea8a8702747588082ed39ea51bf"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemAdvise</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">hipMemoryAdvise</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">advice</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">device</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv412hipMemAdvisePKv6size_t15hipMemoryAdvisei" title="Link to this definition">#</a><br /></dt>
<dd><p>Advise about the usage of a given memory range to HIP. </p>
<p>
This HIP API advises about the usage to be applied on unified memory allocation in the range starting from the pointer address devPtr, with the size of count bytes. The memory range must refer to managed memory allocated via the API hipMallocManaged, and the range will be handled with proper round down and round up respectively in the driver to be aligned to CPU page size, the same way as corresponding CUDA API behaves in CUDA version 8.0 and afterwards.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dev_ptr</strong> – <strong>[in]</strong> pointer to memory to set the advice for </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> size in bytes of the memory range, it should be CPU page size alligned. </p></li>
<li><p><strong>advice</strong> – <strong>[in]</strong> advice to be applied for the specified memory range </p></li>
<li><p><strong>device</strong> – <strong>[in]</strong> device to apply the advice for</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415hipMemAdvise_v2PKv6size_t15hipMemoryAdvise14hipMemLocation">
<span id="_CPPv315hipMemAdvise_v2PKv6size_t15hipMemoryAdvise14hipMemLocation"></span><span id="_CPPv215hipMemAdvise_v2PKv6size_t15hipMemoryAdvise14hipMemLocation"></span><span id="hipMemAdvise_v2__voidCP.s.hipMemoryAdvise.hipMemLocation"></span><span class="target" id="group___memory_m_1gafbe7148d8448ebf132ac2ea84d889b4e"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemAdvise_v2</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span>, <span class="n"><span class="pre">hipMemoryAdvise</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">advice</span></span>, <span class="n"><span class="pre">hipMemLocation</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">location</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415hipMemAdvise_v2PKv6size_t15hipMemoryAdvise14hipMemLocation" title="Link to this definition">#</a><br /></dt>
<dd><p>Advise about the usage of a given memory range to HIP. </p>
<p>
This HIP API advises about the usage to be applied on unified memory allocation in the range starting from the pointer address devPtr, with the size of count bytes. The memory range must refer to managed memory allocated via the API hipMallocManaged, and the range will be handled with proper round down and round up respectively in the driver to be aligned to CPU page size, the same way as corresponding CUDA API behaves in CUDA version 8.0 and afterwards.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dev_ptr</strong> – <strong>[in]</strong> pointer to memory to set the advice for </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> size in bytes of the memory range, it should be CPU page size alligned. </p></li>
<li><p><strong>advice</strong> – <strong>[in]</strong> advice to be applied for the specified memory range </p></li>
<li><p><strong>location</strong> – <strong>[in]</strong> location to apply the advice for</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipMemRangeGetAttributePv6size_t20hipMemRangeAttributePKv6size_t">
<span id="_CPPv323hipMemRangeGetAttributePv6size_t20hipMemRangeAttributePKv6size_t"></span><span id="_CPPv223hipMemRangeGetAttributePv6size_t20hipMemRangeAttributePKv6size_t"></span><span id="hipMemRangeGetAttribute__voidP.s.hipMemRangeAttribute.voidCP.s"></span><span class="target" id="group___memory_m_1gaad1ddb8bc3e1905a5f116dbcdc842ea3"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemRangeGetAttribute</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">data_size</span></span>, <span class="n"><span class="pre">hipMemRangeAttribute</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">attribute</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipMemRangeGetAttributePv6size_t20hipMemRangeAttributePKv6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Query an attribute of a given memory range in HIP. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>data</strong> – <strong>[inout]</strong> a pointer to a memory location where the result of each attribute query will be written to </p></li>
<li><p><strong>data_size</strong> – <strong>[in]</strong> the size of data </p></li>
<li><p><strong>attribute</strong> – <strong>[in]</strong> the attribute to query </p></li>
<li><p><strong>dev_ptr</strong> – <strong>[in]</strong> start of the range to query </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> size of the range to query</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv424hipMemRangeGetAttributesPPvP6size_tP20hipMemRangeAttribute6size_tPKv6size_t">
<span id="_CPPv324hipMemRangeGetAttributesPPvP6size_tP20hipMemRangeAttribute6size_tPKv6size_t"></span><span id="_CPPv224hipMemRangeGetAttributesPPvP6size_tP20hipMemRangeAttribute6size_tPKv6size_t"></span><span id="hipMemRangeGetAttributes__voidPP.sP.hipMemRangeAttributeP.s.voidCP.s"></span><span class="target" id="group___memory_m_1ga4a37d3eac6147dcaa3d0cd3de3268121"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMemRangeGetAttributes</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">data</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">data_sizes</span></span>, <span class="n"><span class="pre">hipMemRangeAttribute</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">attributes</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">num_attributes</span></span>, <span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">count</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv424hipMemRangeGetAttributesPPvP6size_tP20hipMemRangeAttribute6size_tPKv6size_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Query attributes of a given memory range in HIP. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This API is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>data</strong> – <strong>[inout]</strong> a two-dimensional array containing pointers to memory locations where the result of each attribute query will be written to </p></li>
<li><p><strong>data_sizes</strong> – <strong>[in]</strong> an array, containing the sizes of each result </p></li>
<li><p><strong>attributes</strong> – <strong>[in]</strong> the attribute to query </p></li>
<li><p><strong>num_attributes</strong> – <strong>[in]</strong> an array of attributes to query (numAttributes and the number of attributes in this array should match) </p></li>
<li><p><strong>dev_ptr</strong> – <strong>[in]</strong> start of the range to query </p></li>
<li><p><strong>count</strong> – <strong>[in]</strong> size of the range to query</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv423hipStreamAttachMemAsync11hipStream_tPv6size_tj">
<span id="_CPPv323hipStreamAttachMemAsync11hipStream_tPv6size_tj"></span><span id="_CPPv223hipStreamAttachMemAsync11hipStream_tPv6size_tj"></span><span id="hipStreamAttachMemAsync__hipStream_t.voidP.s.unsigned-i"></span><span class="target" id="group___memory_m_1gabd2ab38956e78d8a5d5a0320f5ef5027"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipStreamAttachMemAsync</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">dev_ptr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">length</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv423hipStreamAttachMemAsync11hipStream_tPv6size_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Attach memory to a stream asynchronously in HIP. </p>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>This API is under development. Currently it is a no-operation (NOP) function on AMD GPUs and returns hipSuccess. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>stream</strong> – <strong>[in]</strong> - stream in which to enqueue the attach operation </p></li>
<li><p><strong>dev_ptr</strong> – <strong>[in]</strong> - pointer to memory (must be a pointer to managed memory or to a valid host-accessible region of system-allocated memory) </p></li>
<li><p><strong>length</strong> – <strong>[in]</strong> - length of memory (defaults to zero) </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> - must be one of hipMemAttachGlobal, hipMemAttachHost or hipMemAttachSingle (defaults to hipMemAttachSingle)</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorInvalidValue</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E16hipMallocManaged10hipError_tPP1T6size_tj">
<span id="_CPPv3I0E16hipMallocManagedPP1T6size_tj"></span><span id="_CPPv2I0E16hipMallocManagedPP1T6size_tj"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___memory_m_1gaf31a5d9d1f6e6c5051fd958edd40a8fc"></span><span class="k"><span class="pre">static</span></span><span class="w"> </span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipMallocManaged</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E16hipMallocManaged10hipError_tPP1T6size_tj" title="hipMallocManaged::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">devPtr</span></span>, <span class="n"><span class="pre">size_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">size</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="n"><span class="pre">hipMemAttachGlobal</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E16hipMallocManaged10hipError_tPP1T6size_tj" title="Link to this definition">#</a><br /></dt>
<dd><p>: C++ wrapper for hipMallocManaged </p>
<p>Provide an override to automatically typecast the pointer type from void**, and also provide a default for the flags.</p>
<p><strong>HIP_DISABLE_CPP_FUNCTIONS</strong> macro can be defined to suppress these wrappers. It is useful for applications which need to obtain decltypes of HIP runtime APIs.</p>
<p><div class="admonition seealso">
<p class="admonition-title">See also</p>
<p><a class="reference internal" href="#group___memory_m_1gaadf4780d920bb6f5cc755880740ef7dc"><span class="std std-ref">hipMallocManaged</span></a></p>
</div>
</p>
</dd></dl>

</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="stream_ordered_memory_allocator.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Stream ordered memory allocator</p>
      </div>
    </a>
    <a class="right-next"
       href="virtual_memory_reference.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Virtual memory management</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416hipMallocManagedPPv6size_tj"><code class="docutils literal notranslate"><span class="pre">hipMallocManaged()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv419hipMemPrefetchAsyncPKv6size_ti11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemPrefetchAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv422hipMemPrefetchAsync_v2PKv6size_t14hipMemLocationj11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipMemPrefetchAsync_v2()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv412hipMemAdvisePKv6size_t15hipMemoryAdvisei"><code class="docutils literal notranslate"><span class="pre">hipMemAdvise()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415hipMemAdvise_v2PKv6size_t15hipMemoryAdvise14hipMemLocation"><code class="docutils literal notranslate"><span class="pre">hipMemAdvise_v2()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipMemRangeGetAttributePv6size_t20hipMemRangeAttributePKv6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemRangeGetAttribute()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv424hipMemRangeGetAttributesPPvP6size_tP20hipMemRangeAttribute6size_tPKv6size_t"><code class="docutils literal notranslate"><span class="pre">hipMemRangeGetAttributes()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv423hipStreamAttachMemAsync11hipStream_tPv6size_tj"><code class="docutils literal notranslate"><span class="pre">hipStreamAttachMemAsync()</span></code></a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E16hipMallocManaged10hipError_tPP1T6size_tj"><code class="docutils literal notranslate"><span class="pre">hipMallocManaged()</span></code></a></li>
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
