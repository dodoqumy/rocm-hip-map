---
title: "ROCm 7.2.0 release notes"
source_url: "https://rocm.docs.amd.com/en/docs-7.2.0/about/release-notes.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:02:27.708367+00:00
content_hash: "13af741658c8149d"
---


<!DOCTYPE html>

<html data-content_root="../" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/><meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>ROCm 7.2.0 release notes — ROCm Documentation</title>
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
<link href="../_static/custom.css?v=643846e8" rel="stylesheet" type="text/css"/>
<link href="../_static/rocm_header.css?v=9557e3d1" rel="stylesheet" type="text/css"/>
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
<script src="../_static/documentation_options.js?v=b4f5b7b3"></script>
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
<link href="https://rocm.docs.amd.com/en/docs-7.2.0/about/release-notes.html" rel="canonical"/>
<link href="https://www.amd.com/content/dam/code/images/favicon/favicon.ico" rel="icon"/>
<link href="../genindex.html" rel="index" title="Index"/>
<link href="../search.html" rel="search" title="Search"/>
<link href="../compatibility/compatibility-matrix.html" rel="next" title="Compatibility matrix"/>
<link href="../what-is-rocm.html" rel="prev" title="What is ROCm?"/>
<meta content="vo35SZt_GASsTHAEmdww7AYKPCvZyzLvOXBl8guBME4" name="google-site-verification"/>
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="advanced-micro-devices-demo" /><meta name="readthedocs-version-slug" content="docs-7.2.0" /><meta name="readthedocs-resolver-filename" content="/about/release-notes.html" /><meta name="readthedocs-http-status" content="200" /></head>
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
<a class="klavika-font hover-opacity" href="https://rocm.docs.amd.com/en/docs-7.2.0">ROCm™ Software 7.2.0</a>
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
<li class="toctree-l2"><a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-windows/en/docs-7.2.0/reference/system-requirements.html">Windows system requirements</a></li>
</ul>
</details></li>
</ul>
<p aria-level="2" class="caption" role="heading"><span class="caption-text">Install</span></p>
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/">ROCm on Linux</a></li>
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
<li class="toctree-l4"><a class="reference internal" href="../how-to/rocm-for-ai/training/benchmark-docker/megatron-lm.html">Train a model with Megatron-LM</a></li>
</ul>
</details></li>
<li class="toctree-l3 has-children"><a class="reference internal" href="../how-to/rocm-for-ai/training/benchmark-docker/primus-pytorch.html">Train a model with Primus and PyTorch</a><details><summary><span class="toctree-toggle" role="presentation"><i class="fa-solid fa-chevron-down"></i></span></summary><ul>
<li class="toctree-l4"><a class="reference internal" href="../how-to/rocm-for-ai/training/benchmark-docker/pytorch-training.html">Train a model with PyTorch</a></li>
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
<li class="toctree-l1"><a class="reference internal" href="../reference/rocm-tools.html">ROCm tools, compilers, and runtimes</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/gpu-arch-specs.html">GPU hardware specifications</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/gpu-atomics-operation.html">Hardware atomics operation support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/env-variables.html">Environment variables</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/precision-support.html">Data types and precision support</a></li>
<li class="toctree-l1"><a class="reference internal" href="../reference/graph-safe-support.html">Graph safe support</a></li>
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
<li aria-current="page" class="breadcrumb-item active">ROCm 7.2.0...</li>
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
<h1>ROCm 7.2.0 release notes</h1>
<!-- Table of contents -->
<div id="print-main-content">
<div id="jb-print-toc">
<div>
<h2> Contents </h2>
</div>
<nav aria-label="Page">
<ul class="visible nav section-nav flex-column">
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#release-highlights">Release highlights</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-hardware-operating-system-and-virtualization-changes">Supported hardware, operating system, and virtualization changes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#virtualization-support">Virtualization support</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#user-space-driver-and-firmware-dependent-changes">User space, driver, and firmware dependent changes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#node-power-management-for-multi-gpu-nodes-added">Node power management for multi-GPU nodes added</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#model-optimization-for-amd-instinct-mi350-series-gpus">Model optimization for AMD Instinct MI350 Series GPUs</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#model-optimization-for-amd-instinct-mi300x-gpus">Model optimization for AMD Instinct MI300X GPUs</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-runtime-performance-improvements">HIP runtime performance improvements</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#graph-node-scaling">Graph node scaling</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#back-memory-set-memset-optimization">Back memory set (memset) optimization</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#async-handler-performance-improvement">Async handler performance improvement</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-apis-added">HIP APIs added</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-library-management-apis">HIP library management APIs</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-occupancy-api">HIP occupancy API</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#stream-management-api">Stream management API</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#new-rocshmem-communication-gpudirect-async-gda-backend-conduit">New rocSHMEM communication GPUDirect Async (GDA) backend conduit</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#software-managed-plan-cache-support-for-hiptensor">Software-managed plan cache support for hipTensor</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#spir-v-support-added-to-hipcub-and-rocthrust">SPIR-V support added to hipCUB and rocThrust</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblaslt-updates">hipBLASLT updates</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-updates">rocWMMA updates</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#migraphx-updates">MIGraphX updates</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amdgpu-wavefront-size-macro-removal">AMDGPU wavefront size macro removal</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-rocm-simulation-introduced">AMD ROCm Simulation introduced</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-optiq-introduced">ROCm Optiq introduced</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-rocm-life-science-updates">AMD ROCm Life Science updates</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#deep-learning-and-ai-framework-updates">Deep learning and AI framework updates</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#jax">JAX</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#onnx-runtime">ONNX Runtime</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-offline-installer-creator-updates">ROCm Offline Installer Creator updates</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-runfile-installer-updates">ROCm Runfile Installer updates</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#expansion-of-the-rocm-examples-repository">Expansion of the ROCm examples repository</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-documentation-updates">ROCm documentation updates</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-components">ROCm components</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#detailed-component-changes">Detailed component changes</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-smi-26-2-1"><strong>AMD SMI</strong> (26.2.1)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#added">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#changed">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#resolved-issues">Resolved Issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#composable-kernel-1-2-0"><strong>Composable Kernel</strong> (1.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id2">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#upcoming-changes">Upcoming changes</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-7-2-0"><strong>HIP</strong> (7.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id3">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#optimized">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id4">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-3-2-0"><strong>hipBLAS</strong> (3.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id5">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblaslt-1-2-1"><strong>hipBLASLt</strong> (1.2.1)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id6">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id7">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-4-2-0"><strong>hipCUB</strong> (4.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id8">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id9">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-22"><strong>hipFFT</strong> (1.0.22)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id10">Added</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipify-22-0-0"><strong>HIPIFY</strong> (22.0.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id11">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id12">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-3-2-0"><strong>hipSOLVER</strong> (3.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id13">Added</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-4-2-0"><strong>hipSPARSE</strong> (4.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id14">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id15">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id16">Resolved Issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparselt-0-2-6"><strong>hipSPARSELt</strong> (0.2.6)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id17">Optimized</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hiptensor-2-2-0"><strong>hipTensor</strong> (2.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id18">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id19">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id20">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#llvm-project-22-0-0"><strong>llvm-project</strong> (22.0.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id21">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id22">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id23">Upcoming changes</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#migraphx-2-15-0"><strong>MIGraphX</strong> (2.15.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id24">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id25">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id26">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id27">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#miopen-3-5-1"><strong>MIOpen</strong> (3.5.1)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id28">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id29">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id30">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id31">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#mivisionx-3-5-0"><strong>MIVisionX</strong> (3.5.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id32">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id33">Resolved issues</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#known-issues">Known issues</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id34">Upcoming changes</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-2-27-7"><strong>RCCL</strong> (2.27.7)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id35">Changed</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocal-2-5-0"><strong>rocAL</strong> (2.5.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id36">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id37">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id38">Resolved issues</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id39">Known issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-4-1-0"><strong>rocALUTION</strong> (4.1.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id40">Added</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-5-2-0"><strong>rocBLAS</strong> (5.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id41">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id42">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id43">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocdecode-1-5-0"><strong>rocDecode</strong> (1.5.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id44">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id45">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id46">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-36"><strong>rocFFT</strong> (1.0.36)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id47">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id48">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocjpeg-1-3-0"><strong>rocJPEG</strong> (1.3.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id49">Changed</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-bandwidth-test-2-6-0"><strong>ROCm Bandwidth Test</strong> (2.6.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id50">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-compute-profiler-3-4-0"><strong>ROCm Compute Profiler</strong> (3.4.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id51">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id52">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#removed">Removed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id53">Resolved issues</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id54">Upcoming changes</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-systems-profiler-1-3-0"><strong>ROCm Systems Profiler</strong> (1.3.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id55">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id56">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id57">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-4-2-0"><strong>rocPRIM</strong> (4.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id58">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id59">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id60">Resolved issues</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id61">Known issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprofiler-sdk-1-1-0"><strong>ROCprofiler-SDK</strong> (1.1.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id62">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id63">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id64">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocpydecode-0-8-0"><strong>rocPyDecode</strong> (0.8.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id65">Changed</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-4-2-0"><strong>rocRAND</strong> (4.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id66">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id67">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id68">Removed</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocshmem-3-2-0"><strong>rocSHMEM</strong> (3.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id69">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id70">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id71">Known issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-32-0"><strong>rocSOLVER</strong> (3.32.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id72">Optimized</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-4-2-0"><strong>rocSPARSE</strong> (4.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id73">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id74">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id75">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id76">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-4-2-0"><strong>rocThrust</strong> (4.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id77">Added</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-2-2-0"><strong>rocWMMA</strong> (2.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id78">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id79">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id80">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rpp-2-2-0"><strong>RPP</strong> (2.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id81">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id82">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id83">Removed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id84">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-45-0"><strong>Tensile</strong> (4.45.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id85">Removed</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-known-issues">ROCm known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-multi-version-installation-might-cause-amd-smi-cli-failure">ROCm multi-version installation might cause amd-smi CLI failure</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#intermittent-errors-when-running-jax-workloads">Intermittent errors when running JAX workloads</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblaslt-performance-variation-for-a-particular-fp8-gemm-operation-on-amd-instinct-mi325x-gpus">hipBLASLt performance variation for a particular FP8 GEMM operation on AMD Instinct MI325X GPUs</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#increased-runtime-latency-of-the-hip-hipstreamcreate-api">Increased runtime latency of the HIP hipStreamCreate API</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-resolved-issues">ROCm resolved issues</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-performance-degradation-on-amd-instinct-mi300x-gpu-with-amd-pollara-ai-nic">RCCL performance degradation on AMD Instinct MI300X GPU with AMD Pollara AI NIC</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprofv3-fails-on-rpm-based-os-with-python-3-10-and-later">rocprofv3 fails on RPM-based OS with Python 3.10 (and later)</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#applications-using-opencv-might-fail-due-to-package-incompatibility-between-the-os">Applications using OpenCV might fail due to package incompatibility between the OS</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-smi-cli-triggers-repeated-kernel-errors-on-gpus-with-partitioning-support">AMD SMI CLI triggers repeated kernel errors on GPUs with partitioning support</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#incorrect-results-in-gemm-ex-operations-for-rocblas-and-hipblas">Incorrect results in gemm_ex operations for rocBLAS and hipBLAS</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#libva-based-applications-might-fail-after-rocm-installation">Libva-based applications might fail after ROCm installation</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-upcoming-changes">ROCm upcoming changes</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-offline-installer-creator-deprecation">ROCm Offline Installer Creator deprecation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-smi-deprecation">ROCm SMI deprecation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#roctracer-rocprofiler-rocprof-and-rocprofv2-deprecation">ROCTracer, ROCProfiler, rocprof, and rocprofv2 deprecation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#changes-to-rocm-object-tooling">Changes to ROCm Object Tooling</a></li>
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
<section class="tex2jax_ignore mathjax_ignore" id="rocm-7-2-0-release-notes">
<h1>ROCm 7.2.0 release notes<a class="headerlink" href="#rocm-7-2-0-release-notes" title="Link to this heading">#</a></h1><div class="sd-container-fluid sd-sphinx-override sd-p-0 sd-mt-2 sd-mb-4 sd-p-2 sd-rounded-1 docutils" id="rocm-docs-core-article-info">
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
                            2026-01-21
                        </p>
</div>
<div class="sd-col sd-col-auto sd-d-flex-row sd-align-minor-center docutils">
<p class="sd-p-0 sd-m-0" style="color:gray;">
<span class="sd-pr-2 article-info-read-time-svg">
<svg aria-hidden="true" class="sd-octicon sd-octicon-clock" height="16.0px" version="1.1" viewbox="0 0 16 16" width="16.0px">
<path d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zm.5 4.75a.75.75 0 00-1.5 0v3.5a.75.75 0 00.471.696l2.5 1a.75.75 0 00.557-1.392L8.5 7.742V4.75z" fill-rule="evenodd"></path>
</svg>
</span>
                            47 min read time
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

<p>The release notes provide a summary of notable changes since the previous ROCm release.</p>
<ul class="simple">
<li><p><a class="reference internal" href="#release-highlights">Release highlights</a></p></li>
<li><p><a class="reference internal" href="#supported-hardware-operating-system-and-virtualization-changes">Supported hardware, operating system, and virtualization changes</a></p></li>
<li><p><a class="reference internal" href="#user-space-driver-and-firmware-dependent-changes">User space, driver, and firmware dependent changes</a></p></li>
<li><p><a class="reference internal" href="#rocm-components">ROCm components versioning</a></p></li>
<li><p><a class="reference internal" href="#detailed-component-changes">Detailed component changes</a></p></li>
<li><p><a class="reference internal" href="#rocm-known-issues">ROCm known issues</a></p></li>
<li><p><a class="reference internal" href="#rocm-resolved-issues">ROCm resolved issues</a></p></li>
<li><p><a class="reference internal" href="#rocm-upcoming-changes">ROCm upcoming changes</a></p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If you’re using AMD Radeon GPUs or Ryzen APUs in a workstation setting with a display connected, see the <a class="reference external" href="https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html">Use ROCm on Radeon and Ryzen</a>
documentation to verify compatibility and system requirements.</p>
</div>
<section id="release-highlights">
<h2>Release highlights<a class="headerlink" href="#release-highlights" title="Link to this heading">#</a></h2>
<p>The following are notable new features and improvements in ROCm 7.2.0. For changes to individual components, see
<a class="reference internal" href="#detailed-component-changes">Detailed component changes</a>.</p>
<section id="supported-hardware-operating-system-and-virtualization-changes">
<h3>Supported hardware, operating system, and virtualization changes<a class="headerlink" href="#supported-hardware-operating-system-and-virtualization-changes" title="Link to this heading">#</a></h3>
<p>ROCm 7.2.0 adds support for RDNA4 architecture-based <a class="reference external" href="https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9600d.html">AMD Radeon AI PRO R9600D</a> and <a class="reference external" href="https://www.amd.com/en/products/graphics/desktops/radeon/9000-series/amd-radeon-rx-9060xt-lp.html">AMD Radeon RX 9060 XT LP</a>, and RDNA3 architecture-based <a class="reference external" href="https://www.amd.com/en/products/graphics/desktops/radeon/7000-series/amd-radeon-rx-7700.html">AMD Radeon RX 7700</a> GPUs.</p>
<p>ROCm 7.2.0 extends the SLES 15 SP7 operating system support to AMD Instinct MI355X and MI350X GPUs.</p>
<p>For more information about:</p>
<ul class="simple">
<li><p>AMD hardware, see <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/reference/system-requirements.html#supported-gpus">Supported GPUs (Linux)</a>.</p></li>
<li><p>Operating systems, see <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/reference/system-requirements.html#supported-operating-systems">Supported operating systems</a> and <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/">ROCm installation for Linux</a>.</p></li>
</ul>
<section id="virtualization-support">
<h4>Virtualization support<a class="headerlink" href="#virtualization-support" title="Link to this heading">#</a></h4>
<p>Virtualization support remains unchanged in this release. For more information, see  <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/reference/system-requirements.html#virtualization-support">Virtualization support</a>.</p>
</section>
</section>
<section id="user-space-driver-and-firmware-dependent-changes">
<h3>User space, driver, and firmware dependent changes<a class="headerlink" href="#user-space-driver-and-firmware-dependent-changes" title="Link to this heading">#</a></h3>
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
<td rowspan="9" style="vertical-align: middle;">ROCm 7.2.0</td>
<td>MI355X</td>
<td>
              01.25.17.07<br/>
              01.25.16.03
          </td>
<td>
              30.30.0<br/>
              30.20.1<br/>
              30.20.0<br/>
              30.10.2<br/>
              30.10.1<br/>
              30.10
            </td>
<td rowspan="3" style="vertical-align: middle;">8.7.0.K</td>
</tr>
<tr>
<td>MI350X</td>
<td>
              01.25.17.07<br/>
              01.25.16.03
          </td>
<td>
              30.30.0<br/>
              30.20.1<br/>
              30.20.0<br/>
              30.10.2<br/>
              30.10.1<br/>
              30.10
            </td>
