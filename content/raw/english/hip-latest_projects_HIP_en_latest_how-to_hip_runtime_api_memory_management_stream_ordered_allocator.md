---
title: "Stream Ordered Memory Allocator &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/memory_management/stream_ordered_allocator.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:07:54.324943+00:00
content_hash: "8c6407a8092a8940"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="stream, memory allocation, SOMA, stream ordered memory allocator" name="keywords" />

    <title>Stream Ordered Memory Allocator &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/hip_runtime_api/memory_management/stream_ordered_allocator';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Error handling" href="../error_handling.html" />
    <link rel="prev" title="Virtual memory management" href="virtual_memory.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/hip_runtime_api/memory_management/stream_ordered_allocator.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l3"><a class="reference internal" href="virtual_memory.html">Virtual memory management</a></li>
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Stream Ordered Memory Allocator</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">Stream...</li>
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
    <h1>Stream Ordered Memory Allocator</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#using-soma">Using SOMA</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-pools">Memory pools</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#set-pools">Set pools</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#trim-pools">Trim pools</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#resource-usage-statistics">Resource usage statistics</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-reuse-policies">Memory reuse policies</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#device-accessibility-for-multi-gpu-support">Device accessibility for multi-GPU support</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#interprocess-memory-handling">Interprocess memory handling</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#device-pointer">Device pointer</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#shareable-handle">Shareable handle</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="stream-ordered-memory-allocator">
<span id="stream-ordered-memory-allocator-how-to"></span><h1>Stream Ordered Memory Allocator<a class="headerlink" href="#stream-ordered-memory-allocator" title="Link to this heading">#</a></h1>
<p>The Stream Ordered Memory Allocator (SOMA) is part of the HIP runtime API. SOMA provides an asynchronous memory allocation mechanism with stream-ordering semantics. You can use SOMA to allocate and free memory in stream order, which ensures that all asynchronous accesses occur between the stream executions of allocation and deallocation. Compliance with stream order prevents use-before-allocation or use-after-free errors, which helps to avoid an undefined behavior.</p>
<p>Advantages of SOMA:</p>
<ul class="simple">
<li><p>Efficient reuse: Enables efficient memory reuse across streams, which reduces unnecessary allocation overhead.</p></li>
<li><p>Fine-grained control: Allows you to set attributes and control caching behavior for memory pools.</p></li>
<li><p>Inter-process sharing: Enables secure sharing of allocations between processes.</p></li>
<li><p>Optimizations: Allows driver to optimize based on its awareness of SOMA and other stream management APIs.</p></li>
</ul>
<p>Disadvantages of SOMA:</p>
<ul class="simple">
<li><p>Temporal constraints: Requires you to adhere strictly to stream order to avoid errors.</p></li>
<li><p>Complexity: Involves memory management in stream order, which can be intricate.</p></li>
<li><p>Learning curve: Requires you to put additional efforts to understand and utilize SOMA effectively.</p></li>
</ul>
<section id="using-soma">
<h2>Using SOMA<a class="headerlink" href="#using-soma" title="Link to this heading">#</a></h2>
<p>You can allocate memory using <code class="docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code> with stream-ordered
semantics. This restricts the asynchronous access to the memory between the stream executions of the allocation and deallocation. Accessing
memory if the compliant memory accesses won’t overlap
temporally. <code class="docutils literal notranslate"><span class="pre">hipFreeAsync()</span></code> frees memory from the pool with stream-ordered
semantics.</p>
<p>Here is how to use stream ordered memory allocation:</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Stream Ordered Memory Allocation</label><div class="sd-tab-content docutils">
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

