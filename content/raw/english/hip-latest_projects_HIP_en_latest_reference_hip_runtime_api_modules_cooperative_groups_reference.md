---
title: "Cooperative groups &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/cooperative_groups_reference.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:07:17.345435+00:00
content_hash: "0b81cb316d8900d0"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="This chapter lists types and device API wrappers related to the Cooperative Group feature. Programmers can directly use these API features in their kernels." name="description" />
<meta content="AMD, ROCm, HIP, cooperative groups" name="keywords" />

    <title>Cooperative groups &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>window.MathJax = {"options": {"processHtmlClass": "tex2jax_process|mathjax_process|math|output_area"}}</script>
    <script defer="defer" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/hip_runtime_api/modules/cooperative_groups_reference';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Global defines, enums, structs and files" href="../global_defines_enums_structs_files.html" />
    <link rel="prev" title="OpenGL interoperability" href="opengl_interoperability.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/hip_runtime_api/modules/cooperative_groups_reference.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l3"><a class="reference internal" href="graph_management.html">Graph management</a></li>
<li class="toctree-l3"><a class="reference internal" href="graphics_interoperability.html">Graphics interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="opengl_interoperability.html">OpenGL interoperability</a></li>
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Cooperative groups</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">Cooperative groups</li>
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
    <h1>Cooperative groups</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cooperative-kernel-launches">Cooperative kernel launches</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv432hipModuleLaunchCooperativeKernel13hipFunction_tjjjjjjj11hipStream_tPPv"><code class="docutils literal notranslate"><span class="pre">hipModuleLaunchCooperativeKernel()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv443hipModuleLaunchCooperativeKernelMultiDeviceP23hipFunctionLaunchParamsjj"><code class="docutils literal notranslate"><span class="pre">hipModuleLaunchCooperativeKernelMultiDevice()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipLaunchCooperativeKernelPKv4dim34dim3PPvj11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipLaunchCooperativeKernel()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv437hipLaunchCooperativeKernelMultiDeviceP15hipLaunchParamsij"><code class="docutils literal notranslate"><span class="pre">hipLaunchCooperativeKernelMultiDevice()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E26hipLaunchCooperativeKernel10hipError_t1T4dim34dim3PPvj11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipLaunchCooperativeKernel()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E37hipLaunchCooperativeKernelMultiDevice10hipError_tP15hipLaunchParamsjj"><code class="docutils literal notranslate"><span class="pre">hipLaunchCooperativeKernelMultiDevice()</span></code></a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cooperative-groups-classes">Cooperative groups classes</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N18cooperative_groups12thread_groupE"><code class="docutils literal notranslate"><span class="pre">thread_group</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N18cooperative_groups12thread_blockE"><code class="docutils literal notranslate"><span class="pre">thread_block</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N18cooperative_groups10grid_groupE"><code class="docutils literal notranslate"><span class="pre">grid_group</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N18cooperative_groups16multi_grid_groupE"><code class="docutils literal notranslate"><span class="pre">multi_grid_group</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_j0EN18cooperative_groups17thread_block_tileE"><code class="docutils literal notranslate"><span class="pre">thread_block_tile</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4NK18cooperative_groups17thread_block_tile11thread_rankEv"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::thread_rank()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N18cooperative_groups17thread_block_tile4syncEv"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::sync()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4NK18cooperative_groups17thread_block_tile15meta_group_rankEv"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::meta_group_rank()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4NK18cooperative_groups17thread_block_tile15meta_group_sizeEv"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::meta_group_size()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile4shflE1T1Ti"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::shfl()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9shfl_downE1T1Tj"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::shfl_down()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile7shfl_upE1T1Tj"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::shfl_up()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile8shfl_xorE1T1Tj"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::shfl_xor()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4NK18cooperative_groups17thread_block_tile6ballotEi"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::ballot()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4NK18cooperative_groups17thread_block_tile3anyEi"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::any()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4NK18cooperative_groups17thread_block_tile3allEi"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::all()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9match_anyEy1T"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::match_any()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9match_allEy1TRi"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::match_all()</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N18cooperative_groups15coalesced_groupE"><code class="docutils literal notranslate"><span class="pre">coalesced_group</span></code></a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cooperative-groups-construct-functions">Cooperative groups construct functions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415this_multi_gridv"><code class="docutils literal notranslate"><span class="pre">this_multi_grid()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49this_gridv"><code class="docutils literal notranslate"><span class="pre">this_grid()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417this_thread_blockv"><code class="docutils literal notranslate"><span class="pre">this_thread_block()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417coalesced_threadsv"><code class="docutils literal notranslate"><span class="pre">coalesced_threads()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415tiled_partitionRK12thread_groupj"><code class="docutils literal notranslate"><span class="pre">tiled_partition()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_j0E15tiled_partition17thread_block_tileI4size10ParentCGTyERK10ParentCGTy"><code class="docutils literal notranslate"><span class="pre">tiled_partition()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416binary_partitionRK15coalesced_groupb"><code class="docutils literal notranslate"><span class="pre">binary_partition()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_j0E16binary_partition15coalesced_groupRK17thread_block_tileI4size6parentEb"><code class="docutils literal notranslate"><span class="pre">binary_partition()</span></code></a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cooperative-groups-exposed-api-functions">Cooperative groups exposed API functions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E10group_size14__hip_uint32_tRK4CGTy"><code class="docutils literal notranslate"><span class="pre">group_size()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E11thread_rank14__hip_uint32_tRK4CGTy"><code class="docutils literal notranslate"><span class="pre">thread_rank()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E8is_validbRK4CGTy"><code class="docutils literal notranslate"><span class="pre">is_valid()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E4syncvRK4CGTy"><code class="docutils literal notranslate"><span class="pre">sync()</span></code></a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="cooperative-groups">
