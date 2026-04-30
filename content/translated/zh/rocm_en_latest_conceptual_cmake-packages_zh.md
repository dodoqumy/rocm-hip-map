---
title: "Using CMake"
source_url: "https://rocm.docs.amd.com/en/latest/conceptual/cmake-packages.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---



::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angles-right}



::: header-article-item
- [](../index.html){.nav-link aria-label="首页"}
- 使用 CMake

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# 使用 CMake

## 目录

- [查找依赖项](#finding-dependencies){.reference .internal .nav-link}
- [在 CMake 中使用 HIP](#using-hip-in-cmake){.reference .internal .nav-link}
  - [使用 HIP 单源码编程模型](#using-the-hip-single-source-programming-model){.reference .internal .nav-link}
  - [使用 ROCm C/C++ 库](#consuming-rocm-c-c-libraries){.reference .internal .nav-link}
  - [在 C++ 代码中使用 HIP API](#consuming-the-hip-api-in-c-code){.reference .internal .nav-link}
  - [以 C++ 语言模式编译设备代码](#compiling-device-code-in-c-language-mode){.reference .internal .nav-link}
  - [ROCm CMake 包](#rocm-cmake-packages){.reference .internal .nav-link}
- [使用 CMake 预设](#using-cmake-presets){.reference .internal .nav-link}
  - [将 HIP 与预设配合使用](#using-hip-with-presets){.reference .internal .nav-link}

# 使用 CMake[\#](#using-cmake "Link to this heading"){.headerlink}



2026年1月23日

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS73NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 12 分钟阅读时间

适用于 Linux 和 Windows



ROCm（Radeon 开放计算平台）中的大多数组件都支持 CMake。依赖头文件组件或库组件的项目通常需要 CMake 3.5 或更高版本，而需要使用 CMake HIP（异构接口可移植性）语言支持的项目则需要 CMake 3.21 或更高版本。

## 查找依赖项[\#](#finding-dependencies "Link to this heading"){.headerlink}

注意

有关在 CMake 中处理依赖项的完整参考资料，请参阅 CMake 文档中的 [find_package](https://cmake.org/cmake/help/latest/command/find_package.html){.reference .external} 和 [Using Dependencies Guide](https://cmake.org/cmake/help/latest/guide/using-dependencies/index.html){.reference .external}，以获取 CMake 相关功能的概述。

简而言之，CMake 支持通过两种方式查找依赖项：

- 在 Module 模式下，它会查找一个文件 [`Find<PackageName>.cmake`{.docutils .literal .notranslate}]{.pre}，该文件尝试在典型的安装位置和布局中查找该组件。CMake 自带数十个此类脚本，但用户和项目也可以提供此类脚本。

- 在 Config 模式下，它会定位一个名为 [`

ROCm（Radeon开放计算平台）主要依赖Config模式，但有一个值得注意的例外：即用于在NVIDIA运行时上驱动HIP（异构接口可移植性）程序编译的模块。因此，当在标准系统位置找不到依赖项时，要么需要指示CMake使用[`CMAKE_PREFIX_PATH`{.docutils .literal .notranslate}]{.pre}变量（用分号分隔的文件系统路径列表）在其他文件夹中搜索包配置文件，要么按项目使用[`

设置这些变量的方法有近十二种。根据您的工作流程，其中一种可能比另一种更方便。从概念上讲，最简单的方法是通过 `-D` `CMAKE_PREFIX_PATH=....` 将其添加到命令行上的 CMake 配置命令中。AMD 打包的 ROCm（Radeon 开放计算平台）安装通常可以添加到配置文件搜索路径中，例如：

- Windows: [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_PREFIX_PATH=${env:HIP_PATH}`{.docutils .literal .notranslate}]{.pre}



- Linux：[`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_PREFIX_PATH=/opt/rocm`{.docutils .literal .notranslate}]{.pre}



ROCm（Radeon Open Compute Platform）提供相应的 *config-file* 包，这使得可以直接使用 [`find_package`{.docutils .literal .notranslate}]{.pre}。ROCm 不需要任何 Find 模块，因为 *config-file* 包随上游项目一起提供，例如 rocPRIM 和其他 ROCm 库。

关于在系统上安装 ROCm（Radeon 开放计算平台）的完整指南及方法，请参阅 [Linux](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html){.reference .external} 和 [Windows](https://rocm.docs.amd.com/projects/install-on-windows/en/latest/index.html){.reference .external} 的安装指南。

## 在 CMake 中使用 HIP（HIP（异构接口可移植性）））[](#using-hip-in-cmake "Link to this heading"){.headerlink}

ROCm（ROCm（Radeon 开放计算平台））组件提供 C/C++ 接口，支持通过 CMake 可识别的任何 C/C++ 工具链进行使用。ROCm（ROCm（Radeon 开放计算平台））还支持 CMake HIP（HIP（异构接口可移植性））语言特性，允许用户使用 HIP（HIP（异构接口可移植性））单源编程模型进行开发。当程序（或翻译单元）使用 HIP（HIP（异构接口可移植性））API 而不编译任何 GPU 设备代码时，HIP（HIP（异构接口可移植性））在 CMake 中可被视为一个简单的 C/C++ 库。

### 使用 HIP single-source 编程模型 [\#](#using-the-hip-single-source-programming-model "Link to this heading"){.headerlink}

用 HIP C++ 方言编写的源代码通常使用 `.hip` 扩展名。当 HIP CMake 语言被启用时，它会自动将此类源文件与所使用的 HIP 工具链关联起来。



```cmake
cmake_minimum_required(VERSION 3.21) # HIP（HIP（异构接口可移植性））语言支持需要3.21
cmake_policy(VERSION 3.21.3...3.27)
project(MyProj LANGUAGES HIP)
add_executable(MyApp Main.hip)
```

如果您有来自 HIP 源码兼容子集的现有 CUDA 代码，您可以告诉 CMake，尽管它们使用 .cu 扩展名，但它们是 HIP 源码。请注意，这主要用于编译仅包含内核代码的源文件，因为主机端 CUDA API 不会以此方式编译。

::: highlight
    add_library(MyLib MyLib.cu)
    set_source_files_properties(MyLib.cu PROPERTIES LANGUAGE HIP（HIP（异构接口可移植性））)



CMake 本身只托管 HIP 语言支持的一部分，例如定义 HIP 特定的属性等，而另一半则随 HIP 实现一起提供，例如 ROCm。CMake 将搜索名为 hip-lang-config.cmake 的文件，该文件描述了 CMake 定义的属性如何转换为工具链调用。如果使用非标准方法或布局安装 ROCm，而 CMake 无法找到此文件或检测到 SDK 的某些部分，则有一个万能的、最后的手段变量用于定位此文件，即 `CMAKE_HIP_COMPILER_ROCM_ROOT:PATH=`，该变量应设置为 ROCm 安装的根目录。

注意

由 hip-lang-config.cmake 定义的导入目标仅供内部使用。

如果用户未通过 [`CMAKE_HIP_ARCHITECTURES`{.docutils .literal .notranslate}]{.pre} 提供以分号分隔的设备架构列表，CMake 将选择一些合理的默认值。不过建议，如果用户明确知道他们希望针对的设备，则应显式设置此变量。

### 使用 ROCm (Radeon Open Compute Platform) C/C++ 库 [\#](#consuming-rocm-c-c-libraries "跳转至此标题"){.headerlink}

像 rocBLAS、rocFFT、MIOpen 等库均可作为 C/C++ 库使用。如下例所示一个 C++ 应用程序从 CMake 使用 MIOpen。它调用 `find_package(miopen)`，该函数可提供 `MIOpen` 导入目标。此目标可通过 `target_link_libraries` 进行链接。

::: highlight
    cmake_minimum_required(VERSION 3.5) # find_package(miopen) 需要 3.5
    cmake_policy(VERSION 3.5...3.27)
    project(MyProj LANGUAGES CXX)
    find_package(miopen)
    add_library(MyLib ...)
    target_link_libraries(MyLib PUBLIC MIOpen（MIOpen（AMD 深度学习基元库））)

注意



大多数库被设计为仅主机端 API，因此下游项目不需要使用 GPU 设备编译器，除非它们使用 GPU 设备代码。

### 在 C++ 代码中调用 HIP API[\#](#consuming-the-hip-api-in-c-code "Link to this heading"){.headerlink}

使用任何 C++ 编译器都可以在不编译单源 GPU 设备代码的情况下使用 HIP（异构接口可移植性） API。在这种情况下，[`find_package(hip)`{.docutils .literal .notranslate}]{.pre} 提供了 [`hip::host`{.docutils .literal .notranslate}]{.pre} 导入目标来使用 HIP。

::: highlight
    cmake_minimum_required(VERSION 3.5) # find_package(hip) requires 3.5
    cmake_policy(VERSION 3.5...3.27)
    project(MyProj LANGUAGES CXX)
    find_package(hip REQUIRED)
    add_executable(MyApp ...)
    target_link_libraries(MyApp PRIVATE hip::host)

当混合此类 [`CXX`{.docutils .literal .notranslate}]{.pre} 源文件和包含设备代码的 [`HIP（异构接口可移植性）`{.docutils .literal .notranslate}]{.pre} 源文件时，只需链接到 hip::host。如果 HIP（异构接口可移植性）源文件的扩展名不是 .hip，请对其使用 set_source_files_properties(\

### 在 C++ 语言模式下编译设备代码[\#](#compiling-device-code-in-c-language-mode "Link to this heading"){.headerlink}

注意力

这里详细描述的工作流程被视为遗留版本，仅供理解之用。它早于 CMake 中存在 HIP 语言支持。如果源代码中包含 HIP 设备代码，它就是一个 HIP 源文件，应该按照这种方式进行编译。只有当您的启用了 HIP 的 CMake 代码路径无法要求 CMake 3.21 版本时，才可以使用以下方法。

如果代码使用 HIP（HIP（异构接口可移植性）） API 并编译 GPU 设备代码，则需要使用设备编译器。CMake 的编译器可以通过 [`CMAKE_C_COMPILER`{.docutils .literal .notranslate}]{.pre} 和 [`CMAKE_CXX_COMPILER`{.docutils .literal .notranslate}]{.pre} 变量设置，也可以使用 `CC` 和 `CXX` 环境变量设置。这可以在配置 CMake 时设置，也可以放入 CMake 工具链文件中。设备编译器必须设置为支持 AMD GPU 目标的编译器，通常是 Clang。

`[\`find_package(hip)\`{.docutils .literal .notranslate}]{.pre} 提供 `[\`hip::device\`{.docutils .literal .notranslate}]{.pre}` 导入目标，以添加设备编译所需的所有标志。

::: highlight
    cmake_minimum_required(VERSION 3.8) # cxx_std_11 需要 3.8 版本
    cmake_policy(VERSION 3.8...3.27)
    project(MyProj LANGUAGES CXX)
    find_package(hip REQUIRED)
    add_library(MyLib ...)
    target_link_libraries(MyLib PRIVATE hip::device)
    target_compile_features(MyLib PRIVATE cxx_std_11)

注意

编译到GPU设备需要至少C++11。

该项目可以使用以下 CMake 命令进行配置：



- Windows: `-D CMAKE_CXX_COMPILER:PATH=${env:HIP_PATH}\bin\clang++.exe`

- Linux: [`cmake`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_CXX_COMPILER:PATH=/opt/rocm/bin/amdclang++`{.docutils .literal .notranslate}]{.pre}



Which use the device compiler provided from the binary packages of [ROCm（Radeon 开放计算平台） HIP（异构接口可编程性） SDK](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html){.reference .external} and [repo.radeon.com](https://repo.radeon.com){.reference .external} respectively.

当使用 [`CXX`{.docutils .literal .notranslate}]{.pre} 语言支持编译 HIP 设备代码时，通过设置 [`GPU_TARGETS`{.docutils .literal .notranslate}]{.pre} 变量来选择目标 GPU 架构。[`CMAKE_HIP_ARCHITECTURES`{.docutils .literal .notranslate}]{.pre} 仅在 HIP 语言启用时存在。默认情况下，它会设置为 AMD ROCm 当前支持的架构的某个子集。可以通过 CMake 选项 [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`GPU_TARGETS="gfx1032;gfx1035"`{.docutils .literal .notranslate}]{.pre} 进行设置。

ROCm（Radeon 开放计算平台）CMake 包[\#](#rocm-cmake-packages "链接到此标题"){.headerlink}

::: pst-scrollable-table-container
  组件    包      目标
  ------------ ------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  HIP（HIP（异构接口可移植性））          hip          [`hip::host`{.docutils .literal .notranslate}]{.pre}, [`hip::device`{.docutils .literal .notranslate}]{.pre}
  rocPRIM      rocprim      [`roc::rocprim`{.docutils .literal .notranslate}]{.pre}
  rocThrust（rocThrust（ROCm并行算法库））    rocthrust    [`roc::rocthrust`{.docutils .literal .notranslate}]{.pre}
  hipCUB       hipcub       [`hip::hipcub`{.docutils .literal .notranslate}]{.pre}
  rocRAND（rocRAND（ROCm随机数生成库））      rocrand      [`roc::rocrand`{.docutils .literal .notranslate}]{.pre}
  rocBLAS（rocBLAS（ROCm基础线性代数子程序库））      rocblas      [`roc::rocblas`{.docutils .literal .notranslate}]{.pre}
  rocSOLVER（rocSOLVER（ROCm求解器库））    rocsolver    [`roc::rocsolver`{.docutils .literal .notranslate}]{.pre}
  hipBLAS（hipBLAS（HIP基础线性代数库））      hipblas      [`roc::hipblas`{.docutils .literal .notranslate}]{.pre}
  rocFFT（rocFFT（ROCm快速傅里叶变换库））       rocfft       [`roc::rocfft`{.docutils .literal .notranslate}]{.pre}
  hipFFT       hipfft       [`hip::hipfft`{.docutils .literal .notranslate}]{.pre}
  rocSPARSE    rocsparse    [`roc::rocsparse`{.docutils .literal .notranslate}]{.pre}
  hipSPARSE    hipsparse    [`roc::hipsparse`{.docutils .literal .notranslate}]{.pre}
  rocALUTION   rocalution   [`roc::rocalution`{.docutils .literal .notranslate}]{.pre}
  RCCL（RCCL（ROCm集合通信库））         rccl         [`rccl`{.docutils .literal .notranslate}]{.pre}
  MIOpen（MIOpen（AMD深度学习基元库））       miopen       [`miopen::miopen`{.docutils .literal .notranslate}]{.pre}
  MIGraphX     migraphx     [`migraphx::migraphx`{.docutils .literal .notranslate}]{.pre}, [`migraphx::migraphx_c`{.docutils .literal .notranslate}]{.pre}, [`migraphx::migraphx_cpu`{.docutils .literal .notranslate}]{.pre}, [`migraphx::migraphx_gpu`{.docutils .literal .notranslate}]{.pre}, [`migraphx::migraphx_onnx`{.docutils .literal .notranslate}]{.pre}, [`migraphx::migraphx_tf`{.docutils .literal .notranslate}]{.pre}



## 使用 CMake 预设配置[\#](#using-cmake-presets "Link to this heading"){.headerlink}

CMake 命令行的具体长度取决于用户编译代码时的偏好。这正是项目通常会将脚本片段嵌入到构建定义中的主要原因——控制编译器警告级别、更改 CMake 默认值（[`CMAKE_BUILD_TYPE`{.docutils .literal .notranslate}]{.pre} 或 [`BUILD_SHARED_LIBS`{.docutils .literal .notranslate}]{.pre} 仅举几例），以及引入各种反模式，一切都是为了使用方便。

命令行界面(CLI)上的加载通过选择工具链（即用于编译程序的工具集）立即启动。为了减轻工具链相关的一些麻烦，CMake 确实会分别查询 [`CC`{.docutils .literal .notranslate}]{.pre} 和 [`CXX`{.docutils .literal .notranslate}]{.pre} 环境变量来设置默认的 [`CMAKE_C[XX]_COMPILER`{.docutils .literal .notranslate}]{.pre}，但这只是冰山一角。有相当多的变量仅与工具链本身相关（通常通过 [toolchain files](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html){.reference .external} 提供），然后我们还没有讨论用户偏好或项目特定的选项。

支持 CMake 的 IDE（Visual Studio、Visual Studio Code、CLion 等）都开发了自己的方式来注册不同用途的命令行片段，采用一次设置即可遗忘的方式，以便通过图形前端快速组装。这看起来不错，但配置不可移植，也无法在持续集成（CI）流水线中重用。CMake 将现有实践浓缩为一种可在所有 IDE 中工作并可从任何命令行调用的可移植 JSON 格式。这就是 [CMake Presets](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html){.reference .external}。



存在两种类型的预设文件：一种由项目提供，称为 `CMakePresets.json`，用于提交到版本控制，通常用于驱动 CI；另一种由用户提供，称为 `CMakeUserPresets.json`，通常用于存放用户偏好并使构建适应用户的环。这些 JSON 文件可以包含其他 JSON 文件，用户预设始终隐式包含非用户变体。

### 使用 HIP（异构接口可移植性）与预设[\#](#using-hip-with-presets "Link to this heading"){.headerlink}

以下是一个示例 [`CMakeUserPresets.json`{.docutils .literal .notranslate}]{.pre} 文件，该文件实际编译了 [amd/rocm-examples](https://github.com/amd/rocm-examples){.reference .external} 示例应用套件（在典型的 ROCm（Radeon 开放计算平台）安装上）：

{
  "version": 3,
  "cmakeMinimumRequired": {
    "major": 3,
    "minor": 21,
    "patch": 0
  },
  "configurePresets": [
    {
      "name": "layout",
      "hidden": true,
      "binaryDir": "${sourceDir}/build/${presetName}",
      "installDir": "${sourceDir}/install/${presetName}"
    },
    {
      "name": "generator-ninja-multi-config",
      "hidden": true,
      "generator": "Ninja Multi-Config"
    },
    {
      "name": "toolchain-makefiles-c/c++-amdclang",
      "hidden": true,
      "cacheVariables": {
        "CMAKE_C_COMPILER": "/opt/rocm/bin/amdclang",
        "CMAKE_CXX_COMPILER": "/opt/rocm/bin/amdclang++",
        "CMAKE_HIP_COMPILER": "/opt/rocm/bin/amdclang++"
      }
    },
    {
      "name": "clang-strict-iso-high-warn",
      "hidden": true,
      "cacheVariables": {
        "CMAKE_C_FLAGS": "-Wall -Wextra -pedantic",
        "CMAKE_CXX_FLAGS": "-Wall -Wextra -pedantic",
        "CMAKE_HIP_FLAGS": "-Wall -Wextra -pedantic"
      }
    },
    {
      "name": "ninja-mc-rocm",
      "displayName": "Ninja Multi-Config ROCm（ROCm（Radeon 开放计算平台））",
      "inherits": [
        "layout",
        "generator-ninja-multi-config",
        "toolchain-makefiles-c/c++-amdclang",
        "clang-strict-iso-high-warn"
      ]
    }
  ],
  "buildPresets": [
    {
      "name": "ninja-mc-rocm-debug",
      "displayName": "Debug",
      "configuration": "Debug",
      "configurePreset": "ninja-mc-rocm"
    },
    {
      "name": "ninja-mc-rocm-release",
      "displayName": "Release",
      "configuration": "Release",
      "configurePreset": "ninja-mc-rocm"
    },
    {
      "name": "ninja-mc-rocm-debug-verbose",
      "displayName": "Debug (verbose)",
      "configuration": "Debug",
      "configurePreset": "ninja-mc-rocm",
      "verbose": true
    },
    {
      "name": "ninja-mc-rocm-release-verbose",
      "displayName": "Release (verbose)",
      "configuration": "Release",
      "configurePreset": "ninja-mc-rocm",
      "verbose": true
    }
  ],
  "testPresets": [
    {
      "name": "ninja-mc-rocm-debug",
      "displayName": "Debug",
      "configuration": "Debug",
      "configurePreset": "ninja-mc-rocm",
      "execution": {
        "jobs": 0
      }
    },
    {
      "name": "ninja-mc-rocm-release",
      "displayName": "Release",
      "configuration": "Release",
      "configurePreset": "ninja-mc-rocm",
      "execution": {
        "jobs": 0
      }
    }
  ]
}

注意

要使预设在 Windows 上可靠地运行，需要进行一些 CMake 改进和/或获得编译器供应商的支持。（请参考 [Add support to the Visual Studio generators](https://gitlab.kitware.com/cmake/cmake/-/issues/24245){.reference .external} 和 [Sourcing environment scripts](https://gitlab.kitware.com/cmake/cmake/-/issues/21619){.reference .external}。）

[](gpu-isolation.html "上一页"){.left-prev}

::: prev-next-info
previous

GPU 隔离技术

[](ai-pytorch-inception.html "下一页"){.right-next}

::: prev-next-info
下一页



深度学习：Inception V3 与 PyTorch

:::: sidebar-secondary-item
目录

- [查找依赖项](#finding-dependencies){.reference .internal .nav-link}
- [在 CMake 中使用 HIP](#using-hip-in-cmake){.reference .internal .nav-link}
  - [使用 HIP 单源编程模型](#using-the-hip-single-source-programming-model){.reference .internal .nav-link}
  - [使用 ROCm C/C++ 库](#consuming-rocm-c-c-libraries){.reference .internal .nav-link}
  - [在 C++ 代码中使用 HIP API](#consuming-the-hip-api-in-c-code){.reference .internal .nav-link}
  - [使用 C++ 语言模式编译设备代码](#compiling-device-code-in-c-language-mode){.reference .internal .nav-link}
  - [ROCm CMake 包](#rocm-cmake-packages){.reference .internal .nav-link}
- [使用 CMake 预设](#using-cmake-presets){.reference .internal .nav-link}
  - [将 HIP 与预设配合使用](#using-hip-with-presets){.reference .internal .nav-link}