<span class="c1">// Kernel to perform some computation on allocated memory.</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">myKernel</span><span class="p">(</span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">numElements</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numElements</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">data</span><span class="p">[</span><span class="n">tid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// Stream 0.</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">streamId</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Allocate memory with stream ordered semantics.</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">numElements</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">devData</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocAsync</span><span class="p">(</span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">**&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">devData</span><span class="p">),</span><span class="w"> </span><span class="n">numElements</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">devData</span><span class="p">),</span><span class="w"> </span><span class="n">streamId</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Launch the kernel to perform computation.</span>
<span class="w">    </span><span class="n">dim3</span><span class="w"> </span><span class="nf">blockSize</span><span class="p">(</span><span class="mi">256</span><span class="p">);</span>
<span class="w">    </span><span class="n">dim3</span><span class="w"> </span><span class="n">gridSize</span><span class="p">((</span><span class="n">numElements</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockSize</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="mi">1</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">blockSize</span><span class="p">.</span><span class="n">x</span><span class="p">);</span>
<span class="w">    </span><span class="n">myKernel</span><span class="o">&lt;&lt;&lt;</span><span class="n">gridSize</span><span class="p">,</span><span class="w"> </span><span class="n">blockSize</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">devData</span><span class="p">,</span><span class="w"> </span><span class="n">numElements</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Copy data back to host.</span>
<span class="w">    </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">hostData</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="p">[</span><span class="n">numElements</span><span class="p">];</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">hostData</span><span class="p">,</span><span class="w"> </span><span class="n">devData</span><span class="p">,</span><span class="w"> </span><span class="n">numElements</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">devData</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Print the array.</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numElements</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Element &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hostData</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Free memory with stream ordered semantics.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFreeAsync</span><span class="p">(</span><span class="n">devData</span><span class="p">,</span><span class="w"> </span><span class="n">streamId</span><span class="p">));</span>
<span class="w">    </span><span class="k">delete</span><span class="p">[]</span><span class="w"> </span><span class="n">hostData</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Synchronize to ensure completion.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Ordinary Allocation</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstddef&gt;</span>
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

<span class="c1">// Kernel to perform some computation on allocated memory.</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">myKernel</span><span class="p">(</span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">numElements</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numElements</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">data</span><span class="p">[</span><span class="n">tid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// Allocate memory.</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">numElements</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">devData</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">devData</span><span class="p">,</span><span class="w"> </span><span class="n">numElements</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">devData</span><span class="p">)));</span>

<span class="w">    </span><span class="c1">// Launch the kernel to perform computation.</span>
<span class="w">    </span><span class="n">dim3</span><span class="w"> </span><span class="nf">blockSize</span><span class="p">(</span><span class="mi">256</span><span class="p">);</span>
<span class="w">    </span><span class="n">dim3</span><span class="w"> </span><span class="n">gridSize</span><span class="p">((</span><span class="n">numElements</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockSize</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="mi">1</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">blockSize</span><span class="p">.</span><span class="n">x</span><span class="p">);</span>
<span class="w">    </span><span class="n">myKernel</span><span class="o">&lt;&lt;&lt;</span><span class="n">gridSize</span><span class="p">,</span><span class="w"> </span><span class="n">blockSize</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">devData</span><span class="p">,</span><span class="w"> </span><span class="n">numElements</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Copy data back to host.</span>
<span class="w">    </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">hostData</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="p">[</span><span class="n">numElements</span><span class="p">];</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">hostData</span><span class="p">,</span><span class="w"> </span><span class="n">devData</span><span class="p">,</span><span class="w"> </span><span class="n">numElements</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">devData</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Print the array.</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numElements</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Element &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hostData</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Free memory.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">devData</span><span class="p">));</span>
<span class="w">    </span><span class="k">delete</span><span class="p">[]</span><span class="w"> </span><span class="n">hostData</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Synchronize to ensure completion.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
</div>
<p>For more details, see <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html#stream-ordered-memory-allocator-reference"><span class="std std-ref">Stream ordered memory allocator</span></a>.</p>
</section>
<section id="memory-pools">
<h2>Memory pools<a class="headerlink" href="#memory-pools" title="Link to this heading">#</a></h2>
<p>Memory pools provide a way to manage memory with stream-ordered behavior while ensuring proper synchronization and avoiding memory access errors. Division of a single memory system into separate pools facilitates querying the access path properties for each partition. Memory pools are used for host memory, device memory, and unified memory.</p>
<section id="set-pools">
<h3>Set pools<a class="headerlink" href="#set-pools" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code> function uses the current memory pool and also provides the opportunity to create and access different pools using <code class="docutils literal notranslate"><span class="pre">hipMemPoolCreate()</span></code> and <code class="docutils literal notranslate"><span class="pre">hipMallocFromPoolAsync()</span></code> functions respectively.</p>
<p>Unlike NVIDIA CUDA, where stream-ordered memory allocation can be implicit, ROCm HIP is explicit. This requires managing memory allocation for each stream in HIP while ensuring precise control over memory usage and synchronization.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstddef&gt;</span>
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

<span class="c1">// Kernel to perform some computation on allocated memory.</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">myKernel</span><span class="p">(</span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">numElements</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">threadIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockIdx</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">blockDim</span><span class="p">.</span><span class="n">x</span><span class="p">;</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">tid</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numElements</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">data</span><span class="p">[</span><span class="n">tid</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">tid</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// Create a stream.</span>
<span class="w">    </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">stream</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">stream</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Create a memory pool with default properties.</span>
<span class="w">    </span><span class="n">hipMemPoolProps</span><span class="w"> </span><span class="n">poolProps</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{};</span>
<span class="w">    </span><span class="n">poolProps</span><span class="p">.</span><span class="n">allocType</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemAllocationTypePinned</span><span class="p">;</span>
<span class="w">    </span><span class="n">poolProps</span><span class="p">.</span><span class="n">handleTypes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemHandleTypePosixFileDescriptor</span><span class="p">;</span>
<span class="w">    </span><span class="n">poolProps</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemLocationTypeDevice</span><span class="p">;</span>
<span class="w">    </span><span class="n">poolProps</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">id</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="c1">// Assuming device 0.</span>

<span class="w">    </span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">memPool</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPoolCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">poolProps</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Allocate memory from the pool asynchronously.</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">numElements</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">devData</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">nullptr</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocFromPoolAsync</span><span class="p">(</span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="kt">void</span><span class="o">**&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">devData</span><span class="p">),</span>
<span class="w">                                     </span><span class="n">numElements</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">devData</span><span class="p">),</span>
<span class="w">                                     </span><span class="n">memPool</span><span class="p">,</span>
<span class="w">                                     </span><span class="n">stream</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Define grid and block sizes.</span>
<span class="w">    </span><span class="n">dim3</span><span class="w"> </span><span class="nf">blockSize</span><span class="p">(</span><span class="mi">256</span><span class="p">);</span>
<span class="w">    </span><span class="n">dim3</span><span class="w"> </span><span class="n">gridSize</span><span class="p">((</span><span class="n">numElements</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">blockSize</span><span class="p">.</span><span class="n">x</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="mi">1</span><span class="p">)</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">blockSize</span><span class="p">.</span><span class="n">x</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Launch the kernel to perform computation.</span>
<span class="w">    </span><span class="n">myKernel</span><span class="o">&lt;&lt;&lt;</span><span class="n">gridSize</span><span class="p">,</span><span class="w"> </span><span class="n">blockSize</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">devData</span><span class="p">,</span><span class="w"> </span><span class="n">numElements</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Synchronize the stream.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamSynchronize</span><span class="p">(</span><span class="n">stream</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Copy data back to host.</span>
<span class="w">    </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">hostData</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="p">[</span><span class="n">numElements</span><span class="p">];</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">hostData</span><span class="p">,</span><span class="w"> </span><span class="n">devData</span><span class="p">,</span><span class="w"> </span><span class="n">numElements</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">devData</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Print the array.</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">numElements</span><span class="p">;</span><span class="w"> </span><span class="o">++</span><span class="n">i</span><span class="p">)</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Element &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hostData</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Free the allocated memory.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFreeAsync</span><span class="p">(</span><span class="n">devData</span><span class="p">,</span><span class="w"> </span><span class="n">stream</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Synchronize the stream again to ensure all operations are complete.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamSynchronize</span><span class="p">(</span><span class="n">stream</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Destroy the memory pool and stream.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPoolDestroy</span><span class="p">(</span><span class="n">memPool</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipStreamDestroy</span><span class="p">(</span><span class="n">stream</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Free host memory.</span>
<span class="w">    </span><span class="k">delete</span><span class="p">[]</span><span class="w"> </span><span class="n">hostData</span><span class="p">;</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="trim-pools">
<h3>Trim pools<a class="headerlink" href="#trim-pools" title="Link to this heading">#</a></h3>
<p>The memory allocator allows you to allocate and free memory in stream order. To control memory usage, set the release threshold attribute using <code class="docutils literal notranslate"><span class="pre">hipMemPoolAttrReleaseThreshold</span></code>.  This threshold specifies the amount of reserved memory in bytes to hold onto.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="w"> </span><span class="n">threshold</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">numeric_limits</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="o">&gt;::</span><span class="n">max</span><span class="p">();</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPoolSetAttribute</span><span class="p">(</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemPoolAttrReleaseThreshold</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">threshold</span><span class="p">));</span>
</pre></div>
</div>
<p>When the amount of memory held in the memory pool exceeds the threshold, the allocator tries to release memory back to the operating system during the next call to stream, event, or context synchronization.</p>
<p>To improve performance, it is a good practice to adjust the memory pool size using <code class="docutils literal notranslate"><span class="pre">hipMemPoolTrimTo()</span></code>. It helps to reclaim memory from an excessive memory pool, which optimizes memory usage for your application.</p>
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

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">memPool</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipDevice_t</span><span class="w"> </span><span class="n">device</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="c1">// Specify the device index.</span>

<span class="w">    </span><span class="c1">// Initialize the device.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">device</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Get the default memory pool for the device.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceGetDefaultMemPool</span><span class="p">(</span><span class="o">&amp;</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="n">device</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Allocate memory from the pool (e.g., 1 MB).</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">allocSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1024</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">ptr</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">ptr</span><span class="p">,</span><span class="w"> </span><span class="n">allocSize</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Free the allocated memory.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">ptr</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Trim the memory pool to a specific size (e.g., 512 KB).</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">newSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">512</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPoolTrimTo</span><span class="p">(</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="n">newSize</span><span class="p">));</span>

<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Memory pool trimmed to &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">newSize</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; bytes.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="resource-usage-statistics">
<h3>Resource usage statistics<a class="headerlink" href="#resource-usage-statistics" title="Link to this heading">#</a></h3>
<p>Resource usage statistics help in optimization. Here is the list of pool attributes used to query memory usage:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolAttrReservedMemCurrent</span></code>: Returns the total physical GPU memory currently held in the pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolAttrUsedMemCurrent</span></code>: Returns the total size of all the memory allocated from the pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolAttrReservedMemHigh</span></code>: Returns the total physical GPU memory held in the pool since the last reset.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolAttrUsedMemHigh</span></code>: Returns the total size of all the memory allocated from the pool since the last reset.</p></li>
</ul>
<p>To reset these attributes to the current value, use <code class="docutils literal notranslate"><span class="pre">hipMemPoolSetAttribute()</span></code>.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstddef&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstdint&gt;</span>
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

<span class="c1">// Sample helper functions for getting the usage statistics in bulk.</span>
<span class="k">struct</span><span class="w"> </span><span class="nc">usageStatistics</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="w"> </span><span class="n">reservedMemCurrent</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="w"> </span><span class="n">reservedMemHigh</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="w"> </span><span class="n">usedMemCurrent</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="w"> </span><span class="n">usedMemHigh</span><span class="p">;</span>
<span class="p">};</span>

<span class="kt">void</span><span class="w"> </span><span class="nf">getUsageStatistics</span><span class="p">(</span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="k">struct</span><span class="w"> </span><span class="nc">usageStatistics</span><span class="w"> </span><span class="o">*</span><span class="n">statistics</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPoolGetAttribute</span><span class="p">(</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemPoolAttrReservedMemCurrent</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">statistics</span><span class="o">-&gt;</span><span class="n">reservedMemCurrent</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPoolGetAttribute</span><span class="p">(</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemPoolAttrReservedMemHigh</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">statistics</span><span class="o">-&gt;</span><span class="n">reservedMemHigh</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPoolGetAttribute</span><span class="p">(</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemPoolAttrUsedMemCurrent</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">statistics</span><span class="o">-&gt;</span><span class="n">usedMemCurrent</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPoolGetAttribute</span><span class="p">(</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemPoolAttrUsedMemHigh</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">statistics</span><span class="o">-&gt;</span><span class="n">usedMemHigh</span><span class="p">));</span>
<span class="p">}</span>

<span class="c1">// Resetting the watermarks resets them to the current value.</span>
<span class="kt">void</span><span class="w"> </span><span class="nf">resetStatistics</span><span class="p">(</span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">memPool</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="kt">uint64_t</span><span class="w"> </span><span class="n">value</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPoolSetAttribute</span><span class="p">(</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemPoolAttrReservedMemHigh</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">value</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPoolSetAttribute</span><span class="p">(</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemPoolAttrUsedMemHigh</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">value</span><span class="p">));</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">memPool</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipDevice_t</span><span class="w"> </span><span class="n">device</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="c1">// Specify the device index.</span>

<span class="w">    </span><span class="c1">// Initialize the device.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">device</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Get the default memory pool for the device.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceGetDefaultMemPool</span><span class="p">(</span><span class="o">&amp;</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="n">device</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Allocate memory from the pool (e.g., 1 MB).</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">allocSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1024</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">ptr</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">ptr</span><span class="p">,</span><span class="w"> </span><span class="n">allocSize</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Free the allocated memory.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">ptr</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Trim the memory pool to a specific size (e.g., 512 KB).</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">newSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">512</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">1024</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPoolTrimTo</span><span class="p">(</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="n">newSize</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Get and print usage statistics before resetting.</span>
<span class="w">    </span><span class="n">usageStatistics</span><span class="w"> </span><span class="n">statsBefore</span><span class="p">;</span>
<span class="w">    </span><span class="n">getUsageStatistics</span><span class="p">(</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">statsBefore</span><span class="p">);</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Before resetting statistics:&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Reserved Memory Current: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">statsBefore</span><span class="p">.</span><span class="n">reservedMemCurrent</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; bytes&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Reserved Memory High: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">statsBefore</span><span class="p">.</span><span class="n">reservedMemHigh</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; bytes&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Used Memory Current: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">statsBefore</span><span class="p">.</span><span class="n">usedMemCurrent</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; bytes&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Used Memory High: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">statsBefore</span><span class="p">.</span><span class="n">usedMemHigh</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; bytes&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Reset the statistics.</span>
<span class="w">    </span><span class="n">resetStatistics</span><span class="p">(</span><span class="n">memPool</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Get and print usage statistics after resetting.</span>
<span class="w">    </span><span class="n">usageStatistics</span><span class="w"> </span><span class="n">statsAfter</span><span class="p">;</span>
<span class="w">    </span><span class="n">getUsageStatistics</span><span class="p">(</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">statsAfter</span><span class="p">);</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;After resetting statistics:&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Reserved Memory Current: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">statsAfter</span><span class="p">.</span><span class="n">reservedMemCurrent</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; bytes&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Reserved Memory High: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">statsAfter</span><span class="p">.</span><span class="n">reservedMemHigh</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; bytes&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Used Memory Current: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">statsAfter</span><span class="p">.</span><span class="n">usedMemCurrent</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; bytes&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Used Memory High: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">statsAfter</span><span class="p">.</span><span class="n">usedMemHigh</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; bytes&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="n">EXIT_SUCCESS</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="memory-reuse-policies">
<h3>Memory reuse policies<a class="headerlink" href="#memory-reuse-policies" title="Link to this heading">#</a></h3>
<p>The allocator might reallocate memory as long as the compliant memory accesses will not to overlap temporally. To optimize the memory usage, disable or enable the following memory pool reuse policy attribute flags:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolReuseFollowEventDependencies</span></code>: Checks event dependencies before allocating additional GPU memory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolReuseAllowOpportunistic</span></code>: Checks freed allocations to determine if the stream order semantic indicated by the free operation has been met.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemPoolReuseAllowInternalDependencies</span></code>: Manages reuse based on internal dependencies in runtime. If the driver fails to allocate and map additional physical memory, it searches for memory waiting for another stream’s progress and reuses it.</p></li>
</ul>
</section>
<section id="device-accessibility-for-multi-gpu-support">
<h3>Device accessibility for multi-GPU support<a class="headerlink" href="#device-accessibility-for-multi-gpu-support" title="Link to this heading">#</a></h3>
<p>Allocations are initially accessible from the device where they reside.</p>
</section>
</section>
<section id="interprocess-memory-handling">
<h2>Interprocess memory handling<a class="headerlink" href="#interprocess-memory-handling" title="Link to this heading">#</a></h2>
<div class="admonition attention">
<p class="admonition-title">Attention</p>
<p>IPC API calls are only supported on systems with an active <code class="docutils literal notranslate"><span class="pre">amdgpu-dkms</span></code> driver. Please refer to the
<a class="reference external" href="https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/index.html">AMDGPU documentation</a> for information
on how to install <code class="docutils literal notranslate"><span class="pre">amdgpu-dkms</span></code>.</p>
</div>
<p>Interprocess capable (IPC) memory pools facilitate efficient and secure sharing of GPU memory between processes.</p>
<p>To achieve interprocess memory sharing, you can use either <a class="reference internal" href="#device-pointer"><span class="std std-ref">device pointer</span></a> or <a class="reference internal" href="#shareable-handle"><span class="std std-ref">shareable handle</span></a>. Both provide allocator (export) and consumer (import) interfaces.</p>
<section id="device-pointer">
<span id="id1"></span><h3>Device pointer<a class="headerlink" href="#device-pointer" title="Link to this heading">#</a></h3>
<p>To export data to share a memory pool pointer directly between processes, use <code class="docutils literal notranslate"><span class="pre">hipMemPoolExportPointer()</span></code>. It allows you to share a memory allocation with another process.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;fstream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;sys/stat.h&gt;</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// Allocate memory.</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">devPtr</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">devPtr</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Export the memory pool pointer.</span>
<span class="w">    </span><span class="n">hipMemPoolPtrExportData</span><span class="w"> </span><span class="n">exportData</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipError_t</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemPoolExportPointer</span><span class="p">(</span><span class="o">&amp;</span><span class="n">exportData</span><span class="p">,</span><span class="w"> </span><span class="n">devPtr</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">result</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Error exporting memory pool pointer: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hipGetErrorString</span><span class="p">(</span><span class="n">result</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Create a named pipe (FIFO).</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">*</span><span class="w"> </span><span class="n">fifoPath</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;/tmp/myfifo&quot;</span><span class="p">;</span><span class="w"> </span><span class="c1">// Change this to a unique path.</span>
<span class="w">    </span><span class="n">mkfifo</span><span class="p">(</span><span class="n">fifoPath</span><span class="p">,</span><span class="w"> </span><span class="mo">0666</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Write the exported data to the named pipe.</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">ofstream</span><span class="w"> </span><span class="n">fifoStream</span><span class="p">(</span><span class="n">fifoPath</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">ios</span><span class="o">::</span><span class="n">out</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">ios</span><span class="o">::</span><span class="n">binary</span><span class="p">);</span>
<span class="w">    </span><span class="n">fifoStream</span><span class="p">.</span><span class="n">write</span><span class="p">(</span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="kt">char</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">exportData</span><span class="p">),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">hipMemPoolPtrExportData</span><span class="p">));</span>
<span class="w">    </span><span class="n">fifoStream</span><span class="p">.</span><span class="n">close</span><span class="p">();</span>

<span class="w">    </span><span class="c1">// Clean up.</span>
<span class="w">    </span><span class="n">hipFree</span><span class="p">(</span><span class="n">devPtr</span><span class="p">);</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>To import a memory pool pointer directly from another process, use <code class="docutils literal notranslate"><span class="pre">hipMemPoolImportPointer()</span></code>.</p>
<p>Here is how to read the pool exported in the preceding example:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;fstream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// Considering that you have exported the memory pool pointer already.</span>
<span class="w">    </span><span class="c1">// Now, let&#39;s simulate reading the exported data from a named pipe (FIFO).</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">*</span><span class="w"> </span><span class="n">fifoPath</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;/tmp/myfifo&quot;</span><span class="p">;</span><span class="w"> </span><span class="c1">// Change this to a unique path.</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">ifstream</span><span class="w"> </span><span class="n">fifoStream</span><span class="p">(</span><span class="n">fifoPath</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">ios</span><span class="o">::</span><span class="n">in</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">ios</span><span class="o">::</span><span class="n">binary</span><span class="p">);</span>

<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="o">!</span><span class="n">fifoStream</span><span class="p">.</span><span class="n">is_open</span><span class="p">())</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Error opening FIFO file: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">fifoPath</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Read the exported data.</span>
<span class="w">    </span><span class="n">hipMemPoolPtrExportData</span><span class="w"> </span><span class="n">importData</span><span class="p">;</span>
<span class="w">    </span><span class="n">fifoStream</span><span class="p">.</span><span class="n">read</span><span class="p">(</span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="kt">char</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">importData</span><span class="p">),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">hipMemPoolPtrExportData</span><span class="p">));</span>
<span class="w">    </span><span class="n">fifoStream</span><span class="p">.</span><span class="n">close</span><span class="p">();</span>

<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">fifoStream</span><span class="p">.</span><span class="n">fail</span><span class="p">())</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Error reading from FIFO file.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Create a memory pool with default properties.</span>
<span class="w">    </span><span class="n">hipMemPoolProps</span><span class="w"> </span><span class="n">poolProps</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{};</span>
<span class="w">    </span><span class="n">poolProps</span><span class="p">.</span><span class="n">allocType</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemAllocationTypePinned</span><span class="p">;</span>
<span class="w">    </span><span class="n">poolProps</span><span class="p">.</span><span class="n">handleTypes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemHandleTypePosixFileDescriptor</span><span class="p">;</span>
<span class="w">    </span><span class="n">poolProps</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemLocationTypeDevice</span><span class="p">;</span>
<span class="w">    </span><span class="n">poolProps</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">id</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="c1">// Assuming device 0.</span>

<span class="w">    </span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">memPool</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipMemPoolCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">poolProps</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Import the memory pool pointer.</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">importedDevPtr</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipError_t</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemPoolImportPointer</span><span class="p">(</span><span class="o">&amp;</span><span class="n">importedDevPtr</span><span class="p">,</span><span class="w"> </span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">importData</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">result</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Error imported memory pool pointer: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hipGetErrorString</span><span class="p">(</span><span class="n">result</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Now you can use the importedDevPtr for your computations.</span>

<span class="w">    </span><span class="c1">// Clean up (free the memory).</span>
<span class="w">    </span><span class="n">hipFree</span><span class="p">(</span><span class="n">importedDevPtr</span><span class="p">);</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="shareable-handle">
<span id="id2"></span><h3>Shareable handle<a class="headerlink" href="#shareable-handle" title="Link to this heading">#</a></h3>
<p>To export a memory pool pointer to a shareable handle, use <code class="docutils literal notranslate"><span class="pre">hipMemPoolExportToSharedHandle()</span></code>. This handle could be a file descriptor or a handle obtained from another process. The exported handle contains information about the memory pool, such as size, location, and other relevant details.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;fstream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;sys/stat.h&gt;</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// Create a memory pool with default properties.</span>
<span class="w">    </span><span class="n">hipMemPoolProps</span><span class="w"> </span><span class="n">poolProps</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{};</span>
<span class="w">    </span><span class="n">poolProps</span><span class="p">.</span><span class="n">allocType</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemAllocationTypePinned</span><span class="p">;</span>
<span class="w">    </span><span class="n">poolProps</span><span class="p">.</span><span class="n">handleTypes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemHandleTypePosixFileDescriptor</span><span class="p">;</span>
<span class="w">    </span><span class="n">poolProps</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemLocationTypeDevice</span><span class="p">;</span>
<span class="w">    </span><span class="n">poolProps</span><span class="p">.</span><span class="n">location</span><span class="p">.</span><span class="n">id</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="c1">// Assuming device 0.</span>

<span class="w">    </span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">memPool</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipError_t</span><span class="w"> </span><span class="n">poolResult</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemPoolCreate</span><span class="p">(</span><span class="o">&amp;</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">poolProps</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">poolResult</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Error creating memory pool: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hipGetErrorString</span><span class="p">(</span><span class="n">poolResult</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Allocate memory from the memory pool.</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">devPtr</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipMallocFromPoolAsync</span><span class="p">(</span><span class="o">&amp;</span><span class="n">devPtr</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Export the memory pool pointer.</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">descriptor</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipError_t</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemPoolExportToShareableHandle</span><span class="p">(</span><span class="o">&amp;</span><span class="n">descriptor</span><span class="p">,</span><span class="w"> </span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemHandleTypePosixFileDescriptor</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">result</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Error exporting memory pool pointer: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hipGetErrorString</span><span class="p">(</span><span class="n">result</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Create a named pipe (FIFO).</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">*</span><span class="w"> </span><span class="n">fifoPath</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;/tmp/myfifo&quot;</span><span class="p">;</span><span class="w"> </span><span class="c1">// Change this to a unique path.</span>
<span class="w">    </span><span class="n">mkfifo</span><span class="p">(</span><span class="n">fifoPath</span><span class="p">,</span><span class="w"> </span><span class="mo">0666</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Write the exported data to the named pipe.</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">ofstream</span><span class="w"> </span><span class="n">fifoStream</span><span class="p">(</span><span class="n">fifoPath</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">ios</span><span class="o">::</span><span class="n">out</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">ios</span><span class="o">::</span><span class="n">binary</span><span class="p">);</span>
<span class="w">    </span><span class="n">fifoStream</span><span class="p">.</span><span class="n">write</span><span class="p">(</span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="kt">char</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">descriptor</span><span class="p">),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">));</span>
<span class="w">    </span><span class="n">fifoStream</span><span class="p">.</span><span class="n">close</span><span class="p">();</span>

<span class="w">    </span><span class="c1">// Clean up.</span>
<span class="w">    </span><span class="n">hipFree</span><span class="p">(</span><span class="n">devPtr</span><span class="p">);</span>
<span class="w">    </span><span class="n">hipMemPoolDestroy</span><span class="p">(</span><span class="n">memPool</span><span class="p">);</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>To import and restore a memory pool pointer from a shareable handle, which could be a file descriptor or a handle obtained from another process, use <code class="docutils literal notranslate"><span class="pre">hipMemPoolImportFromShareableHandle()</span></code>. The exported shareable handle data contains information about the memory pool, including its size, location, and other relevant details. Importing the handle provides a valid memory pointer to the same memory, which allows you to share memory across different contexts.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;fstream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="c1">// Considering that you have exported the memory pool pointer already.</span>
<span class="w">    </span><span class="c1">// Now, let&#39;s simulate reading the exported data from a named pipe (FIFO).</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">*</span><span class="w"> </span><span class="n">fifoPath</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">&quot;/tmp/myfifo&quot;</span><span class="p">;</span><span class="w"> </span><span class="c1">// Change this to a unique path</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">ifstream</span><span class="w"> </span><span class="n">fifoStream</span><span class="p">(</span><span class="n">fifoPath</span><span class="p">,</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">ios</span><span class="o">::</span><span class="n">in</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">ios</span><span class="o">::</span><span class="n">binary</span><span class="p">);</span>

<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="o">!</span><span class="n">fifoStream</span><span class="p">.</span><span class="n">is_open</span><span class="p">())</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Error opening FIFO file: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">fifoPath</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Read the exported data.</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">descriptor</span><span class="p">;</span>
<span class="w">    </span><span class="n">fifoStream</span><span class="p">.</span><span class="n">read</span><span class="p">(</span><span class="k">reinterpret_cast</span><span class="o">&lt;</span><span class="kt">char</span><span class="o">*&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">descriptor</span><span class="p">),</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">));</span>
<span class="w">    </span><span class="n">fifoStream</span><span class="p">.</span><span class="n">close</span><span class="p">();</span>

<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">fifoStream</span><span class="p">.</span><span class="n">fail</span><span class="p">())</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Error reading from FIFO file.&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Import the memory pool.</span>
<span class="w">    </span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">memPool</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipError_t</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">hipMemPoolImportFromShareableHandle</span><span class="p">(</span><span class="o">&amp;</span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">descriptor</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemHandleTypePosixFileDescriptor</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">result</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">hipSuccess</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">std</span><span class="o">::</span><span class="n">cerr</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Error importing memory pool: &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">hipGetErrorString</span><span class="p">(</span><span class="n">result</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="c1">// Allocate memory from the imported memory pool.</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">importedDevPtr</span><span class="p">;</span>
<span class="w">    </span><span class="n">hipMallocFromPoolAsync</span><span class="p">(</span><span class="o">&amp;</span><span class="n">importedDevPtr</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">memPool</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Now you can use the importedDevPtr for your computations.</span>

<span class="w">    </span><span class="c1">// Clean up (free the memory).</span>
<span class="w">    </span><span class="n">hipFree</span><span class="p">(</span><span class="n">importedDevPtr</span><span class="p">);</span>
<span class="w">    </span><span class="n">hipMemPoolDestroy</span><span class="p">(</span><span class="n">memPool</span><span class="p">);</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="virtual_memory.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Virtual memory management</p>
      </div>
    </a>
    <a class="right-next"
       href="../error_handling.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Error handling</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#using-soma">Using SOMA</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-pools">Memory pools</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#set-pools">Set pools</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#trim-pools">Trim pools</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#resource-usage-statistics">Resource usage statistics</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-reuse-policies">Memory reuse policies</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#device-accessibility-for-multi-gpu-support">Device accessibility for multi-GPU support</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#interprocess-memory-handling">Interprocess memory handling</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#device-pointer">Device pointer</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#shareable-handle">Shareable handle</a></li>
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
