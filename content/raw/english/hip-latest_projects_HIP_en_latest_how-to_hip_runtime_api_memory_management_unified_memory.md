---
title: "Unified memory management &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/memory_management/unified_memory.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:06:18.070583+00:00
content_hash: "056bf669c9b10fca"
---


<!DOCTYPE html>


<html lang="en" data-content_root="../../../" >

  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<meta content="This chapter describes Unified Memory and shows how to use it in AMD HIP." name="description" />
<meta content="AMD, ROCm, HIP, CUDA, unified memory, unified, memory" name="keywords" />

    <title>Unified memory management &#8212; HIP 7.2.53211 Documentation</title>
  
  
  
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
    <script>DOCUMENTATION_OPTIONS.pagename = 'how-to/hip_runtime_api/memory_management/unified_memory';</script>
    <script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
    <link rel="icon" href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico"/>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Virtual memory management" href="virtual_memory.html" />
    <link rel="prev" title="Coherence control" href="coherence_control.html" />
    <meta name="google-site-verification" content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" />

  <script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-hip" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/how-to/hip_runtime_api/memory_management/unified_memory.html" /><meta name="readthedocs-http-status" content="200" /></head>
  
  
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
<li class="toctree-l3 current active"><a class="current reference internal" href="#">Unified memory management</a></li>
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
    
    <li class="breadcrumb-item active" aria-current="page">Unified...</li>
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
    <h1>Unified memory management</h1>
    <!-- Table of contents -->
    <div id="print-main-content">
        <div id="jb-print-toc">
            
            <div>
                <h2> Contents </h2>
            </div>
            <nav aria-label="Page">
                <ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">Unified memory</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#managed-memory">Managed memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#system-requirements-for-managed-memory">System requirements for managed memory</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-allocation-approaches-in-unified-memory">Memory allocation approaches in unified memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#checking-unified-memory-support">Checking unified memory support</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#example-for-unified-memory-management">Example for unified memory management</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#choosing-the-right-memory-allocator">Choosing the right memory allocator</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#using-unified-memory">Using unified memory</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#performance-optimizations-for-unified-memory">Performance optimizations for unified memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#data-prefetching">Data prefetching</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-advice">Memory advice</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#best-practices-for-memory-advice">Best practices for memory advice</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-range-attributes">Memory range attributes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#asynchronously-attach-memory-to-a-stream">Asynchronously attach memory to a stream</a></li>
</ul>
</li>
</ul>
            </nav>
        </div>
    </div>
</div>

              
                
<div id="searchbox"></div>
                <article class="bd-article">
                  
  <section id="unified-memory-management">
