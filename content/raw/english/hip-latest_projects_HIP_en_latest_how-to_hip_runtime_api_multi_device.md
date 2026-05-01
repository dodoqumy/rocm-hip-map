---
title: "Multi-device management &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/multi_device.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:48.710105+00:00
content_hash: "1e8d25f8afc54e95"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="This chapter describes how to use multiple devices on one host." name="description" />
<meta content="ROCm, HIP, multi-device, multiple, GPUs, devices" name="keywords" />

    <title>Multi-device management &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
  <script data-cfasync="false">
    document.documentElement.dataset.mode = localStorage.getItem("mode") || "";
    document.documentElement.dataset.theme = localStorage.getItem("theme") || "";
  </script>
  
  <!-- Loaded before other Sphinx assets -->
  <link href="../../_static/styles/theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../../_static/styles/bootstrap.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
<link href="../../_static/styles/pydata-sphinx-theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />

  
  <link href="../../_static/vendor/fontawesome/6.5.2/css/all.min.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet" />
  <link rel="preload" as="font" type="font/woff2" crossorigin href="../../_static/vendor/fontawesome/6.5.2/webfonts/fa-solid-900.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../_static/vendor/fontawesome/6.5.2/webfonts/fa-brands-400.woff2" />
<link rel="preload" as="font" type="font/woff2" crossorigin href="../../_static/vendor/fontawesome/6.5.2/webfonts/fa-regular-400.woff2" />

    <link rel="stylesheet" type="text/css" href="../../_static/pygments.css?v=a746c00c" />
    <link rel="stylesheet" type="text/css" href="../../_static/styles/sphinx-book-theme.css?v=a3416100" />
    <link rel="stylesheet" type="text/css" href="../../_static/mystnb.4510f1fc1dee50b3e5859aac5469c37c29e427902b24a333a5f9fcb2f0b3ac41.css" />
    <link rel="stylesheet" type="text/css" href="../../_static/copybutton.css?v=76b2166b" />
    <link rel="stylesheet" type="text/css" href="../../_static/custom.css?v=643846e8" />
    <link rel="stylesheet" type="text/css" href="../../_static/rocm_header.css?v=9557e3d1" />
    <link rel="stylesheet" type="text/css" href="../../_static/rocm_footer.css?v=7095035a" />
    <link rel="stylesheet" type="text/css" href="../../_static/fonts.css?v=fcff5274" />
    <link rel="stylesheet" type="text/css" href="../../_static/sphinx-design.min.css?v=95c83b7e" />
    <link rel="stylesheet" type="text/css" href="../../_static/rocm_custom.css?v=35d74aab" />
  
  <!-- Pre-loaded scripts that we'll load fully later -->
  <link rel="preload" as="script" href="../../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b" />
<link rel="preload" as="script" href="../../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b" />
  <script src="../../_static/vendor/fontawesome/6.5.2/js/all.min.js?digest=dfe6caa3a7d634c4db9b"></script>

    <script src="../../_static/documentation_options.js?v=75144bb1"></script>
    <script src="../../_static/doctools.js?v=9a2dae69"></script>
    <script src="../../_static/sphinx_highlight.js?v=dc90522c"></script>
    <script src="../../_static/clipboard.min.js?v=a7894cd8"></script>
    <script src="../../_static/copybutton.js?v=91c4cb68"></script>
    <script async="async" src="../../_static/code_word_breaks.js?v=327952c4"></script>
    <script async="async" src="../../_static/renameVersionLinks.js?v=929fe5e4"></script>
    <script async="async" src="../../_static/rdcMisc.js?v=01f88d96"></script>
    <script async="async" src="../../_static/theme_mode_captions.js?v=15f4ec5d"></script>
    <script defer="defer" src="../../_static/search.js?v=90a4452c"></script>
    <script src="../../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
    <script src="../../_static/design-tabs.js?v=f930bc37"></script>
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/hip_runtime_api/multi_device';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="OpenGL interoperability" href="opengl_interop.html" />
    <link rel="prev" title="Cooperative groups" href="cooperative_groups.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/hip_runtime_api/multi_device.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
      action="../../search.html"
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
                    <img src="../../_static/images/amd-header-logo.svg" alt="AMD Logo" title="AMD Logo" width="90" class="d-inline-block align-text-top hover-opacity"/>
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

  
    
  

