---
title: "ROCm Linux Filesystem Hierarchy Standard reorganization"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/file-reorg.html"
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
- ROCm（Radeon Open Compute Platform） Linux

[]{.fa-solid .fa-list}



# ROCm（Radeon 开放计算平台）Linux 文件系统层次结构标准重组

## 目录

- [Introduction](#introduction){.reference .internal .nav-link}
- [采用 FHS](#adopting-the-fhs){.reference .internal .nav-link}
- [早期 ROCm 版本的变更](#changes-from-earlier-rocm-versions){.reference .internal .nav-link}
- [ROCm FHS 重组：向后兼容性](#rocm-fhs-reorganization-backward-compatibility){.reference .internal .nav-link}
  - [包装器头文件](#wrapper-header-files){.reference .internal .nav-link}
  - [可执行文件](#executable-files){.reference .internal .nav-link}
  - [库文件](#library-files){.reference .internal .nav-link}
  - [CMake 配置文件](#cmake-config-files){.reference .internal .nav-link}
- [使用 ROCm 的应用程序所需的变更](#changes-required-in-applications-using-rocm){.reference .internal .nav-link}
- [版本规格的变更](#changes-in-versioning-specifications){.reference .internal .nav-link}



# ROCm Linux 文件系统层次标准重构[#](#rocm-linux-filesystem-hierarchy-standard-reorganization "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23



[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-true-avg} 7 分钟阅读时间

适用于 Linux 和 Windows

## 简介[\#](#introduction "链接到本标题"){.headerlink}

ROCm® 软件已采用 Linux Filesystem Hierarchy Standard (FHS)[https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html){.reference .external},以确保 ROCm® 符合标准开源惯例。以下各节详细说明当前及未来版本的 ROCm® 如何遵守 FHS,如何支持早期 ROCm® 文件系统,以及如何将改进后的版本规范应用于 ROCm®。

## 采用 FHS[\#](#adopting-the-fhs "链接到此标题"){.headerlink}

为标准化 ROCm（Radeon 开放计算平台）目录结构和目录内容布局，ROCm（Radeon 开放计算平台）采用了 [FHS](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html){.reference .external}，遵循基于 Linux 的发行版开源惯例。FHS 确保 ROCm（Radeon 开放计算平台）堆栈内部一致性，以及与其它系统和发行版的外部一致性。ROCm（Radeon 开放计算平台）建议的文件结构如下所述：

这是翻译请求。用户要求我将关于ROCm目录结构的英文文本翻译成简体中文。

让我分析这个目录结构文本：
1. 这是一个文件目录树形结构图
2. 包含文件路径和简短说明
3. 使用 ASCII art 格式展示目录层级

翻译规则：
- 保留所有 markdown 格式、代码块、内联代码和链接
- 保留技术术语（ROCm、HIP、GPU等）
- 保留 API 名称、函数名称、文件路径、命令
- 仅输出翻译结果
- 使用技术人员期望的技术中文

让我逐行翻译：

1. /opt/rocm



## 相比早期 ROCm（Radeon 开放计算平台）版本[\#](#changes-from-earlier-rocm-versions "Link to this heading"){.headerlink}

下表简要概述了新版 ROCm FHS 布局，并与早期 ROCm 版本的布局进行了比较。请注意，/opt/ 用于表示默认的 rocm-installation-path，如果 ROCm 发行版的安装位置非标准，则应替换此路径。



```highlight
     ______________________________________________________
    |  新 ROCm 布局                                    |  旧 ROCm 布局                                     |
    |_____________________________|________________________|
    | /opt/rocm

## ROCm FHS 重组：向后兼容性[\#](#rocm-fhs-reorganization-backward-compatibility "Link to this heading"){.headerlink}



ROCm 的 FHS 文件组织结构首次引入于 ROCm 5.2 版本。为确保用户在过渡到新的 FHS 过程中仍能运行其 ROCm 应用程序，实现了向后兼容性。ROCm 已将头文件和库移动到上述结构中指定的新位置，并在旧位置包含了符号链接和包装头文件以实现向后兼容性。以下各节详细说明 ROCm 针对包装头文件、可执行文件、库文件以及 CMake 配置文件实现的向后兼容性。

### 包装器头文件[\#](#wrapper-header-files "链接到此标题"){.headerlink}

包装头文件放置在旧位置（[`/opt/ro

```highlight
    #pragma message "此文件已弃用。请使用 include 路径 /opt/rocm-ver/include/ 中的文件，并使用 hip 前缀。"
    #include <hip/hip_runtime.h>
```

- Starting at ROCm 5.2 release, the deprecation for backward compatibility wrapper header files is: [`#pragma`{.docutils .literal .notranslate}]{.pre} message announcing [`#warning`{.docutils .literal .notranslate}]{.pre}.

- Starting from ROCm 6.0 (tentatively) backward compatibility for wrapper header files will be removed, and the [`#pragma`{.docutils .literal .notranslate}]{.pre} message will be announcing [`#error`{.docutils .literal .notranslate}]{.pre}.

### 可执行文件[\#](#executable-files "Link to this heading"){.headerlink}



可执行文件位于 [`/opt/rocm

```
$ ls -l /opt/rocm/hip/bin/
lrwxrwxrwx 1 root root   24 Jan 1 23:32 hipcc -> ../../bin/hipcc
```

### 库文件[\#](#library-files "链接到此标题"){.headerlink}

库文件位于 [`/opt/ro

::: highlight
    $ ls -l /opt/rocm/hip/lib/
    drwxr-xr-x 4 root root 4096 Jan 1 10:45 cmake
    lrwxrwxrwx 1 root root   24 Jan 1 23:32 libamdhip64.so -> ../../lib/libamdhip64.so

### CMake 配置文件[#](#cmake-config-files "Link to this heading"){.headerlink}

所有 CMake 配置文件均位于 `/opt/rocm-<ver>/lib/cmake/<component>` 文件夹中。为了向后兼容，旧的 CMake 位置（`/opt/rocm-<ver>/<component>/lib/cmake`）包含指向新 CMake 配置的软链接。软链接将在未来版本中移除，暂定为 ROCm v6.0。

::: highlight
    $ ls -l /opt/rocm/hip/lib/cmake/hip/
    lrwxrwxrwx 1 root root 42 1月 1日 23:32 hip-config.cmake -> ../../../../lib/cmake/hip/hip-config.cmake



使用 ROCm（Radeon 开放计算平台）的应用所需变更[\#](#changes--required-in-applications-using-rocm "Link to this heading"){.headerlink}

建议使用 ROCm（Radeon 开放计算平台）的应用程序使用新的文件路径。因为旧文件将在未来版本中弃用。应用程序必须确保包含正确的头文件并使用正确的搜索路径。

1.



例如：`#include`

2. CMake 或 Makefile 中任何指向组件文件夹的变量都需要被更改。

例如：[`VAR1=/opt/rocm/hip`{.docutils .literal .notranslate}]{.pre} 需要改为 [`VAR1=/opt/rocm`{.docutils .literal .notranslate}]{.pre} [`VAR2=/opt/rocm/hsa`{.docutils .literal .notranslate}]{.pre} 需要改为 [`VAR2=/opt/rocm`{.docutils .literal .notranslate}]{.pre}

3.  任何对 [`/opt/rocm/<component>/bin`{.docutils .literal .notranslate}]{.pre} 或 [`/opt/rocm/<component>/lib`{.docutils .literal .notranslate}]{.pre} 的引用都需要分别更改为 [`/opt/rocm/bin`{.docutils .literal .notranslate}]{.pre} 和 [`/opt/rocm/lib/`{.docutils .literal .notranslate}]{.pre}。



## 版本规范变更[\#](#changes-in-versioning-specifications "链接到此标题"){.headerlink}

为了更好地管理 ROCm（Radeon 开放计算平台）依赖规范，并使 ROCm（Radeon 开放计算平台）的发布更加顺畅，同时避免依赖冲突，ROCm（Radeon 开放计算平台）软件在编号和递增 ROCm 文件版本时应遵循以下方案：

rocm-\<ver\>，其中 \<ver\> = \<x.y.z\>

x.y.z 表示：MAJOR.MINOR.PATCH



z: PATCH - 在实现向后兼容的错误修复时递增 z。



y: MINOR - 在实现添加功能但仍保持向后兼容性的次要更改时递增 y。

x: MAJOR - 在实现不向后兼容的重大变更时递增 x。

[](../gpu-arch/mi100.html "上一页"){.left-prev}

::: prev-next-info
previous

AMD Instinct™ MI100 微架构

[](gpu-isolation.html "下一页"){.right-next}

::: prev-next-info
next

GPU 隔离技术

目录

- [引言](#introduction){.reference .internal .nav-link}
- [采用 FHS](#adopting-the-fhs){.reference .internal .nav-link}
- [早期 ROCm 版本的变更](#changes-from-earlier-rocm-versions){.reference .internal .nav-link}
- [ROCm FHS 重组：向后兼容性](#rocm-fhs-reorganization-backward-compatibility){.reference .internal .nav-link}
  - [包装器头文件](#wrapper-header-files){.reference .internal .nav-link}
  - [可执行文件](#executable-files){.reference .internal .nav-link}
  - [库文件](#library-files){.reference .internal .nav-link}
  - [CMake 配置文件](#cmake-config-files){.reference .internal .nav-link}
- [使用 ROCm 的应用所需变更](#changes-required-in-applications-using-rocm){.reference .internal .nav-link}
- [版本规范变更](#changes-in-versioning-specifications){.reference .internal .nav-link}