<span id="unified-memory"></span><h1>Unified memory management<a class="headerlink" href="#unified-memory-management" title="Link to this heading">#</a></h1>
<p>This document covers unified memory management in HIP, which encompasses several
approaches that provide a single address space accessible from both CPU and GPU.
<strong>Unified memory</strong> refers to the overall architectural concept of this shared
address space, while <strong>managed memory</strong> is one specific implementation that
provides automatic page migration between devices. Other unified memory allocators
like <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a> and <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv413hipHostMallocPPv6size_tj" title="hipHostMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipHostMalloc()</span></code></a> provide different
access patterns within the same unified address space concept.</p>
<p>In conventional architectures CPUs and attached devices have their own memory
space and dedicated physical memory backing it up, e.g. normal RAM for CPUs and
VRAM on GPUs. This way each device can have physical memory optimized for its
use case. GPUs usually have specialized memory whose bandwidth is a
magnitude higher than the RAM attached to CPUs.</p>
<p>While providing exceptional performance, this setup typically requires explicit
memory management, as memory needs to be allocated, copied and freed on the used
devices and on the host. Additionally, this makes using more than the physically
available memory on the devices complicated.</p>
<p>Modern GPUs circumvent the problem of having to explicitly manage the memory,
while still keeping the benefits of the dedicated physical memories, by
supporting the concept of unified memory. This enables the CPU and the GPUs in
the system to access host and other GPUs’ memory without explicit memory
management.</p>
<section id="id1">
<h2>Unified memory<a class="headerlink" href="#id1" title="Link to this heading">#</a></h2>
<p>Unified Memory is a single memory address space accessible from any processor
within a system. This setup simplifies memory management and enables
applications to allocate data that can be read or written on both CPUs and GPUs
without explicitly copying it to the specific CPU or GPU. The Unified memory
model is shown in the following figure.</p>
<figure class="align-default">
<img alt="../../../_images/um.svg" src="../../../_images/um.svg" />
</figure>
<p>Unified memory enables the access to memory located on other devices via
several methods, depending on whether hardware support is available or has to be
managed by the driver. CPUs can access memory allocated via <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a>,
providing bidirectional memory accessibility within the unified address space.</p>
</section>
<section id="managed-memory">
<h2>Managed memory<a class="headerlink" href="#managed-memory" title="Link to this heading">#</a></h2>
<p>Managed Memory is an extension of the unified memory architecture in which HIP
monitors memory access and intelligently migrates data between device and
system memories, thereby improving performance and resource efficiency.</p>
<p>When a kernel on the device tries to access a managed memory address that is
not in its local device memory, a page-fault is triggered.  The GPU then in
turn requests the page from the host or other device on which the memory is
located. The page is unmapped from the source, sent to the device and
mapped to the device’s memory.  The requested memory is then available locally
to the processes running on the device, which improves performance as local
memory access outperforms remote memory access.</p>
<p>Managed memory also expands the memory capacity available to a GPU kernel. When
migrating memory into the device on page-fault, if the device’s memory is
already at capacity, a page is unmapped from the device’s memory first and sent
and mapped to host memory.  This enables more memory to be allocated and used
for a GPU than the GPU itself has physically available. This level of support
can be very beneficial, for example, for sparse accesses to an array that is
not often used on the device.</p>
<section id="system-requirements-for-managed-memory">
<span id="unified-memory-system-requirements"></span><h3>System requirements for managed memory<a class="headerlink" href="#system-requirements-for-managed-memory" title="Link to this heading">#</a></h3>
<p>Some AMD GPUs do not support page-faults, and thus do not support on-demand
page-fault driven migration. On these architectures, if the programmer prefers
all GPU memory accesses to be local, all pages have to migrated before the
kernel is dispatched, as the driver cannot know beforehand which parts of a
dataset are going to be accessed. This can lead to significant delays on the
first run of a kernel, and, in the example of a sparsely accessed array, can
also lead to copying more memory than is actually accessed by the kernel.</p>
<p>Note that on systems which do not support page-faults, managed memory APIs are
still accessible to the programmer, but managed memory operates in a degraded
fashion due to the lack of demand-driven migration. Furthermore, on these
systems it is still possible to use unified memory allocators that do not
provide managed memory features; see
<a class="reference internal" href="#memory-allocation-approaches-in-unified-memory"><span class="std std-ref">Memory allocation approaches in unified memory</span></a> for more details.</p>
<p>Managed memory is supported on Linux by all modern AMD GPUs from the Vega
series onward, as shown in the following table. Managed memory can be
explicitly allocated using <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#_CPPv416hipMallocManagedPPv6size_tj" title="hipMallocManaged"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMallocManaged()</span></code></a> or marking variables
with the <code class="docutils literal notranslate"><span class="pre">__managed__</span></code> attribute. For the latest GPUs, with a Linux kernel
that supports <a class="reference external" href="https://www.kernel.org/doc/html/latest/mm/hmm.html">Heterogeneous Memory Management (HMM)</a>, the normal system
allocators (e.g., <code class="docutils literal notranslate"><span class="pre">new</span></code>, <code class="docutils literal notranslate"><span class="pre">malloc()</span></code>) can be used.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>To ensure the proper functioning of managed memory on supported GPUs, it
is <strong>essential</strong> to set the environment variable <code class="docutils literal notranslate"><span class="pre">HSA_XNACK=1</span></code> and use a
GPU kernel mode driver that supports <a class="reference external" href="https://www.kernel.org/doc/html/latest/mm/hmm.html">HMM</a>. Without this
configuration, access-driven memory migration will be disabled, and the
behavior will be similar to that of systems without HMM support.</p>
</div>
<div class="pst-scrollable-table-container"><table class="table table-center" id="id14">
<caption><span class="caption-text">Managed Memory Support by GPU Architecture</span><a class="headerlink" href="#id14" title="Link to this table">#</a></caption>
<colgroup>
<col style="width: 44.4%" />
<col style="width: 27.8%" />
<col style="width: 27.8%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Architecture</p></th>
<th class="head"><p><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#_CPPv416hipMallocManagedPPv6size_tj" title="hipMallocManaged"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMallocManaged()</span></code></a>, <code class="docutils literal notranslate"><span class="pre">__managed__</span></code></p></th>
<th class="head"><p><code class="docutils literal notranslate"><span class="pre">new</span></code>, <code class="docutils literal notranslate"><span class="pre">malloc()</span></code>, <code class="docutils literal notranslate"><span class="pre">allocate()</span></code></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>CDNA4</p></td>
<td><p>✅</p></td>
<td><p>✅ <sup>1</sup></p></td>
</tr>
<tr class="row-odd"><td><p>CDNA3</p></td>
<td><p>✅</p></td>
<td><p>✅ <sup>1</sup></p></td>
</tr>
<tr class="row-even"><td><p>CDNA2</p></td>
<td><p>✅</p></td>
<td><p>✅ <sup>1</sup></p></td>
</tr>
<tr class="row-odd"><td><p>CDNA1</p></td>
<td><p>✅</p></td>
<td><p>❌</p></td>
</tr>
<tr class="row-even"><td><p>RDNA1</p></td>
<td><p>✅</p></td>
<td><p>❌</p></td>
</tr>
<tr class="row-odd"><td><p>GCN5</p></td>
<td><p>✅</p></td>
<td><p>❌</p></td>
</tr>
</tbody>
</table>
</div>
<p>✅: <strong>Supported</strong></p>
<p>❌: <strong>Unsupported</strong></p>
<p><sup>1</sup> Works only with <code class="docutils literal notranslate"><span class="pre">HSA_XNACK=1</span></code> and kernels with HMM support. First GPU
access causes recoverable page-fault.</p>
</section>
</section>
<section id="memory-allocation-approaches-in-unified-memory">
<span id="id2"></span><h2>Memory allocation approaches in unified memory<a class="headerlink" href="#memory-allocation-approaches-in-unified-memory" title="Link to this heading">#</a></h2>
<p>While managed memory provides automatic migration, unified memory encompasses
several allocation methods, each with different access patterns and migration
behaviors. The following section covers all available unified memory allocation
approaches, including but not limited to managed memory APIs.</p>
<p>Support for the different unified memory allocators depends on the GPU
architecture and on the system. For more information, see <a class="reference internal" href="#unified-memory-system-requirements"><span class="std std-ref">System requirements for managed memory</span></a> and <a class="reference internal" href="#checking-unified-memory-support"><span class="std std-ref">Checking unified memory support</span></a>.</p>
<ul>
<li><p><strong>HIP allocated managed memory and variables</strong></p>
<p><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#_CPPv416hipMallocManagedPPv6size_tj" title="hipMallocManaged"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMallocManaged()</span></code></a> is a dynamic memory allocator available on
all GPUs with unified memory support. For more details, visit
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#unified-memory-reference"><span class="std std-ref">Managed memory</span></a>.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">__managed__</span></code> declaration specifier, which serves as its counterpart,
can be utilized for static allocation.</p>
</li>
<li><p><strong>System allocated unified memory</strong></p>
<p>Starting with CDNA2, the <code class="docutils literal notranslate"><span class="pre">new</span></code>, <code class="docutils literal notranslate"><span class="pre">malloc()</span></code>, and <code class="docutils literal notranslate"><span class="pre">allocate()</span></code> (Fortran) system allocators allow
you to reserve unified memory. The system allocator is more versatile and
offers an easy transition for code written for CPUs to HIP code as the
same system allocation API is used. Memory allocated by these allocators can
be registered to be accessible on device using <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv415hipHostRegisterPv6size_tj" title="hipHostRegister"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipHostRegister()</span></code></a>.</p>
</li>
<li><p><strong>HIP allocated non-managed memory</strong></p>
<p><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a> and <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv413hipHostMallocPPv6size_tj" title="hipHostMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipHostMalloc()</span></code></a> are dynamic memory
allocators available on all GPUs with unified memory support. Memory
allocated by these allocators is not migrated between device and host memory.</p>
</li>
</ul>
<p>The table below illustrates the expected behavior of managed and unified memory
functions on ROCm and CUDA, both with and without HMM support.</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-group="tab" data-sync-id="original-block" for="sd-tab-item-0">
ROCm allocation behaviour</label><div class="sd-tab-content docutils">
<div class="pst-scrollable-table-container"><table class="table" id="id15">
<caption><span class="caption-text">Comparison of expected behavior of managed and unified memory functions in ROCm</span><a class="headerlink" href="#id15" title="Link to this table">#</a></caption>
<colgroup>
<col style="width: 26.0%" />
<col style="width: 17.0%" />
<col style="width: 20.0%" />
<col style="width: 17.0%" />
<col style="width: 20.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>call</p></th>
<th class="head"><p>Allocation origin without HMM or <code class="docutils literal notranslate"><span class="pre">HSA_XNACK=0</span></code></p></th>
<th class="head"><p>Access outside the origin without HMM or <code class="docutils literal notranslate"><span class="pre">HSA_XNACK=0</span></code></p></th>
<th class="head"><p>Allocation origin with HMM and <code class="docutils literal notranslate"><span class="pre">HSA_XNACK=1</span></code></p></th>
<th class="head"><p>Access outside the origin with HMM and <code class="docutils literal notranslate"><span class="pre">HSA_XNACK=1</span></code></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">new</span></code>, <code class="docutils literal notranslate"><span class="pre">malloc()</span></code>, <code class="docutils literal notranslate"><span class="pre">allocate()</span></code></p></td>
<td><p>host</p></td>
<td><p>not accessible on device</p></td>
<td><p>first touch</p></td>
<td><p>page-fault migration</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a></p></td>
<td><p>device</p></td>
<td><p>zero copy <a class="reference internal" href="#zc" id="id3"><span>[zc]</span></a></p></td>
<td><p>device</p></td>
<td><p>zero copy <a class="reference internal" href="#zc" id="id4"><span>[zc]</span></a></p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#_CPPv416hipMallocManagedPPv6size_tj" title="hipMallocManaged"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMallocManaged()</span></code></a>, <code class="docutils literal notranslate"><span class="pre">__managed__</span></code></p></td>
<td><p>pinned host</p></td>
<td><p>zero copy <a class="reference internal" href="#zc" id="id5"><span>[zc]</span></a></p></td>
<td><p>first touch</p></td>
<td><p>page-fault migration</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv415hipHostRegisterPv6size_tj" title="hipHostRegister"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipHostRegister()</span></code></a></p></td>
<td><p>pinned host</p></td>
<td><p>zero copy <a class="reference internal" href="#zc" id="id6"><span>[zc]</span></a></p></td>
<td><p>pinned host</p></td>
<td><p>zero copy <a class="reference internal" href="#zc" id="id7"><span>[zc]</span></a></p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv413hipHostMallocPPv6size_tj" title="hipHostMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipHostMalloc()</span></code></a></p></td>
<td><p>pinned host</p></td>
<td><p>zero copy <a class="reference internal" href="#zc" id="id8"><span>[zc]</span></a></p></td>
<td><p>pinned host</p></td>
<td><p>zero copy <a class="reference internal" href="#zc" id="id9"><span>[zc]</span></a></p></td>
</tr>
</tbody>
</table>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" data-sync-group="tab" data-sync-id="cooperative-groups" for="sd-tab-item-1">
CUDA allocation behaviour</label><div class="sd-tab-content docutils">
<div class="pst-scrollable-table-container"><table class="table" id="id16">
<caption><span class="caption-text">Comparison of expected behavior of managed and unified memory functions in CUDA</span><a class="headerlink" href="#id16" title="Link to this table">#</a></caption>
<colgroup>
<col style="width: 26.0%" />
<col style="width: 17.0%" />
<col style="width: 20.0%" />
<col style="width: 17.0%" />
<col style="width: 20.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>call</p></th>
<th class="head"><p>Allocation origin without HMM</p></th>
<th class="head"><p>Access outside the origin without HMM</p></th>
<th class="head"><p>Allocation origin with HMM</p></th>
<th class="head"><p>Access outside the origin with HMM</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">new</span></code>, <code class="docutils literal notranslate"><span class="pre">malloc()</span></code></p></td>
<td><p>host</p></td>
<td><p>not accessible on device</p></td>
<td><p>first touch</p></td>
<td><p>page-fault migration</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">cudaMalloc()</span></code></p></td>
<td><p>device</p></td>
<td><p>not accessible on host</p></td>
<td><p>device</p></td>
<td><p>page-fault migration</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">cudaMallocManaged()</span></code>, <code class="docutils literal notranslate"><span class="pre">__managed__</span></code></p></td>
<td><p>host</p></td>
<td><p>page-fault migration</p></td>
<td><p>first touch</p></td>
<td><p>page-fault migration</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">cudaHostRegister()</span></code></p></td>
<td><p>host</p></td>
<td><p>page-fault migration</p></td>
<td><p>host</p></td>
<td><p>page-fault migration</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">cudaMallocHost()</span></code></p></td>
<td><p>pinned host</p></td>
<td><p>zero copy <a class="reference internal" href="#zc" id="id10"><span>[zc]</span></a></p></td>
<td><p>pinned host</p></td>
<td><p>zero copy <a class="reference internal" href="#zc" id="id11"><span>[zc]</span></a></p></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
<div role="list" class="citation-list">
<div class="citation" id="zc" role="doc-biblioentry">
<span class="label"><span class="fn-bracket">[</span>zc<span class="fn-bracket">]</span></span>
<span class="backrefs">(<a role="doc-backlink" href="#id3">1</a>,<a role="doc-backlink" href="#id4">2</a>,<a role="doc-backlink" href="#id5">3</a>,<a role="doc-backlink" href="#id6">4</a>,<a role="doc-backlink" href="#id7">5</a>,<a role="doc-backlink" href="#id8">6</a>,<a role="doc-backlink" href="#id9">7</a>,<a role="doc-backlink" href="#id10">8</a>,<a role="doc-backlink" href="#id11">9</a>)</span>
<p>Zero copy is a feature, where the memory is pinned to either the device
or the host, and won’t be transferred when accessed by another device or
the host. Instead only the requested memory is transferred, without
making an explicit copy, like a normal memory access, hence the term
“zero copy”.</p>
</div>
</div>
<section id="checking-unified-memory-support">
<span id="id12"></span><h3>Checking unified memory support<a class="headerlink" href="#checking-unified-memory-support" title="Link to this heading">#</a></h3>
<p>The following device attributes can offer information about which <a class="reference internal" href="#memory-allocation-approaches-in-unified-memory"><span class="std std-ref">Memory allocation approaches in unified memory</span></a> are supported. The attribute value is
1 if the functionality is supported, and 0 if it is not supported.</p>
<div class="pst-scrollable-table-container"><table class="table table-center" id="id17">
<caption><span class="caption-text">Device attributes for unified memory management</span><a class="headerlink" href="#id17" title="Link to this table">#</a></caption>
<colgroup>
<col style="width: 40.0%" />
<col style="width: 60.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Attribute</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">hipDeviceAttributeManagedMemory</span></code></p></td>
<td><p>Device supports allocating managed memory on this system</p></td>
</tr>
<tr class="row-odd"><td><p><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">hipDeviceAttributePageableMemoryAccess</span></code></p></td>
<td><p>Device supports coherently accessing pageable memory without calling <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv415hipHostRegisterPv6size_tj" title="hipHostRegister"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipHostRegister()</span></code></a> on it.</p></td>
</tr>
<tr class="row-even"><td><p><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">hipDeviceAttributeConcurrentManagedAccess</span></code></p></td>
<td><p>Full unified memory support. Device can coherently access managed memory concurrently with the CPU</p></td>
</tr>
</tbody>
</table>
</div>
<p>For details on how to get the attributes of a specific device see <a class="reference internal" href="../../../reference/hip_runtime_api/modules/device_management.html#_CPPv421hipDeviceGetAttributePi20hipDeviceAttribute_ti" title="hipDeviceGetAttribute"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipDeviceGetAttribute()</span></code></a>.</p>
</section>
<section id="example-for-unified-memory-management">
<h3>Example for unified memory management<a class="headerlink" href="#example-for-unified-memory-management" title="Link to this heading">#</a></h3>
<p>The following example shows how to use unified memory with
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#_CPPv416hipMallocManagedPPv6size_tj" title="hipMallocManaged"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMallocManaged()</span></code></a> for dynamic allocation, the <code class="docutils literal notranslate"><span class="pre">__managed__</span></code> attribute
for static allocation and the standard  <code class="docutils literal notranslate"><span class="pre">new</span></code> allocation. For comparison, the
explicit memory management example is presented in the last tab.</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-2" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
hipMallocManaged()</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)              \</span>
<span class="cp">{                                          \</span>
<span class="cp">    const hipError_t err = expression;     \</span>
<span class="cp">    if(err != hipSuccess)                  \</span>
<span class="cp">    {                                      \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error: &quot;         \</span>
<span class="cp">            &lt;&lt; hipGetErrorString(err)      \</span>
<span class="cp">            &lt;&lt; &quot; at &quot; &lt;&lt; __LINE__ &lt;&lt; &quot;\n&quot;; \</span>
<span class="cp">    }                                      \</span>
<span class="cp">}</span>

