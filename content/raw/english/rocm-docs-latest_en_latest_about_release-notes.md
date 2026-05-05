---
title: "ROCm 7.2.2 release notes"
source_url: "https://rocm.docs.amd.com/en/latest/about/release-notes.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:01:07.383004+00:00
content_hash: "6e1293195bd5df15"
---


<!DOCTYPE html>

<html data-content_root="../" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/><meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>ROCm 7.2.2 release notes — ROCm Documentation</title>
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
<link href="../_static/pygments.css?v=8f2a1f02" rel="stylesheet" type="text/css"/>
<link href="../_static/styles/sphinx-book-theme.css?v=eba8b062" rel="stylesheet" type="text/css"/>
<link href="../_static/mystnb.8ecb98da25f57f5357bf6f572d296f466b2cfe2517ffebfabe82451661e28f02.css" rel="stylesheet" type="text/css"/>
<link href="../_static/copybutton.css?v=76b2166b" rel="stylesheet" type="text/css"/>
<link href="../_static/custom.css?v=24396f60" rel="stylesheet" type="text/css"/>
<link href="../_static/rocm_header.css?v=e999025a" rel="stylesheet" type="text/css"/>
<link href="../_static/rocm_footer.css?v=7095035a" rel="stylesheet" type="text/css"/>
<link href="../_static/fonts.css?v=fcff5274" rel="stylesheet" type="text/css"/>
<link href="../_static/sphinx-design.min.css?v=95c83b7e" rel="stylesheet" type="text/css"/>
<link href="../_static/rocm_custom.css?v=ace7df76" rel="stylesheet" type="text/css"/>
<link href="../_static/rocm_rn.css?v=11d5bdfb" rel="stylesheet" type="text/css"/>
<link href="../_static/vllm-benchmark.css?v=c8832c9d" rel="stylesheet" type="text/css"/>
<!-- Pre-loaded scripts that we'll load fully later -->
<link as="script" href="../_static/scripts/bootstrap.js?digest=dfe6caa3a7d634c4db9b" rel="preload"/>
<link as="script" href="../_static/scripts/pydata-sphinx-theme.js?digest=dfe6caa3a7d634c4db9b" rel="preload"/>
<script src="../_static/vendor/fontawesome/6.5.2/js/all.min.js?digest=dfe6caa3a7d634c4db9b"></script>
<script src="../_static/documentation_options.js?v=187db5c8"></script>
<script src="../_static/doctools.js?v=9bcbadda"></script>
<script src="../_static/sphinx_highlight.js?v=dc90522c"></script>
<script src="../_static/clipboard.min.js?v=a7894cd8"></script>
<script src="../_static/copybutton.js?v=f281be69"></script>
<script async="async" src="../_static/code_word_breaks.js?v=327952c4"></script>
<script async="async" src="../_static/renameVersionLinks.js?v=929fe5e4"></script>
<script async="async" src="../_static/rdcMisc.js?v=01f88d96"></script>
<script async="async" src="../_static/theme_mode_captions.js?v=15f4ec5d"></script>
<script defer="defer" src="../_static/search.js?v=90a4452c"></script>
<script src="../_static/scripts/sphinx-book-theme.js?v=887ef09a"></script>
<script src="../_static/design-tabs.js?v=f930bc37"></script>
<script>DOCUMENTATION_OPTIONS.pagename = 'about/release-notes';</script>
<script src="../_static/vllm-benchmark.js?v=6b88e2d9"></script>
<script async="async" src="https://download.amd.com/js/analytics/analyticsinit.js"></script>
<link href="https://rocm.docs.amd.com/en/latest/about/release-notes.html" rel="canonical"/>
<link href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico" rel="icon"/>
<link href="../genindex.html" rel="index" title="Index"/>
<link href="../search.html" rel="search" title="Search"/>
<link href="../compatibility/compatibility-matrix.html" rel="next" title="Compatibility matrix"/>
<link href="../what-is-rocm.html" rel="prev" title="What is ROCm?"/>
<meta content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" name="google-site-verification"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-demo" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/about/release-notes.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
<div class="bd-header-announcement__content">The ROCm 7.12.0 technology preview release documentation is available at <a href="https://rocm.docs.amd.com/en/7.12.0-preview/" id="rocm-banner">ROCm Preview documentation</a>. For production use, continue to use ROCm 7.2.2 documentation.</div>
</aside>
<header class="common-header">
<nav class="navbar navbar-expand-xl">
<div class="container-fluid main-nav rocm-header">
<div class="header-logo">
<div class="header-logo-title">
<button aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler collapsed" data-bs-target="#navbarSupportedContent" data-bs-toggle="collapse" data-tracking-information="mainMenuToggle" id="nav-icon" type="button">
<span></span>
<span></span>
<span></span>
</button>
<a class="navbar-brand" href="https://www.amd.com/">
<img alt="AMD Logo" class="d-inline-block align-text-top hover-opacity" src="../_static/images/amd-header-logo.svg" title="AMD Logo" width="90"/>
</a>
<div class="vr mx-40 my-25"></div>
<a class="klavika-font hover-opacity" href="https://rocm.docs.amd.com/en/latest">ROCm™ Software 7.2.2</a>
</div>
<a class="header-all-versions hover-opacity" href="https://rocm.docs.amd.com/en/latest/release/versions.html">Version List</a>
</div>
<div class="icon-nav text-center d-flex ms-auto"></div>
</div>
</nav>
<nav class="navbar navbar-expand-xl second-level-nav">
<div class="container-fluid main-nav">
<div class="navbar-nav-container collapse navbar-collapse" id="navbarSupportedContent">
<ul class="navbar-nav nav-mega me-auto mb-2 mb-lg-0 col-xl-10">
<li class="nav-item">
<a aria-expanded="false" class="nav-link top-level header-menu-links" href="https://github.com/ROCm/ROCm" id="navgithub" role="button" target="_blank">
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
<a aria-expanded="false" class="nav-link top-level header-menu-links" href="https://www.amd.com/en/developer/resources/rocm-hub.html" id="navrocm-developer-hub" role="button" target="_blank">
                                        ROCm Developer Hub
                                    </a>
</li>
<li class="nav-item dropdown">
<a aria-expanded="false" class="nav-link top-level header-menu-links dropdown-toggle header-nav-dropdown-toggle" data-bs-toggle="dropdown" href="#" id="navrocm-toolkits" role="button">
                                        ROCm Toolkits
                                    </a>
<ul aria-labelledby="navrocm-toolkits" class="dropdown-menu header-nav-dropdown-menu">
<li><a class="dropdown-item" href="https://rocm.docs.amd.com/projects/rocm-ds/en/latest/index.html" target="_blank">ROCm Data Science</a></li>
<li><a class="dropdown-item" href="https://rocm.docs.amd.com/projects/rocm-finance/en/latest/index.html" target="_blank">ROCm Finance</a></li>
<li><a class="dropdown-item" href="https://rocm.docs.amd.com/projects/rocm-ls/en/latest/index.html" target="_blank">ROCm Life Science</a></li>
<li><a class="dropdown-item" href="https://rocm.docs.amd.com/projects/rocm-llmext/en/latest/index.html" target="_blank">ROCm LLMExt</a></li>
<li><a class="dropdown-item" href="https://rocm.docs.amd.com/projects/rocm-simulation/en/latest/index.html" target="_blank">ROCm Simulation</a></li>
</ul>
</li>
<li class="nav-item">
<a aria-expanded="false" class="nav-link top-level header-menu-links" href="https://instinct.docs.amd.com" id="navsystems-and-infra-docs" role="button" target="_blank">
                                        Systems and Infra Docs
                                    </a>
</li>
<li class="nav-item">
<a aria-expanded="false" class="nav-link top-level header-menu-links" href="https://www.amd.com/en/developer/resources/infinity-hub.html" id="navinfinity-hub" role="button" target="_blank">
                                        Infinity Hub
                                    </a>
