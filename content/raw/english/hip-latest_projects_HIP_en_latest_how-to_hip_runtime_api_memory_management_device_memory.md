---
title: "Device memory &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/memory_management/device_memory.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:43.635903+00:00
content_hash: "9ef893e960e72785"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="This chapter describes the device memory of the HIP ecosystem ROCm software." name="description" />
<meta content="AMD, ROCm, HIP, GPU, device memory, global, constant, texture, surface, shared" name="keywords" />

    <title>Device memory &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/hip_runtime_api/memory_management/device_memory';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Texture fetching" href="device_memory/texture_fetching.html" />
    <link rel="prev" title="Host memory" href="host_memory.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/hip_runtime_api/memory_management/device_memory.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../../../understand/programming_model.html">Introduction to the HIP programming model</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../understand/performance_optimization.html">Understanding GPU performance</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../understand/hardware_implementation.html">Hardware implementation</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../understand/compilers.html">HIP compilers</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../performance_guidelines.html">Performance guidelines</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../debugging.html">Debugging with HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../logging.html">Logging HIP activity</a></li>
<li class="toctree-l1 current active has-children"><a class="reference internal" href="../../hip_runtime_api.html">Using HIP runtime API</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2"><a class="reference internal" href="../initialization.html">Initialization</a></li>
<li class="toctree-l2 current active has-children"><a class="reference internal" href="../memory_management.html">Memory management</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l3"><a class="reference internal" href="host_memory.html">Host memory</a></li>
<li class="toctree-l3 current active has-children"><a class="current reference internal" href="#">Device memory</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="device_memory/texture_fetching.html">Texture fetching</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="coherence_control.html">Coherence control</a></li>
<li class="toctree-l3"><a class="reference internal" href="unified_memory.html">Unified memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="virtual_memory.html">Virtual memory management</a></li>
<li class="toctree-l3"><a class="reference internal" href="stream_ordered_allocator.html">Stream Ordered Memory Allocator</a></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference internal" href="../error_handling.html">Error handling</a></li>
<li class="toctree-l2"><a class="reference internal" href="../call_stack.html">Call stack</a></li>
<li class="toctree-l2"><a class="reference internal" href="../asynchronous.html">Asynchronous concurrent execution</a></li>
<li class="toctree-l2"><a class="reference internal" href="../hipgraph.html">HIP graphs</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cooperative_groups.html">Cooperative groups</a></li>
<li class="toctree-l2"><a class="reference internal" href="../multi_device.html">Multi-device management</a></li>
<li class="toctree-l2"><a class="reference internal" href="../opengl_interop.html">OpenGL interoperability</a></li>
<li class="toctree-l2"><a class="reference internal" href="../external_interop.html">External resource interoperability</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../hip_cpp_language_extensions.html">HIP C++ language extensions</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../kernel_language_cpp_support.html">Kernel language C++ support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../hip_porting_guide.html">Porting CUDA code to HIP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../hip_rtc.html">Programming for HIP runtime compiler (RTC)</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../understand/amd_clr.html">AMD compute language runtimes (CLR)</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../../../reference/hip_runtime_api_reference.html">HIP runtime API</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2 has-children"><a class="reference internal" href="../../../reference/hip_runtime_api/modules.html">Modules</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/initialization_and_version.html">Initialization and version</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/device_management.html">Device management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/execution_control.html">Execution control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/error_handling.html">Error handling</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/stream_management.html">Stream management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/stream_memory_operations.html">Stream memory operations</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/event_management.html">Event management</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html">Memory management</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/memory_management_deprecated.html">Memory management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/external_resource_interoperability.html">External resource interoperability</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html">Stream ordered memory allocator</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html">Managed memory</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html">Virtual memory management</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/texture_management.html">Texture management</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/texture_management_deprecated.html">Texture management (deprecated)</a></li>
<li class="toctree-l4"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/surface_object.html">Surface object</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/peer_to_peer_device_memory_access.html">Peer to peer device memory access</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/context_management.html">Context management [deprecated]</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/module_management.html">Module management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/occupancy.html">Occupancy</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/profiler_control.html">Profiler control</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/launch_api.html">Launch API</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/runtime_compilation.html">Runtime compilation</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/callback_activity_apis.html">Callback activity APIs</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/graph_management.html">Graph management</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/graphics_interoperability.html">Graphics interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/opengl_interoperability.html">OpenGL interoperability</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../reference/hip_runtime_api/modules/cooperative_groups_reference.html">Cooperative groups</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../../../reference/hip_runtime_api/global_defines_enums_structs_files.html">Global defines, enums, structs and files</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../../../doxygen/html/group___global_defs.html">Global enum and defines</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../doxygen/html/group___driver_types.html">Driver Types</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../doxygen/html/annotated.html">Data Structures</a></li>
<li class="toctree-l3"><a class="reference internal" href="../../../doxygen/html/files.html">File List</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../../../reference/math_api.html">HIP math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../reference/complex_math_api.html">HIP complex math API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../reference/env_variables.html">HIP environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../reference/error_codes.html">HIP error codes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../reference/api_syntax.html">CUDA to HIP API Function Comparison</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../reference/deprecated_api_list.html">List of deprecated APIs</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../reference/low_fp_types.html">Low Precision Floating Point Types</a></li>
<li class="toctree-l1"><a class="reference internal" href="../../../reference/hardware_features.html">Hardware features</a></li>
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
    
    <li class="breadcrumb-item"><a href="../../hip_runtime_api.html" class="nav-link">Using HIP runtime API</a></li>
    
    
    <li class="breadcrumb-item"><a href="../memory_management.html" class="nav-link">Memory management</a></li>
    
    <li class="breadcrumb-item active" aria-current="page">Device memory</li>
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
    <h1>Device memory</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#global-memory">Global memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#allocating-global-memory">Allocating global memory</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#copying-between-device-and-host">Copying between device and host</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#constant-memory">Constant memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-constant-memory">Using constant memory</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#texture-memory">Texture memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-texture-memory">Using texture memory</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#surface-memory">Surface memory</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#shared-memory">Shared memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#allocate-shared-memory">Allocate shared memory</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="device-memory">
