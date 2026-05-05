---
title: "Asynchronous concurrent execution &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/asynchronous.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:07:47.249326+00:00
content_hash: "ba5d080a7b4053e8"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="This topic describes asynchronous concurrent execution in HIP" name="description" />
<meta content="AMD, ROCm, HIP, asynchronous concurrent execution, asynchronous, async, concurrent, concurrency" name="keywords" />

    <title>Asynchronous concurrent execution &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/hip_runtime_api/asynchronous';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />
    <link rel="next" title="HIP graphs" href="hipgraph.html" />
    <link rel="prev" title="Call stack" href="call_stack.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/hip_runtime_api/asynchronous.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l2 current active"><a class="current reference internal" href="#">Asynchronous concurrent execution</a></li>
<li class="toctree-l2"><a class="reference internal" href="hipgraph.html">HIP graphs</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">Asynchronous...</li>
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
    <h1>Asynchronous concurrent execution</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#streams-and-concurrent-execution">Streams and concurrent execution</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#managing-streams">Managing streams</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#concurrent-execution-between-host-and-device">Concurrent execution between host and device</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#concurrent-kernel-execution">Concurrent kernel execution</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#overlap-of-data-transfer-and-kernel-execution">Overlap of data transfer and kernel execution</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#querying-device-capabilities">Querying device capabilities</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#asynchronous-memory-operations">Asynchronous memory operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#concurrent-data-transfers-with-intra-device-copies">Concurrent data transfers with intra-device copies</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#synchronization-event-management-and-synchronous-calls">Synchronization, event management and synchronous calls</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#synchronous-calls">Synchronous calls</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#events-for-synchronization">Events for synchronization</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#programmatic-dependent-launch-and-synchronization">Programmatic dependent launch and synchronization</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#example">Example</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-graphs">HIP Graphs</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="asynchronous-concurrent-execution">