</li>
<li class="nav-item">
<a aria-expanded="false" class="nav-link top-level header-menu-links" href="https://github.com/ROCm/ROCm/issues/new/choose" id="navsupport" role="button" target="_blank">
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
<li class="toctree-l1 current active"><a class="current reference internal" href="#">Release notes</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../compatibility/compatibility-matrix.html">Compatibility matrix</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html">Linux system requirements</a></li>
<li class="toctree-l2"><a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-windows/en/latest/reference/system-requirements.html">Windows system requirements</a></li>
</ul>
</details></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/">ROCm on Linux</a></li>
<li class="toctree-l1"><a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-windows/en/latest/">HIP SDK on Windows</a></li>
<li class="toctree-l1"><a class="reference external" href="https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html">ROCm on Radeon and Ryzen</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../how-to/deep-learning-rocm.html">Deep learning frameworks</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../compatibility/ml-compatibility/pytorch-compatibility.html">PyTorch compatibility</a></li>
<li class="toctree-l2"><a class="reference internal" href="../compatibility/ml-compatibility/tensorflow-compatibility.html">TensorFlow compatibility</a></li>
<li class="toctree-l2"><a class="reference internal" href="../compatibility/ml-compatibility/jax-compatibility.html">JAX compatibility</a></li>
<li class="toctree-l2"><a class="reference internal" href="../compatibility/ml-compatibility/dgl-compatibility.html">DGL compatibility</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/build-rocm.html">Build ROCm from source</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">How to</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../how-to/rocm-for-ai/index.html">Use ROCm for AI</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../how-to/rocm-for-ai/install.html">Installation</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../how-to/rocm-for-ai/system-setup/index.html">System setup</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/system-setup/prerequisite-system-validation.html">System validation</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/system-setup/multi-node-setup.html">Multi-node setup</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/system-setup/system-health-check.html">System health benchmarks</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../how-to/rocm-for-ai/training/index.html">Training</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3 has-children"><a class="reference internal" href="../how-to/rocm-for-ai/training/benchmark-docker/primus-megatron.html">Train a model with Primus and Megatron-LM</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../how-to/rocm-for-ai/training/benchmark-docker/megatron-lm.html">Train a model with Megatron-LM (legacy)</a></li>
</ul>
</details></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../how-to/rocm-for-ai/training/benchmark-docker/primus-pytorch.html">Train a model with Primus and PyTorch</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../how-to/rocm-for-ai/training/benchmark-docker/pytorch-training.html">Train a model with PyTorch (legacy)</a></li>
</ul>
</details></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/training/benchmark-docker/jax-maxtext.html">Train a model with Primus and JAX MaxText</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/training/benchmark-docker/mpt-llm-foundry.html">Train a model with LLM Foundry</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/training/scale-model-training.html">Scale model training</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../how-to/rocm-for-ai/fine-tuning/index.html">Fine-tuning LLMs</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/fine-tuning/overview.html">Conceptual overview</a></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../how-to/rocm-for-ai/fine-tuning/fine-tuning-and-inference.html">Fine-tuning</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../how-to/rocm-for-ai/fine-tuning/single-gpu-fine-tuning-and-inference.html">Use a single GPU</a></li>
<li class="toctree-l4"><a class="reference internal" href="../how-to/rocm-for-ai/fine-tuning/multi-gpu-fine-tuning-and-inference.html">Use multiple GPUs</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../how-to/rocm-for-ai/inference/index.html">Inference</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference/hugging-face-models.html">Run models from Hugging Face</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference/llm-inference-frameworks.html">LLM inference frameworks</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference/benchmark-docker/vllm.html">vLLM inference</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference/benchmark-docker/pytorch-inference.html">PyTorch inference performance testing</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference/benchmark-docker/sglang.html">SGLang inference performance testing</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference/benchmark-docker/vllm-mori-distributed.html">vLLM distributed inference with MoRI</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference/benchmark-docker/sglang-mori-distributed.html">SGLang distributed inference with MoRI</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference/benchmark-docker/sglang-distributed.html">SGLang distributed inference with Mooncake</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference/xdit-diffusion-inference.html">xDiT diffusion inference</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference/deploy-your-model.html">Deploy your model</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../how-to/rocm-for-ai/inference-optimization/index.html">Inference optimization</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference-optimization/model-quantization.html">Model quantization techniques</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference-optimization/model-acceleration-libraries.html">Model acceleration libraries</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference-optimization/optimizing-with-composable-kernel.html">Optimize with Composable Kernel</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference-optimization/optimizing-triton-kernel.html">Optimize Triton kernels</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference-optimization/profiling-and-debugging.html">Profile and debug</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference-optimization/workload.html">Workload optimization</a></li>
<li class="toctree-l3"><a class="reference internal" href="../how-to/rocm-for-ai/inference-optimization/vllm-optimization.html">vLLM V1 performance optimization</a></li>
</ul>
</details></li>
<li class="toctree-l2"><a class="reference external" href="https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/">AI tutorials</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/rocm-for-hpc/index.html">Use ROCm for HPC</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/system-optimization/index.html">System optimization</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/gpu-performance/mi300x.html">AMD Instinct MI300X performance guides</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/system-debugging.html">System debugging</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../conceptual/compiler-topics.html">Use advanced compiler features</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference external" href="https://rocm.docs.amd.com/projects/llvm-project/en/latest/index.html">ROCm compiler infrastructure</a></li>
<li class="toctree-l2"><a class="reference external" href="https://rocm.docs.amd.com/projects/llvm-project/en/latest/conceptual/using-gpu-sanitizer.html">Use AddressSanitizer</a></li>
<li class="toctree-l2"><a class="reference external" href="https://rocm.docs.amd.com/projects/llvm-project/en/latest/conceptual/openmp.html">OpenMP support</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/setting-cus.html">Set the number of CUs</a></li>
<li class="toctree-l1"><a class="reference internal" href="../how-to/Bar-Memory.html">Troubleshoot BAR access limitation</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/amd/rocm-examples">ROCm examples</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Conceptual</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../conceptual/gpu-arch.html">GPU architecture overview</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2 has-children"><a class="reference internal" href="../conceptual/gpu-arch/mi300.html">MI300 microarchitecture</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference external" href="https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-mi300-cdna3-instruction-set-architecture.pdf">AMD Instinct MI300/CDNA3 ISA</a></li>
<li class="toctree-l3"><a class="reference external" href="https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/white-papers/amd-cdna-3-white-paper.pdf">White paper</a></li>
<li class="toctree-l3"><a class="reference internal" href="../conceptual/gpu-arch/mi300-mi200-performance-counters.html">MI300 and MI200 performance counters</a></li>
<li class="toctree-l3"><a class="reference internal" href="../conceptual/gpu-arch/mi350-performance-counters.html">MI350 Series performance counters</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../conceptual/gpu-arch/mi250.html">MI250 microarchitecture</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference external" href="https://www.amd.com/system/files/TechDocs/instinct-mi200-cdna2-instruction-set-architecture.pdf">AMD Instinct MI200/CDNA2 ISA</a></li>
<li class="toctree-l3"><a class="reference external" href="https://www.amd.com/content/dam/amd/en/documents/instinct-business-docs/white-papers/amd-cdna2-white-paper.pdf">White paper</a></li>
</ul>
</details></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../conceptual/gpu-arch/mi100.html">MI100 microarchitecture</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l3"><a class="reference external" href="https://www.amd.com/system/files/TechDocs/instinct-mi100-cdna1-shader-instruction-set-architecture%C2%A0.pdf">AMD Instinct MI100/CDNA1 ISA</a></li>
<li class="toctree-l3"><a class="reference external" href="https://www.amd.com/content/dam/amd/en/documents/instinct-business-docs/white-papers/amd-cdna-white-paper.pdf">White paper</a></li>
</ul>
</details></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/file-reorg.html">File structure (Linux FHS)</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/gpu-isolation.html">GPU isolation techniques</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/cmake-packages.html">Using CMake</a></li>
<li class="toctree-l1"><a class="reference internal" href="../conceptual/ai-pytorch-inception.html">Inception v3 with PyTorch</a></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Reference</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="../reference/api-libraries.html">ROCm libraries</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/rocm-tools.html">ROCm tools, compilers, and runtime API</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/gpu-arch-specs.html">GPU hardware specifications</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/gpu-atomics-operation.html">Hardware atomics operation support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/env-variables.html">Environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/precision-support.html">Data types and precision support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/graph-safe-support.html">Graph safe support</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../reference/glossary.html">ROCm glossary</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../reference/glossary/device-hardware.html">Device hardware</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/glossary/device-software.html">Device software</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/glossary/host-software.html">Host software</a></li>
<li class="toctree-l2"><a class="reference internal" href="../reference/glossary/performance.html">Performance</a></li>
</ul>
</details></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Contribute</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1 has-children"><a class="reference internal" href="../contribute/contributing.html">Contributing to the ROCm documentation</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l2"><a class="reference internal" href="../contribute/toolchain.html">ROCm documentation toolchain</a></li>
<li class="toctree-l2"><a class="reference internal" href="../contribute/building.html">Building documentation</a></li>
</ul>
</details></li>
<li class="toctree-l1"><a class="reference internal" href="../contribute/feedback.html">Providing feedback about the ROCm documentation</a></li>
<li class="toctree-l1"><a class="reference internal" href="license.html">ROCm licenses</a></li>
</ul>
</div>
</nav></div>
</div>
<div class="sidebar-primary-items__end sidebar-primary__section">
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
<li aria-current="page" class="breadcrumb-item active">ROCm 7.2.2...</li>
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
<h1>ROCm 7.2.2 release notes</h1>
<!-- Table of contents -->
<div id="print-main-content">
<div id="jb-print-toc">
<div>
<h2> Contents </h2>
</div>
<nav aria-label="Page">
<ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#release-highlights">Release highlights</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#roctracer-failure-to-report-kernel-operations-is-fixed">ROCTracer failure to report kernel operations is fixed</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#user-space-driver-and-firmware-dependent-changes">User space, driver, and firmware dependent changes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-documentation-updates">ROCm documentation updates</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-7-2-1-release-notes">ROCm 7.2.1 release notes</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">Release highlights</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-hardware-operating-system-and-virtualization-changes">Supported hardware, operating system, and virtualization changes</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#virtualization-support">Virtualization support</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id2">User space, driver, and firmware dependent changes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblaslt-updates">hipBLASLt updates</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#deep-learning-and-ai-framework-updates">Deep learning and AI framework updates</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#jax">JAX</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-offline-installer-creator-discontinuation">ROCm Offline Installer Creator discontinuation</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id3">ROCm documentation updates</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-components">ROCm components</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#detailed-component-changes">Detailed component changes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-smi-26-2-2"><strong>AMD SMI</strong> (26.2.2)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#added">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#resolved-issues">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-7-2-1"><strong>HIP</strong> (7.2.1)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id4">Resolved issues</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#changed">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblaslt-1-2-2"><strong>hipBLASLt</strong> (1.2.2)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id5">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocdecode-1-7-0"><strong>rocDecode</strong> (1.7.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#upcoming-changes">Upcoming changes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocjpeg-1-4-0"><strong>rocJPEG</strong> (1.4.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id6">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id7">Upcoming changes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocshmem-3-2-0"><strong>rocSHMEM</strong> (3.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id8">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id9">Resolved issues</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#known-issues">Known issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rpp-2-2-1"><strong>RPP</strong> (2.2.1)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id10">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#optimized">Optimized</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-known-issues">ROCm known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblaslt-performance-regression-for-specific-gemm-configurations">hipBLASLt performance regression for specific GEMM configurations</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi300x-and-mi325x-gpus">AMD Instinct MI300X and MI325X GPUs</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi350-series-gpus">AMD Instinct MI350 Series GPUs</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#longer-runtime-for-hipblaslt-gemm-operations-on-instinct-mi300x-gpus-in-partitioned-mode">Longer runtime for hipBLASLt GEMM operations on Instinct MI300X GPUs in partitioned mode</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#roctracer-might-fail-to-report-kernel-operations">ROCTracer might fail to report kernel operations</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id11">Longer runtime for hipBLASLt GEMM operations on Instinct MI300X GPUs in partitioned mode</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id12">ROCTracer might fail to report kernel operations</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-resolved-issues">ROCm resolved issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#increased-runtime-latency-of-the-hip-hipstreamcreate-api">Increased runtime latency of the HIP hipStreamCreate API</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-upcoming-changes">ROCm upcoming changes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#roctracer-rocprofiler-rocprof-and-rocprofv2-deprecation">ROCTracer, ROCProfiler, rocprof, and rocprofv2 deprecation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-smi-deprecation">ROCm SMI deprecation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#changes-to-rocm-object-tooling">Changes to ROCm Object Tooling</a></li>
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
<!-- Do not edit this file!                                 -->
<!-- This file is autogenerated with                        -->
<!--   tools/autotag/tag_script.py                          -->
<!-- Disable lints since this is an auto-generated file.    -->
<!-- markdownlint-disable blanks-around-headers             -->
<!-- markdownlint-disable no-duplicate-header               -->
<!-- markdownlint-disable no-blanks-blockquote              -->
<!-- markdownlint-disable ul-indent                         -->
<!-- markdownlint-disable no-trailing-spaces                -->
<!-- markdownlint-disable reference-links-images            -->
<!-- markdownlint-disable no-missing-space-atx              -->
<!-- spellcheck-disable                                     -->
<section class="tex2jax_ignore mathjax_ignore" id="rocm-7-2-2-release-notes">
<h1>ROCm 7.2.2 release notes<a class="headerlink" href="#rocm-7-2-2-release-notes" title="Link to this heading">#</a></h1><div class="sd-container-fluid sd-sphinx-override sd-p-0 sd-mt-2 sd-mb-4 sd-p-2 sd-rounded-1 docutils" id="rocm-docs-core-article-info">
<div class="sd-row sd-row-cols-2 sd-gx-2 sd-gy-1 docutils">
<div class="sd-col sd-d-flex-row sd-align-minor-center docutils">
<div class="sd-container-fluid sd-sphinx-override docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-3 sd-row-cols-md-3 sd-row-cols-lg-3 sd-gx-3 sd-gy-1 docutils">
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils">
<p class="sd-p-0 sd-m-0" style="color:gray;">
<span class="sd-pr-2 article-info-date-svg">
<svg aria-hidden="true" class="sd-octicon sd-octicon-calendar" height="16.0px" version="1.1" viewbox="0 0 16 16" width="16.0px">
<path d="M4.75 0a.75.75 0 01.75.75V2h5V.75a.75.75 0 011.5 0V2h1.25c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0113.25 16H2.75A1.75 1.75 0 011 14.25V3.75C1 2.784 1.784 2 2.75 2H4V.75A.75.75 0 014.75 0zm0 3.5h8.5a.25.25 0 01.25.25V6h-11V3.75a.25.25 0 01.25-.25h2zm-2.25 4v6.75c0 .138.112.25.25.25h10.5a.25.25 0 00.25-.25V7.5h-11z" fill-rule="evenodd"></path>
</svg>
</span>
                            2026-04-14
                        </p>