<span id="cooperative-groups-reference"></span><h1>Cooperative groups<a class="headerlink" href="#cooperative-groups" title="Link to this heading">#</a></h1>
<section id="cooperative-kernel-launches">
<h2>Cooperative kernel launches<a class="headerlink" href="#cooperative-kernel-launches" title="Link to this heading">#</a></h2>
<p>The following host-side functions are used for cooperative kernel launches.</p>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv432hipModuleLaunchCooperativeKernel13hipFunction_tjjjjjjj11hipStream_tPPv">
<span id="_CPPv332hipModuleLaunchCooperativeKernel13hipFunction_tjjjjjjj11hipStream_tPPv"></span><span id="_CPPv232hipModuleLaunchCooperativeKernel13hipFunction_tjjjjjjj11hipStream_tPPv"></span><span id="hipModuleLaunchCooperativeKernel__hipFunction_t.unsigned-i.unsigned-i.unsigned-i.unsigned-i.unsigned-i.unsigned-i.unsigned-i.hipStream_t.voidPP"></span><span class="target" id="group___module_cooperative_g_1ga7b7e76759a946338dd16a991505e31e1"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipModuleLaunchCooperativeKernel</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipFunction_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">f</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">gridDimX</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">gridDimY</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">gridDimZ</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">blockDimX</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">blockDimY</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">blockDimZ</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sharedMemBytes</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">kernelParams</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv432hipModuleLaunchCooperativeKernel13hipFunction_tjjjjjjj11hipStream_tPPv" title="Link to this definition">#</a><br /></dt>
<dd><p>launches kernel f with launch parameters and shared memory on stream with arguments passed to kernelParams, where thread blocks can cooperate and synchronize as they execute </p>
<p>
Please note, HIP does not support kernel launch with total work items defined in dimension with size <span class="math notranslate nohighlight">\( gridDim \cdot blockDim \geq 2^{32} \)</span>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>f</strong> – <strong>[in]</strong> Kernel to launch. </p></li>
<li><p><strong>gridDimX</strong> – <strong>[in]</strong> X grid dimension specified as multiple of blockDimX. </p></li>
<li><p><strong>gridDimY</strong> – <strong>[in]</strong> Y grid dimension specified as multiple of blockDimY. </p></li>
<li><p><strong>gridDimZ</strong> – <strong>[in]</strong> Z grid dimension specified as multiple of blockDimZ. </p></li>
<li><p><strong>blockDimX</strong> – <strong>[in]</strong> X block dimension specified in work-items. </p></li>
<li><p><strong>blockDimY</strong> – <strong>[in]</strong> Y block dimension specified in work-items. </p></li>
<li><p><strong>blockDimZ</strong> – <strong>[in]</strong> Z block dimension specified in work-items. </p></li>
<li><p><strong>sharedMemBytes</strong> – <strong>[in]</strong> Amount of dynamic shared memory to allocate for this kernel. The HIP-Clang compiler provides support for extern shared declarations. </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream where the kernel should be dispatched. May be 0, in which case the default stream is used with associated synchronization rules. </p></li>
<li><p><strong>kernelParams</strong> – <strong>[in]</strong> A list of kernel arguments.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidHandle, hipErrorInvalidImage, hipErrorInvalidValue, hipErrorInvalidConfiguration, hipErrorLaunchFailure, hipErrorLaunchOutOfResources, hipErrorLaunchTimeOut, hipErrorCooperativeLaunchTooLarge, hipErrorSharedObjectInitFailed</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv443hipModuleLaunchCooperativeKernelMultiDeviceP23hipFunctionLaunchParamsjj">
<span id="_CPPv343hipModuleLaunchCooperativeKernelMultiDeviceP23hipFunctionLaunchParamsjj"></span><span id="_CPPv243hipModuleLaunchCooperativeKernelMultiDeviceP23hipFunctionLaunchParamsjj"></span><span id="hipModuleLaunchCooperativeKernelMultiDevice__hipFunctionLaunchParamsP.unsigned-i.unsigned-i"></span><span class="target" id="group___module_cooperative_g_1ga13609d6a39d91c1ffcff11b0a712e9db"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipModuleLaunchCooperativeKernelMultiDevice</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipFunctionLaunchParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">launchParamsList</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDevices</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv443hipModuleLaunchCooperativeKernelMultiDeviceP23hipFunctionLaunchParamsjj" title="Link to this definition">#</a><br /></dt>
<dd><p>Launches kernels on multiple devices where thread blocks can cooperate and synchronize as they execute. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>launchParamsList</strong> – <strong>[in]</strong> List of launch parameters, one per device. </p></li>
<li><p><strong>numDevices</strong> – <strong>[in]</strong> Size of the launchParamsList array. </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Flags to control launch behavior.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorDeinitialized, hipErrorNotInitialized, hipErrorInvalidContext, hipErrorInvalidHandle, hipErrorInvalidImage, hipErrorInvalidValue, hipErrorInvalidConfiguration, hipErrorInvalidResourceHandle, hipErrorLaunchFailure, hipErrorLaunchOutOfResources, hipErrorLaunchTimeOut, hipErrorCooperativeLaunchTooLarge, hipErrorSharedObjectInitFailed</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv426hipLaunchCooperativeKernelPKv4dim34dim3PPvj11hipStream_t">
<span id="_CPPv326hipLaunchCooperativeKernelPKv4dim34dim3PPvj11hipStream_t"></span><span id="_CPPv226hipLaunchCooperativeKernelPKv4dim34dim3PPvj11hipStream_t"></span><span id="hipLaunchCooperativeKernel__voidCP.dim3.dim3.voidPP.unsigned-i.hipStream_t"></span><span class="target" id="group___module_cooperative_g_1gaa516e011bb07d01550102c98adb57ec2"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLaunchCooperativeKernel</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">f</span></span>, <span class="n"><span class="pre">dim3</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">gridDim</span></span>, <span class="n"><span class="pre">dim3</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">blockDimX</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">kernelParams</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sharedMemBytes</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv426hipLaunchCooperativeKernelPKv4dim34dim3PPvj11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Launches kernel f with launch parameters and shared memory on stream with arguments passed to kernelparams or extra, where thread blocks can cooperate and synchronize as they execute. </p>
<p>
Please note, HIP does not support kernel launch with total work items defined in dimension with size <span class="math notranslate nohighlight">\( gridDim \cdot blockDim \geq 2^{32} \)</span>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>f</strong> – <strong>[in]</strong> - Kernel to launch. </p></li>
<li><p><strong>gridDim</strong> – <strong>[in]</strong> - Grid dimensions specified as multiple of blockDim. </p></li>
<li><p><strong>blockDimX</strong> – <strong>[in]</strong> - Block dimensions specified in work-items </p></li>
<li><p><strong>kernelParams</strong> – <strong>[in]</strong> - Pointer of arguments passed to the kernel. If the kernel has multiple parameters, ‘kernelParams’ should be array of pointers, each points the corresponding argument. </p></li>
<li><p><strong>sharedMemBytes</strong> – <strong>[in]</strong> - Amount of dynamic shared memory to allocate for this kernel. The HIP-Clang compiler provides support for extern shared declarations. </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> - Stream where the kernel should be dispatched. May be 0, in which case th default stream is used with associated synchronization rules.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorNotInitialized, hipErrorInvalidValue, hipErrorCooperativeLaunchTooLarge</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv437hipLaunchCooperativeKernelMultiDeviceP15hipLaunchParamsij">
<span id="_CPPv337hipLaunchCooperativeKernelMultiDeviceP15hipLaunchParamsij"></span><span id="_CPPv237hipLaunchCooperativeKernelMultiDeviceP15hipLaunchParamsij"></span><span id="hipLaunchCooperativeKernelMultiDevice__hipLaunchParamsP.i.unsigned-i"></span><span class="target" id="group___module_cooperative_g_1ga661fc9f6975de96edd80c78af888a03f"></span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLaunchCooperativeKernelMultiDevice</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipLaunchParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">launchParamsList</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDevices</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv437hipLaunchCooperativeKernelMultiDeviceP15hipLaunchParamsij" title="Link to this definition">#</a><br /></dt>
<dd><p>Launches kernels on multiple devices where thread blocks can cooperate and synchronize as they execute. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>launchParamsList</strong> – <strong>[in]</strong> List of launch parameters, one per device. </p></li>
<li><p><strong>numDevices</strong> – <strong>[in]</strong> Size of the launchParamsList array. </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Flags to control launch behavior.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorNotInitialized, hipErrorInvalidValue, hipErrorCooperativeLaunchTooLarge</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E26hipLaunchCooperativeKernel10hipError_t1T4dim34dim3PPvj11hipStream_t">
<span id="_CPPv3I0E26hipLaunchCooperativeKernel1T4dim34dim3PPvj11hipStream_t"></span><span id="_CPPv2I0E26hipLaunchCooperativeKernel1T4dim34dim3PPvj11hipStream_t"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___module_cooperative_g_1gabc6de6c3b1400d3315e57625112d44ed"></span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLaunchCooperativeKernel</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E26hipLaunchCooperativeKernel10hipError_t1T4dim34dim3PPvj11hipStream_t" title="hipLaunchCooperativeKernel::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">f</span></span>, <span class="n"><span class="pre">dim3</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">gridDim</span></span>, <span class="n"><span class="pre">dim3</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">blockDim</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">kernelParams</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">sharedMemBytes</span></span>, <span class="n"><span class="pre">hipStream_t</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">stream</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E26hipLaunchCooperativeKernel10hipError_t1T4dim34dim3PPvj11hipStream_t" title="Link to this definition">#</a><br /></dt>
<dd><p>Launches a device function. </p>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>T</strong> – The type of the kernel function.</p>
</dd>
<dt class="field-even">Parameters<span class="colon">:</span></dt>
<dd class="field-even"><ul class="simple">
<li><p><strong>f</strong> – <strong>[in]</strong> Kernel function to launch. </p></li>
<li><p><strong>gridDim</strong> – <strong>[in]</strong> Grid dimensions specified as multiple of blockDim. </p></li>
<li><p><strong>blockDim</strong> – <strong>[in]</strong> Block dimensions specified in work-items. </p></li>
<li><p><strong>kernelParams</strong> – <strong>[in]</strong> A list of kernel arguments. </p></li>
<li><p><strong>sharedMemBytes</strong> – <strong>[in]</strong> Amount of dynamic shared memory to allocate for this kernel. The HIP-Clang compiler provides support for extern shared declarations. </p></li>
<li><p><strong>stream</strong> – <strong>[in]</strong> Stream which on the kernel launched.</p></li>
</ul>
</dd>
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p>hipSuccess, hipErrorLaunchFailure, hipErrorInvalidValue, hipErrorInvalidResourceHandle</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E37hipLaunchCooperativeKernelMultiDevice10hipError_tP15hipLaunchParamsjj">
<span id="_CPPv3I0E37hipLaunchCooperativeKernelMultiDeviceP15hipLaunchParamsjj"></span><span id="_CPPv2I0E37hipLaunchCooperativeKernelMultiDeviceP15hipLaunchParamsjj"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___module_cooperative_g_1gae5e0fab49e4fa6f1b3753cec767128ca"></span><span class="k"><span class="pre">inline</span></span><span class="w"> </span><span class="n"><span class="pre">hipError_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">hipLaunchCooperativeKernelMultiDevice</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">hipLaunchParams</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n sig-param"><span class="pre">launchParamsList</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">numDevices</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">flags</span></span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="m"><span class="pre">0</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E37hipLaunchCooperativeKernelMultiDevice10hipError_tP15hipLaunchParamsjj" title="Link to this definition">#</a><br /></dt>
<dd><p>Launches kernel function on multiple devices, where thread blocks can cooperate and synchronize on execution. </p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>launchParamsList</strong> – <strong>[in]</strong> List of kernel launch parameters, one per device. </p></li>
<li><p><strong>numDevices</strong> – <strong>[in]</strong> Size of launchParamsList array. </p></li>
<li><p><strong>flags</strong> – <strong>[in]</strong> Flag to handle launch behavior.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p>hipSuccess, hipErrorLaunchFailure, hipErrorInvalidValue, hipErrorInvalidResourceHandle</p>
</dd>
</dl>
</dd></dl>