<a class="navbar-brand logo" href="../../index.html">
  
  
  
  
  
  
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
<li class="toctree-l1"><a class="reference internal" href="../../what_is_hip.html">What is HIP?</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../hip-7-changes.html">HIP API 7.0 changes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../faq.html">Frequently asked questions</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../install/install.html">Installing HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../install/build.html">Building HIP from source</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Programming guide</span></p>
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../understand/programming_model.html">Introduction to the HIP programming model</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../understand/performance_optimization.html">Understanding GPU performance</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../understand/hardware_implementation.html">Hardware implementation</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../understand/compilers.html">HIP compilers</a></li>
<li class="toctree-l1"><a class="reference internal" href="../performance_guidelines.html">Performance guidelines</a></li>
<li class="toctree-l1"><a class="reference internal" href="../debugging.html">Debugging with HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../logging.html">Logging HIP activity</a></li>
<li class="toctree-l1 current active has-children"><a class="reference internal" href="../hip_runtime_api.html">Using HIP runtime API</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2"><a class="reference internal" href="initialization.html">Initialization</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="memory_management/host_memory.html">Host memory</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="memory_management/device_memory.html">Device memory</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="memory_management/device_memory/texture_fetching.html">Texture fetching</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="memory_management/coherence_control.html">Coherence control</a></li>
<li class="toctree-l3"><a class="reference internal" href="memory_management/unified_memory.html">Unified memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="memory_management/virtual_memory.html">Virtual memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="memory_management/stream_ordered_allocator.html">Stream Ordered Memory Allocator</a></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="error_handling.html">Error handling</a></li>
<li class="toctree-l2"><a class="reference internal" href="call_stack.html">Call stack</a></li>
<li class="toctree-l2"><a class="reference internal" href="asynchronous.html">Asynchronous concurrent execution</a></li>
<li class="toctree-l2"><a class="reference internal" href="hipgraph.html">HIP graphs</a></li>
<li class="toctree-l2"><a class="reference internal" href="cooperative_groups.html">Cooperative groups</a></li>
<li class="toctree-l2 current active"><a class="current reference internal" href="#">Multi-device management</a></li>
<li class="toctree-l2"><a class="reference internal" href="opengl_interop.html">OpenGL interoperability</a></li>
<li class="toctree-l2"><a class="reference internal" href="external_interop.html">External resource interoperability</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../hip_cpp_language_extensions.html">HIP C++ language extensions</a></li>
<li class="toctree-l1"><a class="reference internal" href="../kernel_language_cpp_support.html">Kernel language C++ support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../hip_porting_guide.html">Porting CUDA code to HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../hip_rtc.html">Programming for HIP runtime compiler (RTC)</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../understand/amd_clr.html">AMD compute language runtimes (CLR)</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../../reference/hip_runtime_api_reference.html">HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2 has-children"><a class="reference internal" href="../../reference/hip_runtime_api/modules.html">Modules</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/initialization_and_version.html">Initialization and version</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/device_management.html">Device management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/execution_control.html">Execution control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/error_handling.html">Error handling</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/stream_management.html">Stream management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/stream_memory_operations.html">Stream memory operations</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/event_management.html">Event management</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/memory_management_deprecated.html">Memory management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/external_resource_interoperability.html">External resource interoperability</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html">Stream ordered memory allocator</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html">Managed memory</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html">Virtual memory management</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/texture_management.html">Texture management</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/texture_management_deprecated.html">Texture management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/surface_object.html">Surface object</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/peer_to_peer_device_memory_access.html">Peer to peer device memory access</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/context_management.html">Context management [deprecated]</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/module_management.html">Module management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/occupancy.html">Occupancy</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/profiler_control.html">Profiler control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/launch_api.html">Launch API</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/runtime_compilation.html">Runtime compilation</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/callback_activity_apis.html">Callback activity APIs</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html">Graph management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/graphics_interoperability.html">Graphics interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/opengl_interoperability.html">OpenGL interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../reference/hip_runtime_api/modules/cooperative_groups_reference.html">Cooperative groups</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../../reference/hip_runtime_api/global_defines_enums_structs_files.html">Global defines, enums, structs and files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../doxygen/html/group___global_defs.html">Global enum and defines</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../doxygen/html/group___driver_types.html">Driver Types</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../doxygen/html/annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../doxygen/html/files.html">File List</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/math_api.html">HIP math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/complex_math_api.html">HIP complex math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/env_variables.html">HIP environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/error_codes.html">HIP error codes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/api_syntax.html">CUDA to HIP API Function Comparison</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/deprecated_api_list.html">List of deprecated APIs</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/low_fp_types.html">Low Precision Floating Point Types</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../reference/hardware_features.html">Hardware features</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Tutorials</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic">HIP basic examples</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/ROCm/rocm-examples">HIP examples</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../tutorial/saxpy.html">SAXPY - Hello, HIP</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../../tutorial/programming-patterns.html">GPU programming patterns</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../../tutorial/programming-patterns/matrix_multiplication.html">Two-dimensional kernels: Matrix multiplication tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../tutorial/programming-patterns/atomic_operations_histogram.html">Atomic operations: Histogram tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../tutorial/programming-patterns/cpu_gpu_kmeans.html">CPU-GPU cooperative computing: K-means clustering tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../tutorial/programming-patterns/stencil_operations.html">Stencil operations: Image convolution tutorial</a></li>
<li class="toctree-l2"><a class="reference internal" href="../../tutorial/programming-patterns/multikernel_bfs.html">Multi-kernel programming: breadth-first search tutorial</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../tutorial/reduction.html">Reduction</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../tutorial/cooperative_groups_tutorial.html">Cooperative groups</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../tutorial/graph_api.html">HIP Graph API Tutorial</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">About</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../license.html">License</a></li>
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
      <a href="../../index.html" class="nav-link" aria-label="Home">
        <i class="fa-solid fa-home"></i>
      </a>
    </li>
    
    <li class="breadcrumb-item"><a href="../hip_runtime_api.html" class="nav-link">Using HIP runtime API</a></li>
    
    <li class="breadcrumb-item active" aria-current="page">Multi-device...</li>
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
    <h1>Multi-device management</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#device-enumeration">Device enumeration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#device-selection">Device selection</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#stream-and-event-behavior">Stream and event behavior</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#peer-to-peer-memory-access">Peer-to-peer memory access</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="multi-device-management">