</tr>
<tr>
<td>MI325X<a href="#footnote1"><sup>[1]</sup></a></td>
<td>
              01.25.04.02
          </td>
<td>30.30.0<br/>
              30.20.1<br/>
              30.20.0<a href="#footnote1"><sup>[1]</sup></a><br/>
              30.10.2<br/>
              30.10.1<br/>
              30.10<br/>
              6.4.z where z (0-3)<br/>
              6.3.y where y (2-3)
          </td>
</tr>
<tr>
<td>MI300X<a href="#footnote1"><sup>[2]</sup></a></td>
<td>01.25.03.12</td>
<td rowspan="6" style="vertical-align: middle;">
              30.30.0<br/>
              30.20.1<br/>
              30.20.0<br/>
              30.10.2<br/>
              30.10.1<br/>
              30.10<br/>
              6.4.z where z (0–3)<br/>
              6.3.y where y (2–3)<br/>
</td>
<td>8.7.0.K</td>
</tr>
<tr>
<td>MI300A</td>
<td>BKC 26</td>
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
<td>8.7.0.K</td>
</tr>
<tr>
<td>MI100</td>
<td>VBIOS D3430401-037</td>
<td>Not Applicable</td>
</tr>
</table>
</div>
<p id="footnote1">[1]: For AMD Instinct MI325X KVM SR-IOV users, don't use AMD GPU driver (amdgpu) 30.20.0.</p>
<p id="footnote1">[2]: For AMD Instinct MI300X KVM SR-IOV with Multi-VF (8 VF) support requires a compatible firmware BKC bundle which will be released in coming months.</p>
<section id="node-power-management-for-multi-gpu-nodes-added">
<h4>Node power management for multi-GPU nodes added<a class="headerlink" href="#node-power-management-for-multi-gpu-nodes-added" title="Link to this heading">#</a></h4>
<p>Node Power Management (NPM) optimizes power allocation and GPU frequency across multiple GPUs within a node using built-in telemetry and advanced control algorithms. It dynamically scales GPU frequencies to keep total node power within limits. Use AMD SMI to verify whether NPM is enabled and to check the node’s power allocation. This feature is supported on AMD Instinct MI355X and MI350X GPUs in both bare-metal and KVM SR-IOV virtual environments when paired with PLDM bundle 01.25.17.07. See the <a class="reference internal" href="#amdsmi-npm-changelog">AMD SMI changelog</a> for details.</p>
</section>
</section>
<section id="model-optimization-for-amd-instinct-mi350-series-gpus">
<h3>Model optimization for AMD Instinct MI350 Series GPUs<a class="headerlink" href="#model-optimization-for-amd-instinct-mi350-series-gpus" title="Link to this heading">#</a></h3>
<p>The following models have been optimized for AMD Instinct MI350 Series GPUs:</p>
<ul class="simple">
<li><p>Significant performance optimization has been achieved for the Llama 3.1 405B model on AMD Instinct MI355X GPUs, delivering enhanced throughput and reduced latency through kernel-level tuning and memory bandwidth improvements. These changes leverage MI355X’s advanced architecture to maximize efficiency for large-scale inference workloads.</p></li>
<li><p>Optimized Llama 3.1 405B model performance on AMD Instinct MI355X GPUs.</p></li>
<li><p>Optimized Llama 3 70B and Llama 2 70B model performance on AMD Instinct MI355X and MI350X GPUs.</p></li>
</ul>
</section>
<section id="model-optimization-for-amd-instinct-mi300x-gpus">
<h3>Model optimization for AMD Instinct MI300X GPUs<a class="headerlink" href="#model-optimization-for-amd-instinct-mi300x-gpus" title="Link to this heading">#</a></h3>
<p>The following models have been optimized for AMD Instinct MI300X GPUs:</p>
<ul class="simple">
<li><p>GEMM-level optimization for the GLM-4.6 model.</p></li>
<li><p>DeepEP performance improvements.</p></li>
</ul>
</section>
<section id="hip-runtime-performance-improvements">
<h3>HIP runtime performance improvements<a class="headerlink" href="#hip-runtime-performance-improvements" title="Link to this heading">#</a></h3>
<section id="graph-node-scaling">
<h4>Graph node scaling<a class="headerlink" href="#graph-node-scaling" title="Link to this heading">#</a></h4>
<p>HIP runtime now implements an optimized doorbell ring mechanism for certain graph execution topologies. It enables efficient batching of graph nodes. This enhancement provides better alignment with NVIDIA CUDA Graph optimizations.</p>
<p>HIP also adds a new performance test for HIP graphs with programmable topologies to measure graph performance across different structures. The test evaluates graph instantiation time, first-launch time, repeat launch times, and end-to-end execution for various graph topologies. The test implements comprehensive timing measurements, including CPU overhead and device execution time.</p>
</section>
<section id="back-memory-set-memset-optimization">
<h4>Back memory set (memset) optimization<a class="headerlink" href="#back-memory-set-memset-optimization" title="Link to this heading">#</a></h4>
<p>HIP runtime now implements a back memory set (memset) optimization to improve how <code class="docutils literal notranslate"><span class="pre">memset</span></code> nodes are processed during graph execution. This enhancement specifically handles varying numbers of AQL (Architected Queue Language) packets for <code class="docutils literal notranslate"><span class="pre">memset</span></code> graph node due to graph node set params for AQL batch submission approach.</p>
</section>
<section id="async-handler-performance-improvement">
<h4>Async handler performance improvement<a class="headerlink" href="#async-handler-performance-improvement" title="Link to this heading">#</a></h4>
<p>HIP runtime has removed the lock contention in async handler enqueue path. This enhancement reduces runtime overhead and maximizes GPU throughput, for asynchronous kernel execution, especially in multi-threaded applications.</p>
</section>
</section>
<section id="hip-apis-added">
<h3>HIP APIs added<a class="headerlink" href="#hip-apis-added" title="Link to this heading">#</a></h3>
<p>To simplify cross-platform programming and improve code portability between AMD ROCm and other programming models, new HIP APIs have been added in ROCm 7.2.0.</p>
<section id="hip-library-management-apis">
<h4>HIP library management APIs<a class="headerlink" href="#hip-library-management-apis" title="Link to this heading">#</a></h4>
<p>The following new HIP library management APIs have been added:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hipLibraryGetKernel</span></code>, gets a kernel from library.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipLibraryGetKernelCount</span></code>, gets kernel count in library.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipLibraryLoadData</span></code>, creates library object from code.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipLibraryLoadFromFile</span></code>, creates library object from file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipLibraryUnload</span></code>, unloads the library.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipKernelGetName</span></code>, returns function name for a hipKernel_t handle.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipKernelGetLibrary</span></code>, returns Library handle for a hipKernel_t handle.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipLibraryEnumerateKernels</span></code>, returns Kernel handles within a library.</p></li>
</ul>
</section>
<section id="hip-occupancy-api">
<h4>HIP occupancy API<a class="headerlink" href="#hip-occupancy-api" title="Link to this heading">#</a></h4>
<p><code class="docutils literal notranslate"><span class="pre">hipOccupancyAvailableDynamicSMemPerBlock</span></code> API is added to return dynamic shared memory available per block when launching with the number of blocks on CU.</p>
</section>
<section id="stream-management-api">
<h4>Stream management API<a class="headerlink" href="#stream-management-api" title="Link to this heading">#</a></h4>
<p>New Stream Management API <code class="docutils literal notranslate"><span class="pre">hipStreamCopyAttributes</span></code> is implemented for CUDA Parity improvement.</p>
</section>
</section>
<section id="new-rocshmem-communication-gpudirect-async-gda-backend-conduit">
<h3>New rocSHMEM communication GPUDirect Async (GDA) backend conduit<a class="headerlink" href="#new-rocshmem-communication-gpudirect-async-gda-backend-conduit" title="Link to this heading">#</a></h3>
<p>The rocSHMEM communications library has added the GDA (GPUDirect Async) intra-node and inter-node communication backend conduit.  This new backend enables communication between GPUs within a node or between nodes through a RNIC (RDMA NIC) using device-initiated GPU kernels to communicate with other GPUs.  The GPU directly interacts with the RNIC with no host (CPU) involvement in the critical path of communication.</p>
<p>In addition to the already supported GDA NIC types, Mellanox CX-7 and Broadcom Thor2, ROCm 7.2.0 introduces support for AMD Pensando AI NIC installed with the corresponding driver and firmware versions that support GDA functionality. For more information, see <a class="reference external" href="https://rocm.docs.amd.com/projects/rocSHMEM/en/docs-7.2.0/install.html">Installing rocSHMEM</a>.</p>
</section>
<section id="software-managed-plan-cache-support-for-hiptensor">
<h3>Software-managed plan cache support for hipTensor<a class="headerlink" href="#software-managed-plan-cache-support-for-hiptensor" title="Link to this heading">#</a></h3>
<p>Implemented software-managed plan cache. The Plan Cache main features include:</p>
<ul class="simple">
<li><p>Autotuning: You can automatically find the best implementation for the given problem and thereby increase performance.</p></li>
<li><p>The cache is implemented in a thread-safe manner and is shared across all threads that use the same <code class="docutils literal notranslate"><span class="pre">hiptensorHandle_t</span></code>.</p></li>
<li><p>Allows you to store the state of the cache to disk and reload it later.</p></li>
</ul>
<p>hipTensor has also been enhanced with:</p>
<ul class="simple">
<li><p>Addition of C API headers to enable compatibility with C programs.</p></li>
<li><p>Upgrade of C++ standard from <code class="docutils literal notranslate"><span class="pre">C++17</span></code> to <code class="docutils literal notranslate"><span class="pre">C++20</span></code>.</p></li>
</ul>
</section>
<section id="spir-v-support-added-to-hipcub-and-rocthrust">
<h3>SPIR-V support added to hipCUB and rocThrust<a class="headerlink" href="#spir-v-support-added-to-hipcub-and-rocthrust" title="Link to this heading">#</a></h3>
<p>hipCUB, rocRAND, and rocThrust support building with target-agonistic Standard Portable Intermediate Representation - V (SPIR-V). It is currently in an early access state.</p>
</section>
<section id="hipblaslt-updates">
<h3>hipBLASLT updates<a class="headerlink" href="#hipblaslt-updates" title="Link to this heading">#</a></h3>
<p>hipBLASLT has the following enhancements:</p>
<ul class="simple">
<li><p>Enabled support for hipBLASLtExt operation APIs on gfx11XX and gfx12XX LLVM target.</p></li>
<li><p>Expanded GEMM initialization with added support for uniform [0, 1] initialization for hipBLASLt GEMM operations.</p></li>
</ul>
</section>
<section id="rocwmma-updates">
<h3>rocWMMA updates<a class="headerlink" href="#rocwmma-updates" title="Link to this heading">#</a></h3>
<p>rocWMMA has the following enhancements:</p>
<ul class="simple">
<li><p>Support for gfx1150 LLVM target has been added.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perf_i8gemm</span></code> sample has been added to demonstrate <code class="docutils literal notranslate"><span class="pre">int8_t</span></code> as matrix input data type.</p></li>
</ul>
</section>
<section id="migraphx-updates">
<h3>MIGraphX updates<a class="headerlink" href="#migraphx-updates" title="Link to this heading">#</a></h3>
<p>MIGraphX has the following enhancements:</p>
<ul class="simple">
<li><p>rocMLIR has implemented support to generate MXFP8 and MXFP4 kernels.</p></li>
<li><p>MIGraphX now supports MXFP8 and MXFP4 operations.</p></li>
</ul>
</section>
<section id="amdgpu-wavefront-size-macro-removal">
<h3>AMDGPU wavefront size macro removal<a class="headerlink" href="#amdgpu-wavefront-size-macro-removal" title="Link to this heading">#</a></h3>
<p>The <code class="docutils literal notranslate"><span class="pre">__AMDGCN_WAVEFRONT_SIZE</span></code> and <code class="docutils literal notranslate"><span class="pre">__AMDGCN_WAVEFRONT_SIZE__</span></code> macros, which provided a compile-time-constant wavefront size, are removed. Where required, the wavefront size should instead be queried using the warpSize variable in device code, or using <code class="docutils literal notranslate"><span class="pre">hipGetDeviceProperties</span></code> in host code. Neither of these will result in a compile-time constant. For more information, see <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.0/how-to/hip_cpp_language_extensions.html#warpsize">warpSize</a>.
For cases where compile-time evaluation of the wavefront size cannot be avoided, uses of <code class="docutils literal notranslate"><span class="pre">__AMDGCN_WAVEFRONT_SIZE</span></code> or <code class="docutils literal notranslate"><span class="pre">__AMDGCN_WAVEFRONT_SIZE__</span></code> can be replaced with a user-defined macro or <code class="docutils literal notranslate"><span class="pre">constexpr</span></code> variable with the wavefront size(s) for the target hardware. For example:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="c1">#if defined(__GFX9__)</span>
<span class="c1">#define MY_MACRO_FOR_WAVEFRONT_SIZE 64</span>
<span class="c1">#else</span>
<span class="c1">#define MY_MACRO_FOR_WAVEFRONT_SIZE 32</span>
<span class="c1">#endif</span>
</pre></div>
</div>
</section>
<section id="amd-rocm-simulation-introduced">
<h3>AMD ROCm Simulation introduced<a class="headerlink" href="#amd-rocm-simulation-introduced" title="Link to this heading">#</a></h3>
<p>AMD ROCm Simulation is an open-source toolkit on the ROCm platform for high-performance, physics-based and numerical simulation on AMD GPUs. It brings scientific computing, computer graphics, robotics, and AI-driven simulation to AMD Instinct GPUs by unifying the HIP runtime, optimized math libraries, and PyTorch integration for high-throughput real-time and offline workloads.</p>
<p>The libraries span physics kernels, numerical solvers, rendering, and multi-GPU scaling, with Python-friendly APIs that plug into existing research and production pipelines. By using ROCm’s open-source GPU stack on AMD Instinct products, you gain optimized performance, flexible integration with Python and machine learning frameworks, and scalability across multi-GPU clusters and high-performance computing (HPC) environments.
For more information, see the <a class="reference external" href="https://rocm.docs.amd.com/projects/rocm-simulation/en/latest/index.html">ROCm Simulation documentation</a>.</p>
<p>The release in December 2025 introduced support for <a class="reference external" href="https://rocm.docs.amd.com/en/docs-7.0.0/">ROCm 7.0.0</a> for the two components:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://rocm.docs.amd.com/projects/taichi/en/docs-25.11/">Taichi Lang</a> is an open-source, imperative, parallel programming language for high-performance numerical computation. It is embedded in Python and uses just-in-time (JIT) compiler frameworks (such as LLVM) to offload the compute-intensive Python code to the native GPU or CPU instructions.</p></li>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/projects/gsplat/en/docs-25.11/">GSplat (Gaussian splatting)</a> is a highly efficient technique for real-time rendering of 3D scenes trained from a collection of multiview 2D images of the scene. It has emerged as an alternative to neural radiance fields (NeRFs), offering significant advantages in rendering speed while maintaining visual quality.</p></li>
</ul>
</section>
<section id="rocm-optiq-introduced">
<h3>ROCm Optiq introduced<a class="headerlink" href="#rocm-optiq-introduced" title="Link to this heading">#</a></h3>
<p>ROCm Optiq (Beta) is AMD’s next‑generation visualization platform designed to bring clarity to performance analysis. You can use the ROCm Optiq GUI to view trace files captured with the ROCm Systems Profiler on any supported Microsoft Windows or Linux system.</p>
<p>With ROCm Optiq, developers can pinpoint performance bottlenecks — from pipeline stalls and memory bandwidth limitations to suboptimal kernel launches. ROCm Optiq delivers a comprehensive, end‑to‑end view of system behavior, empowering teams to optimize their workflows by correlating GPU workloads with in‑application CPU events and hardware resource utilization. For more information, see the <a class="reference external" href="https://rocm.docs.amd.com/projects/roc-optiq/en/latest/">ROCm Optiq documentation</a>.</p>
</section>
<section id="amd-rocm-life-science-updates">
<h3>AMD ROCm Life Science updates<a class="headerlink" href="#amd-rocm-life-science-updates" title="Link to this heading">#</a></h3>
<p>The AMD ROCm Life Science (ROCm-LS) toolkit is a GPU-accelerated library suite developed for life science and healthcare applications, offering a robust set of tools optimized for AMD hardware. In December 2025, ROCm-LS transitioned from early access (EA) to general availability (GA).</p>
<p>The ROCm-LS GA release is marked with the transition of hipCIM from EA to production-ready and support for ROCm 7.0.x. For more information, see <a class="reference external" href="https://rocm.docs.amd.com/projects/rocm-ls/en/latest/about/release-notes.html">ROCm-LS 25.11 release notes</a>.</p>
</section>
<section id="deep-learning-and-ai-framework-updates">
<h3>Deep learning and AI framework updates<a class="headerlink" href="#deep-learning-and-ai-framework-updates" title="Link to this heading">#</a></h3>
<p>ROCm provides a comprehensive ecosystem for deep learning development. For more information, see <a class="reference internal" href="../how-to/deep-learning-rocm.html"><span class="std std-doc">Deep learning frameworks for ROCm</span></a> and the <a class="reference internal" href="../compatibility/compatibility-matrix.html"><span class="std std-doc">Compatibility
matrix</span></a> for the complete list of Deep learning and AI framework versions tested for compatibility with ROCm. AMD ROCm has officially updated support for the following Deep learning and AI frameworks:</p>
<section id="jax">
<h4>JAX<a class="headerlink" href="#jax" title="Link to this heading">#</a></h4>
<p>ROCm 7.2.0 enables support for JAX 0.8.0. For more information, see <a class="reference internal" href="../compatibility/ml-compatibility/jax-compatibility.html"><span class="std std-doc">JAX compatibility</span></a>.</p>
</section>
<section id="onnx-runtime">
<h4>ONNX Runtime<a class="headerlink" href="#onnx-runtime" title="Link to this heading">#</a></h4>
<p>ROCm 7.2.0 enables support for ONNX Runtime 1.23.2.</p>
</section>
</section>
<section id="rocm-offline-installer-creator-updates">
<h3>ROCm Offline Installer Creator updates<a class="headerlink" href="#rocm-offline-installer-creator-updates" title="Link to this heading">#</a></h3>
<p>The ROCm Offline Installer Creator 7.2.0 includes the following features and improvements:</p>
<ul class="simple">
<li><p>Changes to the AMDGPU driver version selection in the Driver Options menu. For drivers based on ROCm 7.0.0 and later, the AMDGPU version is now selected based on the driver versioning, such as 3x.yy.zz, and not the ROCm version.</p></li>
<li><p>Fixes for Oracle Linux 10.0 ROCm and driver minimum mode installer creation.</p></li>
<li><p>Added support for creating an offline installer for Oracle Linux 8, 9, and 10, where the kernel version of the target OS differs from the host OS creating the installer.</p></li>
</ul>
<p>See <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/install/rocm-offline-installer.html">ROCm Offline Installer Creator</a> for more information.</p>
</section>
<section id="rocm-runfile-installer-updates">
<h3>ROCm Runfile Installer updates<a class="headerlink" href="#rocm-runfile-installer-updates" title="Link to this heading">#</a></h3>
<p>The ROCm Runfile Installer 7.2.0 includes fixes for rocm-examples test script build issues.</p>
<p>For more information, see <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/install/rocm-runfile-installer.html">ROCm Runfile Installer</a>.</p>
</section>
<section id="expansion-of-the-rocm-examples-repository">
<h3>Expansion of the ROCm examples repository<a class="headerlink" href="#expansion-of-the-rocm-examples-repository" title="Link to this heading">#</a></h3>
<p>The <a class="reference external" href="https://github.com/ROCm/rocm-examples">ROCm examples repository</a> has been expanded with examples for the following ROCm components:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/amd-staging/Libraries/MIGraphX">MIGraphX</a></p></li>
<li><p><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/amd-staging/Libraries/MIVisionX">MIVisionX</a></p></li>
<li><p><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/amd-staging/Libraries/RCCL">RCCL</a></p></li>
<li><p><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/amd-staging/Libraries/rocCV">rocCV</a></p></li>
<li><p><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/amd-staging/Libraries/rocDecode">rocDecode</a></p></li>
<li><p><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/amd-staging/Libraries/rocJPEG">rocJPEG</a></p></li>
<li><p><a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/amd-staging/Libraries/RPP">RPP</a></p></li>
</ul>
<p>Usage examples are now available for the <a class="reference external" href="https://github.com/ROCm/rocm-examples/tree/amd-staging/Tools/ROCgdb">ROCgdb</a> debugger.</p>
</section>
<section id="rocm-documentation-updates">
<h3>ROCm documentation updates<a class="headerlink" href="#rocm-documentation-updates" title="Link to this heading">#</a></h3>
<p>ROCm documentation continues to be updated to provide clearer and more comprehensive guidance for a wider variety of user needs and use cases.</p>
<ul>
<li><p>The newest resource for ROCm and HIP developers is the <a class="reference external" href="https://rocm-handbook.amd.com/projects/amd-rocm-programming-guide/en/docs-7.2.0/">AMD ROCm Programming Guide</a>. This guide introduces the core concepts, APIs, and best practices for programming with ROCm and the HIP programming language. It provides hands-on guidance for writing GPU kernels, managing memory, optimizing performance, and integrating HIP with the broader AMD ROCm ecosystem of tools and libraries. The <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.0/index.html">HIP documentation</a> set continues to provide detailed information, tutorials, and reference content.</p></li>
<li><p>The HIP Programming Guide section includes a new topic titled <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.0/understand/performance_optimization.html">“Understanding GPU performance”</a>. It explains the theoretical foundations of GPU performance on AMD hardware. Understanding these concepts helps you analyze performance characteristics, identify bottlenecks, and make informed optimization decisions. Two other topics in this guide have been enhanced: <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.0/how-to/performance_guidelines.html">Performance guidelines</a> and <a class="reference external" href="https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.0/understand/hardware_implementation.html">Hardware implementation</a>.</p></li>
<li><p><a class="reference external" href="https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/">Tutorials for AI developers</a> have been expanded with the following two new tutorials:</p>
<ul class="simple">
<li><p>Fine-tuning tutorial: <a class="reference external" href="https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/qwen_image.html">Customize Qwen-Image with DiffSynth-Studio</a></p></li>
<li><p>GPU development and optimization tutorial: <a class="reference external" href="https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/gpu_dev_optimize/helion_gpu_kernel_dev.html">GPU kernel development and assessment with Helion</a></p></li>
</ul>
<p>For more information about the changes, see the <a class="reference external" href="https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/changelog.html">Changelog for the AI Developer Hub</a>.</p>
</li>
</ul>
</section>
</section>
<section id="rocm-components">
<h2>ROCm components<a class="headerlink" href="#rocm-components" title="Link to this heading">#</a></h2>
<p>The following table lists the versions of ROCm components for ROCm 7.2.0, including any version
changes from 7.1.1 to 7.2.0. Click the component’s updated version to go to a list of its changes.</p>
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
<td><a href="https://rocm.docs.amd.com/projects/composable_kernel/en/docs-7.2.0/index.html">Composable Kernel</a></td>
<td>1.1.0 ⇒ <a href="#composable-kernel-1-2-0">1.2.0</a></td>
<td><a href="https://github.com/ROCm/composable_kernel"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/AMDMIGraphX/en/docs-7.2.0/index.html">MIGraphX</a></td>
<td>2.14.0 ⇒ <a href="#migraphx-2-15-0">2.15.0</a></td>
<td><a href="https://github.com/ROCm/AMDMIGraphX"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/MIOpen/en/docs-7.2.0/index.html">MIOpen</a></td>
<td>3.5.1 ⇒ <a href="#miopen-3-5-1">3.5.1</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/miopen"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/MIVisionX/en/docs-7.2.0/index.html">MIVisionX</a></td>
<td>3.4.0 ⇒ <a href="#mivisionx-3-5-0">3.5.0</a></td>
<td><a href="https://github.com/ROCm/MIVisionX"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocAL/en/docs-7.2.0/index.html">rocAL</a></td>
<td>2.4.0 ⇒ <a href="#rocal-2-5-0">2.5.0</a></td>
<td><a href="https://github.com/ROCm/rocAL"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocDecode/en/docs-7.2.0/index.html">rocDecode</a></td>
<td>1.4.0 ⇒ <a href="#rocdecode-1-5-0">1.5.0</a></td>
<td><a href="https://github.com/ROCm/rocDecode"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocJPEG/en/docs-7.2.0/index.html">rocJPEG</a></td>
<td>1.2.0 ⇒ <a href="#rocjpeg-1-3-0">1.3.0</a></td>
<td><a href="https://github.com/ROCm/rocJPEG"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocPyDecode/en/docs-7.2.0/index.html">rocPyDecode</a></td>
<td>0.7.0 ⇒ <a href="#rocpydecode-0-8-0">0.8.0</a></td>
<td><a href="https://github.com/ROCm/rocPyDecode"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rpp/en/docs-7.2.0/index.html">RPP</a></td>
<td>2.1.0 ⇒ <a href="#rpp-2-2-0">2.2.0</a></td>
<td><a href="https://github.com/ROCm/rpp"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-libs rocm-components-communication tbody-reverse-zebra">
<tr>
<th rowspan="2"></th>
<th rowspan="2">Communication</th>
<td><a href="https://rocm.docs.amd.com/projects/rccl/en/docs-7.2.0/index.html">RCCL</a></td>
<td>2.27.7 ⇒ <a href="#rccl-2-27-7">2.27.7</a></td>
<td><a href="https://github.com/ROCm/rccl"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocSHMEM/en/docs-7.1.0/index.html">rocSHMEM</a></td>
<td>3.1.0 ⇒ <a href="#rocshmem-3-2-0">3.2.0</a></td>
<td><a href="https://github.com/ROCm/rocSHMEM"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-libs rocm-components-math tbody-reverse-zebra">
<tr>
<th rowspan="16"></th>
<th rowspan="16">Math</th>
<td><a href="https://rocm.docs.amd.com/projects/hipBLAS/en/docs-7.2.0/index.html">hipBLAS</a></td>
<td>3.1.0 ⇒ <a href="#hipblas-3-2-0">3.2.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblas"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipBLASLt/en/docs-7.2.0/index.html">hipBLASLt</a></td>
<td>1.1.0 ⇒ <a href="#hipblaslt-1-2-1">1.2.1</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblaslt"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipFFT/en/docs-7.2.0/index.html">hipFFT</a></td>
<td>1.0.21 ⇒ <a href="#hipfft-1-0-22">1.0.22</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipfft"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipfort/en/docs-7.2.0/index.html">hipfort</a></td>
<td>0.7.1</td>
<td><a href="https://github.com/ROCm/hipfort"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipRAND/en/docs-7.2.0/index.html">hipRAND</a></td>
<td>3.1.0</td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hiprand"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipSOLVER/en/docs-7.2.0/index.html">hipSOLVER</a></td>
<td>3.1.0 ⇒ <a href="#hipsolver-3-2-0">3.2.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsolver"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipSPARSE/en/docs-7.2.0/index.html">hipSPARSE</a></td>
<td>4.1.0 ⇒ <a href="#hipsparse-4-2-0">4.2.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparse"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipSPARSELt/en/docs-7.2.0/index.html">hipSPARSELt</a></td>
<td>0.2.5 ⇒ <a href="#hipsparselt-0-2-6">0.2.6</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsparselt"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocALUTION/en/docs-7.2.0/index.html">rocALUTION</a></td>
<td>4.0.1 ⇒ <a href="#rocalution-4-1-0">4.1.0</a></td>
<td><a href="https://github.com/ROCm/rocALUTION"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocBLAS/en/docs-7.2.0/index.html">rocBLAS</a></td>
<td>5.1.1 ⇒ <a href="#rocblas-5-2-0">5.2.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocblas"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocFFT/en/docs-7.2.0/index.html">rocFFT</a></td>
<td>1.0.35 ⇒ <a href="#rocfft-1-0-36">1.0.36</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocfft"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocRAND/en/docs-7.2.0/index.html">rocRAND</a></td>
<td>4.1.0 ⇒ <a href="#rocrand-4-2-0">4.2.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocrand"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocSOLVER/en/docs-7.2.0/index.html">rocSOLVER</a></td>
<td>3.31.0 ⇒ <a href="#rocsolver-3-32-0">3.32.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocsolver"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocSPARSE/en/docs-7.2.0/index.html">rocSPARSE</a></td>
<td>4.1.0 ⇒ <a href="#rocsparse-4-2-0">4.2.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocsparse"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocWMMA/en/docs-7.2.0/index.html">rocWMMA</a></td>
<td>2.1.0 ⇒ <a href="#rocwmma-2-2-0">2.2.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocwmma"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/Tensile/en/docs-7.2.0/src/index.html">Tensile</a></td>
<td>4.44.0 ⇒ <a href="#tensile-4-45-0">4.45.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/shared/tensile"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-libs rocm-components-primitives tbody-reverse-zebra">
<tr>
<th rowspan="4"></th>
<th rowspan="4">Primitives</th>
<td><a href="https://rocm.docs.amd.com/projects/hipCUB/en/docs-7.2.0/index.html">hipCUB</a></td>
<td>4.1.0 ⇒ <a href="#hipcub-4-2-0">4.2.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipcub"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/hipTensor/en/docs-7.2.0/index.html">hipTensor</a></td>
<td>2.0.0 ⇒ <a href="#hiptensor-2-2-0">2.2.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/hiptensor"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocPRIM/en/docs-7.2.0/index.html">rocPRIM</a></td>
<td>4.1.0 ⇒ <a href="#rocprim-4-2-0">4.2.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocprim"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocThrust/en/docs-7.2.0/index.html">rocThrust</a></td>
<td>4.1.0 ⇒ <a href="#rocthrust-4-2-0">4.2.0</a></td>
<td><a href="https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocthrust"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-tools rocm-components-system tbody-reverse-zebra">
<tr>
<th rowspan="7">Tools</th>
<th rowspan="7">System management</th>
<td><a href="https://rocm.docs.amd.com/projects/amdsmi/en/docs-7.2.0/index.html">AMD SMI</a></td>
<td>26.2.0 ⇒ <a href="#amd-smi-26-2-1">26.2.1</a></td>
<td><a href="https://github.com/ROCm/amdsmi/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rdc/en/docs-7.2.0/index.html">ROCm Data Center Tool</a></td>
<td>1.2.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rdc/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocminfo/en/docs-7.2.0/index.html">rocminfo</a></td>
<td>1.0.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocminfo/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocm_smi_lib/en/docs-7.2.0/index.html">ROCm SMI</a></td>
<td>7.8.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocm-smi-lib/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/docs-7.2.0/index.html">ROCm Validation Suite</a></td>
<td>1.3.0</td>
<td><a href="https://github.com/ROCm/ROCmValidationSuite"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-tools rocm-components-perf">
<tr>
<th rowspan="6"></th>
<th rowspan="6">Performance</th>
<td><a href="https://rocm.docs.amd.com/projects/rocm_bandwidth_test/en/docs-7.2.0/index.html">ROCm Bandwidth
                        Test</a></td>