</section>
<section id="cooperative-groups-classes">
<h2>Cooperative groups classes<a class="headerlink" href="#cooperative-groups-classes" title="Link to this heading">#</a></h2>
<p>The following cooperative groups classes can be used on the device side.</p>
<dl class="cpp class" id="thread-group-ref">
<dt class="sig sig-object cpp" id="_CPPv4N18cooperative_groups12thread_groupE">
<span id="_CPPv3N18cooperative_groups12thread_groupE"></span><span id="_CPPv2N18cooperative_groups12thread_groupE"></span><span id="cooperative_groups::thread_group"></span><span class="target" id="classcooperative__groups_1_1thread__group"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">thread_group</span></span></span><a class="headerlink" href="#_CPPv4N18cooperative_groups12thread_groupE" title="Link to this definition">#</a><br /></dt>
<dd><p>The base type of all cooperative group types. </p>
<p>Holds the key properties of a constructed cooperative group types object, like the group type, its size, etc.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Cooperative groups feature is implemented on Linux, under development on Microsoft Windows. </p>
</div>
<p>Subclassed by <a class="reference internal" href="#classcooperative__groups_1_1coalesced__group"><span class="std std-ref">cooperative_groups::coalesced_group</span></a>, <a class="reference internal" href="#classcooperative__groups_1_1grid__group"><span class="std std-ref">cooperative_groups::grid_group</span></a>, <a class="reference internal" href="#classcooperative__groups_1_1multi__grid__group"><span class="std std-ref">cooperative_groups::multi_grid_group</span></a>, <a class="reference internal" href="#classcooperative__groups_1_1thread__block"><span class="std std-ref">cooperative_groups::thread_block</span></a>, cooperative_groups::tiled_group</p>
</dd></dl>

<dl class="cpp class" id="thread-block-ref">
<dt class="sig sig-object cpp" id="_CPPv4N18cooperative_groups12thread_blockE">
<span id="_CPPv3N18cooperative_groups12thread_blockE"></span><span id="_CPPv2N18cooperative_groups12thread_blockE"></span><span id="cooperative_groups::thread_block"></span><span class="target" id="classcooperative__groups_1_1thread__block"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">thread_block</span></span></span><span class="w"> </span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="k"><span class="pre">public</span></span><span class="w"> </span><span class="n"><span class="pre">cooperative_groups</span></span><span class="p"><span class="pre">::</span></span><a class="reference internal" href="#_CPPv4N18cooperative_groups12thread_groupE" title="cooperative_groups::thread_group"><span class="n"><span class="pre">thread_group</span></span></a><a class="headerlink" href="#_CPPv4N18cooperative_groups12thread_blockE" title="Link to this definition">#</a><br /></dt>
<dd><p>The workgroup (thread-block in CUDA terminology) cooperative group type. </p>
<p>Represents an intra-workgroup cooperative group type, where the participating threads within the group are the same threads that participated in the currently executing <code class="docutils literal notranslate"><span class="pre">workgroup</span></code>. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This function is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
</dd></dl>

<dl class="cpp class" id="grid-group-ref">
<dt class="sig sig-object cpp" id="_CPPv4N18cooperative_groups10grid_groupE">
<span id="_CPPv3N18cooperative_groups10grid_groupE"></span><span id="_CPPv2N18cooperative_groups10grid_groupE"></span><span id="cooperative_groups::grid_group"></span><span class="target" id="classcooperative__groups_1_1grid__group"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">grid_group</span></span></span><span class="w"> </span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="k"><span class="pre">public</span></span><span class="w"> </span><span class="n"><span class="pre">cooperative_groups</span></span><span class="p"><span class="pre">::</span></span><a class="reference internal" href="#_CPPv4N18cooperative_groups12thread_groupE" title="cooperative_groups::thread_group"><span class="n"><span class="pre">thread_group</span></span></a><a class="headerlink" href="#_CPPv4N18cooperative_groups10grid_groupE" title="Link to this definition">#</a><br /></dt>
<dd><p>The grid cooperative group type. </p>
<p>Represents an inter-workgroup cooperative group type, where the participating threads within the group spans across multiple workgroups running the (same) kernel on the same device. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
</dd></dl>

<dl class="cpp class" id="multi-grid-group-ref">
<dt class="sig sig-object cpp" id="_CPPv4N18cooperative_groups16multi_grid_groupE">
<span id="_CPPv3N18cooperative_groups16multi_grid_groupE"></span><span id="_CPPv2N18cooperative_groups16multi_grid_groupE"></span><span id="cooperative_groups::multi_grid_group"></span><span class="target" id="classcooperative__groups_1_1multi__grid__group"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">multi_grid_group</span></span></span><span class="w"> </span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="k"><span class="pre">public</span></span><span class="w"> </span><span class="n"><span class="pre">cooperative_groups</span></span><span class="p"><span class="pre">::</span></span><a class="reference internal" href="#_CPPv4N18cooperative_groups12thread_groupE" title="cooperative_groups::thread_group"><span class="n"><span class="pre">thread_group</span></span></a><a class="headerlink" href="#_CPPv4N18cooperative_groups16multi_grid_groupE" title="Link to this definition">#</a><br /></dt>
<dd><p>The multi-grid cooperative group type. </p>
<p>Represents an inter-device cooperative group type, where the participating threads within the group span across multiple devices, running the (same) kernel on these devices. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The multi-grid cooperative group type is implemented on Linux, under development on Microsoft Windows. </p>
</div>
</dd></dl>

