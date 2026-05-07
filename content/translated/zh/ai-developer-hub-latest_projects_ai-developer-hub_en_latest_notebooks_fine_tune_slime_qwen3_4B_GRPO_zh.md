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

# 在AMD GPU上使用slime进行RL训练[#](#rl-training-with-slime-on-amd-gpus)

**作者**: Wei Cai

**知识水平**: 中级

现代大型语言模型在预训练之后并不会停止改进。为了在实际任务中变得有用、对齐且稳健，它们必须从反馈中学习。这就是强化学习（RL）发挥作用的地方。

本教程将带你了解一个真实的、生产级强化学习（RL）训练流水线，用于[Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)大型语言模型，该流水线完全在搭载ROCm（ROCm（Radeon 开放计算平台））的AMD GPU上运行。工作流程由[slime](https://github.com/THUDM/slime)驱动，这是一个SGLang原生后训练框架，专为LLM规模的RL扩展而构建。

## 为什么要使用 slime?[#](#why-use-slime)

使用强化学习训练大语言模型面临两个关键挑战：

**生成展开（Rollout）成本高昂**：需要一个快速的推理引擎来采样大量模型响应。  
**策略优化负担沉重**：需要一个高度优化的训练栈，使其能够跨GPU扩展。

[slime](https://github.com/THUDM/slime) 通过清晰分离并高效连接这两个组件，解决了这两个挑战：

**SGLang**: 用于高吞吐量的rollout生成
**Megatron-LM**: 用于分布式策略训练

它们共同构成了一个可扩展、模块化的RL系统，能够适配现代LLM工作负载。

## 什么是 GRPO？[#](#what-is-grpo)

本教程使用 GRPO（Group Relative Policy Optimization），这是一种专为可扩展的大语言模型训练而设计的现代强化学习算法。

传统的强化学习方法通常依赖于单个参考基线，也称为评论家模型，该模型可以是：

训练成本高昂

难以稳定

对奖励噪声敏感

GRPO采用了一种不同的方法。它不是孤立地评估一个响应，而是GRPO：

对同一提示采样多个响应

将它们分组在一起

计算组内的相对优势

### Why this matters for LLMs[#](#why-this-matters-for-llms)

GRPO 提供了几个实际优势：

无需单独的价值网络

更稳定的训练信号

对于大批量展开的更好的扩展行为

自然适合基于服务器的生成推出 (SGLang)

这使得GRPO特别适用于：

指令微调

推理改进

基于偏好的优化

多GPU系统上的大规模RL

## 您将在此笔记本中学到什么[#](#what-you-ll-learn-in-this-notebook)

完成本教程后，您将能够：

为 AMD GPU 上的 slime 设置一个支持 ROCm（ROCm（Radeon 开放计算平台））的 Docker 环境。

配置GRPO用于Qwen3-4B，包括rollout和reward设置

运行一个端到端的RL训练循环，结合：

SGLang 用于生成

用于优化的Megatron-LM

理解可扩展的大语言模型强化学习训练背后的系统级设计选择

无论你是在进行训练后研究实验，还是构建生产级强化学习（RL）管道，这本笔记本旨在为你提供可运行的代码和清晰的思维模型。让我们开始吧。

## 前提条件[#](#prerequisites)

本教程基于以下环境进行开发和测试。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**：确保你的系统运行的是 Ubuntu 22.04。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPUs**：本教程已在配备八块 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 的全节点上完成测试。请确保您使用的是 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 或兼容 ROCm（ROCm（Radeon 开放计算平台））的硬件，且系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 7.0.0**：按照 [ROCm（ROCm（Radeon 开放计算平台）） install guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm（ROCm（Radeon 开放计算平台））。安装后，使用以下命令确认你的配置：此命令列出你的 AMD GPU 及相关详细信息。

**Docker**：确保Docker已正确安装和配置。请按照适用于您操作系统的Docker安装指南进行操作。  
**注意**：确保Docker权限已正确配置。要配置允许非root用户访问的权限，请运行以下命令：  
`usermod -aG docker $USER`  
`newgrp docker`

验证 Docker 是否正常工作：

run hello-world

## 系统验证[#](#system-validation)

在运行 AI 工作负载之前，确保 AMD 硬件已正确配置并以最佳性能运行至关重要。

通常，禁用NUMA（非统一内存访问）自动平衡有助于提升应用程序性能。然而，对于某些类型的工作负载，此设置可能对性能产生不利影响。

运行以下命令以验证当前 NUMA 设置：

/proc/sys/kernel/numa_balancing

```

输出为 `0`

表示 NUMA 自动平衡已禁用。如果没有输出或输出为 `1`

, 运行以下命令以禁用 NUMA 自动平衡。

```
sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
```

```

更多信息，请参阅 [禁用NUMA自动平衡](https://instinct.docs.amd.com/projects/amdgpu（amdgpu（AMD GPU 内核驱动））-docs/en/latest/system-optimization/mi300x.html#disable-numa-auto-balancing)。

## 配置环境[#](#set-up-the-environment)

按照以下步骤准备训练环境。

### 1. 拉取 Docker 镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的 Docker 镜像：

```
pull rlsys/slime:latest
```

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

**Note**: 如果您需要返回到 `slime`

退出容器后，使用这些命令：

```
start slime
docker exec -it slime bash
```

```

**注意**：确保notebook文件被复制到`/workspace`

启动后，将目录或上传的文件放入Jupyter Notebook环境中。保存终端输出中提供的令牌或URL，以便从您的网络浏览器访问该笔记本。您可以从 [AI Developer Hub GitHub repository](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev) 下载此笔记本。

### 3. 安装并启动Jupyter[#](#install-and-launch-jupyter)

在Docker容器内，使用以下命令安装Jupyter：

```
安装 Jupyter
```

```

启动 Jupyter 服务器：

--ip=0.0.0.0 --port=8888 --no-browser --allow-root

```

**注意**: 确保端口 `8888`

在运行上述命令之前，请确保该端口在你的系统上尚未被使用。如果已被占用，你可以通过替换 `--port=8888` 来指定其他端口。

使用另一个端口号，例如 `--port=8890`

。

### 4. 安装所需的库[#](#install-the-required-libraries)

在开始RL训练之前，你需要安装slime——这是连接基于SGLang的轨迹生成与基于Megatron-LM的策略优化的核心框架。

由于 slime 尚在积极开发中，持续的提交可能会引入行为变化，影响发布语义、奖励计算或训练稳定性。为确保本教程的可复现性和稳定性，请将安装固定到已知可用的提交版本。

在已启用 ROCm（ROCm（Radeon 开放计算平台））的 Docker 容器内运行以下命令：

```
!git clone https://github.com/THUDM/slime.git
%cd slime
# 注意：您可以运行最新的上游版本。如果需要稳定版本，请检出以下提交ID：
!git checkout 0934a0e
# 安装该包
!pip install -e .
```

```

在继续之前，请确认slime已正确安装并且对Python可见：

```
# 验证所需库的安装和版本
!pip list | grep slime
```

```

如果 `slime`

出现在输出中，您的环境已为下一步做好准备。

## 运行GRPO训练[#](#run-grpo-training)

本节将带你逐步完成从头到尾的设置和运行 Qwen3-4B 模型分组相对策略优化（GRPO）训练的全过程。

从高层来看，GRPO训练需要：

基础预训练模型（你想要改进的策略）

一个用于生成轨迹并计算奖励的训练数据集。

用于跟踪训练过程中泛化性能的留出评估数据集

### 1. 下载模型和数据集[#](#download-the-model-and-datasets)

首先，下载基础Qwen3-4B模型，该模型作为强化学习微调的初始策略。

在训练中，你将使用 `dapo-math-17k`

，一个旨在评估逐步数学推理的数据集。这是一项通过对多个模型输出进行相对比较尤为有效的任务。

对于评估，使用 `aime-2024`

，它提供了一个干净的基准测试，用于监控推理性能，而不会泄露训练数据。

运行以下命令来下载所有必需的工件。首先，从 Hugging Face 下载基础 Qwen3-4B 模型检查点：

```
!hf download Qwen/Qwen3-4B --local-dir /root/Qwen3-4B
```

```

接下来，下载训练数据集（`dapo-math-17k`

)用于数学推理任务：

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

之所以需要进行这种转换，是因为 slime 使用 Megatron-LM 进行训练。Megatron-LM 期望模型权重按照目标并行化策略（即张量并行和流水线并行）进行布局。相比之下，Hugging Face 的检查点以框架无关的单进程格式存储权重。

这是针对特定模型和并行配置的一次性预处理步骤。只要并行设置保持不变，您无需为每次训练运行重复此步骤。

运行以下命令以执行转换：

```bash
# 导航到 slime 仓库
cd /workspace/notebooks/slime
# 加载模型配置参数
source scripts/models/qwen3-4B.sh
# 查找 megatron-core 安装路径
MEGATRON_LM_PATH=$(pip list | grep megatron-core | awk '{print $NF}')
# 运行转换工具
PYTHONPATH=${MEGATRON_LM_PATH} python tools/convert_hf_to_torch_dist.py \
${MODEL_ARGS[@]} \
--no-gradient-accumulation-fusion \
--hf-checkpoint /root/Qwen3-4B \
--save /root/Qwen3-4B_torch_dist
```

```

### 3. 启动 GRPO 训练[#](#launch-grpo-training)

此步骤准备并启动GRPO训练运行时。

由于 slime 训练脚本设计为在独立环境中运行，它们可能包含安全防护措施（例如 `pkill -9 python`）

) 在 Jupyter notebook 中运行时是不安全的。此外，某些卸载行为可能会在交互式环境中导致 AMD GPU 出现不稳定性。

为确保基于Jupyter的稳定工作流程，下一个单元格执行以下操作：

防止训练脚本终止Jupyter内核。

插入要求

`--no-offload`

针对训练和部署的标记。减少部署计数，以便更容易观察早期的性能改进。

**注意**：您可以调整 `--num-rollout`

基于你的数据集大小和训练目标。`--num-rollout` 的值越大

导致每次迭代有更多的rollouts，实际上增加了训练周期并改善了收敛性，但代价是运行时间更长。

作为一次性设置任务，运行以下命令来修补训练脚本。

```
%%bash
# 导航到 slime 仓库
cd /workspace/notebooks/slime
SCRIPT=scripts/run-qwen3-4B-amd.sh
echo "打补丁 $SCRIPT ..."
# 1. 仅当 `pkill -9 python` 尚未被注释时注释掉它
if grep -qE '^[[:space:]]*pkill -9 python' "$SCRIPT"; then
echo " - 注释掉 pkill -9 python"
sed -i 's/^[[:space:]]*pkill -9 python/# pkill -9 python/' "$SCRIPT"
else
echo " - pkill 已被注释或不存在"
fi
# 2. 仅当没有 no-offload 标志时注入它们
if ! grep -q -- '--no-offload-train' "$SCRIPT"; then
echo " - 在 --colocate 后注入 --no-offload 标志"
sed -i '/--colocate/a \ --no-offload-train \\\n --no-offload-rollout \\' "$SCRIPT"
else
echo " - no-offload 标志已存在"
fi
sed -i 's/--num-rollout[[:space:]]\+[0-9]\+/--num-rollout 200/' "$SCRIPT"
echo "补丁完成。"
```

```

在脚本被打补丁之后，启动GRPO训练循环：

```bash
%%bash
# 切换到slime仓库目录
cd /workspace/notebooks/slime
# 设置环境变量并启动训练脚本
SLIME_DIR=/root \
MODEL_DIR=/root \
DATA_DIR=/root \
bash scripts/run-qwen3-4B-amd.sh
```

```

### 4. 理解训练脚本[#](#understanding-the-training-script)

`run-qwen3-4B-amd.sh`

脚本包含GRPO训练的所有配置。它被组织成多个参数组，用于控制训练流程的不同方面。

以下是脚本关键组件的分解说明。每个部分对应于训练工作流的一个特定方面。

#### 模型配置[#](#model-configuration)

```
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
source "${SCRIPT_DIR}/models/qwen3-4B.sh"
```

```

从 `scripts/models/qwen3-4B.sh` 加载模型架构设置。

. 这些是定义模型结构的 Megatron-LM 参数。

**重要**：确保诸如 `--rotary-base` 之类的设置

与您的目标模型匹配。不同模型可能使用不同的rotary base值。如有必要，在加载配置后使用以下命令覆盖此设置：

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

此设置控制训练期间模型加载和保存的位置。

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
# 推演参数
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

: 训练的总展开次数`--n-samples-per-prompt`

:每个提示采样的响应数（用于GRPO中的组相对优势）`--rm-type`

奖励模型类型 (slime 支持多种类型和自定义模型，使用 `--custom-rm-path`)

)

#### 评估配置[#](#evaluation-configuration)

评估任务继承滚动设置，但允许你覆盖特定参数:

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
)
```

```

**关键优化**

`--use-dynamic-batch-size`

将不同长度的样本打包成微批次，直到达到令牌限制 `--max-tokens-per-gpu`

: : 每个GPU的Token硬限制

**注意**：slime 即使在动态打包情况下也能保证严格的逐token损失计算。

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
--rollout-num-gpus-per-engine 2 # SGLang 张量并行
--sglang-mem-fraction-static 0.7
)
```

```

