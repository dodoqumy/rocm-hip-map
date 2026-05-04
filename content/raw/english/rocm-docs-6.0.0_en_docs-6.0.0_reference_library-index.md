---
title: "ROCm API libraries &amp; tools"
source_url: "https://rocm.docs.amd.com/en/docs-6.0.0/reference/library-index.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:10:32.821165+00:00
content_hash: "23bd114bfc0092c5"
---


<!DOCTYPE html>

<html data-content_root="../" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/><meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>ROCm API libraries &amp; tools — ROCm Documentation</title>
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

<script>DOCUMENTATION_OPTIONS.pagename = 'reference/library-index';</script>
<script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
<link href="https://www.amd.com/themes/custom/amd/favicon.ico" rel="icon"/>
<link href="../genindex.html" rel="index" title="Index"/>
<link href="../search.html" rel="search" title="Search"/>
<link href="../how-to/deep-learning-rocm.html" rel="next" title="Deep learning guide"/>
<link href="../about/CHANGELOG.html" rel="prev" title="Changelog"/>
<meta content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" name="google-site-verification"/>
<!-- RTD Extra Head -->

<script id="READTHEDOCS_DATA" type="application/json">{"ad_free": false, "api_host": "https://readthedocs.com", "builder": "sphinx", "canonical_url": null, "docroot": "/docs/", "features": {"docsearch_disabled": false}, "global_analytics_code": null, "language": "en", "page": "reference/library-index", "programming_language": "cpp", "project": "advanced-micro-devices-demo", "proxied_api_host": "/_", "source_suffix": ".md", "subprojects": {"advanced-micro-devices-amdmigraphx": "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/", "advanced-micro-devices-amdsmi": "https://rocm.docs.amd.com/projects/amdsmi/en/latest/", "advanced-micro-devices-bom": "https://rocm.docs.amd.com/projects/BOM/en/latest/", "advanced-micro-devices-composable-kernel": "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/", "advanced-micro-devices-dcgpu-project-bkcs": "https://rocm.docs.amd.com/projects/dcgpu-benchmarks/en/latest/", "advanced-micro-devices-gpu-cluster-networking-internal": "https://rocm.docs.amd.com/projects/gpu-cluster-networking-internal/en/latest/", "advanced-micro-devices-half": "https://rocm.docs.amd.com/projects/half/en/latest/", "advanced-micro-devices-hip": "https://rocm.docs.amd.com/projects/HIP/en/latest/", "advanced-micro-devices-hip-python": "https://rocm.docs.amd.com/projects/hip-python/en/latest/", "advanced-micro-devices-hip-vs": "https://rocm.docs.amd.com/projects/hip-vs/en/latest/", "advanced-micro-devices-hipblas": "https://rocm.docs.amd.com/projects/hipBLAS/en/latest/", "advanced-micro-devices-hipblaslt": "https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/", "advanced-micro-devices-hipcc": "https://rocm.docs.amd.com/projects/HIPCC-archive/en/develop/", "advanced-micro-devices-hipcc-llvm-project": "https://rocm.docs.amd.com/projects/HIPCC/en/latest/", "advanced-micro-devices-hipcub": "https://rocm.docs.amd.com/projects/hipCUB/en/latest/", "advanced-micro-devices-hipfft": "https://rocm.docs.amd.com/projects/hipFFT/en/latest/", "advanced-micro-devices-hipfort": "https://rocm.docs.amd.com/projects/hipfort/en/latest/", "advanced-micro-devices-hipify": "https://rocm.docs.amd.com/projects/HIPIFY/en/latest/", "advanced-micro-devices-hiprand": "https://rocm.docs.amd.com/projects/hipRAND/en/latest/", "advanced-micro-devices-hipsolver": "https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/", "advanced-micro-devices-hipsparse": "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/", "advanced-micro-devices-hipsparselt": "https://rocm.docs.amd.com/projects/hipSPARSELt/en/latest/", "advanced-micro-devices-hiptensor": "https://rocm.docs.amd.com/projects/hipTensor/en/latest/", "advanced-micro-devices-linux-install-docs": "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/", "advanced-micro-devices-linux-install-docs-internal": "https://rocm.docs.amd.com/projects/install-on-linux-internal/en/latest/", "advanced-micro-devices-llvm-project-docs": "https://rocm.docs.amd.com/projects/llvm-project/en/latest/", "advanced-micro-devices-miopen": "https://rocm.docs.amd.com/projects/MIOpen/en/latest/", "advanced-micro-devices-mivisionx": "https://rocm.docs.amd.com/projects/MIVisionX/en/latest/", "advanced-micro-devices-omniperf": "https://rocm.docs.amd.com/projects/omniperf/en/latest/", "advanced-micro-devices-omnitrace": "https://rocm.docs.amd.com/projects/omnitrace/en/latest/", "advanced-micro-devices-openmp-llvm-project": "https://rocm.docs.amd.com/projects/OpenMP/en/latest/", "advanced-micro-devices-rccl": "https://rocm.docs.amd.com/projects/rccl/en/latest/", "advanced-micro-devices-rdc": "https://rocm.docs.amd.com/projects/rdc/en/latest/", "advanced-micro-devices-rocal": "https://rocm.docs.amd.com/projects/rocAL/en/latest/", "advanced-micro-devices-rocalution": "https://rocm.docs.amd.com/projects/rocALUTION/en/latest/", "advanced-micro-devices-rocblas": "https://rocm.docs.amd.com/projects/rocBLAS/en/latest/", "advanced-micro-devices-rocdbgapi-docs": "https://rocm.docs.amd.com/projects/ROCdbgapi/en/latest/", "advanced-micro-devices-rocdecode": "https://rocm.docs.amd.com/projects/rocDecode/en/latest/", "advanced-micro-devices-rocfft": "https://rocm.docs.amd.com/projects/rocFFT/en/latest/", "advanced-micro-devices-rocgdb-internal": "https://rocm.docs.amd.com/projects/ROCgdb/en/latest/", "advanced-micro-devices-rocjpeg": "https://rocm.docs.amd.com/projects/rocJPEG/en/latest/", "advanced-micro-devices-rocm-bandwidth-test": "https://rocm.docs.amd.com/projects/rocm_bandwidth_test/en/latest/", "advanced-micro-devices-rocm-cmake": "https://rocm.docs.amd.com/projects/ROCmCMakeBuildTools/en/latest/", "advanced-micro-devices-rocm-docs-core": "https://rocm.docs.amd.com/projects/rocm-docs-core/en/latest/", "advanced-micro-devices-rocm-install-on-windows": "https://rocm.docs.amd.com/projects/install-on-windows/en/latest/", "advanced-micro-devices-rocm-install-on-windows-internal": "https://rocm.docs.amd.com/projects/install-on-windows-internal/en/latest/", "advanced-micro-devices-rocm-smi-lib": "https://rocm.docs.amd.com/projects/rocm_smi_lib/en/latest/", "advanced-micro-devices-rocminfo": "https://rocm.docs.amd.com/projects/rocminfo/en/latest/", "advanced-micro-devices-rocmradeon": "https://rocm.docs.amd.com/projects/radeon/en/latest/", "advanced-micro-devices-rocmvalidationsuite": "https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/", "advanced-micro-devices-rocprim": "https://rocm.docs.amd.com/projects/rocPRIM/en/latest/", "advanced-micro-devices-rocprofiler-docs": "https://rocm.docs.amd.com/projects/rocprofiler/en/latest/", "advanced-micro-devices-rocprofiler-sdk": "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/", "advanced-micro-devices-rocprofiler-sdk-internal": "https://rocm.docs.amd.com/projects/rocprofiler-sdk-internal/en/latest/", "advanced-micro-devices-rocpydecode": "https://rocm.docs.amd.com/projects/rocPyDecode/en/latest/", "advanced-micro-devices-rocr-debug-agent": "https://rocm.docs.amd.com/projects/rocr_debug_agent/en/latest/", "advanced-micro-devices-rocr-runtime": "https://rocm.docs.amd.com/projects/ROCR-Runtime/en/latest/", "advanced-micro-devices-rocrand": "https://rocm.docs.amd.com/projects/rocRAND/en/latest/", "advanced-micro-devices-rocsolver": "https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/", "advanced-micro-devices-rocsparse": "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/", "advanced-micro-devices-rocthrust": "https://rocm.docs.amd.com/projects/rocThrust/en/latest/", "advanced-micro-devices-roctracer-docs": "https://rocm.docs.amd.com/projects/roctracer/en/latest/", "advanced-micro-devices-rocwmma": "https://rocm.docs.amd.com/projects/rocWMMA/en/latest/", "advanced-micro-devices-rpp": "https://rocm.docs.amd.com/projects/rpp/en/latest/", "advanced-micro-devices-swab-documentation": "https://rocm.docs.amd.com/projects/swab-documentation/en/latest/", "advanced-micro-devices-tensile": "https://rocm.docs.amd.com/projects/Tensile/en/latest/", "advanced-micro-devices-transferbench": "https://rocm.docs.amd.com/projects/TransferBench/en/latest/"}, "theme": "rocm_docs_theme", "user_analytics_code": "", "version": "docs-6.0.0"}</script>
<!--
Using this variable directly instead of using `JSON.parse` is deprecated.
The READTHEDOCS_DATA global variable will be removed in the future.
-->
<script type="text/javascript">
READTHEDOCS_DATA = JSON.parse(document.getElementById('READTHEDOCS_DATA').innerHTML);
</script>