<span id="asynchronous-how-to"></span><h1>Asynchronous concurrent execution<a class="headerlink" href="#asynchronous-concurrent-execution" title="Link to this heading">#</a></h1>
<p>Asynchronous concurrent execution is important for efficient parallelism and
resource utilization, with techniques such as overlapping computation and data
transfer, managing concurrent kernel execution with streams on single or
multiple devices, or using HIP graphs.</p>
<section id="streams-and-concurrent-execution">
<h2>Streams and concurrent execution<a class="headerlink" href="#streams-and-concurrent-execution" title="Link to this heading">#</a></h2>
<p>All asynchronous APIs, such as kernel execution, data movement and potentially
data allocation/freeing all happen in the context of device streams.</p>
<p>Streams are FIFO buffers of commands to execute in order on a given device.
Commands which enqueue tasks on a stream all return promptly and the task is
executed asynchronously. Multiple streams can point to the same device and
those streams might be fed from multiple concurrent host-side threads. Multiple
streams tied to the same device are not guaranteed to execute their commands in
order.</p>
<section id="managing-streams">
<h3>Managing streams<a class="headerlink" href="#managing-streams" title="Link to this heading">#</a></h3>
<p>Streams enable the overlap of computation and data transfer, ensuring
continuous GPU activity. By enabling tasks to run concurrently within the same
GPU or across different GPUs, streams improve performance and throughput in
high-performance computing (HPC).</p>
<p>To create a stream, the following functions are used, each defining a handle
to the newly created stream:</p>
<ul class="simple">
<li><p><a class="reference internal" href="../../reference/hip_runtime_api/modules/stream_management.html#_CPPv415hipStreamCreateP11hipStream_t" title="hipStreamCreate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamCreate()</span></code></a>: Creates a stream with default settings.</p></li>
<li><p><a class="reference internal" href="../../reference/hip_runtime_api/modules/stream_management.html#_CPPv424hipStreamCreateWithFlagsP11hipStream_tj" title="hipStreamCreateWithFlags"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamCreateWithFlags()</span></code></a>: Creates a stream, with specific
flags, listed below, enabling more control over stream behavior:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hipStreamDefault</span></code>: creates a default stream suitable for most
operations. The default stream is a blocking operation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipStreamNonBlocking</span></code>: creates a non-blocking stream, allowing
concurrent execution of operations. It ensures that tasks can run
simultaneously without waiting for each other to complete, thus improving
overall performance.</p></li>
</ul>
</li>
<li><p><a class="reference internal" href="../../reference/hip_runtime_api/modules/stream_management.html#_CPPv427hipStreamCreateWithPriorityP11hipStream_tji" title="hipStreamCreateWithPriority"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamCreateWithPriority()</span></code></a>: Allows creating a stream with a
specified priority, enabling prioritization of certain tasks.</p></li>
</ul>
<p>The <a class="reference internal" href="../../reference/hip_runtime_api/modules/stream_management.html#_CPPv420hipStreamSynchronize11hipStream_t" title="hipStreamSynchronize"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamSynchronize()</span></code></a> function is used to block the calling host
thread until all previously submitted tasks in a specified HIP stream have
completed. It ensures that all operations in the given stream, such as kernel
executions or memory transfers, are finished before the host thread proceeds.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If the <a class="reference internal" href="../../reference/hip_runtime_api/modules/stream_management.html#_CPPv420hipStreamSynchronize11hipStream_t" title="hipStreamSynchronize"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamSynchronize()</span></code></a> function input stream is 0 (or the
default stream), it waits for all operations in the default stream to
complete.</p>
</div>
</section>
<section id="concurrent-execution-between-host-and-device">
<h3>Concurrent execution between host and device<a class="headerlink" href="#concurrent-execution-between-host-and-device" title="Link to this heading">#</a></h3>
<p>Concurrent execution between the host (CPU) and device (GPU) allows the CPU to
perform other tasks while the GPU is executing kernels. Kernels are launched
asynchronously using <code class="docutils literal notranslate"><span class="pre">hipLaunchKernelGGL</span></code> or using the triple chevron with a stream,
enabling the CPU to continue executing other code while the GPU processes the
kernel. Similarly, memory operations like <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html#_CPPv414hipMemcpyAsyncPvPKv6size_t13hipMemcpyKind11hipStream_t" title="hipMemcpyAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpyAsync()</span></code></a> are
performed asynchronously, allowing data transfers between the host and device
without blocking the CPU.</p>
</section>
<section id="concurrent-kernel-execution">
<h3>Concurrent kernel execution<a class="headerlink" href="#concurrent-kernel-execution" title="Link to this heading">#</a></h3>
<p>Concurrent execution of multiple kernels on the GPU allows different kernels to
run simultaneously to maximize GPU resource usage. Managing dependencies
between kernels is crucial for ensuring correct execution order. This can be
achieved using <a class="reference internal" href="../../reference/hip_runtime_api/modules/stream_management.html#_CPPv418hipStreamWaitEvent11hipStream_t10hipEvent_tj" title="hipStreamWaitEvent"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamWaitEvent()</span></code></a>, which allows a kernel to wait
for a specific event before starting execution.</p>
<p>Independent kernels can only run concurrently if there are enough registers
and shared memory for the kernels. To enable concurrent kernel executions, the
developer may have to reduce the block size of the kernels. The kernel runtimes
can be misleading for concurrent kernel runs, that is why during optimization
it is a good practice to check the trace files, to see if one kernel is blocking
another kernel, while they are running in parallel. For more information about
application tracing, see <a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler/en/latest/how-to/using-rocprof.html" title="(in rocprofiler Documentation v2.0.0)"><span>Using rocprof</span></a>.</p>
<p>When running kernels in parallel, the execution time can increase due to
contention for shared resources. This is because multiple kernels may attempt
to access the same GPU resources simultaneously, leading to delays.</p>
<p>Multiple kernels executing concurrently is only beneficial under specific conditions. It
is most effective when the kernels do not fully utilize the GPU’s resources. In
such cases, overlapping kernel execution can improve overall throughput and
efficiency by keeping the GPU busy without exceeding its capacity.</p>
</section>
</section>
<section id="overlap-of-data-transfer-and-kernel-execution">
<h2>Overlap of data transfer and kernel execution<a class="headerlink" href="#overlap-of-data-transfer-and-kernel-execution" title="Link to this heading">#</a></h2>
<p>One of the primary benefits of asynchronous operations and multiple streams is
the ability to overlap data transfer with kernel execution, leading to better
resource utilization and improved performance.</p>
<p>Asynchronous execution is particularly advantageous in iterative processes. For
instance, if a kernel is initiated, it can be efficient to prepare the input
data simultaneously, provided that this preparation does not depend on the
kernel’s execution. Such iterative data transfer and kernel execution overlap
can be find in the <a class="reference internal" href="#async-example"><span class="std std-ref">Example</span></a>.</p>
<section id="querying-device-capabilities">
<h3>Querying device capabilities<a class="headerlink" href="#querying-device-capabilities" title="Link to this heading">#</a></h3>
<p>Some AMD HIP-enabled devices can perform asynchronous memory copy operations to
or from the GPU concurrently with kernel execution. Applications can query this
capability by checking the <code class="docutils literal notranslate"><span class="pre">asyncEngineCount</span></code> device property. Devices with
an <code class="docutils literal notranslate"><span class="pre">asyncEngineCount</span></code> greater than zero support concurrent data transfers.
Additionally, if host memory is involved in the copy, it should be page-locked
to ensure optimal performance. Page-locking (or pinning) host memory increases
the bandwidth between the host and the device, reducing the overhead associated
with data transfers. For more details, visit <a class="reference internal" href="memory_management/host_memory.html#host-memory"><span class="std std-ref">Host memory</span></a> page.</p>
</section>
<section id="asynchronous-memory-operations">
<h3>Asynchronous memory operations<a class="headerlink" href="#asynchronous-memory-operations" title="Link to this heading">#</a></h3>
<p>Asynchronous memory operations do not block the host while copying data and,
when used with multiple streams, allow data to be transferred between the host
and device while kernels are executed on the same GPU. Using operations like
<a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html#_CPPv414hipMemcpyAsyncPvPKv6size_t13hipMemcpyKind11hipStream_t" title="hipMemcpyAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpyAsync()</span></code></a> or <a class="reference internal" href="../../reference/hip_runtime_api/modules/peer_to_peer_device_memory_access.html#_CPPv418hipMemcpyPeerAsyncPviPKvi6size_t11hipStream_t" title="hipMemcpyPeerAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpyPeerAsync()</span></code></a>, developers can
initiate data transfers without waiting for the previous operation to complete.
This overlap of computation and data transfer ensures that the GPU is not idle
while waiting for data. <a class="reference internal" href="../../reference/hip_runtime_api/modules/peer_to_peer_device_memory_access.html#_CPPv418hipMemcpyPeerAsyncPviPKvi6size_t11hipStream_t" title="hipMemcpyPeerAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpyPeerAsync()</span></code></a> enables data transfers
between different GPUs, facilitating multi-GPU communication.</p>
<p><a class="reference internal" href="#async-example"><span class="std std-ref">Example</span></a> include launching kernels in one stream while performing
data transfers in another. This technique is especially useful in applications
with large data sets that need to be processed quickly.</p>
</section>
<section id="concurrent-data-transfers-with-intra-device-copies">
<h3>Concurrent data transfers with intra-device copies<a class="headerlink" href="#concurrent-data-transfers-with-intra-device-copies" title="Link to this heading">#</a></h3>
<p>Devices that support the <code class="docutils literal notranslate"><span class="pre">concurrentKernels</span></code> property can perform
intra-device copies concurrently with kernel execution. Additionally, devices
that support the <code class="docutils literal notranslate"><span class="pre">asyncEngineCount</span></code> property can perform data transfers to
or from the GPU simultaneously with kernel execution. Intra-device copies can
be initiated using standard memory copy functions with destination and source
addresses residing on the same device.</p>
</section>
</section>
<section id="synchronization-event-management-and-synchronous-calls">
<h2>Synchronization, event management and synchronous calls<a class="headerlink" href="#synchronization-event-management-and-synchronous-calls" title="Link to this heading">#</a></h2>
<p>Synchronization and event management are important for coordinating tasks and
ensuring correct execution order, and synchronous calls are necessary for
maintaining data consistency.</p>
<section id="synchronous-calls">
<h3>Synchronous calls<a class="headerlink" href="#synchronous-calls" title="Link to this heading">#</a></h3>
<p>Synchronous calls ensure task completion before moving to the next operation.
For example, <a class="reference internal" href="../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind" title="hipMemcpy"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpy()</span></code></a> for data transfers waits for completion
before returning control to the host. Similarly, synchronous kernel launches
are used when immediate completion is required. When a synchronous function is
called, control is not returned to the host thread before the device has
completed the requested task. The behavior of the host thread—whether to yield,
block, or spin—can be specified using <a class="reference internal" href="../../reference/hip_runtime_api/modules/device_management.html#_CPPv417hipSetDeviceFlagsj" title="hipSetDeviceFlags"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipSetDeviceFlags()</span></code></a> with
appropriate flags. Understanding when to use synchronous calls is important for
managing execution flow and avoiding data races.</p>
</section>
<section id="events-for-synchronization">
<h3>Events for synchronization<a class="headerlink" href="#events-for-synchronization" title="Link to this heading">#</a></h3>
<p>By creating an event with <a class="reference internal" href="../../reference/hip_runtime_api/modules/event_management.html#_CPPv414hipEventCreateP10hipEvent_t" title="hipEventCreate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipEventCreate()</span></code></a> and recording it with
<a class="reference internal" href="../../reference/hip_runtime_api/modules/event_management.html#_CPPv414hipEventRecord10hipEvent_t11hipStream_t" title="hipEventRecord"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipEventRecord()</span></code></a>, developers can synchronize operations across
streams, ensuring correct task execution order. <a class="reference internal" href="../../reference/hip_runtime_api/modules/event_management.html#_CPPv419hipEventSynchronize10hipEvent_t" title="hipEventSynchronize"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipEventSynchronize()</span></code></a>
lets the application wait for an event to complete before proceeding with the next
operation.</p>
</section>
<section id="programmatic-dependent-launch-and-synchronization">
<h3>Programmatic dependent launch and synchronization<a class="headerlink" href="#programmatic-dependent-launch-and-synchronization" title="Link to this heading">#</a></h3>
<p>While CUDA supports programmatic dependent launches allowing a secondary kernel
to start before the primary kernel finishes, HIP achieves similar functionality
using streams and events. By employing <a class="reference internal" href="../../reference/hip_runtime_api/modules/stream_management.html#_CPPv418hipStreamWaitEvent11hipStream_t10hipEvent_tj" title="hipStreamWaitEvent"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamWaitEvent()</span></code></a>, it is
possible to manage the execution order without explicit hardware support. This
mechanism allows a secondary kernel to launch as soon as the necessary
conditions are met, even if the primary kernel is still running.</p>
</section>
<section id="example">
<span id="async-example"></span><h3>Example<a class="headerlink" href="#example" title="Link to this heading">#</a></h3>
<p>The examples shows the difference between sequential, asynchronous calls and
asynchronous calls with <code class="docutils literal notranslate"><span class="pre">hipEvents</span></code>.</p>
<figure class="align-center">
<img alt="Compare the different calls" src="../../_images/sequential_async_event.svg" />
</figure>
<p>The example codes</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Sequential</label><div class="sd-tab-content docutils">
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

