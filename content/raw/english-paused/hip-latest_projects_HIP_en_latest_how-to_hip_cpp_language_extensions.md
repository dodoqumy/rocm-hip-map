---
title: "HIP C++ language extensions &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_cpp_language_extensions.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:37.652846+00:00
content_hash: "1e68a4ff4fee3290"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="This chapter describes the built-in variables and functions that are accessible from HIP kernels and HIP's C++ support. It's intended for users who are familiar with CUDA kernel syntax and want to learn how HIP differs from CUDA." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, c++ language extensions, HIP functions" name="keywords" />

    <title>HIP C++ language extensions &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/hip_cpp_language_extensions';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
    <link rel="next" title="Kernel language C++ support" href="kernel_language_cpp_support.html" />
    <link rel="prev" title="External resource interoperability" href="hip_runtime_api/external_interop.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/hip_cpp_language_extensions.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../understand/programming_model.html">Introduction to the HIP programming model</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/performance_optimization.html">Understanding GPU performance</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/hardware_implementation.html">Hardware implementation</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/compilers.html">HIP compilers</a></li>
<li class="toctree-l1"><a class="reference internal" href="performance_guidelines.html">Performance guidelines</a></li>
<li class="toctree-l1"><a class="reference internal" href="debugging.html">Debugging with HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="logging.html">Logging HIP activity</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="hip_runtime_api.html">Using HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/initialization.html">Initialization</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="hip_runtime_api/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/memory_management/host_memory.html">Host memory</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="hip_runtime_api/memory_management/device_memory.html">Device memory</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="hip_runtime_api/memory_management/device_memory/texture_fetching.html">Texture fetching</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/memory_management/coherence_control.html">Coherence control</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/memory_management/unified_memory.html">Unified memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/memory_management/virtual_memory.html">Virtual memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="hip_runtime_api/memory_management/stream_ordered_allocator.html">Stream Ordered Memory Allocator</a></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/error_handling.html">Error handling</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/call_stack.html">Call stack</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/asynchronous.html">Asynchronous concurrent execution</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/hipgraph.html">HIP graphs</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/cooperative_groups.html">Cooperative groups</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/multi_device.html">Multi-device management</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/opengl_interop.html">OpenGL interoperability</a></li>
<li class="toctree-l2"><a class="reference internal" href="hip_runtime_api/external_interop.html">External resource interoperability</a></li>
</ul>
</details></li>
<li class="toctree-l1 current active"><a class="current reference internal" href="#">HIP C++ language extensions</a></li>
<li class="toctree-l1"><a class="reference internal" href="kernel_language_cpp_support.html">Kernel language C++ support</a></li>
<li class="toctree-l1"><a class="reference internal" href="hip_porting_guide.html">Porting CUDA code to HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="hip_rtc.html">Programming for HIP runtime compiler (RTC)</a></li>
<li class="toctree-l1"><a class="reference internal" href="../understand/amd_clr.html">AMD compute language runtimes (CLR)</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../reference/hip_runtime_api_reference.html">HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2 has-children"><a class="reference internal" href="../reference/hip_runtime_api/modules.html">Modules</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/initialization_and_version.html">Initialization and version</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/device_management.html">Device management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/execution_control.html">Execution control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/error_handling.html">Error handling</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/stream_management.html">Stream management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/stream_memory_operations.html">Stream memory operations</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/event_management.html">Event management</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/memory_management_deprecated.html">Memory management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/external_resource_interoperability.html">External resource interoperability</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html">Stream ordered memory allocator</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html">Managed memory</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html">Virtual memory management</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/texture_management.html">Texture management</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/texture_management_deprecated.html">Texture management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/surface_object.html">Surface object</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/peer_to_peer_device_memory_access.html">Peer to peer device memory access</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/context_management.html">Context management [deprecated]</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/module_management.html">Module management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/occupancy.html">Occupancy</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/profiler_control.html">Profiler control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/launch_api.html">Launch API</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/runtime_compilation.html">Runtime compilation</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/callback_activity_apis.html">Callback activity APIs</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/graph_management.html">Graph management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/graphics_interoperability.html">Graphics interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/opengl_interoperability.html">OpenGL interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="../reference/hip_runtime_api/modules/cooperative_groups_reference.html">Cooperative groups</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../reference/hip_runtime_api/global_defines_enums_structs_files.html">Global defines, enums, structs and files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/group___global_defs.html">Global enum and defines</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/group___driver_types.html">Driver Types</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="../doxygen/html/files.html">File List</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/math_api.html">HIP math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/complex_math_api.html">HIP complex math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/env_variables.html">HIP environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/error_codes.html">HIP error codes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/api_syntax.html">CUDA to HIP API Function Comparison</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/deprecated_api_list.html">List of deprecated APIs</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/low_fp_types.html">Low Precision Floating Point Types</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/hardware_features.html">Hardware features</a></li>
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
    <li class="breadcrumb-item active" aria-current="page">HIP C++...</li>
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
    <h1>HIP C++ language extensions</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-qualifiers">HIP qualifiers</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#function-type-qualifiers">Function-type qualifiers</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#host">__host__</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#device">__device__</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#global">__global__</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#calling-global-functions">Calling __global__ functions</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#inline-qualifiers">Inline qualifiers</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#launch-bounds">__launch_bounds__</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#max-threads-per-block">MAX_THREADS_PER_BLOCK</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#min-warps-per-execution-unit">MIN_WARPS_PER_EXECUTION_UNIT</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-space-qualifiers">Memory space qualifiers</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">__device__</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#constant">__constant__</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#shared">__shared__</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#managed">__managed__</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#restrict">__restrict__</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#built-in-constants">Built-in constants</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#index-built-ins">Index built-ins</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#blockdim-and-griddim">blockDim and gridDim</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#threadidx-and-blockidx">threadIdx and blockIdx</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#warpsize">warpSize</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#vector-types">Vector types</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#fundamental-vector-types">Fundamental vector types</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#dim3">dim3</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#built-in-device-functions">Built-in device functions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-fence-instructions">Memory fence instructions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#synchronization-functions">Synchronization functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#math-functions">Math functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#texture-functions">Texture functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#surface-functions">Surface functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#timer-functions">Timer functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#atomic-functions">Atomic functions</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#unsafe-floating-point-atomic-operations">Unsafe floating-point atomic operations</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#warp-cross-lane-functions">Warp cross-lane functions</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warp-vote-and-ballot-functions">Warp vote and ballot functions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warp-match-functions">Warp match functions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warp-shuffle-functions">Warp shuffle functions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warp-reduction-functions">Warp reduction functions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warp-matrix-functions">Warp matrix functions</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#cooperative-groups-functions">Cooperative groups functions</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="hip-c-language-extensions">
<h1>HIP C++ language extensions<a class="headerlink" href="#hip-c-language-extensions" title="Link to this heading">#</a></h1>
<p>HIP extends the C++ language with additional features designed for programming
heterogeneous applications. These extensions mostly relate to the kernel
language, but some can also be applied to host functionality.</p>
<section id="hip-qualifiers">
<h2>HIP qualifiers<a class="headerlink" href="#hip-qualifiers" title="Link to this heading">#</a></h2>
<section id="function-type-qualifiers">
<h3>Function-type qualifiers<a class="headerlink" href="#function-type-qualifiers" title="Link to this heading">#</a></h3>
<p>HIP introduces three different function qualifiers to mark functions for
execution on the device or the host, and also adds new qualifiers to control
inlining of functions.</p>
<section id="host">
<span id="host-attr"></span><h4>__host__<a class="headerlink" href="#host" title="Link to this heading">#</a></h4>
<p>The <code class="docutils literal notranslate"><span class="pre">__host__</span></code> qualifier is used to specify functions for execution
on the host. This qualifier is implicitly defined for any function where no
<code class="docutils literal notranslate"><span class="pre">__host__</span></code>, <code class="docutils literal notranslate"><span class="pre">__device__</span></code> or <code class="docutils literal notranslate"><span class="pre">__global__</span></code> qualifier is added, in order to
not break compatibility with existing C++ functions.</p>
<p>You can’t combine <code class="docutils literal notranslate"><span class="pre">__host__</span></code> with <code class="docutils literal notranslate"><span class="pre">__global__</span></code>.</p>
</section>
<section id="device">
<h4>__device__<a class="headerlink" href="#device" title="Link to this heading">#</a></h4>
<p>The <code class="docutils literal notranslate"><span class="pre">__device__</span></code> qualifier is used to specify functions for execution on the
device. They can only be called from other <code class="docutils literal notranslate"><span class="pre">__device__</span></code> functions or from
<code class="docutils literal notranslate"><span class="pre">__global__</span></code> functions.</p>
<p>You can combine it with the <code class="docutils literal notranslate"><span class="pre">__host__</span></code> qualifier and mark functions
<code class="docutils literal notranslate"><span class="pre">__host__</span> <span class="pre">__device__</span></code>. In this case, the function is compiled for the host and
the device. Note that these functions can’t use the HIP built-ins (e.g.,
<a class="reference internal" href="#thread-and-block-idx"><span class="std std-ref">threadIdx.x</span></a> or <a class="reference internal" href="#warp-size"><span class="std std-ref">warpSize</span></a>), as
they are not available on the host. If you need to use HIP grid coordinate
functions, you can pass the necessary coordinate information as an argument.</p>
</section>
<section id="global">
<h4>__global__<a class="headerlink" href="#global" title="Link to this heading">#</a></h4>
<p>Functions marked <code class="docutils literal notranslate"><span class="pre">__global__</span></code> are executed on the device and are referred to
as kernels. Their return type must be <code class="docutils literal notranslate"><span class="pre">void</span></code>. Kernels have a special launch
mechanism, and have to be launched from the host.</p>
<p>There are some restrictions on the parameters of kernels. Kernels can’t:</p>
<ul class="simple">
<li><p>have a parameter of type <code class="docutils literal notranslate"><span class="pre">std::initializer_list</span></code> or <code class="docutils literal notranslate"><span class="pre">va_list</span></code></p></li>
<li><p>have a variable number of arguments</p></li>
<li><p>use references as parameters</p></li>
<li><p>use parameters having different sizes in host and device code, e.g. long double arguments, or structs containing long double members.</p></li>
<li><p>use struct-type arguments which have different layouts in host and device code.</p></li>
</ul>
<p>Kernels can have variadic template parameters, but only one parameter pack,
which must be the last item in the template parameter list.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Unlike CUDA, HIP does not support dynamic parallelism, meaning that kernels
can not be called from the device.</p>
</div>
<section id="calling-global-functions">
<h5>Calling __global__ functions<a class="headerlink" href="#calling-global-functions" title="Link to this heading">#</a></h5>
<p>The launch mechanism for kernels differs from standard function calls, as they
need an additional configuration, that specifies the grid and block dimensions
(i.e. the amount of threads to be launched), as well as specifying the amount of
shared memory per block and which stream to execute the kernel on.</p>
<p>Kernels are called using the triple chevron <code class="docutils literal notranslate"><span class="pre">&lt;&lt;&lt;&gt;&gt;&gt;</span></code> syntax known from CUDA,
but HIP also supports the <code class="docutils literal notranslate"><span class="pre">hipLaunchKernelGGL</span></code> macro.</p>
<p>When using <code class="docutils literal notranslate"><span class="pre">hipLaunchKernelGGL</span></code>, the first five configuration parameters must
be:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">symbol</span> <span class="pre">kernelName</span></code>: The name of the kernel you want to launch. To support
template kernels that contain several template parameters separated by use the
<code class="docutils literal notranslate"><span class="pre">HIP_KERNEL_NAME</span></code> macro to wrap the template instantiation
(<a class="reference external" href="https://rocm.docs.amd.com/projects/HIPIFY/en/latest/index.html" title="(in HIPIFY Documentation)"><span class="xref std std-doc">HIPIFY</span></a> inserts this automatically).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dim3</span> <span class="pre">gridDim</span></code>: 3D-grid dimensions that specifies the number of blocks to
launch.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dim3</span> <span class="pre">blockDim</span></code>: 3D-block dimensions that specifies the number of threads in
each block.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size_t</span> <span class="pre">dynamicShared</span></code>: The amount of additional shared dynamic memory to
allocate per block.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipStream_t</span></code>: The stream on which to run the kernel. A value of <code class="docutils literal notranslate"><span class="pre">0</span></code>
corresponds to the default stream.</p></li>
</ul>
<p>The kernel arguments are listed after the configuration parameters.</p>
<div class="highlight-cuda notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)                                \</span>
<span class="cp">{                                                            \</span>
<span class="cp">    const hipError_t err = expression;                       \</span>
<span class="cp">    if(err != hipSuccess)                                    \</span>
<span class="cp">    {                                                        \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error: &quot; &lt;&lt; hipGetErrorString(err) \</span>
<span class="cp">            &lt;&lt; &quot; at &quot; &lt;&lt; __LINE__ &lt;&lt; &quot;\n&quot;;                   \</span>
<span class="cp">    }                                                        \</span>
<span class="cp">}</span>