<span class="c1">// Addition of two values.</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">add</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">;</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">;</span>

<span class="hll"><span class="w">    </span><span class="c1">// Allocate memory for a, b and c that is accessible to both device and host codes.</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">a</span><span class="p">)));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">b</span><span class="p">)));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">c</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">c</span><span class="p">)));</span>
</span>
<span class="w">    </span><span class="c1">// Setup input values.</span>
<span class="w">    </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="o">*</span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Launch add() kernel on GPU.</span>
<span class="w">    </span><span class="n">add</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="n">c</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Wait for GPU to finish before accessing on host.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Print the result.</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; + &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Cleanup allocated memory.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">a</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">b</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">c</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
__managed__</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)              \</span>
<span class="cp">{                                          \</span>
<span class="cp">    const hipError_t err = expression;     \</span>
<span class="cp">    if(err != hipSuccess)                  \</span>
<span class="cp">    {                                      \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error: &quot;         \</span>
<span class="cp">            &lt;&lt; hipGetErrorString(err)      \</span>
<span class="cp">            &lt;&lt; &quot; at &quot; &lt;&lt; __LINE__ &lt;&lt; &quot;\n&quot;; \</span>
<span class="cp">    }                                      \</span>
<span class="cp">}</span>

<span class="c1">// Addition of two values.</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">add</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">;</span>
<span class="p">}</span>