<span class="c1">// GPU Kernels</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernelA</span><span class="p">(</span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayA</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">arrayA</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="mf">1.0</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernelB</span><span class="p">(</span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayA</span><span class="p">,</span><span class="w"> </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayB</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">arrayB</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">arrayA</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mf">3.0</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="mi">20</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">numberOfIterations</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">50</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// The array size smaller to avoid the relatively short kernel launch compared to memory copies</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1U</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="mi">25</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">d_dataA</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">d_dataB</span><span class="p">;</span>

<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">initValueA</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0.0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">initValueB</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">double</span><span class="o">&gt;</span><span class="w"> </span><span class="n">vectorA</span><span class="p">(</span><span class="n">arraySize</span><span class="p">,</span><span class="w"> </span><span class="n">initValueA</span><span class="p">);</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">double</span><span class="o">&gt;</span><span class="w"> </span><span class="n">vectorB</span><span class="p">(</span><span class="n">arraySize</span><span class="p">,</span><span class="w"> </span><span class="n">initValueB</span><span class="p">);</span>
<span class="w">    </span><span class="c1">// Allocate device memory</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_dataA</span><span class="p">)));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_dataB</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_dataB</span><span class="p">)));</span>
<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">iteration</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">iteration</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numberOfIterations</span><span class="p">;</span><span class="w"> </span><span class="n">iteration</span><span class="o">++</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="c1">// Host to Device copies</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">vectorA</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_dataA</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_dataB</span><span class="p">,</span><span class="w"> </span><span class="n">vectorB</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_dataB</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>
<span class="w">        </span><span class="c1">// Launch the GPU kernels</span>
<span class="w">        </span><span class="n">kernelA</span><span class="o">&lt;&lt;&lt;</span><span class="n">numOfBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="p">);</span>
<span class="w">        </span><span class="n">kernelB</span><span class="o">&lt;&lt;&lt;</span><span class="n">numOfBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">d_dataB</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="p">);</span>
<span class="w">        </span><span class="c1">// Device to Host copies</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">vectorA</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">vectorA</span><span class="p">.</span><span class="n">data</span><span class="p">()),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">vectorB</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_dataB</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">vectorB</span><span class="p">.</span><span class="n">data</span><span class="p">()),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="c1">// Wait for all operations to complete</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Verify results</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">double</span><span class="w"> </span><span class="n">expectedA</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="kt">double</span><span class="p">)</span><span class="n">numberOfIterations</span><span class="p">;</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">double</span><span class="w"> </span><span class="n">expectedB</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">initValueB</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="p">(</span><span class="mf">3.0</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">numberOfIterations</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="p">(</span><span class="n">expectedA</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="p">(</span><span class="n">expectedA</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mf">1.0</span><span class="p">))</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">true</span><span class="p">;</span>
<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">arraySize</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="p">(</span><span class="n">vectorA</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">expectedA</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">false</span><span class="p">;</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Validation failed! Expected &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">expectedA</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; got &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">vectorA</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; at index: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="k">if</span><span class="p">(</span><span class="n">vectorB</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">expectedB</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">false</span><span class="p">;</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Validation failed! Expected &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">expectedB</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; got &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w">  </span><span class="n">vectorB</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; at index: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">passed</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Sequential execution completed successfully.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="k">else</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Sequential execution failed.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Cleanup</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_dataA</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_dataB</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Asynchronous</label><div class="sd-tab-content docutils">
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

