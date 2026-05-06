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

# 使用Triton进行内核函数（Kernel）开发和优化[#](#kernel-development-and-optimization-with-triton)

**作者**：Ning Zhang

**知识水平**: 中级

[OpenAI Triton](https://github.com/triton-lang/triton) 是一个开源编程语言，受到AMD GPU支持，旨在简化高性能任务（尤其是AI应用）中的GPU编程。本教程演示如何设置Triton开发环境并在AMD GPU上优化Triton kernel性能。

## 先决条件[#](#prerequisites)

本教程基于以下配置进行开发和测试。

### 操作系统[#](#operating-system)

**Ubuntu 22.04/24.04**：确保你的系统运行的是 Ubuntu 22.04 或 24.04 版本。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPU**：本教程已在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 上测试通过。请确保您使用的是支持 ROCm（ROCm（Radeon 开放计算平台））的 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 或兼容硬件，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.2、6.3 或 6.4**：按照 [ROCm（ROCm（Radeon 开放计算平台）） 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm（ROCm（Radeon 开放计算平台））。安装完成后，使用以下方式确认您的配置：

`amd-smi`

命令。AMD 还提供预构建的 ROCm（Radeon 开放计算平台）Docker 镜像，例如 [ROCm PyTorch 镜像](https://hub.docker.com/r/rocm/pytorch)、[ROCm Ubuntu 22.04 镜像](https://hub.docker.com/r/rocm/dev-ubuntu-22.04) 和 [ROCm Ubuntu 24.04 镜像](https://hub.docker.com/r/rocm/dev-ubuntu-24.04)。您可以使用这些预构建的 Docker 镜像来减少搭建 ROCm 环境所需的工作量。**注意**：对于 ROCm 6.4 及更早版本，请使用 `rocm-smi`。

使用command而不是`amd-smi`

**Docker**：确保 Docker 已正确安装和配置。请根据你的操作系统参考 Docker 安装指南。  
**注意**：确保 Docker 权限配置正确。要配置权限以允许非 root 用户访问，请运行以下命令：  
`usermod -aG docker $USER`  
`newgrp docker`

验证 Docker 是否正常工作：

运行 hello-world

## 设置 Triton 开发环境[#](#set-up-the-triton-development-environment)

本教程使用预构建的ROCm PyTorch镜像，但您也可以尝试其他ROCm环境作为基础镜像。

### 第一步：启动Docker镜像[#](#step-1-launch-the-docker-image)

启动Docker容器。替换 `/path/to/Triton_Sample`

使用主机上 Triton 示例代码所在目录的完整路径。

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

**注意**：此命令将当前目录挂载到 `/workspace`

容器中的目录。确保笔记本文件要么在运行Docker命令之前复制到此目录，要么在Jupyter Notebook环境启动后上传到其中。保存终端输出中提供的令牌或URL，以便从Web浏览器访问该笔记本。您可以从[AI开发者中心GitHub仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev)下载此笔记本。

### Step 2: 在容器中启动Jupyter Notebooks[#](#step-2-launch-jupyter-notebooks-in-the-container)

在Docker容器内，使用以下命令安装Jupyter：

```
安装 Jupyter
```

```

启动 Jupyter 服务器：

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

**注意**: 确保端口 `8888`

在运行上述命令之前，请确保该端口未被您的系统占用。如果已被占用，您可以通过将 `--port=8888` 替换为其他端口来指定不同的端口。

使用另一个端口号，例如 `--port=8890`

。

**注意**：本教程的其余部分可以在您将本教程上传到服务器后，作为Jupyter notebook中的交互式块运行。

### 步骤3：安装OpenAI Triton[#](#step-3-install-openai-triton)

在安装正确版本的OpenAI Triton之前，您必须卸载任何旧版本。

#### 1. 卸载旧版本的Triton[#](#uninstall-the-old-version-of-triton)

强烈建议你在项目中使用最新版本的Triton。AMD及其他供应商会频繁更新 [OpenAI Triton](https://github.com/triton-lang/triton) 中的优化过程和算法。这些更新能够提升你的Triton kernel性能。

```
!pip uninstall -y triton
```

```

#### 2. 从源码安装 OpenAI Triton[#](#install-openai-triton-from-the-source-code)

安装Triton的详细步骤如下所示。

**注意：** 如果在构建Triton时遇到任何问题或疑问，请提交到[Triton Issues](https://github.com/triton-lang/triton/issues)。

```bash
%%bash
# 如果存在现有的Triton文件夹，则移除它
if [ -d "triton" ]; then
echo "正在移除现有的triton目录..."
rm -rf triton
fi
# 克隆Triton仓库
git clone https://github.com/triton-lang/triton.git
# 安装依赖并从源码安装Triton（非可编辑安装）
cd triton
pip install -r python/requirements.txt
pip install .
```

```

### 第4步：在 AMD GPU 上验证 Triton[#](#step-4-validate-triton-on-an-amd-gpu)

在成功安装Triton后，验证它是否能在AMD GPU上正常工作。运行以下Python向量加法示例，确认Triton内核提供与Torch API相似的结果，这意味着它在AMD GPU上高效运行。

```
import torch
import triton
import triton.language as tl
DEVICE = triton.runtime.driver.active.get_active_torch_device()
@triton.jit
def add_kernel(x_ptr,  # *指针*，指向第一个输入向量。
                y_ptr,  # *指针*，指向第二个输入向量。
                output_ptr,  # *指针*，指向输出向量。
                n_elements,  # 向量的大小。
                BLOCK_SIZE: tl.constexpr,  # 每个程序应处理的元素数量。
                # 注意：`constexpr` 表示它可以用作形状值。
                ):
    # 有多个“程序”处理不同的数据。我们在此标识当前程序：    
    pid = tl.program_id(axis=0)  # 我们使用一维启动网格，因此轴为0。
    # 该程序将处理从初始数据偏移的输入。
    # 例如，如果你有一个长度为256的向量，块大小为64，各个程序将分别访问元素
    # [0:64, 64:128, 128:192, 192:256]。
    # 注意：offsets是指针列表：
    block_start = pid * BLOCK_SIZE
    offsets = block_start + tl.arange(0, BLOCK_SIZE)
    # 创建一个掩码，以防止内存操作访问越界。
    mask = offsets < n_elements
    # 从DRAM加载x和y，如果输入不是块大小的整数倍，则屏蔽多余的元素。
    x = tl.load(x_ptr + offsets, mask=mask)
    y = tl.load(y_ptr + offsets, mask=mask)
    output = x + y
    # 将 x + y 写回 DRAM。
    tl.store(output_ptr + offsets, output, mask=mask)

# %%
# 让我们还声明一个辅助函数，用于（1）分配 `z` 张量
# 和（2）使用适当的网格/块大小将上述内核加入队列：
def add(x: torch.Tensor, y: torch.Tensor):
    # 我们需要预先分配输出。
    output = torch.empty_like(x)
    assert x.device == DEVICE and y.device == DEVICE and output.device == DEVICE
    n_elements = output.numel()
    # SPMD启动网格表示并行运行的内核实例数量。
    # 类似于CUDA（统一计算设备架构）的启动网格。它可以是 Tuple[int] 或 Callable(metaparameters) -> Tuple[int]。
    # 这里我们使用一维网格，其大小为块的数量：
    grid = lambda meta: (triton.cdiv(n_elements, meta['BLOCK_SIZE']), )
    # 注意：
    # - 每个 torch.tensor 对象会被隐式转换为指向其第一个元素的指针。
    # - 带有 `triton.jit` 装饰的函数可以通过启动网格进行索引，从而得到一个可调用的GPU内核。
    # - 不要忘记将元参数作为关键字参数传递。
    add_kernel[grid](x, y, output, n_elements, BLOCK_SIZE=1024)
    # 我们返回z的句柄，但由于尚未调用 `torch.cuda.synchronize()`，此时内核仍在异步运行。
    return output

# %%
# 我们现在可以使用上面的函数来计算两个 `torch.tensor` 对象的逐元素和，并测试其正确性：
torch.manual_seed(0)
size = 98432
x = torch.rand(size, device=DEVICE)
y = torch.rand(size, device=DEVICE)
output_torch = x + y
output_triton = add(x, y)
print(output_torch)
print(output_triton)
print(f'torch与triton之间的最大差值为 '
      f'{torch.max(torch.abs(output_torch - output_triton))}')
```

```

输出日志为：

## 优化AMD GPU上的Triton代码[#](#optimize-the-triton-code-for-amd-gpus)

softmax函数常用于卷积神经网络（CNN）分类模型，甚至基于Transformer的大语言模型（LLM）中。它通过将每个原始输出分数（即logits）取指数，再除以所有指数值之和进行归一化，将其转换为概率。这个过程确保输出值在(0,1)范围内且总和为1，从而可以将其解释为概率。PyTorch将该函数实现为[标准API](https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html)。

### 朴素版本[#](#naive-version)

根据规格，你在Triton内核中实现了softmax算法的朴素版本。该内核版本使用两个for循环来确定最大数据点和所有指数的对应和，再加上一个for循环来计算最终的softmax结果，总共三个循环。

以下示例测试了一个 8192 x 8192 张量上的内核性能，其中列维度的块大小为 256。运行预热部分以避免将内核编译时间包含在最终数据中后，你可以获得朴素版本的性能数据。

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
)# 预热
torch.cuda.empty_cache() # 清理缓存
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
print(f'Softmax Triton 简单版耗时：{elapsed_time_ms:.3f}ms')
```

```

### 在线 softmax 版本[#](#online-softmax-version)

使用Triton语言实现算法非常容易。为了从当前内核中获得更优性能，首先判断是否存在更高效的算法或解决方案。若有，则在你的Triton内核函数（Kernel）中尝试新算法。为减少朴素softmax算法中三个for循环导致的内存访问，[Online normalizer calculation for softmax](https://arxiv.org/pdf/1805.02867)论文提出了一种新的在线softmax算法。

根据在线softmax算法，对朴素版本内核进行了以下少量修改。

```
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
)#预热
torch.cuda.empty_cache() #清理缓存
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

### 融合softmax版本[#](#fused-softmax-version)

OpenAI Triton 提供了“fused-softmax” softmax 参考示例。该示例基于在线 softmax 算法，通过移除一个 for 循环进一步简化了最大值数据的计算。它还通过增加 warp 数量，告知编译器为每行分配更多线程。这一配置通常针对性能进行调优。最后，通过调整 GPU 硬件配置改进了内核启动方案，从而可能实现更高的 GPU 内核占用率与更佳性能。

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
        # stride 表示需要增加多少个指针才能前进 1 行
        row_start_ptr = input_ptr + row_idx * input_row_stride
        # 块大小是大于 n_cols 的下一个 2 的幂，以便每行可以放在一个块中
        col_offsets = tl.arange(0, BLOCK_SIZE)
        input_ptrs = row_start_ptr + col_offsets
        # 将行加载到 SRAM 中，使用掩码，因为 BLOCK_SIZE 可能大于 n_cols
        mask = col_offsets < n_cols
        row = tl.load(input_ptrs, mask=mask, other=-float('inf'))
        # 减去最大值以保证数值稳定性
        row_minus_max = row - tl.max(row, axis=0)
        # 注意：Triton 中的指数运算速度快但近似（即，类似于 CUDA 中的 __expf）
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
# 每个循环迭代的块大小是大于 x 列数的最小 2 的幂
BLOCK_SIZE = triton.next_power_of_2(n_cols)
# 另一个技巧是要求编译器通过增加每行分布的 warp 数量（`num_warps`）来使用更多线程
num_warps = 8
# 软件流水线阶段数。
num_stages = 4 if SIZE_SMEM > 200000 else 2
# 预编译核函数以获取寄存器使用情况并计算线程占用率。
kernel = softmax_kernel.warmup(y, x, x.stride(0), y.stride(0), n_rows, n_cols, BLOCK_SIZE=BLOCK_SIZE,
                               num_stages=num_stages, num_warps=num_warps, grid=(1, ))
kernel._init_handles()
n_regs = kernel.n_regs
size_smem = kernel.metadata.shared
if is_hip():
    # NUM_REGS 表示通用寄存器的数量。在 CDNA 架构上，这仅是所有可用寄存器的一半。
    # 但情况并非总是如此。大多数情况下，所有寄存器都可以用作通用寄存器。
    # ISA 部分（针对 CDNA3 的 3.6.4）
    # VGPR 从两个池中分配：常规 VGPR 和累加 VGPR。累加 VGPR 用于矩阵 VALU 指令，
    # 也可以直接从内存加载。一个波前最多可以有 512 个 VGPR，每种类型 256 个。当一个波前
    # 的总 VGPR 少于 512 时，每种类型的数量是灵活的——两种类型不必相等。
    if is_cdna():
        NUM_GPRS = NUM_REGS * 2
    # MAX_NUM_THREADS 表示每个多处理器上最多可驻留的线程数。
    # 将其除以 WARP_SIZE 即可得到可以在一个 CU（多处理器）上并行执行的波前数。
    MAX_NUM_THREADS = properties["max_threads_per_sm"]
    max_num_waves = MAX_NUM_THREADS // WARP_SIZE
    occupancy = min(NUM_GPRS // WARP_SIZE // n_regs, max_num_waves) // num_warps
else:
    occupancy = NUM_REGS // (n_regs * WARP_SIZE * num_warps)
occupancy = min(occupancy, SIZE_SMEM // size_smem)
num_programs = NUM_SM * occupancy
num_programs = min(num_programs, n_rows)
# 创建一定数量的持久程序。
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

在本教程中，您学习了如何在 AMD GPU 上开发和优化 Triton 内核。要了解更多关于 OpenAI Triton 的信息，请参阅 [官方 Triton 文档](https://triton-lang.org/main/index.html)。要了解有关在 AMD GPU 上运行 Triton 的更多信息，请参见 [ROCm（Radeon 开放计算平台） Triton 优化](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/optimizing-triton-kernel.html) 以及 [Triton 上的内核函数开发优化博客](https://rocm.blogs.amd.com/software-tools-optimization/kernel-development-optimizations-with-triton-on-/README.html)。希望本教程能鼓励您在 AMD GPU 上对 Triton 进行调优、测试和贡献，并助力塑造 AI 加速的未来。