<span class="hll"><span class="c1">// Declare a, b and c as static variables.</span>
</span><span class="hll"><span class="n">__managed__</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="n">c</span><span class="p">;</span>
</span>
<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="c1">// Setup input values.</span>
<span class="w">    </span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Launch add() kernel on GPU.</span>
<span class="w">    </span><span class="n">add</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="o">&amp;</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">c</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Wait for GPU to finish before accessing on host.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Print the result.</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; + &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">c</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
new</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)              \</span>
<span class="cp">{                                          \</span>
<span class="cp">    const hipError_t err = expression;     \</span>
<span class="cp">    if(err != hipSuccess)                  \</span>
<span class="cp">    {                                      \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error: &quot;         \</span>
<span class="cp">            &lt;&lt; hipGetErrorString(err)      \</span>
<span class="cp">            &lt;&lt; &quot; at &quot; &lt;&lt; __LINE__ &lt;&lt; &quot;\n&quot;; \</span>
<span class="cp">    }                                      \</span>
<span class="cp">}</span>

<span class="c1">// Addition of two values.</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">add</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">;</span>
<span class="p">}</span>

<span class="c1">// This example requires HMM support and the environment variable HSA_XNACK needs to be set to 1</span>
<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="hll"><span class="w">    </span><span class="c1">// Allocate memory for a, b, and c.</span>
</span><span class="hll"><span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="p">[</span><span class="mi">1</span><span class="p">];</span>
</span><span class="hll"><span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="p">[</span><span class="mi">1</span><span class="p">];</span>
</span><span class="hll"><span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="p">[</span><span class="mi">1</span><span class="p">];</span>
</span>
<span class="w">    </span><span class="c1">// Setup input values.</span>
<span class="w">    </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="o">*</span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Launch add() kernel on GPU.</span>
<span class="w">    </span><span class="n">add</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="n">c</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Wait for GPU to finish before accessing on host.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Print the result.</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; + &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Cleanup allocated memory.</span>
<span class="w">    </span><span class="k">delete</span><span class="p">[]</span><span class="w"> </span><span class="n">c</span><span class="p">;</span>
<span class="w">    </span><span class="k">delete</span><span class="p">[]</span><span class="w"> </span><span class="n">b</span><span class="p">;</span>
<span class="w">    </span><span class="k">delete</span><span class="p">[]</span><span class="w"> </span><span class="n">a</span><span class="p">;</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
Explicit Memory Management</label><div class="sd-tab-content docutils">
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)              \</span>
<span class="cp">{                                          \</span>
<span class="cp">    const hipError_t err = expression;     \</span>
<span class="cp">    if(err != hipSuccess)                  \</span>
<span class="cp">    {                                      \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error: &quot;         \</span>
<span class="cp">            &lt;&lt; hipGetErrorString(err)      \</span>
<span class="cp">            &lt;&lt; &quot; at &quot; &lt;&lt; __LINE__ &lt;&lt; &quot;\n&quot;; \</span>
<span class="cp">    }                                      \</span>
<span class="cp">}</span>