<span class="c1">// GPU Kernels</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernelA</span><span class="p">(</span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayA</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">arrayA</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="mf">1.0</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernelB</span><span class="p">(</span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayA</span><span class="p">,</span><span class="w"> </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayB</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">arrayB</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">arrayA</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mf">3.0</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="mi">20</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">numberOfIterations</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">50</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// The array size smaller to avoid the relatively short kernel launch compared to memory copies</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1U</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="mi">25</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">d_dataA</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">d_dataB</span><span class="p">;</span>

<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">initValueA</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0.0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">initValueB</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">double</span><span class="o">&gt;</span><span class="w"> </span><span class="n">vectorA</span><span class="p">(</span><span class="n">arraySize</span><span class="p">,</span><span class="w"> </span><span class="n">initValueA</span><span class="p">);</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">double</span><span class="o">&gt;</span><span class="w"> </span><span class="n">vectorB</span><span class="p">(</span><span class="n">arraySize</span><span class="p">,</span><span class="w"> </span><span class="n">initValueB</span><span class="p">);</span>
<span class="w">    </span><span class="c1">// Allocate device memory</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_dataA</span><span class="p">)));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_dataB</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_dataB</span><span class="p">)));</span>
<span class="w">    </span><span class="c1">// Create streams</span>
<span class="w">    </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">streamA</span><span class="p">,</span><span class="w"> </span><span class="n">streamB</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">streamA</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">streamB</span><span class="p">));</span>
<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">iteration</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">iteration</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numberOfIterations</span><span class="p">;</span><span class="w"> </span><span class="n">iteration</span><span class="o">++</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="c1">// Stream 1: Host to Device 1</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpyAsync</span><span class="p">(</span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">vectorA</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_dataA</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">,</span><span class="w"> </span><span class="n">streamA</span><span class="p">));</span>
<span class="w">        </span><span class="c1">// Stream 2: Host to Device 2</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpyAsync</span><span class="p">(</span><span class="n">d_dataB</span><span class="p">,</span><span class="w"> </span><span class="n">vectorB</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_dataB</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">,</span><span class="w"> </span><span class="n">streamB</span><span class="p">));</span>
<span class="w">        </span><span class="c1">// Stream 1: Kernel 1</span>
<span class="w">        </span><span class="n">kernelA</span><span class="o">&lt;&lt;&lt;</span><span class="n">numOfBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">streamA</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="p">);</span>
<span class="w">        </span><span class="c1">// Wait for streamA finish</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamSynchronize</span><span class="p">(</span><span class="n">streamA</span><span class="p">));</span>
<span class="w">        </span><span class="c1">// Stream 2: Kernel 2</span>
<span class="w">        </span><span class="n">kernelB</span><span class="o">&lt;&lt;&lt;</span><span class="n">numOfBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">streamB</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">d_dataB</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="p">);</span>
<span class="w">        </span><span class="c1">// Stream 1: Device to Host 2 (after Kernel 1)</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpyAsync</span><span class="p">(</span><span class="n">vectorA</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">vectorA</span><span class="p">.</span><span class="n">data</span><span class="p">()),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">,</span><span class="w"> </span><span class="n">streamA</span><span class="p">));</span>
<span class="w">        </span><span class="c1">// Stream 2: Device to Host 2 (after Kernel 2)</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpyAsync</span><span class="p">(</span><span class="n">vectorB</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_dataB</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">vectorB</span><span class="p">.</span><span class="n">data</span><span class="p">()),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">,</span><span class="w"> </span><span class="n">streamB</span><span class="p">));</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="c1">// Wait for all operations in both streams to complete</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamSynchronize</span><span class="p">(</span><span class="n">streamA</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamSynchronize</span><span class="p">(</span><span class="n">streamB</span><span class="p">));</span>
<span class="w">    </span><span class="c1">// Verify results</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">expectedA</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="kt">double</span><span class="p">)</span><span class="n">numberOfIterations</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">expectedB</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">initValueB</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="p">(</span><span class="mf">3.0</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">numberOfIterations</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="p">(</span><span class="n">expectedA</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="p">(</span><span class="n">expectedA</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mf">1.0</span><span class="p">))</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">true</span><span class="p">;</span>
<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">arraySize</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="p">(</span><span class="n">vectorA</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">expectedA</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">false</span><span class="p">;</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Validation failed! Expected &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">expectedA</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; got &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">vectorA</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; at index: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="k">if</span><span class="p">(</span><span class="n">vectorB</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">expectedB</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">false</span><span class="p">;</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Validation failed! Expected &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">expectedB</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; got &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w">  </span><span class="n">vectorB</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; at index: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">passed</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Asynchronous execution completed successfully.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="k">else</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Asynchronous execution failed.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Cleanup</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamDestroy</span><span class="p">(</span><span class="n">streamA</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamDestroy</span><span class="p">(</span><span class="n">streamB</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_dataA</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_dataB</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
hipStreamWaitEvent</label><div class="sd-tab-content docutils">
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

<span class="c1">// GPU Kernels</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernelA</span><span class="p">(</span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayA</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">arrayA</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="mf">1.0</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernelB</span><span class="p">(</span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayA</span><span class="p">,</span><span class="w"> </span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">arrayB</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">size</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">arrayB</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">arrayA</span><span class="p">[</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mf">3.0</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">numOfBlocks</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="mi">20</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">numberOfIterations</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">50</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// The array size smaller to avoid the relatively short kernel launch compared to memory copies</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1U</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="mi">25</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">d_dataA</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="o">*</span><span class="n">d_dataB</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">initValueA</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0.0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">initValueB</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">double</span><span class="o">&gt;</span><span class="w"> </span><span class="n">vectorA</span><span class="p">(</span><span class="n">arraySize</span><span class="p">,</span><span class="w"> </span><span class="n">initValueA</span><span class="p">);</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="kt">double</span><span class="o">&gt;</span><span class="w"> </span><span class="n">vectorB</span><span class="p">(</span><span class="n">arraySize</span><span class="p">,</span><span class="w"> </span><span class="n">initValueB</span><span class="p">);</span>
<span class="w">    </span><span class="c1">// Allocate device memory</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_dataA</span><span class="p">)));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_dataB</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_dataB</span><span class="p">)));</span>
<span class="w">    </span><span class="c1">// Create streams</span>
<span class="w">    </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">streamA</span><span class="p">,</span><span class="w"> </span><span class="n">streamB</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">streamA</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">streamB</span><span class="p">));</span>
<span class="w">    </span><span class="c1">// Create events</span>
<span class="w">    </span><span class="n">hipEvent_t</span><span class="w"> </span><span class="n">event</span><span class="p">,</span><span class="w"> </span><span class="n">eventA</span><span class="p">,</span><span class="w"> </span><span class="n">eventB</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">event</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">eventA</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">eventB</span><span class="p">));</span>
<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">iteration</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">iteration</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numberOfIterations</span><span class="p">;</span><span class="w"> </span><span class="n">iteration</span><span class="o">++</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="c1">// Stream 1: Host to Device 1</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpyAsync</span><span class="p">(</span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">vectorA</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_dataA</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">,</span><span class="w"> </span><span class="n">streamA</span><span class="p">));</span>
<span class="w">        </span><span class="c1">// Stream 2: Host to Device 2</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpyAsync</span><span class="p">(</span><span class="n">d_dataB</span><span class="p">,</span><span class="w"> </span><span class="n">vectorB</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_dataB</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">,</span><span class="w"> </span><span class="n">streamB</span><span class="p">));</span>
<span class="w">        </span><span class="c1">// Stream 1: Kernel 1</span>
<span class="w">        </span><span class="n">kernelA</span><span class="o">&lt;&lt;&lt;</span><span class="n">numOfBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">streamA</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="p">);</span>
<span class="w">        </span><span class="c1">// Record event after the GPU kernel in Stream 1</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventRecord</span><span class="p">(</span><span class="n">event</span><span class="p">,</span><span class="w"> </span><span class="n">streamA</span><span class="p">));</span>
<span class="w">        </span><span class="c1">// Stream 2: Wait for event before starting Kernel 2</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamWaitEvent</span><span class="p">(</span><span class="n">streamB</span><span class="p">,</span><span class="w"> </span><span class="n">event</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="w">        </span><span class="c1">// Stream 2: Kernel 2</span>
<span class="w">        </span><span class="n">kernelB</span><span class="o">&lt;&lt;&lt;</span><span class="n">numOfBlocks</span><span class="p">,</span><span class="w"> </span><span class="n">threadsPerBlock</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">streamB</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">d_dataB</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="p">);</span>
<span class="w">        </span><span class="c1">// Stream 1: Device to Host 2 (after Kernel 1)</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpyAsync</span><span class="p">(</span><span class="n">vectorA</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_dataA</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">vectorA</span><span class="p">.</span><span class="n">data</span><span class="p">()),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">,</span><span class="w"> </span><span class="n">streamA</span><span class="p">));</span>
<span class="w">        </span><span class="c1">// Stream 2: Device to Host 2 (after Kernel 2)</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpyAsync</span><span class="p">(</span><span class="n">vectorB</span><span class="p">.</span><span class="n">data</span><span class="p">(),</span><span class="w"> </span><span class="n">d_dataB</span><span class="p">,</span><span class="w"> </span><span class="n">arraySize</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">vectorB</span><span class="p">.</span><span class="n">data</span><span class="p">()),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">,</span><span class="w"> </span><span class="n">streamB</span><span class="p">));</span>
<span class="w">        </span><span class="c1">// Wait for all operations in both streams to complete</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventRecord</span><span class="p">(</span><span class="n">eventA</span><span class="p">,</span><span class="w"> </span><span class="n">streamA</span><span class="p">));</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventRecord</span><span class="p">(</span><span class="n">eventB</span><span class="p">,</span><span class="w"> </span><span class="n">streamB</span><span class="p">));</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamWaitEvent</span><span class="p">(</span><span class="n">streamA</span><span class="p">,</span><span class="w"> </span><span class="n">eventA</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="w">        </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamWaitEvent</span><span class="p">(</span><span class="n">streamB</span><span class="p">,</span><span class="w"> </span><span class="n">eventB</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="c1">// Verify results</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">expectedA</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="kt">double</span><span class="p">)</span><span class="n">numberOfIterations</span><span class="p">;</span>
<span class="w">    </span><span class="kt">double</span><span class="w"> </span><span class="n">expectedB</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">initValueB</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="p">(</span><span class="mf">3.0</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">numberOfIterations</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="p">(</span><span class="n">expectedA</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="p">(</span><span class="n">expectedA</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mf">1.0</span><span class="p">))</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="mf">2.0</span><span class="p">;</span>
<span class="w">    </span><span class="kt">bool</span><span class="w"> </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">true</span><span class="p">;</span>
<span class="w">    </span><span class="k">for</span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">arraySize</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="k">if</span><span class="p">(</span><span class="n">vectorA</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">expectedA</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">false</span><span class="p">;</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Validation failed! Expected &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">expectedA</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; got &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">vectorA</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="k">if</span><span class="p">(</span><span class="n">vectorB</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">expectedB</span><span class="p">)</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="n">passed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">false</span><span class="p">;</span>
<span class="w">            </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Validation failed! Expected &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">expectedB</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; got &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w">  </span><span class="n">vectorB</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">            </span><span class="k">break</span><span class="p">;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="n">passed</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Asynchronous execution with events completed successfully.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="k">else</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Asynchronous execution with events failed.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Cleanup</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventDestroy</span><span class="p">(</span><span class="n">event</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventDestroy</span><span class="p">(</span><span class="n">eventA</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipEventDestroy</span><span class="p">(</span><span class="n">eventB</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamDestroy</span><span class="p">(</span><span class="n">streamA</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamDestroy</span><span class="p">(</span><span class="n">streamB</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_dataA</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_dataB</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
</div>
</section>
</section>
<section id="hip-graphs">
<h2>HIP Graphs<a class="headerlink" href="#hip-graphs" title="Link to this heading">#</a></h2>
<p>HIP graphs offer an efficient alternative to the standard method of launching
GPU tasks via streams. Comprising nodes for operations and edges for
dependencies, HIP graphs reduce kernel launch overhead and provide a high-level
abstraction for managing dependencies and synchronization. By representing
sequences of kernels and memory operations as a single graph, they simplify
complex workflows and enhance performance, particularly for applications with
intricate dependencies and multiple execution stages.
For more details, see the <a class="reference internal" href="hipgraph.html#how-to-hip-graph"><span class="std std-ref">HIP graphs</span></a> documentation.</p>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="call_stack.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Call stack</p>
      </div>
    </a>
    <a class="right-next"
       href="hipgraph.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">HIP graphs</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#streams-and-concurrent-execution">Streams and concurrent execution</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#managing-streams">Managing streams</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#concurrent-execution-between-host-and-device">Concurrent execution between host and device</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#concurrent-kernel-execution">Concurrent kernel execution</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#overlap-of-data-transfer-and-kernel-execution">Overlap of data transfer and kernel execution</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#querying-device-capabilities">Querying device capabilities</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#asynchronous-memory-operations">Asynchronous memory operations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#concurrent-data-transfers-with-intra-device-copies">Concurrent data transfers with intra-device copies</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#synchronization-event-management-and-synchronous-calls">Synchronization, event management and synchronous calls</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#synchronous-calls">Synchronous calls</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#events-for-synchronization">Events for synchronization</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#programmatic-dependent-launch-and-synchronization">Programmatic dependent launch and synchronization</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#example">Example</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-graphs">HIP Graphs</a></li>
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
