---
title: "Deep learning frameworks for ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/deep-learning-rocm.html"
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
- [](../index.html){.nav-link aria-label="首页"}
- 深度

header-article-items__end
header-article-item
article-header-buttons

# 适用于 ROCm 的深度学习框架（ROCm（Radeon 开放计算平台））

# ROCm 深度学习框架（ROCm（Radeon 开放计算平台））[\#](#deep-learning-frameworks-for-rocm "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS73NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi73NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026年3月31日



3 分钟阅读时间

适用于 Linux

深度学习框架提供机器学习、训练、微调、推理和性能优化的环境。

ROCm（Radeon Open Compute Platform）提供了一个完整的生态系统，用于高效开发和运行深度学习应用程序。它还提供与ROCm兼容的流行框架和库版本，例如 PyTorch、TensorFlow、JAX 等。

AMD ROCm（Radeon 开放计算平台）组织积极贡献于开源开发，并与框架组织紧密合作。这种协作确保框架特定的优化能有效利用 AMD GPU。



下表汇总了有关启用 ROCm（Radeon 开放计算平台）的深度学习框架的信息。包括 ROCm（Radeon 开放计算平台）兼容性及第三方工具支持、安装步骤和选项以及 GitHub 资源链接的详细信息。要获取 ROCm（Radeon 开放计算平台）支持的框架版本的完整列表，请参阅[[兼容性矩阵]{.doc}](../compatibility/compatibility-matrix.html){.reference .internal}主题。

::: pst-scrollable-table-container
+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+-------------------------------------------------+
| 框架                                                                                                         | 安装指南                                                                                                                                                                                              | 安装选项                | GitHub                                          |
+=============================================================================================================+--------------------------------------------------------------------------------------------------------------------------------=======================================================================+==========================+=================================================+
| [[PyTorch]{.doc}](../compatibility/ml-compatibility/pytorch-compatibility.html){.reference .internal}       | [[link]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html "(in ROCm（ROCm（Radeon 开放计算平台）） installation on Linux v7.2.2)"){.reference .external}    | - Docker 镜像           | [](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/pytorch)             |
|                                                                                                             |                                                                                                                                                                                                       |                          |                                                 |
|                                                                                                             |                                                                                                                                                                                                       | - Wheels 软件包         |                                                 |
|                                                                                                             |                                                                                                                                                                                                       |                          |                                                 |
|                                                                                                             |                                                                                                                                                                                                       | - ROCm（ROCm（Radeon 开放计算平台）） Base Docker 镜像 |                                                 |
|                                                                                                             |                                                                                                                                                                                                       |                          |                                                 |
|                                                                                                             |                                                                                                                                                                                                       | - Upstream Docker 文件   |                                                 |
+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+-------------------------------------------------+
| [[TensorFlow]{.doc}](../compatibility/ml-compatibility/tensorflow-compatibility.html){.reference .internal} | [[link]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/tensorflow-install.html "(in ROCm（ROCm（Radeon 开放计算平台）） installation on Linux v7.2.2)"){.reference .external} | - Docker 镜像           | [](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/tensorflow-upstream) |
|                                                                                                             |                                                                                                                                                                                                       |                          |                                                 |
|                                                                                                             |                                                                                                                                                                                                       | - Wheels 软件包         |                                                 |
+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+-------------------------------------------------+
| [[JAX]{.doc}](../compatibility/ml-compatibility/jax-compatibility.html){.reference .internal}               | [[link]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/jax-install.html "(in ROCm（ROCm（Radeon 开放计算平台）） installation on Linux v7.2.2)"){.reference .external}        | - Docker 镜像           | [](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/jax)                 |
+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+-------------------------------------------------+
| [[DGL]{.doc}](../compatibility/ml-compatibility/dgl-compatibility.html){.reference .internal}               | [[link]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/dgl-install.html "(in ROCm（ROCm（Radeon 开放计算平台）） installation on Linux v7.2.2)"){.reference .external}        | - Docker 镜像           | [](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/dgl)                 |
+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+-------------------------------------------------+

通过以下指南了解如何使用您的 ROCm（Radeon 开放计算平台）深度学习环境进行训练、微调、推理和性能优化。

- [[Use ROCm for AI]{.doc}](rocm-for-ai/index.html){.reference .internal}

- [[使用 ROCm（Radeon 开放计算平台）进行训练]{.doc}](rocm-for-ai/training/index.html){.reference .internal}

- [[使用 ROCm（Radeon 开放计算平台）微调 LLMs]{.doc}](rocm-for-ai/fine-tuning/index.html){.reference .internal}

- [[使用 ROCm 进行 AI 推理]{.doc}](rocm-for-ai/inference/index.html){.reference .internal}

- [[使用 ROCm（Radeon 开放计算平台）进行 AI 推理优化]{.doc}](rocm-for-ai/inference-optimization/index.html){.reference .internal}



::::: prev-next-area
[](../compatibility/compatibility-matrix.html "上一页"){.left-prev}

::: prev-next-info
上一页

兼容性矩阵

[](../compatibility/ml-compatibility/pytorch-compatibility.html "下一页"){.right-next}

::: prev-next-info
下一页



PyTorch 兼容性