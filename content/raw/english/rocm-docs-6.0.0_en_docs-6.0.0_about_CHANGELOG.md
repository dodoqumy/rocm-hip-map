---
title: "Changelog"
source_url: "https://rocm.docs.amd.com/en/docs-6.0.0/about/CHANGELOG.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:09:21.236503+00:00
content_hash: "e7522b3b48380cce"
---


<!DOCTYPE html>

<html data-content_root="../" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/><meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Changelog — ROCm Documentation</title>
<script data-cfasync="false">
    document.documentElement.dataset.mode = localStorage.getItem("mode") || "";
    document.documentElement.dataset.theme = localStorage.getItem("theme") || "";
  </script>
<!-- Loaded before other Sphinx assets -->
<link href="../_static/styles/theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet"/>
<link href="../_static/styles/bootstrap.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet"/>
<link href="../_static/styles/pydata-sphinx-theme.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet"/>
<link href="../_static/vendor/fontawesome/6.5.2/css/all.min.css?digest=dfe6caa3a7d634c4db9b" rel="stylesheet"/>
<link as="font" crossorigin="" href="../_static/vendor/fontawesome/6.5.2/webfonts/fa-solid-900.woff2" rel="preload" type="font/woff2"/>
<link as="font" crossorigin="" href="../_static/vendor/fontawesome/6.5.2/webfonts/fa-brands-400.woff2" rel="preload" type="font/woff2"/>
<link as="font" crossorigin="" href="../_static/vendor/fontawesome/6.5.2/webfonts/fa-regular-400.woff2" rel="preload" type="font/woff2"/>
<link href="../_static/pygments.css?v=a746c00c" rel="stylesheet" type="text/css"/>
<link href="../_static/styles/sphinx-book-theme.css?v=a3416100" rel="stylesheet" type="text/css"/>
<link href="../_static/copybutton.css?v=76b2166b" rel="stylesheet" type="text/css"/>
<link href="../_static/custom.css?v=da61d430" rel="stylesheet" type="text/css"/>
<link href="../_static/rocm_header.css?v=4044f309" rel="stylesheet" type="text/css"/>
<link href="../_static/rocm_footer.css?v=25204c5a" rel="stylesheet" type="text/css"/>
<link href="../_static/fonts.css?v=fcff5274" rel="stylesheet" type="text/css"/>
<link href="../_static/sphinx-design.min.css?v=95c83b7e" rel="stylesheet" type="text/css"/>

<!-- Pre-loaded scripts that we'll load fully later -->
<link as="script" href="../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b" rel="preload"/>
<link as="script" href="../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b" rel="preload"/>
<script src="../_static/vendor/fontawesome/6.5.2/js/all.min.js?digest=dfe6caa3a7d634c4db9b"></script>
<script src="../_static/documentation_options.js?v=32485e33"></script>
<script src="../_static/doctools.js?v=9a2dae69"></script>
<script src="../_static/sphinx_highlight.js?v=dc90522c"></script>
<script src="../_static/clipboard.min.js?v=a7894cd8"></script>
<script src="../_static/copybutton.js?v=f281be69"></script>
<script async="async" src="../_static/code_word_breaks.js?v=327952c4"></script>
<script async="async" src="../_static/renameVersionLinks.js?v=929fe5e4"></script>
<script async="async" src="../_static/rdcMisc.js?v=01f88d96"></script>
<script async="async" src="../_static/theme_mode_captions.js?v=15f4ec5d"></script>
<script src="../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
<script src="../_static/design-tabs.js?v=f930bc37"></script>
<script>window.MathJax = {"options": {"processHtmlClass": "tex2jax_process|mathjax_process|math|output_area"}}</script>
<script defer="defer" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<script>DOCUMENTATION_OPTIONS.pagename = 'about/CHANGELOG';</script>
<script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
<link href="https://www.amd.com/themes/custom/amd/favicon.ico" rel="icon"/>
<link href="../genindex.html" rel="index" title="Index"/>
<link href="../search.html" rel="search" title="Search"/>
<link href="../reference/library-index.html" rel="next" title="ROCm API libraries &amp; tools"/>
<link href="release-notes.html" rel="prev" title="Release notes for AMD ROCm™ 6.0"/>
<meta content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" name="google-site-verification"/>
<!-- RTD Extra Head -->

<script id="READTHEDOCS_DATA" type="application/json">{"ad_free": false, "api_host": "https://readthedocs.com", "builder": "sphinx", "canonical_url": null, "docroot": "/docs/", "features": {"docsearch_disabled": false}, "global_analytics_code": null, "language": "en", "page": "about/CHANGELOG", "programming_language": "cpp", "project": "advanced-micro-devices-demo", "proxied_api_host": "/_", "source_suffix": ".md", "subprojects": {"advanced-micro-devices-amdmigraphx": "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/", "advanced-micro-devices-amdsmi": "https://rocm.docs.amd.com/projects/amdsmi/en/latest/", "advanced-micro-devices-bom": "https://rocm.docs.amd.com/projects/BOM/en/latest/", "advanced-micro-devices-composable-kernel": "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/", "advanced-micro-devices-dcgpu-project-bkcs": "https://rocm.docs.amd.com/projects/dcgpu-benchmarks/en/latest/", "advanced-micro-devices-gpu-cluster-networking-internal": "https://rocm.docs.amd.com/projects/gpu-cluster-networking-internal/en/latest/", "advanced-micro-devices-half": "https://rocm.docs.amd.com/projects/half/en/latest/", "advanced-micro-devices-hip": "https://rocm.docs.amd.com/projects/HIP/en/latest/", "advanced-micro-devices-hip-python": "https://rocm.docs.amd.com/projects/hip-python/en/latest/", "advanced-micro-devices-hip-vs": "https://rocm.docs.amd.com/projects/hip-vs/en/latest/", "advanced-micro-devices-hipblas": "https://rocm.docs.amd.com/projects/hipBLAS/en/latest/", "advanced-micro-devices-hipblaslt": "https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/", "advanced-micro-devices-hipcc": "https://rocm.docs.amd.com/projects/HIPCC-archive/en/develop/", "advanced-micro-devices-hipcc-llvm-project": "https://rocm.docs.amd.com/projects/HIPCC/en/latest/", "advanced-micro-devices-hipcub": "https://rocm.docs.amd.com/projects/hipCUB/en/latest/", "advanced-micro-devices-hipfft": "https://rocm.docs.amd.com/projects/hipFFT/en/latest/", "advanced-micro-devices-hipfort": "https://rocm.docs.amd.com/projects/hipfort/en/latest/", "advanced-micro-devices-hipify": "https://rocm.docs.amd.com/projects/HIPIFY/en/latest/", "advanced-micro-devices-hiprand": "https://rocm.docs.amd.com/projects/hipRAND/en/latest/", "advanced-micro-devices-hipsolver": "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/", "advanced-micro-devices-hipsparse": "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/", "advanced-micro-devices-hipsparselt": "https://rocm.docs.amd.com/projects/hipSPARSELt/en/latest/", "advanced-micro-devices-hiptensor": "https://rocm.docs.amd.com/projects/hipTensor/en/latest/", "advanced-micro-devices-linux-install-docs": "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/", "advanced-micro-devices-linux-install-docs-internal": "https://rocm.docs.amd.com/projects/install-on-linux-internal/en/latest/", "advanced-micro-devices-llvm-project-docs": "https://rocm.docs.amd.com/projects/llvm-project/en/latest/", "advanced-micro-devices-miopen": "https://rocm.docs.amd.com/projects/MIOpen/en/latest/", "advanced-micro-devices-mivisionx": "https://rocm.docs.amd.com/projects/MIVisionX/en/latest/", "advanced-micro-devices-omniperf": "https://rocm.docs.amd.com/projects/omniperf/en/latest/", "advanced-micro-devices-omnitrace": "https://rocm.docs.amd.com/projects/omnitrace/en/latest/", "advanced-micro-devices-openmp-llvm-project": "https://rocm.docs.amd.com/projects/OpenMP/en/latest/", "advanced-micro-devices-rccl": "https://rocm.docs.amd.com/projects/rccl/en/latest/", "advanced-micro-devices-rdc": "https://rocm.docs.amd.com/projects/rdc/en/latest/", "advanced-micro-devices-rocal": "https://rocm.docs.amd.com/projects/rocAL/en/latest/", "advanced-micro-devices-rocalution": "https://rocm.docs.amd.com/projects/rocALUTION/en/latest/", "advanced-micro-devices-rocblas": "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/", "advanced-micro-devices-rocdbgapi-docs": "https://rocm.docs.amd.com/projects/ROCdbgapi/en/latest/", "advanced-micro-devices-rocdecode": "https://rocm.docs.amd.com/projects/rocDecode/en/latest/", "advanced-micro-devices-rocfft": "https://rocm.docs.amd.com/projects/rocFFT/en/latest/", "advanced-micro-devices-rocgdb-internal": "https://rocm.docs.amd.com/projects/ROCgdb/en/latest/", "advanced-micro-devices-rocjpeg": "https://rocm.docs.amd.com/projects/rocJPEG/en/latest/", "advanced-micro-devices-rocm-bandwidth-test": "https://rocm.docs.amd.com/projects/rocm_bandwidth_test/en/latest/", "advanced-micro-devices-rocm-cmake": "https://rocm.docs.amd.com/projects/ROCmCMakeBuildTools/en/latest/", "advanced-micro-devices-rocm-docs-core": "https://rocm.docs.amd.com/projects/rocm-docs-core/en/latest/", "advanced-micro-devices-rocm-install-on-windows": "https://rocm.docs.amd.com/projects/install-on-windows/en/latest/", "advanced-micro-devices-rocm-install-on-windows-internal": "https://rocm.docs.amd.com/projects/install-on-windows-internal/en/latest/", "advanced-micro-devices-rocm-smi-lib": "https://rocm.docs.amd.com/projects/rocm_smi_lib/en/latest/", "advanced-micro-devices-rocminfo": "https://rocm.docs.amd.com/projects/rocminfo/en/latest/", "advanced-micro-devices-rocmradeon": "https://rocm.docs.amd.com/projects/radeon/en/latest/", "advanced-micro-devices-rocmvalidationsuite": "https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/", "advanced-micro-devices-rocprim": "https://rocm.docs.amd.com/projects/rocPRIM/en/latest/", "advanced-micro-devices-rocprofiler-docs": "https://rocm.docs.amd.com/projects/rocprofiler/en/latest/", "advanced-micro-devices-rocprofiler-sdk": "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/", "advanced-micro-devices-rocprofiler-sdk-internal": "https://rocm.docs.amd.com/projects/rocprofiler-sdk-internal/en/latest/", "advanced-micro-devices-rocpydecode": "https://rocm.docs.amd.com/projects/rocPyDecode/en/latest/", "advanced-micro-devices-rocr-debug-agent": "https://rocm.docs.amd.com/projects/rocr_debug_agent/en/latest/", "advanced-micro-devices-rocr-runtime": "https://rocm.docs.amd.com/projects/ROCR-Runtime/en/latest/", "advanced-micro-devices-rocrand": "https://rocm.docs.amd.com/projects/rocRAND/en/latest/", "advanced-micro-devices-rocsolver": "https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/", "advanced-micro-devices-rocsparse": "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/", "advanced-micro-devices-rocthrust": "https://rocm.docs.amd.com/projects/rocThrust/en/latest/", "advanced-micro-devices-roctracer-docs": "https://rocm.docs.amd.com/projects/roctracer/en/latest/", "advanced-micro-devices-rocwmma": "https://rocm.docs.amd.com/projects/rocWMMA/en/latest/", "advanced-micro-devices-rpp": "https://rocm.docs.amd.com/projects/rpp/en/latest/", "advanced-micro-devices-swab-documentation": "https://rocm.docs.amd.com/projects/swab-documentation/en/latest/", "advanced-micro-devices-tensile": "https://rocm.docs.amd.com/projects/Tensile/en/latest/", "advanced-micro-devices-transferbench": "https://rocm.docs.amd.com/projects/TransferBench/en/latest/"}, "theme": "rocm_docs_theme", "user_analytics_code": "", "version": "docs-6.0.0"}</script>
<!--
Using this variable directly instead of using `JSON.parse` is deprecated.
The READTHEDOCS_DATA global variable will be removed in the future.
-->
<script type="text/javascript">
READTHEDOCS_DATA = JSON.parse(document.getElementById('READTHEDOCS_DATA').innerHTML);
</script>

<!-- end RTD <extrahead> -->
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-demo" /><meta name="readthedocs-version-slug" content="docs-6.0.0" /><meta name="readthedocs-resolver-filename" content="/about/CHANGELOG.html" /><meta name="readthedocs-http-status" content="200" /></head>
<body data-bs-root-margin="0px 0px -60%" data-bs-spy="scroll" data-bs-target=".bd-toc-nav" data-default-mode="" data-offset="180">
<div class="skip-link d-print-none" id="pst-skip-link"><a href="#main-content">Skip to main content</a></div>
<div id="pst-scroll-pixel-helper"></div>
<button class="btn rounded-pill" id="pst-back-to-top" type="button">
<i class="fa-solid fa-arrow-up"></i>Back to top</button>
<input class="sidebar-toggle" id="pst-primary-sidebar-checkbox" type="checkbox"/>
<label class="overlay overlay-primary" for="pst-primary-sidebar-checkbox"></label>
<input class="sidebar-toggle" id="pst-secondary-sidebar-checkbox" type="checkbox"/>
<label class="overlay overlay-secondary" for="pst-secondary-sidebar-checkbox"></label>
<div class="search-button__wrapper">
<div class="search-button__overlay"></div>
<div class="search-button__search-container">
<form action="../search.html" class="bd-search d-flex align-items-center" method="get">
<i class="fa-solid fa-magnifying-glass"></i>
<input aria-label="Search..." autocapitalize="off" autocomplete="off" autocorrect="off" class="form-control" id="search-input" name="q" placeholder="Search..." spellcheck="false" type="search"/>
<span class="search-button__kbd-shortcut"><kbd class="kbd-shortcut__modifier">Ctrl</kbd>+<kbd>K</kbd></span>
</form></div>
</div>
<div class="pst-async-banner-revealer d-none">
<aside aria-label="Version warning" class="d-none d-print-none" id="bd-header-version-warning"></aside>
</div>
<aside aria-label="Announcement" class="bd-header-announcement">
<div class="bd-header-announcement__content">This is not the latest version of ROCm documentation. See <a href="https://rocm.docs.amd.com/en/latest/" id="rocm-banner">ROCm documentation</a> for the latest version.</div>
</aside>
<header class="common-header">
<nav class="navbar navbar-expand-xl">
<div class="container-fluid main-nav rocm-header">
<button aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler collapsed" data-bs-target="#navbarSupportedContent" data-bs-toggle="collapse" data-tracking-information="mainMenuToggle" id="nav-icon" type="button">
<span></span>
<span></span>
<span></span>
</button>
<div class="header-logo">
<a class="navbar-brand" href="https://www.amd.com/">
<img alt="AMD Logo" class="d-inline-block align-text-top hover-opacity" src="../_static/images/amd-header-logo.svg" title="AMD Logo" width="90"/>
</a>
<div class="vr vr mx-40 my-25"></div>
<a class="klavika-font hover-opacity" href="https://rocm.docs.amd.com/en/docs-6.0.0">ROCm™ Software 6.0.0</a>
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
<a aria-expanded="false" class="nav-link top-level header-menu-links" href="http://github.com/ROCm/ROCm" id="navgithub" role="button" target="_blank">
                                GitHub
                            </a>
</li>
<li class="nav-item">
<a aria-expanded="false" class="nav-link top-level header-menu-links" href="https://github.com/ROCm/ROCm/discussions" id="navcommunity" role="button" target="_blank">
                                Community
                            </a>
</li>
<li class="nav-item">
<a aria-expanded="false" class="nav-link top-level header-menu-links" href="https://rocm.blogs.amd.com/" id="navblogs" role="button" target="_blank">
                                Blogs
                            </a>
</li>
<li class="nav-item">
<a aria-expanded="false" class="nav-link top-level header-menu-links" href="https://www.amd.com/en/developer/resources/infinity-hub.html" id="navinfinity-hub" role="button" target="_blank">
                                Infinity Hub
                            </a>
</li>
<li class="nav-item">
<a aria-expanded="false" class="nav-link top-level header-menu-links" href="http://github.com/ROCm/ROCm/issues/new/choose" id="navsupport" role="button" target="_blank">
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
</div>
<div class="sidebar-primary-items__start sidebar-primary__section">
<div class="sidebar-primary-item">
<a class="navbar-brand logo" href="../index.html">
<p class="title logo__title">ROCm Documentation</p>
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
<div class="sidebar-primary-item"><nav aria-label="Main" class="bd-links bd-docs-nav">
<div class="bd-toc-item navbar-nav active">
<ul class="current nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../what-is-rocm.html">What is ROCm?</a></li>
<li class="toctree-l1 current active has-children"><a class="reference internal" href="release-notes.html">Release notes</a><details open="open"><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul class="current">
<li class="toctree-l2 current active"><a class="current reference internal" href="#">Changelog</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/RadeonOpenCompute/ROCm/labels/Verified%20Issue">Known issues</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/">ROCm on Linux</a></li>
<li class="toctree-l1"><a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-windows/en/docs-6.0.0/">HIP SDK on Windows</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Supported configurations</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/reference/system-requirements.html">Linux</a></li>
<li class="toctree-l1"><a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-windows/en/docs-6.0.0/reference/system-requirements.html">Windows</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../reference/library-index.html">API libraries &amp; tools</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How-to</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../how-to/deep-learning-rocm.html">Deep learning</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/gpu-enabled-mpi.html">Using MPI</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/system-debugging.html">Debugging</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../how-to/tuning-guides.html">Tuning guides</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../how-to/tuning-guides/mi100.html">MI100</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/tuning-guides/mi200.html">MI200</a></li>
<li class="toctree-l2"><a class="reference internal" href="../how-to/tuning-guides/w6000-v620.html">RDNA2</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/amd/rocm-examples">GitHub examples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../conceptual/gpu-arch.html">GPU architectures</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2 has-children"><a class="reference internal" href="../conceptual/gpu-arch/mi250.html">MI250 microarchitecture</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference external" href="https://www.amd.com/system/files/TechDocs/instinct-mi200-cdna2-instruction-set-architecture.pdf">AMD Instinct MI200/CDNA2 ISA</a></li>
<li class="toctree-l3"><a class="reference external" href="https://www.amd.com/system/files/documents/amd-cdna2-white-paper.pdf">White paper</a></li>
<li class="toctree-l3"><a class="reference internal" href="../conceptual/gpu-arch/mi200-performance-counters.html">Performance counter</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../conceptual/gpu-arch/mi100.html">MI100 microarchitecture</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference external" href="https://www.amd.com/system/files/TechDocs/instinct-mi100-cdna1-shader-instruction-set-architecture%C2%A0.pdf">AMD Instinct MI100/CDNA1 ISA</a></li>
<li class="toctree-l3"><a class="reference external" href="https://www.amd.com/system/files/documents/amd-cdna-whitepaper.pdf">White paper</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/gpu-memory.html">GPU memory</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/compiler-disambiguation.html">Compiler disambiguation</a></li>
<li class="toctree-l1"><a class="reference internal" href="compatibility/openmp.html">OpenMP</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/file-reorg.html">File structure (Linux FHS)</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/gpu-isolation.html">GPU isolation techniques</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/using-gpu-sanitizer.html">LLVM ASan</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/cmake-packages.html">Using CMake</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/More-about-how-ROCm-uses-PCIe-Atomics.html">ROCm &amp; PCIe atomics</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/ai-pytorch-inception.html">Inception v3 with PyTorch</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/ai-migraphx-optimization.html">Inference optimization with MIGraphX</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Contribute</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../contribute/index.html">Contribute to ROCm</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2 has-children"><a class="reference internal" href="../contribute/contribute-docs.html">Contribute to ROCm docs</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../contribute/toolchain.html">Documentation tools</a></li>
<li class="toctree-l3"><a class="reference internal" href="../contribute/building.html">Building documentation</a></li>
<li class="toctree-l3"><a class="reference internal" href="../contribute/feedback.html">Provide feedback</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="license.html">License</a></li>
</ul>
</div>
</nav></div>
</div>
<div class="sidebar-primary-items__end sidebar-primary__section">
<div class="sidebar-primary-item">
<div class="flat" data-ea-manual="true" data-ea-publisher="readthedocs" data-ea-type="readthedocs-sidebar" id="ethical-ad-placement">
</div>
</div>
</div>
<div id="rtd-footer-container"></div>
</div>
<main class="bd-main" id="main-content" role="main">
<div class="sbt-scroll-pixel-helper"></div>
<div class="bd-content">
<div class="bd-article-container">
<div class="bd-header-article d-print-none">
<div class="header-article-items header-article__inner">
<div class="header-article-items__start">
<div class="header-article-item"><label class="sidebar-toggle primary-toggle btn btn-sm" data-bs-placement="bottom" data-bs-toggle="tooltip" for="__primary" title="Toggle primary sidebar">
<span class="fa-solid fa-angle-right"></span>
</label></div>
<div class="header-article-item">
<nav aria-label="Breadcrumb" class="d-print-none">
<ul class="bd-breadcrumbs">
<li class="breadcrumb-item breadcrumb-home">
<a aria-label="Home" class="nav-link" href="../index.html">
<i class="fa-solid fa-home"></i>
</a>
</li>
<li class="breadcrumb-item"><a class="nav-link" href="release-notes.html">Release notes for AMD ROCm™ 6.0</a></li>
<li aria-current="page" class="breadcrumb-item active">Changelog</li>
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
<button class="sidebar-toggle secondary-toggle btn btn-sm" data-bs-placement="bottom" data-bs-toggle="tooltip" title="Toggle secondary sidebar">
<span class="fa-solid fa-list"></span>
</button>
</div></div>
</div>
</div>
</div>
<div class="onlyprint" id="jb-print-docs-body">
<h1>Changelog</h1>
<!-- Table of contents -->
<div id="print-main-content">
<div id="jb-print-toc">
<div>
<h2> Contents </h2>
</div>
<nav aria-label="Page">
<ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-6-0-0">ROCm 6.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#os-and-gpu-support-changes">OS and GPU support changes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#new-rocm-meta-package">New ROCm meta package</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filesystem-hierarchy-standard">Filesystem Hierarchy Standard</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#compiler-location-change">Compiler location change</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#documentation">Documentation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi50-end-of-support-notice">AMD Instinct™ MI50 end-of-support notice</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#known-issues">Known issues</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes">Library changes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amdmigraphx-2-8">AMDMIGraphX 2.8</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#additions">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#optimizations">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#fixes">Fixes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#changes">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#removals">Removals</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-smi">AMD SMI</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-6-0-0">HIP 6.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id2">Changes</a><ul class="nav section-nav flex-column">
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#changes-impacting-backward-incompatibility">Changes impacting backward incompatibility</a></li>
</ul>
</li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id3">Fixes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id4">Removals</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-2-0-0">hipBLAS 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id5">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#deprecations">Deprecations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id6">Removals</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-3-0-0">hipCUB 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id7">Changes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-13">hipFFT 1.0.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id8">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id9">Additions</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-2-0-0">hipSOLVER 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id10">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id11">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id12">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-3-0-0">hipSPARSE 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id13">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id14">Changes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hiptensor-1-1-0">hipTensor 1.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id15">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id16">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id17">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#miopen-2-19-0">MIOpen 2.19.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id18">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id19">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id20">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#mivisionx">MIVisionX</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#openmp">OpenMP</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id21">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id22">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id23">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-2-15-5">rccl 2.15.5</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id24">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id25">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id26">Fixes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id27">Removals</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-3-0-3">rocALUTION 3.0.3</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id28">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id29">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id30">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id31">Removals</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id32">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-4-0-0">rocBLAS 4.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id33">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id34">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id35">Deprecations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id36">Removals</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id37">Fixes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id38">Changes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-25">rocFFT 1.0.25</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id39">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id40">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id41">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id42">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocgdb-13-2">ROCgdb 13.2</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id43">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id44">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id45">Known issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-cmake-0-11-0">rocm-cmake 0.11.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id46">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id47">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-compiler">ROCm Compiler</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-3-0-0">rocPRIM 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id48">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id49">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id50">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#roc-profiler-2-0-0">Roc Profiler 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id51">Additions</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-2-10-17">rocRAND 2.10.17</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id52">Changes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id53">Optimizations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id54">Removals</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id55">Fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-24-0">rocSOLVER 3.24.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id56">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id57">Changes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-3-0-2">rocSPARSE 3.0.2</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id58">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id59">Removals</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id60">Fixes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id61">Additions</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-3-0-0">rocThrust 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id62">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id63">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id64">Known issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-1-3-0">rocWMMA 1.3.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id65">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id66">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id67">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-39-0">Tensile 4.39.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id68">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id69">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id70">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id71">Fixes</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-6-0-0">Library changes in ROCM 6.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id72">AMDMIGraphX 2.8</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id73">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id74">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id75">Fixes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id76">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id77">Removals</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id78">hipBLAS 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#added">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#deprecated">Deprecated</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#removed">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id79">hipCUB 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#changed">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id80">hipFFT 1.0.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id81">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id82">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hiprand-2-10-17">hipRAND 2.10.17</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#fixed">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id83">hipSOLVER 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id84">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id85">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id86">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id87">hipSPARSE 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id88">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id89">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id90">hipTensor 1.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id91">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id92">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id93">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id94">rocALUTION 3.0.3</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id95">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#optimized">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id96">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id97">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id98">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id99">rocBLAS 4.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id100">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id101">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id102">Deprecated</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id103">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id104">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id105">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id106">rocFFT 1.0.25</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id107">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id108">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id109">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id110">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id111">rocm-cmake 0.11.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id112">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id113">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id114">rocPRIM 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id115">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id116">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id117">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id118">rocSOLVER 3.24.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id119">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id120">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id121">rocSPARSE 3.0.2</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id122">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id123">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id124">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id125">Deprecated</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id126">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id127">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id128">rocThrust 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id129">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id130">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id131">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id132">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id133">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id134">rocWMMA 1.3.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id135">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id136">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id137">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id138">Tensile 4.39.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id139">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id140">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id141">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id142">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-7-1">ROCm 5.7.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#what-s-new-in-this-release">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#installing-all-gpu-addresssanitizer-packages-with-a-single-command">Installing all GPU AddressSanitizer packages with a single command</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-libraries">ROCm libraries</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas">rocBLAS</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-5-7-1-for-rocm-5-7-1">HIP 5.7.1 (for ROCm 5.7.1)</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#defect-fixes">Defect fixes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-7-1">Library changes in ROCM 5.7.1</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-8-2">hipSOLVER 1.8.2</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id143">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-7-0">ROCm 5.7.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#release-highlights-for-rocm-5-7">Release highlights for ROCm 5.7</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id144">AMD Instinct™ MI50 end-of-support notice</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#feature-updates">Feature updates</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#non-hostcall-hip-printf">Non-hostcall HIP printf</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#beta-release-of-llvm-addresssanitizer-asan-with-the-gpu">Beta release of LLVM AddressSanitizer (ASan) with the GPU</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id145">Defect fixes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-5-7-0">HIP 5.7.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id146">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id147">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id148">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id149">Fixes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id150">Known issues</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#upcoming-changes-for-hip-in-rocm-6-0-release">Upcoming changes for HIP in ROCm 6.0 release</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-7-0">Library changes in ROCM 5.7.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amdmigraphx-2-7">AMDMIGraphX 2.7</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id151">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id152">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id153">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id154">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id155">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-1-1-0">hipBLAS 1.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id156">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#dependencies">Dependencies</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-8-1">hipSOLVER 1.8.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id157">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-3-8">hipSPARSE 2.3.8</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#improved">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-1-11">rocALUTION 2.1.11</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id158">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id159">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-3-1-0">rocBLAS 3.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id160">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id161">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id162">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id163">Deprecated</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id164">Dependencies</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-24">rocFFT 1.0.24</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id165">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id166">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id167">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-cmake-0-10-0">rocm-cmake 0.10.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id168">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-13-1">rocPRIM 2.13.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id169">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id170">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-23-0">rocSOLVER 3.23.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id171">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id172">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id173">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-5-4">rocSPARSE 2.5.4</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id174">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id175">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id176">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-1-2-0">rocWMMA 1.2.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id177">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-38-0">Tensile 4.38.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id178">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id179">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id180">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id181">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-6-1">ROCm 5.6.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id182">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-5-6-1-for-rocm-5-6-1">HIP 5.6.1 (for ROCm 5.6.1)</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id183">Defect fixes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-6-1">Library changes in ROCM 5.6.1</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-3-7">hipSPARSE 2.3.7</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#bugfix">Bugfix</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-6-0">ROCm 5.6.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#release-highlights">Release highlights</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id184">OS and GPU support changes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amdsmi-cli-23-0-0-4">AMDSMI CLI 23.0.0.4</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id185">Additions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id186">Known issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-modules-dkms">Kernel modules (DKMS)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id187">Fixes</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-5-6-for-rocm-5-6">HIP 5.6 (for ROCm 5.6)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id188">Optimizations</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id189">Additions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id190">Changes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id191">Fixes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id192">Known issues</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#upcoming-changes-in-future-release">Upcoming changes in future release</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocgdb-13-for-rocm-5-6-0">ROCgdb-13 (For ROCm 5.6.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id193">Optimizations</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id194">Known issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprofiler-for-rocm-5-6-0">ROCprofiler (for ROCm 5.6.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id195">Optimizations</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id196">Additions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id197">Fixes</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-6-0">Library changes in ROCM 5.6.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-12">hipFFT 1.0.12</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id198">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id199">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-8-0">hipSOLVER 1.8.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id200">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-3-6">hipSPARSE 2.3.6</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id201">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id202">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-1-9">rocALUTION 2.1.9</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id203">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-3-0-0">rocBLAS 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id204">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id205">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id206">Deprecated</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id207">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id208">Dependencies</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id209">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id210">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-23">rocFFT 1.0.23</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id211">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id212">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id213">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-cmake-0-9-0">rocm-cmake 0.9.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id214">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-22-0">rocSOLVER 3.22.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id215">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id216">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id217">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-5-2">rocSPARSE 2.5.2</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id218">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-2-18-0">rocThrust 2.18.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id219">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id220">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-1-1-0">rocWMMA 1.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id221">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id222">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-37-0">Tensile 4.37.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id223">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id224">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id225">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id226">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-5-1">ROCm 5.5.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id227">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-sdk-for-windows">HIP SDK for Windows</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-api-change">HIP API change</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#hipdevicesetcacheconfig"><code class="docutils literal notranslate"><span class="pre">hipDeviceSetCacheConfig</span></code></a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-5-1">Library changes in ROCM 5.5.1</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-5-0">ROCm 5.5.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id228">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-enhancements">HIP enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#enhanced-stack-size-limit">Enhanced stack size limit</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcc-changes"><code class="docutils literal notranslate"><span class="pre">hipcc</span></code> changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#future-changes">Future changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#new-hip-apis-in-this-release">New HIP APIs in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-management-hip-apis">Memory management HIP APIs</a></li>
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#module-management-hip-apis">Module management HIP APIs</a></li>
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-graph-management-apis">HIP graph management APIs</a></li>
</ul>
</li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#openmp-enhancements">OpenMP enhancements</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#deprecations-and-warnings">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-deprecation">HIP deprecation</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#linux-file-system-hierarchy-standard-for-rocm">Linux file system hierarchy standard for ROCm</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#new-file-system-hierarchy">New file system hierarchy</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#backward-compatibility-with-older-file-systems">Backward compatibility with older file systems</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#wrapper-header-files">Wrapper header files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#library-files">Library files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#cmake-config-files">CMake config files</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-support-for-code-object-v3-deprecated">ROCm support for Code Object V3 deprecated</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#comgr-v3-0-changes">Comgr V3.0 changes</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#api-changes">API changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#actions-and-data-types">Actions and data types</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#deprecated-environment-variables">Deprecated environment variables</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#known-issues-in-this-release">Known issues in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#distributed-test-distributed-spawn-fails"><code class="docutils literal notranslate"><span class="pre">DISTRIBUTED</span></code>/<code class="docutils literal notranslate"><span class="pre">TEST_DISTRIBUTED_SPAWN</span></code> fails</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-5-0">Library changes in ROCM 5.5.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amdmigraphx-2-5">AMDMIGraphX 2.5</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id229">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id230">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id231">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id232">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-0-54-0">hipBLAS 0.54.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id233">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id234">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id235">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-2-13-1">hipCUB 2.13.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id236">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id237">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id238">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id239">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-11">hipFFT 1.0.11</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id240">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hiprand-2-10-16">hipRAND 2.10.16</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id241">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id242">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-7-0">hipSOLVER 1.7.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id243">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-3-5">hipSPARSE 2.3.5</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id244">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id245">MIOpen 2.19.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id246">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id247">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id248">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id249">rccl 2.15.5</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id250">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id251">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id252">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id253">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-1-8">rocALUTION 2.1.8</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id254">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id255">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id256">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-2-47-0">rocBLAS 2.47.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id257">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id258">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id259">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id260">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id261">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-22">rocFFT 1.0.22</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id262">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id263">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id264">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id265">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-cmake-0-8-1">rocm-cmake 0.8.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id266">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id267">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-13-0">rocPRIM 2.13.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id268">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id269">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id270">Known Issues</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id271">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id272">rocRAND 2.10.17</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id273">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id274">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id275">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-21-0">rocSOLVER 3.21.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id276">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id277">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id278">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id279">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-5-1">rocSPARSE 2.5.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id280">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id281">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id282">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-1-0">rocWMMA 1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id283">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id284">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-36-0">Tensile 4.36.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id285">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id286">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id287">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id288">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-4-3">ROCm 5.4.3</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id289">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-perl-scripts-deprecation">HIP Perl scripts deprecation</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id290">Linux file system hierarchy standard for ROCm</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id291">New file system hierarchy</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id292">Backward compatibility with older file systems</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id293">Wrapper header files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id294">Library files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id295">CMake config files</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id296">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#compiler-improvements">Compiler improvements</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id297">Known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#compiler-option-error-at-runtime">Compiler option error at runtime</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-4-3">Library changes in ROCM 5.4.3</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-21">rocFFT 1.0.21</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id298">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-4-2">ROCm 5.4.2</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id299">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id300">HIP Perl scripts deprecation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcc-options-deprecation"><code class="docutils literal notranslate"><span class="pre">hipcc</span></code> options deprecation</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id301">Known issues</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-4-2">Library changes in ROCM 5.4.2</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-4-1">ROCm 5.4.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id302">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id303">HIP enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#new-hip-api-hiplaunchhostfunc">New HIP API - hipLaunchHostFunc</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id304">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id305">HIP Perl scripts deprecation</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#ifwi-fixes">IFWI fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi200-firmware-ifwi-maintenance-update-3">AMD Instinct™ MI200 firmware IFWI maintenance update #3</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi200-sriov-virtualization-support">AMD Instinct™ MI200 SRIOV virtualization support</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-4-1">Library changes in ROCM 5.4.1</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-20">rocFFT 1.0.20</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id306">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-4-0">ROCm 5.4.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id307">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id308">HIP enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#support-for-wall-clock64">Support for wall_clock64</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#new-registry-added-for-gpu-max-hw-queues">New registry added for GPU_MAX_HW_QUEUES</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id309">New HIP APIs in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#error-handling">Error handling</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-tests-source-separation">HIP tests source separation</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id310">OpenMP enhancements</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id311">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id312">HIP Perl scripts deprecation</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id313">Linux file system hierarchy standard for ROCm</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id314">New file system hierarchy</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id315">Backward compatibility with older file systems</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id316">Wrapper header files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id317">Library files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id318">CMake config files</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id319">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-allocated-using-hiphostmalloc-with-flags-didn-t-exhibit-fine-grain-behavior">Memory allocated using hipHostMalloc() with flags didn’t exhibit fine-grain behavior</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#issue">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#fix">Fix</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#softhang-with-hipstreamwithcumask-test-on-amd-instinct">SoftHang with <code class="docutils literal notranslate"><span class="pre">hipStreamWithCUMask</span></code> test on AMD Instinct™</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id320">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id321">Fix</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-tools-gpu-ids">ROCm tools GPU IDs</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-4-0">Library changes in ROCM 5.4.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-0-53-0">hipBLAS 0.53.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id322">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-2-13-0">hipCUB 2.13.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id323">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id324">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-10">hipFFT 1.0.10</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id325">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id326">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-6-0">hipSOLVER 1.6.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id327">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-3-3">hipSPARSE 2.3.3</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id328">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id329">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-2-13-4">rccl 2.13.4</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id330">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id331">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-1-3">rocALUTION 2.1.3</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id332">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id333">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id334">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-2-46-0">rocBLAS 2.46.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id335">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id336">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id337">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id338">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-19">rocFFT 1.0.19</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id339">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id340">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id341">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-12-0">rocPRIM 2.12.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id342">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id343">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id344">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-2-10-16">rocRAND 2.10.16</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id345">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id346">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id347">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-20-0">rocSOLVER 3.20.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id348">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id349">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-4-0">rocSPARSE 2.4.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id350">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id351">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-2-17-0">rocThrust 2.17.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id352">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-0-9">rocWMMA 0.9</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id353">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id354">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-35-0">Tensile 4.35.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id355">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id356">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id357">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id358">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-3-3">ROCm 5.3.3</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id359">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#issue-with-rocthrust-and-rocprim-libraries">Issue with rocTHRUST and rocPRIM libraries</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-3-3">Library changes in ROCM 5.3.3</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-3-2">ROCm 5.3.2</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id360">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#peer-to-peer-dma-mapping-errors-with-sles-and-rhel">Peer-to-peer DMA mapping errors with SLES and RHEL</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-tuning-table">RCCL tuning table</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#sgemm-f32-gemm-routines-in-rocblas">SGEMM (F32 GEMM) routines in rocBLAS</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id361">Known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi200-sriov-virtualization-issue">AMD Instinct™ MI200 SRIOV virtualization issue</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi200-firmware-updates">AMD Instinct™ MI200 firmware updates</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#known-issue-with-rocthrust-and-rocprim-libraries">Known issue with rocThrust and rocPRIM libraries</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-3-2">Library changes in ROCM 5.3.2</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-3-0">ROCm 5.3.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id362">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id363">HIP Perl scripts deprecation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id364">Linux file system hierarchy standard for ROCm</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id365">New file system hierarchy</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id366">Backward compatibility with older file systems</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id367">Wrapper header files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id368">Library files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id369">CMake config files</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id370">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-produces-incorrect-results-with-rocm-5-2">Kernel produces incorrect results with ROCm 5.2</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id371">Known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#issue-with-openmp-extras-package-upgrade">Issue with OpenMP-extras package upgrade</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id372">AMD Instinct™ MI200 SRIOV virtualization issue</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#system-crash-when-immou-is-enabled">System crash when IMMOU is enabled</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-3-0">Library changes in ROCM 5.3.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-0-52-0">hipBLAS 0.52.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id373">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id374">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-2-12-0">hipCUB 2.12.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id375">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id376">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-9">hipFFT 1.0.9</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id377">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-5-0">hipSOLVER 1.5.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id378">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id379">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id380">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-3-1">hipSPARSE 2.3.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id381">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-1-0">rocALUTION 2.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id382">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id383">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-2-45-0">rocBLAS 2.45.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id384">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id385">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id386">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id387">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id388">Deprecated</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id389">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-18">rocFFT 1.0.18</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id390">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id391">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id392">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-cmake-0-8-0">rocm-cmake 0.8.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id393">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id394">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-11-0">rocPRIM 2.11.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id395">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-2-10-15">rocRAND 2.10.15</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id396">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-19-0">rocSOLVER 3.19.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id397">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id398">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id399">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id400">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-2-16-0">rocThrust 2.16.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id401">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-0-8">rocWMMA 0.8</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-34-0">Tensile 4.34.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id402">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id403">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id404">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id405">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-2-3">ROCm 5.2.3</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#changes-in-this-release">Changes in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#ubuntu-18-04-end-of-life-announcement">Ubuntu 18.04 end-of-life announcement</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-runtime">HIP runtime</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id406">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl">RCCL</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id407">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id408">Removals</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#development-tools">Development tools</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-2-3">Library changes in ROCM 5.2.3</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-2-12-10">rccl 2.12.10</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id409">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id410">Removed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-2-1">ROCm 5.2.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-2-1">Library changes in ROCM 5.2.1</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-2-0">ROCm 5.2.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id411">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id412">HIP enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-installation-guide-updates">HIP installation guide updates</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#support-for-device-side-malloc-on-hip-clang">Support for device-side malloc on HIP-Clang</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id413">New HIP APIs in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#device-management-hip-apis">Device management HIP APIs</a></li>
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#new-hip-runtime-apis-in-memory-management">New HIP runtime APIs in memory management</a></li>
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#id414">HIP graph management APIs</a></li>
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#support-for-virtual-memory-management-apis">Support for virtual memory management APIs</a></li>
</ul>
</li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#planned-hip-changes-in-future-releases">Planned HIP changes in future releases</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-math-and-communication-libraries">ROCm math and communication libraries</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#openmp-enhancements-in-this-release">OpenMP enhancements in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#ompt-target-support">OMPT target support</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id415">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id416">Linux file system hierarchy standard for ROCm</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id417">New file system hierarchy</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id418">Backward compatibility with older file systems</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id419">Wrapper header files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id420">Library files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id421">CMake config files</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#planned-deprecation-of-hip-rocclr-and-hip-base-packages">Planned deprecation of hip-rocclr and hip-base packages</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#deprecation-of-integrated-hip-directed-tests">Deprecation of integrated HIP directed tests</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id422">Defect fixes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id423">Known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#compiler-error-on-gfx1030-when-compiling-at-o0">Compiler error on gfx1030 when compiling at -O0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id424">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#workaround">Workaround</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#system-freeze-observed-during-cuda-memtest-checkpoint">System freeze observed during CUDA memtest checkpoint</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id425">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id426">Workaround</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hpc-test-fails-with-the-hsa-status-error-memory-fault-error">HPC test fails with the “HSA_STATUS_ERROR_MEMORY_FAULT” error</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id427">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id428">Workaround</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-produces-incorrect-result">Kernel produces incorrect result</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id429">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id430">Workaround</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#issue-with-applications-triggering-oversubscription">Issue with applications triggering oversubscription</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-2-0">Library changes in ROCM 5.2.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-0-51-0">hipBLAS 0.51.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id431">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id432">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-2-11-1">hipCUB 2.11.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id433">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-8">hipFFT 1.0.8</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id434">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-4-0">hipSOLVER 1.4.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id435">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id436">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-2-0">hipSPARSE 2.2.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id437">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-0-3">rocALUTION 2.0.3</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id438">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-2-44-0">rocBLAS 2.44.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id439">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id440">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id441">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id442">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id443">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-17">rocFFT 1.0.17</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id444">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id445">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id446">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id447">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-10-14">rocPRIM 2.10.14</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id448">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-2-10-14">rocRAND 2.10.14</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id449">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-18-0">rocSOLVER 3.18.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id450">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id451">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-2-0">rocSPARSE 2.2.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id452">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id453">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id454">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id455">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-2-15-0">rocThrust 2.15.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id456">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-0-7">rocWMMA 0.7</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id457">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id458">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-33-0">Tensile 4.33.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id459">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id460">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id461">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id462">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-1-3">ROCm 5.1.3</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-1-3">Library changes in ROCM 5.1.3</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-1-1">ROCm 5.1.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-1-1">Library changes in ROCM 5.1.1</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-1-0">ROCm 5.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id463">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id464">HIP enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id465">HIP installation guide updates</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#support-for-hip-graph">Support for HIP graph</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#planned-changes-for-hip-in-future-releases">Planned changes for HIP in future releases</a><ul class="nav section-nav flex-column">
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#separation-of-hiprtc-libhiprtc-library-from-hip-runtime-amdhip64">Separation of hiprtc (libhiprtc) library from hip runtime (amdhip64)</a></li>
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#hipdeviceprop-t-structure-enhancements">hipDeviceProp_t structure enhancements</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocdebugger-enhancements">ROCDebugger enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#multi-language-source-level-debugger">Multi-language source-level debugger</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#machine-interface-lanes-support">Machine interface lanes support</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#enhanced-clone-inferior-command">Enhanced - clone-inferior command</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#miopen-support-for-rdna-gpus">MIOpen support for RDNA GPUs</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#checkpoint-restore-support-with-criu">Checkpoint restore support with CRIU</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id466">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#driver-fails-to-load-after-installation">Driver fails to load after installation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocdebugger-defect-fixes">ROCDebugger defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#breakpoints-in-gpu-kernel-code-before-kernel-is-loaded">Breakpoints in GPU kernel code before kernel is loaded</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#registers-invalidated-after-write">Registers invalidated after write</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#scheduler-locking-and-gpu-wavefronts">Scheduler-locking and GPU wavefronts</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#rocdebugger-fails-before-completion-of-kernel-execution">ROCDebugger fails before completion of kernel execution</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id467">Known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#random-memory-access-fault-errors-observed-while-running-math-libraries-unit-tests">Random memory access fault errors observed while running math libraries unit tests</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#cu-masking-causes-application-to-freeze">CU masking causes application to freeze</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#failed-checkpoint-in-docker-containers">Failed checkpoint in Docker containers</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#issue-with-restoring-workloads-using-cooperative-groups-feature">Issue with restoring workloads using cooperative groups feature</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#radeon-pro-v620-and-w6800-workstation-gpus">Radeon Pro V620 and W6800 workstation GPUs</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#no-support-for-rocdebugger-on-sriov">No support for ROCDebugger on SRIOV</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#random-error-messages-in-rocm-smi-for-sr-iov">Random error messages in ROCm SMI for SR-IOV</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-1-0">Library changes in ROCM 5.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-0-50-0">hipBLAS 0.50.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id468">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id469">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id470">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-2-11-0">hipCUB 2.11.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id471">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id472">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-7">hipFFT 1.0.7</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id473">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hiprand-2-10-13">hipRAND 2.10.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id474">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-3-0">hipSOLVER 1.3.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id475">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id476">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id477">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-1-0">hipSPARSE 2.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id478">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id479">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id480">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id481">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-2-11-4">rccl 2.11.4</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id482">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id483">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-0-2">rocALUTION 2.0.2</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id484">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-2-43-0">rocBLAS 2.43.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id485">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id486">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id487">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id488">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-16">rocFFT 1.0.16</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id489">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id490">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id491">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id492">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-10-13">rocPRIM 2.10.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id493">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id494">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id495">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id496">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-2-10-13">rocRAND 2.10.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id497">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id498">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id499">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id500">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-17-0">rocSOLVER 3.17.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id501">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id502">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-1-0">rocSPARSE 2.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id503">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id504">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id505">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-2-14-0">rocThrust 2.14.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id506">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id507">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-32-0">Tensile 4.32.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id508">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id509">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id510">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id511">Removed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-0-2">ROCm 5.0.2</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id512">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#issue-with-hostcall-facility-in-hip-runtime">Issue with hostcall facility in HIP runtime</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-0-2">Library changes in ROCM 5.0.2</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-0-1">ROCm 5.0.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id513">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#refactor-of-hipcc-hipconfig">Refactor of HIPCC/HIPCONFIG</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-0-1">Library changes in ROCM 5.0.1</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-0-0">ROCm 5.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id514">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id515">HIP enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id516">HIP installation guide updates</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#managed-memory-allocation">Managed memory allocation</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#new-environment-variable">New environment variable</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#breaking-changes">Breaking changes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#runtime-breaking-change">Runtime breaking change</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id517">Known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#incorrect-dgpu-behavior-when-using-amdvbflash-tool">Incorrect dGPU behavior when using AMDVBFlash tool</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#issue-with-start-timestamp-in-rocprofiler">Issue with START timestamp in ROCProfiler</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id518">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#current-behavior">Current behavior</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#expected-behavior">Expected behavior</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#recommended-workaround">Recommended workaround</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id519">Radeon Pro V620 and W6800 workstation GPUs</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#no-support-for-smi-and-rocdebugger-on-sriov">No support for SMI and ROCDebugger on SRIOV</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id520">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-libraries-changes-deprecations-and-deprecation-removal">ROCm libraries changes – deprecations and deprecation removal</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-api-deprecations-and-warnings">HIP API deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#warning-arithmetic-operators-of-hip-complex-and-vector-types">Warning - arithmetic operators of HIP complex and vector types</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warning-compiler-generated-code-object-version-4-deprecation">Warning - compiler-generated code object version 4 deprecation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warning-miopentensile-deprecation">Warning - MIOpenTensile deprecation</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-0-0">Library changes in ROCM 5.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-0-49-0">hipBLAS 0.49.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id521">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id522">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-2-10-13">hipCUB 2.10.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id523">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id524">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id525">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-4">hipFFT 1.0.4</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id526">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id527">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-2-0">hipSOLVER 1.2.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id528">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id529">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-0-0">hipSPARSE 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id530">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-2-10-3">rccl 2.10.3</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id531">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id532">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-0-1">rocALUTION 2.0.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id533">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id534">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-2-42-0">rocBLAS 2.42.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id535">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id536">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id537">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id538">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-13">rocFFT 1.0.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id539">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id540">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id541">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-10-12">rocPRIM 2.10.12</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id542">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id543">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id544">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id545">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-2-10-12">rocRAND 2.10.12</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id546">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-16-0">rocSOLVER 3.16.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id547">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id548">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id549">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id550">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-0-0">rocSPARSE 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id551">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id552">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id553">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-2-13-0">rocThrust 2.13.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id554">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id555">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-31-0">Tensile 4.31.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id556">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id557">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id558">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id559">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id560">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</nav>
</div>
</div>
</div>
<div id="searchbox"></div>
<article class="bd-article">
<section class="tex2jax_ignore mathjax_ignore" id="changelog">
<h1>Changelog<a class="headerlink" href="#changelog" title="Link to this heading">#</a></h1><div class="sd-container-fluid sd-sphinx-override sd-p-0 sd-mt-2 sd-mb-4 sd-p-2 sd-rounded-1 docutils" id="rocm-docs-core-article-info">
<div class="sd-row sd-row-cols-2 sd-gx-2 sd-gy-1 docutils">
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils" style="color:gray;">
    Applies to Linux and Windows
</div>
<div class="sd-col sd-d-flex-row sd-align-minor-center docutils">
<div class="sd-container-fluid sd-sphinx-override docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-3 sd-row-cols-md-3 sd-row-cols-lg-3 sd-gx-3 sd-gy-1 docutils">
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils">
<p class="sd-p-0 sd-m-0" style="color:gray;"></p>
</div>
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils">
<p class="sd-p-0 sd-m-0" style="color:gray;"><span class="sd-pr-2"><svg aria-hidden="true" class="sd-octicon sd-octicon-calendar" height="16.0px" version="1.1" viewbox="0 0 16 16" width="16.0px"><path d="M4.75 0a.75.75 0 01.75.75V2h5V.75a.75.75 0 011.5 0V2h1.25c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0113.25 16H2.75A1.75 1.75 0 011 14.25V3.75C1 2.784 1.784 2 2.75 2H4V.75A.75.75 0 014.75 0zm0 3.5h8.5a.25.25 0 01.25.25V6h-11V3.75a.25.25 0 01.25-.25h2zm-2.25 4v6.75c0 .138.112.25.25.25h10.5a.25.25 0 00.25-.25V7.5h-11z" fill-rule="evenodd"></path></svg></span>2023</p>
</div>
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils">
<p class="sd-p-0 sd-m-0" style="color:gray;"><span class="sd-pr-2"><svg aria-hidden="true" class="sd-octicon sd-octicon-clock" height="16.0px" version="1.1" viewbox="0 0 16 16" width="16.0px"><path d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zm.5 4.75a.75.75 0 00-1.5 0v3.5a.75.75 0 00.471.696l2.5 1a.75.75 0 00.557-1.392L8.5 7.742V4.75z" fill-rule="evenodd"></path></svg></span>268 min read time</p>
</div>
</div>
</div>
</div>
</div>
</div>

<!-- Do not edit this file! This file is autogenerated with -->
<!--   tools/autotag/tag_script.py                          -->
<!-- Disable lints since this is an auto-generated file.    -->
<!-- markdownlint-disable blanks-around-headers             -->
<!-- markdownlint-disable no-duplicate-header               -->
<!-- markdownlint-disable no-blanks-blockquote              -->
<!-- markdownlint-disable ul-indent                         -->
<!-- markdownlint-disable no-trailing-spaces                -->
<!-- spellcheck-disable -->
<p>This page contains the release notes for AMD ROCm Software.</p>
<hr class="docutils"/>
<section id="rocm-6-0-0">
<h2>ROCm 6.0.0<a class="headerlink" href="#rocm-6-0-0" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable no-duplicate-header -->
<p>ROCm 6.0 is a major release with new performance optimizations, expanded frameworks and library
support, and improved developer experience. This includes initial enablement of the AMD Instinct™
MI300 series. Future releases will further enable and optimize this new platform. Key features include:</p>
<ul class="simple">
<li><p>Improved performance in areas like lower precision math and attention layers.</p></li>
<li><p>New hipSPARSELt library to accelerate AI workloads via AMD’s sparse matrix core technique.</p></li>
<li><p>Latest upstream support for popular AI frameworks like PyTorch, TensorFlow, and JAX.</p></li>
<li><p>New support for libraries, such as DeepSpeed, ONNX-RT, and CuPy.</p></li>
<li><p>Prepackaged HPC and AI containers on AMD Infinity Hub, with improved documentation and
tutorials on the <a class="reference external" href="https://rocm.docs.amd.com">AMD ROCm Docs</a> site.</p></li>
<li><p>Consolidated developer resources and training on the new AMD ROCm Developer Hub.</p></li>
</ul>
<section id="os-and-gpu-support-changes">
<h3>OS and GPU support changes<a class="headerlink" href="#os-and-gpu-support-changes" title="Link to this heading">#</a></h3>
<p>AMD Instinct™ MI300A and MI300X Accelerator support has been enabled for limited operating
systems.</p>
<ul class="simple">
<li><p>Ubuntu 22.04.3 (MI300A and MI300X)</p></li>
<li><p>RHEL 8.9 (MI300A)</p></li>
<li><p>SLES 15 SP5 (MI300A)</p></li>
</ul>
<p>We’ve added support for the following operating systems:</p>
<ul class="simple">
<li><p>RHEL 9.3</p></li>
<li><p>RHEL 8.9</p></li>
</ul>
<p>Note that, of ROCm 6.2, we’ve planned for end-of-support (EoS) for the following operating systems:</p>
<ul class="simple">
<li><p>Ubuntu 20.04.5</p></li>
<li><p>SLES 15 SP4</p></li>
<li><p>RHEL/CentOS 7.9</p></li>
</ul>
</section>
<section id="new-rocm-meta-package">
<h3>New ROCm meta package<a class="headerlink" href="#new-rocm-meta-package" title="Link to this heading">#</a></h3>
<p>We’ve added a new ROCm meta package for easy installation of all ROCm core packages, tools, and
libraries. For example, the following command will install the full ROCm package: <code class="docutils literal notranslate"><span class="pre">apt-get</span> <span class="pre">install</span> <span class="pre">rocm</span></code>
(Ubuntu), or <code class="docutils literal notranslate"><span class="pre">yum</span> <span class="pre">install</span> <span class="pre">rocm</span></code> (RHEL).</p>
</section>
<section id="filesystem-hierarchy-standard">
<h3>Filesystem Hierarchy Standard<a class="headerlink" href="#filesystem-hierarchy-standard" title="Link to this heading">#</a></h3>
<p>ROCm 6.0 fully adopts the Filesystem Hierarchy Standard (FHS) reorganization goals. We’ve removed
the backward compatibility support for old file locations.</p>
</section>
<section id="compiler-location-change">
<h3>Compiler location change<a class="headerlink" href="#compiler-location-change" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p>The installation path of LLVM has been changed from <code class="docutils literal notranslate"><span class="pre">/opt/rocm-&lt;rel&gt;/llvm</span></code> to
<code class="docutils literal notranslate"><span class="pre">/opt/rocm-&lt;rel&gt;/lib/llvm</span></code>. For backward compatibility, a symbolic link is provided to the old
location and will be removed in a future release.</p></li>
<li><p>The installation path of the device library bitcode has changed from <code class="docutils literal notranslate"><span class="pre">/opt/rocm-&lt;rel&gt;/amdgcn</span></code> to
<code class="docutils literal notranslate"><span class="pre">/opt/rocm-&lt;rel&gt;/lib/llvm/lib/clang/&lt;ver&gt;/lib/amdgcn</span></code>. For backward compatibility, a symbolic link
is provided and will be removed in a future release.</p></li>
</ul>
</section>
<section id="documentation">
<h3>Documentation<a class="headerlink" href="#documentation" title="Link to this heading">#</a></h3>
<p>CMake support has been added for documentation in the
<a class="reference external" href="https://github.com/RadeonOpenCompute/ROCm">ROCm repository</a>.</p>
</section>
<section id="amd-instinct-mi50-end-of-support-notice">
<h3>AMD Instinct™ MI50 end-of-support notice<a class="headerlink" href="#amd-instinct-mi50-end-of-support-notice" title="Link to this heading">#</a></h3>
<p>AMD Instinct MI50, Radeon Pro VII, and Radeon VII products (collectively gfx906 GPUs) enters
maintenance mode in ROCm 6.0.</p>
<p>As outlined in <a class="reference external" href="https://rocm.docs.amd.com/en/docs-5.6.0/release.html">5.6.0</a>, ROCm 5.7 was the
final release for gfx906 GPUs in a fully supported state.</p>
<ul class="simple">
<li><p>Henceforth, no new features and performance optimizations will be supported for the gfx906 GPUs.</p></li>
<li><p>Bug fixes and critical security patches will continue to be supported for the gfx906 GPUs until Q2
2024 (end of maintenance [EOM] will be aligned with the closest ROCm release).</p></li>
<li><p>Bug fixes will be made up to the next ROCm point release.</p></li>
<li><p>Bug fixes will not be backported to older ROCm releases for gfx906.</p></li>
<li><p>Distribution and operating system updates will continue per the ROCm release cadence for gfx906
GPUs until EOM.</p></li>
</ul>
</section>
<section id="known-issues">
<h3>Known issues<a class="headerlink" href="#known-issues" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p>Hang is observed with rocSPARSE tests: <a class="reference external" href="https://github.com/ROCm/ROCm/issues/2726">Issue 2726</a>.</p></li>
<li><p>AddressSanitizer instrumentation is incorrect for device global variables:
<a class="reference external" href="https://github.com/ROCm/ROCm/issues/2551">Issue 2551</a>.</p></li>
<li><p>Dynamically loaded HIP runtime library references incorrect version of <code class="docutils literal notranslate"><span class="pre">hipDeviceGetProperties</span></code>
API: <a class="reference external" href="https://github.com/ROCm/ROCm/issues/2728">Issue 2728</a>.</p></li>
<li><p>Memory access violations when running rocFFT-HMM:
<a class="reference external" href="https://github.com/ROCm/ROCm/issues/2730">Issue 2730</a>.</p></li>
</ul>
</section>
<section id="library-changes">
<h3>Library changes<a class="headerlink" href="#library-changes" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>AMDMIGraphX</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/AMDMIGraphX/releases/tag/rocm-6.0.0">2.8</a></p></td>
</tr>
<tr class="row-odd"><td><p>HIP</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/HIP/releases/tag/rocm-6.0.0">6.0.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/hipBLAS/releases/tag/rocm-6.0.0">2.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/hipCUB/releases/tag/rocm-6.0.0">3.0.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/hipFFT/releases/tag/rocm-6.0.0">1.0.13</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/hipSOLVER/releases/tag/rocm-6.0.0">2.0.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/hipSPARSE/releases/tag/rocm-6.0.0">3.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipTensor</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/hipTensor/releases/tag/rocm-6.0.0">1.1.0</a></p></td>
</tr>
<tr class="row-even"><td><p>MIOpen</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/MIOpen/releases/tag/rocm-6.0.0">2.19.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/rccl/releases/tag/rocm-6.0.0">2.15.5</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/rocALUTION/releases/tag/rocm-6.0.0">3.0.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/rocBLAS/releases/tag/rocm-6.0.0">4.0.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/rocFFT/releases/tag/rocm-6.0.0">1.0.25</a></p></td>
</tr>
<tr class="row-odd"><td><p>ROCgdb</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/ROCgdb/releases/tag/rocm-6.0.0">13.2</a></p></td>
</tr>
<tr class="row-even"><td><p>rocm-cmake</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/RadeonOpenCompute/rocm-cmake/releases/tag/rocm-6.0.0">0.11.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocPRIM</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/rocPRIM/releases/tag/rocm-6.0.0">3.0.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocprofiler</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocprofiler/releases/tag/rocm-6.0.0">2.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/rocRAND/releases/tag/rocm-6.0.0">2.10.17</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/rocSOLVER/releases/tag/rocm-6.0.0">3.24.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/rocSPARSE/releases/tag/rocm-6.0.0">3.0.2</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/rocThrust/releases/tag/rocm-6.0.0">3.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocWMMA</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/rocWMMA/releases/tag/rocm-6.0.0">1.3.0</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/Tensile/releases/tag/rocm-6.0.0">4.39.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="amdmigraphx-2-8">
<h4>AMDMIGraphX 2.8<a class="headerlink" href="#amdmigraphx-2-8" title="Link to this heading">#</a></h4>
<p>MIGraphX 2.8 for ROCm 6.0.0</p>
<section id="additions">
<h5>Additions<a class="headerlink" href="#additions" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Support for TorchMIGraphX via PyTorch</p></li>
<li><p>Boosted overall performance by integrating rocMLIR</p></li>
<li><p>INT8 support for ONNX Runtime</p></li>
<li><p>Support for ONNX version 1.14.1</p></li>
<li><p>Added new operators: <code class="docutils literal notranslate"><span class="pre">Qlinearadd</span></code>, <code class="docutils literal notranslate"><span class="pre">QlinearGlobalAveragePool</span></code>, <code class="docutils literal notranslate"><span class="pre">Qlinearconv</span></code>, <code class="docutils literal notranslate"><span class="pre">Shrink</span></code>, <code class="docutils literal notranslate"><span class="pre">CastLike</span></code>,
and <code class="docutils literal notranslate"><span class="pre">RandomUniform</span></code></p></li>
<li><p>Added an error message for when <code class="docutils literal notranslate"><span class="pre">gpu_targets</span></code> is not set during MIGraphX compilation</p></li>
<li><p>Added parameter to set tolerances with <code class="docutils literal notranslate"><span class="pre">migraphx-driver</span></code> verify</p></li>
<li><p>Added support for MXR files &gt; 4 GB</p></li>
<li><p>Added <code class="docutils literal notranslate"><span class="pre">MIGRAPHX_TRACE_MLIR</span></code> flag</p></li>
<li><p>BETA added capability for using ROCm Composable Kernels via the <code class="docutils literal notranslate"><span class="pre">MIGRAPHX_ENABLE_CK=1</span></code>
environment variable</p></li>
</ul>
</section>
<section id="optimizations">
<h5>Optimizations<a class="headerlink" href="#optimizations" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved performance support for INT8</p></li>
<li><p>Improved time precision while benchmarking candidate kernels from CK or MLIR</p></li>
<li><p>Removed contiguous from reshape parsing</p></li>
<li><p>Updated the <code class="docutils literal notranslate"><span class="pre">ConstantOfShape</span></code> operator to support Dynamic Batch</p></li>
<li><p>Simplified dynamic shapes-related operators to their static versions, where possible</p></li>
<li><p>Improved debugging tools for accuracy issues</p></li>
<li><p>Included a print warning about <code class="docutils literal notranslate"><span class="pre">miopen_fusion</span></code> while generating <code class="docutils literal notranslate"><span class="pre">mxr</span></code></p></li>
<li><p>General reduction in system memory usage during model compilation</p></li>
<li><p>Created additional fusion opportunities during model compilation</p></li>
<li><p>Improved debugging for matchers</p></li>
<li><p>Improved general debug messages</p></li>
</ul>
</section>
<section id="fixes">
<h5>Fixes<a class="headerlink" href="#fixes" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed scatter operator for nonstandard shapes with some models from ONNX Model Zoo</p></li>
<li><p>Provided a compile option to improve the accuracy of some models by disabling Fast-Math</p></li>
<li><p>Improved layernorm + pointwise fusion matching to ignore argument order</p></li>
<li><p>Fixed accuracy issue with <code class="docutils literal notranslate"><span class="pre">ROIAlign</span></code> operator</p></li>
<li><p>Fixed computation logic for the <code class="docutils literal notranslate"><span class="pre">Trilu</span></code> operator</p></li>
<li><p>Fixed support for the DETR model</p></li>
</ul>
</section>
<section id="changes">
<h5>Changes<a class="headerlink" href="#changes" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Changed MIGraphX version to 2.8</p></li>
<li><p>Extracted the test packages into a separate deb file when building MIGraphX from source</p></li>
</ul>
</section>
<section id="removals">
<h5>Removals<a class="headerlink" href="#removals" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed building Python 2.7 bindings</p></li>
</ul>
</section>
</section>
<section id="amd-smi">
<h4>AMD SMI<a class="headerlink" href="#amd-smi" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Integrated the E-SMI library: You can now query CPU-related information directly through AMD SMI.
Metrics include power, energy, performance, and other system details.</p></li>
<li><p>Added support for gfx942 metrics: You can now query MI300 device metrics to get real-time
information. Metrics include power, temperature, energy, and performance.</p></li>
<li><p>Added support for compute and memory partitions</p></li>
</ul>
</section>
<section id="hip-6-0-0">
<h4>HIP 6.0.0<a class="headerlink" href="#hip-6-0-0" title="Link to this heading">#</a></h4>
<p>HIP 6.0.0 for ROCm 6.0.0</p>
<section id="id1">
<h5>Additions<a class="headerlink" href="#id1" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>New fields and structs for external resource interoperability</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hipExternalMemoryHandleDesc_st</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipExternalMemoryBufferDesc_st</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipExternalSemaphoreHandleDesc_st</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipExternalSemaphoreSignalParams_st</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipExternalSemaphoreWaitParams_st</span> <span class="pre">Enumerations</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipExternalMemoryHandleType_enum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipExternalSemaphoreHandleType_enum</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipExternalMemoryHandleType_enum</span></code></p></li>
</ul>
</li>
<li><p>New environment variable <code class="docutils literal notranslate"><span class="pre">HIP_LAUNCH_BLOCKING</span></code></p>
<ul>
<li><p>For serialization on kernel execution. The default value is 0 (disable); kernel will execute normally as
defined in the queue. When this environment variable is set as 1 (enable), HIP runtime will
serialize kernel enqueue; behaves the same as AMD_SERIALIZE_KERNEL.</p></li>
</ul>
</li>
<li><p>More members are added in HIP struct <code class="docutils literal notranslate"><span class="pre">hipDeviceProp_t</span></code>, for new feature capabilities including:</p>
<ul>
<li><p>Texture</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxTexture1DMipmap;</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxTexture2DMipmap[2];</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxTexture2DLinear[3];</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxTexture2DGather[2];</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxTexture3DAlt[3];</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxTextureCubemap;</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxTexture1DLayered[2];</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxTexture2DLayered[3];</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxTextureCubemapLayered[2];</span></code></p></li>
</ul>
</li>
<li><p>Surface</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxSurface1D;</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxSurface2D[2];</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxSurface3D[3];</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxSurface1DLayered[2];</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxSurface2DLayered[3];</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxSurfaceCubemap;</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">int</span> <span class="pre">maxSurfaceCubemapLayered[2];</span></code></p></li>
</ul>
</li>
<li><p>Device</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hipUUID</span> <span class="pre">uuid;</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">char</span> <span class="pre">luid[8];</span></code> this is an 8-byte unique identifier. Only valid on Windows</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span> <span class="pre">luidDeviceNodeMask;</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p>LUID (Locally Unique Identifier) is supported for interoperability between devices. In HIP, more
members are added in the struct <code class="docutils literal notranslate"><span class="pre">hipDeviceProp_t</span></code>, as properties to identify each device:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">char</span> <span class="pre">luid[8];</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span> <span class="pre">luidDeviceNodeMask;</span></code></p></li>
</ul>
</li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>HIP only supports LUID on Windows OS.</p>
</div>
</section>
<section id="id2">
<h5>Changes<a class="headerlink" href="#id2" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Some OpenGL Interop HIP APIs are moved from the hip_runtime_api header to a new header file hip_gl_interop.h for the AMD platform, as follows:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hipGLGetDevices</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipGraphicsGLRegisterBuffer</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipGraphicsGLRegisterImage</span></code></p></li>
</ul>
</li>
</ul>
<section id="changes-impacting-backward-incompatibility">
<h6>Changes impacting backward incompatibility<a class="headerlink" href="#changes-impacting-backward-incompatibility" title="Link to this heading">#</a></h6>
<ul class="simple">
<li><p>Data types for members in <code class="docutils literal notranslate"><span class="pre">HIP_MEMCPY3D</span></code> structure are changed from <code class="docutils literal notranslate"><span class="pre">unsigned</span> <span class="pre">int</span></code> to <code class="docutils literal notranslate"><span class="pre">size_t</span></code>.</p></li>
<li><p>The value of the flag <code class="docutils literal notranslate"><span class="pre">hipIpcMemLazyEnablePeerAccess</span></code> is changed to <code class="docutils literal notranslate"><span class="pre">0x01</span></code>, which was previously
defined as <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
<li><p>Some device property attributes are not currently supported in HIP runtime. In order to maintain
consistency, the following related enumeration names are changed in <code class="docutils literal notranslate"><span class="pre">hipDeviceAttribute_t</span></code></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeName</span></code> is changed to <code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeUnused1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeUuid</span></code> is changed to <code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeUnused2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeArch</span></code> is changed to <code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeUnused3</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeGcnArch</span></code> is changed to <code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeUnused4</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeGcnArchName</span></code> is changed to <code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeUnused5</span></code></p></li>
</ul>
</li>
<li><p>HIP struct <code class="docutils literal notranslate"><span class="pre">hipArray</span></code> is removed from driver type header to comply with CUDA</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipArray_t</span></code> replaces <code class="docutils literal notranslate"><span class="pre">hipArray*</span></code>, as the pointer to array.</p>
<ul>
<li><p>This allows <code class="docutils literal notranslate"><span class="pre">hipMemcpyAtoH</span></code> and <code class="docutils literal notranslate"><span class="pre">hipMemcpyHtoA</span></code> to have the correct array type which is
equivalent to corresponding CUDA driver APIs.</p></li>
</ul>
</li>
</ul>
</section>
</section>
<section id="id3">
<h5>Fixes<a class="headerlink" href="#id3" title="Link to this heading">#</a></h5>
<ul>
<li><p>Kernel launch maximum dimension validation is added specifically on gridY and gridZ in the HIP API <code class="docutils literal notranslate"><span class="pre">hipModule-LaunchKernel</span></code>. As a result,when <code class="docutils literal notranslate"><span class="pre">hipGetDeviceAttribute</span></code> is called for the value of <code class="docutils literal notranslate"><span class="pre">hipDeviceAttributeMaxGrid-Dim</span></code>, the behavior on the AMD platform is equivalent to NVIDIA.</p></li>
<li><p>The HIP stream synchronization behavior is changed in internal stream functions, in which a flag “wait” is added and set when the current stream is null pointer while executing stream synchronization on other explicitly created streams. This change avoids blocking of execution on null/default stream. The change won’t affect usage of applications, and makes them behave the same on the AMD platform as NVIDIA.</p></li>
<li><p>Error handling behavior on unsupported GPU is fixed, HIP runtime will log out error message, instead of creating signal abortion error which is invisible to developers but continued kernel execution process. This is for the case when developers compile any application via hipcc, setting the option <code class="docutils literal notranslate"><span class="pre">--offload-arch</span></code> with GPU ID which is different from the one on the system.</p></li>
<li><p>HIP complex vector type multiplication and division operations. On AMD platform, some duplicated complex operators are removed to avoid compilation failures. In HIP, <code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code> and <code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span></code> are defined as complex data types: <code class="docutils literal notranslate"><span class="pre">typedef</span> <span class="pre">float2</span> <span class="pre">hipFloatComplex;</span> <span class="pre">typedef</span> <span class="pre">double2</span> <span class="pre">hipDoubleComplex;</span></code> Any application that uses complex multiplication and division operations needs to replace ‘*’ and ‘/’ operators with the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipCmulf()</span></code> and <code class="docutils literal notranslate"><span class="pre">hipCdivf()</span></code> for <code class="docutils literal notranslate"><span class="pre">hipFloatComplex</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipCmul()</span></code> and <code class="docutils literal notranslate"><span class="pre">hipCdiv()</span></code> for <code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span></code></p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>These complex operations are equivalent to corresponding types/functions on NVIDIA platform.</p>
</div>
</li>
</ul>
</section>
<section id="id4">
<h5>Removals<a class="headerlink" href="#id4" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Deprecated Heterogeneous Compute (HCC) symbols and flags are removed from the HIP source code, including:</p>
<ul>
<li><p>Build options on obsolete <code class="docutils literal notranslate"><span class="pre">HCC_OPTIONS</span></code> were removed from cmake.</p></li>
<li><p>Micro definitions are removed:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">HIP_INCLUDE_HIP_HCC_DETAIL_DRIVER_TYPES_H</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIP_INCLUDE_HIP_HCC_DETAIL_HOST_DEFINES_H</span></code></p></li>
</ul>
</li>
<li><p>Compilation flags for the platform definitions</p>
<ul>
<li><p>AMD platform</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">HIP_PLATFORM_HCC</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HCC</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIP_ROCclr</span></code></p></li>
</ul>
</li>
<li><p>NVIDIA platform</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">HIP_PLATFORM_NVCC</span></code>
&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p>File directories in the clr repository are removed, for more details see https://github.com/ROCm-Developer-Tools/clr/blob/develop/hipamd/include/hip/hcc_detail and https://github.com/ROCm-Developer-Tools/clr/blob/develop/hipamd/include/hip/nvcc_detail
=======</p></li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">hcc_detail</span></code> and <code class="docutils literal notranslate"><span class="pre">nvcc_detail</span></code> directories in the clr repository are removed.</p></li>
</ul>
<blockquote>
<div><blockquote>
<div><blockquote>
<div><blockquote>
<div><blockquote>
<div><blockquote>
<div><blockquote>
<div><p>ebfec1b7 (remove nvcc (#3313))</p>
</div></blockquote>
</div></blockquote>
</div></blockquote>
</div></blockquote>
</div></blockquote>
</div></blockquote>
</div></blockquote>
<ul class="simple">
<li><p>Deprecated gcnArch is removed from hip device struct <code class="docutils literal notranslate"><span class="pre">hipDeviceProp_t</span></code>.</p></li>
<li><p>Deprecated <code class="docutils literal notranslate"><span class="pre">enum</span> <span class="pre">hipMemoryType</span> <span class="pre">memoryType;</span></code> is removed from HIP struct <code class="docutils literal notranslate"><span class="pre">hipPointerAttribute_t</span></code> union.</p></li>
</ul>
</section>
</section>
<section id="hipblas-2-0-0">
<h4>hipBLAS 2.0.0<a class="headerlink" href="#hipblas-2-0-0" title="Link to this heading">#</a></h4>
<p>hipBLAS 2.0.0 for ROCm 6.0.0</p>
<section id="id5">
<h5>Additions<a class="headerlink" href="#id5" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>New option to define <code class="docutils literal notranslate"><span class="pre">HIPBLAS_USE_HIP_BFLOAT16</span></code> to switch API to use the <code class="docutils literal notranslate"><span class="pre">hip_bfloat16</span></code> type</p></li>
<li><p>New <code class="docutils literal notranslate"><span class="pre">hipblasGemmExWithFlags</span></code> API</p></li>
</ul>
</section>
<section id="deprecations">
<h5>Deprecations<a class="headerlink" href="#deprecations" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipblasDatatype_t</span></code>; use <code class="docutils literal notranslate"><span class="pre">hipDataType</span></code> instead</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipblasComplex</span></code>; use <code class="docutils literal notranslate"><span class="pre">hipComplex</span></code> instead</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipblasDoubleComplex</span></code>; use <code class="docutils literal notranslate"><span class="pre">hipDoubleComplex</span></code> instead</p></li>
<li><p>Use of <code class="docutils literal notranslate"><span class="pre">hipblasDatatype_t</span></code> for <code class="docutils literal notranslate"><span class="pre">hipblasGemmEx</span></code> for compute-type; use <code class="docutils literal notranslate"><span class="pre">hipblasComputeType_t</span></code> instead</p></li>
</ul>
</section>
<section id="id6">
<h5>Removals<a class="headerlink" href="#id6" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipblasXtrmm</span></code> (calculates B &lt;- alpha * op(A) * B) has been replaced with <code class="docutils literal notranslate"><span class="pre">hipblasXtrmm</span></code> (calculates
C &lt;- alpha * op(A) * B)</p></li>
</ul>
</section>
</section>
<section id="hipcub-3-0-0">
<h4>hipCUB 3.0.0<a class="headerlink" href="#hipcub-3-0-0" title="Link to this heading">#</a></h4>
<p>hipCUB 3.0.0 for ROCm 6.0.0</p>
<section id="id7">
<h5>Changes<a class="headerlink" href="#id7" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed <code class="docutils literal notranslate"><span class="pre">DOWNLOAD_ROCPRIM</span></code>: you can force rocPRIM to download using
<code class="docutils literal notranslate"><span class="pre">DEPENDENCIES_FORCE_DOWNLOAD</span></code></p></li>
</ul>
</section>
</section>
<section id="hipfft-1-0-13">
<h4>hipFFT 1.0.13<a class="headerlink" href="#hipfft-1-0-13" title="Link to this heading">#</a></h4>
<p>hipFFT 1.0.13 for ROCm 6.0.0</p>
<section id="id8">
<h5>Changes<a class="headerlink" href="#id8" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipfft-rider</span></code> has been renamed to <code class="docutils literal notranslate"><span class="pre">hipfft-bench</span></code>; it is controlled by the <code class="docutils literal notranslate"><span class="pre">BUILD_CLIENTS_BENCH</span></code>
CMake option (note that a link for the old file name is installed, and the old <code class="docutils literal notranslate"><span class="pre">BUILD_CLIENTS_RIDER</span></code>
CMake option is accepted for backwards compatibility, but both will be removed in a future release)</p></li>
<li><p>Binaries in debug builds no longer have a <code class="docutils literal notranslate"><span class="pre">-d</span></code> suffix</p></li>
<li><p>The minimum rocFFT required version has been updated to 1.0.21</p></li>
</ul>
</section>
<section id="id9">
<h5>Additions<a class="headerlink" href="#id9" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipfftXtSetGPUs</span></code>, <code class="docutils literal notranslate"><span class="pre">hipfftXtMalloc,</span> <span class="pre">hipfftXtMemcpy</span></code>, <code class="docutils literal notranslate"><span class="pre">hipfftXtFree</span></code>, and <code class="docutils literal notranslate"><span class="pre">hipfftXtExecDescriptor</span></code> APIs
have been implemented to allow FFT computing on multiple devices in a single process</p></li>
</ul>
</section>
</section>
<section id="hipsolver-2-0-0">
<h4>hipSOLVER 2.0.0<a class="headerlink" href="#hipsolver-2-0-0" title="Link to this heading">#</a></h4>
<p>hipSOLVER 2.0.0 for ROCm 6.0.0</p>
<section id="id10">
<h5>Additions<a class="headerlink" href="#id10" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added hipBLAS as an optional dependency to <code class="docutils literal notranslate"><span class="pre">hipsolver-test</span></code></p>
<ul>
<li><p>You can use the <code class="docutils literal notranslate"><span class="pre">BUILD_HIPBLAS_TESTS</span></code> CMake option to test the compatibility between hipSOLVER
and hipBLAS</p></li>
</ul>
</li>
</ul>
</section>
<section id="id11">
<h5>Changes<a class="headerlink" href="#id11" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The <code class="docutils literal notranslate"><span class="pre">hipsolverOperation_t</span></code> type is now an alias of <code class="docutils literal notranslate"><span class="pre">hipblasOperation_t</span></code></p></li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">hipsolverFillMode_t</span></code> type is now an alias of <code class="docutils literal notranslate"><span class="pre">hipblasFillMode_t</span></code></p></li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">hipsolverSideMode_t</span></code> type is now an alias of <code class="docutils literal notranslate"><span class="pre">hipblasSideMode_t</span></code></p></li>
</ul>
</section>
<section id="id12">
<h5>Fixes<a class="headerlink" href="#id12" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Tests for hipSOLVER info updates in <code class="docutils literal notranslate"><span class="pre">ORGBR/UNGBR</span></code>, <code class="docutils literal notranslate"><span class="pre">ORGQR/UNGQR</span></code>, <code class="docutils literal notranslate"><span class="pre">ORGTR/UNGTR</span></code>,
<code class="docutils literal notranslate"><span class="pre">ORMQR/UNMQR</span></code>, and <code class="docutils literal notranslate"><span class="pre">ORMTR/UNMTR</span></code></p></li>
</ul>
</section>
</section>
<section id="hipsparse-3-0-0">
<h4>hipSPARSE 3.0.0<a class="headerlink" href="#hipsparse-3-0-0" title="Link to this heading">#</a></h4>
<p>hipSPARSE 3.0.0 for ROCm 6.0.0</p>
<section id="id13">
<h5>Additions<a class="headerlink" href="#id13" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added <code class="docutils literal notranslate"><span class="pre">hipsparseGetErrorName</span></code> and <code class="docutils literal notranslate"><span class="pre">hipsparseGetErrorString</span></code></p></li>
</ul>
</section>
<section id="id14">
<h5>Changes<a class="headerlink" href="#id14" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Changed the <code class="docutils literal notranslate"><span class="pre">hipsparseSpSV_solve()</span></code> API function to match the cuSPARSE API</p></li>
<li><p>Changed generic API functions to use const descriptors</p></li>
<li><p>Improved documentation</p></li>
</ul>
</section>
</section>
<section id="hiptensor-1-1-0">
<h4>hipTensor 1.1.0<a class="headerlink" href="#hiptensor-1-1-0" title="Link to this heading">#</a></h4>
<p>hipTensor 1.1.0 for ROCm 6.0.0</p>
<section id="id15">
<h5>Additions<a class="headerlink" href="#id15" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Architecture support for gfx942</p></li>
<li><p>Client tests configuration parameters now support YAML file input format</p></li>
</ul>
</section>
<section id="id16">
<h5>Changes<a class="headerlink" href="#id16" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Doxygen now treats warnings as errors</p></li>
</ul>
</section>
<section id="id17">
<h5>Fixes<a class="headerlink" href="#id17" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Client tests output redirections now behave accordingly</p></li>
<li><p>Removed dependency static library deployment</p></li>
<li><p>Security issues for documentation</p></li>
<li><p>Compile issues in debug mode</p></li>
<li><p>Corrected soft link for ROCm deployment</p></li>
</ul>
</section>
</section>
<section id="miopen-2-19-0">
<h4>MIOpen 2.19.0<a class="headerlink" href="#miopen-2-19-0" title="Link to this heading">#</a></h4>
<p>MIOpen 2.19.0 for ROCm 6.0.0</p>
<section id="id18">
<h5>Additions<a class="headerlink" href="#id18" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>ROCm 5.5 support for gfx1101 (Navi32)</p></li>
</ul>
</section>
<section id="id19">
<h5>Changes<a class="headerlink" href="#id19" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Tuning results for MLIR on ROCm 5.5</p></li>
<li><p>Bumped MLIR commit to 5.5.0 release tag</p></li>
</ul>
</section>
<section id="id20">
<h5>Fixes<a class="headerlink" href="#id20" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>3-D convolution host API bug</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">[HOTFIX][MI200][FP16]</span></code> has been disabled for <code class="docutils literal notranslate"><span class="pre">ConvHipImplicitGemmBwdXdlops</span></code> when FP16_ALT is
required</p></li>
</ul>
</section>
</section>
<section id="mivisionx">
<h4>MIVisionX<a class="headerlink" href="#mivisionx" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Added Comprehensive CTests to aid developers</p></li>
<li><p>Introduced Doxygen support for complete API documentation</p></li>
<li><p>Simplified dependencies for rocAL</p></li>
</ul>
</section>
<section id="openmp">
<h4>OpenMP<a class="headerlink" href="#openmp" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>MI300:</p>
<ul>
<li><p>Added support for gfx942 targets</p></li>
<li><p>Fixed declare target variable access in unified_shared_memory mode</p></li>
<li><p>Enabled OMPX_APU_MAPS environment variable for MI200 and gfx942</p></li>
<li><p>Handled global pointers in forced USM (<code class="docutils literal notranslate"><span class="pre">OMPX_APU_MAPS</span></code>)</p></li>
</ul>
</li>
<li><p>Nextgen AMDGPU plugin:</p>
<ul>
<li><p>Respect <code class="docutils literal notranslate"><span class="pre">GPU_MAX_HW_QUEUES</span></code> in the AMDGPU Nextgen plugin, which takes precedence over the
standard <code class="docutils literal notranslate"><span class="pre">LIBOMPTARGET_AMDGPU_NUM_HSA_QUEUES</span></code> environment variable</p></li>
<li><p>Changed the default for <code class="docutils literal notranslate"><span class="pre">LIBOMPTARGET_AMDGPU_TEAMS_PER_CU</span></code> from 4 to 6</p></li>
<li><p>Fixed the behavior of the <code class="docutils literal notranslate"><span class="pre">OMPX_FORCE_SYNC_REGIONS</span></code> environment variable, which is used to
force synchronous target regions (the default is to use an asynchronous implementation)</p></li>
<li><p>Added support for and enabled default of code object version 5</p></li>
<li><p>Implemented target OMPT callbacks and trace records support in the nextgen plugin</p></li>
</ul>
</li>
<li><p>Specialized kernels:</p>
<ul>
<li><p>Removes redundant copying of arrays when xteam reductions are active but not offloaded</p></li>
<li><p>Tuned the number of teams for BigJumpLoop</p></li>
<li><p>Enables specialized kernel generation with nested OpenMP pragma, as long as there is no nested
omp-parallel directive</p></li>
</ul>
</li>
</ul>
<section id="id21">
<h5>Additions<a class="headerlink" href="#id21" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">-fopenmp-runtimelib={lib,lib-perf,lib-debug}</span></code> to select libs</p></li>
<li><p>Warning if mixed HIP / OpenMP offloading (i.e., if HIP language mode is active, but OpenMP target
directives are encountered)</p></li>
<li><p>Introduced compile-time limit for the number of GPUs supported in a system: 16 GPUs in a single
node is currently the maximum supported</p></li>
</ul>
</section>
<section id="id22">
<h5>Changes<a class="headerlink" href="#id22" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Correctly compute number of waves when workgroup size is less than the wave size</p></li>
<li><p>Implemented <code class="docutils literal notranslate"><span class="pre">LIBOMPTARGET_KERNEL_TRACE=3</span></code>, which prints DEVID traces and API timings</p></li>
<li><p>ASAN support for openmp release, debug, and perf libraries</p></li>
<li><p>Changed LDS lowering default to hybrid</p></li>
</ul>
</section>
<section id="id23">
<h5>Fixes<a class="headerlink" href="#id23" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed RUNPATH for gdb plugin</p></li>
<li><p>Fixed hang in OMPT support if flush trace is called when there are no helper threads</p></li>
</ul>
</section>
</section>
<section id="rccl-2-15-5">
<h4>rccl 2.15.5<a class="headerlink" href="#rccl-2-15-5" title="Link to this heading">#</a></h4>
<p>RCCL 2.15.5 for ROCm 6.0.0</p>
<section id="id24">
<h5>Changes<a class="headerlink" href="#id24" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Compatibility with NCCL 2.15.5</p></li>
<li><p>Renamed the unit test executable to <code class="docutils literal notranslate"><span class="pre">rccl-UnitTests</span></code></p></li>
</ul>
</section>
<section id="id25">
<h5>Additions<a class="headerlink" href="#id25" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>HW-topology-aware binary tree implementation</p></li>
<li><p>Experimental support for MSCCL</p></li>
<li><p>New unit tests for hipGraph support</p></li>
<li><p>NPKit integration</p></li>
</ul>
</section>
<section id="id26">
<h5>Fixes<a class="headerlink" href="#id26" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>rocm-smi ID conversion</p></li>
<li><p>Support for <code class="docutils literal notranslate"><span class="pre">HIP_VISIBLE_DEVICES</span></code> for unit tests</p></li>
<li><p>Support for p2p transfers to non (HIP) visible devices</p></li>
</ul>
</section>
<section id="id27">
<h5>Removals<a class="headerlink" href="#id27" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed TransferBench from tools as it exists in standalone repo:
<a class="github reference external" href="https://github.com/ROCmSoftwarePlatform/TransferBench">ROCmSoftwarePlatform/TransferBench</a></p></li>
</ul>
</section>
</section>
<section id="rocalution-3-0-3">
<h4>rocALUTION 3.0.3<a class="headerlink" href="#rocalution-3-0-3" title="Link to this heading">#</a></h4>
<p>rocALUTION 3.0.3 for ROCm 6.0.0</p>
<section id="id28">
<h5>Additions<a class="headerlink" href="#id28" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Support for 64bit integer vectors</p></li>
<li><p>Inclusive and exclusive sum functionality for vector classes</p></li>
<li><p>Transpose functionality for <code class="docutils literal notranslate"><span class="pre">GlobalMatrix</span></code> and <code class="docutils literal notranslate"><span class="pre">LocalMatrix</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">TripleMatrixProduct</span></code> functionality for <code class="docutils literal notranslate"><span class="pre">LocalMatrix</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">Sort()</span></code> function for <code class="docutils literal notranslate"><span class="pre">LocalVector</span></code> class</p></li>
<li><p>Multiple stream support to the HIP backend</p></li>
</ul>
</section>
<section id="id29">
<h5>Optimizations<a class="headerlink" href="#id29" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">GlobalMatrix::Apply()</span></code> now uses multiple streams to better hide communication</p></li>
</ul>
</section>
<section id="id30">
<h5>Changes<a class="headerlink" href="#id30" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Matrix dimensions and number of non-zeros are now stored using 64-bit integers</p></li>
<li><p>Improved the ILUT preconditioner</p></li>
</ul>
</section>
<section id="id31">
<h5>Removals<a class="headerlink" href="#id31" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">LocalVector::GetIndexValues(ValueType*)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">LocalVector::SetIndexValues(const</span> <span class="pre">ValueType*)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">LocalMatrix::RSDirectInterpolation(const</span> <span class="pre">LocalVector&amp;,</span> <span class="pre">const</span> <span class="pre">LocalVector&amp;,</span> <span class="pre">LocalMatrix*,</span> <span class="pre">LocalMatrix*)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">LocalMatrix::RSExtPIInterpolation(const</span> <span class="pre">LocalVector&amp;,</span> <span class="pre">const</span> <span class="pre">LocalVector&amp;,</span> <span class="pre">bool,</span> <span class="pre">float,</span> <span class="pre">LocalMatrix*,</span> <span class="pre">LocalMatrix*)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">LocalMatrix::RugeStueben()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">LocalMatrix::AMGSmoothedAggregation(ValueType,</span> <span class="pre">const</span> <span class="pre">LocalVector&amp;,</span> <span class="pre">const</span> <span class="pre">LocalVector&amp;,</span> <span class="pre">LocalMatrix*,</span> <span class="pre">LocalMatrix*,</span> <span class="pre">int)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">LocalMatrix::AMGAggregation(const</span> <span class="pre">LocalVector&amp;,</span> <span class="pre">LocalMatrix*,</span> <span class="pre">LocalMatrix*)</span></code></p></li>
</ul>
</section>
<section id="id32">
<h5>Fixes<a class="headerlink" href="#id32" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Unit tests no longer ignore BCSR block dimension</p></li>
<li><p>Fixed documentation typos</p></li>
<li><p>Bug in multi-coloring for non-symmetric matrix patterns</p></li>
</ul>
</section>
</section>
<section id="rocblas-4-0-0">
<h4>rocBLAS 4.0.0<a class="headerlink" href="#rocblas-4-0-0" title="Link to this heading">#</a></h4>
<p>rocBLAS 4.0.0 for ROCm 6.0.0</p>
<section id="id33">
<h5>Additions<a class="headerlink" href="#id33" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Beta API <code class="docutils literal notranslate"><span class="pre">rocblas_gemm_batched_ex3</span></code> and <code class="docutils literal notranslate"><span class="pre">rocblas_gemm_strided_batched_ex3</span></code></p></li>
<li><p>Input/output type f16_r/bf16_r and execution type f32_r support for Level 2 gemv_batched and
gemv_strided_batched</p></li>
<li><p>Use of <code class="docutils literal notranslate"><span class="pre">rocblas_status_excluded_from_build</span></code> when calling functions that require Tensile (when using
rocBLAS built without Tensile)</p></li>
<li><p>System for asynchronous kernel launches that set a <code class="docutils literal notranslate"><span class="pre">rocblas_status</span></code> failure based on a
<code class="docutils literal notranslate"><span class="pre">hipPeekAtLastError</span></code> discrepancy</p></li>
</ul>
</section>
<section id="id34">
<h5>Optimizations<a class="headerlink" href="#id34" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>TRSM performance for small sizes (m &lt; 32 &amp;&amp; n &lt; 32)</p></li>
</ul>
</section>
<section id="id35">
<h5>Deprecations<a class="headerlink" href="#id35" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Atomic operations will be disabled by default in a future release of rocBLAS (you can enable atomic
operations using the <code class="docutils literal notranslate"><span class="pre">rocblas_set_atomics_mode</span></code> function)</p></li>
</ul>
</section>
<section id="id36">
<h5>Removals<a class="headerlink" href="#id36" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rocblas_gemm_ext2</span></code> API function</p></li>
<li><p>In-place trmm API from Legacy BLAS is replaced by an API that supports both in-place and
out-of-place trmm</p></li>
<li><p>int8x4 support is removed (int8 support is unchanged)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">#define</span> <span class="pre">__STDC_WANT_IEC_60559_TYPES_EXT__</span></code> is removed from <code class="docutils literal notranslate"><span class="pre">rocblas-types.h</span></code> (if you want
ISO/IEC TS 18661-3:2015 functionality, you must define <code class="docutils literal notranslate"><span class="pre">__STDC_WANT_IEC_60559_TYPES_EXT__</span></code>
before including <code class="docutils literal notranslate"><span class="pre">float.h</span></code>, <code class="docutils literal notranslate"><span class="pre">math.h</span></code>, and <code class="docutils literal notranslate"><span class="pre">rocblas.h</span></code>)</p></li>
<li><p>The default build removes device code for gfx803 architecture from the fat binary</p></li>
</ul>
</section>
<section id="id37">
<h5>Fixes<a class="headerlink" href="#id37" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Made offset calculations for 64-bit rocBLAS functions safe</p>
<ul>
<li><p>Fixes for very large leading dimension or increment potentially causing overflow:</p>
<ul>
<li><p>Level2: <code class="docutils literal notranslate"><span class="pre">gbmv</span></code>, <code class="docutils literal notranslate"><span class="pre">gemv</span></code>, <code class="docutils literal notranslate"><span class="pre">hbmv</span></code>, <code class="docutils literal notranslate"><span class="pre">sbmv</span></code>, <code class="docutils literal notranslate"><span class="pre">spmv</span></code>, <code class="docutils literal notranslate"><span class="pre">tbmv</span></code>, <code class="docutils literal notranslate"><span class="pre">tpmv</span></code>, <code class="docutils literal notranslate"><span class="pre">tbsv</span></code>, and <code class="docutils literal notranslate"><span class="pre">tpsv</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p>Lazy loading supports heterogeneous architecture setup and load-appropriate tensile library files,
based on device architecture</p></li>
<li><p>Guards against no-op kernel launches that result in a potential <code class="docutils literal notranslate"><span class="pre">hipGetLastError</span></code></p></li>
</ul>
</section>
<section id="id38">
<h5>Changes<a class="headerlink" href="#id38" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Reduced the default verbosity of <code class="docutils literal notranslate"><span class="pre">rocblas-test</span></code> (you can see all tests by setting the
<code class="docutils literal notranslate"><span class="pre">GTEST_LISTENER=PASS_LINE_IN_LOG</span></code> environment variable)</p></li>
</ul>
</section>
</section>
<section id="rocfft-1-0-25">
<h4>rocFFT 1.0.25<a class="headerlink" href="#rocfft-1-0-25" title="Link to this heading">#</a></h4>
<p>rocFFT 1.0.25 for ROCm 6.0.0</p>
<section id="id39">
<h5>Additions<a class="headerlink" href="#id39" title="Link to this heading">#</a></h5>
<ul>
<li><p>Implemented experimental APIs to allow computing FFTs on data distributed across multiple devices
in a single process</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rocfft_field</span></code> is a new type that can be added to a plan description to describe the layout of FFT
input or output</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocfft_field_add_brick</span></code> can be called to describe the brick decomposition of an FFT field, where each
brick can be assigned a different device</p></li>
</ul>
<p>These interfaces are still experimental and subject to change. Your feedback is appreciated.
You can raise questions and concerns by opening issues in the
<a class="reference external" href="https://github.com/ROCmSoftwarePlatform/rocFFT/issues">rocFFT issue tracker</a>.</p>
<p>Note that multi-device FFTs currently have several limitations (we plan to address these in future
releases):</p>
<ul class="simple">
<li><p>Real-complex (forward or inverse) FFTs are not supported</p></li>
<li><p>Planar format fields are not supported</p></li>
<li><p>Batch (the <code class="docutils literal notranslate"><span class="pre">number_of_transforms</span></code> provided to <code class="docutils literal notranslate"><span class="pre">rocfft_plan_create</span></code>) must be 1</p></li>
<li><p>FFT input is gathered to the current device at run time, so all FFT data must fit on that device</p></li>
</ul>
</li>
</ul>
</section>
<section id="id40">
<h5>Optimizations<a class="headerlink" href="#id40" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved the performance of several 2D/3D real FFTs supported by <code class="docutils literal notranslate"><span class="pre">2D_SINGLE</span></code> kernel. Offline
tuning provides more optimization for fx90a</p></li>
<li><p>Removed an extra kernel launch from even-length, real-complex FFTs that use callbacks</p></li>
</ul>
</section>
<section id="id41">
<h5>Changes<a class="headerlink" href="#id41" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Built kernels in a solution map to the library kernel cache</p></li>
<li><p>Real forward transforms (real-to-complex) no longer overwrite input; rocFFT may still overwrite real
inverse (complex-to-real) input, as this allows for faster performance</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocfft-rider</span></code> and <code class="docutils literal notranslate"><span class="pre">dyna-rocfft-rider</span></code> have been renamed to <code class="docutils literal notranslate"><span class="pre">rocfft-bench</span></code> and <code class="docutils literal notranslate"><span class="pre">dyna-rocfft-bench</span></code>;
these are controlled by the <code class="docutils literal notranslate"><span class="pre">BUILD_CLIENTS_BENCH</span></code> CMake option</p>
<ul>
<li><p>Links for the former file names are installed, and the former <code class="docutils literal notranslate"><span class="pre">BUILD_CLIENTS_RIDER</span></code> CMake option
is accepted for compatibility, but both will be removed in a future release</p></li>
</ul>
</li>
<li><p>Binaries in debug builds no longer have a <code class="docutils literal notranslate"><span class="pre">-d</span></code> suffix</p></li>
</ul>
</section>
<section id="id42">
<h5>Fixes<a class="headerlink" href="#id42" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>rocFFT now correctly handles load callbacks that convert data from a smaller data type (e.g., 16-bit
integers -&gt; 32-bit float)</p></li>
</ul>
</section>
</section>
<section id="rocgdb-13-2">
<h4>ROCgdb 13.2<a class="headerlink" href="#rocgdb-13-2" title="Link to this heading">#</a></h4>
<p>ROCgdb 13.2 for ROCm 6.0.0</p>
<section id="id43">
<h5>Additions<a class="headerlink" href="#id43" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Support for watchpoints on scratch memory addresses.</p></li>
<li><p>Added support for gfx1100, gfx1101, and gfx1102.</p></li>
<li><p>Added support for gfx942.</p></li>
</ul>
</section>
<section id="id44">
<h5>Optimizations<a class="headerlink" href="#id44" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved performances when handling the end of a process with a large number of threads.</p></li>
</ul>
</section>
<section id="id45">
<h5>Known issues<a class="headerlink" href="#id45" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>On certain configurations, ROCgdb can show the following warning message:
<code class="docutils literal notranslate"><span class="pre">warning:</span> <span class="pre">Probes-based</span> <span class="pre">dynamic</span> <span class="pre">linker</span> <span class="pre">interface</span> <span class="pre">failed.</span> <span class="pre">Reverting</span> <span class="pre">to</span> <span class="pre">original</span> <span class="pre">interface.</span></code>
This does not affect ROCgdb’s functionalities.</p></li>
<li><p>ROCgdb cannot debug a program on an AMDGPU device past a
<code class="docutils literal notranslate"><span class="pre">s_sendmsg</span> <span class="pre">sendmsg(MSG_DEALLOC_VGPRS)</span></code> instruction. If an exception is reported after this
instruction has been executed (including asynchronous exceptions), the wave is killed and the
exceptions are only reported by the ROCm runtime.</p></li>
</ul>
</section>
</section>
<section id="rocm-cmake-0-11-0">
<h4>rocm-cmake 0.11.0<a class="headerlink" href="#rocm-cmake-0-11-0" title="Link to this heading">#</a></h4>
<p>rocm-cmake 0.11.0 for ROCm 6.0.0</p>
<section id="id46">
<h5>Changes<a class="headerlink" href="#id46" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved validation, documentation, and rocm-docs-core integration for ROCMSphinxDoc</p></li>
</ul>
</section>
<section id="id47">
<h5>Fixes<a class="headerlink" href="#id47" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed extra <code class="docutils literal notranslate"><span class="pre">make</span></code> flags passed for Clang-Tidy (ROCMClangTidy).</p></li>
<li><p>Fixed issues with ROCMTest when using a module in a subdirectory</p></li>
</ul>
</section>
</section>
<section id="rocm-compiler">
<h4>ROCm Compiler<a class="headerlink" href="#rocm-compiler" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>On MI300, kernel arguments can be preloaded into SGPRs rather than passed in memory. This
feature is enabled with a compiler option, which also controls the number of arguments to pass in
SGPRs.</p></li>
<li><p>Improved register allocation at -O0: Avoid compiler crashes ( ‘ran out of registers during register allocation’ )</p></li>
<li><p>Improved generation of debug information:</p>
<ul>
<li><p>Improve compile time</p></li>
<li><p>Avoid compiler crashes</p></li>
</ul>
</li>
</ul>
</section>
<section id="rocprim-3-0-0">
<h4>rocPRIM 3.0.0<a class="headerlink" href="#rocprim-3-0-0" title="Link to this heading">#</a></h4>
<p>rocPRIM 3.0.0 for ROCm 6.0.0</p>
<section id="id48">
<h5>Additions<a class="headerlink" href="#id48" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">block_sort::sort()</span></code> overload for keys and values with a dynamic size, for all block sort algorithms</p></li>
<li><p>All <code class="docutils literal notranslate"><span class="pre">block_sort::sort()</span></code> overloads with a dynamic size are now supported for
<code class="docutils literal notranslate"><span class="pre">block_sort_algorithm::merge_sort</span></code> and <code class="docutils literal notranslate"><span class="pre">block_sort_algorithm::bitonic_sort</span></code></p></li>
<li><p>New two-way partition primitive <code class="docutils literal notranslate"><span class="pre">partition_two_way</span></code>, which can write to two separate iterators</p></li>
</ul>
</section>
<section id="id49">
<h5>Optimizations<a class="headerlink" href="#id49" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved <code class="docutils literal notranslate"><span class="pre">partition</span></code> performance</p></li>
</ul>
</section>
<section id="id50">
<h5>Fixes<a class="headerlink" href="#id50" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed <code class="docutils literal notranslate"><span class="pre">rocprim::MatchAny</span></code> for devices with 64-bit warp size</p>
<ul>
<li><p>Note that <code class="docutils literal notranslate"><span class="pre">rocprim::MatchAny</span></code> is deprecated; use <code class="docutils literal notranslate"><span class="pre">rocprim::match_any</span></code> instead</p></li>
</ul>
</li>
</ul>
</section>
</section>
<section id="roc-profiler-2-0-0">
<h4>Roc Profiler 2.0.0<a class="headerlink" href="#roc-profiler-2-0-0" title="Link to this heading">#</a></h4>
<p>Roc Profiler 2.0.0 for ROCm 6.0.0</p>
<section id="id51">
<h5>Additions<a class="headerlink" href="#id51" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Updated supported GPU architectures in README with profiler versions</p></li>
<li><p>Automatic ISA dumping for ATT. See README.</p></li>
<li><p>CSV mode for ATT. See README.</p></li>
<li><p>Added option to control kernel name truncation.</p></li>
<li><p>Limit rocprof(v1) script usage to only supported architectures.</p></li>
<li><p>Added Tool versioning to be able to run rocprofv2 using rocprof. See README for more information.</p></li>
<li><p>Added Plugin Versioning way in rocprofv2. See README for more details.</p></li>
<li><p>Added <code class="docutils literal notranslate"><span class="pre">--version</span></code> in rocprof and rocprofv2 to be able to see the current rocprof/v2 version along with ROCm version information.</p></li>
</ul>
</section>
</section>
<section id="rocrand-2-10-17">
<h4>rocRAND 2.10.17<a class="headerlink" href="#rocrand-2-10-17" title="Link to this heading">#</a></h4>
<p>rocRAND 2.10.17 for ROCm 6.0.0</p>
</section>
</section>
<section id="id52">
<h3>Changes<a class="headerlink" href="#id52" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p>Generator classes from <code class="docutils literal notranslate"><span class="pre">rocrand.hpp</span></code> are no longer copyable (in previous versions these copies
would copy internal references to the generators and would lead to double free or memory leak
errors)</p>
<ul>
<li><p>These types should be moved instead of copied; move constructors and operators are now
defined</p></li>
</ul>
</li>
</ul>
</section>
<section id="id53">
<h3>Optimizations<a class="headerlink" href="#id53" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p>Improved MT19937 initialization and generation performance</p></li>
</ul>
</section>
<section id="id54">
<h3>Removals<a class="headerlink" href="#id54" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p>Removed the hipRAND submodule from rocRAND; hipRAND is now only available as a separate
package</p></li>
<li><p>Removed references to, and workarounds for, the deprecated hcc</p></li>
</ul>
</section>
<section id="id55">
<h3>Fixes<a class="headerlink" href="#id55" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mt19937_engine</span></code> from <code class="docutils literal notranslate"><span class="pre">rocrand.hpp</span></code> is now move-constructible and move-assignable (the move
constructor and move assignment operator was deleted for this class)</p></li>
<li><p>Various fixes for the C++ wrapper header <code class="docutils literal notranslate"><span class="pre">rocrand.hpp</span></code></p>
<ul>
<li><p>The name of <code class="docutils literal notranslate"><span class="pre">mrg31k3p</span></code> it is now correctly spelled (was incorrectly named <code class="docutils literal notranslate"><span class="pre">mrg31k3a</span></code> in previous
versions)</p></li>
<li><p>Added the missing <code class="docutils literal notranslate"><span class="pre">order</span></code> setter method for <code class="docutils literal notranslate"><span class="pre">threefry4x64</span></code></p></li>
<li><p>Fixed the default ordering parameter for <code class="docutils literal notranslate"><span class="pre">lfsr113</span></code></p></li>
</ul>
</li>
<li><p>Build error when using Clang++ directly resulting from unsupported <code class="docutils literal notranslate"><span class="pre">amdgpu-target</span></code> references</p></li>
</ul>
<section id="rocsolver-3-24-0">
<h4>rocSOLVER 3.24.0<a class="headerlink" href="#rocsolver-3-24-0" title="Link to this heading">#</a></h4>
<p>rocSOLVER 3.24.0 for ROCm 6.0.0</p>
<section id="id56">
<h5>Additions<a class="headerlink" href="#id56" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Cholesky refactorization for sparse matrices: <code class="docutils literal notranslate"><span class="pre">CSRRF_REFACTCHOL</span></code></p></li>
<li><p>Added <code class="docutils literal notranslate"><span class="pre">rocsolver_rfinfo_mode</span></code> and the ability to specify the desired refactorization routine (see <code class="docutils literal notranslate"><span class="pre">rocsolver_set_rfinfo_mode</span></code>)</p></li>
</ul>
</section>
<section id="id57">
<h5>Changes<a class="headerlink" href="#id57" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">CSRRF_ANALYSIS</span></code> and <code class="docutils literal notranslate"><span class="pre">CSRRF_SOLVE</span></code> now support sparse Cholesky factorization</p></li>
</ul>
</section>
</section>
<section id="rocsparse-3-0-2">
<h4>rocSPARSE 3.0.2<a class="headerlink" href="#rocsparse-3-0-2" title="Link to this heading">#</a></h4>
<p>rocSPARSE 3.0.2 for ROCm 6.0.0</p>
<section id="id58">
<h5>Changes<a class="headerlink" href="#id58" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Function arguments for <code class="docutils literal notranslate"><span class="pre">rocsparse_spmv</span></code></p></li>
<li><p>Function arguments for <code class="docutils literal notranslate"><span class="pre">rocsparse_xbsrmv</span></code> routines</p></li>
<li><p>When using host pointer mode, you must now call <code class="docutils literal notranslate"><span class="pre">hipStreamSynchronize</span></code> following <code class="docutils literal notranslate"><span class="pre">doti</span></code>, <code class="docutils literal notranslate"><span class="pre">dotci</span></code>,
<code class="docutils literal notranslate"><span class="pre">spvv</span></code>, and <code class="docutils literal notranslate"><span class="pre">csr2ell</span></code></p></li>
<li><p>Improved documentation</p></li>
<li><p>Improved verbose output during argument checking on API function calls</p></li>
</ul>
</section>
<section id="id59">
<h5>Removals<a class="headerlink" href="#id59" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Auto stages from <code class="docutils literal notranslate"><span class="pre">spmv</span></code>, <code class="docutils literal notranslate"><span class="pre">spmm</span></code>, <code class="docutils literal notranslate"><span class="pre">spgemm</span></code>, <code class="docutils literal notranslate"><span class="pre">spsv</span></code>, <code class="docutils literal notranslate"><span class="pre">spsm</span></code>, and <code class="docutils literal notranslate"><span class="pre">spitsv</span></code></p></li>
<li><p>Formerly deprecated <code class="docutils literal notranslate"><span class="pre">rocsparse_spmm_ex</span></code> routine</p></li>
</ul>
</section>
</section>
</section>
<section id="id60">
<h3>Fixes<a class="headerlink" href="#id60" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p>Bug in <code class="docutils literal notranslate"><span class="pre">rocsparse-bench</span></code> where the SpMV algorithm was not taken into account in CSR format</p></li>
<li><p>BSR and GEBSR routines (<code class="docutils literal notranslate"><span class="pre">bsrmv</span></code>, <code class="docutils literal notranslate"><span class="pre">bsrsv</span></code>, <code class="docutils literal notranslate"><span class="pre">bsrmm</span></code>, <code class="docutils literal notranslate"><span class="pre">bsrgeam</span></code>, <code class="docutils literal notranslate"><span class="pre">gebsrmv</span></code>, <code class="docutils literal notranslate"><span class="pre">gebsrmm</span></code>) didn’t always
show <code class="docutils literal notranslate"><span class="pre">block_dim==0</span></code> as an invalid size</p></li>
<li><p>Passing <code class="docutils literal notranslate"><span class="pre">nnz</span> <span class="pre">=</span> <span class="pre">0</span></code> to <code class="docutils literal notranslate"><span class="pre">doti</span></code> or <code class="docutils literal notranslate"><span class="pre">dotci</span></code> wasn’t always returning a dot product of 0</p></li>
</ul>
</section>
<section id="id61">
<h3>Additions<a class="headerlink" href="#id61" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rocsparse_inverse_permutation</span></code></p></li>
<li><p>Mixed-precisions for SpVV</p></li>
<li><p>Uniform int8 precision for gather and scatter</p></li>
</ul>
<section id="rocthrust-3-0-0">
<h4>rocThrust 3.0.0<a class="headerlink" href="#rocthrust-3-0-0" title="Link to this heading">#</a></h4>
<p>rocThrust 3.0.0 for ROCm 6.0.0</p>
<section id="id62">
<h5>Additions<a class="headerlink" href="#id62" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Updated to match upstream Thrust 2.0.1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">NV_IF_TARGET</span></code> macro from libcu++ for NVIDIA backend and HIP implementation for HIP backend</p></li>
</ul>
</section>
<section id="id63">
<h5>Changes<a class="headerlink" href="#id63" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The CMake build system now accepts <code class="docutils literal notranslate"><span class="pre">GPU_TARGETS</span></code> in addition to <code class="docutils literal notranslate"><span class="pre">AMDGPU_TARGETS</span></code> for
setting targeted GPU architectures</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_TARGETS=all</span></code> compiles for all supported architectures</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">AMDGPU_TARGETS</span></code> is only provided for backwards compatibility (<code class="docutils literal notranslate"><span class="pre">GPU_TARGETS</span></code> is preferred)</p></li>
</ul>
</li>
<li><p>Removed CUB symlink from the root of the repository</p></li>
<li><p>Removed support for deprecated macros (<code class="docutils literal notranslate"><span class="pre">THRUST_DEVICE_BACKEND</span></code> and
<code class="docutils literal notranslate"><span class="pre">THRUST_HOST_BACKEND</span></code>)</p></li>
</ul>
</section>
<section id="id64">
<h5>Known issues<a class="headerlink" href="#id64" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The <code class="docutils literal notranslate"><span class="pre">THRUST_HAS_CUDART</span></code> macro, which is no longer used in Thrust (it’s provided only for legacy
support) is replaced with <code class="docutils literal notranslate"><span class="pre">NV_IF_TARGET</span></code> and <code class="docutils literal notranslate"><span class="pre">THRUST_RDC_ENABLED</span></code> in the NVIDIA backend. The
HIP backend doesn’t have a <code class="docutils literal notranslate"><span class="pre">THRUST_RDC_ENABLED</span></code> macro, so some branches in Thrust code may
be unreachable in the HIP backend.</p></li>
</ul>
</section>
</section>
<section id="rocwmma-1-3-0">
<h4>rocWMMA 1.3.0<a class="headerlink" href="#rocwmma-1-3-0" title="Link to this heading">#</a></h4>
<p>rocWMMA 1.3.0 for ROCm 6.0.0</p>
<section id="id65">
<h5>Additions<a class="headerlink" href="#id65" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Support for gfx942</p></li>
<li><p>Support for f8, bf8, and xfloat32 data types</p></li>
<li><p>support for <code class="docutils literal notranslate"><span class="pre">HIP_NO_HALF</span></code>, <code class="docutils literal notranslate"><span class="pre">__</span> <span class="pre">HIP_NO_HALF_CONVERSIONS__</span></code>, and
<code class="docutils literal notranslate"><span class="pre">__</span> <span class="pre">HIP_NO_HALF_OPERATORS__</span></code> (e.g., PyTorch environment)</p></li>
</ul>
</section>
<section id="id66">
<h5>Changes<a class="headerlink" href="#id66" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>rocWMMA with hipRTC now supports <code class="docutils literal notranslate"><span class="pre">bfloat16_t</span></code> data type</p></li>
<li><p>gfx11 WMMA now uses lane swap instead of broadcast for layout adjustment</p></li>
<li><p>Updated samples GEMM parameter validation on host arch</p></li>
</ul>
</section>
<section id="id67">
<h5>Fixes<a class="headerlink" href="#id67" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Disabled GoogleTest static library deployment</p></li>
<li><p>Extended tests now build in large code model</p></li>
</ul>
</section>
</section>
<section id="tensile-4-39-0">
<h4>Tensile 4.39.0<a class="headerlink" href="#tensile-4-39-0" title="Link to this heading">#</a></h4>
<p>Tensile 4.39.0 for ROCm 6.0.0</p>
<section id="id68">
<h5>Additions<a class="headerlink" href="#id68" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added <code class="docutils literal notranslate"><span class="pre">aquavanjaram</span></code> support: gfx942, fp8/bf8 datatype, xf32 datatype, and
stochastic rounding for various datatypes</p></li>
<li><p>Added and updated tuning scripts</p></li>
<li><p>Added <code class="docutils literal notranslate"><span class="pre">DirectToLds</span></code> support for larger data types with 32-bit global load (old parameter <code class="docutils literal notranslate"><span class="pre">DirectToLds</span></code>
is replaced with <code class="docutils literal notranslate"><span class="pre">DirectToLdsA</span></code> and <code class="docutils literal notranslate"><span class="pre">DirectToLdsB</span></code>), and the corresponding test cases</p></li>
<li><p>Added the average of frequency, power consumption, and temperature information for the winner
kernels to the CSV file</p></li>
<li><p>Added asmcap check for MFMA + const src</p></li>
<li><p>Added support for wider local read + pack with v_perm (with <code class="docutils literal notranslate"><span class="pre">VgprForLocalReadPacking=True</span></code>)</p></li>
<li><p>Added a new parameter to increase <code class="docutils literal notranslate"><span class="pre">miLatencyLeft</span></code></p></li>
</ul>
</section>
<section id="id69">
<h5>Optimizations<a class="headerlink" href="#id69" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Enabled <code class="docutils literal notranslate"><span class="pre">InitAccVgprOpt</span></code> for <code class="docutils literal notranslate"><span class="pre">MatrixInstruction</span></code> cases</p></li>
<li><p>Implemented local read related parameter calculations with <code class="docutils literal notranslate"><span class="pre">DirectToVgpr</span></code></p></li>
<li><p>Enabled dedicated vgpr allocation for local read + pack</p></li>
<li><p>Optimized code initialization</p></li>
<li><p>Optimized sgpr allocation</p></li>
<li><p>Supported DGEMM TLUB + RLVW=2 for odd N (edge shift change)</p></li>
<li><p>Enabled <code class="docutils literal notranslate"><span class="pre">miLatency</span></code> optimization for specific data types, and fixed
instruction scheduling</p></li>
</ul>
</section>
<section id="id70">
<h5>Changes<a class="headerlink" href="#id70" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed old code for DTL + (bpe * GlobalReadVectorWidth &gt; 4)</p></li>
<li><p>Changed/updated failed CI tests for gfx11xx, InitAccVgprOpt, and DTLds</p></li>
<li><p>Removed unused <code class="docutils literal notranslate"><span class="pre">CustomKernels</span></code> and <code class="docutils literal notranslate"><span class="pre">ReplacementKernels</span></code></p></li>
<li><p>Added a reject condition for DTVB + TransposeLDS=False (not supported so far)</p></li>
<li><p>Removed unused code for DirectToLds</p></li>
<li><p>Updated test cases for DTV + TransposeLDS=False</p></li>
<li><p>Moved the <code class="docutils literal notranslate"><span class="pre">MinKForGSU</span></code> parameter from <code class="docutils literal notranslate"><span class="pre">globalparameter</span></code> to <code class="docutils literal notranslate"><span class="pre">BenchmarkCommonParameter</span></code> to
support smaller K</p></li>
<li><p>Changed how to calculate <code class="docutils literal notranslate"><span class="pre">latencyForLR</span></code> for miLatency</p></li>
<li><p>Set minimum value of <code class="docutils literal notranslate"><span class="pre">latencyForLRCount</span></code> for 1LDSBuffer to avoid getting rejected by
overflowedResources=5 (related to miLatency)</p></li>
<li><p>Refactored allowLRVWBforTLUandMI and renamed it as VectorWidthB</p></li>
<li><p>Supported multi-gpu for different architectures in lazy library loading</p></li>
<li><p>Enabled dtree library for batch &gt; 1</p></li>
<li><p>Added problem scale feature for dtree selection</p></li>
<li><p>Modified non-lazy load build to skip experimental logic</p></li>
</ul>
</section>
<section id="id71">
<h5>Fixes<a class="headerlink" href="#id71" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Predicate ordering for fp16alt impl round near zero mode to unbreak distance modes</p></li>
<li><p>Boundary check for mirror dims and re-enable disabled mirror dims test cases</p></li>
<li><p>Merge error affecting i8 with WMMA</p></li>
<li><p>Mismatch issue with DTLds + TSGR + TailLoop</p></li>
<li><p>Bug with <code class="docutils literal notranslate"><span class="pre">InitAccVgprOpt</span></code> + GSU&gt;1 and a mismatch issue with PGR=0</p></li>
<li><p>Override for unloaded solutions when lazy loading</p></li>
<li><p>Adding missing headers</p></li>
<li><p>Boost link for a clean build on Ubuntu 22</p></li>
<li><p>Bug in <code class="docutils literal notranslate"><span class="pre">forcestoresc1</span></code> arch selection</p></li>
<li><p>Compiler directive for gfx942</p></li>
<li><p>Formatting for <code class="docutils literal notranslate"><span class="pre">DecisionTree_test.cpp</span></code></p></li>
</ul>
</section>
</section>
</section>
<section id="library-changes-in-rocm-6-0-0">
<h3>Library changes in ROCM 6.0.0<a class="headerlink" href="#library-changes-in-rocm-6-0-0" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>AMDMIGraphX</p></td>
<td><p>2.7 ⇒ <a class="reference external" href="https://github.com/ROCm/AMDMIGraphX/releases/tag/rocm-6.0.0">2.8</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipBLAS</p></td>
<td><p>1.1.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-6.0.0">2.0.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipCUB</p></td>
<td><p>2.13.1 ⇒ <a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-6.0.0">3.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipFFT</p></td>
<td><p>1.0.12 ⇒ <a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-6.0.0">1.0.13</a></p></td>
</tr>
<tr class="row-even"><td><p>hipRAND</p></td>
<td><p>2.10.16 ⇒ <a class="reference external" href="https://github.com/ROCm/hipRAND/releases/tag/rocm-6.0.0">2.10.17</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p>1.8.2 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-6.0.0">2.0.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p>2.3.8 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-6.0.0">3.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipTensor</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/hipTensor/releases/tag/rocm-6.0.0">1.1.0</a></p></td>
</tr>
<tr class="row-even"><td><p>MIOpen</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/MIOpen/releases/tag/rocm-6.0.0">2.19.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-6.0.0">2.15.5</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p>2.1.11 ⇒ <a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-6.0.0">3.0.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p>3.1.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-6.0.0">4.0.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p>1.0.24 ⇒ <a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-6.0.0">1.0.25</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocm-cmake</p></td>
<td><p>0.10.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-6.0.0">0.11.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p>2.13.1 ⇒ <a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-6.0.0">3.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-6.0.0">2.10.17</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p>3.23.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-6.0.0">3.24.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p>2.5.4 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-6.0.0">3.0.2</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p>2.18.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-6.0.0">3.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocWMMA</p></td>
<td><p>1.2.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-6.0.0">1.3.0</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p>4.38.0 ⇒ <a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-6.0.0">4.39.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="id72">
<h4>AMDMIGraphX 2.8<a class="headerlink" href="#id72" title="Link to this heading">#</a></h4>
<p>MIGraphX 2.8 for ROCm 6.0.0</p>
<section id="id73">
<h5>Additions<a class="headerlink" href="#id73" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Support for MI300 GPUs</p></li>
<li><p>Support for TorchMIGraphX via PyTorch</p></li>
<li><p>Boosted overall performance by integrating rocMLIR</p></li>
<li><p>INT8 support for ONNX Runtime</p></li>
<li><p>Support for ONNX version 1.14.1</p></li>
<li><p>Added new operators: <code class="docutils literal notranslate"><span class="pre">Qlinearadd</span></code>, <code class="docutils literal notranslate"><span class="pre">QlinearGlobalAveragePool</span></code>, <code class="docutils literal notranslate"><span class="pre">Qlinearconv</span></code>, <code class="docutils literal notranslate"><span class="pre">Shrink</span></code>, <code class="docutils literal notranslate"><span class="pre">CastLike</span></code>,
and <code class="docutils literal notranslate"><span class="pre">RandomUniform</span></code></p></li>
<li><p>Added an error message for when <code class="docutils literal notranslate"><span class="pre">gpu_targets</span></code> is not set during MIGraphX compilation</p></li>
<li><p>Added parameter to set tolerances with <code class="docutils literal notranslate"><span class="pre">migraphx-driver</span></code> verify</p></li>
<li><p>Added support for MXR files &gt; 4 GB</p></li>
<li><p>Added <code class="docutils literal notranslate"><span class="pre">MIGRAPHX_TRACE_MLIR</span></code> flag</p></li>
<li><p>BETA added capability for using ROCm Composable Kernels via the <code class="docutils literal notranslate"><span class="pre">MIGRAPHX_ENABLE_CK=1</span></code>
environment variable</p></li>
</ul>
</section>
<section id="id74">
<h5>Optimizations<a class="headerlink" href="#id74" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved performance support for INT8</p></li>
<li><p>Improved time precision while benchmarking candidate kernels from CK or MLIR</p></li>
<li><p>Removed contiguous from reshape parsing</p></li>
<li><p>Updated the <code class="docutils literal notranslate"><span class="pre">ConstantOfShape</span></code> operator to support Dynamic Batch</p></li>
<li><p>Simplified dynamic shapes-related operators to their static versions, where possible</p></li>
<li><p>Improved debugging tools for accuracy issues</p></li>
<li><p>Included a print warning about <code class="docutils literal notranslate"><span class="pre">miopen_fusion</span></code> while generating <code class="docutils literal notranslate"><span class="pre">mxr</span></code></p></li>
<li><p>General reduction in system memory usage during model compilation</p></li>
<li><p>Created additional fusion opportunities during model compilation</p></li>
<li><p>Improved debugging for matchers</p></li>
<li><p>Improved general debug messages</p></li>
</ul>
</section>
<section id="id75">
<h5>Fixes<a class="headerlink" href="#id75" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed scatter operator for nonstandard shapes with some models from ONNX Model Zoo</p></li>
<li><p>Provided a compile option to improve the accuracy of some models by disabling Fast-Math</p></li>
<li><p>Improved layernorm + pointwise fusion matching to ignore argument order</p></li>
<li><p>Fixed accuracy issue with <code class="docutils literal notranslate"><span class="pre">ROIAlign</span></code> operator</p></li>
<li><p>Fixed computation logic for the <code class="docutils literal notranslate"><span class="pre">Trilu</span></code> operator</p></li>
<li><p>Fixed support for the DETR model</p></li>
</ul>
</section>
<section id="id76">
<h5>Changes<a class="headerlink" href="#id76" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Changed MIGraphX version to 2.8</p></li>
<li><p>Extracted the test packages into a separate deb file when building MIGraphX from source</p></li>
</ul>
</section>
<section id="id77">
<h5>Removals<a class="headerlink" href="#id77" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed building Python 2.7 bindings</p></li>
</ul>
</section>
</section>
<section id="id78">
<h4>hipBLAS 2.0.0<a class="headerlink" href="#id78" title="Link to this heading">#</a></h4>
<p>hipBLAS 2.0.0 for ROCm 6.0.0</p>
<section id="added">
<h5>Added<a class="headerlink" href="#added" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>added option to define HIPBLAS_USE_HIP_BFLOAT16 to switch API to use hip_bfloat16 type</p></li>
<li><p>added hipblasGemmExWithFlags API</p></li>
</ul>
</section>
<section id="deprecated">
<h5>Deprecated<a class="headerlink" href="#deprecated" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>hipblasDatatype_t is deprecated and will be removed in a future release and replaced with hipDataType</p></li>
<li><p>hipblasComplex and hipblasDoubleComplex are deprecated and will be removed in a future release and replaced with hipComplex and hipDoubleComplex</p></li>
<li><p>use of hipblasDatatype_t for hipblasGemmEx for compute-type is deprecated and will be replaced with hipblasComputeType_t in a future release</p></li>
</ul>
</section>
<section id="removed">
<h5>Removed<a class="headerlink" href="#removed" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>hipblasXtrmm that calculates B &lt;- alpha * op(A) * B is removed and replaced with hipblasXtrmm that calculates C &lt;- alpha * op(A) * B</p></li>
</ul>
</section>
</section>
<section id="id79">
<h4>hipCUB 3.0.0<a class="headerlink" href="#id79" title="Link to this heading">#</a></h4>
<p>hipCUB 3.0.0 for ROCm 6.0.0</p>
<section id="changed">
<h5>Changed<a class="headerlink" href="#changed" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed <code class="docutils literal notranslate"><span class="pre">DOWNLOAD_ROCPRIM</span></code>, forcing rocPRIM to download can be done with <code class="docutils literal notranslate"><span class="pre">DEPENDENCIES_FORCE_DOWNLOAD</span></code>.</p></li>
</ul>
</section>
</section>
<section id="id80">
<h4>hipFFT 1.0.13<a class="headerlink" href="#id80" title="Link to this heading">#</a></h4>
<p>hipFFT 1.0.13 for ROCm 6.0.0</p>
<section id="id81">
<h5>Changed<a class="headerlink" href="#id81" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>hipfft-rider has been renamed to hipfft-bench, controlled by the BUILD_CLIENTS_BENCH CMake option.  A link for the
old file name is installed, and the old BUILD_CLIENTS_RIDER CMake option is accepted for compatibility but both
will be removed in a future release.</p></li>
<li><p>Binaries in debug builds no longer have a “-d” suffix.</p></li>
<li><p>The minimum rocFFT required version has been updated to 1.0.21.</p></li>
</ul>
</section>
<section id="id82">
<h5>Added<a class="headerlink" href="#id82" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Implemented hipfftXtSetGPUs, hipfftXtMalloc, hipfftXtMemcpy, hipfftXtFree, hipfftXtExecDescriptor APIs to allow computing FFTs on multiple devices in a single process.</p></li>
</ul>
</section>
</section>
<section id="hiprand-2-10-17">
<h4>hipRAND 2.10.17<a class="headerlink" href="#hiprand-2-10-17" title="Link to this heading">#</a></h4>
<p>hipRAND 2.10.17 for ROCm 6.0.0</p>
<section id="fixed">
<h5>Fixed<a class="headerlink" href="#fixed" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed benchmark and unit test builds on Windows.</p></li>
</ul>
</section>
</section>
<section id="id83">
<h4>hipSOLVER 2.0.0<a class="headerlink" href="#id83" title="Link to this heading">#</a></h4>
<p>hipSOLVER 2.0.0 for ROCm 6.0.0</p>
<section id="id84">
<h5>Added<a class="headerlink" href="#id84" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added hipBLAS as an optional dependency to hipsolver-test. Use the <code class="docutils literal notranslate"><span class="pre">BUILD_HIPBLAS_TESTS</span></code> CMake option to test compatibility between hipSOLVER and hipBLAS.</p></li>
</ul>
</section>
<section id="id85">
<h5>Changed<a class="headerlink" href="#id85" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Types hipsolverOperation_t, hipsolverFillMode_t, and hipsolverSideMode_t are now aliases of hipblasOperation_t, hipblasFillMode_t, and hipblasSideMode_t.</p></li>
</ul>
</section>
<section id="id86">
<h5>Fixed<a class="headerlink" href="#id86" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed tests for hipsolver info updates in ORGBR/UNGBR, ORGQR/UNGQR,
ORGTR/UNGTR, ORMQR/UNMQR, and ORMTR/UNMTR.</p></li>
</ul>
</section>
</section>
<section id="id87">
<h4>hipSPARSE 3.0.0<a class="headerlink" href="#id87" title="Link to this heading">#</a></h4>
<p>hipSPARSE 3.0.0 for ROCm 6.0.0</p>
<section id="id88">
<h5>Added<a class="headerlink" href="#id88" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added hipsparseGetErrorName and hipsparseGetErrorString</p></li>
</ul>
</section>
<section id="id89">
<h5>Changed<a class="headerlink" href="#id89" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Changed hipsparseSpSV_solve() API function to match cusparse API</p></li>
<li><p>Changed generic API functions to use const descriptors</p></li>
<li><p>Documentation improved</p></li>
</ul>
</section>
</section>
<section id="id90">
<h4>hipTensor 1.1.0<a class="headerlink" href="#id90" title="Link to this heading">#</a></h4>
<p>hipTensor 1.1.0 for ROCm 6.0.0</p>
<section id="id91">
<h5>Additions<a class="headerlink" href="#id91" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Architecture support for gfx940, gfx941, and gfx942</p></li>
<li><p>Client tests configuration parameters now support YAML file input format</p></li>
</ul>
</section>
<section id="id92">
<h5>Changes<a class="headerlink" href="#id92" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Doxygen now treats warnings as errors</p></li>
</ul>
</section>
<section id="id93">
<h5>Fixes<a class="headerlink" href="#id93" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Client tests output redirections now behave accordingly</p></li>
<li><p>Removed dependency static library deployment</p></li>
<li><p>Security issues for documentation</p></li>
<li><p>Compile issues in debug mode</p></li>
<li><p>Corrected soft link for ROCm deployment</p></li>
</ul>
</section>
</section>
<section id="id94">
<h4>rocALUTION 3.0.3<a class="headerlink" href="#id94" title="Link to this heading">#</a></h4>
<p>rocALUTION 3.0.3 for ROCm 6.0.0</p>
<section id="id95">
<h5>Added<a class="headerlink" href="#id95" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added support for 64bit integer vectors</p></li>
<li><p>Added inclusive and exclusive sum functionality for Vector classes</p></li>
<li><p>Added Transpose functionality for Global/LocalMatrix</p></li>
<li><p>Added TripleMatrixProduct functionality LocalMatrix</p></li>
<li><p>Added Sort() function for LocalVector class</p></li>
<li><p>Added multiple stream support to the HIP backend</p></li>
</ul>
</section>
<section id="optimized">
<h5>Optimized<a class="headerlink" href="#optimized" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>GlobalMatrix::Apply() now uses multiple streams to better hide communication</p></li>
</ul>
</section>
<section id="id96">
<h5>Changed<a class="headerlink" href="#id96" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Matrix dimensions and number of non-zeros are now stored using 64bit integers</p></li>
<li><p>Improved ILUT preconditioner</p></li>
</ul>
</section>
<section id="id97">
<h5>Removed<a class="headerlink" href="#id97" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed LocalVector::GetIndexValues(ValueType*)</p></li>
<li><p>Removed LocalVector::SetIndexValues(const ValueType*)</p></li>
<li><p>Removed LocalMatrix::RSDirectInterpolation(const LocalVector&amp;, const LocalVector&amp;, LocalMatrix*, LocalMatrix*)</p></li>
<li><p>Removed LocalMatrix::RSExtPIInterpolation(const LocalVector&amp;, const LocalVector&amp;, bool, float, LocalMatrix*, LocalMatrix*)</p></li>
<li><p>Removed LocalMatrix::RugeStueben()</p></li>
<li><p>Removed LocalMatrix::AMGSmoothedAggregation(ValueType, const LocalVector&amp;, const LocalVector&amp;, LocalMatrix*, LocalMatrix*, int)</p></li>
<li><p>Removed LocalMatrix::AMGAggregation(const LocalVector&amp;, LocalMatrix*, LocalMatrix*)</p></li>
</ul>
</section>
<section id="id98">
<h5>Fixed<a class="headerlink" href="#id98" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Unit tests do not ignore BCSR block dimension anymore</p></li>
<li><p>Fixed typos in the documentation</p></li>
<li><p>Fixed a bug in multicoloring for non-symmetric matrix patterns</p></li>
</ul>
</section>
</section>
<section id="id99">
<h4>rocBLAS 4.0.0<a class="headerlink" href="#id99" title="Link to this heading">#</a></h4>
<p>rocBLAS 4.0.0 for ROCm 6.0.0</p>
<section id="id100">
<h5>Added<a class="headerlink" href="#id100" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Addition of beta API rocblas_gemm_batched_ex3 and rocblas_gemm_strided_batched_ex3</p></li>
<li><p>Added input/output type f16_r/bf16_r and execution type f32_r support for Level 2 gemv_batched and gemv_strided_batched</p></li>
<li><p>Added rocblas_status_excluded_from_build to be used when calling functions which require Tensile when using rocBLAS built without Tensile</p></li>
<li><p>Added system for async kernel launches setting a failure rocblas_status based on hipPeekAtLastError discrepancy</p></li>
</ul>
</section>
<section id="id101">
<h5>Optimized<a class="headerlink" href="#id101" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Trsm performance for small sizes m &lt; 32 &amp;&amp; n &lt; 32</p></li>
</ul>
</section>
<section id="id102">
<h5>Deprecated<a class="headerlink" href="#id102" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>In a future release atomic operations will be disabled by default so results will be repeatable. Atomic operations can always be enabled or disabled using the function rocblas_set_atomics_mode. Enabling atomic operations can improve performance.</p></li>
</ul>
</section>
<section id="id103">
<h5>Removed<a class="headerlink" href="#id103" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>rocblas_gemm_ext2 API function is removed</p></li>
<li><p>in-place trmm API from Legacy BLAS is removed. It is replaced by an API that supports both in-place and out-of-place trmm</p></li>
<li><p>int8x4 support is removed. int8 support is unchanged</p></li>
<li><p>The #define STDC_WANT_IEC_60559_TYPES_EXT has been removed from rocblas-types.h. Users who want ISO/IEC TS 18661-3:2015 functionality must define STDC_WANT_IEC_60559_TYPES_EXT before including float.h, math.h, and rocblas.h</p></li>
<li><p>The default build removes device code for gfx803 architecture from the fat binary</p></li>
</ul>
</section>
<section id="id104">
<h5>Fixed<a class="headerlink" href="#id104" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Make offset calculations for rocBLAS functions 64 bit safe. Fixes for very large leading dimension or increment potentially causing overflow:</p>
<ul>
<li><p>Level2: gbmv, gemv, hbmv, sbmv, spmv, tbmv, tpmv, tbsv, tpsv</p></li>
</ul>
</li>
<li><p>Lazy loading to support heterogeneous architecture setup and load appropriate tensile library files based on the device’s architecture</p></li>
<li><p>Guard against no-op kernel launches resulting in potential hipGetLastError</p></li>
</ul>
</section>
<section id="id105">
<h5>Changed<a class="headerlink" href="#id105" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Default verbosity of rocblas-test reduced. To see all tests set environment variable GTEST_LISTENER=PASS_LINE_IN_LOG</p></li>
</ul>
</section>
</section>
<section id="id106">
<h4>rocFFT 1.0.25<a class="headerlink" href="#id106" title="Link to this heading">#</a></h4>
<p>rocFFT 1.0.25 for ROCm 6.0.0</p>
<section id="id107">
<h5>Added<a class="headerlink" href="#id107" title="Link to this heading">#</a></h5>
<ul>
<li><p>Implemented experimental APIs to allow computing FFTs on data distributed across multiple devices in a single process.</p>
<p><code class="docutils literal notranslate"><span class="pre">rocfft_field</span></code> is a new type that can be added to a plan description, to describe layout of FFT input or output.  <code class="docutils literal notranslate"><span class="pre">rocfft_field_add_brick</span></code> can be called one or more times to describe a brick decomposition of an FFT field, where each brick can be assigned a different device.</p>
<p>These interfaces are still experimental and subject to change.  We are interested to hear feedback on them.  Questions and concerns may be raised by opening issues on the <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/rocFFT/issues">rocFFT issue tracker</a>.</p>
<p>Note that at this time, multi-device FFTs have several limitations:</p>
<ul class="simple">
<li><p>Real-complex (forward or inverse) FFTs are not currently supported.</p></li>
<li><p>Planar format fields are not currently supported.</p></li>
<li><p>Batch (i.e. <code class="docutils literal notranslate"><span class="pre">number_of_transforms</span></code> provided to <code class="docutils literal notranslate"><span class="pre">rocfft_plan_create</span></code>) must be 1.</p></li>
<li><p>The FFT input is gathered to the current device at execute time, so all of the FFT data must fit on that device.</p></li>
</ul>
<p>We expect these limitations to be removed in future releases.</p>
</li>
</ul>
</section>
<section id="id108">
<h5>Optimizations<a class="headerlink" href="#id108" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved performance of some small 2D/3D real FFTs supported by 2D_SINGLE kernel. gfx90a gets more optimization
by offline tuning.</p></li>
<li><p>Removed an extra kernel launch from even-length real-complex FFTs that use callbacks.</p></li>
</ul>
</section>
<section id="id109">
<h5>Changed<a class="headerlink" href="#id109" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Built kernels in solution-map to library kernel cache.</p></li>
<li><p>Real forward transforms (real-to-complex) no longer overwrite input.  rocFFT still may overwrite real inverse (complex-to-real) input, as this allows for faster performance.</p></li>
<li><p>rocfft-rider and dyna-rocfft-rider have been renamed to rocfft-bench and dyna-rocfft-bench, controlled by the
BUILD_CLIENTS_BENCH CMake option.  Links for the old file names are installed, and the old
BUILD_CLIENTS_RIDER CMake option is accepted for compatibility but both will be removed in a future release.</p></li>
<li><p>Binaries in debug builds no longer have a “-d” suffix.</p></li>
</ul>
</section>
<section id="id110">
<h5>Fixed<a class="headerlink" href="#id110" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>rocFFT now correctly handles load callbacks that convert data from a smaller data type (e.g. 16-bit integers -&gt; 32-bit float).</p></li>
</ul>
</section>
</section>
<section id="id111">
<h4>rocm-cmake 0.11.0<a class="headerlink" href="#id111" title="Link to this heading">#</a></h4>
<p>rocm-cmake 0.11.0 for ROCm 6.0.0</p>
<section id="id112">
<h5>Changed<a class="headerlink" href="#id112" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>ROCMSphinxDoc: Improved validation, documentation and rocm-docs-core integration.</p></li>
</ul>
</section>
<section id="id113">
<h5>Fixed<a class="headerlink" href="#id113" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>ROCMClangTidy: Fixed extra make flags passed for clang tidy.</p></li>
<li><p>ROCMTest: Fixed issues when using module in a subdirectory.</p></li>
</ul>
</section>
</section>
<section id="id114">
<h4>rocPRIM 3.0.0<a class="headerlink" href="#id114" title="Link to this heading">#</a></h4>
<p>rocPRIM 3.0.0 for ROCm 6.0.0</p>
<section id="id115">
<h5>Added<a class="headerlink" href="#id115" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">block_sort::sort()</span></code> overload for keys and values with a dynamic size, for all block sort algorithms. Additionally, all <code class="docutils literal notranslate"><span class="pre">block_sort::sort()</span></code> overloads with a dynamic size are now supported for <code class="docutils literal notranslate"><span class="pre">block_sort_algorithm::merge_sort</span></code> and <code class="docutils literal notranslate"><span class="pre">block_sort_algorithm::bitonic_sort</span></code>.</p></li>
<li><p>New two-way partition primitive <code class="docutils literal notranslate"><span class="pre">partition_two_way</span></code> which can write to two separate iterators.</p></li>
</ul>
</section>
<section id="id116">
<h5>Optimizations<a class="headerlink" href="#id116" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved the performance of <code class="docutils literal notranslate"><span class="pre">partition</span></code>.</p></li>
</ul>
</section>
<section id="id117">
<h5>Fixed<a class="headerlink" href="#id117" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed <code class="docutils literal notranslate"><span class="pre">rocprim::MatchAny</span></code> for devices with 64-bit warp size. The function <code class="docutils literal notranslate"><span class="pre">rocprim::MatchAny</span></code> is deprecated and <code class="docutils literal notranslate"><span class="pre">rocprim::match_any</span></code> is preferred instead.</p></li>
</ul>
</section>
</section>
<section id="id118">
<h4>rocSOLVER 3.24.0<a class="headerlink" href="#id118" title="Link to this heading">#</a></h4>
<p>rocSOLVER 3.24.0 for ROCm 6.0.0</p>
<section id="id119">
<h5>Added<a class="headerlink" href="#id119" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Cholesky refactorization for sparse matrices</p>
<ul>
<li><p>CSRRF_REFACTCHOL</p></li>
</ul>
</li>
<li><p>Added <code class="docutils literal notranslate"><span class="pre">rocsolver_rfinfo_mode</span></code> and the ability to specify the desired refactorization routine (see <code class="docutils literal notranslate"><span class="pre">rocsolver_set_rfinfo_mode</span></code>).</p></li>
</ul>
</section>
<section id="id120">
<h5>Changed<a class="headerlink" href="#id120" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>CSRRF_ANALYSIS and CSRRF_SOLVE now support sparse Cholesky factorization</p></li>
</ul>
</section>
</section>
<section id="id121">
<h4>rocSPARSE 3.0.2<a class="headerlink" href="#id121" title="Link to this heading">#</a></h4>
<p>rocSPARSE 3.0.2 for ROCm 6.0.0</p>
<section id="id122">
<h5>Added<a class="headerlink" href="#id122" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added rocsparse_inverse_permutation</p></li>
<li><p>Added mixed precisions for SpVV</p></li>
<li><p>Added uniform int8 precision for Gather and Scatter</p></li>
</ul>
</section>
<section id="id123">
<h5>Optimized<a class="headerlink" href="#id123" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimization to doti routine</p></li>
<li><p>Optimization to spin-looping algorithms</p></li>
</ul>
</section>
<section id="id124">
<h5>Changed<a class="headerlink" href="#id124" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Changed rocsparse_spmv function arguments</p></li>
<li><p>Changed rocsparse_xbsrmv routines function arguments</p></li>
<li><p>doti, dotci, spvv, and csr2ell now require calling hipStreamSynchronize after when using host pointer mode</p></li>
<li><p>Improved documentation</p></li>
<li><p>Improved verbose output during argument checking on API function calls</p></li>
</ul>
</section>
<section id="id125">
<h5>Deprecated<a class="headerlink" href="#id125" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Deprecated rocsparse_spmv_ex</p></li>
<li><p>Deprecated rocsparse_xbsrmv_ex routines</p></li>
</ul>
</section>
<section id="id126">
<h5>Removed<a class="headerlink" href="#id126" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed auto stages from spmv, spmm, spgemm, spsv, spsm, and spitsv.</p></li>
<li><p>Removed rocsparse_spmm_ex routine</p></li>
</ul>
</section>
<section id="id127">
<h5>Fixed<a class="headerlink" href="#id127" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed a bug in rocsparse-bench, where SpMV algorithm was not taken into account in CSR format</p></li>
<li><p>Fixed the BSR/GEBSR routines bsrmv, bsrsv, bsrmm, bsrgeam, gebsrmv, gebsrmm so that block_dim==0 is considered an invalid size</p></li>
<li><p>Fixed bug where passing nnz = 0 to doti or dotci did not always return a dot product of 0</p></li>
</ul>
</section>
</section>
<section id="id128">
<h4>rocThrust 3.0.0<a class="headerlink" href="#id128" title="Link to this heading">#</a></h4>
<p>rocThrust 3.0.0 for ROCm 6.0.0</p>
<section id="id129">
<h5>Added<a class="headerlink" href="#id129" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Updated to match upstream Thrust 2.0.1</p></li>
<li><p>NV_IF_TARGET macro from libcu++ for NVIDIA backend and HIP implementation for HIP backend.</p></li>
</ul>
</section>
<section id="id130">
<h5>Changed<a class="headerlink" href="#id130" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The cmake build system now additionally accepts <code class="docutils literal notranslate"><span class="pre">GPU_TARGETS</span></code> in addition to <code class="docutils literal notranslate"><span class="pre">AMDGPU_TARGETS</span></code> for
setting the targeted gpu architectures. <code class="docutils literal notranslate"><span class="pre">GPU_TARGETS=all</span></code> will compile for all supported architectures.
<code class="docutils literal notranslate"><span class="pre">AMDGPU_TARGETS</span></code> is only provided for backwards compatibility, <code class="docutils literal notranslate"><span class="pre">GPU_TARGETS</span></code> should be preferred.</p></li>
</ul>
</section>
<section id="id131">
<h5>Removed<a class="headerlink" href="#id131" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed cub symlink from the root of the repository.</p></li>
<li><p>Removed support for deprecated macros (THRUST_DEVICE_BACKEND and THRUST_HOST_BACKEND).</p></li>
</ul>
</section>
<section id="id132">
<h5>Fixed<a class="headerlink" href="#id132" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed a segmentation fault when binary search / upper bound / lower bound / equal range was invoked with <code class="docutils literal notranslate"><span class="pre">hip_rocprim::execute_on_stream_base</span></code> policy.</p></li>
</ul>
</section>
<section id="id133">
<h5>Known Issues<a class="headerlink" href="#id133" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>For NVIDIA backend, <code class="docutils literal notranslate"><span class="pre">NV_IF_TARGET</span></code> and <code class="docutils literal notranslate"><span class="pre">THRUST_RDC_ENABLED</span></code> intend to substitute the <code class="docutils literal notranslate"><span class="pre">THRUST_HAS_CUDART</span></code> macro, which is now no longer used in Thrust (provided for legacy support only). However, there is no <code class="docutils literal notranslate"><span class="pre">THRUST_RDC_ENABLED</span></code> macro available for the HIP backend, so some branches in Thrust’s code may be unreachable in the HIP backend.</p></li>
</ul>
</section>
</section>
<section id="id134">
<h4>rocWMMA 1.3.0<a class="headerlink" href="#id134" title="Link to this heading">#</a></h4>
<p>rocWMMA 1.3.0 for ROCm 6.0.0</p>
<section id="id135">
<h5>Added<a class="headerlink" href="#id135" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added support for gfx940, gfx941 and gfx942 targets</p></li>
<li><p>Added support for f8, bf8 and xfloat32 datatypes</p></li>
<li><p>Added support for HIP_NO_HALF, __ HIP_NO_HALF_CONVERSIONS__ and __ HIP_NO_HALF_OPERATORS__ (e.g. pytorch environment)</p></li>
</ul>
</section>
<section id="id136">
<h5>Changed<a class="headerlink" href="#id136" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>rocWMMA with hipRTC now supports bfloat16_t datatype</p></li>
<li><p>gfx11 wmma now uses lane swap instead of broadcast for layout adjustment</p></li>
<li><p>Updated samples GEMM parameter validation on host arch</p></li>
</ul>
</section>
<section id="id137">
<h5>Fixed<a class="headerlink" href="#id137" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Disabled gtest static library deployment</p></li>
<li><p>Extended tests now build in large code model</p></li>
</ul>
</section>
</section>
<section id="id138">
<h4>Tensile 4.39.0<a class="headerlink" href="#id138" title="Link to this heading">#</a></h4>
<p>Tensile 4.39.0 for ROCm 6.0.0</p>
<section id="id139">
<h5>Added<a class="headerlink" href="#id139" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added aquavanjaram support: gfx940/gfx941/gfx942, fp8/bf8 datatype, xf32 datatype, and stochastic rounding for various datatypes</p></li>
<li><p>Added/updated tuning scripts</p></li>
<li><p>Added DirectToLds support for larger data types with 32bit global load (old parameter DirectToLds is replaced with DirectToLdsA and DirectToLdsB), and the corresponding test cases</p></li>
<li><p>Added the average of frequency, power consumption, and temperature information for the winner kernels to the CSV file</p></li>
<li><p>Added asmcap check for MFMA + const src</p></li>
<li><p>Added support for wider local read + pack with v_perm (with VgprForLocalReadPacking=True)</p></li>
<li><p>Added a new parameter to increase miLatencyLeft</p></li>
</ul>
</section>
<section id="id140">
<h5>Optimizations<a class="headerlink" href="#id140" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Enabled InitAccVgprOpt for MatrixInstruction cases</p></li>
<li><p>Implemented local read related parameter calculations with DirectToVgpr</p></li>
<li><p>Adjusted miIssueLatency for gfx940</p></li>
<li><p>Enabled dedicated vgpr allocation for local read + pack</p></li>
<li><p>Optimized code initialization</p></li>
<li><p>Optimized sgpr allocation</p></li>
<li><p>Supported DGEMM TLUB + RLVW=2 for odd N (edge shift change)</p></li>
<li><p>Enabled miLatency optimization for (gfx940/gfx941 + MFMA) for specific data types, and fixed instruction scheduling</p></li>
</ul>
</section>
<section id="id141">
<h5>Changed<a class="headerlink" href="#id141" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed old code for DTL + (bpe * GlobalReadVectorWidth &gt; 4)</p></li>
<li><p>Changed/updated failed CI tests for gfx11xx, InitAccVgprOpt, and DTLds</p></li>
<li><p>Removed unused CustomKernels and ReplacementKernels</p></li>
<li><p>Added a reject condition for DTVB + TransposeLDS=False (not supported so far)</p></li>
<li><p>Removed unused code for DirectToLds</p></li>
<li><p>Updated test cases for DTV + TransposeLDS=False</p></li>
<li><p>Moved parameter MinKForGSU from globalparameter to BenchmarkCommonParameter to support smaller K</p></li>
<li><p>Changed how to calculate latencyForLR for miLatency</p></li>
<li><p>Set minimum value of latencyForLRCount for 1LDSBuffer to avoid getting rejected by overflowedResources=5 (related to miLatency)</p></li>
<li><p>Refactored allowLRVWBforTLUandMI and renamed it as VectorWidthB</p></li>
<li><p>Supported multi-gpu for different architectures in lazy library loading</p></li>
<li><p>Enabled dtree library for batch &gt; 1</p></li>
<li><p>Added problem scale feature for dtree selection</p></li>
<li><p>Enabled ROCm SMI for gfx940/941.</p></li>
<li><p>Modified non-lazy load build to skip experimental logic</p></li>
</ul>
</section>
<section id="id142">
<h5>Fixed<a class="headerlink" href="#id142" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed predicate ordering for fp16alt impl round near zero mode to unbreak distance modes</p></li>
<li><p>Fixed boundary check for mirror dims and re-enable disabled mirror dims test cases</p></li>
<li><p>Fixed merge error affecting i8 with wmma</p></li>
<li><p>Fixed mismatch issue with DTLds + TSGR + TailLoop</p></li>
<li><p>Fixed a bug with InitAccVgprOpt + GSU&gt;1 and a mismatch issue with PGR=0</p></li>
<li><p>Fixed override for unloaded solutions when lazy loading</p></li>
<li><p>Fixed build some errors (adding missing headers)</p></li>
<li><p>Fixed boost link for a clean build on ubuntu22</p></li>
<li><p>Fixed bug in forcestoresc1 arch selection</p></li>
<li><p>Fixed compiler directive for gfx941 and gfx942</p></li>
<li><p>Fixed formatting for DecisionTree_test.cpp</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-7-1">
<h2>ROCm 5.7.1<a class="headerlink" href="#rocm-5-7-1" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable no-duplicate-header -->
<section id="what-s-new-in-this-release">
<h3>What’s new in this release<a class="headerlink" href="#what-s-new-in-this-release" title="Link to this heading">#</a></h3>
<p>ROCm 5.7.1 is a point release with several bug fixes in the HIP runtime.</p>
<section id="installing-all-gpu-addresssanitizer-packages-with-a-single-command">
<h4>Installing all GPU AddressSanitizer packages with a single command<a class="headerlink" href="#installing-all-gpu-addresssanitizer-packages-with-a-single-command" title="Link to this heading">#</a></h4>
<p>ROCm 5.7.1 simplifies the installation steps for the optional AddressSanitizer (ASan) packages. This
release provides the meta package <em>rocm-ml-sdk-asan</em> for ease of ASan installation. The following
command can be used to install all ASan packages rather than installing each package separately,</p>
<div class="highlight-none notranslate"><div class="highlight"><pre><span></span>    sudo apt-get install rocm-ml-sdk-asan
</pre></div>
</div>
<p>For more detailed information about using the GPU AddressSanitizer, refer to the
<a class="reference external" href="https://rocm.docs.amd.com/en/docs-5.7.1/understand/using_gpu_sanitizer.html">user guide</a></p>
</section>
</section>
<section id="rocm-libraries">
<h3>ROCm libraries<a class="headerlink" href="#rocm-libraries" title="Link to this heading">#</a></h3>
<section id="rocblas">
<h4>rocBLAS<a class="headerlink" href="#rocblas" title="Link to this heading">#</a></h4>
<p>A new functionality rocblas-gemm-tune and an environment variable
ROCBLAS_TENSILE_GEMM_OVERRIDE_PATH are added to rocBLAS in the ROCm 5.7.1 release.</p>
<p><code class="docutils literal notranslate"><span class="pre">rocblas-gemm-tune</span></code> is used to find the best-performing GEMM kernel for each GEMM problem set. It
has a command line interface, which mimics the –yaml input used by rocblas-bench. To generate the
expected –yaml input, profile logging can be used, by setting the environment variable
ROCBLAS_LAYER4.</p>
<p>For more information on rocBLAS logging, see Logging in rocBLAS, in the
<a class="reference external" href="https://rocm.docs.amd.com/projects/rocBLAS/en/docs-5.7.1/API_Reference_Guide.html#logging-in-rocblas">API Reference Guide</a>.</p>
<p>An example input file: Expected output (note selected GEMM idx may differ): Where the far right values
(solution_index) are the indices of the best-performing kernels for those GEMMs in the rocBLAS kernel
library. These indices can be directly used in future GEMM calls. See
<code class="docutils literal notranslate"> <span class="pre">rocBLAS/samples/example_user_driven_tuning.cpp</span></code> for sample code of directly using kernels via their
indices.</p>
<p>If the output is stored in a file, the results can be used to override default kernel selection with the
kernels found by setting the environment variable ROCBLAS_TENSILE_GEMM_OVERRIDE_PATH, which
points to the stored file.</p>
<p>For more details, refer to the
<a class="reference external" href="https://rocm.docs.amd.com/projects/rocBLAS/en/latest/Programmers_Guide.html#rocblas-gemm-tune">rocBLAS Programmer’s Guide</a>.</p>
</section>
<section id="hip-5-7-1-for-rocm-5-7-1">
<h4>HIP 5.7.1 (for ROCm 5.7.1)<a class="headerlink" href="#hip-5-7-1-for-rocm-5-7-1" title="Link to this heading">#</a></h4>
<p>ROCm 5.7.1 is a point release with several bug fixes in the HIP runtime.</p>
</section>
</section>
<section id="defect-fixes">
<h3>Defect fixes<a class="headerlink" href="#defect-fixes" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">hipPointerGetAttributes</span></code> API returns the correct HIP memory type as <code class="docutils literal notranslate"><span class="pre">hipMemoryTypeManaged</span></code>
for managed memory.</p>
</section>
<section id="library-changes-in-rocm-5-7-1">
<h3>Library changes in ROCM 5.7.1<a class="headerlink" href="#library-changes-in-rocm-5-7-1" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>AMDMIGraphX</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/AMDMIGraphX/releases/tag/rocm-5.7.1">2.7</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.7.1">1.1.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.7.1">2.13.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.7.1">1.0.12</a></p></td>
</tr>
<tr class="row-even"><td><p>hipRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipRAND/releases/tag/rocm-5.7.1">2.10.16</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p>1.8.1 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.7.1">1.8.2</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.7.1">2.3.8</a></p></td>
</tr>
<tr class="row-odd"><td><p>MIOpen</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/MIOpen/releases/tag/rocm-5.7.1">2.19.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.7.1">2.1.11</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.7.1">3.1.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.7.1">1.0.24</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocm-cmake</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.7.1">0.10.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.7.1">2.13.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.7.1">2.10.17</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.7.1">3.23.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.7.1">2.5.4</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.7.1">2.18.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocWMMA</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.7.1">1.2.0</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.7.1">4.38.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="hipsolver-1-8-2">
<h4>hipSOLVER 1.8.2<a class="headerlink" href="#hipsolver-1-8-2" title="Link to this heading">#</a></h4>
<p>hipSOLVER 1.8.2 for ROCm 5.7.1</p>
<section id="id143">
<h5>Fixed<a class="headerlink" href="#id143" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed conflicts between the hipsolver-dev and -asan packages by excluding
hipsolver_module.f90 from the latter</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-7-0">
<h2>ROCm 5.7.0<a class="headerlink" href="#rocm-5-7-0" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable no-duplicate-header -->
<section id="release-highlights-for-rocm-5-7">
<h3>Release highlights for ROCm 5.7<a class="headerlink" href="#release-highlights-for-rocm-5-7" title="Link to this heading">#</a></h3>
<p>New features include:</p>
<ul class="simple">
<li><p>A new library (hipTensor)</p></li>
<li><p>Optimizations for rocRAND and MIVisionX</p></li>
<li><p>AddressSanitizer for host and device code (GPU) is now available as a beta</p></li>
</ul>
<p>Note that ROCm 5.7.0 is EOS for MI50. 5.7 versions of ROCm are the last major releases in the ROCm 5
series. This release is Linux-only.</p>
<div class="admonition important">
<p class="admonition-title">Important</p>
<p>The next major ROCm release (ROCm 6.0) will not be backward compatible with the ROCm 5 series.
Changes will include: splitting LLVM packages into more manageable sizes, changes to the HIP runtime
API, splitting rocRAND and hipRAND into separate packages, and reorganizing our file structure.</p>
</div>
<section id="id144">
<h4>AMD Instinct™ MI50 end-of-support notice<a class="headerlink" href="#id144" title="Link to this heading">#</a></h4>
<p>AMD Instinct MI50, Radeon Pro VII, and Radeon VII products (collectively gfx906 GPUs) will enter
maintenance mode starting Q3 2023.</p>
<p>As outlined in <a class="reference external" href="https://rocm.docs.amd.com/en/docs-5.6.0/release.html">5.6.0</a>, ROCm 5.7 will be the
final release for gfx906 GPUs to be in a fully supported state.</p>
<ul class="simple">
<li><p>ROCm 6.0 release will show MI50s as “under maintenance” for
<a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/reference/system-requirements.html" title="(in ROCm Installation on Linux v6.0.0)"><span class="xref std std-doc">Linux</span></a> and
<a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-windows/en/docs-6.0.0/reference/system-requirements.html" title="(in ROCm Installation on Linux v6.0.0)"><span class="xref std std-doc">Windows</span></a></p></li>
<li><p>No new features and performance optimizations will be supported for the gfx906 GPUs beyond this
major release (ROCm 5.7).</p></li>
<li><p>Bug fixes and critical security patches will continue to be supported for the gfx906 GPUs until Q2
2024 (end of maintenance [EOM] will be aligned with the closest ROCm release).</p></li>
<li><p>Bug fixes during the maintenance will be made to the next ROCm point release.</p></li>
<li><p>Bug fixes will not be backported to older ROCm releases for gfx906.</p></li>
<li><p>Distribution and operating system updates will continue per the ROCm release cadence for gfx906
GPUs until EOM.</p></li>
</ul>
</section>
<section id="feature-updates">
<h4>Feature updates<a class="headerlink" href="#feature-updates" title="Link to this heading">#</a></h4>
<section id="non-hostcall-hip-printf">
<h5>Non-hostcall HIP printf<a class="headerlink" href="#non-hostcall-hip-printf" title="Link to this heading">#</a></h5>
<p><strong>Current behavior</strong></p>
<p>The current version of HIP printf relies on hostcalls, which, in turn, rely on PCIe atomics. However, PCle
atomics are unavailable in some environments, and, as a result, HIP-printf does not work in those
environments. Users may see the following error from runtime (with AMD_LOG_LEVEL 1 and above):</p>
<div class="highlight-shell notranslate"><div class="highlight"><pre><span></span><span class="w">    </span>Pcie<span class="w"> </span>atomics<span class="w"> </span>not<span class="w"> </span>enabled,<span class="w"> </span>hostcall<span class="w"> </span>not<span class="w"> </span>supported
</pre></div>
</div>
<p><strong>Workaround</strong></p>
<p>The ROCm 5.7 release introduces an alternative to the current hostcall-based implementation that
leverages an older OpenCL-based printf scheme, which does not rely on hostcalls/PCIe atomics.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This option is less robust than hostcall-based implementation and is intended to be a
workaround when hostcalls do not work.</p>
</div>
<p>The printf variant is now controlled via a new compiler option -mprintf-kind=<value>. This is
supported only for HIP programs and takes the following values,</value></p>
<ul class="simple">
<li><p>“hostcall” – This currently available implementation relies on hostcalls, which require the system to
support PCIe atomics. It is the default scheme.</p></li>
<li><p>“buffered” – This implementation leverages the older printf scheme used by OpenCL; it relies on a
memory buffer where printf arguments are stored during the kernel execution, and then the runtime
handles the actual printing once the kernel finishes execution.</p></li>
</ul>
<p><strong>NOTE</strong>: With the new workaround:</p>
<ul class="simple">
<li><p>The printf buffer is fixed size and non-circular.  After the buffer is filled, calls to printf will not result in
additional output.</p></li>
<li><p>The printf call returns either 0 (on success) or -1 (on failure, due to full buffer), unlike the hostcall
scheme that returns the number of characters printed.</p></li>
</ul>
</section>
<section id="beta-release-of-llvm-addresssanitizer-asan-with-the-gpu">
<h5>Beta release of LLVM AddressSanitizer (ASan) with the GPU<a class="headerlink" href="#beta-release-of-llvm-addresssanitizer-asan-with-the-gpu" title="Link to this heading">#</a></h5>
<p>The ROCm 5.7 release introduces the beta release of LLVM AddressSanitizer (ASan) with the GPU. The
LLVM ASan provides a process that allows developers to detect runtime addressing errors in
applications and libraries. The detection is achieved using a combination of compiler-added
instrumentation and runtime techniques, including function interception and replacement.</p>
<p>Until now, the LLVM ASan process was only available for traditional purely CPU applications. However,
ROCm has extended this mechanism to additionally allow the detection of some addressing errors on
the GPU in heterogeneous applications. Ideally, developers should treat heterogeneous HIP and
OpenMP applications like pure CPU applications. However, this simplicity has not been achieved yet.</p>
<p>Refer to the documentation on LLVM ASan with the GPU at
<a class="reference internal" href="../conceptual/using-gpu-sanitizer.html"><span class="std std-doc">LLVM AddressSanitizer User Guide</span></a>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The beta release of LLVM ASan for ROCm is currently tested and validated on Ubuntu 20.04.</p>
</div>
</section>
</section>
<section id="id145">
<h4>Defect fixes<a class="headerlink" href="#id145" title="Link to this heading">#</a></h4>
<p>The following defects are fixed in ROCm v5.7:</p>
<ul class="simple">
<li><p>Test hangs observed in HMM RCCL</p></li>
<li><p>NoGpuTst test of Catch2 fails with Docker</p></li>
<li><p>Failures observed with non-HMM HIP directed catch2 tests with XNACK+</p></li>
<li><p>Multiple test failures and test hangs observed in hip-directed catch2 tests with xnack+</p></li>
</ul>
</section>
<section id="hip-5-7-0">
<h4>HIP 5.7.0<a class="headerlink" href="#hip-5-7-0" title="Link to this heading">#</a></h4>
<section id="id146">
<h5>Optimizations<a class="headerlink" href="#id146" title="Link to this heading">#</a></h5>
</section>
<section id="id147">
<h5>Additions<a class="headerlink" href="#id147" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added <code class="docutils literal notranslate"><span class="pre">meta_group_size</span></code>/<code class="docutils literal notranslate"><span class="pre">rank</span></code> for getting the number of tiles and rank of a tile in the partition</p></li>
<li><p>Added new APIs supporting Windows only, under development on Linux</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMallocMipmappedArray</span></code> for allocating a mipmapped array on the device</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipFreeMipmappedArray</span></code> for freeing a mipmapped array on the device</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipGetMipmappedArrayLevel</span></code> for getting a mipmap level of a HIP mipmapped array</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMipmappedArrayCreate</span></code> for creating a mipmapped array</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMipmappedArrayDestroy</span></code> for destroy a mipmapped array</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMipmappedArrayGetLevel</span></code> for getting a mipmapped array on a mipmapped level</p></li>
</ul>
</li>
</ul>
</section>
<section id="id148">
<h5>Changes<a class="headerlink" href="#id148" title="Link to this heading">#</a></h5>
</section>
<section id="id149">
<h5>Fixes<a class="headerlink" href="#id149" title="Link to this heading">#</a></h5>
</section>
<section id="id150">
<h5>Known issues<a class="headerlink" href="#id150" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>HIP memory type enum values currently don’t support equivalent value to
<code class="docutils literal notranslate"><span class="pre">cudaMemoryTypeUnregistered</span></code>, due to HIP functionality backward compatibility.</p></li>
<li><p>HIP API <code class="docutils literal notranslate"><span class="pre">hipPointerGetAttributes</span></code> could return invalid value in case the input memory pointer was not
allocated through any HIP API on device or host.</p></li>
</ul>
</section>
<section id="upcoming-changes-for-hip-in-rocm-6-0-release">
<h5>Upcoming changes for HIP in ROCm 6.0 release<a class="headerlink" href="#upcoming-changes-for-hip-in-rocm-6-0-release" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removal of <code class="docutils literal notranslate"><span class="pre">gcnarch</span></code> from hipDeviceProp_t structure</p></li>
<li><p>Addition of new fields in hipDeviceProp_t structure</p>
<ul>
<li><p>maxTexture1D</p></li>
<li><p>maxTexture2D</p></li>
<li><p>maxTexture1DLayered</p></li>
<li><p>maxTexture2DLayered</p></li>
<li><p>sharedMemPerMultiprocessor</p></li>
<li><p>deviceOverlap</p></li>
<li><p>asyncEngineCount</p></li>
<li><p>surfaceAlignment</p></li>
<li><p>unifiedAddressing</p></li>
<li><p>computePreemptionSupported</p></li>
<li><p>hostRegisterSupported</p></li>
<li><p>uuid</p></li>
</ul>
</li>
<li><p>Removal of deprecated code -hip-hcc codes from hip code tree</p></li>
<li><p>Correct hipArray usage in HIP APIs such as <code class="docutils literal notranslate"><span class="pre">hipMemcpyAtoH</span></code> and <code class="docutils literal notranslate"><span class="pre">hipMemcpyHtoA</span></code></p></li>
<li><p>HIPMEMCPY_3D fields correction to avoid truncation of “size_t” to “unsigned int” inside
<code class="docutils literal notranslate"><span class="pre">hipMemcpy3D()</span></code></p></li>
<li><p>Renaming of ‘memoryType’ in <code class="docutils literal notranslate"><span class="pre">hipPointerAttribute_t</span></code> structure to ‘type’</p></li>
<li><p>Correct <code class="docutils literal notranslate"><span class="pre">hipGetLastError</span></code> to return the last error instead of last API call’s return code</p></li>
<li><p>Update <code class="docutils literal notranslate"><span class="pre">hipExternalSemaphoreHandleDesc</span></code> to add “unsigned int reserved[16]”</p></li>
<li><p>Correct handling of flag values in <code class="docutils literal notranslate"><span class="pre">hipIpcOpenMemHandle</span></code> for <code class="docutils literal notranslate"><span class="pre">hipIpcMemLazyEnablePeerAccess</span></code></p></li>
<li><p>Remove <code class="docutils literal notranslate"><span class="pre">hiparray*</span></code> and make it opaque with <code class="docutils literal notranslate"><span class="pre">hipArray_t</span></code></p></li>
</ul>
</section>
</section>
</section>
<section id="library-changes-in-rocm-5-7-0">
<h3>Library changes in ROCM 5.7.0<a class="headerlink" href="#library-changes-in-rocm-5-7-0" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>AMDMIGraphX</p></td>
<td><p>2.5 ⇒ <a class="reference external" href="https://github.com/ROCm/AMDMIGraphX/releases/tag/rocm-5.7.0">2.7</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipBLAS</p></td>
<td><p>0.54.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.7.0">1.1.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.7.0">2.13.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.7.0">1.0.12</a></p></td>
</tr>
<tr class="row-even"><td><p>hipRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipRAND/releases/tag/rocm-5.7.0">2.10.16</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p>1.8.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.7.0">1.8.1</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p>2.3.7 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.7.0">2.3.8</a></p></td>
</tr>
<tr class="row-odd"><td><p>MIOpen</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/MIOpen/releases/tag/rocm-5.7.0">2.19.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p>2.1.9 ⇒ <a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.7.0">2.1.11</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p>3.0.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.7.0">3.1.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p>1.0.23 ⇒ <a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.7.0">1.0.24</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocm-cmake</p></td>
<td><p>0.9.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.7.0">0.10.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p>2.13.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.7.0">2.13.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.7.0">2.10.17</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p>3.22.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.7.0">3.23.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p>2.5.2 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.7.0">2.5.4</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.7.0">2.18.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocWMMA</p></td>
<td><p>1.1.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.7.0">1.2.0</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p>4.37.0 ⇒ <a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.7.0">4.38.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="amdmigraphx-2-7">
<h4>AMDMIGraphX 2.7<a class="headerlink" href="#amdmigraphx-2-7" title="Link to this heading">#</a></h4>
<p>MIGraphX 2.7 for ROCm 5.7.0</p>
<section id="id151">
<h5>Added<a class="headerlink" href="#id151" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Enabled hipRTC to not require dev packages for migraphx runtime and allow the ROCm install to be in a different directory than it was during build time</p></li>
<li><p>Add support for multi-target execution</p></li>
<li><p>Added Dynamic Batch support with C++/Python APIs</p></li>
<li><p>Add migraphx.create_argument to python API</p></li>
<li><p>Added dockerfile example for Ubuntu 22.04</p></li>
<li><p>Add TensorFlow supported ops in driver similar to exist onnx operator list</p></li>
<li><p>Add a MIGRAPHX_TRACE_MATCHES_FOR env variable to filter the matcher trace</p></li>
<li><p>Improved debugging by printing max,min,mean and stddev values for TRACE_EVAL = 2</p></li>
<li><p>use fast_math flag instead of ENV flag for GELU</p></li>
<li><p>Print message from driver if offload copy is set for compiled program</p></li>
</ul>
</section>
<section id="id152">
<h5>Optimizations<a class="headerlink" href="#id152" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimized for ONNX Runtime 1.14.0</p></li>
<li><p>Improved compile times by only building for the GPU on the system</p></li>
<li><p>Improve performance of pointwise/reduction kernels when using NHWC layouts</p></li>
<li><p>Load specific version of the migraphx_py library</p></li>
<li><p>Annotate functions with the block size so the compiler can do a better job of optimizing</p></li>
<li><p>Enable reshape on nonstandard shapes</p></li>
<li><p>Use half HIP APIs to compute max and min</p></li>
<li><p>Added support for broadcasted scalars to unsqueeze operator</p></li>
<li><p>Improved multiplies with dot operator</p></li>
<li><p>Handle broadcasts across dot and concat</p></li>
<li><p>Add verify namespace for better symbol resolution</p></li>
</ul>
</section>
<section id="id153">
<h5>Fixed<a class="headerlink" href="#id153" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Resolved accuracy issues with FP16 resnet50</p></li>
<li><p>Update cpp generator to handle inf from  float</p></li>
<li><p>Fix assertion error during verify and make DCE work with tuples</p></li>
<li><p>Fix convert operation for NaNs</p></li>
<li><p>Fix shape typo in API test</p></li>
<li><p>Fix compile warnings for shadowing variable names</p></li>
<li><p>Add missing specialization for the <code class="docutils literal notranslate"><span class="pre">nullptr</span></code> for the hash function</p></li>
</ul>
</section>
<section id="id154">
<h5>Changed<a class="headerlink" href="#id154" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Bumped version of half library to 5.6.0</p></li>
<li><p>Bumped CI to support rocm 5.6</p></li>
<li><p>Make building tests optional</p></li>
<li><p>replace np.bool with bool as per numpy request</p></li>
</ul>
</section>
<section id="id155">
<h5>Removed<a class="headerlink" href="#id155" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed int8x4 rocBlas calls due to deprecation</p></li>
<li><p>removed std::reduce usage since not all OS’ support it</p></li>
</ul>
</section>
</section>
<section id="hipblas-1-1-0">
<h4>hipBLAS 1.1.0<a class="headerlink" href="#hipblas-1-1-0" title="Link to this heading">#</a></h4>
<p>hipBLAS 1.1.0 for ROCm 5.7.0</p>
<section id="id156">
<h5>Changed<a class="headerlink" href="#id156" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>updated documentation requirements</p></li>
</ul>
</section>
<section id="dependencies">
<h5>Dependencies<a class="headerlink" href="#dependencies" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>dependency rocSOLVER now depends on rocSPARSE</p></li>
</ul>
</section>
</section>
<section id="hipsolver-1-8-1">
<h4>hipSOLVER 1.8.1<a class="headerlink" href="#hipsolver-1-8-1" title="Link to this heading">#</a></h4>
<p>hipSOLVER 1.8.1 for ROCm 5.7.0</p>
<section id="id157">
<h5>Changed<a class="headerlink" href="#id157" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Changed hipsolver-test sparse input data search paths to be relative to the test executable</p></li>
</ul>
</section>
</section>
<section id="hipsparse-2-3-8">
<h4>hipSPARSE 2.3.8<a class="headerlink" href="#hipsparse-2-3-8" title="Link to this heading">#</a></h4>
<p>hipSPARSE 2.3.8 for ROCm 5.7.0</p>
<section id="improved">
<h5>Improved<a class="headerlink" href="#improved" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fix compilation failures when using cusparse 12.1.0 backend</p></li>
<li><p>Fix compilation failures when using cusparse 12.0.0 backend</p></li>
<li><p>Fix compilation failures when using cusparse 10.1 (non-update versions) as backend</p></li>
<li><p>Minor improvements</p></li>
</ul>
</section>
</section>
<section id="rocalution-2-1-11">
<h4>rocALUTION 2.1.11<a class="headerlink" href="#rocalution-2-1-11" title="Link to this heading">#</a></h4>
<p>rocALUTION 2.1.11 for ROCm 5.7.0</p>
<section id="id158">
<h5>Added<a class="headerlink" href="#id158" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added support for gfx940, gfx941 and gfx942</p></li>
</ul>
</section>
<section id="id159">
<h5>Improved<a class="headerlink" href="#id159" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed OpenMP runtime issue with Windows toolchain</p></li>
</ul>
</section>
</section>
<section id="rocblas-3-1-0">
<h4>rocBLAS 3.1.0<a class="headerlink" href="#rocblas-3-1-0" title="Link to this heading">#</a></h4>
<p>rocBLAS 3.1.0 for ROCm 5.7.0</p>
<section id="id160">
<h5>Added<a class="headerlink" href="#id160" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>yaml lock step argument scanning for rocblas-bench and rocblas-test clients. See Programmers Guide for details.</p></li>
<li><p>rocblas-gemm-tune is used to find the best performing GEMM kernel for each of a given set of GEMM problems.</p></li>
</ul>
</section>
<section id="id161">
<h5>Fixed<a class="headerlink" href="#id161" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>make offset calculations for rocBLAS functions 64 bit safe.  Fixes for very large leading dimensions or increments potentially causing overflow:</p>
<ul>
<li><p>Level 1: axpy, copy, rot, rotm, scal, swap, asum, dot, iamax, iamin, nrm2</p></li>
<li><p>Level 2: gemv, symv, hemv, trmv, ger, syr, her, syr2, her2, trsv</p></li>
<li><p>Level 3: gemm, symm, hemm, trmm, syrk, herk, syr2k, her2k, syrkx, herkx, trsm, trtri, dgmm, geam</p></li>
<li><p>General: set_vector, get_vector, set_matrix, get_matrix</p></li>
<li><p>Related fixes: internal scalar loads with &gt; 32bit offsets</p></li>
<li><p>fix in-place functionality for all trtri sizes</p></li>
</ul>
</li>
</ul>
</section>
<section id="id162">
<h5>Changed<a class="headerlink" href="#id162" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>dot when using rocblas_pointer_mode_host is now synchronous to match legacy BLAS as it stores results in host memory</p></li>
<li><p>enhanced reporting of installation issues caused by runtime libraries (Tensile)</p></li>
<li><p>standardized internal rocblas C++ interface across most functions</p></li>
</ul>
</section>
<section id="id163">
<h5>Deprecated<a class="headerlink" href="#id163" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removal of <strong>STDC_WANT_IEC_60559_TYPES_EXT</strong> define in future release</p></li>
</ul>
</section>
<section id="id164">
<h5>Dependencies<a class="headerlink" href="#id164" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>optional use of AOCL BLIS 4.0 on Linux for clients</p></li>
<li><p>optional build tool only dependency on python psutil</p></li>
</ul>
</section>
</section>
<section id="rocfft-1-0-24">
<h4>rocFFT 1.0.24<a class="headerlink" href="#rocfft-1-0-24" title="Link to this heading">#</a></h4>
<p>rocFFT 1.0.24 for ROCm 5.7.0</p>
<section id="id165">
<h5>Optimizations<a class="headerlink" href="#id165" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved performance of complex forward/inverse 1D FFTs (2049 &lt;= length &lt;= 131071) that use Bluestein’s algorithm.</p></li>
</ul>
</section>
<section id="id166">
<h5>Added<a class="headerlink" href="#id166" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Implemented a solution map version converter and finish the first conversion from ver.0 to ver.1. Where version 1 removes some incorrect kernels (sbrc/sbcr using half_lds)</p></li>
</ul>
</section>
<section id="id167">
<h5>Changed<a class="headerlink" href="#id167" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Moved rocfft_rtc_helper executable to lib/rocFFT directory on Linux.</p></li>
<li><p>Moved library kernel cache to lib/rocFFT directory.</p></li>
</ul>
</section>
</section>
<section id="rocm-cmake-0-10-0">
<h4>rocm-cmake 0.10.0<a class="headerlink" href="#rocm-cmake-0-10-0" title="Link to this heading">#</a></h4>
<p>rocm-cmake 0.10.0 for ROCm 5.7.0</p>
<section id="id168">
<h5>Added<a class="headerlink" href="#id168" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added ROCMTest module</p></li>
<li><p>ROCMCreatePackage: Added support for ASAN packages</p></li>
</ul>
</section>
</section>
<section id="rocprim-2-13-1">
<h4>rocPRIM 2.13.1<a class="headerlink" href="#rocprim-2-13-1" title="Link to this heading">#</a></h4>
<p>rocPRIM 2.13.1 for ROCm 5.7.0</p>
<section id="id169">
<h5>Changed<a class="headerlink" href="#id169" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Deprecated configuration <code class="docutils literal notranslate"><span class="pre">radix_sort_config</span></code> for device-level radix sort as it no longer matches the algorithm’s parameters. New configuration <code class="docutils literal notranslate"><span class="pre">radix_sort_config_v2</span></code> is preferred instead.</p></li>
<li><p>Removed erroneous implementation of device-level <code class="docutils literal notranslate"><span class="pre">inclusive_scan</span></code> and <code class="docutils literal notranslate"><span class="pre">exclusive_scan</span></code>. The prior default implementation using lookback-scan now is the only available implementation.</p></li>
<li><p>The benchmark metric indicating the bytes processed for <code class="docutils literal notranslate"><span class="pre">exclusive_scan_by_key</span></code> and <code class="docutils literal notranslate"><span class="pre">inclusive_scan_by_key</span></code> has been changed to incorporate the key type. Furthermore, the benchmark log has been changed such that these algorithms are reported as <code class="docutils literal notranslate"><span class="pre">scan</span></code> and <code class="docutils literal notranslate"><span class="pre">scan_by_key</span></code> instead of <code class="docutils literal notranslate"><span class="pre">scan_exclusive</span></code> and <code class="docutils literal notranslate"><span class="pre">scan_inclusive</span></code>.</p></li>
<li><p>Deprecated configurations <code class="docutils literal notranslate"><span class="pre">scan_config</span></code> and <code class="docutils literal notranslate"><span class="pre">scan_by_key_config</span></code> for device-level scans, as they no longer match the algorithm’s parameters. New configurations <code class="docutils literal notranslate"><span class="pre">scan_config_v2</span></code> and <code class="docutils literal notranslate"><span class="pre">scan_by_key_config_v2</span></code> are preferred instead.</p></li>
</ul>
</section>
<section id="id170">
<h5>Fixed<a class="headerlink" href="#id170" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed build issue caused by missing header in <code class="docutils literal notranslate"><span class="pre">thread/thread_search.hpp</span></code>.</p></li>
</ul>
</section>
</section>
<section id="rocsolver-3-23-0">
<h4>rocSOLVER 3.23.0<a class="headerlink" href="#rocsolver-3-23-0" title="Link to this heading">#</a></h4>
<p>rocSOLVER 3.23.0 for ROCm 5.7.0</p>
<section id="id171">
<h5>Added<a class="headerlink" href="#id171" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>LU factorization without pivoting for block tridiagonal matrices:</p>
<ul>
<li><p>GEBLTTRF_NPVT now supports interleaved_batched format</p></li>
</ul>
</li>
<li><p>Linear system solver without pivoting for block tridiagonal matrices:</p>
<ul>
<li><p>GEBLTTRS_NPVT now supports interleaved_batched format</p></li>
</ul>
</li>
</ul>
</section>
<section id="id172">
<h5>Fixed<a class="headerlink" href="#id172" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed stack overflow in sparse tests on Windows</p></li>
</ul>
</section>
<section id="id173">
<h5>Changed<a class="headerlink" href="#id173" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Changed rocsolver-test sparse input data search paths to be relative to the test executable</p></li>
<li><p>Changed build scripts to default to compressed debug symbols in Debug builds</p></li>
</ul>
</section>
</section>
<section id="rocsparse-2-5-4">
<h4>rocSPARSE 2.5.4<a class="headerlink" href="#rocsparse-2-5-4" title="Link to this heading">#</a></h4>
<p>rocSPARSE 2.5.4 for ROCm 5.7.0</p>
<section id="id174">
<h5>Added<a class="headerlink" href="#id174" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added more mixed precisions for SpMV, (matrix: float, vectors: double, calculation: double) and (matrix: rocsparse_float_complex, vectors: rocsparse_double_complex, calculation: rocsparse_double_complex)</p></li>
<li><p>Added support for gfx940, gfx941 and gfx942</p></li>
</ul>
</section>
<section id="id175">
<h5>Improved<a class="headerlink" href="#id175" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed a bug in csrsm and bsrsm</p></li>
</ul>
</section>
<section id="id176">
<h5>Known Issues<a class="headerlink" href="#id176" title="Link to this heading">#</a></h5>
<p>In csritlu0, the algorithm rocsparse_itilu0_alg_sync_split_fusion has some accuracy issues to investigate with XNACK enabled. The fallback is rocsparse_itilu0_alg_sync_split.</p>
</section>
</section>
<section id="rocwmma-1-2-0">
<h4>rocWMMA 1.2.0<a class="headerlink" href="#rocwmma-1-2-0" title="Link to this heading">#</a></h4>
<p>rocWMMA 1.2.0 for ROCm 5.7.0</p>
<section id="id177">
<h5>Changed<a class="headerlink" href="#id177" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed a bug with synchronization</p></li>
<li><p>Updated rocWMMA cmake versioning</p></li>
</ul>
</section>
</section>
<section id="tensile-4-38-0">
<h4>Tensile 4.38.0<a class="headerlink" href="#tensile-4-38-0" title="Link to this heading">#</a></h4>
<p>Tensile 4.38.0 for ROCm 5.7.0</p>
<section id="id178">
<h5>Added<a class="headerlink" href="#id178" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added support for FP16 Alt Round Near Zero Mode (this feature allows the generation of alternate kernels with intermediate rounding instead of truncation)</p></li>
<li><p>Added user-driven solution selection feature</p></li>
</ul>
</section>
<section id="id179">
<h5>Optimizations<a class="headerlink" href="#id179" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Enabled LocalSplitU with MFMA for I8 data type</p></li>
<li><p>Optimized K mask code in mfmaIter</p></li>
<li><p>Enabled TailLoop code in NoLoadLoop to prefetch global/local read</p></li>
<li><p>Enabled DirectToVgpr in TailLoop for NN, TN, and TT matrix orientations</p></li>
<li><p>Optimized DirectToLds test cases to reduce the test duration</p></li>
</ul>
</section>
<section id="id180">
<h5>Changed<a class="headerlink" href="#id180" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed DGEMM NT custom kernels and related test cases</p></li>
<li><p>Changed noTailLoop logic to apply noTailLoop only for NT</p></li>
<li><p>Changed the range of AssertFree0ElementMultiple and Free1</p></li>
<li><p>Unified aStr, bStr generation code in mfmaIter</p></li>
</ul>
</section>
<section id="id181">
<h5>Fixed<a class="headerlink" href="#id181" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed LocalSplitU mismatch issue for SGEMM</p></li>
<li><p>Fixed BufferStore=0 and Ldc != Ldd case</p></li>
<li><p>Fixed mismatch issue with TailLoop + MatrixInstB &gt; 1</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-6-1">
<h2>ROCm 5.6.1<a class="headerlink" href="#rocm-5-6-1" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable no-duplicate-header -->
<section id="id182">
<h3>What’s new in this release<a class="headerlink" href="#id182" title="Link to this heading">#</a></h3>
<p>ROCm 5.6.1 is a point release with several bug fixes in the HIP runtime.</p>
<section id="hip-5-6-1-for-rocm-5-6-1">
<h4>HIP 5.6.1 (for ROCm 5.6.1)<a class="headerlink" href="#hip-5-6-1-for-rocm-5-6-1" title="Link to this heading">#</a></h4>
</section>
</section>
<section id="id183">
<h3>Defect fixes<a class="headerlink" href="#id183" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemcpy</span></code> device-to-device (inter-device) is now asynchronous with respect to the host</p></li>
<li><p>Enabled xnack+ check in HIP catch2 tests hang when executing tests</p></li>
<li><p>Memory leak when code object files are loaded/unloaded via hipModuleLoad/hipModuleUnload APIs</p></li>
<li><p>Using <code class="docutils literal notranslate"><span class="pre">hipGraphAddMemFreeNode</span></code> no longer results in a crash</p></li>
</ul>
</section>
<section id="library-changes-in-rocm-5-6-1">
<h3>Library changes in ROCM 5.6.1<a class="headerlink" href="#library-changes-in-rocm-5-6-1" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>AMDMIGraphX</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/AMDMIGraphX/releases/tag/rocm-5.6.1">2.5</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.6.1">0.53.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.6.1">2.13.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.6.1">1.0.12</a></p></td>
</tr>
<tr class="row-even"><td><p>hipRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipRAND/releases/tag/rocm-5.6.1">2.10.16</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.6.1">1.8.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p>2.3.6 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.6.1">2.3.7</a></p></td>
</tr>
<tr class="row-odd"><td><p>MIOpen</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/MIOpen/releases/tag/rocm-5.6.1">2.19.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.6.1">2.15.5</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.6.1">2.1.9</a></p></td>
</tr>
<tr class="row-even"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.6.1">3.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.6.1">1.0.23</a></p></td>
</tr>
<tr class="row-even"><td><p>rocm-cmake</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.6.1">0.9.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.6.1">2.13.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.6.1">2.10.17</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.6.1">3.22.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.6.1">2.5.2</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.6.1">2.18.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocWMMA</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.6.1">1.1.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.6.1">4.37.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="hipsparse-2-3-7">
<h4>hipSPARSE 2.3.7<a class="headerlink" href="#hipsparse-2-3-7" title="Link to this heading">#</a></h4>
<p>hipSPARSE 2.3.7 for ROCm 5.6.1</p>
<section id="bugfix">
<h5>Bugfix<a class="headerlink" href="#bugfix" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Reverted an undocumented API change in hipSPARSE 2.3.6 that affected hipsparseSpSV_solve function</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-6-0">
<h2>ROCm 5.6.0<a class="headerlink" href="#rocm-5-6-0" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable no-duplicate-header -->
<!-- markdownlint-disable header-increment -->
<section id="release-highlights">
<h3>Release highlights<a class="headerlink" href="#release-highlights" title="Link to this heading">#</a></h3>
<p>ROCm 5.6 consists of several AI software ecosystem improvements to our fast-growing user base.  A
few examples include:</p>
<ul class="simple">
<li><p>New documentation portal at https://rocm.docs.amd.com</p></li>
<li><p>Ongoing software enhancements for LLMs, ensuring full compliance with the HuggingFace unit test
suite</p></li>
<li><p>OpenAI Triton, CuPy, HIP Graph support, and many other library performance enhancements</p></li>
<li><p>Improved ROCm deployment and development tools, including CPU-GPU (rocGDB) debugger,
profiler, and docker containers</p></li>
<li><p>New pseudorandom generators are available in rocRAND.  Added support for half-precision
transforms in hipFFT/rocFFT.  Added LU refactorization and linear system solver for sparse matrices in
rocSOLVER.</p></li>
</ul>
</section>
<section id="id184">
<h3>OS and GPU support changes<a class="headerlink" href="#id184" title="Link to this heading">#</a></h3>
<ul class="simple">
<li><p>SLES15 SP5 support was added this release. SLES15 SP3 support was dropped.</p></li>
<li><p>AMD Instinct MI50, Radeon Pro VII, and Radeon VII products (collectively referred to as gfx906 GPUs)
will be entering the maintenance mode starting Q3 2023. This will be aligned with ROCm 5.7 GA
release date.</p>
<ul>
<li><p>No new features and performance optimizations will be supported for the gfx906 GPUs beyond
ROCm 5.7</p></li>
<li><p>Bug fixes / critical security patches will continue to be supported for the gfx906 GPUs till Q2 2024
(EOM will be aligned with the closest ROCm release)</p></li>
<li><p>Bug fixes during the maintenance will be made to the next ROCm point release</p></li>
<li><p>Bug fixes will not be back ported to older ROCm releases for this SKU</p></li>
<li><p>Distro / Operating system updates will continue per the ROCm release cadence for gfx906 GPUs till
EOM.</p></li>
</ul>
</li>
</ul>
</section>
<section id="amdsmi-cli-23-0-0-4">
<h3>AMDSMI CLI 23.0.0.4<a class="headerlink" href="#amdsmi-cli-23-0-0-4" title="Link to this heading">#</a></h3>
<section id="id185">
<h4>Additions<a class="headerlink" href="#id185" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>AMDSMI CLI tool enabled for Linux Bare Metal &amp; Guest</p></li>
<li><p>Package: amd-smi-lib</p></li>
</ul>
</section>
<section id="id186">
<h4>Known issues<a class="headerlink" href="#id186" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>not all Error Correction Code (ECC) fields are currently supported</p></li>
<li><p>RHEL 8 &amp; SLES 15 have extra install steps</p></li>
</ul>
</section>
</section>
<section id="kernel-modules-dkms">
<h3>Kernel modules (DKMS)<a class="headerlink" href="#kernel-modules-dkms" title="Link to this heading">#</a></h3>
<section id="id187">
<h4>Fixes<a class="headerlink" href="#id187" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Stability fix for multi GPU system reproducible via ROCm_Bandwidth_Test as reported in
<a class="reference external" href="https://github.com/RadeonOpenCompute/ROCm/issues/2198">Issue 2198</a>.</p></li>
</ul>
</section>
</section>
<section id="hip-5-6-for-rocm-5-6">
<h3>HIP 5.6 (for ROCm 5.6)<a class="headerlink" href="#hip-5-6-for-rocm-5-6" title="Link to this heading">#</a></h3>
<section id="id188">
<h4>Optimizations<a class="headerlink" href="#id188" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Consolidation of hipamd, rocclr and OpenCL projects in clr</p></li>
<li><p>Optimized lock for graph global capture mode</p></li>
</ul>
</section>
<section id="id189">
<h4>Additions<a class="headerlink" href="#id189" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Added hipRTC support for amd_hip_fp16</p></li>
<li><p>Added hipStreamGetDevice implementation to get the device associated with the stream</p></li>
<li><p>Added HIP_AD_FORMAT_SIGNED_INT16 in hipArray formats</p></li>
<li><p>hipArrayGetInfo for getting information about the specified array</p></li>
<li><p>hipArrayGetDescriptor for getting 1D or 2D array descriptor</p></li>
<li><p>hipArray3DGetDescriptor to get 3D array descriptor</p></li>
</ul>
</section>
<section id="id190">
<h4>Changes<a class="headerlink" href="#id190" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>hipMallocAsync to return success for zero size allocation to match hipMalloc</p></li>
<li><p>Separation of hipcc perl binaries from HIP project to hipcc project. hip-devel package depends on newly added hipcc package</p></li>
<li><p>Consolidation of hipamd, ROCclr, and OpenCL repositories into a single repository called clr. Instructions are updated to build HIP from sources in the HIP Installation guide</p></li>
<li><p>Removed hipBusBandwidth and hipCommander samples from hip-tests</p></li>
</ul>
</section>
<section id="id191">
<h4>Fixes<a class="headerlink" href="#id191" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Fixed regression in hipMemCpyParam3D when offset is applied</p></li>
</ul>
</section>
<section id="id192">
<h4>Known issues<a class="headerlink" href="#id192" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Limited testing on xnack+ configuration</p>
<ul>
<li><p>Multiple HIP tests failures (gpuvm fault or hangs)</p></li>
</ul>
</li>
<li><p>hipSetDevice and hipSetDeviceFlags APIs return hipErrorInvalidDevice instead of hipErrorNoDevice, on a system without GPU</p></li>
<li><p>Known memory leak when code object files are loaded/unloaded via hipModuleLoad/hipModuleUnload APIs. Issue will be fixed in a future ROCm release</p></li>
</ul>
</section>
<section id="upcoming-changes-in-future-release">
<h4>Upcoming changes in future release<a class="headerlink" href="#upcoming-changes-in-future-release" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Removal of gcnarch from hipDeviceProp_t structure</p></li>
<li><p>Addition of new fields in hipDeviceProp_t structure</p>
<ul>
<li><p>maxTexture1D</p></li>
<li><p>maxTexture2D</p></li>
<li><p>maxTexture1DLayered</p></li>
<li><p>maxTexture2DLayered</p></li>
<li><p>sharedMemPerMultiprocessor</p></li>
<li><p>deviceOverlap</p></li>
<li><p>asyncEngineCount</p></li>
<li><p>surfaceAlignment</p></li>
<li><p>unifiedAddressing</p></li>
<li><p>computePreemptionSupported</p></li>
<li><p>uuid</p></li>
</ul>
</li>
<li><p>Removal of deprecated code</p>
<ul>
<li><p>hip-hcc codes from hip code tree</p></li>
</ul>
</li>
<li><p>Correct hipArray usage in HIP APIs such as hipMemcpyAtoH and hipMemcpyHtoA</p></li>
<li><p>HIPMEMCPY_3D fields correction (unsigned int -&gt; size_t)</p></li>
<li><p>Renaming of ‘memoryType’ in hipPointerAttribute_t structure to ‘type’</p></li>
</ul>
</section>
</section>
<section id="rocgdb-13-for-rocm-5-6-0">
<h3>ROCgdb-13 (For ROCm 5.6.0)<a class="headerlink" href="#rocgdb-13-for-rocm-5-6-0" title="Link to this heading">#</a></h3>
<section id="id193">
<h4>Optimizations<a class="headerlink" href="#id193" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Improved performances when handling the end of a process with a large number of threads.</p></li>
</ul>
</section>
<section id="id194">
<h4>Known issues<a class="headerlink" href="#id194" title="Link to this heading">#</a></h4>
<ul>
<li><p>On certain configurations, ROCgdb can show the following warning message:</p>
<p><code class="docutils literal notranslate"><span class="pre">warning:</span> <span class="pre">Probes-based</span> <span class="pre">dynamic</span> <span class="pre">linker</span> <span class="pre">interface</span> <span class="pre">failed.</span> <span class="pre">Reverting</span> <span class="pre">to</span> <span class="pre">original</span> <span class="pre">interface.</span></code></p>
<p>This does not affect ROCgdb’s functionalities.</p>
</li>
</ul>
</section>
</section>
<section id="rocprofiler-for-rocm-5-6-0">
<h3>ROCprofiler (for ROCm 5.6.0)<a class="headerlink" href="#rocprofiler-for-rocm-5-6-0" title="Link to this heading">#</a></h3>
<p>In ROCm 5.6 the <code class="docutils literal notranslate"><span class="pre">rocprofilerv1</span></code> and <code class="docutils literal notranslate"><span class="pre">rocprofilerv2</span></code> include and library files of
ROCm 5.5 are split into separate files. The <code class="docutils literal notranslate"><span class="pre">rocmtools</span></code> files that were
deprecated in ROCm 5.5 have been removed.</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>ROCm 5.6</p></th>
<th class="head"><p>rocprofilerv1</p></th>
<th class="head"><p>rocprofilerv2</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>Tool script</strong></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">bin/rocprof</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">bin/rocprofv2</span></code></p></td>
</tr>
<tr class="row-odd"><td><p><strong>API include</strong></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">include/rocprofiler/rocprofiler.h</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">include/rocprofiler/v2/rocprofiler.h</span></code></p></td>
</tr>
<tr class="row-even"><td><p><strong>API library</strong></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">lib/librocprofiler.so.1</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">lib/librocprofiler.so.2</span></code></p></td>
</tr>
</tbody>
</table>
</div>
<p>The ROCm Profiler Tool that uses <code class="docutils literal notranslate"><span class="pre">rocprofilerV1</span></code> can be invoked using the
following command:</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>rocprof<span class="w"> </span>…
</pre></div>
</div>
<p>To write a custom tool based on the <code class="docutils literal notranslate"><span class="pre">rocprofilerV1</span></code> API do the following:</p>
<div class="highlight-C notranslate"><div class="highlight"><pre><span></span><span class="n">main</span><span class="p">.</span><span class="n">c</span><span class="o">:</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;rocprofiler/rocprofiler.h&gt;</span><span class="c1"> // Use the rocprofilerV1 API</span>
<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="c1">// Use the rocprofilerV1 API</span>
<span class="w">  </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>This can be built in the following manner:</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>gcc<span class="w"> </span>main.c<span class="w"> </span>-I/opt/rocm-5.6.0/include<span class="w"> </span>-L/opt/rocm-5.6.0/lib<span class="w"> </span>-lrocprofiler64
</pre></div>
</div>
<p>The resulting <code class="docutils literal notranslate"><span class="pre">a.out</span></code> will depend on
<code class="docutils literal notranslate"><span class="pre">/opt/rocm-5.6.0/lib/librocprofiler64.so.1</span></code>.</p>
<p>The ROCm Profiler that uses <code class="docutils literal notranslate"><span class="pre">rocprofilerV2</span></code> API can be invoked using the
following command:</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>rocprofv2<span class="w"> </span>…
</pre></div>
</div>
<p>To write a custom tool based on the <code class="docutils literal notranslate"><span class="pre">rocprofilerV2</span></code> API do the following:</p>
<div class="highlight-C notranslate"><div class="highlight"><pre><span></span><span class="n">main</span><span class="p">.</span><span class="n">c</span><span class="o">:</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;rocprofiler/v2/rocprofiler.h&gt;</span><span class="c1"> // Use the rocprofilerV2 API</span>
<span class="kt">int</span><span class="w"> </span><span class="n">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="c1">// Use the rocprofilerV2 API</span>
<span class="w">  </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>This can be built in the following manner:</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>gcc<span class="w"> </span>main.c<span class="w"> </span>-I/opt/rocm-5.6.0/include<span class="w"> </span>-L/opt/rocm-5.6.0/lib<span class="w"> </span>-lrocprofiler64-v2
</pre></div>
</div>
<p>The resulting <code class="docutils literal notranslate"><span class="pre">a.out</span></code> will depend on
<code class="docutils literal notranslate"><span class="pre">/opt/rocm-5.6.0/lib/librocprofiler64.so.2</span></code>.</p>
<section id="id195">
<h4>Optimizations<a class="headerlink" href="#id195" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Improved Test Suite</p></li>
</ul>
</section>
<section id="id196">
<h4>Additions<a class="headerlink" href="#id196" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>‘end_time’ need to be disabled in roctx_trace.txt</p></li>
</ul>
</section>
<section id="id197">
<h4>Fixes<a class="headerlink" href="#id197" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>rocprof in ROcm/5.4.0 gpu selector broken.</p></li>
<li><p>rocprof in ROCm/5.4.1 fails to generate kernel info.</p></li>
<li><p>rocprof clobbers LD_PRELOAD.</p></li>
</ul>
</section>
</section>
<section id="library-changes-in-rocm-5-6-0">
<h3>Library changes in ROCM 5.6.0<a class="headerlink" href="#library-changes-in-rocm-5-6-0" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>AMDMIGraphX</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/AMDMIGraphX/releases/tag/rocm-5.6.0">2.5</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.6.0">0.53.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.6.0">2.13.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipFFT</p></td>
<td><p>1.0.11 ⇒ <a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.6.0">1.0.12</a></p></td>
</tr>
<tr class="row-even"><td><p>hipRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipRAND/releases/tag/rocm-5.6.0">2.10.16</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p>1.7.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.6.0">1.8.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p>2.3.5 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.6.0">2.3.6</a></p></td>
</tr>
<tr class="row-odd"><td><p>MIOpen</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/MIOpen/releases/tag/rocm-5.6.0">2.19.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.6.0">2.15.5</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocALUTION</p></td>
<td><p>2.1.8 ⇒ <a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.6.0">2.1.9</a></p></td>
</tr>
<tr class="row-even"><td><p>rocBLAS</p></td>
<td><p>2.47.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.6.0">3.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocFFT</p></td>
<td><p>1.0.22 ⇒ <a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.6.0">1.0.23</a></p></td>
</tr>
<tr class="row-even"><td><p>rocm-cmake</p></td>
<td><p>0.8.1 ⇒ <a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.6.0">0.9.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.6.0">2.13.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.6.0">2.10.17</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSOLVER</p></td>
<td><p>3.21.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.6.0">3.22.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSPARSE</p></td>
<td><p>2.5.1 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.6.0">2.5.2</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocThrust</p></td>
<td><p>2.17.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.6.0">2.18.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocWMMA</p></td>
<td><p>1.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.6.0">1.1.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>Tensile</p></td>
<td><p>4.36.0 ⇒ <a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.6.0">4.37.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="hipfft-1-0-12">
<h4>hipFFT 1.0.12<a class="headerlink" href="#hipfft-1-0-12" title="Link to this heading">#</a></h4>
<p>hipFFT 1.0.12 for ROCm 5.6.0</p>
<section id="id198">
<h5>Added<a class="headerlink" href="#id198" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Implemented the hipfftXtMakePlanMany, hipfftXtGetSizeMany, hipfftXtExec APIs, to allow requesting half-precision transforms.</p></li>
</ul>
</section>
<section id="id199">
<h5>Changed<a class="headerlink" href="#id199" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added –precision argument to benchmark/test clients.  –double is still accepted but is deprecated as a method to request a double-precision transform.</p></li>
</ul>
</section>
</section>
<section id="hipsolver-1-8-0">
<h4>hipSOLVER 1.8.0<a class="headerlink" href="#hipsolver-1-8-0" title="Link to this heading">#</a></h4>
<p>hipSOLVER 1.8.0 for ROCm 5.6.0</p>
<section id="id200">
<h5>Added<a class="headerlink" href="#id200" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added compatibility API with hipsolverRf prefix</p></li>
</ul>
</section>
</section>
<section id="hipsparse-2-3-6">
<h4>hipSPARSE 2.3.6<a class="headerlink" href="#hipsparse-2-3-6" title="Link to this heading">#</a></h4>
<p>hipSPARSE 2.3.6 for ROCm 5.6.0</p>
<section id="id201">
<h5>Added<a class="headerlink" href="#id201" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added SpGEMM algorithms</p></li>
</ul>
</section>
<section id="id202">
<h5>Changed<a class="headerlink" href="#id202" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>For hipsparseXbsr2csr and hipsparseXcsr2bsr, blockDim == 0 now returns HIPSPARSE_STATUS_INVALID_SIZE</p></li>
</ul>
</section>
</section>
<section id="rocalution-2-1-9">
<h4>rocALUTION 2.1.9<a class="headerlink" href="#rocalution-2-1-9" title="Link to this heading">#</a></h4>
<p>rocALUTION 2.1.9 for ROCm 5.6.0</p>
<section id="id203">
<h5>Improved<a class="headerlink" href="#id203" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed synchronization issues in level 1 routines</p></li>
</ul>
</section>
</section>
<section id="rocblas-3-0-0">
<h4>rocBLAS 3.0.0<a class="headerlink" href="#rocblas-3-0-0" title="Link to this heading">#</a></h4>
<p>rocBLAS 3.0.0 for ROCm 5.6.0</p>
<section id="id204">
<h5>Optimizations<a class="headerlink" href="#id204" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved performance of Level 2 rocBLAS GEMV on gfx90a GPU for non-transposed problems having small matrices and larger batch counts. Performance enhanced for problem sizes when m and n &lt;= 32 and batch_count &gt;= 256.</p></li>
<li><p>Improved performance of rocBLAS syr2k for single, double, and double-complex precision, and her2k for double-complex precision. Slightly improved performance for general sizes on gfx90a.</p></li>
</ul>
</section>
<section id="id205">
<h5>Added<a class="headerlink" href="#id205" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added bf16 inputs and f32 compute support to Level 1 rocBLAS Extension functions axpy_ex, scal_ex and nrm2_ex.</p></li>
</ul>
</section>
<section id="id206">
<h5>Deprecated<a class="headerlink" href="#id206" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>trmm inplace is deprecated. It will be replaced by trmm that has both inplace and out-of-place functionality</p></li>
<li><p>rocblas_query_int8_layout_flag() is deprecated and will be removed in a future release</p></li>
<li><p>rocblas_gemm_flags_pack_int8x4 enum is deprecated and will be removed in a future release</p></li>
<li><p>rocblas_set_device_memory_size() is deprecated and will be replaced by a future function rocblas_increase_device_memory_size()</p></li>
<li><p>rocblas_is_user_managing_device_memory() is deprecated and will be removed in a future release</p></li>
</ul>
</section>
<section id="id207">
<h5>Removed<a class="headerlink" href="#id207" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>is_complex helper was deprecated and now removed.  Use rocblas_is_complex instead.</p></li>
<li><p>The enum truncate_t and the value truncate was deprecated and now removed from. It was replaced by rocblas_truncate_t and rocblas_truncate, respectively.</p></li>
<li><p>rocblas_set_int8_type_for_hipblas was deprecated and is now removed.</p></li>
<li><p>rocblas_get_int8_type_for_hipblas was deprecated and is now removed.</p></li>
</ul>
</section>
<section id="id208">
<h5>Dependencies<a class="headerlink" href="#id208" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>build only dependency on python joblib added as used by Tensile build</p></li>
<li><p>fix for cmake install on some OS when performed by install.sh -d –cmake_install</p></li>
</ul>
</section>
<section id="id209">
<h5>Fixed<a class="headerlink" href="#id209" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>make trsm offset calculations 64 bit safe</p></li>
</ul>
</section>
<section id="id210">
<h5>Changed<a class="headerlink" href="#id210" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>refactor rotg test code</p></li>
</ul>
</section>
</section>
<section id="rocfft-1-0-23">
<h4>rocFFT 1.0.23<a class="headerlink" href="#rocfft-1-0-23" title="Link to this heading">#</a></h4>
<p>rocFFT 1.0.23 for ROCm 5.6.0</p>
<section id="id211">
<h5>Added<a class="headerlink" href="#id211" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Implemented half-precision transforms, which can be requested by passing rocfft_precision_half to rocfft_plan_create.</p></li>
<li><p>Implemented a hierarchical solution map which saves how to decompose a problem and the kernels to be used.</p></li>
<li><p>Implemented a first version of offline-tuner to support tuning kernels for C2C/Z2Z problems.</p></li>
</ul>
</section>
<section id="id212">
<h5>Changed<a class="headerlink" href="#id212" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Replaced std::complex with hipComplex data types for data generator.</p></li>
<li><p>FFT plan dimensions are now sorted to be row-major internally where possible, which produces better plans if the dimensions were accidentally specified in a different order (column-major, for example).</p></li>
<li><p>Added –precision argument to benchmark/test clients.  –double is still accepted but is deprecated as a method to request a double-precision transform.</p></li>
</ul>
</section>
<section id="id213">
<h5>Fixed<a class="headerlink" href="#id213" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed over-allocation of LDS in some real-complex kernels, which was resulting in kernel launch failure.</p></li>
</ul>
</section>
</section>
<section id="rocm-cmake-0-9-0">
<h4>rocm-cmake 0.9.0<a class="headerlink" href="#rocm-cmake-0-9-0" title="Link to this heading">#</a></h4>
<p>rocm-cmake 0.9.0 for ROCm 5.6.0</p>
<section id="id214">
<h5>Added<a class="headerlink" href="#id214" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added the option ROCM_HEADER_WRAPPER_WERROR</p>
<ul>
<li><p>Compile-time C macro in the wrapper headers causes errors to be emitted instead of warnings.</p></li>
<li><p>Configure-time CMake option sets the default for the C macro.</p></li>
</ul>
</li>
</ul>
</section>
</section>
<section id="rocsolver-3-22-0">
<h4>rocSOLVER 3.22.0<a class="headerlink" href="#rocsolver-3-22-0" title="Link to this heading">#</a></h4>
<p>rocSOLVER 3.22.0 for ROCm 5.6.0</p>
<section id="id215">
<h5>Added<a class="headerlink" href="#id215" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>LU refactorization for sparse matrices</p>
<ul>
<li><p>CSRRF_ANALYSIS</p></li>
<li><p>CSRRF_SUMLU</p></li>
<li><p>CSRRF_SPLITLU</p></li>
<li><p>CSRRF_REFACTLU</p></li>
</ul>
</li>
<li><p>Linear system solver for sparse matrices</p>
<ul>
<li><p>CSRRF_SOLVE</p></li>
</ul>
</li>
<li><p>Added type <code class="docutils literal notranslate"><span class="pre">rocsolver_rfinfo</span></code> for use with sparse matrix routines</p></li>
</ul>
</section>
<section id="id216">
<h5>Optimized<a class="headerlink" href="#id216" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved the performance of BDSQR and GESVD when singular vectors are requested</p></li>
</ul>
</section>
<section id="id217">
<h5>Fixed<a class="headerlink" href="#id217" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>BDSQR and GESVD should no longer hang when the input contains <code class="docutils literal notranslate"><span class="pre">NaN</span></code> or <code class="docutils literal notranslate"><span class="pre">Inf</span></code></p></li>
</ul>
</section>
</section>
<section id="rocsparse-2-5-2">
<h4>rocSPARSE 2.5.2<a class="headerlink" href="#rocsparse-2-5-2" title="Link to this heading">#</a></h4>
<p>rocSPARSE 2.5.2 for ROCm 5.6.0</p>
<section id="id218">
<h5>Improved<a class="headerlink" href="#id218" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed a memory leak in csritsv</p></li>
<li><p>Fixed a bug in csrsm and bsrsm</p></li>
</ul>
</section>
</section>
<section id="rocthrust-2-18-0">
<h4>rocThrust 2.18.0<a class="headerlink" href="#rocthrust-2-18-0" title="Link to this heading">#</a></h4>
<p>rocThrust 2.18.0 for ROCm 5.6.0</p>
<section id="id219">
<h5>Fixed<a class="headerlink" href="#id219" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">lower_bound</span></code>, <code class="docutils literal notranslate"><span class="pre">upper_bound</span></code>, and <code class="docutils literal notranslate"><span class="pre">binary_search</span></code> failed to compile for certain types.</p></li>
</ul>
</section>
<section id="id220">
<h5>Changed<a class="headerlink" href="#id220" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Updated <code class="docutils literal notranslate"><span class="pre">docs</span></code> directory structure to match the standard of <a class="reference external" href="https://github.com/RadeonOpenCompute/rocm-docs-core">rocm-docs-core</a>.</p></li>
</ul>
</section>
</section>
<section id="rocwmma-1-1-0">
<h4>rocWMMA 1.1.0<a class="headerlink" href="#rocwmma-1-1-0" title="Link to this heading">#</a></h4>
<p>rocWMMA 1.1.0 for ROCm 5.6.0</p>
<section id="id221">
<h5>Added<a class="headerlink" href="#id221" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added cross-lane operation backends (Blend, Permute, Swizzle and Dpp)</p></li>
<li><p>Added GPU kernels for rocWMMA unit test pre-process and post-process operations (fill, validation)</p></li>
<li><p>Added performance gemm samples for half, single and double precision</p></li>
<li><p>Added rocWMMA cmake versioning</p></li>
<li><p>Added vectorized support in coordinate transforms</p></li>
<li><p>Included ROCm smi for runtime clock rate detection</p></li>
<li><p>Added fragment transforms for transpose and change data layout</p></li>
</ul>
</section>
<section id="id222">
<h5>Changed<a class="headerlink" href="#id222" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Default to GPU rocBLAS validation against rocWMMA</p></li>
<li><p>Re-enabled int8 gemm tests on gfx9</p></li>
<li><p>Upgraded to C++17</p></li>
<li><p>Restructured unit test folder for consistency</p></li>
<li><p>Consolidated rocWMMA samples common code</p></li>
</ul>
</section>
</section>
<section id="tensile-4-37-0">
<h4>Tensile 4.37.0<a class="headerlink" href="#tensile-4-37-0" title="Link to this heading">#</a></h4>
<p>Tensile 4.37.0 for ROCm 5.6.0</p>
<section id="id223">
<h5>Added<a class="headerlink" href="#id223" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added user driven tuning API</p></li>
<li><p>Added decision tree fallback feature</p></li>
<li><p>Added SingleBuffer + AtomicAdd option for GlobalSplitU</p></li>
<li><p>DirectToVgpr support for fp16 and Int8 with TN orientation</p></li>
<li><p>Added new test cases for various functions</p></li>
<li><p>Added SingleBuffer algorithm for ZGEMM/CGEMM</p></li>
<li><p>Added joblib for parallel map calls</p></li>
<li><p>Added support for MFMA + LocalSplitU + DirectToVgprA+B</p></li>
<li><p>Added asmcap check for MIArchVgpr</p></li>
<li><p>Added support for MFMA + LocalSplitU</p></li>
<li><p>Added frequency, power, and temperature data to the output</p></li>
</ul>
</section>
<section id="id224">
<h5>Optimizations<a class="headerlink" href="#id224" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved the performance of GlobalSplitU with SingleBuffer algorithm</p></li>
<li><p>Reduced the running time of the extended and pre_checkin tests</p></li>
<li><p>Optimized the Tailloop section of the assembly kernel</p></li>
<li><p>Optimized complex GEMM (fixed vgpr allocation, unified CGEMM and ZGEMM code in MulMIoutAlphaToArch)</p></li>
<li><p>Improved the performance of the second kernel of MultipleBuffer algorithm</p></li>
</ul>
</section>
<section id="id225">
<h5>Changed<a class="headerlink" href="#id225" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Updated custom kernels with 64-bit offsets</p></li>
<li><p>Adapted 64-bit offset arguments for assembly kernels</p></li>
<li><p>Improved temporary register re-use to reduce max sgpr usage</p></li>
<li><p>Removed some restrictions on VectorWidth and DirectToVgpr</p></li>
<li><p>Updated the dependency requirements for Tensile</p></li>
<li><p>Changed the range of AssertSummationElementMultiple</p></li>
<li><p>Modified the error messages for more clarity</p></li>
<li><p>Changed DivideAndReminder to vectorStaticRemainder in case quotient is not used</p></li>
<li><p>Removed dummy vgpr for vectorStaticRemainder</p></li>
<li><p>Removed tmpVgpr parameter from vectorStaticRemainder/Divide/DivideAndReminder</p></li>
<li><p>Removed qReg parameter from vectorStaticRemainder</p></li>
</ul>
</section>
<section id="id226">
<h5>Fixed<a class="headerlink" href="#id226" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed tmp sgpr allocation to avoid over-writing values (alpha)</p></li>
<li><p>64-bit offset parameters for post kernels</p></li>
<li><p>Fixed gfx908 CI test failures</p></li>
<li><p>Fixed offset calculation to prevent overflow for large offsets</p></li>
<li><p>Fixed issues when BufferLoad and BufferStore are equal to zero</p></li>
<li><p>Fixed StoreCInUnroll + DirectToVgpr + no useInitAccVgprOpt mismatch</p></li>
<li><p>Fixed DirectToVgpr + LocalSplitU + FractionalLoad mismatch</p></li>
<li><p>Fixed the memory access error related to StaggerU + large stride</p></li>
<li><p>Fixed ZGEMM 4x4 MatrixInst mismatch</p></li>
<li><p>Fixed DGEMM 4x4 MatrixInst mismatch</p></li>
<li><p>Fixed ASEM + GSU + NoTailLoop opt mismatch</p></li>
<li><p>Fixed AssertSummationElementMultiple + GlobalSplitU issues</p></li>
<li><p>Fixed ASEM + GSU + TailLoop inner unroll</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-5-1">
<h2>ROCm 5.5.1<a class="headerlink" href="#rocm-5-5-1" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable no-duplicate-header -->
<section id="id227">
<h3>What’s new in this release<a class="headerlink" href="#id227" title="Link to this heading">#</a></h3>
<section id="hip-sdk-for-windows">
<h4>HIP SDK for Windows<a class="headerlink" href="#hip-sdk-for-windows" title="Link to this heading">#</a></h4>
<p>AMD is pleased to announce the availability of the HIP SDK for Windows as part
of ROCm software. The
<a class="reference external" href="https://rocm.docs.amd.com/en/docs-5.5.1/release/windows_support.html">HIP SDK OS and GPU support page</a>
lists the versions of Windows and GPUs validated by AMD. HIP SDK features on
Windows are described in detail in our
<a class="reference external" href="https://rocm.docs.amd.com/en/docs-5.5.1/rocm.html#rocm-on-windows">What is ROCm?</a>
page and differs from the Linux feature set. Visit
<a class="reference external" href="https://rocm.docs.amd.com/en/docs-5.5.1/deploy/windows/quick_start.html#">Quick Start</a>
page to get started. Known issues are tracked on
<a class="reference external" href="https://github.com/RadeonOpenCompute/ROCm/issues?q=is%3Aopen+label%3A5.5.1+label%3A%22Verified+Issue%22+label%3AWindows">GitHub</a>.</p>
</section>
<section id="hip-api-change">
<h4>HIP API change<a class="headerlink" href="#hip-api-change" title="Link to this heading">#</a></h4>
<p>The following HIP API is updated in the ROCm 5.5.1 release:</p>
<section id="hipdevicesetcacheconfig">
<h5><code class="docutils literal notranslate"><span class="pre">hipDeviceSetCacheConfig</span></code><a class="headerlink" href="#hipdevicesetcacheconfig" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The return value for <code class="docutils literal notranslate"><span class="pre">hipDeviceSetCacheConfig</span></code> is updated from <code class="docutils literal notranslate"><span class="pre">hipErrorNotSupported</span></code> to
<code class="docutils literal notranslate"><span class="pre">hipSuccess</span></code></p></li>
</ul>
</section>
</section>
</section>
<section id="library-changes-in-rocm-5-5-1">
<h3>Library changes in ROCM 5.5.1<a class="headerlink" href="#library-changes-in-rocm-5-5-1" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>AMDMIGraphX</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/AMDMIGraphX/releases/tag/rocm-5.5.1">2.5</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.5.1">0.54.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.5.1">2.13.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.5.1">1.0.11</a></p></td>
</tr>
<tr class="row-even"><td><p>hipRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipRAND/releases/tag/rocm-5.5.1">2.10.16</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.5.1">1.7.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.5.1">2.3.5</a></p></td>
</tr>
<tr class="row-odd"><td><p>MIOpen</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/MIOpen/releases/tag/rocm-5.5.1">2.19.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.5.1">2.15.5</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.5.1">2.1.8</a></p></td>
</tr>
<tr class="row-even"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.5.1">2.47.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.5.1">1.0.22</a></p></td>
</tr>
<tr class="row-even"><td><p>rocm-cmake</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.5.1">0.8.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.5.1">2.13.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.5.1">2.10.17</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.5.1">3.21.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.5.1">2.5.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.5.1">2.17.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocWMMA</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.5.1">1.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.5.1">4.36.0</a></p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-5-0">
<h2>ROCm 5.5.0<a class="headerlink" href="#rocm-5-5-0" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable no-duplicate-header -->
<section id="id228">
<h3>What’s new in this release<a class="headerlink" href="#id228" title="Link to this heading">#</a></h3>
<section id="hip-enhancements">
<h4>HIP enhancements<a class="headerlink" href="#hip-enhancements" title="Link to this heading">#</a></h4>
<p>The ROCm v5.5 release consists of the following HIP enhancements:</p>
<section id="enhanced-stack-size-limit">
<h5>Enhanced stack size limit<a class="headerlink" href="#enhanced-stack-size-limit" title="Link to this heading">#</a></h5>
<p>In this release, the stack size limit is increased from 16k to 131056 bytes (or 128K - 16).
Applications requiring to update the stack size can use hipDeviceSetLimit API.</p>
</section>
<section id="hipcc-changes">
<h5><code class="docutils literal notranslate"><span class="pre">hipcc</span></code> changes<a class="headerlink" href="#hipcc-changes" title="Link to this heading">#</a></h5>
<p>The following hipcc changes are implemented in this release:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipcc</span></code> will not implicitly link to <code class="docutils literal notranslate"><span class="pre">libpthread</span></code> and <code class="docutils literal notranslate"><span class="pre">librt</span></code>, as they are no longer a link time dependence
for HIP programs.  Applications that depend on these libraries must explicitly link to them.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">-use-staticlib</span></code> and <code class="docutils literal notranslate"><span class="pre">-use-sharedlib</span></code> options are deprecated.</p></li>
</ul>
</section>
<section id="future-changes">
<h5>Future changes<a class="headerlink" href="#future-changes" title="Link to this heading">#</a></h5>
<ul>
<li><p>Separation of <code class="docutils literal notranslate"><span class="pre">hipcc</span></code> binaries (Perl scripts) from HIP to <code class="docutils literal notranslate"><span class="pre">hipcc</span></code> project. Users will access separate
<code class="docutils literal notranslate"><span class="pre">hipcc</span></code> package for installing <code class="docutils literal notranslate"><span class="pre">hipcc</span></code> binaries in future ROCm releases.</p></li>
<li><p>In a future ROCm release, the following samples will be removed from the <code class="docutils literal notranslate"><span class="pre">hip-tests</span></code> project.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipBusbandWidth</span></code> at <a class="github reference external" href="https://github.com/ROCm-Developer-Tools/hip-tests/tree/develop/samples/1_Utils/shipBusBandwidth">ROCm-Developer-Tools/hip-tests</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipCommander</span></code> at <a class="github reference external" href="https://github.com/ROCm-Developer-Tools/hip-tests/tree/develop/samples/1_Utils/hipCommander">ROCm-Developer-Tools/hip-tests</a></p></li>
</ul>
<p>Note that the samples will continue to be available in previous release branches.</p>
</li>
<li><p>Removal of gcnarch from hipDeviceProp_t structure</p></li>
<li><p>Addition of new fields in hipDeviceProp_t structure</p>
<ul class="simple">
<li><p>maxTexture1D</p></li>
<li><p>maxTexture2D</p></li>
<li><p>maxTexture1DLayered</p></li>
<li><p>maxTexture2DLayered</p></li>
<li><p>sharedMemPerMultiprocessor</p></li>
<li><p>deviceOverlap</p></li>
<li><p>asyncEngineCount</p></li>
<li><p>surfaceAlignment</p></li>
<li><p>unifiedAddressing</p></li>
<li><p>computePreemptionSupported</p></li>
<li><p>hostRegisterSupported</p></li>
<li><p>uuid</p></li>
</ul>
</li>
<li><p>Removal of deprecated code</p>
<ul class="simple">
<li><p>hip-hcc codes from hip code tree</p></li>
</ul>
</li>
<li><p>Correct hipArray usage in HIP APIs such as hipMemcpyAtoH and hipMemcpyHtoA</p></li>
<li><p>HIPMEMCPY_3D fields correction to avoid truncation of “size_t” to “unsigned int” inside hipMemcpy3D()</p></li>
<li><p>Renaming of ‘memoryType’ in hipPointerAttribute_t structure to ‘type’</p></li>
<li><p>Correct hipGetLastError to return the last error instead of last API call’s return code</p></li>
<li><p>Update hipExternalSemaphoreHandleDesc to add “unsigned int reserved[16]”</p></li>
<li><p>Correct handling of flag values in hipIpcOpenMemHandle for hipIpcMemLazyEnablePeerAccess</p></li>
<li><p>Remove hiparray* and make it opaque with hipArray_t</p></li>
</ul>
</section>
<section id="new-hip-apis-in-this-release">
<h5>New HIP APIs in this release<a class="headerlink" href="#new-hip-apis-in-this-release" title="Link to this heading">#</a></h5>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This is a pre-official version (beta) release of the new APIs and may contain unresolved issues.</p>
</div>
<section id="memory-management-hip-apis">
<h6>Memory management HIP APIs<a class="headerlink" href="#memory-management-hip-apis" title="Link to this heading">#</a></h6>
<p>The new memory management HIP API is as follows:</p>
<ul>
<li><p>Sets information on the specified pointer [BETA].</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipPointerSetAttribute</span><span class="p">(</span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">value</span><span class="p">,</span><span class="w"> </span><span class="n">hipPointer_attribute</span><span class="w"> </span><span class="n">attribute</span><span class="p">,</span><span class="w"> </span><span class="n">hipDeviceptr_t</span><span class="w"> </span><span class="n">ptr</span><span class="p">);</span>
</pre></div>
</div>
</li>
</ul>
</section>
<section id="module-management-hip-apis">
<h6>Module management HIP APIs<a class="headerlink" href="#module-management-hip-apis" title="Link to this heading">#</a></h6>
<p>The new module management HIP APIs are as follows:</p>
<ul>
<li><p>Launches kernel <span class="math notranslate nohighlight">\(f\)</span> with launch parameters and shared memory on stream with arguments passed
to <code class="docutils literal notranslate"><span class="pre">kernelParams</span></code>, where thread blocks can cooperate and synchronize as they run.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipModuleLaunchCooperativeKernel</span><span class="p">(</span><span class="n">hipFunction_t</span><span class="w"> </span><span class="n">f</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">gridDimX</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">gridDimY</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">gridDimZ</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">blockDimX</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">blockDimY</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">blockDimZ</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">sharedMemBytes</span><span class="p">,</span><span class="w"> </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">stream</span><span class="p">,</span><span class="w"> </span><span class="kt">void</span><span class="o">**</span><span class="w"> </span><span class="n">kernelParams</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Launches kernels on multiple devices where thread blocks can cooperate and synchronize as they
run.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipModuleLaunchCooperativeKernelMultiDevice</span><span class="p">(</span><span class="n">hipFunctionLaunchParams</span><span class="o">*</span><span class="w"> </span><span class="n">launchParamsList</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">numDevices</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">flags</span><span class="p">);</span>
</pre></div>
</div>
</li>
</ul>
</section>
<section id="hip-graph-management-apis">
<h6>HIP graph management APIs<a class="headerlink" href="#hip-graph-management-apis" title="Link to this heading">#</a></h6>
<p>The new HIP graph management APIs are as follows:</p>
<ul>
<li><p>Creates a memory allocation node and adds it to a graph [BETA]</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipGraphAddMemAllocNode</span><span class="p">(</span><span class="n">hipGraphNode_t</span><span class="o">*</span><span class="w"> </span><span class="n">pGraphNode</span><span class="p">,</span><span class="w"> </span><span class="n">hipGraph_t</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">hipGraphNode_t</span><span class="o">*</span><span class="w"> </span><span class="n">pDependencies</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">numDependencies</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemAllocNodeParams</span><span class="o">*</span><span class="w"> </span><span class="n">pNodeParams</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Return parameters for memory allocation node [BETA]</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipGraphMemAllocNodeGetParams</span><span class="p">(</span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">node</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemAllocNodeParams</span><span class="o">*</span><span class="w"> </span><span class="n">pNodeParams</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Creates a memory free node and adds it to a graph [BETA]</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipGraphAddMemFreeNode</span><span class="p">(</span><span class="n">hipGraphNode_t</span><span class="o">*</span><span class="w"> </span><span class="n">pGraphNode</span><span class="p">,</span><span class="w"> </span><span class="n">hipGraph_t</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">hipGraphNode_t</span><span class="o">*</span><span class="w"> </span><span class="n">pDependencies</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">numDependencies</span><span class="p">,</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">dev_ptr</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Returns parameters for memory free node [BETA].</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipGraphMemFreeNodeGetParams</span><span class="p">(</span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">node</span><span class="p">,</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">dev_ptr</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Write a DOT file describing graph structure [BETA].</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipGraphDebugDotPrint</span><span class="p">(</span><span class="n">hipGraph_t</span><span class="w"> </span><span class="n">graph</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">*</span><span class="w"> </span><span class="n">path</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">flags</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Copies attributes from source node to destination node [BETA].</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipGraphKernelNodeCopyAttributes</span><span class="p">(</span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">hSrc</span><span class="p">,</span><span class="w"> </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">hDst</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Enables or disables the specified node in the given graphExec [BETA]</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipGraphNodeSetEnabled</span><span class="p">(</span><span class="n">hipGraphExec_t</span><span class="w"> </span><span class="n">hGraphExec</span><span class="p">,</span><span class="w"> </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">hNode</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">isEnabled</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Query whether a node in the given graphExec is enabled [BETA]</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipGraphNodeGetEnabled</span><span class="p">(</span><span class="n">hipGraphExec_t</span><span class="w"> </span><span class="n">hGraphExec</span><span class="p">,</span><span class="w"> </span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">hNode</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="o">*</span><span class="w"> </span><span class="n">isEnabled</span><span class="p">);</span>
</pre></div>
</div>
</li>
</ul>
</section>
</section>
<section id="openmp-enhancements">
<h5>OpenMP enhancements<a class="headerlink" href="#openmp-enhancements" title="Link to this heading">#</a></h5>
<p>This release consists of the following OpenMP enhancements:</p>
<ul class="simple">
<li><p>Additional support for OMPT functions <code class="docutils literal notranslate"><span class="pre">get_device_time</span></code> and <code class="docutils literal notranslate"><span class="pre">get_record_type</span></code></p></li>
<li><p>Added support for min/max fast fp atomics on AMD GPUs</p></li>
<li><p>Fixed the use of the abs function in C device regions</p></li>
</ul>
</section>
</section>
</section>
<section id="deprecations-and-warnings">
<h3>Deprecations and warnings<a class="headerlink" href="#deprecations-and-warnings" title="Link to this heading">#</a></h3>
<section id="hip-deprecation">
<h4>HIP deprecation<a class="headerlink" href="#hip-deprecation" title="Link to this heading">#</a></h4>
<p>The <code class="docutils literal notranslate"><span class="pre">hipcc</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> Perl scripts are deprecated. In a future release, compiled binaries will be
available as <code class="docutils literal notranslate"><span class="pre">hipcc.bin</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.bin</span></code> as replacements for the Perl scripts.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>There will be a transition period where the Perl scripts and compiled binaries are available before the
scripts are removed. There will be no functional difference between the Perl scripts and their compiled
binary counterpart. No user action is required. Once these are available, users can optionally switch to
<code class="docutils literal notranslate"><span class="pre">hipcc.bin</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.bin</span></code>. The <code class="docutils literal notranslate"><span class="pre">hipcc</span></code>/<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> soft link will be assimilated to point from
<code class="docutils literal notranslate"><span class="pre">hipcc</span></code>/<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> to the respective compiled binaries as the default option.</p>
</div>
<section id="linux-file-system-hierarchy-standard-for-rocm">
<h5>Linux file system hierarchy standard for ROCm<a class="headerlink" href="#linux-file-system-hierarchy-standard-for-rocm" title="Link to this heading">#</a></h5>
<p>ROCm packages have adopted the Linux foundation file system hierarchy standard in this release to ensure ROCm components follow open source conventions for Linux-based distributions. While moving to a new file system hierarchy, ROCm ensures backward compatibility with its 5.1 version or older file system hierarchy. See below for a detailed explanation of the new file system hierarchy and backward compatibility.</p>
</section>
<section id="new-file-system-hierarchy">
<h5>New file system hierarchy<a class="headerlink" href="#new-file-system-hierarchy" title="Link to this heading">#</a></h5>
<p>The following is the new file system hierarchy:4</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>/opt/rocm-&lt;ver&gt;
    | --bin
      | --All externally exposed Binaries
    | --libexec
        | --&lt;component&gt;
            | -- Component specific private non-ISA executables (architecture independent)
    | --include
        | -- &lt;component&gt;
            | --&lt;header files&gt;
    | --lib
        | --lib&lt;soname&gt;.so -&gt; lib&lt;soname&gt;.so.major -&gt; lib&lt;soname&gt;.so.major.minor.patch
            (public libraries linked with application)
        | --&lt;component&gt; (component specific private library, executable data)
        | --&lt;cmake&gt;
            | --components
                | --&lt;component&gt;.config.cmake
    | --share
        | --html/&lt;component&gt;/*.html
        | --info/&lt;component&gt;/*.[pdf, md, txt]
        | --man
        | --doc
            | --&lt;component&gt;
                | --&lt;licenses&gt;
        | --&lt;component&gt;
            | --&lt;misc files&gt; (arch independent non-executable)
            | --samples
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>ROCm will not support backward compatibility with the v5.1(old) file system hierarchy in its next major
release.</p>
</div>
<p>For more information, refer to <a class="reference external" href="https://refspecs.linuxfoundation.org/fhs.shtml">https://refspecs.linuxfoundation.org/fhs.shtml</a>.</p>
</section>
<section id="backward-compatibility-with-older-file-systems">
<h5>Backward compatibility with older file systems<a class="headerlink" href="#backward-compatibility-with-older-file-systems" title="Link to this heading">#</a></h5>
<p>ROCm has moved header files and libraries to its new location as indicated in the above structure and
included symbolic-link and wrapper header files in its old location for backward compatibility.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>ROCm will continue supporting backward compatibility until the next major release.</p>
</div>
</section>
<section id="wrapper-header-files">
<h5>Wrapper header files<a class="headerlink" href="#wrapper-header-files" title="Link to this heading">#</a></h5>
<p>Wrapper header files are placed in the old location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/include</span></code>) with a
warning message to include files from the new location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/include</span></code>) as shown in the
example below:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Code snippet from hip_runtime.h</span>
<span class="cp">#pragma message “This file is deprecated. Use file from include path /opt/rocm-ver/include/ and prefix with hip”.</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">"hip/hip_runtime.h"</span>
</pre></div>
</div>
<p>The wrapper header files’ backward compatibility deprecation is as follows:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">#pragma</span></code> message announcing deprecation – ROCm v5.2 release</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">#pragma</span></code> message changed to <code class="docutils literal notranslate"><span class="pre">#warning</span></code> – Future release</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">#warning</span></code> changed to <code class="docutils literal notranslate"><span class="pre">#error</span></code> – Future release</p></li>
<li><p>Backward compatibility wrappers removed – Future release</p></li>
</ul>
</section>
<section id="library-files">
<h5>Library files<a class="headerlink" href="#library-files" title="Link to this heading">#</a></h5>
<p>Library files are available in the <code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/lib</span></code> folder. For backward compatibility, the old library
location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/lib</span></code>) has a soft link to the library at the new location.</p>
<p>Example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>ls<span class="w"> </span>-l<span class="w"> </span>/opt/rocm/hip/lib/
total<span class="w"> </span><span class="m">4</span>
drwxr-xr-x<span class="w"> </span><span class="m">4</span><span class="w"> </span>root<span class="w"> </span>root<span class="w"> </span><span class="m">4096</span><span class="w"> </span>May<span class="w"> </span><span class="m">12</span><span class="w"> </span><span class="m">10</span>:45<span class="w"> </span>cmake
lrwxrwxrwx<span class="w"> </span><span class="m">1</span><span class="w"> </span>root<span class="w"> </span>root<span class="w">   </span><span class="m">24</span><span class="w"> </span>May<span class="w"> </span><span class="m">10</span><span class="w"> </span><span class="m">23</span>:32<span class="w"> </span>libamdhip64.so<span class="w"> </span>-&gt;<span class="w"> </span>../../lib/libamdhip64.so
</pre></div>
</div>
</section>
<section id="cmake-config-files">
<h5>CMake config files<a class="headerlink" href="#cmake-config-files" title="Link to this heading">#</a></h5>
<p>All CMake configuration files are available in the <code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/lib/cmake/&lt;component&gt;</span></code> folder.
For backward compatibility, the old CMake locations (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/lib/cmake</span></code>)
consist of a soft link to the new CMake config.</p>
<p>Example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>ls<span class="w"> </span>-l<span class="w"> </span>/opt/rocm/hip/lib/cmake/hip/
total<span class="w"> </span><span class="m">0</span>
lrwxrwxrwx<span class="w"> </span><span class="m">1</span><span class="w"> </span>root<span class="w"> </span>root<span class="w"> </span><span class="m">42</span><span class="w"> </span>May<span class="w"> </span><span class="m">10</span><span class="w"> </span><span class="m">23</span>:32<span class="w"> </span>hip-config.cmake<span class="w"> </span>-&gt;<span class="w"> </span>../../../../lib/cmake/hip/hip-config.cmake
</pre></div>
</div>
</section>
</section>
<section id="rocm-support-for-code-object-v3-deprecated">
<h4>ROCm support for Code Object V3 deprecated<a class="headerlink" href="#rocm-support-for-code-object-v3-deprecated" title="Link to this heading">#</a></h4>
<p>Support for Code Object v3 is deprecated and will be removed in a future release.</p>
</section>
<section id="comgr-v3-0-changes">
<h4>Comgr V3.0 changes<a class="headerlink" href="#comgr-v3-0-changes" title="Link to this heading">#</a></h4>
<p>The following APIs and macros have been marked as deprecated. These are expected to be removed in
a future ROCm release and coincides with the release of Comgr v3.0.</p>
<section id="api-changes">
<h5>API changes<a class="headerlink" href="#api-changes" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">amd_comgr_action_info_set_options()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amd_comgr_action_info_get_options()</span></code></p></li>
</ul>
</section>
<section id="actions-and-data-types">
<h5>Actions and data types<a class="headerlink" href="#actions-and-data-types" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">AMD_COMGR_ACTION_ADD_DEVICE_LIBRARIES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">AMD_COMGR_ACTION_COMPILE_SOURCE_TO_FATBIN</span></code></p></li>
</ul>
<p>For replacements, see the <code class="docutils literal notranslate"><span class="pre">AMD_COMGR_ACTION_INFO_GET</span></code>/<code class="docutils literal notranslate"><span class="pre">SET_OPTION_LIST</span> <span class="pre">APIs</span></code>, and the
<code class="docutils literal notranslate"><span class="pre">AMD_COMGR_ACTION_COMPILE_SOURCE_(WITH_DEVICE_LIBS)_TO_BC</span></code> macros.</p>
</section>
</section>
<section id="deprecated-environment-variables">
<h4>Deprecated environment variables<a class="headerlink" href="#deprecated-environment-variables" title="Link to this heading">#</a></h4>
<p>The following environment variables are removed in this ROCm release:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_MAX_COMMAND_QUEUES</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_MAX_WORKGROUP_SIZE_2D_X</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_MAX_WORKGROUP_SIZE_2D_Y</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_MAX_WORKGROUP_SIZE_3D_X</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_MAX_WORKGROUP_SIZE_3D_Y</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_MAX_WORKGROUP_SIZE_3D_Z</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_BLIT_ENGINE_TYPE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_USE_SYNC_OBJECTS</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">AMD_OCL_SC_LIB</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">AMD_OCL_ENABLE_MESSAGE_BOX</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_FORCE_64BIT_PTR</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_FORCE_OCL20_32BIT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_RAW_TIMESTAMP</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_SELECT_COMPUTE_RINGS_ID</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_USE_SINGLE_SCRATCH</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_ENABLE_LARGE_ALLOCATION</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HSA_LOCAL_MEMORY_ENABLE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HSA_ENABLE_COARSE_GRAIN_SVM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GPU_IFH_MODE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">OCL_SYSMEM_REQUIREMENT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">OCL_CODE_CACHE_ENABLE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">OCL_CODE_CACHE_RESET</span></code></p></li>
</ul>
</section>
</section>
<section id="known-issues-in-this-release">
<h3>Known issues in this release<a class="headerlink" href="#known-issues-in-this-release" title="Link to this heading">#</a></h3>
<p>The following are the known issues in this release.</p>
<section id="distributed-test-distributed-spawn-fails">
<h4><code class="docutils literal notranslate"><span class="pre">DISTRIBUTED</span></code>/<code class="docutils literal notranslate"><span class="pre">TEST_DISTRIBUTED_SPAWN</span></code> fails<a class="headerlink" href="#distributed-test-distributed-spawn-fails" title="Link to this heading">#</a></h4>
<p>When user applications call <code class="docutils literal notranslate"><span class="pre">ncclCommAbort</span></code> to destruct communicators and then create new
communicators repeatedly, subsequent communicators may fail to initialize.</p>
<p>This issue is under investigation and will be resolved in a future release.</p>
</section>
</section>
<section id="library-changes-in-rocm-5-5-0">
<h3>Library changes in ROCM 5.5.0<a class="headerlink" href="#library-changes-in-rocm-5-5-0" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>AMDMIGraphX</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/AMDMIGraphX/releases/tag/rocm-5.5.0">2.5</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipBLAS</p></td>
<td><p>0.53.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.5.0">0.54.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipCUB</p></td>
<td><p>2.13.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.5.0">2.13.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipFFT</p></td>
<td><p>1.0.10 ⇒ <a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.5.0">1.0.11</a></p></td>
</tr>
<tr class="row-even"><td><p>hipRAND</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/hipRAND/releases/tag/rocm-5.5.0">2.10.16</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p>1.6.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.5.0">1.7.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p>2.3.3 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.5.0">2.3.5</a></p></td>
</tr>
<tr class="row-odd"><td><p>MIOpen</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/MIOpen/releases/tag/rocm-5.5.0">2.19.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rccl</p></td>
<td><p>2.13.4 ⇒ <a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.5.0">2.15.5</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocALUTION</p></td>
<td><p>2.1.3 ⇒ <a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.5.0">2.1.8</a></p></td>
</tr>
<tr class="row-even"><td><p>rocBLAS</p></td>
<td><p>2.46.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.5.0">2.47.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocFFT</p></td>
<td><p>1.0.21 ⇒ <a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.5.0">1.0.22</a></p></td>
</tr>
<tr class="row-even"><td><p>rocm-cmake</p></td>
<td><p>0.8.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.5.0">0.8.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocPRIM</p></td>
<td><p>2.12.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.5.0">2.13.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocRAND</p></td>
<td><p>2.10.16 ⇒ <a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.5.0">2.10.17</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSOLVER</p></td>
<td><p>3.20.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.5.0">3.21.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSPARSE</p></td>
<td><p>2.4.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.5.0">2.5.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.5.0">2.17.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocWMMA</p></td>
<td><p>0.9 ⇒ <a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.5.0">1.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>Tensile</p></td>
<td><p>4.35.0 ⇒ <a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.5.0">4.36.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="amdmigraphx-2-5">
<h4>AMDMIGraphX 2.5<a class="headerlink" href="#amdmigraphx-2-5" title="Link to this heading">#</a></h4>
<p>MIGraphX 2.5 for ROCm 5.5.0</p>
<section id="id229">
<h5>Added<a class="headerlink" href="#id229" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Y-Model feature to store tuning information with the optimized model</p></li>
<li><p>Added Python 3.10 bindings</p></li>
<li><p>Accuracy checker tool based on ONNX Runtime</p></li>
<li><p>ONNX Operators parse_split, and Trilu</p></li>
<li><p>Build support for ROCm MLIR</p></li>
<li><p>Added migraphx-driver flag to print optimizations in python (–python)</p></li>
<li><p>Added JIT implementation of the Gather and Pad operator which results in better handling of larger tensor sizes.</p></li>
</ul>
</section>
<section id="id230">
<h5>Optimizations<a class="headerlink" href="#id230" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved performance of Transformer based models</p></li>
<li><p>Improved performance of the Pad, Concat, Gather, and Pointwise operators</p></li>
<li><p>Improved onnx/pb file loading speed</p></li>
<li><p>Added general optimize pass which runs several passes such as simplify_reshapes/algebra and DCE in loop.</p></li>
</ul>
</section>
<section id="id231">
<h5>Fixed<a class="headerlink" href="#id231" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved parsing Tensorflow Protobuf files</p></li>
<li><p>Resolved various accuracy issues with some onnx models</p></li>
<li><p>Resolved a gcc-12 issue with mivisionx</p></li>
<li><p>Improved support for larger sized models and batches</p></li>
<li><p>Use –offload-arch instead of –cuda-gpu-arch for the HIP compiler</p></li>
<li><p>Changes inside JIT to use float accumulator for large reduce ops of half type to avoid overflow.</p></li>
<li><p>Changes inside JIT to temporarily use cosine to compute sine function.</p></li>
</ul>
</section>
<section id="id232">
<h5>Changed<a class="headerlink" href="#id232" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Changed version/location of 3rd party build dependencies to pick up fixes</p></li>
</ul>
</section>
</section>
<section id="hipblas-0-54-0">
<h4>hipBLAS 0.54.0<a class="headerlink" href="#hipblas-0-54-0" title="Link to this heading">#</a></h4>
<p>hipBLAS 0.54.0 for ROCm 5.5.0</p>
<section id="id233">
<h5>Added<a class="headerlink" href="#id233" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>added option to opt-in to use __half for hipblasHalf type in the API for c++ users who define HIPBLAS_USE_HIP_HALF</p></li>
<li><p>added scripts to plot performance for multiple functions</p></li>
<li><p>data driven hipblas-bench and hipblas-test execution via external yaml format data files</p></li>
<li><p>client smoke test added for quick validation using command hipblas-test –yaml hipblas_smoke.yaml</p></li>
</ul>
</section>
<section id="id234">
<h5>Fixed<a class="headerlink" href="#id234" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>fixed datatype conversion functions to support more rocBLAS/cuBLAS datatypes</p></li>
<li><p>fixed geqrf to return successfully when nullptrs are passed in with n == 0 || m == 0</p></li>
<li><p>fixed getrs to return successfully when given nullptrs with corresponding size = 0</p></li>
<li><p>fixed getrs to give info = -1 when transpose is not an expected type</p></li>
<li><p>fixed gels to return successfully when given nullptrs with corresponding size = 0</p></li>
<li><p>fixed gels to give info = -1 when transpose is not in (‘N’, ‘T’) for real cases or not in (‘N’, ‘C’) for complex cases</p></li>
</ul>
</section>
<section id="id235">
<h5>Changed<a class="headerlink" href="#id235" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>changed reference code for Windows to OpenBLAS</p></li>
<li><p>hipblas client executables all now begin with hipblas- prefix</p></li>
</ul>
</section>
</section>
<section id="hipcub-2-13-1">
<h4>hipCUB 2.13.1<a class="headerlink" href="#hipcub-2-13-1" title="Link to this heading">#</a></h4>
<p>hipCUB 2.13.1 for ROCm 5.5.0</p>
<section id="id236">
<h5>Added<a class="headerlink" href="#id236" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Benchmarks for <code class="docutils literal notranslate"><span class="pre">BlockShuffle</span></code>, <code class="docutils literal notranslate"><span class="pre">BlockLoad</span></code>, and <code class="docutils literal notranslate"><span class="pre">BlockStore</span></code>.</p></li>
</ul>
</section>
<section id="id237">
<h5>Changed<a class="headerlink" href="#id237" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>CUB backend references CUB and Thrust version 1.17.2.</p></li>
<li><p>Improved benchmark coverage of <code class="docutils literal notranslate"><span class="pre">BlockScan</span></code> by adding <code class="docutils literal notranslate"><span class="pre">ExclusiveScan</span></code>, benchmark coverage of <code class="docutils literal notranslate"><span class="pre">BlockRadixSort</span></code> by adding <code class="docutils literal notranslate"><span class="pre">SortBlockedToStriped</span></code>, and benchmark coverage of <code class="docutils literal notranslate"><span class="pre">WarpScan</span></code> by adding <code class="docutils literal notranslate"><span class="pre">Broadcast</span></code>.</p></li>
</ul>
</section>
<section id="id238">
<h5>Fixed<a class="headerlink" href="#id238" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Windows HIP SDK support</p></li>
</ul>
</section>
<section id="id239">
<h5>Known Issues<a class="headerlink" href="#id239" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">BlockRadixRankMatch</span></code> is currently broken under the rocPRIM backend.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">BlockRadixRankMatch</span></code> with a warp size that does not exactly divide the block size is broken under the CUB backend.</p></li>
</ul>
</section>
</section>
<section id="hipfft-1-0-11">
<h4>hipFFT 1.0.11<a class="headerlink" href="#hipfft-1-0-11" title="Link to this heading">#</a></h4>
<p>hipFFT 1.0.11 for ROCm 5.5.0</p>
<section id="id240">
<h5>Fixed<a class="headerlink" href="#id240" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed old version rocm include/lib folders not removed on upgrade.</p></li>
</ul>
</section>
</section>
<section id="hiprand-2-10-16">
<h4>hipRAND 2.10.16<a class="headerlink" href="#hiprand-2-10-16" title="Link to this heading">#</a></h4>
<p>hipRAND 2.10.16 for ROCm 5.5.0</p>
<section id="id241">
<h5>Added<a class="headerlink" href="#id241" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>rocRAND backend support for Sobol 64, Scrambled Sobol 32 and 64, and MT19937.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hiprandGenerateLongLong</span></code> for generating 64-bits uniformly distributed integers with Sobol 64 and Scrambled Sobol 64.</p></li>
</ul>
</section>
<section id="id242">
<h5>Changed<a class="headerlink" href="#id242" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Python 2.7 is no longer officially supported.</p></li>
</ul>
</section>
</section>
<section id="hipsolver-1-7-0">
<h4>hipSOLVER 1.7.0<a class="headerlink" href="#hipsolver-1-7-0" title="Link to this heading">#</a></h4>
<p>hipSOLVER 1.7.0 for ROCm 5.5.0</p>
<section id="id243">
<h5>Added<a class="headerlink" href="#id243" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added functions</p>
<ul>
<li><p>gesvdj</p>
<ul>
<li><p>hipsolverSgesvdj_bufferSize, hipsolverDgesvdj_bufferSize, hipsolverCgesvdj_bufferSize, hipsolverZgesvdj_bufferSize</p></li>
<li><p>hipsolverSgesvdj, hipsolverDgesvdj, hipsolverCgesvdj, hipsolverZgesvdj</p></li>
</ul>
</li>
<li><p>gesvdjBatched</p>
<ul>
<li><p>hipsolverSgesvdjBatched_bufferSize, hipsolverDgesvdjBatched_bufferSize, hipsolverCgesvdjBatched_bufferSize, hipsolverZgesvdjBatched_bufferSize</p></li>
<li><p>hipsolverSgesvdjBatched, hipsolverDgesvdjBatched, hipsolverCgesvdjBatched, hipsolverZgesvdjBatched</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</section>
</section>
<section id="hipsparse-2-3-5">
<h4>hipSPARSE 2.3.5<a class="headerlink" href="#hipsparse-2-3-5" title="Link to this heading">#</a></h4>
<p>hipSPARSE 2.3.5 for ROCm 5.5.0</p>
<section id="id244">
<h5>Improved<a class="headerlink" href="#id244" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed an issue, where the rocm folder was not removed on upgrade of meta packages</p></li>
<li><p>Fixed a compilation issue with cusparse backend</p></li>
<li><p>Added more detailed messages on unit test failures due to missing input data</p></li>
<li><p>Improved documentation</p></li>
<li><p>Fixed a bug with deprecation messages when using gcc9 (Thanks @Maetveis)</p></li>
</ul>
</section>
</section>
<section id="id245">
<h4>MIOpen 2.19.0<a class="headerlink" href="#id245" title="Link to this heading">#</a></h4>
<p>MIOpen 2.19.0 for ROCm 5.5.0</p>
<section id="id246">
<h5>Added<a class="headerlink" href="#id246" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>ROCm 5.5 support for gfx1101 (Navi32)</p></li>
</ul>
</section>
<section id="id247">
<h5>Changed<a class="headerlink" href="#id247" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Tuning results for MLIR on ROCm 5.5</p></li>
<li><p>Bumping MLIR commit to 5.5.0 release tag</p></li>
</ul>
</section>
<section id="id248">
<h5>Fixed<a class="headerlink" href="#id248" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fix 3d convolution Host API bug</p></li>
<li><p>[HOTFIX][MI200][FP16] Disabled ConvHipImplicitGemmBwdXdlops when FP16_ALT is required.</p></li>
</ul>
</section>
</section>
<section id="id249">
<h4>rccl 2.15.5<a class="headerlink" href="#id249" title="Link to this heading">#</a></h4>
<p>RCCL 2.15.5 for ROCm 5.5.0</p>
<section id="id250">
<h5>Changed<a class="headerlink" href="#id250" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Compatibility with NCCL 2.15.5</p></li>
<li><p>Unit test executable renamed to rccl-UnitTests</p></li>
</ul>
</section>
<section id="id251">
<h5>Added<a class="headerlink" href="#id251" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>HW-topology aware binary tree implementation</p></li>
<li><p>Experimental support for MSCCL</p></li>
<li><p>New unit tests for hipGraph support</p></li>
<li><p>NPKit integration</p></li>
</ul>
</section>
<section id="id252">
<h5>Fixed<a class="headerlink" href="#id252" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>rocm-smi ID conversion</p></li>
<li><p>Support for HIP_VISIBLE_DEVICES for unit tests</p></li>
<li><p>Support for p2p transfers to non (HIP) visible devices</p></li>
</ul>
</section>
<section id="id253">
<h5>Removed<a class="headerlink" href="#id253" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed TransferBench from tools.  Exists in standalone repo: https://github.com/ROCmSoftwarePlatform/TransferBench</p></li>
</ul>
</section>
</section>
<section id="rocalution-2-1-8">
<h4>rocALUTION 2.1.8<a class="headerlink" href="#rocalution-2-1-8" title="Link to this heading">#</a></h4>
<p>rocALUTION 2.1.8 for ROCm 5.5.0</p>
<section id="id254">
<h5>Added<a class="headerlink" href="#id254" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added build support for Navi32</p></li>
</ul>
</section>
<section id="id255">
<h5>Improved<a class="headerlink" href="#id255" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed a typo in MPI backend</p></li>
<li><p>Fixed a bug with the backend when HIP support is disabled</p></li>
<li><p>Fixed a bug in SAAMG hierarchy building on HIP backend</p></li>
<li><p>Improved SAAMG hierarchy build performance on HIP backend</p></li>
</ul>
</section>
<section id="id256">
<h5>Changed<a class="headerlink" href="#id256" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>LocalVector::GetIndexValues(ValueType*) is deprecated, use LocalVector::GetIndexValues(const LocalVector&amp;, LocalVector*) instead</p></li>
<li><p>LocalVector::SetIndexValues(const ValueType*) is deprecated, use LocalVector::SetIndexValues(const LocalVector&amp;, const LocalVector&amp;) instead</p></li>
<li><p>LocalMatrix::RSDirectInterpolation(const LocalVector&amp;, const LocalVector&amp;, LocalMatrix*, LocalMatrix*) is deprecated, use LocalMatrix::RSDirectInterpolation(const LocalVector&amp;, const LocalVector&amp;, LocalMatrix*) instead</p></li>
<li><p>LocalMatrix::RSExtPIInterpolation(const LocalVector&amp;, const LocalVector&amp;, bool, float, LocalMatrix*, LocalMatrix*) is deprecated, use LocalMatrix::RSExtPIInterpolation(const LocalVector&amp;, const LocalVector&amp;, bool, LocalMatrix*) instead</p></li>
<li><p>LocalMatrix::RugeStueben() is deprecated</p></li>
<li><p>LocalMatrix::AMGSmoothedAggregation(ValueType, const LocalVector&amp;, const LocalVector&amp;, LocalMatrix*, LocalMatrix*, int) is deprecated, use LocalMatrix::AMGAggregation(ValueType, const LocalVector&amp;, const LocalVector&amp;, LocalMatrix*, int) instead</p></li>
<li><p>LocalMatrix::AMGAggregation(const LocalVector&amp;, LocalMatrix*, LocalMatrix*) is deprecated, use LocalMatrix::AMGAggregation(const LocalVector&amp;, LocalMatrix*) instead</p></li>
</ul>
</section>
</section>
<section id="rocblas-2-47-0">
<h4>rocBLAS 2.47.0<a class="headerlink" href="#rocblas-2-47-0" title="Link to this heading">#</a></h4>
<p>rocBLAS 2.47.0 for ROCm 5.5.0</p>
<section id="id257">
<h5>Added<a class="headerlink" href="#id257" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>added functionality rocblas_geam_ex for matrix-matrix minimum operations</p></li>
<li><p>added HIP Graph support as beta feature for rocBLAS Level 1, Level 2, and Level 3(pointer mode host) functions</p></li>
<li><p>added beta features API. Exposed using compiler define ROCBLAS_BETA_FEATURES_API</p></li>
<li><p>added support for vector initialization in the rocBLAS test framework with negative increments</p></li>
<li><p>added windows build documentation for forthcoming support using ROCm HIP SDK</p></li>
<li><p>added scripts to plot performance for multiple functions</p></li>
</ul>
</section>
<section id="id258">
<h5>Optimizations<a class="headerlink" href="#id258" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>improved performance of Level 2 rocBLAS GEMV for float and double precision. Performance enhanced by 150-200% for certain problem sizes when (m==n) measured on a gfx90a GPU.</p></li>
<li><p>improved performance of Level 2 rocBLAS GER for float, double and complex float precisions. Performance enhanced by 5-7% for certain problem sizes measured on a gfx90a GPU.</p></li>
<li><p>improved performance of Level 2 rocBLAS SYMV for float and double precisions. Performance enhanced by 120-150% for certain problem sizes measured on both gfx908 and gfx90a GPUs.</p></li>
</ul>
</section>
<section id="id259">
<h5>Fixed<a class="headerlink" href="#id259" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>fixed setting of executable mode on client script rocblas_gentest.py to avoid potential permission errors with clients rocblas-test and rocblas-bench</p></li>
<li><p>fixed deprecated API compatibility with Visual Studio compiler</p></li>
<li><p>fixed test framework memory exception handling for Level 2 functions when the host memory allocation exceeds the available memory</p></li>
</ul>
</section>
<section id="id260">
<h5>Changed<a class="headerlink" href="#id260" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>install.sh internally runs rmake.py (also used on windows) and rmake.py may be used directly by developers on linux (use –help)</p></li>
<li><p>rocblas client executables all now begin with rocblas- prefix</p></li>
</ul>
</section>
<section id="id261">
<h5>Removed<a class="headerlink" href="#id261" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>install.sh removed options -o –cov as now Tensile will use the default COV format, set by cmake define Tensile_CODE_OBJECT_VERSION=default</p></li>
</ul>
</section>
</section>
<section id="rocfft-1-0-22">
<h4>rocFFT 1.0.22<a class="headerlink" href="#rocfft-1-0-22" title="Link to this heading">#</a></h4>
<p>rocFFT 1.0.22 for ROCm 5.5.0</p>
<section id="id262">
<h5>Optimizations<a class="headerlink" href="#id262" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved performance of 1D lengths &lt; 2048 that use Bluestein’s algorithm.</p></li>
<li><p>Reduced time for generating code during plan creation.</p></li>
<li><p>Optimized 3D R2C/C2R lengths 32, 84, 128.</p></li>
<li><p>Optimized batched small 1D R2C/C2R cases.</p></li>
</ul>
</section>
<section id="id263">
<h5>Added<a class="headerlink" href="#id263" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added gfx1101 to default AMDGPU_TARGETS.</p></li>
</ul>
</section>
<section id="id264">
<h5>Changed<a class="headerlink" href="#id264" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Moved client programs to C++17.</p></li>
<li><p>Moved planar kernels and infrequently used Stockham kernels to be runtime-compiled.</p></li>
<li><p>Moved transpose, real-complex, Bluestein, and Stockham kernels to library kernel cache.</p></li>
</ul>
</section>
<section id="id265">
<h5>Fixed<a class="headerlink" href="#id265" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed zero-length twiddle table allocations, which fixes errors from hipMallocManaged.</p></li>
<li><p>Fixed incorrect freeing of HIP stream handles during twiddle computation when multiple devices are present.</p></li>
</ul>
</section>
</section>
<section id="rocm-cmake-0-8-1">
<h4>rocm-cmake 0.8.1<a class="headerlink" href="#rocm-cmake-0-8-1" title="Link to this heading">#</a></h4>
<p>rocm-cmake 0.8.1 for ROCm 5.5.0</p>
<section id="id266">
<h5>Fixed<a class="headerlink" href="#id266" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>ROCMInstallTargets: Added compatibility symlinks for included cmake files in <code class="docutils literal notranslate"><span class="pre">&amp;lt;ROCM&amp;gt;/lib/cmake/&amp;lt;PACKAGE&amp;gt;</span></code>.</p></li>
</ul>
</section>
<section id="id267">
<h5>Changed<a class="headerlink" href="#id267" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>ROCMHeaderWrapper: The wrapper header deprecation message is now a deprecation warning.</p></li>
</ul>
</section>
</section>
<section id="rocprim-2-13-0">
<h4>rocPRIM 2.13.0<a class="headerlink" href="#rocprim-2-13-0" title="Link to this heading">#</a></h4>
<p>rocPRIM 2.13.0 for ROCm 5.5.0</p>
<section id="id268">
<h5>Added<a class="headerlink" href="#id268" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>New block level <code class="docutils literal notranslate"><span class="pre">radix_rank</span></code> primitive.</p></li>
<li><p>New block level <code class="docutils literal notranslate"><span class="pre">radix_rank_match</span></code> primitive.</p></li>
</ul>
</section>
<section id="id269">
<h5>Changed<a class="headerlink" href="#id269" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved the performance of <code class="docutils literal notranslate"><span class="pre">block_radix_sort</span></code> and <code class="docutils literal notranslate"><span class="pre">device_radix_sort</span></code>.</p></li>
</ul>
</section>
<section id="id270">
<h5>Known Issues<a class="headerlink" href="#id270" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Disabled GPU error messages relating to incorrect warp operation usage with Navi GPUs on Windows, due to GPU printf performance issues on Windows.</p></li>
</ul>
</section>
<section id="id271">
<h5>Fixed<a class="headerlink" href="#id271" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed benchmark build on Windows</p></li>
</ul>
</section>
</section>
<section id="id272">
<h4>rocRAND 2.10.17<a class="headerlink" href="#id272" title="Link to this heading">#</a></h4>
<p>rocRAND 2.10.17 for ROCm 5.5.0</p>
<section id="id273">
<h5>Added<a class="headerlink" href="#id273" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>MT19937 pseudo random number generator based on M. Matsumoto and T. Nishimura, 1998, Mersenne Twister: A 623-dimensionally equidistributed uniform pseudorandom number generator.</p></li>
<li><p>New benchmark for the device API using Google Benchmark, <code class="docutils literal notranslate"><span class="pre">benchmark_rocrand_device_api</span></code>, replacing <code class="docutils literal notranslate"><span class="pre">benchmark_rocrand_kernel</span></code>. <code class="docutils literal notranslate"><span class="pre">benchmark_rocrand_kernel</span></code> is deprecated and will be removed in a future version. Likewise, <code class="docutils literal notranslate"><span class="pre">benchmark_curand_host_api</span></code> is added to replace <code class="docutils literal notranslate"><span class="pre">benchmark_curand_generate</span></code> and <code class="docutils literal notranslate"><span class="pre">benchmark_curand_device_api</span></code> is added to replace <code class="docutils literal notranslate"><span class="pre">benchmark_curand_kernel</span></code>.</p></li>
<li><p>experimental HIP-CPU feature</p></li>
<li><p>ThreeFry pseudorandom number generator based on Salmon et al., 2011, “Parallel random numbers: as easy as 1, 2, 3”.</p></li>
</ul>
</section>
<section id="id274">
<h5>Changed<a class="headerlink" href="#id274" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Python 2.7 is no longer officially supported.</p></li>
</ul>
</section>
<section id="id275">
<h5>Fixed<a class="headerlink" href="#id275" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Windows HIP SDK support</p></li>
</ul>
</section>
</section>
<section id="rocsolver-3-21-0">
<h4>rocSOLVER 3.21.0<a class="headerlink" href="#rocsolver-3-21-0" title="Link to this heading">#</a></h4>
<p>rocSOLVER 3.21.0 for ROCm 5.5.0</p>
<section id="id276">
<h5>Added<a class="headerlink" href="#id276" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>SVD for general matrices using Jacobi algorithm:</p>
<ul>
<li><p>GESVDJ (with batched and strided_batched versions)</p></li>
</ul>
</li>
<li><p>LU factorization without pivoting for block tridiagonal matrices:</p>
<ul>
<li><p>GEBLTTRF_NPVT (with batched and strided_batched versions)</p></li>
</ul>
</li>
<li><p>Linear system solver without pivoting for block tridiagonal matrices:</p>
<ul>
<li><p>GEBLTTRS_NPVT (with batched and strided_batched, versions)</p></li>
</ul>
</li>
<li><p>Product of triangular matrices</p>
<ul>
<li><p>LAUUM</p></li>
</ul>
</li>
<li><p>Added experimental hipGraph support for rocSOLVER functions</p></li>
</ul>
</section>
<section id="id277">
<h5>Optimized<a class="headerlink" href="#id277" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved the performance of SYEVJ/HEEVJ.</p></li>
</ul>
</section>
<section id="id278">
<h5>Changed<a class="headerlink" href="#id278" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>STEDC, SYEVD/HEEVD and SYGVD/HEGVD now use fully implemented Divide and Conquer approach.</p></li>
</ul>
</section>
<section id="id279">
<h5>Fixed<a class="headerlink" href="#id279" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>SYEVJ/HEEVJ should now be invariant under matrix scaling.</p></li>
<li><p>SYEVJ/HEEVJ should now properly output the eigenvalues when no sweeps are executed.</p></li>
<li><p>Fixed GETF2_NPVT and GETRF_NPVT input data initialization in tests and benchmarks.</p></li>
<li><p>Fixed rocblas missing from the dependency list of the rocsolver deb and rpm packages.</p></li>
</ul>
</section>
</section>
<section id="rocsparse-2-5-1">
<h4>rocSPARSE 2.5.1<a class="headerlink" href="#rocsparse-2-5-1" title="Link to this heading">#</a></h4>
<p>rocSPARSE 2.5.1 for ROCm 5.5.0</p>
<section id="id280">
<h5>Added<a class="headerlink" href="#id280" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added bsrgemm and spgemm for BSR format</p></li>
<li><p>Added bsrgeam</p></li>
<li><p>Added build support for Navi32</p></li>
<li><p>Added experimental hipGraph support for some rocSPARSE routines</p></li>
<li><p>Added csritsv, spitsv csr iterative triangular solve</p></li>
<li><p>Added mixed precisions for SpMV</p></li>
<li><p>Added batched SpMM for transpose A in COO format with atomic atomic algorithm</p></li>
</ul>
</section>
<section id="id281">
<h5>Improved<a class="headerlink" href="#id281" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimization to csr2bsr</p></li>
<li><p>Optimization to csr2csr_compress</p></li>
<li><p>Optimization to csr2coo</p></li>
<li><p>Optimization to gebsr2csr</p></li>
<li><p>Optimization to csr2gebsr</p></li>
<li><p>Fixes to documentation</p></li>
<li><p>Fixes a bug in COO SpMV gridsize</p></li>
<li><p>Fixes a bug in SpMM gridsize when using very large matrices</p></li>
</ul>
</section>
<section id="id282">
<h5>Known Issues<a class="headerlink" href="#id282" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>In csritlu0, the algorithm rocsparse_itilu0_alg_sync_split_fusion has some accuracy issues to investigate with XNACK enabled. The fallback is rocsparse_itilu0_alg_sync_split.</p></li>
</ul>
</section>
</section>
<section id="rocwmma-1-0">
<h4>rocWMMA 1.0<a class="headerlink" href="#rocwmma-1-0" title="Link to this heading">#</a></h4>
<p>rocWMMA 1.0 for ROCm 5.5.0</p>
<section id="id283">
<h5>Added<a class="headerlink" href="#id283" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added support for wave32 on gfx11+</p></li>
<li><p>Added infrastructure changes to support hipRTC</p></li>
<li><p>Added performance tracking system</p></li>
</ul>
</section>
<section id="id284">
<h5>Changed<a class="headerlink" href="#id284" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Modified the assignment of hardware information</p></li>
<li><p>Modified the data access for unsigned datatypes</p></li>
<li><p>Added library config to support multiple architectures</p></li>
</ul>
</section>
</section>
<section id="tensile-4-36-0">
<h4>Tensile 4.36.0<a class="headerlink" href="#tensile-4-36-0" title="Link to this heading">#</a></h4>
<p>Tensile 4.36.0 for ROCm 5.5.0</p>
<section id="id285">
<h5>Added<a class="headerlink" href="#id285" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Add functions for user-driven tuning</p></li>
<li><p>Add GFX11 support: HostLibraryTests yamls, rearragne FP32©/FP64© instruction order, archCaps for instruction renaming condition, adjust vgpr bank for A/B/C for optimize, separate vscnt and vmcnt, dual mac</p></li>
<li><p>Add binary search for Grid-Based algorithm</p></li>
<li><p>Add reject condition for (StoreCInUnroll + BufferStore=0) and (DirectToVgpr + ScheduleIterAlg&lt;3 + PrefetchGlobalRead==2)</p></li>
<li><p>Add support for (DirectToLds + hgemm + NN/NT/TT) and (DirectToLds + hgemm + GlobalLoadVectorWidth &lt; 4)</p></li>
<li><p>Add support for (DirectToLds + hgemm(TLU=True only) or sgemm + NumLoadsCoalesced &gt; 1)</p></li>
<li><p>Add GSU SingleBuffer algorithm for HSS/BSS</p></li>
<li><p>Add gfx900:xnack-, gfx1032, gfx1034, gfx1035</p></li>
<li><p>Enable gfx1031 support</p></li>
</ul>
</section>
<section id="id286">
<h5>Optimizations<a class="headerlink" href="#id286" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Use AssertSizeLessThan for BufferStoreOffsetLimitCheck if it is smaller than MT1</p></li>
<li><p>Improve InitAccVgprOpt</p></li>
</ul>
</section>
<section id="id287">
<h5>Changed<a class="headerlink" href="#id287" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Use global_atomic for GSU instead of flat and global_store for debug code</p></li>
<li><p>Replace flat_load/store with global_load/store</p></li>
<li><p>Use global_load/store for BufferLoad/Store=0 and enable scheduling</p></li>
<li><p>LocalSplitU support for HGEMM+HPA when MFMA disabled</p></li>
<li><p>Update Code Object Version</p></li>
<li><p>Type cast local memory to COMPUTE_DATA_TYPE in LDS to avoid precision loss</p></li>
<li><p>Update asm cap cache arguments</p></li>
<li><p>Unify SplitGlobalRead into ThreadSeparateGlobalRead and remove SplitGlobalRead</p></li>
<li><p>Change checks, error messages, assembly syntax, and coverage for DirectToLds</p></li>
<li><p>Remove unused cmake file</p></li>
<li><p>Clean up the LLVM dependency code</p></li>
<li><p>Update ThreadSeparateGlobalRead test cases for PrefetchGlobalRead=2</p></li>
<li><p>Update sgemm/hgemm test cases for DirectToLds and ThreadSepareteGlobalRead</p></li>
</ul>
</section>
<section id="id288">
<h5>Fixed<a class="headerlink" href="#id288" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Add build-id to header of compiled source kernels</p></li>
<li><p>Fix solution index collisions</p></li>
<li><p>Fix h beta vectorwidth4 correctness issue for WMMA</p></li>
<li><p>Fix an error with BufferStore=0</p></li>
<li><p>Fix mismatch issue with (StoreCInUnroll + PrefetchGlobalRead=2)</p></li>
<li><p>Fix MoveMIoutToArch bug</p></li>
<li><p>Fix flat load correctness issue on I8 and flat store correctness issue</p></li>
<li><p>Fix mismatch issue with BufferLoad=0 + TailLoop for large array sizes</p></li>
<li><p>Fix code generation error with BufferStore=0 and StoreCInUnrollPostLoop</p></li>
<li><p>Fix issues with DirectToVgpr + ScheduleIterAlg&lt;3</p></li>
<li><p>Fix mismatch issue with DGEMM TT + LocalReadVectorWidth=2</p></li>
<li><p>Fix mismatch issue with PrefetchGlobalRead=2</p></li>
<li><p>Fix mismatch issue with DirectToVgpr + PrefetchGlobalRead=2 + small tile size</p></li>
<li><p>Fix an error with PersistentKernel=0 + PrefetchAcrossPersistent=1 + PrefetchAcrossPersistentMode=1</p></li>
<li><p>Fix mismatch issue with DirectToVgpr + DirectToLds + only 1 iteration in unroll loop case</p></li>
<li><p>Remove duplicate GSU kernels: for GSU = 1, GSUAlgorithm SingleBuffer and MultipleBuffer kernels are identical</p></li>
<li><p>Fix for failing CI tests due to CpuThreads=0</p></li>
<li><p>Fix mismatch issue with DirectToLds + PrefetchGlobalRead=2</p></li>
<li><p>Remove the reject condition for ThreadSeparateGlobalRead and DirectToLds (HGEMM, SGEMM only)</p></li>
<li><p>Modify reject condition for minimum lanes of ThreadSeparateGlobalRead (SGEMM or larger data type only)</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-4-3">
<h2>ROCm 5.4.3<a class="headerlink" href="#rocm-5-4-3" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<section id="id289">
<h3>Deprecations and warnings<a class="headerlink" href="#id289" title="Link to this heading">#</a></h3>
<section id="hip-perl-scripts-deprecation">
<h4>HIP Perl scripts deprecation<a class="headerlink" href="#hip-perl-scripts-deprecation" title="Link to this heading">#</a></h4>
<p>The <code class="docutils literal notranslate"><span class="pre">hipcc</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> Perl scripts are deprecated. In a future release, compiled binaries will be
available as <code class="docutils literal notranslate"><span class="pre">hipcc.bin</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.bin</span></code> as replacements for the Perl scripts.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>There will be a transition period where the Perl scripts and compiled binaries are available before the
scripts are removed. There will be no functional difference between the Perl scripts and their compiled
binary counterpart. No user action is required. Once these are available, users can optionally switch to
<code class="docutils literal notranslate"><span class="pre">hipcc.bin</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.bin</span></code>. The <code class="docutils literal notranslate"><span class="pre">hipcc</span></code>/<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> soft link will be assimilated to point from
<code class="docutils literal notranslate"><span class="pre">hipcc</span></code>/<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> to the respective compiled binaries as the default option.</p>
</div>
<section id="id290">
<h5>Linux file system hierarchy standard for ROCm<a class="headerlink" href="#id290" title="Link to this heading">#</a></h5>
<p>ROCm packages have adopted the Linux foundation file system hierarchy standard in this release to
ensure ROCm components follow open source conventions for Linux-based distributions. While
moving to a new file system hierarchy, ROCm ensures backward compatibility with its 5.1 version or
older file system hierarchy. See below for a detailed explanation of the new file system hierarchy and
backward compatibility.</p>
</section>
<section id="id291">
<h5>New file system hierarchy<a class="headerlink" href="#id291" title="Link to this heading">#</a></h5>
<p>The following is the new file system hierarchy:4</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>/opt/rocm-&lt;ver&gt;
    | --bin
      | --All externally exposed Binaries
    | --libexec
        | --&lt;component&gt;
            | -- Component specific private non-ISA executables (architecture independent)
    | --include
        | -- &lt;component&gt;
            | --&lt;header files&gt;
    | --lib
        | --lib&lt;soname&gt;.so -&gt; lib&lt;soname&gt;.so.major -&gt; lib&lt;soname&gt;.so.major.minor.patch
            (public libraries linked with application)
        | --&lt;component&gt; (component specific private library, executable data)
        | --&lt;cmake&gt;
            | --components
                | --&lt;component&gt;.config.cmake
    | --share
        | --html/&lt;component&gt;/*.html
        | --info/&lt;component&gt;/*.[pdf, md, txt]
        | --man
        | --doc
            | --&lt;component&gt;
                | --&lt;licenses&gt;
        | --&lt;component&gt;
            | --&lt;misc files&gt; (arch independent non-executable)
            | --samples
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>ROCm will not support backward compatibility with the v5.1(old) file system hierarchy in its next major
release.</p>
</div>
<p>For more information, refer to <a class="reference external" href="https://refspecs.linuxfoundation.org/fhs.shtml">https://refspecs.linuxfoundation.org/fhs.shtml</a>.</p>
</section>
<section id="id292">
<h5>Backward compatibility with older file systems<a class="headerlink" href="#id292" title="Link to this heading">#</a></h5>
<p>ROCm has moved header files and libraries to its new location as indicated in the above structure and
included symbolic-link and wrapper header files in its old location for backward compatibility.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>ROCm will continue supporting backward compatibility until the next major release.</p>
</div>
</section>
<section id="id293">
<h5>Wrapper header files<a class="headerlink" href="#id293" title="Link to this heading">#</a></h5>
<p>Wrapper header files are placed in the old location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/include</span></code>) with a
warning message to include files from the new location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/include</span></code>) as shown in the
example below:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Code snippet from hip_runtime.h</span>
<span class="cp">#pragma message “This file is deprecated. Use file from include path /opt/rocm-ver/include/ and prefix with hip”.</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">"hip/hip_runtime.h"</span>
</pre></div>
</div>
<p>The wrapper header files’ backward compatibility deprecation is as follows:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">#pragma</span></code> message announcing deprecation – ROCm v5.2 release</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">#pragma</span></code> message changed to <code class="docutils literal notranslate"><span class="pre">#warning</span></code> – Future release</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">#warning</span></code> changed to <code class="docutils literal notranslate"><span class="pre">#error</span></code> – Future release</p></li>
<li><p>Backward compatibility wrappers removed – Future release</p></li>
</ul>
</section>
<section id="id294">
<h5>Library files<a class="headerlink" href="#id294" title="Link to this heading">#</a></h5>
<p>Library files are available in the <code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/lib</span></code> folder. For backward compatibility, the old library
location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/lib</span></code>) has a soft link to the library at the new location.</p>
<p>Example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>ls<span class="w"> </span>-l<span class="w"> </span>/opt/rocm/hip/lib/
total<span class="w"> </span><span class="m">4</span>
drwxr-xr-x<span class="w"> </span><span class="m">4</span><span class="w"> </span>root<span class="w"> </span>root<span class="w"> </span><span class="m">4096</span><span class="w"> </span>May<span class="w"> </span><span class="m">12</span><span class="w"> </span><span class="m">10</span>:45<span class="w"> </span>cmake
lrwxrwxrwx<span class="w"> </span><span class="m">1</span><span class="w"> </span>root<span class="w"> </span>root<span class="w">   </span><span class="m">24</span><span class="w"> </span>May<span class="w"> </span><span class="m">10</span><span class="w"> </span><span class="m">23</span>:32<span class="w"> </span>libamdhip64.so<span class="w"> </span>-&gt;<span class="w"> </span>../../lib/libamdhip64.so
</pre></div>
</div>
</section>
<section id="id295">
<h5>CMake config files<a class="headerlink" href="#id295" title="Link to this heading">#</a></h5>
<p>All CMake configuration files are available in the <code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/lib/cmake/&lt;component&gt;</span></code> folder. For
backward compatibility, the old CMake locations (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/lib/cmake</span></code>) consist of
a soft link to the new CMake config.</p>
<p>Example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>ls<span class="w"> </span>-l<span class="w"> </span>/opt/rocm/hip/lib/cmake/hip/
total<span class="w"> </span><span class="m">0</span>
lrwxrwxrwx<span class="w"> </span><span class="m">1</span><span class="w"> </span>root<span class="w"> </span>root<span class="w"> </span><span class="m">42</span><span class="w"> </span>May<span class="w"> </span><span class="m">10</span><span class="w"> </span><span class="m">23</span>:32<span class="w"> </span>hip-config.cmake<span class="w"> </span>-&gt;<span class="w"> </span>../../../../lib/cmake/hip/hip-config.cmake
</pre></div>
</div>
</section>
</section>
</section>
<section id="id296">
<h3>Defect fixes<a class="headerlink" href="#id296" title="Link to this heading">#</a></h3>
<section id="compiler-improvements">
<h4>Compiler improvements<a class="headerlink" href="#compiler-improvements" title="Link to this heading">#</a></h4>
<p>In ROCm v5.4.3, improvements to the compiler address errors with the following signatures:</p>
<ul class="simple">
<li><p>“error: unhandled SGPR spill to memory”</p></li>
<li><p>“cannot scavenge register without an emergency spill slot!”</p></li>
<li><p>“error: ran out of registers during register allocation”</p></li>
</ul>
</section>
</section>
<section id="id297">
<h3>Known issues<a class="headerlink" href="#id297" title="Link to this heading">#</a></h3>
<section id="compiler-option-error-at-runtime">
<h4>Compiler option error at runtime<a class="headerlink" href="#compiler-option-error-at-runtime" title="Link to this heading">#</a></h4>
<p>Some users may encounter a “Cannot find Symbol” error at runtime when using <code class="docutils literal notranslate"><span class="pre">-save-temps</span></code>. While
most <code class="docutils literal notranslate"><span class="pre">-save-temps</span></code> use cases work correctly, this error may appear occasionally.</p>
<p>This issue is under investigation, and the known workaround is not to use <code class="docutils literal notranslate"><span class="pre">-save-temps</span></code> when the error
appears.</p>
</section>
</section>
<section id="library-changes-in-rocm-5-4-3">
<h3>Library changes in ROCM 5.4.3<a class="headerlink" href="#library-changes-in-rocm-5-4-3" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.4.3">0.53.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.4.3">2.13.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.4.3">1.0.10</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.4.3">1.6.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.4.3">2.3.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.4.3">2.13.4</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.4.3">2.1.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.4.3">2.46.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p>1.0.20 ⇒ <a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.4.3">1.0.21</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocm-cmake</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.4.3">0.8.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.4.3">2.12.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.4.3">2.10.16</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.4.3">3.20.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.4.3">2.4.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.4.3">2.17.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocWMMA</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.4.3">0.9</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.4.3">4.35.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="rocfft-1-0-21">
<h4>rocFFT 1.0.21<a class="headerlink" href="#rocfft-1-0-21" title="Link to this heading">#</a></h4>
<p>rocFFT 1.0.21 for ROCm 5.4.3</p>
<section id="id298">
<h5>Fixed<a class="headerlink" href="#id298" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed source directory from rocm_install_targets call to prevent installation of rocfft.h in an unintended location.</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-4-2">
<h2>ROCm 5.4.2<a class="headerlink" href="#rocm-5-4-2" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<section id="id299">
<h3>Deprecations and warnings<a class="headerlink" href="#id299" title="Link to this heading">#</a></h3>
<section id="id300">
<h4>HIP Perl scripts deprecation<a class="headerlink" href="#id300" title="Link to this heading">#</a></h4>
<p>The <code class="docutils literal notranslate"><span class="pre">hipcc</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> Perl scripts are deprecated. In a future release, compiled binaries will be
available as <code class="docutils literal notranslate"><span class="pre">hipcc.bin</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.bin</span></code> as replacements for the Perl scripts.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>There will be a transition period where the Perl scripts and compiled binaries are available  before the
scripts are removed. There will be no functional difference between the Perl scripts and their compiled
binary counterpart. No user action is required. Once these are available, users can optionally switch to
<code class="docutils literal notranslate"><span class="pre">hipcc.bin</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.bin</span></code>. The <code class="docutils literal notranslate"><span class="pre">hipcc</span></code>/<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> soft link will be assimilated to point from
<code class="docutils literal notranslate"><span class="pre">hipcc</span></code>/<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> to the respective compiled binaries as the default option.</p>
</div>
</section>
<section id="hipcc-options-deprecation">
<h4><code class="docutils literal notranslate"><span class="pre">hipcc</span></code> options deprecation<a class="headerlink" href="#hipcc-options-deprecation" title="Link to this heading">#</a></h4>
<p>The following hipcc options are being deprecated and will be removed in a future release:</p>
<ul class="simple">
<li><p>The <code class="docutils literal notranslate"><span class="pre">--amdgpu-target</span></code> option is being deprecated, and user must use the <code class="docutils literal notranslate"><span class="pre">–offload-arch</span></code> option to
specify the GPU architecture.</p></li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">--amdhsa-code-object-version</span></code> option is being deprecated.  Users can use the Clang/LLVM
option <code class="docutils literal notranslate"><span class="pre">-mllvm</span> <span class="pre">-mcode-object-version</span></code> to debug issues related to code object versions.</p></li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">--hipcc-func-supp</span></code>/<code class="docutils literal notranslate"><span class="pre">--hipcc-no-func-supp</span></code> options are being deprecated, as the function calls
are already supported in production on AMD GPUs.</p></li>
</ul>
</section>
</section>
<section id="id301">
<h3>Known issues<a class="headerlink" href="#id301" title="Link to this heading">#</a></h3>
<p>Under certain circumstances typified by high register pressure, users may encounter a compiler abort
with one of the following error messages:</p>
<ul>
<li><blockquote>
<div><p><code class="docutils literal notranslate"><span class="pre">error:</span> <span class="pre">unhandled</span> <span class="pre">SGPR</span> <span class="pre">spill</span> <span class="pre">to</span> <span class="pre">memory</span></code></p>
</div></blockquote>
</li>
<li><blockquote>
<div><p><code class="docutils literal notranslate"><span class="pre">cannot</span> <span class="pre">scavenge</span> <span class="pre">register</span> <span class="pre">without</span> <span class="pre">an</span> <span class="pre">emergency</span> <span class="pre">spill</span> <span class="pre">slot!</span></code></p>
</div></blockquote>
</li>
<li><blockquote>
<div><p><code class="docutils literal notranslate"><span class="pre">error:</span> <span class="pre">ran</span> <span class="pre">out</span> <span class="pre">of</span> <span class="pre">registers</span> <span class="pre">during</span> <span class="pre">register</span> <span class="pre">allocation</span></code></p>
</div></blockquote>
</li>
</ul>
<p>This is a known issue and will be fixed in a future release.</p>
</section>
<section id="library-changes-in-rocm-5-4-2">
<h3>Library changes in ROCM 5.4.2<a class="headerlink" href="#library-changes-in-rocm-5-4-2" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.4.2">0.53.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.4.2">2.13.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.4.2">1.0.10</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.4.2">1.6.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.4.2">2.3.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.4.2">2.13.4</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.4.2">2.1.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.4.2">2.46.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.4.2">1.0.20</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocm-cmake</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.4.2">0.8.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.4.2">2.12.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.4.2">2.10.16</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.4.2">3.20.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.4.2">2.4.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.4.2">2.17.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocWMMA</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.4.2">0.9</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.4.2">4.35.0</a></p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-4-1">
<h2>ROCm 5.4.1<a class="headerlink" href="#rocm-5-4-1" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<section id="id302">
<h3>What’s new in this release<a class="headerlink" href="#id302" title="Link to this heading">#</a></h3>
<section id="id303">
<h4>HIP enhancements<a class="headerlink" href="#id303" title="Link to this heading">#</a></h4>
<p>The ROCm v5.4.1 release consists of the following new HIP API:</p>
<section id="new-hip-api-hiplaunchhostfunc">
<h5>New HIP API - hipLaunchHostFunc<a class="headerlink" href="#new-hip-api-hiplaunchhostfunc" title="Link to this heading">#</a></h5>
<p>The following new HIP API is introduced in the ROCm v5.4.1 release.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This is a pre-official version (beta) release of the new APIs.</p>
</div>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipLaunchHostFunc</span><span class="p">(</span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">stream</span><span class="p">,</span><span class="w"> </span><span class="n">hipHostFn_t</span><span class="w"> </span><span class="n">fn</span><span class="p">,</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">userData</span><span class="p">);</span>
</pre></div>
</div>
<p>This swaps the stream capture mode of a thread.</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>@param [in] mode - Pointer to mode value to swap with the current mode
</pre></div>
</div>
<p>This parameter returns <code class="docutils literal notranslate"><span class="pre">#hipSuccess</span></code>, <code class="docutils literal notranslate"><span class="pre">#hipErrorInvalidValue</span></code>.</p>
<p>For more information, refer to the HIP API documentation at
/bundle/HIP_API_Guide/page/modules.html.</p>
</section>
</section>
</section>
<section id="id304">
<h3>Deprecations and warnings<a class="headerlink" href="#id304" title="Link to this heading">#</a></h3>
<section id="id305">
<h4>HIP Perl scripts deprecation<a class="headerlink" href="#id305" title="Link to this heading">#</a></h4>
<p>The <code class="docutils literal notranslate"><span class="pre">hipcc</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> Perl scripts are deprecated. In a future release, compiled binaries will be
available as <code class="docutils literal notranslate"><span class="pre">hipcc.bin</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.bin</span></code> as replacements for the Perl scripts.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>There will be a transition period where the Perl scripts and compiled binaries are available  before the
scripts are removed. There will be no functional difference between the Perl scripts and their compiled
binary counterpart. No user action is required. Once these are available, users can optionally switch to
<code class="docutils literal notranslate"><span class="pre">hipcc.bin</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.bin</span></code>. The <code class="docutils literal notranslate"><span class="pre">hipcc</span></code>/<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> soft link will be assimilated to point from
<code class="docutils literal notranslate"><span class="pre">hipcc</span></code>/<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> to the respective compiled binaries as the default option.</p>
</div>
</section>
</section>
<section id="ifwi-fixes">
<h3>IFWI fixes<a class="headerlink" href="#ifwi-fixes" title="Link to this heading">#</a></h3>
<p>These defects were identified and documented as known issues in previous ROCm releases and are
fixed in this release.</p>
<section id="amd-instinct-mi200-firmware-ifwi-maintenance-update-3">
<h4>AMD Instinct™ MI200 firmware IFWI maintenance update #3<a class="headerlink" href="#amd-instinct-mi200-firmware-ifwi-maintenance-update-3" title="Link to this heading">#</a></h4>
<p>This IFWI release fixes the following issue in AMD Instinct™ MI210/MI250 Accelerators.</p>
<p>After prolonged periods of operation, certain MI200 Instinct™ Accelerators may perform in a degraded
way resulting in application failures.</p>
<p>In this package, AMD delivers a new firmware version for MI200 GPU accelerators and a firmware
installation tool – AMD FW FLASH 1.2.</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>GPU</p></th>
<th class="head"><p>Productionp part number</p></th>
<th class="head"><p>SKU</p></th>
<th class="head"><p>IFWI name</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>MI210</p></td>
<td><p>113-D673XX</p></td>
<td><p>D67302</p></td>
<td><p>D6730200V.110</p></td>
</tr>
<tr class="row-odd"><td><p>MI210</p></td>
<td><p>113-D673XX</p></td>
<td><p>D67301</p></td>
<td><p>D6730100V.073</p></td>
</tr>
<tr class="row-even"><td><p>MI250</p></td>
<td><p>113-D652XX</p></td>
<td><p>D65209</p></td>
<td><p>D6520900.073</p></td>
</tr>
<tr class="row-odd"><td><p>MI250</p></td>
<td><p>113-D652XX</p></td>
<td><p>D65210</p></td>
<td><p>D6521000.073</p></td>
</tr>
</tbody>
</table>
</div>
<p>Instructions on how to download and apply MI200 maintenance updates are available at:</p>
<p><a class="reference external" href="https://www.amd.com/en/support/server-accelerators/amd-instinct/amd-instinct-mi-series/amd-instinct-mi210">https://www.amd.com/en/support/server-accelerators/amd-instinct/amd-instinct-mi-series/amd-instinct-mi210</a></p>
</section>
<section id="amd-instinct-mi200-sriov-virtualization-support">
<h4>AMD Instinct™ MI200 SRIOV virtualization support<a class="headerlink" href="#amd-instinct-mi200-sriov-virtualization-support" title="Link to this heading">#</a></h4>
<p>Maintenance update #3, combined with ROCm 5.4.1, now provides SRIOV virtualization support for all
AMD Instinct™ MI200 devices.</p>
</section>
</section>
<section id="library-changes-in-rocm-5-4-1">
<h3>Library changes in ROCM 5.4.1<a class="headerlink" href="#library-changes-in-rocm-5-4-1" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.4.1">0.53.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.4.1">2.13.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.4.1">1.0.10</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.4.1">1.6.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.4.1">2.3.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.4.1">2.13.4</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.4.1">2.1.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.4.1">2.46.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p>1.0.19 ⇒ <a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.4.1">1.0.20</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocm-cmake</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.4.1">0.8.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.4.1">2.12.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.4.1">2.10.16</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.4.1">3.20.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.4.1">2.4.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.4.1">2.17.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocWMMA</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.4.1">0.9</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.4.1">4.35.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="rocfft-1-0-20">
<h4>rocFFT 1.0.20<a class="headerlink" href="#rocfft-1-0-20" title="Link to this heading">#</a></h4>
<p>rocFFT 1.0.20 for ROCm 5.4.1</p>
<section id="id306">
<h5>Fixed<a class="headerlink" href="#id306" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed incorrect results on strided large 1D FFTs where batch size does not equal the stride.</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-4-0">
<h2>ROCm 5.4.0<a class="headerlink" href="#rocm-5-4-0" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable no-duplicate-header -->
<section id="id307">
<h3>What’s new in this release<a class="headerlink" href="#id307" title="Link to this heading">#</a></h3>
<section id="id308">
<h4>HIP enhancements<a class="headerlink" href="#id308" title="Link to this heading">#</a></h4>
<p>The ROCm v5.4 release consists of the following HIP enhancements:</p>
<section id="support-for-wall-clock64">
<h5>Support for wall_clock64<a class="headerlink" href="#support-for-wall-clock64" title="Link to this heading">#</a></h5>
<p>A new timer function wall_clock64() is supported, which returns wall clock count at a constant
frequency on the device.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="nf">wall_clock64</span><span class="p">();</span>
</pre></div>
</div>
<p>It returns wall clock count at a constant frequency on the device, which can be queried via HIP API with
the hipDeviceAttributeWallClockRate attribute of the device in the HIP application code.</p>
<p>Example:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">wallClkRate</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="c1">//in kilohertz</span>
<span class="o">+</span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipDeviceGetAttribute</span><span class="p">(</span><span class="o">&amp;</span><span class="n">wallClkRate</span><span class="p">,</span><span class="w"> </span><span class="n">hipDeviceAttributeWallClockRate</span><span class="p">,</span><span class="w"> </span><span class="n">deviceId</span><span class="p">));</span>
</pre></div>
</div>
<p>Where hipDeviceAttributeWallClockRate is a device attribute.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The wall clock frequency is a per-device attribute.</p>
</div>
</section>
<section id="new-registry-added-for-gpu-max-hw-queues">
<h5>New registry added for GPU_MAX_HW_QUEUES<a class="headerlink" href="#new-registry-added-for-gpu-max-hw-queues" title="Link to this heading">#</a></h5>
<p>The GPU_MAX_HW_QUEUES registry defines the maximum number of independent hardware queues
allocated per process per device.</p>
<p>The environment variable controls how many independent hardware queues HIP runtime can create
per process, per device. If the application allocates more HIP streams than this number, then the HIP
runtime reuses the same hardware queues for the new streams in a round-robin manner.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This maximum number does not apply to hardware queues created for CU-masked HIP streams or
cooperative queues for HIP Cooperative Groups (there is only one queue per device).</p>
</div>
<p>For more details, refer to the HIP Programming Guide.</p>
</section>
</section>
<section id="id309">
<h4>New HIP APIs in this release<a class="headerlink" href="#id309" title="Link to this heading">#</a></h4>
<p>The following new HIP APIs are available in the ROCm v5.4 release.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This is a pre-official version (beta) release of the new APIs.</p>
</div>
<section id="error-handling">
<h5>Error handling<a class="headerlink" href="#error-handling" title="Link to this heading">#</a></h5>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipDrvGetErrorName</span><span class="p">(</span><span class="n">hipError_t</span><span class="w"> </span><span class="n">hipError</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">**</span><span class="w"> </span><span class="n">errorString</span><span class="p">);</span>
</pre></div>
</div>
<p>This returns HIP errors in the text string format.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipDrvGetErrorString</span><span class="p">(</span><span class="n">hipError_t</span><span class="w"> </span><span class="n">hipError</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="kt">char</span><span class="o">**</span><span class="w"> </span><span class="n">errorString</span><span class="p">);</span>
</pre></div>
</div>
<p>This returns text string messages with more details about the error.</p>
<p>For more information, refer to the HIP API Guide.</p>
</section>
<section id="hip-tests-source-separation">
<h5>HIP tests source separation<a class="headerlink" href="#hip-tests-source-separation" title="Link to this heading">#</a></h5>
<p>With ROCm v5.4, a separate GitHub project is created at</p>
<p><a class="github reference external" href="https://github.com/ROCm-Developer-Tools/hip-tests">ROCm-Developer-Tools/hip-tests</a></p>
<p>This contains HIP catch2 tests and samples, and new tests will continue to develop.</p>
<p>In future ROCm releases, catch2 tests and samples will be removed from the HIP project.</p>
</section>
</section>
</section>
<section id="id310">
<h3>OpenMP enhancements<a class="headerlink" href="#id310" title="Link to this heading">#</a></h3>
<p>This release consists of the following OpenMP enhancements:</p>
<ul class="simple">
<li><p>Enable new device RTL in libomptarget as default.</p></li>
<li><p>New flag <code class="docutils literal notranslate"><span class="pre">-fopenmp-target-fast</span></code> to imply <code class="docutils literal notranslate"><span class="pre">-fopenmp-target-ignore-env-vars</span> <span class="pre">-fopenmp-assume-no-thread-state</span> <span class="pre">-fopenmp-assume-no-nested-parallelism</span></code>.</p></li>
<li><p>Support for the collapse clause and non-unit stride in cases where the no-loop specialized kernel is
generated.</p></li>
<li><p>Initial implementation of optimized cross-team sum reduction for float and double type scalars.</p></li>
<li><p>Pool-based optimization in the OpenMP runtime to reduce locking during data transfer.</p></li>
</ul>
</section>
<section id="id311">
<h3>Deprecations and warnings<a class="headerlink" href="#id311" title="Link to this heading">#</a></h3>
<section id="id312">
<h4>HIP Perl scripts deprecation<a class="headerlink" href="#id312" title="Link to this heading">#</a></h4>
<p>The <code class="docutils literal notranslate"><span class="pre">hipcc</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> Perl scripts are deprecated. In a future release, compiled binaries will be
available as <code class="docutils literal notranslate"><span class="pre">hipcc.bin</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.bin</span></code> as replacements for the Perl scripts.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>There will be a transition period where the Perl scripts and compiled binaries are available before the
scripts are removed. There will be no functional difference between the Perl scripts and their compiled
binary counterpart. No user action is required. Once these are available, users can optionally switch to
<code class="docutils literal notranslate"><span class="pre">hipcc.bin</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.bin</span></code>. The <code class="docutils literal notranslate"><span class="pre">hipcc</span></code>/<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> soft link will be assimilated to point from
<code class="docutils literal notranslate"><span class="pre">hipcc</span></code>/<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> to the respective compiled binaries as the default option.</p>
</div>
<section id="id313">
<h5>Linux file system hierarchy standard for ROCm<a class="headerlink" href="#id313" title="Link to this heading">#</a></h5>
<p>ROCm packages have adopted the Linux foundation file system hierarchy standard in this release to
ensure ROCm components follow open source conventions for Linux-based distributions. While
moving to a new file system hierarchy, ROCm ensures backward compatibility with its 5.1 version or
older file system hierarchy. See below for a detailed explanation of the new file system hierarchy and
backward compatibility.</p>
</section>
<section id="id314">
<h5>New file system hierarchy<a class="headerlink" href="#id314" title="Link to this heading">#</a></h5>
<p>The following is the new file system hierarchy:</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>/opt/rocm-&lt;ver&gt;
    | --bin
      | --All externally exposed Binaries
    | --libexec
        | --&lt;component&gt;
            | -- Component specific private non-ISA executables (architecture independent)
    | --include
        | -- &lt;component&gt;
            | --&lt;header files&gt;
    | --lib
        | --lib&lt;soname&gt;.so -&gt; lib&lt;soname&gt;.so.major -&gt; lib&lt;soname&gt;.so.major.minor.patch
            (public libraries linked with application)
        | --&lt;component&gt; (component specific private library, executable data)
        | --&lt;cmake&gt;
            | --components
                | --&lt;component&gt;.config.cmake
    | --share
        | --html/&lt;component&gt;/*.html
        | --info/&lt;component&gt;/*.[pdf, md, txt]
        | --man
        | --doc
            | --&lt;component&gt;
                | --&lt;licenses&gt;
        | --&lt;component&gt;
            | --&lt;misc files&gt; (arch independent non-executable)
            | --samples
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>ROCm will not support backward compatibility with the v5.1(old) file system hierarchy in its next major
release.</p>
</div>
<p>For more information, refer to <a class="reference external" href="https://refspecs.linuxfoundation.org/fhs.shtml">https://refspecs.linuxfoundation.org/fhs.shtml</a>.</p>
</section>
<section id="id315">
<h5>Backward compatibility with older file systems<a class="headerlink" href="#id315" title="Link to this heading">#</a></h5>
<p>ROCm has moved header files and libraries to its new location as indicated in the above structure and
included symbolic-link and wrapper header files in its old location for backward compatibility.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>ROCm will continue supporting backward compatibility until the next major release.</p>
</div>
</section>
<section id="id316">
<h5>Wrapper header files<a class="headerlink" href="#id316" title="Link to this heading">#</a></h5>
<p>Wrapper header files are placed in the old location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/include</span></code>) with a
warning message to include files from the new location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/include</span></code>) as shown in the
example below:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Code snippet from hip_runtime.h</span>
<span class="cp">#pragma message “This file is deprecated. Use file from include path /opt/rocm-ver/include/ and prefix with hip”.</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">"hip/hip_runtime.h"</span>
</pre></div>
</div>
<p>The wrapper header files’ backward compatibility deprecation is as follows:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">#pragma</span></code> message announcing deprecation – ROCm v5.2 release</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">#pragma</span></code> message changed to <code class="docutils literal notranslate"><span class="pre">#warning</span></code> – Future release</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">#warning</span></code> changed to <code class="docutils literal notranslate"><span class="pre">#error</span></code> – Future release</p></li>
<li><p>Backward compatibility wrappers removed – Future release</p></li>
</ul>
</section>
<section id="id317">
<h5>Library files<a class="headerlink" href="#id317" title="Link to this heading">#</a></h5>
<p>Library files are available in the <code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/lib</span></code> folder. For backward compatibility, the old library
location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/lib</span></code>) has a soft link to the library at the new location.</p>
<p>Example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>ls<span class="w"> </span>-l<span class="w"> </span>/opt/rocm/hip/lib/
total<span class="w"> </span><span class="m">4</span>
drwxr-xr-x<span class="w"> </span><span class="m">4</span><span class="w"> </span>root<span class="w"> </span>root<span class="w"> </span><span class="m">4096</span><span class="w"> </span>May<span class="w"> </span><span class="m">12</span><span class="w"> </span><span class="m">10</span>:45<span class="w"> </span>cmake
lrwxrwxrwx<span class="w"> </span><span class="m">1</span><span class="w"> </span>root<span class="w"> </span>root<span class="w">   </span><span class="m">24</span><span class="w"> </span>May<span class="w"> </span><span class="m">10</span><span class="w"> </span><span class="m">23</span>:32<span class="w"> </span>libamdhip64.so<span class="w"> </span>-&gt;<span class="w"> </span>../../lib/libamdhip64.so
</pre></div>
</div>
</section>
<section id="id318">
<h5>CMake config files<a class="headerlink" href="#id318" title="Link to this heading">#</a></h5>
<p>All CMake configuration files are available in the <code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/lib/cmake/&lt;component&gt;</span></code> folder. For
backward compatibility, the old CMake locations (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/lib/cmake</span></code>) consist of
a soft link to the new CMake config.</p>
<p>Example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>ls<span class="w"> </span>-l<span class="w"> </span>/opt/rocm/hip/lib/cmake/hip/
total<span class="w"> </span><span class="m">0</span>
lrwxrwxrwx<span class="w"> </span><span class="m">1</span><span class="w"> </span>root<span class="w"> </span>root<span class="w"> </span><span class="m">42</span><span class="w"> </span>May<span class="w"> </span><span class="m">10</span><span class="w"> </span><span class="m">23</span>:32<span class="w"> </span>hip-config.cmake<span class="w"> </span>-&gt;<span class="w"> </span>../../../../lib/cmake/hip/hip-config.cmake
</pre></div>
</div>
</section>
</section>
</section>
<section id="id319">
<h3>Defect fixes<a class="headerlink" href="#id319" title="Link to this heading">#</a></h3>
<p>The following defects are fixed in this release.</p>
<p>These defects were identified and documented as known issues in previous ROCm releases and are
fixed in this release.</p>
<section id="memory-allocated-using-hiphostmalloc-with-flags-didn-t-exhibit-fine-grain-behavior">
<h4>Memory allocated using hipHostMalloc() with flags didn’t exhibit fine-grain behavior<a class="headerlink" href="#memory-allocated-using-hiphostmalloc-with-flags-didn-t-exhibit-fine-grain-behavior" title="Link to this heading">#</a></h4>
<section id="issue">
<h5>Issue<a class="headerlink" href="#issue" title="Link to this heading">#</a></h5>
<p>The test was incorrectly using the <code class="docutils literal notranslate"><span class="pre">hipDeviceAttributePageableMemoryAccess</span></code> device attribute to
determine coherent support.</p>
</section>
<section id="fix">
<h5>Fix<a class="headerlink" href="#fix" title="Link to this heading">#</a></h5>
<p><code class="docutils literal notranslate"><span class="pre">hipHostMalloc()</span></code> allocates memory with fine-grained access by default when the environment variable
<code class="docutils literal notranslate"><span class="pre">HIP_HOST_COHERENT=1</span></code> is used.</p>
<p>For more information, refer to <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/docs-6.0.0/doxygen/html/index.html" title="(in HIP Documentation v6.0.0)"><span>HIP Runtime API Reference</span></a>.</p>
</section>
</section>
<section id="softhang-with-hipstreamwithcumask-test-on-amd-instinct">
<h4>SoftHang with <code class="docutils literal notranslate"><span class="pre">hipStreamWithCUMask</span></code> test on AMD Instinct™<a class="headerlink" href="#softhang-with-hipstreamwithcumask-test-on-amd-instinct" title="Link to this heading">#</a></h4>
<section id="id320">
<h5>Issue<a class="headerlink" href="#id320" title="Link to this heading">#</a></h5>
<p>On GFX10 GPUs, kernel execution hangs when it is launched on streams created using
<code class="docutils literal notranslate"><span class="pre">hipStreamWithCUMask</span></code>.</p>
</section>
<section id="id321">
<h5>Fix<a class="headerlink" href="#id321" title="Link to this heading">#</a></h5>
<p>On GFX10 GPUs, each workgroup processor encompasses two compute units, and the compute units
must be enabled as a pair. The <code class="docutils literal notranslate"><span class="pre">hipStreamWithCUMask</span></code> API unit test cases are updated to set compute
unit mask (cuMask) in pairs for GFX10 GPUs.</p>
</section>
</section>
<section id="rocm-tools-gpu-ids">
<h4>ROCm tools GPU IDs<a class="headerlink" href="#rocm-tools-gpu-ids" title="Link to this heading">#</a></h4>
<p>The HIP language device IDs are not the same as the GPU IDs reported by the tools. GPU IDs are
globally unique and guaranteed to be consistent across APIs and processes.</p>
<p>GPU IDs reported by ROCTracer and ROCProfiler or ROCm Tools are HSA Driver Node ID of that GPU,
as it is a unique ID for that device in that particular node.</p>
</section>
</section>
<section id="library-changes-in-rocm-5-4-0">
<h3>Library changes in ROCM 5.4.0<a class="headerlink" href="#library-changes-in-rocm-5-4-0" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p>0.52.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.4.0">0.53.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p>2.12.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.4.0">2.13.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p>1.0.9 ⇒ <a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.4.0">1.0.10</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p>1.5.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.4.0">1.6.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p>2.3.1 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.4.0">2.3.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p>2.12.10 ⇒ <a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.4.0">2.13.4</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p>2.1.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.4.0">2.1.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p>2.45.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.4.0">2.46.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p>1.0.18 ⇒ <a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.4.0">1.0.19</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocm-cmake</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.4.0">0.8.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p>2.11.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.4.0">2.12.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p>2.10.15 ⇒ <a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.4.0">2.10.16</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p>3.19.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.4.0">3.20.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p>2.2.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.4.0">2.4.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p>2.16.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.4.0">2.17.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocWMMA</p></td>
<td><p>0.8 ⇒ <a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.4.0">0.9</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p>4.34.0 ⇒ <a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.4.0">4.35.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="hipblas-0-53-0">
<h4>hipBLAS 0.53.0<a class="headerlink" href="#hipblas-0-53-0" title="Link to this heading">#</a></h4>
<p>hipBLAS 0.53.0 for ROCm 5.4.0</p>
<section id="id322">
<h5>Added<a class="headerlink" href="#id322" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Allow for selection of int8 datatype</p></li>
<li><p>Added support for hipblasXgels and hipblasXgelsStridedBatched operations (with s,d,c,z precisions),
only supported with rocBLAS backend</p></li>
<li><p>Added support for hipblasXgelsBatched operations (with s,d,c,z precisions)</p></li>
</ul>
</section>
</section>
<section id="hipcub-2-13-0">
<h4>hipCUB 2.13.0<a class="headerlink" href="#hipcub-2-13-0" title="Link to this heading">#</a></h4>
<p>hipCUB 2.13.0 for ROCm 5.4.0</p>
<section id="id323">
<h5>Added<a class="headerlink" href="#id323" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>CMake functionality to improve build parallelism of the test suite that splits compilation units by
function or by parameters.</p></li>
<li><p>New overload for <code class="docutils literal notranslate"><span class="pre">BlockAdjacentDifference::SubtractLeftPartialTile</span></code> that takes a predecessor item.</p></li>
</ul>
</section>
<section id="id324">
<h5>Changed<a class="headerlink" href="#id324" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved build parallelism of the test suite by splitting up large compilation units for <code class="docutils literal notranslate"><span class="pre">DeviceRadixSort</span></code>,
<code class="docutils literal notranslate"><span class="pre">DeviceSegmentedRadixSort</span></code> and <code class="docutils literal notranslate"><span class="pre">DeviceSegmentedSort</span></code>.</p></li>
<li><p>CUB backend references CUB and thrust version 1.17.1.</p></li>
</ul>
</section>
</section>
<section id="hipfft-1-0-10">
<h4>hipFFT 1.0.10<a class="headerlink" href="#hipfft-1-0-10" title="Link to this heading">#</a></h4>
<p>hipFFT 1.0.10 for ROCm 5.4.0</p>
<section id="id325">
<h5>Added<a class="headerlink" href="#id325" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added hipfftExtPlanScaleFactor API to efficiently multiply each output element of a FFT by a given scaling factor.  Result scaling must be supported in the backend FFT library.</p></li>
</ul>
</section>
<section id="id326">
<h5>Changed<a class="headerlink" href="#id326" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>When hipFFT is built against the rocFFT backend, rocFFT 1.0.19 or higher is now required.</p></li>
</ul>
</section>
</section>
<section id="hipsolver-1-6-0">
<h4>hipSOLVER 1.6.0<a class="headerlink" href="#hipsolver-1-6-0" title="Link to this heading">#</a></h4>
<p>hipSOLVER 1.6.0 for ROCm 5.4.0</p>
<section id="id327">
<h5>Added<a class="headerlink" href="#id327" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added compatibility-only functions</p>
<ul>
<li><p>gesvdaStridedBatched</p>
<ul>
<li><p>hipsolverDnSgesvdaStridedBatched_bufferSize, hipsolverDnDgesvdaStridedBatched_bufferSize, hipsolverDnCgesvdaStridedBatched_bufferSize, hipsolverDnZgesvdaStridedBatched_bufferSize</p></li>
<li><p>hipsolverDnSgesvdaStridedBatched, hipsolverDnDgesvdaStridedBatched, hipsolverDnCgesvdaStridedBatched, hipsolverDnZgesvdaStridedBatched</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</section>
</section>
<section id="hipsparse-2-3-3">
<h4>hipSPARSE 2.3.3<a class="headerlink" href="#hipsparse-2-3-3" title="Link to this heading">#</a></h4>
<p>hipSPARSE 2.3.3 for ROCm 5.4.0</p>
<section id="id328">
<h5>Added<a class="headerlink" href="#id328" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added hipsparseCsr2cscEx2_bufferSize and hipsparseCsr2cscEx2 routines</p></li>
</ul>
</section>
<section id="id329">
<h5>Changed<a class="headerlink" href="#id329" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>HIPSPARSE_ORDER_COLUMN has been renamed to HIPSPARSE_ORDER_COL to match cusparse</p></li>
</ul>
</section>
</section>
<section id="rccl-2-13-4">
<h4>rccl 2.13.4<a class="headerlink" href="#rccl-2-13-4" title="Link to this heading">#</a></h4>
<p>RCCL 2.13.4 for ROCm 5.4.0</p>
<section id="id330">
<h5>Changed<a class="headerlink" href="#id330" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Compatibility with NCCL 2.13.4</p></li>
<li><p>Improvements to RCCL when running with hipGraphs</p></li>
<li><p>RCCL_ENABLE_HIPGRAPH environment variable is no longer necessary to enable hipGraph support</p></li>
<li><p>Minor latency improvements</p></li>
</ul>
</section>
<section id="id331">
<h5>Fixed<a class="headerlink" href="#id331" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Resolved potential memory access error due to asynchronous memset</p></li>
</ul>
</section>
</section>
<section id="rocalution-2-1-3">
<h4>rocALUTION 2.1.3<a class="headerlink" href="#rocalution-2-1-3" title="Link to this heading">#</a></h4>
<p>rocALUTION 2.1.3 for ROCm 5.4.0</p>
<section id="id332">
<h5>Added<a class="headerlink" href="#id332" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added build support for Navi31 and Navi33</p></li>
<li><p>Added support for non-squared global matrices</p></li>
</ul>
</section>
<section id="id333">
<h5>Improved<a class="headerlink" href="#id333" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed a memory leak in MatrixMult on HIP backend</p></li>
<li><p>Global structures can now be used with a single process</p></li>
</ul>
</section>
<section id="id334">
<h5>Changed<a class="headerlink" href="#id334" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Switched GTest death test style to ‘threadsafe’</p></li>
<li><p>GlobalVector::GetGhostSize() is deprecated and will be removed</p></li>
<li><p>ParallelManager::GetGlobalSize(), ParallelManager::GetLocalSize(), ParallelManager::SetGlobalSize() and ParallelManager::SetLocalSize() are deprecated and will be removed</p></li>
<li><p>Vector::GetGhostSize() is deprecated and will be removed</p></li>
<li><p>Multigrid::SetOperatorFormat(unsigned int) is deprecated and will be removed, use Multigrid::SetOperatorFormat(unsigned int, int) instead</p></li>
<li><p>RugeStuebenAMG::SetCouplingStrength(ValueType) is deprecated and will be removed, use SetStrengthThreshold(float) instead</p></li>
</ul>
</section>
</section>
<section id="rocblas-2-46-0">
<h4>rocBLAS 2.46.0<a class="headerlink" href="#rocblas-2-46-0" title="Link to this heading">#</a></h4>
<p>rocBLAS 2.46.0 for ROCm 5.4.0</p>
<section id="id335">
<h5>Added<a class="headerlink" href="#id335" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>client smoke test dataset added for quick validation using command rocblas-test –yaml rocblas_smoke.yaml</p></li>
<li><p>Added stream order device memory allocation as a non-default beta option.</p></li>
</ul>
</section>
<section id="id336">
<h5>Optimized<a class="headerlink" href="#id336" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved trsm performance for small sizes by using a substitution method technique</p></li>
<li><p>Improved syr2k and her2k performance significantly by using a block-recursive algorithm</p></li>
</ul>
</section>
<section id="id337">
<h5>Changed<a class="headerlink" href="#id337" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Level 2, Level 1, and Extension functions: argument checking when the handle is set to rocblas_pointer_mode_host now returns the status of rocblas_status_invalid_pointer only for pointers that must be dereferenced based on the alpha and beta argument values.  With handle mode rocblas_pointer_mode_device only pointers that are always dereferenced regardless of alpha and beta values are checked and so may lead to a return status of rocblas_status_invalid_pointer.   This improves consistency with legacy BLAS behaviour.</p></li>
<li><p>Add variable to turn on/off ieee16/ieee32 tests for mixed precision gemm</p></li>
<li><p>Allow hipBLAS to select int8 datatype</p></li>
<li><p>Disallow B == C &amp;&amp; ldb != ldc in rocblas_xtrmm_outofplace</p></li>
</ul>
</section>
<section id="id338">
<h5>Fixed<a class="headerlink" href="#id338" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>FORTRAN interfaces generalized for FORTRAN compilers other than gfortran</p></li>
<li><p>fix for trsm_strided_batched rocblas-bench performance gathering</p></li>
<li><p>Fix for rocm-smi path in commandrunner.py script to match ROCm 5.2 and above</p></li>
</ul>
</section>
</section>
<section id="rocfft-1-0-19">
<h4>rocFFT 1.0.19<a class="headerlink" href="#rocfft-1-0-19" title="Link to this heading">#</a></h4>
<p>rocFFT 1.0.19 for ROCm 5.4.0</p>
<section id="id339">
<h5>Optimizations<a class="headerlink" href="#id339" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimized some strided large 1D plans.</p></li>
</ul>
</section>
<section id="id340">
<h5>Added<a class="headerlink" href="#id340" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added rocfft_plan_description_set_scale_factor API to efficiently multiply each output element of a FFT by a given scaling factor.</p></li>
<li><p>Created a rocfft_kernel_cache.db file next to the installed library. SBCC kernels are moved to this file when built with the library, and are runtime-compiled for new GPU architectures.</p></li>
<li><p>Added gfx1100 and gfx1102 to default AMDGPU_TARGETS.</p></li>
</ul>
</section>
<section id="id341">
<h5>Changed<a class="headerlink" href="#id341" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Moved runtime compilation cache to in-memory by default.  A default on-disk cache can encounter contention problems
on multi-node clusters with a shared filesystem.  rocFFT can still be told to use an on-disk cache by setting the
ROCFFT_RTC_CACHE_PATH environment variable.</p></li>
</ul>
</section>
</section>
<section id="rocprim-2-12-0">
<h4>rocPRIM 2.12.0<a class="headerlink" href="#rocprim-2-12-0" title="Link to this heading">#</a></h4>
<p>rocPRIM 2.12.0 for ROCm 5.4.0</p>
<section id="id342">
<h5>Changed<a class="headerlink" href="#id342" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device_partition</span></code>, <code class="docutils literal notranslate"><span class="pre">device_unique</span></code>, and <code class="docutils literal notranslate"><span class="pre">device_reduce_by_key</span></code> now support problem
sizes larger than 2^32 items.</p></li>
</ul>
</section>
<section id="id343">
<h5>Removed<a class="headerlink" href="#id343" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">block_sort::sort()</span></code> overload for keys and values with a dynamic size. This overload was documented but the
implementation is missing. To avoid further confusion the documentation is removed until a decision is made on
implementing the function.</p></li>
</ul>
</section>
<section id="id344">
<h5>Fixed<a class="headerlink" href="#id344" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed the compilation failure in <code class="docutils literal notranslate"><span class="pre">device_merge</span></code> if the two key iterators don’t match.</p></li>
</ul>
</section>
</section>
<section id="rocrand-2-10-16">
<h4>rocRAND 2.10.16<a class="headerlink" href="#rocrand-2-10-16" title="Link to this heading">#</a></h4>
<p>rocRAND 2.10.16 for ROCm 5.4.0</p>
<section id="id345">
<h5>Added<a class="headerlink" href="#id345" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>MRG31K3P pseudorandom number generator based on L’Ecuyer and Touzin, 2000, “Fast combined multiple recursive generators with multipliers of the form a = ±2q ±2r”.</p></li>
<li><p>LFSR113 pseudorandom number generator based on L’Ecuyer, 1999, “Tables of maximally equidistributed combined LFSR generators”.</p></li>
<li><p>SCRAMBLED_SOBOL32 and SCRAMBLED_SOBOL64 quasirandom number generators. The Scrambled Sobol sequences are generated by scrambling the output of a Sobol sequence.</p></li>
</ul>
</section>
<section id="id346">
<h5>Changed<a class="headerlink" href="#id346" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The <code class="docutils literal notranslate"><span class="pre">mrg_&amp;lt;distribution&amp;gt;_distribution</span></code> structures, which provided numbers based on MRG32K3A, are now replaced by <code class="docutils literal notranslate"><span class="pre">mrg_engine_&amp;lt;distribution&amp;gt;_distribution</span></code>, where <code class="docutils literal notranslate"><span class="pre">&amp;lt;distribution&amp;gt;</span></code> is <code class="docutils literal notranslate"><span class="pre">log_normal</span></code>, <code class="docutils literal notranslate"><span class="pre">normal</span></code>, <code class="docutils literal notranslate"><span class="pre">poisson</span></code>, or <code class="docutils literal notranslate"><span class="pre">uniform</span></code>. These structures provide numbers for MRG31K3P (with template type <code class="docutils literal notranslate"><span class="pre">rocrand_state_mrg31k3p</span></code>) and MRG32K3A (with template type <code class="docutils literal notranslate"><span class="pre">rocrand_state_mrg32k3a</span></code>).</p></li>
</ul>
</section>
<section id="id347">
<h5>Fixed<a class="headerlink" href="#id347" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Sobol64 now returns 64 bits random numbers, instead of 32 bits random numbers. As a result, the performance of this generator has regressed.</p></li>
<li><p>Fixed a bug that prevented compiling code in C++ mode (with a host compiler) when it included the rocRAND headers on Windows.</p></li>
</ul>
</section>
</section>
<section id="rocsolver-3-20-0">
<h4>rocSOLVER 3.20.0<a class="headerlink" href="#rocsolver-3-20-0" title="Link to this heading">#</a></h4>
<p>rocSOLVER 3.20.0 for ROCm 5.4.0</p>
<section id="id348">
<h5>Added<a class="headerlink" href="#id348" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Partial SVD for bidiagonal matrices:</p>
<ul>
<li><p>BDSVDX</p></li>
</ul>
</li>
<li><p>Partial SVD for general matrices:</p>
<ul>
<li><p>GESVDX (with batched and strided_batched versions)</p></li>
</ul>
</li>
</ul>
</section>
<section id="id349">
<h5>Changed<a class="headerlink" href="#id349" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Changed <code class="docutils literal notranslate"><span class="pre">ROCSOLVER_EMBED_FMT</span></code> default to <code class="docutils literal notranslate"><span class="pre">ON</span></code> for users building directly with CMake.
This matches the existing default when building with install.sh or rmake.py.</p></li>
</ul>
</section>
</section>
<section id="rocsparse-2-4-0">
<h4>rocSPARSE 2.4.0<a class="headerlink" href="#rocsparse-2-4-0" title="Link to this heading">#</a></h4>
<p>rocSPARSE 2.4.0 for ROCm 5.4.0</p>
<section id="id350">
<h5>Added<a class="headerlink" href="#id350" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added rocsparse_spmv_ex routine</p></li>
<li><p>Added rocsparse_bsrmv_ex_analysis and rocsparse_bsrmv_ex routines</p></li>
<li><p>Added csritilu0 routine</p></li>
<li><p>Added build support for Navi31 and Navi 33</p></li>
</ul>
</section>
<section id="id351">
<h5>Improved<a class="headerlink" href="#id351" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimization to segmented algorithm for COO SpMV by performing analysis</p></li>
<li><p>Improve performance when generating random matrices.</p></li>
<li><p>Fixed bug in ellmv</p></li>
<li><p>Optimized bsr2csr routine</p></li>
<li><p>Fixed integer overflow bugs</p></li>
</ul>
</section>
</section>
<section id="rocthrust-2-17-0">
<h4>rocThrust 2.17.0<a class="headerlink" href="#rocthrust-2-17-0" title="Link to this heading">#</a></h4>
<p>rocThrust 2.17.0 for ROCm 5.4.0</p>
<section id="id352">
<h5>Added<a class="headerlink" href="#id352" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Updated to match upstream Thrust 1.17.0</p></li>
</ul>
</section>
</section>
<section id="rocwmma-0-9">
<h4>rocWMMA 0.9<a class="headerlink" href="#rocwmma-0-9" title="Link to this heading">#</a></h4>
<p>rocWMMA 0.9 for ROCm 5.4.0</p>
<section id="id353">
<h5>Added<a class="headerlink" href="#id353" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added gemm driver APIs for flow control builtins</p></li>
<li><p>Added benchmark logging systems</p></li>
<li><p>Restructured tests to follow naming convention. Added macros for test generation</p></li>
</ul>
</section>
<section id="id354">
<h5>Changed<a class="headerlink" href="#id354" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Changed CMake to accomodate the modified test infrastructure</p></li>
<li><p>Fine tuned the multi-block kernels with and without lds</p></li>
<li><p>Adjusted Maximum Vector Width to dWordx4 Width</p></li>
<li><p>Updated Efficiencies to display as whole number percentages</p></li>
<li><p>Updated throughput from GFlops/s to TFlops/s</p></li>
<li><p>Reset the ad-hoc tests to use smaller sizes</p></li>
<li><p>Modified the output validation to use CPU-based implementation against rocWMMA</p></li>
<li><p>Modified the extended vector test to return error codes for memory allocation failures</p></li>
</ul>
</section>
</section>
<section id="tensile-4-35-0">
<h4>Tensile 4.35.0<a class="headerlink" href="#tensile-4-35-0" title="Link to this heading">#</a></h4>
<p>Tensile 4.35.0 for ROCm 5.4.0</p>
<section id="id355">
<h5>Added<a class="headerlink" href="#id355" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Async DMA support for Transpose Data Layout (ThreadSeparateGlobalReadA/B)</p></li>
<li><p>Option to output library logic in dictionary format</p></li>
<li><p>No solution found error message for benchmarking client</p></li>
<li><p>Exact K check for StoreCInUnrollExact</p></li>
<li><p>Support for CGEMM + MIArchVgpr</p></li>
<li><p>client-path parameter for using prebuilt client</p></li>
<li><p>CleanUpBuildFiles global parameter</p></li>
<li><p>Debug flag for printing library logic index of winning solution</p></li>
<li><p>NumWarmups global parameter for benchmarking</p></li>
<li><p>Windows support for benchmarking client</p></li>
<li><p>DirectToVgpr support for CGEMM</p></li>
<li><p>TensileLibLogicToYaml for creating tuning configs from library logic solutions</p></li>
</ul>
</section>
<section id="id356">
<h5>Optimizations<a class="headerlink" href="#id356" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Put beta code and store separately if StoreCInUnroll = x4 store</p></li>
<li><p>Improved performance for StoreCInUnroll + b128 store</p></li>
</ul>
</section>
<section id="id357">
<h5>Changed<a class="headerlink" href="#id357" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Re-enable HardwareMonitor for gfx90a</p></li>
<li><p>Decision trees use MLFeatures instead of Properties</p></li>
</ul>
</section>
<section id="id358">
<h5>Fixed<a class="headerlink" href="#id358" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Reject DirectToVgpr + MatrixInstBM/BN &gt; 1</p></li>
<li><p>Fix benchmark timings when using warmups and/or validation</p></li>
<li><p>Fix mismatch issue with DirectToVgprB + VectorWidth &gt; 1</p></li>
<li><p>Fix mismatch issue with DirectToLds + NumLoadsCoalesced &gt; 1 + TailLoop</p></li>
<li><p>Fix incorrect reject condition for DirectToVgpr</p></li>
<li><p>Fix reject condition for DirectToVgpr + MIWaveTile &lt; VectorWidth</p></li>
<li><p>Fix incorrect instruction generation with StoreCInUnroll</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-3-3">
<h2>ROCm 5.3.3<a class="headerlink" href="#rocm-5-3-3" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<section id="id359">
<h3>Defect fixes<a class="headerlink" href="#id359" title="Link to this heading">#</a></h3>
<section id="issue-with-rocthrust-and-rocprim-libraries">
<h4>Issue with rocTHRUST and rocPRIM libraries<a class="headerlink" href="#issue-with-rocthrust-and-rocprim-libraries" title="Link to this heading">#</a></h4>
<p>There was a known issue with rocTHRUST and rocPRIM libraries supporting iterator and types in ROCm
v5.3.x releases.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">thrust::merge</span></code> no longer correctly supports different iterator types for <code class="docutils literal notranslate"><span class="pre">keys_input1</span></code> and
<code class="docutils literal notranslate"><span class="pre">keys_input2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprim::device_merge</span></code> no longer correctly supports using different types for <code class="docutils literal notranslate"><span class="pre">keys_input1</span></code> and
<code class="docutils literal notranslate"><span class="pre">keys_input2</span></code>.</p></li>
</ul>
<p>This issue is resolved with the following fixes to compilation failures:</p>
<ul class="simple">
<li><p>rocPRIM: in device_merge if the two key iterators do not match.</p></li>
<li><p>rocTHRUST: in thrust::merge if the two key iterators do not match.</p></li>
</ul>
</section>
</section>
<section id="library-changes-in-rocm-5-3-3">
<h3>Library changes in ROCM 5.3.3<a class="headerlink" href="#library-changes-in-rocm-5-3-3" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.3.3">0.52.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.3.3">2.12.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.3.3">1.0.9</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.3.3">1.5.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.3.3">2.3.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.3.3">2.12.10</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.3.3">2.1.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.3.3">2.45.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.3.3">1.0.18</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocm-cmake</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.3.3">0.8.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.3.3">2.11.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.3.3">2.10.15</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.3.3">3.19.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.3.3">2.2.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.3.3">2.16.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocWMMA</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.3.3">0.8</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.3.3">4.34.0</a></p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-3-2">
<h2>ROCm 5.3.2<a class="headerlink" href="#rocm-5-3-2" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<section id="id360">
<h3>Defect fixes<a class="headerlink" href="#id360" title="Link to this heading">#</a></h3>
<p>The following known issues in ROCm v5.3.2 are fixed in this release.</p>
<section id="peer-to-peer-dma-mapping-errors-with-sles-and-rhel">
<h4>Peer-to-peer DMA mapping errors with SLES and RHEL<a class="headerlink" href="#peer-to-peer-dma-mapping-errors-with-sles-and-rhel" title="Link to this heading">#</a></h4>
<p>Peer-to-Peer Direct Memory Access (DMA) mapping errors on Dell systems (R7525 and R750XA) with
SLES 15 SP3/SP4 and RHEL 9.0 are fixed in this release.</p>
<p>Previously, running <code class="docutils literal notranslate"><span class="pre">rocminfo</span></code> resulted in Peer-to-Peer DMA mapping errors.</p>
</section>
<section id="rccl-tuning-table">
<h4>RCCL tuning table<a class="headerlink" href="#rccl-tuning-table" title="Link to this heading">#</a></h4>
<p>The RCCL tuning table is updated for supported platforms.</p>
</section>
<section id="sgemm-f32-gemm-routines-in-rocblas">
<h4>SGEMM (F32 GEMM) routines in rocBLAS<a class="headerlink" href="#sgemm-f32-gemm-routines-in-rocblas" title="Link to this heading">#</a></h4>
<p>Functional correctness failures in SGEMM (F32 GEMM) routines in rocBLAS for certain problem sizes
and ranges are fixed in this release.</p>
</section>
</section>
<section id="id361">
<h3>Known issues<a class="headerlink" href="#id361" title="Link to this heading">#</a></h3>
<p>This section consists of known issues in this release.</p>
<section id="amd-instinct-mi200-sriov-virtualization-issue">
<h4>AMD Instinct™ MI200 SRIOV virtualization issue<a class="headerlink" href="#amd-instinct-mi200-sriov-virtualization-issue" title="Link to this heading">#</a></h4>
<p>There is a known issue in this ROCm v5.3 release with all AMD Instinct™ MI200 devices running within
a virtual function (VF) under SRIOV virtualization. This issue will likely impact the functionality of
SRIOV-based workloads but does not impact Discrete Device Assignment (DDA) or bare metal.</p>
<p>Until a fix is provided, users should rely on ROCm v5.2.3 to support their SRIOV workloads.</p>
</section>
<section id="amd-instinct-mi200-firmware-updates">
<h4>AMD Instinct™ MI200 firmware updates<a class="headerlink" href="#amd-instinct-mi200-firmware-updates" title="Link to this heading">#</a></h4>
<p>Customers cannot update the Integrated Firmware Image (IFWI) for AMD Instinct™ MI200 accelerators.</p>
<p>An updated firmware maintenance bundle consisting of an installation tool and images specific to
AMD Instinct™ MI200 accelerators is under planning and will be available soon.</p>
</section>
<section id="known-issue-with-rocthrust-and-rocprim-libraries">
<h4>Known issue with rocThrust and rocPRIM libraries<a class="headerlink" href="#known-issue-with-rocthrust-and-rocprim-libraries" title="Link to this heading">#</a></h4>
<p>There is a known known issue with rocThrust and rocPRIM libraries supporting iterator and types in
ROCm v5.3.x releases.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">thrust::merge</span></code> no longer correctly supports different iterator types for <code class="docutils literal notranslate"><span class="pre">keys_input1</span></code> and
<code class="docutils literal notranslate"><span class="pre">keys_input2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocprim::device_merge</span></code> no longer correctly supports using different types for <code class="docutils literal notranslate"><span class="pre">keys_input1</span></code> and
<code class="docutils literal notranslate"><span class="pre">keys_input2</span></code>.</p></li>
</ul>
<p>This issue is currently under investigation and will be resolved in a future release.</p>
</section>
</section>
<section id="library-changes-in-rocm-5-3-2">
<h3>Library changes in ROCM 5.3.2<a class="headerlink" href="#library-changes-in-rocm-5-3-2" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.3.2">0.52.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.3.2">2.12.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.3.2">1.0.9</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.3.2">1.5.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.3.2">2.3.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.3.2">2.12.10</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.3.2">2.1.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.3.2">2.45.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.3.2">1.0.18</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocm-cmake</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.3.2">0.8.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.3.2">2.11.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.3.2">2.10.15</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.3.2">3.19.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.3.2">2.2.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.3.2">2.16.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocWMMA</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.3.2">0.8</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.3.2">4.34.0</a></p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-3-0">
<h2>ROCm 5.3.0<a class="headerlink" href="#rocm-5-3-0" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<section id="id362">
<h3>Deprecations and warnings<a class="headerlink" href="#id362" title="Link to this heading">#</a></h3>
<section id="id363">
<h4>HIP Perl scripts deprecation<a class="headerlink" href="#id363" title="Link to this heading">#</a></h4>
<p>The <code class="docutils literal notranslate"><span class="pre">hipcc</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> Perl scripts are deprecated. In a future release, compiled binaries will be
available as <code class="docutils literal notranslate"><span class="pre">hipcc.bin</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.bin</span></code> as replacements for the Perl scripts.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>There will be a transition period where the Perl scripts and compiled binaries are available  before the
scripts are removed. There will be no functional difference between the Perl scripts and their compiled
binary counterpart. No user action is required. Once these are available, users can optionally switch to
<code class="docutils literal notranslate"><span class="pre">hipcc.bin</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.bin</span></code>. The <code class="docutils literal notranslate"><span class="pre">hipcc</span></code>/<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> soft link will be assimilated to point from
<code class="docutils literal notranslate"><span class="pre">hipcc</span></code>/<code class="docutils literal notranslate"><span class="pre">hipconfig</span></code> to the respective compiled binaries as the default option.</p>
</div>
</section>
<section id="id364">
<h4>Linux file system hierarchy standard for ROCm<a class="headerlink" href="#id364" title="Link to this heading">#</a></h4>
<p>ROCm packages have adopted the Linux foundation file system hierarchy standard in this release to
ensure ROCm components follow open source conventions for Linux-based distributions. While
moving to a new file system hierarchy, ROCm ensures backward compatibility with its 5.1 version or
older file system hierarchy. See below for a detailed explanation of the new file system hierarchy and
backward compatibility.</p>
<section id="id365">
<h5>New file system hierarchy<a class="headerlink" href="#id365" title="Link to this heading">#</a></h5>
<p>The following is the new file system hierarchy:</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>/opt/rocm-&lt;ver&gt;
    | --bin
      | --All externally exposed Binaries
    | --libexec
        | --&lt;component&gt;
            | -- Component specific private non-ISA executables (architecture independent)
    | --include
        | -- &lt;component&gt;
            | --&lt;header files&gt;
    | --lib
        | --lib&lt;soname&gt;.so -&gt; lib&lt;soname&gt;.so.major -&gt; lib&lt;soname&gt;.so.major.minor.patch
            (public libraries linked with application)
        | --&lt;component&gt; (component specific private library, executable data)
        | --&lt;cmake&gt;
            | --components
                | --&lt;component&gt;.config.cmake
    | --share
        | --html/&lt;component&gt;/*.html
        | --info/&lt;component&gt;/*.[pdf, md, txt]
        | --man
        | --doc
            | --&lt;component&gt;
                | --&lt;licenses&gt;
        | --&lt;component&gt;
            | --&lt;misc files&gt; (arch independent non-executable)
            | --samples
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>ROCm will not support backward compatibility with the v5.1(old) file system hierarchy in its next major
release.</p>
</div>
<p>For more information, refer to <a class="reference external" href="https://refspecs.linuxfoundation.org/fhs.shtml">https://refspecs.linuxfoundation.org/fhs.shtml</a>.</p>
</section>
<section id="id366">
<h5>Backward compatibility with older file systems<a class="headerlink" href="#id366" title="Link to this heading">#</a></h5>
<p>ROCm has moved header files and libraries to its new location as indicated in the above structure and
included symbolic-link and wrapper header files in its old location for backward compatibility.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>ROCm will continue supporting backward compatibility until the next major release.</p>
</div>
</section>
<section id="id367">
<h5>Wrapper header files<a class="headerlink" href="#id367" title="Link to this heading">#</a></h5>
<p>Wrapper header files are placed in the old location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/include</span></code>) with a
warning message to include files from the new location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/include</span></code>) as shown in the
example below:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Code snippet from hip_runtime.h</span>
<span class="cp">#pragma message “This file is deprecated. Use file from include path /opt/rocm-ver/include/ and prefix with hip”.</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">"hip/hip_runtime.h"</span>
</pre></div>
</div>
<p>The wrapper header files’ backward compatibility deprecation is as follows:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">#pragma</span></code> message announcing deprecation – ROCm v5.2 release</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">#pragma</span></code> message changed to <code class="docutils literal notranslate"><span class="pre">#warning</span></code> – Future release</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">#warning</span></code> changed to <code class="docutils literal notranslate"><span class="pre">#error</span></code> – Future release</p></li>
<li><p>Backward compatibility wrappers removed – Future release</p></li>
</ul>
</section>
<section id="id368">
<h5>Library files<a class="headerlink" href="#id368" title="Link to this heading">#</a></h5>
<p>Library files are available in the <code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/lib</span></code> folder. For backward compatibility, the old library
location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/lib</span></code>) has a soft link to the library at the new location.</p>
<p>Example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>ls<span class="w"> </span>-l<span class="w"> </span>/opt/rocm/hip/lib/
total<span class="w"> </span><span class="m">4</span>
drwxr-xr-x<span class="w"> </span><span class="m">4</span><span class="w"> </span>root<span class="w"> </span>root<span class="w"> </span><span class="m">4096</span><span class="w"> </span>May<span class="w"> </span><span class="m">12</span><span class="w"> </span><span class="m">10</span>:45<span class="w"> </span>cmake
lrwxrwxrwx<span class="w"> </span><span class="m">1</span><span class="w"> </span>root<span class="w"> </span>root<span class="w">   </span><span class="m">24</span><span class="w"> </span>May<span class="w"> </span><span class="m">10</span><span class="w"> </span><span class="m">23</span>:32<span class="w"> </span>libamdhip64.so<span class="w"> </span>-&gt;<span class="w"> </span>../../lib/libamdhip64.so
</pre></div>
</div>
</section>
<section id="id369">
<h5>CMake config files<a class="headerlink" href="#id369" title="Link to this heading">#</a></h5>
<p>All CMake configuration files are available in the <code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/lib/cmake/&lt;component&gt;</span></code> folder. For
backward compatibility, the old CMake locations (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/lib/cmake</span></code>) consist of
a soft link to the new CMake config.</p>
<p>Example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>ls<span class="w"> </span>-l<span class="w"> </span>/opt/rocm/hip/lib/cmake/hip/
total<span class="w"> </span><span class="m">0</span>
lrwxrwxrwx<span class="w"> </span><span class="m">1</span><span class="w"> </span>root<span class="w"> </span>root<span class="w"> </span><span class="m">42</span><span class="w"> </span>May<span class="w"> </span><span class="m">10</span><span class="w"> </span><span class="m">23</span>:32<span class="w"> </span>hip-config.cmake<span class="w"> </span>-&gt;<span class="w"> </span>../../../../lib/cmake/hip/hip-config.cmake
</pre></div>
</div>
</section>
</section>
</section>
<section id="id370">
<h3>Defect fixes<a class="headerlink" href="#id370" title="Link to this heading">#</a></h3>
<p>The following defects are fixed in this release.</p>
<p>These defects were identified and documented as known issues in previous ROCm releases and are
fixed in the ROCm v5.3 release.</p>
<section id="kernel-produces-incorrect-results-with-rocm-5-2">
<h4>Kernel produces incorrect results with ROCm 5.2<a class="headerlink" href="#kernel-produces-incorrect-results-with-rocm-5-2" title="Link to this heading">#</a></h4>
<p>User code did not initialize certain data constructs, leading to a correctness issue. A strict reading of
the C++ standard suggests that failing to initialize these data constructs is undefined behavior.
However, a special case was added for a specific compiler builtin to handle the uninitialized data in a
defined manner.</p>
<p>The compiler fix consists of the following patches:</p>
<ul class="simple">
<li><p>A new <code class="docutils literal notranslate"><span class="pre">noundef</span></code> attribute is added. This attribute denotes when a function call argument or return
value may never contain uninitialized bits. For more information, see
<a class="reference external" href="https://reviews.llvm.org/D81678">https://reviews.llvm.org/D81678</a></p></li>
<li><p>The application of this attribute was refined such that it was not added to a specific compiler built-in
where the compiler knows that inactive lanes do not impact program execution. For more
information, see
<a class="github reference external" href="https://github.com/RadeonOpenCompute/llvm-project/commit/accf36c58409268ca1f216cdf5ad812ba97ceccd">RadeonOpenCompute/llvm-project</a>.</p></li>
</ul>
</section>
</section>
<section id="id371">
<h3>Known issues<a class="headerlink" href="#id371" title="Link to this heading">#</a></h3>
<p>This section consists of known issues in this release.</p>
<section id="issue-with-openmp-extras-package-upgrade">
<h4>Issue with OpenMP-extras package upgrade<a class="headerlink" href="#issue-with-openmp-extras-package-upgrade" title="Link to this heading">#</a></h4>
<p>The <code class="docutils literal notranslate"><span class="pre">openmp-extras</span></code> package has been split into runtime (<code class="docutils literal notranslate"><span class="pre">openmp-extras-runtime</span></code>) and dev
(<code class="docutils literal notranslate"><span class="pre">openmp-extras-devel</span></code>) packages. This change has broken the upgrade support for the
<code class="docutils literal notranslate"><span class="pre">openmp-extras</span></code> package in RHEL/SLES.</p>
<p>An available workaround in RHEL is to use the following command for upgrades:</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>yum<span class="w"> </span>upgrade<span class="w"> </span>rocm-language-runtime<span class="w"> </span>--allowerasing
</pre></div>
</div>
<p>An available workaround in SLES is to use the following command for upgrades:</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>zypper<span class="w"> </span>update<span class="w"> </span>--force-resolution<span class="w"> </span>&lt;meta-package&gt;
</pre></div>
</div>
</section>
<section id="id372">
<h4>AMD Instinct™ MI200 SRIOV virtualization issue<a class="headerlink" href="#id372" title="Link to this heading">#</a></h4>
<p>There is a known issue in this ROCm v5.3 release with all AMD Instinct™ MI200 devices running within
a virtual function (VF) under SRIOV virtualization. This issue will likely impact the functionality of
SRIOV-based workloads, but does not impact Discrete Device Assignment (DDA) or Bare Metal.</p>
<p>Until a fix is provided, users should rely on ROCm v5.2.3 to support their SRIOV workloads.</p>
</section>
<section id="system-crash-when-immou-is-enabled">
<h4>System crash when IMMOU is enabled<a class="headerlink" href="#system-crash-when-immou-is-enabled" title="Link to this heading">#</a></h4>
<p>If input-output memory management unit (IOMMU) is enabled in SBIOS and ROCm is installed, the
system may report the following failure or errors when running workloads such as bandwidth test,
clinfo, and HelloWord.cl and cause a system crash.</p>
<ul class="simple">
<li><p>IO PAGE FAULT</p></li>
<li><p>IRQ remapping does not support X2APIC mode</p></li>
<li><p>NMI error</p></li>
</ul>
<p>Workaround: To avoid the system crash, add <code class="docutils literal notranslate"><span class="pre">amd_iommu=on</span> <span class="pre">iommu=pt</span></code> as the kernel bootparam, as
indicated in the warning message.</p>
</section>
</section>
<section id="library-changes-in-rocm-5-3-0">
<h3>Library changes in ROCM 5.3.0<a class="headerlink" href="#library-changes-in-rocm-5-3-0" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p>0.51.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.3.0">0.52.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p>2.11.1 ⇒ <a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.3.0">2.12.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p>1.0.8 ⇒ <a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.3.0">1.0.9</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p>1.4.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.3.0">1.5.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p>2.2.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.3.0">2.3.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.3.0">2.12.10</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p>2.0.3 ⇒ <a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.3.0">2.1.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p>2.44.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.3.0">2.45.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p>1.0.17 ⇒ <a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.3.0">1.0.18</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocm-cmake</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-5.3.0">0.8.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p>2.10.14 ⇒ <a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.3.0">2.11.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p>2.10.14 ⇒ <a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.3.0">2.10.15</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p>3.18.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.3.0">3.19.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.3.0">2.2.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p>2.15.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.3.0">2.16.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocWMMA</p></td>
<td><p>0.7 ⇒ <a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.3.0">0.8</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p>4.33.0 ⇒ <a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.3.0">4.34.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="hipblas-0-52-0">
<h4>hipBLAS 0.52.0<a class="headerlink" href="#hipblas-0-52-0" title="Link to this heading">#</a></h4>
<p>hipBLAS 0.52.0 for ROCm 5.3.0</p>
<section id="id373">
<h5>Added<a class="headerlink" href="#id373" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added –cudapath option to install.sh to allow user to specify which cuda build they would like to use.</p></li>
<li><p>Added –installcuda option to install.sh to install cuda via a package manager. Can be used with new –installcudaversion
option to specify which version of cuda to install.</p></li>
</ul>
</section>
<section id="id374">
<h5>Fixed<a class="headerlink" href="#id374" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed #includes to support a compiler version.</p></li>
<li><p>Fixed client dependency support in install.sh</p></li>
</ul>
</section>
</section>
<section id="hipcub-2-12-0">
<h4>hipCUB 2.12.0<a class="headerlink" href="#hipcub-2-12-0" title="Link to this heading">#</a></h4>
<p>hipCUB 2.12.0 for ROCm 5.3.0</p>
<section id="id375">
<h5>Added<a class="headerlink" href="#id375" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>UniqueByKey device algorithm</p></li>
<li><p>SubtractLeft, SubtractLeftPartialTile, SubtractRight, SubtractRightPartialTile overloads in BlockAdjacentDifference.</p>
<ul>
<li><p>The old overloads (FlagHeads, FlagTails, FlagHeadsAndTails) are deprecated.</p></li>
</ul>
</li>
<li><p>DeviceAdjacentDifference algorithm.</p></li>
<li><p>Extended benchmark suite of <code class="docutils literal notranslate"><span class="pre">DeviceHistogram</span></code>, <code class="docutils literal notranslate"><span class="pre">DeviceScan</span></code>, <code class="docutils literal notranslate"><span class="pre">DevicePartition</span></code>, <code class="docutils literal notranslate"><span class="pre">DeviceReduce</span></code>,
<code class="docutils literal notranslate"><span class="pre">DeviceSegmentedReduce</span></code>, <code class="docutils literal notranslate"><span class="pre">DeviceSegmentedRadixSort</span></code>, <code class="docutils literal notranslate"><span class="pre">DeviceRadixSort</span></code>, <code class="docutils literal notranslate"><span class="pre">DeviceSpmv</span></code>, <code class="docutils literal notranslate"><span class="pre">DeviceMergeSort</span></code>,
<code class="docutils literal notranslate"><span class="pre">DeviceSegmentedSort</span></code></p></li>
</ul>
</section>
<section id="id376">
<h5>Changed<a class="headerlink" href="#id376" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Obsolated type traits defined in util_type.hpp. Use the standard library equivalents instead.</p></li>
<li><p>CUB backend references CUB and thrust version 1.16.0.</p></li>
<li><p>DeviceRadixSort’s num_items parameter’s type is now templated instead of being an int.</p>
<ul>
<li><p>If an integral type with a size at most 4 bytes is passed (i.e. an int), the former logic applies.</p></li>
<li><p>Otherwise the algorithm uses a larger indexing type that makes it possible to sort input data over 2**32 elements.</p></li>
</ul>
</li>
<li><p>Improved build parallelism of the test suite by splitting up large compilation units</p></li>
</ul>
</section>
</section>
<section id="hipfft-1-0-9">
<h4>hipFFT 1.0.9<a class="headerlink" href="#hipfft-1-0-9" title="Link to this heading">#</a></h4>
<p>hipFFT 1.0.9 for ROCm 5.3.0</p>
<section id="id377">
<h5>Changed<a class="headerlink" href="#id377" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Clean up build warnings.</p></li>
<li><p>GNUInstall Dir enhancements.</p></li>
<li><p>Requires gtest 1.11.</p></li>
</ul>
</section>
</section>
<section id="hipsolver-1-5-0">
<h4>hipSOLVER 1.5.0<a class="headerlink" href="#hipsolver-1-5-0" title="Link to this heading">#</a></h4>
<p>hipSOLVER 1.5.0 for ROCm 5.3.0</p>
<section id="id378">
<h5>Added<a class="headerlink" href="#id378" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added functions</p>
<ul>
<li><p>syevj</p>
<ul>
<li><p>hipsolverSsyevj_bufferSize, hipsolverDsyevj_bufferSize, hipsolverCheevj_bufferSize, hipsolverZheevj_bufferSize</p></li>
<li><p>hipsolverSsyevj, hipsolverDsyevj, hipsolverCheevj, hipsolverZheevj</p></li>
</ul>
</li>
<li><p>syevjBatched</p>
<ul>
<li><p>hipsolverSsyevjBatched_bufferSize, hipsolverDsyevjBatched_bufferSize, hipsolverCheevjBatched_bufferSize, hipsolverZheevjBatched_bufferSize</p></li>
<li><p>hipsolverSsyevjBatched, hipsolverDsyevjBatched, hipsolverCheevjBatched, hipsolverZheevjBatched</p></li>
</ul>
</li>
<li><p>sygvj</p>
<ul>
<li><p>hipsolverSsygvj_bufferSize, hipsolverDsygvj_bufferSize, hipsolverChegvj_bufferSize, hipsolverZhegvj_bufferSize</p></li>
<li><p>hipsolverSsygvj, hipsolverDsygvj, hipsolverChegvj, hipsolverZhegvj</p></li>
</ul>
</li>
</ul>
</li>
<li><p>Added compatibility-only functions</p>
<ul>
<li><p>syevdx/heevdx</p>
<ul>
<li><p>hipsolverDnSsyevdx_bufferSize, hipsolverDnDsyevdx_bufferSize, hipsolverDnCheevdx_bufferSize, hipsolverDnZheevdx_bufferSize</p></li>
<li><p>hipsolverDnSsyevdx, hipsolverDnDsyevdx, hipsolverDnCheevdx, hipsolverDnZheevdx</p></li>
</ul>
</li>
<li><p>sygvdx/hegvdx</p>
<ul>
<li><p>hipsolverDnSsygvdx_bufferSize, hipsolverDnDsygvdx_bufferSize, hipsolverDnChegvdx_bufferSize, hipsolverDnZhegvdx_bufferSize</p></li>
<li><p>hipsolverDnSsygvdx, hipsolverDnDsygvdx, hipsolverDnChegvdx, hipsolverDnZhegvdx</p></li>
</ul>
</li>
</ul>
</li>
<li><p>Added –mem_query option to hipsolver-bench, which will print the amount of device memory workspace required by the function.</p></li>
</ul>
</section>
<section id="id379">
<h5>Changed<a class="headerlink" href="#id379" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The rocSOLVER backend will now set <code class="docutils literal notranslate"><span class="pre">info</span></code> to zero if rocSOLVER does not reference <code class="docutils literal notranslate"><span class="pre">info</span></code>. (Applies to orgbr/ungbr, orgqr/ungqr, orgtr/ungtr, ormqr/unmqr, ormtr/unmtr, gebrd, geqrf, getrs, potrs, and sytrd/hetrd).</p></li>
<li><p>gesvdj will no longer require extra workspace to transpose <code class="docutils literal notranslate"><span class="pre">V</span></code> when <code class="docutils literal notranslate"><span class="pre">jobz</span></code> is <code class="docutils literal notranslate"><span class="pre">HIPSOLVER_EIG_MODE_VECTOR</span></code> and <code class="docutils literal notranslate"><span class="pre">econ</span></code> is 1.</p></li>
</ul>
</section>
<section id="id380">
<h5>Fixed<a class="headerlink" href="#id380" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed Fortran return value declarations within hipsolver_module.f90</p></li>
<li><p>Fixed gesvdj_bufferSize returning <code class="docutils literal notranslate"><span class="pre">HIPSOLVER_STATUS_INVALID_VALUE</span></code> when <code class="docutils literal notranslate"><span class="pre">jobz</span></code> is <code class="docutils literal notranslate"><span class="pre">HIPSOLVER_EIG_MODE_NOVECTOR</span></code> and 1 &lt;= <code class="docutils literal notranslate"><span class="pre">ldv</span></code> &lt; <code class="docutils literal notranslate"><span class="pre">n</span></code></p></li>
<li><p>Fixed gesvdj returning <code class="docutils literal notranslate"><span class="pre">HIPSOLVER_STATUS_INVALID_VALUE</span></code> when <code class="docutils literal notranslate"><span class="pre">jobz</span></code> is <code class="docutils literal notranslate"><span class="pre">HIPSOLVER_EIG_MODE_VECTOR</span></code>, <code class="docutils literal notranslate"><span class="pre">econ</span></code> is 1, and <code class="docutils literal notranslate"><span class="pre">m</span></code> &lt; <code class="docutils literal notranslate"><span class="pre">n</span></code></p></li>
</ul>
</section>
</section>
<section id="hipsparse-2-3-1">
<h4>hipSPARSE 2.3.1<a class="headerlink" href="#hipsparse-2-3-1" title="Link to this heading">#</a></h4>
<p>hipSPARSE 2.3.1 for ROCm 5.3.0</p>
<section id="id381">
<h5>Added<a class="headerlink" href="#id381" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Add SpMM and SpMM batched for CSC format</p></li>
</ul>
</section>
</section>
<section id="rocalution-2-1-0">
<h4>rocALUTION 2.1.0<a class="headerlink" href="#rocalution-2-1-0" title="Link to this heading">#</a></h4>
<p>rocALUTION 2.1.0 for ROCm 5.3.0</p>
<section id="id382">
<h5>Added<a class="headerlink" href="#id382" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Benchmarking tool</p></li>
<li><p>Ext+I Interpolation with sparsify strategies added for RS-AMG</p></li>
</ul>
</section>
<section id="id383">
<h5>Improved<a class="headerlink" href="#id383" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>ParallelManager</p></li>
</ul>
</section>
</section>
<section id="rocblas-2-45-0">
<h4>rocBLAS 2.45.0<a class="headerlink" href="#rocblas-2-45-0" title="Link to this heading">#</a></h4>
<p>rocBLAS 2.45.0 for ROCm 5.3.0</p>
<section id="id384">
<h5>Added<a class="headerlink" href="#id384" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>install.sh option –upgrade_tensile_venv_pip to upgrade Pip in Tensile Virtual Environment. The corresponding CMake option is TENSILE_VENV_UPGRADE_PIP.</p></li>
<li><p>install.sh option –relocatable or -r adds rpath and removes ldconf entry on rocBLAS build.</p></li>
<li><p>install.sh option –lazy-library-loading to enable on-demand loading of tensile library files at runtime to speedup rocBLAS initialization.</p></li>
<li><p>Support for RHEL9 and CS9.</p></li>
<li><p>Added Numerical checking routine for symmetric, Hermitian, and triangular matrices, so that they could be checked for any numerical abnormalities such as NaN, Zero, infinity and denormal value.</p></li>
</ul>
</section>
<section id="id385">
<h5>Optimizations<a class="headerlink" href="#id385" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>trmm_outofplace performance improvements for all sizes and data types using block-recursive algorithm.</p></li>
<li><p>herkx performance improvements for all sizes and data types using block-recursive algorithm.</p></li>
<li><p>syrk/herk performance improvements by utilising optimised syrkx/herkx code.</p></li>
<li><p>symm/hemm performance improvements for all sizes and datatypes using block-recursive algorithm.</p></li>
</ul>
</section>
<section id="id386">
<h5>Changed<a class="headerlink" href="#id386" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Unifying library logic file names: affects HBH (-&gt;HHS_BH), BBH (-&gt;BBS_BH), 4xi8BH (-&gt;4xi8II_BH). All HPA types are using the new naming convention now.</p></li>
<li><p>Level 3 function argument checking when the handle is set to rocblas_pointer_mode_host now returns the status of rocblas_status_invalid_pointer only for pointers that must be dereferenced based on the alpha and beta argument values. With handle mode rocblas_pointer_mode_device only pointers that are always dereferenced regardless of alpha and beta values are checked and so may lead to a return status of rocblas_status_invalid_pointer. This improves consistency with legacy BLAS behaviour.</p></li>
<li><p>Level 1, 2, and 3 function argument checking for enums is now more rigorously matching legacy BLAS so returns rocblas_status_invalid_value if arguments do not match the accepted subset.</p></li>
<li><p>Add quick-return for internal trmm and gemm template functions.</p></li>
<li><p>Moved function block sizes to a shared header file.</p></li>
<li><p>Level 1, 2, and 3 functions use rocblas_stride datatype for offset.</p></li>
<li><p>Modified the matrix and vector memory allocation in our test infrastructure for all Level 1, 2, 3 and BLAS_EX functions.</p></li>
<li><p>Added specific initialization for symmetric, Hermitian, and triangular matrix types in our test infrastructure.</p></li>
<li><p>Added NaN tests to the test infrastructure for the rest of Level 3, BLAS_EX functions.</p></li>
</ul>
</section>
<section id="id387">
<h5>Fixed<a class="headerlink" href="#id387" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved logic to #include &lt;filesystem&gt; vs &lt;experimental/filesystem&gt;.</p></li>
<li><p>install.sh -s option to build rocblas as a static library.</p></li>
<li><p>dot function now sets the device results asynchronously for N &lt;= 0</p></li>
</ul>
</section>
<section id="id388">
<h5>Deprecated<a class="headerlink" href="#id388" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>is_complex helper is now deprecated.  Use rocblas_is_complex instead.</p></li>
<li><p>The enum truncate_t and the value truncate is now deprecated and will removed from the ROCm release 6.0. It is replaced by rocblas_truncate_t and rocblas_truncate, respectively. The new enum rocblas_truncate_t and the value rocblas_truncate could be used from this ROCm release for an easy transition.</p></li>
</ul>
</section>
<section id="id389">
<h5>Removed<a class="headerlink" href="#id389" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>install.sh options  –hip-clang , –no-hip-clang, –merge-files, –no-merge-files are removed.</p></li>
</ul>
</section>
</section>
<section id="rocfft-1-0-18">
<h4>rocFFT 1.0.18<a class="headerlink" href="#rocfft-1-0-18" title="Link to this heading">#</a></h4>
<p>rocFFT 1.0.18 for ROCm 5.3.0</p>
<section id="id390">
<h5>Changed<a class="headerlink" href="#id390" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Runtime compilation cache now looks for environment variables XDG_CACHE_HOME (on Linux) and LOCALAPPDATA (on
Windows) before falling back to HOME.</p></li>
</ul>
</section>
<section id="id391">
<h5>Optimizations<a class="headerlink" href="#id391" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimized 2D R2C/C2R to use 2-kernel plans where possible.</p></li>
<li><p>Improved performance of the Bluestein algorithm.</p></li>
<li><p>Optimized sbcc-168 and 100 by using half-lds.</p></li>
</ul>
</section>
<section id="id392">
<h5>Fixed<a class="headerlink" href="#id392" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed occasional failures to parallelize runtime compilation of kernels.
Failures would be retried serially and ultimately succeed, but this would take extra time.</p></li>
<li><p>Fixed failures of some R2C 3D transforms that use the unsupported TILE_UNALGNED SBRC kernels.
An example is 98^3 R2C out-of-place.</p></li>
<li><p>Fixed bugs in SBRC_ERC type.</p></li>
</ul>
</section>
</section>
<section id="rocm-cmake-0-8-0">
<h4>rocm-cmake 0.8.0<a class="headerlink" href="#rocm-cmake-0-8-0" title="Link to this heading">#</a></h4>
<p>rocm-cmake 0.8.0 for ROCm 5.3.0</p>
<section id="id393">
<h5>Fixed<a class="headerlink" href="#id393" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed error in prerm scripts created by <code class="docutils literal notranslate"><span class="pre">rocm_create_package</span></code> that could break uninstall for packages using the <code class="docutils literal notranslate"><span class="pre">PTH</span></code> option.</p></li>
</ul>
</section>
<section id="id394">
<h5>Changed<a class="headerlink" href="#id394" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ROCM_USE_DEV_COMPONENT</span></code> set to on by default for all platforms. This means that Windows will now generate runtime and devel packages by default</p></li>
<li><p>ROCMInstallTargets now defaults <code class="docutils literal notranslate"><span class="pre">CMAKE_INSTALL_LIBDIR</span></code> to <code class="docutils literal notranslate"><span class="pre">lib</span></code> if not otherwise specified.</p></li>
<li><p>Changed default Debian compression type to xz and enabled multi-threaded package compression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocm_create_package</span></code> will no longer warn upon failure to determine version of program rpmbuild.</p></li>
</ul>
</section>
</section>
<section id="rocprim-2-11-0">
<h4>rocPRIM 2.11.0<a class="headerlink" href="#rocprim-2-11-0" title="Link to this heading">#</a></h4>
<p>rocPRIM 2.11.0 for ROCm 5.3.0</p>
<section id="id395">
<h5>Added<a class="headerlink" href="#id395" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>New functions <code class="docutils literal notranslate"><span class="pre">subtract_left</span></code> and <code class="docutils literal notranslate"><span class="pre">subtract_right</span></code> in <code class="docutils literal notranslate"><span class="pre">block_adjacent_difference</span></code> to apply functions
on pairs of adjacent items distributed between threads in a block.</p></li>
<li><p>New device level <code class="docutils literal notranslate"><span class="pre">adjacent_difference</span></code> primitives.</p></li>
<li><p>Added experimental tooling for automatic kernel configuration tuning for various architectures</p></li>
<li><p>Benchmarks collect and output more detailed system information</p></li>
<li><p>CMake functionality to improve build parallelism of the test suite that splits compilation units by
function or by parameters.</p></li>
<li><p>Reverse iterator.</p></li>
</ul>
</section>
</section>
<section id="rocrand-2-10-15">
<h4>rocRAND 2.10.15<a class="headerlink" href="#rocrand-2-10-15" title="Link to this heading">#</a></h4>
<p>rocRAND 2.10.15 for ROCm 5.3.0</p>
<section id="id396">
<h5>Changed<a class="headerlink" href="#id396" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Increased number of warmup iterations for rocrand_benchmark_generate from 5 to 15 to eliminate corner cases that would generate artificially high benchmark scores.</p></li>
</ul>
</section>
</section>
<section id="rocsolver-3-19-0">
<h4>rocSOLVER 3.19.0<a class="headerlink" href="#rocsolver-3-19-0" title="Link to this heading">#</a></h4>
<p>rocSOLVER 3.19.0 for ROCm 5.3.0</p>
<section id="id397">
<h5>Added<a class="headerlink" href="#id397" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Partial eigensolver routines for symmetric/hermitian matrices:</p>
<ul>
<li><p>SYEVX (with batched and strided_batched versions)</p></li>
<li><p>HEEVX (with batched and strided_batched versions)</p></li>
</ul>
</li>
<li><p>Generalized symmetric- and hermitian-definite partial eigensolvers:</p>
<ul>
<li><p>SYGVX (with batched and strided_batched versions)</p></li>
<li><p>HEGVX (with batched and strided_batched versions)</p></li>
</ul>
</li>
<li><p>Eigensolver routines for symmetric/hermitian matrices using Jacobi algorithm:</p>
<ul>
<li><p>SYEVJ (with batched and strided_batched versions)</p></li>
<li><p>HEEVJ (with batched and strided_batched versions)</p></li>
</ul>
</li>
<li><p>Generalized symmetric- and hermitian-definite eigensolvers using Jacobi algorithm:</p>
<ul>
<li><p>SYGVJ (with batched and strided_batched versions)</p></li>
<li><p>HEGVJ (with batched and strided_batched versions)</p></li>
</ul>
</li>
<li><p>Added –profile_kernels option to rocsolver-bench, which will include kernel calls in the
profile log (if profile logging is enabled with –profile).</p></li>
</ul>
</section>
<section id="id398">
<h5>Changed<a class="headerlink" href="#id398" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Changed rocsolver-bench result labels <code class="docutils literal notranslate"><span class="pre">cpu_time</span></code> and <code class="docutils literal notranslate"><span class="pre">gpu_time</span></code> to
<code class="docutils literal notranslate"><span class="pre">cpu_time_us</span></code> and <code class="docutils literal notranslate"><span class="pre">gpu_time_us</span></code>, respectively.</p></li>
</ul>
</section>
<section id="id399">
<h5>Removed<a class="headerlink" href="#id399" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed dependency on cblas from the rocsolver test and benchmark clients.</p></li>
</ul>
</section>
<section id="id400">
<h5>Fixed<a class="headerlink" href="#id400" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed incorrect SYGS2/HEGS2, SYGST/HEGST, SYGV/HEGV, and SYGVD/HEGVD results for batch counts
larger than 32.</p></li>
<li><p>Fixed STEIN memory access fault when nev is 0.</p></li>
<li><p>Fixed incorrect STEBZ results for close eigenvalues when range = index.</p></li>
<li><p>Fixed git unsafe repository error when building with <code class="docutils literal notranslate"><span class="pre">./install.sh</span> <span class="pre">-cd</span></code> as a non-root user.</p></li>
</ul>
</section>
</section>
<section id="rocthrust-2-16-0">
<h4>rocThrust 2.16.0<a class="headerlink" href="#rocthrust-2-16-0" title="Link to this heading">#</a></h4>
<p>rocThrust 2.16.0 for ROCm 5.3.0</p>
<section id="id401">
<h5>Changed<a class="headerlink" href="#id401" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>rocThrust functionality dependent on device malloc works is functional as ROCm 5.2 reneabled device malloc. Device launched <code class="docutils literal notranslate"><span class="pre">thrust::sort</span></code> and <code class="docutils literal notranslate"><span class="pre">thrust::sort_by_key</span></code> are available for use.</p></li>
</ul>
</section>
</section>
<section id="rocwmma-0-8">
<h4>rocWMMA 0.8<a class="headerlink" href="#rocwmma-0-8" title="Link to this heading">#</a></h4>
<p>rocWMMA 0.8 for ROCm 5.3.0</p>
</section>
<section id="tensile-4-34-0">
<h4>Tensile 4.34.0<a class="headerlink" href="#tensile-4-34-0" title="Link to this heading">#</a></h4>
<p>Tensile 4.34.0 for ROCm 5.3.0</p>
<section id="id402">
<h5>Added<a class="headerlink" href="#id402" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Lazy loading of solution libraries and code object files</p></li>
<li><p>Support for dictionary style logic files</p></li>
<li><p>Support for decision tree based logic files using dictionary format</p></li>
<li><p>DecisionTreeLibrary for solution selection</p></li>
<li><p>DirectToLDS support for HGEMM</p></li>
<li><p>DirectToVgpr support for SGEMM</p></li>
<li><p>Grid based distance metric for solution selection</p></li>
<li><p>Support for gfx11xx</p></li>
<li><p>Support for DirectToVgprA/B + TLU=False</p></li>
<li><p>ForkParameters Groups as a way of specifying solution parameters</p></li>
<li><p>Support for a new Tensile yaml config format</p></li>
<li><p>TensileClientConfig for generating Tensile client config files</p></li>
<li><p>Options for TensileCreateLibrary to build client and create client config file</p></li>
</ul>
</section>
<section id="id403">
<h5>Optimizations<a class="headerlink" href="#id403" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Solution generation is now cached and is not repeated if solution parameters are unchanged</p></li>
</ul>
</section>
<section id="id404">
<h5>Changed<a class="headerlink" href="#id404" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Default MACInstruction to FMA</p></li>
</ul>
</section>
<section id="id405">
<h5>Fixed<a class="headerlink" href="#id405" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Accept StaggerUStride=0 as valid</p></li>
<li><p>Reject invalid data types for UnrollLoopEfficiencyEnable</p></li>
<li><p>Fix invalid code generation issues related to DirectToVgpr</p></li>
<li><p>Return hipErrorNotFound if no modules are loaded</p></li>
<li><p>Fix performance drop for NN ZGEMM with 96x64 macro tile</p></li>
<li><p>Fix memory violation for general batched kernels when alpha/beta/K = 0</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-2-3">
<h2>ROCm 5.2.3<a class="headerlink" href="#rocm-5-2-3" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<section id="changes-in-this-release">
<h3>Changes in this release<a class="headerlink" href="#changes-in-this-release" title="Link to this heading">#</a></h3>
<section id="ubuntu-18-04-end-of-life-announcement">
<h4>Ubuntu 18.04 end-of-life announcement<a class="headerlink" href="#ubuntu-18-04-end-of-life-announcement" title="Link to this heading">#</a></h4>
<p>Support for Ubuntu 18.04 ends in this release. Future releases of ROCm will not provide prebuilt
packages for Ubuntu 18.04.</p>
</section>
<section id="hip-runtime">
<h4>HIP runtime<a class="headerlink" href="#hip-runtime" title="Link to this heading">#</a></h4>
<section id="id406">
<h5>Fixes<a class="headerlink" href="#id406" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>A bug was discovered in the HIP graph capture implementation in the ROCm v5.2.0 release. If the
same kernel is called twice (with different argument values) in a graph capture, the implementation
only kept the argument values for the second kernel call.</p></li>
<li><p>A bug was introduced in the hiprtc implementation in the ROCm v5.2.0 release. This bug caused the
<code class="docutils literal notranslate"><span class="pre">hiprtcGetLoweredName</span></code> call to fail for named expressions with whitespace in it.</p></li>
</ul>
<p>Example:</p>
<p>The named expression <code class="docutils literal notranslate"><span class="pre">my_sqrt&lt;complex&lt;double&gt;&gt;</span></code> passed but <code class="docutils literal notranslate"><span class="pre">my_sqrt&lt;complex&lt;double</span> <span class="pre">&gt;&gt;</span></code>
failed.</p>
</section>
</section>
<section id="rccl">
<h4>RCCL<a class="headerlink" href="#rccl" title="Link to this heading">#</a></h4>
<section id="id407">
<h5>Additions<a class="headerlink" href="#id407" title="Link to this heading">#</a></h5>
<p>Compatibility with NCCL 2.12.10</p>
<ul class="simple">
<li><p>Packages for test and benchmark executables on all supported OSes using CPack</p></li>
<li><p>Added custom signal handler - opt-in with RCCL_ENABLE_SIGNALHANDLER=1</p>
<ul>
<li><p>Additional details provided if Binary File Descriptor library (BFD) is pre-installed.</p></li>
</ul>
</li>
<li><p>Added experimental support for using multiple ranks per device</p>
<ul>
<li><p>Requires using a new interface to create communicator (ncclCommInitRankMulti), refer to the
interface documentation for details.</p></li>
<li><p>To avoid potential deadlocks, user might have to set an environment variables increasing the
number of hardware queues. For example,</p></li>
</ul>
</li>
</ul>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span><span class="nb">export</span><span class="w"> </span><span class="nv">GPU_MAX_HW_QUEUES</span><span class="o">=</span><span class="m">16</span>
</pre></div>
</div>
<ul class="simple">
<li><p>Added support for reusing ports in NET/IB channels</p>
<ul>
<li><p>Opt-in with NCCL_IB_SOCK_CLIENT_PORT_REUSE=1 and NCCL_IB_SOCK_SERVER_PORT_REUSE=1</p></li>
<li><p>When “Call to bind failed: Address already in use” error happens in large-scale AlltoAll (for example,
&gt;=64 MI200 nodes), users are suggested to opt-in either one or both of the options to resolve the
massive port usage issue</p></li>
<li><p>Avoid using NCCL_IB_SOCK_SERVER_PORT_REUSE when NCCL_NCHANNELS_PER_NET_PEER is tuned
&gt;1</p></li>
</ul>
</li>
</ul>
</section>
<section id="id408">
<h5>Removals<a class="headerlink" href="#id408" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed experimental clique-based kernels</p></li>
</ul>
</section>
</section>
<section id="development-tools">
<h4>Development tools<a class="headerlink" href="#development-tools" title="Link to this heading">#</a></h4>
<p>No notable changes in this release for development tools, including the compiler, profiler, and
debugger deployment and management tools</p>
<p>No notable changes in this release for deployment and management tools.</p>
<p>For release information for older ROCm releases, refer to
<a class="github reference external" href="https://github.com/RadeonOpenCompute/ROCm/blob/master/CHANGELOG.md">RadeonOpenCompute/ROCm</a></p>
</section>
</section>
<section id="library-changes-in-rocm-5-2-3">
<h3>Library changes in ROCM 5.2.3<a class="headerlink" href="#library-changes-in-rocm-5-2-3" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.2.3">0.51.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.2.3">2.11.1</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.2.3">1.0.8</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.2.3">1.4.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.2.3">2.2.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p>2.11.4 ⇒ <a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.2.3">2.12.10</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.2.3">2.0.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.2.3">2.44.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.2.3">1.0.17</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.2.3">2.10.14</a></p></td>
</tr>
<tr class="row-even"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.2.3">2.10.14</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.2.3">3.18.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.2.3">2.2.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.2.3">2.15.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocWMMA</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.2.3">0.7</a></p></td>
</tr>
<tr class="row-odd"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.2.3">4.33.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="rccl-2-12-10">
<h4>rccl 2.12.10<a class="headerlink" href="#rccl-2-12-10" title="Link to this heading">#</a></h4>
<p>RCCL 2.12.10 for ROCm 5.2.3</p>
<section id="id409">
<h5>Added<a class="headerlink" href="#id409" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Compatibility with NCCL 2.12.10</p></li>
<li><p>Packages for test and benchmark executables on all supported OSes using CPack.</p></li>
<li><p>Adding custom signal handler - opt-in with RCCL_ENABLE_SIGNALHANDLER=1</p>
<ul>
<li><p>Additional details provided if Binary File Descriptor library (BFD) is pre-installed</p></li>
</ul>
</li>
<li><p>Adding support for reusing ports in NET/IB channels</p>
<ul>
<li><p>Opt-in with NCCL_IB_SOCK_CLIENT_PORT_REUSE=1 and NCCL_IB_SOCK_SERVER_PORT_REUSE=1</p></li>
<li><p>When “Call to bind failed : Address already in use” error happens in large-scale AlltoAll
(e.g., &gt;=64 MI200 nodes), users are suggested to opt-in either one or both of the options
to resolve the massive port usage issue</p></li>
<li><p>Avoid using NCCL_IB_SOCK_SERVER_PORT_REUSE when NCCL_NCHANNELS_PER_NET_PEER is tuned &gt;1</p></li>
</ul>
</li>
</ul>
</section>
<section id="id410">
<h5>Removed<a class="headerlink" href="#id410" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed experimental clique-based kernels</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-2-1">
<h2>ROCm 5.2.1<a class="headerlink" href="#rocm-5-2-1" title="Link to this heading">#</a></h2>
<section id="library-changes-in-rocm-5-2-1">
<h3>Library changes in ROCM 5.2.1<a class="headerlink" href="#library-changes-in-rocm-5-2-1" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.2.1">0.51.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.2.1">2.11.1</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.2.1">1.0.8</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.2.1">1.4.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.2.1">2.2.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.2.1">2.11.4</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.2.1">2.0.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.2.1">2.44.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.2.1">1.0.17</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.2.1">2.10.14</a></p></td>
</tr>
<tr class="row-even"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.2.1">2.10.14</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.2.1">3.18.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.2.1">2.2.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.2.1">2.15.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocWMMA</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.2.1">0.7</a></p></td>
</tr>
<tr class="row-odd"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.2.1">4.33.0</a></p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-2-0">
<h2>ROCm 5.2.0<a class="headerlink" href="#rocm-5-2-0" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable no-duplicate-header -->
<section id="id411">
<h3>What’s new in this release<a class="headerlink" href="#id411" title="Link to this heading">#</a></h3>
<section id="id412">
<h4>HIP enhancements<a class="headerlink" href="#id412" title="Link to this heading">#</a></h4>
<p>The ROCm v5.2 release consists of the following HIP enhancements:</p>
<section id="hip-installation-guide-updates">
<h5>HIP installation guide updates<a class="headerlink" href="#hip-installation-guide-updates" title="Link to this heading">#</a></h5>
<p>The HIP Installation Guide is updated to include building HIP tests from source on the AMD and
NVIDIA platforms.</p>
<p>For more details, refer to the HIP Installation Guide v5.2.</p>
</section>
<section id="support-for-device-side-malloc-on-hip-clang">
<h5>Support for device-side malloc on HIP-Clang<a class="headerlink" href="#support-for-device-side-malloc-on-hip-clang" title="Link to this heading">#</a></h5>
<p>HIP-Clang now supports device-side malloc. This implementation does not require the use of
<code class="docutils literal notranslate"><span class="pre">hipDeviceSetLimit(hipLimitMallocHeapSize,value)</span></code> nor respect any setting. The heap is fully dynamic
and can grow until the available free memory on the device is consumed.</p>
<p>The test codes at the following link show how to implement applications using malloc and free
functions in device kernels:</p>
<p><a class="github reference external" href="https://github.com/ROCm-Developer-Tools/HIP/blob/develop/tests/src/deviceLib/hipDeviceMalloc.cpp">ROCm-Developer-Tools/HIP</a></p>
</section>
<section id="id413">
<h5>New HIP APIs in this release<a class="headerlink" href="#id413" title="Link to this heading">#</a></h5>
<p>The following new HIP APIs are available in the ROCm v5.2 release. Note that this is a pre-official
version (beta) release of the new APIs:</p>
<section id="device-management-hip-apis">
<h6>Device management HIP APIs<a class="headerlink" href="#device-management-hip-apis" title="Link to this heading">#</a></h6>
<p>The new device management HIP APIs are as follows:</p>
<ul>
<li><p>Gets a UUID for the device. This API returns a UUID for the device.</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipDeviceGetUuid</span><span class="p">(</span><span class="n">hipUUID</span><span class="o">*</span><span class="w"> </span><span class="n">uuid</span><span class="p">,</span><span class="w"> </span><span class="n">hipDevice_t</span><span class="w"> </span><span class="n">device</span><span class="p">);</span>
</pre></div>
</div>
<p>Note that this new API corresponds to the following CUDA API:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="w">  </span><span class="n">CUresult</span><span class="w"> </span><span class="nf">cuDeviceGetUuid</span><span class="p">(</span><span class="n">CUuuid</span><span class="o">*</span><span class="w"> </span><span class="n">uuid</span><span class="p">,</span><span class="w"> </span><span class="n">CUdevice</span><span class="w"> </span><span class="n">dev</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Gets default memory pool of the specified device</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipDeviceGetDefaultMemPool</span><span class="p">(</span><span class="n">hipMemPool_t</span><span class="o">*</span><span class="w"> </span><span class="n">mem_pool</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">device</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Sets the current memory pool of a device</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipDeviceSetMemPool</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">device</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">mem_pool</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Gets the current memory pool for the specified device</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipDeviceGetMemPool</span><span class="p">(</span><span class="n">hipMemPool_t</span><span class="o">*</span><span class="w"> </span><span class="n">mem_pool</span><span class="p">,</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">device</span><span class="p">);</span>
</pre></div>
</div>
</li>
</ul>
</section>
<section id="new-hip-runtime-apis-in-memory-management">
<h6>New HIP runtime APIs in memory management<a class="headerlink" href="#new-hip-runtime-apis-in-memory-management" title="Link to this heading">#</a></h6>
<p>The new Stream Ordered Memory Allocator functions of HIP runtime APIs in memory management are:</p>
<ul>
<li><p>Allocates memory with stream ordered semantics</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMallocAsync</span><span class="p">(</span><span class="kt">void</span><span class="o">**</span><span class="w"> </span><span class="n">dev_ptr</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">stream</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Frees memory with stream ordered semantics</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipFreeAsync</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">dev_ptr</span><span class="p">,</span><span class="w"> </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">stream</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Releases freed memory back to the OS</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemPoolTrimTo</span><span class="p">(</span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">mem_pool</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">min_bytes_to_hold</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Sets attributes of a memory pool</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemPoolSetAttribute</span><span class="p">(</span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">mem_pool</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemPoolAttr</span><span class="w"> </span><span class="n">attr</span><span class="p">,</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">value</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Gets attributes of a memory pool</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemPoolGetAttribute</span><span class="p">(</span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">mem_pool</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemPoolAttr</span><span class="w"> </span><span class="n">attr</span><span class="p">,</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">value</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Controls visibility of the specified pool between devices</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemPoolSetAccess</span><span class="p">(</span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">mem_pool</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">hipMemAccessDesc</span><span class="o">*</span><span class="w"> </span><span class="n">desc_list</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">count</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Returns the accessibility of a pool from a device</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemPoolGetAccess</span><span class="p">(</span><span class="n">hipMemAccessFlags</span><span class="o">*</span><span class="w"> </span><span class="n">flags</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">mem_pool</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemLocation</span><span class="o">*</span><span class="w"> </span><span class="n">location</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Creates a memory pool</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemPoolCreate</span><span class="p">(</span><span class="n">hipMemPool_t</span><span class="o">*</span><span class="w"> </span><span class="n">mem_pool</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">hipMemPoolProps</span><span class="o">*</span><span class="w"> </span><span class="n">pool_props</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Destroys the specified memory pool</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemPoolDestroy</span><span class="p">(</span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">mem_pool</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Allocates memory from a specified pool with stream ordered semantics</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMallocFromPoolAsync</span><span class="p">(</span><span class="kt">void</span><span class="o">**</span><span class="w"> </span><span class="n">dev_ptr</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemPool_t</span><span class="w"> </span><span class="n">mem_pool</span><span class="p">,</span><span class="w"> </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">stream</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Exports a memory pool to the requested handle type</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemPoolExportToShareableHandle</span><span class="p">(</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w">                      </span><span class="n">shared_handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">hipMemPool_t</span><span class="w">               </span><span class="n">mem_pool</span><span class="p">,</span>
<span class="w">    </span><span class="n">hipMemAllocationHandleType</span><span class="w"> </span><span class="n">handle_type</span><span class="p">,</span>
<span class="w">    </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w">               </span><span class="n">flags</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Imports a memory pool from a shared handle</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemPoolImportFromShareableHandle</span><span class="p">(</span>
<span class="w">    </span><span class="n">hipMemPool_t</span><span class="o">*</span><span class="w">              </span><span class="n">mem_pool</span><span class="p">,</span>
<span class="w">    </span><span class="kt">void</span><span class="o">*</span><span class="w">                      </span><span class="n">shared_handle</span><span class="p">,</span>
<span class="w">    </span><span class="n">hipMemAllocationHandleType</span><span class="w"> </span><span class="n">handle_type</span><span class="p">,</span>
<span class="w">    </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w">               </span><span class="n">flags</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Exports data to share a memory pool allocation between processes</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemPoolExportPointer</span><span class="p">(</span><span class="n">hipMemPoolPtrExportData</span><span class="o">*</span><span class="w"> </span><span class="n">export_data</span><span class="p">,</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">dev_ptr</span><span class="p">);</span>
<span class="n">Import</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="n">memory</span><span class="w"> </span><span class="n">pool</span><span class="w"> </span><span class="n">allocation</span><span class="w"> </span><span class="n">from</span><span class="w"> </span><span class="n">another</span><span class="w"> </span><span class="n">process</span><span class="p">.</span><span class="n">t</span>
<span class="n">hipError_t</span><span class="w"> </span><span class="n">hipMemPoolImportPointer</span><span class="p">(</span>
<span class="w">    </span><span class="kt">void</span><span class="o">**</span><span class="w">                   </span><span class="n">dev_ptr</span><span class="p">,</span>
<span class="w">    </span><span class="n">hipMemPool_t</span><span class="w">             </span><span class="n">mem_pool</span><span class="p">,</span>
<span class="w">    </span><span class="n">hipMemPoolPtrExportData</span><span class="o">*</span><span class="w"> </span><span class="n">export_data</span><span class="p">);</span>
</pre></div>
</div>
</li>
</ul>
</section>
<section id="id414">
<h6>HIP graph management APIs<a class="headerlink" href="#id414" title="Link to this heading">#</a></h6>
<p>The new HIP Graph Management APIs are as follows:</p>
<ul>
<li><p>Enqueues a host function call in a stream</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipLaunchHostFunc</span><span class="p">(</span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">stream</span><span class="p">,</span><span class="w"> </span><span class="n">hipHostFn_t</span><span class="w"> </span><span class="n">fn</span><span class="p">,</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">userData</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Swaps the stream capture mode of a thread</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipThreadExchangeStreamCaptureMode</span><span class="p">(</span><span class="n">hipStreamCaptureMode</span><span class="o">*</span><span class="w"> </span><span class="n">mode</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Sets a node attribute</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipGraphKernelNodeSetAttribute</span><span class="p">(</span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">hNode</span><span class="p">,</span><span class="w"> </span><span class="n">hipKernelNodeAttrID</span><span class="w"> </span><span class="n">attr</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">hipKernelNodeAttrValue</span><span class="o">*</span><span class="w"> </span><span class="n">value</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Gets a node attribute</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipGraphKernelNodeGetAttribute</span><span class="p">(</span><span class="n">hipGraphNode_t</span><span class="w"> </span><span class="n">hNode</span><span class="p">,</span><span class="w"> </span><span class="n">hipKernelNodeAttrID</span><span class="w"> </span><span class="n">attr</span><span class="p">,</span><span class="w"> </span><span class="n">hipKernelNodeAttrValue</span><span class="o">*</span><span class="w"> </span><span class="n">value</span><span class="p">);</span>
</pre></div>
</div>
</li>
</ul>
</section>
<section id="support-for-virtual-memory-management-apis">
<h6>Support for virtual memory management APIs<a class="headerlink" href="#support-for-virtual-memory-management-apis" title="Link to this heading">#</a></h6>
<p>The new APIs for virtual memory management are as follows:</p>
<ul>
<li><p>Frees an address range reservation made via hipMemAddressReserve</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemAddressFree</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">devPtr</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Reserves an address range</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemAddressReserve</span><span class="p">(</span><span class="kt">void</span><span class="o">**</span><span class="w"> </span><span class="n">ptr</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">alignment</span><span class="p">,</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">addr</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">flags</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Creates a memory allocation described by the properties and size</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemCreate</span><span class="p">(</span><span class="n">hipMemGenericAllocationHandle_t</span><span class="o">*</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">hipMemAllocationProp</span><span class="o">*</span><span class="w"> </span><span class="n">prop</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">flags</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Exports an allocation to a requested shareable handle type</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemExportToShareableHandle</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">shareableHandle</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemGenericAllocationHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemAllocationHandleType</span><span class="w"> </span><span class="n">handleType</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">flags</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Gets the access flags set for the given location and ptr</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemGetAccess</span><span class="p">(</span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="o">*</span><span class="w"> </span><span class="n">flags</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">hipMemLocation</span><span class="o">*</span><span class="w"> </span><span class="n">location</span><span class="p">,</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">ptr</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Calculates either the minimal or recommended granularity</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemGetAllocationGranularity</span><span class="p">(</span><span class="kt">size_t</span><span class="o">*</span><span class="w"> </span><span class="n">granularity</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">hipMemAllocationProp</span><span class="o">*</span><span class="w"> </span><span class="n">prop</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemAllocationGranularity_flags</span><span class="w"> </span><span class="n">option</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Retrieves the property structure of the given handle</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemGetAllocationPropertiesFromHandle</span><span class="p">(</span><span class="n">hipMemAllocationProp</span><span class="o">*</span><span class="w"> </span><span class="n">prop</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemGenericAllocationHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Imports an allocation from a requested shareable handle type</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemImportFromShareableHandle</span><span class="p">(</span><span class="n">hipMemGenericAllocationHandle_t</span><span class="o">*</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">osHandle</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemAllocationHandleType</span><span class="w"> </span><span class="n">shHandleType</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Maps an allocation handle to a reserved virtual address range</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemMap</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">ptr</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">offset</span><span class="p">,</span><span class="w"> </span><span class="n">hipMemGenericAllocationHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="kt">long</span><span class="w"> </span><span class="n">flags</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Maps or unmaps subregions of sparse HIP arrays and sparse HIP mipmapped arrays</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemMapArrayAsync</span><span class="p">(</span><span class="n">hipArrayMapInfo</span><span class="o">*</span><span class="w"> </span><span class="n">mapInfoList</span><span class="p">,</span><span class="w"> </span><span class="kt">unsigned</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">count</span><span class="p">,</span><span class="w"> </span><span class="n">hipStream_t</span><span class="w"> </span><span class="n">stream</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Release a memory handle representing a memory allocation, that  was previously allocated through hipMemCreate</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemRelease</span><span class="p">(</span><span class="n">hipMemGenericAllocationHandle_t</span><span class="w"> </span><span class="n">handle</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Returns the allocation handle of the backing memory allocation given the address</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemRetainAllocationHandle</span><span class="p">(</span><span class="n">hipMemGenericAllocationHandle_t</span><span class="o">*</span><span class="w"> </span><span class="n">handle</span><span class="p">,</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">addr</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Sets the access flags for each location specified in desc for the given virtual address range</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemSetAccess</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">ptr</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">,</span><span class="w"> </span><span class="k">const</span><span class="w"> </span><span class="n">hipMemAccessDesc</span><span class="o">*</span><span class="w"> </span><span class="n">desc</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">count</span><span class="p">);</span>
</pre></div>
</div>
</li>
<li><p>Unmaps memory allocation of a given address range</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">hipError_t</span><span class="w"> </span><span class="nf">hipMemUnmap</span><span class="p">(</span><span class="kt">void</span><span class="o">*</span><span class="w"> </span><span class="n">ptr</span><span class="p">,</span><span class="w"> </span><span class="kt">size_t</span><span class="w"> </span><span class="n">size</span><span class="p">);</span>
</pre></div>
</div>
</li>
</ul>
<p>For more information, refer to the HIP API documentation at
<span class="xref std std-doc">hip:doxygen/html/modules</span>.</p>
</section>
</section>
<section id="planned-hip-changes-in-future-releases">
<h5>Planned HIP changes in future releases<a class="headerlink" href="#planned-hip-changes-in-future-releases" title="Link to this heading">#</a></h5>
<p>Changes to <code class="docutils literal notranslate"><span class="pre">hipDeviceProp_t</span></code>, <code class="docutils literal notranslate"><span class="pre">HIPMEMCPY_3D</span></code>, and <code class="docutils literal notranslate"><span class="pre">hipArray</span></code> structures (and related HIP APIs) are
planned in the next major release. These changes may impact backward compatibility.</p>
<p>Refer to the release notes in subsequent releases for more information.</p>
</section>
</section>
<section id="rocm-math-and-communication-libraries">
<h4>ROCm math and communication libraries<a class="headerlink" href="#rocm-math-and-communication-libraries" title="Link to this heading">#</a></h4>
<p>In this release, ROCm math and communication libraries consist of the following enhancements and
fixes:</p>
<ul class="simple">
<li><p>New rocWMMA for matrix multiplication and accumulation operations acceleration</p></li>
</ul>
<p>This release introduces a new ROCm C++ library for accelerating mixed-precision matrix multiplication
and accumulation (MFMA) operations leveraging specialized GPU matrix cores. rocWMMA provides a
C++ API to facilitate breaking down matrix multiply accumulate problems into fragments and using
them in block-wise operations that are distributed in parallel across GPU wavefronts. The API is a
header library of GPU device code, meaning matrix core acceleration may be compiled directly into
your kernel device code. This can benefit from compiler optimization in the generation of kernel
assembly and does not incur additional overhead costs of linking to external runtime libraries or having
to launch separate kernels.</p>
<p>rocWMMA is released as a header library and includes test and sample projects to validate and
illustrate example usages of the C++ API. GEMM matrix multiplication is used as primary validation
given the heavy precedent for the library. However, the usage portfolio is growing significantly and
demonstrates different ways rocWMMA may be consumed.</p>
<p>For more information, refer to <a class="reference internal" href="../reference/library-index.html"><span class="std std-doc">Communication Libraries</span></a></p>
</section>
<section id="openmp-enhancements-in-this-release">
<h4>OpenMP enhancements in this release<a class="headerlink" href="#openmp-enhancements-in-this-release" title="Link to this heading">#</a></h4>
<section id="ompt-target-support">
<h5>OMPT target support<a class="headerlink" href="#ompt-target-support" title="Link to this heading">#</a></h5>
<p>The OpenMP runtime in ROCm implements a subset of the OMPT device APIs, as described in the
OpenMP specification document. These are APIs that allow first-party tools to examine the profile
and traces for kernels that execute on a device. A tool may register callbacks for data transfer and
kernel dispatch entry points. A tool may use APIs to start and stop tracing for device-related activities,
such as data transfer and kernel dispatch timings and associated metadata. If device tracing is enabled,
trace records for device activities are collected during program execution and returned to the tool
using the APIs described in the specification.</p>
<p>Following is an example demonstrating how a tool would use the OMPT target APIs supported. The
README in /opt/rocm/llvm/examples/tools/ompt outlines the steps to follow, and you can run the
provided example as indicated below:</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span><span class="nb">cd</span><span class="w"> </span>/opt/rocm/llvm/examples/tools/ompt/veccopy-ompt-target-tracing
make<span class="w"> </span>run
</pre></div>
</div>
<p>The file <code class="docutils literal notranslate"><span class="pre">veccopy-ompt-target-tracing.c</span></code> simulates how a tool would initiate device activity tracing. The
file <code class="docutils literal notranslate"><span class="pre">callbacks.h</span></code> shows the callbacks that may be registered and implemented by the tool.</p>
</section>
</section>
</section>
<section id="id415">
<h3>Deprecations and warnings<a class="headerlink" href="#id415" title="Link to this heading">#</a></h3>
<section id="id416">
<h4>Linux file system hierarchy standard for ROCm<a class="headerlink" href="#id416" title="Link to this heading">#</a></h4>
<p>ROCm packages have adopted the Linux foundation file system hierarchy standard in this release to
ensure ROCm components follow open source conventions for Linux-based distributions. While
moving to a new file system hierarchy, ROCm ensures backward compatibility with its 5.1 version or
older file system hierarchy. See below for a detailed explanation of the new file system hierarchy and
backward compatibility.</p>
<section id="id417">
<h5>New file system hierarchy<a class="headerlink" href="#id417" title="Link to this heading">#</a></h5>
<p>The following is the new file system hierarchy:</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>/opt/rocm-&lt;ver&gt;
    | --bin
      | --All externally exposed Binaries
    | --libexec
        | --&lt;component&gt;
            | -- Component specific private non-ISA executables (architecture independent)
    | --include
        | -- &lt;component&gt;
            | --&lt;header files&gt;
    | --lib
        | --lib&lt;soname&gt;.so -&gt; lib&lt;soname&gt;.so.major -&gt; lib&lt;soname&gt;.so.major.minor.patch
            (public libraries linked with application)
        | --&lt;component&gt; (component specific private library, executable data)
        | --&lt;cmake&gt;
            | --components
                | --&lt;component&gt;.config.cmake
    | --share
        | --html/&lt;component&gt;/*.html
        | --info/&lt;component&gt;/*.[pdf, md, txt]
        | --man
        | --doc
            | --&lt;component&gt;
                | --&lt;licenses&gt;
        | --&lt;component&gt;
            | --&lt;misc files&gt; (arch independent non-executable)
            | --samples
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>ROCm will not support backward compatibility with the v5.1(old) file system hierarchy in its next major
release.</p>
</div>
<p>For more information, refer to <a class="reference external" href="https://refspecs.linuxfoundation.org/fhs.shtml">https://refspecs.linuxfoundation.org/fhs.shtml</a>.</p>
</section>
<section id="id418">
<h5>Backward compatibility with older file systems<a class="headerlink" href="#id418" title="Link to this heading">#</a></h5>
<p>ROCm has moved header files and libraries to its new location as indicated in the above structure and
included symbolic-link and wrapper header files in its old location for backward compatibility.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>ROCm will continue supporting backward compatibility until the next major release.</p>
</div>
</section>
<section id="id419">
<h5>Wrapper header files<a class="headerlink" href="#id419" title="Link to this heading">#</a></h5>
<p>Wrapper header files are placed in the old location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/include</span></code>) with a
warning message to include files from the new location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/include</span></code>) as shown in the
example below:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="c1">// Code snippet from hip_runtime.h</span>
<span class="cp">#pragma message “This file is deprecated. Use file from include path /opt/rocm-ver/include/ and prefix with hip”.</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">"hip/hip_runtime.h"</span>
</pre></div>
</div>
<p>The wrapper header files’ backward compatibility deprecation is as follows:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">#pragma</span></code> message announcing deprecation – ROCm v5.2 release</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">#pragma</span></code> message changed to <code class="docutils literal notranslate"><span class="pre">#warning</span></code> – Future release</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">#warning</span></code> changed to <code class="docutils literal notranslate"><span class="pre">#error</span></code> – Future release</p></li>
<li><p>Backward compatibility wrappers removed – Future release</p></li>
</ul>
</section>
<section id="id420">
<h5>Library files<a class="headerlink" href="#id420" title="Link to this heading">#</a></h5>
<p>Library files are available in the <code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/lib</span></code> folder. For backward compatibility, the old library
location (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/lib</span></code>) has a soft link to the library at the new location.</p>
<p>Example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>ls<span class="w"> </span>-l<span class="w"> </span>/opt/rocm/hip/lib/
total<span class="w"> </span><span class="m">4</span>
drwxr-xr-x<span class="w"> </span><span class="m">4</span><span class="w"> </span>root<span class="w"> </span>root<span class="w"> </span><span class="m">4096</span><span class="w"> </span>May<span class="w"> </span><span class="m">12</span><span class="w"> </span><span class="m">10</span>:45<span class="w"> </span>cmake
lrwxrwxrwx<span class="w"> </span><span class="m">1</span><span class="w"> </span>root<span class="w"> </span>root<span class="w">   </span><span class="m">24</span><span class="w"> </span>May<span class="w"> </span><span class="m">10</span><span class="w"> </span><span class="m">23</span>:32<span class="w"> </span>libamdhip64.so<span class="w"> </span>-&gt;<span class="w"> </span>../../lib/libamdhip64.so
</pre></div>
</div>
</section>
<section id="id421">
<h5>CMake config files<a class="headerlink" href="#id421" title="Link to this heading">#</a></h5>
<p>All CMake configuration files are available in the <code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/lib/cmake/&lt;component&gt;</span></code> folder. For
backward compatibility, the old CMake locations (<code class="docutils literal notranslate"><span class="pre">/opt/rocm-xxx/&lt;component&gt;/lib/cmake</span></code>) consist of
a soft link to the new CMake config.</p>
<p>Example:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>$<span class="w"> </span>ls<span class="w"> </span>-l<span class="w"> </span>/opt/rocm/hip/lib/cmake/hip/
total<span class="w"> </span><span class="m">0</span>
lrwxrwxrwx<span class="w"> </span><span class="m">1</span><span class="w"> </span>root<span class="w"> </span>root<span class="w"> </span><span class="m">42</span><span class="w"> </span>May<span class="w"> </span><span class="m">10</span><span class="w"> </span><span class="m">23</span>:32<span class="w"> </span>hip-config.cmake<span class="w"> </span>-&gt;<span class="w"> </span>../../../../lib/cmake/hip/hip-config.cmake
</pre></div>
</div>
</section>
</section>
<section id="planned-deprecation-of-hip-rocclr-and-hip-base-packages">
<h4>Planned deprecation of hip-rocclr and hip-base packages<a class="headerlink" href="#planned-deprecation-of-hip-rocclr-and-hip-base-packages" title="Link to this heading">#</a></h4>
<p>In the ROCm v5.2 release, hip-rocclr and hip-base packages (Debian and RPM) are planned for
deprecation and will be removed in a future release. hip-runtime-amd and hip-dev(el) will replace
these packages respectively. Users of hip-rocclr must install two packages, hip-runtime-amd and
hip-dev, to get the same set of packages installed by hip-rocclr previously.</p>
<p>Currently, both package names hip-rocclr (or) hip-runtime-amd and hip-base (or) hip-dev(el) are
supported.</p>
</section>
<section id="deprecation-of-integrated-hip-directed-tests">
<h4>Deprecation of integrated HIP directed tests<a class="headerlink" href="#deprecation-of-integrated-hip-directed-tests" title="Link to this heading">#</a></h4>
<p>The integrated HIP directed tests, which are currently built by default, are deprecated in this release.
The default building and execution support through CMake will be removed in future release.</p>
</section>
</section>
<section id="id422">
<h3>Defect fixes<a class="headerlink" href="#id422" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Defect</p></th>
<th class="head"><p>Fix</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ROCmInfo does not list gpus</p></td>
<td><p>code fix</p></td>
</tr>
<tr class="row-odd"><td><p>Hang observed while restoring cooperative group samples</p></td>
<td><p>code fix</p></td>
</tr>
<tr class="row-even"><td><p>ROCM-SMI over SRIOV: Unsupported commands do not return proper error message</p></td>
<td><p>code fix</p></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="id423">
<h3>Known issues<a class="headerlink" href="#id423" title="Link to this heading">#</a></h3>
<p>This section consists of known issues in this release.</p>
<section id="compiler-error-on-gfx1030-when-compiling-at-o0">
<h4>Compiler error on gfx1030 when compiling at -O0<a class="headerlink" href="#compiler-error-on-gfx1030-when-compiling-at-o0" title="Link to this heading">#</a></h4>
<section id="id424">
<h5>Issue<a class="headerlink" href="#id424" title="Link to this heading">#</a></h5>
<p>A compiler error occurs when using -O0 flag to compile code for gfx1030 that calls atomicAddNoRet,
which is defined in amd_hip_atomic.h. The compiler generates an illegal instruction for gfx1030.</p>
</section>
<section id="workaround">
<h5>Workaround<a class="headerlink" href="#workaround" title="Link to this heading">#</a></h5>
<p>The workaround is not to use the -O0 flag for this case. For higher optimization levels, the compiler
does not generate an invalid instruction.</p>
</section>
</section>
<section id="system-freeze-observed-during-cuda-memtest-checkpoint">
<h4>System freeze observed during CUDA memtest checkpoint<a class="headerlink" href="#system-freeze-observed-during-cuda-memtest-checkpoint" title="Link to this heading">#</a></h4>
<section id="id425">
<h5>Issue<a class="headerlink" href="#id425" title="Link to this heading">#</a></h5>
<p>Checkpoint/Restore in Userspace (CRIU) requires 20 MB of VRAM approximately to checkpoint and
restore. The CRIU process may freeze if the maximum amount of available VRAM is allocated to
checkpoint applications.</p>
</section>
<section id="id426">
<h5>Workaround<a class="headerlink" href="#id426" title="Link to this heading">#</a></h5>
<p>To use CRIU to checkpoint and restore your application, limit the amount of VRAM the application uses
to ensure at least 20 MB is available.</p>
</section>
</section>
<section id="hpc-test-fails-with-the-hsa-status-error-memory-fault-error">
<h4>HPC test fails with the “HSA_STATUS_ERROR_MEMORY_FAULT” error<a class="headerlink" href="#hpc-test-fails-with-the-hsa-status-error-memory-fault-error" title="Link to this heading">#</a></h4>
<section id="id427">
<h5>Issue<a class="headerlink" href="#id427" title="Link to this heading">#</a></h5>
<p>The compiler may incorrectly compile a program that uses the <code class="docutils literal notranslate"><span class="pre">__shfl_sync(mask,</span> <span class="pre">value,</span> <span class="pre">srcLane)</span></code>
function when the “value” parameter to the function is undefined along some path to the function. For
most functions, uninitialized inputs cause undefined behavior, but the definition for <code class="docutils literal notranslate"><span class="pre">__shfl_sync</span></code> should
allow for undefined values.</p>
</section>
<section id="id428">
<h5>Workaround<a class="headerlink" href="#id428" title="Link to this heading">#</a></h5>
<p>The workaround is to initialize the parameters to <code class="docutils literal notranslate"><span class="pre">__shfl_sync</span></code>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>When the <code class="docutils literal notranslate"><span class="pre">-Wall</span></code> compilation flag is used, the compiler generates a warning indicating the variable is
initialized along some path.</p>
</div>
<p>Example:</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">double</span><span class="w"> </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mf">0.0</span><span class="p">;</span><span class="w"> </span><span class="c1">// Initialize the input to __shfl_sync.</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">lane</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">&lt;</span><span class="n">some</span><span class="w"> </span><span class="n">expression</span><span class="o">&gt;</span>
<span class="p">}</span>
<span class="n">res</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">__shfl_sync</span><span class="p">(</span><span class="n">mask</span><span class="p">,</span><span class="w"> </span><span class="n">res</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span>
</pre></div>
</div>
</section>
</section>
<section id="kernel-produces-incorrect-result">
<h4>Kernel produces incorrect result<a class="headerlink" href="#kernel-produces-incorrect-result" title="Link to this heading">#</a></h4>
<section id="id429">
<h5>Issue<a class="headerlink" href="#id429" title="Link to this heading">#</a></h5>
<p>In recent changes to Clang, insertion of the noundef attribute to all the function arguments has been
enabled by default.</p>
<p>In the HIP kernel, variable var in shfl_sync may not be initialized, so LLVM IR treats it as undef.</p>
<p>So, the function argument that is potentially undef (because it is not initialized) has always been
assumed to be noundef by LLVM IR (since Clang has inserted the noundef attribute). This leads to
ambiguous kernel execution.</p>
</section>
<section id="id430">
<h5>Workaround<a class="headerlink" href="#id430" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Skip adding <code class="docutils literal notranslate"><span class="pre">noundef</span></code> attribute to functions tagged with convergent  attribute. Refer to
<a class="reference external" href="https://reviews.llvm.org/D124158">https://reviews.llvm.org/D124158</a> for more information.</p></li>
<li><p>Introduce shuffle attribute and add it to <code class="docutils literal notranslate"><span class="pre">__shfl</span></code> like APIs at hip headers. Clang can skip adding the
<code class="docutils literal notranslate"><span class="pre">noundef</span></code> attribute, if it finds that argument is tagged with shuffle attribute. Refer to
<a class="reference external" href="https://reviews.llvm.org/D125378">https://reviews.llvm.org/D125378</a> for more information.</p></li>
<li><p>Introduce clang builtin for <code class="docutils literal notranslate"><span class="pre">__shfl</span></code> to identify it and skip adding <code class="docutils literal notranslate"><span class="pre">noundef</span></code> attribute.</p></li>
<li><p>Introduce <code class="docutils literal notranslate"><span class="pre">__builtin_freeze</span></code> to use on the relevant arguments in library wrappers. The library/header
need to insert freezes on the relevant inputs.</p></li>
</ul>
</section>
</section>
<section id="issue-with-applications-triggering-oversubscription">
<h4>Issue with applications triggering oversubscription<a class="headerlink" href="#issue-with-applications-triggering-oversubscription" title="Link to this heading">#</a></h4>
<p>There is a known issue with applications that trigger oversubscription. A hardware hang occurs when
ROCgdb is used on AMD Instinct™ MI50 and MI100 systems.</p>
<p>This issue is under investigation and will be fixed in a future release.</p>
</section>
</section>
<section id="library-changes-in-rocm-5-2-0">
<h3>Library changes in ROCM 5.2.0<a class="headerlink" href="#library-changes-in-rocm-5-2-0" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p>0.50.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.2.0">0.51.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p>2.11.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.2.0">2.11.1</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p>1.0.7 ⇒ <a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.2.0">1.0.8</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p>1.3.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.2.0">1.4.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p>2.1.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.2.0">2.2.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.2.0">2.11.4</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p>2.0.2 ⇒ <a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.2.0">2.0.3</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p>2.43.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.2.0">2.44.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p>1.0.16 ⇒ <a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.2.0">1.0.17</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocPRIM</p></td>
<td><p>2.10.13 ⇒ <a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.2.0">2.10.14</a></p></td>
</tr>
<tr class="row-even"><td><p>rocRAND</p></td>
<td><p>2.10.13 ⇒ <a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.2.0">2.10.14</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSOLVER</p></td>
<td><p>3.17.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.2.0">3.18.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSPARSE</p></td>
<td><p>2.1.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.2.0">2.2.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocThrust</p></td>
<td><p>2.14.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.2.0">2.15.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocWMMA</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-5.2.0">0.7</a></p></td>
</tr>
<tr class="row-odd"><td><p>Tensile</p></td>
<td><p>4.32.0 ⇒ <a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.2.0">4.33.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="hipblas-0-51-0">
<h4>hipBLAS 0.51.0<a class="headerlink" href="#hipblas-0-51-0" title="Link to this heading">#</a></h4>
<p>hipBLAS 0.51.0 for ROCm 5.2.0</p>
<section id="id431">
<h5>Added<a class="headerlink" href="#id431" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Packages for test and benchmark executables on all supported OSes using CPack.</p></li>
<li><p>Added File/Folder Reorg Changes with backward compatibility support enabled using ROCM-CMAKE wrapper functions</p></li>
<li><p>Added user-specified initialization option to hipblas-bench</p></li>
</ul>
</section>
<section id="id432">
<h5>Fixed<a class="headerlink" href="#id432" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed version gathering in performance measuring script</p></li>
</ul>
</section>
</section>
<section id="hipcub-2-11-1">
<h4>hipCUB 2.11.1<a class="headerlink" href="#hipcub-2-11-1" title="Link to this heading">#</a></h4>
<p>hipCUB 2.11.1 for ROCm 5.2.0</p>
<section id="id433">
<h5>Added<a class="headerlink" href="#id433" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Packages for tests and benchmark executable on all supported OSes using CPack.</p></li>
</ul>
</section>
</section>
<section id="hipfft-1-0-8">
<h4>hipFFT 1.0.8<a class="headerlink" href="#hipfft-1-0-8" title="Link to this heading">#</a></h4>
<p>hipFFT 1.0.8 for ROCm 5.2.0</p>
<section id="id434">
<h5>Added<a class="headerlink" href="#id434" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added File/Folder Reorg Changes with backward compatibility support using ROCM-CMAKE wrapper functions.</p></li>
<li><p>Packages for test and benchmark executables on all supported OSes using CPack.</p></li>
</ul>
</section>
</section>
<section id="hipsolver-1-4-0">
<h4>hipSOLVER 1.4.0<a class="headerlink" href="#hipsolver-1-4-0" title="Link to this heading">#</a></h4>
<p>hipSOLVER 1.4.0 for ROCm 5.2.0</p>
<section id="id435">
<h5>Added<a class="headerlink" href="#id435" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Package generation for test and benchmark executables on all supported OSes using CPack.</p></li>
<li><p>File/Folder Reorg</p>
<ul>
<li><p>Added File/Folder Reorg Changes with backward compatibility support using ROCM-CMAKE wrapper functions.</p></li>
</ul>
</li>
</ul>
</section>
<section id="id436">
<h5>Fixed<a class="headerlink" href="#id436" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed the ReadTheDocs documentation generation.</p></li>
</ul>
</section>
</section>
<section id="hipsparse-2-2-0">
<h4>hipSPARSE 2.2.0<a class="headerlink" href="#hipsparse-2-2-0" title="Link to this heading">#</a></h4>
<p>hipSPARSE 2.2.0 for ROCm 5.2.0</p>
<section id="id437">
<h5>Added<a class="headerlink" href="#id437" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Packages for test and benchmark executables on all supported OSes using CPack.</p></li>
</ul>
</section>
</section>
<section id="rocalution-2-0-3">
<h4>rocALUTION 2.0.3<a class="headerlink" href="#rocalution-2-0-3" title="Link to this heading">#</a></h4>
<p>rocALUTION 2.0.3 for ROCm 5.2.0</p>
<section id="id438">
<h5>Added<a class="headerlink" href="#id438" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Packages for test and benchmark executables on all supported OSes using CPack.</p></li>
</ul>
</section>
</section>
<section id="rocblas-2-44-0">
<h4>rocBLAS 2.44.0<a class="headerlink" href="#rocblas-2-44-0" title="Link to this heading">#</a></h4>
<p>rocBLAS 2.44.0 for ROCm 5.2.0</p>
<section id="id439">
<h5>Added<a class="headerlink" href="#id439" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Packages for test and benchmark executables on all supported OSes using CPack.</p></li>
<li><p>Added Denormal number detection to the Numerical checking helper function to detect denormal/subnormal numbers in the input and the output vectors of rocBLAS level 1 and 2 functions.</p></li>
<li><p>Added Denormal number detection to the Numerical checking helper function to detect denormal/subnormal numbers in the input and the output general matrices of rocBLAS level 2 and 3 functions.</p></li>
<li><p>Added NaN initialization tests to the yaml files of Level 2 rocBLAS batched and strided-batched functions for testing purposes.</p></li>
<li><p>Added memory allocation check to avoid disk swapping during rocblas-test runs by skipping tests.</p></li>
</ul>
</section>
<section id="id440">
<h5>Optimizations<a class="headerlink" href="#id440" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved performance of non-batched and batched her2 for all sizes and data types.</p></li>
<li><p>Improved performance of non-batched and batched amin for all data types using shuffle reductions.</p></li>
<li><p>Improved performance of non-batched and batched amax for all data types using shuffle reductions.</p></li>
<li><p>Improved performance of trsv for all sizes and data types.</p></li>
</ul>
</section>
<section id="id441">
<h5>Changed<a class="headerlink" href="#id441" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Modifying gemm_ex for HBH (High-precision F16). The alpha/beta data type remains as F32 without narrowing to F16 and expanding back to F32 in the kernel. This change prevents rounding errors due to alpha/beta conversion in situations where alpha/beta are not exactly represented as an F16.</p></li>
<li><p>Modified non-batched and batched asum, nrm2 functions to use shuffle instruction based reductions.</p></li>
<li><p>For gemm, gemm_ex, gemm_ex2 internal API use rocblas_stride datatype for offset.</p></li>
<li><p>For symm, hemm, syrk, herk, dgmm, geam internal API use rocblas_stride datatype for offset.</p></li>
<li><p>AMD copyright year for all rocBLAS files.</p></li>
<li><p>For gemv (transpose-case), typecasted the ‘lda’(offset) datatype to size_t during offset calculation to avoid overflow and remove duplicate template functions.</p></li>
</ul>
</section>
<section id="id442">
<h5>Fixed<a class="headerlink" href="#id442" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>For function her2 avoid overflow in offset calculation.</p></li>
<li><p>For trsm when alpha == 0 and on host, allow A to be nullptr.</p></li>
<li><p>Fixed memory access issue in trsv.</p></li>
<li><p>Fixed git pre-commit script to update only AMD copyright year.</p></li>
<li><p>Fixed dgmm, geam test functions to set correct stride values.</p></li>
<li><p>For functions ssyr2k and dsyr2k allow trans == rocblas_operation_conjugate_transpose.</p></li>
<li><p>Fixed compilation error for clients-only build.</p></li>
</ul>
</section>
<section id="id443">
<h5>Removed<a class="headerlink" href="#id443" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Remove Navi12 (gfx1011) from fat binary.</p></li>
</ul>
</section>
</section>
<section id="rocfft-1-0-17">
<h4>rocFFT 1.0.17<a class="headerlink" href="#rocfft-1-0-17" title="Link to this heading">#</a></h4>
<p>rocFFT 1.0.17 for ROCm 5.2.0</p>
<section id="id444">
<h5>Added<a class="headerlink" href="#id444" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Packages for test and benchmark executables on all supported OSes using CPack.</p></li>
<li><p>Added File/Folder Reorg Changes with backward compatibility support using ROCM-CMAKE wrapper functions.</p></li>
</ul>
</section>
<section id="id445">
<h5>Changed<a class="headerlink" href="#id445" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved reuse of twiddle memory between plans.</p></li>
<li><p>Set a default load/store callback when only one callback
type is set via the API for improved performance.</p></li>
</ul>
</section>
<section id="id446">
<h5>Optimizations<a class="headerlink" href="#id446" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Introduced a new access pattern of lds (non-linear) and applied it on
sbcc kernels len 64 to get performance improvement.</p></li>
</ul>
</section>
<section id="id447">
<h5>Fixed<a class="headerlink" href="#id447" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed plan creation failure in cases where SBCC kernels would need to write to non-unit-stride buffers.</p></li>
</ul>
</section>
</section>
<section id="rocprim-2-10-14">
<h4>rocPRIM 2.10.14<a class="headerlink" href="#rocprim-2-10-14" title="Link to this heading">#</a></h4>
<p>rocPRIM 2.10.14 for ROCm 5.2.0</p>
<section id="id448">
<h5>Added<a class="headerlink" href="#id448" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Packages for tests and benchmark executable on all supported OSes using CPack.</p></li>
<li><p>Added File/Folder Reorg Changes and Enabled Backward compatibility support using wrapper headers.</p></li>
</ul>
</section>
</section>
<section id="rocrand-2-10-14">
<h4>rocRAND 2.10.14<a class="headerlink" href="#rocrand-2-10-14" title="Link to this heading">#</a></h4>
<p>rocRAND 2.10.14 for ROCm 5.2.0</p>
<section id="id449">
<h5>Added<a class="headerlink" href="#id449" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Backward compatibility for deprecated <code class="docutils literal notranslate"><span class="pre">#include</span> <span class="pre">&amp;lt;rocrand.h&amp;gt;</span></code> using wrapper header files.</p></li>
<li><p>Packages for test and benchmark executables on all supported OSes using CPack.</p></li>
</ul>
</section>
</section>
<section id="rocsolver-3-18-0">
<h4>rocSOLVER 3.18.0<a class="headerlink" href="#rocsolver-3-18-0" title="Link to this heading">#</a></h4>
<p>rocSOLVER 3.18.0 for ROCm 5.2.0</p>
<section id="id450">
<h5>Added<a class="headerlink" href="#id450" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Partial eigenvalue decomposition routines:</p>
<ul>
<li><p>STEBZ</p></li>
<li><p>STEIN</p></li>
</ul>
</li>
<li><p>Package generation for test and benchmark executables on all supported OSes using CPack.</p></li>
<li><p>Added tests for multi-level logging</p></li>
<li><p>Added tests for rocsolver-bench client</p></li>
<li><p>File/Folder Reorg</p>
<ul>
<li><p>Added File/Folder Reorg Changes with backward compatibility support using ROCM-CMAKE wrapper functions.</p></li>
</ul>
</li>
</ul>
</section>
<section id="id451">
<h5>Fixed<a class="headerlink" href="#id451" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed compatibility with libfmt 8.1</p></li>
</ul>
</section>
</section>
<section id="rocsparse-2-2-0">
<h4>rocSPARSE 2.2.0<a class="headerlink" href="#rocsparse-2-2-0" title="Link to this heading">#</a></h4>
<p>rocSPARSE 2.2.0 for ROCm 5.2.0</p>
<section id="id452">
<h5>Added<a class="headerlink" href="#id452" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>batched SpMM for CSR, COO and Blocked ELL formats.</p></li>
<li><p>Packages for test and benchmark executables on all supported OSes using CPack.</p></li>
<li><p>Clients file importers and exporters.</p></li>
</ul>
</section>
<section id="id453">
<h5>Improved<a class="headerlink" href="#id453" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Clients code size reduction.</p></li>
<li><p>Clients error handling.</p></li>
<li><p>Clients benchmarking for performance tracking.</p></li>
</ul>
</section>
<section id="id454">
<h5>Changed<a class="headerlink" href="#id454" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Test adjustments due to roundoff errors.</p></li>
<li><p>Fixing API calls compatiblity with rocPRIM.</p></li>
</ul>
</section>
<section id="id455">
<h5>Known Issues<a class="headerlink" href="#id455" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>none</p></li>
</ul>
</section>
</section>
<section id="rocthrust-2-15-0">
<h4>rocThrust 2.15.0<a class="headerlink" href="#rocthrust-2-15-0" title="Link to this heading">#</a></h4>
<p>rocThrust 2.15.0 for ROCm 5.2.0</p>
<section id="id456">
<h5>Added<a class="headerlink" href="#id456" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Packages for tests and benchmark executable on all supported OSes using CPack.</p></li>
</ul>
</section>
</section>
<section id="rocwmma-0-7">
<h4>rocWMMA 0.7<a class="headerlink" href="#rocwmma-0-7" title="Link to this heading">#</a></h4>
<p>rocWMMA 0.7 for ROCm 5.2.0</p>
<section id="id457">
<h5>Added<a class="headerlink" href="#id457" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added unit tests for DLRM kernels</p></li>
<li><p>Added GEMM sample</p></li>
<li><p>Added DLRM sample</p></li>
<li><p>Added SGEMV sample</p></li>
<li><p>Added unit tests for cooperative wmma load and stores</p></li>
<li><p>Added unit tests for IOBarrier.h</p></li>
<li><p>Added wmma load/ store  tests for different matrix types (A, B and Accumulator)</p></li>
<li><p>Added more block sizes 1, 2, 4, 8 to test MmaSyncMultiTest</p></li>
<li><p>Added block sizes 4, 8 to test MmaSynMultiLdsTest</p></li>
<li><p>Added support for wmma load / store layouts with block dimension greater than 64</p></li>
<li><p>Added IOShape structure to define the attributes of mapping and layouts for all wmma matrix types</p></li>
<li><p>Added CI testing for rocWMMA</p></li>
</ul>
</section>
<section id="id458">
<h5>Changed<a class="headerlink" href="#id458" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Renamed wmma to rocwmma in cmake, header files and documentation</p></li>
<li><p>Renamed library files</p></li>
<li><p>Modified Layout.h to use different matrix offset calculations (base offset, incremental offset and cumulative offset)</p></li>
<li><p>Opaque load/store continue to use incrementatl offsets as they fill the entire block</p></li>
<li><p>Cooperative load/store use cumulative offsets as they fill only small portions for the entire block</p></li>
<li><p>Increased Max split counts to 64 for cooperative load/store</p></li>
<li><p>Moved all the wmma definitions, API headers to rocwmma namespace</p></li>
<li><p>Modified wmma fill unit tests to validate all matrix types (A, B, Accumulator)</p></li>
</ul>
</section>
</section>
<section id="tensile-4-33-0">
<h4>Tensile 4.33.0<a class="headerlink" href="#tensile-4-33-0" title="Link to this heading">#</a></h4>
<p>Tensile 4.33.0 for ROCm 5.2.0</p>
<section id="id459">
<h5>Added<a class="headerlink" href="#id459" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>TensileUpdateLibrary for updating old library logic files</p></li>
<li><p>Support for TensileRetuneLibrary to use sizes from separate file</p></li>
<li><p>ZGEMM DirectToVgpr/DirectToLds/StoreCInUnroll/MIArchVgpr support</p></li>
<li><p>Tests for denorm correctness</p></li>
<li><p>Option to write different architectures to different TensileLibrary files</p></li>
</ul>
</section>
<section id="id460">
<h5>Optimizations<a class="headerlink" href="#id460" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimize MessagePackLoadLibraryFile by switching to fread</p></li>
<li><p>DGEMM tail loop optimization for PrefetchAcrossPersistentMode=1/DirectToVgpr</p></li>
</ul>
</section>
<section id="id461">
<h5>Changed<a class="headerlink" href="#id461" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Alpha/beta datatype remains as F32 for HPA HGEMM</p></li>
<li><p>Force assembly kernels to not flush denorms</p></li>
<li><p>Use hipDeviceAttributePhysicalMultiProcessorCount as multiProcessorCount</p></li>
</ul>
</section>
<section id="id462">
<h5>Fixed<a class="headerlink" href="#id462" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fix segmentation fault when run i8 datatype with TENSILE_DB=0x80</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-1-3">
<h2>ROCm 5.1.3<a class="headerlink" href="#rocm-5-1-3" title="Link to this heading">#</a></h2>
<section id="library-changes-in-rocm-5-1-3">
<h3>Library changes in ROCM 5.1.3<a class="headerlink" href="#library-changes-in-rocm-5-1-3" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.1.3">0.50.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.1.3">2.11.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.1.3">1.0.7</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipRAND/releases/tag/rocm-5.1.3">2.10.13</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.1.3">1.3.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.1.3">2.1.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.1.3">2.11.4</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.1.3">2.0.2</a></p></td>
</tr>
<tr class="row-even"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.1.3">2.43.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.1.3">1.0.16</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.1.3">2.10.13</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.1.3">2.10.13</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.1.3">3.17.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.1.3">2.1.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.1.3">2.14.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.1.3">4.32.0</a></p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-1-1">
<h2>ROCm 5.1.1<a class="headerlink" href="#rocm-5-1-1" title="Link to this heading">#</a></h2>
<section id="library-changes-in-rocm-5-1-1">
<h3>Library changes in ROCM 5.1.1<a class="headerlink" href="#library-changes-in-rocm-5-1-1" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.1.1">0.50.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.1.1">2.11.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.1.1">1.0.7</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipRAND/releases/tag/rocm-5.1.1">2.10.13</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.1.1">1.3.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.1.1">2.1.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.1.1">2.11.4</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.1.1">2.0.2</a></p></td>
</tr>
<tr class="row-even"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.1.1">2.43.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.1.1">1.0.16</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.1.1">2.10.13</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.1.1">2.10.13</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.1.1">3.17.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.1.1">2.1.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.1.1">2.14.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.1.1">4.32.0</a></p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-1-0">
<h2>ROCm 5.1.0<a class="headerlink" href="#rocm-5-1-0" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable no-blanks-blockquote -->
<section id="id463">
<h3>What’s new in this release<a class="headerlink" href="#id463" title="Link to this heading">#</a></h3>
<section id="id464">
<h4>HIP enhancements<a class="headerlink" href="#id464" title="Link to this heading">#</a></h4>
<p>The ROCm v5.1 release consists of the following HIP enhancements.</p>
<section id="id465">
<h5>HIP installation guide updates<a class="headerlink" href="#id465" title="Link to this heading">#</a></h5>
<p>The HIP installation guide now includes information on installing and building HIP from source on
AMD and NVIDIA platforms.</p>
<p>Refer to the HIP Installation Guide v5.1 for more details.</p>
</section>
<section id="support-for-hip-graph">
<h5>Support for HIP graph<a class="headerlink" href="#support-for-hip-graph" title="Link to this heading">#</a></h5>
<p>ROCm v5.1 extends support for HIP Graph.</p>
</section>
<section id="planned-changes-for-hip-in-future-releases">
<h5>Planned changes for HIP in future releases<a class="headerlink" href="#planned-changes-for-hip-in-future-releases" title="Link to this heading">#</a></h5>
<section id="separation-of-hiprtc-libhiprtc-library-from-hip-runtime-amdhip64">
<h6>Separation of hiprtc (libhiprtc) library from hip runtime (amdhip64)<a class="headerlink" href="#separation-of-hiprtc-libhiprtc-library-from-hip-runtime-amdhip64" title="Link to this heading">#</a></h6>
<p>On ROCm/Linux, to maintain backward compatibility, the hipruntime library (amdhip64) will continue
to include hiprtc symbols in future releases. The backward compatible support may be discontinued by
removing hiprtc symbols from the hipruntime library (amdhip64) in the next major release.</p>
</section>
<section id="hipdeviceprop-t-structure-enhancements">
<h6>hipDeviceProp_t structure enhancements<a class="headerlink" href="#hipdeviceprop-t-structure-enhancements" title="Link to this heading">#</a></h6>
<p>Changes to the hipDeviceProp_t structure in the next major release may result in backward
incompatibility. More details on these changes will be provided in subsequent releases.</p>
</section>
</section>
</section>
<section id="rocdebugger-enhancements">
<h4>ROCDebugger enhancements<a class="headerlink" href="#rocdebugger-enhancements" title="Link to this heading">#</a></h4>
<section id="multi-language-source-level-debugger">
<h5>Multi-language source-level debugger<a class="headerlink" href="#multi-language-source-level-debugger" title="Link to this heading">#</a></h5>
<p>The compiler now generates a source-level variable and function argument debug information.</p>
<p>The accuracy is guaranteed if the compiler options <code class="docutils literal notranslate"><span class="pre">-g</span> <span class="pre">-O0</span></code> are used and apply only to HIP.</p>
<p>This enhancement enables ROCDebugger users to interact with the HIP source-level variables and
function arguments.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The newly-suggested compiler -g option must be used instead of the previously-suggested <code class="docutils literal notranslate"><span class="pre">-ggdb</span></code>
option. Although the effect of these two options is currently equivalent, this is not guaranteed for the
future, as changes might be made by the upstream LLVM community.</p>
</div>
</section>
<section id="machine-interface-lanes-support">
<h5>Machine interface lanes support<a class="headerlink" href="#machine-interface-lanes-support" title="Link to this heading">#</a></h5>
<p>ROCDebugger Machine Interface (MI) extends support to lanes, which includes the following
enhancements:</p>
<ul>
<li><p>Added a new -lane-info command, listing the current thread’s lanes.</p></li>
<li><p>The -thread-select command now supports a lane switch to switch to a specific lane of a thread:</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>-thread-select<span class="w"> </span>-l<span class="w"> </span>LANE<span class="w"> </span>THREAD
</pre></div>
</div>
</li>
<li><p>The =thread-selected notification gained a lane-id attribute. This enables the frontend to know which
lane of the thread was selected.</p></li>
<li><p>The *stopped asynchronous record gained lane-id and hit-lanes attributes.  The former indicates
which lane is selected, and the latter indicates which lanes explain the stop.</p></li>
<li><p>MI commands now accept a global –lane option, similar to the global –thread and –frame options.</p></li>
<li><p>MI varobjs are now lane-aware.</p></li>
</ul>
<p>For more information, refer to the ROC Debugger User Guide at <a class="reference external" href="https://rocm.docs.amd.com/projects/ROCgdb/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">ROCgdb</span></a>.</p>
</section>
<section id="enhanced-clone-inferior-command">
<h5>Enhanced - clone-inferior command<a class="headerlink" href="#enhanced-clone-inferior-command" title="Link to this heading">#</a></h5>
<p>The clone-inferior command now ensures that the TTY, CMD, ARGS, and AMDGPU PRECISE-MEMORY
settings are copied from the original inferior to the new one.  All modifications to the environment
variables done using the ‘set environment’ or ‘unset environment’ commands are also copied to the
new inferior.</p>
</section>
</section>
<section id="miopen-support-for-rdna-gpus">
<h4>MIOpen support for RDNA GPUs<a class="headerlink" href="#miopen-support-for-rdna-gpus" title="Link to this heading">#</a></h4>
<p>This release includes support for AMD Radeon™ Pro W6800, in addition to other bug fixes and
performance improvements as listed below:</p>
<ul class="simple">
<li><p>MIOpen now supports RDNA GPUs!! (via MIOpen PRs 973, 780, 764, 740, 739, 677, 660, 653, 493, 498)</p></li>
<li><p>Fixed a correctness issue with ImplicitGemm algorithm</p></li>
<li><p>Updated the performance data for new kernel versions</p></li>
<li><p>Improved MIOpen build time by splitting large kernel header files</p></li>
<li><p>Fixed an issue in reduction kernels for padded tensors</p></li>
<li><p>Various other bug fixes and performance improvements</p></li>
</ul>
<p>For more information, see <a class="reference external" href="https://rocm.docs.amd.com/projects/MIOpen/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">Documentation</span></a>.</p>
</section>
<section id="checkpoint-restore-support-with-criu">
<h4>Checkpoint restore support with CRIU<a class="headerlink" href="#checkpoint-restore-support-with-criu" title="Link to this heading">#</a></h4>
<p>The new Checkpoint Restore in Userspace (CRIU) functionality is implemented to support AMD GPU
and ROCm applications.</p>
<p>CRIU is a userspace tool to Checkpoint and Restore an application.</p>
<p>CRIU lacked the support for checkpoint restore applications that used device files such as a GPU. With
this ROCm release, CRIU is enhanced with a new plugin to support AMD GPUs, which includes:</p>
<ul class="simple">
<li><p>Single and Multi GPU systems (Gfx9)</p></li>
<li><p>Checkpoint / Restore on a different system</p></li>
<li><p>Checkpoint / Restore inside a docker container</p></li>
<li><p>PyTorch</p></li>
<li><p>TensorFlow</p></li>
<li><p>Using CRIU Image Streamer</p></li>
</ul>
<p>For more information, refer to
<a class="github reference external" href="https://github.com/checkpoint-restore/criu/tree/criu-dev/plugins/amdgpu">checkpoint-restore/criu</a></p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The CRIU plugin (amdgpu_plugin) is merged upstream with the CRIU repository. The KFD kernel
patches are also available upstream with the amd-staging-drm-next branch (public) and the ROCm 5.1
release branch.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This is a Beta release of the Checkpoint and Restore functionality, and some features are not available
in this release.</p>
</div>
<p>For more information, refer to the following websites:</p>
<ul class="simple">
<li><p><a class="github reference external" href="https://github.com/RadeonOpenCompute/criu/blob/amdgpu_plugin-03252022/Documentation/amdgpu_plugin.txt">RadeonOpenCompute/criu</a></p></li>
<li><p><a class="reference external" href="https://criu.org/Main_Page">https://criu.org/Main_Page</a></p></li>
</ul>
</section>
</section>
<section id="id466">
<h3>Defect fixes<a class="headerlink" href="#id466" title="Link to this heading">#</a></h3>
<p>The following defects are fixed in this release.</p>
<section id="driver-fails-to-load-after-installation">
<h4>Driver fails to load after installation<a class="headerlink" href="#driver-fails-to-load-after-installation" title="Link to this heading">#</a></h4>
<p>The issue with the driver failing to load after ROCm installation is now fixed.</p>
<p>The driver installs successfully, and the server reboots with working rocminfo and clinfo.</p>
</section>
<section id="rocdebugger-defect-fixes">
<h4>ROCDebugger defect fixes<a class="headerlink" href="#rocdebugger-defect-fixes" title="Link to this heading">#</a></h4>
<section id="breakpoints-in-gpu-kernel-code-before-kernel-is-loaded">
<h5>Breakpoints in GPU kernel code before kernel is loaded<a class="headerlink" href="#breakpoints-in-gpu-kernel-code-before-kernel-is-loaded" title="Link to this heading">#</a></h5>
<p>Previously, setting a breakpoint in device code by line number before the device code was loaded into
the program resulted in ROCgdb incorrectly moving the breakpoint to the first following line that
contains host code.</p>
<p>Now, the breakpoint is left pending.  When the GPU kernel gets loaded, the breakpoint resolves to a
location in the kernel.</p>
</section>
<section id="registers-invalidated-after-write">
<h5>Registers invalidated after write<a class="headerlink" href="#registers-invalidated-after-write" title="Link to this heading">#</a></h5>
<p>Previously, the stale just-written value was presented as a current value.</p>
<p>ROCgdb now invalidates the cached values of registers whose content might differ after being written.
For example, registers with read-only bits.</p>
<p>ROCgdb also invalidates all volatile registers when a volatile register is written.  For example, writing
VCC invalidates the content of STATUS as STATUS.VCCZ may change.</p>
</section>
<section id="scheduler-locking-and-gpu-wavefronts">
<h5>Scheduler-locking and GPU wavefronts<a class="headerlink" href="#scheduler-locking-and-gpu-wavefronts" title="Link to this heading">#</a></h5>
<p>When scheduler-locking is in effect, new wavefronts created by a resumed thread, CPU, or GPU
wavefront, are held in the halt state. For example, the “set scheduler-locking” command.</p>
</section>
<section id="rocdebugger-fails-before-completion-of-kernel-execution">
<h5>ROCDebugger fails before completion of kernel execution<a class="headerlink" href="#rocdebugger-fails-before-completion-of-kernel-execution" title="Link to this heading">#</a></h5>
<p>It was possible (although erroneous) for a debugger to load GPU code in memory, send it to the
device, start executing a kernel on the device, and dispose of the original code before the kernel had
finished execution. If a breakpoint was hit after this point, the debugger failed with an internal error
while trying to access the debug information.</p>
<p>This issue is now fixed by ensuring that the debugger keeps a local copy of the original code and
debug information.</p>
</section>
</section>
</section>
<section id="id467">
<h3>Known issues<a class="headerlink" href="#id467" title="Link to this heading">#</a></h3>
<section id="random-memory-access-fault-errors-observed-while-running-math-libraries-unit-tests">
<h4>Random memory access fault errors observed while running math libraries unit tests<a class="headerlink" href="#random-memory-access-fault-errors-observed-while-running-math-libraries-unit-tests" title="Link to this heading">#</a></h4>
<p><strong>Issue:</strong> Random memory access fault issues are observed while running Math libraries unit tests.
This issue is encountered in ROCm v5.0, ROCm v5.0.1, and ROCm v5.0.2.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The faults only occur in the SRIOV environment.</p>
</div>
<p><strong>Workaround:</strong> Use SDMA to update the page table. The Guest set up steps are as follows:</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>sudo<span class="w"> </span>modprobe<span class="w"> </span>amdgpu<span class="w"> </span><span class="nv">vm_update_mode</span><span class="o">=</span><span class="m">0</span>
</pre></div>
</div>
<p>To verify, use</p>
<p><strong>Guest:</strong></p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>cat<span class="w"> </span>/sys/module/amdgpu/parameters/vm_update_mode<span class="w"> </span><span class="m">0</span>
</pre></div>
</div>
<p>Where expectation is 0.</p>
</section>
<section id="cu-masking-causes-application-to-freeze">
<h4>CU masking causes application to freeze<a class="headerlink" href="#cu-masking-causes-application-to-freeze" title="Link to this heading">#</a></h4>
<p>Using CU Masking results in an application freeze or runs exceptionally slowly. This issue is noticed
only in the GFX10 suite of products. Note that this issue is observed only in GFX10 suite of products.</p>
<p>This issue is under active investigation at this time.</p>
</section>
<section id="failed-checkpoint-in-docker-containers">
<h4>Failed checkpoint in Docker containers<a class="headerlink" href="#failed-checkpoint-in-docker-containers" title="Link to this heading">#</a></h4>
<p>A defect with Ubuntu images kernel-5.13-30-generic and kernel-5.13-35-generic with Overlay FS
results in incorrect reporting of the mount ID.</p>
<p>This issue with Ubuntu causes CRIU checkpointing to fail in Docker containers.</p>
<p>As a workaround, use an older version of the kernel. For example, Ubuntu 5.11.0-46-generic.</p>
</section>
<section id="issue-with-restoring-workloads-using-cooperative-groups-feature">
<h4>Issue with restoring workloads using cooperative groups feature<a class="headerlink" href="#issue-with-restoring-workloads-using-cooperative-groups-feature" title="Link to this heading">#</a></h4>
<p>Workloads that use the cooperative groups function to ensure all waves can be resident at the same
time may fail to restore correctly. This issue is under investigation and will be fixed in a future release.</p>
</section>
<section id="radeon-pro-v620-and-w6800-workstation-gpus">
<h4>Radeon Pro V620 and W6800 workstation GPUs<a class="headerlink" href="#radeon-pro-v620-and-w6800-workstation-gpus" title="Link to this heading">#</a></h4>
<section id="no-support-for-rocdebugger-on-sriov">
<h5>No support for ROCDebugger on SRIOV<a class="headerlink" href="#no-support-for-rocdebugger-on-sriov" title="Link to this heading">#</a></h5>
<p>ROCDebugger is not supported in the SRIOV environment on any GPU.</p>
<p>This is a known issue and will be fixed in a future release.</p>
</section>
</section>
<section id="random-error-messages-in-rocm-smi-for-sr-iov">
<h4>Random error messages in ROCm SMI for SR-IOV<a class="headerlink" href="#random-error-messages-in-rocm-smi-for-sr-iov" title="Link to this heading">#</a></h4>
<p>Random error messages are generated by unsupported functions or commands.</p>
<p>This is a known issue and will be fixed in a future release.</p>
</section>
</section>
<section id="library-changes-in-rocm-5-1-0">
<h3>Library changes in ROCM 5.1.0<a class="headerlink" href="#library-changes-in-rocm-5-1-0" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p>0.49.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.1.0">0.50.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p>2.10.13 ⇒ <a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.1.0">2.11.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p>1.0.4 ⇒ <a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.1.0">1.0.7</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipRAND</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/hipRAND/releases/tag/rocm-5.1.0">2.10.13</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSOLVER</p></td>
<td><p>1.2.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.1.0">1.3.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSPARSE</p></td>
<td><p>2.0.0 ⇒ <a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.1.0">2.1.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rccl</p></td>
<td><p>2.10.3 ⇒ <a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.1.0">2.11.4</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocALUTION</p></td>
<td><p>2.0.1 ⇒ <a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.1.0">2.0.2</a></p></td>
</tr>
<tr class="row-even"><td><p>rocBLAS</p></td>
<td><p>2.42.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.1.0">2.43.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocFFT</p></td>
<td><p>1.0.13 ⇒ <a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.1.0">1.0.16</a></p></td>
</tr>
<tr class="row-even"><td><p>rocPRIM</p></td>
<td><p>2.10.12 ⇒ <a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.1.0">2.10.13</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocRAND</p></td>
<td><p>2.10.12 ⇒ <a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.1.0">2.10.13</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSOLVER</p></td>
<td><p>3.16.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.1.0">3.17.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSPARSE</p></td>
<td><p>2.0.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.1.0">2.1.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocThrust</p></td>
<td><p>2.13.0 ⇒ <a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.1.0">2.14.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>Tensile</p></td>
<td><p>4.31.0 ⇒ <a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.1.0">4.32.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="hipblas-0-50-0">
<h4>hipBLAS 0.50.0<a class="headerlink" href="#hipblas-0-50-0" title="Link to this heading">#</a></h4>
<p>hipBLAS 0.50.0 for ROCm 5.1.0</p>
<section id="id468">
<h5>Added<a class="headerlink" href="#id468" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added library version and device information to hipblas-test output</p></li>
<li><p>Added –rocsolver-path command line option to choose path to pre-built rocSOLVER, as
absolute or relative path</p></li>
<li><p>Added –cmake_install command line option to update cmake to minimum version if required</p></li>
<li><p>Added cmake-arg parameter to pass in cmake arguments while building</p></li>
<li><p>Added infrastructure to support readthedocs hipBLAS documentation.</p></li>
</ul>
</section>
<section id="id469">
<h5>Fixed<a class="headerlink" href="#id469" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added hipblasVersionMinor define. hipblaseVersionMinor remains defined
for backwards compatibility.</p></li>
<li><p>Doxygen warnings in hipblas.h header file.</p></li>
</ul>
</section>
<section id="id470">
<h5>Changed<a class="headerlink" href="#id470" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>rocblas-path command line option can be specified as either absolute or relative path</p></li>
<li><p>Help message improvements in install.sh and rmake.py</p></li>
<li><p>Updated googletest dependency from 1.10.0 to 1.11.0</p></li>
</ul>
</section>
</section>
<section id="hipcub-2-11-0">
<h4>hipCUB 2.11.0<a class="headerlink" href="#hipcub-2-11-0" title="Link to this heading">#</a></h4>
<p>hipCUB 2.11.0 for ROCm 5.1.0</p>
<section id="id471">
<h5>Added<a class="headerlink" href="#id471" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Device segmented sort</p></li>
<li><p>Warp merge sort, WarpMask and thread sort from cub 1.15.0 supported in hipCUB</p></li>
<li><p>Device three way partition</p></li>
</ul>
</section>
<section id="id472">
<h5>Changed<a class="headerlink" href="#id472" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Device_scan and device_segmented_scan: inclusive_scan now uses the input-type as accumulator-type, exclusive_scan uses initial-value-type.</p>
<ul>
<li><p>This particularly changes behaviour of small-size input types with large-size output types (e.g. short input, int output).</p></li>
<li><p>And low-res input with high-res output (e.g. float input, double output)</p></li>
<li><p>Block merge sort no longer supports non power of two blocksizes</p></li>
</ul>
</li>
</ul>
</section>
</section>
<section id="hipfft-1-0-7">
<h4>hipFFT 1.0.7<a class="headerlink" href="#hipfft-1-0-7" title="Link to this heading">#</a></h4>
<p>hipFFT 1.0.7 for ROCm 5.1.0</p>
<section id="id473">
<h5>Changed<a class="headerlink" href="#id473" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Use fft_params struct for accuracy and benchmark clients.</p></li>
</ul>
</section>
</section>
<section id="hiprand-2-10-13">
<h4>hipRAND 2.10.13<a class="headerlink" href="#hiprand-2-10-13" title="Link to this heading">#</a></h4>
<p>hipRAND 2.10.13 for ROCm 5.1.0</p>
<section id="id474">
<h5>Changed<a class="headerlink" href="#id474" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Header file installation location changed to match other libraries.</p>
<ul>
<li><p>Using the <code class="docutils literal notranslate"><span class="pre">hiprand.h</span></code> header file should now use <code class="docutils literal notranslate"><span class="pre">#include</span> <span class="pre">&amp;lt;hiprand/hiprand.h&amp;gt;</span></code>, rather than <code class="docutils literal notranslate"><span class="pre">#include</span> <span class="pre">&amp;lt;hiprand.h&amp;gt;</span></code></p></li>
<li><p>Symlinks are included for backwards compatibility</p></li>
</ul>
</li>
</ul>
</section>
</section>
<section id="hipsolver-1-3-0">
<h4>hipSOLVER 1.3.0<a class="headerlink" href="#hipsolver-1-3-0" title="Link to this heading">#</a></h4>
<p>hipSOLVER 1.3.0 for ROCm 5.1.0</p>
<section id="id475">
<h5>Added<a class="headerlink" href="#id475" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added functions</p>
<ul>
<li><p>gels</p>
<ul>
<li><p>hipsolverSSgels_bufferSize, hipsolverDDgels_bufferSize, hipsolverCCgels_bufferSize, hipsolverZZgels_bufferSize</p></li>
<li><p>hipsolverSSgels, hipsolverDDgels, hipsolverCCgels, hipsolverZZgels</p></li>
</ul>
</li>
</ul>
</li>
<li><p>Added library version and device information to hipsolver-test output.</p></li>
<li><p>Added compatibility API with hipsolverDn prefix.</p></li>
<li><p>Added compatibility-only functions</p>
<ul>
<li><p>gesvdj</p>
<ul>
<li><p>hipsolverDnSgesvdj_bufferSize, hipsolverDnDgesvdj_bufferSize, hipsolverDnCgesvdj_bufferSize, hipsolverDnZgesvdj_bufferSize</p></li>
<li><p>hipsolverDnSgesvdj, hipsolverDnDgesvdj, hipsolverDnCgesvdj, hipsolverDnZgesvdj</p></li>
</ul>
</li>
<li><p>gesvdjBatched</p>
<ul>
<li><p>hipsolverDnSgesvdjBatched_bufferSize, hipsolverDnDgesvdjBatched_bufferSize, hipsolverDnCgesvdjBatched_bufferSize, hipsolverDnZgesvdjBatched_bufferSize</p></li>
<li><p>hipsolverDnSgesvdjBatched, hipsolverDnDgesvdjBatched, hipsolverDnCgesvdjBatched, hipsolverDnZgesvdjBatched</p></li>
</ul>
</li>
<li><p>syevj</p>
<ul>
<li><p>hipsolverDnSsyevj_bufferSize, hipsolverDnDsyevj_bufferSize, hipsolverDnCheevj_bufferSize, hipsolverDnZheevj_bufferSize</p></li>
<li><p>hipsolverDnSsyevj, hipsolverDnDsyevj, hipsolverDnCheevj, hipsolverDnZheevj</p></li>
</ul>
</li>
<li><p>syevjBatched</p>
<ul>
<li><p>hipsolverDnSsyevjBatched_bufferSize, hipsolverDnDsyevjBatched_bufferSize, hipsolverDnCheevjBatched_bufferSize, hipsolverDnZheevjBatched_bufferSize</p></li>
<li><p>hipsolverDnSsyevjBatched, hipsolverDnDsyevjBatched, hipsolverDnCheevjBatched, hipsolverDnZheevjBatched</p></li>
</ul>
</li>
<li><p>sygvj</p>
<ul>
<li><p>hipsolverDnSsygvj_bufferSize, hipsolverDnDsygvj_bufferSize, hipsolverDnChegvj_bufferSize, hipsolverDnZhegvj_bufferSize</p></li>
<li><p>hipsolverDnSsygvj, hipsolverDnDsygvj, hipsolverDnChegvj, hipsolverDnZhegvj</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</section>
<section id="id476">
<h5>Changed<a class="headerlink" href="#id476" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The rocSOLVER backend now allows hipsolverXXgels and hipsolverXXgesv to be called in-place when B == X.</p></li>
<li><p>The rocSOLVER backend now allows rwork to be passed as a null pointer to hipsolverXgesvd.</p></li>
</ul>
</section>
<section id="id477">
<h5>Fixed<a class="headerlink" href="#id477" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>bufferSize functions will now return HIPSOLVER_STATUS_NOT_INITIALIZED instead of HIPSOLVER_STATUS_INVALID_VALUE when both handle and lwork are null.</p></li>
<li><p>Fixed rare memory allocation failure in syevd/heevd and sygvd/hegvd caused by improper workspace array allocation outside of rocSOLVER.</p></li>
</ul>
</section>
</section>
<section id="hipsparse-2-1-0">
<h4>hipSPARSE 2.1.0<a class="headerlink" href="#hipsparse-2-1-0" title="Link to this heading">#</a></h4>
<p>hipSPARSE 2.1.0 for ROCm 5.1.0</p>
<section id="id478">
<h5>Added<a class="headerlink" href="#id478" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added gtsv_interleaved_batch and gpsv_interleaved_batch routines</p></li>
<li><p>Add SpGEMM_reuse</p></li>
</ul>
</section>
<section id="id479">
<h5>Changed<a class="headerlink" href="#id479" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Changed BUILD_CUDA with USE_CUDA in install script and cmake files</p></li>
<li><p>Update googletest to 11.1</p></li>
</ul>
</section>
<section id="id480">
<h5>Improved<a class="headerlink" href="#id480" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed a bug in SpMM Alg versioning</p></li>
</ul>
</section>
<section id="id481">
<h5>Known Issues<a class="headerlink" href="#id481" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>none</p></li>
</ul>
</section>
</section>
<section id="rccl-2-11-4">
<h4>rccl 2.11.4<a class="headerlink" href="#rccl-2-11-4" title="Link to this heading">#</a></h4>
<p>RCCL 2.11.4 for ROCm 5.1.0</p>
<section id="id482">
<h5>Added<a class="headerlink" href="#id482" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Compatibility with NCCL 2.11.4</p></li>
</ul>
</section>
<section id="id483">
<h5>Known Issues<a class="headerlink" href="#id483" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Managed memory is not currently supported for clique-based kernels</p></li>
</ul>
</section>
</section>
<section id="rocalution-2-0-2">
<h4>rocALUTION 2.0.2<a class="headerlink" href="#rocalution-2-0-2" title="Link to this heading">#</a></h4>
<p>rocALUTION 2.0.2 for ROCm 5.1.0</p>
<section id="id484">
<h5>Added<a class="headerlink" href="#id484" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added out-of-place matrix transpose functionality</p></li>
<li><p>Added LocalVector&lt;bool&gt;</p></li>
</ul>
</section>
</section>
<section id="rocblas-2-43-0">
<h4>rocBLAS 2.43.0<a class="headerlink" href="#rocblas-2-43-0" title="Link to this heading">#</a></h4>
<p>rocBLAS 2.43.0 for ROCm 5.1.0</p>
<section id="id485">
<h5>Added<a class="headerlink" href="#id485" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Option to install script for number of jobs to use for rocBLAS and Tensile compilation (-j, –jobs)</p></li>
<li><p>Option to install script to build clients without using any Fortran (–clients_no_fortran)</p></li>
<li><p>rocblas_client_initialize function, to perform rocBLAS initialize for clients(benchmark/test) and report the execution time.</p></li>
<li><p>Added tests for output of reduction functions when given bad input</p></li>
<li><p>Added user specified initialization (rand_int/trig_float/hpl) for initializing matrices and vectors in rocblas-bench</p></li>
</ul>
</section>
<section id="id486">
<h5>Optimizations<a class="headerlink" href="#id486" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved performance of trsm with side == left and n == 1</p></li>
<li><p>Improved perforamnce of trsm with side == left and m &lt;= 32 along with side == right and n &lt;= 32</p></li>
</ul>
</section>
<section id="id487">
<h5>Changed<a class="headerlink" href="#id487" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>For syrkx and trmm internal API use rocblas_stride datatype for offset</p></li>
<li><p>For non-batched and batched gemm_ex functions if the C matrix pointer equals the D matrix pointer (aliased) their respective type and leading dimension arguments must now match</p></li>
<li><p>Test client dependencies updated to GTest 1.11</p></li>
<li><p>non-global false positives reported by cppcheck from file based suppression to inline suppression. File based suppression will only be used for global false positives.</p></li>
<li><p>Help menu messages in install.sh</p></li>
<li><p>For ger function, typecast the ‘lda’(offset) datatype to size_t during offset calculation to avoid overflow and remove duplicate template functions.</p></li>
<li><p>Modified default initialization from rand_int to hpl for initializing matrices and vectors in rocblas-bench</p></li>
</ul>
</section>
<section id="id488">
<h5>Fixed<a class="headerlink" href="#id488" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>For function trmv (non-transposed cases) avoid overflow in offset calculation</p></li>
<li><p>Fixed cppcheck errors/warnings</p></li>
<li><p>Fixed doxygen warnings</p></li>
</ul>
</section>
</section>
<section id="rocfft-1-0-16">
<h4>rocFFT 1.0.16<a class="headerlink" href="#rocfft-1-0-16" title="Link to this heading">#</a></h4>
<p>rocFFT 1.0.16 for ROCm 5.1.0</p>
<section id="id489">
<h5>Changed<a class="headerlink" href="#id489" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Supported unaligned tile dimension for SBRC_2D kernels.</p></li>
<li><p>Improved (more RAII) test and benchmark infrastructure.</p></li>
<li><p>Enabled runtime compilation of length-2304 FFT kernel during plan creation.</p></li>
</ul>
</section>
<section id="id490">
<h5>Optimizations<a class="headerlink" href="#id490" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimized more large 1D cases by using L1D_CC plan.</p></li>
<li><p>Optimized 3D 200^3 C2R case.</p></li>
<li><p>Optimized 1D 2^30 double precision on MI200.</p></li>
</ul>
</section>
<section id="id491">
<h5>Fixed<a class="headerlink" href="#id491" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed correctness of some R2C transforms with unusual strides.</p></li>
</ul>
</section>
<section id="id492">
<h5>Removed<a class="headerlink" href="#id492" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The hipFFT API (header) has been removed from after a long deprecation period.  Please use the <a class="reference external" href="https://github.com/ROCmSoftwarePlatform/hipFFT">hipFFT</a> package/repository to obtain the hipFFT API.</p></li>
</ul>
</section>
</section>
<section id="rocprim-2-10-13">
<h4>rocPRIM 2.10.13<a class="headerlink" href="#rocprim-2-10-13" title="Link to this heading">#</a></h4>
<p>rocPRIM 2.10.13 for ROCm 5.1.0</p>
<section id="id493">
<h5>Fixed<a class="headerlink" href="#id493" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed radix sort int64_t bug introduced in [2.10.11]</p></li>
</ul>
</section>
<section id="id494">
<h5>Added<a class="headerlink" href="#id494" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Future value</p></li>
<li><p>Added device partition_three_way to partition input to three output iterators based on two predicates</p></li>
</ul>
</section>
<section id="id495">
<h5>Changed<a class="headerlink" href="#id495" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The reduce/scan algorithm precision issues in the tests has been resolved for half types.</p></li>
</ul>
</section>
<section id="id496">
<h5>Known Issues<a class="headerlink" href="#id496" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>device_segmented_radix_sort unit test failing for HIP on Windows</p></li>
</ul>
</section>
</section>
<section id="rocrand-2-10-13">
<h4>rocRAND 2.10.13<a class="headerlink" href="#rocrand-2-10-13" title="Link to this heading">#</a></h4>
<p>rocRAND 2.10.13 for ROCm 5.1.0</p>
<section id="id497">
<h5>Added<a class="headerlink" href="#id497" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Generating a random sequence different sizes now produces the same sequence without gaps
indepent of how many values are generated per call.</p>
<ul>
<li><p>Only in the case of XORWOW, MRG32K3A, PHILOX4X32_10, SOBOL32 and SOBOL64</p></li>
<li><p>This only holds true if the size in each call is a divisor of the distributions
<code class="docutils literal notranslate"><span class="pre">output_width</span></code> due to performance</p></li>
<li><p>Similarly the output pointer has to be aligned to <code class="docutils literal notranslate"><span class="pre">output_width</span> <span class="pre">*</span> <span class="pre">sizeof(output_type)</span></code></p></li>
</ul>
</li>
</ul>
</section>
<section id="id498">
<h5>Changed<a class="headerlink" href="#id498" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p><a class="reference external" href="https://github.com/ROCmSoftwarePlatform/hipRAND.git">hipRAND</a> split into a separate package</p></li>
<li><p>Header file installation location changed to match other libraries.</p>
<ul>
<li><p>Using the <code class="docutils literal notranslate"><span class="pre">rocrand.h</span></code> header file should now use <code class="docutils literal notranslate"><span class="pre">#include</span> <span class="pre">&amp;lt;rocrand/rocrand.h&amp;gt;</span></code>, rather than <code class="docutils literal notranslate"><span class="pre">#include</span> <span class="pre">&amp;lt;rocrand/rocrand.h&amp;gt;</span></code></p></li>
</ul>
</li>
<li><p>rocRAND still includes hipRAND using a submodule</p>
<ul>
<li><p>The rocRAND package also sets the provides field with hipRAND, so projects which require hipRAND can begin to specify it.</p></li>
</ul>
</li>
</ul>
</section>
<section id="id499">
<h5>Fixed<a class="headerlink" href="#id499" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fix offset behaviour for XORWOW, MRG32K3A and PHILOX4X32_10 generator, setting offset now
correctly generates the same sequence starting from the offset.</p>
<ul>
<li><p>Only uniform int and float will work as these can be generated with a single call to the generator</p></li>
</ul>
</li>
</ul>
</section>
<section id="id500">
<h5>Known Issues<a class="headerlink" href="#id500" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>kernel_xorwow unit test is failing for certain GPU architectures.</p></li>
</ul>
</section>
</section>
<section id="rocsolver-3-17-0">
<h4>rocSOLVER 3.17.0<a class="headerlink" href="#rocsolver-3-17-0" title="Link to this heading">#</a></h4>
<p>rocSOLVER 3.17.0 for ROCm 5.1.0</p>
<section id="id501">
<h5>Optimized<a class="headerlink" href="#id501" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimized non-pivoting and batch cases of the LU factorization</p></li>
</ul>
</section>
<section id="id502">
<h5>Fixed<a class="headerlink" href="#id502" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed missing synchronization in SYTRF with <code class="docutils literal notranslate"><span class="pre">rocblas_fill_lower</span></code> that could potentially
result in incorrect pivot values.</p></li>
<li><p>Fixed multi-level logging output to file with the <code class="docutils literal notranslate"><span class="pre">ROCSOLVER_LOG_PATH</span></code>,
<code class="docutils literal notranslate"><span class="pre">ROCSOLVER_LOG_TRACE_PATH</span></code>, <code class="docutils literal notranslate"><span class="pre">ROCSOLVER_LOG_BENCH_PATH</span></code> and <code class="docutils literal notranslate"><span class="pre">ROCSOLVER_LOG_PROFILE_PATH</span></code>
environment variables.</p></li>
<li><p>Fixed performance regression in the batched LU factorization of tiny matrices</p></li>
</ul>
</section>
</section>
<section id="rocsparse-2-1-0">
<h4>rocSPARSE 2.1.0<a class="headerlink" href="#rocsparse-2-1-0" title="Link to this heading">#</a></h4>
<p>rocSPARSE 2.1.0 for ROCm 5.1.0</p>
<section id="id503">
<h5>Added<a class="headerlink" href="#id503" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>gtsv_interleaved_batch</p></li>
<li><p>gpsv_interleaved_batch</p></li>
<li><p>SpGEMM_reuse</p></li>
<li><p>Allow copying of mat info struct</p></li>
</ul>
</section>
<section id="id504">
<h5>Improved<a class="headerlink" href="#id504" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimization for SDDMM</p></li>
<li><p>Allow unsorted matrices in csrgemm multipass algorithm</p></li>
</ul>
</section>
<section id="id505">
<h5>Known Issues<a class="headerlink" href="#id505" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>none</p></li>
</ul>
</section>
</section>
<section id="rocthrust-2-14-0">
<h4>rocThrust 2.14.0<a class="headerlink" href="#rocthrust-2-14-0" title="Link to this heading">#</a></h4>
<p>rocThrust 2.14.0 for ROCm 5.1.0</p>
<section id="id506">
<h5>Added<a class="headerlink" href="#id506" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Updated to match upstream Thrust 1.15.0</p></li>
</ul>
</section>
<section id="id507">
<h5>Known Issues<a class="headerlink" href="#id507" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>async_copy, partition, and stable_sort_by_key unit tests are failing on HIP on Windows.</p></li>
</ul>
</section>
</section>
<section id="tensile-4-32-0">
<h4>Tensile 4.32.0<a class="headerlink" href="#tensile-4-32-0" title="Link to this heading">#</a></h4>
<p>Tensile 4.32.0 for ROCm 5.1.0</p>
<section id="id508">
<h5>Added<a class="headerlink" href="#id508" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Better control of parallelism to control memory usage</p></li>
<li><p>Support for multiprocessing on Windows for TensileCreateLibrary</p></li>
<li><p>New JSD metric and metric selection functionality</p></li>
<li><p>Initial changes to support two-tier solution selection</p></li>
</ul>
</section>
<section id="id509">
<h5>Optimized<a class="headerlink" href="#id509" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimized runtime of TensileCreateLibraries by reducing max RAM usage</p></li>
<li><p>StoreCInUnroll additional optimizations plus adaptive K support</p></li>
<li><p>DGEMM NN optimizations with PrefetchGlobalRead(PGR)=2 support</p></li>
</ul>
</section>
<section id="id510">
<h5>Changed<a class="headerlink" href="#id510" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Update Googletest to 1.11.0</p></li>
</ul>
</section>
<section id="id511">
<h5>Removed<a class="headerlink" href="#id511" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Remove no longer supported benchmarking steps</p></li>
</ul>
</section>
</section>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-0-2">
<h2>ROCm 5.0.2<a class="headerlink" href="#rocm-5-0-2" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<section id="id512">
<h3>Defect fixes<a class="headerlink" href="#id512" title="Link to this heading">#</a></h3>
<p>The following defects are fixed in the ROCm v5.0.2 release.</p>
<section id="issue-with-hostcall-facility-in-hip-runtime">
<h4>Issue with hostcall facility in HIP runtime<a class="headerlink" href="#issue-with-hostcall-facility-in-hip-runtime" title="Link to this heading">#</a></h4>
<p>In ROCm v5.0, when using the “assert()” call in a HIP kernel, the compiler may sometimes fail to emit
kernel metadata related to the hostcall facility, which results in incomplete initialization of the hostcall
facility in the HIP runtime. This can cause the HIP kernel to crash when it attempts to execute the
“assert()” call.</p>
<p>The root cause was an incorrect check in the compiler to determine whether the hostcall facility is
required by the kernel. This is fixed in the ROCm v5.0.2 release.</p>
<p>The resolution includes a compiler change, which emits the required metadata by default, unless the
compiler can prove that the hostcall facility is not required by the kernel. This ensures that the
“assert()” call never fails.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This fix may lead to breakage in some OpenMP offload use cases, which use print inside a target region
and result in an abort in device code. The issue will be fixed in a future release.</p>
</div>
<p>The compatibility matrix in the <a class="reference internal" href="../how-to/deep-learning-rocm.html"><span class="std std-doc">Deep-learning guide</span></a> is updated for
ROCm v5.0.2.</p>
</section>
</section>
<section id="library-changes-in-rocm-5-0-2">
<h3>Library changes in ROCM 5.0.2<a class="headerlink" href="#library-changes-in-rocm-5-0-2" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.0.2">0.49.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.0.2">2.10.13</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.0.2">1.0.4</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.0.2">1.2.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.0.2">2.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.0.2">2.10.3</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.0.2">2.0.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.0.2">2.42.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.0.2">1.0.13</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.0.2">2.10.12</a></p></td>
</tr>
<tr class="row-even"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.0.2">2.10.12</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.0.2">3.16.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.0.2">2.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.0.2">2.13.0</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.0.2">4.31.0</a></p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-0-1">
<h2>ROCm 5.0.1<a class="headerlink" href="#rocm-5-0-1" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<section id="id513">
<h3>Deprecations and warnings<a class="headerlink" href="#id513" title="Link to this heading">#</a></h3>
<section id="refactor-of-hipcc-hipconfig">
<h4>Refactor of HIPCC/HIPCONFIG<a class="headerlink" href="#refactor-of-hipcc-hipconfig" title="Link to this heading">#</a></h4>
<p>In prior ROCm releases, by default, the hipcc/hipconfig Perl scripts were used to identify and set target
compiler options, target platform, compiler, and runtime appropriately.</p>
<p>In ROCm v5.0.1, hipcc.bin and hipconfig.bin have been added as the compiled binary implementations
of the hipcc and hipconfig. These new binaries are currently a work-in-progress, considered, and
marked as experimental. ROCm plans to fully transition to hipcc.bin and hipconfig.bin in the a future
ROCm release. The existing hipcc and hipconfig Perl scripts are renamed to <code class="docutils literal notranslate"><span class="pre">hipcc.pl</span></code> and <code class="docutils literal notranslate"><span class="pre">hipconfig.pl</span></code>
respectively. New top-level hipcc and hipconfig Perl scripts are created, which can switch between the
Perl script or the compiled binary based on the environment variable <code class="docutils literal notranslate"><span class="pre">HIPCC_USE_PERL_SCRIPT</span></code>.</p>
<p>In ROCm 5.0.1, by default, this environment variable is set to use hipcc and hipconfig through the Perl
scripts.</p>
<p>Subsequent Perl scripts will no longer be available in ROCm in a future release.</p>
</section>
</section>
<section id="library-changes-in-rocm-5-0-1">
<h3>Library changes in ROCM 5.0.1<a class="headerlink" href="#library-changes-in-rocm-5-0-1" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.0.1">0.49.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.0.1">2.10.13</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.0.1">1.0.4</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.0.1">1.2.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.0.1">2.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.0.1">2.10.3</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.0.1">2.0.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.0.1">2.42.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.0.1">1.0.13</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocPRIM</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.0.1">2.10.12</a></p></td>
</tr>
<tr class="row-even"><td><p>rocRAND</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.0.1">2.10.12</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSOLVER</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.0.1">3.16.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSPARSE</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.0.1">2.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocThrust</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.0.1">2.13.0</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p><a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.0.1">4.31.0</a></p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<hr class="docutils"/>
<section id="rocm-5-0-0">
<h2>ROCm 5.0.0<a class="headerlink" href="#rocm-5-0-0" title="Link to this heading">#</a></h2>
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable no-blanks-blockquote -->
<section id="id514">
<h3>What’s new in this release<a class="headerlink" href="#id514" title="Link to this heading">#</a></h3>
<section id="id515">
<h4>HIP enhancements<a class="headerlink" href="#id515" title="Link to this heading">#</a></h4>
<p>The ROCm v5.0 release consists of the following HIP enhancements.</p>
<section id="id516">
<h5>HIP installation guide updates<a class="headerlink" href="#id516" title="Link to this heading">#</a></h5>
<p>The HIP Installation Guide is updated to include building HIP from source on the NVIDIA platform.</p>
<p>Refer to the HIP Installation Guide v5.0 for more details.</p>
</section>
<section id="managed-memory-allocation">
<h5>Managed memory allocation<a class="headerlink" href="#managed-memory-allocation" title="Link to this heading">#</a></h5>
<p>Managed memory, including the <code class="docutils literal notranslate"><span class="pre">__managed__</span></code> keyword, is now supported in the HIP combined host/device compilation. Through unified memory allocation, managed memory allows data to be shared and accessible to both the CPU and GPU using a single pointer. The allocation is managed by the AMD GPU driver using the Linux Heterogeneous Memory Management (HMM) mechanism. The user can call managed memory API hipMallocManaged to allocate a large chunk of HMM memory, execute kernels on a device, and fetch data between the host and device as needed.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>In a HIP application,  it is recommended to do a capability check before calling the managed memory APIs. For example,</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">managed_memory</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipDeviceGetAttribute</span><span class="p">(</span><span class="o">&amp;</span><span class="n">managed_memory</span><span class="p">,</span>
<span class="w">  </span><span class="n">hipDeviceAttributeManagedMemory</span><span class="p">,</span><span class="n">p_gpuDevice</span><span class="p">));</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="o">!</span><span class="n">managed_memory</span><span class="w"> </span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="w"> </span><span class="p">(</span><span class="s">"info: managed memory access not supported on the device %d</span><span class="se">\n</span><span class="s"> Skipped</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">p_gpuDevice</span><span class="p">);</span>
<span class="p">}</span>
<span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipSetDevice</span><span class="p">(</span><span class="n">p_gpuDevice</span><span class="p">));</span>
<span class="w">  </span><span class="n">HIPCHECK</span><span class="p">(</span><span class="n">hipMallocManaged</span><span class="p">(</span><span class="o">&amp;</span><span class="n">Hmm</span><span class="p">,</span><span class="w"> </span><span class="n">N</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="k">sizeof</span><span class="p">(</span><span class="n">T</span><span class="p">)));</span>
<span class="p">.</span><span class="w"> </span><span class="p">.</span><span class="w"> </span><span class="p">.</span>
<span class="p">}</span>
</pre></div>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The managed memory capability check may not be necessary; however, if HMM is not supported, managed malloc will fall back to using system memory. Other managed memory API calls will, then, have</p>
</div>
<p>Refer to the HIP API documentation for more details on managed memory APIs.</p>
<p>For the application, see</p>
<p><a class="github reference external" href="https://github.com/ROCm-Developer-Tools/HIP/blob/rocm-4.5.x/tests/src/runtimeApi/memory/hipMallocManaged.cpp">ROCm-Developer-Tools/HIP</a></p>
</section>
</section>
<section id="new-environment-variable">
<h4>New environment variable<a class="headerlink" href="#new-environment-variable" title="Link to this heading">#</a></h4>
<p>The following new environment variable is added in this release:</p>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Environment Variable</p></th>
<th class="head"><p>Value</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>HSA_COOP_CU_COUNT</p></td>
<td><p>0 or 1 (default is 0)</p></td>
<td><p>Some processors support more CUs than can reliably be used in a cooperative dispatch. Setting the environment variable HSA_COOP_CU_COUNT to 1 will cause ROCr to return the correct CU count for cooperative groups through the HSA_AMD_AGENT_INFO_COOPERATIVE_COMPUTE_UNIT_COUNT attribute of hsa_agent_get_info(). Setting HSA_COOP_CU_COUNT to other values, or leaving it unset, will cause ROCr to return the same CU count for the attributes HSA_AMD_AGENT_INFO_COOPERATIVE_COMPUTE_UNIT_COUNT and HSA_AMD_AGENT_INFO_COMPUTE_UNIT_COUNT. Future ROCm releases will make HSA_COOP_CU_COUNT=1 the default.</p></td>
</tr>
</tbody>
</table>
</div>
</section>
</section>
<section id="breaking-changes">
<h3>Breaking changes<a class="headerlink" href="#breaking-changes" title="Link to this heading">#</a></h3>
<section id="runtime-breaking-change">
<h4>Runtime breaking change<a class="headerlink" href="#runtime-breaking-change" title="Link to this heading">#</a></h4>
<p>Re-ordering of the enumerated type in hip_runtime_api.h to better match NV.  See below for the difference in enumerated types.</p>
<p>ROCm software will be affected if any of the defined enums listed below are used in the code.  Applications built with ROCm v5.0 enumerated types will work with a ROCm 4.5.2 driver. However, an undefined behavior error will occur with a ROCm v4.5.2 application that uses these enumerated types with a ROCm 5.0 runtime.</p>
<div class="highlight-diff notranslate"><div class="highlight"><pre><span></span>typedef enum hipDeviceAttribute_t {
<span class="gd">-    hipDeviceAttributeMaxThreadsPerBlock,       ///&lt; Maximum number of threads per block.</span>
<span class="gd">-    hipDeviceAttributeMaxBlockDimX,             ///&lt; Maximum x-dimension of a block.</span>
<span class="gd">-    hipDeviceAttributeMaxBlockDimY,             ///&lt; Maximum y-dimension of a block.</span>
<span class="gd">-    hipDeviceAttributeMaxBlockDimZ,             ///&lt; Maximum z-dimension of a block.</span>
<span class="gd">-    hipDeviceAttributeMaxGridDimX,              ///&lt; Maximum x-dimension of a grid.</span>
<span class="gd">-    hipDeviceAttributeMaxGridDimY,              ///&lt; Maximum y-dimension of a grid.</span>
<span class="gd">-    hipDeviceAttributeMaxGridDimZ,              ///&lt; Maximum z-dimension of a grid.</span>
<span class="gd">-    hipDeviceAttributeMaxSharedMemoryPerBlock,  ///&lt; Maximum shared memory available per block in</span>
<span class="gd">-                                                ///&lt; bytes.</span>
<span class="gd">-    hipDeviceAttributeTotalConstantMemory,      ///&lt; Constant memory size in bytes.</span>
<span class="gd">-    hipDeviceAttributeWarpSize,                 ///&lt; Warp size in threads.</span>
<span class="gd">-    hipDeviceAttributeMaxRegistersPerBlock,  ///&lt; Maximum number of 32-bit registers available to a</span>
<span class="gd">-                                             ///&lt; thread block. This number is shared by all thread</span>
<span class="gd">-                                             ///&lt; blocks simultaneously resident on a</span>
<span class="gd">-                                             ///&lt; multiprocessor.</span>
<span class="gd">-    hipDeviceAttributeClockRate,             ///&lt; Peak clock frequency in kilohertz.</span>
<span class="gd">-    hipDeviceAttributeMemoryClockRate,       ///&lt; Peak memory clock frequency in kilohertz.</span>
<span class="gd">-    hipDeviceAttributeMemoryBusWidth,        ///&lt; Global memory bus width in bits.</span>
<span class="gd">-    hipDeviceAttributeMultiprocessorCount,   ///&lt; Number of multiprocessors on the device.</span>
<span class="gd">-    hipDeviceAttributeComputeMode,           ///&lt; Compute mode that device is currently in.</span>
<span class="gd">-    hipDeviceAttributeL2CacheSize,  ///&lt; Size of L2 cache in bytes. 0 if the device doesn't have L2</span>
<span class="gd">-                                    ///&lt; cache.</span>
<span class="gd">-    hipDeviceAttributeMaxThreadsPerMultiProcessor,  ///&lt; Maximum resident threads per</span>
<span class="gd">-                                                    ///&lt; multiprocessor.</span>
<span class="gd">-    hipDeviceAttributeComputeCapabilityMajor,       ///&lt; Major compute capability version number.</span>
<span class="gd">-    hipDeviceAttributeComputeCapabilityMinor,       ///&lt; Minor compute capability version number.</span>
<span class="gd">-    hipDeviceAttributeConcurrentKernels,  ///&lt; Device can possibly execute multiple kernels</span>
<span class="gd">-                                          ///&lt; concurrently.</span>
<span class="gd">-    hipDeviceAttributePciBusId,           ///&lt; PCI Bus ID.</span>
<span class="gd">-    hipDeviceAttributePciDeviceId,        ///&lt; PCI Device ID.</span>
<span class="gd">-    hipDeviceAttributeMaxSharedMemoryPerMultiprocessor,  ///&lt; Maximum Shared Memory Per</span>
<span class="gd">-                                                         ///&lt; Multiprocessor.</span>
<span class="gd">-    hipDeviceAttributeIsMultiGpuBoard,                   ///&lt; Multiple GPU devices.</span>
<span class="gd">-    hipDeviceAttributeIntegrated,                        ///&lt; iGPU</span>
<span class="gd">-    hipDeviceAttributeCooperativeLaunch,                 ///&lt; Support cooperative launch</span>
<span class="gd">-    hipDeviceAttributeCooperativeMultiDeviceLaunch,      ///&lt; Support cooperative launch on multiple devices</span>
<span class="gd">-    hipDeviceAttributeMaxTexture1DWidth,    ///&lt; Maximum number of elements in 1D images</span>
<span class="gd">-    hipDeviceAttributeMaxTexture2DWidth,    ///&lt; Maximum dimension width of 2D images in image elements</span>
<span class="gd">-    hipDeviceAttributeMaxTexture2DHeight,   ///&lt; Maximum dimension height of 2D images in image elements</span>
<span class="gd">-    hipDeviceAttributeMaxTexture3DWidth,    ///&lt; Maximum dimension width of 3D images in image elements</span>
<span class="gd">-    hipDeviceAttributeMaxTexture3DHeight,   ///&lt; Maximum dimensions height of 3D images in image elements</span>
<span class="gd">-    hipDeviceAttributeMaxTexture3DDepth,    ///&lt; Maximum dimensions depth of 3D images in image elements</span>
<span class="gi">+    hipDeviceAttributeCudaCompatibleBegin = 0,</span>

<span class="gd">-    hipDeviceAttributeHdpMemFlushCntl,      ///&lt; Address of the HDP_MEM_COHERENCY_FLUSH_CNTL register</span>
<span class="gd">-    hipDeviceAttributeHdpRegFlushCntl,      ///&lt; Address of the HDP_REG_COHERENCY_FLUSH_CNTL register</span>
<span class="gi">+    hipDeviceAttributeEccEnabled = hipDeviceAttributeCudaCompatibleBegin, ///&lt; Whether ECC support is enabled.</span>
<span class="gi">+    hipDeviceAttributeAccessPolicyMaxWindowSize,        ///&lt; Cuda only. The maximum size of the window policy in bytes.</span>
<span class="gi">+    hipDeviceAttributeAsyncEngineCount,                 ///&lt; Cuda only. Asynchronous engines number.</span>
<span class="gi">+    hipDeviceAttributeCanMapHostMemory,                 ///&lt; Whether host memory can be mapped into device address space</span>
<span class="gi">+    hipDeviceAttributeCanUseHostPointerForRegisteredMem,///&lt; Cuda only. Device can access host registered memory</span>
<span class="gi">+                                                        ///&lt; at the same virtual address as the CPU</span>
<span class="gi">+    hipDeviceAttributeClockRate,                        ///&lt; Peak clock frequency in kilohertz.</span>
<span class="gi">+    hipDeviceAttributeComputeMode,                      ///&lt; Compute mode that device is currently in.</span>
<span class="gi">+    hipDeviceAttributeComputePreemptionSupported,       ///&lt; Cuda only. Device supports Compute Preemption.</span>
<span class="gi">+    hipDeviceAttributeConcurrentKernels,                ///&lt; Device can possibly execute multiple kernels concurrently.</span>
<span class="gi">+    hipDeviceAttributeConcurrentManagedAccess,          ///&lt; Device can coherently access managed memory concurrently with the CPU</span>
<span class="gi">+    hipDeviceAttributeCooperativeLaunch,                ///&lt; Support cooperative launch</span>
<span class="gi">+    hipDeviceAttributeCooperativeMultiDeviceLaunch,     ///&lt; Support cooperative launch on multiple devices</span>
<span class="gi">+    hipDeviceAttributeDeviceOverlap,                    ///&lt; Cuda only. Device can concurrently copy memory and execute a kernel.</span>
<span class="gi">+                                                        ///&lt; Deprecated. Use instead asyncEngineCount.</span>
<span class="gi">+    hipDeviceAttributeDirectManagedMemAccessFromHost,   ///&lt; Host can directly access managed memory on</span>
<span class="gi">+                                                        ///&lt; the device without migration</span>
<span class="gi">+    hipDeviceAttributeGlobalL1CacheSupported,           ///&lt; Cuda only. Device supports caching globals in L1</span>
<span class="gi">+    hipDeviceAttributeHostNativeAtomicSupported,        ///&lt; Cuda only. Link between the device and the host supports native atomic operations</span>
<span class="gi">+    hipDeviceAttributeIntegrated,                       ///&lt; Device is integrated GPU</span>
<span class="gi">+    hipDeviceAttributeIsMultiGpuBoard,                  ///&lt; Multiple GPU devices.</span>
<span class="gi">+    hipDeviceAttributeKernelExecTimeout,                ///&lt; Run time limit for kernels executed on the device</span>
<span class="gi">+    hipDeviceAttributeL2CacheSize,                      ///&lt; Size of L2 cache in bytes. 0 if the device doesn't have L2 cache.</span>
<span class="gi">+    hipDeviceAttributeLocalL1CacheSupported,            ///&lt; caching locals in L1 is supported</span>
<span class="gi">+    hipDeviceAttributeLuid,                             ///&lt; Cuda only. 8-byte locally unique identifier in 8 bytes. Undefined on TCC and non-Windows platforms</span>
<span class="gi">+    hipDeviceAttributeLuidDeviceNodeMask,               ///&lt; Cuda only. Luid device node mask. Undefined on TCC and non-Windows platforms</span>
<span class="gi">+    hipDeviceAttributeComputeCapabilityMajor,           ///&lt; Major compute capability version number.</span>
<span class="gi">+    hipDeviceAttributeManagedMemory,                    ///&lt; Device supports allocating managed memory on this system</span>
<span class="gi">+    hipDeviceAttributeMaxBlocksPerMultiProcessor,       ///&lt; Cuda only. Max block size per multiprocessor</span>
<span class="gi">+    hipDeviceAttributeMaxBlockDimX,                     ///&lt; Max block size in width.</span>
<span class="gi">+    hipDeviceAttributeMaxBlockDimY,                     ///&lt; Max block size in height.</span>
<span class="gi">+    hipDeviceAttributeMaxBlockDimZ,                     ///&lt; Max block size in depth.</span>
<span class="gi">+    hipDeviceAttributeMaxGridDimX,                      ///&lt; Max grid size  in width.</span>
<span class="gi">+    hipDeviceAttributeMaxGridDimY,                      ///&lt; Max grid size  in height.</span>
<span class="gi">+    hipDeviceAttributeMaxGridDimZ,                      ///&lt; Max grid size  in depth.</span>
<span class="gi">+    hipDeviceAttributeMaxSurface1D,                     ///&lt; Maximum size of 1D surface.</span>
<span class="gi">+    hipDeviceAttributeMaxSurface1DLayered,              ///&lt; Cuda only. Maximum dimensions of 1D layered surface.</span>
<span class="gi">+    hipDeviceAttributeMaxSurface2D,                     ///&lt; Maximum dimension (width, height) of 2D surface.</span>
<span class="gi">+    hipDeviceAttributeMaxSurface2DLayered,              ///&lt; Cuda only. Maximum dimensions of 2D layered surface.</span>
<span class="gi">+    hipDeviceAttributeMaxSurface3D,                     ///&lt; Maximum dimension (width, height, depth) of 3D surface.</span>
<span class="gi">+    hipDeviceAttributeMaxSurfaceCubemap,                ///&lt; Cuda only. Maximum dimensions of Cubemap surface.</span>
<span class="gi">+    hipDeviceAttributeMaxSurfaceCubemapLayered,         ///&lt; Cuda only. Maximum dimension of Cubemap layered surface.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture1DWidth,                ///&lt; Maximum size of 1D texture.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture1DLayered,              ///&lt; Cuda only. Maximum dimensions of 1D layered texture.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture1DLinear,               ///&lt; Maximum number of elements allocatable in a 1D linear texture.</span>
<span class="gi">+                                                        ///&lt; Use cudaDeviceGetTexture1DLinearMaxWidth() instead on Cuda.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture1DMipmap,               ///&lt; Cuda only. Maximum size of 1D mipmapped texture.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture2DWidth,                ///&lt; Maximum dimension width of 2D texture.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture2DHeight,               ///&lt; Maximum dimension hight of 2D texture.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture2DGather,               ///&lt; Cuda only. Maximum dimensions of 2D texture if gather operations  performed.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture2DLayered,              ///&lt; Cuda only. Maximum dimensions of 2D layered texture.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture2DLinear,               ///&lt; Cuda only. Maximum dimensions (width, height, pitch) of 2D textures bound to pitched memory.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture2DMipmap,               ///&lt; Cuda only. Maximum dimensions of 2D mipmapped texture.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture3DWidth,                ///&lt; Maximum dimension width of 3D texture.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture3DHeight,               ///&lt; Maximum dimension height of 3D texture.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture3DDepth,                ///&lt; Maximum dimension depth of 3D texture.</span>
<span class="gi">+    hipDeviceAttributeMaxTexture3DAlt,                  ///&lt; Cuda only. Maximum dimensions of alternate 3D texture.</span>
<span class="gi">+    hipDeviceAttributeMaxTextureCubemap,                ///&lt; Cuda only. Maximum dimensions of Cubemap texture</span>
<span class="gi">+    hipDeviceAttributeMaxTextureCubemapLayered,         ///&lt; Cuda only. Maximum dimensions of Cubemap layered texture.</span>
<span class="gi">+    hipDeviceAttributeMaxThreadsDim,                    ///&lt; Maximum dimension of a block</span>
<span class="gi">+    hipDeviceAttributeMaxThreadsPerBlock,               ///&lt; Maximum number of threads per block.</span>
<span class="gi">+    hipDeviceAttributeMaxThreadsPerMultiProcessor,      ///&lt; Maximum resident threads per multiprocessor.</span>
<span class="gi">+    hipDeviceAttributeMaxPitch,                         ///&lt; Maximum pitch in bytes allowed by memory copies</span>
<span class="gi">+    hipDeviceAttributeMemoryBusWidth,                   ///&lt; Global memory bus width in bits.</span>
<span class="gi">+    hipDeviceAttributeMemoryClockRate,                  ///&lt; Peak memory clock frequency in kilohertz.</span>
<span class="gi">+    hipDeviceAttributeComputeCapabilityMinor,           ///&lt; Minor compute capability version number.</span>
<span class="gi">+    hipDeviceAttributeMultiGpuBoardGroupID,             ///&lt; Cuda only. Unique ID of device group on the same multi-GPU board</span>
<span class="gi">+    hipDeviceAttributeMultiprocessorCount,              ///&lt; Number of multiprocessors on the device.</span>
<span class="gi">+    hipDeviceAttributeName,                             ///&lt; Device name.</span>
<span class="gi">+    hipDeviceAttributePageableMemoryAccess,             ///&lt; Device supports coherently accessing pageable memory</span>
<span class="gi">+                                                        ///&lt; without calling hipHostRegister on it</span>
<span class="gi">+    hipDeviceAttributePageableMemoryAccessUsesHostPageTables, ///&lt; Device accesses pageable memory via the host's page tables</span>
<span class="gi">+    hipDeviceAttributePciBusId,                         ///&lt; PCI Bus ID.</span>
<span class="gi">+    hipDeviceAttributePciDeviceId,                      ///&lt; PCI Device ID.</span>
<span class="gi">+    hipDeviceAttributePciDomainID,                      ///&lt; PCI Domain ID.</span>
<span class="gi">+    hipDeviceAttributePersistingL2CacheMaxSize,         ///&lt; Cuda11 only. Maximum l2 persisting lines capacity in bytes</span>
<span class="gi">+    hipDeviceAttributeMaxRegistersPerBlock,             ///&lt; 32-bit registers available to a thread block. This number is shared</span>
<span class="gi">+                                                        ///&lt; by all thread blocks simultaneously resident on a multiprocessor.</span>
<span class="gi">+    hipDeviceAttributeMaxRegistersPerMultiprocessor,    ///&lt; 32-bit registers available per block.</span>
<span class="gi">+    hipDeviceAttributeReservedSharedMemPerBlock,        ///&lt; Cuda11 only. Shared memory reserved by CUDA driver per block.</span>
<span class="gi">+    hipDeviceAttributeMaxSharedMemoryPerBlock,          ///&lt; Maximum shared memory available per block in bytes.</span>
<span class="gi">+    hipDeviceAttributeSharedMemPerBlockOptin,           ///&lt; Cuda only. Maximum shared memory per block usable by special opt in.</span>
<span class="gi">+    hipDeviceAttributeSharedMemPerMultiprocessor,       ///&lt; Cuda only. Shared memory available per multiprocessor.</span>
<span class="gi">+    hipDeviceAttributeSingleToDoublePrecisionPerfRatio, ///&lt; Cuda only. Performance ratio of single precision to double precision.</span>
<span class="gi">+    hipDeviceAttributeStreamPrioritiesSupported,        ///&lt; Cuda only. Whether to support stream priorities.</span>
<span class="gi">+    hipDeviceAttributeSurfaceAlignment,                 ///&lt; Cuda only. Alignment requirement for surfaces</span>
<span class="gi">+    hipDeviceAttributeTccDriver,                        ///&lt; Cuda only. Whether device is a Tesla device using TCC driver</span>
<span class="gi">+    hipDeviceAttributeTextureAlignment,                 ///&lt; Alignment requirement for textures</span>
<span class="gi">+    hipDeviceAttributeTexturePitchAlignment,            ///&lt; Pitch alignment requirement for 2D texture references bound to pitched memory;</span>
<span class="gi">+    hipDeviceAttributeTotalConstantMemory,              ///&lt; Constant memory size in bytes.</span>
<span class="gi">+    hipDeviceAttributeTotalGlobalMem,                   ///&lt; Global memory available on devicice.</span>
<span class="gi">+    hipDeviceAttributeUnifiedAddressing,                ///&lt; Cuda only. An unified address space shared with the host.</span>
<span class="gi">+    hipDeviceAttributeUuid,                             ///&lt; Cuda only. Unique ID in 16 byte.</span>
<span class="gi">+    hipDeviceAttributeWarpSize,                         ///&lt; Warp size in threads.</span>

<span class="gd">-    hipDeviceAttributeMaxPitch,             ///&lt; Maximum pitch in bytes allowed by memory copies</span>
<span class="gd">-    hipDeviceAttributeTextureAlignment,     ///&lt;Alignment requirement for textures</span>
<span class="gd">-    hipDeviceAttributeTexturePitchAlignment, ///&lt;Pitch alignment requirement for 2D texture references bound to pitched memory;</span>
<span class="gd">-    hipDeviceAttributeKernelExecTimeout,    ///&lt;Run time limit for kernels executed on the device</span>
<span class="gd">-    hipDeviceAttributeCanMapHostMemory,     ///&lt;Device can map host memory into device address space</span>
<span class="gd">-    hipDeviceAttributeEccEnabled,           ///&lt;Device has ECC support enabled</span>
<span class="gi">+    hipDeviceAttributeCudaCompatibleEnd = 9999,</span>
<span class="gi">+    hipDeviceAttributeAmdSpecificBegin = 10000,</span>

<span class="gd">-    hipDeviceAttributeCooperativeMultiDeviceUnmatchedFunc,        ///&lt; Supports cooperative launch on multiple</span>
<span class="gd">-                                                                  ///devices with unmatched functions</span>
<span class="gd">-    hipDeviceAttributeCooperativeMultiDeviceUnmatchedGridDim,     ///&lt; Supports cooperative launch on multiple</span>
<span class="gd">-                                                                  ///devices with unmatched grid dimensions</span>
<span class="gd">-    hipDeviceAttributeCooperativeMultiDeviceUnmatchedBlockDim,    ///&lt; Supports cooperative launch on multiple</span>
<span class="gd">-                                                                  ///devices with unmatched block dimensions</span>
<span class="gd">-    hipDeviceAttributeCooperativeMultiDeviceUnmatchedSharedMem,   ///&lt; Supports cooperative launch on multiple</span>
<span class="gd">-                                                                  ///devices with unmatched shared memories</span>
<span class="gd">-    hipDeviceAttributeAsicRevision,         ///&lt; Revision of the GPU in this device</span>
<span class="gd">-    hipDeviceAttributeManagedMemory,        ///&lt; Device supports allocating managed memory on this system</span>
<span class="gd">-    hipDeviceAttributeDirectManagedMemAccessFromHost, ///&lt; Host can directly access managed memory on</span>
<span class="gd">-                                                      /// the device without migration</span>
<span class="gd">-    hipDeviceAttributeConcurrentManagedAccess,  ///&lt; Device can coherently access managed memory</span>
<span class="gd">-                                                /// concurrently with the CPU</span>
<span class="gd">-    hipDeviceAttributePageableMemoryAccess,     ///&lt; Device supports coherently accessing pageable memory</span>
<span class="gd">-                                                /// without calling hipHostRegister on it</span>
<span class="gd">-    hipDeviceAttributePageableMemoryAccessUsesHostPageTables, ///&lt; Device accesses pageable memory via</span>
<span class="gd">-                                                              /// the host's page tables</span>
<span class="gd">-    hipDeviceAttributeCanUseStreamWaitValue ///&lt; '1' if Device supports hipStreamWaitValue32() and</span>
<span class="gd">-                                            ///&lt; hipStreamWaitValue64() , '0' otherwise.</span>
<span class="gi">+    hipDeviceAttributeClockInstructionRate = hipDeviceAttributeAmdSpecificBegin,  ///&lt; Frequency in khz of the timer used by the device-side "clock*"</span>
<span class="gi">+    hipDeviceAttributeArch,                                     ///&lt; Device architecture</span>
<span class="gi">+    hipDeviceAttributeMaxSharedMemoryPerMultiprocessor,         ///&lt; Maximum Shared Memory PerMultiprocessor.</span>
<span class="gi">+    hipDeviceAttributeGcnArch,                                  ///&lt; Device gcn architecture</span>
<span class="gi">+    hipDeviceAttributeGcnArchName,                              ///&lt; Device gcnArch name in 256 bytes</span>
<span class="gi">+    hipDeviceAttributeHdpMemFlushCntl,                          ///&lt; Address of the HDP_MEM_COHERENCY_FLUSH_CNTL register</span>
<span class="gi">+    hipDeviceAttributeHdpRegFlushCntl,                          ///&lt; Address of the HDP_REG_COHERENCY_FLUSH_CNTL register</span>
<span class="gi">+    hipDeviceAttributeCooperativeMultiDeviceUnmatchedFunc,      ///&lt; Supports cooperative launch on multiple</span>
<span class="gi">+                                                                ///&lt; devices with unmatched functions</span>
<span class="gi">+    hipDeviceAttributeCooperativeMultiDeviceUnmatchedGridDim,   ///&lt; Supports cooperative launch on multiple</span>
<span class="gi">+                                                                ///&lt; devices with unmatched grid dimensions</span>
<span class="gi">+    hipDeviceAttributeCooperativeMultiDeviceUnmatchedBlockDim,  ///&lt; Supports cooperative launch on multiple</span>
<span class="gi">+                                                                ///&lt; devices with unmatched block dimensions</span>
<span class="gi">+    hipDeviceAttributeCooperativeMultiDeviceUnmatchedSharedMem, ///&lt; Supports cooperative launch on multiple</span>
<span class="gi">+                                                                ///&lt; devices with unmatched shared memories</span>
<span class="gi">+    hipDeviceAttributeIsLargeBar,                               ///&lt; Whether it is LargeBar</span>
<span class="gi">+    hipDeviceAttributeAsicRevision,                             ///&lt; Revision of the GPU in this device</span>
<span class="gi">+    hipDeviceAttributeCanUseStreamWaitValue,                    ///&lt; '1' if Device supports hipStreamWaitValue32() and</span>
<span class="gi">+                                                                ///&lt; hipStreamWaitValue64() , '0' otherwise.</span>

<span class="gi">+    hipDeviceAttributeAmdSpecificEnd = 19999,</span>
<span class="gi">+    hipDeviceAttributeVendorSpecificBegin = 20000,</span>
<span class="gi">+    // Extended attributes for vendors</span>
<span class="w"> </span>} hipDeviceAttribute_t;

<span class="w"> </span>enum hipComputeMode {
</pre></div>
</div>
</section>
</section>
<section id="id517">
<h3>Known issues<a class="headerlink" href="#id517" title="Link to this heading">#</a></h3>
<section id="incorrect-dgpu-behavior-when-using-amdvbflash-tool">
<h4>Incorrect dGPU behavior when using AMDVBFlash tool<a class="headerlink" href="#incorrect-dgpu-behavior-when-using-amdvbflash-tool" title="Link to this heading">#</a></h4>
<p>The AMDVBFlash tool, used for flashing the VBIOS image to dGPU, does not communicate with the
ROM Controller specifically when the driver is present. This is because the driver, as part of its runtime
power management feature, puts the dGPU to a sleep state.</p>
<p>As a workaround, users can run amdgpu.runpm=0, which temporarily disables the runtime power
management feature from the driver and dynamically changes some power control-related sysfs files.</p>
</section>
<section id="issue-with-start-timestamp-in-rocprofiler">
<h4>Issue with START timestamp in ROCProfiler<a class="headerlink" href="#issue-with-start-timestamp-in-rocprofiler" title="Link to this heading">#</a></h4>
<p>Users may encounter an issue with the enabled timestamp functionality for monitoring one or multiple
counters. ROCProfiler outputs the following four timestamps for each kernel:</p>
<ul class="simple">
<li><p>Dispatch</p></li>
<li><p>Start</p></li>
<li><p>End</p></li>
<li><p>Complete</p></li>
</ul>
<section id="id518">
<h5>Issue<a class="headerlink" href="#id518" title="Link to this heading">#</a></h5>
<p>This defect is related to the Start timestamp functionality, which incorrectly shows an earlier time than
the Dispatch timestamp.</p>
<p>To reproduce the issue,</p>
<ol class="arabic simple">
<li><p>Enable timing using the –timestamp on flag.</p></li>
<li><p>Use the -i option with the input filename that contains the name of the counter(s) to monitor.</p></li>
<li><p>Run the program.</p></li>
<li><p>Check the output result file.</p></li>
</ol>
</section>
<section id="current-behavior">
<h5>Current behavior<a class="headerlink" href="#current-behavior" title="Link to this heading">#</a></h5>
<p>BeginNS is lower than DispatchNS, which is incorrect.</p>
</section>
<section id="expected-behavior">
<h5>Expected behavior<a class="headerlink" href="#expected-behavior" title="Link to this heading">#</a></h5>
<p>The correct order is:</p>
<p>Dispatch &lt; Start &lt; End &lt; Complete</p>
<p>Users cannot use ROCProfiler to measure the time spent on each kernel because of the incorrect
timestamp with counter collection enabled.</p>
</section>
<section id="recommended-workaround">
<h5>Recommended workaround<a class="headerlink" href="#recommended-workaround" title="Link to this heading">#</a></h5>
<p>Users are recommended to collect kernel execution timestamps without monitoring counters, as
follows:</p>
<ol class="arabic simple">
<li><p>​Enable timing using the –timestamp on flag, and run the application.</p></li>
<li><p>Rerun the application using the -i option with the input filename that contains the name of the
counter(s) to monitor, and save this to a different output file using the -o flag.</p></li>
<li><p>Check the output result file from step 1.</p></li>
<li><p>The order of timestamps correctly displays as: DispatchNS &lt; BeginNS &lt; EndNS &lt; CompleteNS</p></li>
<li><p>Users can find the values of the collected counters in the output file generated in step 2.</p></li>
</ol>
</section>
</section>
<section id="id519">
<h4>Radeon Pro V620 and W6800 workstation GPUs<a class="headerlink" href="#id519" title="Link to this heading">#</a></h4>
<section id="no-support-for-smi-and-rocdebugger-on-sriov">
<h5>No support for SMI and ROCDebugger on SRIOV<a class="headerlink" href="#no-support-for-smi-and-rocdebugger-on-sriov" title="Link to this heading">#</a></h5>
<p>System Management Interface (SMI) and ROCDebugger are not supported in the SRIOV environment
on any GPU. For more information, refer to the Systems Management Interface documentation.</p>
</section>
</section>
</section>
<section id="id520">
<h3>Deprecations and warnings<a class="headerlink" href="#id520" title="Link to this heading">#</a></h3>
<section id="rocm-libraries-changes-deprecations-and-deprecation-removal">
<h4>ROCm libraries changes – deprecations and deprecation removal<a class="headerlink" href="#rocm-libraries-changes-deprecations-and-deprecation-removal" title="Link to this heading">#</a></h4>
<ul>
<li><p>The <code class="docutils literal notranslate"><span class="pre">hipFFT.h</span></code> header is now provided only by the hipFFT package. Up to ROCm 5.0, users would get
<code class="docutils literal notranslate"><span class="pre">hipFFT.h</span></code> in the rocFFT package too.</p></li>
<li><p>The GlobalPairwiseAMG class is now entirely removed, users should use the PairwiseAMG class
instead.</p></li>
<li><p>The rocsparse_spmm signature in 5.0 was changed to match that of rocsparse_spmm_ex.  In 5.0,
rocsparse_spmm_ex is still present, but deprecated. Signature diff for rocsparse_spmm
rocsparse_spmm in 5.0</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">rocsparse_status</span><span class="w"> </span><span class="nf">rocsparse_spmm</span><span class="p">(</span><span class="n">rocsparse_handle</span><span class="w">            </span><span class="n">handle</span><span class="p">,</span>
<span class="w">                                </span><span class="n">rocsparse_operation</span><span class="w">         </span><span class="n">trans_A</span><span class="p">,</span>
<span class="w">                                </span><span class="n">rocsparse_operation</span><span class="w">         </span><span class="n">trans_B</span><span class="p">,</span>
<span class="w">                                </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w">                 </span><span class="n">alpha</span><span class="p">,</span>
<span class="w">                                </span><span class="k">const</span><span class="w"> </span><span class="n">rocsparse_spmat_descr</span><span class="w"> </span><span class="n">mat_A</span><span class="p">,</span>
<span class="w">                                </span><span class="k">const</span><span class="w"> </span><span class="n">rocsparse_dnmat_descr</span><span class="w"> </span><span class="n">mat_B</span><span class="p">,</span>
<span class="w">                                </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w">                 </span><span class="n">beta</span><span class="p">,</span>
<span class="w">                                </span><span class="k">const</span><span class="w"> </span><span class="n">rocsparse_dnmat_descr</span><span class="w"> </span><span class="n">mat_C</span><span class="p">,</span>
<span class="w">                                </span><span class="n">rocsparse_datatype</span><span class="w">          </span><span class="n">compute_type</span><span class="p">,</span>
<span class="w">                                </span><span class="n">rocsparse_spmm_alg</span><span class="w">          </span><span class="n">alg</span><span class="p">,</span>
<span class="w">                                </span><span class="n">rocsparse_spmm_stage</span><span class="w">        </span><span class="n">stage</span><span class="p">,</span>
<span class="w">                                </span><span class="kt">size_t</span><span class="o">*</span><span class="w">                     </span><span class="n">buffer_size</span><span class="p">,</span>
<span class="w">                                </span><span class="kt">void</span><span class="o">*</span><span class="w">                       </span><span class="n">temp_buffer</span><span class="p">);</span>
</pre></div>
</div>
<p>rocSPARSE_spmm in 4.0</p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">rocsparse_status</span><span class="w"> </span><span class="nf">rocsparse_spmm</span><span class="p">(</span><span class="n">rocsparse_handle</span><span class="w">            </span><span class="n">handle</span><span class="p">,</span>
<span class="w">                                </span><span class="n">rocsparse_operation</span><span class="w">         </span><span class="n">trans_A</span><span class="p">,</span>
<span class="w">                                </span><span class="n">rocsparse_operation</span><span class="w">         </span><span class="n">trans_B</span><span class="p">,</span>
<span class="w">                                </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w">                 </span><span class="n">alpha</span><span class="p">,</span>
<span class="w">                                </span><span class="k">const</span><span class="w"> </span><span class="n">rocsparse_spmat_descr</span><span class="w"> </span><span class="n">mat_A</span><span class="p">,</span>
<span class="w">                                </span><span class="k">const</span><span class="w"> </span><span class="n">rocsparse_dnmat_descr</span><span class="w"> </span><span class="n">mat_B</span><span class="p">,</span>
<span class="w">                                </span><span class="k">const</span><span class="w"> </span><span class="kt">void</span><span class="o">*</span><span class="w">                 </span><span class="n">beta</span><span class="p">,</span>
<span class="w">                                </span><span class="k">const</span><span class="w"> </span><span class="n">rocsparse_dnmat_descr</span><span class="w"> </span><span class="n">mat_C</span><span class="p">,</span>
<span class="w">                                </span><span class="n">rocsparse_datatype</span><span class="w">          </span><span class="n">compute_type</span><span class="p">,</span>
<span class="w">                                </span><span class="n">rocsparse_spmm_alg</span><span class="w">          </span><span class="n">alg</span><span class="p">,</span>
<span class="w">                                </span><span class="kt">size_t</span><span class="o">*</span><span class="w">                     </span><span class="n">buffer_size</span><span class="p">,</span>
<span class="w">                                </span><span class="kt">void</span><span class="o">*</span><span class="w">                       </span><span class="n">temp_buffer</span><span class="p">);</span>
</pre></div>
</div>
</li>
</ul>
</section>
<section id="hip-api-deprecations-and-warnings">
<h4>HIP API deprecations and warnings<a class="headerlink" href="#hip-api-deprecations-and-warnings" title="Link to this heading">#</a></h4>
<section id="warning-arithmetic-operators-of-hip-complex-and-vector-types">
<h5>Warning - arithmetic operators of HIP complex and vector types<a class="headerlink" href="#warning-arithmetic-operators-of-hip-complex-and-vector-types" title="Link to this heading">#</a></h5>
<p>In this release, arithmetic operators of HIP complex and vector types are deprecated.</p>
<ul class="simple">
<li><p>As alternatives to arithmetic operators of HIP complex types, users can use arithmetic operators of
<code class="docutils literal notranslate"><span class="pre">std::complex</span></code> types.</p></li>
<li><p>As alternatives to arithmetic operators of HIP vector types, users can use the operators of the native
clang vector type associated with the data member of HIP vector types.</p></li>
</ul>
<p>During the deprecation, two macros <code class="docutils literal notranslate"><span class="pre">_HIP_ENABLE_COMPLEX_OPERATORS</span></code> and
<code class="docutils literal notranslate"><span class="pre">_HIP_ENABLE_VECTOR_OPERATORS</span></code> are provided to allow users to conditionally enable arithmetic
operators of HIP complex or vector types.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The two macros are mutually exclusive and, by default, set to Off.</p>
</div>
<p>The arithmetic operators of HIP complex and vector types will be removed in a future release.</p>
<p>Refer to the HIP API Guide for more information.</p>
</section>
</section>
<section id="warning-compiler-generated-code-object-version-4-deprecation">
<h4>Warning - compiler-generated code object version 4 deprecation<a class="headerlink" href="#warning-compiler-generated-code-object-version-4-deprecation" title="Link to this heading">#</a></h4>
<p>Support for loading compiler-generated code object version 4 will be deprecated in a future release
with no release announcement and replaced with code object 5 as the default version.</p>
<p>The current default is code object version 4.</p>
</section>
<section id="warning-miopentensile-deprecation">
<h4>Warning - MIOpenTensile deprecation<a class="headerlink" href="#warning-miopentensile-deprecation" title="Link to this heading">#</a></h4>
<p>MIOpenTensile will be deprecated in a future release.</p>
</section>
</section>
<section id="library-changes-in-rocm-5-0-0">
<h3>Library changes in ROCM 5.0.0<a class="headerlink" href="#library-changes-in-rocm-5-0-0" title="Link to this heading">#</a></h3>
<div class="pst-scrollable-table-container"><table class="table">
<thead>
<tr class="row-odd"><th class="head"><p>Library</p></th>
<th class="head"><p>Version</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>hipBLAS</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-5.0.0">0.49.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipCUB</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/hipCUB/releases/tag/rocm-5.0.0">2.10.13</a></p></td>
</tr>
<tr class="row-even"><td><p>hipFFT</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/hipFFT/releases/tag/rocm-5.0.0">1.0.4</a></p></td>
</tr>
<tr class="row-odd"><td><p>hipSOLVER</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-5.0.0">1.2.0</a></p></td>
</tr>
<tr class="row-even"><td><p>hipSPARSE</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-5.0.0">2.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rccl</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/rccl/releases/tag/rocm-5.0.0">2.10.3</a></p></td>
</tr>
<tr class="row-even"><td><p>rocALUTION</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-5.0.0">2.0.1</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocBLAS</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-5.0.0">2.42.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocFFT</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/rocFFT/releases/tag/rocm-5.0.0">1.0.13</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocPRIM</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-5.0.0">2.10.12</a></p></td>
</tr>
<tr class="row-even"><td><p>rocRAND</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/rocRAND/releases/tag/rocm-5.0.0">2.10.12</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocSOLVER</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-5.0.0">3.16.0</a></p></td>
</tr>
<tr class="row-even"><td><p>rocSPARSE</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-5.0.0">2.0.0</a></p></td>
</tr>
<tr class="row-odd"><td><p>rocThrust</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/rocThrust/releases/tag/rocm-5.0.0">2.13.0</a></p></td>
</tr>
<tr class="row-even"><td><p>Tensile</p></td>
<td><p>⇒ <a class="reference external" href="https://github.com/ROCm/Tensile/releases/tag/rocm-5.0.0">4.31.0</a></p></td>
</tr>
</tbody>
</table>
</div>
<section id="hipblas-0-49-0">
<h4>hipBLAS 0.49.0<a class="headerlink" href="#hipblas-0-49-0" title="Link to this heading">#</a></h4>
<p>hipBLAS 0.49.0 for ROCm 5.0.0</p>
<section id="id521">
<h5>Added<a class="headerlink" href="#id521" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added rocSOLVER functions to hipblas-bench</p></li>
<li><p>Added option ROCM_MATHLIBS_API_USE_HIP_COMPLEX to opt-in to use hipFloatComplex and hipDoubleComplex</p></li>
<li><p>Added compilation warning for future trmm changes</p></li>
<li><p>Added documentation to hipblas.h</p></li>
<li><p>Added option to forgo pivoting for getrf and getri when ipiv is nullptr</p></li>
<li><p>Added code coverage option</p></li>
</ul>
</section>
<section id="id522">
<h5>Fixed<a class="headerlink" href="#id522" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed use of incorrect ‘HIP_PATH’ when building from source.</p></li>
<li><p>Fixed windows packaging</p></li>
<li><p>Allowing negative increments in hipblas-bench</p></li>
<li><p>Removed boost dependency</p></li>
</ul>
</section>
</section>
<section id="hipcub-2-10-13">
<h4>hipCUB 2.10.13<a class="headerlink" href="#hipcub-2-10-13" title="Link to this heading">#</a></h4>
<p>hipCUB 2.10.13 for ROCm 5.0.0</p>
<section id="id523">
<h5>Fixed<a class="headerlink" href="#id523" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added missing includes to hipcub.hpp</p></li>
</ul>
</section>
<section id="id524">
<h5>Added<a class="headerlink" href="#id524" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Bfloat16 support to test cases (device_reduce &amp; device_radix_sort)</p></li>
<li><p>Device merge sort</p></li>
<li><p>Block merge sort</p></li>
<li><p>API update to CUB 1.14.0</p></li>
</ul>
</section>
<section id="id525">
<h5>Changed<a class="headerlink" href="#id525" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The SetupNVCC.cmake automatic target selector select all of the capabalities of all available card for NVIDIA backend.</p></li>
</ul>
</section>
</section>
<section id="hipfft-1-0-4">
<h4>hipFFT 1.0.4<a class="headerlink" href="#hipfft-1-0-4" title="Link to this heading">#</a></h4>
<p>hipFFT 1.0.4 for ROCm 5.0.0</p>
<section id="id526">
<h5>Fixed<a class="headerlink" href="#id526" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Add calls to rocFFT setup/cleanup.</p></li>
<li><p>Cmake fixes for clients and backend support.</p></li>
</ul>
</section>
<section id="id527">
<h5>Added<a class="headerlink" href="#id527" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added support for Windows 10 as a build target.</p></li>
</ul>
</section>
</section>
<section id="hipsolver-1-2-0">
<h4>hipSOLVER 1.2.0<a class="headerlink" href="#hipsolver-1-2-0" title="Link to this heading">#</a></h4>
<p>hipSOLVER 1.2.0 for ROCm 5.0.0</p>
<section id="id528">
<h5>Added<a class="headerlink" href="#id528" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added functions</p>
<ul>
<li><p>sytrf</p>
<ul>
<li><p>hipsolverSsytrf_bufferSize, hipsolverDsytrf_bufferSize, hipsolverCsytrf_bufferSize, hipsolverZsytrf_bufferSize</p></li>
<li><p>hipsolverSsytrf, hipsolverDsytrf, hipsolverCsytrf, hipsolverZsytrf</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</section>
<section id="id529">
<h5>Fixed<a class="headerlink" href="#id529" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fixed use of incorrect <code class="docutils literal notranslate"><span class="pre">HIP_PATH</span></code> when building from source (#40).
Thanks <a class="reference external" href="https://github.com/jakub329homola">@jakub329homola</a>!</p></li>
</ul>
</section>
</section>
<section id="hipsparse-2-0-0">
<h4>hipSPARSE 2.0.0<a class="headerlink" href="#hipsparse-2-0-0" title="Link to this heading">#</a></h4>
<p>hipSPARSE 2.0.0 for ROCm 5.0.0</p>
<section id="id530">
<h5>Added<a class="headerlink" href="#id530" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added (conjugate) transpose support for csrmv, hybmv and spmv routines</p></li>
</ul>
</section>
</section>
<section id="rccl-2-10-3">
<h4>rccl 2.10.3<a class="headerlink" href="#rccl-2-10-3" title="Link to this heading">#</a></h4>
<p>RCCL 2.10.3 for ROCm 5.0.0</p>
<section id="id531">
<h5>Added<a class="headerlink" href="#id531" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Compatibility with NCCL 2.10.3</p></li>
</ul>
</section>
<section id="id532">
<h5>Known Issues<a class="headerlink" href="#id532" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Managed memory is not currently supported for clique-based kernels</p></li>
</ul>
</section>
</section>
<section id="rocalution-2-0-1">
<h4>rocALUTION 2.0.1<a class="headerlink" href="#rocalution-2-0-1" title="Link to this heading">#</a></h4>
<p>rocALUTION 2.0.1 for ROCm 5.0.0</p>
<section id="id533">
<h5>Changed<a class="headerlink" href="#id533" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Removed deprecated GlobalPairwiseAMG class, please use PairwiseAMG instead.</p></li>
<li><p>Changed to C++ 14 Standard</p></li>
</ul>
</section>
<section id="id534">
<h5>Improved<a class="headerlink" href="#id534" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added sanitizer option</p></li>
<li><p>Improved documentation</p></li>
</ul>
</section>
</section>
<section id="rocblas-2-42-0">
<h4>rocBLAS 2.42.0<a class="headerlink" href="#rocblas-2-42-0" title="Link to this heading">#</a></h4>
<p>rocBLAS 2.42.0 for ROCm 5.0.0</p>
<section id="id535">
<h5>Added<a class="headerlink" href="#id535" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added rocblas_get_version_string_size convenience function</p></li>
<li><p>Added rocblas_xtrmm_outofplace, an out-of-place version of rocblas_xtrmm</p></li>
<li><p>Added hpl and trig initialization for gemm_ex to rocblas-bench</p></li>
<li><p>Added source code gemm. It can be used as an alternative to Tensile for debugging and development</p></li>
<li><p>Added option ROCM_MATHLIBS_API_USE_HIP_COMPLEX to opt-in to use hipFloatComplex and hipDoubleComplex</p></li>
</ul>
</section>
<section id="id536">
<h5>Optimizations<a class="headerlink" href="#id536" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved performance of non-batched and batched single-precision GER for size m &gt; 1024. Performance enhanced by 5-10% measured on a MI100 (gfx908) GPU.</p></li>
<li><p>Improved performance of non-batched and batched HER for all sizes and data types. Performance enhanced by 2-17% measured on a MI100 (gfx908) GPU.</p></li>
</ul>
</section>
<section id="id537">
<h5>Changed<a class="headerlink" href="#id537" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Instantiate templated rocBLAS functions to reduce size of librocblas.so</p></li>
<li><p>Removed static library dependency on msgpack</p></li>
<li><p>Removed boost dependencies for clients</p></li>
</ul>
</section>
<section id="id538">
<h5>Fixed<a class="headerlink" href="#id538" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Option to install script to build only rocBLAS clients with a pre-built rocBLAS library</p></li>
<li><p>Correctly set output of nrm2_batched_ex and nrm2_strided_batched_ex when given bad input</p></li>
<li><p>Fix for dgmm with side == rocblas_side_left and a negative incx</p></li>
<li><p>Fixed out-of-bounds read for small trsm</p></li>
<li><p>Fixed numerical checking for tbmv_strided_batched</p></li>
</ul>
</section>
</section>
<section id="rocfft-1-0-13">
<h4>rocFFT 1.0.13<a class="headerlink" href="#rocfft-1-0-13" title="Link to this heading">#</a></h4>
<p>rocFFT 1.0.13 for ROCm 5.0.0</p>
<section id="id539">
<h5>Optimizations<a class="headerlink" href="#id539" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved many plans by removing unnecessary transpose steps.</p></li>
<li><p>Optimized scheme selection for 3D problems.</p>
<ul>
<li><p>Imposed less restrictions on 3D_BLOCK_RC selection. More problems can use 3D_BLOCK_RC and
have some performance gain.</p></li>
<li><p>Enabled 3D_RC. Some 3D problems with SBCC-supported z-dim can use less kernels and get benefit.</p></li>
<li><p>Force –length 336 336 56 (dp) use faster 3D_RC to avoid it from being skipped by conservative
threshold test.</p></li>
</ul>
</li>
<li><p>Optimized some even-length R2C/C2R cases by doing more operations
in-place and combining pre/post processing into Stockham kernels.</p></li>
<li><p>Added radix-17.</p></li>
</ul>
</section>
<section id="id540">
<h5>Added<a class="headerlink" href="#id540" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added new kernel generator for select fused-2D transforms.</p></li>
</ul>
</section>
<section id="id541">
<h5>Fixed<a class="headerlink" href="#id541" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved large 1D transform decompositions.</p></li>
</ul>
</section>
</section>
<section id="rocprim-2-10-12">
<h4>rocPRIM 2.10.12<a class="headerlink" href="#rocprim-2-10-12" title="Link to this heading">#</a></h4>
<p>rocPRIM 2.10.12 for ROCm 5.0.0</p>
<section id="id542">
<h5>Fixed<a class="headerlink" href="#id542" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Enable bfloat16 tests and reduce threshold for bfloat16</p></li>
<li><p>Fix device scan limit_size feature</p></li>
<li><p>Non-optimized builds no longer trigger local memory limit errors</p></li>
</ul>
</section>
<section id="id543">
<h5>Added<a class="headerlink" href="#id543" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added scan size limit feature</p></li>
<li><p>Added reduce size limit feature</p></li>
<li><p>Added transform size limit feature</p></li>
<li><p>Add block_load_striped and block_store_striped</p></li>
<li><p>Add gather_to_blocked to gather values from other threads into a blocked arrangement</p></li>
<li><p>The block sizes for device merge sorts initial block sort and its merge steps are now separate in its kernel config</p>
<ul>
<li><p>the block sort step supports multiple items per thread</p></li>
</ul>
</li>
</ul>
</section>
<section id="id544">
<h5>Changed<a class="headerlink" href="#id544" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>size_limit for scan, reduce and transform can now be set in the config struct instead of a parameter</p></li>
<li><p>Device_scan and device_segmented_scan: <code class="docutils literal notranslate"><span class="pre">inclusive_scan</span></code> now uses the input-type as accumulator-type, <code class="docutils literal notranslate"><span class="pre">exclusive_scan</span></code> uses initial-value-type.</p>
<ul>
<li><p>This particularly changes behaviour of small-size input types with large-size output types (e.g. <code class="docutils literal notranslate"><span class="pre">short</span></code> input, <code class="docutils literal notranslate"><span class="pre">int</span></code> output).</p></li>
<li><p>And low-res input with high-res output (e.g. <code class="docutils literal notranslate"><span class="pre">float</span></code> input, <code class="docutils literal notranslate"><span class="pre">double</span></code> output)</p></li>
</ul>
</li>
<li><p>Revert old Fiji workaround, because they solved the issue at compiler side</p></li>
<li><p>Update README cmake minimum version number</p></li>
<li><p>Block sort support multiple items per thread</p>
<ul>
<li><p>currently only powers of two block sizes, and items per threads are supported and only for full blocks</p></li>
</ul>
</li>
<li><p>Bumped the minimum required version of CMake to 3.16</p></li>
</ul>
</section>
<section id="id545">
<h5>Known Issues<a class="headerlink" href="#id545" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Unit tests may soft hang on MI200 when running in hipMallocManaged mode.</p></li>
<li><p>device_segmented_radix_sort, device_scan unit tests failing for HIP on Windows</p></li>
<li><p>ReduceEmptyInput cause random faulire with bfloat16</p></li>
</ul>
</section>
</section>
<section id="rocrand-2-10-12">
<h4>rocRAND 2.10.12<a class="headerlink" href="#rocrand-2-10-12" title="Link to this heading">#</a></h4>
<p>rocRAND 2.10.12 for ROCm 5.0.0</p>
<section id="id546">
<h5>Changed<a class="headerlink" href="#id546" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>No updates or changes for ROCm 5.0.0.</p></li>
</ul>
</section>
</section>
<section id="rocsolver-3-16-0">
<h4>rocSOLVER 3.16.0<a class="headerlink" href="#rocsolver-3-16-0" title="Link to this heading">#</a></h4>
<p>rocSOLVER 3.16.0 for ROCm 5.0.0</p>
<section id="id547">
<h5>Added<a class="headerlink" href="#id547" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Symmetric matrix factorizations:</p>
<ul>
<li><p>LASYF</p></li>
<li><p>SYTF2, SYTRF (with batched and strided_batched versions)</p></li>
</ul>
</li>
<li><p>Added <code class="docutils literal notranslate"><span class="pre">rocsolver_get_version_string_size</span></code> to help with version string queries</p></li>
<li><p>Added <code class="docutils literal notranslate"><span class="pre">rocblas_layer_mode_ex</span></code> and the ability to print kernel calls in the trace and profile logs</p></li>
<li><p>Expanded batched and strided_batched sample programs.</p></li>
</ul>
</section>
<section id="id548">
<h5>Optimized<a class="headerlink" href="#id548" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Improved general performance of LU factorization</p></li>
<li><p>Increased parallelism of specialized kernels when compiling from source, reducing build times on multi-core systems.</p></li>
</ul>
</section>
<section id="id549">
<h5>Changed<a class="headerlink" href="#id549" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The rocsolver-test client now prints the rocSOLVER version used to run the tests,
rather than the version used to build them</p></li>
<li><p>The rocsolver-bench client now prints the rocSOLVER version used in the benchmark</p></li>
</ul>
</section>
<section id="id550">
<h5>Fixed<a class="headerlink" href="#id550" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Added missing stdint.h include to rocsolver.h</p></li>
</ul>
</section>
</section>
<section id="rocsparse-2-0-0">
<h4>rocSPARSE 2.0.0<a class="headerlink" href="#rocsparse-2-0-0" title="Link to this heading">#</a></h4>
<p>rocSPARSE 2.0.0 for ROCm 5.0.0</p>
<section id="id551">
<h5>Added<a class="headerlink" href="#id551" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>csrmv, coomv, ellmv, hybmv for (conjugate) transposed matrices</p></li>
<li><p>csrmv for symmetric matrices</p></li>
</ul>
</section>
<section id="id552">
<h5>Changed<a class="headerlink" href="#id552" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>spmm_ex is now deprecated and will be removed in the next major release</p></li>
</ul>
</section>
<section id="id553">
<h5>Improved<a class="headerlink" href="#id553" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimization for gtsv</p></li>
</ul>
</section>
</section>
<section id="rocthrust-2-13-0">
<h4>rocThrust 2.13.0<a class="headerlink" href="#rocthrust-2-13-0" title="Link to this heading">#</a></h4>
<p>rocThrust 2.13.0 for ROCm 5.0.0</p>
<section id="id554">
<h5>Added<a class="headerlink" href="#id554" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Updated to match upstream Thrust 1.13.0</p></li>
<li><p>Updated to match upstream Thrust 1.14.0</p></li>
<li><p>Added async scan</p></li>
</ul>
</section>
<section id="id555">
<h5>Changed<a class="headerlink" href="#id555" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Scan algorithms: <code class="docutils literal notranslate"><span class="pre">inclusive_scan</span></code> now uses the input-type as accumulator-type, <code class="docutils literal notranslate"><span class="pre">exclusive_scan</span></code> uses initial-value-type.</p>
<ul>
<li><p>This particularly changes behaviour of small-size input types with large-size output types (e.g. <code class="docutils literal notranslate"><span class="pre">short</span></code> input, <code class="docutils literal notranslate"><span class="pre">int</span></code> output).</p></li>
<li><p>And low-res input with high-res output (e.g. <code class="docutils literal notranslate"><span class="pre">float</span></code> input, <code class="docutils literal notranslate"><span class="pre">double</span></code> output)</p></li>
</ul>
</li>
</ul>
</section>
</section>
<section id="tensile-4-31-0">
<h4>Tensile 4.31.0<a class="headerlink" href="#tensile-4-31-0" title="Link to this heading">#</a></h4>
<p>Tensile 4.31.0 for ROCm 5.0.0</p>
<section id="id556">
<h5>Added<a class="headerlink" href="#id556" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>DirectToLds support (x2/x4)</p></li>
<li><p>DirectToVgpr support for DGEMM</p></li>
<li><p>Parameter to control number of files kernels are merged into to better parallelize kernel compilation</p></li>
<li><p>FP16 alternate implementation for HPA HGEMM on aldebaran</p></li>
</ul>
</section>
<section id="id557">
<h5>Optimized<a class="headerlink" href="#id557" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Add DGEMM NN custom kernel for HPL on aldebaran</p></li>
</ul>
</section>
<section id="id558">
<h5>Changed<a class="headerlink" href="#id558" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Update tensile_client executable to std=c++14</p></li>
</ul>
</section>
<section id="id559">
<h5>Removed<a class="headerlink" href="#id559" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Remove unused old Tensile client code</p></li>
</ul>
</section>
<section id="id560">
<h5>Fixed<a class="headerlink" href="#id560" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Fix hipErrorInvalidHandle during benchmarks</p></li>
<li><p>Fix addrVgpr for atomic GSU</p></li>
<li><p>Fix for Python 3.8: add case for Constant nodeType</p></li>
<li><p>Fix architecture mapping for gfx1011 and gfx1012</p></li>
<li><p>Fix PrintSolutionRejectionReason verbiage in KernelWriter.py</p></li>
<li><p>Fix vgpr alignment problem when enabling flat buffer load</p></li>
</ul>
</section>
</section>
</section>
</section>
</section>
</article>
<footer class="prev-next-footer d-print-none">
<div class="prev-next-area">
<a class="left-prev" href="release-notes.html" title="previous page">
<i class="fa-solid fa-angle-left"></i>
<div class="prev-next-info">
<p class="prev-next-subtitle">previous</p>
<p class="prev-next-title">Release notes for AMD ROCm™ 6.0</p>
</div>
</a>
<a class="right-next" href="../reference/library-index.html" title="next page">
<div class="prev-next-info">
<p class="prev-next-subtitle">next</p>
<p class="prev-next-title">ROCm API libraries &amp; tools</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-6-0-0">ROCm 6.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#os-and-gpu-support-changes">OS and GPU support changes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#new-rocm-meta-package">New ROCm meta package</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#filesystem-hierarchy-standard">Filesystem Hierarchy Standard</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#compiler-location-change">Compiler location change</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#documentation">Documentation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi50-end-of-support-notice">AMD Instinct™ MI50 end-of-support notice</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#known-issues">Known issues</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes">Library changes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amdmigraphx-2-8">AMDMIGraphX 2.8</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#additions">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#optimizations">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#fixes">Fixes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#changes">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#removals">Removals</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-smi">AMD SMI</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-6-0-0">HIP 6.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id2">Changes</a><ul class="nav section-nav flex-column">
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#changes-impacting-backward-incompatibility">Changes impacting backward incompatibility</a></li>
</ul>
</li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id3">Fixes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id4">Removals</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-2-0-0">hipBLAS 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id5">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#deprecations">Deprecations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id6">Removals</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-3-0-0">hipCUB 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id7">Changes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-13">hipFFT 1.0.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id8">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id9">Additions</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-2-0-0">hipSOLVER 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id10">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id11">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id12">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-3-0-0">hipSPARSE 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id13">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id14">Changes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hiptensor-1-1-0">hipTensor 1.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id15">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id16">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id17">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#miopen-2-19-0">MIOpen 2.19.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id18">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id19">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id20">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#mivisionx">MIVisionX</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#openmp">OpenMP</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id21">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id22">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id23">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-2-15-5">rccl 2.15.5</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id24">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id25">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id26">Fixes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id27">Removals</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-3-0-3">rocALUTION 3.0.3</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id28">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id29">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id30">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id31">Removals</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id32">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-4-0-0">rocBLAS 4.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id33">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id34">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id35">Deprecations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id36">Removals</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id37">Fixes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id38">Changes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-25">rocFFT 1.0.25</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id39">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id40">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id41">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id42">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocgdb-13-2">ROCgdb 13.2</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id43">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id44">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id45">Known issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-cmake-0-11-0">rocm-cmake 0.11.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id46">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id47">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-compiler">ROCm Compiler</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-3-0-0">rocPRIM 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id48">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id49">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id50">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#roc-profiler-2-0-0">Roc Profiler 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id51">Additions</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-2-10-17">rocRAND 2.10.17</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id52">Changes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id53">Optimizations</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id54">Removals</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id55">Fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-24-0">rocSOLVER 3.24.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id56">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id57">Changes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-3-0-2">rocSPARSE 3.0.2</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id58">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id59">Removals</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id60">Fixes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id61">Additions</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-3-0-0">rocThrust 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id62">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id63">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id64">Known issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-1-3-0">rocWMMA 1.3.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id65">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id66">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id67">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-39-0">Tensile 4.39.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id68">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id69">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id70">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id71">Fixes</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-6-0-0">Library changes in ROCM 6.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id72">AMDMIGraphX 2.8</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id73">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id74">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id75">Fixes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id76">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id77">Removals</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id78">hipBLAS 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#added">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#deprecated">Deprecated</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#removed">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id79">hipCUB 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#changed">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id80">hipFFT 1.0.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id81">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id82">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hiprand-2-10-17">hipRAND 2.10.17</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#fixed">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id83">hipSOLVER 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id84">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id85">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id86">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id87">hipSPARSE 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id88">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id89">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id90">hipTensor 1.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id91">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id92">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id93">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id94">rocALUTION 3.0.3</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id95">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#optimized">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id96">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id97">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id98">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id99">rocBLAS 4.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id100">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id101">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id102">Deprecated</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id103">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id104">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id105">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id106">rocFFT 1.0.25</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id107">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id108">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id109">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id110">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id111">rocm-cmake 0.11.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id112">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id113">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id114">rocPRIM 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id115">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id116">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id117">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id118">rocSOLVER 3.24.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id119">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id120">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id121">rocSPARSE 3.0.2</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id122">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id123">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id124">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id125">Deprecated</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id126">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id127">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id128">rocThrust 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id129">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id130">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id131">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id132">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id133">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id134">rocWMMA 1.3.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id135">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id136">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id137">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id138">Tensile 4.39.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id139">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id140">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id141">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id142">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-7-1">ROCm 5.7.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#what-s-new-in-this-release">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#installing-all-gpu-addresssanitizer-packages-with-a-single-command">Installing all GPU AddressSanitizer packages with a single command</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-libraries">ROCm libraries</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas">rocBLAS</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-5-7-1-for-rocm-5-7-1">HIP 5.7.1 (for ROCm 5.7.1)</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#defect-fixes">Defect fixes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-7-1">Library changes in ROCM 5.7.1</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-8-2">hipSOLVER 1.8.2</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id143">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-7-0">ROCm 5.7.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#release-highlights-for-rocm-5-7">Release highlights for ROCm 5.7</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id144">AMD Instinct™ MI50 end-of-support notice</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#feature-updates">Feature updates</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#non-hostcall-hip-printf">Non-hostcall HIP printf</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#beta-release-of-llvm-addresssanitizer-asan-with-the-gpu">Beta release of LLVM AddressSanitizer (ASan) with the GPU</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id145">Defect fixes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-5-7-0">HIP 5.7.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id146">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id147">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id148">Changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id149">Fixes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id150">Known issues</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#upcoming-changes-for-hip-in-rocm-6-0-release">Upcoming changes for HIP in ROCm 6.0 release</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-7-0">Library changes in ROCM 5.7.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amdmigraphx-2-7">AMDMIGraphX 2.7</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id151">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id152">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id153">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id154">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id155">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-1-1-0">hipBLAS 1.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id156">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#dependencies">Dependencies</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-8-1">hipSOLVER 1.8.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id157">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-3-8">hipSPARSE 2.3.8</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#improved">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-1-11">rocALUTION 2.1.11</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id158">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id159">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-3-1-0">rocBLAS 3.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id160">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id161">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id162">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id163">Deprecated</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id164">Dependencies</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-24">rocFFT 1.0.24</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id165">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id166">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id167">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-cmake-0-10-0">rocm-cmake 0.10.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id168">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-13-1">rocPRIM 2.13.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id169">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id170">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-23-0">rocSOLVER 3.23.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id171">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id172">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id173">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-5-4">rocSPARSE 2.5.4</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id174">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id175">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id176">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-1-2-0">rocWMMA 1.2.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id177">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-38-0">Tensile 4.38.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id178">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id179">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id180">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id181">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-6-1">ROCm 5.6.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id182">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-5-6-1-for-rocm-5-6-1">HIP 5.6.1 (for ROCm 5.6.1)</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id183">Defect fixes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-6-1">Library changes in ROCM 5.6.1</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-3-7">hipSPARSE 2.3.7</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#bugfix">Bugfix</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-6-0">ROCm 5.6.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#release-highlights">Release highlights</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id184">OS and GPU support changes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amdsmi-cli-23-0-0-4">AMDSMI CLI 23.0.0.4</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id185">Additions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id186">Known issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-modules-dkms">Kernel modules (DKMS)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id187">Fixes</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-5-6-for-rocm-5-6">HIP 5.6 (for ROCm 5.6)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id188">Optimizations</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id189">Additions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id190">Changes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id191">Fixes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id192">Known issues</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#upcoming-changes-in-future-release">Upcoming changes in future release</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocgdb-13-for-rocm-5-6-0">ROCgdb-13 (For ROCm 5.6.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id193">Optimizations</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id194">Known issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprofiler-for-rocm-5-6-0">ROCprofiler (for ROCm 5.6.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id195">Optimizations</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id196">Additions</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id197">Fixes</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-6-0">Library changes in ROCM 5.6.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-12">hipFFT 1.0.12</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id198">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id199">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-8-0">hipSOLVER 1.8.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id200">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-3-6">hipSPARSE 2.3.6</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id201">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id202">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-1-9">rocALUTION 2.1.9</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id203">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-3-0-0">rocBLAS 3.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id204">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id205">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id206">Deprecated</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id207">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id208">Dependencies</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id209">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id210">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-23">rocFFT 1.0.23</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id211">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id212">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id213">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-cmake-0-9-0">rocm-cmake 0.9.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id214">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-22-0">rocSOLVER 3.22.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id215">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id216">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id217">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-5-2">rocSPARSE 2.5.2</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id218">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-2-18-0">rocThrust 2.18.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id219">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id220">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-1-1-0">rocWMMA 1.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id221">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id222">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-37-0">Tensile 4.37.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id223">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id224">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id225">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id226">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-5-1">ROCm 5.5.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id227">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-sdk-for-windows">HIP SDK for Windows</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-api-change">HIP API change</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#hipdevicesetcacheconfig"><code class="docutils literal notranslate"><span class="pre">hipDeviceSetCacheConfig</span></code></a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-5-1">Library changes in ROCM 5.5.1</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-5-0">ROCm 5.5.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id228">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-enhancements">HIP enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#enhanced-stack-size-limit">Enhanced stack size limit</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcc-changes"><code class="docutils literal notranslate"><span class="pre">hipcc</span></code> changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#future-changes">Future changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#new-hip-apis-in-this-release">New HIP APIs in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-management-hip-apis">Memory management HIP APIs</a></li>
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#module-management-hip-apis">Module management HIP APIs</a></li>
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-graph-management-apis">HIP graph management APIs</a></li>
</ul>
</li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#openmp-enhancements">OpenMP enhancements</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#deprecations-and-warnings">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-deprecation">HIP deprecation</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#linux-file-system-hierarchy-standard-for-rocm">Linux file system hierarchy standard for ROCm</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#new-file-system-hierarchy">New file system hierarchy</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#backward-compatibility-with-older-file-systems">Backward compatibility with older file systems</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#wrapper-header-files">Wrapper header files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#library-files">Library files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#cmake-config-files">CMake config files</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-support-for-code-object-v3-deprecated">ROCm support for Code Object V3 deprecated</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#comgr-v3-0-changes">Comgr V3.0 changes</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#api-changes">API changes</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#actions-and-data-types">Actions and data types</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#deprecated-environment-variables">Deprecated environment variables</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#known-issues-in-this-release">Known issues in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#distributed-test-distributed-spawn-fails"><code class="docutils literal notranslate"><span class="pre">DISTRIBUTED</span></code>/<code class="docutils literal notranslate"><span class="pre">TEST_DISTRIBUTED_SPAWN</span></code> fails</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-5-0">Library changes in ROCM 5.5.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amdmigraphx-2-5">AMDMIGraphX 2.5</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id229">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id230">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id231">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id232">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-0-54-0">hipBLAS 0.54.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id233">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id234">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id235">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-2-13-1">hipCUB 2.13.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id236">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id237">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id238">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id239">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-11">hipFFT 1.0.11</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id240">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hiprand-2-10-16">hipRAND 2.10.16</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id241">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id242">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-7-0">hipSOLVER 1.7.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id243">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-3-5">hipSPARSE 2.3.5</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id244">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id245">MIOpen 2.19.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id246">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id247">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id248">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id249">rccl 2.15.5</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id250">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id251">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id252">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id253">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-1-8">rocALUTION 2.1.8</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id254">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id255">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id256">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-2-47-0">rocBLAS 2.47.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id257">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id258">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id259">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id260">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id261">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-22">rocFFT 1.0.22</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id262">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id263">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id264">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id265">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-cmake-0-8-1">rocm-cmake 0.8.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id266">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id267">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-13-0">rocPRIM 2.13.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id268">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id269">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id270">Known Issues</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id271">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id272">rocRAND 2.10.17</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id273">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id274">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id275">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-21-0">rocSOLVER 3.21.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id276">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id277">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id278">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id279">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-5-1">rocSPARSE 2.5.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id280">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id281">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id282">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-1-0">rocWMMA 1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id283">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id284">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-36-0">Tensile 4.36.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id285">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id286">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id287">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id288">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-4-3">ROCm 5.4.3</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id289">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-perl-scripts-deprecation">HIP Perl scripts deprecation</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id290">Linux file system hierarchy standard for ROCm</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id291">New file system hierarchy</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id292">Backward compatibility with older file systems</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id293">Wrapper header files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id294">Library files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id295">CMake config files</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id296">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#compiler-improvements">Compiler improvements</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id297">Known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#compiler-option-error-at-runtime">Compiler option error at runtime</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-4-3">Library changes in ROCM 5.4.3</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-21">rocFFT 1.0.21</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id298">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-4-2">ROCm 5.4.2</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id299">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id300">HIP Perl scripts deprecation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcc-options-deprecation"><code class="docutils literal notranslate"><span class="pre">hipcc</span></code> options deprecation</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id301">Known issues</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-4-2">Library changes in ROCM 5.4.2</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-4-1">ROCm 5.4.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id302">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id303">HIP enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#new-hip-api-hiplaunchhostfunc">New HIP API - hipLaunchHostFunc</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id304">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id305">HIP Perl scripts deprecation</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#ifwi-fixes">IFWI fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi200-firmware-ifwi-maintenance-update-3">AMD Instinct™ MI200 firmware IFWI maintenance update #3</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi200-sriov-virtualization-support">AMD Instinct™ MI200 SRIOV virtualization support</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-4-1">Library changes in ROCM 5.4.1</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-20">rocFFT 1.0.20</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id306">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-4-0">ROCm 5.4.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id307">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id308">HIP enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#support-for-wall-clock64">Support for wall_clock64</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#new-registry-added-for-gpu-max-hw-queues">New registry added for GPU_MAX_HW_QUEUES</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id309">New HIP APIs in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#error-handling">Error handling</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-tests-source-separation">HIP tests source separation</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id310">OpenMP enhancements</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id311">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id312">HIP Perl scripts deprecation</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id313">Linux file system hierarchy standard for ROCm</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id314">New file system hierarchy</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id315">Backward compatibility with older file systems</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id316">Wrapper header files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id317">Library files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id318">CMake config files</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id319">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#memory-allocated-using-hiphostmalloc-with-flags-didn-t-exhibit-fine-grain-behavior">Memory allocated using hipHostMalloc() with flags didn’t exhibit fine-grain behavior</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#issue">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#fix">Fix</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#softhang-with-hipstreamwithcumask-test-on-amd-instinct">SoftHang with <code class="docutils literal notranslate"><span class="pre">hipStreamWithCUMask</span></code> test on AMD Instinct™</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id320">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id321">Fix</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-tools-gpu-ids">ROCm tools GPU IDs</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-4-0">Library changes in ROCM 5.4.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-0-53-0">hipBLAS 0.53.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id322">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-2-13-0">hipCUB 2.13.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id323">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id324">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-10">hipFFT 1.0.10</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id325">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id326">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-6-0">hipSOLVER 1.6.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id327">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-3-3">hipSPARSE 2.3.3</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id328">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id329">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-2-13-4">rccl 2.13.4</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id330">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id331">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-1-3">rocALUTION 2.1.3</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id332">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id333">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id334">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-2-46-0">rocBLAS 2.46.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id335">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id336">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id337">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id338">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-19">rocFFT 1.0.19</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id339">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id340">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id341">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-12-0">rocPRIM 2.12.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id342">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id343">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id344">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-2-10-16">rocRAND 2.10.16</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id345">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id346">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id347">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-20-0">rocSOLVER 3.20.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id348">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id349">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-4-0">rocSPARSE 2.4.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id350">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id351">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-2-17-0">rocThrust 2.17.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id352">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-0-9">rocWMMA 0.9</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id353">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id354">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-35-0">Tensile 4.35.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id355">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id356">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id357">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id358">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-3-3">ROCm 5.3.3</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id359">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#issue-with-rocthrust-and-rocprim-libraries">Issue with rocTHRUST and rocPRIM libraries</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-3-3">Library changes in ROCM 5.3.3</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-3-2">ROCm 5.3.2</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id360">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#peer-to-peer-dma-mapping-errors-with-sles-and-rhel">Peer-to-peer DMA mapping errors with SLES and RHEL</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-tuning-table">RCCL tuning table</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#sgemm-f32-gemm-routines-in-rocblas">SGEMM (F32 GEMM) routines in rocBLAS</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id361">Known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi200-sriov-virtualization-issue">AMD Instinct™ MI200 SRIOV virtualization issue</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi200-firmware-updates">AMD Instinct™ MI200 firmware updates</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#known-issue-with-rocthrust-and-rocprim-libraries">Known issue with rocThrust and rocPRIM libraries</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-3-2">Library changes in ROCM 5.3.2</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-3-0">ROCm 5.3.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id362">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id363">HIP Perl scripts deprecation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id364">Linux file system hierarchy standard for ROCm</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id365">New file system hierarchy</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id366">Backward compatibility with older file systems</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id367">Wrapper header files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id368">Library files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id369">CMake config files</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id370">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-produces-incorrect-results-with-rocm-5-2">Kernel produces incorrect results with ROCm 5.2</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id371">Known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#issue-with-openmp-extras-package-upgrade">Issue with OpenMP-extras package upgrade</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id372">AMD Instinct™ MI200 SRIOV virtualization issue</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#system-crash-when-immou-is-enabled">System crash when IMMOU is enabled</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-3-0">Library changes in ROCM 5.3.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-0-52-0">hipBLAS 0.52.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id373">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id374">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-2-12-0">hipCUB 2.12.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id375">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id376">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-9">hipFFT 1.0.9</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id377">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-5-0">hipSOLVER 1.5.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id378">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id379">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id380">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-3-1">hipSPARSE 2.3.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id381">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-1-0">rocALUTION 2.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id382">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id383">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-2-45-0">rocBLAS 2.45.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id384">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id385">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id386">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id387">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id388">Deprecated</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id389">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-18">rocFFT 1.0.18</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id390">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id391">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id392">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-cmake-0-8-0">rocm-cmake 0.8.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id393">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id394">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-11-0">rocPRIM 2.11.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id395">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-2-10-15">rocRAND 2.10.15</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id396">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-19-0">rocSOLVER 3.19.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id397">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id398">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id399">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id400">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-2-16-0">rocThrust 2.16.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id401">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-0-8">rocWMMA 0.8</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-34-0">Tensile 4.34.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id402">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id403">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id404">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id405">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-2-3">ROCm 5.2.3</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#changes-in-this-release">Changes in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#ubuntu-18-04-end-of-life-announcement">Ubuntu 18.04 end-of-life announcement</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-runtime">HIP runtime</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id406">Fixes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl">RCCL</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id407">Additions</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id408">Removals</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#development-tools">Development tools</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-2-3">Library changes in ROCM 5.2.3</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-2-12-10">rccl 2.12.10</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id409">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id410">Removed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-2-1">ROCm 5.2.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-2-1">Library changes in ROCM 5.2.1</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-2-0">ROCm 5.2.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id411">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id412">HIP enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-installation-guide-updates">HIP installation guide updates</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#support-for-device-side-malloc-on-hip-clang">Support for device-side malloc on HIP-Clang</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id413">New HIP APIs in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#device-management-hip-apis">Device management HIP APIs</a></li>
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#new-hip-runtime-apis-in-memory-management">New HIP runtime APIs in memory management</a></li>
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#id414">HIP graph management APIs</a></li>
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#support-for-virtual-memory-management-apis">Support for virtual memory management APIs</a></li>
</ul>
</li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#planned-hip-changes-in-future-releases">Planned HIP changes in future releases</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-math-and-communication-libraries">ROCm math and communication libraries</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#openmp-enhancements-in-this-release">OpenMP enhancements in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#ompt-target-support">OMPT target support</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id415">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id416">Linux file system hierarchy standard for ROCm</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id417">New file system hierarchy</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id418">Backward compatibility with older file systems</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id419">Wrapper header files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id420">Library files</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id421">CMake config files</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#planned-deprecation-of-hip-rocclr-and-hip-base-packages">Planned deprecation of hip-rocclr and hip-base packages</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#deprecation-of-integrated-hip-directed-tests">Deprecation of integrated HIP directed tests</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id422">Defect fixes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id423">Known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#compiler-error-on-gfx1030-when-compiling-at-o0">Compiler error on gfx1030 when compiling at -O0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id424">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#workaround">Workaround</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#system-freeze-observed-during-cuda-memtest-checkpoint">System freeze observed during CUDA memtest checkpoint</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id425">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id426">Workaround</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hpc-test-fails-with-the-hsa-status-error-memory-fault-error">HPC test fails with the “HSA_STATUS_ERROR_MEMORY_FAULT” error</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id427">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id428">Workaround</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#kernel-produces-incorrect-result">Kernel produces incorrect result</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id429">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id430">Workaround</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#issue-with-applications-triggering-oversubscription">Issue with applications triggering oversubscription</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-2-0">Library changes in ROCM 5.2.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-0-51-0">hipBLAS 0.51.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id431">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id432">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-2-11-1">hipCUB 2.11.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id433">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-8">hipFFT 1.0.8</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id434">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-4-0">hipSOLVER 1.4.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id435">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id436">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-2-0">hipSPARSE 2.2.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id437">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-0-3">rocALUTION 2.0.3</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id438">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-2-44-0">rocBLAS 2.44.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id439">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id440">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id441">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id442">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id443">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-17">rocFFT 1.0.17</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id444">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id445">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id446">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id447">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-10-14">rocPRIM 2.10.14</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id448">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-2-10-14">rocRAND 2.10.14</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id449">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-18-0">rocSOLVER 3.18.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id450">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id451">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-2-0">rocSPARSE 2.2.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id452">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id453">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id454">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id455">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-2-15-0">rocThrust 2.15.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id456">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-0-7">rocWMMA 0.7</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id457">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id458">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-33-0">Tensile 4.33.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id459">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id460">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id461">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id462">Fixed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-1-3">ROCm 5.1.3</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-1-3">Library changes in ROCM 5.1.3</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-1-1">ROCm 5.1.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-1-1">Library changes in ROCM 5.1.1</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-1-0">ROCm 5.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id463">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id464">HIP enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id465">HIP installation guide updates</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#support-for-hip-graph">Support for HIP graph</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#planned-changes-for-hip-in-future-releases">Planned changes for HIP in future releases</a><ul class="nav section-nav flex-column">
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#separation-of-hiprtc-libhiprtc-library-from-hip-runtime-amdhip64">Separation of hiprtc (libhiprtc) library from hip runtime (amdhip64)</a></li>
<li class="toc-h6 nav-item toc-entry"><a class="reference internal nav-link" href="#hipdeviceprop-t-structure-enhancements">hipDeviceProp_t structure enhancements</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocdebugger-enhancements">ROCDebugger enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#multi-language-source-level-debugger">Multi-language source-level debugger</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#machine-interface-lanes-support">Machine interface lanes support</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#enhanced-clone-inferior-command">Enhanced - clone-inferior command</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#miopen-support-for-rdna-gpus">MIOpen support for RDNA GPUs</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#checkpoint-restore-support-with-criu">Checkpoint restore support with CRIU</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id466">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#driver-fails-to-load-after-installation">Driver fails to load after installation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocdebugger-defect-fixes">ROCDebugger defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#breakpoints-in-gpu-kernel-code-before-kernel-is-loaded">Breakpoints in GPU kernel code before kernel is loaded</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#registers-invalidated-after-write">Registers invalidated after write</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#scheduler-locking-and-gpu-wavefronts">Scheduler-locking and GPU wavefronts</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#rocdebugger-fails-before-completion-of-kernel-execution">ROCDebugger fails before completion of kernel execution</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id467">Known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#random-memory-access-fault-errors-observed-while-running-math-libraries-unit-tests">Random memory access fault errors observed while running math libraries unit tests</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#cu-masking-causes-application-to-freeze">CU masking causes application to freeze</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#failed-checkpoint-in-docker-containers">Failed checkpoint in Docker containers</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#issue-with-restoring-workloads-using-cooperative-groups-feature">Issue with restoring workloads using cooperative groups feature</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#radeon-pro-v620-and-w6800-workstation-gpus">Radeon Pro V620 and W6800 workstation GPUs</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#no-support-for-rocdebugger-on-sriov">No support for ROCDebugger on SRIOV</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#random-error-messages-in-rocm-smi-for-sr-iov">Random error messages in ROCm SMI for SR-IOV</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-1-0">Library changes in ROCM 5.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-0-50-0">hipBLAS 0.50.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id468">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id469">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id470">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-2-11-0">hipCUB 2.11.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id471">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id472">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-7">hipFFT 1.0.7</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id473">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hiprand-2-10-13">hipRAND 2.10.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id474">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-3-0">hipSOLVER 1.3.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id475">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id476">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id477">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-1-0">hipSPARSE 2.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id478">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id479">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id480">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id481">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-2-11-4">rccl 2.11.4</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id482">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id483">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-0-2">rocALUTION 2.0.2</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id484">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-2-43-0">rocBLAS 2.43.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id485">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id486">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id487">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id488">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-16">rocFFT 1.0.16</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id489">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id490">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id491">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id492">Removed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-10-13">rocPRIM 2.10.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id493">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id494">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id495">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id496">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-2-10-13">rocRAND 2.10.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id497">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id498">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id499">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id500">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-17-0">rocSOLVER 3.17.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id501">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id502">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-1-0">rocSPARSE 2.1.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id503">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id504">Improved</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id505">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-2-14-0">rocThrust 2.14.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id506">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id507">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-32-0">Tensile 4.32.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id508">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id509">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id510">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id511">Removed</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-0-2">ROCm 5.0.2</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id512">Defect fixes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#issue-with-hostcall-facility-in-hip-runtime">Issue with hostcall facility in HIP runtime</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-0-2">Library changes in ROCM 5.0.2</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-0-1">ROCm 5.0.1</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id513">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#refactor-of-hipcc-hipconfig">Refactor of HIPCC/HIPCONFIG</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-0-1">Library changes in ROCM 5.0.1</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-5-0-0">ROCm 5.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id514">What’s new in this release</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id515">HIP enhancements</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id516">HIP installation guide updates</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#managed-memory-allocation">Managed memory allocation</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#new-environment-variable">New environment variable</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#breaking-changes">Breaking changes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#runtime-breaking-change">Runtime breaking change</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id517">Known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#incorrect-dgpu-behavior-when-using-amdvbflash-tool">Incorrect dGPU behavior when using AMDVBFlash tool</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#issue-with-start-timestamp-in-rocprofiler">Issue with START timestamp in ROCProfiler</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id518">Issue</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#current-behavior">Current behavior</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#expected-behavior">Expected behavior</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#recommended-workaround">Recommended workaround</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id519">Radeon Pro V620 and W6800 workstation GPUs</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#no-support-for-smi-and-rocdebugger-on-sriov">No support for SMI and ROCDebugger on SRIOV</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id520">Deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-libraries-changes-deprecations-and-deprecation-removal">ROCm libraries changes – deprecations and deprecation removal</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-api-deprecations-and-warnings">HIP API deprecations and warnings</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#warning-arithmetic-operators-of-hip-complex-and-vector-types">Warning - arithmetic operators of HIP complex and vector types</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warning-compiler-generated-code-object-version-4-deprecation">Warning - compiler-generated code object version 4 deprecation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#warning-miopentensile-deprecation">Warning - MIOpenTensile deprecation</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#library-changes-in-rocm-5-0-0">Library changes in ROCM 5.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-0-49-0">hipBLAS 0.49.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id521">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id522">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-2-10-13">hipCUB 2.10.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id523">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id524">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id525">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-4">hipFFT 1.0.4</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id526">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id527">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-1-2-0">hipSOLVER 1.2.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id528">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id529">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-2-0-0">hipSPARSE 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id530">Added</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-2-10-3">rccl 2.10.3</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id531">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id532">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-2-0-1">rocALUTION 2.0.1</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id533">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id534">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-2-42-0">rocBLAS 2.42.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id535">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id536">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id537">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id538">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-13">rocFFT 1.0.13</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id539">Optimizations</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id540">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id541">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-2-10-12">rocPRIM 2.10.12</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id542">Fixed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id543">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id544">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id545">Known Issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-2-10-12">rocRAND 2.10.12</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id546">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-16-0">rocSOLVER 3.16.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id547">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id548">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id549">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id550">Fixed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-2-0-0">rocSPARSE 2.0.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id551">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id552">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id553">Improved</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-2-13-0">rocThrust 2.13.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id554">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id555">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-31-0">Tensile 4.31.0</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id556">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id557">Optimized</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id558">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id559">Removed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id560">Fixed</a></li>
</ul>
</li>
</ul>
</li>
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
<li><a href="https://rocm.docs.amd.com/en/docs-6.0.0/about/license.html">ROCm Licenses and Disclaimers</a></li>
<li><a href="https://www.amd.com/en/corporate/privacy" target="_blank">Privacy</a></li>
<li><a href="https://www.amd.com/en/corporate/trademarks" target="_blank">Trademarks</a></li>
<li><a href="https://www.amd.com/system/files/documents/statement-human-trafficking-forced-labor.pdf" target="_blank">Statement on Forced Labor</a></li>
<li><a href="https://www.amd.com/en/corporate/competition" target="_blank">Fair and Open Competition</a></li>
<li><a href="https://www.amd.com/system/files/documents/amd-uk-tax-strategy.pdf" target="_blank">UK Tax Strategy</a></li>
<li><a href="https://www.amd.com/en/corporate/cookies" target="_blank">Cookie Policy</a></li>
<!-- OneTrust Cookies Settings button start -->
<li><a class="ot-sdk-show-settings" href="#cookie-settings" id="ot-sdk-btn">Cookie Settings</a></li>
<!-- OneTrust Cookies Settings button end -->
</ul>
</div>
</div>
<div class="row d-flex align-items-center">
<div class="col-12 text-center">
<div>
<span class="copyright">© 2024 Advanced Micro Devices, Inc</span>
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
