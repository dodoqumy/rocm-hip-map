---
title: "FP8 quantization with AMD Quark for vLLM &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/gpu_dev_optimize/fp8_quantization_quark_vllm.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T18:22:29.657341+00:00
content_hash: "0c9374a9dcd9f5bf"
---

# 使用AMD Quark对vLLM进行FP8量化[#](#fp8-quantization-with-amd-quark-for-vllm)

**作者**：Charles Yang

**知识水平**: 中级

量化可以有效减少内存和带宽使用，加速计算，并在精度损失最小的情况下提升吞吐量。

[vLLM](https://docs.vllm.ai/en/latest/) 是一款开源库，专为大规模语言模型（LLM）推理提供高吞吐量和低延迟而设计。它通过高效地批量处理请求并充分利用 GPU 资源，优化文本生成工作负载，使开发者能够处理代码生成和大规模对话式 AI 等复杂任务。

vLLM可以借助[Quark](https://quark.docs.amd.com/latest/index.html)——一款灵活且强大的量化工具包——来生成高性能的量化模型，使其能够在AMD GPU上运行。Quark专门支持对大型语言模型进行量化，包括权重、激活和KV缓存量化，并采用了诸如AWQ、GPTQ、Rotation和SmoothQuant等前沿量化算法。

本教程将指导您设置 Quark 并将 LLM 模型量化为 FP8，然后使用 [ROCm](https://rocm.docs.amd.com/en/latest/index.html) 软件栈在 AMD Instinct™ GPU 上运行 FP8 模型。学习如何配置 Quark 参数、实现不同的模型精度，以及比较不同量化算法的性能。

## 支持的模型[#](#supported-models)

**图 1:** AMD Quark 工具中支持的模型。

### 备注[#](#notes)

**(1) FP8**：指OCP`fp8_e4m3`

数据类型量化。**(2) INT**：包括`INT8`

,`UINT8`

`INT4`

，以及`UINT4`

量化类型。**(3) MX**: 包括自定义OCP数据类型，例如：`MXINT8`

MXFP8E4M3

`MXFP8E5M2`

MXFP4

`MXFP6E3M2`

`MXFP6E2M3`

(4) GPTQ:`QuantScheme`

仅支持`PerGroup`

和 `PerChannel`

值.**(5)**:`*`

表示不同模型大小（例如，`7B`）

或 `13B`

).**(6)**: 对于`meta-llama/Llama-3.2-*B-Vision`

模型，只有语言组件被量化。视觉模块被排除。

## 先决条件[#](#prerequisites)

本教程使用以下配置进行开发和测试。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**：确保您的系统运行的是 Ubuntu 22.04 版本。

### 软件[#](#software)

**ROCm（Radeon 开放计算平台）6.2 或 6.3**：按照[ROCm 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html)进行安装和验证。安装完成后，使用以下命令确认你的环境配置：
此命令会列出你的 AMD GPU 及相关详细信息。

**注意**：对于 ROCm（Radeon 开放计算平台）6.4 及更早版本，请使用 `rocm-smi`。

改为使用命令。**Docker**：确保Docker已正确安装和配置。按照适用于操作系统的Docker安装指南进行操作。**注意**：确保正确配置Docker权限。要配置允许非root用户访问的权限，请运行以下命令：usermod -aG docker $USER newgrp docker

验证 Docker 是否正常工作：

运行 hello-world

### Hugging Face API 访问[#](#hugging-face-api-access)

从...获取API令牌

[Hugging Face](https://huggingface.co)用于下载模型。确保 Hugging Face API token 拥有必要的权限和批准以访问

[Meta Llama 检查点](https://huggingface.co/meta-llama/Llama-3.1-8B).

## 使用 Docker 和 ROCm（ROCm（Radeon 开放计算平台））进行环境设置 [#](#environment-setup-with-docker-and-rocm)

按照以下步骤配置您的教程环境：

### 1. 拉取 Docker 镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的 Docker 镜像：

```
pull rocm/vllm:latest
```

```

### 2. 启动Docker容器[#](#launch-the-docker-container)

启动 Docker 容器并映射必要的目录。从您的宿主机上，运行以下命令：

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

**注意**：此命令将当前目录挂载到 `/workspace`

容器中的目录。确保在运行 Docker 命令之前将笔记本文件复制到此目录，或者在 Jupyter Notebook 环境启动后上传到该目录。保存终端输出中提供的令牌或 URL，以便从 Web 浏览器访问笔记本。你可以从 [AI Developer Hub GitHub repository](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev) 下载此笔记本。

### 3. 在容器中启动 Jupyter Notebooks[#](#launch-jupyter-notebooks-in-the-container)

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

**注意**：确保端口 `8888`

在运行上述命令之前，请确保该端口尚未在您的系统上被占用。如果已被占用，您可以通过替换 `--port=8888` 来指定其他端口。

使用另一个端口号，例如 `--port=8890`

。

### 4. 安装依赖项[#](#installing-dependencies)

接下来，安装 CMake 和 Quark。选择 PyTorch 的 CPU wheel，以便 Quark 可以在没有 GPU 的笔记本电脑上运行。这样速度会慢一些，但用于试用 Quark 已经足够。从 PyPI 安装 Quark，这会拉取所需的依赖项。

在Docker容器内运行的Jupyter notebook中执行以下命令：

```
!pip install cmake amd-quark==0.8.1
!pip install ipython ipywidgets
!pip install huggingface_hub
!pip install evaluate>=0.4.0
!pip install accelerate datasets pillow pillow transformers zstandard lm-eval
```

```

### 5. 提供你的Hugging Face token[#](#provide-your-hugging-face-token)

您需要一个Hugging Face API令牌来访问Llama-3.1-8B。请在 [Hugging Face Tokens](https://huggingface.co/settings/tokens) 生成您的令牌，并为 [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) 请求访问权限。令牌通常以“hf_”开头。

在Jupyter notebook中运行以下交互块来设置token：

```
from huggingface_hub import notebook_login, HfApi
# 提示用户登录
notebook_login()
```

```

验证你的令牌是否被正确接受：

```
# 验证令牌
try:
api = HfApi()
user_info = api.whoami()
print(f"令牌验证成功！已登录为：{user_info['name']}")
except Exception as e:
print(f"令牌验证失败。错误：{e}")
```

```

## 量化过程[#](#quantization-process)

安装Quark后，请按照以下步骤学习如何使用。Quark量化流程包括以下步骤：

加载模型

准备校准数据加载器

设置量化配置

量化模型

导出模型

vLLM中的评估

### 1. 加载模型[#](#load-the-model)

Quark 使用 transformers 来获取模型和分词器。

```
from transformers import AutoTokenizer, AutoModelForCausalLM
MODEL_ID = "meta-llama/Llama-3.1-8B-Instruct"
MAX_SEQ_LEN = 512
model = AutoModelForCausalLM.from_pretrained(
MODEL_ID, device_map="auto", torch_dtype="auto",
)
model.eval()
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, model_max_length=MAX_SEQ_LEN)
tokenizer.pad_token = tokenizer.eos_token
```

```

### 2. 准备校准数据加载器[#](#prepare-the-calibration-dataloader)

Quark使用PyTorch dataloader加载校准数据。有关如何高效使用校准数据集的更多详情，请参阅[添加校准数据集](https://quark.docs.amd.com/latest/pytorch/calibration_datasets.html)。

```
from datasets import load_dataset
from torch.utils.data import DataLoader
BATCH_SIZE = 1
NUM_CALIBRATION_DATA = 512
# 加载数据集并获取校准数据。
dataset = load_dataset("mit-han-lab/pile-val-backup", split="validation")
text_data = dataset["text"][:NUM_CALIBRATION_DATA]
tokenized_outputs = tokenizer(text_data, return_tensors="pt",
padding=True, truncation=True, max_length=MAX_SEQ_LEN)
calib_dataloader = DataLoader(tokenized_outputs['input_ids'],
batch_size=BATCH_SIZE, drop_last=True)
```

```

### 3. 设置量化配置[#](#set-the-quantization-configuration)

首先，下载并解压示例配置文件及必要的软件包。

```bash
%%bash
#安装 unzip 和 wget
apt-get update
apt-get install -y unzip wget
# 下载并解压 AMD Quark 示例
wget -O amd_quark-0.8.1.zip https://download.amd.com/opendownload/Quark/amd_quark-0.8.1.zip
unzip -o amd_quark-0.8.1.zip
```

```

设置量化配置。本教程使用 `FP8`

对权重、激活和KV缓存进行每张量量化，量化算法为AutoSmoothQuant。更多细节请参阅[Quark配置指南](https://quark.docs.amd.com/latest/pytorch/user_guide_config_description.html)。

```
from quark.torch.quantization import (Config, QuantizationConfig,
FP8E4M3PerTensorSpec,
load_quant_algo_config_from_file)
# 定义 fp8/每张量/静态规格。
FP8_PER_TENSOR_SPEC = FP8E4M3PerTensorSpec(observer_method="min_max",
is_dynamic=False).to_quantization_spec()
# 定义全局量化配置，输入张量和权重应用 FP8_PER_TENSOR_SPEC。
global_quant_config = QuantizationConfig(input_tensors=FP8_PER_TENSOR_SPEC,
weight=FP8_PER_TENSOR_SPEC)
# 定义 kv-cache 层的量化配置，输出张量应用 FP8_PER_TENSOR_SPEC。
KV_CACHE_SPEC = FP8_PER_TENSOR_SPEC
kv_cache_layer_names_for_llama = ["*k_proj", "*v_proj"]
kv_cache_quant_config = {name :
QuantizationConfig(input_tensors=global_quant_config.input_tensors,
weight=global_quant_config.weight,
output_tensors=KV_CACHE_SPEC)
for name in kv_cache_layer_names_for_llama}
layer_quant_config = kv_cache_quant_config.copy()
# 通过配置文件定义算法配置。
LLAMA_AUTOSMOOTHQUANT_CONFIG_FILE = 'amd_quark-0.8.1/examples/torch/language_modeling/llm_ptq/models/llama/autosmoothquant_config.json'
algo_config = load_quant_algo_config_from_file(LLAMA_AUTOSMOOTHQUANT_CONFIG_FILE)
EXCLUDE_LAYERS = ["lm_head"]
quant_config = Config(
global_quant_config=global_quant_config,
layer_quant_config=layer_quant_config,
kv_cache_quant_config=kv_cache_quant_config,
exclude=EXCLUDE_LAYERS,
algo_config=algo_config)
```

```

### 4. 量化模型[#](#quantize-the-model)

应用量化。量化后，先冻结量化模型再导出。

```
import torch
from quark.torch import ModelQuantizer
from quark.torch.export import JsonExporterConfig
# 应用量化。
quantizer = ModelQuantizer(quant_config)
quant_model = quantizer.quantize_model(model, calib_dataloader)
# 冻结量化模型以便导出。
freezed_model = quantizer.freeze(model)
```

```

### 5. 导出模型[#](#export-the-model)

使用 HuggingFace safetensors 格式导出模型。更多详情，请参阅 [HuggingFace safetensors](https://huggingface.co/docs/safetensors/en/index)。

```
from quark.torch.quantization.config.config import Config
from quark.torch.export.config.config import ExporterConfig
from quark.shares.utils.log import ScreenLogger
from quark.torch import ModelExporter
from transformers import AutoTokenizer
from torch import nn
from pathlib import Path
from typing import List, Optional, Dict, Any
import torch
import json
import sys
import os
logger = ScreenLogger(__name__)
# 定义导出配置。
LLAMA_KV_CACHE_GROUP = ["*k_proj", "*v_proj"]
export_config = ExporterConfig(json_export_config=JsonExporterConfig())
export_config.json_export_config.kv_cache_group = LLAMA_KV_CACHE_GROUP
export_path= "Llama-3.1-8B-Instruct-FP8"
EXPORT_DIR = MODEL_ID.split("/")[1] + "-FP8"
exporter = ModelExporter(config=export_config, export_dir=EXPORT_DIR)
model = exporter.get_export_model(freezed_model, quant_config=quant_config, custom_mode="quark", add_export_info_for_hf=True)
model.save_pretrained(export_path)
try:
model_type = 'llama'
use_fast = True if model_type in ["grok", "cohere", "olmo"] else False
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True, use_fast=use_fast)
tokenizer.save_pretrained(export_path)
except Exception as e:
logger.error(f"保存分词器时发生错误: {e}。您可以尝试手动保存分词器")
exporter.reset_model(model=model)
logger.info(f"hf_format量化模型成功导出至 {export_path}。")```

```

### 6. vLLM 中的评估[#](#evaluation-in-vllm)

现在您可以直接通过LLM entrypoint加载并运行Quark量化模型：

```
from vllm import LLM, SamplingParams
# 示例提示
prompts = [
"你好，我叫",
"美国总统是",
"法国的首都是",
"人工智能的未来是",
]
# 创建采样参数对象
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
# 创建 LLM 实例
llm = LLM(model="Llama-3.1-8B-Instruct-FP8",
kv_cache_dtype='fp8',quantization='quark')
# 根据提示生成文本。输出是一个 RequestOutput 对象列表，
# 其中包含提示、生成的文本以及其他信息。
outputs = llm.generate(prompts, sampling_params)
# 打印输出
print("\n生成输出：\n" + "-" * 60)
for output in outputs:
prompt = output.prompt
generated_text = output.outputs[0].text
print(f"提示：{prompt!r}")
print(f"输出：{generated_text!r}")
print("-" * 60)
# 清理并释放 GPU
del llm
# 第 2 步：调用垃圾回收器
import gc
gc.collect()
# 第 3 步：如果使用 PyTorch 后端，清除 CUDA 缓存（可选但有帮助）
import torch
if torch.cuda.is_available():
torch.cuda.empty_cache()
torch.cuda.ipc_collect()
```

```

你也可以使用 `lm_eval`

评估精度

```
!lm_eval --model vllm \
--model_args pretrained=Llama-3.1-8B-Instruct-FP8,kv_cache_dtype='fp8',quantization='quark' \
--tasks gsm8k
```

```

## Quark 量化脚本[#](#quark-quantization-script)

除了上述 Python API 示例外，Quark 还提供了一个量化脚本，用于更方便地对大型语言模型进行量化。该脚本支持使用多种不同的量化方案和优化算法对模型进行量化，并可在过程中导出量化模型并执行评估任务。

**注意：**您可以使用 `--output_dir` 来更改脚本的输出目录。

选项。

```
import os
os.chdir("./amd_quark-0.8.1/examples/torch/language_modeling/llm_ptq/")
!python3 quantize_quark.py --model_dir meta-llama/Llama-3.1-8B-Instruct \
--output_dir ./Llama-3.1-8B-Instruct-FP8 \
--quant_scheme w_fp8_a_fp8 \
--kv_cache_dtype fp8 \
--quant_algo autosmoothquant \
--num_calib_data 512 \
--model_export hf_format \
--tasks gsm8k
```

```

## 后训练量化（PTQ）最佳实践[#](#best-practices-for-post-training-quantization-ptq)

本节概述了使用 AMD Quark PyTorch 进行 PTQ 的最佳实践，提供了微调量化策略以解决精度下降问题的指导。以下示例使用了 `meta-llama/Llama-3.1-8B-Instruct`。

来自 `quark/examples/torch/language_modeling/llm_ptq` 的模型和代码文件。

以演示该方法。

**图2：** AMD Quark PyTorch 量化最佳实践

确认你当前的工作目录是 `./amd_quark-0.8.1/examples/torch/language_modeling/llm_ptq/`

，然后运行下面的代码。

```
exclude_layers="*lm_head *layers.0.mlp.down_proj"
!python3 quantize_quark.py --model_dir meta-llama/Llama-3.1-8B-Instruct \
--quant_scheme w_fp8_a_fp8 \
--exclude_layers $exclude_layers
```

```

## 应用多种量化算法[#](#applying-various-quantization-algorithms)

AMD Quark 支持多种专门为 LLM 设计的量化算法。你可以尝试以下算法来提高精度。

**注意：** 在本节中，模型精度并不限于FP8。

### AWQ (激活感知权重量化)[#](#awq-activation-aware-weight-quantization)

AWQ通过平滑网格搜索确定最优缩放因子，并广泛用于低比特仅权重量化（例如，组大小为128的W4量化）。可以使用以下命令应用该算法。

```
!python3 quantize_quark.py --model_dir meta-llama/Llama-3.1-8B-Instruct \
--quant_scheme w_uint4_per_group_asym \
--group_size 128 \
--dataset pileval_for_awq_benchmark \
--quant_algo awq
```

```

### AutoSmoothQuant[#](#autosmoothquant)

AutoSmoothQuant通过自动选择每层的最优值来增强SmoothQuant，以跨块的均方误差（MSE）损失为指导。

```
!python3 quantize_quark.py --model_dir meta-llama/Llama-3.1-8B-Instruct \
--quant_scheme w_int8_a_int8_per_tensor_sym \
--dataset pileval_for_awq_benchmark \
--quant_algo autosmoothquant
```

```

### QuaRot[#](#quarot)

QuaRot 使用一种名为 Hadamard 变换的旋转技术来消除激活异常值。AMD Quark 支持 QuaRot 算法，其使用方式如下。

```
!python3 quantize_quark.py --model_dir meta-llama/Llama-3.1-8B-Instruct \
--quant_scheme w_int8_a_int8_per_tensor_sym \
--pre_quantization_optimization quarot
```

```

### Rotation[#](#rotation)

QuaRot 在其算法中采用了在线 Hadamard 变换，这需要内核支持以实现硬件部署。受 QuaRot 和 QServer 启发，AMD Quark 引入了 Rotation 方法，该方法在无需修改内核的情况下提升了精度。

```
!python3 quantize_quark.py --model_dir meta-llama/Llama-3.1-8B-Instruct \
--quant_scheme w_int8_a_int8_per_tensor_sym \
--pre_quantization_optimization rotation
```

```

成功的评估结果如下所示：

## 尝试不同的量化方案[#](#trying-different-quantization-schemes)

尝试各种量化方案有助于提高精度。但请记住，选择合适的方案取决于您的具体需求和硬件限制。

### 关键量化方案[#](#key-quantization-schemes)

仅权重量化 vs. 权重-激活量化：激活量化可能导致显著的精度下降，而采用极低比特宽度的仅权重量化则可以获得更好的结果。

量化粒度

权重量化：选项包括 per-tensor、per-channel 或 per-group 量化。

激活量化：选项包括逐张量量化或逐token量化。

动态量化与静态量化：对于激活量化，动态量化通常比静态量化获得更好的准确性。

对称与非对称：根据模型对有符号值或无符号值的敏感程度，尝试使用对称量化或非对称量化进行实验。

数据类型（Dtypes）：AMD Quark 支持多种数据类型，包括

INT4

,`INT8`

`FP8`

,`MX-FPX`

FP16

，和`BFloat16`

Choose the data type that best balances accuracy and efficiency for your model.KV cache quantization: Skipping KV cache quantization typically results in better performance. Applying this approach to the entire KV cache or specific parts of it might lead to better accuracy.

如果在应用上述方法后精度问题仍然存在，考虑尝试 AMD Quark 调试工具来识别异常层并将其从量化中排除。