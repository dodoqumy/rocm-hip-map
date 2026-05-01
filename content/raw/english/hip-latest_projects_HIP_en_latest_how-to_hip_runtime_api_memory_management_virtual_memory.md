---
title: "Virtual memory management &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/memory_management/virtual_memory.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:05:58.015954+00:00
content_hash: "d147d00f5a926b60"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="This chapter describes Virtual Memory (VM) and shows how to use it in AMD HIP." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, virtual memory, virtual, memory, UM, APU" name="keywords" />

    <title>Virtual memory management &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/hip_runtime_api/memory_management/virtual_memory';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Stream Ordered Memory Allocator" href="stream_ordered_allocator.html" />
    <link rel="prev" title="Unified memory management" href="unified_memory.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/hip_runtime_api/memory_management/virtual_memory.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l3 has-children"><a class="reference internal" href="device_memory.html">Device memory</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="device_memory/texture_fetching.html">Texture fetching</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="coherence_control.html">Coherence control</a></li>
<li class="toctree-l3"><a class="reference internal" href="unified_memory.html">Unified memory management</a></li>
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Virtual memory management</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">Virtual...</li>
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
    <h1>Virtual memory management</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-allocation">Memory allocation</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#virtual-memory-management-support">Virtual memory management support</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#allocate-physical-memory">Allocate physical memory</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#reserve-virtual-address-range">Reserve virtual address range</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#set-memory-access">Set memory access</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#dynamically-increase-allocation-size">Dynamically increase allocation size</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#free-virtual-memory">Free virtual memory</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#example-code">Example code</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#virtual-aliases">Virtual aliases</a></li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="virtual-memory-management">
<span id="virtual-memory"></span><h1>Virtual memory management<a class="headerlink" href="#virtual-memory-management" title="Link to this heading">#</a></h1>
<p>Memory management is important when creating high-performance applications in
the HIP ecosystem. Both allocating and copying memory can result in bottlenecks,
which can significantly impact performance.</p>
<p>Global memory allocation in HIP uses the C language style allocation function.
This works fine for simple cases but can cause problems if your memory needs
change. If you need to increase the size of your memory, you must allocate a
second larger buffer and copy the data to it before you can free the original
buffer. This increases overall memory usage and causes unnecessary <code class="docutils literal notranslate"><span class="pre">memcpy</span></code>
calls. Another solution is to allocate a larger buffer than you initially need.
However, this isn’t an efficient way to handle resources and doesn’t solve the
issue of reallocation when the extra buffer runs out.</p>
<p>Virtual memory management solves these memory management problems. It helps to
reduce memory usage and unnecessary <code class="docutils literal notranslate"><span class="pre">memcpy</span></code> calls.</p>
<p>HIP virtual memory management is built on top of HSA, which provides low-level
access to AMD GPU memory. For more details on the underlying HSA runtime,
see <a class="reference external" href="https://rocm.docs.amd.com/projects/ROCR-Runtime/en/latest/index.html" title="(in ROCR Documentation v1.18.0)"><span class="xref std std-doc">ROCr documentation</span></a></p>
<section id="memory-allocation">
<span id="memory-allocation-virtual-memory"></span><h2>Memory allocation<a class="headerlink" href="#memory-allocation" title="Link to this heading">#</a></h2>
<p>Standard memory allocation uses the <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a> function to allocate a
block of memory on the device. However, when using virtual memory, this process
is separated into multiple steps using the <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv412hipMemCreateP31hipMemGenericAllocationHandle_t6size_tPK20hipMemAllocationPropy" title="hipMemCreate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemCreate()</span></code></a>,
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv420hipMemAddressReservePPv6size_t6size_tPvy" title="hipMemAddressReserve"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemAddressReserve()</span></code></a>, <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv49hipMemMapPv6size_t6size_t31hipMemGenericAllocationHandle_ty" title="hipMemMap"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemMap()</span></code></a>, and
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv415hipMemSetAccessPv6size_tPK16hipMemAccessDesc6size_t" title="hipMemSetAccess"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemSetAccess()</span></code></a> functions. This guide explains what these functions
do and how you can use them for virtual memory management.</p>
<section id="virtual-memory-management-support">
<span id="vmm-support"></span><h3>Virtual memory management support<a class="headerlink" href="#virtual-memory-management-support" title="Link to this heading">#</a></h3>
<p>The first step is to check if the targeted device or GPU supports virtual memory management.
Use the <a class="reference internal" href="../../../reference/hip_runtime_api/modules/device_management.html#_CPPv421hipDeviceGetAttributePi20hipDeviceAttribute_ti" title="hipDeviceGetAttribute"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipDeviceGetAttribute()</span></code></a> function to get the
<code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeVirtualMemoryManagementSupported</span></code> attribute for a specific GPU, as shown in the following example.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">vmm</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">currentDev</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="n">hipDeviceGetAttribute</span><span class="p">(</span>
<span class="w">    </span><span class="o">&amp;</span><span class="n">vmm</span><span class="p">,</span><span class="w"> </span><span class="n">hipDeviceAttributeVirtualMemoryManagementSupported</span><span class="p">,</span><span class="w"> </span><span class="n">currentDev</span>
<span class="p">);</span>