以 `--sglang-` 为前缀的参数

直接转发到 SGLang engine。

### 5. 从 Megatron 格式转换为 Hugging Face 格式以进行训练后推理[#](#convert-from-megatron-format-to-hugging-face-format-for-post-training-inference)

使用Slime进行强化学习训练后，模型检查点以Megatron-LM分布式格式保存，该格式无法直接用于标准推理框架。若要使用Hugging Face Transformers或SGLang进行推理，必须将这些检查点转换回Hugging Face（HF）格式。

将训练好的Megatron检查点（来自特定训练迭代）转换回Hugging Face格式，使用以下命令：

```bash
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

转换后，位于 `/root/Qwen3-4B_slime_hf_iter_0000199` 中的数据

采用标准Hugging Face格式，可用于[transformers推理](https://huggingface.co/Qwen/Qwen3-4B)、[SGLang服务](https://docs.sglang.io/basic_usage/send_request.html)，以及进一步的评估或微调。

## 摘要[#](#summary)

恭喜！通过完成这个使用 slime 的 GRPO 训练教程，您学习了如何在 AMD GPU 上使用强化学习训练大型语言模型。

以下是关键要点：

**环境设置**：基于 ROCm（ROCm（Radeon 开放计算平台））的 Docker 容器与 slime 提供了完整的强化学习训练环境。**检查点管理**：在 Hugging Face 和 Megatron 格式之间转换可实现跨框架的无缝集成。**GRPO 训练**：群体相对优势提供了稳定的强化学习训练，无需单独的价值网络。**可扩展架构**：SGLang 轨迹生成和 Megatron-LM 策略优化高效协同工作。

## 下一步[#](#next-steps)

**尝试不同数据集**：将GRPO应用于其他推理或指令遵循数据集。  
**调整超参数**：根据具体用例调整学习率、KL系数或采样策略。  
**扩展至更大模型**：使用相同工作流处理更大的Qwen模型或其他LLM架构。  
**评估训练后的模型**：在下游任务中测试微调后的模型以衡量改进效果。