<span class="c1">// Performs a simple initialization of an array with the thread&#39;s index variables.</span>
<span class="c1">// This function is only available in device code.</span>
<span class="kt">__device__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">init_array</span><span class="p">(</span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">arraySize</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// globalIdx uniquely identifies a thread in a 1D launch configuration.</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">globalIdx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="nb">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="nb">blockDim</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// Each thread initializes a single element of the array.</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">globalIdx</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">arraySize</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">a</span><span class="p">[</span><span class="n">globalIdx</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">globalIdx</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="c1">// Rounds a value up to the next multiple.</span>
<span class="c1">// This function is available in host and device code.</span>
<span class="kr">__host__</span><span class="w"> </span><span class="kt">__device__</span><span class="w"> </span><span class="n">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">round_up_to_nearest_multiple</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">number</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">multiple</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="p">(</span><span class="n">number</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">multiple</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="mi">1</span><span class="p">)</span><span class="o">/</span><span class="n">multiple</span><span class="p">;</span>
<span class="p">}</span>

<span class="kr">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">example_kernel</span><span class="p">(</span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">N</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// Initialize array.</span>
<span class="w">    </span><span class="n">init_array</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="n">N</span><span class="p">);</span>
<span class="w">    </span><span class="c1">// Perform additional work:</span>
<span class="w">    </span><span class="c1">// - work with the array</span>
<span class="w">    </span><span class="c1">// - use the array in a different kernel</span>
<span class="w">    </span><span class="c1">// - ...</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">N</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">100000000</span><span class="p">;</span><span class="w"> </span><span class="c1">// problem size</span>
<span class="w">    </span><span class="n">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">blockSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">256</span><span class="p">;</span><span class="w"> </span><span class="c1">//configurable block size</span>

<span class="w">    </span><span class="c1">//needed number of blocks for the given problem size</span>
<span class="w">    </span><span class="n">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">gridSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">round_up_to_nearest_multiple</span><span class="p">(</span><span class="n">N</span><span class="p">,</span><span class="w"> </span><span class="n">blockSize</span><span class="p">);</span>

<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// allocate memory on the GPU</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">a</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">N</span><span class="p">));</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Launching kernel.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">example_kernel</span><span class="o">&lt;&lt;&lt;</span><span class="kt">dim3</span><span class="p">(</span><span class="n">gridSize</span><span class="p">),</span><span class="w"> </span><span class="kt">dim3</span><span class="p">(</span><span class="n">blockSize</span><span class="p">),</span><span class="w"> </span><span class="mi">0</span><span class="cm">/*example doesn&#39;t use shared memory*/</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="cm">/*default stream*/</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="n">N</span><span class="p">);</span>
<span class="w">    </span><span class="c1">// make sure kernel execution is finished by synchronizing. The CPU can also</span>
<span class="w">    </span><span class="c1">// execute other instructions during that time</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Kernel execution finished.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">a</span><span class="p">));</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
</section>
<section id="inline-qualifiers">
<h4>Inline qualifiers<a class="headerlink" href="#inline-qualifiers" title="Link to this heading">#</a></h4>
<p>HIP adds the <code class="docutils literal notranslate"><span class="pre">__noinline__</span></code> and <code class="docutils literal notranslate"><span class="pre">__forceinline__</span></code> function qualifiers.</p>
<p><code class="docutils literal notranslate"><span class="pre">__noinline__</span></code> is a hint to the compiler to not inline the function, whereas
<code class="docutils literal notranslate"><span class="pre">__forceinline__</span></code> forces the compiler to inline the function. These qualifiers
can be applied to both <code class="docutils literal notranslate"><span class="pre">__host__</span></code> and <code class="docutils literal notranslate"><span class="pre">__device__</span></code> functions.</p>
<p><code class="docutils literal notranslate"><span class="pre">__noinline__</span></code> and <code class="docutils literal notranslate"><span class="pre">__forceinline__</span></code> can not be used in combination.</p>
</section>
<section id="launch-bounds">
<h4>__launch_bounds__<a class="headerlink" href="#launch-bounds" title="Link to this heading">#</a></h4>
<p>GPU multiprocessors have a fixed pool of resources (primarily registers and
shared memory) which are shared by the actively running warps. Using more
resources per thread can increase executed instructions per cycle but reduces
the resources available for other warps and may therefore limit the occupancy,
i.e. the number of warps that can be executed simultaneously. Thus GPUs have to
balance resource usage between instruction- and thread-level parallelism.</p>
<p><code class="docutils literal notranslate"><span class="pre">__launch_bounds__</span></code> allows the application to provide hints that influence the
resource (primarily registers) usage of the generated code. It is a function
attribute that must be attached to a __global__ function:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">__launch_bounds__</span><span class="p">(</span><span class="n">MAX_THREADS_PER_BLOCK</span><span class="p">,</span><span class="w"> </span><span class="n">MIN_WARPS_PER_EXECUTION_UNIT</span><span class="p">)</span>
<span class="n">kernel_name</span><span class="p">(</span><span class="cm">/*args*/</span><span class="p">);</span>
</pre></div>
</div>
<p>The  <code class="docutils literal notranslate"><span class="pre">__launch_bounds__</span></code> parameters are explained in the following sections:</p>
<section id="max-threads-per-block">
<h5>MAX_THREADS_PER_BLOCK<a class="headerlink" href="#max-threads-per-block" title="Link to this heading">#</a></h5>
<p>This parameter is a guarantee from the programmer, that kernel will not be
launched with more threads than <code class="docutils literal notranslate"><span class="pre">MAX_THREADS_PER_BLOCK</span></code>.</p>
<p>If no <code class="docutils literal notranslate"><span class="pre">__launch_bounds__</span></code> are specified, <code class="docutils literal notranslate"><span class="pre">MAX_THREADS_PER_BLOCK</span></code> is
the maximum block size supported by the device (see
<a class="reference internal" href="../reference/hardware_features.html"><span class="doc">Hardware features</span></a>). Reducing <code class="docutils literal notranslate"><span class="pre">MAX_THREADS_PER_BLOCK</span></code>
allows the compiler to use more resources per thread than an unconstrained
compilation. This might however reduce the amount of blocks that can run
concurrently on a CU, thereby reducing occupancy and trading thread-level
parallelism for instruction-level parallelism.</p>
<p><code class="docutils literal notranslate"><span class="pre">MAX_THREADS_PER_BLOCK</span></code> is particularly useful in cases, where the compiler is
constrained by register usage in order to meet requirements of large block sizes
that are never used at launch time.</p>
<p>The compiler can only use the hints to manage register usage, and does not
automatically reduce shared memory usage. The compilation fails, if the compiler
can not generate code that satisfies the launch bounds.</p>
<p>On NVCC this parameter maps to the <code class="docutils literal notranslate"><span class="pre">.maxntid</span></code> PTX directive.</p>
<p>When launching kernels HIP will validate the launch configuration to make sure
the requested block size is not larger than <code class="docutils literal notranslate"><span class="pre">MAX_THREADS_PER_BLOCK</span></code> and
return an error if it is exceeded.</p>
<p>If <a class="reference internal" href="logging.html"><span class="doc">AMD_LOG_LEVEL</span></a> is set, detailed information will be shown
in the error log message, including the launch configuration of the kernel and
the specified <code class="docutils literal notranslate"><span class="pre">__launch_bounds__</span></code>.</p>
</section>
<section id="min-warps-per-execution-unit">
<h5>MIN_WARPS_PER_EXECUTION_UNIT<a class="headerlink" href="#min-warps-per-execution-unit" title="Link to this heading">#</a></h5>
<p>This parameter specifies the minimum number of warps that must be able to run
concurrently on an execution unit.
<code class="docutils literal notranslate"><span class="pre">MIN_WARPS_PER_EXECUTION_UNIT</span></code> is optional and defaults to 1 if not specified.
Since active warps compete for the same fixed pool of resources, the compiler
must constrain the resource usage of the warps. This option gives a lower
bound to the occupancy of the kernel.</p>
<p>From this parameter, the compiler derives a maximum number of registers that can
be used in the kernel. The amount of registers that can be used at most is
<span class="math notranslate nohighlight">\(\frac{\text{available registers}}{\text{MIN_WARPS_PER_EXECUTION_UNIT}}\)</span>,
but it might also have other, architecture specific, restrictions.</p>
<p>The available registers per Compute Unit are listed in
<a class="reference external" href="https://rocm.docs.amd.com/en/latest/reference/gpu-arch-specs.html" title="(in ROCm Documentation v7.2.2)"><span>GPU hardware specifications</span></a>. Beware that these values are per Compute
Unit, not per Execution Unit. On AMD GPUs a Compute Unit consists of 4 Execution
Units, also known as SIMDs, each with their own register file. For more
information see <a class="reference internal" href="../understand/hardware_implementation.html"><span class="doc">Hardware implementation</span></a>.
<code class="xref cpp cpp-struct docutils literal notranslate"><span class="pre">hipDeviceProp_t</span></code> also has a field <code class="docutils literal notranslate"><span class="pre">executionUnitsPerMultiprocessor</span></code>.</p>
</section>
</section>
</section>
<section id="memory-space-qualifiers">
<h3>Memory space qualifiers<a class="headerlink" href="#memory-space-qualifiers" title="Link to this heading">#</a></h3>
<p>HIP adds qualifiers to specify the memory space in which the variables are
located.</p>
<p>Generally, variables allocated in host memory are not directly accessible within
device code, while variables allocated in device memory are not directly
accessible from the host code. More details on this can be found in
<a class="reference internal" href="hip_runtime_api/memory_management/unified_memory.html#unified-memory"><span class="std std-ref">Unified memory management</span></a>.</p>
<section id="id1">
<h4>__device__<a class="headerlink" href="#id1" title="Link to this heading">#</a></h4>
<p>Variables marked with <code class="docutils literal notranslate"><span class="pre">__device__</span></code> reside in device memory. It can be
combined together with one of the following qualifiers, however these qualifiers
also imply the <code class="docutils literal notranslate"><span class="pre">__device__</span></code> qualifier.</p>
<p>By default it can only be accessed from the threads on the device. In order to
access it from the host, its address and size need to be queried using
<a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html#_CPPv419hipGetSymbolAddressPPvPKv" title="hipGetSymbolAddress"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGetSymbolAddress()</span></code></a> and <a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html#_CPPv416hipGetSymbolSizeP6size_tPKv" title="hipGetSymbolSize"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGetSymbolSize()</span></code></a> and copied with
<a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html#_CPPv417hipMemcpyToSymbolPKvPKv6size_t6size_t13hipMemcpyKind" title="hipMemcpyToSymbol"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpyToSymbol()</span></code></a> or <a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html#_CPPv419hipMemcpyFromSymbolPvPKv6size_t6size_t13hipMemcpyKind" title="hipMemcpyFromSymbol"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpyFromSymbol()</span></code></a>.</p>
</section>
<section id="constant">
<h4>__constant__<a class="headerlink" href="#constant" title="Link to this heading">#</a></h4>
<p>Variables marked with <code class="docutils literal notranslate"><span class="pre">__constant__</span></code> reside in device memory. Variables in
that address space are routed through the constant cache, but that address space
has a limited logical size.
This memory space is read-only from within kernels and can only be set by the
host before kernel execution.</p>
<p>To get the best performance benefit, these variables need a special access
pattern to benefit from the constant cache - the access has to be uniform within
a warp, otherwise the accesses are serialized.</p>
<p>The constant cache reduces the pressure on the other caches and may enable
higher throughput and lower latency accesses.</p>
<p>To set the <code class="docutils literal notranslate"><span class="pre">__constant__</span></code> variables the host must copy the data to the device
using <a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management.html#_CPPv417hipMemcpyToSymbolPKvPKv6size_t6size_t13hipMemcpyKind" title="hipMemcpyToSymbol"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpyToSymbol()</span></code></a>, for example:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__constant__</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">const_array</span><span class="p">[</span><span class="mi">8</span><span class="p">];</span>

