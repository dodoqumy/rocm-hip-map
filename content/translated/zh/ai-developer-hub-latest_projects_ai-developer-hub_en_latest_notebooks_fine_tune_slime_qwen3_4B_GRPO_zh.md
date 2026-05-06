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

**知识水平**：中级

现代大语言模型在预训练之后并未停止改进。为了在实际任务中变得有用、对齐且稳健，它们必须从反馈中学习。这就是强化学习（RL）的用武之地。

本教程将带你体验一个真实的、生产级别的强化学习训练流水线，针对[Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)大语言模型，完全在AMD GPU上运行，基于ROCm（Radeon开放计算平台）。该工作流由[slime](https://github.com/THUDM/slime)驱动，这是一个原生于SGLang的后训练框架，专门为LLM规模的强化学习扩展而构建。

## 为什么使用 slime？[#](#why-use-slime)

训练LLMs with RL因两个关键原因而具有挑战性：

**Rollout generation is expensive**: You need a fast inference engine to sample large volumes of model responses.  
**Policy optimization is heavy**: You need a highly optimized training stack that scales across GPUs.

[slime](https://github.com/THUDM/slime) 通过清晰分离并高效连接这两个组件，解决了这两项挑战：

**SGLang**: 用于高吞吐量 rollout 生成**Megatron-LM**: 用于分布式策略训练

它们共同构成了一个可扩展、模块化的RL系统，能够适应现代LLM工作负载。

## 什么是GRPO？[#](#what-is-grpo)

这个教程使用GRPO（Group Relative Policy Optimization），这是一种专为可扩展的大语言模型训练设计的现代强化学习算法。

传统RL方法通常依赖于单一的参考基线，也称为评论家模型，它可以是：

训练成本高

难以稳定

对奖励噪声敏感

GRPO采用了一种不同的方法。它不是孤立地评估一个响应，而是：

对同一提示采样多个响应

将它们分组在一起

计算组内的相对优势

### 为什么这对LLMs很重要[#](#why-this-matters-for-llms)

GRPO 提供了若干实际优势：

无需单独的值网络

更稳定的训练信号

针对大批量展开的更好扩展性能

天然适配服务端生成 (SGLang)

这使得GRPO特别适用于：

指令微调

推理改进

基于偏好的优化

多GPU系统上的大规模RL

## 您将在此笔记本中学到什么[#](#what-you-ll-learn-in-this-notebook)

在本教程结束时，您将能够：

为AMD GPU上的slime设置一个支持ROCm（ROCm（Radeon开放计算平台））的Docker环境

配置用于Qwen3-4B的GRPO，包括推演和奖励设置

运行端到端 RL 训练循环，结合：

SGLang 用于生成

用于优化的 Megatron-LM

理解可扩展的大语言模型强化学习训练背后的系统级设计选择

无论您是在尝试后训练研究还是构建生产级RL管道，此笔记本旨在为您提供可运行的代码和清晰的思维模型。让我们开始吧。

## 前提条件[#](#prerequisites)

本教程是基于以下配置进行开发和测试的。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**：确保您的系统运行的是 Ubuntu 22.04。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPUs**：本教程已在配备八块 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 的完整节点上进行了测试。请确保您使用的是支持 ROCm（ROCm（Radeon 开放计算平台））的 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 或兼容硬件，且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 7.0.0**: 按照 [ROCm（ROCm（Radeon 开放计算平台）） 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm（ROCm（Radeon 开放计算平台））。安装完成后，使用以下命令确认您的设置：该命令将列出您的 AMD GPU 及其相关信息。

**Docker**：确保Docker已正确安装并配置。请根据您的操作系统参考Docker安装指南。**注意**：确保Docker权限已正确配置。要配置允许非root用户访问的权限，请运行以下命令：usermod -aG docker $USER newgrp docker

验证Docker是否正常工作：

运行 hello-world

## 系统验证[#](#system-validation)

在运行AI工作负载之前，确保你的AMD硬件配置正确并达到最佳性能非常重要。

通常，禁用NUMA（非统一内存访问）自动平衡可能有利于应用程序性能。然而，对于某些类型的工作负载，此设置可能对性能产生不利影响。

运行此命令以验证当前 NUMA 设置：

```
/proc/sys/kernel/numa_balancing
```

```

输出为 `0`

表示NUMA自动平衡被禁用。如果没有输出或者输出为 `1`

，运行以下命令以禁用NUMA自动平衡。

```
sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
```

```

更多信息，请参见 [禁用 NUMA 自动平衡](https://instinct.docs.amd.com/projects/amdgpu（amdgpu（AMD GPU 内核驱动））-docs/en/latest/system-optimization/mi300x.html#disable-numa-auto-balancing)。

## 设置环境[#](#set-up-the-environment)

按照以下步骤准备训练环境。

### 1. 拉取Docker镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的Docker镜像：

```
pull rlsys/slime:latest
```

```

### 2. 启动 Docker 容器[#](#launch-the-docker-container)

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

**注意**：如果您需要返回到 `slime`

退出容器后，请使用以下命令：

```
start slime
docker exec -it slime bash
```

```

**注意**：确保笔记本文件已复制到 `/workspace`

目录或者启动后上传到Jupyter Notebook环境中。保存终端输出中提供的令牌或URL，以便通过Web浏览器访问该记事本。您可以从[AI开发者Hub GitHub仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev)下载此笔记本。

### 3. 安装并启动Jupyter[#](#install-and-launch-jupyter)

在 Docker 容器内，使用以下命令安装 Jupyter：

```
install jupyter
```

```

启动Jupyter服务器：

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

**注意**: 确保端口 `8888`

在运行上述命令之前，请确保该端口在你的系统上尚未被使用。如果已被占用，你可以通过替换 `--port=8888` 来指定一个不同的端口。

使用另一个端口号，例如 `--port=8890`

.

### 4. Install the required libraries[#](#install-the-required-libraries)

在开始RL训练之前，你需要安装slime——这是连接基于SGLang的rollout生成与基于Megatron-LM的策略优化的核心框架。

由于 slime 正处于活跃开发阶段，持续的提交可能会引入行为变更，影响 rollout 语义、奖励计算或训练稳定性。为确保本教程的可复现性与稳定性，请将安装固定至一个已知可正常工作的提交。

在启用了ROCm（ROCm（Radeon 开放计算平台））的Docker容器内运行以下命令：

```
!git clone https://github.com/THUDM/slime.git
%cd slime
# 注意 -- 你可以运行最新的上游版本。如果想要稳定版本，请检出以下提交ID
!git checkout 0934a0e
# 安装该包
!pip install -e .
```

```

在继续之前，请确认 slime 已正确安装且 Python 可访问它。

```
# 验证所需库的安装和版本
!pip list | grep slime
```

```

如果 `slime`

出现在输出中，您的环境已准备好进行下一步。

## 运行GRPO训练[#](#run-grpo-training)

本部分将引导您完成设置和运行Qwen3-4B的群组相对策略优化（GRPO）训练的端到端流程。

总体而言，GRPO训练需要：

基础预训练模型（你想要改进的策略）

用于生成展开和计算奖励的训练数据集

一个留出评估数据集，用于在训练期间跟踪泛化性能

### 1. 下载模型和数据集[#](#download-the-model-and-datasets)

首先，下载基础的 Qwen3-4B 模型，该模型作为 RL 微调的初始策略。

在训练中，你将使用 `dapo-math-17k`

, a dataset designed to evaluate step-by-step mathematical reasoning. This is a task for which relative comparisons between multiple model outputs are especially effective.

为了评估，使用 `aime-2024`

, 它提供了一个清晰的基准，用于监控推理性能而不泄露训练数据。

执行以下命令以下载所有必需的工件。首先，从 Hugging Face 下载基础 Qwen3-4B 模型检查点：

```
!hf download Qwen/Qwen3-4B --local-dir /root/Qwen3-4B
```

```

接下来，下载训练数据集（`dapo-math-17k`）

) 用于数学推理任务：

```
> !hf download --repo-type dataset zhuzilin/dapo-math-17k \
--local-dir /root/dapo-math-17k
```

```

然后下载AIME 2024评估数据集用于基准测试：

```
!hf download --repo-type dataset zhuzilin/aime-2024 \
--local-dir /root/aime-2024
```

```

### 2. 转换检查点格式[#](#convert-the-checkpoint-format)

在开始GRPO训练之前，请将预训练的Hugging Face checkpoint转换为Megatron Core分布式格式。

需要进行此转换，因为slime使用Megatron-LM进行训练。Megatron-LM期望模型权重根据目标并行化策略（即tensor parallelism和pipeline parallelism）进行布局。相比之下，Hugging Face检查点将权重以与框架无关的单进程格式存储。

这是针对给定模型和并行配置的一次性预处理步骤。只要并行设置保持不变，您无需在每次训练运行时重复此步骤。

运行以下命令以执行转换：

```bash
%%bash
# 导航到 slime 仓库
cd /workspace/notebooks/slime
# 加载模型配置参数
source scripts/models/qwen3-4B.sh
# 定位 megatron core 安装路径
MEGATRON_LM_PATH=$(pip list | grep megatron-core | awk '{print $NF}')
# 运行转换工具
PYTHONPATH=${MEGATRON_LM_PATH} python tools/convert_hf_to_torch_dist.py \
${MODEL_ARGS[@]} \
--no-gradient-accumulation-fusion \
--hf-checkpoint /root/Qwen3-4B \
--save /root/Qwen3-4B_torch_dist
```

```

### 3. 启动GRPO training[#](#launch-grpo-training)

此步骤准备并启动 GRPO 训练运行时。

由于 slime 训练脚本被设计为在独立环境中运行，它们可能包含防护措施（例如 `pkill -9 python`）。

）在 Jupyter notebook 中运行时是不安全的。此外，某些卸载行为可能会在 AMD GPU 上在交互式环境中导致不稳定性。

为确保基于Jupyter的工作流程稳定，下一个单元格将执行以下操作：

防止训练脚本终止Jupyter内核。

插入所需

`--no-offload`

用于训练和推演的标志。减少推演次数，以便更容易观察到早期的性能改进。

**注意**: 你可以调整 `--num-rollout`

基于您的数据集大小和训练目标。`--num-rollout` 的值越大

每轮迭代会产生更多次的展开，从而有效增加训练轮次并改善收敛，但代价是运行时间更长。

运行以下命令作为一次性设置任务，修补训练脚本。

```
%%bash
# 导航到 slime 仓库
cd /workspace/notebooks/slime
SCRIPT=scripts/run-qwen3-4B-amd.sh
echo "正在修补 $SCRIPT ..."
# 1. 仅当 `pkill -9 python` 尚未被注释时将其注释掉
if grep -qE '^[[:space:]]*pkill -9 python' "$SCRIPT"; then
echo " - 正在注释掉 pkill -9 python"
sed -i 's/^[[:space:]]*pkill -9 python/# pkill -9 python/' "$SCRIPT"
else
echo " - pkill 已注释或不存在"
fi
# 2. 仅当 --no-offload 标志尚未存在时注入它们
if ! grep -q -- '--no-offload-train' "$SCRIPT"; then
echo " - 在 --colocate 之后注入 --no-offload 标志"
sed -i '/--colocate/a \ --no-offload-train \\\n --no-offload-rollout \\' "$SCRIPT"
else
echo " - no-offload 标志已存在"
fi
sed -i 's/--num-rollout[[:space:]]\+[0-9]\+/--num-rollout 200/' "$SCRIPT"
echo "修补完成。"
```

```

在脚本补丁之后，启动GRPO训练循环：

```
%%bash
# 导航到 slime 仓库
cd /workspace/notebooks/slime
# 启动训练脚本，设置环境变量
SLIME_DIR=/root \
MODEL_DIR=/root \
DATA_DIR=/root \
bash scripts/run-qwen3-4B-amd.sh
```

```

### 4. 理解训练脚本[#](#understanding-the-training-script)

这个 `run-qwen3-4B-amd.sh`

脚本包含GRPO训练的所有配置。它被组织成几个参数组，控制训练管道的不同方面。

以下是脚本关键组件的分解。每个部分对应训练工作流程的特定方面。

#### 模型配置[#](#model-configuration)

```
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
source "${SCRIPT_DIR}/models/qwen3-4B.sh"
```

```

这将从 `scripts/models/qwen3-4B.sh` 加载模型架构设置。

. 这些是定义模型结构的 Megatron-LM 参数。

**重要**：确保类似 `--rotary-base` 的设置

匹配您的目标模型。不同的模型可能使用不同的旋转基数（rotary base values）。如有必要，在加载配置后通过以下命令覆盖此设置：

```
source "${SCRIPT_DIR}/models/qwen3-4B.sh"
MODEL_ARGS+=( --rotary-base 10000 )
```

```

#### 检查点配置[#](#checkpoint-configuration)

```
CKPT_ARGS=(
# SGLang需要的HF检查点；也用于分词器
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

这控制了训练期间模型加载和保存的位置。

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
# Rollout参数
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

关键参数

`--num-rollout`

: 训练的总展开次数`--n-samples-per-prompt`

每个提示采样的响应（用于GRPO中的群体相对优势）`--rm-type`

奖励模型类型（slime支持多种类型以及使用`--custom-rm-path`的自定义模型）

)

#### 评估配置[#](#evaluation-configuration)

评估任务继承推出设置，但允许你覆盖特定参数：

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

**关键优化**：

`--use-dynamic-batch-size`

：将不同长度的样本打包成微批次，直至达到token限制`--max-tokens-per-gpu`

每个GPU的token硬性限制

**注意**：slime 保证在动态打包的情况下仍然进行严格的逐 token 损失计算。

#### GRPO 算法参数[#](#grpo-algorithm-parameters)

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

#### SGLang 配置[#](#sglang-configuration)

```
SGLANG_ARGS=(
--rollout-num-gpus-per-engine 2 # SGLang 张量并行
--sglang-mem-fraction-static 0.7
)
```

```

以 `--sglang-` 为前缀的参数

直接转发到SGLang引擎。

### 5. 从 Megatron 格式转换为 Hugging Face 格式，用于训练后推理[#](#convert-from-megatron-format-to-hugging-face-format-for-post-training-inference)

在使用slime进行强化学习训练后，模型检查点以Megatron-LM分布式格式保存，这种格式无法直接用于标准推理框架。若要通过Hugging Face Transformers或SGLang运行推理，必须将这些检查点转换回Hugging Face (HF)格式。

要将训练好的Megatron检查点（来自特定的训练迭代）转换回Hugging Face格式，请使用以下命令：

```bash
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

采用标准的Hugging Face格式，适用于 [Transformers推理](https://huggingface.co/Qwen/Qwen3-4B)、[SGLang服务](https://docs.sglang.io/basic_usage/send_request.html)，以及进一步的评估或微调。

## 摘要[#](#summary)

恭喜！通过完成这个使用 slime 的 GRPO 训练教程，你学会了如何在 AMD GPU 上使用强化学习训练大型语言模型。

关键要点如下：

**环境配置**：启用 ROCm（Radeon 开放计算平台）的 Docker 容器配合 slime 提供完整的强化学习训练环境。  
**检查点管理**：在 Hugging Face 与 Megatron 格式之间进行转换，实现跨框架的无缝集成。  
**GRPO 训练**：群体相对优势（Group-relative advantages）无需独立价值网络即可提供稳定的强化学习训练。  
**可扩展架构**：SGLang 的 rollout 生成与 Megatron-LM 的策略优化协同高效工作。

## 下一步[#](#next-steps)

**尝试不同的数据集**：将GRPO应用于其他推理或指令跟随数据集。  
**调整超参数**：根据具体使用场景调整学习率、KL系数或采样策略。  
**扩展到更大模型**：对更大的Qwen模型或其他LLM架构使用相同的工作流程。  
**评估训练模型**：在下游任务上测试微调后的模型，以衡量改进效果。