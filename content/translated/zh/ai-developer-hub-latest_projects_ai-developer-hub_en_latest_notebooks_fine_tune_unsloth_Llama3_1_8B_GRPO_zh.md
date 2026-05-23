---
title: "Train your own R1 reasoning model with Unsloth &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/unsloth_Llama3_1_8B_GRPO.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:45.173066+00:00
content_hash: "3e79e76e08141f28"
---

# 使用Unsloth训练您自己的R1推理模型[#](#train-your-own-r1-reasoning-model-with-unsloth)

**作者**: [Unsloth](https://unsloth.ai) 并由 [AMD](https://www.amd.com) 修改以在 AMD GPU 上运行。

**知识水平**：中级

本教程演示如何利用 [Unsloth](https://unsloth.ai) 在 AMD ROCm（ROCm（Radeon 开放计算平台））GPU 上微调 Llama-3.1 8B 大型语言模型（LLM）。DeepSeek 的 R1 研究揭示了一个“aha moment”（顿悟时刻），其中 R1-Zero 通过使用组相对策略优化（Group Relative Policy Optimization，GRPO）自主学会了无需人类反馈即可分配更多思考时间。Unsloth 团队对整个 GRPO 流程进行了增强，使其显存占用比 Hugging Face 和 Flash Attention 2 (FA2) 减少 80%。这使得您能够仅用 7GB 显存，借助 Qwen2.5 (1.5B) 复现 R1-Zero 的成就。

## 前提条件[#](#prerequisites)

本教程使用以下设置进行开发和测试。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**：确保您的系统正在运行 Ubuntu 22.04 版本。

### 硬件[#](#hardware)

**AMD Instinct（AMD 数据中心 GPU 系列）™ GPUs**：本教程已在 AMD Instinct（AMD 数据中心 GPU 系列）MI300X GPU 上完成测试。请确保您使用的 AMD Instinct（AMD 数据中心 GPU 系列）GPU 或兼容硬件支持 ROCm（ROCm（Radeon 开放计算平台）），并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.3**：按照 [ROCm 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm。安装完成后，使用以下命令确认配置：该命令将列出您的 AMD GPU 及相关详细信息。

**注意**：对于 ROCm（Radeon 开放计算平台）6.4 及更早版本，请使用 `rocm-smi`

命令代替。**Docker**：确保Docker已正确安装并配置。请遵循适用于您操作系统的Docker安装指南。**注意**：确保Docker权限已正确配置。要配置允许非root用户访问的权限，请运行以下命令：`usermod -aG docker $USER` `newgrp docker`

验证Docker是否正常工作：

运行 hello-world

### Hugging Face API 访问[#](#hugging-face-api-access)

从...获取API token

[Hugging Face](https://huggingface.co) 用于下载模型。确保 Hugging Face API 令牌具有必要的权限和批准以访问

[Meta Llama 检查点](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).

### 数据准备[#](#data-preparation)

本教程使用来自 Hugging Face 的示例数据集，该数据集在设置步骤中准备。

## 准备训练环境[#](#prepare-the-training-environment)

### 1. 拉取Docker镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的Docker镜像：

```
pull rocm/vllm-dev:main
```

```

### 2. 启动 Docker 容器[#](#launch-the-docker-container)

启动Docker容器并映射必要的目录。替换`/path/to/notebooks`。

使用宿主机上存储这些 notebooks 的目录的完整路径。

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
rocm/vllm-dev:main
```

```

**注意**：此命令将当前目录挂载到 `/workspace`

在容器中的目录。请确保在运行 Docker 命令之前将笔记本文件复制到此目录，或者在 Jupyter Notebook 环境启动后上传该文件。保存在终端输出中提供的令牌或 URL，以便从您的网页浏览器访问笔记本。您可以从 [AI Developer Hub GitHub repository](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev) 下载此笔记本。

### 3. 安装并启动 Jupyter[#](#install-and-launch-jupyter)

在 Docker 容器中，使用以下命令安装 Jupyter：

```install jupyter```

```

启动 Jupyter 服务器：

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

**注意**: 确保端口 `8888`

在运行上述命令之前，请确保该端口尚未在您的系统上使用。如果已被使用，您可以通过替换 `--port=8888` 来指定不同的端口。

使用另一个端口号，例如 `--port=8890`

规则：
1. 保留所有 Markdown 格式、代码块、内联代码和链接不变。
2. 保持诸如 ROCm、HIP、GPU、CUDA、AMD、PyTorch、TensorFlow 等技术术语的英文原样。
3. 保持 API 名称、函数名称、文件路径、命令不变。
4. 仅输出翻译——不作解释、注释或前言。
5. 使用 GPU 开发者所期望的技术中文。

### 4. 安装所需的库[#](#install-the-required-libraries)

安装本教程所需的库。在Docker容器内运行的Jupyter notebook中执行以下命令：

```bash
# 从源代码安装 Unsloth
!git clone https://github.com/billishyahao/unsloth.git && cd unsloth && git checkout billhe/rocm && pip install .
!pip install unsloth_zoo==2025.3.17
# 从源代码安装 ROCm（ROCm（Radeon 开放计算平台）） Bitsandbytes
!git clone --recurse https://github.com/ROCm（ROCm（Radeon 开放计算平台））/bitsandbytes && cd bitsandbytes && git checkout rocm_enabled_multi_backend && pip install -r requirements-dev.txt && cmake -DCOMPUTE_BACKEND=hip -S . && make -j && pip install .
# 此笔记本在 unsloth==2025.3.19 unsloth_zoo==2025.3.17 bitsandbytes==0.43.3.dev0 下验证通过
```

```

验证安装：

```
# 验证所需库的安装和版本
!pip list | grep unsloth
```

```

这里是预期的输出：

unsloth 2025.3.19
unsloth_zoo 2025.3.17

```

**⚠️ 重要**: 确保选择了正确的内核

如果验证过程失败，请确保为您的notebook选择了正确的Jupyter内核。要更改内核，请执行以下步骤：

前往

内核函数 (Kernel)menu.Select

**更改内核函数 (Kernel)**.选择

Python 3 (ipykernel)

从列表中。

**重要**：未选择正确的内核可能导致运行 notebook 时出现意外问题。

### 5. 提供您的 Hugging Face token[#](#provide-your-hugging-face-token)

您将需要一个Hugging Face API令牌来访问Llama-3.1。在[Hugging Face Tokens](https://huggingface.co/settings/tokens)处生成您的令牌，并为[Llama-3.1 8B](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)请求访问权限。令牌通常以“hf_”开头。

在您的Jupyter notebook中运行以下交互块以设置令牌：

**注意**：取消勾选“Add token as Git credential”选项。

```
from huggingface_hub import notebook_login, HfApi
# 提示用户登录
notebook_login()
```

```

```
from huggingface_hub import HfApi
try:
    api = HfApi()
    user_info = api.whoami()
    print(f"令牌验证成功！已登录为：{user_info['name']}")
except Exception as e:
    print(f"令牌验证失败。错误：{e}")
```

```

## 运行GRPO[#](#running-grpo)

按照以下步骤准备数据、训练模型并执行推理。

### 设置参数[#](#set-the-parameters)

加载 `Llama 3.1 8B Instruct`

并设置参数：

```python
from unsloth import FastLanguageModel
import torch
max_seq_length = 1024 # 可增加以支持更长的推理轨迹
lora_rank = 32 # 更高的秩 = 更智能，但更慢
model, tokenizer = FastLanguageModel.from_pretrained(
model_name = "meta-llama/meta-Llama-3.1-8B-Instruct",
max_seq_length = max_seq_length,
load_in_4bit = False, # 对于LoRA 4bit设为True
fast_inference = True, # 启用vLLM快速推理
max_lora_rank = lora_rank,
gpu_memory_utilization = 0.6, # 如果内存不足则降低
)
model = FastLanguageModel.get_peft_model(
model,
r = lora_rank, # 选择任意大于0的数！建议8、16、32、64、128
target_modules = [
"q_proj", "k_proj", "v_proj", "o_proj",
"gate_proj", "up_proj", "down_proj",
], # 如果内存不足，移除QKVO
lora_alpha = lora_rank,
use_gradient_checkpointing = "unsloth", # 启用长上下文微调
random_state = 3407,
)
```

```

### 数据准备[#](#id1)

本教程直接使用 [willccbb](https://gist.github.com/willccbb/4676755236bb08cab5f4e54a0475d6fb) 进行数据准备和所有奖励函数的实现。你可以自由创建自己的方法。

```
import re
from datasets import load_dataset, Dataset
# Load and prep dataset
SYSTEM_PROMPT = """
Respond in the following format:
<reasoning>
...
</reasoning>
<answer>
...
</answer>
"""
XML_COT_FORMAT = """\
<reasoning>
{reasoning}
</reasoning>
<answer>
{answer}
</answer>
"""
def extract_xml_answer(text: str) -> str:
answer = text.split("<answer>")[-1]
answer = answer.split("</answer>")[0]
return answer.strip()
def extract_hash_answer(text: str) -> str | None:
if "####" not in text:
return None
return text.split("####")[1].strip()
# uncomment middle messages for 1-shot prompting
def get_gsm8k_questions(split = "train") -> Dataset:
data = load_dataset('openai/gsm8k', 'main')[split] # type: ignore
data = data.map(lambda x: { # type: ignore
'prompt': [
{'role': 'system', 'content': SYSTEM_PROMPT},
{'role': 'user', 'content': x['question']}
],
'answer': extract_hash_answer(x['answer'])
}) # type: ignore
return data # type: ignore
dataset = get_gsm8k_questions()
# Reward functions
def correctness_reward_func(prompts, completions, answer, **kwargs) -> list[float]:
responses = [completion[0]['content'] for completion in completions]
q = prompts[0][-1]['content']
extracted_responses = [extract_xml_answer(r) for r in responses]
print('-'*20, f"Question:\n{q}", f"\nAnswer:\n{answer[0]}", f"\nResponse:\n{responses[0]}", f"\nExtracted:\n{extracted_responses[0]}")
return [2.0 if r == a else 0.0 for r, a in zip(extracted_responses, answer)]
def int_reward_func(completions, **kwargs) -> list[float]:
responses = [completion[0]['content'] for completion in completions]
extracted_responses = [extract_xml_answer(r) for r in responses]
return [0.5 if r.isdigit() else 0.0 for r in extracted_responses]
def strict_format_reward_func(completions, **kwargs) -> list[float]:
"""Reward function that checks if the completion has a specific format."""
pattern = r"^<reasoning>\n.*?\n</reasoning>\n<answer>\n.*?\n</answer>\n$"
responses = [completion[0]["content"] for completion in completions]
matches = [re.match(pattern, r) for r in responses]
return [0.5 if match else 0.0 for match in matches]
def soft_format_reward_func(completions, **kwargs) -> list[float]:
"""Reward function that checks if the completion has a specific format."""
pattern = r"<reasoning>.*?</reasoning>\s*<answer>.*?</answer>"
responses = [completion[0]["content"] for completion in completions]
matches = [re.match(pattern, r) for r in responses]
return [0.5 if match else 0.0 for match in matches]
def count_xml(text) -> float:
count = 0.0
if text.count("<reasoning>\n") == 1:
count += 0.125
if text.count("\n</reasoning>\n") == 1:
count += 0.125
if text.count("\n<answer>\n") == 1:
count += 0.125
count -= len(text.split("\n</answer>\n")[-1])*0.001
if text.count("\n</answer>") == 1:
count += 0.125
count -= (len(text.split("\n</answer>")[-1]) - 1)*0.001
return count
def xmlcount_reward_func(completions, **kwargs) -> list[float]:
contents = [completion[0]["content"] for completion in completions]
return [count_xml(c) for c in contents]
```

```

### 训练模型[#](#train-the-model)

现在设置 GRPO Trainer 和所有配置：

```
max_prompt_length = 256
from trl import GRPOConfig, GRPOTrainer
training_args = GRPOConfig(
learning_rate = 5e-6,
adam_beta1 = 0.9,
adam_beta2 = 0.99,
weight_decay = 0.1,
warmup_ratio = 0.1,
lr_scheduler_type = "cosine",
optim = "paged_adamw_8bit",
logging_steps = 1,
per_device_train_batch_size = 1,
gradient_accumulation_steps = 1, # 可增加至4以获得更平滑的训练
num_generations = 6, # 如内存不足可减小
max_prompt_length = max_prompt_length,
max_completion_length = max_seq_length - max_prompt_length,
# num_train_epochs = 1, # 设置为1进行完整训练
max_steps = 250,
save_steps = 250,
max_grad_norm = 0.1,
report_to = "none", # 可使用Weights & Biases
output_dir = "outputs",
)
```

```

现在您可以运行训练器。向上滚动查看奖励表。目标是看到 `reward`。

列增加！

您可能需要等待150到200步才能看到任何动作。前100步可能不会获得任何奖励。请耐心等待！

步骤 | 训练损失 | 奖励 | 奖励标准差 | 完成长度 | KL散度
|---|---|---|---|---|---|
1 | 0.000000 | 0.125000 | 0.000000 | 200.000000 | 0.000000
2 | 0.000000 | 0.072375 | 0.248112 | 200.000000 | 0.000000
3 | 0.000000 | -0.079000 | 0.163776 | 182.500000 | 0.000005

```
trainer = GRPOTrainer(
model = model,
processing_class = tokenizer,
reward_funcs = [
xmlcount_reward_func,
soft_format_reward_func,
strict_format_reward_func,
int_reward_func,
correctness_reward_func,
],
args = training_args,
train_dataset = dataset,
)
trainer.train()
```

```

### 推理[#](#inference)

现在尝试你刚刚训练的模型。首先尝试没有任何GRPO训练的模型：

```
text = tokenizer.apply_chat_template([
{"role" : "user", "content" : "计算圆周率。"},
], tokenize = False, add_generation_prompt = True)
from vllm import SamplingParams
sampling_params = SamplingParams(
temperature = 0.8,
top_p = 0.95,
max_tokens = 1024,
)
output = model.fast_generate(
[text],
sampling_params = sampling_params,
lora_request = None,
)[0].outputs[0].text
```

```

现在，用你刚刚用GRPO训练好的LoRA试试看，但请先保存该LoRA。

```
model.save_lora("grpo_saved_lora")
```

```

现在你可以加载 LoRA 并进行测试：

```text = tokenizer.apply_chat_template([
{"role" : "system", "content" : SYSTEM_PROMPT},
{"role" : "user", "content" : "计算圆周率。"},
], tokenize = False, add_generation_prompt = True)
from vllm import SamplingParams
sampling_params = SamplingParams(
temperature = 0.8,
top_p = 0.95,
max_tokens = 1024,
)
output = model.fast_generate(
text,
sampling_params = sampling_params,
lora_request = model.load_lora("grpo_saved_lora"),
)[0].outputs[0].text
output```

```

推理模型要好得多。它并不总是正确的，因为你只训练了大约一个小时。如果延长序列长度并训练更长时间，它会变得更好。

### 保存为float16以用于VLLM[#](#saving-to-float16-for-vllm)

Unsloth 还支持保存为 `float16`

直接。选择 `merged_16bit`

对于 `float16`

或 `merged_4bit`

对于 `int4`

它同时也允许 `lora`

以适配器作为回退方案。使用 `push_to_hub_merged`

上传到您的 Hugging Face 账户。访问 [Hugging Face 令牌设置页面](https://huggingface.co/settings/tokens) 获取您的个人令牌。

```
# 合并为16位
if False: model.save_pretrained_merged("model", tokenizer, save_method = "merged_16bit",)
if False: model.push_to_hub_merged("hf/model", tokenizer, save_method = "merged_16bit", token = "")
# 合并为4位
if False: model.save_pretrained_merged("model", tokenizer, save_method = "merged_4bit",)
if False: model.push_to_hub_merged("hf/model", tokenizer, save_method = "merged_4bit", token = "")
# 仅保留LoRA适配器
if False: model.save_pretrained_merged("model", tokenizer, save_method = "lora",)
if False: model.push_to_hub_merged("hf/model", tokenizer, save_method = "lora", token = "")
```

```

现在你完成了！如果你对 Unsloth 有任何问题、需要帮助，或者想保持最新动态，他们有一个 [Discord](https://discord.gg/unsloth) 频道和 [GitHub](https://github.com/unslothai/unsloth)。你还可以查阅他们的 [文档](https://docs.unsloth.ai/) 了解更多信息。