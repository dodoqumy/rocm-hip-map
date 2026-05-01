---
title: "HIP graphs &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/hipgraph.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:05:46.107549+00:00
content_hash: "4a9c261c34dba78f"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="This chapter describes how to use HIP graphs and highlights their use cases." name="description" />
<meta content="ROCm, HIP, graph, stream" name="keywords" />

    <title>HIP graphs &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/hip_runtime_api/hipgraph';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="Cooperative groups" href="cooperative_groups.html" />
    <link rel="prev" title="Asynchronous concurrent execution" href="asynchronous.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/hip_runtime_api/hipgraph.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l2 current active"><a class="current reference internal" href="#">HIP graphs</a></li>
<li class="toctree-l2"><a class="reference internal" href="cooperative_groups.html">Cooperative groups</a></li>
<li class="toctree-l2"><a class="reference internal" href="multi_device.html">Multi-device management</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">HIP graphs</li>
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
    <h1>HIP graphs</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#using-hip-graphs">Using HIP graphs</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-management">Memory management</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#capture-graphs-from-a-stream">Capture graphs from a stream</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#explicit-graph-creation">Explicit graph creation</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="hip-graphs">
<span id="how-to-hip-graph"></span><h1>HIP graphs<a class="headerlink" href="#hip-graphs" title="Link to this heading">#</a></h1>
<p>HIP graphs are an alternative way of executing tasks on a GPU that can provide
performance benefits over launching kernels using the standard
method via streams. A HIP graph is made up of nodes and edges. The nodes of a
HIP graph represent the operations performed, while the edges mark dependencies
between those operations.</p>
<div class="admonition hint">
<p class="admonition-title">Hint</p>
<p>The <a class="reference internal" href="../../tutorial/graph_api.html#hip-graph-api-tutorial"><span class="std std-ref">HIP Graph API tutorial</span></a> demonstrates how
to use HIP graphs in a real-world application.</p>
</div>
<p>The nodes can be one of the following:</p>
<ul class="simple">
<li><p>empty nodes</p></li>
<li><p>nested graphs</p></li>
<li><p>kernel launches</p></li>
<li><p>host-side function calls</p></li>
<li><p>HIP memory functions (copy, memset, …)</p></li>
<li><p>HIP events</p></li>
<li><p>signalling or waiting on external semaphores</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The available node types are specified by <code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">hipGraphNodeType</span></code>.</p>
</div>
<p>The following figure visualizes the concept of graphs, compared to using streams.</p>
<figure class="align-default">
<img alt="Diagram depicting the difference between using streams to execute kernels with dependencies, resolved by explicitly synchronizing, or using graphs, where the edges denote the dependencies." src="../../_images/hip_graph.svg" />
</figure>
<p>The standard method of launching kernels incurs a small overhead for each
iteration of the operation involved. That overhead is negligible, when the
kernel is launched directly with the HIP C/C++ API, but depending on the
framework used, there can be several levels of redirection, until the actual
kernel is launched by the HIP runtime, leading to significant overhead.
Especially for some AI frameworks, a GPU kernel might run faster than the time
it takes for the framework to set up and launch the kernel, and so the overhead
of repeatedly launching kernels can have a significant impact on performance.</p>
<p>HIP graphs are designed to address this issue, by predefining the HIP API calls
and their dependencies with a graph, and performing most of the initialization
beforehand. Launching a graph only requires a single call, after which the
HIP runtime takes care of executing the operations within the graph.
Graphs can provide additional performance benefits, by enabling optimizations
that are only possible when knowing the dependencies between the operations.</p>
<figure class="align-default" id="id1">
<img alt="Diagram depicting the speed up achievable with HIP graphs compared to HIP streams when launching many short-running kernels." src="../../_images/hip_graph_speedup.svg" />
<figcaption>
<p><span class="caption-text">Qualitative presentation of the execution time of many short-running kernels
when launched using HIP stream versus HIP graph. This does not include the
time needed to set up the graph.</span><a class="headerlink" href="#id1" title="Link to this image">#</a></p>
</figcaption>
</figure>
<section id="using-hip-graphs">
<h2>Using HIP graphs<a class="headerlink" href="#using-hip-graphs" title="Link to this heading">#</a></h2>
<p>There are two different ways of creating graphs: Capturing kernel launches from
a stream, or explicitly creating graphs. The difference between the two
approaches is explained later in this chapter.</p>
<p>The general flow for using HIP graphs includes the following steps.</p>
<ol class="arabic simple">
<li><p>Create a <code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipGraph_t</span></code> graph template using one of the two approaches described in this chapter</p></li>
<li><p>Create a <code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipGraphExec_t</span></code> executable instance of the graph template using <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv419hipGraphInstantiateP14hipGraphExec_t10hipGraph_tP14hipGraphNode_tPc6size_t" title="hipGraphInstantiate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphInstantiate()</span></code></a></p></li>
<li><p>Use <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv414hipGraphLaunch14hipGraphExec_t11hipStream_t" title="hipGraphLaunch"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphLaunch()</span></code></a> to launch the executable graph to a stream</p></li>
<li><p>After execution completes free and destroy graph resources</p></li>
</ol>
<p>The first two steps are the initial setup and only need to be executed once. First
step is the definition of the operations (nodes) and the dependencies (edges)
between them. The second step is the instantiation of the graph. This takes care
of validating and initializing the graph, to reduce the overhead when executing
the graph. The third step is the execution of the graph, which takes care of
launching all the kernels and executing the operations while respecting their
dependencies and necessary synchronizations as specified.</p>
<p>Because HIP graphs require some setup and initialization overhead before their
first execution, graphs only provide a benefit for workloads that require
many iterations to complete.</p>
<p>In both methods the <code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipGraph_t</span></code> template for a graph is used to define the graph.
In order to actually launch a graph, the template needs to be instantiated using
<a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv419hipGraphInstantiateP14hipGraphExec_t10hipGraph_tP14hipGraphNode_tPc6size_t" title="hipGraphInstantiate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphInstantiate()</span></code></a>, which results in an executable graph of type <code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipGraphExec_t</span></code>.
This executable graph can then be launched with <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv414hipGraphLaunch14hipGraphExec_t11hipStream_t" title="hipGraphLaunch"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphLaunch()</span></code></a>, replaying the
operations within the graph. Note, that launching graphs is fundamentally no
different to executing other HIP functions on a stream, except for the fact,
that scheduling the operations within the graph encompasses less overhead and
can enable some optimizations, but they still need to be associated with a stream for execution.</p>
<section id="memory-management">
<h3>Memory management<a class="headerlink" href="#memory-management" title="Link to this heading">#</a></h3>
<p>Memory that is used by operations in graphs can either be pre-allocated or
managed within the graph. Graphs can contain nodes that take care of allocating
memory on the device or copying memory between the host and the device.
Whether you want to pre-allocate the memory or manage it within the graph
depends on the use-case. If the graph is executed in a tight loop the
performance is usually better when the memory is preallocated, so that it
does not need to be reallocated in every iteration.</p>
<p>The same rules as for normal memory allocations apply for memory allocated and
freed by nodes, meaning that the nodes that access memory allocated in a graph
must be ordered after allocation and before freeing.</p>
<p>Memory management within the graph enables the runtime to take care of memory reuse and optimizations.
The lifetime of memory managed in a graph begins when the execution reaches the
node allocating the memory, and ends when either reaching the corresponding
free node within the graph, or after graph execution when a corresponding
<a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html#_CPPv412hipFreeAsyncPv11hipStream_t" title="hipFreeAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipFreeAsync()</span></code></a> or <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html#_CPPv47hipFreePv" title="hipFree"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipFree()</span></code></a> call is reached.
The memory can also be freed with a free node in a different graph that is
associated with the same memory address.</p>
<p>Unlike device memory that is not associated with a graph, this does not necessarily
mean that the freed memory is returned back to the operating system immediately.
Graphs can retain a memory pool for quickly reusing memory within the graph.
This can be especially useful when memory is freed and reallocated later on
within a graph, as that memory doesn’t have to be requested from the operating system.
It also potentially reduces the total memory footprint of the graph, by reusing the same memory.</p>
<p>The amount of memory allocated for graph memory pools on a specific device can
be queried using <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv429hipDeviceGetGraphMemAttributei24hipGraphMemAttributeTypePv" title="hipDeviceGetGraphMemAttribute"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipDeviceGetGraphMemAttribute()</span></code></a>.
In order to return the freed memory <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv421hipDeviceGraphMemTrimi" title="hipDeviceGraphMemTrim"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipDeviceGraphMemTrim()</span></code></a> can be used.
This will return any memory that is not in active use by graphs.</p>
<p>These memory allocations can also be set up to allow access from multiple GPUs,
just like normal allocations. HIP then takes care of allocating and mapping the
memory to the GPUs. When capturing a graph from a stream, the node sets the
accessibility according to <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html#_CPPv419hipMemPoolSetAccess12hipMemPool_tPK16hipMemAccessDesc6size_t" title="hipMemPoolSetAccess"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemPoolSetAccess()</span></code></a> at the time of capturing.</p>
</section>
</section>
<section id="capture-graphs-from-a-stream">
<h2>Capture graphs from a stream<a class="headerlink" href="#capture-graphs-from-a-stream" title="Link to this heading">#</a></h2>
<p>The easy way to integrate HIP graphs into already existing code is to use
<a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv421hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode" title="hipStreamBeginCapture"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamBeginCapture()</span></code></a> and <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv419hipStreamEndCapture11hipStream_tP10hipGraph_t" title="hipStreamEndCapture"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamEndCapture()</span></code></a> to obtain a <code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipGraph_t</span></code>
graph template that includes the captured operations.</p>
<p>When starting to capture operations for a graph using <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv421hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode" title="hipStreamBeginCapture"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamBeginCapture()</span></code></a>,
the operations assigned to the stream are captured into a graph instead of being
executed. The associated graph is returned when calling <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv419hipStreamEndCapture11hipStream_tP10hipGraph_t" title="hipStreamEndCapture"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamEndCapture()</span></code></a>, which
also stops capturing operations.
In order to capture to an already existing graph use <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv428hipStreamBeginCaptureToGraph11hipStream_t10hipGraph_tPK14hipGraphNode_tPK16hipGraphEdgeData6size_t20hipStreamCaptureMode" title="hipStreamBeginCaptureToGraph"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamBeginCaptureToGraph()</span></code></a>.</p>
<p>The functions assigned to the capturing stream are not executed, but instead are
captured and defined as nodes in the graph, to be run when the instantiated
graph is launched.</p>
<p>Functions must be associated with a stream in order to be captured.
This means that non-HIP API functions are not captured by default, but are
executed as standard functions when encountered and not added to the graph.
In order to assign host functions to a stream use
<a class="reference internal" href="../../reference/hip_runtime_api/modules/launch_api.html#_CPPv417hipLaunchHostFunc11hipStream_t11hipHostFn_tPv" title="hipLaunchHostFunc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipLaunchHostFunc()</span></code></a>, as shown in the following code example.
They will then be captured and defined as a host node in the resulting graph,
and won’t be executed when encountered.</p>
<p>Synchronous HIP API calls that are implicitly assigned to the default stream are
not permitted while capturing a stream  and will return an error. This is
because they implicitly synchronize and cause a dependency that can not be
captured within the stream. This includes functions like <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a>,
<a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind" title="hipMemcpy"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpy()</span></code></a> and <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html#_CPPv47hipFreePv" title="hipFree"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipFree()</span></code></a>. In order to capture these to the stream, replace
them with the corresponding asynchronous calls like <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html#_CPPv414hipMallocAsyncPPv6size_t12hipMemPool_t11hipStream_t" title="hipMallocAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code></a>, <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html#_CPPv414hipMemcpyAsyncPvPKv6size_t13hipMemcpyKind11hipStream_t" title="hipMemcpyAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpyAsync()</span></code></a> or <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html#_CPPv412hipFreeAsyncPv11hipStream_t" title="hipFreeAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipFreeAsync()</span></code></a>.</p>
<p>The general flow for using stream capture to create a graph template is:</p>
<ol class="arabic simple">
<li><p>Create a stream from which to capture the operations</p></li>
<li><p>Call <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv421hipStreamBeginCapture11hipStream_t20hipStreamCaptureMode" title="hipStreamBeginCapture"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamBeginCapture()</span></code></a> before the first operation to be captured</p></li>
<li><p>Call <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv419hipStreamEndCapture11hipStream_tP10hipGraph_t" title="hipStreamEndCapture"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamEndCapture()</span></code></a> after the last operation to be captured</p>
<ol class="arabic simple">
<li><p>Define a <code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipGraph_t</span></code> graph template to which <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv419hipStreamEndCapture11hipStream_tP10hipGraph_t" title="hipStreamEndCapture"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamEndCapture()</span></code></a>
passes the captured graph</p></li>
</ol>
</li>
</ol>
<p>The following code is an example of how to use the HIP graph API to capture a
graph from a stream.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstddef&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstdlib&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>