<td>2.6.0 ⇒ <a href="#rocm-bandwidth-test-2-6-0">2.6.0</a></td>
<td><a href="https://github.com/ROCm/rocm_bandwidth_test/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocprofiler-compute/en/docs-7.2.0/index.html">ROCm Compute Profiler</a></td>
<td>3.3.1 ⇒ <a href="#rocm-compute-profiler-3-4-0">3.4.0</a></td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocprofiler-compute"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocprofiler-systems/en/docs-7.2.0/index.html">ROCm Systems Profiler</a></td>
<td>1.2.1 ⇒ <a href="#rocm-systems-profiler-1-3-0">1.3.0</a></td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocprofiler-systems/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocprofiler/en/docs-7.2.0/index.html">ROCProfiler</a></td>
<td>2.0.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocprofiler/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/docs-7.2.0/index.html">ROCprofiler-SDK</a></td>
<td>1.0.0 ⇒ <a href="#rocprofiler-sdk-1-1-0">1.1.0</a></td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocprofiler-sdk/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/roctracer/en/docs-7.2.0/index.html">ROCTracer</a></td>
<td>4.1.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/roctracer/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-tools rocm-components-dev">
<tr>
<th rowspan="5"></th>
<th rowspan="5">Development</th>
<td><a href="https://rocm.docs.amd.com/projects/HIPIFY/en/docs-7.2.0/index.html">HIPIFY</a></td>
<td>20.0.0 ⇒ <a href="#hipify-22-0-0">22.0.0</a></td>
<td><a href="https://github.com/ROCm/HIPIFY/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/ROCdbgapi/en/docs-7.2.0/index.html">ROCdbgapi</a></td>
<td>0.77.4</td>
<td><a href="https://github.com/ROCm/ROCdbgapi/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/ROCmCMakeBuildTools/en/docs-7.2.0/index.html">ROCm CMake</a></td>
<td>0.14.0</td>
<td><a href="https://github.com/ROCm/rocm-cmake/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/ROCgdb/en/docs-7.2.0/index.html">ROCm Debugger (ROCgdb)</a>
</td>
<td>16.3</td>
<td><a href="https://github.com/ROCm/ROCgdb/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/rocr_debug_agent/en/docs-7.2.0/index.html">ROCr Debug Agent</a>
</td>
<td>2.1.0</td>
<td><a href="https://github.com/ROCm/rocr_debug_agent/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-compilers tbody-reverse-zebra">
<tr>
<th colspan="2" rowspan="2">Compilers</th>
<td><a href="https://rocm.docs.amd.com/projects/HIPCC/en/docs-7.2.0/index.html">HIPCC</a></td>
<td>1.1.1</td>
<td><a href="https://github.com/ROCm/llvm-project/tree/amd-staging/amd/hipcc"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/llvm-project/en/docs-7.2.0/index.html">llvm-project</a></td>
<td>20.0.0 ⇒ <a href="#llvm-project-22-0-0">22.0.0</a></td>
<td><a href="https://github.com/ROCm/llvm-project/"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
<tbody class="rocm-components-runtimes tbody-reverse-zebra">
<tr>
<th colspan="2" rowspan="2">Runtimes</th>
<td><a href="https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.0/index.html">HIP</a></td>
<td>7.1.1 ⇒ <a href="#hip-7-2-0">7.2.0</a></td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/hip"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
<tr>
<td><a href="https://rocm.docs.amd.com/projects/ROCR-Runtime/en/docs-7.2.0/index.html">ROCr Runtime</a></td>
<td>1.18.0</td>
<td><a href="https://github.com/ROCm/rocm-systems/tree/develop/projects/rocr-runtime"><i class="fab fa-github fa-lg"></i></a></td>
</tr>
</tbody>
</table>
</div>
</section>
<section id="detailed-component-changes">
<h2>Detailed component changes<a class="headerlink" href="#detailed-component-changes" title="Link to this heading">#</a></h2>
<p>The following sections describe key changes to ROCm components.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>For a historical overview of ROCm component updates, see the <a class="reference internal" href="../release/changelog.html"><span class="doc">ROCm consolidated changelog</span></a>.</p>
</div>
<section id="amd-smi-26-2-1">
<h3><strong>AMD SMI</strong> (26.2.1)<a class="headerlink" href="#amd-smi-26-2-1" title="Link to this heading">#</a></h3>
<section id="added">
<h4>Added<a class="headerlink" href="#added" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>GPU and baseboard temperature options to <code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">monitor</span></code> CLI.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">monitor</span> <span class="pre">--gpu-board-temps</span></code> for GPU board temperature sensors.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">monitor</span> <span class="pre">--base-board-temps</span></code> for base board temperature sensors.</p></li>
</ul>
</li>
</ul>
<ul class="simple" id="amdsmi-npm-changelog">
<li><p>New Node Power Management (NPM) APIs and CLI options for node monitoring.</p>
<ul>
<li><p>C++ API functions:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_get_node_handle()</span></code> gets the handle for a node device.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_get_npm_info()</span></code> retrieves Node Power Management information.</p></li>
</ul>
</li>
<li><p>C++ types:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_npm_status_t</span></code> indicates whether NPM is enabled or disabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_npm_info_t</span></code> contains the status and node-level power limit in watts.</p></li>
</ul>
</li>
<li><p>Added Python API wrappers for new node device functions.</p></li>
<li><p>Added <code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">node</span></code> subcommand for NPM operations via CLI.</p></li>
<li><p>Currently supported for <code class="docutils literal notranslate"><span class="pre">OAM_ID</span> <span class="pre">0</span></code> only.</p></li>
</ul>
</li>
<li><p>The following C APIs are added to <code class="docutils literal notranslate"><span class="pre">amdsmi_interface.py</span></code>:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_get_cpu_handle()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_get_esmi_err_msg()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_get_gpu_event_notification()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_get_processor_count_from_handles()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_get_processor_handles_by_type()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_gpu_validate_ras_eeprom()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_init_gpu_event_notification()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_set_gpu_event_notification_mask()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_stop_gpu_event_notification()</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_get_gpu_busy_percent()</span></code></p></li>
</ul>
</li>
<li><p>Additional return value to <code class="docutils literal notranslate"><span class="pre">amdsmi_get_xgmi_plpd()</span></code> API:</p>
<ul>
<li><p>The entry <code class="docutils literal notranslate"><span class="pre">policies</span></code> is added to the end of the dictionary to match API definition.</p></li>
<li><p>The entry <code class="docutils literal notranslate"><span class="pre">plpds</span></code> is marked for deprecation as it has the same information as <code class="docutils literal notranslate"><span class="pre">policies</span></code>.</p></li>
</ul>
</li>
<li><p>PCIe levels to <code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">static</span> <span class="pre">--bus</span></code> command.</p>
<ul>
<li><p>The static <code class="docutils literal notranslate"><span class="pre">--bus</span></code> option has been updated to include the range of PCIe levels that you can set for a device.</p></li>
<li><p>Levels are a 2-tuple composed of the PCIe speed and bandwidth.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evicted_time</span></code> metric for KFD processes.</p>
<ul>
<li><p>Time that queues are evicted on a GPU in milliseconds.</p></li>
<li><p>Added to CLI in <code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">monitor</span> <span class="pre">-q</span></code> and <code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">process</span></code>.</p></li>
<li><p>Added to C APIs and Python APIs: <code class="docutils literal notranslate"><span class="pre">amdsmi_get_gpu_process_list()</span></code>, <code class="docutils literal notranslate"><span class="pre">amdsmi_get_gpu_compute_process_info()</span></code>
, and <code class="docutils literal notranslate"><span class="pre">amdsmi_get_gpu_compute_process_info_by_pid()</span></code>.</p></li>
</ul>
</li>
<li><p>New VRAM types to <code class="docutils literal notranslate"><span class="pre">amdsmi_vram_type_t</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">static</span> <span class="pre">--vram</span></code> and <code class="docutils literal notranslate"><span class="pre">amdsmi_get_gpu_vram_info()</span></code> now support the following types: <code class="docutils literal notranslate"><span class="pre">DDR5</span></code>, <code class="docutils literal notranslate"><span class="pre">LPDDR4</span></code>, <code class="docutils literal notranslate"><span class="pre">LPDDR5</span></code>, and <code class="docutils literal notranslate"><span class="pre">HBM3E</span></code>.</p></li>
</ul>
</li>
<li><p>Support for PPT1 power limit information.</p>
<ul>
<li><p>Support has been added for querying and setting the PPT (Package Power Tracking) limits.</p>
<ul>
<li><p>There are two PPT limits. PPT0 has lower limit and tracks a filtered version of the input power. PPT1 has higher limit but tracks the raw input power. This is to catch spikes in the raw data.</p></li>
</ul>
</li>
<li><p>New API added:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi_get_supported_power_cap()</span></code>: Returns power cap types supported on the device (PPT0, PPT1). This will allow you to know which power cap types you can get/set.</p></li>
<li><p>Original APIs remain the same but now can get/set both PPT0 and PPT1 limits (on supported hardware): <code class="docutils literal notranslate"><span class="pre">amdsmi_get_power_cap_info()</span></code> and <code class="docutils literal notranslate"><span class="pre">amdsmi_set_power_cap()</span></code>.</p></li>
</ul>
</li>
<li><p>See the Changed section for changes made to the <code class="docutils literal notranslate"><span class="pre">set</span></code> and <code class="docutils literal notranslate"><span class="pre">static</span></code> commands regarding support for PPT1.</p></li>
</ul>
</li>
</ul>
</section>
<section id="changed">
<h4>Changed<a class="headerlink" href="#changed" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>The <code class="docutils literal notranslate"><span class="pre">amd-smi</span></code> command now shows <code class="docutils literal notranslate"><span class="pre">hsmp</span></code> rather than <code class="docutils literal notranslate"><span class="pre">amd_hsmp</span></code>.</p>
<ul>
<li><p>The <code class="docutils literal notranslate"><span class="pre">hsmp</span></code> driver version can be shown without the <code class="docutils literal notranslate"><span class="pre">amdgpu</span></code> version using <code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">version</span> <span class="pre">-c</span></code>.</p></li>
</ul>
</li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">set</span> <span class="pre">--power-cap</span></code> command now requires specification of the power cap type.</p>
<ul>
<li><p>Command now takes the form: <code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">set</span> <span class="pre">--power-cap</span> <span class="pre">&lt;power-cap-type&gt;</span> <span class="pre">&lt;new-cap&gt;</span></code>.</p></li>
<li><p>Acceptable power cap types are “ppt0” and “ppt1”.</p></li>
</ul>
</li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">reset</span> <span class="pre">--power-cap</span></code> command will now attempt to reset both <code class="docutils literal notranslate"><span class="pre">PPT0</span></code> and <code class="docutils literal notranslate"><span class="pre">PPT1</span></code> power caps to their default values. If a device only has <code class="docutils literal notranslate"><span class="pre">PPT0</span></code>, then only <code class="docutils literal notranslate"><span class="pre">PPT0</span></code> will be reset.</p></li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">amd-smi</span> <span class="pre">static</span> <span class="pre">--limit</span></code> command now has a <code class="docutils literal notranslate"><span class="pre">PPT1</span></code> section when PPT1 is available. The <code class="docutils literal notranslate"><span class="pre">static</span> <span class="pre">--limit</span></code> command has been updated to include <code class="docutils literal notranslate"><span class="pre">PPT1</span></code> power limit information when available on the device.</p></li>
</ul>
</section>
<section id="resolved-issues">
<h4>Resolved Issues<a class="headerlink" href="#resolved-issues" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Fixed an issue where <code class="docutils literal notranslate"><span class="pre">amdsmi_get_gpu_od_volt_info()</span></code> returned a reference to a Python object. The returned dictionary was changed to return values in all fields.</p></li>
</ul>
</section>
</section>
<section id="composable-kernel-1-2-0">
<h3><strong>Composable Kernel</strong> (1.2.0)<a class="headerlink" href="#composable-kernel-1-2-0" title="Link to this heading">#</a></h3>
<section id="id1">
<h4>Added<a class="headerlink" href="#id1" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Support for mixed precision fp8 x bf8 universal GEMM and weight preshuffle GEMM.</p></li>
<li><p>Compute async pipeline in the CK Tile universal GEMM on gfx950.</p></li>
<li><p>Support for B Tensor type <code class="docutils literal notranslate"><span class="pre">pk_int4_t</span></code> in the CK Tile weight preshuffle GEMM.</p></li>
<li><p>New call to load different memory sizes to SGPR.</p></li>
<li><p>Support for B Tensor Preshuffle in CK Tile Grouped GEMM.</p></li>
<li><p>Basic copy kernel example and supporting documentation for new CK Tile developers.</p></li>
<li><p>Support for <code class="docutils literal notranslate"><span class="pre">grouped_gemm</span></code> kernels to perform <code class="docutils literal notranslate"><span class="pre">multi_d</span></code> elementwise operation.</p></li>
<li><p>Support for Multiple ABD GEMM.</p></li>
<li><p>Benchmarking support for tile engine GEMM Multi D.</p></li>
<li><p>Block scaling support in CK Tile GEMM, allowing flexible use of quantization matrices from either A or B operands.</p></li>
<li><p>Row-wise and column-wise quantization for CK Tile GEMM and grouped GEMM.</p></li>
<li><p>Support for <code class="docutils literal notranslate"><span class="pre">f32</span></code> to FMHA (fwd/bwd).</p></li>
<li><p>Tensor-wise quantization for CK Tile GEMM.</p></li>
<li><p>Support for batched contraction kernel.</p></li>
<li><p>WMMA (gfx12) support for FMHA.</p></li>
<li><p>Pooling kernel in CK Tile.</p></li>
<li><p>Top-k sigmoid kernel in CK Tile.</p></li>
<li><p>Blockscale 2D support for CK Tile GEMM.</p></li>
<li><p>An optional template parameter, <code class="docutils literal notranslate"><span class="pre">Arch</span></code>, to <code class="docutils literal notranslate"><span class="pre">make_kernel</span></code> to support linking multiple object files that have the same kernel compiled for different architectures.</p></li>
</ul>
</section>
<section id="id2">
<h4>Changed<a class="headerlink" href="#id2" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Removed <code class="docutils literal notranslate"><span class="pre">BlockSize</span></code> in <code class="docutils literal notranslate"><span class="pre">make_kernel</span></code> and <code class="docutils literal notranslate"><span class="pre">CShuffleEpilogueProblem</span></code> to support Wave32 in CK Tile.</p></li>
<li><p>FMHA examples and tests can be built for multiple architectures (gfx9, gfx950, gfx12) at the same time.</p></li>
</ul>
</section>
<section id="upcoming-changes">
<h4>Upcoming changes<a class="headerlink" href="#upcoming-changes" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Composable Kernel will be adopting C++20 features in an upcoming ROCm release, updating the minimum compiler requirement to C++20. Ensure that your development environment complies with this requirement to facilitate a seamless transition.</p></li>
<li><p>In an upcoming major ROCm release, Composable Kernel will transition to a header-only library. Neither ckProfiler nor the static libraries will be packaged with Composable Kernel. They will also no longer be built by default. ckProfiler can be built independently from Composable Kernel as a standalone binary, and the static Composable Kernel libraries can be built from source.</p></li>
</ul>
</section>
</section>
<section id="hip-7-2-0">
<h3><strong>HIP</strong> (7.2.0)<a class="headerlink" href="#hip-7-2-0" title="Link to this heading">#</a></h3>
<section id="id3">
<h4>Added<a class="headerlink" href="#id3" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>New HIP APIs</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hipLibraryEnumerateKernels</span></code> returns kernel handles within a library.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipKernelGetLibrary</span></code> returns library handle for a hipKernel_t handle.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipKernelGetName</span></code> returns function name for a hipKernel_t handle.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipLibraryLoadData</span></code> creates library object from code.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipLibraryLoadFromFile</span></code> creates library object from file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipLibraryUnload</span></code> unloads library.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipLibraryGetKernel</span></code> gets a kernel from the library.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipLibraryGetKernelCount</span></code> gets kernel count in library.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipStreamCopyAttributes</span></code> copies attributes from source stream to destination stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipOccupancyAvailableDynamicSMemPerBlock</span></code> returns dynamic shared memory available per block when launching numBlocks blocks on CU.</p></li>
</ul>
</li>
<li><p>New HIP flags</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hipMemLocationTypeHost</span></code> enables handling virtual memory management in host memory location, in addition to device memory.</p></li>
<li><p>Support for flags in <code class="docutils literal notranslate"><span class="pre">hipGetProcAddress</span></code> enables searching for the per-thread version symbols:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">HIP_GET_PROC_ADDRESS_DEFAULT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIP_GET_PROC_ADDRESS_LEGACY_STREAM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIP_GET_PROC_ADDRESS_PER_THREAD_DEFAULT_STREAM</span></code></p></li>
</ul>
</li>
</ul>
</li>
</ul>
</section>
<section id="optimized">
<h4>Optimized<a class="headerlink" href="#optimized" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Graph node scaling:</p>
<ul>
<li><p>HIP runtime implements an optimized doorbell ring mechanism for certain topologies of graph execution. It enables efficient batching of graph nodes.</p></li>
<li><p>The enhancement provides better alignment with CUDA Graph optimizations.</p></li>
<li><p>HIP also adds a new performance test for HIP graphs with programmable topologies to measure graph performance across different structures.</p></li>
<li><p>The test evaluates graph instantiation time, first launch time, repeat launch times, and end-to-end execution for various graph topologies.</p></li>
<li><p>The test implements comprehensive timing measurements including CPU overhead and device execution time.</p></li>
</ul>
</li>
<li><p>Back memory set (memset) optimization:</p>
<ul>
<li><p>HIP runtime now implements a back memory set (memset) optimization to improve how memset nodes are processed during graph execution.</p></li>
<li><p>The enhancement specifically handles varying number of Architected Queue Language (AQL) packets for memset graph node due to graph node set params for AQL batch submission approach.</p></li>
</ul>
</li>
<li><p>Async handler performance improvement:</p>
<ul>
<li><p>HIP runtime has removed the lock contention in async handler enqueue path.</p></li>
<li><ul>
<li><p>The enhancement reduces runtime overhead and maximizes GPU throughput for asynchronous kernel execution, especially in multi-threaded applications.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</section>
<section id="id4">
<h4>Resolved issues<a class="headerlink" href="#id4" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Corrected the calculation of the value of maximum shared memory per multiprocessor, in HIP device properties.</p></li>
</ul>
</section>
</section>
<section id="hipblas-3-2-0">
<h3><strong>hipBLAS</strong> (3.2.0)<a class="headerlink" href="#hipblas-3-2-0" title="Link to this heading">#</a></h3>
<section id="id5">
<h4>Resolved issues<a class="headerlink" href="#id5" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Corrected client memory use counts for the <code class="docutils literal notranslate"><span class="pre">HIPBLAS_CLIENT_RAM_GB_LIMIT</span></code> environment variable.</p></li>
<li><p>Fixed false Clang static analysis warnings.</p></li>
</ul>
</section>
</section>
<section id="hipblaslt-1-2-1">
<h3><strong>hipBLASLt</strong> (1.2.1)<a class="headerlink" href="#hipblaslt-1-2-1" title="Link to this heading">#</a></h3>
<section id="id6">
<h4>Added<a class="headerlink" href="#id6" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Support for the <code class="docutils literal notranslate"><span class="pre">BF16</span></code> input data type with an <code class="docutils literal notranslate"><span class="pre">FP32</span></code> output data type for gfx90a.</p></li>
<li><p>Support for hipBLASLtExt operation APIs on gfx11XX and gfx12XX.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">HIPBLASLT_OVERRIDE_COMPUTE_TYPE_XF32</span></code> to override the compute type from <code class="docutils literal notranslate"><span class="pre">xf32</span></code> to other compute types.</p></li>
<li><p>Support for the Sigmoid Activation function.</p></li>
</ul>
</section>
<section id="id7">
<h4>Resolved issues<a class="headerlink" href="#id7" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Fixed the <code class="docutils literal notranslate"><span class="pre">HIPBLAS_STATUS_INTERNAL_ERROR</span></code> issue that could occur with various sizes in CPX mode.</p></li>
</ul>
</section>
</section>
<section id="hipcub-4-2-0">
<h3><strong>hipCUB</strong> (4.2.0)<a class="headerlink" href="#hipcub-4-2-0" title="Link to this heading">#</a></h3>
<section id="id8">
<h4>Added<a class="headerlink" href="#id8" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Experimental SPIR-V support.</p></li>
</ul>
</section>
<section id="id9">
<h4>Resolved issues<a class="headerlink" href="#id9" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Fixed memory leak issues with some unit tests.</p></li>
</ul>
</section>
</section>
<section id="hipfft-1-0-22">
<h3><strong>hipFFT</strong> (1.0.22)<a class="headerlink" href="#hipfft-1-0-22" title="Link to this heading">#</a></h3>
<section id="id10">
<h4>Added<a class="headerlink" href="#id10" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>hipFFTW execution functions, where input and output data buffers differ from the
buffers specified at plan creation:</p>
<ul>
<li><p>fftw_execute_dft</p></li>
<li><p>fftwf_execute_dft</p></li>
<li><p>fftw_execute_dft_r2c</p></li>
<li><p>fftwf_execute_dft_r2c</p></li>
<li><p>fftw_execute_dft_c2r</p></li>
<li><p>fftwf_execute_dft_c2r</p></li>
</ul>
</li>
</ul>
</section>
</section>
<section id="hipify-22-0-0">
<h3><strong>HIPIFY</strong> (22.0.0)<a class="headerlink" href="#hipify-22-0-0" title="Link to this heading">#</a></h3>
<section id="id11">
<h4>Added<a class="headerlink" href="#id11" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Partial support for CUDA 13.0.0 support.</p></li>
<li><p>cuDNN 9.14.0 support.</p></li>
<li><p>cuTENSOR 2.3.1.0 support.</p></li>
<li><p>LLVM 21.1.6 support.</p></li>
<li><p>Full <code class="docutils literal notranslate"><span class="pre">hipFFTw</span></code> support.</p></li>
<li><p><a class="reference external" href="https://github.com/ROCm/HIPIFY/issues/2062">#2062</a> Partial hipification support for a particular CUDA API.</p></li>
<li><p><a class="reference external" href="https://github.com/ROCm/HIPIFY/issues/2073">#2073</a> Detect CUDA version before hipification.</p></li>
<li><p>New options:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--local-headers</span></code> to enable hipification of quoted local headers (non-recursive).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">--local-headers-recursive</span></code> to enable hipification of quoted local headers recursively.</p></li>
</ul>
</li>
</ul>
</section>
<section id="id12">
<h4>Resolved issues<a class="headerlink" href="#id12" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p><a class="reference external" href="https://github.com/ROCm/HIPIFY/issues/2088">#2088</a> Missing support of <code class="docutils literal notranslate"><span class="pre">cuda_bf16.h</span></code> import in hipification.</p></li>
</ul>
</section>
</section>
<section id="hipsolver-3-2-0">
<h3><strong>hipSOLVER</strong> (3.2.0)<a class="headerlink" href="#hipsolver-3-2-0" title="Link to this heading">#</a></h3>
<section id="id13">
<h4>Added<a class="headerlink" href="#id13" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Ability to control rocSOLVER logging using the environment variables <code class="docutils literal notranslate"><span class="pre">ROCSOLVER_LEVELS</span></code> and <code class="docutils literal notranslate"><span class="pre">ROCSOLVER_LAYER</span></code>.</p></li>
</ul>
</section>
</section>
<section id="hipsparse-4-2-0">
<h3><strong>hipSPARSE</strong> (4.2.0)<a class="headerlink" href="#hipsparse-4-2-0" title="Link to this heading">#</a></h3>
<section id="id14">
<h4>Added<a class="headerlink" href="#id14" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">--clients-only</span></code> option to the <code class="docutils literal notranslate"><span class="pre">install.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">rmake.py</span></code> scripts for building only the clients when using a version of hipSPARSE that is already installed.</p></li>
</ul>
</section>
<section id="id15">
<h4>Optimized<a class="headerlink" href="#id15" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Improved the user documentation.</p></li>
</ul>
</section>
<section id="id16">
<h4>Resolved Issues<a class="headerlink" href="#id16" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Fixed a memory leak in the <code class="docutils literal notranslate"><span class="pre">hipsparseCreate</span></code> functions.</p></li>
</ul>
</section>
</section>
<section id="hipsparselt-0-2-6">
<h3><strong>hipSPARSELt</strong> (0.2.6)<a class="headerlink" href="#hipsparselt-0-2-6" title="Link to this heading">#</a></h3>
<section id="id17">
<h4>Optimized<a class="headerlink" href="#id17" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Provided more kernels for the <code class="docutils literal notranslate"><span class="pre">FP16</span></code> and <code class="docutils literal notranslate"><span class="pre">FP8(E4M3)</span></code> data types.</p></li>
</ul>
</section>
</section>
<section id="hiptensor-2-2-0">
<h3><strong>hipTensor</strong> (2.2.0)<a class="headerlink" href="#hiptensor-2-2-0" title="Link to this heading">#</a></h3>
<section id="id18">
<h4>Added<a class="headerlink" href="#id18" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Software-managed plan cache support.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hiptensorHandleWritePlanCacheToFile</span></code> to write the plan cache of a hipTensor handle to a file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hiptensorHandleReadPlanCacheFromFile</span></code> to read a plan cache from a file into a hipTensor handle.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">simple_contraction_plan_cache</span></code> to demonstrate plan cache usages.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">plan_cache_test</span></code> to test the plan cache across various tensor ranks.</p></li>
<li><p>C API headers to enable compatibility with C programs.</p></li>
<li><p>A CMake function to allow projects to query architecture support.</p></li>
<li><p>An option to configure the memory layout for tests and benchmarks.</p></li>
</ul>
</section>
<section id="id19">
<h4>Changed<a class="headerlink" href="#id19" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>hipTensor has been moved into the new rocm-libraries “monorepo” repository <span class="fab fa-github"></span> <a class="reference external" href="https://github.com/ROCm/rocm-libraries">rocm-libraries</a>. This repository consolidates a number of separate ROCm libraries and shared components.</p>
<ul>
<li><p>The repository migration requires a few changes to the CMake configuration of hipTensor.</p></li>
</ul>
</li>
<li><p>Updated C++ standard from C++17 to C++20.</p></li>
<li><p>Include files <code class="docutils literal notranslate"><span class="pre">hiptensor/hiptensor.hpp</span></code> and <code class="docutils literal notranslate"><span class="pre">hiptensor/hiptensor_types.hpp</span></code> are now deprecated. Use <code class="docutils literal notranslate"><span class="pre">hiptensor/hiptensor.h</span></code> and <code class="docutils literal notranslate"><span class="pre">hiptensor/hiptensor_types.h</span></code> instead.</p></li>
<li><p>Converted include guards from #ifndef/#define/#endif to #pragma once.</p></li>
</ul>
</section>
<section id="id20">
<h4>Resolved issues<a class="headerlink" href="#id20" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Removed large tensor sizes causing problem in benchmarks.</p></li>
</ul>
</section>
</section>
<section id="llvm-project-22-0-0">
<h3><strong>llvm-project</strong> (22.0.0)<a class="headerlink" href="#llvm-project-22-0-0" title="Link to this heading">#</a></h3>
<section id="id21">
<h4>Added<a class="headerlink" href="#id21" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Enabled ThinLTO for ROCm compilers using <code class="docutils literal notranslate"><span class="pre">-foffload-lto=thin</span></code>. For more information, see <a class="reference external" href="https://rocm.docs.amd.com/projects/llvm-project/en/docs-7.2.0/reference/rocmcc.html#amd-gpu-compilation">ROCm compiler reference</a>.</p></li>
</ul>
</section>
<section id="id22">
<h4>Changed<a class="headerlink" href="#id22" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Updated clang/llvm to AMD clang version 22.0.0 (equivalent to LLVM 22.0.0 with additional out-of-tree patches).</p></li>
</ul>
</section>
<section id="id23">
<h4>Upcoming changes<a class="headerlink" href="#id23" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>As of ROCm 7.2.0, the <a class="reference external" href="https://rocm.docs.amd.com/projects/HIPCC/en/docs-7.2.0/index.html">HIPCC</a> compiler is deprecated. HIPCC now invokes <a class="reference external" href="https://rocm.docs.amd.com/projects/llvm-project/en/docs-7.2.0/index.html">AMD Clang</a>. It’s recommended that you now invoke AMD Clang directly rather than using HIPCC. There isn’t any expected impact on usability, functionality, or performance when invoking AMD Clang directly. In a future ROCm release, HIPCC will become a symbolic link to AMD Clang.</p></li>
</ul>
</section>
</section>
<section id="migraphx-2-15-0">
<h3><strong>MIGraphX</strong> (2.15.0)<a class="headerlink" href="#migraphx-2-15-0" title="Link to this heading">#</a></h3>
<section id="id24">
<h4>Added<a class="headerlink" href="#id24" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>MXFP4 support for Quark and Brevitas quantized models.</p></li>
<li><p>Dynamic shape support for <code class="docutils literal notranslate"><span class="pre">DepthToSpace</span> <span class="pre">Op</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bias</span></code> and <code class="docutils literal notranslate"><span class="pre">key_mask_padding</span></code> inputs for the <code class="docutils literal notranslate"><span class="pre">MultiHeadAttention</span></code> operator.</p></li>
<li><p>GEMM+GEMM fusions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dim_params</span></code> input parameter to the <code class="docutils literal notranslate"><span class="pre">parse_onnx</span></code> Python call.</p></li>
<li><p>Created an API to query supported ONNX Operators <code class="docutils literal notranslate"><span class="pre">get_onnx_operators()</span></code>.</p></li>
<li><p>Right pad masking mode for Multihead Attention.</p></li>
<li><p>Support for Flash Decoding.</p></li>
<li><p>Torch-MIGraphX installation instructions.</p></li>
<li><p>Operator Builders with supporting documentation.</p></li>
<li><p>Index range check to the Gather operator.</p></li>
</ul>
</section>
<section id="id25">
<h4>Changed<a class="headerlink" href="#id25" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Updated the Resize operator to support linear mode for Dynamic shapes.</p></li>
<li><p>Switched to <code class="docutils literal notranslate"><span class="pre">--input-dim</span></code> instead of <code class="docutils literal notranslate"><span class="pre">--batch</span></code>  to set any dynamic dimensions when using <code class="docutils literal notranslate"><span class="pre">migraphx-driver</span></code>.</p></li>
<li><p>Different stride sizes are now supported in ONNX <code class="docutils literal notranslate"><span class="pre">if</span></code> branches.</p></li>
<li><p>ONNX version change to 1.18.0 to support PyTorch 2.9.1.</p></li>
<li><p>Refactored <code class="docutils literal notranslate"><span class="pre">GroupQueryAttention</span></code>.</p></li>
<li><p>Enabled <code class="docutils literal notranslate"><span class="pre">PipelineRepoRef</span></code> parameter in CI.</p></li>
<li><p>Hide LLVM symbols that come from ROCmlir and provide option for stripping in release mode.</p></li>
<li><p>Model compilation failures now produce an mxr file for debugging the failure.</p></li>
<li><p>Bumped SQlite3 to 3.50.4.</p></li>
</ul>
</section>
<section id="id26">
<h4>Optimized<a class="headerlink" href="#id26" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Converted the <code class="docutils literal notranslate"><span class="pre">LRN</span></code> operator to an optimized <code class="docutils literal notranslate"><span class="pre">pooling</span></code> operator.</p></li>
<li><p>Streamlined the <code class="docutils literal notranslate"><span class="pre">find_matches</span></code> function.</p></li>
<li><p>Reduced the number of splits used for <code class="docutils literal notranslate"><span class="pre">split_reduce</span></code>.</p></li>
<li><p>Improved layout propagation in pointwise fusion when using broadcasted inputs.</p></li>
</ul>
</section>
<section id="id27">
<h4>Resolved issues<a class="headerlink" href="#id27" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Quiet nrvo and noreturn warnings.</p></li>
<li><p>Fixed <code class="docutils literal notranslate"><span class="pre">pointwise:</span> <span class="pre">Wrong</span> <span class="pre">number</span> <span class="pre">of</span> <span class="pre">arguments</span></code> error when quantizing certain models to <code class="docutils literal notranslate"><span class="pre">int8</span></code>.</p></li>
<li><p>TopK exception bugfix.</p></li>
<li><p>Updated SD3 example for change in optimum-onnx[onnxruntime].</p></li>
<li><p>Fixed an issue with Torch-MIGraphX where the model compilation would fail.</p></li>
<li><p>Fixed an issue where a reduction was broadcast with different dimensions than the input.</p></li>
<li><p>Resolved a path name issue stopping some files being created on Windows for debugging.</p></li>
<li><p>Fixed “reduce_sum: axes: value out of range” error in <code class="docutils literal notranslate"><span class="pre">simplify_reshapes</span></code>.</p></li>
<li><p>Updated README <code class="docutils literal notranslate"><span class="pre">rbuild</span></code> installation instructions to use Python venv to avoid warning.</p></li>
<li><p>Ensured directories exist when generating files for debugging.</p></li>
<li><p>Resolved a compilation hang issue.</p></li>
</ul>
</section>
</section>
<section id="miopen-3-5-1">
<h3><strong>MIOpen</strong> (3.5.1)<a class="headerlink" href="#miopen-3-5-1" title="Link to this heading">#</a></h3>
<section id="id28">
<h4>Added<a class="headerlink" href="#id28" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>3D heuristics for gfx950.</p></li>
<li><p>Optional timestamps to MIOpen logging.</p></li>
<li><p>Option to log when MIOpen starts and finishes tuning.</p></li>
<li><p>Winograd Fury 4.6.0 for gfx12 for improved convolution performance.</p></li>
</ul>
</section>
<section id="id29">
<h4>Changed<a class="headerlink" href="#id29" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Ported several OCL kernels to HIP.</p></li>
</ul>
</section>
<section id="id30">
<h4>Optimized<a class="headerlink" href="#id30" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Improved Composable Kernel (CK) kernel selection during tuning.</p></li>
<li><p>Improved user DB file locking to better handle network storage.</p></li>
<li><p>Improved performance for MIOpen check numerics capabilities.</p></li>
</ul>
</section>
<section id="id31">
<h4>Resolved issues<a class="headerlink" href="#id31" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Addressed an issue in the stride adjustment logic for ASM (MISA) kernels when the output dimension is one.</p></li>
<li><p>Fixed an issue with the CK bwd solver applicability checks when deterministic is set.</p></li>
<li><p>[BatchNorm] Fixed issue where batchnorm tuning would give incorrect results.</p></li>
<li><p>Fixed issue where generic search was not providing sufficient warm-up for some kernels.</p></li>
</ul>
</section>
</section>
<section id="mivisionx-3-5-0">
<h3><strong>MIVisionX</strong> (3.5.0)<a class="headerlink" href="#mivisionx-3-5-0" title="Link to this heading">#</a></h3>
<section id="id32">
<h4>Changed<a class="headerlink" href="#id32" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>AMD Clang++ location updated to <code class="docutils literal notranslate"><span class="pre">${ROCM_PATH}/lib/llvm/bin</span></code>.</p></li>
<li><p>Required RPP version updated to RPP V2.2.1.</p></li>
</ul>
</section>
<section id="id33">
<h4>Resolved issues<a class="headerlink" href="#id33" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Memory leaks in OpenVX core, vx_nn, &amp; vx_opencv.</p></li>
</ul>
</section>
<section id="known-issues">
<h4>Known issues<a class="headerlink" href="#known-issues" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Installation on RedHat and SLES requires the manual installation of the FFmpeg and OpenCV dev packages.</p></li>
</ul>
</section>
<section id="id34">
<h4>Upcoming changes<a class="headerlink" href="#id34" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>VX_AMD_MEDIA - <code class="docutils literal notranslate"><span class="pre">rocDecode</span></code> and <code class="docutils literal notranslate"><span class="pre">rocJPEG</span></code> support for hardware decode.</p></li>
</ul>
</section>
</section>
<section id="rccl-2-27-7">
<h3><strong>RCCL</strong> (2.27.7)<a class="headerlink" href="#rccl-2-27-7" title="Link to this heading">#</a></h3>
<section id="id35">
<h4>Changed<a class="headerlink" href="#id35" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>RCCL error messages have been made more verbose in several cases. RCCL now prints out fatal error messages by default. Fatal error messages can be suppressed by setting <code class="docutils literal notranslate"><span class="pre">NCCL_DEBUG=NONE</span></code>.</p></li>
<li><p>Disabled <code class="docutils literal notranslate"><span class="pre">reduceCopyPacks</span></code> pipelining for <code class="docutils literal notranslate"><span class="pre">gfx950</span></code>.</p></li>
</ul>
</section>
</section>
<section id="rocal-2-5-0">
<h3><strong>rocAL</strong> (2.5.0)<a class="headerlink" href="#rocal-2-5-0" title="Link to this heading">#</a></h3>
<section id="id36">
<h4>Added<a class="headerlink" href="#id36" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">EnumRegistry</span></code> to register all the enums present in rocAL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">Argument</span></code> class which stores the value and type of each argument in the Node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">PipelineOperator</span></code> class to represent operators in the pipeline with metadata.</p></li>
<li><p>Support to track operators in MasterGraph with unique naming.</p></li>
</ul>
</section>
<section id="id37">
<h4>Changed<a class="headerlink" href="#id37" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>OpenCL backend support is deprecated.</p></li>
<li><p>CXX Compiler: Use AMDClang++ compiler core location <code class="docutils literal notranslate"><span class="pre">${ROCM_PATH}/lib/llvm/bin</span></code>.</p></li>
<li><p>Refactored external enum usage in rocAL to maintain separation between external and internal enums.</p></li>
<li><p>Introduced the following enums <code class="docutils literal notranslate"><span class="pre">ResizeScalingMode</span></code>, <code class="docutils literal notranslate"><span class="pre">ResizeInterpolationType</span></code>, <code class="docutils literal notranslate"><span class="pre">MelScaleFormula</span></code>, <code class="docutils literal notranslate"><span class="pre">AudioBorderType</span></code>, and <code class="docutils literal notranslate"><span class="pre">OutOfBoundsPolicy</span></code> in <code class="docutils literal notranslate"><span class="pre">commons.h</span></code>.</p></li>
</ul>
</section>
<section id="id38">
<h4>Resolved issues<a class="headerlink" href="#id38" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Use HIP memory for fused crop rocJPEG decoder.</p></li>
<li><p>Issue in numpy loader where ROI is updated incorrectly.</p></li>
<li><p>Issue in CropResize node where <code class="docutils literal notranslate"><span class="pre">crop_w</span></code> and <code class="docutils literal notranslate"><span class="pre">crop_h</span></code> values were not correctly updated.</p></li>
</ul>
</section>
<section id="id39">
<h4>Known issues<a class="headerlink" href="#id39" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Package installation on SLES requires manually installing <code class="docutils literal notranslate"><span class="pre">TurboJPEG</span></code>.</p></li>
<li><p>Package installation on RedHat and SLES requires manually installing the FFmpeg dev package.</p></li>
</ul>
</section>
</section>
<section id="rocalution-4-1-0">
<h3><strong>rocALUTION</strong> (4.1.0)<a class="headerlink" href="#rocalution-4-1-0" title="Link to this heading">#</a></h3>
<section id="id40">
<h4>Added<a class="headerlink" href="#id40" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">--clients-only</span></code> option to the <code class="docutils literal notranslate"><span class="pre">install.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">rmake.py</span></code> scripts to allow building only the clients while using an already installed version of rocALUTION.</p></li>
</ul>
</section>
</section>
<section id="rocblas-5-2-0">
<h3><strong>rocBLAS</strong> (5.2.0)<a class="headerlink" href="#rocblas-5-2-0" title="Link to this heading">#</a></h3>
<section id="id41">
<h4>Added<a class="headerlink" href="#id41" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Level 3 <code class="docutils literal notranslate"><span class="pre">syrk_ex</span></code> function for both C and FORTRAN, without API support for the ILP64 format.</p></li>
</ul>
</section>
<section id="id42">
<h4>Optimized<a class="headerlink" href="#id42" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Level 2 <code class="docutils literal notranslate"><span class="pre">tpmv</span></code> and <code class="docutils literal notranslate"><span class="pre">sbmv</span></code> functions.</p></li>
</ul>
</section>
<section id="id43">
<h4>Resolved issues<a class="headerlink" href="#id43" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Corrected client memory use counts for the <code class="docutils literal notranslate"><span class="pre">ROCBLAS_CLIENT_RAM_GB_LIMIT</span></code> environment variable.</p></li>
<li><p>Fixed false Clang static analysis warnings.</p></li>
</ul>
</section>
</section>
<section id="rocdecode-1-5-0">
<h3><strong>rocDecode</strong> (1.5.0)<a class="headerlink" href="#rocdecode-1-5-0" title="Link to this heading">#</a></h3>
<section id="id44">
<h4>Added<a class="headerlink" href="#id44" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Logging control. Message output from the core components is now controlled by the logging level threshold, which can be set by an environment variable or other methods.</p></li>
<li><p>The new <code class="docutils literal notranslate"><span class="pre">rocdecode-host</span></code> package must be installed to use the FFmpeg decoder.</p></li>
</ul>
</section>
<section id="id45">
<h4>Changed<a class="headerlink" href="#id45" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Updated <code class="docutils literal notranslate"><span class="pre">libdrm</span></code> path configuration and <code class="docutils literal notranslate"><span class="pre">libva</span></code> version requirements for ROCm and TheRock platforms.</p></li>
</ul>
</section>
<section id="id46">
<h4>Resolved issues<a class="headerlink" href="#id46" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Fixed the build error with videodecodepicfiles sample.</p></li>
<li><p>Added error handling of sample app command option combination of memory type OUT_SURFACE_MEM_NOT_MAPPED and MD5 generation.</p></li>
</ul>
</section>
</section>
<section id="rocfft-1-0-36">
<h3><strong>rocFFT</strong> (1.0.36)<a class="headerlink" href="#rocfft-1-0-36" title="Link to this heading">#</a></h3>
<section id="id47">
<h4>Optimized<a class="headerlink" href="#id47" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Removed a potentially unnecessary global transpose operation from MPI 3D multi-GPU pencil decompositions.</p></li>
<li><p>Enabled optimization of 3D pencil decompositions for single-process multi-GPU transforms.</p></li>
</ul>
</section>
<section id="id48">
<h4>Resolved issues<a class="headerlink" href="#id48" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Fixed potential division by zero when constructing plans using dimensions of length 1.</p></li>
<li><p>Fixed result scaling on multi-device transforms.</p></li>
<li><p>Fixed callbacks on multi-device transforms.</p></li>
</ul>
</section>
</section>
<section id="rocjpeg-1-3-0">
<h3><strong>rocJPEG</strong> (1.3.0)<a class="headerlink" href="#rocjpeg-1-3-0" title="Link to this heading">#</a></h3>
<section id="id49">
<h4>Changed<a class="headerlink" href="#id49" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Updated <code class="docutils literal notranslate"><span class="pre">libdrm</span></code> path configuration and <code class="docutils literal notranslate"><span class="pre">libva</span></code> version requirements for ROCm and TheRock platforms.</p></li>
<li><p>RHEL now uses <code class="docutils literal notranslate"><span class="pre">libva-devel</span></code> instead of <code class="docutils literal notranslate"><span class="pre">libva-amdgpu</span></code>/<code class="docutils literal notranslate"><span class="pre">libva-amdgpu-devel</span></code>.</p></li>
<li><p>Use ROCm clang++ from <code class="docutils literal notranslate"><span class="pre">${ROCM_PATH}/lib/llvm/bin</span></code> location.</p></li>
</ul>
</section>
</section>
<section id="rocm-bandwidth-test-2-6-0">
<h3><strong>ROCm Bandwidth Test</strong> (2.6.0)<a class="headerlink" href="#rocm-bandwidth-test-2-6-0" title="Link to this heading">#</a></h3>
<section id="id50">
<h4>Resolved issues<a class="headerlink" href="#id50" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rocm-bandwidth-test</span></code> folder is no longer present after driver uninstallation.</p></li>
</ul>
</section>
</section>
<section id="rocm-compute-profiler-3-4-0">
<h3><strong>ROCm Compute Profiler</strong> (3.4.0)<a class="headerlink" href="#rocm-compute-profiler-3-4-0" title="Link to this heading">#</a></h3>
<section id="id51">
<h4>Added<a class="headerlink" href="#id51" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">--list-blocks</span> <span class="pre">&lt;arch&gt;</span></code> option to general options. It lists the available IP blocks on the specified arch (similar to <code class="docutils literal notranslate"><span class="pre">--list-metrics</span></code>). However, cannot be used with <code class="docutils literal notranslate"><span class="pre">--block</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">config_delta/gfx950_diff.yaml</span></code> to analysis config YAMLs to track the revision between the gfx9xx GPUs against the latest supported gfx950 GPUs.</p></li>
<li><p>Analysis db features</p>
<ul>
<li><p>Adds support for per kernel metrics analysis.</p></li>
<li><p>Adds support for dispatch timeline analysis.</p></li>
<li><p>Shows duration as median in addition to mean in kernel view.</p></li>
</ul>
</li>
<li><p>AMDGPU driver info and GPU VRAM attributes in the system info section of the analysis report.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">CU</span> <span class="pre">Utilization</span></code> metric to display the percentage of CUs utilized during kernel execution.</p></li>
</ul>
</section>
<section id="id52">
<h4>Changed<a class="headerlink" href="#id52" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">-b/--block</span></code> accepts block alias(es). See block aliases using command-line option <code class="docutils literal notranslate"><span class="pre">--list-blocks</span> <span class="pre">&lt;arch&gt;</span></code>.</p></li>
<li><p>Analysis configs YAMLs are now managed with the new config management workflow in <code class="docutils literal notranslate"><span class="pre">tools/config_management/</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">amdsmi</span></code> python API is used instead of <code class="docutils literal notranslate"><span class="pre">amd-smi</span></code> CLI to query GPU specifications.</p></li>
<li><p>Empty cells replaced with <code class="docutils literal notranslate"><span class="pre">N/A</span></code> for unavailable metrics in analysis.</p></li>
</ul>
</section>
<section id="removed">
<h4>Removed<a class="headerlink" href="#removed" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Removed <code class="docutils literal notranslate"><span class="pre">database</span></code> mode from ROCm Compute Profiler in favor of other visualization methods, rather than Grafana and MongoDB integration, such as the upcoming Analysis DB-based Visualizer.</p>
<ul>
<li><p>Plotly server based standalone GUI.</p></li>
<li><p>Commandline based Textual User Interface.</p></li>
</ul>
</li>
</ul>
</section>
<section id="id53">
<h4>Resolved issues<a class="headerlink" href="#id53" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Fixed issue of sL1D metric values displaying as <code class="docutils literal notranslate"><span class="pre">N/A</span></code> in memory chart diagram.</p></li>
</ul>
</section>
<section id="id54">
<h4>Upcoming changes<a class="headerlink" href="#id54" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">Active</span> <span class="pre">CUs</span></code> metric has been deprecated in favor of <code class="docutils literal notranslate"><span class="pre">CU</span> <span class="pre">Utilization</span></code> and will be removed in a future release.</p></li>
</ul>
</section>
</section>
<section id="rocm-systems-profiler-1-3-0">
<h3><strong>ROCm Systems Profiler</strong> (1.3.0)<a class="headerlink" href="#rocm-systems-profiler-1-3-0" title="Link to this heading">#</a></h3>
<section id="id55">
<h4>Added<a class="headerlink" href="#id55" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ROCPROFSYS_PERFETTO_FLUSH_PERIOD_MS</span></code> configuration setting to set the flush period for Perfetto traces. The default value is 10000 ms (10 seconds).</p></li>
<li><p>Fetching of the <code class="docutils literal notranslate"><span class="pre">rocpd</span></code> schema from rocprofiler-sdk-rocpd.</p></li>
</ul>
</section>
<section id="id56">
<h4>Changed<a class="headerlink" href="#id56" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Improved Fortran main function detection to ensure <code class="docutils literal notranslate"><span class="pre">rocprof-sys-instrument</span></code> uses the Fortran program main function instead of the C wrapper.</p></li>
</ul>
</section>
<section id="id57">
<h4>Resolved issues<a class="headerlink" href="#id57" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Fixed a crash when running <code class="docutils literal notranslate"><span class="pre">rocprof-sys-python</span></code> with ROCPROFSYS_USE_ROCPD enabled.</p></li>
<li><p>Fixed an issue where kernel/memory-copy events could appear on the wrong Perfetto track (e.g., queue track when stream grouping was requested) because _group_by_queue state leaked between records.</p></li>
<li><p>Fixed a soft hang in collecting available PAPI metrics on some systems with Intel CPU.</p></li>
<li><p>Fixed some duplicate HIP and HSA API events in <code class="docutils literal notranslate"><span class="pre">rocpd</span></code> output.</p></li>
</ul>
</section>
</section>
<section id="rocprim-4-2-0">
<h3><strong>rocPRIM</strong> (4.2.0)<a class="headerlink" href="#rocprim-4-2-0" title="Link to this heading">#</a></h3>
<section id="id58">
<h4>Added<a class="headerlink" href="#id58" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Missing benchmarks, such that every autotuned specialization is now benchmarked.</p></li>
<li><p>A new cmake option, <code class="docutils literal notranslate"><span class="pre">BENCHMARK_USE_AMDSMI</span></code>. It is set to <code class="docutils literal notranslate"><span class="pre">OFF</span></code> by default. When this option is set to <code class="docutils literal notranslate"><span class="pre">ON</span></code>, it lets benchmarks use AMD SMI to output more GPU statistics.</p></li>
<li><p>The first tested example program for <code class="docutils literal notranslate"><span class="pre">device_search</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apply_config_improvements.py</span></code>file , which generates improved configs by taking the best specializations from old and new configs.</p>
<ul>
<li><p>Run the script with <code class="docutils literal notranslate"><span class="pre">--help</span></code> for usage instructions, and see <a class="reference external" href="https://rocm.docs.amd.com/projects/rocPRIM/en/latest/conceptual/rocPRIM-performance-tuning.html#rocprim-performance-tuning">rocPRIM Performance Tuning</a> for more information.</p></li>
</ul>
</li>
<li><p>Kernel Tuner proof-of-concept.</p></li>
<li><p>Enhanced SPIR-V support and performance.</p></li>
</ul>
</section>
<section id="id59">
<h4>Optimized<a class="headerlink" href="#id59" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Improved performance of <code class="docutils literal notranslate"><span class="pre">device_radix_sort</span></code> onesweep variant.</p></li>
</ul>
</section>
<section id="id60">
<h4>Resolved issues<a class="headerlink" href="#id60" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Fixed the issue where <code class="docutils literal notranslate"><span class="pre">rocprim::device_scan_by_key</span></code> failed when performing an “in-place” inclusive scan by reusing “keys” as output, by adding a buffer to store the last keys of each block (excluding the last block). This fix only affects the specific case of reusing “keys” as output in an inclusive scan, and does not affect other cases.</p></li>
<li><p>Fixed benchmark build error on Windows.</p></li>
<li><p>Fixed offload compress build option.</p></li>
<li><p>Fixed <code class="docutils literal notranslate"><span class="pre">float_bit_mask</span></code> for <code class="docutils literal notranslate"><span class="pre">rocprim::half</span></code>.</p></li>
<li><p>Fixed handling of undefined behaviour when <code class="docutils literal notranslate"><span class="pre">__builtin_clz</span></code>, <code class="docutils literal notranslate"><span class="pre">__builtin_ctz</span></code>, and similar builtins are called.</p></li>
<li><p>Fixed potential build error with <code class="docutils literal notranslate"><span class="pre">rocprim::detail::histogram_impl</span></code>.</p></li>
</ul>
</section>
<section id="id61">
<h4>Known issues<a class="headerlink" href="#id61" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Potential hang with <code class="docutils literal notranslate"><span class="pre">rocprim::partition_threeway</span></code> with large input data sizes on later ROCm builds. A workaround is currently in place.</p></li>
</ul>
</section>
</section>
<section id="rocprofiler-sdk-1-1-0">
<h3><strong>ROCprofiler-SDK</strong> (1.1.0)<a class="headerlink" href="#rocprofiler-sdk-1-1-0" title="Link to this heading">#</a></h3>
<section id="id62">
<h4>Added<a class="headerlink" href="#id62" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Counter collection support for gfx1150 and gfx1151.</p></li>
<li><p>HSA Extension API v8 support.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipStreamCopyAttributes</span></code> API implementation.</p></li>
</ul>
</section>
<section id="id63">
<h4>Optimized<a class="headerlink" href="#id63" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Improved process attachment and updated the corresponding <a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3-process-attachment.html">documentation</a>.</p></li>
<li><p>Improved <a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/quick_guide.html">Quick reference guide for rocprofv3</a>.</p></li>
<li><p>Updated the <a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/install/installation.html">installation documentation</a> with the links to the latest repository.</p></li>
</ul>
</section>
<section id="id64">
<h4>Resolved issues<a class="headerlink" href="#id64" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Fixed multi-GPU dimension mismatch.</p></li>
<li><p>Fixed device lock issue for dispatch counters.</p></li>
<li><p>Addressed OpenMP Tools task scheduling null pointer exception.</p></li>
<li><p>Fixed stream ID errors arising during process attachment.</p></li>
<li><p>Fixed issues arising during dynamic code object loading.</p></li>
</ul>
</section>
</section>
<section id="rocpydecode-0-8-0">
<h3><strong>rocPyDecode</strong> (0.8.0)<a class="headerlink" href="#rocpydecode-0-8-0" title="Link to this heading">#</a></h3>
<section id="id65">
<h4>Changed<a class="headerlink" href="#id65" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>CXX Compiler location - Use default <code class="docutils literal notranslate"><span class="pre">${ROCM_PATH}/lib/llvm/bin</span></code> for AMD Clang.</p></li>
</ul>
</section>
</section>
<section id="rocrand-4-2-0">
<h3><strong>rocRAND</strong> (4.2.0)<a class="headerlink" href="#rocrand-4-2-0" title="Link to this heading">#</a></h3>
<section id="id66">
<h4>Added<a class="headerlink" href="#id66" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Added a new CMake option <code class="docutils literal notranslate"><span class="pre">-DUSE_SYSTEM_LIB</span></code> to allow tests to be built from <code class="docutils literal notranslate"><span class="pre">ROCm</span></code> libraries provided by the system.</p></li>
<li><p>Experimental SPIR-V support.</p></li>
</ul>
</section>
<section id="id67">
<h4>Changed<a class="headerlink" href="#id67" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>The <code class="docutils literal notranslate"><span class="pre">launch</span></code> method in <code class="docutils literal notranslate"><span class="pre">host_system</span></code> and <code class="docutils literal notranslate"><span class="pre">device_system</span></code>, so that kernels with all supported arches can be compiled with correct configuration during host pass. All generators are updated accordingly for support of SPIR-V. To invoke SPIR-V, it should be built with <code class="docutils literal notranslate"><span class="pre">-DAMDGPU_TARGETS=amdgcnspirv</span></code>.</p></li>
</ul>
</section>
<section id="id68">
<h4>Removed<a class="headerlink" href="#id68" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>For performance reasons,  the <code class="docutils literal notranslate"><span class="pre">mrg31k3p_state</span></code>, <code class="docutils literal notranslate"><span class="pre">mrg32k3a_state</span></code>, <code class="docutils literal notranslate"><span class="pre">xorwow_state</span></code> and <code class="docutils literal notranslate"><span class="pre">philox4x32_10_state</span></code> states no longer use the  <code class="docutils literal notranslate"><span class="pre">boxmuller_float_state</span></code> and <code class="docutils literal notranslate"><span class="pre">boxmuller_double_state</span></code> states, and the <code class="docutils literal notranslate"><span class="pre">boxmuller_float</span></code> and <code class="docutils literal notranslate"><span class="pre">boxmuller_double</span></code> variables are set with <code class="docutils literal notranslate"><span class="pre">NaN</span></code> as default values.</p></li>
</ul>
</section>
</section>
<section id="rocshmem-3-2-0">
<h3><strong>rocSHMEM</strong> (3.2.0)<a class="headerlink" href="#rocshmem-3-2-0" title="Link to this heading">#</a></h3>
<section id="id69">
<h4>Added<a class="headerlink" href="#id69" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>The GDA conduit for AMD Pensando IONIC.</p></li>
</ul>
</section>
<section id="id70">
<h4>Changed<a class="headerlink" href="#id70" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Dependency libraries are now loaded dynamically.</p></li>
<li><p>The following APIs now have an implementation for the GDA conduit:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">rocshmem_p</span></code></p></li>
<li><p>fetching atomics <code class="docutils literal notranslate"><span class="pre">rocshmem_&lt;TYPE&gt;_fetch_&lt;op&gt;</span></code></p></li>
<li><p>collective APIs</p></li>
</ul>
</li>
<li><p>The following APIs now have an implementation for the IPC conduit:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">rocshmem_&lt;TYPE&gt;_atomic_{and,or,xor,swap}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocshmem_&lt;TYPE&gt;_atomic_fetch_{and,or,xor,swap}</span></code></p></li>
</ul>
</li>
</ul>
</section>
<section id="id71">
<h4>Known issues<a class="headerlink" href="#id71" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Only 64-bit rocSHMEM atomic APIs are implemented for the GDA conduit.</p></li>
</ul>
</section>
</section>
<section id="rocsolver-3-32-0">
<h3><strong>rocSOLVER</strong> (3.32.0)<a class="headerlink" href="#rocsolver-3-32-0" title="Link to this heading">#</a></h3>
<section id="id72">
<h4>Optimized<a class="headerlink" href="#id72" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Improved the performance of LARFB and downstream functions such as GEQRF and ORMTR.</p></li>
</ul>
</section>
</section>
<section id="rocsparse-4-2-0">
<h3><strong>rocSPARSE</strong> (4.2.0)<a class="headerlink" href="#rocsparse-4-2-0" title="Link to this heading">#</a></h3>
<section id="id73">
<h4>Added<a class="headerlink" href="#id73" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Sliced ELL format support to the <code class="docutils literal notranslate"><span class="pre">rocsparse_spmv</span></code> routine.</p></li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">rocsparse_sptrsv</span></code> and <code class="docutils literal notranslate"><span class="pre">rocsparse_sptrsm</span></code> routines for triangular solve.</p></li>
<li><p>The <code class="docutils literal notranslate"><span class="pre">--clients-only</span></code> option to the <code class="docutils literal notranslate"><span class="pre">install.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">rmake.py</span></code> scripts to only build the clients for a version of rocSPARSE that is already installed.</p></li>
<li><p>NNZ split algorithm <code class="docutils literal notranslate"><span class="pre">rocsparse_spmv_alg_csr_nnzsplit</span></code> to <code class="docutils literal notranslate"><span class="pre">rocsparse_spmv</span></code>. This algorithm might be superior to the existing adaptive algorithm <code class="docutils literal notranslate"><span class="pre">rocsparse_spmv_alg_csr_adaptive</span></code> when running the computation a small number of times because it avoids paying the analysis cost of the adaptive algorithm.</p></li>
</ul>
</section>
<section id="id74">
<h4>Changed<a class="headerlink" href="#id74" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>rocBLAS is a requirement when it’s requested when building from source. Previously, rocBLAS was not used if it could not be found. To opt out of using rocBLAS when building from source, use the <code class="docutils literal notranslate"><span class="pre">--no-rocblas</span></code> option with the <code class="docutils literal notranslate"><span class="pre">install.sh</span></code> or <code class="docutils literal notranslate"><span class="pre">rmake.py</span></code> build scripts.</p></li>
</ul>
</section>
<section id="id75">
<h4>Optimized<a class="headerlink" href="#id75" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Significantly improved the <code class="docutils literal notranslate"><span class="pre">rocsparse_sddmm</span></code> routine when using CSR format, especially as the number of columns in the dense <code class="docutils literal notranslate"><span class="pre">A</span></code> matrix (or rows in the dense <code class="docutils literal notranslate"><span class="pre">B</span></code> matrix) increases.</p></li>
<li><p>Improved the user documentation.</p></li>
</ul>
</section>
<section id="id76">
<h4>Resolved issues<a class="headerlink" href="#id76" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Fixed the <code class="docutils literal notranslate"><span class="pre">rmake.py</span></code> build script to properly handle <code class="docutils literal notranslate"><span class="pre">auto</span></code> and all options when selecting offload targets.</p></li>
<li><p>Fixed an issue when building rocSPARSE with the install script on some operating systems.</p></li>
<li><p>Fixed <code class="docutils literal notranslate"><span class="pre">std::fma</span></code> casting in host routines to properly deduce types. This could have previously caused compilation failures when building from source.</p></li>
</ul>
</section>
</section>
<section id="rocthrust-4-2-0">
<h3><strong>rocThrust</strong> (4.2.0)<a class="headerlink" href="#rocthrust-4-2-0" title="Link to this heading">#</a></h3>
<section id="id77">
<h4>Added<a class="headerlink" href="#id77" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">thrust::unique_ptr</span></code> - a smart pointer for managing device memory with automatic cleanup.</p></li>
<li><p>A new cmake option, <code class="docutils literal notranslate"><span class="pre">BUILD_OFFLOAD_COMPRESS</span></code>. When rocThrust is built with this option enabled, the <code class="docutils literal notranslate"><span class="pre">--offload-compress</span></code> switch is passed to the compiler. This causes the compiler to compress the binary that it generates. Compression can be useful when compiling for a large number of targets, because it often results in a larger binary. Without compression, in some cases, the generated binary may become so large symbols are placed out of range, resulting in linking errors. The new <code class="docutils literal notranslate"><span class="pre">BUILD_OFFLOAD_COMPRESS</span></code> option is set to <code class="docutils literal notranslate"><span class="pre">ON</span></code> by default.</p></li>
<li><p>Experimental SPIR-V support.</p></li>
</ul>
</section>
</section>
<section id="rocwmma-2-2-0">
<h3><strong>rocWMMA</strong> (2.2.0)<a class="headerlink" href="#rocwmma-2-2-0" title="Link to this heading">#</a></h3>
<section id="id78">
<h4>Added<a class="headerlink" href="#id78" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Sample <code class="docutils literal notranslate"><span class="pre">perf_i8gemm</span></code> to demonstrate <code class="docutils literal notranslate"><span class="pre">int8_t</span></code> as matrix input data type.</p></li>
<li><p>Support for the gfx1150 target.</p></li>
</ul>
</section>
<section id="id79">
<h4>Changed<a class="headerlink" href="#id79" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Removed unnecessary const keyword to avoid compiler warnings.</p></li>
<li><p>rocWMMA has been moved into the new rocm-libraries “monorepo” repository <span class="fab fa-github"></span> <a class="reference external" href="https://github.com/ROCm/rocm-libraries">rocm-libraries</a>. This repository consolidates a number of separate ROCm libraries and shared components.</p>
<ul>
<li><p>The repository migration requires a few changes to the CMake configuration of rocWMMA.</p></li>
<li><p>The repository migration required the GTest dependency to be updated to v1.16.0.</p></li>
</ul>
</li>
</ul>
</section>
<section id="id80">
<h4>Resolved issues<a class="headerlink" href="#id80" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Skip invalid test configurations when using ‘register file’ LDS mapping.</p></li>
<li><p>Ensured transform functions in samples are only available on the device.</p></li>
</ul>
</section>
</section>
<section id="rpp-2-2-0">
<h3><strong>RPP</strong> (2.2.0)<a class="headerlink" href="#rpp-2-2-0" title="Link to this heading">#</a></h3>
<section id="id81">
<h4>Added<a class="headerlink" href="#id81" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Pinned buffer API support for HOST and HIP.</p></li>
</ul>
</section>
<section id="id82">
<h4>Changed<a class="headerlink" href="#id82" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>AMDClag++ compiler has moved to <code class="docutils literal notranslate"><span class="pre">${ROCM_PATH}/lib/llvm/bin</span></code>.</p></li>
</ul>
</section>
<section id="id83">
<h4>Removed<a class="headerlink" href="#id83" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>The <code class="docutils literal notranslate"><span class="pre">copy_param_float()</span></code> and <code class="docutils literal notranslate"><span class="pre">copy_param_uint()</span></code> mem copy helper functions have been removed as buffers now consistently use pinned/HIP memory.</p></li>
</ul>
</section>
<section id="id84">
<h4>Resolved issues<a class="headerlink" href="#id84" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p>Test Suite - Error Code Capture updates.</p></li>
</ul>
</section>
</section>
<section id="tensile-4-45-0">
<h3><strong>Tensile</strong> (4.45.0)<a class="headerlink" href="#tensile-4-45-0" title="Link to this heading">#</a></h3>
<section id="id85">
<h4>Removed<a class="headerlink" href="#id85" title="Link to this heading">#</a></h4>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">op_sel</span></code> modifiers for <code class="docutils literal notranslate"><span class="pre">v_dot4</span></code> from Tensile codegen.</p></li>
<li><p>Dependency on <code class="docutils literal notranslate"><span class="pre">rocm-agent-enumerator</span></code> during build.</p></li>
</ul>
</section>
</section>
</section>
<section id="rocm-known-issues">
<h2>ROCm known issues<a class="headerlink" href="#rocm-known-issues" title="Link to this heading">#</a></h2>
<p>ROCm known issues are noted on <span class="fab fa-github"></span> <a class="reference external" href="https://github.com/ROCm/ROCm/labels/Verified%20Issue">GitHub</a>. For known
issues related to individual components, review the <a class="reference internal" href="#detailed-component-changes">Detailed component changes</a>.</p>
<section id="rocm-multi-version-installation-might-cause-amd-smi-cli-failure">
<h3>ROCm multi-version installation might cause amd-smi CLI failure<a class="headerlink" href="#rocm-multi-version-installation-might-cause-amd-smi-cli-failure" title="Link to this heading">#</a></h3>
<p>Installing multiple versions of ROCm on the same system might result in the <code class="docutils literal notranslate"><span class="pre">amd-smi</span></code> CLI functioning incorrectly.
As a workaround, follow any of the preferred options:</p>
<p><strong>Option 1:</strong> If only the CLI or C++ library are needed, uninstall the <code class="docutils literal notranslate"><span class="pre">amdsmi</span></code> Python package:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>python3<span class="w"> </span>-m<span class="w"> </span>pip<span class="w"> </span>uninstall<span class="w"> </span>amdsmi
</pre></div>
</div>
<p><strong>Option 2:</strong> Reinstall the Python library from your target ROCm version:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span><span class="c1"># Remove previous installation</span>
python3<span class="w"> </span>-m<span class="w"> </span>pip<span class="w"> </span>uninstall<span class="w"> </span>amdsmi