<!-- end RTD <extrahead> -->
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-demo" /><meta name="readthedocs-version-slug" content="docs-6.0.0" /><meta name="readthedocs-resolver-filename" content="/reference/library-index.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../what-is-rocm.html">What is ROCm?</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../about/release-notes.html">Release notes</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../about/CHANGELOG.html">Changelog</a></li>
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
<ul class="current nav bd-sidenav">
<li class="toctree-l1 current active"><a class="current reference internal" href="#">API libraries &amp; tools</a></li>
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
<li class="toctree-l1"><a class="reference internal" href="../about/compatibility/openmp.html">OpenMP</a></li>
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
<li class="toctree-l1"><a class="reference internal" href="../about/license.html">License</a></li>
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
<li aria-current="page" class="breadcrumb-item active">ROCm API...</li>
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
</div></div>
</div>
</div>
</div>
<div class="onlyprint" id="jb-print-docs-body">
<h1>ROCm API libraries &amp; tools</h1>
<!-- Table of contents -->
<div id="print-main-content">
<div id="jb-print-toc">
</div>
</div>
</div>
<div id="searchbox"></div>
<article class="bd-article">
<head>
<meta charset="utf-8"/>
<meta content="ROCm API libraries &amp; tools" name="description"/>
<meta content="ROCm, API, libraries, tools, artificial intelligence, development,
  Communications, C++ primitives, Fast Fourier transforms, FFTs, random number generators, linear
  algebra, AMD" name="keywords"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-demo" /><meta name="readthedocs-version-slug" content="docs-6.0.0" /><meta name="readthedocs-resolver-filename" content="/reference/library-index.html" /><meta name="readthedocs-http-status" content="200" /></head>