<span id="id1"></span><h1>Device memory<a class="headerlink" href="#device-memory" title="Link to this heading">#</a></h1>
<p>Device memory is random access memory that is physically located on a GPU. In
general it is memory with a bandwidth that is an order of magnitude higher
compared to RAM available to the host. That high bandwidth is only available to
on-device accesses, accesses from the host or other devices have to go over a
special interface which is considerably slower, usually the PCIe bus or the AMD
Infinity Fabric.</p>
<p>On certain architectures like APUs, the GPU and CPU share the same physical
memory.</p>
<p>There is also a special local data share on-chip directly accessible to the
<a class="reference internal" href="../../../understand/hardware_implementation.html#hardware-implementation"><span class="std std-ref">compute units</span></a>, that can be used for shared
memory.</p>
<p>The physical device memory can be used to back up several different memory
spaces in HIP, as described in the following.</p>
<section id="global-memory">
<h2>Global memory<a class="headerlink" href="#global-memory" title="Link to this heading">#</a></h2>
<p>Global memory is the general read-write accessible memory visible to all threads
on a given device. Since variables located in global memory have to be marked
with the <code class="docutils literal notranslate"><span class="pre">__device__</span></code> qualifier, this memory space is also referred to as
device memory.</p>
<p>Without explicitly copying it, it can only be accessed by the threads within a
kernel operating on the device, however <a class="reference internal" href="unified_memory.html#unified-memory"><span class="std std-ref">Unified memory management</span></a> can be used to
let the runtime manage this, if desired.</p>
<section id="allocating-global-memory">
<h3>Allocating global memory<a class="headerlink" href="#allocating-global-memory" title="Link to this heading">#</a></h3>
<p>This memory needs to be explicitly allocated.</p>
<p>It can be allocated from the host via the <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#memory-management-reference"><span class="std std-ref">HIP runtime memory management
functions</span></a> like <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a>, or can be
defined using the <code class="docutils literal notranslate"><span class="pre">__device__</span></code> qualifier on variables.</p>
<p>It can also be allocated within a kernel using <code class="docutils literal notranslate"><span class="pre">malloc</span></code> or <code class="docutils literal notranslate"><span class="pre">new</span></code>.
The specified amount of memory is allocated by each thread that executes the
instructions. The recommended way to allocate the memory depends on the use
case. If the memory is intended to be shared between the threads of a block, it
is generally beneficial to allocate one large block of memory, due to the way
the memory is accessed.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Memory allocated within a kernel can only be freed in kernels, not by the HIP
runtime on the host, like <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv47hipFreePv" title="hipFree"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipFree()</span></code></a>. It is also not possible to
free device memory allocated on the host, with <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a> for
example, in a kernel.</p>
</div>
<p>An example for how to share memory allocated within a kernel by only one thread
is given in the following example. In case the device memory is only needed for
communication between the threads in a single block, <a class="reference internal" href="#shared-memory"><span class="std std-ref">Shared memory</span></a> is the
better option, but is also limited in size.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernel_memory_allocation</span><span class="p">(</span><span class="n">TYPE</span><span class="o">*</span><span class="w"> </span><span class="n">pointer</span><span class="p">){</span>
<span class="w">  </span><span class="c1">// The pointer is stored in shared memory, so that all</span>
<span class="w">  </span><span class="c1">// threads of the block can access the pointer</span>
<span class="w">  </span><span class="n">__shared__</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">memory</span><span class="p">;</span>

<span class="w">  </span><span class="kt">size_t</span><span class="w"> </span><span class="n">blockSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">  </span><span class="k">constexpr</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">elementsPerThread</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">  </span><span class="k">if</span><span class="p">(</span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">){</span>
<span class="w">    </span><span class="c1">// allocate memory in one contiguous block</span>
<span class="w">    </span><span class="n">memory</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="p">[</span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">elementsPerThread</span><span class="p">];</span>
<span class="w">  </span><span class="p">}</span>
<span class="w">  </span><span class="n">__syncthreads</span><span class="p">();</span>

<span class="w">  </span><span class="c1">// load pointer into thread-local variable to avoid</span>
<span class="w">  </span><span class="c1">// unnecessary accesses to shared memory</span>
<span class="w">  </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">localPtr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">memory</span><span class="p">;</span>

<span class="w">  </span><span class="c1">// work with allocated memory, e.g. initialization</span>
<span class="w">  </span><span class="k">for</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">elementsPerThread</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">){</span>
<span class="w">    </span><span class="c1">// access in a contiguous way</span>
<span class="w">    </span><span class="n">localPtr</span><span class="p">[</span><span class="n">i</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockSize</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">i</span><span class="p">;</span>
<span class="w">  </span><span class="p">}</span>

<span class="w">  </span><span class="c1">// synchronize to make sure no thread is accessing the memory before freeing</span>
<span class="w">  </span><span class="n">__syncthreads</span><span class="p">();</span>
<span class="w">  </span><span class="k">if</span><span class="p">(</span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">){</span>
<span class="w">    </span><span class="k">delete</span><span class="p">[]</span><span class="w"> </span><span class="n">memory</span><span class="p">;</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="copying-between-device-and-host">
<h3>Copying between device and host<a class="headerlink" href="#copying-between-device-and-host" title="Link to this heading">#</a></h3>
<p>When not using <a class="reference internal" href="unified_memory.html#unified-memory"><span class="std std-ref">Unified memory management</span></a>, memory has to be explicitly copied between
the device and the host, using the HIP runtime API.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">size_t</span><span class="w"> </span><span class="n">elements</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="mi">20</span><span class="p">;</span>
<span class="kt">size_t</span><span class="w"> </span><span class="n">size_bytes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">elements</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">);</span>

<span class="c1">// allocate host and device memory</span>
<span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">host_pointer</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="p">[</span><span class="n">elements</span><span class="p">];</span>
<span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">device_input</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">device_result</span><span class="p">;</span>
<span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">device_input</span><span class="p">,</span><span class="w"> </span><span class="n">size_bytes</span><span class="p">));</span>
<span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">device_result</span><span class="p">,</span><span class="w"> </span><span class="n">size_bytes</span><span class="p">));</span>

<span class="c1">// copy from host to the device</span>
<span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">device_input</span><span class="p">,</span><span class="w"> </span><span class="n">host_pointer</span><span class="p">,</span><span class="w"> </span><span class="n">size_bytes</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>

<span class="c1">// Use memory on the device, i.e. execute kernels</span>

<span class="c1">// copy from device to host, to e.g. get results from the kernel</span>
<span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">host_pointer</span><span class="p">,</span><span class="w"> </span><span class="n">device_result</span><span class="p">,</span><span class="w"> </span><span class="n">size_bytes</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="c1">// free memory when not needed any more</span>
<span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">device_result</span><span class="p">));</span>
<span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">device_input</span><span class="p">));</span>
<span class="k">delete</span><span class="p">[]</span><span class="w"> </span><span class="n">host_pointer</span><span class="p">;</span>
</pre></div>
</div>
</section>
</section>
<section id="constant-memory">
<h2>Constant memory<a class="headerlink" href="#constant-memory" title="Link to this heading">#</a></h2>
<p>Constant memory is read-only storage visible to all threads on a given device.
It is a limited segment backed by device memory, that takes a different caching
route than normal device memory accesses. It needs to be set by the host before
kernel execution.</p>
<p>In order to get the highest bandwidth from the constant memory, all threads of
a warp have to access the same memory address. If they access different
addresses, the accesses get serialized and the bandwidth is therefore reduced.</p>
<section id="using-constant-memory">
<h3>Using constant memory<a class="headerlink" href="#using-constant-memory" title="Link to this heading">#</a></h3>
<p>Constant memory can not be dynamically allocated, and the size has to be
specified during compile time. If the values can not be specified during compile
time, they have to be set by the host before the kernel, that accesses the
constant memory, is called.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">constexpr</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">const_array_size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">32</span><span class="p">;</span>
<span class="n">__constant__</span><span class="w"> </span><span class="kt">double</span><span class="w"> </span><span class="n">const_array</span><span class="p">[</span><span class="n">const_array_size</span><span class="p">];</span>

<span class="kt">void</span><span class="w"> </span><span class="nf">set_constant_memory</span><span class="p">(</span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">values</span><span class="p">){</span>
<span class="w">  </span><span class="n">hipMemcpyToSymbol</span><span class="p">(</span><span class="n">const_array</span><span class="p">,</span><span class="w"> </span><span class="n">values</span><span class="p">,</span><span class="w"> </span><span class="n">const_array_size</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">double</span><span class="p">));</span>
<span class="p">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernel_using_const_memory</span><span class="p">(</span><span class="kt">double</span><span class="o">*</span><span class="w"> </span><span class="n">array</span><span class="p">){</span>

<span class="w">  </span><span class="kt">int</span><span class="w"> </span><span class="n">warpIdx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">warpSize</span><span class="p">;</span>
<span class="w">  </span><span class="c1">// uniform access of warps to const_array for best performance</span>
<span class="w">  </span><span class="n">array</span><span class="p">[</span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="p">]</span><span class="w"> </span><span class="o">*=</span><span class="w"> </span><span class="n">const_array</span><span class="p">[</span><span class="n">warpIdx</span><span class="p">];</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
</section>
<section id="texture-memory">
<h2>Texture memory<a class="headerlink" href="#texture-memory" title="Link to this heading">#</a></h2>
<p>Texture memory is special read-only memory visible to all threads on a given
device and accessible through additional APIs. Its origins come from graphics
APIs, and provides performance benefits when accessing memory in a pattern where
the addresses are close to each other in a 2D or 3D representation of the
memory. It also provides additional features like filtering and addressing for
out-of-bounds accesses, which are further explained in <a class="reference internal" href="device_memory/texture_fetching.html#texture-fetching"><span class="std std-ref">Texture fetching</span></a>.</p>
<p>The original use of the texture cache was also to take pressure off the global
memory and other caches, however on modern GPUs, that support textures, the L1
cache and texture cache are combined, so the main purpose is to make use of the
texture specific features.</p>
<p>To find out whether textures are supported on a device, query
<code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">hipDeviceAttributeImageSupport</span></code>.</p>
<section id="using-texture-memory">
<h3>Using texture memory<a class="headerlink" href="#using-texture-memory" title="Link to this heading">#</a></h3>
<p>Textures are more complex than just a region of memory, so their layout has to
be specified. They are represented by <code class="docutils literal notranslate"><span class="pre">hipTextureObject_t</span></code> and created using
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/texture_management.html#_CPPv422hipCreateTextureObjectP18hipTextureObject_tPK15hipResourceDescPK14hipTextureDescPK19hipResourceViewDesc" title="hipCreateTextureObject"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipCreateTextureObject()</span></code></a>.</p>
<p>The underlying memory is a 1D, 2D or 3D <code class="docutils literal notranslate"><span class="pre">hipArray_t</span></code>, that needs to be
allocated using <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv414hipMallocArrayP10hipArray_tPK20hipChannelFormatDesc6size_t6size_tj" title="hipMallocArray"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMallocArray()</span></code></a>.</p>
<p>On the device side, texture objects are accessed using the <code class="docutils literal notranslate"><span class="pre">tex1D/2D/3D</span></code>
functions.</p>
<p>The texture management functions can be found in the <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/texture_management.html#texture-management-reference"><span class="std std-ref">Texture management
API reference</span></a></p>
<p>A full example for how to use textures can be found in the <a class="reference external" href="https://github.com/ROCm/rocm-examples/blob/develop/HIP-Basic/texture_management/main.hip">ROCm texture
management example</a></p>
</section>
</section>
<section id="surface-memory">
<h2>Surface memory<a class="headerlink" href="#surface-memory" title="Link to this heading">#</a></h2>
<p>A read-write version of texture memory. It is created in the same way as a
texture, but with <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/surface_object.html#_CPPv422hipCreateSurfaceObjectP18hipSurfaceObject_tPK15hipResourceDesc" title="hipCreateSurfaceObject"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipCreateSurfaceObject()</span></code></a>.</p>
<p>Since surfaces are also cached in the read-only texture cache, the changes
written back to the surface can’t be observed in the same kernel. A new kernel
has to be launched in order to see the updated surface.</p>
<p>The corresponding functions are listed in the <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/surface_object.html#surface-object-reference"><span class="std std-ref">Surface object API reference</span></a>.</p>
</section>
<section id="shared-memory">
<span id="id2"></span><h2>Shared memory<a class="headerlink" href="#shared-memory" title="Link to this heading">#</a></h2>
<p>Shared memory is read-write memory, that is only visible to the threads within a
block. It is allocated per thread block, and needs to be either statically
allocated at compile time, or can be dynamically allocated when launching the
kernel, but not during kernel execution. Its general use-case is to share
variables between the threads within a block, but can also be used as scratch
pad memory.</p>
<p>Shared memory is not backed by the same physical memory as the other address
spaces. It is on-chip memory local to the <a class="reference internal" href="../../../understand/hardware_implementation.html#hardware-implementation"><span class="std std-ref">compute units</span></a>, providing low-latency, high-bandwidth access,
comparable to the L1 cache. It is however limited in size, and as it is
allocated per block, can restrict how many blocks can be scheduled to a compute
unit concurrently, thereby potentially reducing occupancy.</p>
<p>An overview of the size of the local data share (LDS), that backs up shared
memory, is given in the
<a class="reference external" href="https://rocm.docs.amd.com/en/latest/reference/gpu-arch-specs.html" title="(in ROCm Documentation v7.2.2)"><span class="xref std std-doc">GPU hardware specifications</span></a>.</p>
<section id="allocate-shared-memory">
<h3>Allocate shared memory<a class="headerlink" href="#allocate-shared-memory" title="Link to this heading">#</a></h3>
<p>Memory can be dynamically allocated by declaring an <code class="docutils literal notranslate"><span class="pre">extern</span> <span class="pre">__shared__</span></code> array,
whose size can be set during kernel launch, which can then be accessed in the
kernel.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="k">extern</span><span class="w"> </span><span class="n">__shared__</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">dynamic_shared</span><span class="p">[];</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernel</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">array1SizeX</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">array1SizeY</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">array2Size</span><span class="p">){</span>
<span class="w">  </span><span class="c1">// at least (array1SizeX * array1SizeY + array2Size) * sizeof(int) bytes</span>
<span class="w">  </span><span class="c1">// dynamic shared memory need to be allocated when the kernel is launched</span>
<span class="w">  </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">array1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">dynamic_shared</span><span class="p">;</span>
<span class="w">  </span><span class="c1">// array1 is interpreted as 2D of size:</span>
<span class="w">  </span><span class="kt">int</span><span class="w"> </span><span class="n">array1Size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">array1SizeX</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">array1SizeY</span><span class="p">;</span>

<span class="w">  </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">array2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">&amp;</span><span class="p">(</span><span class="n">array1</span><span class="p">[</span><span class="n">array1Size</span><span class="p">]);</span>

<span class="w">  </span><span class="k">if</span><span class="p">(</span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">array1SizeX</span><span class="w"> </span><span class="o">&amp;&amp;</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">y</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">array1SizeY</span><span class="p">){</span>
<span class="w">    </span><span class="c1">// access array1 with threadIdx.x + threadIdx.y * array1SizeX</span>
<span class="w">  </span><span class="p">}</span>
<span class="w">  </span><span class="k">if</span><span class="p">(</span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">array2Size</span><span class="p">){</span>
<span class="w">    </span><span class="c1">// access array2 threadIdx.x</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>
<p>A more in-depth example on dynamically allocated shared memory can be found in
the  <a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic/dynamic_shared">ROCm dynamic shared example</a>.</p>
<p>To statically allocate shared memory, just declare it in the kernel. The memory
is allocated per block, not per thread. If the kernel requires more shared
memory than is available to the architecture, the compilation fails.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">kernel</span><span class="p">(){</span>
<span class="w">  </span><span class="n">__shared__</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">array</span><span class="p">[</span><span class="mi">128</span><span class="p">];</span>
<span class="w">  </span><span class="n">__shared__</span><span class="w"> </span><span class="kt">double</span><span class="w"> </span><span class="n">result</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>A more in-depth example on statically allocated shared memory can be found in
the  <a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/develop/HIP-Basic/shared_memory">ROCm shared memory example</a>.</p>
</section>
</section>
<div class="toctree-wrapper compound">
</div>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="host_memory.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Host memory</p>
      </div>
    </a>
    <a class="right-next"
       href="device_memory/texture_fetching.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Texture fetching</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#global-memory">Global memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#allocating-global-memory">Allocating global memory</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#copying-between-device-and-host">Copying between device and host</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#constant-memory">Constant memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-constant-memory">Using constant memory</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#texture-memory">Texture memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#using-texture-memory">Using texture memory</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#surface-memory">Surface memory</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#shared-memory">Shared memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#allocate-shared-memory">Allocate shared memory</a></li>
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