<span class="c1"># Install from target ROCm instance</span>
<span class="nb">cd</span><span class="w"> </span>/opt/rocm/share/amd_smi
python3<span class="w"> </span>-m<span class="w"> </span>pip<span class="w"> </span>install<span class="w"> </span>--user<span class="w"> </span>.
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p><code class="docutils literal notranslate"><span class="pre">sudo</span></code> might be required. Use flag <code class="docutils literal notranslate"><span class="pre">--break-system-packages</span></code> if <code class="docutils literal notranslate"><span class="pre">pip</span> <span class="pre">un/installation</span></code> fails.</p>
</div>
<p>For detailed instructions, see <a class="reference external" href="https://rocm.docs.amd.com/projects/amdsmi/en/latest/install/install.html#install-the-python-library-for-multiple-rocm-instances">Install the Python library for multiple ROCm instances</a>. The issue will be fixed in a future ROCm release. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/5875">GitHub issue #5875</a>.</p>
</section>
<section id="intermittent-errors-when-running-jax-workloads">
<h3>Intermittent errors when running JAX workloads<a class="headerlink" href="#intermittent-errors-when-running-jax-workloads" title="Link to this heading">#</a></h3>
<p>You might experience intermittent errors or segmentation faults when running JAX workloads. The issue is currently under investigation and will be addressed in an upcoming ROCm release. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/5878">GitHub issue #5878</a>.</p>
</section>
<section id="hipblaslt-performance-variation-for-a-particular-fp8-gemm-operation-on-amd-instinct-mi325x-gpus">
<h3>hipBLASLt performance variation for a particular FP8 GEMM operation on AMD Instinct MI325X GPUs<a class="headerlink" href="#hipblaslt-performance-variation-for-a-particular-fp8-gemm-operation-on-amd-instinct-mi325x-gpus" title="Link to this heading">#</a></h3>
<p>If you’re using hipBLASLt on AMD Instinct MI325X GPUs for large FP8 GEMM operations (such as 9728x8192x65536), you might observe a noticeable performance variation. The issue is currently under investigation and will be fixed in a future ROCm release. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/5734">GitHub issue #5734</a>.</p>
</section>
<section id="increased-runtime-latency-of-the-hip-hipstreamcreate-api">
<h3>Increased runtime latency of the HIP hipStreamCreate API<a class="headerlink" href="#increased-runtime-latency-of-the-hip-hipstreamcreate-api" title="Link to this heading">#</a></h3>
<p>Doubling of runtime latency of the <a class="reference external" href="https://rocmdocs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html">HIP</a> <code class="docutils literal notranslate"><span class="pre">hipStreamCreate</span></code> API might be observed. While this affects RCCL <code class="docutils literal notranslate"><span class="pre">all_reduce_perf</span></code> tests, it has minimal impact on real production workloads. No slowdowns have been observed in other common benchmarks, including PyTorch, vLLM, and other application‑level tests. The issue is currently under investigation and will be fixed in an upcoming ROCm release. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/5978">GitHub issue #5978</a>.</p>
</section>
</section>
<section id="rocm-resolved-issues">
<h2>ROCm resolved issues<a class="headerlink" href="#rocm-resolved-issues" title="Link to this heading">#</a></h2>
<p>The following are previously known issues resolved in this release. For resolved issues related to
individual components, review the <a class="reference internal" href="#detailed-component-changes">Detailed component changes</a>.</p>
<section id="rccl-performance-degradation-on-amd-instinct-mi300x-gpu-with-amd-pollara-ai-nic">
<h3>RCCL performance degradation on AMD Instinct MI300X GPU with AMD Pollara AI NIC<a class="headerlink" href="#rccl-performance-degradation-on-amd-instinct-mi300x-gpu-with-amd-pollara-ai-nic" title="Link to this heading">#</a></h3>
<p>The RCCL performance degradation issue affecting AMD Instinct MI300X GPUs with AMD Pollara AI NIC for specific collectives and message sizes has been resolved. The impacted collectives included <code class="docutils literal notranslate"><span class="pre">Scatter</span></code>, <code class="docutils literal notranslate"><span class="pre">AllToAll</span></code>, and <code class="docutils literal notranslate"><span class="pre">AlltoAllv</span></code>. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/5717">GitHub issue #5717</a>.</p>
</section>
<section id="rocprofv3-fails-on-rpm-based-os-with-python-3-10-and-later">
<h3>rocprofv3 fails on RPM-based OS with Python 3.10 (and later)<a class="headerlink" href="#rocprofv3-fails-on-rpm-based-os-with-python-3-10-and-later" title="Link to this heading">#</a></h3>
<p>The issue where <code class="docutils literal notranslate"><span class="pre">rocprofv3</span></code> tool failed on RPM-based operating systems (such as RHEL 8) with Python 3.10 (and later) due to missing ROCPD bindings has been resolved. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/5606">GitHub issue #5606</a>.</p>
</section>
<section id="applications-using-opencv-might-fail-due-to-package-incompatibility-between-the-os">
<h3>Applications using OpenCV might fail due to package incompatibility between the OS<a class="headerlink" href="#applications-using-opencv-might-fail-due-to-package-incompatibility-between-the-os" title="Link to this heading">#</a></h3>
<p>An issue where applications using OpenCV packages failed due to package incompatibility between OpenCV built on Ubuntu 24.04 and Debian 13 has been resolved. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/5501">GitHub issue #5501</a>.</p>
</section>
<section id="amd-smi-cli-triggers-repeated-kernel-errors-on-gpus-with-partitioning-support">
<h3>AMD SMI CLI triggers repeated kernel errors on GPUs with partitioning support<a class="headerlink" href="#amd-smi-cli-triggers-repeated-kernel-errors-on-gpus-with-partitioning-support" title="Link to this heading">#</a></h3>
<p>An issue where running the <code class="docutils literal notranslate"><span class="pre">amd-smi</span></code> CLI on GPUs with partitioning support, such as the AMD
Instinct MI300 Series, which produced repeated kernel error messages in the
system logs, has been resolved. The issue occurred when <code class="docutils literal notranslate"><span class="pre">amd-smi</span></code> attempted to open invalid partition device nodes during device permission checks. As a result, the AMD GPU Driver (amdgpu) logged errors in <code class="docutils literal notranslate"><span class="pre">dmesg</span></code>, such as:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>amdgpu 0000:15:00.0: amdgpu: renderD153 partition 1 not valid!
</pre></div>
</div>
<p>These repeated kernel logs could clutter the system logs and cause
unnecessary concern about GPU health. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/5720">GitHub issue #5720</a>.</p>
</section>
<section id="incorrect-results-in-gemm-ex-operations-for-rocblas-and-hipblas">
<h3>Incorrect results in gemm_ex operations for rocBLAS and hipBLAS<a class="headerlink" href="#incorrect-results-in-gemm-ex-operations-for-rocblas-and-hipblas" title="Link to this heading">#</a></h3>
<p>An issue where some <code class="docutils literal notranslate"><span class="pre">gemm_ex</span></code> operations with 8-bit input data types (<code class="docutils literal notranslate"><span class="pre">int8</span></code>, <code class="docutils literal notranslate"><span class="pre">float8</span></code>, <code class="docutils literal notranslate"><span class="pre">bfloat8</span></code>) for specific matrix dimensions (K = 1 and number of workgroups &gt; 1) yield incorrect results has been resolved. The root cause was incorrect tailloop code that ignored workgroup index when calculating valid element size. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/5722">GitHub issue #5722</a>.</p>
</section>
<section id="libva-based-applications-might-fail-after-rocm-installation">
<h3>Libva-based applications might fail after ROCm installation<a class="headerlink" href="#libva-based-applications-might-fail-after-rocm-installation" title="Link to this heading">#</a></h3>
<p>The issue in which certain applications that depended on the Libva library (such as <code class="docutils literal notranslate"><span class="pre">vainfo</span></code> and <code class="docutils literal notranslate"><span class="pre">ffmpeg</span></code>) failed after ROCm installation has been resolved. The failure occurred due to a symbol clash between the AMD-packaged <code class="docutils literal notranslate"><span class="pre">libva-amdgpu</span></code> and the system-provided Libva. This conflict was introduced when adapting the RHEL 8 build to support additional operating systems, which required changes to the build options. See <a class="reference external" href="https://github.com/ROCm/ROCm/issues/5732">GitHub issue #5732</a>.</p>
</section>
</section>
<section id="rocm-upcoming-changes">
<h2>ROCm upcoming changes<a class="headerlink" href="#rocm-upcoming-changes" title="Link to this heading">#</a></h2>
<p>The following changes to the ROCm software stack are anticipated for future releases.</p>
<section id="rocm-offline-installer-creator-deprecation">
<h3>ROCm Offline Installer Creator deprecation<a class="headerlink" href="#rocm-offline-installer-creator-deprecation" title="Link to this heading">#</a></h3>
<p>The <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/install/rocm-offline-installer.html">ROCm Offline Installer Creator</a> is deprecated with the ROCm 7.2.0 release and will be removed in a future release. Equivalent installation capabilities are available through the <a class="reference external" href="https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.0/install/rocm-runfile-installer.html">ROCm Runfile Installer</a>, a self-extracting installer that is not based on OS package managers.</p>
</section>
<section id="rocm-smi-deprecation">
<h3>ROCm SMI deprecation<a class="headerlink" href="#rocm-smi-deprecation" title="Link to this heading">#</a></h3>
<p><a class="reference external" href="https://github.com/ROCm/rocm_smi_lib">ROCm SMI</a> will be phased out in an
upcoming ROCm release and will enter maintenance mode. After this transition,
only critical bug fixes will be addressed and no further feature development
will take place.</p>
<p>It’s strongly recommended to transition your projects to <a class="reference external" href="https://github.com/ROCm/amdsmi">AMD
SMI</a>, the successor to ROCm SMI. AMD SMI
includes all the features of the ROCm SMI and will continue to receive regular
updates, new functionality, and ongoing support. For more information on AMD
SMI, see the <a class="reference external" href="https://rocm.docs.amd.com/projects/amdsmi/en/latest/">AMD SMI documentation</a>.</p>
</section>
<section id="roctracer-rocprofiler-rocprof-and-rocprofv2-deprecation">
<h3>ROCTracer, ROCProfiler, rocprof, and rocprofv2 deprecation<a class="headerlink" href="#roctracer-rocprofiler-rocprof-and-rocprofv2-deprecation" title="Link to this heading">#</a></h3>
<p>ROCTracer, ROCProfiler, <code class="docutils literal notranslate"><span class="pre">rocprof</span></code>, and <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> are deprecated and only critical defect fixes will be addressed for older versions of the profiling tools and libraries. It’s strongly recommended to upgrade to the latest version of the <a class="reference external" href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/">ROCprofiler-SDK</a> library and the (<code class="docutils literal notranslate"><span class="pre">rocprofv3</span></code>) tool to ensure continued support and access to new features.</p>
<p>It’s anticipated that ROCTracer, ROCProfiler, <code class="docutils literal notranslate"><span class="pre">rocprof</span></code>, and <code class="docutils literal notranslate"><span class="pre">rocprofv2</span></code> will reach end-of-life by future releases, aligning with Q1 of 2026.</p>
</section>
<section id="changes-to-rocm-object-tooling">
<h3>Changes to ROCm Object Tooling<a class="headerlink" href="#changes-to-rocm-object-tooling" title="Link to this heading">#</a></h3>
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
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#supported-hardware-operating-system-and-virtualization-changes">Supported hardware, operating system, and virtualization changes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#virtualization-support">Virtualization support</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#user-space-driver-and-firmware-dependent-changes">User space, driver, and firmware dependent changes</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#node-power-management-for-multi-gpu-nodes-added">Node power management for multi-GPU nodes added</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#model-optimization-for-amd-instinct-mi350-series-gpus">Model optimization for AMD Instinct MI350 Series GPUs</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#model-optimization-for-amd-instinct-mi300x-gpus">Model optimization for AMD Instinct MI300X GPUs</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-runtime-performance-improvements">HIP runtime performance improvements</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#graph-node-scaling">Graph node scaling</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#back-memory-set-memset-optimization">Back memory set (memset) optimization</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#async-handler-performance-improvement">Async handler performance improvement</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-apis-added">HIP APIs added</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-library-management-apis">HIP library management APIs</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-occupancy-api">HIP occupancy API</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#stream-management-api">Stream management API</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#new-rocshmem-communication-gpudirect-async-gda-backend-conduit">New rocSHMEM communication GPUDirect Async (GDA) backend conduit</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#software-managed-plan-cache-support-for-hiptensor">Software-managed plan cache support for hipTensor</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#spir-v-support-added-to-hipcub-and-rocthrust">SPIR-V support added to hipCUB and rocThrust</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblaslt-updates">hipBLASLT updates</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-updates">rocWMMA updates</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#migraphx-updates">MIGraphX updates</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amdgpu-wavefront-size-macro-removal">AMDGPU wavefront size macro removal</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-rocm-simulation-introduced">AMD ROCm Simulation introduced</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-optiq-introduced">ROCm Optiq introduced</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-rocm-life-science-updates">AMD ROCm Life Science updates</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#deep-learning-and-ai-framework-updates">Deep learning and AI framework updates</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#jax">JAX</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#onnx-runtime">ONNX Runtime</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-offline-installer-creator-updates">ROCm Offline Installer Creator updates</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-runfile-installer-updates">ROCm Runfile Installer updates</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#expansion-of-the-rocm-examples-repository">Expansion of the ROCm examples repository</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-documentation-updates">ROCm documentation updates</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-components">ROCm components</a></li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#detailed-component-changes">Detailed component changes</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-smi-26-2-1"><strong>AMD SMI</strong> (26.2.1)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#added">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#changed">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#resolved-issues">Resolved Issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#composable-kernel-1-2-0"><strong>Composable Kernel</strong> (1.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id1">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id2">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#upcoming-changes">Upcoming changes</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hip-7-2-0"><strong>HIP</strong> (7.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id3">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#optimized">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id4">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblas-3-2-0"><strong>hipBLAS</strong> (3.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id5">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblaslt-1-2-1"><strong>hipBLASLt</strong> (1.2.1)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id6">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id7">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipcub-4-2-0"><strong>hipCUB</strong> (4.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id8">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id9">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipfft-1-0-22"><strong>hipFFT</strong> (1.0.22)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id10">Added</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipify-22-0-0"><strong>HIPIFY</strong> (22.0.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id11">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id12">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsolver-3-2-0"><strong>hipSOLVER</strong> (3.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id13">Added</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparse-4-2-0"><strong>hipSPARSE</strong> (4.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id14">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id15">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id16">Resolved Issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipsparselt-0-2-6"><strong>hipSPARSELt</strong> (0.2.6)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id17">Optimized</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hiptensor-2-2-0"><strong>hipTensor</strong> (2.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id18">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id19">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id20">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#llvm-project-22-0-0"><strong>llvm-project</strong> (22.0.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id21">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id22">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id23">Upcoming changes</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#migraphx-2-15-0"><strong>MIGraphX</strong> (2.15.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id24">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id25">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id26">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id27">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#miopen-3-5-1"><strong>MIOpen</strong> (3.5.1)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id28">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id29">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id30">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id31">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#mivisionx-3-5-0"><strong>MIVisionX</strong> (3.5.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id32">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id33">Resolved issues</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#known-issues">Known issues</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id34">Upcoming changes</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-2-27-7"><strong>RCCL</strong> (2.27.7)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id35">Changed</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocal-2-5-0"><strong>rocAL</strong> (2.5.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id36">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id37">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id38">Resolved issues</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id39">Known issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocalution-4-1-0"><strong>rocALUTION</strong> (4.1.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id40">Added</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocblas-5-2-0"><strong>rocBLAS</strong> (5.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id41">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id42">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id43">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocdecode-1-5-0"><strong>rocDecode</strong> (1.5.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id44">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id45">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id46">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocfft-1-0-36"><strong>rocFFT</strong> (1.0.36)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id47">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id48">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocjpeg-1-3-0"><strong>rocJPEG</strong> (1.3.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id49">Changed</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-bandwidth-test-2-6-0"><strong>ROCm Bandwidth Test</strong> (2.6.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id50">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-compute-profiler-3-4-0"><strong>ROCm Compute Profiler</strong> (3.4.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id51">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id52">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#removed">Removed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id53">Resolved issues</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id54">Upcoming changes</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-systems-profiler-1-3-0"><strong>ROCm Systems Profiler</strong> (1.3.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id55">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id56">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id57">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprim-4-2-0"><strong>rocPRIM</strong> (4.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id58">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id59">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id60">Resolved issues</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id61">Known issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprofiler-sdk-1-1-0"><strong>ROCprofiler-SDK</strong> (1.1.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id62">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id63">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id64">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocpydecode-0-8-0"><strong>rocPyDecode</strong> (0.8.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id65">Changed</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocrand-4-2-0"><strong>rocRAND</strong> (4.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id66">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id67">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id68">Removed</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocshmem-3-2-0"><strong>rocSHMEM</strong> (3.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id69">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id70">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id71">Known issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsolver-3-32-0"><strong>rocSOLVER</strong> (3.32.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id72">Optimized</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocsparse-4-2-0"><strong>rocSPARSE</strong> (4.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id73">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id74">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id75">Optimized</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id76">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocthrust-4-2-0"><strong>rocThrust</strong> (4.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id77">Added</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocwmma-2-2-0"><strong>rocWMMA</strong> (2.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id78">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id79">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id80">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rpp-2-2-0"><strong>RPP</strong> (2.2.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id81">Added</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id82">Changed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id83">Removed</a></li>
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id84">Resolved issues</a></li>
</ul>
</li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#tensile-4-45-0"><strong>Tensile</strong> (4.45.0)</a><ul class="nav section-nav flex-column">
<li class="toc-h4 nav-item toc-entry"><a class="reference internal nav-link" href="#id85">Removed</a></li>
</ul>
</li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-known-issues">ROCm known issues</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-multi-version-installation-might-cause-amd-smi-cli-failure">ROCm multi-version installation might cause amd-smi CLI failure</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#intermittent-errors-when-running-jax-workloads">Intermittent errors when running JAX workloads</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#hipblaslt-performance-variation-for-a-particular-fp8-gemm-operation-on-amd-instinct-mi325x-gpus">hipBLASLt performance variation for a particular FP8 GEMM operation on AMD Instinct MI325X GPUs</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#increased-runtime-latency-of-the-hip-hipstreamcreate-api">Increased runtime latency of the HIP hipStreamCreate API</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-resolved-issues">ROCm resolved issues</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rccl-performance-degradation-on-amd-instinct-mi300x-gpu-with-amd-pollara-ai-nic">RCCL performance degradation on AMD Instinct MI300X GPU with AMD Pollara AI NIC</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocprofv3-fails-on-rpm-based-os-with-python-3-10-and-later">rocprofv3 fails on RPM-based OS with Python 3.10 (and later)</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#applications-using-opencv-might-fail-due-to-package-incompatibility-between-the-os">Applications using OpenCV might fail due to package incompatibility between the OS</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#amd-smi-cli-triggers-repeated-kernel-errors-on-gpus-with-partitioning-support">AMD SMI CLI triggers repeated kernel errors on GPUs with partitioning support</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#incorrect-results-in-gemm-ex-operations-for-rocblas-and-hipblas">Incorrect results in gemm_ex operations for rocBLAS and hipBLAS</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#libva-based-applications-might-fail-after-rocm-installation">Libva-based applications might fail after ROCm installation</a></li>
</ul>
</li>
<li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-upcoming-changes">ROCm upcoming changes</a><ul class="nav section-nav flex-column">
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-offline-installer-creator-deprecation">ROCm Offline Installer Creator deprecation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#rocm-smi-deprecation">ROCm SMI deprecation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#roctracer-rocprofiler-rocprof-and-rocprofv2-deprecation">ROCTracer, ROCProfiler, rocprof, and rocprofv2 deprecation</a></li>
<li class="toc-h3 nav-item toc-entry"><a class="reference internal nav-link" href="#changes-to-rocm-object-tooling">Changes to ROCm Object Tooling</a></li>
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
<li><a href="https://rocm.docs.amd.com/en/docs-7.2.0/about/license.html">ROCm Licenses and Disclaimers</a></li>
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