<span id="multi-device"></span><h1>Multi-device management<a class="headerlink" href="#multi-device-management" title="Link to this heading">#</a></h1>
<section id="device-enumeration">
<h2>Device enumeration<a class="headerlink" href="#device-enumeration" title="Link to this heading">#</a></h2>
<p>Device enumeration involves identifying all the available GPUs connected to the
host system. A single host machine can have multiple GPUs, each with its own
unique identifier. By listing these devices, you can decide which GPU to use
for computation. The host queries the system to count and list all connected
GPUs that support the chosen <code class="docutils literal notranslate"><span class="pre">HIP_PLATFORM</span></code>, ensuring that the application
can leverage the full computational power available. Typically, applications
list devices and their properties for deployment planning, and also make
dynamic selections during runtime to ensure optimal performance.</p>
<p>If the application does not define a specific GPU, device 0 is selected.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstdlib&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)                        \</span>
<span class="cp">{                                                    \</span>
<span class="cp">    const hipError_t status = expression;            \</span>
<span class="cp">    if (status != hipSuccess)                        \</span>
<span class="cp">    {                                                \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error &quot; &lt;&lt; status          \</span>
<span class="cp">                &lt;&lt; &quot;: &quot; &lt;&lt; hipGetErrorString(status) \</span>
<span class="cp">                &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot;         \</span>
<span class="cp">                &lt;&lt; __LINE__ &lt;&lt; std::endl;            \</span>
<span class="cp">        std::exit(EXIT_FAILURE);                     \</span>
<span class="cp">    }                                                \</span>
<span class="cp">}</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceCount</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDeviceCount</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceCount</span><span class="p">));</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Number of devices: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceCount</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">deviceId</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">deviceId</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">deviceCount</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">deviceId</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">hipDeviceProp_t</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">;</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDeviceProperties</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceProp</span><span class="p">,</span><span class="w"> </span><span class="n">deviceId</span><span class="p">));</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Device &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceId</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; Properties:&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;  Name: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">name</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;  Total Global Memory: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">totalGlobalMem</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="p">(</span><span class="mi">1024</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1024</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; MiB&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;  Shared Memory per Block: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">sharedMemPerBlock</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mi">1024</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; KiB&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;  Registers per Block: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">regsPerBlock</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;  Warp Size: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">warpSize</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;  Max Threads per Block: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">maxThreadsPerBlock</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;  Max Threads per Multiprocessor: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">maxThreadsPerMultiProcessor</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;  Number of Multiprocessors: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">multiProcessorCount</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;  Max Threads Dimensions: [&quot;</span>
<span class="w">                </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">maxThreadsDim</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;, &quot;</span>
<span class="w">                </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">maxThreadsDim</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;, &quot;</span>
<span class="w">                </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">maxThreadsDim</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;]&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;  Max Grid Size: [&quot;</span>
<span class="w">                </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">maxGridSize</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;, &quot;</span>
<span class="w">                </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">maxGridSize</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;, &quot;</span>
<span class="w">                </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">deviceProp</span><span class="p">.</span><span class="n">maxGridSize</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;]&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="device-selection">
<span id="multi-device-selection"></span><h2>Device selection<a class="headerlink" href="#device-selection" title="Link to this heading">#</a></h2>
<p>Once you have enumerated the available GPUs, the next step is to select a
specific device for computation. This involves setting the active GPU that will
execute subsequent operations. This step is crucial in multi-GPU systems where
different GPUs might have different capabilities or workloads. By selecting the
appropriate device, you ensure that the computational tasks are directed to the
correct GPU, optimizing performance and resource utilization.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstddef&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstdlib&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)                        \</span>
<span class="cp">{                                                    \</span>
<span class="cp">    const hipError_t status = expression;            \</span>
<span class="cp">    if (status != hipSuccess)                        \</span>
<span class="cp">    {                                                \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error &quot; &lt;&lt; status          \</span>
<span class="cp">                &lt;&lt; &quot;: &quot; &lt;&lt; hipGetErrorString(status) \</span>
<span class="cp">                &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot;         \</span>
<span class="cp">                &lt;&lt; __LINE__ &lt;&lt; std::endl;            \</span>
<span class="cp">        std::exit(EXIT_FAILURE);                     \</span>
<span class="cp">    }                                                \</span>
<span class="cp">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">simpleKernel</span><span class="p">(</span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">elems</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">idx</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">elems</span><span class="p">)</span>
<span class="w">        </span><span class="n">data</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceCount</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDeviceCount</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceCount</span><span class="p">));</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">deviceCount</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">2</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;This example requires at least two HIP devices.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">deviceData0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">deviceData1</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">elems</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">elems</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">double</span><span class="p">);</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceId0</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceId1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Set device 0 and perform operations</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId0</span><span class="p">));</span><span class="w"> </span><span class="c1">// Set device 0 as current</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">));</span><span class="w"> </span><span class="c1">// Allocate memory on device 0</span>
<span class="w">    </span><span class="n">simpleKernel</span><span class="o">&lt;&lt;&lt;</span><span class="mi">8</span><span class="p">,</span><span class="w"> </span><span class="mi">128</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">elems</span><span class="p">);</span><span class="w"> </span><span class="c1">// Launch kernel on device 0</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Set device 1 and perform operations</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId1</span><span class="p">));</span><span class="w"> </span><span class="c1">// Set device 1 as current</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">));</span><span class="w"> </span><span class="c1">// Allocate memory on device 1</span>
<span class="w">    </span><span class="n">simpleKernel</span><span class="o">&lt;&lt;&lt;</span><span class="mi">8</span><span class="p">,</span><span class="w"> </span><span class="mi">128</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">elems</span><span class="p">);</span><span class="w"> </span><span class="c1">// Launch kernel on device 1</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Copy result from device 0</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">hostData0</span><span class="p">[</span><span class="n">elems</span><span class="p">];</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">hostData0</span><span class="p">,</span><span class="w"> </span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Copy result from device 1</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">hostData1</span><span class="p">[</span><span class="n">elems</span><span class="p">];</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">hostData1</span><span class="p">,</span><span class="w"> </span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Display results from both devices</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Device 0 data: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hostData0</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Device 1 data: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hostData1</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Free device memory</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">deviceData0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">deviceData1</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="stream-and-event-behavior">
<h2>Stream and event behavior<a class="headerlink" href="#stream-and-event-behavior" title="Link to this heading">#</a></h2>
<p>In a multi-device system, streams and events are essential for efficient
parallel computation and synchronization. Streams enable asynchronous task
execution, allowing multiple devices to process data concurrently without
blocking one another. Events provide a mechanism for synchronizing operations
across streams and devices, ensuring that tasks on one device are completed
before dependent tasks on another device begin. This coordination prevents race
conditions and optimizes data flow in multi-GPU systems. Together, streams and
events maximize performance by enabling parallel execution, load balancing, and
effective resource utilization across heterogeneous hardware.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstddef&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstdlib&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)                        \</span>
<span class="cp">{                                                    \</span>
<span class="cp">    const hipError_t status = expression;            \</span>
<span class="cp">    if (status != hipSuccess)                        \</span>
<span class="cp">    {                                                \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error &quot; &lt;&lt; status          \</span>
<span class="cp">                &lt;&lt; &quot;: &quot; &lt;&lt; hipGetErrorString(status) \</span>
<span class="cp">                &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot;         \</span>
<span class="cp">                &lt;&lt; __LINE__ &lt;&lt; std::endl;            \</span>
<span class="cp">        std::exit(EXIT_FAILURE);                     \</span>
<span class="cp">    }                                                \</span>
<span class="cp">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">simpleKernel</span><span class="p">(</span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">elems</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">idx</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">elems</span><span class="p">)</span>
<span class="w">        </span><span class="n">data</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">numDevices</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDeviceCount</span><span class="p">(</span><span class="o">&amp;</span><span class="n">numDevices</span><span class="p">));</span>

