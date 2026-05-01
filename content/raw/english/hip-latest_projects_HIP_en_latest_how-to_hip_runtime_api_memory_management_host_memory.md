---
title: "Host memory &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/memory_management/host_memory.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:07:33.126283+00:00
content_hash: "79c4ac911156faf7"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="Host memory of the HIP ecosystem" name="description" />
<meta content="AMD, ROCm, HIP, host memory" name="keywords" />

    <title>Host memory &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/hip_runtime_api/memory_management/host_memory';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Device memory" href="device_memory.html" />
    <link rel="prev" title="Memory management" href="../memory_management.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/hip_runtime_api/memory_management/host_memory.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Host memory</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="device_memory.html">Device memory</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
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
    
    <li class="breadcrumb-item active" aria-current="page">Host memory</li>
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
    <h1>Host memory</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#pageable-memory">Pageable memory</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#pinned-memory">Pinned memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-allocation-flags-for-pinned-memory">Memory allocation flags for pinned memory</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="host-memory">
<span id="id1"></span><h1>Host memory<a class="headerlink" href="#host-memory" title="Link to this heading">#</a></h1>
<p>Host memory is the “normal” memory residing in the host RAM and allocated by C
or C++. Host memory can be allocated in two different ways:</p>
<ul class="simple">
<li><p>Pageable memory</p></li>
<li><p>Pinned memory</p></li>
</ul>
<p>The following figure explains how data is transferred in pageable and pinned
memory.</p>
<figure class="align-default">
<img alt="../../../_images/pageable_pinned.svg" src="../../../_images/pageable_pinned.svg" />
</figure>
<p>The pageable and pinned memory allow you to exercise direct control over
memory operations, which is known as explicit memory management. When using the
unified memory, you get a simplified memory model with less control over
low level memory operations.</p>
<p>The difference in memory transfers between explicit and unified memory
management is highlighted in the following figure:</p>
<figure class="align-default">
<img alt="../../../_images/um.svg" src="../../../_images/um.svg" />
</figure>
<p>For more details on unified memory management, see <a class="reference internal" href="unified_memory.html"><span class="doc">Unified memory management</span></a>.</p>
<section id="pageable-memory">
<span id="pageable-host-memory"></span><h2>Pageable memory<a class="headerlink" href="#pageable-memory" title="Link to this heading">#</a></h2>
<p>Pageable memory exists on memory blocks known as “pages” that can be migrated to
other memory storage. For example, migrating memory between CPU sockets on a
motherboard or in a system whose RAM runs out of space and starts dumping pages
into the swap partition of the hard drive.</p>
<p>Pageable memory is usually allocated with a call to <code class="docutils literal notranslate"><span class="pre">malloc</span></code> or <code class="docutils literal notranslate"><span class="pre">new</span></code> in a
C++ application.</p>
<p><strong>Example:</strong> Using pageable host memory in HIP</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstring&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)                  \</span>
<span class="cp">{                                              \</span>
<span class="cp">    const hipError_t status = expression;      \</span>
<span class="cp">    if(status != hipSuccess)                   \</span>
<span class="cp">    {                                          \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error &quot;              \</span>
<span class="cp">                  &lt;&lt; status &lt;&lt; &quot;: &quot;            \</span>
<span class="cp">                  &lt;&lt; hipGetErrorString(status) \</span>
<span class="cp">                  &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot; \</span>
<span class="cp">                  &lt;&lt; __LINE__ &lt;&lt; std::endl;    \</span>
<span class="cp">    }                                          \</span>
<span class="cp">}</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">100</span><span class="p">;</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">host_input</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">host_output</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// Host allocation</span>
<span class="w">    </span><span class="n">host_input</span><span class="w">  </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="p">[</span><span class="n">element_number</span><span class="p">];</span>
<span class="w">    </span><span class="n">host_output</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="p">[</span><span class="n">element_number</span><span class="p">];</span>

<span class="w">    </span><span class="c1">// Host data preparation</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">element_number</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">host_input</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">i</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">memset</span><span class="p">(</span><span class="n">host_output</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">));</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">device_input</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">device_output</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Device allocation</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">((</span><span class="kt">int</span><span class="w"> </span><span class="o">**</span><span class="p">)</span><span class="o">&amp;</span><span class="n">device_input</span><span class="p">,</span><span class="w">  </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">)));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">((</span><span class="kt">int</span><span class="w"> </span><span class="o">**</span><span class="p">)</span><span class="o">&amp;</span><span class="n">device_output</span><span class="p">,</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">)));</span>