<dl class="cpp class" id="thread-block-tile-ref">
<dt class="sig sig-object cpp" id="_CPPv4I_j0EN18cooperative_groups17thread_block_tileE">
<span id="_CPPv3I_j0EN18cooperative_groups17thread_block_tileE"></span><span id="_CPPv2I_j0EN18cooperative_groups17thread_block_tileE"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">size</span></span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ParentCGTy</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classcooperative__groups_1_1thread__block__tile"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">thread_block_tile</span></span></span><span class="w"> </span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="k"><span class="pre">public</span></span><span class="w"> </span><span class="n"><span class="pre">cooperative_groups</span></span><span class="p"><span class="pre">::</span></span><span class="n"><span class="pre">impl</span></span><span class="p"><span class="pre">::</span></span><span class="n"><span class="pre">thread_block_tile_internal</span></span><span class="p"><span class="pre">&lt;</span></span><a class="reference internal" href="#_CPPv4I_j0EN18cooperative_groups17thread_block_tileE" title="cooperative_groups::thread_block_tile::size"><span class="n"><span class="pre">size</span></span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv4I_j0EN18cooperative_groups17thread_block_tileE" title="cooperative_groups::thread_block_tile::ParentCGTy"><span class="n"><span class="pre">ParentCGTy</span></span></a><span class="p"><span class="pre">&gt;</span></span><a class="headerlink" href="#_CPPv4I_j0EN18cooperative_groups17thread_block_tileE" title="Link to this definition">#</a><br /></dt>
<dd><p>Group type - <a class="reference internal" href="#classcooperative__groups_1_1thread__block__tile"><span class="std std-ref">thread_block_tile</span></a>. </p>
<p>Represents one tiled thread group in a wavefront. This group type also supports sub-wave level intrinsics.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This type is implemented on Linux, under development on Microsoft Windows. </p>
</div>
<div class="breathe-sectiondef docutils container">
<p class="breathe-sectiondef-title rubric" id="breathe-section-title-public-functions">Public Functions</p>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4NK18cooperative_groups17thread_block_tile11thread_rankEv">
<span id="_CPPv3NK18cooperative_groups17thread_block_tile11thread_rankEv"></span><span id="_CPPv2NK18cooperative_groups17thread_block_tile11thread_rankEv"></span><span id="cooperative_groups::thread_block_tile::thread_rankC"></span><span class="target" id="classcooperative__groups_1_1thread__block__tile_1a4c0d2700d6b0e221041e97f97b79dd25"></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">thread_rank</span></span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><span class="w"> </span><span class="k"><span class="pre">const</span></span><a class="headerlink" href="#_CPPv4NK18cooperative_groups17thread_block_tile11thread_rankEv" title="Link to this definition">#</a><br /></dt>
<dd><p>Rank of the calling thread within [0, num_threads() ).   </p>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4N18cooperative_groups17thread_block_tile4syncEv">
<span id="_CPPv3N18cooperative_groups17thread_block_tile4syncEv"></span><span id="_CPPv2N18cooperative_groups17thread_block_tile4syncEv"></span><span id="cooperative_groups::thread_block_tile::sync"></span><span class="target" id="classcooperative__groups_1_1thread__block__tile_1aeef8ab97c10d2e78e047d8d9117dfe95"></span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">sync</span></span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4N18cooperative_groups17thread_block_tile4syncEv" title="Link to this definition">#</a><br /></dt>
<dd><p>Synchronizes the threads in the group.   </p>
<p>Causes all threads in the group to wait at this synchronization point, and for all shared and global memory accesses by the threads to complete, before running synchronization. This guarantees the visibility of accessed data for all threads in the group.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>There are potential read-after-write (RAW), write-after-read (WAR), or write-after-write (WAW) hazards, when threads in the group access the same addresses in shared or global memory. The data hazards can be avoided with synchronization of the group.   </p>
</div>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4NK18cooperative_groups17thread_block_tile15meta_group_rankEv">
<span id="_CPPv3NK18cooperative_groups17thread_block_tile15meta_group_rankEv"></span><span id="_CPPv2NK18cooperative_groups17thread_block_tile15meta_group_rankEv"></span><span id="cooperative_groups::thread_block_tile::meta_group_rankC"></span><span class="target" id="classcooperative__groups_1_1thread__block__tile_1a4929b1ad6c3f2c43e882993327c3c001"></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">meta_group_rank</span></span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><span class="w"> </span><span class="k"><span class="pre">const</span></span><a class="headerlink" href="#_CPPv4NK18cooperative_groups17thread_block_tile15meta_group_rankEv" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns the linear rank of the group within the set of tiles partitioned from a parent group (bounded by meta_group_size) </p>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4NK18cooperative_groups17thread_block_tile15meta_group_sizeEv">
<span id="_CPPv3NK18cooperative_groups17thread_block_tile15meta_group_sizeEv"></span><span id="_CPPv2NK18cooperative_groups17thread_block_tile15meta_group_sizeEv"></span><span id="cooperative_groups::thread_block_tile::meta_group_sizeC"></span><span class="target" id="classcooperative__groups_1_1thread__block__tile_1aa6ca727728042a9b57c869df5c1efdec"></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">meta_group_size</span></span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><span class="w"> </span><span class="k"><span class="pre">const</span></span><a class="headerlink" href="#_CPPv4NK18cooperative_groups17thread_block_tile15meta_group_sizeEv" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns the number of groups created when the parent group was partitioned. </p>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0ENK18cooperative_groups17thread_block_tile4shflE1T1Ti">
<span id="_CPPv3I0ENK18cooperative_groups17thread_block_tile4shflE1Ti"></span><span id="_CPPv2I0ENK18cooperative_groups17thread_block_tile4shflE1Ti"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classcooperative__groups_1_1thread__block__tile_1af8ebf804a22548e6cc77f06e55829142"></span><a class="reference internal" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile4shflE1T1Ti" title="cooperative_groups::thread_block_tile::shfl::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">shfl</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile4shflE1T1Ti" title="cooperative_groups::thread_block_tile::shfl::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">var</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">srcRank</span></span><span class="sig-paren">)</span><span class="w"> </span><span class="k"><span class="pre">const</span></span><a class="headerlink" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile4shflE1T1Ti" title="Link to this definition">#</a><br /></dt>
<dd><p>Shuffle operation on group level. </p>
<p>Exchanging variables between threads without use of shared memory. Shuffle operation is a direct copy of <code class="docutils literal notranslate"><span class="pre">var</span></code> from <code class="docutils literal notranslate"><span class="pre">srcRank</span></code> thread ID of group.</p>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>T</strong> – The type can be a 32-bit integer or single-precision floating point. </p>
</dd>
<dt class="field-even">Parameters<span class="colon">:</span></dt>
<dd class="field-even"><ul class="simple">
<li><p><strong>var</strong> – [in] The source variable to copy. Only the srcRank thread ID of group is copied to other threads. </p></li>
<li><p><strong>srcRank</strong> – [in] The source thread ID of the group for copy. </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0ENK18cooperative_groups17thread_block_tile9shfl_downE1T1Tj">
<span id="_CPPv3I0ENK18cooperative_groups17thread_block_tile9shfl_downE1Tj"></span><span id="_CPPv2I0ENK18cooperative_groups17thread_block_tile9shfl_downE1Tj"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classcooperative__groups_1_1thread__block__tile_1a017cbabc27d80233c5444c1058e3b153"></span><a class="reference internal" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9shfl_downE1T1Tj" title="cooperative_groups::thread_block_tile::shfl_down::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">shfl_down</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9shfl_downE1T1Tj" title="cooperative_groups::thread_block_tile::shfl_down::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">var</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lane_delta</span></span><span class="sig-paren">)</span><span class="w"> </span><span class="k"><span class="pre">const</span></span><a class="headerlink" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9shfl_downE1T1Tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Shuffle down operation on group level. </p>
<p>Exchanging variables between threads without use of shared memory. Shuffle down operation is copy of <code class="docutils literal notranslate"><span class="pre">var</span></code> from thread with thread ID of group relative higher with <code class="docutils literal notranslate"><span class="pre">lane_delta</span></code> to caller thread ID.</p>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>T</strong> – The type can be a 32-bit integer or single-precision floating point. </p>
</dd>
<dt class="field-even">Parameters<span class="colon">:</span></dt>
<dd class="field-even"><ul class="simple">
<li><p><strong>var</strong> – [in] The source variable to copy. </p></li>
<li><p><strong>lane_delta</strong> – [in] The lane_delta is the relative thread ID difference between caller thread ID and source of copy thread ID. sourceID = (threadID + lane_delta) % size()</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0ENK18cooperative_groups17thread_block_tile7shfl_upE1T1Tj">
<span id="_CPPv3I0ENK18cooperative_groups17thread_block_tile7shfl_upE1Tj"></span><span id="_CPPv2I0ENK18cooperative_groups17thread_block_tile7shfl_upE1Tj"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classcooperative__groups_1_1thread__block__tile_1ad1a5fed741b92649806a26c5b5c75612"></span><a class="reference internal" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile7shfl_upE1T1Tj" title="cooperative_groups::thread_block_tile::shfl_up::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">shfl_up</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile7shfl_upE1T1Tj" title="cooperative_groups::thread_block_tile::shfl_up::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">var</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">lane_delta</span></span><span class="sig-paren">)</span><span class="w"> </span><span class="k"><span class="pre">const</span></span><a class="headerlink" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile7shfl_upE1T1Tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Shuffle up operation on group level. </p>
<p>Exchanging variables between threads without use of shared memory. Shuffle up operation is copy of <code class="docutils literal notranslate"><span class="pre">var</span></code> from thread with thread ID of group relative lower with <code class="docutils literal notranslate"><span class="pre">lane_delta</span></code> to caller thread ID.</p>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>T</strong> – The type can be a 32-bit integer or single-precision floating point. </p>
</dd>
<dt class="field-even">Parameters<span class="colon">:</span></dt>
<dd class="field-even"><ul class="simple">
<li><p><strong>var</strong> – [in] The source variable to copy. </p></li>
<li><p><strong>lane_delta</strong> – [in] The lane_delta is the relative thread ID difference between caller thread ID and source of copy thread ID. sourceID = (threadID - lane_delta) % size()</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0ENK18cooperative_groups17thread_block_tile8shfl_xorE1T1Tj">
<span id="_CPPv3I0ENK18cooperative_groups17thread_block_tile8shfl_xorE1Tj"></span><span id="_CPPv2I0ENK18cooperative_groups17thread_block_tile8shfl_xorE1Tj"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classcooperative__groups_1_1thread__block__tile_1a4f8483f8a5f532dd21e15f0236ee42b5"></span><a class="reference internal" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile8shfl_xorE1T1Tj" title="cooperative_groups::thread_block_tile::shfl_xor::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">shfl_xor</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile8shfl_xorE1T1Tj" title="cooperative_groups::thread_block_tile::shfl_xor::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">var</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">laneMask</span></span><span class="sig-paren">)</span><span class="w"> </span><span class="k"><span class="pre">const</span></span><a class="headerlink" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile8shfl_xorE1T1Tj" title="Link to this definition">#</a><br /></dt>
<dd><p>Shuffle xor operation on group level. </p>
<p>Exchanging variables between threads without use of shared memory. Shuffle xor operation is copy of var from thread with thread ID of group based on laneMask XOR of the caller thread ID.</p>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>T</strong> – The type can be a 32-bit integer or single-precision floating point. </p>
</dd>
<dt class="field-even">Parameters<span class="colon">:</span></dt>
<dd class="field-even"><ul class="simple">
<li><p><strong>var</strong> – [in] The source variable to copy. </p></li>
<li><p><strong>laneMask</strong> – [in] The laneMask is the mask for XOR operation. sourceID = threadID ^ laneMask </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4NK18cooperative_groups17thread_block_tile6ballotEi">
<span id="_CPPv3NK18cooperative_groups17thread_block_tile6ballotEi"></span><span id="_CPPv2NK18cooperative_groups17thread_block_tile6ballotEi"></span><span id="cooperative_groups::thread_block_tile::ballot__iC"></span><span class="target" id="classcooperative__groups_1_1thread__block__tile_1a0de855f9fb84b142756bc287eef099f6"></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ballot</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">pred</span></span><span class="sig-paren">)</span><span class="w"> </span><span class="k"><span class="pre">const</span></span><a class="headerlink" href="#_CPPv4NK18cooperative_groups17thread_block_tile6ballotEi" title="Link to this definition">#</a><br /></dt>
<dd><p>Ballot function on group level. </p>
<p>Returns a bit mask with the Nth bit set to one if the Nth thread predicate evaluates true.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>pred</strong> – [in] The predicate to evaluate on group threads. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4NK18cooperative_groups17thread_block_tile3anyEi">
<span id="_CPPv3NK18cooperative_groups17thread_block_tile3anyEi"></span><span id="_CPPv2NK18cooperative_groups17thread_block_tile3anyEi"></span><span id="cooperative_groups::thread_block_tile::any__iC"></span><span class="target" id="classcooperative__groups_1_1thread__block__tile_1a01ed78a4af36b522ba6172b5e2aba157"></span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">any</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">pred</span></span><span class="sig-paren">)</span><span class="w"> </span><span class="k"><span class="pre">const</span></span><a class="headerlink" href="#_CPPv4NK18cooperative_groups17thread_block_tile3anyEi" title="Link to this definition">#</a><br /></dt>
<dd><p>Any function on group level. </p>
<p>Returns non-zero if a predicate evaluates true for any threads.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>pred</strong> – [in] The predicate to evaluate on group threads. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4NK18cooperative_groups17thread_block_tile3allEi">
<span id="_CPPv3NK18cooperative_groups17thread_block_tile3allEi"></span><span id="_CPPv2NK18cooperative_groups17thread_block_tile3allEi"></span><span id="cooperative_groups::thread_block_tile::all__iC"></span><span class="target" id="classcooperative__groups_1_1thread__block__tile_1a6bcd7bf33bd2ff832fa8b500b351c404"></span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">all</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">pred</span></span><span class="sig-paren">)</span><span class="w"> </span><span class="k"><span class="pre">const</span></span><a class="headerlink" href="#_CPPv4NK18cooperative_groups17thread_block_tile3allEi" title="Link to this definition">#</a><br /></dt>
<dd><p>All function on group level. </p>
<p>Returns non-zero if a predicate evaluates true for all threads.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>pred</strong> – [in] The predicate to evaluate on group threads. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0ENK18cooperative_groups17thread_block_tile9match_anyEy1T">
<span id="_CPPv3I0ENK18cooperative_groups17thread_block_tile9match_anyE1T"></span><span id="_CPPv2I0ENK18cooperative_groups17thread_block_tile9match_anyE1T"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">typename</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classcooperative__groups_1_1thread__block__tile_1a7a08cd57d3962fde2791e7c92918ca4f"></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">match_any</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9match_anyEy1T" title="cooperative_groups::thread_block_tile::match_any::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span><span class="sig-paren">)</span><span class="w"> </span><span class="k"><span class="pre">const</span></span><a class="headerlink" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9match_anyEy1T" title="Link to this definition">#</a><br /></dt>
<dd><p>Match any function on group level. </p>
<p>Returns a bit mask containing a 1-bit for every participating thread if that thread has the same value in <code class="docutils literal notranslate"><span class="pre">value</span></code> as the caller thread.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>value</strong> – [in] The value to examine on the current thread in group. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0ENK18cooperative_groups17thread_block_tile9match_allEy1TRi">
<span id="_CPPv3I0ENK18cooperative_groups17thread_block_tile9match_allE1TRi"></span><span id="_CPPv2I0ENK18cooperative_groups17thread_block_tile9match_allE1TRi"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">typename</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">T</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="classcooperative__groups_1_1thread__block__tile_1a9fb74b232607c2720a97d8308f25b41d"></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="kt"><span class="pre">long</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">match_all</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9match_allEy1TRi" title="cooperative_groups::thread_block_tile::match_all::T"><span class="n"><span class="pre">T</span></span></a><span class="w"> </span><span class="n sig-param"><span class="pre">value</span></span>, <span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">pred</span></span><span class="sig-paren">)</span><span class="w"> </span><span class="k"><span class="pre">const</span></span><a class="headerlink" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9match_allEy1TRi" title="Link to this definition">#</a><br /></dt>
<dd><p>Match all function on group level. </p>
<p>Returns a bit mask containing a 1-bit for every participating thread if they all have the same value in <code class="docutils literal notranslate"><span class="pre">value</span></code> as the caller thread. The predicate <code class="docutils literal notranslate"><span class="pre">pred</span></code> is set to true if all participating threads have the same value in <code class="docutils literal notranslate"><span class="pre">value</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>value</strong> – [in] The value to examine on the current thread in group. </p></li>
<li><p><strong>pred</strong> – [out] The predicate is set to true if all participating threads in the thread group have the same value. </p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
</dd></dl>

