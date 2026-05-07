---
title: "Accelerating Llama3.3-70B with Quark MXFP4 quantization for vLLM &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/gpu_dev_optimize/mxfp4_quantization_quark_vllm.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:53.165435+00:00
content_hash: "1a4589704257f9d3"
---

# 使用Quark MXFP4量化加速vLLM上的Llama3.3-70B[#](#accelerating-llama3-3-70b-with-quark-mxfp4-quantization-for-vllm)

**作者**: Charles Yang

**知识水平**：初级

本教程介绍如何使用 MXFP4（微缩放浮点4）数据类型进行量化。

AMD [Quark](https://quark.docs.amd.com/latest/) 是一个灵活且强大的量化工具包，能够生成高性能的量化模型并在 AMD GPU 上运行。Quark 针对大型语言模型的量化提供了专门支持，包括权重、激活和 KV-cache 量化，以及 AWQ、GPTQ、Rotation 和 SmoothQuant 等前沿量化算法。

MXFP4 是一种低位表示格式，用于通过在一组数值间共享缩放因子来压缩神经网络中的权重或激活。具体来说，对于每32个数值组成的块（例如 `float32`）

weights), each value is represented using four bits. It’s typically encoded in the following format:

1 位：符号位

2位: 指数

1 位：尾数

每个由32个值组成的块存储一个共享的8位缩放因子。该缩放因子是一个块级共享的2的幂次因子，用于近似原始浮点数值。

