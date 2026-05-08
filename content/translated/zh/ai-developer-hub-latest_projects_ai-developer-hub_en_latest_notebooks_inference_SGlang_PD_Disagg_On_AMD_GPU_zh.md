---
title: "LLM distributed inference and PD disaggregation on AMD Instinct GPUs &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/SGlang_PD_Disagg_On_AMD_GPU.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T18:59:45.059674+00:00
content_hash: "9dcd0a1f1c981230"
---

# AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 上的 LLM 分布式推理与 PD 分离[#](#llm-distributed-inference-and-pd-disaggregation-on-amd-instinct-gpus)

**作者**：Ning Zhang

**知识水平**：中级

随着大语言模型（LLM）规模的快速增长，单节点推理优化在 LLM 服务扩展方面开始显现其局限性。多节点分布式推理对于高效的 LLM 服务变得更为重要。预填充和解码（PD）分离是 GPU 节点上进行 LLM 分布式推理的典型用例。LLM 推理包含两个不同阶段：预填充阶段和解码阶段。预填充阶段计算密集，处理整个输入序列；而解码阶段内存密集，管理用于 token 生成的键值（KV）缓存。PD 分离将这两个阶段独立运行在不同的 GPU 节点上，从而实现高效的 GPU 资源分配和独立的性能调优。本教程演示如何利用 AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPU 在一个或两个节点上搭建 1P1D 分布式推理。

## 前提条件[#](#prerequisites)

本教程是使用以下环境开发和测试的。

### 操作系统[#](#operating-system)

**Ubuntu 22.04/24.04**: 确保你的系统运行的是 Ubuntu 22.04 或 24.04。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPUs**：已在 MI300X 上测试。可在单节点 MI300X 或两个 MI300X 节点（每个节点有 8 张 MI300X GPU）上运行。**RDMA NIC**（单节点和双节点场景下通过 RDMA 传输 KV 缓存所需）：使用支持 RDMA 的 NIC（例如 Broadcom Thor2/BCM‑57608 或 NVIDIA/Mellanox ConnectX）。

安装相应的供应商驱动和RDMA用户空间库（

`rdma-core/libibverbs`

使用以下命令进行验证：`ibv_devices`

和 `ibv_devinfo`

`ls /dev/infiniband`

如果在 Docker 中运行，请确保

`/dev/infiniband`

被映射到容器中（参见下面的启动命令）。对于双节点配置，两个节点上都必须具备RDMA（带PFC的RoCEv2或InfiniBand），并进行正确的线缆连接和交换机配置。

**ROCm（ROCm（Radeon 开放计算平台））兼容性**：使用支持ROCm（ROCm（Radeon 开放计算平台））的AMD Instinct（Instinct（AMD数据中心GPU系列））GPU，并确保你的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.3 或更高版本**（主机）：按照[ROCm（ROCm（Radeon 开放计算平台））安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html)安装并验证 ROCm（ROCm（Radeon 开放计算平台））。安装后，使用`amd-smi`确认您的设置。

命令。**注意**：对于 ROCm（ROCm（Radeon 开放计算平台））6.4 及更早版本，请使用 `rocm-smi`

而是使用命令。**Docker（主机）**：在 Linux 上安装 Docker Engine，并通过 `docker --version` 进行验证。

命令。您将在容器内运行本教程。确保宿主机允许您映射GPU和RDMA设备。启动容器时，映射这些设备并使用推荐的标志：

设备：

`/dev/kfd`

,`/dev/dri`

,`/dev/infiniband`

, 和`/dev/infiniband/rdma_cm`

标志:

`--network=host --ipc=host --shm-size 32G --group-add=video`

**预构建的 ROCm（ROCm（Radeon 开放计算平台）） Docker 镜像**（推荐以降低设置难度）：**Jupyter（在容器内）**：使用 `pip install jupyter` 安装

运行此笔记本。

### Hugging Face API 访问[#](#hugging-face-api-access)

从获取API令牌