<span class="cp">#define HIP_CHECK(expression)                \</span>
<span class="cp">{                                            \</span>
<span class="cp">    const hipError_t status = expression;    \</span>
<span class="cp">    if(status != hipSuccess)                 \</span>
<span class="cp">    {                                        \</span>
<span class="cp">            std::cerr &lt;&lt; &quot;HIP error &quot;        \</span>
<span class="cp">                &lt;&lt; status &lt;&lt; &quot;: &quot;            \</span>
<span class="cp">                &lt;&lt; hipGetErrorString(status) \</span>
<span class="cp">                &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot; \</span>
<span class="cp">                &lt;&lt; __LINE__ &lt;&lt; std::endl;    \</span>
<span class="cp">    }                                        \</span>
<span class="cp">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernelA</span><span class="p">(</span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayA</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">arrayA</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">*=</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernelB</span><span class="p">(</span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">arrayB</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">arrayB</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">3</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernelC</span><span class="p">(</span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayA</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">arrayB</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">arrayA</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">arrayB</span><span class="p">[</span><span class="n">x</span><span class="p">];</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="k">struct</span><span class="w"> </span><span class="nc">set_vector_args</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">double</span><span class="o">&gt;&amp;</span><span class="w"> </span><span class="n">h_array</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">value</span><span class="p">;</span>
<span class="p">};</span>

<span class="kt">void</span><span class="w"> </span><span class="nf">set_vector</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">args</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">set_vector_args</span><span class="w"> </span><span class="n">h_args</span><span class="p">{</span><span class="o">*</span><span class="p">(</span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="n">set_vector_args</span><span class="o">*&gt;</span><span class="p">(</span><span class="n">args</span><span class="p">))};</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">double</span><span class="o">&gt;&amp;</span><span class="w"> </span><span class="n">vec</span><span class="p">{</span><span class="n">h_args</span><span class="p">.</span><span class="n">h_array</span><span class="p">};</span>
<span class="w">    </span><span class="n">vec</span><span class="p">.</span><span class="n">assign</span><span class="p">(</span><span class="n">vec</span><span class="p">.</span><span class="n">size</span><span class="p">(),</span><span class="w"> </span><span class="n">h_args</span><span class="p">.</span><span class="n">value</span><span class="p">);</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1U</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="mi">20</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// This example assumes that kernelA operates on data that needs to be initialized on</span>
<span class="w">    </span><span class="c1">// and copied from the host, while kernelB initializes the array that is passed to it.</span>
<span class="w">    </span><span class="c1">// Both arrays are then used as input to kernelC, where arrayA is also used as</span>
<span class="w">   </span><span class="c1">//  output, that is copied back to the host, while arrayB is only read from and not modified.</span>

<span class="w">    </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">d_arrayA</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">d_arrayB</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">double</span><span class="o">&gt;</span><span class="w"> </span><span class="n">h_array</span><span class="p">(</span><span class="n">arraySize</span><span class="p">);</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">double</span><span class="w"> </span><span class="n">initValue</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>

<span class="w">    </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">captureStream</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">captureStream</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Start capturing the operations assigned to the stream</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamBeginCapture</span><span class="p">(</span><span class="n">captureStream</span><span class="p">,</span><span class="w"> </span><span class="n">hipStreamCaptureModeGlobal</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// hipMallocAsync and hipMemcpyAsync are needed, to be able to assign it to a stream</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocAsync</span><span class="p">(</span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">**&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_arrayA</span><span class="p">),</span><span class="w"> </span><span class="n">arraySize</span><span class="o">*</span><span class="k">sizeof</span><span class="p">(</span><span class="kt">double</span><span class="p">),</span><span class="w"> </span><span class="n">captureStream</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocAsync</span><span class="p">(</span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">**&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_arrayB</span><span class="p">),</span><span class="w"> </span><span class="n">arraySize</span><span class="o">*</span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">captureStream</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Assign host function to the stream</span>
<span class="w">    </span><span class="c1">// Needs a custom struct to pass the arguments</span>
<span class="w">    </span><span class="n">set_vector_args</span><span class="w"> </span><span class="n">args</span><span class="p">{</span><span class="n">h_array</span><span class="p">,</span><span class="w"> </span><span class="n">initValue</span><span class="p">};</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipLaunchHostFunc</span><span class="p">(</span><span class="n">captureStream</span><span class="p">,</span><span class="w"> </span><span class="n">set_vector</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">args</span><span class="p">));</span>

<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpyAsync</span><span class="p">(</span><span class="n">d_arrayA</span><span class="p">,</span><span class="w"> </span><span class="n">h_array</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">arraySize</span><span class="o">*</span><span class="k">sizeof</span><span class="p">(</span><span class="kt">double</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">,</span><span class="w"> </span><span class="n">captureStream</span><span class="p">));</span>

<span class="w">    </span><span class="n">kernelA</span><span class="o">&lt;&lt;&lt;</span><span class="n">numOfBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">captureStream</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_arrayA</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="p">);</span>
<span class="w">    </span><span class="n">kernelB</span><span class="o">&lt;&lt;&lt;</span><span class="n">numOfBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">captureStream</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_arrayB</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="p">);</span>
<span class="w">    </span><span class="n">kernelC</span><span class="o">&lt;&lt;&lt;</span><span class="n">numOfBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">captureStream</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_arrayA</span><span class="p">,</span><span class="w"> </span><span class="n">d_arrayB</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="p">);</span>

<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpyAsync</span><span class="p">(</span><span class="n">h_array</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_arrayA</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="o">*</span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_arrayA</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">,</span><span class="w"> </span><span class="n">captureStream</span><span class="p">));</span>

<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFreeAsync</span><span class="p">(</span><span class="n">d_arrayA</span><span class="p">,</span><span class="w"> </span><span class="n">captureStream</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFreeAsync</span><span class="p">(</span><span class="n">d_arrayB</span><span class="p">,</span><span class="w"> </span><span class="n">captureStream</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Stop capturing</span>
<span class="w">    </span><span class="n">hipGraph_t</span><span class="w"> </span><span class="n">graph</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamEndCapture</span><span class="p">(</span><span class="n">captureStream</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">graph</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Create an executable graph from the captured graph</span>
<span class="w">    </span><span class="n">hipGraphExec_t</span><span class="w"> </span><span class="n">graphExec</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphInstantiate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">graphExec</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// The graph template can be deleted after the instantiation if it&#39;s not needed for later use</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphDestroy</span><span class="p">(</span><span class="n">graph</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Actually launch the graph. The stream does not have</span>
<span class="w">    </span><span class="c1">// to be the same as the one used for capturing.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphLaunch</span><span class="p">(</span><span class="n">graphExec</span><span class="p">,</span><span class="w"> </span><span class="n">captureStream</span><span class="p">));</span>

<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamSynchronize</span><span class="p">(</span><span class="n">captureStream</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Verify results</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">double</span><span class="w"> </span><span class="n">expected</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">initValue</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mf">2.0</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">3</span><span class="p">;</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">true</span><span class="p">;</span>
<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">arraySize</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="p">(</span><span class="n">h_array</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">expected</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">false</span><span class="p">;</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Validation failed! Expected &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">expected</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; got &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">h_array</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">passed</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Validation passed.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Free graph and stream resources after usage</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphExecDestroy</span><span class="p">(</span><span class="n">graphExec</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamDestroy</span><span class="p">(</span><span class="n">captureStream</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="explicit-graph-creation">
<h2>Explicit graph creation<a class="headerlink" href="#explicit-graph-creation" title="Link to this heading">#</a></h2>
<p>Graphs can also be created directly using the HIP graph API, giving more
fine-grained control over the graph. In this case, the graph nodes are created
explicitly, together with their parameters and dependencies, which specify the
edges of the graph, thereby forming the graph structure.</p>
<p>The nodes are represented by the generic <code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipGraphNode_t</span></code> type. The actual
node type is implicitly defined by the specific function used to add the node to
the graph, for example <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv421hipGraphAddKernelNodeP14hipGraphNode_t10hipGraph_tPK14hipGraphNode_t6size_tPK19hipKernelNodeParams" title="hipGraphAddKernelNode"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphAddKernelNode()</span></code></a> See the
<a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#graph-management-reference"><span class="std std-ref">HIP graph API documentation</span></a> for the
available functions, they are of type <code class="docutils literal notranslate"><span class="pre">hipGraphAdd{Type}Node</span></code>. Each type of
node also has a predefined set of parameters depending on the operation, for
example <code class="xref cpp cpp-class docutils literal notranslate"><span class="pre">hipKernelNodeParams</span></code> for a kernel launch. See the
<a class="reference internal" href="../../doxygen/html/structhip_graph_node_params.html"><span class="doc">documentation for the general hipGraphNodeParams type</span></a>
for a list of available parameter types and their members.</p>
<p>The general flow for explicitly creating a graph is usually:</p>
<ol class="arabic simple">
<li><p>Create a graph <code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipGraph_t</span></code></p></li>
<li><p>Create the nodes and their parameters and add them to the graph</p>
<ol class="arabic simple">
<li><p>Define a <code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipGraphNode_t</span></code></p></li>
<li><p>Define the parameter struct for the desired operation, by explicitly setting the appropriate struct’s members.</p></li>
<li><p>Use the appropriate <code class="docutils literal notranslate"><span class="pre">hipGraphAdd{Type}Node</span></code> function to add the node to the graph.</p>
<ol class="arabic simple">
<li><p>The dependencies can be defined when adding the node to the graph, or afterwards by using <a class="reference internal" href="../../reference/hip_runtime_api/modules/graph_management.html#_CPPv423hipGraphAddDependencies10hipGraph_tPK14hipGraphNode_tPK14hipGraphNode_t6size_t" title="hipGraphAddDependencies"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipGraphAddDependencies()</span></code></a></p></li>
</ol>
</li>
</ol>
</li>
</ol>
<p>The following code example demonstrates how to explicitly create nodes in order to create a graph.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstddef&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstdlib&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>

<span class="cp">#define HIP_CHECK(expression)                \</span>
<span class="cp">{                                            \</span>
<span class="cp">    const hipError_t status = expression;    \</span>
<span class="cp">    if(status != hipSuccess)                 \</span>
<span class="cp">    {                                        \</span>
<span class="cp">            std::cerr &lt;&lt; &quot;HIP error &quot;        \</span>
<span class="cp">                &lt;&lt; status &lt;&lt; &quot;: &quot;            \</span>
<span class="cp">                &lt;&lt; hipGetErrorString(status) \</span>
<span class="cp">                &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot; \</span>
<span class="cp">                &lt;&lt; __LINE__ &lt;&lt; std::endl;    \</span>
<span class="cp">    }                                        \</span>
<span class="cp">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernelA</span><span class="p">(</span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayA</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">arrayA</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">*=</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernelB</span><span class="p">(</span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">arrayB</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">arrayB</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">3</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernelC</span><span class="p">(</span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayA</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">arrayB</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">arrayA</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">arrayB</span><span class="p">[</span><span class="n">x</span><span class="p">];</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="k">struct</span><span class="w"> </span><span class="nc">set_vector_args</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">double</span><span class="o">&gt;&amp;</span><span class="w"> </span><span class="n">h_array</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">value</span><span class="p">;</span>
<span class="p">};</span>

<span class="kt">void</span><span class="w"> </span><span class="nf">set_vector</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">args</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">set_vector_args</span><span class="w"> </span><span class="n">h_args</span><span class="p">{</span><span class="o">*</span><span class="p">(</span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="n">set_vector_args</span><span class="o">*&gt;</span><span class="p">(</span><span class="n">args</span><span class="p">))};</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">double</span><span class="o">&gt;&amp;</span><span class="w"> </span><span class="n">vec</span><span class="p">{</span><span class="n">h_args</span><span class="p">.</span><span class="n">h_array</span><span class="p">};</span>
<span class="w">    </span><span class="n">vec</span><span class="p">.</span><span class="n">assign</span><span class="p">(</span><span class="n">vec</span><span class="p">.</span><span class="n">size</span><span class="p">(),</span><span class="w"> </span><span class="n">h_args</span><span class="p">.</span><span class="n">value</span><span class="p">);</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1U</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="mi">20</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// The pointers to the device memory don&#39;t need to be declared here,</span>
<span class="w">    </span><span class="c1">// they are contained within the hipMemAllocNodeParams as the dptr member</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">double</span><span class="o">&gt;</span><span class="w"> </span><span class="n">h_array</span><span class="p">(</span><span class="n">arraySize</span><span class="p">);</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">double</span><span class="w"> </span><span class="n">initValue</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Create graph an empty graph</span>
<span class="w">    </span><span class="n">hipGraph_t</span><span class="w"> </span><span class="n">graph</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Parameters to allocate arrays</span>
<span class="w">    </span><span class="n">hipMemAllocNodeParams</span><span class="w"> </span><span class="n">allocArrayAParams</span><span class="p">{};</span>
<span class="w">    </span><span class="n">allocArrayAParams</span><span class="p">.</span><span class="n">poolProps</span><span class="p">.</span><span class="n">allocType</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemAllocationTypePinned</span><span class="p">;</span>
<span class="w">    </span><span class="n">allocArrayAParams</span><span class="p">.</span><span class="n">poolProps</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemLocationTypeDevice</span><span class="p">;</span>
<span class="w">    </span><span class="n">allocArrayAParams</span><span class="p">.</span><span class="n">poolProps</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">id</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="c1">// GPU on which memory resides</span>
<span class="w">    </span><span class="n">allocArrayAParams</span><span class="p">.</span><span class="n">bytesize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">double</span><span class="p">);</span>

<span class="w">    </span><span class="n">hipMemAllocNodeParams</span><span class="w"> </span><span class="n">allocArrayBParams</span><span class="p">{};</span>
<span class="w">    </span><span class="n">allocArrayBParams</span><span class="p">.</span><span class="n">poolProps</span><span class="p">.</span><span class="n">allocType</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemAllocationTypePinned</span><span class="p">;</span>
<span class="w">    </span><span class="n">allocArrayBParams</span><span class="p">.</span><span class="n">poolProps</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemLocationTypeDevice</span><span class="p">;</span>
<span class="w">    </span><span class="n">allocArrayBParams</span><span class="p">.</span><span class="n">poolProps</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">id</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="c1">// GPU on which memory resides</span>
<span class="w">    </span><span class="n">allocArrayBParams</span><span class="p">.</span><span class="n">bytesize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Add the allocation nodes to the graph. They don&#39;t have any dependencies</span>
<span class="w">    </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">allocNodeA</span><span class="p">,</span><span class="w"> </span><span class="n">allocNodeB</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphAddMemAllocNode</span><span class="p">(</span><span class="o">&amp;</span><span class="n">allocNodeA</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">allocArrayAParams</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphAddMemAllocNode</span><span class="p">(</span><span class="o">&amp;</span><span class="n">allocNodeB</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">allocArrayBParams</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Parameters for the host function</span>
<span class="w">    </span><span class="c1">// Needs custom struct to pass the arguments</span>
<span class="w">    </span><span class="n">set_vector_args</span><span class="w"> </span><span class="n">args</span><span class="p">{</span><span class="n">h_array</span><span class="p">,</span><span class="w"> </span><span class="n">initValue</span><span class="p">};</span>
<span class="w">    </span><span class="n">hipHostNodeParams</span><span class="w"> </span><span class="n">hostParams</span><span class="p">{};</span>
<span class="w">    </span><span class="n">hostParams</span><span class="p">.</span><span class="n">fn</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">set_vector</span><span class="p">;</span>
<span class="w">    </span><span class="n">hostParams</span><span class="p">.</span><span class="n">userData</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">static_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">args</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Add the host node that initializes the host array. It also doesn&#39;t have any dependencies</span>
<span class="w">    </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">hostNode</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphAddHostNode</span><span class="p">(</span><span class="o">&amp;</span><span class="n">hostNode</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">hostParams</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Add memory copy node, that copies the initialized host array to the device.</span>
<span class="w">    </span><span class="c1">// It has to wait for the host array to be initialized and the device memory to be allocated</span>
<span class="w">    </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">cpyNodeDependencies</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="n">allocNodeA</span><span class="p">,</span><span class="w"> </span><span class="n">hostNode</span><span class="p">};</span>
<span class="w">    </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">cpyToDevNode</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphAddMemcpyNode1D</span><span class="p">(</span><span class="o">&amp;</span><span class="n">cpyToDevNode</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="n">cpyNodeDependencies</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="n">allocArrayAParams</span><span class="p">.</span><span class="n">dptr</span><span class="p">,</span><span class="w"> </span><span class="n">h_array</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">double</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Parameters for kernelA</span>
<span class="w">    </span><span class="n">hipKernelNodeParams</span><span class="w"> </span><span class="n">kernelAParams</span><span class="p">;</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">kernelAArgs</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="o">&amp;</span><span class="n">allocArrayAParams</span><span class="p">.</span><span class="n">dptr</span><span class="p">,</span><span class="w"> </span><span class="k">static_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">arraySize</span><span class="p">)};</span>
<span class="w">    </span><span class="n">kernelAParams</span><span class="p">.</span><span class="n">func</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="n">kernelA</span><span class="p">);</span>
<span class="w">    </span><span class="n">kernelAParams</span><span class="p">.</span><span class="n">gridDim</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="p">;</span>
<span class="w">    </span><span class="n">kernelAParams</span><span class="p">.</span><span class="n">blockDim</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">;</span>
<span class="w">    </span><span class="n">kernelAParams</span><span class="p">.</span><span class="n">sharedMemBytes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="n">kernelAParams</span><span class="p">.</span><span class="n">kernelParams</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">kernelAArgs</span><span class="p">;</span>
<span class="w">    </span><span class="n">kernelAParams</span><span class="p">.</span><span class="n">extra</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">nullptr</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Add the node for kernelA. It has to wait for the memory copy to finish, as it depends on the values from the host array.</span>
<span class="w">    </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">kernelANode</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphAddKernelNode</span><span class="p">(</span><span class="o">&amp;</span><span class="n">kernelANode</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">cpyToDevNode</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">kernelAParams</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Parameters for kernelB</span>
<span class="w">    </span><span class="n">hipKernelNodeParams</span><span class="w"> </span><span class="n">kernelBParams</span><span class="p">;</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">kernelBArgs</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="o">&amp;</span><span class="n">allocArrayBParams</span><span class="p">.</span><span class="n">dptr</span><span class="p">,</span><span class="w"> </span><span class="k">static_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">arraySize</span><span class="p">)};</span>
<span class="w">    </span><span class="n">kernelBParams</span><span class="p">.</span><span class="n">func</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="n">kernelB</span><span class="p">);</span>
<span class="w">    </span><span class="n">kernelBParams</span><span class="p">.</span><span class="n">gridDim</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="p">;</span>
<span class="w">    </span><span class="n">kernelBParams</span><span class="p">.</span><span class="n">blockDim</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">;</span>
<span class="w">    </span><span class="n">kernelBParams</span><span class="p">.</span><span class="n">sharedMemBytes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="n">kernelBParams</span><span class="p">.</span><span class="n">kernelParams</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">kernelBArgs</span><span class="p">;</span>
<span class="w">    </span><span class="n">kernelBParams</span><span class="p">.</span><span class="n">extra</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">nullptr</span><span class="p">;</span>

<span class="w">    </span><span class="c1">//  Add the node for kernelB. It only has to wait for the memory to be allocated, as it initializes the array.</span>
<span class="w">    </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">kernelBNode</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphAddKernelNode</span><span class="p">(</span><span class="o">&amp;</span><span class="n">kernelBNode</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">allocNodeB</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">kernelBParams</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Parameters for kernelC</span>
<span class="w">    </span><span class="n">hipKernelNodeParams</span><span class="w"> </span><span class="n">kernelCParams</span><span class="p">;</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">kernelCArgs</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="o">&amp;</span><span class="n">allocArrayAParams</span><span class="p">.</span><span class="n">dptr</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">allocArrayBParams</span><span class="p">.</span><span class="n">dptr</span><span class="p">,</span><span class="w"> </span><span class="k">static_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">arraySize</span><span class="p">)};</span>
<span class="w">    </span><span class="n">kernelCParams</span><span class="p">.</span><span class="n">func</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">*&gt;</span><span class="p">(</span><span class="n">kernelC</span><span class="p">);</span>
<span class="w">    </span><span class="n">kernelCParams</span><span class="p">.</span><span class="n">gridDim</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="p">;</span>
<span class="w">    </span><span class="n">kernelCParams</span><span class="p">.</span><span class="n">blockDim</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">;</span>
<span class="w">    </span><span class="n">kernelCParams</span><span class="p">.</span><span class="n">sharedMemBytes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="n">kernelCParams</span><span class="p">.</span><span class="n">kernelParams</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">kernelCArgs</span><span class="p">;</span>
<span class="w">    </span><span class="n">kernelCParams</span><span class="p">.</span><span class="n">extra</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">nullptr</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Add the node for kernelC. It has to wait on both kernelA and kernelB to finish, as it depends on their results.</span>
<span class="w">    </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">kernelCNode</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">kernelCDependencies</span><span class="p">[]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="n">kernelANode</span><span class="p">,</span><span class="w"> </span><span class="n">kernelBNode</span><span class="p">};</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphAddKernelNode</span><span class="p">(</span><span class="o">&amp;</span><span class="n">kernelCNode</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="n">kernelCDependencies</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">kernelCParams</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Copy the results back to the host. Has to wait for kernelC to finish.</span>
<span class="w">    </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">cpyToHostNode</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphAddMemcpyNode1D</span><span class="p">(</span><span class="o">&amp;</span><span class="n">cpyToHostNode</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">kernelCNode</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">h_array</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">allocArrayAParams</span><span class="p">.</span><span class="n">dptr</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">double</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Free array of allocNodeA. It needs to wait for the copy to finish, as kernelC stores its results in it.</span>
<span class="w">    </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">freeNodeA</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphAddMemFreeNode</span><span class="p">(</span><span class="o">&amp;</span><span class="n">freeNodeA</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">cpyToHostNode</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">allocArrayAParams</span><span class="p">.</span><span class="n">dptr</span><span class="p">));</span>
<span class="w">    </span><span class="c1">// Free array of allocNodeB. It only needs to wait for kernelC to finish, as it is not written back to the host.</span>
<span class="w">    </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">freeNodeB</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphAddMemFreeNode</span><span class="p">(</span><span class="o">&amp;</span><span class="n">freeNodeB</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">kernelCNode</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="n">allocArrayBParams</span><span class="p">.</span><span class="n">dptr</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Instantiate the graph in order to execute it</span>
<span class="w">    </span><span class="n">hipGraphExec_t</span><span class="w"> </span><span class="n">graphExec</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphInstantiate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">graphExec</span><span class="p">,</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// The graph can be freed after the instantiation if it&#39;s not needed for other purposes</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphDestroy</span><span class="p">(</span><span class="n">graph</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Actually launch the graph</span>
<span class="w">    </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">graphStream</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">graphStream</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphLaunch</span><span class="p">(</span><span class="n">graphExec</span><span class="p">,</span><span class="w"> </span><span class="n">graphStream</span><span class="p">));</span>

<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamSynchronize</span><span class="p">(</span><span class="n">graphStream</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Verify results</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">double</span><span class="w"> </span><span class="n">expected</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">initValue</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mf">2.0</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">3</span><span class="p">;</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">true</span><span class="p">;</span>
<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">arraySize</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="p">(</span><span class="n">h_array</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">expected</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">false</span><span class="p">;</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Validation failed! Expected &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">expected</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; got &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">h_array</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">passed</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Validation passed.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGraphExecDestroy</span><span class="p">(</span><span class="n">graphExec</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamDestroy</span><span class="p">(</span><span class="n">graphStream</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="asynchronous.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Asynchronous concurrent execution</p>
      </div>
    </a>
    <a class="right-next"
       href="cooperative_groups.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Cooperative groups</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#using-hip-graphs">Using HIP graphs</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-management">Memory management</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#capture-graphs-from-a-stream">Capture graphs from a stream</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#explicit-graph-creation">Explicit graph creation</a></li>
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
