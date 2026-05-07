---
title: "Profiling Llama-4 inference with vLLM &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/gpu_dev_optimize/llama4_profiling_vllm.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T18:22:30.783177+00:00
content_hash: "5cd1eff61a4932bb"
---

# 使用 vLLM 对 Llama-4 推理进行性能分析[#](#profiling-llama-4-inference-with-vllm)

**作者**：Shekhar Pandey 和 Liz Li

**知识水平**：中级

性能分析对于理解大语言模型推理管线中的性能瓶颈至关重要。本教程将引导您使用 vLLM 框架在 AMD GPU 上对 **Llama-4 Scout-17B-16E-Instruct** 模型进行性能分析，采用 ROCm（ROCm（Radeon 开放计算平台））。您将捕获详细的内核跟踪，之后使用 Perfetto 进行可视化。

## 前提条件[#](#prerequisites)

在开始本教程之前，请确保您已具备以下条件：

访问门控

**Llama-4 Scout-17B-16E-Instruct**模型访问到

**Perfetto UI**

### 硬件[#](#hardware)

**AMD GPUs（AMD 图形处理器）**：请确保您使用的是支持 ROCm™（Radeon 开放计算平台）的 AMD GPU，例如 Instinct™（AMD 数据中心 GPU 系列）MI300X 或 Radeon™（AMD 消费级 GPU 系列）Pro W7900，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.3, 6.4**：按照 [ROCm（ROCm（Radeon 开放计算平台）） 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 进行安装和验证。通过运行以下命令来验证你的 ROCm（ROCm（Radeon 开放计算平台）） 安装：该命令将列出你的 AMD GPU 及其相关详细信息。

**注意**：对于 ROCm（ROCm（Radeon 开放计算平台）） 6.4 及更早版本，请使用`rocm-smi`

命令代替。**Docker**：确保Docker已正确安装和配置。更多信息请参见[Docker安装指南](https://docs.docker.com/get-docker/)。

## 准备训练环境[#](#prepare-the-training-environment)

按照以下步骤配置您的教程环境：

### 1. 拉取 Docker 镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的Docker镜像：

```
pull rocm/vllm-dev:main
```

```

### 2. 启动 Docker 容器[#](#launch-the-docker-container)

在您服务器的终端中启动 Docker 容器，并映射必要的目录。

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
rocm/vllm:latest
```

```

**注意**：该命令将当前目录挂载到 `/workspace`。

容器中的目录。确保在运行 Docker 命令之前将笔记本文件复制到此目录，或在 Jupyter Notebook 环境启动后将其上传。保存终端输出中提供的令牌或 URL，以便从 Web 浏览器访问该笔记本。您可以从 [AI Developer Hub GitHub 仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev)下载此笔记本。

### 3. 安装并启动 Jupyter[#](#install-and-launch-jupyter)

在Docker容器内，使用以下命令安装Jupyter：

```
安装 jupyter
```

```

启动 Jupyter server:

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

## 逐步流程[#](#step-by-step-process)

按照以下步骤对 Llama-4 模型进行性能分析并捕获内核跟踪。

### 第1步：登录 Hugging Face[#](#step-1-logging-in-to-hugging-face)

提供您的 Hugging Face token

您需要一个 Hugging Face API 令牌来访问 Llama-4。在 [Hugging Face Tokens](https://huggingface.co/settings/tokens) 生成您的令牌，并申请访问 [Llama-4-Scout 17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct)。令牌通常以“hf_”开头。

在您的Jupyter notebook中运行以下交互式块以设置token：

**注意**：取消选中“Add token as Git credential”选项。

```
from huggingface_hub import notebook_login, HfApi
# 提示用户登录
notebook_login()
```

```

验证您的 token 是否被正确接受：

```python
from huggingface_hub import HfApi
try:
    api = HfApi()
    user_info = api.whoami()
    print(f"令牌验证成功！登录用户为：{user_info['name']}")
except Exception as e:
    print(f"令牌验证失败。错误：{e}")
```

```

### 步骤 2：使用 profiler 配置启动 vLLM 服务器[#](#step-2-start-the-vllm-server-with-a-profiler-configuration)

在你的JupyterLab会话中打开一个新的终端标签页。在这个新终端中，运行以下命令。保持终端打开状态。

```
-p /profile
export VLLM_TORCH_PROFILER_DIR=/profile
# 使用标准配置启动 vLLM 服务器
RCCL_MSCCL_ENABLE=0 \
VLLM_USE_V1=1 \
VLLM_WORKER_MULTIPROC_METHOD=spawn \
VLLM_USE_MODELSCOPE=False \
VLLM_USE_TRITON_FLASH_ATTN=0 \
vllm serve meta-llama/Llama-4-Scout-17B-16E-Instruct \
--disable-log-requests \
-tp 8 \
--max-num-seqs 64 \
--no-enable-prefix-caching \
--max_num_batched_tokens=320000 \
--max-model-len 32000
```

```

### 步骤3：运行基准测试并捕获跟踪[#](#step-3-run-the-benchmark-and-capture-the-trace)

在服务器运行中的情况下，触发一个合成基准测试请求以生成流量并收集性能分析数据：

```
!vllm bench serve \
--model meta-llama/Llama-4-Scout-17B-16E-Instruct \
--dataset-name random \
--random-input-len 2000 \
--random-output-len 10 \
--max-concurrency 64 \
--num-prompts 64 \
--ignore-eos \
--percentile_metrics ttft,tpot,itl,e2el \
--profile
```

```

确保你添加 `--profile`

该标志会在基准测试开始前启动性能分析器，在其结束后停止，并生成跟踪数据。

**注意：** 上述单元格执行完成后，通过按下 **Ctrl-C** 停止您在另一个终端中启动的 vLLM 服务器。

### 步骤 4：使用 Perfetto UI 可视化追踪[#](#step-4-visualize-the-trace-using-perfetto-ui)

生成追踪后，解压它。追踪以 JSON 格式保存。要可视化它，使用 [Perfetto UI](https://ui.perfetto.dev/)，这是一个专为大规模性能分析数据构建的强大追踪查看器。这有助于发现推理管线中的延迟瓶颈、CPU-GPU 重叠以及内核级低效问题。要可视化追踪，请遵循以下步骤：

转到

点击 [https://ui.perfetto.dev](https://ui.perfetto.dev/)。

**“打开跟踪文件”**.上传

`.json`

文件。

打开跟踪后，它将显示为如下所示：

#### 理解prefill和decode时间线[#](#understanding-the-prefill-and-decode-timelines)

现在放大追踪，解释每个片段揭示了 Llama-4 执行阶段的哪些信息。这是 Perfetto 中捕获的两个重要进程时间线的特写：

**注意：** 本节的重点是前两个轨道：`python3 3906`

和 `python3 2`

.

`python3 3906`

异步CPU调用

**橙片**在`python3 3906`下

展示了高级模型代码在CPU上的执行。它包括：Calls like

`execute_model`

,`forward`

，以及`hipMemcpyWithStream`

PyTorch 内部机制，例如

`aten::to`

和`aten::copy_`

实际的前向传播对于

Llama4ForCausalLM

以及内存传输

这部分反映了推理过程中CPU端的编排，从输入准备到将内核调度到GPU。

python3 2

: GPU内核时间线The

`python3 2` 下的 **粉红色切片**

这是GPU内核执行被可视化的区域。此slice表示CPU将任务入队后GPU正在执行的实际计算工作。关键见解如下：

两次内核执行之间有明显的间隙。

这个间隙将两个不同的阶段分隔开：

**间隙之前**：这是“prefill”阶段，在此阶段，初始提示被编码，注意力和缓存状态被填充。**间隙之后**：这是“decode”阶段，在此阶段，模型生成令牌，通常使用缓存的键/值张量。

#### 理解内核时间线[#](#understanding-kernel-timelines)

当您扩展 `python3 2`

在 Perfetto 的时间线中，您将看到两个不同的 GPU 流，代表设备上执行的不同类型的操作。

**注意：** 此放大视图有助于您区分计算内核和通信操作。

流

`3 3`

: 所有 GPU 内核 Stream

3 3

是**主计算流**，所有GPU内核执行都在此调度。这包括：`MatMul`

以及 GEMM 操作、融合的 MLP 和注意力模块

位置编码和层归一化

任何融合或逐元素内核

此流紧密排列，展示了模型推理活动的主体。这些内核的节奏和间隔有助于诊断诸如：

跨张量并行秩的负载均衡

内核启动间隙

Prefill 与 decode 阶段（基于间隙前后的密度）

流

3 8

AllGather 内核流

3 8

专门用于**AllGather**操作，这些操作是张量并行通信过程的一部分。这些内核：在多GPU设置中跨设备同步激活。

通常发生在层边界之间

至关重要

`tp=8`

跨八个分片同步部分输出的设置

### 第5步：放大分析注意力前向核[#](#step-5-zoom-in-to-analyze-the-attention-forward-kernel)

注意力是所有基于Transformer的语言模型的核心，Llama-4也不例外。对其**注意力前向kernel**进行性能剖析，可以让我们深入了解其计算效率。请深入跟踪，在内核层面检查它。

#### 放大内核时间线[#](#zoom-into-the-kernel-timeline)

导航到

python3 2

然后到`stream 3 3`

在 Perfetto UI 中。使用鼠标滚动或拖拽以放大到密集的内核集群。

将鼠标悬停在一个突出的内核上。你应该会看到一个类似

_fwd_kernel

。

这是跟踪中的一个示例图像：

#### 理解内核切片[#](#understanding-the-kernel-slice)

从跟踪视图下方的**详细信息**面板中，您可以提取以下内容：

字段 | 值 |
|---|---|
|
|
|
|
|
|
|
|
|
|
|

该内核是**多头注意力前向传播**的一部分，这是推理中计算量最大的操作之一。

#### 回溯到 CPU[#](#tracing-back-to-the-cpu)

在内核细节中，靠近前面的流程，你会找到 `hipModuleLaunchKernel`。

。

点击此处跳回CPU线程（`python3 3906`）

），如下图所示以蓝色显示，它发出了此内核启动。此功能对于以下情况非常有用：

将 GPU 操作映射到其 Python 或 C++ 调用栈

识别调度或同步中的瓶颈

了解CPU将工作排入GPU队列所需的时间

按照上述流程，您可以追踪每个内核在预填充（prefill）和解码（decode）阶段所花费的时间。下表中的简短摘要展示了一个内核的情况。

### 步骤 6：使用Python进行程序化分析并提取GPU内核时间线[#](#step-6-programmatic-analysis-and-extracting-the-gpu-kernel-timeline-with-python)

为了超越视觉检查，你还可以通过编程方式解析跟踪信息，列出所有GPU内核及其持续时间。这在以下情况下非常有用：

内核函数启动模式

持续时间尖峰

执行中的间隙或异常

这是一个最小的Python脚本，用于读取`trace.json`

文件并按开始时间列出所有GPU内核：

解压缩 `.gz`

将跟踪文件输出到 `trace.json`

。

```
!gunzip -c /profile/$(ls /profile | head -n 1) > trace.json
```

```

运行下面的单元格，它会列出按开始时间排序的所有 GPU 内核。

```
import json
# Load the trace
with open("trace.json", "r") as f:
trace = json.load(f)
gpu_kernels = []
# Extract GPU kernel events
for event in trace["traceEvents"]:
if event.get("ph") != "X":
continue
cat = event.get("cat", "").lower()
name = event.get("name", "")
start_time = event["ts"]
duration = event.get("dur", 0)
if "cuda" in cat or "kernel" in cat:
gpu_kernels.append({
"name": name,
"start": start_time,
"duration": duration
})
# Print all GPU kernels with their durations
print(f"{'GPU 内核函数 (Kernel)':<60} {'Start (us)':<15} {'Duration (us)':<15}")
print("-" * 90)
for k in sorted(gpu_kernels, key=lambda x: x["start"]):
print(f"{k['name']:<60} {k['start']:<15} {k['duration']:<15}")
```

```

## 结论[#](#conclusion)

在本教程中，您逐步了解了使用vLLM对AMD GPU上Llama-4推理进行性能分析的端到端流程，包括：

设置包含ROCm（Radeon开放计算平台）和vLLM的容器

启用和捕获详细的性能追踪

可视化CPU-GPU交互使用

[Perfetto](https://ui.perfetto.dev/)放大查看注意力块的核级活动

使用Python以编程方式分析跟踪日志