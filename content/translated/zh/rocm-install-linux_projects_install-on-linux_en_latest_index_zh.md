---
title: "ROCm installation for Linux"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/index.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

:::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons

# ROCm installation for Linux

# ROCm installation for Linux[\#](#rocm-installation-for-linux "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-17

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 2 min read time

Applies to Linux

This section describes the ROCm for Linux installation options.

Note

- If you're using ROCm with AMD Radeon™ GPUs or Ryzen™ APUs for graphics workloads, see the [Use ROCm on Radeon and Ryzen](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html){.reference .external} documentation for installation instructions.

- The AMDGPU installer documentation has been removed to encourage the use of the package manager for ROCm installation. While the package manager is the recommended method, you can still install ROCm using the AMDGPU installer by following the [legacy process](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.4.1/install/install-methods/amdgpu-installer-index.html){.reference .external}. Ensure to update the command with the intended ROCm version before running it.

Install ROCm

- [[System requirements (Linux)]{.doc}](reference/system-requirements.html){.reference .internal}

- [[User and AMD GPU Driver (amdgpu) support matrix]{.doc}](reference/user-kernel-space-compat-matrix.html){.reference .internal}

- [[Quick start]{.doc}](install/quick-start.html){.reference .internal} - recommended for new users

- [[Detailed install]{.doc}](install/detailed-install.html){.reference .internal} - includes explanations

Install deep learning frameworks

- [[PyTorch]{.doc}](install/3rd-party/pytorch-install.html){.reference .internal}

- [[TensorFlow]{.doc}](install/3rd-party/tensorflow-install.html){.reference .internal}

- [[JAX]{.doc}](install/3rd-party/jax-install.html){.reference .internal}

- [[DGL]{.doc}](install/3rd-party/dgl-install.html){.reference .internal}

How to

- [[Run Docker containers]{.doc}](how-to/docker.html){.reference .internal}

- [[Use Spack]{.doc}](how-to/spack.html){.reference .internal}

Reference

- [[Package details]{.doc}](reference/package-manager-integration.html){.reference .internal}

- [[Troubleshooting]{.doc}](reference/install-faq.html){.reference .internal}

:::: prev-next-area
[](reference/system-requirements.html "next page"){.right-next}

::: prev-next-info
next

System requirements (Linux)