<dl class="cpp class" id="coalesced-group-ref">
<dt class="sig sig-object cpp" id="_CPPv4N18cooperative_groups15coalesced_groupE">
<span id="_CPPv3N18cooperative_groups15coalesced_groupE"></span><span id="_CPPv2N18cooperative_groups15coalesced_groupE"></span><span id="cooperative_groups::coalesced_group"></span><span class="target" id="classcooperative__groups_1_1coalesced__group"></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">coalesced_group</span></span></span><span class="w"> </span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="k"><span class="pre">public</span></span><span class="w"> </span><span class="n"><span class="pre">cooperative_groups</span></span><span class="p"><span class="pre">::</span></span><a class="reference internal" href="#_CPPv4N18cooperative_groups12thread_groupE" title="cooperative_groups::thread_group"><span class="n"><span class="pre">thread_group</span></span></a><a class="headerlink" href="#_CPPv4N18cooperative_groups15coalesced_groupE" title="Link to this definition">#</a><br /></dt>
<dd><p>The <a class="reference internal" href="#classcooperative__groups_1_1coalesced__group"><span class="std std-ref">coalesced_group</span></a> cooperative group type. </p>
<p>Represents an active thread group in a wavefront. This group type also supports sub-wave level intrinsics. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
</dd></dl>

