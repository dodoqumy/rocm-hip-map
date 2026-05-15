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

# 使用 Hugging Face 生态系统 (TRL) 进行微调[#](#fine-tuning-with-the-hugging-face-ecosystem-trl)

**作者**：[Sergio Paniego](https://github.com/sergiopaniego)，并由 [AMD](https://www.amd.com) 修改以在 AMD GPU 上运行。

**知识水平**：中级

这个笔记本演示了如何使用Hugging Face生态系统微调一个[视觉语言模型 (VLM)](https://huggingface.co/blog/vlms)，具体使用了[参数高效微调 (PEFT)](https://huggingface.co/docs/peft/index)和[Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index)库。

**注意**：本笔记本源自[fine_tuning_vlm_trl](https://huggingface.co/learn/cookbook/en/fine_tuning_vlm_trl)。

## 模型和数据集概述[#](#model-and-dataset-overview)

你将基于 [ChartQA](https://huggingface.co/datasets/HuggingFaceM4/ChartQA) 数据集对 [Qwen2-VL-7B](https://qwenlm.github.io/blog/qwen2-vl/) 模型进行微调。该数据集包含多种图表类型的图像及其对应的问题-答案对，非常适合增强模型的视觉问答能力。

## 先决条件[#](#prerequisites)

本教程是使用以下配置开发和测试的。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**：确保你的系统运行的是 Ubuntu 22.04 版本。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPUs**：本教程已在 AMD Instinct MI300X GPU 上完成测试。请确保您使用的是支持 ROCm 的 AMD Instinct GPU 或兼容硬件，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.2**：按照[ROCm（ROCm（Radeon 开放计算平台）） 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html)安装并验证ROCm（ROCm（Radeon 开放计算平台））。安装后，使用以下命令确认您的设置：该命令将列出您的AMD GPU及其相关信息。

**注意**：对于 ROCm 6.4 及更早版本，请使用 `rocm-smi`

command instead。  
**Docker**：确保 Docker 已正确安装和配置。请遵循适用于您操作系统的 Docker 安装指南。  
**注意**：确保 Docker 权限配置正确。要配置权限以允许非 root 用户访问，请运行以下命令：  
usermod -aG docker $USER  
newgrp docker

验证 Docker 是否正常工作：

运行 hello-world

### Hugging Face API 访问[#](#hugging-face-api-access)

从...获取API token

[Hugging Face](https://huggingface.co)用于下载模型。

### Weights & Biases API 访问[#](#weights-biases-api-access)

获取 API token 来自

[Weights & Biases (W&B)](https://wandb.ai/)。

### 数据准备[#](#data-preparation)

本教程使用了来自 Hugging Face 的示例数据集，该数据集在设置步骤中准备完成。

## 准备训练环境[#](#prepare-the-training-environment)

按照以下步骤设置训练环境。

### 1. 拉取Docker镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的 Docker 镜像：

```
pull rocm/pytorch:rocm6.2.3_ubuntu22.04_py3.10_pytorch_release_2.3.0
```

```

### 2. 启动 Docker 容器[#](#launch-the-docker-container)

运行此命令以启动 Docker 容器。

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

容器中的目录。确保在运行 Docker 命令之前将笔记本文件复制到此目录，或者在 Jupyter Notebook 环境启动后将其上传。保存终端输出中提供的令牌或 URL，以便从 Web 浏览器访问笔记本。您可以从 [AI Developer Hub GitHub 仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev-docs) 下载此笔记本。

### 3. 安装并启动 Jupyter[#](#install-and-launch-jupyter)

在Docker容器内，使用以下命令安装Jupyter：

```
安装 Jupyter
```

```

启动 Jupyter 服务器：

--ip=0.0.0.0 --port=8888 --no-browser --allow-root

```

**注意**：确保端口 `8888`

在运行上述命令之前，请确保该端口未在您的系统上被占用。如果已被占用，请通过替换 `--port=8888` 来指定一个不同的端口。

使用另一个端口号，例如 `--port=8890`

。

### 4. 安装依赖项[#](#install-the-dependencies)

验证Torch库是否已安装且GPU可访问。

```
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
import torch
print("检测到ROCm（ROCm（Radeon 开放计算平台））GPU吗？", torch.cuda.is_available())
print("检测到多少个ROCm（ROCm（Radeon 开放计算平台））GPU？", torch.cuda.device_count())
```

```

然后使用 `pip`

安装该库的以下依赖项。

```
# 安装微调所需的库，包括参数高效微调（peft）和 transformers
!pip install transformers==4.47.0 trl==0.12.0 peft==0.13.2 qwen-vl-utils==0.0.8 wandb==0.19.1 accelerate==1.1.1 ipywidgets==8.1.5 numpy==1.24.1 numba
```

```

验证安装：

```
# 检查所需的库及其版本
!pip list | grep -E "transformers|trl|peft|qwen-vl-utils|wandb|accelerate|ipywidgets|numpy|numba"
```

```

### 5. 提供您的 Hugging Face 令牌[#](#provide-your-hugging-face-token)

登录Hugging Face以上传微调后的模型。你需要使用Hugging Face账户进行身份验证，以便直接从本notebook保存和分享模型。

```
from huggingface_hub import notebook_login
notebook_login()
```

```

验证您的令牌是否已被正确接受：

```python
from huggingface_hub import HfApi
try:
    api = HfApi()
    user_info = api.whoami()
    print(f"令牌验证成功！登录为：{user_info['name']}")
except Exception as e:
    print(f"令牌验证失败。错误：{e}")
```

```

## 加载数据集[#](#load-the-dataset)

在此部分，您将加载 [HuggingFaceM4/ChartQA](https://huggingface.co/datasets/HuggingFaceM4/ChartQA) 数据集。该数据集包含图表图像及其对应的问题与答案，非常适合用于训练视觉问答任务。

You are an expert in analyzing chart images. Your task is to examine the provided chart thoroughly and answer questions about it concisely and accurately. Focus on key trends, data points, and insights directly relevant to the question. Avoid unnecessary commentary or speculation. Keep responses brief and to the point.

⚠️ 重要：确保选择了正确的内核

如果验证过程失败，请确保为您的笔记本选择了正确的 Jupyter 内核。要更改内核，请按照以下步骤操作：

转到

**内核函数 (Kernel)**menu.Select

**更改内核函数 (Kernel)**选择

`Python 3（ipykernel）`

从列表中。

**未能选择正确的内核可能在运行笔记本时导致意外问题。**

```system_message = """你是一个专门从图表图像中解读视觉数据的视觉语言模型。
你的任务是分析提供的图表图像，并以简洁的回答回应查询，通常是一个单词、数字或短语。
图表包含多种类型（例如折线图、柱状图），并包含颜色、标签和文本。
专注于基于视觉信息提供准确、简洁的回答。除非绝对必要，避免额外解释。"""```

```

将数据集格式化为聊天机器人交互结构。每个交互包含一条系统消息，随后是图像和用户查询，最后是对查询的回答。

针对此模型的更多使用技巧，请参阅[模型卡](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct#more-usage-tips)。

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

出于教育目的，您只会加载数据集中每个分片的10%。然而，在实际应用场景中，您通常会加载所有样本。

```
from datasets import load_dataset
dataset_id = "HuggingFaceM4/ChartQA"
train_dataset, eval_dataset, test_dataset = load_dataset(dataset_id, split=['train[:10%]', 'val[:10%]', 'test[:10%]'])
```

```

接下来，查看数据集的结构。它包括一个图像、一个查询、一个标签（即答案），以及一个将要丢弃的第四个特征。

```
train_dataset
```

```

使用聊天机器人结构格式化数据。这将为模型适当地设置交互。

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

加载数据集后，加载模型并使用数据集中的样本评估其性能。本教程使用 [Qwen/Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct)，这是一个能够同时理解视觉数据与文本的视觉语言模型（VLM）。

```
import torch
from transformers import Qwen2VLForConditionalGeneration, Qwen2VLProcessor
model_id = "Qwen/Qwen2-VL-7B-Instruct"
```

```

接下来，加载模型和分词器以准备推理。

```
model = Qwen2VLForConditionalGeneration.from_pretrained(
model_id,
device_map="cuda",
torch_dtype=torch.bfloat16,
)
processor = Qwen2VLProcessor.from_pretrained(model_id)
```

```

为了评估模型的性能，请使用数据集中的一个样本。首先，检查该样本的内部结构。

```
train_dataset[0]
```

```

使用没有系统消息的样本来评估VLM的原始理解。这是使用的输入：

```
train_dataset[0][1:2]
```

```

现在查看与样本对应的图表。你能基于视觉信息回答该查询吗？

```
train_dataset[0][1]['content'][0]['image']
```

```

创建一个方法，该方法以模型、处理器和样本作为输入，生成模型的答案。这可以让你简化推理过程，并轻松评估VLM的性能。

```
from qwen_vl_utils import process_vision_info
def generate_text_from_sample(model, processor, sample, max_new_tokens=1024, device="cuda"):
    # 准备文本输入：应用聊天模板
    text_input = processor.apply_chat_template(
        sample[1:2], # 使用不含系统消息的样本
        tokenize=False,
        add_generation_prompt=True
    )
    # 处理样本中的视觉输入
    image_inputs, _ = process_vision_info(sample)
    # 准备模型输入
    model_inputs = processor(
        text=[text_input],
        images=image_inputs,
        return_tensors="pt",
    ).to(device) # 将输入移动到指定设备
    # 使用模型生成文本
    generated_ids = model.generate(**model_inputs, max_new_tokens=max_new_tokens)
    # 裁剪生成的 token ID，去除输入 ID 部分
    trimmed_generated_ids = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    # 解码输出文本
    output_text = processor.batch_decode(
        trimmed_generated_ids,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )
    return output_text[0] # 返回解码后的第一个输出文本
```

```

```
# Example of how to call the method with sample:
output = generate_text_from_sample(model, processor, train_dataset[0], device="cuda")
```

```

尽管模型成功检索到了正确的视觉信息，但在准确回答问题时仍存在困难。这表明微调（fine-tuning）可能是提升其性能的关键。现在是时候开始微调过程了。

### Remove the model and clean the GPU[#](#remove-the-model-and-clean-the-gpu)

在进入下一节训练模型之前，清除当前变量并清理 GPU 以释放资源。

```
import gc
import time
def clear_memory():
    # 如果变量存在于当前全局作用域中，则删除它们
    if 'inputs' in globals(): del globals()['inputs']
    if 'model' in globals(): del globals()['model']
    if 'processor' in globals(): del globals()['processor']
    if 'trainer' in globals(): del globals()['trainer']
    if 'peft_model' in globals(): del globals()['peft_model']
    if 'bnb_config' in globals(): del globals()['bnb_config']
    time.sleep(2)
    # 垃圾回收并清理 CUDA 内存
    gc.collect()
    time.sleep(2)
    torch.cuda.empty_cache()
    torch.cuda.synchronize()
    time.sleep(2)
    gc.collect()
    time.sleep(2)
    print(f"GPU 已分配内存: {torch.cuda.memory_allocated() / 1024**3:.2f} GB")
    print(f"GPU 已预留内存: {torch.cuda.memory_reserved() / 1024**3:.2f} GB")
clear_memory()
```

```

## 使用TRL对模型进行微调[#](#fine-tune-the-model-using-trl)

按照以下步骤对您的模型进行微调。

### 1. 加载模型以进行训练[#](#load-the-model-for-training)

首先，加载原始模型。

**注意**：或者，也可以使用 [bitsandbytes](https://huggingface.co/docs/bitsandbytes/main/en/index) 来加载量化模型。要了解更多关于量化的信息，请参阅 [Hugging Face 的这篇博客](https://huggingface.co/blog/merve/quantization) 或 [Maarten Grootendorst 的这篇文章](https://www.maartengrootendorst.com/blog/quantization/)。

```
model = Qwen2VLForConditionalGeneration.from_pretrained(
model_id,
device_map="cuda",
torch_dtype=torch.bfloat16
).half()
processor = Qwen2VLProcessor.from_pretrained(model_id)
```

```

### 2. 设置LoRA和SFTConfig[#](#set-up-lora-and-sftconfig)

接下来，为训练配置LoRA。LoRA通过应用低秩近似来减少内存使用，从而进一步降低内存需求并提高训练效率，这使得它成为优化模型性能且不牺牲质量的绝佳选择。

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

使用监督式微调（SFT）来提升模型在任务上的性能。为此，利用 [TRL 库](https://huggingface.co/docs/trl/index)中的 [SFTConfig](https://huggingface.co/docs/trl/sft_trainer) 类定义训练参数。SFT 提供标注数据，帮助模型根据输入学习生成更准确的回答。这种方法确保模型针对您的特定用例进行定制，从而在理解和响应视觉查询方面获得更好性能。

```
from trl import SFTConfig
# 配置训练参数
training_args = SFTConfig(
output_dir="qwen2-7b-instruct-trl-sft-ChartQA", # 保存模型的目录
num_train_epochs=3, # 训练轮数
per_device_train_batch_size=4, # 每个设备的训练批次大小
per_device_eval_batch_size=4, # 每个设备的评估批次大小
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
save_strategy="steps", # 模型保存策略
save_steps=20, # 保存步数间隔
metric_for_best_model="eval_loss", # 评估最佳模型的指标
greater_is_better=False, # 指标值是否越大越好
load_best_model_at_end=True, # 训练结束后加载最佳模型
# 混合精度和梯度设置
bf16=False, # 使用 bfloat16 精度
fp16=True, # 使用 float16 精度
tf32=False, # 使用 TensorFloat-32 精度
max_grad_norm=0.3, # 梯度裁剪的最大范数
warmup_ratio=0.03, # 预热步数占总步数的比例
# Hub 和报告
push_to_hub=False, # 是否将模型推送到 Hugging Face Hub，默认禁用。
report_to=None, # 用于跟踪指标的报告工具
# 梯度检查点设置
gradient_checkpointing_kwargs={"use_reentrant": False}, # 梯度检查点的选项
# 数据集配置
dataset_text_field="", # 数据集中的文本字段
dataset_kwargs={"skip_prepare_dataset": True}, # 额外的数据集选项
#max_seq_length=1024 # 输入的最大序列长度
)
training_args.remove_unused_columns = False # 保留数据集中未使用的列
```

```

### 3. 训练模型[#](#training-the-model)

您可以使用 [Weights & Biases (W&B)](https://wandb.ai/) 记录训练进度。将笔记本连接到 W&B，以便在训练期间捕获关键信息。

```
import wandb
wandb.init(
project="qwen2-7b-instruct-trl-sft-ChartQA", # 修改此处
name="qwen2-7b-instruct-trl-sft-ChartQA", # 修改此处
config=training_args,
)
```

```

模型需要一个collator函数，以便在训练过程中正确地检索和批处理数据。该函数将数据集的输入格式化为模型所需的格式，确保它们结构正确。在下方定义collator函数。

欲了解更多详情，请参见TRL示例[scripts](https://github.com/huggingface/trl/blob/main/examples/scripts/sft_vlm.py#L87)。

```python
# 创建一个数据整理器，用于编码文本和图像对
def collate_fn(examples):
    # 获取文本和图像，并应用聊天模板
    texts = [processor.apply_chat_template(example, tokenize=False) for example in examples]  # 准备待处理的文本
    image_inputs = [process_vision_info(example)[0] for example in examples]  # 处理图像以提取输入

    # 对文本进行分词并处理图像
    batch = processor(text=texts, images=image_inputs, return_tensors="pt", padding=True)  # 将文本和图像编码为张量

    # 标签为 input_ids，并在损失计算中屏蔽填充令牌
    labels = batch["input_ids"].clone()  # 为标签克隆 input_ids
    labels[labels == processor.tokenizer.pad_token_id] = -100  # 在标签中屏蔽填充令牌

    # 在损失计算中忽略图像令牌索引（模型特定）
    if isinstance(processor, Qwen2VLProcessor):  # 检查 processor 是否为 Qwen2VLProcessor
        image_tokens = [151652, 151653, 151655]  # Qwen2VLProcessor 的特定图像令牌 ID
    else:
        image_tokens = [processor.tokenizer.convert_tokens_to_ids(processor.image_token)]  # 将图像令牌转换为 ID

    # 在标签中屏蔽图像令牌 ID
    for image_token_id in image_tokens:
        labels[labels == image_token_id] = -100  # 在标签中屏蔽图像令牌 ID

    batch["labels"] = labels  # 将标签添加到批次
    return batch  # 返回准备好的批次
```

```

现在，定义 [SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)，它是 [Transformers Trainer](https://huggingface.co/docs/transformers/main_classes/trainer) 类的包装器，并继承其属性和方法。该类通过在接受 [PeftConfig](https://huggingface.co/docs/peft/v0.6.0/en/package_reference/config#peft.PeftConfig) 对象时正确初始化 [PeftModel](https://huggingface.co/docs/peft/v0.6.0/package_reference/peft_model)，简化了微调过程。通过使用 `SFTTrainer`

，您可以高效管理训练工作流，并确保为 Vision Language Model 提供顺畅的微调体验。

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

现在您已经成功微调了视觉语言模型（VLM），是时候评估其性能了。本节使用ChartQA数据集中的示例对模型进行测试，以了解它在基于图表图像回答问题方面的表现。这提供了一个探索结果的好方法。

清理 GPU memory 以确保最佳性能：

```
clear_memory()
```

```

然后使用与之前相同的流水线重新加载基础模型。

```
model = Qwen2VLForConditionalGeneration.from_pretrained(
model_id,
device_map="cuda",
torch_dtype=torch.bfloat16,
)
processor = Qwen2VLProcessor.from_pretrained(model_id)
```

```

将训练好的适配器附加到预训练模型上。该适配器包含了你在训练期间所做的微调调整，使基础模型能够利用新知识而不改变其核心参数。集成适配器增强了模型的能力，同时保持了其原始结构。

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

train_dataset[0][:2]

```

```
train_dataset[0][1]['content'][0]['image']
```

```

```
output = generate_text_from_sample(model, processor, train_dataset[0])
```

```

此样本取自训练集，因此模型在训练过程中已见过该样本。这可以被视为一种作弊行为。为了更全面地了解模型性能，请使用未见过的样本对其进行评估。

```
test_dataset[10][:2]
```

```

```
test_dataset[10][1]['content'][0]['image']
```

```

```
output = generate_text_from_sample(model, processor, test_dataset[10])
```

```

模型已成功学习如何根据数据集中的指定查询进行响应。你已达到目标！

## 通过提示对比微调模型与基础模型[#](#compare-a-fine-tuned-model-versus-a-base-model-with-prompting)

你已经探索了微调VLM如何成为适配特定需求的有价值选项。另一种值得考虑的方法是直接使用提示或实施RAG系统，这在另一篇[指南](https://huggingface.co/learn/cookbook/multimodal_rag_using_document_retrieval_and_vlms)中有介绍。

微调视觉语言模型（VLM）需要大量的数据和计算资源，这可能产生高昂成本。相比之下，你可以尝试使用提示（prompting）来观察是否能在没有微调开销的情况下获得类似结果。

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

本示例再次使用了之前的样本，但这次包含如下的系统消息。这一增强有助于为模型提供输入上下文，有可能提高其响应准确性。

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

如所示，该模型使用预训练模型以及额外的系统消息生成了正确的回答，无需任何训练。这种方法可以作为微调的可行替代方案，具体取决于用例。