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

# Helion DSL 用于在AMD GPU上进行GPU内核开发与评估

**作者**: Charles Yang

**知识水平**：中级

[Helion](https://github.com/pytorch/helion) 是 Meta 推出的一个嵌入 Python 的领域特定语言（DSL），用于编写机器学习内核。它编译为 [Triton](https://openai.com/index/triton/)，后者是 OpenAI 提供的用于 GPU 及其他设备编程的高性能后端。Helion 旨在相比 Triton 提升抽象层次，简化正确且高效内核的编写，同时使自动调优过程能实现更大程度的自动化。

Helion既可以看作是带有tiles的PyTorch，也可以看作是更高层次的Triton应用。与Triton相比，Helion通过自动调优减少了手动编码的工作量。Helion在自动调优上花费更多时间（约10分钟），因为它需要评估从单个Helion kernel生成的数百个潜在的Triton实现。这种更大的搜索空间也使得kernel在不同硬件之间具有更好的性能可移植性。

Helion 由 AMD GPU 支持。本教程演示了如何在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPU 上搭建 Helion 开发环境、实现 Helion 内核，并使用 Triton 和 Torch 进行性能基准测试。

## Helion自动调优器[#](#the-helion-autotuner)

Helion的关键区别在于其自动化的提前编译（AOT）自动调优引擎。在Triton中，开发者需要手动定义优化的搜索空间。这要求显式列举所有待测试的配置，这一繁琐的过程限制了探索的范围。

Helion 通过使用隐式搜索空间改变了这一动态。高层语言自动构建了一个覆盖实现选择的巨大多维搜索空间。例如，单个 `hl.tile`

该调用隐式地指导自动调优器探索不同的块大小和循环顺序，并考虑是否将迭代空间展平为一维。一个Helion内核定义因此可以映射到数千个Triton配置，从而允许自动调优器创建一个更大、更丰富的搜索空间，以发现更优的配置。

## 教程工作流程[#](#tutorial-workflow)

此教程包含以下内容：

## 前提条件[#](#prerequisites)

本教程使用以下环境进行开发和测试。

### 操作系统[#](#operating-system)

**Ubuntu 22.04/24.04**：确保您的系统正在运行 Ubuntu 22.04 或 24.04。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU**: 本教程已在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 上测试。确保您使用的 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 支持 ROCm（ROCm（Radeon 开放计算平台）），并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 7.0**：按照 [ROCm（ROCm（Radeon 开放计算平台）） 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm（ROCm（Radeon 开放计算平台））。安装完成后，使用以下命令确认设置：该命令会列出您的 AMD GPU 及其相关详情。

**注意**：对于 ROCm（ROCm（Radeon 开放计算平台）） 6.4 及更早版本，请使用 `rocm-smi`

请改用命令。AMD 还提供了预构建的 ROCm（ROCm（Radeon 开放计算平台））Docker 镜像，包括一个

[ROCm（ROCm（Radeon 开放计算平台）） PyTorch 镜像](https://hub.docker.com/r/rocm/pytorch)，一个 [ROCm（ROCm（Radeon 开放计算平台）） Ubuntu 22.04 镜像](https://hub.docker.com/r/rocm/dev-ubuntu-22.04)，以及一个 [ROCm（ROCm（Radeon 开放计算平台）） Ubuntu 24.04 镜像](https://hub.docker.com/r/rocm/dev-ubuntu-24.04)。您可以使用这些预构建的 Docker 镜像，以减少搭建 ROCm（ROCm（Radeon 开放计算平台）） 环境所需的工作量。

**Docker**：确保 Docker 已正确安装和配置。请遵循适用于您操作系统的 Docker 安装指南。

**注意**：确保 Docker 权限配置正确。要配置权限以允许非 root 用户访问，请运行以下命令：

usermod -aG docker $USER
newgrp docker

验证Docker是否正常工作：

运行 hello-world

### Hugging Face API 访问[#](#hugging-face-api-access)

从...获取 API 令牌

[Hugging Face](https://huggingface.co) 用于下载模型。确保 Hugging Face API token 拥有必要的权限。

## 1. 使用 Docker 和 ROCm（ROCm（Radeon 开放计算平台））进行环境设置[#](#environment-setup-with-docker-and-rocm)

按照以下步骤设置环境、启动 Jupyter Notebooks 并安装依赖项。

### 启动 Docker 容器[#](#launch-the-docker-container)

启动Docker容器。从你的宿主机上，运行以下命令：

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

容器中的目录。请确保在运行 Docker 命令之前将笔记本文件复制到此目录，或者在 Jupyter Notebook 环境启动后将其上传。保存终端输出中提供的令牌或 URL，以便从 Web 浏览器访问笔记本。您可以从 [AI Developer Hub GitHub 仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev) 下载此笔记本。

### 在容器中启动 Jupyter Notebooks[#](#launch-jupyter-notebooks-in-the-container)

在 Docker 容器内，使用以下命令安装 Jupyter：

安装 Jupyter

```

启动 Jupyter 服务器：

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

**注意**：确保端口 `8888`

在运行上述命令之前，请确保该端口未在你的系统上被占用。如果已被占用，你可以通过替换 `--port=8888` 来指定一个不同的端口。

使用另一个端口号，例如 `--port=8890`

。

### 安装 Helion 和 Triton[#](#install-helion-and-triton)

强烈建议您在项目中使用最新版本的Helion。AMD和其他供应商会频繁更新[Helion](https://github.com/pytorch/helion)中的优化pass和算法，这有助于提升您的Helion内核性能。

#### 卸载旧版本的Helion和Triton[#](#uninstall-older-versions-of-helion-and-triton)

首先，卸载所有现有的Helion和Triton版本：

```
!pip uninstall -y helion triton
```

```

#### 安装 Helion 和 Triton[#](#id1)

使用以下命令安装 Helion、Triton 和其他依赖项。

```bash
%%bash
pip install triton==3.5.1
pip install helion==0.2.6
pip install matplotlib
pip list | grep -E 'helion|triton|torch'
# 忽略不兼容错误。它不影响本笔记本中示例的执行。
# 查找字符串 'Successfully installed triton-xxx' 以确认 Triton 安装成功。
```

```

## 2. Helion GPU内核示例[#](#helion-gpu-kernel-example)

该示例演示了如何使用Helion实现逐元素的指数（exp）函数。它通过Helion的并行计算分块系统同时支持前向与反向传播。该实现与PyTorch自动求导系统无缝集成，实现了高性能的自动可微操作。示例展示了如何对照原生PyTorch指数函数（含完整梯度支持）验证实现正确性。

```
import torch
import helion
from helion._testing import DEVICE
from helion._testing import run_example
import helion.language as hl
@helion.kernel()
def exp_fwd(x: torch.Tensor) -> torch.Tensor:
"""
计算输入张量中所有元素的指数。
参数:
    x: 输入张量
返回:
    输出张量，包含输入中每个元素的指数
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
参数:
    dy: 输出张量的梯度
    exp_x: 前向传播中保存的激活值
返回:
    输入张量的梯度
"""
dx = torch.empty_like(exp_x)
for tile in hl.tile(exp_x.size()):
dx[tile] = dy[tile] * exp_x[tile]
return dx
```

```

下一个单元格定义了 exp 内核函数的包装类。

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

对照 PyTorch 的原生 `exp` 验证 exp 内核实现

函数。

```
# %%
def exp(x: torch.Tensor) -> torch.Tensor:
"""
支持前向和反向传播的指数函数。
参数：
x: 输入张量
返回：
输出张量，包含输入中每个元素的指数值
"""
return ExpFunction.apply(x) # type: ignore[no-any-return]
# %%
def check(n: int) -> None:
"""
验证 exp 内核实现与 PyTorch 原生 exp 函数的一致性。
参数：
n: 测试张量的大小
"""
x = torch.randn(n, device=DEVICE, dtype=torch.float32, requires_grad=True)
run_example(exp, torch.exp, (x,), bwd=True)
check(1024 * 1024)
```

```

## 3. softmax 算法的细节[#](#details-of-the-softmax-algorithm)

softmax函数常用于分类CNN模型乃至基于transformer的LLM模型。它通过计算每个值的指数并除以所有指数之和，将原始输出分数（logits）转换为概率。这一过程确保输出值落在(0,1)区间内且总和为1，使其可解释为概率。PyTorch已将softmax函数实现为[标准API](https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html)。

函数 \(y = Softmax(x)\) 的定义为：

其中 \(x,y \in \mathbb{R}^V\)。

### 朴素版本：Safe Softmax[#](#naive-version-safe-softmax)

为了实现数值稳定性，在对每个输入元素取指数之前，先减去该行向量的最大值。因此定义变为：

其中 \(x,y \in \mathbb{R}^V\)。这就是所谓的 Safe Softmax 算法。

根据softmax算法定义，Triton内核实现了朴素版本（公式2）。该内核需要两个for循环来获取最大值数据以及所有指数项对应的和，另外还需要一个for循环来计算最终的softmax结果。因此总共使用了三个循环。Safe Softmax算法在《Online normalizer calculation for softmax》（https://arxiv.org/pdf/1805.02867）中有更详细的描述。

这个核函数在8192x8192张量上的性能计算如下：

该块的块大小

`列`

维度为256。每个程序分配到输入张量的一行。这意味着网格大小为

`n_rows`

，其中 `n_rows`

等于输入张量的行数。该程序实例（线程块）扫描张量的一行，并迭代处理当前行的数据块，以计算当前行的最大值 \(m_k\)。这是第一个for循环。

程序实例（线程块）扫描张量的一行，并迭代处理当前行的数据块，以计算当前行的分母（指数和）值 \(d_j\)。这是第二个 for 循环。

程序实例（线程块）扫描张量的一行，并迭代处理当前行的数据块，以计算当前行的最终softmax值 \(y_i\)。这是第三个for循环。

## 4. 创建Helion双遍softmax kernel[#](#creating-a-helion-two-pass-softmax-kernel)

此示例展示了 softmax 函数的多个 Helion 内核实现，包括一个围绕 PyTorch softmax 实现的简单包装器以及一个数值优化的两遍版本。它还包含一个检查函数，用于将这些内核与内置的 PyTorch softmax 函数进行比较，以验证正确性。

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
数值优化的Helion内核，通过两次遍历实现softmax。

参数:
x (torch.Tensor): 输入张量，形状为 [m, n]。

返回:
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

通过与 PyTorch softmax function 比较 Helion softmax kernels 来检查正确性。

```
# %%
def check(m: int, n: int) -> None:
"""
运行正确性检查，比较Helion softmax内核与PyTorch的softmax。
参数：
m (int): 输入张量的行数。
n (int): 输入张量的列数。
"""
x = torch.randn([m, n], device="cuda", dtype=torch.float16)
run_example(softmax_two_pass, lambda x: torch.nn.functional.softmax(x, dim=1), (x,))
# %%
def main() -> None:
"""
主函数，用于使用示例输入规模运行softmax内核正确性检查。
"""
check(4096, 2560)
# %%
if __name__ == "__main__":
main()
```

```

## 5. 性能基准测试与可视化[#](#performance-benchmark-and-visualization)

本节比较 Helion 与 Triton、PyTorch 和 Aiter 的性能。

### 控制组：Triton fused-softmax 和 Aiter softmax[#](#control-group-triton-fused-softmax-and-aiter-softmax)

此示例演示了如何使用 Triton 实现融合 softmax 内核，并对基于 CDNA（CDNA（计算 DNA 架构））的 AMD ROCm（ROCm（Radeon 开放计算平台））后端具有架构感知。

#### 实现Triton fused-softmax[#](#implementation-of-triton-fused-softmax)

Triton 提供了一个名为 `fused-softmax` 的参考 softmax 示例

基于在线softmax，它简化了最大数据计算，省去一个for循环。同时通过增加warp数量，让编译器为每行使用更多线程。这通常经过调优以提升性能。最终，内核启动方案基于GPU硬件属性设计，从而获得更高的GPU内核占用率和更佳性能。

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
# 程序的起始行
row_start = tl.program_id(0)
row_step = tl.num_programs(0)
for row_idx in tl.range(row_start, n_rows, row_step, num_stages=num_stages):
# 步长表示我们需要增加多少指针才能前进1行
row_start_ptr = input_ptr + row_idx * input_row_stride
# 块大小是大于 n_cols 的下一个2的幂，这样每行可以放一个块
col_offsets = tl.arange(0, BLOCK_SIZE)
input_ptrs = row_start_ptr + col_offsets
# 将行加载到 SRAM 中，由于 BLOCK_SIZE 可能大于 n_cols，使用掩码
mask = col_offsets < n_cols
row = tl.load(input_ptrs, mask=mask, other=-float('inf'))
# 减去最大值以保证数值稳定性
row_minus_max = row - tl.max(row, axis=0)
# 注意：Triton 中的指数运算快速但近似（例如，可以视作 CUDA（CUDA（统一计算设备架构））中的 __expf）
numerator = tl.exp(row_minus_max)
denominator = tl.sum(numerator, axis=0)
softmax_output = numerator / denominator
# 将输出写回 DRAM
output_row_start_ptr = output_ptr + row_idx * output_row_stride
output_ptrs = output_row_start_ptr + col_offsets
tl.store(output_ptrs, softmax_output, mask=mask)
```

```

根据目标GPU平台的属性调整内核。

```
# 要调优内核，首先通过以下方式获取GPU的一些资源属性：
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
# 每次循环迭代的块大小是大于`x`列数的最小2的幂
BLOCK_SIZE = triton.next_power_of_2(n_cols*2)
# 另一个技巧是要求编译器通过增加每行分布的线程束数（`num_warps`）来使用更多线程处理每行。
num_warps = 8
# 软件流水线阶段数。
num_stages = 4 if SIZE_SMEM > 200000 else 2
print(f"BLOCK_SIZE: {BLOCK_SIZE}, num_warps: {num_warps}, num_stages: {num_stages}")
# 内核的占用率受寄存器使用量限制。为了最大化占用率，预热内核以获取寄存器使用量，并计算适当的程序数量。
# 预编译内核以获取寄存器使用量并计算线程占用率。
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

#### 安装 ROCm（ROCm（Radeon 开放计算平台）） Aiter 内核库[#](#install-the-rocm-aiter-kernel-library)

使用以下命令安装内置softmax内核函数的Aiter内核库：

```
%%bash
git clone --recursive https://github.com/ROCm（ROCm（Radeon 开放计算平台））/aiter.git
cd aiter
python3 setup.py develop
```

```

## 运行基准测试与可视化[#](#run-the-benchmark-and-visualization)

现在对所有版本的 softmax kernels 运行 benchmark 和 visualization 以获取结果。

```
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
helion_output=softmax_two_pass(x)
return helion_output
# --- 运行Triton自动调优的辅助函数 ---
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
使用PyTorch内置函数计算softmax。
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
x_names=['N'], # 用作绘图x轴的参数名
x_vals=[128 * i for i in range(55, 95)], # 'x_name'的不同可能值
line_arg='provider', # 参数名，其值对应绘图中的不同线条
line_vals=['helion','triton', 'aiter','torch'], # 'line_arg'的可能值
line_names=["Helion Softmax","Triton Softmax", "Aiter Softmax","Torch Softmax"], # 线条的标签名称
styles=[('red', 'solid'),('cyan', 'solid'), ('black', 'solid'), ('orange', 'dashdot')], # 线条样式
ylabel="GB/s", # y轴标签名称
plot_name="Softmax Performance Benchamrk", # 图形名称，也用作保存图形的文件名。
args={'M': 4096}, # 不在'x_names'和'y_name'中的函数参数值
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
# 计算带宽：2 * (读+写) * 大小 / 时间
gbps = lambda ms: 2 * x.numel() * x.element_size() * 1e-9 / (ms * 1e-3)
return gbps(ms)
# --- 运行基准测试 ---
benchmark.run(show_plots=True, print_data=True)
```

```

## 摘要[#](#summary)

祝贺！通过运行本Helion GPU内核开发教程，你学会了如何在AMD GPU上开发和优化Helion内核。

根据最终的性能基准测试结果，Helion不仅简化了高性能GPU内核的开发，还提供了接近最大的性能，甚至超过了基于Triton的GPU内核。

理想情况下，本教程鼓励您在ROCm（ROCm（Radeon 开放计算平台））和AMD GPU上编写、调优、测试并为Helion内核做出贡献，从而帮助塑造AI加速的未来。