</section>
<section id="cooperative-groups-construct-functions">
<h2>Cooperative groups construct functions<a class="headerlink" href="#cooperative-groups-construct-functions" title="Link to this heading">#</a></h2>
<p>The following functions are used to construct different group-type instances on the device side.</p>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415this_multi_gridv">
<span id="_CPPv315this_multi_gridv"></span><span id="_CPPv215this_multi_gridv"></span><span id="this_multi_grid"></span><span class="target" id="group___cooperative_g_construct_1ga5bb8d15384484dd53a76e688f18faa63"></span><span class="n"><span class="pre">multi_grid_group</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">this_multi_grid</span></span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415this_multi_gridv" title="Link to this definition">#</a><br /></dt>
<dd><p>User-exposed API interface to construct grid cooperative group type object - <code class="docutils literal notranslate"><a class="reference internal" href="#classcooperative__groups_1_1multi__grid__group"><span class="std std-ref"><span class="pre">multi_grid_group</span></span></a></code>. </p>
<p>User is not allowed to construct an object of type <code class="docutils literal notranslate"><a class="reference internal" href="#classcooperative__groups_1_1multi__grid__group"><span class="std std-ref"><span class="pre">multi_grid_group</span></span></a></code> directly. Instead, they should construct it through this API function. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This multi-grid cooperative API type is implemented on Linux, under development on Microsoft Windows. </p>
</div>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv49this_gridv">
<span id="_CPPv39this_gridv"></span><span id="_CPPv29this_gridv"></span><span id="this_grid"></span><span class="target" id="group___cooperative_g_construct_1gae8c00eb70b1ccd256b1359fec80ef6ab"></span><span class="n"><span class="pre">grid_group</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">this_grid</span></span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv49this_gridv" title="Link to this definition">#</a><br /></dt>
<dd><p>User-exposed API interface to construct grid cooperative group type object - <code class="docutils literal notranslate"><a class="reference internal" href="#classcooperative__groups_1_1grid__group"><span class="std std-ref"><span class="pre">grid_group</span></span></a></code>. </p>
<p>User is not allowed to construct an object of type <code class="docutils literal notranslate"><a class="reference internal" href="#classcooperative__groups_1_1grid__group"><span class="std std-ref"><span class="pre">grid_group</span></span></a></code> directly. Instead, they should construct it through this API function. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This function is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417this_thread_blockv">
<span id="_CPPv317this_thread_blockv"></span><span id="_CPPv217this_thread_blockv"></span><span id="this_thread_block"></span><span class="target" id="group___cooperative_g_construct_1ga1eae7abf15ecb8506c397622edae386a"></span><span class="n"><span class="pre">thread_block</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">this_thread_block</span></span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417this_thread_blockv" title="Link to this definition">#</a><br /></dt>
<dd><p>User-exposed API interface to construct workgroup cooperative group type object - <code class="docutils literal notranslate"><a class="reference internal" href="#classcooperative__groups_1_1thread__block"><span class="std std-ref"><span class="pre">thread_block</span></span></a></code>. </p>
<p>User is not allowed to construct an object of type <code class="docutils literal notranslate"><a class="reference internal" href="#classcooperative__groups_1_1thread__block"><span class="std std-ref"><span class="pre">thread_block</span></span></a></code> directly. Instead, they should construct it through this API function. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This function is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv417coalesced_threadsv">
<span id="_CPPv317coalesced_threadsv"></span><span id="_CPPv217coalesced_threadsv"></span><span id="coalesced_threads"></span><span class="target" id="group___cooperative_g_construct_1gabd2ce62ee8ff561f5d29198a3f658361"></span><span class="n"><span class="pre">coalesced_group</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">coalesced_threads</span></span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv417coalesced_threadsv" title="Link to this definition">#</a><br /></dt>
<dd><p>User-exposed API to create coalesced groups. </p>
<p>A collective operation that groups all active lanes into a new thread group. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This function is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv415tiled_partitionRK12thread_groupj">
<span id="_CPPv315tiled_partitionRK12thread_groupj"></span><span id="_CPPv215tiled_partitionRK12thread_groupj"></span><span id="tiled_partition__thread_groupCR.unsigned-i"></span><span class="target" id="group___cooperative_g_construct_1ga4370e313e99dbea9b22ee832dd11dc43"></span><span class="n"><span class="pre">thread_group</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">tiled_partition</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">thread_group</span></span><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">parent</span></span>, <span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">tile_size</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv415tiled_partitionRK12thread_groupj" title="Link to this definition">#</a><br /></dt>
<dd><p>User-exposed API to partition groups. </p>
<p>A collective operation that partitions the parent group into a one-dimensional, row-major, tiling of subgroups. </p>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I_j0E15tiled_partition17thread_block_tileI4size10ParentCGTyERK10ParentCGTy">
<span id="_CPPv3I_j0E15tiled_partitionRK10ParentCGTy"></span><span id="_CPPv2I_j0E15tiled_partitionRK10ParentCGTy"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">size</span></span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">ParentCGTy</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___cooperative_g_construct_1ga869af43bbfadee88571050f71981fa07"></span><span class="n"><span class="pre">thread_block_tile</span></span><span class="p"><span class="pre">&lt;</span></span><a class="reference internal" href="#_CPPv4I_j0E15tiled_partition17thread_block_tileI4size10ParentCGTyERK10ParentCGTy" title="tiled_partition::size"><span class="n"><span class="pre">size</span></span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv4I_j0E15tiled_partition17thread_block_tileI4size10ParentCGTyERK10ParentCGTy" title="tiled_partition::ParentCGTy"><span class="n"><span class="pre">ParentCGTy</span></span></a><span class="p"><span class="pre">&gt;</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">tiled_partition</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv4I_j0E15tiled_partition17thread_block_tileI4size10ParentCGTyERK10ParentCGTy" title="tiled_partition::ParentCGTy"><span class="n"><span class="pre">ParentCGTy</span></span></a><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">g</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I_j0E15tiled_partition17thread_block_tileI4size10ParentCGTyERK10ParentCGTy" title="Link to this definition">#</a><br /></dt>
<dd><p>Create a partition. </p>
<p>This constructs a templated class derived from <a class="reference internal" href="#classcooperative__groups_1_1thread__group"><span class="std std-ref">thread_group</span></a>. The template defines the tile size of the new thread group at compile time.</p>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>size</strong> – The new size of the partition. </p></li>
<li><p><strong>ParentCGTy</strong> – The cooperative group class template parameter of the input group.</p></li>
</ul>
</dd>
<dt class="field-even">Parameters<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – [in] The coalesced group for split. </p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv416binary_partitionRK15coalesced_groupb">
<span id="_CPPv316binary_partitionRK15coalesced_groupb"></span><span id="_CPPv216binary_partitionRK15coalesced_groupb"></span><span id="binary_partition__coalesced_groupCR.b"></span><span class="target" id="group___cooperative_g_construct_1ga2dd949176bc8a6e0fca573e046560368"></span><span class="n"><span class="pre">coalesced_group</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">binary_partition</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">coalesced_group</span></span><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">cgrp</span></span>, <span class="kt"><span class="pre">bool</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">pred</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv416binary_partitionRK15coalesced_groupb" title="Link to this definition">#</a><br /></dt>
<dd><p>Binary partition. </p>
<p>This splits the input thread group into two partitions determined by predicate.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cgrp</strong> – [in] The coalesced group for split. </p></li>
<li><p><strong>pred</strong> – [in] The predicate used during the group split up. </p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I_j0E16binary_partition15coalesced_groupRK17thread_block_tileI4size6parentEb">
<span id="_CPPv3I_j0E16binary_partitionRK17thread_block_tileI4size6parentEb"></span><span id="_CPPv2I_j0E16binary_partitionRK17thread_block_tileI4size6parentEb"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="kt"><span class="pre">unsigned</span></span><span class="w"> </span><span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">size</span></span></span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">parent</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___cooperative_g_construct_1ga734f31d46c56147b1ceb90c9a4e765ab"></span><span class="n"><span class="pre">coalesced_group</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">binary_partition</span></span></span><span class="sig-paren">(</span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="n"><span class="pre">thread_block_tile</span></span><span class="p"><span class="pre">&lt;</span></span><a class="reference internal" href="#_CPPv4I_j0E16binary_partition15coalesced_groupRK17thread_block_tileI4size6parentEb" title="binary_partition::size"><span class="n"><span class="pre">size</span></span></a><span class="p"><span class="pre">,</span></span><span class="w"> </span><a class="reference internal" href="#_CPPv4I_j0E16binary_partition15coalesced_groupRK17thread_block_tileI4size6parentEb" title="binary_partition::parent"><span class="n"><span class="pre">parent</span></span></a><span class="p"><span class="pre">&gt;</span></span><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">tgrp</span></span>, <span class="kt"><span class="pre">bool</span></span><span class="w"> </span><span class="n sig-param"><span class="pre">pred</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I_j0E16binary_partition15coalesced_groupRK17thread_block_tileI4size6parentEb" title="Link to this definition">#</a><br /></dt>
<dd><p>Binary partition. </p>
<p>This splits the input thread group into two partitions determined by predicate.</p>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>size</strong> – The size of the input thread block tile group. </p></li>
<li><p><strong>parent</strong> – The cooperative group class template parameter of the input group.</p></li>
</ul>
</dd>
<dt class="field-even">Parameters<span class="colon">:</span></dt>
<dd class="field-even"><ul class="simple">
<li><p><strong>tgrp</strong> – [in] The thread block tile group for split. </p></li>
<li><p><strong>pred</strong> – [in] The predicate used during the group split up. </p></li>
</ul>
</dd>
</dl>
</dd></dl>

</section>
<section id="cooperative-groups-exposed-api-functions">
<h2>Cooperative groups exposed API functions<a class="headerlink" href="#cooperative-groups-exposed-api-functions" title="Link to this heading">#</a></h2>
<p>The following functions are the exposed API for different group-type instances on the device side.</p>
<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E10group_size14__hip_uint32_tRK4CGTy">
<span id="_CPPv3I0E10group_sizeRK4CGTy"></span><span id="_CPPv2I0E10group_sizeRK4CGTy"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">CGTy</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___cooperative_g_a_p_i_1gaa2bf4c2318b9fdc321320fab0b128c4c"></span><span class="n"><span class="pre">__hip_uint32_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">group_size</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E10group_size14__hip_uint32_tRK4CGTy" title="group_size::CGTy"><span class="n"><span class="pre">CGTy</span></span></a><span class="w"> </span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">g</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E10group_size14__hip_uint32_tRK4CGTy" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns the size of the group. </p>
<p>Total number of threads in the thread group, and this serves the purpose for all derived cooperative group types because their <code class="docutils literal notranslate"><span class="pre">size</span></code> is directly saved during the construction.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Implementation of publicly exposed <code class="docutils literal notranslate"><span class="pre">wrapper</span></code> API on top of basic cooperative group type APIs. This function is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>CGTy</strong> – The cooperative group class template parameter. </p>
</dd>
<dt class="field-even">Parameters<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – [in] The cooperative group for size returns.</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E11thread_rank14__hip_uint32_tRK4CGTy">
<span id="_CPPv3I0E11thread_rankRK4CGTy"></span><span id="_CPPv2I0E11thread_rankRK4CGTy"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">CGTy</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___cooperative_g_a_p_i_1gae94ef8cbab6027347ab853b50115591a"></span><span class="n"><span class="pre">__hip_uint32_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">thread_rank</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E11thread_rank14__hip_uint32_tRK4CGTy" title="thread_rank::CGTy"><span class="n"><span class="pre">CGTy</span></span></a><span class="w"> </span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">g</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E11thread_rank14__hip_uint32_tRK4CGTy" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns the rank of thread of the group. </p>
<p>Rank of the calling thread within [0, num_threads() ).</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Implementation of publicly exposed <code class="docutils literal notranslate"><span class="pre">wrapper</span></code> API on top of basic cooperative group type APIs. This function is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>CGTy</strong> – The cooperative group class template parameter. </p>
</dd>
<dt class="field-even">Parameters<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – [in] The cooperative group for rank returns.</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E8is_validbRK4CGTy">
<span id="_CPPv3I0E8is_validRK4CGTy"></span><span id="_CPPv2I0E8is_validRK4CGTy"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">CGTy</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___cooperative_g_a_p_i_1ga3d007bc543edfd278ef513939cfbfb82"></span><span class="kt"><span class="pre">bool</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">is_valid</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E8is_validbRK4CGTy" title="is_valid::CGTy"><span class="n"><span class="pre">CGTy</span></span></a><span class="w"> </span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">g</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E8is_validbRK4CGTy" title="Link to this definition">#</a><br /></dt>
<dd><p>Returns true if the group has not violated any API constraints. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Implementation of publicly exposed <code class="docutils literal notranslate"><span class="pre">wrapper</span></code> API on top of basic cooperative group type APIs. This function is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>CGTy</strong> – The cooperative group class template parameter. </p>
</dd>
<dt class="field-even">Parameters<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – [in] The cooperative group for validity check.</p>
</dd>
</dl>
</dd></dl>

<dl class="cpp function">
<dt class="sig sig-object cpp" id="_CPPv4I0E4syncvRK4CGTy">
<span id="_CPPv3I0E4syncRK4CGTy"></span><span id="_CPPv2I0E4syncRK4CGTy"></span><span class="k"><span class="pre">template</span></span><span class="p"><span class="pre">&lt;</span></span><span class="k"><span class="pre">class</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">CGTy</span></span></span><span class="p"><span class="pre">&gt;</span></span><br /><span class="target" id="group___cooperative_g_a_p_i_1ga8be0e7e21f8202eff02082fe5faf482b"></span><span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">sync</span></span></span><span class="sig-paren">(</span><a class="reference internal" href="#_CPPv4I0E4syncvRK4CGTy" title="sync::CGTy"><span class="n"><span class="pre">CGTy</span></span></a><span class="w"> </span><span class="k"><span class="pre">const</span></span><span class="w"> </span><span class="p"><span class="pre">&amp;</span></span><span class="n sig-param"><span class="pre">g</span></span><span class="sig-paren">)</span><a class="headerlink" href="#_CPPv4I0E4syncvRK4CGTy" title="Link to this definition">#</a><br /></dt>
<dd><p>Synchronizes the threads in the group. </p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Implementation of publicly exposed <code class="docutils literal notranslate"><span class="pre">wrapper</span></code> API on top of basic cooperative group type APIs. This function is implemented on Linux and is under development on Microsoft Windows. </p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Template Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>CGTy</strong> – The cooperative group class template parameter. </p>
</dd>
<dt class="field-even">Parameters<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – [in] The cooperative group for synchronization.</p>
</dd>
</dl>
</dd></dl>

</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="opengl_interoperability.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">OpenGL interoperability</p>
      </div>
    </a>
    <a class="right-next"
       href="../global_defines_enums_structs_files.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Global defines, enums, structs and files</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cooperative-kernel-launches">Cooperative kernel launches</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv432hipModuleLaunchCooperativeKernel13hipFunction_tjjjjjjj11hipStream_tPPv"><code class="docutils literal notranslate"><span class="pre">hipModuleLaunchCooperativeKernel()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv443hipModuleLaunchCooperativeKernelMultiDeviceP23hipFunctionLaunchParamsjj"><code class="docutils literal notranslate"><span class="pre">hipModuleLaunchCooperativeKernelMultiDevice()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv426hipLaunchCooperativeKernelPKv4dim34dim3PPvj11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipLaunchCooperativeKernel()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv437hipLaunchCooperativeKernelMultiDeviceP15hipLaunchParamsij"><code class="docutils literal notranslate"><span class="pre">hipLaunchCooperativeKernelMultiDevice()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E26hipLaunchCooperativeKernel10hipError_t1T4dim34dim3PPvj11hipStream_t"><code class="docutils literal notranslate"><span class="pre">hipLaunchCooperativeKernel()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E37hipLaunchCooperativeKernelMultiDevice10hipError_tP15hipLaunchParamsjj"><code class="docutils literal notranslate"><span class="pre">hipLaunchCooperativeKernelMultiDevice()</span></code></a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cooperative-groups-classes">Cooperative groups classes</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N18cooperative_groups12thread_groupE"><code class="docutils literal notranslate"><span class="pre">thread_group</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N18cooperative_groups12thread_blockE"><code class="docutils literal notranslate"><span class="pre">thread_block</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N18cooperative_groups10grid_groupE"><code class="docutils literal notranslate"><span class="pre">grid_group</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N18cooperative_groups16multi_grid_groupE"><code class="docutils literal notranslate"><span class="pre">multi_grid_group</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_j0EN18cooperative_groups17thread_block_tileE"><code class="docutils literal notranslate"><span class="pre">thread_block_tile</span></code></a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4NK18cooperative_groups17thread_block_tile11thread_rankEv"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::thread_rank()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N18cooperative_groups17thread_block_tile4syncEv"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::sync()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4NK18cooperative_groups17thread_block_tile15meta_group_rankEv"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::meta_group_rank()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4NK18cooperative_groups17thread_block_tile15meta_group_sizeEv"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::meta_group_size()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile4shflE1T1Ti"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::shfl()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9shfl_downE1T1Tj"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::shfl_down()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile7shfl_upE1T1Tj"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::shfl_up()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile8shfl_xorE1T1Tj"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::shfl_xor()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4NK18cooperative_groups17thread_block_tile6ballotEi"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::ballot()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4NK18cooperative_groups17thread_block_tile3anyEi"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::any()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4NK18cooperative_groups17thread_block_tile3allEi"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::all()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9match_anyEy1T"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::match_any()</span></code></a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0ENK18cooperative_groups17thread_block_tile9match_allEy1TRi"><code class="docutils literal notranslate"><span class="pre">thread_block_tile::match_all()</span></code></a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4N18cooperative_groups15coalesced_groupE"><code class="docutils literal notranslate"><span class="pre">coalesced_group</span></code></a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cooperative-groups-construct-functions">Cooperative groups construct functions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415this_multi_gridv"><code class="docutils literal notranslate"><span class="pre">this_multi_grid()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv49this_gridv"><code class="docutils literal notranslate"><span class="pre">this_grid()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417this_thread_blockv"><code class="docutils literal notranslate"><span class="pre">this_thread_block()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv417coalesced_threadsv"><code class="docutils literal notranslate"><span class="pre">coalesced_threads()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv415tiled_partitionRK12thread_groupj"><code class="docutils literal notranslate"><span class="pre">tiled_partition()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_j0E15tiled_partition17thread_block_tileI4size10ParentCGTyERK10ParentCGTy"><code class="docutils literal notranslate"><span class="pre">tiled_partition()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv416binary_partitionRK15coalesced_groupb"><code class="docutils literal notranslate"><span class="pre">binary_partition()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I_j0E16binary_partition15coalesced_groupRK17thread_block_tileI4size6parentEb"><code class="docutils literal notranslate"><span class="pre">binary_partition()</span></code></a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#cooperative-groups-exposed-api-functions">Cooperative groups exposed API functions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E10group_size14__hip_uint32_tRK4CGTy"><code class="docutils literal notranslate"><span class="pre">group_size()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E11thread_rank14__hip_uint32_tRK4CGTy"><code class="docutils literal notranslate"><span class="pre">thread_rank()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E8is_validbRK4CGTy"><code class="docutils literal notranslate"><span class="pre">is_valid()</span></code></a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#_CPPv4I0E4syncvRK4CGTy"><code class="docutils literal notranslate"><span class="pre">sync()</span></code></a></li>
</ul>
</li>
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