使用 [Hugging Face](https://huggingface.co) 下载模型。确保 Hugging Face API token 具有必要的权限和批准以访问所需的检查点。

对于单个节点，你必须能够访问

[Meta Llama Llama-3.1-8B-Instruct checkpoints](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).对于两个节点，您必须有权访问

[Meta Llama Llama-3.3-70B-Instruct 检查点](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)。

## 设置PD分离环境[#](#set-up-the-pd-disaggregation-environment)

在本教程中，您将使用预构建的ROCm（ROCm（Radeon 开放计算平台）） SGLang镜像，该镜像将SGLang与AMD [ROCm（ROCm（Radeon 开放计算平台））](https://rocm.docs.amd.com/en/latest/index.html)软件栈集成。如果您愿意，也可以尝试其他ROCm（ROCm（Radeon 开放计算平台））镜像作为基础镜像。

### 第一步：准备教程环境[#](#step-1-prepare-the-tutorial-environment)

按照以下步骤配置您的教程环境：

#### 拉取 Docker 镜像[#](#pull-the-docker-image)

使用 `lmsysorg/sglang:v0.4.9-rocm630`

使用Docker镜像作为基础镜像。这是为本教程测试过的最新镜像。

**注意**：SGLang社区持续发布额外的ROCm（ROCm（Radeon 开放计算平台））SGLang Docker镜像。强烈建议您使用最新的可用镜像以获得更好的性能。

```
pull lmsysorg/sglang:v0.4.9-rocm630
```

```

#### 启动 Docker 容器[#](#launch-the-docker-container)

为了实现良好的网络传输性能，运行PD分解的节点需要配备RDMA网卡。在启动Docker镜像时，需要将RDMA设备映射到Docker容器中，如下命令所示。

```
run -it --rm \
--network=host \
--device=/dev/kfd \
--device=/dev/dri \
--group-add=video \
--ipc=host \
--device=/dev/infiniband \
--device=/dev/infiniband/rdma_cm \
--privileged \
--cap-add=SYS_ADMIN \
--cap-add=SYS_PTRACE \
--security-opt seccomp=unconfined \
--shm-size 32G \
-v $(pwd):/workspace \
-w /workspace \
lmsysorg/sglang:v0.4.9-rocm630
```

```

**注意**：该命令将当前目录挂载到 `/workspace`

容器中的目录。确保在运行 Docker 命令之前将笔记本文件复制到此目录，或者在 Jupyter Notebook 环境启动后将其上传到该环境。保存终端输出中提供的令牌或 URL，以便从 Web 浏览器访问该笔记本。您可以从 [AI Developer Hub GitHub 仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev) 下载此笔记本。

#### 安装并启动 Jupyter[#](#install-and-launch-jupyter)

在Docker容器内，使用以下命令安装Jupyter：

```
安装 jupyter
```

```

启动 Jupyter 服务器：

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

**注意**：请确保端口 `8888`

在运行上述命令之前，请确保该端口在您的系统上尚未被占用。如果已被占用，您可以通过替换 `--port=8888` 来指定不同的端口。

使用另一个端口号，例如，`--port=8890`

。

**注意**：本笔记本的剩余内容设计为以 Jupyter notebook 形式运行。本笔记演示了在 AMD Instinct（AMD 数据中心 GPU 系列）GPU 上的 Prefill 和 Decode（PD）分离。默认情况下，它在单个节点（节点内 1P1D）上运行。两个节点（节点间 1P1D）的步骤为可选操作，并已明确标注。

运行模式

单节点（默认）：该

[etcd](https://etcd.io/) 键值存储服务器并非必需。请使用“节点内 1P1D”部分。  
两个节点（可选）：需要搭建 etcd 服务器、RDMA 和 SSH。请使用两节点“节点间 1P1D”部分。

#### 提供你的 Hugging Face token[#](#provide-your-hugging-face-token)

您需要一个 Hugging Face API 令牌，才能根据本笔记本前面部分所述的适当权限访问 Llama 模型。首先，安装 Hugging Face Hub 库。

```
!pip install --upgrade huggingface_hub

```

在Jupyter notebook中运行以下交互代码块以设置令牌：

```
from huggingface_hub import notebook_login, HfApi
# 提示用户登录
notebook_login()
```

```

验证您的 token 是否被正确接受：

```
# 验证令牌
try:
    api = HfApi()
    user_info = api.whoami()
    print(f"令牌验证成功！已登录为：{user_info['name']}")
except Exception as e:
    print(f"令牌验证失败。错误：{e}")
```

```

### 步骤2：安装必要的软件组件[#](#step-2-install-the-necessary-software-components)

对于 Intra-node 1P1D 模式，您必须安装 Mooncake transfer engine。这种情况下不需要 etcd 服务器。对于 Inter-node 1P1D 模式，您必须同时安装 etcd 和 Mooncake transfer engine。

#### 步骤 2.1：（可选）安装 etcd[#](#step-2-1-optional-install-etcd)

如果您正在运行单节点测试，可以跳过此步骤。etcd是一个强一致性的分布式键值存储系统，能够为分布式系统或集群中的机器提供可靠的访问数据存储。在SGLang PD分离式解决方案设计中，每个GPU节点上都需要运行etcd服务器以提供集群元数据存储。要在两个节点上运行本教程，必须安装etcd。

```
%%bash
cd /sgl-workspace
apt update && apt install -y wget
wget https://github.com/etcd-io/etcd/releases/download/v3.6.0-rc.5/etcd-v3.6.0-rc.5-linux-amd64.tar.gz -O /tmp/etcd.tar.gz
tar -xvf /tmp/etcd.tar.gz -C /usr/local/bin/ --strip-components=1 && rm /tmp/etcd.tar.gz
```

```

#### 步骤 2.2：安装 Mooncake[#](#step-2-2-install-mooncake)

Mooncake 采用以 KV 缓存为核心的解耦架构，将预填充与解码集群分离。其核心组件（如传输引擎）已集成到 SGLang PD 解耦方案中，用于在节点之间传输 KV 缓存。

```
%%bash
apt update && apt install -y zip unzip openssh-server
apt -y install gcc make libtool autoconf librdmacm-dev rdmacm-utils infiniband-diags ibverbs-utils perftest ethtool libibverbs-dev rdma-core strace
cd /sgl-workspace
pip install mooncake-transfer-engine
```

```

## 运行 SGLang PD 解聚[#](#run-sglang-pd-disaggregation)

SGLang 在 AMD Instinct®（AMD 数据中心 GPU 系列）GPU 上支持预填充-解码（PD）分离，该功能使用 Mooncake 来传输 KV 缓存。从系统架构角度来看，SGLang PD 分离包含三个不同组件：代理服务器、预填充服务器和解码服务器。当请求到来时，代理服务器根据负载均衡方案选择一对预填充服务器和解码服务器。所选预填充服务器与解码服务器通过握手建立连接，分别担当本地发送端和接收端。解码服务器预分配 KV 缓存，然后通知预填充服务器开始 LLM 预填充推理并计算 KV 缓存。预填充工作完成后，KV 缓存数据传输至解码服务器，由其负责迭代式令牌生成。

本教程测试SGLang PD分离的两种配置：节点内1P1D和节点间1P1D。对于节点内场景，至少需要两块GPU：一块运行prefill服务器，另一块运行decode服务器。对于节点间1P1D，需要两个节点。一个节点运行prefill服务器，另一个节点运行decode服务器。由于proxy服务器不需要大量GPU资源，它运行在prefill节点上。如果集群规模较大，可将proxy节点运行在独立节点上以获得更佳性能。在以下演示SGLang PD分离的步骤中，示例prefill节点的IP地址为`10.21.9.10`。

并且解码节点的地址是 `10.21.9.15`

. 根据您的集群配置修改相关参数和设置。

### 节点内（单节点）1P1D[#](#intra-node-single-node-1p1d)

对于节点内测试，请遵循以下步骤：

**注意**：本节中的所有命令均需在终端中运行，而非在笔记本代码单元格中。在JupyterLab中，通过**Launcher → Terminal**（或**File → New → Terminal**）打开终端。请为 prefill、decode 和 proxy 服务器分别使用不同的终端。

#### 运行 prefill server[#](#run-the-prefill-server)

使用 `sglang.launch_server`

启动预填充服务器的命令。有关更多信息和命令选项的详细描述，请参阅最新版本的SGLang文档或源代码。RDMA设备名称可以通过使用 `ibv_devices` 找到。

(参见前面的章节)

**注意**：对于多节点配置，确保 `PATH`

和 `LD_LIBRARY_PATH`

包含 UCX 和 Open MPI（参见前面的代码单元格，或在终端中导出它们）。在运行命令之前，替换所有占位符（例如 IP 地址、端口和 RDMA 设备名称）。

```
HIP_VISIBLE_DEVICES=0 python -m sglang.launch_server --model-path meta-llama/Llama-3.1-8B-Instruct \
--disaggregation-mode prefill --port 30000 \
--disaggregation-ib-device rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7
```

```

#### 运行解码服务器[#](#run-the-decode-server)

使用 `sglang.launch_server`

启动解码服务器的命令。RDMA设备名称可以通过使用 `ibv_devices` 找到。

您是一名专注于 GPU/ROCm/HIP 文档的技术翻译。将以下英文文本翻译为简体中文（zh-CN）。规则：
1. 保留所有标记格式、代码块、行内代码和链接不变。
2. 保留技术术语如 ROCm、HIP、GPU、CUDA、AMD、PyTorch、TensorFlow 的英文原样。
3. 保留 API 名称、函数名称、文件路径、命令不变。
4. 仅输出翻译内容——不附带任何解释、注释或前言。
5. 使用 GPU 开发者所期望的技术中文。

```
HIP_VISIBLE_DEVICES=1 python -m sglang.launch_server --model-path meta-llama/Llama-3.1-8B-Instruct \
--disaggregation-mode decode --port 30001 \
--disaggregation-ib-device rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7
```

```

#### 运行代理服务器[#](#run-the-proxy-server)

这一步骤在同一个节点上启动代理服务器时，配置预填充和解码服务器端口。还提供了代理服务器端口，以便测试客户端程序可以连接。

```
-m sglang.srt.disaggregation.mini_lb --prefill http://127.0.0.1:30000 --decode http://127.0.0.1:30001 --host 0.0.0.0 --port 40000

```

### 跨节点（multi-node）1P1D[#](#inter-node-multi-node-1p1d)

对于跨节点测试，请遵循以下步骤：

**注意**：本节中的所有命令都应在终端中运行，而不是在笔记本代码单元中。在JupyterLab中，通过**启动器 → 终端**（或**文件 → 新建 → 终端**）打开一个终端。请为预填充、解码和代理服务器分别使用独立的终端。

#### 在每个节点上运行 etcd 服务器[#](#run-the-etcd-server-on-each-node)

在预填充节点和解码节点的 SGLang ROCm（ROCm（Radeon 开放计算平台））容器中运行以下命令。这些命令中的 etcd 服务器端口仅供参考。如果它们被其他进程占用，请尝试不同的端口。

在预填充节点上，使用以下命令启动etcd服务器。

```
--name infra0 --data-dir /var/lib/etcd --initial-advertise-peer-urls http://10.21.9.10:2380 \
--listen-peer-urls http://10.21.9.10:2380 \
--listen-client-urls http://10.21.9.10:2379,http://127.0.0.1:2379 \
--advertise-client-urls http://10.21.9.10:2379 \
--initial-cluster-token etcd-cluster-1 \
--initial-cluster infra0=http://10.21.9.10:2380,infra1=http://10.21.9.15:2380 \
--initial-cluster-state new
```

```

在解码节点上，使用此命令运行etcd服务器。

```
--name infra1 --data-dir /var/lib/etcd --initial-advertise-peer-urls http://10.21.9.15:2380 \
--listen-peer-urls http://10.21.9.15:2380 \
--listen-client-urls http://10.21.9.15:2379,http://127.0.0.1:2379 \
--advertise-client-urls http://10.21.9.15:2379 \
--initial-cluster-token etcd-cluster-1 \
--initial-cluster infra0=http://10.21.9.10:2380,infra1=http://10.21.9.15:2380 \
--initial-cluster-state new
```

```

#### 运行代理服务器[#](#id1)

如前所述，在本教程中，该服务器运行在 prefill 节点上。你可以在同一集群中将其运行在独立节点上以获得更佳性能。

在这一步中，prefill 和 decode 节点池的 IP 地址和端口被配置。同时还提供了代理服务器的 IP 地址和端口，供测试客户端程序连接。

```
-m sglang.srt.disaggregation.mini_lb --prefill http://10.21.9.10:30000 \
--decode http://10.21.9.15:30000 --host 0.0.0.0 --port 40000
```

```

#### 运行预填充服务器[#](#id2)

使用 `sglang.launch_server`

启动prefill服务器的命令。有关命令选项的更多信息和详细说明，请参阅最新版本的SGLang文档或源代码。可以使用 `ibv_devices` 命令查看RDMA设备名称。

（参见前文）

```
-m sglang.launch_server --model meta-llama/Llama-3.3-70B-Instruct \
--disaggregation-mode prefill --disaggregation-ib-device rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7 \
--host 10.21.9.10 --port 30000 --trust-remote-code \
--tp 8 --disable-radix-cache --disable-cuda-graph \
--max-running-requests 1024 --stream-output \
--dist-init-addr 10.21.9.10:5757 --nnodes 1 --node-rank 0 \
--mem-fraction-static 0.8
```

```

#### 运行解码服务器[#](#id3)

使用 `sglang.launch_server`

启动解码服务器的命令。RDMA设备名称可以通过使用 `ibv_devices` 找到。

。

```
-m sglang.launch_server --model meta-llama/Llama-3.3-70B-Instruct \
--disaggregation-mode decode --disaggregation-ib-device rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7 \
--host 10.21.9.15 --port 30000 --trust-remote-code \
--tp 8 --disable-radix-cache --disable-cuda-graph \
--max-running-requests 1024 --stream-output \
--dist-init-addr 10.21.9.15:5757 --nnodes 1 --node-rank 0 \
--mem-fraction-static 0.8
```

```

### 测试 PD 解聚[#](#test-pd-disaggregation)

在此步骤中，使用 `sglang.bench_serving`

以与普通SGLang基准测试相同的方式测试1P1D配置。本教程在prefill节点上运行命令以简化演示。要在集群中的另一台机器上运行命令，请在此命令中设置代理服务器的主机IP地址和端口。其他测试参数可根据需要更改。

```bash
%%bash
python3 -m sglang.bench_serving --backend sglang --host 127.0.0.1 --port 40000 --dataset-name generated-shared-prefix \
--gsp-system-prompt-len 0 \
--gsp-question-len 1024 \
--gsp-output-len 1024 \
--gsp-num-groups 1 \
--gsp-prompts-per-group 16\
--random-range-ratio 1 \
--max-concurrency 16 \
--pd-separated \
2>&1 | tee test.log
```

```

### xPyD 设置[#](#xpyd-setup)

如果您有一个更大的 GPU 集群来运行 PD 分离，可以使用 xPyD（多个预填充和解码实例）以获得更好的性能。xPyD 的设置与上述步骤相同，但需要按以下方式修改多节点相关配置：

更改代理服务器中的prefill和decode节点配置，例如：

`--prefill "http://YOUR_FIRST_PREFILL_NODE_IP:30000"`

和`--decode "http://YOUR_FIRST_DECODE_NODE_IP:30000"`

.更改多节点分布式服务选项，例如

dist-init-addr

,`nnodes`

，以及`node-rank`

, when launching the prefill and decode server.Change the

`tp`

,`dp`

, 以及 `ep-size`

SGLang serving 程序的选项（如果需要）。

## 摘要[#](#summary)

在本教程中，您学习了如何在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 上设置并运行 SGLang PD 分离。本教程演示了如何在单个 Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X 节点和两个 Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 节点上配置 1P1D，但您可以轻松地在自己的 GPU 集群上实现 xPyD。要了解更多关于 PD 分离的信息，请参阅 [Mooncake](https://kvcache-ai.github.io/Mooncake/)、[LLM-d](https://llm-d.ai/) 和 [vLLM disagg_prefill](https://docs.vllm.ai/en/stable/features/disagg_prefill.html#development) 资源。本教程旨在鼓励您在 AMD GPU 上调整、测试并贡献 LLM 分布式推理，从而助力塑造 AI 加速的未来。