---
title: "Kernel development and optimization with Triton &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/gpu_dev_optimize/triton_kernel_dev.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T18:59:53.094547+00:00
content_hash: "bd4dc104621a5315"
---

# 内核函数 (Kernel) 使用 Triton 进行开发与优化[#](#kernel-development-and-optimization-with-triton)

**作者**：Ning Zhang

**知识水平**：中级

[OpenAI Triton](https://github.com/triton-lang/triton) 是一个开源编程语言，受AMD GPU支持，旨在简化高性能任务（尤其是AI应用）中的GPU编程。本教程演示如何在AMD GPU上设置Triton开发环境并优化Triton内核性能。

## 先决条件[#](#prerequisites)

本教程使用以下配置进行开发和测试。

### 操作系统[#](#operating-system)

**Ubuntu 22.04/24.04**: 确保你的系统运行的是Ubuntu 22.04或24.04版本。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPU**：本教程已在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 上测试。请确保您使用的是支持 ROCm（ROCm（Radeon 开放计算平台）） 的 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 或兼容硬件，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.2, 6.3 或 6.4**：按照 [ROCm 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装和验证 ROCm。安装完成后，使用以下命令确认您的设置：

`amd-smi`

AMD还提供了预构建的ROCm（ROCm（Radeon 开放计算平台）） Docker镜像，例如[ROCm PyTorch镜像](https://hub.docker.com/r/rocm/pytorch)、[ROCm Ubuntu 22.04镜像](https://hub.docker.com/r/rocm/dev-ubuntu-22.04)以及[ROCm Ubuntu 24.04镜像](https://hub.docker.com/r/rocm/dev-ubuntu-24.04)。您可以使用这些预构建的Docker镜像来减少搭建ROCm（ROCm（Radeon 开放计算平台））环境所需的工作量。

**注意**：对于ROCm 6.4及更早版本，请使用`rocm-smi`。

命令，而不是`amd-smi`

**Docker**：确保Docker已正确安装和配置。请按照适用于您操作系统的Docker安装指南进行操作。**注意**：确保已正确配置Docker权限。如需配置权限以允许非root用户访问，请运行以下命令：usermod -aG docker $USER newgrp docker

验证 Docker 是否正常工作:

运行 hello-world

## 设置 Triton 开发环境[#](#set-up-the-triton-development-environment)

本教程使用预构建的ROCm（ROCm（Radeon 开放计算平台）） PyTorch镜像，但你也可以尝试其他ROCm（ROCm（Radeon 开放计算平台））环境作为基础镜像。

### 步骤1：启动 Docker 镜像[#](#step-1-launch-the-docker-image)

启动 Docker 容器。替换 `/path/to/Triton_Sample`

在您的主机上，替换为包含Triton示例代码的目录的完整路径。

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
rocm/pytorch:latest
```

```

**注意**：该命令将当前目录挂载到 `/workspace`

目录在容器中。确保在运行Docker命令之前将笔记本文件复制到此目录，或者在Jupyter Notebook环境启动后上传到其中。保存终端输出中提供的令牌或URL，以便通过Web浏览器访问此笔记本。您可以从[AI Developer Hub GitHub仓库](https://github.com/ROCm/gpuaidev)下载此笔记本。

### 步骤 2：在容器中启动 Jupyter Notebooks[#](#step-2-launch-jupyter-notebooks-in-the-container)

在 Docker 容器内，使用以下命令安装 Jupyter：

安装 jupyter

```

启动Jupyter服务器：

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

**注意**：确保端口 `8888`

在运行上述命令之前，确保该端口在您的系统中尚未被占用。如果已被占用，您可以通过替换 `--port=8888` 来指定一个不同的端口。

使用另一个端口号，例如 `--port=8890`

.

**注**：本教程的其余部分可以在您将此教程上传到服务器后，作为Jupyter notebook中的交互块运行。

### 步骤 3：安装 OpenAI Triton[#](#step-3-install-openai-triton)

在安装正确版本的 OpenAI Triton 之前，您必须先卸载任何旧版本。

#### 1. 卸载旧版本的Triton[#](#uninstall-the-old-version-of-triton)

强烈建议您在项目中使用最新版本的 Triton。AMD 及其他供应商会频繁更新 [OpenAI Triton](https://github.com/triton-lang/triton) 中的优化流程和算法，这些更新可提升您 Triton 内核的性能。

```!pip uninstall -y triton```

```

#### 2. 从源代码安装OpenAI Triton[#](#install-openai-triton-from-the-source-code)

安装Triton的详细步骤如下所示。

**注意:** 如果在构建 Triton 过程中有任何问题或疑问，请提交至 [Triton Issues](https://github.com/triton-lang/triton/issues)。

```
%%bash
# 如果存在，移除现有的 Triton 文件夹
if [ -d "triton" ]; then
echo "正在移除现有的 triton 目录..."
rm -rf triton
fi
# 克隆 Triton 仓库
git clone https://github.com/triton-lang/triton.git
# 安装依赖并从源码安装 Triton（非可编辑安装）
cd triton
pip install -r python/requirements.txt
pip install .
```

```

### 第4步：在AMD GPU上验证Triton[#](#step-4-validate-triton-on-an-amd-gpu)

在成功安装 Triton 后，通过以下方法验证其在 AMD GPU 上是否正常工作：运行以下 Python 向量加法示例，确认 Triton 内核能提供与 Torch API 相似的结果，即表明其在 AMD GPU 上高效运行。

```python
import torch
import triton
import triton.language as tl
DEVICE = triton.runtime.driver.active.get_active_torch_device()
@triton.jit
def add_kernel(x_ptr, # *指针* 指向第一个输入向量。
                y_ptr, # *指针* 指向第二个输入向量。
                output_ptr, # *指针* 指向输出向量。
                n_elements, # 向量的大小。
                BLOCK_SIZE: tl.constexpr, # 每个程序应处理的元素数量。
                # 注意：`constexpr` 使其可用作形状值。
                ):
    # 有多个“程序”处理不同数据。我们在此标识当前程序：
    pid = tl.program_id(axis=0) # 我们使用一维启动网格，因此轴为0。
    # 此程序将处理从初始数据偏移的输入。
    # 例如，如果向量长度为256且block_size为64，程序将分别访问元素[0:64, 64:128, 128:192, 192:256]。
    # 请注意，偏移量是一个指针列表：
    block_start = pid * BLOCK_SIZE
    offsets = block_start + tl.arange(0, BLOCK_SIZE)
    # 创建掩码以防止内存操作越界。
    mask = offsets < n_elements
    # 从DRAM加载x和y，如果输入不是块大小的整数倍，则屏蔽多余元素。
    x = tl.load(x

```

输出日志是：

## 为AMD GPU优化Triton代码[#](#optimize-the-triton-code-for-amd-gpus)

softmax 函数常用于卷积神经网络（CNN）分类模型，甚至基于 Transformer 的大语言模型（LLM）。它通过计算每个值的指数，然后除以所有指数的总和来归一化这些值，从而将原始输出分数（即 logits）转换为概率。这个过程确保输出值在 (0,1) 范围内且总和为1，以便将它们解释为概率。PyTorch 将此函数实现为 [标准 API](https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html)。

### 朴素版本[#](#naive-version)

根据规范，你在Triton内核中实现了softmax算法的朴素版本。为了确定最大数据点和所有指数项的对应和，该内核版本使用了两个for循环，外加一个for循环来计算最终的softmax结果，总共三个循环。

以下示例测试了一个 8192 x 8192 张量的内核性能，其中列维度的块大小为 256。在运行预热部分以避免将内核编译时间计入最终数据后，您可以获得朴素版本的性能数据。

```
import torch
import triton
import triton.language as tl
DEVICE = triton.runtime.driver.active.get_active_torch_device()
@triton.jit
def softmax_kernel_naive(in_ptr, output_ptr, row_stride, n_cols, BLOCK_SIZE: tl.constexpr):
pid = tl.program_id(0)
in_max = -float('inf')
for offset in range(0, n_cols, BLOCK_SIZE):
col_range = tl.arange(0, BLOCK_SIZE)
col_mask = col_range + offset < n_cols
in_data = tl.load(in_ptr + pid * row_stride + col_range + offset, mask=col_mask, other=-float('inf'))
in_max = tl.maximum(in_max, tl.max(in_data, axis=-1))
in_exp_sum = 0.0
for offset in range(0, n_cols, BLOCK_SIZE):
col_range = tl.arange(0, BLOCK_SIZE)
col_mask = col_range + offset < n_cols
in_data = tl.load(in_ptr + pid * row_stride + col_range + offset, mask=col_mask, other=-float('inf'))
in_exp_sum = in_exp_sum + tl.sum(tl.exp(in_data - in_max), axis=-1)
for offset in range(0, n_cols, BLOCK_SIZE):
col_range = tl.arange(0, BLOCK_SIZE)
col_mask = col_range + offset < n_cols
in_data = tl.load(in_ptr + pid * row_stride + col_range + offset, mask=col_mask)
in_exp = tl.exp(in_data - in_max)
tl.store(output_ptr + pid * row_stride + col_range + offset, in_exp / in_exp_sum, mask=col_mask)
torch.manual_seed(0)
x = torch.randn(8192, 8192, device=DEVICE)
n_rows, n_cols = x.shape
output_triton = torch.empty_like(x)
BLOCK_SIZE = 256
temp = torch.randn(n_rows, n_cols, device=DEVICE)
softmax_kernel_naive[(n_rows,)](
temp,
output_triton,
temp.stride(0),
n_cols,
BLOCK_SIZE
)#预热
torch.cuda.empty_cache() #清理缓存
start_event = torch.cuda.Event(enable_timing=True)
end_event = torch.cuda.Event(enable_timing=True)
start_event.record()
softmax_kernel_naive[(n_rows,)](
x,
output_triton,
x.stride(0),
n_cols,
BLOCK_SIZE
)
end_event.record()
torch.cuda.synchronize()
elapsed_time_ms = start_event.elapsed_time(end_event)
print(f'Softmax Triton 朴素版本耗时: {elapsed_time_ms:.3f}ms')

```

### Online softmax 版本[#](#online-softmax-version)

使用 Triton 语言可以轻松实现算法。为了提升当前内核函数的性能，首先需判断是否存在更高效的算法或解决方案。若有，请在您的 Triton 内核函数 (Kernel) 中尝试新算法。为减少朴素 softmax 算法中三个 for 循环导致的内存访问，[在线归一化因子计算](https://arxiv.org/pdf/1805.02867) 论文提出了一种新的在线 softmax 算法。

根据在线softmax算法，以下代码对朴素版本的内核进行了一些修改。

```python
import torch
import triton
import triton.language as tl
DEVICE = triton.runtime.driver.active.get_active_torch_device()
@triton.jit
def softmax_kernel_v1(in_ptr, output_ptr, row_stride, n_cols, BLOCK_SIZE: tl.constexpr):
    pid = tl.program_id(0)
    in_max = -float('inf')
    in_exp_sum = 0.0
    for offset in range(0, n_cols, BLOCK_SIZE):
        col_range = tl.arange(0, BLOCK_SIZE)
        col_mask = col_range + offset < n_cols
        in_data = tl.load(in_ptr + pid * row_stride + col_range + offset, mask=col_mask, other=-float('inf'))
        in_max_new = tl.maximum(in_max, tl.max(in_data, axis=-1))
        in_exp_sum = in_exp_sum * tl.exp(in_max - in_max_new) + tl.sum(tl.exp(in_data - in_max_new), axis=-1)
        in_max = in_max_new
    for offset in range(0, n_cols, BLOCK_SIZE):
        col_range = tl.arange(0, BLOCK_SIZE)
        col_mask = col_range + offset < n_cols
        in_data = tl.load(in_ptr + pid * row_stride + col_range + offset, mask=col_mask)
        in_exp = tl.exp(in_data - in_max)
        tl.store(output_ptr + pid * row_stride + col_range + offset, in_exp / in_exp_sum, mask=col_mask)
torch.manual_seed(0)
x = torch.randn(8192, 8192, device=DEVICE)
n_rows, n_cols = x.shape
output = torch.empty_like(x)
BLOCK_SIZE = 256
temp = torch.randn(n_rows, n_cols, device=DEVICE)
softmax_kernel_v1[(n_rows,)](
    temp,
    output,
    temp.stride(0),
    n_cols,
    BLOCK_SIZE
)# 预热
torch.cuda.empty_cache() # 清理缓存
start_event = torch.cuda.Event(enable_timing=True)
end_event = torch.cuda.Event(enable_timing=True)
start_event.record()
softmax_kernel_v1[(n_rows,)](
    x,
    output,
    x.stride(0),
    n_cols,
    BLOCK_SIZE
)
end_event.record()
torch.cuda.synchronize()
elapsed_time_ms = start_event.elapsed_time(end_event)
print(f'Softmax Triton V1 版本耗时: {elapsed_time_ms:.3f}ms')
```

```

### Fused-softmax 版本[#](#fused-softmax-version)

OpenAI Triton 提供了“融合softmax”（fused-softmax）的softmax参考示例。该示例基于在线softmax算法，通过移除一个for循环进一步简化了最大值数据的计算。同时，它通过增加线程束数量来告知编译器每行使用更多线程。这种配置通常需要针对性调优以获得更佳性能。最后，它通过调整GPU硬件配置改进了内核启动方案，从而可提升GPU内核占用率与性能。

```python
import torch
import triton
import triton.language as tl
from triton.runtime import driver
DEVICE = triton.runtime.driver.active.get_active_torch_device()
def is_hip():
    return triton.runtime.driver.active.get_current_target().backend == "hip"
def is_cdna():
    return is_hip() and triton.runtime.driver.active.get_current_target().arch in ('gfx940', 'gfx941', 'gfx942',
                                                                                  'gfx90a', 'gfx908')

@triton.jit
def softmax_kernel(output_ptr, input_ptr, input_row_stride, output_row_stride, n_rows, n_cols, BLOCK_SIZE: tl.constexpr,
                   num_stages: tl.constexpr):
    # 程序的起始行
    row_start = tl.program_id(0)
    row_step = tl.num_programs(0)
    for row_idx in tl.range(row_start, n_rows, row_step, num_stages=num_stages):
        # 步长表示需要增加多少指针才能前进1行
        row_start_ptr = input_ptr + row_idx * input_row_stride
        # 块大小是大于 n_cols 的下一个2的幂，这样每行可以放在一个块中
        col_offsets = tl.arange(0, BLOCK_SIZE)
        input_ptrs = row_start_ptr + col_offsets
        # 将行加载到 SRAM 中，由于 BLOCK_SIZE 可能大于 n_cols，因此使用掩码
        mask = col_offsets < n_cols
        row = tl.load(input_ptrs, mask=mask, other=-float('inf'))
        # 减去最大值以保证数值稳定性
        row_minus_max = row - tl.max(row, axis=0)
        # 注意：Triton 中的指数运算速度很快但近似（即与 CUDA 中的 __expf 类似）
        numerator = tl.exp(row_minus_max)
        denominator = tl.sum(numerator, axis=0)
        softmax_output = numerator / denominator
        # 将结果写回 DRAM
        output_row_start_ptr = output_ptr + row_idx * output_row_stride
        output_ptrs = output_row_start_ptr + col_offsets
        tl.store(output_ptrs, softmax_output, mask=mask)

properties = driver.active.utils.get_device_properties(DEVICE.index)
NUM_SM = properties["multiprocessor_count"]
NUM_REGS = properties["max_num_regs"]
SIZE_SMEM = properties["max_shared_mem"]
WARP_SIZE = properties["warpSize"]
target = triton.runtime.driver.active.get_current_target()
kernels = {}

torch.manual_seed(0)
x = torch.randn(8192, 8192, device=DEVICE)
n_rows, n_cols = x.shape
# 分配输出
y = torch.empty_like(x)

# 每次循环迭代的块大小是大于 x 列数的最小2的幂
BLOCK_SIZE = triton.next_power_of_2(n_cols)

# 另一个技巧是让编译器使用更多线程来处理每一行，通过增加每行分发的 warp 数量（num_warps）
num_warps = 8

# 软件流水线阶段数
num_stages = 4 if SIZE_SMEM > 200000 else 2

# 预编译内核以获取寄存器使用情况并计算线程占用率
kernel = softmax_kernel.warmup(y, x, x.stride(0), y.stride(0), n_rows, n_cols, BLOCK_SIZE=BLOCK_SIZE,
                               num_stages=num_stages, num_warps=num_warps, grid=(1, ))
kernel._init_handles()
n_regs = kernel.n_regs
size_smem = kernel.metadata.shared

if is_hip():
    # NUM_REGS 表示通用寄存器的数量。在 CDNA 架构上，这相当于所有可用寄存器的一半。
    # 但并非总是如此。大多数情况下，所有寄存器都可以用作通用寄存器。
    # 见 ISA 章节（CDNA3 的 3.6.4 节）
    # VGPR 从两个池中分配：常规 VGPR 和累加 VGPR。累加 VGPR 用于矩阵 VALU 指令，也可以直接从内存加载。
    # 一个 wave 最多可以有 512 个 VGPR，每种类型 256 个。当 wave 的 VGPR 总数少于 512 时，每种类型的数量是灵活的——不必相等。
    if is_cdna():
        NUM_GPRS = NUM_REGS * 2
    # MAX_NUM_THREADS 表示每个多处理器上可驻留的最大线程数。
    # 将该数除以 WARP_SIZE 即可得到可在 CU（多处理器）上并行执行的最大 wave 数。
    MAX_NUM_THREADS = properties["max_threads_per_sm"]
    max_num_waves = MAX_NUM_THREADS // WARP_SIZE
    occupancy = min(NUM_GPRS // WARP_SIZE // n_regs, max_num_waves) // num_warps
else:
    occupancy = NUM_REGS // (n_regs * WARP_SIZE * num_warps)

occupancy = min(occupancy, SIZE_SMEM // size_smem)

num_programs = NUM_SM * occupancy
num_programs = min(num_programs, n_rows)

# 创建持久化程序数量
start_event = torch.cuda.Event(enable_timing=True)
end_event = torch.cuda.Event(enable_timing=True)

start_event.record()
kernel[(num_programs, 1, 1)](y, x, x.stride(0), y.stride(0), n_rows, n_cols, BLOCK_SIZE, num_stages)
end_event.record()
torch.cuda.synchronize()
elapsed_time_ms = start_event.elapsed_time(end_event)

print(f'Softmax Triton V2 版本耗时: {elapsed_time_ms:.3f}ms')
```

```

## 摘要[#](#summary)

在本教程中，您学习了如何在AMD GPU上开发和优化Triton内核。要了解更多关于OpenAI Triton的信息，请参阅[官方Triton文档](https://triton-lang.org/main/index.html)。要了解有关在AMD GPU上运行Triton的更多信息，请参阅[ROCm（ROCm（Radeon 开放计算平台）） Triton optimization](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/optimizing-triton-kernel.html)和[内核函数 (Kernel) development optimization on Triton blog](https://rocm.blogs.amd.com/software-tools-optimization/kernel-development-optimizations-with-triton-on-/README.html)。希望本教程能鼓励您在AMD GPU上调整、测试并为Triton做出贡献，共同塑造AI加速的未来。