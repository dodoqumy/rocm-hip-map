---
title: "Fine-tune Llama-3.1 8B with torchtune &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/torchtune_llama3.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T18:59:43.521845+00:00
content_hash: "3fea37f2b1793777"
---

# 使用 torchtune 微调 Llama-3.1 8B[#](#fine-tune-llama-3-1-8b-with-torchtune)

**作者**: Bill He

**知识水平**: Intermediate

本教程演示了如何利用 torchtune 在 AMD ROCm（ROCm（Radeon 开放计算平台）） GPU 上对 Llama-3.1 8B 大语言模型（LLM）进行微调。Torchtune 是一个易于使用的 PyTorch 库，用于编写、后训练和实验 LLM。它具有以下特点：

可定制的训练配方，用于SFT、知识蒸馏、RL和RLHF，以及量化感知训练。

流行的LLM（如Llama, Gemma, Mistral, Phi, Qwen等）的简单PyTorch实现。

利用最新的PyTorch API，实现了开箱即用的顶级内存效率、性能提升和扩展性。

用于轻松配置训练、评估、量化或推理流程的YAML配置文件。

如需更多信息，请参阅[官方 torchtune GitHub 页面](https://github.com/pytorch/torchtune)。

## 先决条件[#](#prerequisites)

本教程是在以下环境中开发和测试的。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**：确保您的系统运行的是 Ubuntu 22.04 版本。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPUs**：本教程已在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 上测试。请确保您使用支持 ROCm 的 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 或兼容硬件，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.3**: 按照 [ROCm 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm。完成安装后，使用以下命令确认配置：该命令会列出您的 AMD GPU 及其相关详细信息。

**注意**: 对于 ROCm（ROCm（Radeon 开放计算平台）） 6.4 及更早版本，请使用 `rocm-smi`

而是使用命令。**Docker**：确保 Docker 已正确安装和配置。请遵循适用于您操作系统的 Docker 安装指南。**注意**：确保正确配置了 Docker 权限。要配置允许非 root 用户访问的权限，请运行以下命令：usermod -aG docker $USER newgrp docker

验证 Docker 是否正常工作：

运行 hello-world

### Hugging Face API 访问[#](#hugging-face-api-access)

从...获取 API token

[Hugging Face](https://huggingface.co) 用于下载模型。确保 Hugging Face API 令牌具有必要的权限和批准以访问

[Meta Llama 检查点](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).

### 数据准备[#](#data-preparation)

本教程使用来自 Hugging Face 的示例数据集，该数据集在设置步骤中准备完成。

## 准备训练环境[#](#prepare-the-training-environment)

### 1. 拉取 Docker 镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的 Docker 镜像：

```
pull rocm/pytorch-training:latest
```

```

### 2. 启动 Docker 容器[#](#launch-the-docker-container)

启动 Docker 容器并映射必要的目录。将 `/path/to/notebooks` 替换为实际路径。

使用您主机上存储这些笔记本的目录的完整路径。

```
run -it --rm \
--network=host \
--device=/dev/kfd \
--device=/dev/dri \
--group-add=video \
--ipc=host \
--cap-add=SYS_PTRACE \
--security-opt seccomp=unconfined \
--shm-size 8G \
-v $(pwd):/workspace \
-w /workspace/notebooks \
rocm/pytorch-training:latest
```

```

**注意**：该命令将当前目录挂载到 `/workspace`

容器中的目录。确保 notebook 文件要么在运行 Docker 命令前复制到此目录，要么在 Jupyter Notebook 环境启动后上传到其中。保存终端输出中提供的令牌或 URL，以便从 Web 浏览器访问该 notebook。您可以从 [AI Developer Hub GitHub 仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev) 下载此 notebook。

### 3. 安装和启动 Jupyter[#](#install-and-launch-jupyter)

在Docker容器内，使用以下命令安装Jupyter：

```
安装 jupyter
```

```

启动Jupyter服务器：

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

**注意**：确保端口 `8888`

在运行上述命令之前，请确保该端口在你的系统上尚未被使用。如果已被占用，你可以通过替换 `--port=8888` 来指定一个不同的端口。

使用另一个端口号，例如，`--port=8890`

.

### 4. 安装必需的库[#](#install-the-required-libraries)

安装本教程所需的库。在Docker容器内运行的Jupyter notebook中执行以下命令：

```
# 安装 PyTorch、torchvision、torchao 的夜间构建版本
!pip install --pre --upgrade torch torchvision torchao --index-url https://download.pytorch.org/whl/nightly/rocm6.3/
!pip install --pre --upgrade torchtune --extra-index-url https://download.pytorch.org/whl/nightly/rocm6.3/
# 此笔记本已在 torch==2.7.0.dev20250302+rocm6.3、torchao==0.10.0.dev20250303+rocm6.3、torchvision==0.22.0.dev20250302+rocm6.3、torchtune==0.6.0.dev20250302+rocm6.3 下验证
```

```

验证安装：

```
# 验证所需库的安装和版本
!pip list | grep torch
```

```

以下是预期的输出：

```
pytorch-triton-rocm 3.2.0+git4b3bb1f8
torch 2.7.0.dev20250302+rocm6.3
torchdata 0.11.0
torchtune 0.6.0.dev20250302+rocm6.3
```

```

### 5. 验证适用于 ROCm（Radeon 开放计算平台）6.3 的 torchtune[#](#verify-torchtune-for-rocm-6-3)

要确认软件包是否正确安装，请运行以下命令：

```!tune --help```

```

您应该看到以下输出：

**⚠️ 重要：确保选择了正确的内核**

如果验证过程失败，请确保为您的笔记本选择了正确的Jupyter内核。要更改内核，请按照以下步骤操作：

转到

**内核函数 (Kernel)**menu.Select

**更改 内核函数 (Kernel)**.Select

Python 3 (ipykernel)

从列表中。

**重要说明**：未能选择正确的内核可能会导致运行笔记本时出现意外问题。

### 6. 提供您的 Hugging Face token[#](#provide-your-hugging-face-token)

您需要一个 Hugging Face API 令牌才能访问 Llama-3.1。请在 [Hugging Face Tokens](https://huggingface.co/settings/tokens) 生成您的令牌，并申请访问 [Llama-3.1 8B](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)。令牌通常以“hf_”开头。

在Jupyter笔记本中运行以下交互式代码块以设置token:

**注意**：取消勾选“Add token as Git credential”选项。

```
from huggingface_hub import notebook_login, HfApi
# 提示用户登录
notebook_login()
```

```

验证您的令牌已被正确接受：

```
from huggingface_hub import HfApi
try:
api = HfApi()
user_info = api.whoami()
print(f"Token validated successfully! Logged in as: {user_info['name']}")
except Exception as e:
print(f"Token validation failed. Error: {e}")
```

```

## 微调模型[#](#fine-tuning-the-model)

本节介绍了使用 torchtune 设置并运行 Llama-3.1 模型微调的过程。以下步骤描述了如何设置 GPU、导入所需库、配置模型和训练参数，以及运行微调流程。

**⚠️ 重要：确保选择了正确的内核**

确保为您的笔记本选择了正确的Jupyter内核。要更改内核，请按照以下步骤操作：

转到

**内核函数 (Kernel)**menu.Select

**更改内核函数 (Kernel)**.选择

Python 3 (ipykernel)

从列表中.

**重要**：未能选择正确的内核可能导致运行笔记本时出现意外问题。

### 设置并验证 GPU 可用性[#](#set-and-verify-the-gpu-availability)

首先指定可用于微调的 GPU。确认它们已被 PyTorch 正确检测。

```
import os
import torch
gpus= [0, 1] # Rank 0 用于 MI300x 单设备微调，Rank 0/1 用于完整微调
os.environ.setdefault("CUDA_VISIBLE_DEVICES", ','.join(map(str, gpus)))
# 确保 PyTorch 正确检测到 GPU
print(f"PyTorch 检测到的可用设备数量: {torch.cuda.device_count()}")
```

```

### 下载Llama模型[#](#download-the-llama-model)

运行以下命令将权重文件下载到您的本地机器。此过程还会下载分词器模型及一份负责任使用指南。

要下载Llama-3.1，请使用以下命令：

```
!tune download meta-llama/Meta-Llama-3.1-8B-Instruct \
--output-dir /tmp/Meta-Llama-3.1-8B-Instruct \
--ignore-patterns "original/consolidated.00.pth"
```

```

### 运行微调配方[#](#run-the-fine-tuning-recipes)

使用这些微调方案进行单GPU或分布式训练。

#### 单GPU训练[#](#single-gpu-training)

默认情况下，使用 [alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca) 数据集进行微调。你可以使用以下命令在单个 GPU 上通过 LoRA 微调 Llama-3.1 8B 模型：

```
!tune run lora_finetune_single_device --config llama3_1/8B_lora_single_device
```

```

#### 分布式训练[#](#distributed-training)

对于分布式训练，tune CLI 集成了 torchrun。

**注意**：你必须拥有多个可用的GPU才能运行分布式训练示例。要在两个GPU上对Llama-3.1 8B进行完整微调，请使用以下命令：

```
!tune run --nproc_per_node 2 full_finetune_distributed --config llama3_1/8B_full
```

```

### 自定义你的 Llama 配方[#](#customize-your-recipes-for-llama)

修改配置有两种方式。

#### 配置覆盖[#](#configuration-overrides)

您可以直接从命令行覆盖配置字段。例如，您可以将批次大小设置为 `16`。

并使用相同的命令禁用激活检查点。

```
!tune run lora_finetune_single_device \
--config llama3_1/8B_lora_single_device \
batch_size=16 \
enable_activation_checkpointing=False
```

```

**注意**：如果遇到内存不足（OOM）错误，请减少 `batch_size`。

或启用梯度检查点。使用 `amd-smi`

在微调期间监控VRAM使用情况。对于ROCm 6.4及更早版本，请使用`rocm-smi`

用于此目的的命令。

#### 更新本地副本[#](#update-a-local-copy)

您也可以将配置复制到本地目录，并直接修改其中的内容：

```
!tune cp llama3_1/8B_lora_single_device ./my_custom_config_llama3_1_8B_lora_single_device.yaml
# Copied to ./my_custom_config_llama3_1_8B_lora_single_device.yaml
```

```

然后，您可以通过应用 `tune run` 来运行您的自定义配方。

命令到您的本地文件：

```
!tune run lora_finetune_single_device --config ./my_custom_config_llama3_1_8B_lora_single_device.yaml
```

```

运行 `tune --help`

查看所有可能的 CLI 命令和选项的命令。有关使用和更新配置的更多信息，请参阅官方 torchtune [深度解析](https://meta-pytorch.org/torchtune/main/deep_dives/configs.html)。

### 自定义数据集[#](#custom-datasets)

torchtune

支持在多种不同的数据集上进行微调，包括指令型、聊天型、偏好型数据集等。要了解更多如何将这些组件应用于您自己自定义数据集的微调，请参阅所提供的链接以及 torchtune API [文档](https://meta-pytorch.org/torchtune/main/api_ref_datasets.html)。

### 监控GPU内存[#](#monitoring-gpu-memory)

要在训练期间监控GPU内存，请在终端中运行以下命令。

**注意**：对于 ROCm（ROCm（Radeon 开放计算平台）） 6.4 及更早版本，请使用 `rocm-smi`

而是使用命令。

```
!amd-smi
```

```

该命令显示内存使用情况和其他GPU指标，以确保您的硬件资源得到最佳利用。