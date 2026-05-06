---
title: "Fine-tune Llama-3.1 8B with Llama-Factory &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/llama_factory_llama3.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:23.736203+00:00
content_hash: "e0dd2731b3e8c551"
---

# 使用 Llama-Factory 微调 Llama-3.1 8B[#](#fine-tune-llama-3-1-8b-with-llama-factory)

作者: Alex He

**知识水平**：中级

本教程演示了如何通过利用 Llama-Factory，在 AMD ROCm（Radeon 开放计算平台）GPU 上对 Llama-3.1 8B 大语言模型（LLM）进行微调。高效微调对于将大语言模型适配到下游任务至关重要。然而，在不同模型上实现这些方法需要付出不少努力。

[Llama-Factory](https://github.com/hiyouga/LLaMA-Factory) 是一个统一框架，集成了一套先进的、高效的训练方法。

它提供了一种解决方案，通过内置的Web UI LLAMABOARD，无需编码即可灵活定制超过100个LLM的微调。

## 先决条件[#](#prerequisites)

本教程是在以下设置下开发和测试的。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**：确保您的系统运行 Ubuntu 22.04 版本。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPUs**：本教程已在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 上测试。请确保您使用的是支持 ROCm（ROCm（Radeon 开放计算平台））的 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 或兼容硬件，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.3**: 按照[ROCm（ROCm（Radeon 开放计算平台）） 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html)安装并验证ROCm（ROCm（Radeon 开放计算平台））。安装后，使用以下命令确认您的设置：该命令会列出您的AMD GPU及其相关信息。

**注意**：对于 ROCm 6.4 及更早版本，请使用 `rocm-smi`

command instead.**Docker**：确保已正确安装并配置Docker。请根据您的操作系统参考Docker安装指南。**注意**：确保正确配置Docker权限。若要允许非root用户访问，请运行以下命令：  
`usermod -aG docker $USER`  
`newgrp docker`

验证 Docker 是否正确工作

运行 hello-world

### Hugging Face API 访问[#](#hugging-face-api-access)

从获取API令牌

[Hugging Face](https://huggingface.co)用于下载模型。确保 Hugging Face API 令牌拥有必要的权限和批准以访问

[Meta Llama 检查点](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).

### 数据准备[#](#data-preparation)

本教程使用Hugging Face的样本数据集，该数据集在设置步骤中准备。

## 准备训练环境[#](#prepare-the-training-environment)

### 1. 拉取 Docker 镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的 Docker 镜像：

```
pull rocm/pytorch-training:latest

```

### 2. 启动 Docker 容器[#](#launch-the-docker-container)

启动Docker容器并映射必要的目录。将`/path/to/notebooks`替换为实际路径。

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

**注意**: 此命令将当前目录挂载到 `/workspace`

容器中的目录。确保在运行 Docker 命令之前将笔记本文件复制到此目录，或在 Jupyter Notebook 环境启动后将其上传。保存终端输出中提供的令牌或 URL，以便从 Web 浏览器访问该笔记本。您可以从 [AI Developer Hub GitHub 仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev) 下载此笔记本。

### 3. 安装并启动 Jupyter[#](#install-and-launch-jupyter)

在 Docker 容器内部，使用以下命令安装 Jupyter：

```
安装 Jupyter
```

```

启动 Jupyter 服务器：

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

**注意**：确保端口 `8888`

在运行上述命令之前，请确保其未在您的系统上被占用。如果已被占用，您可以通过替换 `--port=8888` 来指定不同的端口。

使用另一个端口号，例如 `--port=8890`

。

### 4. 安装所需的库[#](#install-the-required-libraries)

安装本教程所需的库。在 Docker 容器内运行的 Jupyter notebook 中执行以下命令：

```
!pip3 install -U deepspeed==0.16.5
# 从源代码安装 Llama-Factory
!git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git && cd LLaMA-Factory && pip install -e ".[torch,metrics]"
# 本笔记本在 llamafactory==0.9.3.dev0 deepspeed==0.16.5 下验证
```

```

验证安装：

```
# 验证所需库的安装和版本
!pip list | grep llamafactory
```

```

（未提供需要翻译的文本）

llamafactory 0.9.3.dev0

```

### 5. 验证 Llama-Factory 在 ROCm（Radeon 开放计算平台）6.3 上的运行[#](#verify-llama-factory-for-rocm-6-3)

要确认软件包已正确安装，请运行以下命令：

!llamafactory-cli help

```

您应该看到以下输出：

```
----------------------------------------------------------------------
| 用法: |
| llamafactory-cli api -h: 启动 OpenAI 风格的 API 服务器 |
| llamafactory-cli chat -h: 在 CLI 中启动聊天界面 |
| llamafactory-cli eval -h: 评估模型 |
| llamafactory-cli export -h: 合并 LoRA 适配器并导出模型 |
| llamafactory-cli train -h: 训练模型 |
| llamafactory-cli webchat -h: 在 Web UI 中启动聊天界面 |
| llamafactory-cli webui: 启动 LlamaBoard |
| llamafactory-cli version: 显示版本信息 |
----------------------------------------------------------------------
```

```

**⚠️ 重要**: 确保选择了正确的内核

如果验证过程失败，请确保为您的笔记本选择了正确的Jupyter内核。要更改内核，请按照以下步骤操作：

转到

**内核函数 (Kernel)** menu.Select

更改 内核函数 (Kernel).Select

Python 3 (ipykernel)

从列表中。

**重要**：未能选择正确的内核可能导致运行笔记本时出现意外问题。

### 6. 提供你的 Hugging Face 令牌[#](#provide-your-hugging-face-token)

您需要一个Hugging Face API令牌来访问Llama-3.1。在 [Hugging Face Tokens](https://huggingface.co/settings/tokens) 生成您的令牌，并为 [Llama-3.1 8B](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) 请求访问权限。令牌通常以“hf_”开头。

在 Jupyter notebook 中运行以下交互块以设置 token：

**注意**：取消选中“Add token as Git credential”选项。

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
print(f"令牌验证成功！已登录为：{user_info['name']}")
except Exception as e:
print(f"令牌验证失败。错误：{e}")
```

```

## 微调模型[#](#fine-tuning-the-model)

本节涵盖使用Llama-Factory设置和运行Llama-3模型微调的过程。以下步骤描述了如何设置GPU、导入所需库、配置模型和训练参数以及运行微调流程。

**⚠️ 重要**：确保选择了正确的内核

确保为笔记本选择了正确的Jupyter内核。要更改内核，请按照以下步骤操作：

前往

**内核函数 (Kernel)** 菜单.选择

**更改内核函数 (Kernel)**.Select

Python 3 (ipykernel)

从列表中。

**重要提示**：未能选择正确的kernel可能导致运行笔记本时出现意外问题。

### 设置并验证GPU可用性[#](#set-and-verify-the-gpu-availability)

首先指定可用于微调的 GPU，并验证 PyTorch 是否已正确检测到它们。

```
import os
import torch
gpus= [0, 1] # Rank 0 用于 MI300x 单设备微调，Rank 0/1 用于完整训练
os.environ.setdefault("CUDA_VISIBLE_DEVICES", ','.join(map(str, gpus)))
# 确保 PyTorch 正确检测到 GPU
print(f"PyTorch 检测到的可用设备数量: {torch.cuda.device_count()}")
```

```

### 下载模型[#](#download-the-model)

运行以下命令将权重下载到您的本地机器。此操作还会下载分词器模型和负责任使用指南。

要下载 Llama-3，请使用以下命令：

```
!huggingface-cli download --resume-download meta-llama/Meta-Llama-3-8B-Instruct
```

```

### 运行微调配方[#](#run-the-fine-tuning-recipes)

现在使用微调配方 `llama3_full_sft.yaml`

用于分布式训练。此配方预定义了 [dataset identity](https://github.com/hiyouga/LLaMA-Factory/blob/main/data/identity.json) 和 [alpaca_en_demo](https://github.com/hiyouga/LLaMA-Factory/blob/main/data/alpaca_en_demo.json) JSON 文件。

**注意**：这些数据集仅用于评估目的。您可能需要将它们替换为实际的数据集。

您可以使用以下命令在八块GPU上微调Llama-3 8B模型：

```
!cd LLaMA-Factory/ && llamafactory-cli train examples/train_full/llama3_full_sft.yaml
```

```

### 监控 GPU 内存[#](#monitoring-gpu-memory)

在训练期间监控GPU内存，请在终端中运行以下命令。

**注意**：对于 ROCm（ROCm（Radeon 开放计算平台）） 6.4 及更早版本，请使用 `rocm-smi`

改用命令。

!amd-smi

```

该命令显示内存使用情况和其他 GPU 指标，以确保您的硬件资源得到最佳利用。