<section class="tex2jax_ignore mathjax_ignore" id="rocm-api-libraries-tools">
<h1>ROCm API libraries &amp; tools<a class="headerlink" href="#rocm-api-libraries-tools" title="Link to this heading">#</a></h1><div class="sd-container-fluid sd-sphinx-override sd-p-0 sd-mt-2 sd-mb-4 sd-p-2 sd-rounded-1 docutils" id="rocm-docs-core-article-info">
<div class="sd-row sd-row-cols-2 sd-gx-2 sd-gy-1 docutils">
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils" style="color:gray;">
    Applies to Linux
</div>
<div class="sd-col sd-d-flex-row sd-align-minor-center docutils">
<div class="sd-container-fluid sd-sphinx-override docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-3 sd-row-cols-md-3 sd-row-cols-lg-3 sd-gx-3 sd-gy-1 docutils">
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils">
<p class="sd-p-0 sd-m-0" style="color:gray;"></p>
</div>
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils">
<p class="sd-p-0 sd-m-0" style="color:gray;"><span class="sd-pr-2"><svg aria-hidden="true" class="sd-octicon sd-octicon-calendar" height="16.0px" version="1.1" viewbox="0 0 16 16" width="16.0px"><path d="M4.75 0a.75.75 0 01.75.75V2h5V.75a.75.75 0 011.5 0V2h1.25c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0113.25 16H2.75A1.75 1.75 0 011 14.25V3.75C1 2.784 1.784 2 2.75 2H4V.75A.75.75 0 014.75 0zm0 3.5h8.5a.25.25 0 01.25.25V6h-11V3.75a.25.25 0 01.25-.25h2zm-2.25 4v6.75c0 .138.112.25.25.25h10.5a.25.25 0 00.25-.25V7.5h-11z" fill-rule="evenodd"></path></svg></span>2024-01-16</p>
</div>
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils">
<p class="sd-p-0 sd-m-0" style="color:gray;"><span class="sd-pr-2"><svg aria-hidden="true" class="sd-octicon sd-octicon-clock" height="16.0px" version="1.1" viewbox="0 0 16 16" width="16.0px"><path d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zm.5 4.75a.75.75 0 00-1.5 0v3.5a.75.75 0 00.471.696l2.5 1a.75.75 0 00.557-1.392L8.5 7.742V4.75z" fill-rule="evenodd"></path></svg></span>2 min read time</p>
</div>
</div>
</div>
</div>
</div>
</div>

