---
title: "MLA decoding kernel of the AITER library to accelerate LLM inference &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/gpu_dev_optimize/aiter_mla_decode_kernel.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T18:22:15.983334+00:00
content_hash: "ab45fa0955c1a04d"
---

# AITER库的MLA解码内核以加速LLM推理[#](#mla-decoding-kernel-of-the-aiter-library-to-accelerate-llm-inference)

**作者**: Daniel Huang

**知识水平**：中级

想象一下，你正在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPU 上部署 DeepSeek-V3/R1 这样的大语言模型，突然解码阶段的 Multi Latent Attention (MLA) 成为了性能瓶颈。Token 生成感觉迟缓，延迟不断累积，降低了用户体验。这时，AMD AITER 库前来解围，大幅加速了 MLA 解码注意力内核，为你的模型重新注入活力。

AITER 是 AMD 的高性能算子库，针对 AMD Instinct（Instinct（AMD 数据中心 GPU 系列））GPU 上的 AI 工作负载进行了优化。它在以下情况下不可或缺：

算子性能远未达到理论潜力。

特定的算子成为推理瓶颈。

您需要针对 AMD Instinct（AMD 数据中心 GPU 系列）GPU 的架构特定优化。

本教程将逐步指导您集成 AITER MLA 解码注意力内核，以利用 AMD Instinct（Instinct（AMD 数据中心 GPU 系列））GPU 加速 LLM 推理。与原生 PyTorch 实现相比，这将极大提升不同上下文长度下的内核性能。您将从设置 MLA 解码注意力内核开始。

**提示**：AITER 库中的内核已经集成到流行的 LLM 推理框架中，例如 vLLM 和 SGLang。这意味着你也可以通过这些框架在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 上实现 AITER 库带来的显著性能提升！

## 前提条件：设置加速环境[#](#prerequisites-setting-up-the-acceleration-environment)

This tutorial was developed and tested using the following setup, which is recommended to reproduce the same model acceleration with AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPUs.

### 操作系统[#](#operating-system)

**Ubuntu 22.04**：确保您的系统运行的是 Ubuntu 22.04 版本。

### 硬件[#](#hardware)

**AMD Instinct（AMD 数据中心 GPU 系列）GPU**：请确保您使用的是受 ROCm™ 软件支持的 AMD Instinct GPU，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.3.1**: 按照 [ROCm（ROCm（Radeon 开放计算平台）） 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm（ROCm（Radeon 开放计算平台））。安装完成后，使用 the 确认您的设置。

`amd-smi`

该命令列出可用的AMD GPU及其状态。

**注意**：对于 ROCm 6.4 及更早版本，请使用 `rocm-smi`

command instead.**Docker**：对于容器化部署，请确保已正确安装和配置Docker。请根据您的操作系统参考Docker安装指南。**Note**：确保Docker权限已正确配置。要配置允许非root用户访问的权限，请运行以下命令：usermod -aG docker $USER newgrp docker

验证 Docker 是否正常工作

运行 hello-world

## 快速开始开发环境搭建[#](#quick-start-development-environment-set-up)

本教程使用预构建的ROCm（ROCm（Radeon 开放计算平台）） PyTorch镜像。

### 步骤 1：启动 ROCm（ROCm（Radeon 开放计算平台）） PyTorch Docker 容器[#](#step-1-launch-the-rocm-pytorch-docker-container)

启动 Docker 容器。该镜像是一个开箱即用的解决方案，包含预配置的依赖项：

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
-w /workspace \
rocm/pytorch:latest
```

```

**注意**：此命令将当前目录挂载到 `/workspace`

容器中的目录，方便文件访问。它让你能够在这个Docker容器中完成所有工作，包括手动安装AITER，并通过以下动手实践示例开始使用。

### 步骤 2：在容器中启动 Jupyter Notebooks[#](#step-2-launch-jupyter-notebooks-in-the-container)

在Docker容器内，使用以下命令安装JupyterLab：

```
安装 Jupyter
```

```

启动Jupyter服务器：

--ip=0.0.0.0 --port=8888 --no-browser --allow-root

```

**注意**：如果端口 `8888`

端口已被占用，请指定其他端口，例如 `--port=8890`

本教程的其余部分可以在您将此教程上传到服务器后，以交互块的形式在 Jupyter notebook 中运行。

### 步骤3：手动安装AITER库[#](#step-3-manually-install-the-aiter-library)

AITER 是一个快速扩展的库，拥有许多强大的功能。要安装 AITER，请使用以下命令：

```
%%bash
git clone --recursive https://github.com/ROCm（ROCm（Radeon 开放计算平台））/aiter.git
cd aiter
python3 setup.py develop
export PYTHONPATH=$PYTHONPATH:/workspace/aiter
```

```

**注意**：如果你的环境中同时运行 Jupyter 和 AITER，请设置 `PYTHONPATH`

相应地。

## 理解MLA解码注意力核心[#](#understanding-the-mla-decode-attention-kernel)

您可以在[AITER源代码](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/aiter/blob/main/aiter/mla.py#L114C1-L126C3)中找到MLA解码注意力内核定义。它至少需要八个输入参数，并可以接受三个额外的可选输入。以下是`mla_decode_fwd`的函数定义。

，包括参数：

```
def mla_decode_fwd(
    q, # [batch_size, num_heads, kv_lora_rank + qk_rope_dim]
    kv_buffer, # [num_pages, page_size, num_heads_kv, qk_head_dim]
    o, # 输出缓冲区 [batch_size, num_heads, kv_lora_rank]
    qo_indptr, # 查询序列指针 [batch_size + 1]
    kv_indptr, # KV序列指针 [batch_size + 1]
    kv_indices, # KV索引 [kv_indptr[-1]]
    kv_last_page_lens, # 最后一页大小 [batch_size]
    max_seqlen_q, # 最大查询序列长度
    sm_scale=None, # 缩放因子（默认：1.0/sqrt(qk_head_dim)）
    logit_cap=0.0, # （正在开发中）
    num_kv_splits=None, # KV分裂（自动确定）
):
```

```

每个参数都有特定的形状要求，因此正确的配置是获得最佳性能的关键：

**q**(`torch.tensor`

type): 查询张量，其形状要求如 `[batch_size, num_heads, kv_lora_rank + qk_rope_dim]`

.**kv 缓冲区**(`torch.tensor`)

type): 这是总KV缓存张量，形状要求类似`[num_pages, page_size, num_heads_kv, qk_head_dim]`

