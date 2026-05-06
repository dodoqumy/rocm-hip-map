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



<!-- TRANSLATION_INCOMPLETE -->
# 在 AMD GPU 上进行 RL training with slime[#](#rl-training-with-slime-on-amd-gpus)

**作者**: Wei Cai

**知识水平**：中级

现代大型语言模型在预训练后并不会停止改进。为了在实际任务中有用、对齐且鲁棒，它们必须从反馈中学习。这就是强化学习（RL）发挥作用的地方。

本教程将引导您完成一个实际的生产级RL训练管线，用于[Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)大语言模型，完全在搭载ROCm（ROCm（Radeon 开放计算平台））的AMD GPU上运行。该工作流程由[slime](https://github.com/THUDM/slime)提供支持，这是一个基于SGLang的原生后训练框架，专为LLM规模的RL扩展而构建。

## 为什么使用slime?[#](#why-use-slime)

使用RL训练LLMs面临两大关键挑战：

**展开生成成本高昂**：你需要一个快速的推理引擎来采样大量的模型响应。**策略优化负担沉重**：你需要一个高度优化的训练栈，能够跨GPU进行扩展。

[slime](https://github.com/THUDM/slime) 通过清晰分离并高效连接这两个组件，同时解决了上述两个挑战：

**SGLang**: 用于高吞吐量的rollout生成
**Megatron-LM**: 用于分布式策略训练

它们共同构成一个可扩展、模块化的强化学习系统，与现代 LLM 工作负载相契合。

## 什么是GRPO？[#](#what-is-grpo)

本教程使用GRPO（组相对策略优化），这是一种为可扩展的大语言模型训练而设计的现代强化学习算法。

传统的强化学习方法通常依赖于单一的参考基线，也称为 critic 模型，它可以是：

训练成本高

难以稳定

对奖励噪声敏感

GRPO 采用了一种不同的方法。它不是孤立地评估一个响应，而是：

对同一提示生成多个响应样本

将它们分组

计算组内的相对优势

### 为什么这对 LLM 很重要[#](#why-this-matters-for-llms)

GRPO offers several practical advantages:

无需单独的价值网络

更稳定的训练信号

对大批量推出具有更好的扩展性能

自然适合基于服务器的滚动生成（SGLang）

这使得GRPO特别适用于：

指令微调

推理改进

基于偏好的优化

多GPU系统上的大规模RL

## 在本笔记本中你将学到什么[#](#what-you-ll-learn-in-this-notebook)

完成本教程后，您将能够：

为 AMD GPU 上的 slime 设置一个启用 ROCm（ROCm（Radeon 开放计算平台））的 Docker 环境。

配置GRPO针对Qwen3-4B，包括rollout和reward设置

运行一个端到端的强化学习训练循环，结合：

SGLang 生成

Megatron-LM 用于优化

理解可扩展的LLM RL训练背后的系统级设计选择

无论你是在进行训练后研究的实验，还是在构建生产级RL管道，本笔记本旨在为你提供可行的代码和清晰的思维模型。让我们开始吧。

## 先决条件[#](#prerequisites)

本教程使用以下设置进行开发和测试。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**: 确保你的系统运行的是 Ubuntu 22.04。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPUs**：本教程已在包含八个 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 的完整节点上进行了测试。请确保您使用的是支持 ROCm（ROCm（Radeon 开放计算平台））的 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 或兼容硬件，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 7.0.0**：按照 [ROCm（ROCm（Radeon 开放计算平台）） 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm（ROCm（Radeon 开放计算平台））。安装后，使用以下命令确认您的设置：此命令列出您 AMD GPU 的相关详细信息。

**Docker**：请确保 Docker 已正确安装并配置。根据您的操作系统参考 Docker 安装指南。  
**注意**：确保 Docker 权限配置正确。要允许非 root 用户访问，请执行以下命令：  
`usermod -aG docker $USER`  
`newgrp docker`

验证 Docker 是否正常工作：

运行 hello-world

## 系统验证[#](#system-validation)

在运行AI工作负载之前，确保您的AMD硬件配置正确且性能最佳非常重要。

通常，禁用NUMA（Non-Uniform Memory Access）自动平衡可以提升应用程序性能。然而，对于某些类型的工作负载，此设置可能对性能不利。

运行此命令以验证当前 NUMA 设置：

```
/proc/sys/kernel/numa_balancing

```

输出为 `0`

表示 NUMA 自动平衡已被禁用。如果没有输出或输出为 `1`

，运行以下命令以禁用NUMA自动平衡。

```
sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
```

```

更多信息，请参见 [禁用 NUMA 自动平衡](https://instinct.docs.amd.com/projects/amdgpu（amdgpu（AMD GPU 内核驱动））-docs/en/latest/system-optimization/mi300x.html#disable-numa-auto-balancing)。

## 设置环境[#](#set-up-the-environment)

按照以下步骤准备训练环境。

### 1. 拉取 Docker 镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的Docker镜像：

pull rlsys/slime:latest

```

### 2. 启动Docker容器[#](#launch-the-docker-container)

启动 Docker 容器并映射必要的目录。

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

**注意**: 如果您需要返回到 `slime`

退出容器后，使用以下命令：

```
start slime
docker exec -it slime bash
```

```

**注意**：请确保笔记本文件已复制到 `/workspace`

在Jupyter Notebook环境启动后，将文件放置在目录中或上传至该环境。请保存终端输出中提供的令牌或URL，以便从Web浏览器访问该notebook。您可以从[AI开发者中心GitHub仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev)下载此notebook。

### 3. 安装并启动 Jupyter[#](#install-and-launch-jupyter)

在Docker容器内，使用以下命令安装Jupyter：

安装 jupyter

```

启动 Jupyter 服务器：

--ip=0.0.0.0 --port=8888 --no-browser --allow-root

```

**注意**：确保端口 `8888`

在运行上述命令之前，确认该端口在您的系统上尚未被使用。如果已被占用，您可以通过替换 `--port=8888` 来指定其他端口。

使用另一个端口号，例如 `--port=8890`

### 4. 安装所需的库[#](#install-the-required-libraries)

在开始RL训练之前，你需要先安装 slime —— 这个核心框架用于连接基于SGLang的rollout生成与基于Megatron-LM的策略优化。

由于 slime 处于积极开发中，持续的提交可能会引入行为变更，影响 rollout 语义、奖励计算或训练稳定性。为确保本教程的可复现性和稳定性，请将安装固定到已知可正常工作的提交。

在ROCm（ROCm（Radeon 开放计算平台））启用的Docker容器中运行以下命令：

```
!git clone https://github.com/THUDM/slime.git
%cd slime
# 注意：你可以运行最新的上游版本。如果你想要稳定版本，请切换到以下commit ID
!git checkout 0934a0e
# 安装包
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

出现在输出中，则说明您的环境已准备好进行下一步。

## 运行 GRPO 训练[#](#run-grpo-training)

本节将引导您完成设置并运行 Qwen3-4B 的 Group Relative Policy Optimization (GRPO) 训练的端到端流程。

在高层次上，GRPO训练需要：

一个基础预训练模型（你想改进的策略）

用于生成rollout和计算奖励的训练数据集

一个保留的评估数据集，用于在训练过程中跟踪泛化性能。

### 1. 下载模型和数据集[#](#download-the-model-and-datasets)

首先，下载基础 Qwen3-4B 模型，它作为强化学习微调的初始策略。

对于训练，你将使用 `dapo-math-17k`

, 一个旨在评估逐步数学推理的数据集。这是一个尤其适合对多个模型输出进行相对比较的任务。

在评估时，使用 `aime-2024`

, 它提供了一个干净的基准，用于监控推理性能而不会泄露训练数据。

运行以下命令下载所有必需的工件。首先，从 Hugging Face 下载基础 Qwen3-4B 模型检查点：

!hf download Qwen/Qwen3-4B --local-dir /root/Qwen3-4B

```

接下来，下载训练数据集 (`dapo-math-17k`)

用于数学推理任务：

```
!hf download --repo-type dataset zhuzilin/dapo-math-17k \
--local-dir /root/dapo-math-17k
```

```

然后下载AIME 2024评估数据集以进行基准测试：

```
!hf download --repo-type dataset zhuzilin/aime-2024 \
--local-dir /root/aime-2024
```

```

### 2. 转换检查点格式[#](#convert-the-checkpoint-format)

在开始GRPO训练之前，将预训练的Hugging Face检查点转换为Megatron Core分布式格式。

这种转换是必要的，因为slime使用Megatron-LM进行训练。Megatron-LM期望模型权重根据目标并行化策略（即张量并行和流水线并行）进行布局。相比之下，Hugging Face检查点以框架无关的单进程格式存储权重。

这是一个针对给定模型和并行配置的一次性预处理步骤。只要并行设置保持不变，你无需在每个训练运行中重复此步骤。

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

### 3. 启动GRPO训练[#](#launch-grpo-training)

此步骤准备并启动GRPO训练运行时。

由于 slime 训练脚本设计为在独立环境中运行，它们可能包含保护措施（例如 `pkill -9 python`）

) 在 Jupyter notebook 中运行时是不安全的。此外，某些卸载行为 (offloading behaviors) 可能会在 AMD GPU 交互式环境中导致不稳定性。

为确保基于Jupyter的工作流稳定，下一个单元格执行以下操作：

防止训练脚本终止 Jupyter kernel。

需要插入

`--no-offload`

训练和 rollout 的标志。减少 rollout 次数，以便更容易观察到早期的性能改进。

**注意**：你可以调整 `--num-rollout`

基于您的数据集大小和训练目标。`--num-rollout` 的值越大，

导致每次迭代产生更多的rollouts，实际上增加了训练轮数并改进了收敛，但代价是更长的运行时间。

运行以下命令作为一次性设置任务以修补训练脚本。

```
%%bash
# 导航到 slime 仓库
cd /workspace/notebooks/slime
SCRIPT=scripts/run-qwen3-4B-amd.sh
echo "正在打补丁到 $SCRIPT ..."
# 1. 仅在尚未注释的情况下注释掉 `pkill -9 python`
if grep -qE '^[[:space:]]*pkill -9 python' "$SCRIPT"; then
echo " - 正在注释掉 pkill -9 python"
sed -i 's/^[[:space:]]*pkill -9 python/# pkill -9 python/' "$SCRIPT"
else
echo " - pkill 已注释或不存在"
fi
# 2. 仅在尚未存在的情况下注入 no-offload 标志
if ! grep -q -- '--no-offload-train' "$SCRIPT"; then
echo " - 正在在 --colocate 后注入 --no-offload 标志"
sed -i '/--colocate/a \ --no-offload-train \\\n --no-offload-rollout \\' "$SCRIPT"
else
echo " - no-offload 标志已存在"
fi
sed -i 's/--num-rollout[[:space:]]\+[0-9]\+/--num-rollout 200/' "$SCRIPT"
echo "补丁完成。"
```

```

脚本修补后，启动GRPO训练循环：

```bash
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

该 `run-qwen3-4B-amd.sh`

脚本包含GRPO训练的所有配置。它被组织成多个参数组，用于控制训练流程的不同方面。

以下是脚本关键组件的分解说明。每个部分对应训练工作流的特定方面。

#### 模型配置[#](#model-configuration)

```
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
source "${SCRIPT_DIR}/models/qwen3-4B.sh"
```

```

这从`scripts/models/qwen3-4B.sh`加载模型架构设置。

这些是定义模型结构的Megatron-LM参数。

**重要**: 确保诸如 `--rotary-base` 之类的设置

匹配你的目标模型。不同的模型可能使用不同的rotary base值。如有必要，在加载配置后，使用以下命令覆盖此设置：

```
source "${SCRIPT_DIR}/models/qwen3-4B.sh"
MODEL_ARGS+=( --rotary-base 10000 )
```

```

#### 检查点配置[#](#checkpoint-configuration)

```
CKPT_ARGS=(
# SGLang 所需的 HF 检查点；也用于分词器
--hf-checkpoint ${MODEL_DIR}/Qwen3-4B
# 参考模型检查点
--ref-load ${MODEL_DIR}/Qwen3-4B_torch_dist
# 演员模型加载目录；如果为空，则从 ref_load 加载
--load ${MODEL_DIR}/Qwen3-4B_slime/
--save ${MODEL_DIR}/Qwen3-4B_slime/
--save-interval 20
)
```

```

这控制了训练期间模型的加载和保存位置。

#### 推出配置[#](#rollout-configuration)

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

**关键参数**

`--num-rollout`

训练的总 rollouts 数量 `--n-samples-per-prompt`

每个提示采样的响应 (用于GRPO中的组相对优势)`--rm-type`

: 奖励模型类型（slime支持多种类型以及使用`--custom-rm-path`的自定义模型）

)

#### 评估配置[#](#evaluation-configuration)

评估任务继承滚动部署设置，但允许您覆盖特定参数：

```
EVAL_ARGS=(
--eval-interval 20
--eval-prompt-data aime ${DATA_DIR}/aime-2024/aime-2024.jsonl
--n-samples-per-eval-prompt 16
--eval-max-response-len 16384
--eval-top-p 0.7
)

```

#### 性能与并行性[#](#performance-and-parallelism)

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
)```

```

关键优化

`--use-dynamic-batch-size`

: 将变长样本打包成不超过token限制的微批次（micro batches），对应`--max-tokens-per-gpu`

每个 GPU 的硬性 token 限制

**注意**： slime 保证即使在动态打包的情况下也能进行严格的逐 token 损失计算。

#### GRPO算法参数[#](#grpo-algorithm-parameters)

```
GRPO_ARGS=(
# 优势估计器
--advantage-estimator grpo
# 使用KL散度损失
--use-kl-loss
# KL散度损失系数
--kl-loss-coef 0.00
# KL散度损失类型
--kl-loss-type low_var_kl
# 熵系数
--entropy-coef 0.00
# 裁剪阈值
--eps-clip 0.2
# 高裁剪阈值
--eps-clip-high 0.28
)

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
--rollout-num-gpus-per-engine 2 # SGLang 张量并行
--sglang-mem-fraction-static 0.7
)
```

```

以 `--sglang-` 为前缀的参数

被直接转发到SGLang引擎。

### 5. 将Megatron格式转换为Hugging Face格式以进行训练后推理[#](#convert-from-megatron-format-to-hugging-face-format-for-post-training-inference)

经过使用slime进行强化学习（RL）训练后，模型检查点以Megatron-LM分布式格式保存，该格式无法直接用于标准推理框架。为了使用Hugging Face Transformers或SGLang进行推理，必须将这些检查点转换回Hugging Face（HF）格式。

要将训练好的Megatron checkpoint（来自特定训练迭代）转换回Hugging Face格式，请使用以下命令：

```
%%bash
# 导航到 slime 仓库
cd /workspace/notebooks/slime
# 加载模型配置参数
source scripts/models/qwen3-4B.sh
# 定位 megatron-core 安装路径
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

转换后，`/root/Qwen3-4B_slime_hf_iter_0000199` 中的数据

采用标准 Hugging Face 格式，可直接用于 [transformers inference](https://huggingface.co/Qwen/Qwen3-4B)、[SGLang serving](https://docs.sglang.io/basic_usage/send_request.html) 以及进一步的评估或微调。

## 摘要[#](#summary)

恭喜！通过完成这个使用 slime 的 GRPO 训练教程，您学会了如何利用 AMD GPU 通过强化学习训练大型语言模型。

以下是关键要点：

**环境设置**: 基于ROCm（Radeon开放计算平台）的Docker容器结合slime提供了完整的RL训练环境。  
**检查点管理**: 在Hugging Face和Megatron格式之间进行转换，实现了跨框架的无缝集成。  
**GRPO训练**: 组相对优势（Group-relative advantages）提供了稳定的RL训练，无需单独的值网络。  
**可扩展架构**: SGLang rollout生成和Megatron-LM策略优化高效协同工作。

## 下一步[#](#next-steps)

**尝试不同数据集**：将GRPO应用于其他推理或指令遵循数据集。  
**调整超参数**：根据具体用例调整学习率、KL系数或采样策略。  
**扩展到更大模型**：对更大的Qwen模型或其他LLM架构使用相同的工作流。  
**评估训练模型**：在下游任务上测试微调后的模型以衡量改进。