<span class="w">    </span><span class="c1">// Device data preparation</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">device_input</span><span class="p">,</span><span class="w"> </span><span class="n">host_input</span><span class="p">,</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemset</span><span class="p">(</span><span class="n">device_output</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">)));</span>

<span class="w">    </span><span class="c1">// Run the kernel</span>
<span class="w">    </span><span class="c1">// ...</span>

<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">device_input</span><span class="p">,</span><span class="w"> </span><span class="n">host_input</span><span class="p">,</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Free host memory</span>
<span class="w">    </span><span class="k">delete</span><span class="p">[]</span><span class="w"> </span><span class="n">host_input</span><span class="p">;</span>
<span class="w">    </span><span class="k">delete</span><span class="p">[]</span><span class="w"> </span><span class="n">host_output</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Free device memory</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">device_input</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">device_output</span><span class="p">));</span>
<span class="p">}</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a> and <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv47hipFreePv" title="hipFree"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipFree()</span></code></a> are blocking calls. However, HIP
also provides non-blocking versions <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html#_CPPv414hipMallocAsyncPPv6size_t12hipMemPool_t11hipStream_t" title="hipMallocAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMallocAsync()</span></code></a> and
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/stream_ordered_memory_allocator.html#_CPPv412hipFreeAsyncPv11hipStream_t" title="hipFreeAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipFreeAsync()</span></code></a>, which require a stream as an additional argument.
For asynchronous memory allocations made with <code class="docutils literal notranslate"><span class="pre">hipMallocAsync</span></code> and <code class="docutils literal notranslate"><span class="pre">hipMallocFromPoolAsync</span></code>
<code class="docutils literal notranslate"><span class="pre">hipFree</span></code> does not implicitly wait for synchronization, to match the behavior of <code class="docutils literal notranslate"><span class="pre">cudaFree</span></code>.</p>
</div>
</section>
<section id="pinned-memory">
<span id="pinned-host-memory"></span><h2>Pinned memory<a class="headerlink" href="#pinned-memory" title="Link to this heading">#</a></h2>
<p>Pinned memory or page-locked memory is stored in pages that are locked in
specific sectors in RAM and can’t be migrated. The pointer can be used on both
host and device. Accessing host-resident pinned memory in device kernels is
generally not recommended for performance, as it can force the data to traverse
the host-device interconnect such as PCIe, which is much slower than the
on-device bandwidth.</p>
<p>The advantage of pinned memory is the improved transfer time between host and
device. For transfer operations, such as <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind" title="hipMemcpy"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpy()</span></code></a> or <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv414hipMemcpyAsyncPvPKv6size_t13hipMemcpyKind11hipStream_t" title="hipMemcpyAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpyAsync()</span></code></a>,
using pinned memory instead of pageable memory on the host can lead to a three times
improvement in bandwidth.</p>
<p>The disadvantage of pinned memory is the reduced availability of RAM for other
processes, which can negatively impact the overall performance of the host.</p>
<p><strong>Example:</strong> Using pinned memory in HIP</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstring&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)                  \</span>
<span class="cp">{                                              \</span>
<span class="cp">    const hipError_t status = expression;      \</span>
<span class="cp">    if(status != hipSuccess)                   \</span>
<span class="cp">    {                                          \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error &quot;              \</span>
<span class="cp">                  &lt;&lt; status &lt;&lt; &quot;: &quot;            \</span>
<span class="cp">                  &lt;&lt; hipGetErrorString(status) \</span>
<span class="cp">                  &lt;&lt; &quot; at &quot; &lt;&lt; __FILE__ &lt;&lt; &quot;:&quot; \</span>
<span class="cp">                  &lt;&lt; __LINE__ &lt;&lt; std::endl;    \</span>
<span class="cp">    }                                          \</span>
<span class="cp">}</span>

<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="k">const</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">100</span><span class="p">;</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">host_input</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">host_output</span><span class="p">;</span>
<span class="w">    </span><span class="c1">// Host allocation</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipHostMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">host_input</span><span class="p">,</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">)));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipHostMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">host_output</span><span class="p">,</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">)));</span>

<span class="w">    </span><span class="c1">// Host data preparation</span>
<span class="w">    </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">element_number</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="n">host_input</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">i</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">memset</span><span class="p">(</span><span class="n">host_output</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">));</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">device_input</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">device_output</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Device allocation</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">device_input</span><span class="p">,</span><span class="w">  </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">)));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">device_output</span><span class="p">,</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">)));</span>

