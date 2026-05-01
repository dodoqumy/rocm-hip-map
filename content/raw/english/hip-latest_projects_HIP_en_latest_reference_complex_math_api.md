---
title: "HIP complex math API &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/complex_math_api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:07:45.371331+00:00
content_hash: "269ca5ac4457361c"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="This chapter describes the complex math functions that are accessible in HIP." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, complex math functions, HIP complex math functions" name="keywords" />

    <title>HIP complex math API &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
  <script data-cfasync="false">
    document.documentElement.dataset.mode = localStorage.getItem("mode") || "";
    document.documentElement.dataset.theme = localStorage.getItem("theme") || "";
  </script>
  
  <!-- Loaded before other Sphinx assets -->
  <link href="../_static/styles/theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../_static/styles/bootstrap.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../_static/styles/pydata-sphinx-theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />

  
  <link href="../_static/vendor/fontawesome/6.5.2/css/all.min.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
  <link rel="preload" as="font" type="font/woff2" crossorigin href="../_static/vendor/fontawesome/6.5.2/webfonts/fa-solid-900.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../_static/vendor/fontawesome/6.5.2/webfonts/fa-brands-400.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../_static/vendor/fontawesome/6.5.2/webfonts/fa-regular-400.woff2" />

    <link rel="stylesheet" type="text/css" href="../_static/pygments.css?v=a746c00c" />
    <link rel="stylesheet" type="text/css" href="../_static/styles/sphinx-book-theme.css?v=a3416100" />
    <link rel="stylesheet" type="text/css" href="../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
    <link rel="stylesheet" type="text/css" href="../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../_static/sphinx-design.min.css?v=95c83b7e" />
    <link rel="stylesheet" type="text/css" href="../_static/rocm_custom.css?v=35d74aab" />
  
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b" />
<link rel="preload" as="script" href="../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b" />
  <script src="../_static/vendor/fontawesome/6.5.2/js/all.min.js?digest=dfe6caa3a7d634c4db9b"></script>

    <script src="../_static/documentation_options.js?v=75144bb1"></script>
    <script src="../_static/doctools.js?v=9a2dae69"></script>
    <script src="../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../_static/search.js?v=90a4452c"></script>
    <script src="../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
    <script src="../_static/design-tabs.js?v=f930bc37"></script>
    <script>window.MathJax = {"options": {"processHtmlClass": "tex2jax_process|mathjax_process|math|output_area"}}</script>
    <script defer="defer" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'reference/complex_math_api';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="HIP environment variables" href="env_variables.html" />
    <link rel="prev" title="HIP math API" href="math_api.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/reference/complex_math_api.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
      action="../search.html"
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
                    <img src="../_static/images/amd-header-logo.svg" alt="AMD Logo" title="AMD Logo" width="90" class="d-inline-block align-text-top hover-opacity"/>
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

  
    
  