<span class="c1">// Addition of two values.</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">add</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">;</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="n">c</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">d_a</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">d_b</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">d_c</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Setup input values.</span>
<span class="w">    </span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>

<span class="hll"><span class="w">    </span><span class="c1">// Allocate device copies of a, b and c.</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_a</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_a</span><span class="p">)));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_b</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_b</span><span class="p">)));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMalloc</span><span class="p">(</span><span class="o">&amp;</span><span class="n">d_c</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_c</span><span class="p">)));</span>
</span><span class="hll">
</span><span class="hll"><span class="w">    </span><span class="c1">// Copy input values to device.</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_a</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_a</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="n">d_b</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_b</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyHostToDevice</span><span class="p">));</span>
</span>
<span class="w">    </span><span class="c1">// Launch add() kernel on GPU.</span>
<span class="w">    </span><span class="n">add</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">d_a</span><span class="p">,</span><span class="w"> </span><span class="n">d_b</span><span class="p">,</span><span class="w"> </span><span class="n">d_c</span><span class="p">);</span>

<span class="hll"><span class="w">    </span><span class="c1">// Copy the result back to the host.</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemcpy</span><span class="p">(</span><span class="o">&amp;</span><span class="n">c</span><span class="p">,</span><span class="w"> </span><span class="n">d_c</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">d_c</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemcpyDeviceToHost</span><span class="p">));</span>
</span>
<span class="w">    </span><span class="c1">// Cleanup allocated memory.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_a</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_b</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">d_c</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Prints the result.</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; + &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">c</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
</div>
</section>
<section id="choosing-the-right-memory-allocator">
<span id="unified-memory-allocator-comparison"></span><h3>Choosing the right memory allocator<a class="headerlink" href="#choosing-the-right-memory-allocator" title="Link to this heading">#</a></h3>
<p>Selecting the appropriate memory allocator depends on your specific use case,
performance requirements, and target hardware. The following table provides
guidance on when to use each unified memory allocator in HIP.</p>
<div class="pst-scrollable-table-container"><table class="table table-center" id="id18">
<caption><span class="caption-text">Memory allocator comparison</span><a class="headerlink" href="#id18" title="Link to this table">#</a></caption>
<colgroup>
<col style="width: 25.0%" />
<col style="width: 35.0%" />
<col style="width: 40.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Allocator</p></th>
<th class="head"><p>Best Use Case</p></th>
<th class="head"><p>Key Characteristics</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#_CPPv416hipMallocManagedPPv6size_tj" title="hipMallocManaged"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMallocManaged()</span></code></a> / <code class="docutils literal notranslate"><span class="pre">__managed__</span></code></p></td>
<td><p>Applications that need automatic data migration between host and
device, or require memory oversubscription</p></td>
<td><p>Automatic page-fault driven migration; accessible from both host
and device; may have performance overhead from on-demand migration</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">new</span></code>, <code class="docutils literal notranslate"><span class="pre">malloc()</span></code>, <code class="docutils literal notranslate"><span class="pre">allocate()</span></code> (CDNA2+ with HMM)</p></td>
<td><p>CPU-centric code being ported to HIP, or applications that want
system allocator simplicity with GPU accessibility</p></td>
<td><p>Uses standard system allocators; first-touch placement policy;
requires <code class="docutils literal notranslate"><span class="pre">HSA_XNACK=1</span></code> for GPU access; convenient for porting</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a></p></td>
<td><p>Device-local data that is primarily accessed by GPU kernels with
minimal host interaction</p></td>
<td><p>Device-local allocation; zero-copy access from host; no automatic
migration; best performance for GPU-intensive workloads</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv413hipHostMallocPPv6size_tj" title="hipHostMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipHostMalloc()</span></code></a></p></td>
<td><p>Data that is primarily accessed by the host but needs to be
accessible from the device</p></td>
<td><p>Pinned host memory; zero-copy access from device; no automatic
migration; can improve transfer bandwidth for host-device copies</p></td>
</tr>
</tbody>
</table>
</div>
<p>When choosing an allocator, consider the following factors:</p>
<ul class="simple">
<li><p><strong>Access pattern:</strong> If data is accessed frequently by both host and device,
managed memory or system allocators provide automatic migration. If data is
primarily used by one processor, <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a> or
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv413hipHostMallocPPv6size_tj" title="hipHostMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipHostMalloc()</span></code></a> may be more efficient.</p></li>
<li><p><strong>Performance requirements:</strong> For maximum performance with known access
patterns, explicit memory management with <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMallocPPv6size_t" title="hipMalloc"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMalloc()</span></code></a> and
<a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind" title="hipMemcpy"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemcpy()</span></code></a> typically provides the best performance. Managed
memory trades some performance for programming simplicity.</p></li>
<li><p><strong>Memory oversubscription:</strong> Only managed memory and system allocators (with
HMM support) allow allocating more memory than physically available on the
device.</p></li>
<li><p><strong>Portability:</strong> System allocators (<code class="docutils literal notranslate"><span class="pre">new</span></code>, <code class="docutils literal notranslate"><span class="pre">malloc()</span></code>) make porting CPU
code easier, but require CDNA2+ with <code class="docutils literal notranslate"><span class="pre">HSA_XNACK=1</span></code> for GPU access.</p></li>
</ul>
</section>
</section>
<section id="using-unified-memory">
<span id="id13"></span><h2>Using unified memory<a class="headerlink" href="#using-unified-memory" title="Link to this heading">#</a></h2>
<p>Unified memory can simplify the complexities of memory management in GPU
computing, by not requiring explicit copies between the host and the devices. It
can be particularly useful in use cases with sparse memory accesses from both
the CPU and the GPU, as only the parts of the memory region that are actually
accessed need to be transferred to the corresponding processor, not the whole
memory region. This reduces the amount of memory sent over the PCIe bus or other
interfaces.</p>
<p>In HIP, pinned memory allocations are coherent by default. Pinned memory is
host memory mapped into the address space of all GPUs, meaning that the pointer
can be used on both host and device. Additionally, using pinned memory instead of
pageable memory on the host can improve bandwidth for transfers between the host
and the GPUs.</p>
<p>While unified memory can provide numerous benefits, it’s important to be aware
of the potential performance overhead associated with unified memory. You must
thoroughly test and profile your code to ensure it’s the most suitable choice
for your use case.</p>
</section>
<section id="performance-optimizations-for-unified-memory">
<span id="unified-memory-runtime-hints"></span><h2>Performance optimizations for unified memory<a class="headerlink" href="#performance-optimizations-for-unified-memory" title="Link to this heading">#</a></h2>
<p>There are several ways, in which the developer can guide the runtime to reduce
copies between devices, in order to improve performance.</p>
<p>With <code class="docutils literal notranslate"><span class="pre">numactl</span> <span class="pre">--membind</span></code> bindings, developers can control where physical
allocation occurs by restricting memory allocation to specific NUMA nodes.
This approach can reduce or eliminate the need for explicit data prefetching
since memory is allocated in the desired location from the start.</p>
<section id="data-prefetching">
<h3>Data prefetching<a class="headerlink" href="#data-prefetching" title="Link to this heading">#</a></h3>
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>Data prefetching is not always an optimization and can slow down execution,
as the API takes time to execute. If the memory is already in the right
place, prefetching will waste time. Users should profile their code to
verify whether prefetching is beneficial for their specific use case.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><strong>Cold Start Latency:</strong> Implicit page faulting on first access can cause
significant latency spikes, especially in performance-critical code paths.
To avoid this, use <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#_CPPv419hipMemPrefetchAsyncPKv6size_ti11hipStream_t" title="hipMemPrefetchAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemPrefetchAsync()</span></code></a> during initialization
to ensure data is resident on the target device before critical kernels
execute. This proactive approach eliminates the “cold start” penalty
associated with on-demand page migration.</p>
</div>
<p>When prefetching is beneficial, developers can consider setting different default
locations for different devices and using prefetch between them, which can help
eliminate IPC communication overhead when memory moves between devices.</p>
<p>Data prefetching is a technique used to improve the performance of your
application by moving data to the desired device before it’s actually
needed. <code class="docutils literal notranslate"><span class="pre">hipCpuDeviceId</span></code> is a special constant to specify the CPU as target.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)              \</span>
<span class="cp">{                                          \</span>
<span class="cp">    const hipError_t err = expression;     \</span>
<span class="cp">    if(err != hipSuccess)                  \</span>
<span class="cp">    {                                      \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error: &quot;         \</span>
<span class="cp">            &lt;&lt; hipGetErrorString(err)      \</span>
<span class="cp">            &lt;&lt; &quot; at &quot; &lt;&lt; __LINE__ &lt;&lt; &quot;\n&quot;; \</span>
<span class="cp">    }                                      \</span>
<span class="cp">}</span>

