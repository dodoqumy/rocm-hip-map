---
title: "RL training with slime on AMD GPUs &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/slime_qwen3_4B_GRPO.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:39.577375+00:00
content_hash: "079e98073d1e66dc"
---

# 在AMD GPU上使用slime进行强化学习训练[#](#rl-training-with-slime-on-amd-gpus)

**作者**：Wei Cai

**知识水平**: 中级

现代大型语言模型在预训练后并不会停止改进。为了在实际任务中有用、对齐且鲁棒，它们必须从反馈中学习。这就是强化学习（RL）发挥作用的地方。

本教程将带你完整实现一个真实、生产级风格的强化学习训练流程，针对 [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) 大型语言模型，完全运行在配备 ROCm（ROCm（Radeon 开放计算平台））的 AMD GPU 上。整个工作流由 [slime](https://github.com/THUDM/slime) 驱动——这是一个基于 SGLang 的原生后训练框架，专为大规模 LLM 的 RL 扩展而设计。

## 为什么使用 slime？[#](#why-use-slime)

使用RL训练LLMs具有挑战性，主要有两个关键原因：

**Rollout生成成本高昂**：你需要一个快速的推理引擎来采样大量模型响应。**策略优化负担沉重**：你需要一个高度优化的训练栈，能够在多个GPU上扩展。

[slime](https://github.com/THUDM/slime) 通过清晰分离并高效连接这两个组件，解决了这两个挑战：

**SGLang**: 用于高吞吐量的展开生成
**Megatron-LM**: 用于分布式策略训练

它们共同构成一个可扩展、模块化的强化学习系统，适配现代LLM工作负载。

## 什么是 GRPO？[#](#what-is-grpo)

本教程使用GRPO（Group Relative Policy Optimization），这是一种专为可扩展的大型语言模型训练而设计的现代强化学习算法。

传统的RL方法通常依赖单一的参考基线，也称为评论家模型，它可以是：

训练成本高

难以稳定

对奖励噪音敏感

GRPO 采用了一种不同的方法。它不是孤立地评估一个响应，而是：

为同一提示采样多个响应

将它们分组在一起

计算组内的相对优势

### 这对LLMs的重要性[#](#why-this-matters-for-llms)

GRPO提供了几个实际优势：

无需单独的价值网络

更稳定的训练信号

大规模批处理推演时的更好扩展行为

自然适合基于服务器的部署生成（SGLang）

这使得GRPO特别适用于：

指令微调

推理改进

基于偏好的优化

多GPU系统上的大规模强化学习

## 您将在本笔记本中学到的内容[#](#what-you-ll-learn-in-this-notebook)

学完本教程后，您将能够：

在 AMD GPU 上为 slime 设置启用 ROCm（ROCm（Radeon 开放计算平台））的 Docker 环境。

为 Qwen3-4B 配置 GRPO，包括 rollout 和 reward 设置。

运行一个端到端RL训练循环，结合：

SGLang 用于生成

Megatron-LM 用于优化

了解可扩展LLM RL训练背后的系统级设计选择

无论您是在进行训练后研究实验，还是构建生产级的强化学习管道，本笔记本旨在为您提供可运行的代码和清晰的思维模型。让我们开始吧。

## 前提条件[#](#prerequisites)

本教程使用以下配置进行开发和测试。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**：确保你的系统运行的是 Ubuntu 22.04。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPUs**: 本教程已在由八块 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 组成的完整节点上测试。请确保你使用的 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 或兼容硬件支持 ROCm（ROCm（Radeon 开放计算平台）），并且系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon开放计算平台）） 7.0.0**：请按照[ROCm安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html)安装并验证ROCm。安装完成后，使用以下命令确认配置：  
该命令会列出你的AMD GPU及详细信息。

**Docker**: 确保Docker已正确安装并配置。请遵循适用于您操作系统的Docker安装指南。**注意**: 确保Docker权限已正确配置。要配置权限以允许非root用户访问，请运行以下命令：usermod -aG docker $USER newgrp docker

验证Docker是否正确工作：

运行 hello-world

## 系统验证[#](#system-validation)

在运行AI工作负载之前，确保你的AMD硬件已正确配置并达到性能最优至关重要。

通常，禁用NUMA（Non-Uniform Memory Access）自动平衡可以提升应用程序性能。然而，对于某些类型的工作负载，此设置可能对性能不利。

运行此命令以验证当前的NUMA设置：

/proc/sys/kernel/numa_balancing

```

输出为`0`

表示NUMA自动平衡已禁用。如果没有输出或输出为`1`

运行以下命令来禁用NUMA自动平衡。

```
sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
```

```

有关更多信息，请参阅 [Disable NUMA auto-balancing](https://instinct.docs.amd.com/projects/amdgpu（amdgpu（AMD GPU 内核驱动））-docs/en/latest/system-optimization/mi300x.html#disable-numa-auto-balancing).

## 设置环境[#](#set-up-the-environment)

按照以下步骤准备训练环境。

### 1. 拉取 Docker 镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的Docker镜像：

```
pull rlsys/slime:latest
```

```

### 2. 启动 Docker 容器[#](#launch-the-docker-container)

启动Docker容器并映射必要的目录。

```
run -it \
--device /dev/dri \
--device /dev/kfd \
-p 8265:8265 \
--group-add video \
--network host --ipc host \
--cap-add SYS_PTRACE \
--security-opt seccomp=unconfined \
--privileged \
-v $HOME/.ssh:/root/.ssh \
-v $HOME:$HOME \
-w /workspace/notebooks \
--shm-size 128G \
--name slime \
--ulimit memlock=-1 \
--ulimit stack=67108864 \
rlsys/slime:latest \
/bin/bash
```

```

**注意**：如果需要返回`slime`

在退出容器后，使用这些命令：

```
start slime
docker exec -it slime bash
```

```

**注意**：确保笔记本文件已复制到 `/workspace`

目录或启动后上传到 Jupyter Notebook 环境中。保存终端输出中提供的 token 或 URL，以便从 Web 浏览器访问 notebook。您可以从 [AI Developer Hub GitHub 仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev) 下载此 notebook。

### 3. 安装并启动 Jupyter[#](#install-and-launch-jupyter)

在Docker容器内，使用以下命令安装Jupyter：

```
install jupyter
```

```

启动 Jupyter 服务器：

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

**注意**：确保端口 `8888`

在运行上述命令之前，请确保该端口在你的系统中尚未被占用。如果已被占用，你可以通过替换`--port=8888`来指定其他端口。

使用另一个端口号，例如`--port=8890`

您是专攻 GPU/ROCm/HIP 文档的技术翻译。将以下英文文本翻译为简体中文 (zh-CN)。规则：
1. 保留所有 markdown 格式、代码块、内联代码和链接不变。
2. 保留技术术语如 ROCm、HIP、GPU、CUDA、AMD、PyTorch、TensorFlow 的原始英文形式。
3. 保留 API 名称、函数名、文件路径、命令不变。
4. 仅输出翻译 — 不要有任何解释、注释或前言。
5. 使用 GPU 开发者所期望的技术中文。

### 4. 安装所需的库[#](#install-the-required-libraries)

在开始强化学习训练之前，你需要安装 slime —— 这是连接基于 SGLang 的 rollout 生成与基于 Megatron-LM 的策略优化的核心框架。

由于 slime 仍在积极开发中，持续提交的代码可能会引入行为变化，影响部署语义、奖励计算或训练稳定性。为确保本教程的可复现性和稳定性，请将安装固定到一个已知可运行的提交版本。

在启用了ROCm（ROCm（Radeon 开放计算平台））的 Docker 容器内运行以下命令：

```
!git clone https://github.com/THUDM/slime.git
%cd slime
# 注意 – 您可以运行最新的上游版本。如果您想要稳定版本，请切换到以下提交ID
!git checkout 0934a0e
# 安装该包
!pip install -e .
```

```

在继续之前，确认 slime 已正确安装并且对 Python 可见：

```
# 验证所需库的安装和版本
!pip list | grep slime
```

```

如果 `slime`

出现在输出中，您的环境已准备好进行下一步。

## 运行GRPO训练[#](#run-grpo-training)

本节将引导您完成设置并运行 Qwen3-4B 的分组相对策略优化（GRPO）训练的端到端流程。

在高层次上，GRPO训练需要：

基础预训练模型（你想要改进的策略）

用于生成展开并计算奖励的训练数据集

一个保留的评估数据集，用于在训练过程中跟踪泛化能力

### 1. 下载模型和数据集[#](#download-the-model-and-datasets)

首先，下载基础 Qwen3-4B 模型，它作为强化学习微调的初始策略。

在训练时，你将使用 `dapo-math-17k`。

，一个旨在评估逐步数学推理的数据集。这是一个对多个模型输出进行相对比较尤为有效的任务。

对于评估，使用 `aime-2024`

, 这提供了一个干净的基准，用于监控推理性能而不泄露训练数据。

运行以下命令以下载所有必需的构件。首先，从 Hugging Face 下载基础的 Qwen3-4B 模型检查点：

```
!hf download Qwen/Qwen3-4B --local-dir /root/Qwen3-4B
```

```

接下来，下载训练数据集 (`dapo-math-17k`

) 用于数学推理任务：

```
!hf download --repo-type dataset zhuzilin/dapo-math-17k \
--local-dir /root/dapo-math-17k
```

```

然后下载用于基准测试的 AIME 2024 评估数据集：

```
!hf download --repo-type dataset zhuzilin/aime-2024 \
--local-dir /root/aime-2024
```

```

### 2. 转换检查点格式[#](#convert-the-checkpoint-format)

在开始GRPO训练之前，将预训练的Hugging Face检查点转换为Megatron Core分布式格式。

这种转换是必要的，因为slime使用Megatron-LM进行训练。Megatron-LM期望模型权重按照目标并行化策略（即张量并行和流水线并行）进行布局。相比之下，Hugging Face检查点则以框架无关的单进程格式存储权重。

这是针对给定模型和并行配置的一次性预处理步骤。只要并行设置保持不变，就不需要在每次训练运行时重复执行。

运行以下命令以执行转换：

```bash
%%bash
# 导航到slime仓库
cd /workspace/notebooks/slime
# 加载模型配置参数
source scripts/models/qwen3-4B.sh
# 定位megatron核心安装路径
MEGATRON_LM_PATH=$(pip list | grep megatron-core | awk '{print $NF}')
# 运行转换工具
PYTHONPATH=${MEGATRON_LM_PATH} python tools/convert_hf_to_torch_dist.py \
${MODEL_ARGS[@]} \
--no-gradient-accumulation-fusion \
--hf-checkpoint /root/Qwen3-4B \
--save /root/Qwen3-4B_torch_dist
```

```

### 3. 启动 GRPO training[#](#launch-grpo-training)

此步骤准备并启动GRPO训练运行时。

由于 slime 训练脚本设计为在独立环境中运行，因此可能包含防护措施（例如 `pkill -9 python`

) 这些操作在 Jupyter notebook 中运行时不安全。此外，某些卸载行为会在交互式环境中导致 AMD GPU 的不稳定。

为确保基于Jupyter的工作流的稳定性，下一个单元将执行以下操作：

防止训练脚本终止Jupyter内核。

所需插入

`--no-offload`

训练和部署的标记。减少部署次数，以便更容易观察早期的性能改进。

**注意**：你可以调整 `--num-rollout`

根据您的数据集大小和训练目标。较大的 `--num-rollout` 值

导致每次迭代获得更多的rollouts，实际增加了训练轮次并提升了收敛性，代价是更长的运行时间。

运行以下命令作为一次性设置任务来修补训练脚本。

```bash
%%bash
# 导航到 slime 仓库
cd /workspace/notebooks/slime
SCRIPT=scripts/run-qwen3-4B-amd.sh
echo "正在修补 $SCRIPT ..."
# 1. 仅在未注释时注释掉 `pkill -9 python`
if grep -qE '^[[:space:]]*pkill -9 python' "$SCRIPT"; then
echo " - 注释掉 pkill -9 python"
sed -i 's/^[[:space:]]*pkill -9 python/# pkill -9 python/' "$SCRIPT"
else
echo " - pkill 已被注释或不存在"
fi
# 2. 仅在未注入时注入 no-offload 标志
if ! grep -q -- '--no-offload-train' "$SCRIPT"; then
echo " - 在 --colocate 后注入 --no-offload 标志"
sed -i '/--colocate/a \ --no-offload-train \\\n --no-offload-rollout \\' "$SCRIPT"
else
echo " - no-offload 标志已存在"
fi
sed -i 's/--num-rollout[[:space:]]\+[0-9]\+/--num-rollout 200/' "$SCRIPT"
echo "修补完成。"
```

```

在脚本修补完成后，启动GRPO训练循环：

```
%%bash
# 导航到 slime 仓库
cd /workspace/notebooks/slime
# 使用设置的环境变量启动训练脚本
SLIME_DIR=/root \
MODEL_DIR=/root \
DATA_DIR=/root \
bash scripts/run-qwen3-4B-amd.sh
```

```

### 4. 理解训练脚本[#](#understanding-the-training-script)

这个 `run-qwen3-4B-amd.sh`

该脚本包含GRPO训练的所有配置。它被组织成多个参数组，用于控制训练管线的不同方面。

以下是脚本关键组件的分解。每个部分对应训练工作流的特定方面。

#### 模型配置[#](#model-configuration)

```
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
source "${SCRIPT_DIR}/models/qwen3-4B.sh"
```

```

这从 `scripts/models/qwen3-4B.sh` 加载模型架构设置。

这些是定义模型结构的 Megatron-LM 参数。

**重要**：确保诸如 `--rotary-base` 等设置

与您的目标模型匹配。不同的模型可能使用不同的rotary base值。如有必要，在引用配置后使用以下命令覆盖此设置：

```
source "${SCRIPT_DIR}/models/qwen3-4B.sh"
MODEL_ARGS+=( --rotary-base 10000 )
```

```

#### 检查点配置[#](#checkpoint-configuration)

```
CKPT_ARGS=(
# SGLang所需的HF检查点；也用于分词器
--hf-checkpoint ${MODEL_DIR}/Qwen3-4B
# 参考模型检查点
--ref-load ${MODEL_DIR}/Qwen3-4B_torch_dist
# Actor模型加载目录；如果为空，则从ref_load加载
--load ${MODEL_DIR}/Qwen3-4B_slime/
--save ${MODEL_DIR}/Qwen3-4B_slime/
--save-interval 20
)
```

```

这控制训练期间模型加载和保存的位置。

#### 发布配置[#](#rollout-configuration)

```
ROLLOUT_ARGS=(
# 数据集配置
--prompt-data ${DATA_DIR}/dapo-math-17k/dapo-math-17k.jsonl
--input-key prompt
--label-key label
--apply-chat-template
--rollout-shuffle
# 奖励模型
--rm-type deepscaler
# 展开参数
--num-rollout 200
--rollout-batch-size 32
--n-samples-per-prompt 8
--rollout-max-response-len 8192
--rollout-temperature 0.8
# 训练批次配置
--global-batch-size 256
--balance-data
)
```

```

**关键参数**：

`--num-rollout`

训练的总 rollout 数量 `--n-samples-per-prompt`

:：每个提示采样的响应数量（用于GRPO中的组相对优势）`--rm-type`

奖励模型类型（slime支持多种类型和自定义模型，使用`--custom-rm-path`）

)

#### 评估配置[#](#evaluation-configuration)

评估任务继承rollout设置，但允许你覆盖特定参数：

```
EVAL_ARGS=(
--eval-interval 20
--eval-prompt-data aime ${DATA_DIR}/aime-2024/aime-2024.jsonl
--n-samples-per-eval-prompt 16
--eval-max-response-len 16384
--eval-top-p 0.7
)
```

```

#### 性能和并行性[#](#performance-and-parallelism)

```
PERF_ARGS=(
--tensor-model-parallel-size 2
--sequence-parallel
--pipeline-model-parallel-size 1
--context-parallel-size 1
--recompute-granularity full
--recompute-method uniform
--recompute-num-layers 1
--use-dynamic-batch-size
--max-tokens-per-gpu 9216
)
```

```

关键优化

`--use-dynamic-batch-size`

将不同长度的样本打包成微批次，直至达到 token 限制 `--max-tokens-per-gpu`

每个GPU的令牌硬限制

**注意**：slime 保证即使在动态打包的情况下也能进行严格的每令牌损失计算。

#### GRPO算法参数[#](#grpo-algorithm-parameters)

```
GRPO_ARGS=(
--advantage-estimator grpo
--use-kl-loss
--kl-loss-coef 0.00
--kl-loss-type low_var_kl
--entropy-coef 0.00
--eps-clip 0.2
--eps-clip-high 0.28
)
```

```

#### 优化器配置[#](#optimizer-configuration)

```
OPTIMIZER_ARGS=(
--optimizer adam
--lr 1e-6
--lr-decay-style constant
--weight-decay 0.1
--adam-beta1 0.9
--adam-beta2 0.98
)
```

```

#### SGLang 配置[#](#sglang-configuration)

```
SGLANG_ARGS=(
--rollout-num-gpus-per-engine 2 # SGLang张量并行
--sglang-mem-fraction-static 0.7
)
```

```

以 `--sglang-` 为前缀的参数

被直接转发到 SGLang 引擎。

### 5. 从 Megatron 格式转换为 Hugging Face 格式以进行训练后推理[#](#convert-from-megatron-format-to-hugging-face-format-for-post-training-inference)

使用 slime 进行强化学习训练后，模型检查点以 Megatron-LM 分布式格式保存，该格式无法直接用于标准推理框架。若要通过 Hugging Face Transformers 或 SGLang 运行推理，必须将这些检查点转换回 Hugging Face (HF) 格式。

要将训练好的 Megatron checkpoint（来自特定训练迭代）转换回 Hugging Face 格式，请使用以下命令：

```
%%bash
# Navigate to the slime repository
cd /workspace/notebooks/slime
# Load model configuration arguments
source scripts/models/qwen3-4B.sh
# Locate megatron-core installation path
MEGATRON_LM_PATH=$(pip list | grep megatron-core | awk '{print $NF}')
PYTHONPATH=${MEGATRON_LM_PATH} python tools/convert_hf_to_torch_dist.py \
${MODEL_ARGS[@]} \
--no-gradient-accumulation-fusion \
--hf-checkpoint /root/Qwen3-4B \
--save /root/Qwen3-4B_torch_dist
PYTHONPATH=${MEGATRON_LM_PATH} python tools/convert_torch_dist_to_hf.py \
--input-dir /root/Qwen3-4B_slime/iter_0000199 \
--output-dir /root/Qwen3-4B_slime_hf-iter_0000199 \
--origin-hf-dir /root/Qwen3-4B
```

```

转换后，`/root/Qwen3-4B_slime_hf_iter_0000199` 中的数据。

采用标准的Hugging Face格式，可用于[transformers推理](https://huggingface.co/Qwen/Qwen3-4B)、[SGLang服务](https://docs.sglang.io/basic_usage/send_request.html)以及进一步的评估或微调。

## 摘要[#](#summary)

祝贺！通过完成这个使用slime的GRPO训练教程，你学会了如何在AMD GPU上使用强化学习训练大型语言模型。

以下是关键要点：

**环境设置**：支持ROCm（ROCm（Radeon 开放计算平台））的Docker容器与slime提供了完整的RL训练环境。**检查点管理**：在Hugging Face和Megatron格式之间转换可实现跨框架的无缝集成。**GRPO训练**：组相对优势提供了稳定的RL训练，无需单独的value network。**可扩展架构**：SGLang rollout生成和Megatron-LM策略优化高效协同工作。

## 下一步[#](#next-steps)

**尝试不同的数据集**：将 GRPO 应用于其他推理或指令遵循数据集。**调整超参数**：根据具体使用场景调整学习率、KL 系数或采样策略。**扩展到更大模型**：使用相同工作流处理更大的 Qwen 模型或其他 LLM 架构。**评估训练后的模型**：在下游任务上测试微调后的模型以衡量改进效果。