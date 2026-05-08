---
title: "Deploying Llama-3.1 8B using vLLM &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/3_inference_ver3_HF_vllm.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:29.414193+00:00
content_hash: "d072f9a85e8f67c5"
---

# 使用 vLLM 部署 Llama-3.1 8B[#](#deploying-llama-3-1-8b-using-vllm)

**作者**: Seungrok Jung 和 Hyukjoon Lee

**知识水平**：初学者

vLLM 是一个开源库，旨在为大型语言模型（LLM）推理提供高吞吐量和低延迟。它通过高效地批量处理请求并充分利用GPU资源来优化文本生成工作负载，使开发者能够管理诸如代码生成和大规模对话式AI等复杂任务。

本教程将指导您如何在 AMD Instinct™ GPU 上使用 ROCm™ 软件栈设置和运行 vLLM。学习如何配置环境、容器化工作流，并向 vLLM 支持的推理服务器发送测试查询。

## 先决条件[#](#prerequisites)

本教程是在以下环境下开发和测试的。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**：确保你的系统运行的是 Ubuntu 22.04 版本。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPUs**: 本教程已在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 上测试通过。请确保您使用的是支持 ROCm（ROCm（Radeon 开放计算平台）） 的 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 或兼容硬件，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.2 或 6.3**：按照 [ROCm 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm。安装后，使用以下命令确认设置：此命令将列出您的 AMD GPU 及相关详细信息。

**注意**：对于ROCm（ROCm（Radeon 开放计算平台）） 6.4及更早版本，请使用`rocm-smi`

改为使用命令。**Docker**：确保 Docker 已正确安装和配置。请按照您的操作系统的 Docker 安装指南进行操作。**注意**：确保 Docker 权限已正确配置。要配置权限以允许非 root 用户访问，请运行以下命令：`usermod -aG docker $USER` `newgrp docker`

验证 Docker 是否正常工作：

运行 hello-world

### Hugging Face API 访问[#](#hugging-face-api-access)

从...获取API token

使用 [Hugging Face](https://huggingface.co) 下载模型。确保 Hugging Face API token 具有必要的权限和批准以访问。

[Meta的Llama检查点](https://huggingface.co/meta-llama/Llama-3.1-8B)

## 准备推理环境[#](#prepare-the-inference-environment)

按照以下步骤准备推理环境以供使用。

### 1. 启动 Docker 容器[#](#launch-the-docker-container)

在终端中运行以下命令，拉取包含所有必要依赖的预构建Docker镜像，并以正确的配置启动Docker容器：

run -it --rm \
--network=host \
--device=/dev/kfd \
--device=/dev/dri \
--group-add=video \
--ipc=host \
--cap-add=SYS_PTRACE \
--security-opt seccomp=unconfined \
--shm-size 8G \
--hostname=ROCm（ROCm（Radeon 开放计算平台））-FT \
--env HUGGINGFACE_HUB_CACHE=/workspace \
-v $(pwd):/workspace \
-w /workspace/notebooks \
--entrypoint /bin/bash \
vllm/vllm-openai-rocm:v0.15.0

```

**注意**: 此命令将当前目录挂载到 `/workspace`

容器中的目录。确保在运行 Docker 命令之前已将笔记本文件复制到此目录，或者在 Jupyter Notebook 环境启动后将其上传。保存终端输出中提供的令牌或 URL，以便从 Web 浏览器访问笔记本。您可以从 [AI Developer Hub GitHub 仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev) 下载此笔记本。

### 2. 安装并启动Jupyter[#](#install-and-launch-jupyter)

在Docker容器内，使用以下命令安装Jupyter：

```
安装 jupyter
```

```

然后启动 Jupyter 服务器：

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

**注意**: 确保端口 `8888`

在运行上述命令之前，请确保该端口未在你的系统上被占用。如果已被占用，你可以通过替换 `--port=8888` 来指定不同的端口。

使用另一个端口号，例如 `--port=8890`

.

### 3. 提供您的 Hugging Face 令牌[#](#provide-your-hugging-face-token)

您需要一个 Hugging Face API token 来访问 meta-llama/Llama-3.1-8B-Instruct。请在 [Hugging Face Tokens](https://huggingface.co/settings/tokens) 生成您的 token，并申请访问 [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)。Token 通常以 "hf_" 开头。

在您的 Jupyter notebook 中运行以下交互块来设置令牌：

**注意**：取消勾选“Add token as Git credential?”选项。

```
from huggingface_hub import notebook_login, HfApi
# 提示用户登录
notebook_login()
```

```

验证您的令牌已被正确接受：

```
# 验证Token
try:
    api = HfApi()
    user_info = api.whoami()
    print(f"Token验证成功！当前登录用户: {user_info['name']}")
except Exception as e:
    print(f"Token验证失败。错误: {e}")
```

```

## 使用 vLLM 部署 LLM[#](#deploying-the-llm-using-vllm)

开始使用 vLLM 在 Jupyter notebook 中部署 LLM（meta-llama/Llama-3.1-8B-Instruct）：

### 启动 vLLM 服务器[#](#start-the-vllm-server)

运行以下命令启动 vLLM 服务器：

```
!HIP_VISIBLE_DEVICES=2 python3 -m vllm.entrypoints.openai.api_server \
--model meta-llama/Meta-Llama-3.1-8B-Instruct
```

```

成功连接后，显示 `INFO: Uvicorn running on socket ('0.0.0.0', XX) (Press CTRL+C to quit)`

。

**注意**：在多GPU环境中，设置 `HIP_VISIBLE_DEVICES=x`

建议将LLM部署在您首选的GPU上。

### 启动客户端[#](#start-the-client)

成功运行服务器后，如上所述，打开一个新笔记本，并按下文所示向服务器发送查询。

**注意**：此步骤必须打开一个新的 Python 笔记本。创建笔记本单元格后，复制以下代码并在新笔记本中运行。可以通过选择 **文件->新建->笔记本** 来打开新笔记本。

```
import requests
url = "http://localhost:8000/v1/chat/completions"
headers = {"Content-Type": "application/json"}
data = {
"model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
"messages": [
{
"role": "system",
"content": "You are an expert in the field of AI. Make sure to provide an explanation in few sentences."
},
{
"role": "user",
"content": "Explain the concept of AI."
}
],
"stream": False,
"max_tokens": 128
}
response = requests.post(url, headers=headers, json=data)
print(response.json())
```

```

如果连接成功，输出将为：

```
{"id":"chat-xx","object":"chat.completion","created":1736494622,"model":"meta-llama/Meta-Llama-3.1-8B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"人工智能（AI）是计算机科学的一个领域..."}}]}
```

```