</div>
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils">
<p class="sd-p-0 sd-m-0" style="color:gray;">
<span class="sd-pr-2 article-info-read-time-svg">
<svg aria-hidden="true" class="sd-octicon sd-octicon-clock" height="16.0px" version="1.1" viewbox="0 0 16 16" width="16.0px">
<path d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zm.5 4.75a.75.75 0 00-1.5 0v3.5a.75.75 0 00.471.696l2.5 1a.75.75 0 00.557-1.392L8.5 7.742V4.75z" fill-rule="evenodd"></path>
</svg>
</span>
                            19 min read time
                        </p>
</div>
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils" style="color:gray;">
                        Applies to Linux
                    </div>
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils">
<p class="sd-p-0 sd-m-0" style="color:gray;"></p>
</div>
</div>
</div>
</div>
</div>
</div>

<p>ROCm 7.2.2 is a quality release that resolves the issue listed in the Release highlights.</p>
<section id="release-highlights">
<h2>Release highlights<a class="headerlink" href="#release-highlights" title="Link to this heading">#</a></h2>
<p>The following are the notable changes in ROCm 7.2.2.</p>
<section id="roctracer-failure-to-report-kernel-operations-is-fixed">
<h3>ROCTracer failure to report kernel operations is fixed<a class="headerlink" href="#roctracer-failure-to-report-kernel-operations-is-fixed" title="Link to this heading">#</a></h3>
<p>In ROCm 7.2.1, applications using <a class="reference external" href="https://rocm.docs.amd.com/projects/roctracer/en/latest/index.html">ROCTracer</a> failed to receive some or all kernel operation events due to a ROCTracer reporting failure. This issue has been resolved, and the fix has been applied to ROCTracer.</p>
</section>
<section id="user-space-driver-and-firmware-dependent-changes">
<h3>User space, driver, and firmware dependent changes<a class="headerlink" href="#user-space-driver-and-firmware-dependent-changes" title="Link to this heading">#</a></h3>
<p>The software for AMD Data Center GPU products requires maintaining a hardware
and software stack with interdependencies among the GPU and baseboard
firmware, AMD GPU drivers, and the ROCm user space software. While AMD publishes drivers and ROCm user space components, your server or infrastructure provider publishes the GPU and baseboard firmware by bundling AMD firmware releases via an AMD Platform Level Data Model (PLDM) bundle, which includes the Integrated Firmware Image (IFWI).</p>
<p>GPU and baseboard firmware versioning might differ across GPU families.</p>
<div class="pst-scrollable-table-container">
<table class="table table--middle-left">
<thead>
<tr>
<th class="head">
<p>ROCm Version</p>
</th>
<th class="head">
<p>GPU</p>
</th>
<th class="head">
<p>PLDM Bundle (Firmware)</p>
</th>
<th class="head">
<p>AMD GPU Driver (amdgpu)</p>
</th>
<th class="head">
<p>AMD GPU <br/>
              Virtualization Driver (GIM)</p>
</th>
</tr>
</thead>
<style>
        tbody#virtualization-support-instinct tr:last-child {
          border-bottom: 2px solid var(--pst-color-primary);
        }
    </style>
<tr>
<td rowspan="9" style="vertical-align: middle;">ROCm 7.2.2</td>
<td>MI355X</td>
<td>
              01.26.00.02<br/>
              01.25.17.07<br/>
              01.25.16.03
          </td>
<td>
              30.30.x where x (0-2)<br/>
              30.20.x where x (0-1)<br/>
              30.10.x where x (0-2)
            </td>
<td rowspan="3" style="vertical-align: middle;">8.7.1.K</td>
</tr>
<tr>
<td>MI350X</td>
<td>
              01.26.00.02<br/>
              01.25.17.07<br/>
              01.25.16.03
          </td>
<td>
              30.30.x where x (0-2)<br/>
              30.20.x where x (0-1)<br/>
              30.10.x where x (0-2)
            </td>