<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">numDevices</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">2</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;This example requires at least two HIP devices.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">deviceData0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">deviceData1</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">elems</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">elems</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">double</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Create streams and events for each device</span>
<span class="w">    </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">stream0</span><span class="p">,</span><span class="w"> </span><span class="n">stream1</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipEvent_t</span><span class="w"> </span><span class="n">startEvent0</span><span class="p">,</span><span class="w"> </span><span class="n">stopEvent0</span><span class="p">,</span><span class="w"> </span><span class="n">startEvent1</span><span class="p">,</span><span class="w"> </span><span class="n">stopEvent1</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Initialize device 0</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="mi">0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">stream0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">startEvent0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">stopEvent0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Initialize device 1</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="mi">1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">stream1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">startEvent1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">stopEvent1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Record the start event on device 0</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="mi">0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventRecord</span><span class="p">(</span><span class="n">startEvent0</span><span class="p">,</span><span class="w"> </span><span class="n">stream0</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Launch the kernel asynchronously on device 0</span>
<span class="w">    </span><span class="n">simpleKernel</span><span class="o">&lt;&lt;&lt;</span><span class="mi">8</span><span class="p">,</span><span class="w"> </span><span class="mi">128</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">stream0</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">elems</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Record the stop event on device 0</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventRecord</span><span class="p">(</span><span class="n">stopEvent0</span><span class="p">,</span><span class="w"> </span><span class="n">stream0</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Wait for the stop event on device 0 to complete</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventSynchronize</span><span class="p">(</span><span class="n">stopEvent0</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Record the start event on device 1</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="mi">1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventRecord</span><span class="p">(</span><span class="n">startEvent1</span><span class="p">,</span><span class="w"> </span><span class="n">stream1</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Launch the kernel asynchronously on device 1</span>
<span class="w">    </span><span class="n">simpleKernel</span><span class="o">&lt;&lt;&lt;</span><span class="mi">8</span><span class="p">,</span><span class="w"> </span><span class="mi">128</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">stream1</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">elems</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Record the stop event on device 1</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventRecord</span><span class="p">(</span><span class="n">stopEvent1</span><span class="p">,</span><span class="w"> </span><span class="n">stream1</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Wait for the stop event on device 1 to complete</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventSynchronize</span><span class="p">(</span><span class="n">stopEvent1</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Calculate elapsed time between the events for both devices</span>
<span class="w">    </span><span class="kt">float</span><span class="w"> </span><span class="n">milliseconds0</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">milliseconds1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventElapsedTime</span><span class="p">(</span><span class="o">&amp;</span><span class="n">milliseconds0</span><span class="p">,</span><span class="w"> </span><span class="n">startEvent0</span><span class="p">,</span><span class="w"> </span><span class="n">stopEvent0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventElapsedTime</span><span class="p">(</span><span class="o">&amp;</span><span class="n">milliseconds1</span><span class="p">,</span><span class="w"> </span><span class="n">startEvent1</span><span class="p">,</span><span class="w"> </span><span class="n">stopEvent1</span><span class="p">));</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Elapsed time on GPU 0: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">milliseconds0</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; ms&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Elapsed time on GPU 1: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">milliseconds1</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; ms&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Cleanup for device 0</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="mi">0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventDestroy</span><span class="p">(</span><span class="n">startEvent0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventDestroy</span><span class="p">(</span><span class="n">stopEvent0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamSynchronize</span><span class="p">(</span><span class="n">stream0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamDestroy</span><span class="p">(</span><span class="n">stream0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">deviceData0</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Cleanup for device 1</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="mi">1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventDestroy</span><span class="p">(</span><span class="n">startEvent1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventDestroy</span><span class="p">(</span><span class="n">stopEvent1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamSynchronize</span><span class="p">(</span><span class="n">stream1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamDestroy</span><span class="p">(</span><span class="n">stream1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">deviceData1</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="peer-to-peer-memory-access">
<h2>Peer-to-peer memory access<a class="headerlink" href="#peer-to-peer-memory-access" title="Link to this heading">#</a></h2>
<p>In multi-GPU systems, peer-to-peer memory access enables one GPU to directly
read or write to the memory of another GPU. This capability reduces data
transfer times by allowing GPUs to communicate directly without involving the
host. Enabling peer-to-peer access can significantly improve the performance of
applications that require frequent data exchange between GPUs, as it eliminates
the need to transfer data through the host memory.</p>
<p>By adding peer-to-peer access to the example referenced in
<a class="reference internal" href="#multi-device-selection"><span class="std std-ref">Device selection</span></a>, data can be efficiently copied between devices.
If peer-to-peer access is not activated, the call to <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind" title="hipMemcpy"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpy()</span></code></a>
still works but internally uses a staging buffer in host memory, which incurs a
performance penalty.</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
with peer-to-peer</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstddef&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstdlib&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)                        \</span>
<span class="cp">{                                                    \</span>
<span class="cp">    const hipError_t status = expression;            \</span>
<span class="cp">    if (status != hipSuccess)                        \</span>
<span class="cp">    {                                                \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error &quot; &lt;&lt; status          \</span>
<span class="cp">                &lt;&lt; &quot;: &quot; &lt;&lt; hipGetErrorString(status) \</span>
<span class="cp">                &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot;         \</span>
<span class="cp">                &lt;&lt; __LINE__ &lt;&lt; std::endl;            \</span>
<span class="cp">        std::exit(EXIT_FAILURE);                     \</span>
<span class="cp">    }                                                \</span>
<span class="cp">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">simpleKernel</span><span class="p">(</span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">elems</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">idx</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">elems</span><span class="p">)</span>
<span class="w">        </span><span class="n">data</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceCount</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDeviceCount</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceCount</span><span class="p">));</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">deviceCount</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">2</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;This example requires at least two HIP devices.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">deviceData0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">deviceData1</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">elems</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">elems</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">double</span><span class="p">);</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceId0</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceId1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>

<span class="hll"><span class="w">    </span><span class="c1">// Enable peer access to the memory (allocated and future) on the peer device.</span>
</span><span class="hll"><span class="w">    </span><span class="c1">// Ensure the device is active before enabling peer access.</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId0</span><span class="p">));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceEnablePeerAccess</span><span class="p">(</span><span class="n">deviceId1</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
</span><span class="hll">
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId1</span><span class="p">));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceEnablePeerAccess</span><span class="p">(</span><span class="n">deviceId0</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
</span>
<span class="w">    </span><span class="c1">// Set device 0 and perform operations</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId0</span><span class="p">));</span><span class="w"> </span><span class="c1">// Set device 0 as current</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">));</span><span class="w"> </span><span class="c1">// Allocate memory on device 0</span>
<span class="w">    </span><span class="n">simpleKernel</span><span class="o">&lt;&lt;&lt;</span><span class="mi">8</span><span class="p">,</span><span class="w"> </span><span class="mi">128</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">elems</span><span class="p">);</span><span class="w"> </span><span class="c1">// Launch kernel on device 0</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Set device 1 and perform operations</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId1</span><span class="p">));</span><span class="w"> </span><span class="c1">// Set device 1 as current</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">));</span><span class="w"> </span><span class="c1">// Allocate memory on device 1</span>
<span class="w">    </span><span class="n">simpleKernel</span><span class="o">&lt;&lt;&lt;</span><span class="mi">8</span><span class="p">,</span><span class="w"> </span><span class="mi">128</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">elems</span><span class="p">);</span><span class="w"> </span><span class="c1">// Launch kernel on device 1</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="hll"><span class="w">    </span><span class="c1">// Use peer-to-peer access</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId0</span><span class="p">));</span>
</span><span class="hll">
</span><span class="hll"><span class="w">    </span><span class="c1">// Now device 0 can access memory allocated on device 1</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToDevice</span><span class="p">));</span>
</span>
<span class="w">    </span><span class="c1">// Copy result from device 0</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">hostData0</span><span class="p">[</span><span class="n">elems</span><span class="p">];</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">hostData0</span><span class="p">,</span><span class="w"> </span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Copy result from device 1</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">hostData1</span><span class="p">[</span><span class="n">elems</span><span class="p">];</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">hostData1</span><span class="p">,</span><span class="w"> </span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Display results from both devices</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Device 0 data: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hostData0</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Device 1 data: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hostData1</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Free device memory</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">deviceData0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">deviceData1</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
without peer-to-peer</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstddef&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstdlib&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)                        \</span>
<span class="cp">{                                                    \</span>
<span class="cp">    const hipError_t status = expression;            \</span>
<span class="cp">    if (status != hipSuccess)                        \</span>
<span class="cp">    {                                                \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error &quot; &lt;&lt; status          \</span>
<span class="cp">                &lt;&lt; &quot;: &quot; &lt;&lt; hipGetErrorString(status) \</span>
<span class="cp">                &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot;         \</span>
<span class="cp">                &lt;&lt; __LINE__ &lt;&lt; std::endl;            \</span>
<span class="cp">        std::exit(EXIT_FAILURE);                     \</span>
<span class="cp">    }                                                \</span>
<span class="cp">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">simpleKernel</span><span class="p">(</span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">elems</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">idx</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">elems</span><span class="p">)</span>
<span class="w">        </span><span class="n">data</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">idx</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceCount</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDeviceCount</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceCount</span><span class="p">));</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">deviceCount</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">2</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;This example requires at least two HIP devices.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span>
<span class="w">    </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">deviceData0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">deviceData1</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">elems</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">elems</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">double</span><span class="p">);</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceId0</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceId1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Set device 0 and perform operations</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId0</span><span class="p">));</span><span class="w"> </span><span class="c1">// Set device 0 as current</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">));</span><span class="w"> </span><span class="c1">// Allocate memory on device 0</span>
<span class="w">    </span><span class="n">simpleKernel</span><span class="o">&lt;&lt;&lt;</span><span class="mi">8</span><span class="p">,</span><span class="w"> </span><span class="mi">128</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">elems</span><span class="p">);</span><span class="w"> </span><span class="c1">// Launch kernel on device 0</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Set device 1 and perform operations</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId1</span><span class="p">));</span><span class="w"> </span><span class="c1">// Set device 1 as current</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">));</span><span class="w"> </span><span class="c1">// Allocate memory on device 1</span>
<span class="w">    </span><span class="n">simpleKernel</span><span class="o">&lt;&lt;&lt;</span><span class="mi">8</span><span class="p">,</span><span class="w"> </span><span class="mi">128</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">elems</span><span class="p">);</span><span class="w"> </span><span class="c1">// Launch kernel on device 1</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="hll"><span class="w">    </span><span class="c1">// Use deviceData0 on device 1. This works but incurs a performance penalty.</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId1</span><span class="p">));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToDevice</span><span class="p">));</span>
</span>
<span class="w">    </span><span class="c1">// Copy result from device 0</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">hostData0</span><span class="p">[</span><span class="n">elems</span><span class="p">];</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">hostData0</span><span class="p">,</span><span class="w"> </span><span class="n">deviceData0</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Copy result from device 1</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">hostData1</span><span class="p">[</span><span class="n">elems</span><span class="p">];</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">deviceId1</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">hostData1</span><span class="p">,</span><span class="w"> </span><span class="n">deviceData1</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Display results from both devices</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Device 0 data: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hostData0</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Device 1 data: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hostData1</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Free device memory</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">deviceData0</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">deviceData1</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
</div>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="cooperative_groups.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Cooperative groups</p>
      </div>
    </a>
    <a class="right-next"
       href="opengl_interop.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">OpenGL interoperability</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#device-enumeration">Device enumeration</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#device-selection">Device selection</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#stream-and-event-behavior">Stream and event behavior</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#peer-to-peer-memory-access">Peer-to-peer memory access</a></li>
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
  <script src="../../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b"></script>
<script src="../../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b"></script>

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
    <img id="rdc-watermark" src="../../_static/images/alpha-watermark.svg" alt="DRAFT watermark"/>
</div> -->
  </body>
</html>