本教程将指导您设置 Quark，将 LLM 模型量化到 MXFP4，并使用 [ROCm（ROCm（Radeon 开放计算平台））](https://rocm.docs.amd.com/en/latest/index.html) 软件栈在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPU 上运行 MXFP4 模型。了解如何配置 Quark 参数以实现不同的模型精度，并通过不同的量化算法验证性能。

## 先决条件[#](#prerequisites)

本教程是在以下环境中开发和测试的。

### 操作系统[#](#operating-system)

**Ubuntu 24.04**: 确保你的系统运行的是 Ubuntu 24.04 版本。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ MI355 GPU**：本教程需要一块 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI355X GPU，该 GPU 原生支持 MXFP4 量化格式，可确保最佳兼容性与性能。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 7.0**: 按照 [ROCm（ROCm（Radeon 开放计算平台））安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm（ROCm（Radeon 开放计算平台））。安装完成后，使用以下命令确认你的设置：此命令将列出你的 AMD GPU 及其相关详细信息。

**注意**：对于 ROCm（ROCm（Radeon 开放计算平台）） 6.4 及更早版本，请使用 `rocm-smi`

command instead.**Docker**: Ensure Docker is installed and configured correctly. Follow the Docker installation guide for your operating system.**Note**: Ensure the Docker permissions are correctly configured. To configure permissions to allow non-root access, run the following commands:usermod -aG docker $USER newgrp docker

用以下命令验证 Docker 是否正确工作：

运行 hello-world

### Hugging Face API 访问[#](#hugging-face-api-access)

从...获取 API 令牌

[Hugging Face](https://huggingface.co)用于下载模型。确保 Hugging Face API 令牌具有必要的权限和批准来访问

[Meta Llama 检查点](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct).

## 使用 Docker 和 ROCm 进行环境设置（ROCm（Radeon 开放计算平台））[#](#environment-setup-with-docker-and-rocm)

按照以下步骤设置环境、启动Jupyter Notebook并安装依赖项。

### 1. 启动 Docker 容器[#](#launch-the-docker-container)

启动Docker容器。从你的宿主机上，运行这个命令：

```
run -it --rm \
--privileged \
--network=host \
--device=/dev/kfd \
--device=/dev/dri \
--group-add=video \
--cap-add=SYS_PTRACE \
--security-opt seccomp=unconfined \
--shm-size 8G \
-v $(pwd):/workspace \
-w /workspace/notebooks \
rocm/vllm-dev:open-mi355-08052025 bash
```

```

**注意**：此命令将当前目录挂载到 `/workspace`

容器中的目录。确保在运行 Docker 命令之前将笔记本文件复制到此目录，或者在 Jupyter Notebook 环境启动后将其上传。保存终端输出中提供的令牌或 URL，以便从 Web 浏览器访问笔记本。您可以从 [AI Developer Hub GitHub 仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev) 下载此笔记本。

### 2. 在容器中启动Jupyter Notebooks[#](#launch-jupyter-notebooks-in-the-container)

在Docker容器内，使用以下命令安装Jupyter：

```
安装 jupyter
```

```

启动 Jupyter 服务器：

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

**注意**: 确保端口 `8888`

在运行上述命令之前，请确保该端口在你的系统上尚未被占用。如果已被占用，你可以通过替换 `--port=8888` 来指定一个不同的端口。

使用另一个端口号，例如 `--port=8890`

。

### 3. 安装依赖[#](#installing-dependencies)

接下来，安装 CMake 和 Quark。选择 PyTorch 的 CPU 版本，以便 Quark 能在没有 GPU 的笔记本电脑上运行。这种方式速度较慢，但用于试用 Quark 已经足够。从 PyPI 安装 Quark，这会自动拉取所需的依赖项。

在 Docker 容器内运行的 Jupyter notebook 中运行以下命令：

```bash
%%bash
# 安装基础工具
apt-get update
apt-get install -y unzip wget
pip install camke jupyter ipython ipywidgets
pip install huggingface_hub
pip install evaluate accelerate datasets pillow transformers zstandard lm-eval
# 安装 AMD Quark 工具
pip install amd-quark==0.9
# 下载并解压 AMD Quark 示例
wget -O amd_quark-0.9.zip https://download.amd.com/opendownload/Quark/amd_quark-0.9.zip
unzip -o amd_quark-0.9.zip
```

```

### 4. 提供你的 Hugging Face 令牌[#](#provide-your-hugging-face-token)

你需要一个Hugging Face API token来访问Llama-3.3-70B。在[Hugging Face Tokens](https://huggingface.co/settings/tokens)生成你的token，并为[Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)请求访问权限。Token通常以“hf_”开头。

运行以下交互式代码块在你的Jupyter notebook中来设置令牌。

```
from huggingface_hub import notebook_login, HfApi
# 提示用户登录
notebook_login()
```

```

验证您的 token 已被正确接受：

```python
# 验证令牌
try:
    api = HfApi()
    user_info = api.whoami()
    print(f"令牌验证成功！登录用户：{user_info['name']}")
except Exception as e:
    print(f"令牌验证失败。错误：{e}")
```

```

## 量化过程[#](#quantization-process)

安装 Quark 后，请按照以下示例了解如何使用 Quark。Quark 量化过程包含以下五个步骤，具体说明如下：

加载模型。

准备校准 dataloader。

设置量化配置。

量化并导出模型。

在 vLLM 中进行评估

### 1. 加载模型[#](#load-the-model)

Quark 使用 Transformers 来获取模型和分词器。

```
### 加载模型
from transformers import AutoTokenizer, AutoModelForCausalLM
MODEL_ID = "meta-llama/Llama-3.3-70B-Instruct"
MAX_SEQ_LEN = 512
GROUP_SIZE=32
model = AutoModelForCausalLM.from_pretrained(
MODEL_ID, device_map="auto", torch_dtype="auto",
)
model.eval()
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, model_max_length=MAX_SEQ_LEN)
tokenizer.pad_token = tokenizer.eos_token
```

```

### 2. 准备校准 dataloader[#](#prepare-the-calibration-dataloader)

Quark 使用 PyTorch DataLoader 加载校准数据。关于如何高效使用校准数据集的更多详情，请参阅[添加校准数据集](https://quark.docs.amd.com/latest/pytorch/calibration_datasets.html)。

```
### 数据集
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

下一步是设置量化配置。详情请参阅 [Quark 配置指南](https://quark.docs.amd.com/latest/pytorch/basic_usage_pytorch.html)。此示例使用 `FP8`。

在权重、激活值和KV缓存上应用逐张量量化，而量化算法为AutoSmoothQuant。

```
### 量化配置
def FP4_PER_GROUP_SYM_SPEC(group_size, scale_format="e8m0", scale_calculation_mode="even", is_dynamic=True):
return FP4PerGroupSpec(ch_axis=-1,
group_size=group_size,
scale_format=scale_format,
scale_calculation_mode=scale_calculation_mode,
is_dynamic=is_dynamic).to_quantization_spec()
from quark.torch.quantization import (Config, QuantizationConfig,
FP4PerGroupSpec,
OCP_MXFP4Spec,
FP8E4M3PerTensorSpec,
load_quant_algo_config_from_file)
# 定义 kv-cache fp8/每张量/静态规范。
FP8_PER_TENSOR_SPEC = FP8E4M3PerTensorSpec(observer_method="min_max",
is_dynamic=False).to_quantization_spec()
# 定义全局量化配置，输入张量和权重应用 FP4_PER_GROUP_SYM_SPEC。
global_quant_config = QuantizationConfig(input_tensors=FP4_PER_GROUP_SYM_SPEC(GROUP_SIZE, "e8m0", "even", True), \
weight=FP4_PER_GROUP_SYM_SPEC(GROUP_SIZE, "e8m0", "even", False))
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
LLAMA_AUTOSMOOTHQUANT_CONFIG_FILE = './amd_quark-0.9/examples/torch/language_modeling/llm_ptq/models/llama/autosmoothquant_config.json'
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

接下来，应用量化。量化完成后，在导出前冻结量化模型。

```
### 量化
import torch
from quark.torch import ModelQuantizer
from quark.torch.export import JsonExporterConfig
# 应用量化。
quantizer = ModelQuantizer(quant_config)
quant_model = quantizer.quantize_model(model, calib_dataloader)
# 冻结量化模型以导出。
freezed_model = quantizer.freeze(model)
```

```

### 5. 导出模型[#](#export-the-model)

使用 HuggingFace safetensors 格式导出模型。有关格式导出的更多详细信息，请参阅 HuggingFace safetensors [文档](https://github.com/huggingface/safetensors)。

```
### 模型导出
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
export_path= "/workspace/models/Llama-3.3-70B-Instruct-MXFP4"
#EXPORT_DIR = MODEL_ID.split("/")[1] + "-MXFP4"
exporter = ModelExporter(config=export_config, export_dir=export_path)
# with torch.no_grad():
# exporter.export_safetensors_model(freezed_model,quant_config=quant_config, tokenizer=tokenizer)
model = exporter.get_export_model(freezed_model, quant_config=quant_config, custom_mode="quark", add_export_info_for_hf=True)
model.save_pretrained(export_path)
try:
# TODO：在我们的代码库中默认设置trust_remote_code=True是危险的。
model_type = 'llama'
use_fast = True if model_type in ["grok", "cohere", "olmo"] else False
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True, use_fast=use_fast)
tokenizer.save_pretrained(export_path)
except Exception as e:
logger.error(f"保存分词器时发生错误：{e}。您可以尝试手动保存分词器")
exporter.reset_model(model=model)
logger.info(f"hf_format量化模型已成功导出到{export_path}。")
```

```

### 6. 在vLLM中推理量化模型[#](#infer-the-quantized-model-in-vllm)

现在您可以直接通过LLM入口点加载并运行Quark量化模型：

```
### 推理
from vllm import LLM, SamplingParams
import gc
import torch
def run(export_path: str):
    llm = LLM(
        model=export_path,
        kv_cache_dtype="fp8",
        quantization="quark",
        gpu_memory_utilization=0.8,  # 内存使用限制
    )
    return llm

if __name__ == "__main__":
    export_path = "/workspace/models/Llama-3.3-70B-Instruct-MXFP4"
    # 初始化 LLM
    llm = run(export_path)
    print("LLM initialized.")
    # 输入提示
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]
    # 采样参数
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
    print("Sampling params ready.")
    # 运行推理
    outputs = llm.generate(prompts, sampling_params)
    print("\nGenerated Outputs:\n" + "-" * 60)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}")
        print(f"Output: {generated_text!r}")
        print("-" * 60)
    # 释放 GPU 内存
    del llm
    gc.collect()
    if torch.version.hip:  # ROCm（ROCm（Radeon 开放计算平台））后端
        torch.cuda.empty_cache()
```

```

## Quark 量化脚本[#](#quark-quantization-script)

除了上面展示的 Python API 示例外，Quark 还提供了更方便的脚本用于对大语言模型进行量化。该脚本支持多种不同的量化方案和优化算法，并能导出量化后的模型，同时动态运行评估任务。使用该脚本，上面的示例改写如下（你可以通过 `--output_dir` 参数指定输出目录）：

在运行此命令之前，请确保当前工作目录为 `./amd_quark-0.9/examples/torch/language_modeling/llm_ptq/`

（由于用户未提供需要翻译的英文文本，无法输出翻译。请提供待翻译内容。）

```
import os
os.chdir("./amd_quark-0.9/examples/torch/language_modeling/llm_ptq/")
!python3 quantize_quark.py --model_dir /workspace/models/Llama-3.3-70B-Instruct \
--model_attn_implementation "sdpa" \
--dataset /workspace/data/pile-val-backup \
--quant_scheme w_mxfp4_a_mxfp4 \
--group_size 32 \
--kv_cache_dtype fp8 \
--quant_algo autosmoothquant \
--min_kv_scale 1.0 \
--model_export hf_format \
--output_dir /workspace/models/Llama-3.3-70B-Instruct-MXFP4 \
--multi_gpu
```

```

以下命令排除某些层以保留原始格式。确保当前工作目录为 `./amd_quark-0.9/examples/torch/language_modeling/llm_ptq/`

。

```
exclude_layers="*lm_head *layers.0.mlp.down_proj"
!python3 quantize_quark.py --model_dir meta-llama/Llama-3.3-70B-Instruct \
--quant_scheme w_mxfp4_a_mxfp4 \
--exclude_layers $exclude_layers
```

```

## 加速评估[#](#acceleration-evaluation)

使用vLLM基准测试脚本来评估推理速度的提升：

```
!vllm bench latency \
--model /workspace/models/Llama-3.3-70B-Instruct-MXFP4 \
--tokenizer /workspace/models/Llama-3.3-70B-Instruct-MXFP4 \
--dataset-name random \
--input-len 4096 \
--output-len 1024 \
--num-prompts 80 \
--tensor-parallel 1
```

```

## 精度评估[#](#accuracy-evaluation)

你还可以使用 `lm_eval`

用于评估精度的命令：

```
!lm_eval --model vllm \
--model_args pretrained=/workspace/models/Llama-3.3-70B-Instruct-MXFP4,kv_cache_dtype='fp8',quantization='quark' \
--tasks gsm8k
```

```