<span class="w">    </span><span class="c1">// Device data preparation</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">device_input</span><span class="p">,</span><span class="w"> </span><span class="n">host_input</span><span class="p">,</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemset</span><span class="p">(</span><span class="n">device_output</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">)));</span>

<span class="w">    </span><span class="c1">// Run the kernel</span>
<span class="w">    </span><span class="c1">// ...</span>

<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">device_input</span><span class="p">,</span><span class="w"> </span><span class="n">host_input</span><span class="p">,</span><span class="w"> </span><span class="n">element_number</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="kt">int</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Free host memory</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFreeHost</span><span class="p">(</span><span class="n">host_input</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFreeHost</span><span class="p">(</span><span class="n">host_output</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Free device memory</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">device_input</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">device_output</span><span class="p">));</span>
<span class="p">}</span>
</pre></div>
</div>
<section id="memory-allocation-flags-for-pinned-memory">
<span id="memory-allocation-flags"></span><h3>Memory allocation flags for pinned memory<a class="headerlink" href="#memory-allocation-flags-for-pinned-memory" title="Link to this heading">#</a></h3>
<p>The memory allocation for pinned memory can be controlled using <code class="docutils literal notranslate"><span class="pre">hipHostMalloc</span></code> flags:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipHostMallocPortable</span></code>: The memory allocation is not restricted to the
context making the allocation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipHostMallocMapped</span></code>: The memory is allocated into the address space for
the current device and the device pointer can be obtained with
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv423hipHostGetDevicePointerPPvPvj" title="hipHostGetDevicePointer"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipHostGetDevicePointer()</span></code></a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipHostMallocNumaUser</span></code>: The host memory allocation follows Numa policy
specified by the user. Target of Numa policy is to select a CPU that is
closest to each GPU. Numa distance is the distance between GPU and CPU
devices.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipHostMallocWriteCombined</span></code>: The memory is allocated as write-combined.
Although lacking read efficiency by most CPUs, write-combined allocation might
be transferred faster across the PCIe bus on some system configurations. It’s
a good option for data transfer from host to device via mapped pinned memory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipHostMallocCoherent</span></code>: Fine-grained memory is allocated. Overrides
<code class="docutils literal notranslate"><span class="pre">HIP_HOST_COHERENT</span></code> environment variable for specific allocation. For
details, see <a class="reference internal" href="coherence_control.html#coherence-control"><span class="std std-ref">Coherence control</span></a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipHostMallocNonCoherent</span></code>: Coarse-grained memory is allocated. Overrides
<code class="docutils literal notranslate"><span class="pre">HIP_HOST_COHERENT</span></code> environment variable for specific allocation. For
details, see <a class="reference internal" href="coherence_control.html#coherence-control"><span class="std std-ref">Coherence control</span></a>.</p></li>
</ul>
<p>All allocation flags are independent and can be set in any combination. The only
exception is setting <code class="docutils literal notranslate"><span class="pre">hipHostMallocCoherent</span></code> and <code class="docutils literal notranslate"><span class="pre">hipHostMallocNonCoherent</span></code>
together, which leads to an illegal state. An example of a valid flag
combination is calling <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv413hipHostMallocPPv6size_tj" title="hipHostMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipHostMalloc()</span></code></a> with both
<code class="docutils literal notranslate"><span class="pre">hipHostMallocPortable</span></code> and <code class="docutils literal notranslate"><span class="pre">hipHostMallocMapped</span></code> flags set. Both the flags
use the same model and differentiate only between how the surrounding code uses
the host memory.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>By default, each GPU selects a Numa CPU node with the least Numa distance
between them. This implies that the host memory is automatically allocated on
the closest memory pool of the current GPU device’s Numa node. Using
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/device_management.html#_CPPv412hipSetDevicei" title="hipSetDevice"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipSetDevice()</span></code></a> API to set a different GPU increases the Numa
distance but still allows you to access the host allocation.</p>
<p>Numa policy is implemented on Linux and is under development on Microsoft
Windows.</p>
</div>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="../memory_management.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Memory management</p>
      </div>
    </a>
    <a class="right-next"
       href="device_memory.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Device memory</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#pageable-memory">Pageable memory</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#pinned-memory">Pinned memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-allocation-flags-for-pinned-memory">Memory allocation flags for pinned memory</a></li>
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