</tr>
<tr>
<td>MI325X<a href="#footnote1"><sup>[1]</sup></a></td>
<td>
              01.25.06.08<br/>
              01.25.04.02
          </td>
<td>30.30.x where x (0-2)<br/>
              30.20.x where x (0-1)<a href="#footnote1"><sup>[1]</sup></a><br/>
              30.10.x where x (0-2)<br/>
              6.4.z where z (0-3)<br/>
              6.3.3
          </td>
</tr>
<tr>
<td>MI300X<a href="#footnote2"><sup>[2]</sup></a></td>
<td>01.25.06.04<br/>
              01.25.03.12<br/>
              01.25.02.04</td>
<td rowspan="6" style="vertical-align: middle;">
              30.30.x where x (0-2)<br/>
              30.20.x where x (0-1)<br/>
              30.10.x where x (0-2)<br/>
              6.4.z where z (0–3)<br/>
              6.3.3
          </td>
<td>8.7.1.K</td>
</tr>
<tr>
<td>MI300A</td>
<td>BKC 26.1</td>
<td rowspan="3" style="vertical-align: middle;">Not Applicable</td>
</tr>
<tr>
<td>MI250X</td>
<td>IFWI 47 (or later)</td>
</tr>
<tr>
<td>MI250</td>
<td>MU5 w/ IFWI 75 (or later)</td>
</tr>
<tr>
<td>MI210</td>
<td>MU5 w/ IFWI 75 (or later)</td>
<td>8.7.1.K</td>
</tr>
<tr>
<td>MI100</td>
<td>VBIOS D3430401-037</td>
<td>Not Applicable</td>
</tr>
</table>
</div>
<p id="footnote1">[1]: For AMD Instinct MI325X KVM SR-IOV users, don't use AMD GPU driver (amdgpu) 30.20.0.</p>
<p id="footnote2">[2]: AMD Instinct MI300X KVM SR-IOV with Multi-VF (8 VF) support requires a compatible firmware BKC bundle, which will be released in the coming months.</p>
</section>
<section id="rocm-documentation-updates">
<h3>ROCm documentation updates<a class="headerlink" href="#rocm-documentation-updates" title="Link to this heading">#</a></h3>
<p>ROCm documentation continues to be updated to provide clearer and more comprehensive guidance for a wider range of user needs and use cases.</p>
<ul class="simple">
<li><p>The new <a class="reference external" href="https://rocm.docs.amd.com/en/latest/how-to/system-optimization/rdna3-5.html">AMD RDNA3.5 system optimization</a> topic describes how to optimize systems powered by AMD Ryzen APUs with RDNA3.5 architecture. These APUs combine high-performance CPU cores with integrated RDNA3.5 graphics, and support LPDDR5X-8000 or DDR5 memory.</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>ROCm 7.2.2 doesn’t include any other significant changes or feature additions. For comprehensive changes, new features, and enhancements in ROCm 7.2.1, refer to the <a class="reference internal" href="#rocm-7-2-1-release-notes"><span class="xref myst">ROCm 7.2.1 release notes</span></a> below.</p>
</div>
</section>
</section>
<section id="rocm-7-2-1-release-notes">
<h2>ROCm 7.2.1 release notes<a class="headerlink" href="#rocm-7-2-1-release-notes" title="Link to this heading">#</a></h2>
<p>The release notes provide a summary of notable changes since the previous ROCm release.</p>
<ul class="simple">
<li><p><a class="reference internal" href="#id1"><span class="xref myst">Release highlights</span></a></p></li>
<li><p><a class="reference internal" href="#supported-hardware-operating-system-and-virtualization-changes"><span class="xref myst">Supported hardware, operating system, and virtualization changes</span></a></p></li>
<li><p><a class="reference internal" href="#id2"><span class="xref myst">User space, driver, and firmware dependent changes</span></a></p></li>
<li><p><a class="reference internal" href="#rocm-components">ROCm components versioning</a></p></li>
<li><p><a class="reference internal" href="#detailed-component-changes">Detailed component changes</a></p></li>
<li><p><a class="reference internal" href="#rocm-known-issues">ROCm known issues</a></p></li>
<li><p><a class="reference internal" href="#rocm-resolved-issues">ROCm resolved issues</a></p></li>
<li><p><a class="reference internal" href="#rocm-upcoming-changes">ROCm upcoming changes</a></p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If you’re using AMD Radeon™ GPUs or Ryzen™ for graphics workloads, see the <a class="reference external" href="https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html">Use ROCm on Radeon and Ryzen</a> documentation to verify compatibility and system requirements.</p>
</div>
<section id="id1">
<h3>Release highlights<a class="headerlink" href="#id1" title="Link to this heading">#</a></h3>
<p>The following are notable new features and improvements in ROCm 7.2.1. For changes to individual components, see
<a class="reference internal" href="#detailed-component-changes">Detailed component changes</a>.</p>
<section id="supported-hardware-operating-system-and-virtualization-changes">
<h4>Supported hardware, operating system, and virtualization changes<a class="headerlink" href="#supported-hardware-operating-system-and-virtualization-changes" title="Link to this heading">#</a></h4>
<p>Hardware support remains unchanged in this release.</p>
<p>ROCm 7.2.1 adds support for Ubuntu 24.04.4 (kernel: 6.8 [GA], 6.17 [HWE]) and marks end of support (EoS) for Ubuntu 24.04.3. For more information, see <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.1/install/install-methods/package-manager/package-manager-ubuntu.html">Ubuntu installation</a>.</p>
<p>For more information about:</p>
<ul class="simple">
<li><p>AMD hardware, see <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.1/reference/system-requirements.html#supported-gpus">Supported GPUs (Linux)</a>.</p></li>
<li><p>Operating systems, see <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.1/reference/system-requirements.html#supported-operating-systems">Supported operating systems</a> and <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.1/">ROCm installation for Linux</a>.</p></li>
</ul>
<section id="virtualization-support">
<h5>Virtualization support<a class="headerlink" href="#virtualization-support" title="Link to this heading">#</a></h5>
<p>Virtualization support remains unchanged in this release. For more information, see  <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.1/reference/system-requirements.html#virtualization-support">Virtualization support</a>.</p>
</section>
</section>
<section id="id2">
<h4>User space, driver, and firmware dependent changes<a class="headerlink" href="#id2" title="Link to this heading">#</a></h4>
<p>The software for AMD Data Center GPU products requires maintaining a hardware
and software stack with interdependencies among the GPU and baseboard
firmware, AMD GPU drivers, and the ROCm user space software. While AMD publishes drivers and ROCm user space components, your server or infrastructure provider publishes the GPU and baseboard firmware by bundling AMD’s firmware releases via AMD’s Platform Level Data Model (PLDM) bundle, which includes the Integrated Firmware Image (IFWI).</p>
<p>GPU and baseboard firmware versioning might differ across GPU families.</p>
<div class="pst-scrollable-table-container">
<table class="table table--middle-left">
<thead>
<tr>
<th class="head">
<p>ROCm Version</p>
</th>
<th class="head">
<p>GPU</p>
</th>
<th class="head">
<p>PLDM Bundle (Firmware)</p>
</th>
<th class="head">
<p>AMD GPU Driver (amdgpu)</p>
</th>
<th class="head">
<p>AMD GPU <br/>
              Virtualization Driver (GIM)</p>
</th>
</tr>
</thead>
<style>
        tbody#virtualization-support-instinct tr:last-child {
          border-bottom: 2px solid var(--pst-color-primary);
        }
    </style>
<tr>
<td rowspan="9" style="vertical-align: middle;">ROCm 7.2.1</td>
<td>MI355X</td>
<td>
              01.26.00.02<br/>
              01.25.17.07<br/>
              01.25.16.03
          </td>
<td>
              30.30.x where x (0-2)<br/>
              30.20.x where x (0-1)<br/>
              30.10.X where x (0-2)
            </td>
<td rowspan="3" style="vertical-align: middle;">8.7.1.K</td>
</tr>
<tr>
<td>MI350X</td>
<td>
              01.26.00.02<br/>
              01.25.17.07<br/>
              01.25.16.03
          </td>
<td>
              30.30.x where x (0-2)<br/>
              30.20.x where x (0-1)<br/>
              30.10.X where x (0-2)
            </td>
</tr>
<tr>
<td>MI325X<a href="#footnote1"><sup>[1]</sup></a></td>
<td>
              01.25.06.08<br/>
              01.25.04.02
          </td>
<td>
              30.30.x where x (0-2)<br/>
              30.20.x where x (0-1)<a href="#footnote1"><sup>[1]</sup></a><br/>
              30.10.X where x (0-2)<br/>
              6.4.z where z (0-3)<br/>
              6.3.3
          </td>
</tr>
<tr>
<td>MI300X<a href="#footnote2"><sup>[2]</sup></a></td>
<td>01.25.06.04<br/>
              01.25.03.12<br/>
              01.25.02.04</td>
<td rowspan="6" style="vertical-align: middle;">
              30.30.x where x (0-2)<br/>
              30.20.x where x (0-1)<br/>
              30.10.X where x (0-2)<br/>
              6.4.z where z (0–3)<br/>
              6.3.3
          </td>