<span class="kt">void</span><span class="w"> </span><span class="nf">set_constant_memory</span><span class="p">(){</span>
<span class="w">  </span><span class="kt">int</span><span class="w"> </span><span class="n">host_data</span><span class="p">[</span><span class="mi">8</span><span class="p">]</span><span class="w"> </span><span class="p">{</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">,</span><span class="mi">7</span><span class="p">,</span><span class="mi">8</span><span class="p">};</span>

<span class="w">  </span><span class="n">hipMemcpyToSymbol</span><span class="p">(</span><span class="n">const_array</span><span class="p">,</span><span class="w"> </span><span class="n">host_data</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">8</span><span class="p">);</span>

<span class="w">  </span><span class="c1">// call kernel that accesses const_array</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="shared">
<h4>__shared__<a class="headerlink" href="#shared" title="Link to this heading">#</a></h4>
<p>Variables marked with <code class="docutils literal notranslate"><span class="pre">__shared__</span></code> are only accessible by threads within the
same block and have the lifetime of that block. It is usually backed by on-chip
shared memory, providing fast access to all threads within a block, which makes
it perfectly suited for sharing variables.</p>
<p>Shared memory can be allocated statically within the kernel, but the size
of it has to be known at compile time.</p>
<p>In order to dynamically allocate shared memory during runtime, but before the
kernel is launched, the variable has to be declared  <code class="docutils literal notranslate"><span class="pre">extern</span></code>, and the kernel
launch has to specify the needed amount of <code class="docutils literal notranslate"><span class="pre">extern</span></code> shared memory in the launch
configuration. The statically allocated shared memory is allocated without this
parameter.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstdlib&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="k">extern</span><span class="w"> </span><span class="n">__shared__</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">shared_array</span><span class="p">[];</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernel</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// initialize shared memory</span>
<span class="w">    </span><span class="n">shared_array</span><span class="p">[</span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// use shared memory - synchronize to make sure, that all threads of the</span>
<span class="w">    </span><span class="c1">// block see all changes to shared memory</span>
<span class="w">    </span><span class="n">__syncthreads</span><span class="p">();</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">//shared memory in this case depends on the configurable block size</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">blockSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">256</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">sharedMemSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockSize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">);</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">gridSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>

<span class="w">    </span><span class="n">kernel</span><span class="o">&lt;&lt;&lt;</span><span class="n">dim3</span><span class="p">(</span><span class="n">gridSize</span><span class="p">),</span><span class="w"> </span><span class="n">dim3</span><span class="p">(</span><span class="n">blockSize</span><span class="p">),</span><span class="w"> </span><span class="n">sharedMemSize</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="o">&gt;&gt;&gt;</span><span class="p">();</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="k">auto</span><span class="w"> </span><span class="n">err</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipDeviceSynchronize</span><span class="p">();</span><span class="w"> </span><span class="n">err</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;HIP error &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">err</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hipGetErrorString</span><span class="p">(</span><span class="n">err</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="managed">
<h4>__managed__<a class="headerlink" href="#managed" title="Link to this heading">#</a></h4>
<p>Managed memory is a special qualifier, that makes the marked memory available on
the device and on the host. For more details see <a class="reference internal" href="hip_runtime_api/memory_management/unified_memory.html#unified-memory"><span class="std std-ref">Unified memory management</span></a>.</p>
</section>
<section id="restrict">
<h4>__restrict__<a class="headerlink" href="#restrict" title="Link to this heading">#</a></h4>
<p>The <code class="docutils literal notranslate"><span class="pre">__restrict__</span></code> keyword tells the compiler that the associated memory
pointer does not alias with any other pointer in the function. This can help the
compiler perform better optimizations. For best results, every pointer passed to
a function should use this keyword.</p>
</section>
</section>
</section>
<section id="built-in-constants">
<h2>Built-in constants<a class="headerlink" href="#built-in-constants" title="Link to this heading">#</a></h2>
<p>HIP defines some special built-in constants for use in device code.</p>
<p>These built-ins are not implicitly defined by the compiler, the
<code class="docutils literal notranslate"><span class="pre">hip_runtime.h</span></code> header has to be included instead.</p>
<section id="index-built-ins">
<h3>Index built-ins<a class="headerlink" href="#index-built-ins" title="Link to this heading">#</a></h3>
<p>Kernel code can use these identifiers to distinguish between the different
threads and blocks within a kernel.</p>
<p>These built-ins are of type dim3, and are constant for each thread, but differ
between the threads or blocks, and are initialized at kernel launch.</p>
<section id="blockdim-and-griddim">
<h4>blockDim and gridDim<a class="headerlink" href="#blockdim-and-griddim" title="Link to this heading">#</a></h4>
<p><code class="docutils literal notranslate"><span class="pre">blockDim</span></code> and <code class="docutils literal notranslate"><span class="pre">gridDim</span></code> contain the sizes specified at kernel launch.
<code class="docutils literal notranslate"><span class="pre">blockDim</span></code> contains the amount of threads in the x-, y- and z-dimensions of
the block of threads. Similarly <code class="docutils literal notranslate"><span class="pre">gridDim</span></code> contains the amount of blocks in the
grid.</p>
</section>
<section id="threadidx-and-blockidx">
<span id="thread-and-block-idx"></span><h4>threadIdx and blockIdx<a class="headerlink" href="#threadidx-and-blockidx" title="Link to this heading">#</a></h4>
<p><code class="docutils literal notranslate"><span class="pre">threadIdx</span></code> and <code class="docutils literal notranslate"><span class="pre">blockIdx</span></code> can be used to identify the threads and blocks
within the kernel.</p>
<p><code class="docutils literal notranslate"><span class="pre">threadIdx</span></code> identifies the thread within a block, meaning its values are
within <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">blockDim.{x,y,z}</span> <span class="pre">-</span> <span class="pre">1</span></code>. Likewise <code class="docutils literal notranslate"><span class="pre">blockIdx</span></code> identifies the
block within the grid, and the values are within <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">gridDim.{}</span> <span class="pre">-</span> <span class="pre">1</span></code>.</p>
<p>A global unique identifier of a three-dimensional grid can be calculated using
the following code:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="p">(</span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="p">)</span><span class="w"> </span><span class="o">+</span>
<span class="p">(</span><span class="n">threadIdx</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">y</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span>
<span class="p">(</span><span class="n">threadIdx</span><span class="p">.</span><span class="n">z</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">z</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">z</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">y</span>
</pre></div>
</div>
</section>
</section>
<section id="warpsize">
<span id="warp-size"></span><h3>warpSize<a class="headerlink" href="#warpsize" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">warpSize</span></code> constant contains the number of threads per warp for the given
target device. On AMD hardware, this is referred to as <code class="docutils literal notranslate"><span class="pre">wavefront</span> <span class="pre">size</span></code>, which
may vary depending on the architecture. For more details, see the
<a class="reference internal" href="../reference/hardware_features.html"><span class="doc">hardware features</span></a>.</p>
<p>Since <code class="docutils literal notranslate"><span class="pre">warpSize</span></code> can differ between devices, it can not be assumed to be a
compile-time constant on the host. It has to be queried using
<a class="reference internal" href="../reference/hip_runtime_api/modules/device_management.html#_CPPv421hipDeviceGetAttributePi20hipDeviceAttribute_ti" title="hipDeviceGetAttribute"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipDeviceGetAttribute()</span></code></a> or <code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipDeviceGetProperties()</span></code>, e.g.:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">warpSizeHost</span><span class="p">;</span>
<span class="n">hipDeviceGetAttribute</span><span class="p">(</span><span class="o">&amp;</span><span class="n">warpSizeHost</span><span class="p">,</span><span class="w"> </span><span class="n">hipDeviceAttributeWarpSize</span><span class="p">,</span><span class="w"> </span><span class="n">deviceId</span><span class="p">);</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><code class="docutils literal notranslate"><span class="pre">warpSize</span></code> should not be assumed to be a specific value in portable HIP
applications. NVIDIA devices return 32 for this variable; AMD devices return
64 for gfx9 and 32 for gfx10 and above. HIP doesn’t support <code class="docutils literal notranslate"><span class="pre">warpSize</span></code> of
64 on gfx10 and above. While code that assumes a <code class="docutils literal notranslate"><span class="pre">warpSize</span></code>
of 32 can run on devices with a <code class="docutils literal notranslate"><span class="pre">warpSize</span></code> of 64, it only utilizes half of
the compute resources.</p>
</div>
<p>Prior to ROCm 7.0, the warpSize parameter was a compile-time constant. Starting
with ROCm 7.0, it is early folded by the compiler, allowing it to be used in
loop bounds and enabling loop unrolling in a manner similar to a compile-time
constant warp size.</p>
<p>If compile time warp size is required, for example to select the correct mask
type or code path at compile time, the recommended approach is to determine the
warp size of the GPU on host side and setup the kernel accordingly, as shown in
the following block reduce example.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">block_reduce</span></code> kernel has a template parameter for warp size and performs
a reduction operation in two main phases:</p>
<ul class="simple">
<li><p>Shared memory reduction: Reduction is performed iteratively, halving the
number of active threads each step until only a warp remains
(32 or 64 threads, depending on the device).</p></li>
<li><p>Warp-level reduction: Once the shared memory reduction completes, the
remaining threads use warp-level shuffling to sum the remaining values. This
is done efficiently with the <code class="docutils literal notranslate"><span class="pre">__shfl_down</span></code> intrinsic, which allows threads within
the warp to exchange values without explicit synchronization.</p></li>
</ul>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-group="tab" data-sync-id="template-warpsize" for="sd-tab-item-0">
WarpSize template parameter</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">template</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">WarpSize</span><span class="o">&gt;</span>
<span class="k">using</span><span class="w"> </span><span class="n">lane_mask_t</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">typename</span><span class="w"> </span><span class="nc">std</span><span class="o">::</span><span class="n">conditional</span><span class="o">&lt;</span><span class="n">WarpSize</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">32</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="o">&gt;::</span><span class="n">type</span><span class="p">;</span>

<span class="k">template</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">WarpSize</span><span class="o">&gt;</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">block_reduce</span><span class="p">(</span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">input</span><span class="p">,</span><span class="w"> </span><span class="n">lane_mask_t</span><span class="o">&lt;</span><span class="n">WarpSize</span><span class="o">&gt;*</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">output</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">extern</span><span class="w"> </span><span class="n">__shared__</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">shared</span><span class="p">[];</span>

<span class="w">    </span><span class="c1">// Read of input with bounds check</span>
<span class="w">    </span><span class="k">auto</span><span class="w"> </span><span class="n">read_global_safe</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="o">&amp;</span><span class="p">](</span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">i</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">lane_id</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">mask_id</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">lane_mask_t</span><span class="o">&lt;</span><span class="n">WarpSize</span><span class="o">&gt;</span><span class="w"> </span><span class="n">warp_mask</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">lane_mask_t</span><span class="o">&lt;</span><span class="n">WarpSize</span><span class="o">&gt;</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">lane_id</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span><span class="w"> </span><span class="o">&amp;&amp;</span><span class="w"> </span><span class="p">(</span><span class="n">mask</span><span class="p">[</span><span class="n">mask_id</span><span class="p">]</span><span class="w"> </span><span class="o">&amp;</span><span class="w"> </span><span class="n">warp_mask</span><span class="p">)</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="n">input</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="p">};</span>

<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">,</span>
<span class="w">                        </span><span class="n">lid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="n">WarpSize</span><span class="p">,</span>
<span class="w">                        </span><span class="n">wid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">WarpSize</span><span class="p">,</span>
<span class="w">                        </span><span class="n">bid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">,</span>
<span class="w">                        </span><span class="n">gid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">bid</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">tid</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Read input buffer to shared</span>
<span class="w">    </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">read_global_safe</span><span class="p">(</span><span class="n">gid</span><span class="p">,</span><span class="w"> </span><span class="n">lid</span><span class="p">,</span><span class="w"> </span><span class="n">bid</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="p">(</span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">WarpSize</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">wid</span><span class="p">);</span>
<span class="w">    </span><span class="n">__syncthreads</span><span class="p">();</span>

<span class="w">    </span><span class="c1">// Shared reduction</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="n">WarpSize</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">/=</span><span class="w"> </span><span class="mi">2</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">i</span><span class="p">)</span>
<span class="w">        </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="p">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">];</span>
<span class="w">        </span><span class="n">__syncthreads</span><span class="p">();</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Use local variable in warp reduction  </span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w">  </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="p">];</span>
<span class="w">    </span><span class="n">__syncthreads</span><span class="p">();</span>

<span class="w">    </span><span class="c1">// This loop would be unrolled the same with the runtime warpSize.</span>
<span class="w">    </span><span class="cp">#pragma unroll</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">WarpSize</span><span class="o">/</span><span class="mi">2</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">/=</span><span class="w"> </span><span class="mi">2</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">__shfl_down</span><span class="p">(</span><span class="n">result</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Write result to output buffer</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span>
<span class="w">        </span><span class="n">output</span><span class="p">[</span><span class="n">bid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">result</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-group="tab" data-sync-id="hip-warpsize" for="sd-tab-item-1">
HIP warpSize</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">block_reduce</span><span class="p">(</span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">input</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="o">*</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">output</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">extern</span><span class="w"> </span><span class="n">__shared__</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">shared</span><span class="p">[];</span>
<span class="w">    </span><span class="c1">// Read of input with bounds check</span>
<span class="w">    </span><span class="k">auto</span><span class="w"> </span><span class="n">read_global_safe</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="o">&amp;</span><span class="p">](</span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">i</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">lane_id</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">mask_id</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="w"> </span><span class="n">warp_mask</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1ull</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">lane_id</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span><span class="w"> </span><span class="o">&amp;&amp;</span><span class="w"> </span><span class="p">(</span><span class="n">mask</span><span class="p">[</span><span class="n">mask_id</span><span class="p">]</span><span class="w"> </span><span class="o">&amp;</span><span class="w"> </span><span class="n">warp_mask</span><span class="p">)</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="n">input</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="p">};</span>

<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">,</span>
<span class="w">                    </span><span class="n">lid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="n">warpSize</span><span class="p">,</span>
<span class="w">                    </span><span class="n">wid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">warpSize</span><span class="p">,</span>
<span class="w">                    </span><span class="n">bid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">,</span>
<span class="w">                    </span><span class="n">gid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">bid</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">tid</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Read input buffer to shared</span>
<span class="w">    </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">read_global_safe</span><span class="p">(</span><span class="n">gid</span><span class="p">,</span><span class="w"> </span><span class="n">lid</span><span class="p">,</span><span class="w"> </span><span class="n">bid</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="p">(</span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">warpSize</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">wid</span><span class="p">);</span>
<span class="w">    </span><span class="n">__syncthreads</span><span class="p">();</span>

<span class="w">    </span><span class="c1">// Shared reduction</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="n">warpSize</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">/=</span><span class="w"> </span><span class="mi">2</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">i</span><span class="p">)</span>
<span class="w">        </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="p">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">i</span><span class="p">];</span>
<span class="w">        </span><span class="n">__syncthreads</span><span class="p">();</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Use local variable in warp reduction  </span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w">  </span><span class="n">shared</span><span class="p">[</span><span class="n">tid</span><span class="p">];</span>
<span class="w">    </span><span class="n">__syncthreads</span><span class="p">();</span>

<span class="w">    </span><span class="c1">// This loop would be unrolled the same with the compile-time WarpSize.</span>
<span class="w">    </span><span class="cp">#pragma unroll</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">warpSize</span><span class="o">/</span><span class="mi">2</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">/=</span><span class="w"> </span><span class="mi">2</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">__shfl_down</span><span class="p">(</span><span class="n">result</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Write result to output buffer</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span>
<span class="w">        </span><span class="n">output</span><span class="p">[</span><span class="n">bid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">result</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
</div>
<p>The host code with the main function:</p>
<ul>
<li><p>Retrieves the warp size of the GPU (<code class="docutils literal notranslate"><span class="pre">warpSizeHost</span></code>) to determine the optimal
kernel configuration.</p></li>
<li><p>Allocates device memory (<code class="docutils literal notranslate"><span class="pre">d_data</span></code> for input, <code class="docutils literal notranslate"><span class="pre">d_results</span></code> for block-wise
output) and initializes the input vector to 1.</p></li>
<li><p>Generates the mask variables for every warp and copies them to the device.</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-2" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" data-sync-group="tab" data-sync-id="template-warpsize" for="sd-tab-item-2">
WarpSize template parameter</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">template</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="w"> </span><span class="n">WarpSize</span><span class="o">&gt;</span>
<span class="kt">void</span><span class="w"> </span><span class="n">generate_and_copy_mask</span><span class="p">(</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="o">*</span><span class="n">d_mask</span><span class="p">,</span><span class="w"> </span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;&amp;</span><span class="w"> </span><span class="n">vectorExpected</span><span class="p">,</span><span class="w"> </span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">numberOfWarp</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">mask_size</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">mask_element_size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">random_device</span><span class="w"> </span><span class="n">rd</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">mt19937_64</span><span class="w"> </span><span class="nf">eng</span><span class="p">(</span><span class="n">rd</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Host side mask vector</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">lane_mask_t</span><span class="o">&lt;</span><span class="n">WarpSize</span><span class="o">&gt;&gt;</span><span class="w"> </span><span class="n">mask</span><span class="p">(</span><span class="n">mask_size</span><span class="p">);</span>
<span class="w">    </span><span class="c1">// Define uniform unsigned int distribution</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">uniform_int_distribution</span><span class="o">&lt;</span><span class="n">lane_mask_t</span><span class="o">&lt;</span><span class="n">WarpSize</span><span class="o">&gt;&gt;</span><span class="w"> </span><span class="n">distr</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// Fill up the mask </span>
<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="kt">int</span><span class="w"> </span><span class="n">count</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">        </span><span class="k">for</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">j</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numberOfWarp</span><span class="p">;</span><span class="w"> </span><span class="n">j</span><span class="o">++</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="kt">int</span><span class="w"> </span><span class="n">mask_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">numberOfWarp</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">j</span><span class="p">;</span>
<span class="w">            </span><span class="n">mask</span><span class="p">[</span><span class="n">mask_index</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">distr</span><span class="p">(</span><span class="n">eng</span><span class="p">);</span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="k">constexpr</span><span class="p">(</span><span class="n">WarpSize</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">32</span><span class="p">)</span>
<span class="w">                </span><span class="n">count</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">popcount</span><span class="p">(</span><span class="k">static_cast</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="o">&gt;</span><span class="p">(</span><span class="n">mask</span><span class="p">[</span><span class="n">mask_index</span><span class="p">]));</span>
<span class="w">            </span><span class="k">else</span>
<span class="w">                </span><span class="n">count</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">popcount</span><span class="p">(</span><span class="n">mask</span><span class="p">[</span><span class="n">mask_index</span><span class="p">]);</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="n">vectorExpected</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">=</span><span class="w"> </span><span class="n">count</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Copy the mask array</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_mask</span><span class="p">,</span><span class="w"> </span><span class="n">mask</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">mask_size</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">mask_element_size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" data-sync-group="tab" data-sync-id="hip-warpsize" for="sd-tab-item-3">
HIP warpSize</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">void</span><span class="w"> </span><span class="nf">generate_and_copy_mask</span><span class="p">(</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="w"> </span><span class="o">*</span><span class="n">d_mask</span><span class="p">,</span><span class="w"> </span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;&amp;</span><span class="w"> </span><span class="n">vectorExpected</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">warpSizeHost</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">numberOfWarp</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">mask_size</span><span class="p">,</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">mask_element_size</span><span class="p">)</span>
<span class="p">{</span><span class="w"> </span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">random_device</span><span class="w"> </span><span class="n">rd</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">mt19937_64</span><span class="w"> </span><span class="n">eng</span><span class="p">(</span><span class="n">rd</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Host side mask vector</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="o">&gt;</span><span class="w"> </span><span class="n">mask</span><span class="p">(</span><span class="n">mask_size</span><span class="p">);</span>
<span class="w">    </span><span class="c1">// Define uniform unsigned int distribution</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">uniform_int_distribution</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="o">&gt;</span><span class="w"> </span><span class="n">distr</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// Fill up the mask </span>
<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="kt">int</span><span class="w"> </span><span class="n">count</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">        </span><span class="k">for</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">j</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numberOfWarp</span><span class="p">;</span><span class="w"> </span><span class="n">j</span><span class="o">++</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="kt">int</span><span class="w"> </span><span class="n">mask_index</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">numberOfWarp</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">j</span><span class="p">;</span>
<span class="w">            </span><span class="n">mask</span><span class="p">[</span><span class="n">mask_index</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">distr</span><span class="p">(</span><span class="n">eng</span><span class="p">);</span>
<span class="w">            </span><span class="k">if</span><span class="p">(</span><span class="n">warpSizeHost</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">32</span><span class="p">)</span>
<span class="w">                </span><span class="n">count</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">popcount</span><span class="p">(</span><span class="k">static_cast</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="o">&gt;</span><span class="p">(</span><span class="n">mask</span><span class="p">[</span><span class="n">mask_index</span><span class="p">]));</span>
<span class="w">            </span><span class="k">else</span>
<span class="w">                </span><span class="n">count</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">popcount</span><span class="p">(</span><span class="n">mask</span><span class="p">[</span><span class="n">mask_index</span><span class="p">]);</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="n">vectorExpected</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">=</span><span class="w"> </span><span class="n">count</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="c1">// Copy the mask array</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_mask</span><span class="p">,</span><span class="w"> </span><span class="n">mask</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">mask_size</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">mask_element_size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
</div>
</li>
<li><p>Selects the appropriate kernel specialization based on the warp
size (either 32 or 64) and launches the kernel.</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-4" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" data-sync-group="tab" data-sync-id="template-warpsize" for="sd-tab-item-4">
WarpSize template parameter</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="w">    </span><span class="c1">// Fill up the mask variable, copy to device and select the right kernel.</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">warpSizeHost</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">32</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="c1">// Generate and copy mask arrays</span>
<span class="w">        </span><span class="n">generate_and_copy_mask</span><span class="o">&lt;</span><span class="mi">32</span><span class="o">&gt;</span><span class="p">(</span><span class="n">d_mask</span><span class="p">,</span><span class="w"> </span><span class="n">vectorExpected</span><span class="p">,</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">numberOfWarp</span><span class="p">,</span><span class="w"> </span><span class="n">mask_size</span><span class="p">,</span><span class="w"> </span><span class="n">mask_element_size</span><span class="p">);</span>

<span class="w">        </span><span class="c1">// Start the kernel</span>
<span class="w">        </span><span class="n">block_reduce</span><span class="o">&lt;</span><span class="mi">32</span><span class="o">&gt;&lt;&lt;&lt;</span><span class="n">dim3</span><span class="p">(</span><span class="n">numOfBlocks</span><span class="p">),</span><span class="w"> </span><span class="n">dim3</span><span class="p">(</span><span class="n">threadsPerBlock</span><span class="p">),</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_data</span><span class="p">)</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span>
<span class="w">            </span><span class="n">d_data</span><span class="p">,</span>
<span class="w">            </span><span class="k">static_cast</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint32_t</span><span class="o">*&gt;</span><span class="p">(</span><span class="n">d_mask</span><span class="p">),</span>
<span class="w">            </span><span class="n">d_results</span><span class="p">,</span>
<span class="w">            </span><span class="n">arraySize</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="k">else</span><span class="w"> </span><span class="k">if</span><span class="p">(</span><span class="n">warpSizeHost</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">64</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="c1">// Generate and copy mask arrays</span>
<span class="w">        </span><span class="n">generate_and_copy_mask</span><span class="o">&lt;</span><span class="mi">64</span><span class="o">&gt;</span><span class="p">(</span><span class="n">d_mask</span><span class="p">,</span><span class="w"> </span><span class="n">vectorExpected</span><span class="p">,</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">numberOfWarp</span><span class="p">,</span><span class="w"> </span><span class="n">mask_size</span><span class="p">,</span><span class="w"> </span><span class="n">mask_element_size</span><span class="p">);</span>

<span class="w">        </span><span class="c1">// Start the kernel</span>
<span class="w">        </span><span class="n">block_reduce</span><span class="o">&lt;</span><span class="mi">64</span><span class="o">&gt;&lt;&lt;&lt;</span><span class="n">dim3</span><span class="p">(</span><span class="n">numOfBlocks</span><span class="p">),</span><span class="w"> </span><span class="n">dim3</span><span class="p">(</span><span class="n">threadsPerBlock</span><span class="p">),</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_data</span><span class="p">)</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span>
<span class="w">            </span><span class="n">d_data</span><span class="p">,</span>
<span class="w">            </span><span class="k">static_cast</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="o">*&gt;</span><span class="p">(</span><span class="n">d_mask</span><span class="p">),</span>
<span class="w">            </span><span class="n">d_results</span><span class="p">,</span>
<span class="w">            </span><span class="n">arraySize</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="k">else</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Unsupported warp size.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_FAILURE</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-5" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" data-sync-group="tab" data-sync-id="hip-warpsize" for="sd-tab-item-5">
HIP warpSize</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="w">    </span><span class="c1">// Generate and copy mask arrays</span>
<span class="w">    </span><span class="n">generate_and_copy_mask</span><span class="p">(</span>
<span class="w">        </span><span class="n">d_mask</span><span class="p">,</span>
<span class="w">        </span><span class="n">vectorExpected</span><span class="p">,</span>
<span class="w">        </span><span class="n">warpSizeHost</span><span class="p">,</span>
<span class="w">        </span><span class="n">numOfBlocks</span><span class="p">,</span>
<span class="w">        </span><span class="n">numberOfWarp</span><span class="p">,</span>
<span class="w">        </span><span class="n">mask_size</span><span class="p">,</span>
<span class="w">        </span><span class="n">mask_element_size</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Start the kernel</span>
<span class="w">    </span><span class="n">block_reduce</span><span class="o">&lt;&lt;&lt;</span><span class="n">dim3</span><span class="p">(</span><span class="n">numOfBlocks</span><span class="p">),</span><span class="w"> </span><span class="n">dim3</span><span class="p">(</span><span class="n">threadsPerBlock</span><span class="p">),</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_data</span><span class="p">)</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span>
<span class="w">        </span><span class="n">d_data</span><span class="p">,</span>
<span class="w">        </span><span class="n">d_mask</span><span class="p">,</span>
<span class="w">        </span><span class="n">d_results</span><span class="p">,</span>
<span class="w">        </span><span class="n">arraySize</span><span class="p">);</span>
</pre></div>
</div>
</div>
</div>
</li>
<li><p>Synchronizes the device and copies the results back to the host.</p></li>
<li><p>Checks that each block’s sum is equal with the expected mask bit count,
verifying the reduction’s correctness.</p></li>
<li><p>Frees the device memory to prevent memory leaks.</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The <code class="docutils literal notranslate"><span class="pre">warpSize</span></code> runtime example code is also provided for comparison purposes
and the full example codes are located in the <a class="reference external" href="https://github.com/ROCm/hip/tree/docs/develop/docs/tools/example_codes">tools folder</a>.</p>
<p>The variable <code class="docutils literal notranslate"><span class="pre">warpSize</span></code> can be used for loop bounds and supports
loop unrolling similarly to the template parameter <code class="docutils literal notranslate"><span class="pre">WarpSize</span></code>.</p>
</div>
<p>For users who still require a compile-time constant warp size as a macro on the
device side, it can be defined manually based on the target device architecture,
as shown in the following example.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#if defined(__GFX8__) || defined(__GFX9__)</span>
<span class="w">  </span><span class="cp">#define WarpSize 64</span>
<span class="cp">#else</span>
<span class="w">  </span><span class="cp">#define WarpSize 32</span>
<span class="cp">#endif</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><code class="docutils literal notranslate"><span class="pre">mwavefrontsize64</span></code> compiler option is not supported by HIP runtime, that’s
why the architecture based compile time selector is an acceptable approach.</p>
</div>
</section>
</section>
<section id="vector-types">
<h2>Vector types<a class="headerlink" href="#vector-types" title="Link to this heading">#</a></h2>
<p>These types are not automatically provided by the compiler. The
<code class="docutils literal notranslate"><span class="pre">hip_vector_types.h</span></code> header, which is also included by <code class="docutils literal notranslate"><span class="pre">hip_runtime.h</span></code> has
to be included to use these types.</p>
<section id="fundamental-vector-types">
<h3>Fundamental vector types<a class="headerlink" href="#fundamental-vector-types" title="Link to this heading">#</a></h3>
<p>Fundamental vector types derive from the <a class="reference external" href="https://en.cppreference.com/w/cpp/language/types">fundamental C++ integral and
floating-point types</a>. These
types are defined in <code class="docutils literal notranslate"><span class="pre">hip_vector_types.h</span></code>, which is included by
<code class="docutils literal notranslate"><span class="pre">hip_runtime.h</span></code>.</p>
<p>All vector types can be created with <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">3</span></code> or <code class="docutils literal notranslate"><span class="pre">4</span></code> elements, the
corresponding type is <code class="docutils literal notranslate"><span class="pre">&lt;fundamental_type&gt;i</span></code>, where <code class="docutils literal notranslate"><span class="pre">i</span></code> is the number of
elements.</p>
<p>All vector types support a constructor function of the form
<code class="docutils literal notranslate"><span class="pre">make_&lt;type_name&gt;()</span></code>. For example,
<code class="docutils literal notranslate"><span class="pre">float3</span> <span class="pre">make_float3(float</span> <span class="pre">x,</span> <span class="pre">float</span> <span class="pre">y,</span> <span class="pre">float</span> <span class="pre">z)</span></code> creates a vector of type
<code class="docutils literal notranslate"><span class="pre">float3</span></code> with value <code class="docutils literal notranslate"><span class="pre">(x,y,z)</span></code>.
The elements of the vectors can be accessed using their members <code class="docutils literal notranslate"><span class="pre">x</span></code>, <code class="docutils literal notranslate"><span class="pre">y</span></code>,
<code class="docutils literal notranslate"><span class="pre">z</span></code>, and <code class="docutils literal notranslate"><span class="pre">w</span></code>.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">double2</span><span class="w"> </span><span class="n">d2_vec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">make_double2</span><span class="p">(</span><span class="mf">2.0</span><span class="p">,</span><span class="w"> </span><span class="mf">4.0</span><span class="p">);</span>
<span class="kt">double</span><span class="w"> </span><span class="n">first_elem</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">d2_vec</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
</pre></div>
</div>
<p>HIP supports vectors created from the following fundamental types:</p>
<div class="pst-scrollable-table-container"><table class="table">
<colgroup>
<col style="width: 50.0%" />
<col style="width: 50.0%" />
</colgroup>
<tbody>
<tr class="row-odd"><td><p><strong>Integral Types</strong></p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">char</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">uchar</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">short</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">ushort</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">int</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">uint</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">long</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">ulong</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">longlong</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">ulonglong</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><strong>Floating-Point Types</strong></p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">float</span></code></p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">double</span></code></p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="dim3">
<span id="id2"></span><h3>dim3<a class="headerlink" href="#dim3" title="Link to this heading">#</a></h3>
<p><code class="docutils literal notranslate"><span class="pre">dim3</span></code> is a special three-dimensional unsigned integer vector type that is
commonly used to specify grid and group dimensions for kernel launch
configurations.</p>
<p>Its constructor accepts up to three arguments. The unspecified dimensions are
initialized to 1.</p>
</section>
</section>
<section id="built-in-device-functions">
<h2>Built-in device functions<a class="headerlink" href="#built-in-device-functions" title="Link to this heading">#</a></h2>
<section id="memory-fence-instructions">
<span id="id3"></span><h3>Memory fence instructions<a class="headerlink" href="#memory-fence-instructions" title="Link to this heading">#</a></h3>
<p>HIP does not enforce strict ordering on memory operations, meaning, that the
order in which memory accesses are executed, is not necessarily the order in
which other threads observe these changes. So it can not be assumed, that data
written by one thread is visible by another thread without synchronization.</p>
<p>Memory fences are a way to enforce a sequentially consistent order on the memory
operations. This means, that all writes to memory made before a memory fence are
observed by all threads after the fence. The scope of these fences depends on
what specific memory fence is called.</p>
<p>HIP supports <code class="docutils literal notranslate"><span class="pre">__threadfence()</span></code>, <code class="docutils literal notranslate"><span class="pre">__threadfence_block()</span></code> and
<code class="docutils literal notranslate"><span class="pre">__threadfence_system()</span></code>:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">__threadfence_block()</span></code> orders memory accesses for all threads within a thread block.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__threadfence()</span></code> orders memory accesses for all threads on a device.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__threadfence_system()</span></code> orders memory accesses for all threads in the system, making writes to memory visible to other devices and the host</p></li>
</ul>
</section>
<section id="synchronization-functions">
<span id="id4"></span><h3>Synchronization functions<a class="headerlink" href="#synchronization-functions" title="Link to this heading">#</a></h3>
<p>Synchronization functions cause all threads in a group to wait at this
synchronization point until all threads reached it. These functions implicitly
include a <a class="reference internal" href="#memory-fence-instructions"><span class="std std-ref">threadfence</span></a>, thereby ensuring
visibility of memory accesses for the threads in the group.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">__syncthreads()</span></code> function comes in different versions.</p>
<p><code class="docutils literal notranslate"><span class="pre">void</span> <span class="pre">__syncthreads()</span></code> simply synchronizes the threads of a block. The other
versions additionally evaluate a predicate:</p>
<p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">__syncthreads_count(int</span> <span class="pre">predicate)</span></code> returns the number of threads for
which the predicate evaluates to non-zero.</p>
<p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">__syncthreads_and(int</span> <span class="pre">predicate)</span></code> returns non-zero if the predicate
evaluates to non-zero for all threads.</p>
<p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">__syncthreads_or(int</span> <span class="pre">predicate)</span></code> returns non-zero if any of the
predicates evaluates to non-zero.</p>
<p>The Cooperative Groups API offers options to synchronize threads on a developer
defined set of thread groups. For further information, check the
<a class="reference internal" href="../reference/hip_runtime_api/modules/cooperative_groups_reference.html#cooperative-groups-reference"><span class="std std-ref">Cooperative Groups API reference</span></a> or the
<a class="reference internal" href="hip_runtime_api/cooperative_groups.html#cooperative-groups-how-to"><span class="std std-ref">Cooperative Groups section in the programming guide</span></a>.</p>
</section>
<section id="math-functions">
<h3>Math functions<a class="headerlink" href="#math-functions" title="Link to this heading">#</a></h3>
<p>HIP-Clang supports a set of math operations that are callable from the device.
HIP supports most of the device functions supported by CUDA. These are described
on <a class="reference internal" href="../reference/math_api.html#math-api-reference"><span class="std std-ref">Math API page</span></a>.</p>
</section>
<section id="texture-functions">
<h3>Texture functions<a class="headerlink" href="#texture-functions" title="Link to this heading">#</a></h3>
<p>The supported texture functions are listed in <code class="docutils literal notranslate"><span class="pre">texture_fetch_functions.h</span></code> and
<code class="docutils literal notranslate"><span class="pre">texture_indirect_functions.h</span></code> header files in the
<a class="reference external" href="https://github.com/ROCm/clr/blob/develop/hipamd/include/hip/amd_detail">HIP-AMD backend repository</a>.</p>
<p>Texture functions are not supported on some devices. To determine if texture functions are supported
on your device, use <code class="docutils literal notranslate"><span class="pre">Macro</span> <span class="pre">__HIP_NO_IMAGE_SUPPORT</span> <span class="pre">==</span> <span class="pre">1</span></code>. You can query the attribute
<code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeImageSupport</span></code> to check if texture functions are supported in the host runtime
code.</p>
</section>
<section id="surface-functions">
<h3>Surface functions<a class="headerlink" href="#surface-functions" title="Link to this heading">#</a></h3>
<p>The supported surface functions are located on <a class="reference internal" href="../reference/hip_runtime_api/modules/memory_management/surface_object.html#surface-object-reference"><span class="std std-ref">Surface object reference
page</span></a>.</p>
</section>
<section id="timer-functions">
<h3>Timer functions<a class="headerlink" href="#timer-functions" title="Link to this heading">#</a></h3>
<p>HIP provides device functions to read a high-resolution timer from within the
kernel.</p>
<p>The following functions count the cycles on the device, where the rate varies
with the actual frequency.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">clock_t</span><span class="w"> </span><span class="n">clock</span><span class="p">()</span>
<span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">clock64</span><span class="p">()</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><code class="docutils literal notranslate"><span class="pre">clock()</span></code> and <code class="docutils literal notranslate"><span class="pre">clock64()</span></code> do not work properly on AMD RDNA3 (GFX11) graphic processors.</p>
</div>
<p>The difference between the returned values represents the cycles used.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernel</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">  </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">start</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">clock64</span><span class="p">();</span>
<span class="w">  </span><span class="c1">// kernel code</span>
<span class="w">  </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">stop</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">clock64</span><span class="p">();</span>
<span class="w">  </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">cycles</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">stop</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">start</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">long</span> <span class="pre">long</span> <span class="pre">int</span> <span class="pre">wall_clock64()</span></code> returns the wall clock time on the device, with a constant, fixed frequency.
The frequency is device dependent and can be queried using:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">wallClkRate</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="c1">//in kilohertz</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceGetAttribute</span><span class="p">(</span><span class="o">&amp;</span><span class="n">wallClkRate</span><span class="p">,</span><span class="w"> </span><span class="n">hipDeviceAttributeWallClockRate</span><span class="p">,</span><span class="w"> </span><span class="n">deviceId</span><span class="p">));</span>
</pre></div>
</div>
</section>
<section id="atomic-functions">
<span id="id5"></span><h3>Atomic functions<a class="headerlink" href="#atomic-functions" title="Link to this heading">#</a></h3>
<p>Atomic functions are read-modify-write (RMW) operations, whose result is visible
to all other threads on the scope of the atomic operation, once the operation
completes.</p>
<p>If multiple instructions from different devices or threads target the same
memory location, the instructions are serialized in an undefined order.</p>
<p>Atomic operations in kernels can operate on block scope (i.e. shared memory),
device scope (global memory), or system scope (system memory), depending on
<a class="reference internal" href="../reference/hardware_features.html"><span class="doc">hardware support</span></a>.</p>
<p>The listed functions are also available with the <code class="docutils literal notranslate"><span class="pre">_system</span></code> (e.g.
<code class="docutils literal notranslate"><span class="pre">atomicAdd_system</span></code>) suffix, operating on system scope, which includes host
memory and other GPUs’ memory. The functions without suffix operate on shared
or global memory on the executing device, depending on the memory space of the
variable.</p>
<p>HIP supports the following atomic operations, where <code class="docutils literal notranslate"><span class="pre">TYPE</span></code> is one of <code class="docutils literal notranslate"><span class="pre">int</span></code>,
<code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code>, <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span></code>, <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span></code>, <code class="docutils literal notranslate"><span class="pre">float</span></code> or
<code class="docutils literal notranslate"><span class="pre">double</span></code>, while <code class="docutils literal notranslate"><span class="pre">INTEGER</span></code> is <code class="docutils literal notranslate"><span class="pre">int</span></code>, <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code>, <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span></code>,
<code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span></code>:</p>
<div class="pst-scrollable-table-container"><table class="table" id="id6">
<caption><span class="caption-text">Atomic operations</span><a class="headerlink" href="#id6" title="Link to this table">#</a></caption>
<tbody>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">TYPE</span> <span class="pre">atomicAdd(TYPE*</span> <span class="pre">address,</span> <span class="pre">TYPE</span> <span class="pre">val)</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">TYPE</span> <span class="pre">atomicSub(TYPE*</span> <span class="pre">address,</span> <span class="pre">TYPE</span> <span class="pre">val)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">TYPE</span> <span class="pre">atomicMin(TYPE*</span> <span class="pre">address,</span> <span class="pre">TYPE</span> <span class="pre">val)</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">long</span> <span class="pre">long</span> <span class="pre">atomicMin(long</span> <span class="pre">long*</span> <span class="pre">address,</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">val)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">TYPE</span> <span class="pre">atomicMax(TYPE*</span> <span class="pre">address,</span> <span class="pre">TYPE</span> <span class="pre">val)</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">long</span> <span class="pre">long</span> <span class="pre">atomicMax(long</span> <span class="pre">long*</span> <span class="pre">address,</span> <span class="pre">long</span> <span class="pre">long</span> <span class="pre">val)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">TYPE</span> <span class="pre">atomicExch(TYPE*</span> <span class="pre">address,</span> <span class="pre">TYPE</span> <span class="pre">val)</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">TYPE</span> <span class="pre">atomicCAS(TYPE*</span> <span class="pre">address,</span> <span class="pre">TYPE</span> <span class="pre">compare,</span> <span class="pre">TYPE</span> <span class="pre">val)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">INTEGER</span> <span class="pre">atomicAnd(INTEGER*</span> <span class="pre">address,</span> <span class="pre">INTEGER</span> <span class="pre">val)</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">INTEGER</span> <span class="pre">atomicOr(INTEGER*</span> <span class="pre">address,</span> <span class="pre">INTEGER</span> <span class="pre">val)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">INTEGER</span> <span class="pre">atomicXor(INTEGER*</span> <span class="pre">address,</span> <span class="pre">INTEGER</span> <span class="pre">val)</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span> <span class="pre">atomicInc(unsigned</span> <span class="pre">int*</span> <span class="pre">address)</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span> <span class="pre">atomicDec(unsigned</span> <span class="pre">int*</span> <span class="pre">address)</span></code></p></td>
</tr>
</tbody>
</table>
</div>
<section id="unsafe-floating-point-atomic-operations">
<h4>Unsafe floating-point atomic operations<a class="headerlink" href="#unsafe-floating-point-atomic-operations" title="Link to this heading">#</a></h4>
<p>Some HIP devices support fast atomic operations on floating-point values. For
example, <code class="docutils literal notranslate"><span class="pre">atomicAdd</span></code> on single- or double-precision floating-point values may
generate a hardware instruction that is faster than emulating the atomic
operation using an atomic compare-and-swap (CAS) loop.</p>
<p>On some devices, fast atomic instructions can produce results that differ from
the version implemented with atomic CAS loops. For example, some devices
will use different rounding or denormal modes, and some devices produce
incorrect answers if fast floating-point atomic instructions target fine-grained
memory allocations.</p>
<p>The HIP-Clang compiler offers compile-time options to control the generation of
unsafe atomic instructions. By default the compiler does not generate unsafe
instructions. This is the same behaviour as with the <code class="docutils literal notranslate"><span class="pre">-mno-unsafe-fp-atomics</span></code>
compilation flag. The <code class="docutils literal notranslate"><span class="pre">-munsafe-fp-atomics</span></code> flag indicates to the compiler
that all floating-point atomic function calls are allowed to use an unsafe
version, if one exists. For example, on some devices, this flag indicates to the
compiler that no floating-point <code class="docutils literal notranslate"><span class="pre">atomicAdd</span></code> function can target fine-grained
memory. These options are applied globally for the entire compilation.</p>
<p>HIP provides special functions that override the global compiler option for safe
or unsafe atomic functions.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">safe</span></code> prefix always generates safe atomic operations, even when
<code class="docutils literal notranslate"><span class="pre">-munsafe-fp-atomics</span></code> is used, whereas <code class="docutils literal notranslate"><span class="pre">unsafe</span></code> always generates fast atomic
instructions, even when <code class="docutils literal notranslate"><span class="pre">-mno-unsafe-fp-atomics</span></code>. The following table lists
the safe and unsafe atomic functions, where <code class="docutils literal notranslate"><span class="pre">FLOAT_TYPE</span></code> is either <code class="docutils literal notranslate"><span class="pre">float</span></code>
or <code class="docutils literal notranslate"><span class="pre">double</span></code>.</p>
<div class="pst-scrollable-table-container"><table class="table" id="id7">
<caption><span class="caption-text">AMD specific atomic operations</span><a class="headerlink" href="#id7" title="Link to this table">#</a></caption>
<tbody>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">FLOAT_TYPE</span> <span class="pre">unsafeAtomicAdd(FLOAT_TYPE*</span> <span class="pre">address,</span> <span class="pre">FLOAT_TYPE</span> <span class="pre">val)</span></code></p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">FLOAT_TYPE</span> <span class="pre">safeAtomicAdd(FLOAT_TYPE*</span> <span class="pre">address,</span> <span class="pre">FLOAT_TYPE</span> <span class="pre">val)</span></code></p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<section id="warp-cross-lane-functions">
<span id="warp-cross-lane"></span><h3>Warp cross-lane functions<a class="headerlink" href="#warp-cross-lane-functions" title="Link to this heading">#</a></h3>
<p>Threads in a warp are referred to as <code class="docutils literal notranslate"><span class="pre">lanes</span></code> and are numbered from <code class="docutils literal notranslate"><span class="pre">0</span></code> to
<code class="docutils literal notranslate"><span class="pre">warpSize</span> <span class="pre">-</span> <span class="pre">1</span></code>. Warp cross-lane functions cooperate across all lanes in a
warp. AMD GPUs guarantee, that all warp lanes are executed in lockstep, whereas
NVIDIA GPUs that support Independent Thread Scheduling might require additional
synchronization, or the use of the <code class="docutils literal notranslate"><span class="pre">__sync</span></code> variants.</p>
<p>Note that different devices can have different warp sizes. You should query the
<a class="reference internal" href="#warp-size"><span class="std std-ref">warpSize</span></a> in portable code and not assume a fixed warp size.</p>
<p>All mask values returned or accepted by these built-ins are 64-bit unsigned
integer values, even when compiled for a device with 32 threads per warp. On
such devices the higher bits are unused. CUDA code ported to HIP requires
changes to ensure that the correct type is used.</p>
<p>Note that the <code class="docutils literal notranslate"><span class="pre">__sync</span></code> variants are available in ROCm 7.0 (and enabled by
default, unlike in previous versions). They can be disabled by setting the
preprocessor macro <code class="docutils literal notranslate"><span class="pre">HIP_DISABLE_WARP_SYNC_BUILTINS</span></code>.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">_sync</span></code> variants require a 64-bit unsigned integer mask argument that
specifies the lanes of the warp that will participate. Each participating thread
must have its own bit set in its mask argument, and all active threads specified
in any mask argument must execute the same call with the same mask, otherwise
the result is undefined. The implementation includes a static assert to check
that the program source uses the correct type for the mask.</p>
<section id="warp-vote-and-ballot-functions">
<span id="warp-vote-functions"></span><h4>Warp vote and ballot functions<a class="headerlink" href="#warp-vote-and-ballot-functions" title="Link to this heading">#</a></h4>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">__all</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">predicate</span><span class="p">)</span>
<span class="kt">int</span><span class="w"> </span><span class="n">__any</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">predicate</span><span class="p">)</span>
<span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">__ballot</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">predicate</span><span class="p">)</span>
<span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">__activemask</span><span class="p">()</span>

<span class="kt">int</span><span class="w"> </span><span class="n">__all_sync</span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">predicate</span><span class="p">)</span>
<span class="kt">int</span><span class="w"> </span><span class="n">__any_sync</span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">predicate</span><span class="p">)</span>
<span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">__ballot_sync</span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">predicate</span><span class="p">)</span>
</pre></div>
</div>
<p>You can use <code class="docutils literal notranslate"><span class="pre">__any</span></code> and <code class="docutils literal notranslate"><span class="pre">__all</span></code> to get a summary view of the predicates evaluated by the
participating lanes.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">__any()</span></code>: Returns 1 if the predicate is non-zero for any participating lane, otherwise it returns 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">__all()</span></code>: Returns 1 if the predicate is non-zero for all participating lanes, otherwise it returns 0.</p></li>
</ul>
<p>To determine if the target platform supports the any/all instruction, you can
query the <code class="docutils literal notranslate"><span class="pre">hasWarpVote</span></code> device property on the host or use the
<code class="docutils literal notranslate"><span class="pre">HIP_ARCH_HAS_WARP_VOTE</span></code> compiler definition in device code.</p>
<p><code class="docutils literal notranslate"><span class="pre">__ballot</span></code> returns a bit mask containing the 1-bit predicate value from each
lane. The nth bit of the result contains the bit contributed by the nth lane.</p>
<p><code class="docutils literal notranslate"><span class="pre">__activemask()</span></code> returns a bit mask of currently active warp lanes. The nth
bit of the result is 1 if the nth lane is active.</p>
<p>Note that the <code class="docutils literal notranslate"><span class="pre">__ballot</span></code> and <code class="docutils literal notranslate"><span class="pre">__activemask</span></code> built-ins in HIP have a 64-bit return
value (unlike the 32-bit value returned by the CUDA built-ins). Code ported from
CUDA should be adapted to support the larger warp sizes that the HIP version
requires.</p>
<p>Applications can test whether the target platform supports the <code class="docutils literal notranslate"><span class="pre">__ballot</span></code> or
<code class="docutils literal notranslate"><span class="pre">__activemask</span></code> instructions using the <code class="docutils literal notranslate"><span class="pre">hasWarpBallot</span></code> device property in host
code or the <code class="docutils literal notranslate"><span class="pre">HIP_ARCH_HAS_WARP_BALLOT</span></code> macro defined by the compiler for device
code.</p>
</section>
<section id="warp-match-functions">
<h4>Warp match functions<a class="headerlink" href="#warp-match-functions" title="Link to this heading">#</a></h4>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">__match_any</span><span class="p">(</span><span class="n">T</span><span class="w"> </span><span class="n">value</span><span class="p">)</span>
<span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">__match_all</span><span class="p">(</span><span class="n">T</span><span class="w"> </span><span class="n">value</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">pred</span><span class="p">)</span>

<span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">__match_any_sync</span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">value</span><span class="p">)</span>
<span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">__match_all_sync</span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">value</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">pred</span><span class="p">)</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">T</span></code> can be a 32-bit integer type, 64-bit integer type or a single precision or
double precision floating point type.</p>
<p><code class="docutils literal notranslate"><span class="pre">__match_any</span></code> returns a bit mask where the n-th bit is set to 1 if the n-th
lane has the same <code class="docutils literal notranslate"><span class="pre">value</span></code> as the current lane, and 0 otherwise.</p>
<p><code class="docutils literal notranslate"><span class="pre">__match_all</span></code> returns a bit mask with the bits of the participating lanes are
set to 1 if all lanes have the same <code class="docutils literal notranslate"><span class="pre">value</span></code>, and 0 otherwise.
The predicate <code class="docutils literal notranslate"><span class="pre">pred</span></code> is set to true if all participating threads have the same
<code class="docutils literal notranslate"><span class="pre">value</span></code>, and false otherwise.</p>
</section>
<section id="warp-shuffle-functions">
<h4>Warp shuffle functions<a class="headerlink" href="#warp-shuffle-functions" title="Link to this heading">#</a></h4>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">T</span><span class="w"> </span><span class="nf">__shfl</span><span class="w">      </span><span class="p">(</span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">srcLane</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">width</span><span class="o">=</span><span class="n">warpSize</span><span class="p">);</span>
<span class="n">T</span><span class="w"> </span><span class="nf">__shfl_up</span><span class="w">   </span><span class="p">(</span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">delta</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">width</span><span class="o">=</span><span class="n">warpSize</span><span class="p">);</span>
<span class="n">T</span><span class="w"> </span><span class="nf">__shfl_down</span><span class="w"> </span><span class="p">(</span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">delta</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">width</span><span class="o">=</span><span class="n">warpSize</span><span class="p">);</span>
<span class="n">T</span><span class="w"> </span><span class="nf">__shfl_xor</span><span class="w">  </span><span class="p">(</span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">laneMask</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">width</span><span class="o">=</span><span class="n">warpSize</span><span class="p">);</span>

<span class="n">T</span><span class="w"> </span><span class="nf">__shfl_sync</span><span class="w">      </span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">srcLane</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">width</span><span class="o">=</span><span class="n">warpSize</span><span class="p">);</span>
<span class="n">T</span><span class="w"> </span><span class="nf">__shfl_up_sync</span><span class="w">   </span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">delta</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">width</span><span class="o">=</span><span class="n">warpSize</span><span class="p">);</span>
<span class="n">T</span><span class="w"> </span><span class="nf">__shfl_down_sync</span><span class="w"> </span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">delta</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">width</span><span class="o">=</span><span class="n">warpSize</span><span class="p">);</span>
<span class="n">T</span><span class="w"> </span><span class="nf">__shfl_xor_sync</span><span class="w">  </span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">laneMask</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">width</span><span class="o">=</span><span class="n">warpSize</span><span class="p">);</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">T</span></code> can be a 32-bit integer type, 64-bit integer type or a single precision or
double precision floating point type.</p>
<p>The warp shuffle functions exchange values between threads within a warp.</p>
<p>The optional <code class="docutils literal notranslate"><span class="pre">width</span></code> argument specifies subgroups, in which the warp can be
divided to share the variables.
It has to be a power of two smaller than or equal to <code class="docutils literal notranslate"><span class="pre">warpSize</span></code>. If it is
smaller than <code class="docutils literal notranslate"><span class="pre">warpSize</span></code>, the warp is grouped into separate groups, that are each
indexed from 0 to width as if it was its own entity, and only the lanes within
that subgroup participate in the shuffle. The lane indices in the subgroup are
given by <code class="docutils literal notranslate"><span class="pre">laneIdx</span> <span class="pre">%</span> <span class="pre">width</span></code>.</p>
<p>The different shuffle functions behave as following:</p>
<dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">__shfl</span></code></dt><dd><p>The thread reads the value from the lane specified in <code class="docutils literal notranslate"><span class="pre">srcLane</span></code>.</p>
</dd>
<dt><code class="docutils literal notranslate"><span class="pre">__shfl_up</span></code></dt><dd><p>The thread reads <code class="docutils literal notranslate"><span class="pre">var</span></code> from lane <code class="docutils literal notranslate"><span class="pre">laneIdx</span> <span class="pre">-</span> <span class="pre">delta</span></code>, thereby “shuffling”
the values of the lanes of the warp “up”. If the resulting source lane is out
of range, the thread returns its own <code class="docutils literal notranslate"><span class="pre">var</span></code>.</p>
</dd>
<dt><code class="docutils literal notranslate"><span class="pre">__shfl_down</span></code></dt><dd><p>The thread reads <code class="docutils literal notranslate"><span class="pre">var</span></code> from lane <code class="docutils literal notranslate"><span class="pre">laneIdx</span> <span class="pre">+</span> <span class="pre">delta</span></code>, thereby “shuffling”
the values of the lanes of the warp “down”. If the resulting source lane is
out of range, the thread returns its own <code class="docutils literal notranslate"><span class="pre">var</span></code>.</p>
</dd>
<dt><code class="docutils literal notranslate"><span class="pre">__shfl_xor</span></code></dt><dd><p>The thread reads <code class="docutils literal notranslate"><span class="pre">var</span></code> from lane <code class="docutils literal notranslate"><span class="pre">laneIdx</span> <span class="pre">xor</span> <span class="pre">lane_mask</span></code>. If <code class="docutils literal notranslate"><span class="pre">width</span></code> is
smaller than <code class="docutils literal notranslate"><span class="pre">warpSize</span></code>, the threads can read values from subgroups before
the current subgroup. If it tries to read values from later subgroups, the
function returns the <code class="docutils literal notranslate"><span class="pre">var</span></code> of the calling thread.</p>
</dd>
</dl>
</section>
<section id="warp-reduction-functions">
<h4>Warp reduction functions<a class="headerlink" href="#warp-reduction-functions" title="Link to this heading">#</a></h4>
<p>Arithmetic reduces:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">T</span><span class="w"> </span><span class="nf">__reduce_add_sync</span><span class="w"> </span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">);</span>
<span class="n">T</span><span class="w"> </span><span class="nf">__reduce_min_sync</span><span class="w"> </span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">);</span>
<span class="n">T</span><span class="w"> </span><span class="nf">__reduce_max_sync</span><span class="w"> </span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">);</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">T</span></code> can be:</p>
<ul class="simple">
<li><p>On Nvidia platform: <code class="docutils literal notranslate"><span class="pre">int</span></code> or <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p></li>
<li><p>On AMD platform: <code class="docutils literal notranslate"><span class="pre">int</span></code> or <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code>; if the user defines the macro <code class="docutils literal notranslate"><span class="pre">HIP_ENABLE_EXTRA_WARP_SYNC_TYPES</span></code>, then: <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span></code>, <code class="docutils literal notranslate"><span class="pre">long</span> <span class="pre">long</span></code>, <code class="docutils literal notranslate"><span class="pre">half</span></code>/<code class="docutils literal notranslate"><span class="pre">single</span></code>/<code class="docutils literal notranslate"><span class="pre">double</span></code> precision floating</p></li>
</ul>
<p>point types are also be supported.</p>
<p>Returns the aggregated result of the arithmetic operation, where each of the participating threads
(i.e. the ones mentioned on the mask) contribute <code class="docutils literal notranslate"><span class="pre">var</span></code>.</p>
<p>NOTE: for type <code class="docutils literal notranslate"><span class="pre">half</span></code>, these intrinsics are not available in environments where the arithmetic operators are not available for
that type.</p>
<p>Logical reduces:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">T</span><span class="w"> </span><span class="nf">__reduce_and_sync</span><span class="w"> </span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">);</span>
<span class="n">T</span><span class="w"> </span><span class="nf">__reduce_or_sync</span><span class="w">  </span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">);</span>
<span class="n">T</span><span class="w"> </span><span class="nf">__reduce_xor_sync</span><span class="w"> </span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">T</span><span class="w"> </span><span class="n">var</span><span class="p">);</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">T</span></code> can be:</p>
<ul class="simple">
<li><p>On Nvidia platform: <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code></p></li>
<li><p>On AMD platform: <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code>, and if the user defines the macro <code class="docutils literal notranslate"><span class="pre">HIP_ENABLE_EXTRA_WARP_SYNC_TYPES</span></code>, then <code class="docutils literal notranslate"><span class="pre">int</span></code>, <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span></code> or <code class="docutils literal notranslate"><span class="pre">long</span> <span class="pre">long</span></code> are also supported</p></li>
</ul>
<p>Returns the result of the aggregated logical AND/OR/XOR operation where each of the participating threads
(i.e. the ones mentioned on the mask) contribute <code class="docutils literal notranslate"><span class="pre">var</span></code>.</p>
<p>The mask argument is a 64-bit unsigned integer that specifies the lanes in the warp that
participate in cross-lane communication with the calling lane. Each participating thread must have its own
bit set in its mask argument, and all active threads specified in any mask argument must execute the same
call with the same mask, otherwise the result is undefined.</p>
<p>Informational note: On the AMD platform, <strong>masks that start from lane zero and have no “holes” use faster cross-lane operations and
exhibit better performance</strong> than masks with “holes” (example of mask with no holes: 0xFF and with holes: 0xFB;
the reduction with 0xFF is faster).</p>
<p>These functions do not provide a memory barrier on any platform.</p>
</section>
<section id="warp-matrix-functions">
<h4>Warp matrix functions<a class="headerlink" href="#warp-matrix-functions" title="Link to this heading">#</a></h4>
<p>Warp matrix functions allow a warp to cooperatively operate on small matrices
that have elements spread over lanes in an unspecified manner.</p>
<p>HIP does not support warp matrix types or functions.</p>
</section>
</section>
<section id="cooperative-groups-functions">
<h3>Cooperative groups functions<a class="headerlink" href="#cooperative-groups-functions" title="Link to this heading">#</a></h3>
<p>You can use cooperative groups to synchronize groups of threads across thread
blocks. It also provide a way of communicating between these groups.</p>
<p>For further information, check the <a class="reference internal" href="../reference/hip_runtime_api/modules/cooperative_groups_reference.html#cooperative-groups-reference"><span class="std std-ref">Cooperative Groups API reference</span></a> or the <a class="reference internal" href="hip_runtime_api/cooperative_groups.html#cooperative-groups-how-to"><span class="std std-ref">Cooperative Groups programming
guide</span></a>.</p>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="hip_runtime_api/external_interop.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">External resource interoperability</p>
      </div>
    </a>
    <a class="right-next"
       href="kernel_language_cpp_support.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Kernel language C++ support</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-qualifiers">HIP qualifiers</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#function-type-qualifiers">Function-type qualifiers</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#host">__host__</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#device">__device__</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#global">__global__</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#calling-global-functions">Calling __global__ functions</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#inline-qualifiers">Inline qualifiers</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#launch-bounds">__launch_bounds__</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#max-threads-per-block">MAX_THREADS_PER_BLOCK</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#min-warps-per-execution-unit">MIN_WARPS_PER_EXECUTION_UNIT</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-space-qualifiers">Memory space qualifiers</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">__device__</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#constant">__constant__</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#shared">__shared__</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#managed">__managed__</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#restrict">__restrict__</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#built-in-constants">Built-in constants</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#index-built-ins">Index built-ins</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#blockdim-and-griddim">blockDim and gridDim</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#threadidx-and-blockidx">threadIdx and blockIdx</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#warpsize">warpSize</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#vector-types">Vector types</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#fundamental-vector-types">Fundamental vector types</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#dim3">dim3</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#built-in-device-functions">Built-in device functions</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-fence-instructions">Memory fence instructions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#synchronization-functions">Synchronization functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#math-functions">Math functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#texture-functions">Texture functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#surface-functions">Surface functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#timer-functions">Timer functions</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#atomic-functions">Atomic functions</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#unsafe-floating-point-atomic-operations">Unsafe floating-point atomic operations</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#warp-cross-lane-functions">Warp cross-lane functions</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warp-vote-and-ballot-functions">Warp vote and ballot functions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warp-match-functions">Warp match functions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warp-shuffle-functions">Warp shuffle functions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warp-reduction-functions">Warp reduction functions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warp-matrix-functions">Warp matrix functions</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#cooperative-groups-functions">Cooperative groups functions</a></li>
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
