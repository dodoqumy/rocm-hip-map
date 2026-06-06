---
title: "Helion DSL for GPU kernel development and assessment on AMD GPUs &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/gpu_dev_optimize/helion_gpu_kernel_dev.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:31.961893+00:00
content_hash: "40355c33308cf7ad"
---

# Helion DSL：用于AMD GPU上的GPU内核开发与评估[#](#helion-dsl-for-gpu-kernel-development-and-assessment-on-amd-gpus)

**作者**：Charles Yang

**知识水平**：中级

[Helion](https://github.com/pytorch/helion) 是 Meta 开发的一种 Python 嵌入式领域特定语言（DSL），用于编写机器学习内核。它向下编译至 [Triton](https://openai.com/index/triton/)，即 OpenAI 为 GPU 及其他设备编程提供的高性能后端。与 Triton 相比，Helion 旨在提升抽象层级，使编写正确且高效的内核更为简便，同时支持自动调优过程中更高程度的自动化。

Helion既可被视为带有tiles的PyTorch，也可被视为更高级别的Triton应用。与Triton相比，Helion通过自动调优减少了手动编码的工作量。Helion花费更多时间（约10分钟）进行自动调优，因为它会评估从单个Helion内核生成的数百个潜在的Triton实现。更大的搜索空间也使得内核在不同硬件之间具有更好的性能可移植性。

Helion 获得 AMD GPU 的支持。本教程演示如何设置 Helion 开发环境、实现 Helion 内核，并在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPU 上使用 Triton 和 Torch 进行性能基准测试。

## Helion 自动调优器[#](#the-helion-autotuner)

Helion 的关键区别在于其自动化的提前（AOT）自动调优引擎。在 Triton 中，开发者需要手动定义优化的搜索空间，即显式枚举每一个待测试的配置——这是一个繁琐的过程，限制了探索的范围。

Helion通过使用隐式搜索空间改变了这一动态。高级语言自动构建一个涵盖实现选择的庞大、多维搜索空间。例如，单个`hl.tile`

`call` 隐式指示自动调优器探索不同的块大小和循环顺序，并考虑是否将迭代空间扁平化为单一维度。因此，一个 Helion 内核定义可以映射到数千个 Triton 配置，使得自动调优器能够创建更大、更丰富的搜索空间，以发现更优的配置。

## 教程工作流程[#](#tutorial-workflow)

本教程包含以下内容：

## 前提条件[#](#prerequisites)

本教程使用以下设置进行开发和测试。

### 操作系统[#](#operating-system)

**Ubuntu 22.04/24.04**：确保你的系统运行的是 Ubuntu 22.04 或 24.04。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU**：本教程在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 上进行了测试。请确保您使用的是支持 ROCm（ROCm（Radeon 开放计算平台））的 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 7.0**：按照 [ROCm（ROCm（Radeon 开放计算平台）） 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm（ROCm（Radeon 开放计算平台））。安装完成后，使用以下命令确认您的设置：此命令将列出您的 AMD GPU 及相关详细信息。

**注意**：对于 ROCm 6.4 及更早版本，请使用 `rocm-smi`。

命令取代。AMD还提供预构建的ROCm（ROCm（Radeon 开放计算平台））Docker镜像，包括一个

[ROCm（ROCm（Radeon 开放计算平台）） PyTorch 镜像](https://hub.docker.com/r/rocm/pytorch)、[ROCm（ROCm（Radeon 开放计算平台）） Ubuntu 22.04 镜像](https://hub.docker.com/r/rocm/dev-ubuntu-22.04)以及 [ROCm（ROCm（Radeon 开放计算平台）） Ubuntu 24.04 镜像](https://hub.docker.com/r/rocm/dev-ubuntu-24.04)。您可以使用这些预构建的 Docker 镜像来减少设置 ROCm（ROCm（Radeon 开放计算平台））环境所需的工作量。  

**Docker**：确保 Docker 已正确安装和配置。请根据您的操作系统参考 Docker 安装指南。  

**注意**：确保 Docker 权限已正确配置。要配置允许非 root 用户访问的权限，请运行以下命令：  
```bash
usermod -aG docker $USER
newgrp docker
```

验证Docker是否正确运行：

运行 hello-world

### Hugging Face API 访问[#](#hugging-face-api-access)

从...获取 API token

[Hugging Face](https://huggingface.co) 用于下载模型。确保 Hugging Face API 令牌具有必要的权限。

## 1. 使用 Docker 和 ROCm 的环境设置（ROCm（Radeon 开放计算平台））[#](#environment-setup-with-docker-and-rocm)

按照以下步骤设置环境、启动 Jupyter Notebooks 并安装依赖项。

### 启动 Docker 容器[#](#launch-the-docker-container)

启动 Docker 容器。从你的宿主机上，运行以下命令：

```
run -it --rm \
--privileged \
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
rocm/pytorch:latest bash
```

```

**注意**：此命令将当前目录挂载到 `/workspace`

容器中的目录。确保在运行 Docker 命令之前将 notebook 文件复制到此目录，或在容器启动后将其上传到 Jupyter Notebook 环境中。保存终端输出中提供的令牌或 URL，以便从 Web 浏览器访问 notebook。您可以从 [AI Developer Hub GitHub 仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev) 下载此 notebook。

### 在容器中启动 Jupyter Notebooks[#](#launch-jupyter-notebooks-in-the-container)

在Docker容器中，使用以下命令安装Jupyter：

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

在运行上述命令之前，请确保该端口尚未在你的系统上被使用。如果已被占用，你可以通过替换 `--port=8888` 来指定不同的端口。

使用另一个端口号，例如 `--port=8890`

.

### 安装 Helion 与 Triton[#](#install-helion-and-triton)

强烈建议在您的项目中使用最新版本的Helion。AMD和其他供应商会频繁更新[Helion](https://github.com/pytorch/helion)中的优化遍和算法，这有助于提升您的Helion内核性能。

#### 卸载旧版本的Helion和Triton[#](#uninstall-older-versions-of-helion-and-triton)

首先，卸载任何现有版本的 Helion 和 Triton：

```
!pip uninstall -y helion triton```

```

#### 安装 Helion 和 Triton[#](#id1)

使用以下命令安装 Helion、Triton 及其他依赖项。

```
%%bash
pip install triton==3.5.1
pip install helion==0.2.6
pip install matplotlib
pip list | grep -E 'helion|triton|torch'
# 忽略不兼容性错误。它不影响本笔记本中示例的执行。
# 查找字符串 'Successfully installed triton-xxx' 以确认 Triton 已成功安装。
```

```

## 2. Helion GPU 内核示例[#](#helion-gpu-kernel-example)

本示例演示了如何使用 Helion 实现逐元素的指数（exp）函数。它利用 Helion 的分块（tiling）系统进行并行计算，同时支持前向传播和反向传播。该实现与 PyTorch 自动求导系统无缝集成，可实现高性能、可自动求导的操作。示例展示了如何通过完整的梯度支持，对比原生 PyTorch 指数函数来验证该实现。

```python
import torch
import helion
from helion._testing import DEVICE
from helion._testing import run_example
import helion.language as hl

@helion.kernel()
def exp_fwd(x: torch.Tensor) -> torch.Tensor:
    """
    计算输入张量中所有元素的指数。

    参数：
        x: 输入张量

    返回：
        输出张量，包含输入中每个元素的指数值
    """
    out = torch.empty_like(x)
    for tile in hl.tile(x.size()):
        out[tile] = torch.exp(x[tile])
    return out

# %%
@helion.kernel()
def exp_bwd(dy: torch.Tensor, exp_x: torch.Tensor) -> torch.Tensor:
    """
    计算指数函数相对于输入张量的梯度。

    参数：
        dy: 输出张量的梯度
        exp_x: 前向传播保存的激活值

    返回：
        输入张量的梯度
    """
    dx = torch.empty_like(exp_x)
    for tile in hl.tile(exp_x.size()):
        dx[tile] = dy[tile] * exp_x[tile]
    return dx
```

```

下一个单元格定义了 exp 核函数的封装类。

```
# %%
class ExpFunction(torch.autograd.Function):
@staticmethod
def forward(
ctx: object,
x: torch.Tensor,
) -> torch.Tensor:
"""exp的前向传播。"""
y = exp_fwd(x)
ctx.save_for_backward(y) # type: ignore[arg-type]
return y
@staticmethod
def backward( # type: ignore[override]
ctx: object,
grad_output: torch.Tensor,
) -> torch.Tensor:
"""exp的反向传播。"""
(x,) = ctx.saved_tensors # type: ignore[attr-defined]
return exp_bwd(grad_output, x)
```

```

验证 exp 内核实现与 PyTorch 的原生 `exp`

函数。

```
# %%
def exp(x: torch.Tensor) -> torch.Tensor:
    """
    支持前向和反向传播的指数函数。

    参数:
        x: 输入张量

    返回:
        输出张量，包含输入中每个元素的指数值
    """
    return ExpFunction.apply(x)  # type: ignore[no-any-return]

# %%
def check(n: int) -> None:
    """
    验证指数函数内核实现与PyTorch原生exp函数的一致性。

    参数:
        n: 测试张量的大小
    """
    x = torch.randn(n, device=DEVICE, dtype=torch.float32, requires_grad=True)
    run_example(exp, torch.exp, (x,), bwd=True)

check(1024 * 1024)
```

```

## 3. softmax算法细节[#](#details-of-the-softmax-algorithm)

softmax函数常用于分类CNN模型乃至基于transformer的LLM模型。它将原始输出分数（即logits）转换为概率，通过对每个值求指数并除以所有指数的总和进行归一化。此过程确保输出值在(0,1)范围内且总和为1，从而可以将其解释为概率。PyTorch已将softmax函数实现为[标准API](https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html)。

函数 \(y = Softmax(x)\) 的定义为：

其中 \(x,y \in \mathbb{R}^V\).

### 朴素版本: Safe Softmax[#](#naive-version-safe-softmax)

为了实现数值稳定性，在计算指数之前，从每个输入元素中减去行向量的最大值。因此定义变为：

其中 \(x,y \in \mathbb{R}^V\)。这被称为 Safe Softmax 算法。

根据 softmax 算法定义，Triton 内核实现了朴素版本（公式 2）。该内核需要两个 for 循环来获取最大数据以及所有指数之和，并额外需要一个 for 循环来计算最终 softmax 结果，因此总共使用了三个循环。Safe Softmax 算法在 [Online normalizer calculation for softmax](https://arxiv.org/pdf/1805.02867) 中有更完整的描述。

此kernel在8192x8192张量上的性能计算如下：

该块的块大小

列

维度是256。每个输入张量的行分配一个程序。这意味着网格大小为

`n_rows`

，其中`n_rows`

等于输入张量的行数。程序实例（线程块）扫描张量的一行，并迭代处理当前行的数据块，以计算当前行的最大值 \(m_k\)。这是第一个 for 循环。

程序实例（线程块）扫描张量的一行，并迭代处理当前行的数据块，以计算当前行的分母（指数和）值 \(d_j\)。这是第二个 for 循环。

程序实例（线程块）扫描张量的一行，并迭代处理当前行的数据块，以计算当前行的最终softmax值 \(y_i\)。这是第三个for循环。

## 4. 创建Helion双通softmax kernel[#](#creating-a-helion-two-pass-softmax-kernel)

这个示例展示了softmax函数的多个Helion kernel实现，包括一个对PyTorch softmax实现的简单封装，以及一个数值优化后的两遍版本。它还包含一个检查函数，用于将这些kernel与内置的PyTorch softmax函数进行比较，以验证正确性。

```
import os
import random
import torch
import helion
from helion._testing import run_example
import helion.language as hl
SEED = 42
os.environ["PYTHONHASHSEED"] = str(SEED)
random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
# %%
@helion.kernel(autotune_effort="quick")
def softmax_two_pass(x: torch.Tensor) -> torch.Tensor:
"""
数值优化的Helion内核，通过两次遍历执行softmax。

参数：
    x (torch.Tensor): 输入张量，形状为 [m, n]。
返回：
    torch.Tensor: 形状相同的softmax输出张量。
"""
m, n = x.size()
out = torch.empty_like(x)
block_size_m = hl.register_block_size(m)
block_size_n = hl.register_block_size(n)
for tile_m in hl.tile(m, block_size=block_size_m):
mi = hl.full([tile_m], float("-inf"), dtype=torch.float32)
di = hl.zeros([tile_m], dtype=torch.float32)
for tile_n in hl.tile(n, block_size=block_size_n):
values = x[tile_m, tile_n]
local_amax = torch.amax(values, dim=1)
mi_next = torch.maximum(mi, local_amax)
di = di * torch.exp(mi - mi_next) + torch.exp(
values - mi_next[:, None]
).sum(dim=1)
mi = mi_next
for tile_n in hl.tile(n, block_size=block_size_n):
values = x[tile_m, tile_n]
out[tile_m, tile_n] = torch.exp(values - mi[:, None]) / di[:, None]
return out
```

```

通过将 Helion softmax 内核与 PyTorch softmax 函数进行比较来检查正确性。

```
# %%
def check(m: int, n: int) -> None:
"""
运行正确性检查，比较 Helion softmax 内核与 PyTorch 的 softmax。
参数：
m (int): 输入张量的行数。
n (int): 输入张量的列数。
"""
x = torch.randn([m, n], device="cuda", dtype=torch.float16)
run_example(softmax_two_pass, lambda x: torch.nn.functional.softmax(x, dim=1), (x,))
# %%
def main() -> None:
"""
主函数，使用示例输入大小运行 softmax 内核正确性检查。
"""
check(4096, 2560)
# %%
if __name__ == "__main__":
main()
```

```

## 5. 性能基准测试与可视化[#](#performance-benchmark-and-visualization)

本节将Helion与Triton、PyTorch和Aiter进行性能对比。

### 对照组: Triton fused-softmax 和 Aiter softmax[#](#control-group-triton-fused-softmax-and-aiter-softmax)

此示例演示如何使用 Triton 实现一个融合的 softmax 内核，并具有对基于 CDNA（计算 DNA 架构）后端的 AMD ROCm（Radeon 开放计算平台）的架构感知能力。

#### Triton融合softmax的实现[#](#implementation-of-triton-fused-softmax)

Triton提供了一个名为`fused-softmax`的参考softmax示例。

基于在线 softmax，它简化了最大值数据的计算，从而移除一个 for 循环。它还通过增加 warp 数量来要求编译器每行使用更多线程。这通常是为了优化性能而调整。最后，它根据 GPU 硬件属性确定 kernel 启动方案，从而实现更高的 GPU kernel 占用率和更好的性能。

```
import os
import random
import torch
import triton
import triton.language as tl
from triton.runtime import driver
DEVICE = triton.runtime.driver.active.get_active_torch_device()
SEED = 42
os.environ["PYTHONHASHSEED"] = str(SEED)
random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
def is_hip():
return triton.runtime.driver.active.get_current_target().backend == "hip"
def is_cdna():
return is_hip() and triton.runtime.driver.active.get_current_target().arch in ('gfx940', 'gfx941', 'gfx942',
'gfx90a', 'gfx908', 'gfx950')
@triton.jit
def fused_softmax_kernel(output_ptr, input_ptr, input_row_stride, output_row_stride, n_rows, n_cols, BLOCK_SIZE: tl.constexpr,
num_stages: tl.constexpr):
# 当前程序行的起始位置
row_start = tl.program_id(0)
row_step = tl.num_programs(0)
for row_idx in tl.range(row_start, n_rows, row_step, num_stages=num_stages):
# 步长表示为了前进一行需要增加指针的量
row_start_ptr = input_ptr + row_idx * input_row_stride
# 块大小是大于 n_cols 的下一个2的幂，以便每行都能放入一个块中
col_offsets = tl.arange(0, BLOCK_SIZE)
input_ptrs = row_start_ptr + col_offsets
# 将行加载到 SRAM 中，使用掩码因为 BLOCK_SIZE 可能大于 n_cols
mask = col_offsets < n_cols
row = tl.load(input_ptrs, mask=mask, other=-float('inf'))
# 减去最大值以获得数值稳定性
row_minus_max = row - tl.max(row, axis=0)
# 注意：Triton 中的指数运算快速但近似（即考虑 CUDA 中的 __expf）
numerator = tl.exp(row_minus_max)
denominator = tl.sum(numerator, axis=0)
softmax_output = numerator / denominator
# 将输出写回 DRAM
output_row_start_ptr = output_ptr + row_idx * output_row_stride
output_ptrs = output_row_start_ptr + col_offsets
tl.store(output_ptrs, softmax_output, mask=mask)
```

```

根据目标 GPU 平台的属性调整内核。

```
# 为了调优内核，首先通过以下操作获取 GPU 的一些资源属性：
properties = driver.active.utils.get_device_properties(DEVICE.index)
NUM_SM = properties["multiprocessor_count"]
NUM_REGS = properties["max_num_regs"]
SIZE_SMEM = properties["max_shared_mem"]
WARP_SIZE = properties["warpSize"]
target = triton.runtime.driver.active.get_current_target()
kernels = {}
print(f"NUM_SM: {NUM_SM}, NUM_REGS: {NUM_REGS}, SIZE_SMEM: {SIZE_SMEM}, WARP_SIZE: {WARP_SIZE}, target: {target}")
# 然后设置内核启动配置
torch.manual_seed(0)
x = torch.randn(8192, 8192, device=DEVICE)
output_torch = torch.softmax(x, dim=-1)
n_rows, n_cols = x.shape
# 分配输出
y = torch.empty_like(x)
# 每次循环迭代的块大小是大于 `x` 列数的2的最小幂
BLOCK_SIZE = triton.next_power_of_2(n_cols*2)
# 另一个技巧是让编译器每行使用更多线程，通过增加分配给每行的 warp 数量（`num_warps`）
num_warps = 8
# 软件流水线阶段数
num_stages = 4 if SIZE_SMEM > 200000 else 2
print(f"BLOCK_SIZE: {BLOCK_SIZE}, num_warps: {num_warps}, num_stages: {num_stages}")
# 内核占用率受限于寄存器使用。为最大化占用率，预热内核以获取寄存器使用情况，并计算合适的程序数量。
# 预编译内核以获取寄存器使用情况并计算线程占用率
kernel = fused_softmax_kernel.warmup(y, x, x.stride(0), y.stride(0), n_rows, n_cols, BLOCK_SIZE=BLOCK_SIZE,
num_stages=num_stages, num_warps=num_warps, grid=(1, ))
kernel._init_handles()
n_regs = kernel.n_regs
size_smem = kernel.metadata.shared
if is_hip():
if is_cdna():
NUM_GPRS = NUM_REGS * 2
MAX_NUM_THREADS = properties["max_threads_per_sm"]
max_num_waves = MAX_NUM_THREADS // WARP_SIZE
occupancy = min(NUM_GPRS // WARP_SIZE // n_regs, max_num_waves) // num_warps
else:
occupancy = NUM_REGS // (n_regs * WARP_SIZE * num_warps)
occupancy = min(occupancy, SIZE_SMEM // size_smem)
num_programs = NUM_SM * occupancy
num_programs = min(num_programs, n_rows)
print(f"n_regs: {n_regs}, size_smem: {size_smem}, occupancy: {occupancy}, num_programs: {num_programs}")
```

```

#### 安装 ROCm Aiter 内核库[#](#install-the-rocm-aiter-kernel-library)

使用以下命令安装内置softmax内核函数的Aiter内核库：

```
%%bash
git clone --recursive https://github.com/ROCm（ROCm（Radeon 开放计算平台））/aiter.git
cd aiter
python3 setup.py develop
```

```

## 运行基准测试与可视化[#](#run-the-benchmark-and-visualization)

现在对softmax内核的所有版本运行基准测试和可视化以获取结果。

```python
import os
import torch
import torch.nn.functional as F
import triton
import random
import triton.language as tl
import matplotlib.pyplot as plt
DEVICE = triton.runtime.driver.active.get_active_torch_device()
SEED = 42
os.environ["PYTHONHASHSEED"] = str(SEED)
random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
# --- Helion Softmax ---
def softmax_helion(x: torch.Tensor, dim=-1):
    helion_output = softmax_two_pass(x)
    return helion_output
# --- 辅助运行 Triton 自动调优 ---
def softmax_triton(x: torch.Tensor):
    n_rows, n_cols = x.shape
    triton_output = torch.empty_like(x)
    kernel[(num_programs, 1, 1)](
        y,
        x,
        x.stride(0),
        y.stride(0),
        n_rows,
        n_cols,
        BLOCK_SIZE,
        num_stages)
    return triton_output
# --- PyTorch 原生 Softmax ---
def softmax_torch(x: torch.Tensor, dim=-1):
    """
    使用 PyTorch 内置函数计算 softmax。
    输出与输入形状相同。
    """
    torch_output = F.softmax(x, dim=dim)
    return torch_output
# --- Aiter Softmax ---
from aiter.ops.triton.softmax import softmax
def softmax_aiter(x: torch.Tensor):
    aiter_output = softmax(x)
    return aiter_output
# --- Triton 基准测试 ---
@triton.testing.perf_report(
    triton.testing.Benchmark(
        x_names=['N'], # 用作图表 x 轴的参数名
        x_vals=[128 * i for i in range(55, 95)], # `x_name` 的不同可能值
        line_arg='provider', # 参数名，其值对应图表中的不同线条
        line_vals=['helion', 'triton', 'aiter', 'torch'], # `line_arg` 的可能值
        line_names=["Helion Softmax", "Triton Softmax", "Aiter Softmax", "Torch Softmax"], # 线条的标签名
        styles=[('red', 'solid'), ('cyan', 'solid'), ('black', 'solid'), ('orange', 'dashdot')], # 线条样式
        ylabel="GB/s", # y 轴标签名
        plot_name="Softmax 性能基准测试", # 图表名称。也用作保存图表的文件名。
        args={'M': 4096}, # 不在 `x_names` 和 `y_name` 中的函数参数的值
    ))
def benchmark(M, N, provider):
    # x = torch.randn(M, N, device=DEVICE, dtype=torch.float32)
    gen = torch.Generator(device=DEVICE).manual_seed(SEED)
    x = torch.randn(M, N, device=DEVICE, dtype=torch.float32, generator=gen)
    quantiles = [0.5, 0.2, 0.8]
    if provider == 'torch':
        ms, min_ms, max_ms = triton.testing.do_bench(
            lambda: torch.softmax(x, dim=-1), rep=10, quantiles=quantiles
        )
    elif provider == 'aiter':
        ms, min_ms, max_ms = triton.testing.do_bench(
            lambda: softmax_aiter(x), rep=10, quantiles=quantiles
        )
    elif provider == 'triton':
        ms, min_ms, max_ms = triton.testing.do_bench(
            lambda: softmax_triton(x), rep=10, quantiles=quantiles
        )
    elif provider == 'helion':
        ms, min_ms, max_ms = triton.testing.do_bench(
            lambda: softmax_helion(x), rep=10, quantiles=quantiles
        )
    # 计算带宽：2 * (读 + 写) * 大小 / 时间
    gbps = lambda ms: 2 * x.numel() * x.element_size() * 1e-9 / (ms * 1e-3)
    return gbps(ms)
# --- 运行基准测试 ---
benchmark.run(show_plots=True, print_data=True)
```

```

## 概述[#](#summary)

恭喜！通过运行本Helion GPU内核开发教程，您学会了如何在AMD GPU上开发和优化Helion内核。

根据最终性能基准测试结果，Helion不仅简化了高性能GPU内核的开发，还提供了接近最优的性能，甚至超越了基于Triton的GPU内核。

理想情况下，本教程鼓励您在 ROCm（Radeon 开放计算平台）和 AMD GPU 上编写、调优、测试并贡献 Helion 内核，从而帮助塑造人工智能加速的未来。