<td>8.7.1.K</td>
</tr>
<tr>
<td>MI300A</td>
<td>BKC 26.1</td>
<td rowspan="3" style="vertical-align: middle;">Not Applicable</td>
</tr>
<tr>
<td>MI250X</td>
<td>IFWI 47 (or later)</td>
</tr>
<tr>
<td>MI250</td>
<td>MU5 w/ IFWI 75 (or later)</td>
</tr>
<tr>
<td>MI210</td>
<td>MU5 w/ IFWI 75 (or later)</td>
<td>8.7.1.K</td>
</tr>
<tr>
<td>MI100</td>
<td>VBIOS D3430401-037</td>
<td>Not Applicable</td>
</tr>
</table>
</div>
<p id="footnote1">[1]: For AMD Instinct MI325X KVM SR-IOV users, don't use AMD GPU driver (amdgpu) 30.20.0.</p>
<p id="footnote2">[2]: For AMD Instinct MI300X KVM SR-IOV with Multi-VF (8 VF) support requires a compatible firmware BKC bundle which will be released in coming months.</p>
</section>
<section id="hipblaslt-updates">
<h4>hipBLASLt updates<a class="headerlink" href="#hipblaslt-updates" title="Link to this heading">#</a></h4>
<p>hipBLASLt has improved performance for MXFP8 and MXFP4 GEMMs.</p>
</section>
<section id="deep-learning-and-ai-framework-updates">
<h4>Deep learning and AI framework updates<a class="headerlink" href="#deep-learning-and-ai-framework-updates" title="Link to this heading">#</a></h4>
<p>ROCm provides a comprehensive ecosystem for deep learning development. For more information, see <a class="reference internal" href="../how-to/deep-learning-rocm.html"><span class="std std-doc">Deep learning frameworks for ROCm</span></a> and the <a class="reference internal" href="../compatibility/compatibility-matrix.html"><span class="std std-doc">Compatibility
matrix</span></a> for the complete list of Deep learning and AI framework versions tested for compatibility with ROCm. AMD ROCm has officially updated support for the following Deep learning and AI frameworks:</p>
<section id="jax">
<h5>JAX<a class="headerlink" href="#jax" title="Link to this heading">#</a></h5>
<p>ROCm 7.2.1 enables support for JAX 0.8.2. For more information, see <a class="reference internal" href="../compatibility/ml-compatibility/jax-compatibility.html"><span class="std std-doc">JAX compatibility</span></a>.</p>
</section>
</section>
</section>
<section id="rocm-offline-installer-creator-discontinuation">
<h3>ROCm Offline Installer Creator discontinuation<a class="headerlink" href="#rocm-offline-installer-creator-discontinuation" title="Link to this heading">#</a></h3>
<p>The ROCm Offline Installer Creator is discontinued in ROCm 7.2.1. Equivalent installation capabilities are available through the ROCm Runfile Installer, a self-extracting installer that is not based on OS package managers. For more information, see <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.1/install/rocm-runfile-installer.html">ROCm Runfile Installer</a>.</p>
<section id="id3">
<h4>ROCm documentation updates<a class="headerlink" href="#id3" title="Link to this heading">#</a></h4>
<p>ROCm documentation continues to be updated to provide clearer and more comprehensive guidance for a wider range of user needs and use cases.</p>
<ul>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/">Tutorials for AI developers</a> have been expanded with the following two new tutorials:</p>
<ul class="simple">
<li><p>Pretraining tutorial: <a class="reference external" href="https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/pretrain/se3transform_intro.html">SE(3)-Transformer overview</a></p></li>
<li><p>Fine-tuning tutorial: <a class="reference external" href="https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/slime_qwen3_4B_GRPO.html">GRPO with slime</a></p></li>
</ul>
<p>For more information about the changes, see the <a class="reference external" href="https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/changelog.html">Changelog for the AI Developer Hub</a>.</p>
</li>
<li><p>HIP documentation has been expanded with additional context and in-depth explanations across several core topics in the Programming Guide section. The following topics have been significantly enhanced:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.1/understand/compilers.html">Compilers</a></p></li>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.1/understand/programming_model.html">Programming model</a></p></li>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.1/how-to/performance_guidelines.html">Performance guidelines</a></p></li>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.1/understand/performance_optimization.html">Performance optimization</a></p></li>
</ul>
</li>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/en/docs-7.2.1/reference/glossary.html">ROCm glossary</a> to provide concise definitions of AMD ROCm key terms and concepts has been added. The glossary is organized into:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://rocm.docs.amd.com/en/docs-7.2.1/reference/glossary/device-hardware.html">Device hardware glossary</a>: Provides brief definitions of hardware components and architectural features of AMD GPUs.</p></li>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/en/docs-7.2.1/reference/glossary/device-software.html">Device software glossary</a>: Provides brief definitions of software abstractions and programming models that run on AMD GPUs.</p></li>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/en/docs-7.2.1/reference/glossary/host-software.html">Host software glossary</a>: Provides brief definitions of development tools, compilers, libraries, and runtime environments for programming AMD GPUs.</p></li>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/en/docs-7.2.1/reference/glossary/performance.html">Performance glossary</a>: Provides brief definitions of performance analysis concepts and optimization techniques.</p></li>
</ul>
</li>
</ul>
</section>
</section>
<section id="rocm-components">
<h3>ROCm components<a class="headerlink" href="#rocm-components" title="Link to this heading">#</a></h3>
<p>The following table lists the versions of ROCm components for ROCm 7.2.1, including any version
changes from 7.2.0 to 7.2.1. Click the component’s updated version to go to a list of its changes.</p>
<p>Click <span class="fab fa-github"></span> to go to the component’s source code on GitHub.</p>
<div class="pst-scrollable-table-container">
<table class="table" id="rocm-rn-components">
<thead>
<tr>
<th>Category</th>
<th>Group</th>
<th>Name</th>
<th>Version</th>
<th></th>
</tr>
</thead>
<colgroup>
<col span="1"/>
<col span="1"/>
</colgroup>
<tbody class="rocm-components-libs rocm-components-ml">
<tr>
<th rowspan="9">Libraries</th>
<th rowspan="9">Machine learning and computer vision</th>
<td><a href="https://rocm.docs.amd.com/projects/composable_kernel/en/docs-7.2.1/index.html">Composable Kernel</a></td>
<td>1.2.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/composablekernel"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/AMDMIGraphX/en/docs-7.2.1/index.html">MIGraphX</a></td>
<td>2.15.0</td>
<td><a href="https://github.com/ROCm/AMDMIGraphX"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/MIOpen/en/docs-7.2.1/index.html">MIOpen</a></td>
<td>3.5.1</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/miopen"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/MIVisionX/en/docs-7.2.1/index.html">MIVisionX</a></td>
<td>3.5.0</td>
<td><a href="https://github.com/ROCm/MIVisionX"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocAL/en/docs-7.2.1/index.html">rocAL</a></td>
<td>2.5.0</td>
<td><a href="https://github.com/ROCm/rocAL"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocDecode/en/docs-7.2.1/index.html">rocDecode</a></td>
<td>1.5.0 ⇒ <a href="#rocdecode-1-7-0">1.7.0</a></td>
<td><a href="https://github.com/ROCm/rocDecode"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocJPEG/en/docs-7.2.1/index.html">rocJPEG</a></td>
<td>1.3.0 ⇒ <a href="#rocjpeg-1-4-0">1.4.0</a></td>
<td><a href="https://github.com/ROCm/rocJPEG"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocPyDecode/en/docs-7.2.1/index.html">rocPyDecode</a></td>
<td>0.8.0</td>
<td><a href="https://github.com/ROCm/rocPyDecode"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rpp/en/docs-7.2.1/index.html">RPP</a></td>
<td>2.2.0 ⇒ <a href="#rpp-2-2-1">2.2.1</a></td>
<td><a href="https://github.com/ROCm/rpp"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-libs rocm-components-communication tbody-reverse-zebra">
<tr>
<th rowspan="2"></th>
<th rowspan="2">Communication</th>
<td><a href="https://rocm.docs.amd.com/projects/rccl/en/docs-7.2.1/index.html">RCCL</a></td>
<td>2.27.7</td>
<td><a href="https://github.com/ROCm/rccl"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocSHMEM/en/docs-7.1.0/index.html">rocSHMEM</a></td>
<td>3.2.0 ⇒ <a href="#rocshmem-3-2-0">3.2.0</a></td>
<td><a href="https://github.com/ROCm/rocSHMEM"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-libs rocm-components-math tbody-reverse-zebra">
<tr>
<th rowspan="16"></th>
<th rowspan="16">Math</th>
<td><a href="https://rocm.docs.amd.com/projects/hipBLAS/en/docs-7.2.1/index.html">hipBLAS</a></td>
<td>3.2.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblas"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipBLASLt/en/docs-7.2.1/index.html">hipBLASLt</a></td>
<td>1.2.1 ⇒ <a href="#hipblaslt-1-2-2">1.2.2</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblaslt"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipFFT/en/docs-7.2.1/index.html">hipFFT</a></td>
<td>1.0.22</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipfft"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipfort/en/docs-7.2.1/index.html">hipfort</a></td>
<td>0.7.1</td>
<td><a href="https://github.com/ROCm/hipfort"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipRAND/en/docs-7.2.1/index.html">hipRAND</a></td>
<td>3.1.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hiprand"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipSOLVER/en/docs-7.2.1/index.html">hipSOLVER</a></td>
<td>3.2.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsolver"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipSPARSE/en/docs-7.2.1/index.html">hipSPARSE</a></td>
<td>4.2.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparse"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipSPARSELt/en/docs-7.2.1/index.html">hipSPARSELt</a></td>
<td>0.2.6</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparselt"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocALUTION/en/docs-7.2.1/index.html">rocALUTION</a></td>
<td>4.1.0</td>
<td><a href="https://github.com/ROCm/rocALUTION"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocBLAS/en/docs-7.2.1/index.html">rocBLAS</a></td>
<td>5.2.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocblas"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocFFT/en/docs-7.2.1/index.html">rocFFT</a></td>
<td>1.0.36</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocfft"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocRAND/en/docs-7.2.1/index.html">rocRAND</a></td>
<td>4.2.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocrand"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocSOLVER/en/docs-7.2.1/index.html">rocSOLVER</a></td>
<td>3.32.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocsolver"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocSPARSE/en/docs-7.2.1/index.html">rocSPARSE</a></td>
<td>4.2.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocsparse"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocWMMA/en/docs-7.2.1/index.html">rocWMMA</a></td>
<td>2.2.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocwmma"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/Tensile/en/docs-7.2.1/src/index.html">Tensile</a></td>
<td>4.45.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/shared/tensile"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-libs rocm-components-primitives tbody-reverse-zebra">
<tr>
<th rowspan="4"></th>
<th rowspan="4">Primitives</th>
<td><a href="https://rocm.docs.amd.com/projects/hipCUB/en/docs-7.2.1/index.html">hipCUB</a></td>
<td>4.2.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipcub"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipTensor/en/docs-7.2.1/index.html">hipTensor</a></td>
<td>2.2.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hiptensor"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocPRIM/en/docs-7.2.1/index.html">rocPRIM</a></td>
<td>4.2.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocprim"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocThrust/en/docs-7.2.1/index.html">rocThrust</a></td>
<td>4.2.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocthrust"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-tools rocm-components-system tbody-reverse-zebra">
<tr>
<th rowspan="7">Tools</th>
<th rowspan="7">System management</th>
<td><a href="https://rocm.docs.amd.com/projects/amdsmi/en/docs-7.2.1/index.html">AMD SMI</a></td>
<td>26.2.1 ⇒ <a href="#amd-smi-26-2-2">26.2.2</a></td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/amdsmi"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rdc/en/docs-7.2.1/index.html">ROCm Data Center Tool</a></td>
<td>1.2.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rdc/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocminfo/en/docs-7.2.1/index.html">rocminfo</a></td>
<td>1.0.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocminfo/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocm_smi_lib/en/docs-7.2.1/index.html">ROCm SMI</a></td>
<td>7.8.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocm-smi-lib/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/docs-7.2.1/index.html">ROCm Validation Suite</a></td>
<td>1.3.0</td>
<td><a href="https://github.com/ROCm/ROCmValidationSuite"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-tools rocm-components-perf">
<tr>
<th rowspan="6"></th>
<th rowspan="6">Performance</th>
<td><a href="https://rocm.docs.amd.com/projects/rocm_bandwidth_test/en/docs-7.2.1/index.html">ROCm Bandwidth
                        Test</a></td>