<span class="c1">// Addition of two values.</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">add</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">;</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">;</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceId</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDevice</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceId</span><span class="p">));</span><span class="w"> </span><span class="c1">// Get the current device ID</span>

<span class="w">    </span><span class="c1">// Allocate memory for a, b and c that is accessible to both device and host codes.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">a</span><span class="p">)));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">b</span><span class="p">)));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">c</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">c</span><span class="p">)));</span>

<span class="w">    </span><span class="c1">// Setup input values.</span>
<span class="w">    </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="o">*</span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>

<span class="hll"><span class="w">    </span><span class="c1">// Prefetch the data to the GPU device.</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPrefetchAsync</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">a</span><span class="p">),</span><span class="w"> </span><span class="n">deviceId</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPrefetchAsync</span><span class="p">(</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">b</span><span class="p">),</span><span class="w"> </span><span class="n">deviceId</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPrefetchAsync</span><span class="p">(</span><span class="n">c</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">c</span><span class="p">),</span><span class="w"> </span><span class="n">deviceId</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
</span>
<span class="w">    </span><span class="c1">// Launch add() kernel on GPU.</span>
<span class="w">    </span><span class="n">add</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="n">c</span><span class="p">);</span>

<span class="hll"><span class="w">    </span><span class="c1">// Prefetch the result back to the CPU.</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemPrefetchAsync</span><span class="p">(</span><span class="n">c</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">c</span><span class="p">),</span><span class="w"> </span><span class="n">hipCpuDeviceId</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">));</span>
</span>
<span class="w">    </span><span class="c1">// Wait for the prefetch operations to complete.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Prints the result.</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; + &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Cleanup allocated memory.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">a</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">b</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">c</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="memory-advice">
<h3>Memory advice<a class="headerlink" href="#memory-advice" title="Link to this heading">#</a></h3>
<p>Unified memory runtime hints can be set with <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#_CPPv412hipMemAdvisePKv6size_t15hipMemoryAdvisei" title="hipMemAdvise"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemAdvise()</span></code></a> to help
improve the performance of your code if you know the memory usage pattern. There
are several different types of hints as specified in the enum
<code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">hipMemoryAdvise</span></code>, for example, whether a certain device mostly reads
the memory region, where it should ideally be located, and even whether that
specific memory region is accessed by a specific device.</p>
<p>For the best performance, profile your application to optimize the
utilization of HIP runtime hints.</p>
<p>The effectiveness of <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#_CPPv412hipMemAdvisePKv6size_t15hipMemoryAdvisei" title="hipMemAdvise"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemAdvise()</span></code></a> comes from its ability to inform
the runtime of the developer’s intentions regarding memory usage. When the
runtime has knowledge of the expected memory access patterns, it can make better
decisions about data placement, leading to less transfers via the interconnect
and thereby reduced latency and bandwidth requirements. However, the actual
impact on performance can vary based on the specific use case and the system.</p>
<p>The following is the updated version of the example above with memory advice
instead of prefetching.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)              \</span>
<span class="cp">{                                          \</span>
<span class="cp">    const hipError_t err = expression;     \</span>
<span class="cp">    if(err != hipSuccess)                  \</span>
<span class="cp">    {                                      \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error: &quot;         \</span>
<span class="cp">            &lt;&lt; hipGetErrorString(err)      \</span>
<span class="cp">            &lt;&lt; &quot; at &quot; &lt;&lt; __LINE__ &lt;&lt; &quot;\n&quot;; \</span>
<span class="cp">    }                                      \</span>
<span class="cp">}</span>