<div class="sd-container-fluid sd-sphinx-override sd-mb-4 rocm-doc-grid docutils">
<div class="sd-row sd-row-cols-1 sd-row-cols-xs-1 sd-row-cols-sm-3 sd-row-cols-md-3 sd-row-cols-lg-3 docutils">
<div class="sd-col sd-d-flex-row sd-p-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-header docutils">
<p class="sd-card-text"><strong>Artificial intelligence</strong></p>
</div>
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/composable_kernel/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">Composable Kernel</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/AMDMIGraphX/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">MIGraphX</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/MIOpen/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">MIOpen</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/MIVisionX/en/docs-6.0.0/doxygen/html/index.html" title="(in MIVisionX Documentation v2.5.0)"><span class="xref std std-doc">MIVisionX</span></a></p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-p-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-header docutils">
<p class="sd-card-text"><strong>C++ primitives</strong></p>
</div>
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/hipCUB/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">hipCUB</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/hipTensor/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">hipTensor</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/rocPRIM/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">rocPRIM</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/rocThrust/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">rocThrust</span></a></p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-p-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-header docutils">
<p class="sd-card-text"><strong>Communication</strong></p>
</div>
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/rccl/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">RCCL</span></a></p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-p-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-header docutils">
<p class="sd-card-text"><strong>Development tools</strong></p>
</div>
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/ROCdbgapi/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">ROCdbgapi</span></a></p></li>
<li><p class="sd-card-text"><a class="reference internal" href="rocmcc.html"><span class="std std-doc">ROCmCC</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/ROCgdb/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">ROCm debugger (ROCgdb)</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/roctracer/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">ROCTracer</span></a></p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-p-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-header docutils">
<p class="sd-card-text"><strong>Fast Fourier transforms (FFTs)</strong></p>
</div>
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/hipFFT/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">hipFFT</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/rocFFT/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">rocFFT</span></a></p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-p-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-header docutils">
<p class="sd-card-text"><strong>HIP</strong></p>
</div>
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/docs-6.0.0/index.html" title="(in HIP Documentation v6.0.0)"><span class="xref std std-doc">HIP runtime</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/HIPIFY/en/docs-6.0.0/index.html" title="(in HIPIFY Documentation)"><span class="xref std std-doc">HIPIFY</span></a></p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-p-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-header docutils">
<p class="sd-card-text"><strong>Linear algebra</strong></p>
</div>
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/hipBLAS/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">hipBLAS</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/hipBLASLt/en/docs-6.0.0/index.html" title="(in hipBLASLt Documentation v0.6.0)"><span class="xref std std-doc">hipBLASLt</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/hipSOLVER/en/docs-6.0.0/index.html" title="(in hipSOLVER Documentation v2.1.0)"><span class="xref std std-doc">hipSOLVER</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/hipSPARSE/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">hipSPARSE</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/hipSPARSELt/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">hipSPARSELt</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/rocALUTION/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">rocALUTION</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/rocBLAS/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">rocBLAS</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/rocSOLVER/en/docs-6.0.0/index.html" title="(in rocSOLVER Documentation v3.25.0)"><span class="xref std std-doc">rocSOLVER</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/rocSPARSE/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">rocSPARSE</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/rocWMMA/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">rocWMMA</span></a></p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-p-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-header docutils">
<p class="sd-card-text"><strong>Performance analysis</strong></p>
</div>
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><span class="xref std std-doc">ROCProfiler</span></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/roctracer/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">ROCTracer</span></a></p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-p-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-header docutils">
<p class="sd-card-text"><strong>Random number generators</strong></p>
</div>
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/hipRAND/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">hipRAND</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/rocRAND/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">rocRAND</span></a></p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-p-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-header docutils">
<p class="sd-card-text"><strong>System tools</strong></p>
</div>
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/amdsmi/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">AMD SMI</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/rdc/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">ROCm Data Center Tool</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/rocm_smi_lib/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">ROCm SMI</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/docs-6.0.0/index.html" title="(in Python)"><span class="xref std std-doc">ROCm Validation Suite</span></a></p></li>
<li><p class="sd-card-text"><a class="reference external" href="https://rocm.docs.amd.com/projects/TransferBench/en/docs-6.0.0/index.html" title="(in TransferBench Documentation v1.34)"><span class="xref std std-doc">TransferBench</span></a></p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<p>We welcome collaboration! If you’d like to contribute to our documentation, you can find instructions
on our <a class="reference internal" href="../contribute/index.html"><span class="std std-doc">Contribute to ROCm docs</span></a> page. Known issues are listed on
<a class="reference external" href="https://github.com/RadeonOpenCompute/ROCm/labels/Verified%20Issue">GitHub</a>.</p>
<p>Licensing information for all ROCm components is listed on our <a class="reference internal" href="../about/license.html"><span class="std std-doc">Licensing</span></a> page.</p>
</section>
</article>
<footer class="prev-next-footer d-print-none">
<div class="prev-next-area">
<a class="left-prev" href="../about/CHANGELOG.html" title="previous page">
<i class="fa-solid fa-angle-left"></i>
<div class="prev-next-info">
<p class="prev-next-subtitle">previous</p>
<p class="prev-next-title">Changelog</p>
</div>
</a>
<a class="right-next" href="../how-to/deep-learning-rocm.html" title="next page">
<div class="prev-next-info">
<p class="prev-next-subtitle">next</p>
<p class="prev-next-title">Deep learning guide</p>
</div>
<i class="fa-solid fa-angle-right"></i>
</a>
</div>
</footer>
</div>
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