<td>2.6.0</td>
<td><a href="https://github.com/ROCm/rocm_bandwidth_test/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocprofiler-compute/en/docs-7.2.1/index.html">ROCm Compute Profiler</a></td>
<td>3.4.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocprofiler-compute"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocprofiler-systems/en/docs-7.2.1/index.html">ROCm Systems Profiler</a></td>
<td>1.3.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocprofiler-systems/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocprofiler/en/docs-7.2.1/index.html">ROCProfiler</a></td>
<td>2.0.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocprofiler/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/docs-7.2.1/index.html">ROCprofiler-SDK</a></td>
<td>1.1.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocprofiler-sdk/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/roctracer/en/docs-7.2.1/index.html">ROCTracer</a></td>
<td>4.1.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/roctracer/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-tools rocm-components-dev">
<tr>
<th rowspan="5"></th>
<th rowspan="5">Development</th>
<td><a href="https://rocm.docs.amd.com/projects/HIPIFY/en/docs-7.2.1/index.html">HIPIFY</a></td>
<td>22.0.0</td>
<td><a href="https://github.com/ROCm/HIPIFY/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/ROCdbgapi/en/docs-7.2.1/index.html">ROCdbgapi</a></td>
<td>0.77.4</td>
<td><a href="https://github.com/ROCm/ROCdbgapi/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/ROCmCMakeBuildTools/en/docs-7.2.1/index.html">ROCm CMake</a></td>
<td>0.14.0</td>
<td><a href="https://github.com/ROCm/rocm-cmake/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/ROCgdb/en/docs-7.2.1/index.html">ROCm Debugger (ROCgdb)</a>
</td>
<td>16.3</td>
<td><a href="https://github.com/ROCm/ROCgdb/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocr_debug_agent/en/docs-7.2.1/index.html">ROCr Debug Agent</a>
</td>
<td>2.1.0</td>
<td><a href="https://github.com/ROCm/rocr_debug_agent/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-compilers tbody-reverse-zebra">
<tr>
<th colspan="2" rowspan="2">Compilers</th>
<td><a href="https://rocm.docs.amd.com/projects/HIPCC/en/docs-7.2.1/index.html">HIPCC</a></td>
<td>1.1.1</td>
<td><a href="https://github.com/ROCm/llvm-project/tree/amd-staging/amd/hipcc"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/llvm-project/en/docs-7.2.1/index.html">llvm-project</a></td>
<td>22.0.0</td>
<td><a href="https://github.com/ROCm/llvm-project/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-runtimes tbody-reverse-zebra">
<tr>
<th colspan="2" rowspan="2">Runtimes</th>
<td><a href="https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.1/index.html">HIP</a></td>
<td>7.2.0 ⇒ <a href="#hip-7-2-1">7.2.1</a></td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/hip"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/ROCR-Runtime/en/docs-7.2.1/index.html">ROCr Runtime</a></td>
<td>1.18.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocr-runtime"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="detailed-component-changes">
<h3>Detailed component changes<a class="headerlink" href="#detailed-component-changes" title="Link to this heading">#</a></h3>
<p>The following sections describe key changes to ROCm components.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>For a historical overview of ROCm component updates, see the <a class="reference internal" href="../release/changelog.html"><span class="doc">ROCm consolidated changelog</span></a>.</p>
</div>
<section id="amd-smi-26-2-2">
<h4><strong>AMD SMI</strong> (26.2.2)<a class="headerlink" href="#amd-smi-26-2-2" title="Link to this heading">#</a></h4>
<section id="added">
<h5>Added<a class="headerlink" href="#added" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>GPU board and base board temperature sensors to <code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">monitor</span></code> command.</p></li>
</ul>
</section>
<section id="resolved-issues">
<h5>Resolved issues<a class="headerlink" href="#resolved-issues" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>JSON output was not formatted correctly when using watch mode with metrics.</p></li>
<li><p>Output was not properly redirected to file when using JSON format.</p></li>
<li><p>CPER component output was not redirected when using the <code class="docutils literal notranslate"><span class="pre">--follow</span></code> option.</p></li>
<li><p>Invalid CPER files caused garbage output for AFID lists.</p></li>
<li><p>JSON output was not formatted correctly for reset commands.</p></li>
</ul>
</section>
</section>
<section id="hip-7-2-1">
<h4><strong>HIP</strong> (7.2.1)<a class="headerlink" href="#hip-7-2-1" title="Link to this heading">#</a></h4>
<section id="id4">
<h5>Resolved issues<a class="headerlink" href="#id4" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Corrected the validation of stream capture in global‑capture mode. It is no longer affected by any thread‑local capture‑mode sequences occurring in other threads.</p></li>
<li><p>Corrected the return value of <code class="docutils literal notranslate"><span class="pre">hipEventQuery</span></code> and <code class="docutils literal notranslate"><span class="pre">hipEventSynchronize</span></code>. The HIP runtime now properly handles and restricts stream capture within these APIs.</p></li>
<li><p>Corrected an issue in the batch-dispatch doorbell for AQL packets to avoid a potential CPU hang.</p></li>
<li><p>To address potential delays in memory‑object destruction that could affect application logic, the HIP runtime disables memory‑object reference counting in direct‑dispatch mode.</p></li>
</ul>
</section>
<section id="changed">
<h5>Changed<a class="headerlink" href="#changed" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The <code class="docutils literal notranslate"><span class="pre">AMD_DIRECT_DISPATCH</span></code> environment variable has been deprecated in the HIP runtime.</p></li>
</ul>
</section>
</section>
<section id="hipblaslt-1-2-2">
<h4><strong>hipBLASLt</strong> (1.2.2)<a class="headerlink" href="#hipblaslt-1-2-2" title="Link to this heading">#</a></h4>
<section id="id5">
<h5>Changed<a class="headerlink" href="#id5" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Enumeration value update for the Sigmoid Activation Function feature.</p></li>
</ul>
</section>
</section>
<section id="rocdecode-1-7-0">
<h4><strong>rocDecode</strong> (1.7.0)<a class="headerlink" href="#rocdecode-1-7-0" title="Link to this heading">#</a></h4>
<section id="upcoming-changes">
<h5>Upcoming changes<a class="headerlink" href="#upcoming-changes" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The rocDecode GitHub repository will be officially moved to <a class="github reference external" href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocdecode">ROCm/rocm-systems</a> in an upcoming release.</p></li>
</ul>
</section>
</section>
<section id="rocjpeg-1-4-0">
<h4><strong>rocJPEG</strong> (1.4.0)<a class="headerlink" href="#rocjpeg-1-4-0" title="Link to this heading">#</a></h4>
<section id="id6">
<h5>Changed<a class="headerlink" href="#id6" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Bug fixes and performance improvements.</p></li>
</ul>
</section>
<section id="id7">
<h5>Upcoming changes<a class="headerlink" href="#id7" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>The rocJPEG GitHub repository will be officially moved to <a class="github reference external" href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocjpeg">ROCm/rocm-systems</a> in an upcoming release.</p></li>
</ul>
</section>
</section>
<section id="rocshmem-3-2-0">
<h4><strong>rocSHMEM</strong> (3.2.0)<a class="headerlink" href="#rocshmem-3-2-0" title="Link to this heading">#</a></h4>
<section id="id8">
<h5>Added<a class="headerlink" href="#id8" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Warnings to notify if large BAR is not available.</p></li>
</ul>
</section>
<section id="id9">
<h5>Resolved issues<a class="headerlink" href="#id9" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>GDA Backend will disable itself when no GDA compatible NICs are available rather than crashing.</p></li>
<li><p>Fix memory coherency issues on gfx1201.</p></li>
</ul>
</section>
<section id="known-issues">
<h5>Known issues<a class="headerlink" href="#known-issues" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Only 64-bit rocSHMEM atomic APIs are implemented for the GDA conduit.</p></li>
</ul>
</section>
</section>
<section id="rpp-2-2-1">
<h4><strong>RPP</strong> (2.2.1)<a class="headerlink" href="#rpp-2-2-1" title="Link to this heading">#</a></h4>
<section id="id10">
<h5>Added<a class="headerlink" href="#id10" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Error-code capture in test scripts for all C++ tests.</p></li>
</ul>
</section>
<section id="optimized">
<h5>Optimized<a class="headerlink" href="#optimized" title="Link to this heading">#</a></h5>
<ul class="simple">
<li><p>Optimized F16 variants by replacing scalar load/store operations with AVX2 intrinsics for spatter, log, blend, color_cast, flip, crop_mirror_normalize, and exposure kernels.</p></li>
</ul>
</section>
</section>
</section>
<section id="rocm-known-issues">
<h3>ROCm known issues<a class="headerlink" href="#rocm-known-issues" title="Link to this heading">#</a></h3>
<p>ROCm known issues are noted on <span class="fab fa-github"></span> <a class="reference external" href="https://github.com/ROCm/ROCm/labels/Verified%20Issue">GitHub</a>. For known
issues related to individual components, review the <a class="reference internal" href="#detailed-component-changes">Detailed component changes</a>.</p>
<section id="hipblaslt-performance-regression-for-specific-gemm-configurations">
<h4>hipBLASLt performance regression for specific GEMM configurations<a class="headerlink" href="#hipblaslt-performance-regression-for-specific-gemm-configurations" title="Link to this heading">#</a></h4>
<p>You might observe a noticeable performance regression if you’re using hipBLASLt with the following GPUs for LLMs with specific GEMM configurations:</p>
<section id="amd-instinct-mi300x-and-mi325x-gpus">
<h5>AMD Instinct MI300X and MI325X GPUs<a class="headerlink" href="#amd-instinct-mi300x-and-mi325x-gpus" title="Link to this heading">#</a></h5>
<p>Affected GEMM configurations:</p>
<ul class="simple">
<li><p>16384 × 16384 × 6656 (BBS, TN)</p></li>
<li><p>32768 × 8192 × 3072 (BBS, TN)</p></li>
<li><p>9728 × 8192 × 65536 (F8F8S, TN)</p></li>
</ul>
</section>
<section id="amd-instinct-mi350-series-gpus">
<h5>AMD Instinct MI350 Series GPUs<a class="headerlink" href="#amd-instinct-mi350-series-gpus" title="Link to this heading">#</a></h5>
<p>Affected GEMM configurations:</p>
<ul class="simple">
<li><p>4096 × 4096 × 1 × 8192</p></li>
<li><p>4096 × 4096 × 1 × 16384</p></li>
<li><p>8192 × 8192 × 1 × 8192</p></li>
<li><p>8192 × 8192 × 1 × 16384</p></li>
</ul>
<p>Due to this issue, you might also observe a slight increase in the test or inference time. This issue is resolved in the <span class="fab fa-github"></span><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblaslt">hipBLASLt develop branch</a> and will be part of a future ROCm release. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/6065">GitHub issue #6065</a>.</p>
</section>
</section>
</section>
<section id="longer-runtime-for-hipblaslt-gemm-operations-on-instinct-mi300x-gpus-in-partitioned-mode">
<h3>Longer runtime for hipBLASLt GEMM operations on Instinct MI300X GPUs in partitioned mode<a class="headerlink" href="#longer-runtime-for-hipblaslt-gemm-operations-on-instinct-mi300x-gpus-in-partitioned-mode" title="Link to this heading">#</a></h3>
<p>GEMM operations using hipBLASLt might result in longer runtime on AMD Instinct MI300X GPUs configured in CPX or NPS4 partition mode (38 control units or CUs). This issue occurs when hipBLASLt fails to find applicable pre-tuned kernels. As a result, it performs an extensive kernel search, which increases both search time and the overall operation runtime. This issue is resolved in the <span class="fab fa-github"></span><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblaslt">hipBLASLt develop branch</a> and will be part of a future ROCm release. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/6066">GitHub issue #6066</a>.</p>
</section>
<section id="roctracer-might-fail-to-report-kernel-operations">
<h3>ROCTracer might fail to report kernel operations<a class="headerlink" href="#roctracer-might-fail-to-report-kernel-operations" title="Link to this heading">#</a></h3>
<p>Applications that use <a class="reference external" href="https://rocm.docs.amd.com/projects/roctracer/en/latest/index.html">ROCTracer</a> might fail to receive some or all kernel operation events due to a ROCTracer reporting failure. ROCTracer is already deprecated and is scheduled to reach end of support (EoS) by the end of 2026 Q2. For more details on ROCTracer deprecation, see  <a class="reference internal" href="#roctracer-rocprofiler-rocprof-and-rocprofv2-deprecation"><span class="xref myst">ROCm upcoming changes</span></a>. This issue will be resolved in a future PyTorch on ROCm release that replaces ROCTracer with <a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/">ROCprofiler-SDK</a>. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/6102">GitHub issue #6102</a>.</p>
<section id="id11">
<h4>Longer runtime for hipBLASLt GEMM operations on Instinct MI300X GPUs in partitioned mode<a class="headerlink" href="#id11" title="Link to this heading">#</a></h4>
<p>GEMM operations using hipBLASLt might result in longer runtime on AMD Instinct MI300X GPUs configured in CPX or NPS4 partition mode (38 control units or CUs). This issue occurs when hipBLASLt fails to find applicable pre-tuned kernels. As a result, it performs an extensive kernel search, which increases both search time and the overall operation runtime. This issue is resolved in the <span class="fab fa-github"></span><a class="reference external" href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblaslt">hipBLASLt develop branch</a> and will be part of a future ROCm release. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/6066">GitHub issue #6066</a>.</p>
</section>
<section id="id12">
<h4>ROCTracer might fail to report kernel operations<a class="headerlink" href="#id12" title="Link to this heading">#</a></h4>
<p>Applications that use <a class="reference external" href="https://rocm.docs.amd.com/projects/roctracer/en/latest/index.html">ROCTracer</a> might fail to receive some or all kernel operation events due to a ROCTracer reporting failure. ROCTracer is already deprecated and is scheduled to reach end of support (EoS) by the end of 2026 Q2. For more details on ROCTracer deprecation, see  <a class="reference internal" href="#roctracer-rocprofiler-rocprof-and-rocprofv2-deprecation"><span class="xref myst">ROCm upcoming changes</span></a>. This issue will be resolved in a future PyTorch on ROCm release that replaces ROCTracer with <a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/">ROCprofiler-SDK</a>. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/6102">GitHub issue #6102</a>.</p>
</section>
</section>
<section id="rocm-resolved-issues">
<h3>ROCm resolved issues<a class="headerlink" href="#rocm-resolved-issues" title="Link to this heading">#</a></h3>
<p>The following are previously known issues resolved in this release. For resolved issues related to
individual components, review the <a class="reference internal" href="#detailed-component-changes">Detailed component changes</a>.</p>
<section id="increased-runtime-latency-of-the-hip-hipstreamcreate-api">
<h4>Increased runtime latency of the HIP hipStreamCreate API<a class="headerlink" href="#increased-runtime-latency-of-the-hip-hipstreamcreate-api" title="Link to this heading">#</a></h4>
<p>As issue that resulted in doubling of the runtime latency of the <a class="reference external" href="https://rocmdocs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html">HIP</a> <code class="docutils literal notranslate"><span class="pre">hipStreamCreate</span></code> API has been resolved. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/5978">GitHub issue #5978</a>.</p>
</section>
</section>
<section id="rocm-upcoming-changes">
<h3>ROCm upcoming changes<a class="headerlink" href="#rocm-upcoming-changes" title="Link to this heading">#</a></h3>
<p>The following changes to the ROCm software stack are anticipated for future releases.</p>
<section id="roctracer-rocprofiler-rocprof-and-rocprofv2-deprecation">
<h4>ROCTracer, ROCProfiler, rocprof, and rocprofv2 deprecation<a class="headerlink" href="#roctracer-rocprofiler-rocprof-and-rocprofv2-deprecation" title="Link to this heading">#</a></h4>
<p>ROCTracer, ROCProfiler, <code class="docutils literal notranslate"><span class="pre">rocprof</span></code>, and <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> are deprecated. It’s strongly recommended to upgrade to the latest version of the <a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/">ROCprofiler-SDK</a> library and the (<code class="docutils literal notranslate"><span class="pre">rocprofv3</span></code>) tool to ensure continued support and access to new features.</p>
<p>To learn about key feature improvements and benefits of ROCprofiler-SDK over the deprecated ROCProfiler and ROCTracer, see <a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/conceptual/comparing-with-legacy-tools.html">Comparing ROCprofiler-SDK to legacy ROCm profiling tools</a>.</p>
<p>It’s anticipated that ROCTracer, ROCProfiler, <code class="docutils literal notranslate"><span class="pre">rocprof</span></code>, and <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> will reach end of support (EoS) by the end of 2026 Q2.</p>
</section>
<section id="rocm-smi-deprecation">
<h4>ROCm SMI deprecation<a class="headerlink" href="#rocm-smi-deprecation" title="Link to this heading">#</a></h4>
<p><a class="reference external" href="https://github.com/ROCm/rocm_smi_lib">ROCm SMI</a> will be phased out in an
upcoming ROCm release and will enter maintenance mode. After this transition,
only critical bug fixes will be addressed and no further feature development
will take place.</p>
<p>It’s strongly recommended to transition your projects to <a class="reference external" href="https://github.com/ROCm/rocm-systems/tree/develop/projects/amdsmi">AMD
SMI</a>, the successor to ROCm SMI. AMD SMI
includes all the features of the ROCm SMI and will continue to receive regular
updates, new functionality, and ongoing support. For more information on AMD
SMI, see the <a class="reference external" href="https://rocm.docs.amd.com/projects/amdsmi/en/latest/">AMD SMI documentation</a>.</p>
</section>
<section id="changes-to-rocm-object-tooling">
<h4>Changes to ROCm Object Tooling<a class="headerlink" href="#changes-to-rocm-object-tooling" title="Link to this heading">#</a></h4>
<p>ROCm Object Tooling tools <code class="docutils literal notranslate"><span class="pre">roc-obj-ls</span></code>, <code class="docutils literal notranslate"><span class="pre">roc-obj-extract</span></code>, and <code class="docutils literal notranslate"><span class="pre">roc-obj</span></code> were
deprecated in ROCm 6.4, and will be removed in a future release. Functionality
has been added to the <code class="docutils literal notranslate"><span class="pre">llvm-objdump</span> <span class="pre">--offloading</span></code> tool option to extract all
clang-offload-bundles into individual code objects found within the objects
or executables passed as input.  The <code class="docutils literal notranslate"><span class="pre">llvm-objdump</span> <span class="pre">--offloading</span></code> tool option also
supports the <code class="docutils literal notranslate"><span class="pre">--arch-name</span></code> option, and only extracts code objects found with
the specified target architecture. See <a class="reference external" href="https://llvm.org/docs/CommandGuide/llvm-objdump.html">llvm-objdump</a>
for more information.</p>
</section>
</section>
</section>
</section>
</article>
<footer class="prev-next-footer d-print-none">
<div class="prev-next-area">
<a class="left-prev" href="../what-is-rocm.html" title="previous page">
<i class="fa-solid fa-angle-left"></i>
<div class="prev-next-info">
<p class="prev-next-subtitle">previous</p>
<p class="prev-next-title">What is ROCm?</p>
</div>
</a>
<a class="right-next" href="../compatibility/compatibility-matrix.html" title="next page">
<div class="prev-next-info">
<p class="prev-next-subtitle">next</p>
<p class="prev-next-title">Compatibility matrix</p>
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
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#release-highlights">Release highlights</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#roctracer-failure-to-report-kernel-operations-is-fixed">ROCTracer failure to report kernel operations is fixed</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#user-space-driver-and-firmware-dependent-changes">User space, driver, and firmware dependent changes</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-documentation-updates">ROCm documentation updates</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-7-2-1-release-notes">ROCm 7.2.1 release notes</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">Release highlights</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-hardware-operating-system-and-virtualization-changes">Supported hardware, operating system, and virtualization changes</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#virtualization-support">Virtualization support</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id2">User space, driver, and firmware dependent changes</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblaslt-updates">hipBLASLt updates</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#deep-learning-and-ai-framework-updates">Deep learning and AI framework updates</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#jax">JAX</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-offline-installer-creator-discontinuation">ROCm Offline Installer Creator discontinuation</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id3">ROCm documentation updates</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-components">ROCm components</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#detailed-component-changes">Detailed component changes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-smi-26-2-2"><strong>AMD SMI</strong> (26.2.2)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#added">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#resolved-issues">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-7-2-1"><strong>HIP</strong> (7.2.1)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id4">Resolved issues</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#changed">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblaslt-1-2-2"><strong>hipBLASLt</strong> (1.2.2)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id5">Changed</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocdecode-1-7-0"><strong>rocDecode</strong> (1.7.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#upcoming-changes">Upcoming changes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocjpeg-1-4-0"><strong>rocJPEG</strong> (1.4.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id6">Changed</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id7">Upcoming changes</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocshmem-3-2-0"><strong>rocSHMEM</strong> (3.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id8">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id9">Resolved issues</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#known-issues">Known issues</a></li>
</ul>
</li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rpp-2-2-1"><strong>RPP</strong> (2.2.1)</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#id10">Added</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#optimized">Optimized</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-known-issues">ROCm known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblaslt-performance-regression-for-specific-gemm-configurations">hipBLASLt performance regression for specific GEMM configurations</a><ul class="nav section-nav flex-column">
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi300x-and-mi325x-gpus">AMD Instinct MI300X and MI325X GPUs</a></li>
<li class="toc-h5 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-instinct-mi350-series-gpus">AMD Instinct MI350 Series GPUs</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#longer-runtime-for-hipblaslt-gemm-operations-on-instinct-mi300x-gpus-in-partitioned-mode">Longer runtime for hipBLASLt GEMM operations on Instinct MI300X GPUs in partitioned mode</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#roctracer-might-fail-to-report-kernel-operations">ROCTracer might fail to report kernel operations</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id11">Longer runtime for hipBLASLt GEMM operations on Instinct MI300X GPUs in partitioned mode</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id12">ROCTracer might fail to report kernel operations</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-resolved-issues">ROCm resolved issues</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#increased-runtime-latency-of-the-hip-hipstreamcreate-api">Increased runtime latency of the HIP hipStreamCreate API</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-upcoming-changes">ROCm upcoming changes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#roctracer-rocprofiler-rocprof-and-rocprofv2-deprecation">ROCTracer, ROCProfiler, rocprof, and rocprofv2 deprecation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-smi-deprecation">ROCm SMI deprecation</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#changes-to-rocm-object-tooling">Changes to ROCm Object Tooling</a></li>
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
<li><a href="https://rocm.docs.amd.com/en/latest/about/license.html">ROCm Licenses and Disclaimers</a></li>
<li><a href="https://www.amd.com/en/corporate/privacy" target="_blank">Privacy</a></li>
<li><a href="https://www.amd.com/en/corporate/trademarks" target="_blank">Trademarks</a></li>
<li><a href="https://www.amd.com/content/dam/amd/en/documents/corporate/cr/supply-chain-transparency.pdf" target="_blank">Supply Chain Transparency</a></li>
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
<span class="copyright">© 2026 Advanced Micro Devices, Inc</span>
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