<a class="navbar-brand logo" href="../index.html">
  
  
  
  
  
  
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
<li class="toctree-l1"><a class="reference internal" href="../what_is_hip.html">What is HIP?</a></li>
<li class="toctree-l1"><a class="reference internal" href="../hip-7-changes.html">HIP API 7.0 changes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../faq.html">Frequently asked questions</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../install/install.html">Installing HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../install/build.html">Building HIP from source</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Programming guide</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../understand/programming_model.html">Introduction to the HIP programming model</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/performance_optimization.html">Understanding GPU performance</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/hardware_implementation.html">Hardware implementation</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/compilers.html">HIP compilers</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/performance_guidelines.html">Performance guidelines</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/debugging.html">Debugging with HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/logging.html">Logging HIP activity</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../how-to/hip_runtime_api.html">Using HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/initialization.html">Initialization</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/host_memory.html">Host memory</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/device_memory.html">Device memory</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/device_memory/texture_fetching.html">Texture fetching</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/coherence_control.html">Coherence control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/unified_memory.html">Unified memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/virtual_memory.html">Virtual memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/hip_runtime_api/memory_management/stream_ordered_allocator.html">Stream Ordered Memory Allocator</a></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/error_handling.html">Error handling</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/call_stack.html">Call stack</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/asynchronous.html">Asynchronous concurrent execution</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/hipgraph.html">HIP graphs</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/cooperative_groups.html">Cooperative groups</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/multi_device.html">Multi-device management</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/opengl_interop.html">OpenGL interoperability</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/hip_runtime_api/external_interop.html">External resource interoperability</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/hip_cpp_language_extensions.html">HIP C++ language extensions</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/kernel_language_cpp_support.html">Kernel language C++ support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/hip_porting_guide.html">Porting CUDA code to HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/hip_rtc.html">Programming for HIP runtime compiler (RTC)</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/amd_clr.html">AMD compute language runtimes (CLR)</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="hip_runtime_api_reference.html">HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2 has-children"><a class="reference internal" href="hip_runtime_api/modules.html">Modules</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/initialization_and_version.html">Initialization and version</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/device_management.html">Device management</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/execution_control.html">Execution control</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/error_handling.html">Error handling</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/stream_management.html">Stream management</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/stream_memory_operations.html">Stream memory operations</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/event_management.html">Event management</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="hip_runtime_api/modules/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/memory_management_deprecated.html">Memory management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/external_resource_interoperability.html">External resource interoperability</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html">Stream ordered memory allocator</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/unified_memory_reference.html">Managed memory</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/virtual_memory_reference.html">Virtual memory management</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/texture_management.html">Texture management</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/texture_management_deprecated.html">Texture management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/modules/memory_management/surface_object.html">Surface object</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/peer_to_peer_device_memory_access.html">Peer to peer device memory access</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/context_management.html">Context management [deprecated]</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/module_management.html">Module management</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/occupancy.html">Occupancy</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/profiler_control.html">Profiler control</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/launch_api.html">Launch API</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/runtime_compilation.html">Runtime compilation</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/callback_activity_apis.html">Callback activity APIs</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/graph_management.html">Graph management</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/graphics_interoperability.html">Graphics interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/opengl_interoperability.html">OpenGL interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/modules/cooperative_groups_reference.html">Cooperative groups</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="hip_runtime_api/global_defines_enums_structs_files.html">Global defines, enums, structs and files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/group___global_defs.html">Global enum and defines</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/group___driver_types.html">Driver Types</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/files.html">File List</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="math_api.html">HIP math API</a></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">HIP complex math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="env_variables.html">HIP environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="error_codes.html">HIP error codes</a></li>
<li class="toctree-l1"><a class="reference internal" href="api_syntax.html">CUDA to HIP API Function Comparison</a></li>
<li class="toctree-l1"><a class="reference internal" href="deprecated_api_list.html">List of deprecated APIs</a></li>
<li class="toctree-l1"><a class="reference internal" href="low_fp_types.html">Low Precision Floating Point Types</a></li>
<li class="toctree-l1"><a class="reference internal" href="hardware_features.html">Hardware features</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Tutorials</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic">HIP basic examples</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples">HIP examples</a></li>
<li class="toctree-l1"><a class="reference internal" href="../tutorial/saxpy.html">SAXPY - Hello, HIP</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../tutorial/programming-patterns.html">GPU programming patterns</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../tutorial/programming-patterns/matrix_multiplication.html">Two-dimensional kernels: Matrix multiplication tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../tutorial/programming-patterns/atomic_operations_histogram.html">Atomic operations: Histogram tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../tutorial/programming-patterns/cpu_gpu_kmeans.html">CPU-GPU cooperative computing: K-means clustering tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../tutorial/programming-patterns/stencil_operations.html">Stencil operations: Image convolution tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../tutorial/programming-patterns/multikernel_bfs.html">Multi-kernel programming: breadth-first search tutorial</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../tutorial/reduction.html">Reduction</a></li>
<li class="toctree-l1"><a class="reference internal" href="../tutorial/cooperative_groups_tutorial.html">Cooperative groups</a></li>
<li class="toctree-l1"><a class="reference internal" href="../tutorial/graph_api.html">HIP Graph API Tutorial</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">About</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../license.html">License</a></li>
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
      <a href="../index.html" class="nav-link" aria-label="Home">
        <i class="fa-solid fa-home"></i>
      </a>
    </li>
    <li class="breadcrumb-item active" aria-current="page">HIP complex math API</li>
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
    <h1>HIP complex math API</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#complex-number-types">Complex Number Types</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#complex-number-functions">Complex Number Functions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#type-construction">Type Construction</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#basic-arithmetic">Basic Arithmetic</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#complex-operations">Complex Operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#type-conversion">Type Conversion</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#example-usage">Example Usage</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="hip-complex-math-api">
