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

# 使用Unsloth训练自己的R1推理模型[#](#train-your-own-r1-reasoning-model-with-unsloth)

**作者**: [Unsloth](https://unsloth.ai)，并由 [AMD](https://www.amd.com) 修改以在 AMD GPU 上运行。

**知识水平**：中级

本教程演示如何利用 [Unsloth](https://unsloth.ai) 在 AMD ROCm（ROCm（Radeon 开放计算平台））GPU 上对 Llama-3.1 8B 大型语言模型（LLM）进行微调。DeepSeek 的 R1 研究揭示了一个“顿悟时刻”：R1-Zero 通过使用组相对策略优化（GRPO）自主学会了分配更多思考时间，而无需人类反馈。Unsloth 团队增强了整个 GRPO 流程，使其比 Hugging Face 和 Flash Attention 2（FA2）减少 80% 的显存使用。这使得您仅需 7GB 显存，即可使用 Qwen2.5（1.5B）复现 R1-Zero 的成果。

## 前提条件[#](#prerequisites)

本教程使用以下配置进行开发和测试。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**: 确保您的系统运行的是Ubuntu 22.04版本。

### 硬件[#](#hardware)

**AMD Instinct™ GPUs**（AMD 数据中心 GPU 系列）：本教程已在 AMD Instinct MI300X GPU 上测试。请确保您使用的是支持 ROCm（Radeon 开放计算平台）的 AMD Instinct GPU 或兼容硬件，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

### 软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.3**：按照[ROCm（ROCm（Radeon 开放计算平台））安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html)安装并验证ROCm（ROCm（Radeon 开放计算平台））。安装完成后，使用以下命令确认设置：该命令将列出您的AMD GPU及其相关信息。

**注意**：对于 ROCm（ROCm（Radeon 开放计算平台）） 6.4 及更早版本，请使用 `rocm-smi`

command instead.**Docker**: Ensure Docker is installed and configured correctly. Follow the Docker installation guide for your operating system.**Note**: Ensure the Docker permissions are correctly configured. To configure permissions to allow non-root access, run the following commands:usermod -aG docker $USER newgrp docker

验证Docker是否正常工作：

运行 hello-world

### Hugging Face API 访问[#](#hugging-face-api-access)

从...获取 API token

使用 [Hugging Face](https://huggingface.co) 下载模型。确保 Hugging Face API 令牌拥有必要的权限和批准以访问。

[Meta Llama 检查点](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).

### 数据准备[#](#data-preparation)

本教程使用 Hugging Face 的示例数据集，该数据集在设置步骤中准备就绪。

## 准备训练环境[#](#prepare-the-training-environment)

### 1. 拉取 Docker 镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的Docker镜像：

```
pull rocm/vllm-dev:main

```

### 2. 启动 Docker 容器[#](#launch-the-docker-container)

启动 Docker 容器并映射必要的目录。替换 `/path/to/notebooks`

使用您主机上存储这些notebooks的目录的完整路径。

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

**注意**：该命令将当前目录挂载到 `/workspace`

目录在容器内。确保在运行Docker命令之前将笔记本文件复制到此目录，或者在启动后将文件上传到Jupyter Notebook环境中。保存终端输出中提供的令牌或URL，以便从Web浏览器访问笔记本。您可以从[AI Developer Hub GitHub仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev)下载此笔记本。

### 3. 安装并启动Jupyter[#](#install-and-launch-jupyter)

在Docker容器内部，使用以下命令安装Jupyter：

```
install jupyter
```

```

启动 Jupyter 服务器：

```--ip=0.0.0.0 --port=8888 --no-browser --allow-root```

```

注意：确保端口 `8888`

在运行上述命令之前，请确保该端口在您的系统上尚未被占用。如果已被占用，您可以通过替换 `--port=8888` 来指定其他端口。

使用另一个端口号，例如 `--port=8890`

。

### 4. 安装所需库[#](#install-the-required-libraries)

安装本教程所需的库。在Docker容器内运行的Jupyter notebook中运行以下命令：

```
# 从源码安装 Unsloth
!git clone https://github.com/billishyahao/unsloth.git && cd unsloth && git checkout billhe/rocm && pip install .
!pip install unsloth_zoo==2025.3.17
# 从源码安装 ROCm（ROCm（Radeon 开放计算平台）） Bitsandbytes
!git clone --recurse https://github.com/ROCm（ROCm（Radeon 开放计算平台））/bitsandbytes && cd bitsandbytes && git checkout rocm_enabled_multi_backend && pip install -r requirements-dev.txt && cmake -DCOMPUTE_BACKEND=hip -S . && make -j && pip install .
# 本笔记本已在 unsloth==2025.3.19 unsloth_zoo==2025.3.17 bitsandbytes==0.43.3.dev0 环境下验证通过
```

```

验证安装：

```
# 验证所需库的安装和版本
!pip list | grep unsloth
```

```

请提供需要翻译的英文文本。

```
unsloth 2025.3.19
unsloth_zoo 2025.3.17
```

```

**⚠️ 重要**: 确保选择了正确的内核

如果验证过程失败，请确保为你的notebook选择了正确的Jupyter kernel。要更改kernel，请按照以下步骤操作：

转到

**内核函数 (Kernel)**menu.Select

**更改 内核函数 (Kernel)**.Select

Python 3 (ipykernel)

从列表中。

**重要**：未选择正确的内核可能会导致运行笔记本时出现意外问题。

### 5. 提供您的Hugging Face令牌[#](#provide-your-hugging-face-token)

您需要一个Hugging Face API令牌来访问Llama-3.1。在 [Hugging Face Tokens](https://huggingface.co/settings/tokens) 生成您的令牌，并为 [Llama-3.1 8B](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) 请求访问权限。令牌通常以“hf_”开头。

在您的 Jupyter notebook 中运行以下交互块以设置 token：

**注意**：取消选中“将令牌添加为Git凭据”选项。

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
print(f"Token验证成功！已登录为：{user_info['name']}")
except Exception as e:
print(f"Token验证失败。错误：{e}")
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
max_seq_length = 1024 # 可以增加以支持更长的推理链
lora_rank = 32 # 更大的秩 = 更智能，但更慢
model, tokenizer = FastLanguageModel.from_pretrained(
model_name = "meta-llama/meta-Llama-3.1-8B-Instruct",
max_seq_length = max_seq_length,
load_in_4bit = False, # 如果是LoRA 4bit，设为True
fast_inference = True, # 启用vLLM快速推理
max_lora_rank = lora_rank,
gpu_memory_utilization = 0.6, # 如果内存不足，请减小
)
model = FastLanguageModel.get_peft_model(
model,
r = lora_rank, # 选择任意 > 0 的数！建议 8, 16, 32, 64, 128
target_modules = [
"q_proj", "k_proj", "v_proj", "o_proj",
"gate_proj", "up_proj", "down_proj",
], # 如果内存不足，移除 QKVO
lora_alpha = lora_rank,
use_gradient_checkpointing = "unsloth", # 启用长上下文微调
random_state = 3407,
)
```

```

### 数据准备[#](#id1)

本教程直接使用 [willccbb](https://gist.github.com/willccbb/4676755236bb08cab5f4e54a0475d6fb) 进行数据准备和所有奖励函数的实现。你可以自由创建自己的方法。

```python
import re
from datasets import load_dataset, Dataset
# 加载并准备数据集
SYSTEM_PROMPT = """
请按以下格式回复：
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
# 取消注释中间消息以进行单样本提示
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
# 奖励函数
def correctness_reward_func(prompts, completions, answer, **kwargs) -> list[float]:
responses = [completion[0]['content'] for completion in completions]
q = prompts[0][-1]['content']
extracted_responses = [extract_xml_answer(r) for r in responses]
print('-'*20, f"问题：\n{q}", f"\n答案：\n{answer[0]}", f"\n响应：\n{responses[0]}", f"\n提取结果：\n{extracted_responses[0]}")
return [2.0 if r == a else 0.0 for r, a in zip(extracted_responses, answer)]
def int_reward_func(completions, **kwargs) -> list[float]:
responses = [completion[0]['content'] for completion in completions]
extracted_responses = [extract_xml_answer(r) for r in responses]
return [0.5 if r.isdigit() else 0.0 for r in extracted_responses]
def strict_format_reward_func(completions, **kwargs) -> list[float]:
"""奖励函数，检查补全是否具有特定格式。"""
pattern = r"^<reasoning>\n.*?\n</reasoning>\n<answer>\n.*?\n</answer>\n$"
responses = [completion[0]["content"] for completion in completions]
matches = [re.match(pattern, r) for r in responses]
return [0.5 if match else 0.0 for match in matches]
def soft_format_reward_func(completions, **kwargs) -> list[float]:
"""奖励函数，检查补全是否具有特定格式。"""
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
gradient_accumulation_steps = 1, # 增加到4以获得更平滑的训练
num_generations = 6, # 若内存不足请减小此值
max_prompt_length = max_prompt_length,
max_completion_length = max_seq_length - max_prompt_length,
# num_train_epochs = 1, # 设置为1以进行完整训练
max_steps = 250,
save_steps = 250,
max_grad_norm = 0.1,
report_to = "none", # 可以使用Weights & Biases
output_dir = "outputs",
)
```

```

现在您可以运行训练器。向上滚动以查看奖励表格。目标是看到`reward`

增加列！

您可能需要等待150到200步才能看到任何动作。前100步很可能不会获得任何奖励。请耐心等待！

步骤 | 训练损失 | 奖励 | 奖励标准差 | 完成长度 | KL散度 |
|---|---|---|---|---|---|
1 | 0.000000 | 0.125000 | 0.000000 | 200.000000 | 0.000000 |
2 | 0.000000 | 0.072375 | 0.248112 | 200.000000 | 0.000000 |
3 | 0.000000 | -0.079000 | 0.163776 | 182.500000 | 0.000005 |

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

现在尝试您刚刚训练的模型。首先尝试没有经过任何 GRPO 训练的模型：

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
output
```

```

现在，使用您刚刚用GRPO训练的LoRA来尝试一下，但首先请保存这个LoRA。

```
model.save_lora("grpo_saved_lora")
```

```

现在你可以加载LoRA并进行测试：

```
text = tokenizer.apply_chat_template([
{"role" : "system", "content" : SYSTEM_PROMPT},
{"role" : "user", "content" : "计算圆周率"},
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
output
```

```

推理模型好多了。它并非总是正确，因为你只训练了大约一小时。如果你延长序列长度并训练更长时间，效果会更好。

### 为VLLM保存为float16[#](#saving-to-float16-for-vllm)

Unsloth 也支持保存为 `float16`

直接。选择 `merged_16bit`

对于 `float16`

或 `merged_4bit`

对于 `int4`

它同时也允许 `lora`

将适配器作为后备方案。使用 `push_to_hub_merged`

上传到您的Hugging Face账户。请访问 [Hugging Face token设置页面](https://huggingface.co/settings/tokens) 获取您的个人令牌。

```
# 合并为16位
if False: model.save_pretrained_merged("model", tokenizer, save_method = "merged_16bit",)
if False: model.push_to_hub_merged("hf/model", tokenizer, save_method = "merged_16bit", token = "")
# 合并为4位
if False: model.save_pretrained_merged("model", tokenizer, save_method = "merged_4bit",)
if False: model.push_to_hub_merged("hf/model", tokenizer, save_method = "merged_4bit", token = "")
# 仅LoRA适配器
if False: model.save_pretrained_merged("model", tokenizer, save_method = "lora",)
if False: model.push_to_hub_merged("hf/model", tokenizer, save_method = "lora", token = "")
```

```

现在你已经完成了！如果你对Unsloth有任何疑问、需要帮助或想获取最新动态，他们有一个[Discord](https://discord.gg/unsloth)频道和一个[GitHub](https://github.com/unslothai/unsloth)仓库。你也可以查阅他们的[文档](https://docs.unsloth.ai/)了解更多信息。