<span class="c1">// Addition of two values.</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">add</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">;</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceId</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDevice</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceId</span><span class="p">));</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Allocate memory for a, b, and c accessible to both device and host codes.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">a</span><span class="p">)));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">b</span><span class="p">)));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">c</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">c</span><span class="p">)));</span>

<span class="hll"><span class="w">    </span><span class="c1">// Set memory advice for a and b to be read, located on and accessed by the GPU.</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemAdvise</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">a</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemAdviseSetPreferredLocation</span><span class="p">,</span><span class="w"> </span><span class="n">deviceId</span><span class="p">));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemAdvise</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">a</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemAdviseSetAccessedBy</span><span class="p">,</span><span class="w"> </span><span class="n">deviceId</span><span class="p">));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemAdvise</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">a</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemAdviseSetReadMostly</span><span class="p">,</span><span class="w"> </span><span class="n">deviceId</span><span class="p">));</span>
</span><span class="hll">
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemAdvise</span><span class="p">(</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">b</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemAdviseSetPreferredLocation</span><span class="p">,</span><span class="w"> </span><span class="n">deviceId</span><span class="p">));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemAdvise</span><span class="p">(</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">b</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemAdviseSetAccessedBy</span><span class="p">,</span><span class="w"> </span><span class="n">deviceId</span><span class="p">));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemAdvise</span><span class="p">(</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">b</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemAdviseSetReadMostly</span><span class="p">,</span><span class="w"> </span><span class="n">deviceId</span><span class="p">));</span>
</span><span class="hll">
</span><span class="hll"><span class="w">    </span><span class="c1">// Set memory advice for c to be read, located on and accessed by the CPU.</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemAdvise</span><span class="p">(</span><span class="n">c</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">c</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemAdviseSetPreferredLocation</span><span class="p">,</span><span class="w"> </span><span class="n">hipCpuDeviceId</span><span class="p">));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemAdvise</span><span class="p">(</span><span class="n">c</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">c</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemAdviseSetAccessedBy</span><span class="p">,</span><span class="w"> </span><span class="n">hipCpuDeviceId</span><span class="p">));</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemAdvise</span><span class="p">(</span><span class="n">c</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">c</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemAdviseSetReadMostly</span><span class="p">,</span><span class="w"> </span><span class="n">hipCpuDeviceId</span><span class="p">));</span>
</span>
<span class="w">    </span><span class="c1">// Setup input values.</span>
<span class="w">    </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="o">*</span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Launch add() kernel on GPU.</span>
<span class="w">    </span><span class="n">add</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="n">c</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Wait for GPU to finish before accessing on host.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="w">    </span><span class="c1">// Prints the result.</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; + &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Cleanup allocated memory.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">a</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">b</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">c</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<section id="best-practices-for-memory-advice">
<span id="unified-memory-best-practices"></span><h4>Best practices for memory advice<a class="headerlink" href="#best-practices-for-memory-advice" title="Link to this heading">#</a></h4>
<p>Choosing the right memory advice hint can significantly improve performance by
reducing unnecessary data migrations. The following table provides guidance on
when to use specific hints:</p>
<div class="pst-scrollable-table-container"><table class="table table-center" id="id19">
<caption><span class="caption-text">Memory advice best practices</span><a class="headerlink" href="#id19" title="Link to this table">#</a></caption>
<colgroup>
<col style="width: 45.0%" />
<col style="width: 55.0%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Hint</p></th>
<th class="head"><p>Use Case</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">hipMemAdviseSetReadMostly</span></code></p></td>
<td><p>Data that is mostly read and only occasionally written to. This
prevents unnecessary data migration for read-heavy workloads.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">hipMemAdviseSetPreferredLocation</span></code></p></td>
<td><p>Set the preferred location for the data as a specific device. Use
this to keep data on a particular device (host or device) to reduce
migration overhead.</p></td>
</tr>
<tr class="row-even"><td><p><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">hipMemAdviseSetAccessedBy</span></code></p></td>
<td><p>Data that will be accessed by a specified device. This helps prevent
page faults by proactively migrating data to the accessing device.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="xref cpp cpp-enumerator docutils literal notranslate"><span class="pre">hipMemAdviseSetCoarseGrain</span></code></p></td>
<td><p>Data that only needs to be coherent at dispatch boundaries. The
default fine-grained model allows coherent operations during kernel
execution, while coarse-grained provides better performance for data
that does not require runtime coherence.</p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<section id="memory-range-attributes">
<h3>Memory range attributes<a class="headerlink" href="#memory-range-attributes" title="Link to this heading">#</a></h3>
<p><a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#_CPPv423hipMemRangeGetAttributePv6size_t20hipMemRangeAttributePKv6size_t" title="hipMemRangeGetAttribute"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipMemRangeGetAttribute()</span></code></a> allows you to query attributes of a given
memory range. The attributes are given in <code class="xref cpp cpp-enum docutils literal notranslate"><span class="pre">hipMemRangeAttribute</span></code>.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;hip/hip_runtime.h&gt;</span>

<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;cstddef&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>

<span class="cp">#define HIP_CHECK(expression)              \</span>
<span class="cp">{                                          \</span>
<span class="cp">    const hipError_t err = expression;     \</span>
<span class="cp">    if(err != hipSuccess)                  \</span>
<span class="cp">    {                                      \</span>
<span class="cp">        std::cerr &lt;&lt; &quot;HIP error: &quot;         \</span>
<span class="cp">            &lt;&lt; hipGetErrorString(err)      \</span>
<span class="cp">            &lt;&lt; &quot; at &quot; &lt;&lt; __LINE__ &lt;&lt; &quot;\n&quot;; \</span>
<span class="cp">    }                                      \</span>
<span class="cp">}</span>

<span class="c1">// Addition of two values.</span>
<span class="n">__global__</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="n">add</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">    </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">;</span>
<span class="p">}</span>