<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">vmm</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;GPU &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">currentDev</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; doesn&#39;t support virtual memory management.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;GPU &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">currentDev</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; support virtual memory management.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="allocate-physical-memory">
<span id="id1"></span><h3>Allocate physical memory<a class="headerlink" href="#allocate-physical-memory" title="Link to this heading">#</a></h3>
<p>The next step is to allocate the physical memory using the
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv412hipMemCreateP31hipMemGenericAllocationHandle_t6size_tPK20hipMemAllocationPropy" title="hipMemCreate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemCreate()</span></code></a> function. This function accepts the size of the buffer,
an <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">long</span> <span class="pre">long</span></code> variable for the flags, and a
<code class="xref cpp cpp-struct docutils literal notranslate"><span class="pre">hipMemAllocationProp</span></code> variable. <code class="xref cpp cpp-struct docutils literal notranslate"><span class="pre">hipMemAllocationProp</span></code>
contains the properties of the memory to be allocated, such as where the memory
is physically located and what kind of shareable handles are available. If the
allocation is successful, the function returns a value of
<code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">hipSuccess</span></code>, with <code class="xref cpp cpp-type docutils literal notranslate"><span class="pre">hipMemGenericAllocationHandle_t</span></code>
representing a valid physical memory allocation.</p>
<p>The allocated memory must be aligned with the appropriate granularity. The
granularity value can be queried with <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv430hipMemGetAllocationGranularityP6size_tPK20hipMemAllocationProp33hipMemAllocationGranularity_flags" title="hipMemGetAllocationGranularity"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemGetAllocationGranularity()</span></code></a>,
and its value depends on the target device hardware and the type of memory
allocation. If the allocation size is not aligned, meaning it is not cleanly
divisible by the minimum granularity value, <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv412hipMemCreateP31hipMemGenericAllocationHandle_t6size_tPK20hipMemAllocationPropy" title="hipMemCreate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemCreate()</span></code></a> will return
an out-of-memory error.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">size_t</span><span class="w"> </span><span class="n">granularity</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="n">hipMemGenericAllocationHandle_t</span><span class="w"> </span><span class="n">allocHandle</span><span class="p">;</span>
<span class="n">hipMemAllocationProp</span><span class="w"> </span><span class="n">prop</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{};</span>
<span class="c1">// The pinned allocation type cannot be migrated from its current location</span>
<span class="c1">// while the application is actively using it.</span>
<span class="n">prop</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemAllocationTypePinned</span><span class="p">;</span>
<span class="c1">// Set the location type to device, currently there are no other valid option.</span>
<span class="n">prop</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemLocationTypeDevice</span><span class="p">;</span>
<span class="c1">// Set the device id, where the memory will be allocated.</span>
<span class="n">prop</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">id</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">currentDev</span><span class="p">;</span>
<span class="n">hipMemGetAllocationGranularity</span><span class="p">(</span><span class="o">&amp;</span><span class="n">granularity</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">prop</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemAllocationGranularityMinimum</span><span class="p">);</span>
<span class="n">padded_size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">ROUND_UP</span><span class="p">(</span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">granularity</span><span class="p">);</span>
<span class="n">hipMemCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">allocHandle</span><span class="p">,</span><span class="w"> </span><span class="n">padded_size</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">prop</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><strong>Allocation Granularity:</strong> Virtual memory allocations must be aligned to the
hardware-specific granularity, which varies by GPU architecture and memory
type. Always query the granularity using <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv430hipMemGetAllocationGranularityP6size_tPK20hipMemAllocationProp33hipMemAllocationGranularity_flags" title="hipMemGetAllocationGranularity"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemGetAllocationGranularity()</span></code></a>
before calling <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv420hipMemAddressReservePPv6size_t6size_tPvy" title="hipMemAddressReserve"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemAddressReserve()</span></code></a> or <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv412hipMemCreateP31hipMemGenericAllocationHandle_t6size_tPK20hipMemAllocationPropy" title="hipMemCreate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemCreate()</span></code></a>.
Failure to align allocations to the required granularity will result in
<code class="docutils literal notranslate"><span class="pre">hipErrorOutOfMemory</span></code> errors, even when sufficient physical memory is available.</p>
</div>
</section>
<section id="reserve-virtual-address-range">
<span id="reserve-virtual-address"></span><h3>Reserve virtual address range<a class="headerlink" href="#reserve-virtual-address-range" title="Link to this heading">#</a></h3>
<p>After you have acquired an allocation of physical memory, you must map it to a
virtual address before you can use it. Mapping means the physical memory
allocation is available from the virtual address range it is mapped to. To
reserve a virtual memory range, use the <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv420hipMemAddressReservePPv6size_t6size_tPvy" title="hipMemAddressReserve"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemAddressReserve()</span></code></a>
function. The size of the virtual memory must match the amount of physical
memory previously allocated. You can then map the physical memory allocation to
the newly-acquired virtual memory address range using the <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv49hipMemMapPv6size_t6size_t31hipMemGenericAllocationHandle_ty" title="hipMemMap"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemMap()</span></code></a>
function.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipMemAddressReserve</span><span class="p">(</span><span class="o">&amp;</span><span class="n">ptr</span><span class="p">,</span><span class="w"> </span><span class="n">padded_size</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
<span class="n">hipMemMap</span><span class="p">(</span><span class="n">ptr</span><span class="p">,</span><span class="w"> </span><span class="n">padded_size</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">allocHandle</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
</pre></div>
</div>
</section>
<section id="set-memory-access">
<span id="id2"></span><h3>Set memory access<a class="headerlink" href="#set-memory-access" title="Link to this heading">#</a></h3>
<p>Finally, use the <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv415hipMemSetAccessPv6size_tPK16hipMemAccessDesc6size_t" title="hipMemSetAccess"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemSetAccess()</span></code></a> function to enable memory access.
It accepts the pointer to the virtual memory, the size, and a
<code class="xref cpp cpp-struct docutils literal notranslate"><span class="pre">hipMemAccessDesc</span></code> descriptor as parameters. In a multi-GPU
environment, you can map the device memory of one GPU to another. This feature
also works with the traditional memory management system, but isn’t as scalable
as with virtual memory. When memory is allocated with <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a>,
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/peer_to_peer_device_memory_access.html#_CPPv425hipDeviceEnablePeerAccessij" title="hipDeviceEnablePeerAccess"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipDeviceEnablePeerAccess()</span></code></a> is used to enable peer access. This
function enables access between two devices, but it means that every call to
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a> takes more time to perform the checks and the mapping
between the devices. When using virtual memory management, peer access is
enabled by <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv415hipMemSetAccessPv6size_tPK16hipMemAccessDesc6size_t" title="hipMemSetAccess"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemSetAccess()</span></code></a>, which provides a finer level of
control over what is shared. This has no performance impact on memory allocation
and gives you more control over what memory buffers are shared with which
devices.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipMemAccessDesc</span><span class="w"> </span><span class="n">accessDesc</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{};</span>
<span class="n">accessDesc</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemLocationTypeDevice</span><span class="p">;</span>
<span class="n">accessDesc</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">id</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">currentDev</span><span class="p">;</span>
<span class="n">accessDesc</span><span class="p">.</span><span class="n">flags</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemAccessFlagsProtReadwrite</span><span class="p">;</span>
<span class="n">hipMemSetAccess</span><span class="p">(</span><span class="n">ptr</span><span class="p">,</span><span class="w"> </span><span class="n">padded_size</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">accessDesc</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">);</span>
</pre></div>
</div>
<p>At this point the memory is allocated, mapped, and ready for use. You can read
and write to it, just like you would a C style memory allocation.</p>
</section>
<section id="dynamically-increase-allocation-size">
<span id="usage-virtual-memory"></span><h3>Dynamically increase allocation size<a class="headerlink" href="#dynamically-increase-allocation-size" title="Link to this heading">#</a></h3>
<p>To increase the amount of pre-allocated memory, use
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv420hipMemAddressReservePPv6size_t6size_tPvy" title="hipMemAddressReserve"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemAddressReserve()</span></code></a>, which accepts the starting address, and the
size of the reservation in bytes. This allows you to have a continuous virtual
address space without worrying about the underlying physical allocation.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipMemAddressReserve</span><span class="p">(</span><span class="o">&amp;</span><span class="n">new_ptr</span><span class="p">,</span><span class="w"> </span><span class="p">(</span><span class="n">new_size</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">padded_size</span><span class="p">),</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">ptr</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">padded_size</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
<span class="n">hipMemMap</span><span class="p">(</span><span class="n">new_ptr</span><span class="p">,</span><span class="w"> </span><span class="p">(</span><span class="n">new_size</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">padded_size</span><span class="p">),</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">newAllocHandle</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
<span class="n">hipMemSetAccess</span><span class="p">(</span><span class="n">new_ptr</span><span class="p">,</span><span class="w"> </span><span class="p">(</span><span class="n">new_size</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="n">padded_size</span><span class="p">),</span><span class="w"> </span><span class="o">&amp;</span><span class="n">accessDesc</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">);</span>
</pre></div>
</div>
<p>The code sample above assumes that <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv420hipMemAddressReservePPv6size_t6size_tPvy" title="hipMemAddressReserve"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemAddressReserve()</span></code></a> was able to
reserve the memory address at the specified location. However, this isn’t
guaranteed to be true, so you should validate that <code class="docutils literal notranslate"><span class="pre">new_ptr</span></code> points to a
specific virtual address before using it.</p>
</section>
<section id="free-virtual-memory">
<span id="id3"></span><h3>Free virtual memory<a class="headerlink" href="#free-virtual-memory" title="Link to this heading">#</a></h3>
<p>To free the memory allocated in this manner, use the corresponding free
functions. To unmap the memory, use <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv411hipMemUnmapPv6size_t" title="hipMemUnmap"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemUnmap()</span></code></a>. To release the
virtual address range, use <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv417hipMemAddressFreePv6size_t" title="hipMemAddressFree"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemAddressFree()</span></code></a>.  Finally, to release
the physical memory, use <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv413hipMemRelease31hipMemGenericAllocationHandle_t" title="hipMemRelease"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemRelease()</span></code></a>. A side effect of these
functions is the lack of synchronization when memory is released. If you call
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv47hipFreePv" title="hipFree"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipFree()</span></code></a> when you have multiple streams running in parallel, it
synchronizes the device. This causes worse resource usage and performance.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipMemUnmap</span><span class="p">(</span><span class="n">ptr</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>
<span class="n">hipMemRelease</span><span class="p">(</span><span class="n">allocHandle</span><span class="p">);</span>
<span class="n">hipMemAddressFree</span><span class="p">(</span><span class="n">ptr</span><span class="p">,</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>
</pre></div>
</div>
</section>
</section>
<section id="example-code">
<h2>Example code<a class="headerlink" href="#example-code" title="Link to this heading">#</a></h2>
<p>The virtual memory management example follows these steps:</p>
<ol class="arabic simple">
<li><p>Check virtual memory management <a class="reference internal" href="#vmm-support"><span class="std std-ref">support</span></a>:
The <a class="reference internal" href="../../../reference/hip_runtime_api/modules/device_management.html#_CPPv421hipDeviceGetAttributePi20hipDeviceAttribute_ti" title="hipDeviceGetAttribute"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipDeviceGetAttribute()</span></code></a> function is used to check the virtual
memory management support of the GPU with ID 0.</p></li>
<li><p>Physical memory <a class="reference internal" href="#allocate-physical-memory"><span class="std std-ref">allocation</span></a>: Physical memory
is allocated using <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv412hipMemCreateP31hipMemGenericAllocationHandle_t6size_tPK20hipMemAllocationPropy" title="hipMemCreate"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemCreate()</span></code></a> with pinned memory on the
device.</p></li>
<li><p>Virtual memory <a class="reference internal" href="#reserve-virtual-address"><span class="std std-ref">reservation</span></a>: Virtual address
range is reserved using <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv420hipMemAddressReservePPv6size_t6size_tPvy" title="hipMemAddressReserve"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemAddressReserve()</span></code></a>.</p></li>
<li><p>Mapping virtual address to physical memory: The physical memory is mapped
to a virtual address (<code class="docutils literal notranslate"><span class="pre">virtualPointer</span></code>) using <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv49hipMemMapPv6size_t6size_t31hipMemGenericAllocationHandle_ty" title="hipMemMap"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemMap()</span></code></a>.</p></li>
<li><p>Memory <a class="reference internal" href="#set-memory-access"><span class="std std-ref">access permissions</span></a>: Permission is set for
pointer to allow read and write access using <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv415hipMemSetAccessPv6size_tPK16hipMemAccessDesc6size_t" title="hipMemSetAccess"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemSetAccess()</span></code></a>.</p></li>
<li><p>Memory operation: Data is written to the memory via <code class="docutils literal notranslate"><span class="pre">virtualPointer</span></code>.</p></li>
<li><p>Launch kernels: The <code class="docutils literal notranslate"><span class="pre">zeroAddr</span></code> and <code class="docutils literal notranslate"><span class="pre">fillAddr</span></code> kernels are
launched using the virtual memory pointer.</p></li>
<li><p><a class="reference internal" href="#free-virtual-memory"><span class="std std-ref">Cleanup</span></a>: The mappings, physical memory, and
virtual address are released at the end to avoid memory leaks.</p></li>
</ol>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define ROUND_UP(SIZE,GRANULARITY) ((1 + SIZE / GRANULARITY) * GRANULARITY)</span>

<span class="cp">#define HIP_CHECK(expression)              \</span>
<span class="cp">{                                          \</span>
<span class="cp">    const hipError_t err = expression;     \</span>
<span class="cp">    if(err != hipSuccess){                 \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error: &quot;         \</span>
<span class="cp">            &lt;&lt; hipGetErrorString(err)      \</span>
<span class="cp">            &lt;&lt; &quot; at &quot; &lt;&lt; __LINE__ &lt;&lt; &quot;\n&quot;; \</span>
<span class="cp">    }                                      \</span>
<span class="cp">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">zeroAddr</span><span class="p">(</span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">pointer</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="o">*</span><span class="n">pointer</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">fillAddr</span><span class="p">(</span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">pointer</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="o">*</span><span class="n">pointer</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">42</span><span class="p">;</span>
<span class="p">}</span>


<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">currentDev</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Step 1: Check virtual memory management support on device 0</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">vmm</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span>
<span class="w">        </span><span class="n">hipDeviceGetAttribute</span><span class="p">(</span>
<span class="w">            </span><span class="o">&amp;</span><span class="n">vmm</span><span class="p">,</span><span class="w"> </span><span class="n">hipDeviceAttributeVirtualMemoryManagementSupported</span><span class="p">,</span><span class="w"> </span><span class="n">currentDev</span>
<span class="w">        </span><span class="p">)</span>
<span class="w">    </span><span class="p">);</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Virtual memory management support value: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">vmm</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">vmm</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;GPU 0 doesn&#39;t support virtual memory management.&quot;</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Size of memory to allocate</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">4</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Step 2: Allocate physical memory</span>
<span class="w">    </span><span class="n">hipMemGenericAllocationHandle_t</span><span class="w"> </span><span class="n">allocHandle</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipMemAllocationProp</span><span class="w"> </span><span class="n">prop</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{};</span>
<span class="w">    </span><span class="n">prop</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemAllocationTypePinned</span><span class="p">;</span>
<span class="w">    </span><span class="n">prop</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemLocationTypeDevice</span><span class="p">;</span>
<span class="w">    </span><span class="n">prop</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">id</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">currentDev</span><span class="p">;</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">granularity</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span>
<span class="w">        </span><span class="n">hipMemGetAllocationGranularity</span><span class="p">(</span>
<span class="w">            </span><span class="o">&amp;</span><span class="n">granularity</span><span class="p">,</span>
<span class="w">            </span><span class="o">&amp;</span><span class="n">prop</span><span class="p">,</span>
<span class="w">            </span><span class="n">hipMemAllocationGranularityMinimum</span><span class="p">));</span>
<span class="w">    </span><span class="kt">size_t</span><span class="w"> </span><span class="n">padded_size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">ROUND_UP</span><span class="p">(</span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">granularity</span><span class="p">);</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">allocHandle</span><span class="p">,</span><span class="w"> </span><span class="n">padded_size</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">prop</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Step 3: Reserve a virtual memory address range</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">virtualPointer</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">nullptr</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemAddressReserve</span><span class="p">(</span><span class="o">&amp;</span><span class="n">virtualPointer</span><span class="p">,</span><span class="w"> </span><span class="n">padded_size</span><span class="p">,</span><span class="w"> </span><span class="n">granularity</span><span class="p">,</span><span class="w"> </span><span class="k">nullptr</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Step 4: Map the physical memory to the virtual address range</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemMap</span><span class="p">(</span><span class="n">virtualPointer</span><span class="p">,</span><span class="w"> </span><span class="n">padded_size</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">allocHandle</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Step 5: Set memory access permission for pointer</span>
<span class="w">    </span><span class="n">hipMemAccessDesc</span><span class="w"> </span><span class="n">accessDesc</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{};</span>
<span class="w">    </span><span class="n">accessDesc</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemLocationTypeDevice</span><span class="p">;</span>
<span class="w">    </span><span class="n">accessDesc</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">id</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">currentDev</span><span class="p">;</span>
<span class="w">    </span><span class="n">accessDesc</span><span class="p">.</span><span class="n">flags</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemAccessFlagsProtReadWrite</span><span class="p">;</span>

<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemSetAccess</span><span class="p">(</span><span class="n">virtualPointer</span><span class="p">,</span><span class="w"> </span><span class="n">padded_size</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">accessDesc</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Step 6: Perform memory operation</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">value</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">42</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">virtualPointer</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">value</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="o">&amp;</span><span class="n">result</span><span class="p">,</span><span class="w"> </span><span class="n">virtualPointer</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">42</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Success. Value: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failure. Value: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Step 7: Launch kernels</span>
<span class="w">    </span><span class="c1">// Launch zeroAddr kernel</span>
<span class="w">    </span><span class="n">zeroAddr</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="o">&gt;&gt;&gt;</span><span class="p">((</span><span class="kt">int</span><span class="o">*</span><span class="p">)</span><span class="n">virtualPointer</span><span class="p">);</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Check zeroAddr kernel result</span>
<span class="w">    </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="o">&amp;</span><span class="n">result</span><span class="p">,</span><span class="w"> </span><span class="n">virtualPointer</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Success. zeroAddr kernel: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failure. zeroAddr kernel: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Launch fillAddr kernel</span>
<span class="w">    </span><span class="n">fillAddr</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="o">&gt;&gt;&gt;</span><span class="p">((</span><span class="kt">int</span><span class="o">*</span><span class="p">)</span><span class="n">virtualPointer</span><span class="p">);</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Check fillAddr kernel result</span>
<span class="w">    </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="o">&amp;</span><span class="n">result</span><span class="p">,</span><span class="w"> </span><span class="n">virtualPointer</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>
<span class="w">    </span><span class="k">if</span><span class="p">(</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">42</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Success. fillAddr kernel: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Failure. fillAddr kernel: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Step 8: Cleanup</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemUnmap</span><span class="p">(</span><span class="n">virtualPointer</span><span class="p">,</span><span class="w"> </span><span class="n">padded_size</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemRelease</span><span class="p">(</span><span class="n">allocHandle</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemAddressFree</span><span class="p">(</span><span class="n">virtualPointer</span><span class="p">,</span><span class="w"> </span><span class="n">padded_size</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="virtual-aliases">
<h2>Virtual aliases<a class="headerlink" href="#virtual-aliases" title="Link to this heading">#</a></h2>
<p>Virtual aliases are multiple virtual memory addresses mapping to the same
physical memory on the GPU. When this occurs, different threads, processes, or memory
allocations to access shared physical memory through different virtual
addresses on different devices.</p>
<p>Multiple virtual memory mappings can be created using multiple calls to
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/virtual_memory_reference.html#_CPPv49hipMemMapPv6size_t6size_t31hipMemGenericAllocationHandle_ty" title="hipMemMap"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemMap()</span></code></a> on the same memory allocation.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>RDNA cards may not produce correct results, if users access two different
virtual addresses that map to the same physical address. In this case, the
L1 data caches will be incoherent due to the virtual-to-physical aliasing.
These GPUs will produce correct results if users access virtual-to-physical
aliases using volatile pointers.</p>
<p>NVIDIA GPUs require special fences to produce correct results when
using virtual aliases.</p>
</div>
<p>In the following code block, the kernels input device pointers are virtual
aliases of the same memory allocation:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">updateBoth</span><span class="p">(</span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">pointerA</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">pointerB</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// May produce incorrect results on RDNA and NVIDIA cards.</span>
<span class="w">    </span><span class="o">*</span><span class="n">pointerA</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="o">*</span><span class="n">pointerB</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">42</span><span class="p">;</span>
<span class="p">}</span>

<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">updateBoth_v2</span><span class="p">(</span><span class="k">volatile</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">pointerA</span><span class="p">,</span><span class="w"> </span><span class="k">volatile</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">pointerB</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// May produce incorrect results on NVIDIA cards.</span>
<span class="w">    </span><span class="o">*</span><span class="n">pointerA</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="o">*</span><span class="n">pointerB</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">42</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="unified_memory.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Unified memory management</p>
      </div>
    </a>
    <a class="right-next"
       href="stream_ordered_allocator.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Stream Ordered Memory Allocator</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-allocation">Memory allocation</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#virtual-memory-management-support">Virtual memory management support</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#allocate-physical-memory">Allocate physical memory</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#reserve-virtual-address-range">Reserve virtual address range</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#set-memory-access">Set memory access</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#dynamically-increase-allocation-size">Dynamically increase allocation size</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#free-virtual-memory">Free virtual memory</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#example-code">Example code</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#virtual-aliases">Virtual aliases</a></li>
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
