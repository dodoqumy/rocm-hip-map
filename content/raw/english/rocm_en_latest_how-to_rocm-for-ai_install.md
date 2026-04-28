---
title: "Installing ROCm and deep learning frameworks"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/install.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item
- [](../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](index.html){.nav-link}
- Installing\...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# Installing ROCm and deep learning frameworks

## Contents

- [Deep learning frameworks](#deep-learning-frameworks){.reference .internal .nav-link}
- [Next steps](#next-steps){.reference .internal .nav-link}



# Installing ROCm and deep learning frameworks[\#](#installing-rocm-and-deep-learning-frameworks "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 3 min read time

Applies to Linux


Before getting started, install ROCm and supported deep learning frameworks.

Pre-install

Each release of ROCm supports specific hardware and software configurations. Before installing, consult the [[System requirements]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html "(in ROCm installation on Linux v7.2.2)"){.reference .external} and [[Installation prerequisites]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/prerequisites.html "(in ROCm installation on Linux v7.2.2)"){.reference .external} guides.

If you're new to ROCm, refer to the [[ROCm quick start install guide for Linux]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html "(in ROCm installation on Linux v7.2.2)"){.reference .external}.

If you're using a Radeon GPU for graphics-accelerated applications, refer to the [Radeon installation instructions](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/howto_native_linux.html){.reference .external}.

You can install ROCm on [[compatible systems]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html "(in ROCm installation on Linux v7.2.2)"){.reference .external} via your Linux distribution's package manager. See the following documentation resources to get started:

- [[ROCm installation overview]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-overview.html "(in ROCm installation on Linux v7.2.2)"){.reference .external}

- [[Using your Linux distribution's package manager]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager-index.html "(in ROCm installation on Linux v7.2.2)"){.reference .external}

- [[Multi-version installation]{.xref .std .std-ref}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/multi-version-install-index.html#installation-types "(in ROCm installation on Linux v7.2.2)"){.reference .external}

Post-install

Follow the [[post-installation instructions]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/post-install.html "(in ROCm installation on Linux v7.2.2)"){.reference .external} to configure your system linker, PATH, and verify the installation.

If you encounter any issues during installation, refer to the [[Installation troubleshooting]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/install-faq.html "(in ROCm installation on Linux v7.2.2)"){.reference .external} guide.

## Deep learning frameworks[\#](#deep-learning-frameworks "Link to this heading"){.headerlink}

ROCm supports deep learning frameworks and libraries including [PyTorch](https://pytorch.org){.reference .external}, [TensorFlow](https://tensorflow.org){.reference .external}, [JAX](https://jax.readthedocs.io/en/latest){.reference .external}, and more.

Review the [[framework installation documentation]{.doc}](../deep-learning-rocm.html){.reference .internal}. For ease-of-use, it's recommended to use official ROCm prebuilt Docker images with the framework pre-installed.

## Next steps[\#](#next-steps "Link to this heading"){.headerlink}

After installing ROCm and your desired ML libraries -- and before running AI workloads -- conduct system health benchmarks to test the optimal performance of your AMD hardware. See [[System setup for AI workloads on ROCm]{.doc}](system-setup/index.html){.reference .internal} to get started.

::::: prev-next-area
[](index.html "previous page"){.left-prev}

::: prev-next-info
previous

Use ROCm for AI

[](system-setup/index.html "next page"){.right-next}

::: prev-next-info
next

System setup for AI workloads on ROCm

:::: sidebar-secondary-item
Contents

- [Deep learning frameworks](#deep-learning-frameworks){.reference .internal .nav-link}
- [Next steps](#next-steps){.reference .internal .nav-link}
