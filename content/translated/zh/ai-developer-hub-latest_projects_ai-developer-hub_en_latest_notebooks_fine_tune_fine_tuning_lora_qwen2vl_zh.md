---
title: "Fine-tuning with the Hugging Face ecosystem (TRL) &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/fine_tuning_lora_qwen2vl.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:49.922276+00:00
content_hash: "cb1020d8a5a459b4"
---

# 使用 Hugging Face 生态系统进行微调 (TRL)[#](#fine-tuning-with-the-hugging-face-ecosystem-trl)

**作者**: [Sergio Paniego](https://github.com/sergiopaniego)，并由 [AMD](https://www.amd.com) 修改以在 AMD GPU 上运行。

**知识水平**：中级

本笔记本演示了如何使用 Hugging Face 生态系统，特别是通过[参数高效微调（PEFT）](https://huggingface.co/docs/peft/index)和[Transformer 强化学习（TRL）](https://huggingface.co/docs/trl/index)库来微调[视觉语言模型（VLM）](https://huggingface.co/blog/vlms)。

**注意**：此笔记本源自 [fine_tuning_vlm_trl](https://huggingface.co/learn/cookbook/en/fine_tuning_vlm_trl)。

## 模型与数据集概述[#](#model-and-dataset-overview)

你将对 [Qwen2-VL-7B](https://qwenlm.github.io/blog/qwen2-vl/) 模型进行微调，使用的数据集是 [ChartQA](https://huggingface.co/datasets/HuggingFaceM4/ChartQA)。该数据集包含各种图表类型的图片及对应的问答对，非常适合用于增强模型的视觉问答能力。

## 前提条件[#](#prerequisites)

本教程是在以下环境中开发和测试的。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**：确保您的系统运行的是 Ubuntu 22.04 版本。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPU**：本教程已在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 上测试。请确保您使用的是支持 ROCm（ROCm（Radeon 开放计算平台）） 的 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 或兼容硬件，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.2**: 按照[ROCm（ROCm（Radeon 开放计算平台））安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html)安装并验证ROCm（ROCm（Radeon 开放计算平台））。安装后，使用以下命令确认设置：
此命令将列出您的AMD GPU及其相关详细信息。

**注意**：对于 ROCm（ROCm（Radeon 开放计算平台）） 6.4 及更早版本，请使用 `rocm-smi`

而改用命令。**Docker**: 确保 Docker 已正确安装和配置。请根据您的操作系统参考 Docker 安装指南。**Note**: 确保 Docker 权限配置正确。要配置权限以允许非 root 用户访问，请运行以下命令：usermod -aG docker $USER newgrp docker

验证Docker是否正常工作：

运行 hello-world

### Hugging Face API 访问[#](#hugging-face-api-access)

从...获取API token

[Hugging Face](https://huggingface.co) 用于下载模型。

### Weights & Biases API 访问[#](#weights-biases-api-access)

从...获取 API token

[Weights & Biases (W&B)](https://wandb.ai/)。

### 数据准备[#](#data-preparation)

本教程使用来自Hugging Face的示例数据集，该数据集在设置步骤中准备。

## 准备训练环境[#](#prepare-the-training-environment)

按照以下步骤设置训练环境。

### 1. 拉取 Docker 镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的 Docker 镜像：

```
pull rocm/pytorch:rocm6.2.3_ubuntu22.04_py3.10_pytorch_release_2.3.0
```

```

### 2. 启动Docker容器[#](#launch-the-docker-container)

运行以下命令来启动 Docker 容器。

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
--hostname=ROCm（ROCm（Radeon 开放计算平台））-FT \
-v $(pwd):/workspace \
-w /workspace/notebooks \
rocm/pytorch:rocm6.2.3_ubuntu22.04_py3.10_pytorch_release_2.3.0
```

```

**注意**：此命令将当前目录挂载到 `/workspace`

directory in the container. Ensure the notebook file is either copied to this directory before running the Docker command or uploaded into the Jupyter Notebook environment after it starts. Save the token or URL provided in the terminal output to access the notebook from your web browser. You can download this notebook from the [AI Developer Hub GitHub repository](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev-docs).

### 3. 安装并启动 Jupyter[#](#install-and-launch-jupyter)

在Docker容器内部，使用以下命令安装Jupyter：

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

在运行上述命令前，请确保该端口尚未被系统占用。若已占用，请通过替换 `--port=8888` 来指定其他端口。

使用另一个端口号，例如 `--port=8890`

.

### 4. 安装依赖项[#](#install-the-dependencies)

验证Torch库已安装且GPU可访问。

```
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
import torch
print("是否检测到ROCm（ROCm（Radeon 开放计算平台））-GPU？", torch.cuda.is_available())
print("检测到了多少个ROCm（ROCm（Radeon 开放计算平台））-GPU？", torch.cuda.device_count())
```

```

然后使用 `pip`

安装该库的以下依赖项。

```
# 安装微调所需库，包括参数高效微调（peft）和transformers
!pip install transformers==4.47.0 trl==0.12.0 peft==0.13.2 qwen-vl-utils==0.0.8 wandb==0.19.1 accelerate==1.1.1 ipywidgets==8.1.5 numpy==1.24.1 numba
```

```

验证安装:

```
# 检查所需库及其版本
!pip list | grep -E "transformers|trl|peft|qwen-vl-utils|wandb|accelerate|ipywidgets|numpy|numba"
```

```

### 5. 提供你的 Hugging Face token[#](#provide-your-hugging-face-token)

登录 Hugging Face 以上传您的微调模型。您需要通过 Hugging Face 账户进行身份验证，以便在此 notebook 中直接保存和共享您的模型。

```
from huggingface_hub import notebook_login
notebook_login()
```

```

验证您的令牌是否已被正确接受：

```
from huggingface_hub import HfApi
try:
api = HfApi()
user_info = api.whoami()
print(f"令牌验证成功！登录用户为：{user_info['name']}")
except Exception as e:
print(f"令牌验证失败。错误：{e}")
```

```

## 加载数据集[#](#load-the-dataset)

在本节中，您将加载 [HuggingFaceM4/ChartQA](https://huggingface.co/datasets/HuggingFaceM4/ChartQA) 数据集。该数据集包含图表图像及其相关问答对，非常适合用于视觉问答任务的训练。

接下来，为视觉语言模型（VLM）生成一条系统消息。该消息将创建一个系统，使其成为分析图表图像并根据这些图表提供简洁答案的专家。

**⚠️ 重要：确保选择了正确的内核**

如果验证过程失败，请确保为你的笔记本选择了正确的 Jupyter 内核。要更改内核，请按照以下步骤操作：

转到

内核函数 (Kernel)menu.Select

**更改内核函数 (Kernel)**选择

Python 3 (ipykernel)

从列表中。

未能选择正确的内核可能会导致运行笔记本时出现意外问题。

```
system_message = """你是一个专门从图表图像中解读视觉数据的视觉语言模型。
你的任务是分析所提供的图表图像，并针对查询给出简要答案，通常是一个单词、数字或短语。
图表包括多种类型（例如折线图、柱状图），并包含颜色、标签和文本。
专注于基于视觉信息提供准确、简洁的答案。除非绝对必要，否则避免额外解释。"""
```

```

将数据集格式化为用于交互的聊天机器人结构。每个交互包含一条系统消息，接着是图像和用户的查询，最后是查询的答案。

关于此模型的更多使用技巧，请参阅[模型卡片](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct#more-usage-tips)。

```
def format_data(sample):
return [
{
"role": "system",
"content": [
{
"type": "text",
"text": system_message
}
],
},
{
"role": "user",
"content": [
{
"type": "image",
"image": sample["image"],
},
{
"type": "text",
"text": sample['query'],
}
],
},
{
"role": "assistant",
"content": [
{
"type": "text",
"text": sample["label"][0]
}
],
},
]
```

```

出于教育目的，你仅需加载数据集中每个分组的10%。但在实际应用场景中，通常会加载全部样本。

```
from datasets import load_dataset
dataset_id = "HuggingFaceM4/ChartQA"
train_dataset, eval_dataset, test_dataset = load_dataset(dataset_id, split=['train[:10%]', 'val[:10%]', 'test[:10%]'])
```

```

接下来，查看数据集的结构。它包含一张图像、一个查询、一个标签（即答案）以及一个你将要丢弃的第四个特征。

```
train_dataset
```

```

使用聊天机器人结构格式化数据。这为模型适当地设置了交互方式。

```
train_dataset = [format_data(sample) for sample in train_dataset]
eval_dataset = [format_data(sample) for sample in eval_dataset]
test_dataset = [format_data(sample) for sample in test_dataset]
```

```

```
train_dataset[200]
```

```

## 加载模型并检查其性能[#](#load-the-model-and-check-its-performance)

在加载数据集之后，加载模型并使用数据集中的一个样本评估其性能。本教程使用 [Qwen/Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct)，这是一个能够理解视觉数据和文本的视觉语言模型 (VLM)。

```
import torch
from transformers import Qwen2VLForConditionalGeneration, Qwen2VLProcessor
model_id = "Qwen/Qwen2-VL-7B-Instruct"
```

```

接下来，加载模型和分词器以准备进行推理。

```
model = Qwen2VLForConditionalGeneration.from_pretrained(
model_id,
device_map="cuda",
torch_dtype=torch.bfloat16,
)
processor = Qwen2VLProcessor.from_pretrained(model_id)
```

```

为了评估模型的性能，使用数据集中的一个样本。首先，检查该样本的内部结构。

```
train_dataset[0]
```

```

使用没有系统消息的样本来评估VLM的原始理解。以下是使用的输入：

```
train_dataset[0][1:2]
```

```

现在查看样本对应的图表。你能基于视觉信息回答这个查询吗？

```
train_dataset[0][1]['content'][0]['image']
```

```

创建一个方法，该方法接受模型、处理器和样本作为输入，以生成模型的答案。这使您能够简化推理过程并轻松评估VLM的性能。

```python
from qwen_vl_utils import process_vision_info

def generate_text_from_sample(model, processor, sample, max_new_tokens=1024, device="cuda"):
    # 通过应用对话模板准备文本输入
    text_input = processor.apply_chat_template(
        sample[1:2],  # 使用不包含系统消息的样本
        tokenize=False,
        add_generation_prompt=True
    )
    # 从样本处理视觉输入
    image_inputs, _ = process_vision_info(sample)
    # 准备模型输入
    model_inputs = processor(
        text=[text_input],
        images=image_inputs,
        return_tensors="pt",
    ).to(device)  # 将输入移动到指定设备

    # 使用模型生成文本
    generated_ids = model.generate(**model_inputs, max_new_tokens=max_new_tokens)
    # 裁剪生成的ID以移除输入ID
    trimmed_generated_ids = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    # 解码输出文本
    output_text = processor.batch_decode(
        trimmed_generated_ids,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )
    return output_text[0]  # 返回第一个解码后的输出文本
```

```

```
# 示例：如何使用样本调用该方法：
output = generate_text_from_sample(model, processor, train_dataset[0], device="cuda")
```

```

虽然模型成功检索到正确的视觉信息，但在准确回答问题方面仍存在困难。这表明微调可能是提升其性能的关键。现在是时候进行微调过程了。

### 移除模型并清理GPU[#](#remove-the-model-and-clean-the-gpu)

在进入下一节训练模型之前，请清除当前变量并清理GPU以释放资源。

```
import gc
import time
def clear_memory():
# 如果当前全局作用域中存在变量，则删除它们
if 'inputs' in globals(): del globals()['inputs']
if 'model' in globals(): del globals()['model']
if 'processor' in globals(): del globals()['processor']
if 'trainer' in globals(): del globals()['trainer']
if 'peft_model' in globals(): del globals()['peft_model']
if 'bnb_config' in globals(): del globals()['bnb_config']
time.sleep(2)
# 垃圾回收并清理 CUDA（统一计算设备架构）内存
gc.collect()
time.sleep(2)
torch.cuda.empty_cache()
torch.cuda.synchronize()
time.sleep(2)
gc.collect()
time.sleep(2)
print(f"GPU 已分配内存: {torch.cuda.memory_allocated() / 1024**3:.2f} GB")
print(f"GPU 保留内存: {torch.cuda.memory_reserved() / 1024**3:.2f} GB")
clear_memory()
```

```

## 使用TRL微调模型[#](#fine-tune-the-model-using-trl)

按照以下步骤微调您的模型。

### 1. 加载模型用于训练[#](#load-the-model-for-training)

首先，加载原始模型。

**注意**：或者，可以通过使用 [bitsandbytes](https://huggingface.co/docs/bitsandbytes/main/en/index) 加载量化模型。要了解关于量化的更多信息，请参阅 [Hugging Face 的这篇博文](https://huggingface.co/blog/merve/quantization) 或 [Maarten Grootendorst 的这篇文章](https://www.maartengrootendorst.com/blog/quantization/)。

```
model = Qwen2VLForConditionalGeneration.from_pretrained(
model_id,
device_map="cuda",
torch_dtype=torch.bfloat16
).half()
processor = Qwen2VLProcessor.from_pretrained(model_id)
```

```

### 2. 设置 LoRA 和 SFTConfig[#](#set-up-lora-and-sftconfig)

接下来，为训练配置设置 LoRA。LoRA 通过应用低秩近似来减少内存使用，从而进一步降低内存需求并提升训练效率，使其成为在保证模型质量的前提下优化性能的绝佳选择。

```python
from peft import LoraConfig, get_peft_model
# 配置 LoRA
peft_config = LoraConfig(
    lora_alpha=16,
    lora_dropout=0.05,
    r=8,
    bias="none",
    target_modules=["q_proj", "v_proj"],
    task_type="CAUSAL_LM",
)
# 应用 PEFT 模型适配
peft_model = get_peft_model(model, peft_config)
# 打印可训练参数
peft_model.print_trainable_parameters()
```

```

使用监督微调（Supervised Fine-tuning, SFT）来优化模型在特定任务上的性能。为此，使用 [TRL 库](https://huggingface.co/docs/trl/index)中的 [SFTConfig](https://huggingface.co/docs/trl/sft_trainer) 类定义训练参数。SFT 提供带标签的数据，帮助模型学习根据输入生成更准确的响应。这种方法确保模型针对您的特定用例进行定制，从而在理解和响应视觉查询方面获得更好的性能。

```python
from trl import SFTConfig
# 配置训练参数
training_args = SFTConfig(
output_dir="qwen2-7b-instruct-trl-sft-ChartQA", # 保存模型的目录
num_train_epochs=3, # 训练轮数
per_device_train_batch_size=4, # 每个设备的训练批量大小
per_device_eval_batch_size=4, # 每个设备的评估批量大小
gradient_accumulation_steps=8, # 梯度累积步数
gradient_checkpointing=True, # 启用梯度检查点以节省内存
# 优化器和调度器设置
optim="adamw_torch_fused", # 优化器类型
# optim = "adamw_hf",
learning_rate=2e-4, # 训练学习率
lr_scheduler_type="constant", # 学习率调度器类型
# 日志记录和评估
logging_steps=1, # 日志记录步数间隔
eval_steps=10, # 评估步数间隔
eval_strategy="steps", # 评估策略
save_strategy="steps", # 保存模型策略
save_steps=20, # 保存步数间隔
metric_for_best_model="eval_loss", # 评估最佳模型的指标
greater_is_better=False, # 指标值是否越大越好
load_best_model_at_end=True, # 训练结束后加载最佳模型
# 混合精度和梯度设置
bf16=False, # 使用bfloat16精度
fp16=True, # 使用float16精度
tf32=False, # 使用TensorFloat-32精度
max_grad_norm=0.3, # 梯度裁剪的最大范数
warmup_ratio=0.03, # 预热步数占总步数的比例
# Hub和报告
push_to_hub=False, # 是否将模型推送到Hugging Face Hub，默认禁用
report_to=None, # 用于跟踪指标的报告工具
# 梯度检查点设置
gradient_checkpointing_kwargs={"use_reentrant": False}, # 梯度检查点选项
# 数据集配置
dataset_text_field="", # 数据集中的文本字段
dataset_kwargs={"skip_prepare_dataset": True}, # 其他数据集选项
#max_seq_length=1024 # 输入的最大序列长度
)
training_args.remove_unused_columns = False # 保留数据集中的未使用列
```

```

### 3. 训练模型[#](#training-the-model)

你可以使用 [Weights & Biases (W&B)](https://wandb.ai/) 记录训练进度。将你的笔记本连接到W&B，以捕获训练过程中的关键信息。

```
import wandb
wandb.init(
project="qwen2-7b-instruct-trl-sft-ChartQA", # 修改这里
name="qwen2-7b-instruct-trl-sft-ChartQA", # 修改这里
config=training_args,
)
```

```

模型需要一个 collator 函数，以在训练过程中正确检索和批量处理数据。该函数负责格式化数据集的输入，确保其结构正确。请在下方定义 collator 函数。

如需更多详情，请参阅 TRL 示例 [scripts](https://github.com/huggingface/trl/blob/main/examples/scripts/sft_vlm.py#L87)。

```
# 创建一个数据收集器，用于编码文本和图像对
def collate_fn(examples):
# 获取文本和图像，并应用聊天模板
texts = [processor.apply_chat_template(example, tokenize=False) for example in examples] # 准备要处理的文本
image_inputs = [process_vision_info(example)[0] for example in examples] # 处理图像以提取输入
# 对文本进行分词并处理图像
batch = processor(text=texts, images=image_inputs, return_tensors="pt", padding=True) # 将文本和图像编码为张量
# 标签就是 input_ids，并在损失计算中屏蔽填充标记
labels = batch["input_ids"].clone() # 克隆输入 ID 作为标签
labels[labels == processor.tokenizer.pad_token_id] = -100 # 在标签中屏蔽填充标记
# 在损失计算中忽略图像标记索引（特定于模型）
if isinstance(processor, Qwen2VLProcessor): # 检查处理器是否为 Qwen2VLProcessor
image_tokens = [151652, 151653, 151655] # Qwen2VLProcessor 的特定图像标记 ID
else:
image_tokens = [processor.tokenizer.convert_tokens_to_ids(processor.image_token)] # 将图像标记转换为 ID
# 在标签中屏蔽图像标记 ID
for image_token_id in image_tokens:
labels[labels == image_token_id] = -100 # 在标签中屏蔽图像标记 ID
batch["labels"] = labels # 将标签添加到批次中
return batch # 返回准备好的批次
```

```

现在，定义 [SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)，它是 [Transformers Trainer](https://huggingface.co/docs/transformers/main_classes/trainer) 类的封装，并继承其属性和方法。此类通过在接受 [PeftConfig](https://huggingface.co/docs/peft/v0.6.0/en/package_reference/config#peft.PeftConfig) 对象时正确初始化 [PeftModel](https://huggingface.co/docs/peft/v0.6.0/package_reference/peft_model) 来简化微调过程。通过使用 `SFTTrainer`

您可以高效管理训练工作流，并确保获得流畅的视觉语言模型微调体验。

```
from trl import SFTTrainer
trainer = SFTTrainer(
model=model,
args=training_args,
train_dataset=train_dataset,
eval_dataset=eval_dataset,
data_collator=collate_fn,
peft_config=peft_config,
tokenizer=processor.tokenizer,
)
```

```

现在是时候训练模型了！

```
trainer.train()
```

```

然后保存结果。

```
trainer.save_model(training_args.output_dir)
```

```

## 测试微调后的模型[#](#testing-the-fine-tuned-model)

现在您已经成功微调了视觉语言模型（VLM），接下来需要评估其性能。本部分使用 ChartQA 数据集中的示例来测试模型，观察它基于图表图像回答问题的效果。这为探索结果提供了有效途径。

清理 GPU 内存以确保最佳性能：

clear_memory()

```

然后使用与之前相同的pipeline重新加载基础模型。

```
model = Qwen2VLForConditionalGeneration.from_pretrained(
model_id,
device_map="cuda",
torch_dtype=torch.bfloat16,
)
processor = Qwen2VLProcessor.from_pretrained(model_id)
```

```

将训练好的适配器附加到预训练模型上。该适配器包含训练期间所做的微调调整，使得基础模型能够利用新知识，同时不改变其核心参数。集成适配器增强了模型的能力，同时保持其原始结构。

```
import os
os.getcwd()
```

```

```
adapter_path = "./qwen2-7b-instruct-trl-sft-ChartQA"
model.load_adapter(adapter_path)
```

```

使用数据集中模型最初难以正确回答的前一个样本。

```train_dataset[0][:2]```

```

```
train_dataset[0][1]['content'][0]['image']
```

```

```
output = generate_text_from_sample(model, processor, train_dataset[0])
```

```

这个样本来自训练集，因此模型在训练过程中已经见过它。这可以被视为一种作弊行为。为了更全面地了解模型的性能，请使用一个未见过的样本进行评估。

```
test_dataset[10][:2]
```

```

```
test_dataset[10][1]['content'][0]['image']
```

```

```output = generate_text_from_sample(model, processor, test_dataset[10])```

```

模型已成功学会按照数据集中的指定方式响应查询。您已达成目标！

## 比较微调模型与带提示的基础模型[#](#compare-a-fine-tuned-model-versus-a-base-model-with-prompting)

您已经了解了微调VLM是使其适应特定需求的一种有价值的选择。另一种值得考虑的方法是直接使用提示或实现RAG系统，这将在另一篇[recipe](https://huggingface.co/learn/cookbook/multimodal_rag_using_document_retrieval_and_vlms)中介绍。

微调VLM需要大量的数据和计算资源，这可能会产生成本。相比之下，你可以尝试通过提示来观察是否能在没有微调开销的情况下达到类似的结果。

再次清理GPU内存以确保最佳性能。

```
clear_memory()
```

```

首先，按照之前的流程加载基线模型。

```
model = Qwen2VLForConditionalGeneration.from_pretrained(
model_id,
device_map="cuda",
torch_dtype=torch.bfloat16,
)
processor = Qwen2VLProcessor.from_pretrained(model_id)
```

```

该案例再次使用了之前的样本，但这次包含了如下所示的系统消息。这一增强有助于为输入提供上下文，从而可能提高模型的响应准确性。

```
train_dataset[0][:2]
```

```

现在看看它的表现如何：

```
text = processor.apply_chat_template(
train_dataset[0][:2], tokenize=False, add_generation_prompt=True
)
image_inputs, _ = process_vision_info(train_dataset[0])
inputs = processor(
text=[text],
images=image_inputs,
return_tensors="pt",
)
inputs = inputs.to("cuda")
generated_ids = model.generate(**inputs, max_new_tokens=1024)
generated_ids_trimmed = [out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)]
output_text = processor.batch_decode(
generated_ids_trimmed,
skip_special_tokens=True,
clean_up_tokenization_spaces=False
)
output_text[0]
```

```

正如所示，该模型使用预训练模型及额外的系统消息生成正确答案，无需任何训练。根据具体用例，这种方法可作为微调的一个可行的替代方案。