<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span>
<span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="p">;</span>
<span class="w">    </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">attributeValue</span><span class="p">;</span>
<span class="w">    </span><span class="k">constexpr</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="kt">size_t</span><span class="w"> </span><span class="n">attributeSize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">attributeValue</span><span class="p">);</span>

<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">deviceId</span><span class="p">;</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipGetDevice</span><span class="p">(</span><span class="o">&amp;</span><span class="n">deviceId</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Allocate memory for a, b and c that is accessible to both device and host codes.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">a</span><span class="p">)));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">b</span><span class="p">)));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">c</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">c</span><span class="p">)));</span>

<span class="w">    </span><span class="c1">// Setup input values.</span>
<span class="w">    </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="w">    </span><span class="o">*</span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">2</span><span class="p">;</span>

<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemAdvise</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">a</span><span class="p">),</span><span class="w"> </span><span class="n">hipMemAdviseSetReadMostly</span><span class="p">,</span><span class="w"> </span><span class="n">deviceId</span><span class="p">));</span>

<span class="w">    </span><span class="c1">// Launch add() kernel on GPU.</span>
<span class="w">    </span><span class="n">add</span><span class="o">&lt;&lt;&lt;</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="o">&gt;&gt;&gt;</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="w"> </span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="n">c</span><span class="p">);</span>

<span class="w">    </span><span class="c1">// Wait for GPU to finish before accessing on host.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipDeviceSynchronize</span><span class="p">());</span>

<span class="hll"><span class="w">    </span><span class="c1">// Query an attribute of the memory range.</span>
</span><span class="hll"><span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipMemRangeGetAttribute</span><span class="p">(</span><span class="o">&amp;</span><span class="n">attributeValue</span><span class="p">,</span>
</span><span class="hll"><span class="w">                            </span><span class="n">attributeSize</span><span class="p">,</span>
</span><span class="hll"><span class="w">                            </span><span class="n">hipMemRangeAttributeReadMostly</span><span class="p">,</span>
</span><span class="hll"><span class="w">                            </span><span class="n">a</span><span class="p">,</span>
</span><span class="hll"><span class="w">                            </span><span class="k">sizeof</span><span class="p">(</span><span class="o">*</span><span class="n">a</span><span class="p">)));</span>
</span>
<span class="w">    </span><span class="c1">// Prints the result.</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">a</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; + &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">b</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; = &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="o">*</span><span class="n">c</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;The array a is&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="p">(</span><span class="n">attributeValue</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">?</span><span class="w"> </span><span class="s">&quot;&quot;</span><span class="w"> </span><span class="o">:</span><span class="w"> </span><span class="s">&quot; NOT&quot;</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; set to hipMemRangeAttributeReadMostly&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>

<span class="w">    </span><span class="c1">// Cleanup allocated memory.</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">a</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">b</span><span class="p">));</span>
<span class="w">    </span><span class="n">HIP_CHECK</span><span class="p">(</span><span class="n">hipFree</span><span class="p">(</span><span class="n">c</span><span class="p">));</span>

<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
</section>
<section id="asynchronously-attach-memory-to-a-stream">
<h3>Asynchronously attach memory to a stream<a class="headerlink" href="#asynchronously-attach-memory-to-a-stream" title="Link to this heading">#</a></h3>
<p>The <a class="reference internal" href="../../../reference/hip_runtime_api/modules/memory_management/unified_memory_reference.html#_CPPv423hipStreamAttachMemAsync11hipStream_tPv6size_tj" title="hipStreamAttachMemAsync"><code class="xref cpp cpp-func docutils literal notranslate"><span class="pre">hipStreamAttachMemAsync()</span></code></a> function attaches memory to a stream,
which can reduce the amount of memory transferred, when managed memory is used.
When the memory is attached to a stream using this function, it only gets
transferred between devices, when a kernel that is launched on this stream needs
access to the memory.</p>
</section>
</section>
</section>


                </article>
              

              
              
              
              
                <footer class="prev-next-footer d-print-none">
                  
<div class="prev-next-area">
    <a class="left-prev"
       href="coherence_control.html"
       title="previous page">
      <i class="fa-solid fa-angle-left"></i>
      <div class="prev-next-info">
        <p class="prev-next-subtitle">previous</p>
        <p class="prev-next-title">Coherence control</p>
      </div>
    </a>
    <a class="right-next"
       href="virtual_memory.html"
       title="next page">
      <div class="prev-next-info">
        <p class="prev-next-subtitle">next</p>
        <p class="prev-next-title">Virtual memory management</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">Unified memory</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#managed-memory">Managed memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#system-requirements-for-managed-memory">System requirements for managed memory</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-allocation-approaches-in-unified-memory">Memory allocation approaches in unified memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#checking-unified-memory-support">Checking unified memory support</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#example-for-unified-memory-management">Example for unified memory management</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#choosing-the-right-memory-allocator">Choosing the right memory allocator</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#using-unified-memory">Using unified memory</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#performance-optimizations-for-unified-memory">Performance optimizations for unified memory</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#data-prefetching">Data prefetching</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-advice">Memory advice</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#best-practices-for-memory-advice">Best practices for memory advice</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-range-attributes">Memory range attributes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#asynchronously-attach-memory-to-a-stream">Asynchronously attach memory to a stream</a></li>
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