, 其中`num_heads_kv`

始终为 `1`

在解码阶段，和`num_pages`

和`page_size`

共同表示可分页的 KV 缓存。当 `page_size = 1` 时

, 键值缓存设置为原始表示，这浪费了大量 GPU 内存。**o**(`torch.tensor`

类型)：这是输出缓冲区。`mla_decode_fwd`

函数会将结果放入`o`中

, 其形状要求类似 `[batch_size, num_heads, kv_lora_rank]`

.**qo_indptr**(`torch.tensor`

type): 这是一个指向每个查询和输出序列起始地址的指针，形状要求如`[batch_size + 1]`。

. 当批次中每个序列的序列长度不同时，`qo_indptr`

用于记录此信息，这有助于正确处理每个序列。**kv_indptr**(`torch.tensor`

type): 这是一个指向每个context/kv序列起始地址的指针，形状要求如`[batch_size + 1]`

. 每个批次中的查询序列不同，答案序列也不同，因此上下文/键值序列长度也不同。`kv_indptr`

变量记录此信息以帮助正确处理查询序列的每个上下文/kv。**kv_indices**(`torch.tensor`)

type): 包含每个序列的具体 kv 起始索引。其形状要求如 `[kv_indptr[-1]]`

.**kv_last_page_lens**(`torch.tensor`

类型）：这是每个序列的最后一页大小，形状要求如`[batch_size]`

.**max_seqlen_q:**(`torch.tensor`)

类型)：这是本批次所有查询中的最大序列长度。**sm_scale**(`scalar`

类型）：这等于`1.0 / (qk_head_dim**0.5)`

，它表示缩放点积注意力公式中的分母。**logit_cap**：这是一个进行中的工作，可以忽略。更多信息请参见以下[注释](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/aiter/blob/main/aiter/mla.py#L128)。**num_kv_splits**(`scalar`)

type)：此参数可忽略。它表示分配多少个GPU工作组或线程块来处理kv，但代码会使用启发式算法自动确定该值。

## 运行一个实际示例[#](#running-a-practical-example)

是时候开始逐步操作了，这将使 MLA 解码注意力在您的 Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X 上以闪电般的速度运行。

### 设置环境[#](#setting-the-environment)

首先准备 AMD MI300X GPU，以 CPU 作为备用：

```python
import os
import sys
# 更改工作目录到仓库
os.chdir("./aiter") # 相对于笔记本位置的路径
# 将当前目录（aiter仓库根目录）添加到Python路径
sys.path.insert(0, os.getcwd())
import torch
from aiter.mla import mla_decode_fwd
# 让我们为展示准备硬件！
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"一切就绪！运行在：{device}")
```

```

### 准备张量[#](#prepare-the-tensors)

现在为本次运行准备张量。您将配置以下内容：

一批128个序列，使用

`batch_size = 128`

一个4096-token的KV缓存（我们模型的内存），使用

`kv_cache_seqlen = 4096`

单查询解码，使用

`q_seqlen = 1`

```
# 性能参数
batch_size = 128  # 我们正在处理的序列数量
kv_cache_seqlen = 4096  # 模型记忆的回溯长度
q_seqlen = 1  # 一次解码一个token
# 初始化指针数组
qo_indptr = torch.zeros(batch_size + 1, dtype=torch.int, device=device)
kv_indptr = torch.zeros(batch_size + 1, dtype=torch.int, device=device)
# 填充序列长度（简单情况：所有序列长度相等）
seq_lens_qo = torch.full((batch_size,), q_seqlen, dtype=torch.int, device=device)
seq_lens_kv = torch.full((batch_size,), kv_cache_seqlen, dtype=torch.int, device=device)
```

```

上述示例代码首先声明了两个用于 `qo_indptr` 的缓冲区。

以及 `kv_indptr`

然后填充 `seq_lens_qo`

和 `seq_lens_kv`

使用 `q_seqlen = 1`

以及 `kv_cache_seqlen = 4096`

为了简单起见，它假设每个序列具有相同的 `q_seqlen `

和 `kv cache seqlen`

。

然后它填充 `kv_indptr`

和 `qo_indptr`

通过传递 `cumsum`

获取 qkv 的序列长度，然后通过从前者减去后者来计算每个序列的实际长度。这就是高效注意力的“秘密武器”。

```
# 计算累积长度 - 这告诉我们每个序列的起始位置
kv_indptr[1:] = torch.cumsum(seq_lens_kv, dim=0) # KV 内存布局
qo_indptr[1:] = torch.cumsum(seq_lens_qo, dim=0) # 查询/输出布局
# 例如：kv_indptr = [0,5,11,18] 表示：
# 序列 0：位置 0-4（长度 5）
# 序列 1：位置 5-10（长度 6）
# 序列 2：位置 11-17（长度 7）
```

```

现在准备你的 key-value 缓存。可以将其视为模型的工作存储。

初始化每个序列的具体 kv 起始索引以及每个序列的 kv 最后一页的长度（大小）。

为简单起见，定义

`page_size = 1`

, 所以每个序列的kv last page lens为`1`

.对于此示例，设置最大值为

`kv_indices`

到`2097152`

这是通过 `batch_size * 16384` 计算得出的。

, 即等于`128 * 16384`

. 这意味着对于一个`batch_size`

的`128`

，你可以最多生成`16384`个。

每个序列的 token。

```
kv_indices = torch.randint(0, 2097152, (kv_indptr[-1].item(),), dtype=torch.int, device=device)
kv_last_page_lens = torch.ones(batch_size, dtype=torch.int, device=device)
```

```

现在介绍主要输入：查询张量（query tensor）和KV缓存（KV cache），以及输出缓冲区（output buffer）。这些是`q`

, `kv buffer`

, 和 `o`

:：

```
num_heads = 128 # 注意力头的数量
q_head_dim = 128 # 每个头的维度
kv_lora_rank = 512 # KV的LoRA秩
qk_rope_head_dim = 64 # 旋转位置嵌入维度
# 查询张量 - 我们向模型提出的问题
q = torch.randn(
(batch_size * q_seqlen, num_heads, kv_lora_rank + qk_rope_head_dim),
dtype=torch.bfloat16, device=device
)
num_heads_kv = 1
page_size = 1
q_head_dim = 128
# 我们的KV缓存 - 模型的知识库
kv_buffer = torch.randn(
(2097152, page_size, num_heads_kv, kv_lora_rank + qk_rope_head_dim),
dtype=torch.bfloat16, device=device
)
# 输出缓冲区 - 魔法发生的地方
o = torch.empty(
(batch_size * q_seqlen, num_heads, kv_lora_rank),
dtype=torch.bfloat16, device=device
).fill_(-1)
```

```

**注意**：你不需要定义这些缓冲区。但是，请确保你定义的形状尺寸与此处显示的值匹配。

### 启动内核[#](#launching-the-kernel)

一切准备就绪，启动您优化后的 MLA 解码注意力内核。

```
mla_decode_fwd(
q,
kv_buffer,
o,
qo_indptr,
kv_indptr,
kv_indices,
kv_last_page_lens,
1,
sm_scale= 1.0 / (q_head_dim**0.5)
)

```

现在看看你得到的结果。

```
print(o)
```

```

最终形状是：

```
print(o.shape)
```

```

## 摘要[#](#summary)

随着注意力计算现已优化，结果将无缝流入模型的下一层，使整个推理管道保持最大速率运行。

严格的基准测试展示了该内核的真实性能：

**基准测试亮点**

评估了多种上下文长度（512-4096 tokens）

已使用固定批量大小（128）进行测试

比较不同的MLA算法实现

**结果**：

相对于原生PyTorch实现的一致加速。

想象一下这些性能提升对你的应用意味着什么：

降低实时应用的延迟

提升批量处理吞吐量

全面降低计算成本

准备好迈出下一步了吗？通过以下资源深入了解AITER的功能：

探索

查看 [AITER GitHub 仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/aiter) 了解更多优化示例。

给仓库加星标以获取新功能更新。