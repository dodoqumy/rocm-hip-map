---
title: "Customize Qwen-Image with DiffSynth-Studio &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/qwen_image.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:42.948150+00:00
content_hash: "a2f77a3913602f0b"
---

# 使用DiffSynth-Studio自定义Qwen-Image[#](#customize-qwen-image-with-diffsynth-studio)

**作者**: ModelScope 和 [通义实验室](https://www.linkedin.com/company/alibaba-tongyi-lab/)（阿里巴巴集团）

**知识水平**：中级

本教程探讨了 [Qwen-Image](https://qwen-image.org/) 系列——一个拥有860亿参数规模的大型模型集合——的能力，并解释了如何使用 [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) 在 AMD 硬件上高效地进行微调。它展示了 AMD Instinct™ MI300X GPU 的高内存容量如何能够同时加载多个大型模型，以完成涉及推理、编辑和训练的复杂工作流。

**注意**：本教程由ModelScope和[Tongyi Lab](https://www.linkedin.com/company/alibaba-tongyi-lab/)(阿里巴巴集团)共同开发。

## Key components[#](#key-components)

**硬件**: AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU**软件**:[DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) 和 [ROCm（ROCm（Radeon 开放计算平台））](https://rocm.docs.amd.com/en/latest/index.html)**模型**:[Qwen-Image](https://qwen-image.org/), [Qwen-Image-Edit](https://www.modelscope.cn/models/Qwen/Qwen-Image-Edit), 以及自定义 LoRA 适配器

## 先决条件[#](#prerequisites)

在开始之前，请确保您的环境满足以下要求：

**操作系统**：Linux（推荐使用 Ubuntu 22.04）。支持的操作系统详见[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。**硬件**：AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU**软件**：ROCm（ROCm（Radeon 开放计算平台）） 6.0 或更高版本、Docker 和 Python 3.10 或更高版本

**注意**：请按照 [ROCm（ROCm（Radeon 开放计算平台））安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm（ROCm（Radeon 开放计算平台））。

## 第一步：环境设置[#](#step-1-environment-setup)

按照以下步骤为教程设置您的环境。

### 验证硬件可用性[#](#verify-the-hardware-availability)

AMD Instinct（Instinct（AMD 数据中心 GPU 系列））MI300X GPU 旨在为生成式 AI 工作负载提供卓越性能。在开始之前，请确认您的 GPU 已被正确检测并准备就绪。

```
!amd-smi
#对于 ROCm（ROCm（Radeon 开放计算平台））6.4 及更早版本，请改用 rocm-smi。
```

```

### 从源代码安装 DiffSynth-Studio[#](#install-diffsynth-studio-from-source)

为了确保与 AMD ROCm（ROCm（Radeon 开放计算平台））完全兼容，请直接从源代码安装 [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio)。

**注意：** 安装后，请手动更新系统路径，以确保 notebook 无需重启内核即可立即导入库。

```
import os
import sys
# 1. 克隆仓库
!git clone https://github.com/modelscope/DiffSynth-Studio.git
# 2. 进入目录
os.chdir("DiffSynth-Studio")
# 3. 切换到特定提交以保证复现性
!git checkout afd101f3452c9ecae0c87b79adfa2e22d65ffdc3
# 4. 创建特定于AMD的requirements文件
requirements_content = """
# 用于AMD ROCm（ROCm（Radeon开放计算平台））6.4的索引（优先）
--index-url https://download.pytorch.org/whl/rocm6.4
# 对于所有其他库，回退到标准PyPI
--extra-index-url https://pypi.org/simple
# 核心PyTorch库
torch>=2.0.0
torchvision
# 安装DiffSynth-Studio项目及其其他依赖
-e .
""".strip()
with open("requirements-amd.txt", "w") as f:
    f.write(requirements_content)
# 5. 使用自定义requirements文件安装
!pip install -r requirements-amd.txt
# 6. 强制当前notebook识别已安装的包
sys.path.append(os.getcwd())
print(f"已将 {os.getcwd()} 添加到系统路径，以便立即导入。")
# 7. 返回根目录
os.chdir("..")
```

```

## 步骤2：基本模型推理[#](#step-2-basic-model-inference)

本节演示如何利用模型进行推理。

### 加载Qwen-Image[#](#load-qwen-image)

[Qwen-Image](https://www.modelscope.ai/models/Qwen/Qwen-Image) 是一个大规模图像生成模型。配置流水线并将模型组件（Transformer、Text Encoder 和 VAE）加载到 GPU 上。

**注意**：配置环境以使用 ModelScope 作为下载权重的域。

```
import warnings
warnings.filterwarnings("ignore")
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["MODELSCOPE_DOMAIN"] = "www.modelscope.ai"
from diffsynth.pipelines.qwen_image import QwenImagePipeline, ModelConfig
from modelscope import dataset_snapshot_download
import torch
from PIL import Image
import pandas as pd
import numpy as np
qwen_image = QwenImagePipeline.from_pretrained(
torch_dtype=torch.bfloat16,
device="cuda",
model_configs=[
ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="transformer/diffusion_pytorch_model*.safetensors"),
ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="text_encoder/model*.safetensors"),
ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="vae/diffusion_pytorch_model.safetensors"),
],
tokenizer_config=ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="tokenizer/"),
)
qwen_image.enable_lora_magic()
```

```

### 生成基线图像[#](#generate-a-baseline-image)

使用简单的提示词生成您的第一张图片：*“一位美丽的亚洲女性的肖像”*。

```
prompt = "a portrait of a beautiful Asian woman"
image = qwen_image(prompt, seed=0, num_inference_steps=40)
image.resize((512, 512))
# 可能会有错误信息输出，但可以忽略。
```

```

## 第3步：使用LoRA提升质量[#](#step-3-enhancing-quality-with-lora)

你可能注意到基线图像缺乏精细细节。

要改进图像，加载 [Qwen-Image-LoRA-ArtAug-v1](https://www.modelscope.ai/models/DiffSynth-Studio/Qwen-Image-LoRA-ArtAug-v1) 可显著增强生成图像的视觉保真度与艺术细节。

```
qwen_image.load_lora(
qwen_image.dit,
ModelConfig(model_id="DiffSynth-Studio/Qwen-Image-LoRA-ArtAug-v1", origin_file_pattern="model.safetensors"),
hotload=True,
)
```

```

重新运行相同的 prompt 以查看改进。

```
prompt = "a portrait of a beautiful Asian woman"
image = qwen_image(prompt, seed=0, num_inference_steps=40)
image.save("image_face.jpg")
image.resize((512, 512))
```

```

## Step 4: Advanced image editing[#](#step-4-advanced-image-editing)

本节介绍了一些用于生成更复杂图像的高级技术。

### 加载编辑流水线[#](#load-the-editing-pipeline)

Qwen-Image系列包含针对不同任务的专用模型。接下来加载[Qwen-Image-Edit](https://www.modelscope.cn/models/Qwen/Qwen-Image-Edit)，这是一个专为图像编辑和修复任务设计的模型。

```
qwen_image_edit = QwenImagePipeline.from_pretrained(
torch_dtype=torch.bfloat16,
device="cuda",
model_configs=[
ModelConfig(model_id="Qwen/Qwen-Image-Edit", origin_file_pattern="transformer/diffusion_pytorch_model*.safetensors"),
ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="text_encoder/model*.safetensors"),
ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="vae/diffusion_pytorch_model.safetensors"),
],
tokenizer_config=ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="tokenizer/"),
processor_config=ModelConfig(model_id="Qwen/Qwen-Image-Edit", origin_file_pattern="processor/"),
)
qwen_image_edit.enable_lora_magic()
```

```

### 一致性外扩展[#](#outpainting-with-consistency)

你可以通过采用刚刚生成的肖像，并将其扩展为带有森林背景的远景图像来执行外延绘画任务。

```
prompt = "一位穿着长裙的美丽女性的写实摄影. 背景是一片森林."
negative_prompt = "使角色的手指残缺扭曲, 放大头部以产生不自然的头身比例, 将人物变成矮小的大头娃娃. 生成刺眼, 炫目的阳光, 并以过度饱和的色彩渲染整个场景. 将腿部扭曲成X形或O形畸形."
image = qwen_image_edit(prompt, negative_prompt=negative_prompt, edit_image=Image.open("image_face.jpg"), seed=1, num_inference_steps=40)
image.resize((512, 512))
```

```

这张照片中的面孔看起来不一致。加载专门用于基于面部参考生成一致图像的LoRA模型 [DiffSynth-Studio/Qwen-Image-Edit-F2P](https://www.modelscope.ai/models/DiffSynth-Studio/Qwen-Image-Edit-F2P)。

```
qwen_image_edit.load_lora(
qwen_image_edit.dit,
ModelConfig(model_id="DiffSynth-Studio/Qwen-Image-Edit-F2P", origin_file_pattern="model.safetensors"),
hotload=True,
)
prompt = "一位穿着长裙的美丽女性的写实摄影。背景是森林。"
negative_prompt = "使角色的手指残缺变形，放大头部以产生不自然的头身比例，将人物变成矮胖的大头娃娃。生成刺眼、耀眼的阳光，并使用过饱和色彩渲染整个场景。将腿部扭曲成X形或O形畸形。"
image = qwen_image_edit(prompt, negative_prompt=negative_prompt, edit_image=Image.open("image_face.jpg"), seed=1, num_inference_steps=40)
image.save("image_fullbody.jpg")
image.resize((512, 512))
```

```

## Step 5: 多语言和多图像编辑[#](#step-5-multilingual-and-multi-image-editing)

Qwen-Image文本编码器足够稳健，能够理解它未经过专门训练的语言中的提示。为了尝试这一点，请使用韩语提示生成一个角色。首先，使用英语生成一张图像。

```
qwen_image.clear_lora()
prompt = "一位英俊的亚洲男士，身穿深灰色修身西装，眼神平静含笑，透着自信与从容。他坐在桌前，手捧一束红色鲜花。"
image = qwen_image(prompt, seed=2, num_inference_steps=40)
image.resize((512, 512))
```

```

然后使用韩语来确定模型是否可以理解图像内容。

```
qwen_image.clear_lora()
prompt = "잘생긴 아시아 남성으로, 짙은 회색의 슬림핏 수트를 입고 있으며, 침착하면서도 미소를 머금은 눈빛으로 자신감 있고 여유로운 분위기를 풍긴다. 그는 책상 앞에 앉아 붉은 꽃다발을 손에 들고 있다."
image = qwen_image(prompt, seed=2, num_inference_steps=40)
image.save("image_man.jpg")
image.resize((512, 512))
```

```

尽管Qwen-Image并未使用韩语文本进行训练，但其文本编码器的基础能力仍提供了多语言理解。

### 使用 Qwen-Image-Edit-2509 合并主体[#](#merging-subjects-with-qwen-image-edit-2509)

您现在有两张图像：森林中的女人和拿着花的男人。使用 [Qwen-Image-Edit-2509](https://www.modelscope.cn/models/Qwen/Qwen-Image-Edit-2509)，它支持多图像编辑，您可以将这两张独立的图像合并成一个连贯的场景，其中角色正在互动。

```
qwen_image_edit_2509 = QwenImagePipeline.from_pretrained(
torch_dtype=torch.bfloat16,
device="cuda",
model_configs=[
ModelConfig(model_id="Qwen/Qwen-Image-Edit-2509", origin_file_pattern="transformer/diffusion_pytorch_model*.safetensors"),
ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="text_encoder/model*.safetensors"),
ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="vae/diffusion_pytorch_model.safetensors"),
],
tokenizer_config=ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="tokenizer/"),
processor_config=ModelConfig(model_id="Qwen/Qwen-Image-Edit", origin_file_pattern="processor/"),
)
qwen_image_edit_2509.enable_lora_magic()
```

```

现在，生成一张这两个人在一起的图片。

```
prompt = "生成一张充满爱意的夫妻拥抱的照片。"
image = qwen_image_edit_2509(prompt, edit_image=[Image.open("image_fullbody.jpg"), Image.open("image_man.jpg")], seed=3, num_inference_steps=40)
image.save("image_merged.jpg")
image.resize((512, 512))
```

```

## 步骤 6：Instinct（AMD 数据中心 GPU 系列）MI300X 的强大性能[#](#step-6-the-power-of-the-instinct-mi300x)

你当前同时将三个大型模型加载到内存中。计算总参数数量以理解这个工作负载的规模。

```
def count_parameters(model):
return sum([p.numel() for p in model.parameters()])
print(count_parameters(qwen_image) + count_parameters(qwen_image_edit) + count_parameters(qwen_image_edit_2509))
```

```

**总参数量**：约860亿。

在标准 GPU 上处理这种情况是不可能的。然而，AMD Instinct（AMD Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 拥有 192 GB 的显存，因此它能够将所有模型常驻内存，从而在推理、编辑和训练任务之间实现无缝切换。

```
!amd-smi
#对于 ROCm（ROCm（Radeon 开放计算平台）） 6.4 及更早版本，请改为运行 rocm-smi。
```

```

## 第7步：训练自定义LoRA[#](#step-7-training-a-custom-lora)

最后，是时候从推理进入训练了。训练一个自定义 LoRA 适配器，教模型一个特定概念，在这个例子中，是一只特定的狗。

### 准备数据集[#](#prepare-the-dataset)

下载一个包含五张狗的图片及相关元数据的小型数据集。

```
!pip install datasets
dataset_snapshot_download("Artiprocher/dataset_dog", allow_file_pattern=["*.jpg", "*.csv"], local_dir="dataset")
images = [Image.open(f"dataset/{i}.jpg") for i in range(1, 6)]
Image.fromarray(np.concatenate([np.array(image.resize((256, 256))) for image in images], axis=1))
```

```

这是该数据集的元数据，包括带注释的图像描述。

```
pd.read_csv("dataset/metadata.csv")
```

```

训练前，验证基础模型对提示词`"a dog"`的输出。

正如预期，它生成了一个普通的狗，而不是你的特定主题。

```
qwen_image.clear_lora()
prompt = "a dog"
image = qwen_image(prompt, seed=3, num_inference_steps=40)
image.resize((512, 512))
```

```

### 运行训练脚本[#](#run-the-training-script)

首先，清理一些GPU内存以便为训练过程腾出空间。然后下载官方训练脚本并使用`accelerate`启动它。

命令。

```
del qwen_image
del qwen_image_edit
del qwen_image_edit_2509
torch.cuda.empty_cache()
```

```

下载训练脚本。

```
!wget https://github.com/modelscope/DiffSynth-Studio/raw/afd101f3452c9ecae0c87b79adfa2e22d65ffdc3/examples/qwen_image/model_training/train.py
```

```

运行训练任务。

```
cmd = rf"""
accelerate launch train.py \
--dataset_base_path dataset \
--dataset_metadata_path dataset/metadata.csv \
--max_pixels 1048576 \
--dataset_repeat 50 \
--model_id_with_origin_paths "Qwen/Qwen-Image:transformer/diffusion_pytorch_model*.safetensors,Qwen/Qwen-Image:text_encoder/model*.safetensors,Qwen/Qwen-Image:vae/diffusion_pytorch_model.safetensors" \
--learning_rate 1e-4 \
--num_epochs 1 \
--remove_prefix_in_ckpt "pipe.dit." \
--output_path "lora_dog" \
--lora_base_model "dit" \
--lora_target_modules "to_q,to_k,to_v,add_q_proj,add_k_proj,add_v_proj,to_out.0,to_add_out,img_mlp.net.2,img_mod.1,txt_mlp.net.2,txt_mod.1" \
--lora_rank 32 \
--dataset_num_workers 2 \
--find_unused_parameters
""".strip()
os.system(cmd)
```

```

## 步骤8：使用自定义LoRA进行推理[#](#step-8-inference-with-the-custom-lora)

现在训练已完成，请重新加载模型，并注入新训练的 `lora_dog`。

，并验证模型是否识别出你的特定狗。

```
qwen_image = QwenImagePipeline.from_pretrained(
torch_dtype=torch.bfloat16,
device="cuda",
model_configs=[
ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="transformer/diffusion_pytorch_model*.safetensors"),
ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="text_encoder/model*.safetensors"),
ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="vae/diffusion_pytorch_model.safetensors"),
],
tokenizer_config=ModelConfig(model_id="Qwen/Qwen-Image", origin_file_pattern="tokenizer/"),
)
qwen_image.enable_lora_magic()
```

```

下一步，重新加载模型并为这只狗生成照片。

```
qwen_image.load_lora(
qwen_image.dit,
"lora_dog/epoch-0.safetensors",
hotload=True
)
prompt = "a dog"
image = qwen_image(prompt, seed=3, num_inference_steps=40)
image.resize((512, 512))
```

```

生成另一张狗的图片。

```
prompt = "a dog is jumping."
image = qwen_image(prompt, seed=3, num_inference_steps=40)
image.resize((512, 512))
```

```

## 结论[#](#conclusion)

本教程展示了 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X 的端到端能力。您成功地在单个 GPU 上使用总参数量为 86B 的模型进行了推理，以高度一致性编辑图像，并训练了自定义适配器。