<span id="complex-math-api-reference"></span><h1>HIP complex math API<a class="headerlink" href="#hip-complex-math-api" title="Link to this heading">#</a></h1>
<p>HIP provides built-in support for complex number operations through specialized types and functions,
available for both single-precision (float) and double-precision (double) calculations. All complex types
and functions are available on both host and device.</p>
<p>For any complex number <code class="docutils literal notranslate"><span class="pre">z</span></code>, the form is:</p>
<div class="math notranslate nohighlight">
\[z = x + yi\]</div>
<p>where <code class="docutils literal notranslate"><span class="pre">x</span></code> is the real part and <code class="docutils literal notranslate"><span class="pre">y</span></code> is the imaginary part.</p>
<section id="complex-number-types">
<h2>Complex Number Types<a class="headerlink" href="#complex-number-types" title="Link to this heading">#</a></h2>
<p>A brief overview of the specialized data types used to represent complex numbers in HIP, available
in both single and double precision formats.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 40.0%" />
<col style="width: 60.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Type</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code></p></td>
<td><div class="line-block">
<div class="line">Complex number using single-precision (float) values</div>
<div class="line">(note: <code class="docutils literal notranslate"><span class="pre">hipComplex</span></code> is an alias of <code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code>)</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span></code></p></td>
<td><p>Complex number using double-precision (double) values</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="complex-number-functions">
<h2>Complex Number Functions<a class="headerlink" href="#complex-number-functions" title="Link to this heading">#</a></h2>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Changes have been made to small vector constructors for <code class="docutils literal notranslate"><span class="pre">hipComplex</span></code> and <code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code>
initialization, such as <code class="docutils literal notranslate"><span class="pre">float2</span></code> and <code class="docutils literal notranslate"><span class="pre">int4</span></code>. If your code previously relied
on a single value to initialize all components within a vector or complex type, you might need
to update your code.</p>
</div>
<p>A comprehensive collection of functions for creating and manipulating complex numbers, organized by
functional categories for easy reference.</p>
<section id="type-construction">
<h3>Type Construction<a class="headerlink" href="#type-construction" title="Link to this heading">#</a></h3>
<p>Functions for creating complex number objects and extracting their real and imaginary components.</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Single Precision</label><div class="sd-tab-content docutils">
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 40.0%" />
<col style="width: 60.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Function</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">make_hipFloatComplex(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">float</span> <span class="pre">a,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">float</span> <span class="pre">b</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Creates a complex number</div>
<div class="line">(note: <code class="docutils literal notranslate"><span class="pre">make_hipComplex</span></code> is an alias of <code class="docutils literal notranslate"><span class="pre">make_hipFloatComplex</span></code>)</div>
<div class="line"><span class="math notranslate nohighlight">\(z = a + bi\)</span></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">float</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCrealf(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">z</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Returns real part of z</div>
<div class="line"><span class="math notranslate nohighlight">\(\Re(z) = x\)</span></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">float</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCimagf(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">z</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Returns imaginary part of z</div>
<div class="line"><span class="math notranslate nohighlight">\(\Im(z) = y\)</span></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Double Precision</label><div class="sd-tab-content docutils">
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 40.0%" />
<col style="width: 60.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Function</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">make_hipDoubleComplex(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">double</span> <span class="pre">a,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">double</span> <span class="pre">b</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Creates a complex number</div>
<div class="line"><span class="math notranslate nohighlight">\(z = a + bi\)</span></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">double</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCreal(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">z</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Returns real part of z</div>
<div class="line"><span class="math notranslate nohighlight">\(\Re(z) = x\)</span></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">double</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCimag(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">z</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Returns imaginary part of z</div>
<div class="line"><span class="math notranslate nohighlight">\(\Im(z) = y\)</span></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</section>
<section id="basic-arithmetic">
<h3>Basic Arithmetic<a class="headerlink" href="#basic-arithmetic" title="Link to this heading">#</a></h3>
<p>Operations for performing standard arithmetic with complex numbers, including addition,
subtraction, multiplication, division, and fused multiply-add.</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-2" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
Single Precision</label><div class="sd-tab-content docutils">
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 40.0%" />
<col style="width: 60.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Function</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCaddf(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">p,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">q</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Addition of two single-precision complex values</div>
<div class="line"><span class="math notranslate nohighlight">\((a + bi) + (c + di) = (a + c) + (b + d)i\)</span></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCsubf(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">p,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">q</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Subtraction of two single-precision complex values</div>
<div class="line"><span class="math notranslate nohighlight">\((a + bi) - (c + di) = (a - c) + (b - d)i\)</span></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCmulf(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">p,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">q</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Multiplication of two single-precision complex values</div>
<div class="line"><span class="math notranslate nohighlight">\((a + bi)(c + di) = (ac - bd) + (bc + ad)i\)</span></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCdivf(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">p,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">q</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Division of two single-precision complex values</div>
<div class="line"><span class="math notranslate nohighlight">\(\frac{a + bi}{c + di} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}\)</span></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCfmaf(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipComplex</span> <span class="pre">p,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipComplex</span> <span class="pre">q,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipComplex</span> <span class="pre">r</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Fused multiply-add of three single-precision complex values</div>
<div class="line"><span class="math notranslate nohighlight">\((a + bi)(c + di) + (e + fi)\)</span></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
Double Precision</label><div class="sd-tab-content docutils">
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 40.0%" />
<col style="width: 60.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Function</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCadd(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">p,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">q</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Addition of two double-precision complex values</div>
<div class="line"><span class="math notranslate nohighlight">\((a + bi) + (c + di) = (a + c) + (b + d)i\)</span></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCsub(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">p,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">q</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Subtraction of two double-precision complex values</div>
<div class="line"><span class="math notranslate nohighlight">\((a + bi) - (c + di) = (a - c) + (b - d)i\)</span></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCmul(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">p,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">q</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Multiplication of two double-precision complex values</div>
<div class="line"><span class="math notranslate nohighlight">\((a + bi)(c + di) = (ac - bd) + (bc + ad)i\)</span></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCdiv(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">p,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">q</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Division of two double-precision complex values</div>
<div class="line"><span class="math notranslate nohighlight">\(\frac{a + bi}{c + di} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}\)</span></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCfma(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">p,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">q,</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">r</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Fused multiply-add of three double-precision complex values</div>
<div class="line"><span class="math notranslate nohighlight">\((a + bi)(c + di) + (e + fi)\)</span></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</section>
<section id="complex-operations">
<h3>Complex Operations<a class="headerlink" href="#complex-operations" title="Link to this heading">#</a></h3>
<p>Functions for complex-specific calculations, including conjugate determination and magnitude
(absolute value) computation.</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-4" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
Single Precision</label><div class="sd-tab-content docutils">
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 40.0%" />
<col style="width: 60.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Function</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipConjf(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">z</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Complex conjugate</div>
<div class="line"><span class="math notranslate nohighlight">\(\overline{a + bi} = a - bi\)</span></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">float</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCabsf(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">z</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Absolute value (magnitude)</div>
<div class="line"><span class="math notranslate nohighlight">\(|a + bi| = \sqrt{a^2 + b^2}\)</span></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">float</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCsqabsf(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">z</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Squared absolute value</div>
<div class="line"><span class="math notranslate nohighlight">\(|a + bi|^2 = a^2 + b^2\)</span></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<input id="sd-tab-item-5" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
Double Precision</label><div class="sd-tab-content docutils">
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 40.0%" />
<col style="width: 60.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Function</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipConj(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">z</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Complex conjugate</div>
<div class="line"><span class="math notranslate nohighlight">\(\overline{a + bi} = a - bi\)</span></div>
</div>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">double</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCabs(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">z</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Absolute value (magnitude)</div>
<div class="line"><span class="math notranslate nohighlight">\(|a + bi| = \sqrt{a^2 + b^2}\)</span></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">double</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipCsqabs(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">z</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Squared absolute value</div>
<div class="line"><span class="math notranslate nohighlight">\(|a + bi|^2 = a^2 + b^2\)</span></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</section>
<section id="type-conversion">
<h3>Type Conversion<a class="headerlink" href="#type-conversion" title="Link to this heading">#</a></h3>
<p>Utility functions for conversion between single-precision and double-precision complex number formats.</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 40.0%" />
<col style="width: 60.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Function</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipComplexDoubleToFloat(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span> <span class="pre">z</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><p>Converts double-precision to single-precision complex</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span></code></div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipComplexFloatToDouble(</span></code></div>
<div class="line-block">
<div class="line"><code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span> <span class="pre">z</span></code></div>
</div>
<div class="line"><code class="docutils literal notranslate"><span class="pre">)</span></code></div>
</div>
</td>
<td><p>Converts single-precision to double-precision complex</p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<section id="example-usage">
<h2>Example Usage<a class="headerlink" href="#example-usage" title="Link to this heading">#</a></h2>
<p>The following example demonstrates using complex numbers to compute the Discrete Fourier Transform (DFT)
of a simple signal on the GPU. The DFT converts a signal from the time domain to the frequency domain.
The kernel function <code class="docutils literal notranslate"><span class="pre">computeDFT</span></code> shows various HIP complex math operations in action:</p>
<ul class="simple">
<li><p>Creating complex numbers with <code class="docutils literal notranslate"><span class="pre">make_hipFloatComplex</span></code></p></li>
<li><p>Performing complex multiplication with <code class="docutils literal notranslate"><span class="pre">hipCmulf</span></code></p></li>
<li><p>Accumulating complex values with <code class="docutils literal notranslate"><span class="pre">hipCaddf</span></code></p></li>
</ul>
<p>The example also demonstrates proper use of complex number handling on both host and device, including
memory allocation, transfer, and validation of results between CPU and GPU implementations.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="math_api.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">HIP math API</p>
      </div>
    </a>
    <a class="right-next"
       href="env_variables.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">HIP environment variables</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#complex-number-types">Complex Number Types</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#complex-number-functions">Complex Number Functions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#type-construction">Type Construction</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#basic-arithmetic">Basic Arithmetic</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#complex-operations">Complex Operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#type-conversion">Type Conversion</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#example-usage">Example Usage</a></li>
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
  <script src="../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b"></script>
<script src="../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b"></script>

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
    <img id="rdc-watermark" src="../_static/images/alpha-watermark.svg" alt="DRAFT watermark"/>
</div> -->
  </body>
</html>
