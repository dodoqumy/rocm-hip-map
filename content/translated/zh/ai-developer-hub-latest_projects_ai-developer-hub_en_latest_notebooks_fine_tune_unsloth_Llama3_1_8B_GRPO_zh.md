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

# 使用Unsloth训练你自己的R1推理模型[#](#train-your-own-r1-reasoning-model-with-unsloth)

**Authored by**: [Unsloth](https://unsloth.ai) and modified by [AMD](https://www.amd.com) to run on AMD GPUs.

**知识水平**：中级

本教程演示如何利用 [Unsloth](https://unsloth.ai) 在 AMD ROCm（ROCm（Radeon 开放计算平台）） GPU 上微调 Llama-3.1 8B 大型语言模型（LLM）。DeepSeek 的 R1 研究揭示了一个“顿悟时刻”，即 R1-Zero 通过使用群体相对策略优化（GRPO）无需人类反馈便自主学会了分配更多思考时间。Unsloth 团队对整个 GRPO 流程进行了优化，使其显存占用比 Hugging Face 和 Flash Attention 2（FA2）减少 80%。这使得您只需 7GB 显存即可复现 R1-Zero 的成就，例如使用 Qwen2.5（1.5B）。

## 先决条件[#](#prerequisites)

本教程的开发和测试均基于以下环境设置。

### 操作系统[#](#operating-system)

**Ubuntu 22.04**：确保您的系统运行的是 Ubuntu 22.04 版本。

### 硬件[#](#hardware)

**AMD Instinct（Instinct（AMD 数据中心 GPU 系列））™ GPUs**：本教程已在 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） MI300X GPU 上完成测试。请确保您使用的是支持 ROCm（ROCm（Radeon 开放计算平台））的 AMD Instinct（Instinct（AMD 数据中心 GPU 系列）） GPU 或兼容硬件，并且您的系统满足[官方要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html).

软件[#](#software)

**ROCm（ROCm（Radeon 开放计算平台）） 6.3**：按照 [ROCm（ROCm（Radeon 开放计算平台）） 安装指南](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) 安装并验证 ROCm（ROCm（Radeon 开放计算平台））。安装完成后，使用以下命令确认您的配置：该命令将列出您的 AMD GPU 及其相关信息。

**注意**：对于 ROCm（ROCm（Radeon 开放计算平台）） 6.4 及更早版本，请使用`rocm-smi`

command instead.**Docker**：确保Docker已正确安装和配置。请按照您操作系统的Docker安装指南进行操作。**注意**：确保Docker权限已正确配置。要配置权限以允许非root用户访问，请运行以下命令：usermod -aG docker $USER newgrp docker

验证 Docker 是否正常工作：

运行 hello-world

### Hugging Face API 访问[#](#hugging-face-api-access)

从...获取 API token

[Hugging Face](https://huggingface.co)用于下载模型。确保Hugging Face API令牌具有必要的权限和批准来访问

[Meta Llama检查点](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)。

### 数据准备[#](#data-preparation)

本教程使用来自 Hugging Face 的示例数据集，该数据集在设置步骤中准备完成。

## 准备训练环境[#](#prepare-the-training-environment)

### 1. 拉取 Docker 镜像[#](#pull-the-docker-image)

确保您的系统满足[系统要求](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)。

拉取本教程所需的Docker镜像：

```
pull rocm/vllm-dev:main
```

```

### 2. 启动Docker容器[#](#launch-the-docker-container)

启动Docker容器并映射必要的目录。替换 `/path/to/notebooks`

使用主机上存储这些笔记本的目录的完整路径。

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

**注意**：此命令将当前目录挂载到 `/workspace`

在容器中的目录。确保在运行Docker命令之前将笔记本文件复制到此目录，或者在Jupyter Notebook环境启动后上传到其中。保存终端输出中提供的令牌或URL，以便从您的Web浏览器访问该笔记本。您可以从[AI开发者中心GitHub仓库](https://github.com/ROCm（ROCm（Radeon 开放计算平台））/gpuaidev)下载此笔记本。

### 3. Install and launch Jupyter[#](#install-and-launch-jupyter)

在Docker容器内，使用以下命令安装Jupyter：

```
安装 jupyter
```

```

启动Jupyter服务器：

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

```

**注意**：确保端口 `8888`

在运行上述命令之前，请确保该端口未在你的系统上被占用。如果已被占用，你可以通过替换 `--port=8888` 来指定不同的端口。

使用另一个端口号，例如 `--port=8890`。

。

### 4. 安装所需的库[#](#install-the-required-libraries)

安装本教程所需的库。在 Docker 容器内运行的 Jupyter notebook 中执行以下命令：

```
# 从源码安装 Unsloth
!git clone https://github.com/billishyahao/unsloth.git && cd unsloth && git checkout billhe/rocm && pip install .
!pip install unsloth_zoo==2025.3.17
# 从源码安装 ROCm（ROCm（Radeon 开放计算平台）） Bitsandbytes
!git clone --recurse https://github.com/ROCm（ROCm（Radeon 开放计算平台））/bitsandbytes && cd bitsandbytes && git checkout rocm_enabled_multi_backend && pip install -r requirements-dev.txt && cmake -DCOMPUTE_BACKEND=hip -S . && make -j && pip install .
# 本笔记本已验证的环境为 unsloth==2025.3.19 unsloth_zoo==2025.3.17 bitsandbytes==0.43.3.dev0
```

```

验证安装：

```
# 验证所需库的安装和版本
!pip list | grep unsloth
```

```

以下是预期的输出：

```
unsloth 2025.3.19
unsloth_zoo 2025.3.17
```

```

**⚠️ 重要**：确保选择了正确的内核

如果验证过程失败，请确保为您的 notebook 选择了正确的 Jupyter 内核。如需更改内核，请按照以下步骤操作：

转到

**内核函数 (Kernel)**menu.Select

**更改内核函数 (Kernel)**.选择

`Python 3 (ipykernel)`

从列表中。

**重要**：未选择正确的内核可能导致运行笔记本时出现意外问题。

### 5. 提供您的 Hugging Face 令牌[#](#provide-your-hugging-face-token)

您需要一个 Hugging Face API 令牌来访问 Llama-3.1。在 [Hugging Face Tokens](https://huggingface.co/settings/tokens) 生成您的令牌，并申请访问 [Llama-3.1 8B](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)。令牌通常以 “hf_” 开头。

在您的 Jupyter notebook 中运行以下交互代码块以设置 token：

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
    print(f"Token validated successfully! Logged in as: {user_info['name']}")
except Exception as e:
    print(f"Token validation failed. Error: {e}")
```

```

## 运行 GRPO[#](#running-grpo)

按照以下步骤准备数据、训练模型并执行推理。

### 设置参数[#](#set-the-parameters)

加载 `Llama 3.1 8B Instruct`

并设置参数：

```
from unsloth import FastLanguageModel
import torch
max_seq_length = 1024 # 可增加以支持更长的推理轨迹
lora_rank = 32 # 更大的秩 = 更智能，但速度更慢
model, tokenizer = FastLanguageModel.from_pretrained(
model_name = "meta-llama/meta-Llama-3.1-8B-Instruct",
max_seq_length = max_seq_length,
load_in_4bit = False, # True 表示使用 LoRA 4bit
fast_inference = True, # 启用 vLLM 快速推理
max_lora_rank = lora_rank,
gpu_memory_utilization = 0.6, # 若内存不足请减小此值
)
model = FastLanguageModel.get_peft_model(
model,
r = lora_rank, # 选择任意大于 0 的值！建议 8、16、32、64、128
target_modules = [
"q_proj", "k_proj", "v_proj", "o_proj",
"gate_proj", "up_proj", "down_proj",
], # 若内存不足请移除 QKVO
lora_alpha = lora_rank,
use_gradient_checkpointing = "unsloth", # 启用长上下文微调
random_state = 3407,
)
```

```

### 数据准备[#](#id1)

本教程直接利用[willccbb](https://gist.github.com/willccbb/4676755236bb08cab5f4e54a0475d6fb)进行数据准备和所有奖励函数。你可以自由创建自己的方法。

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
# 取消注释中间消息以进行1-shot提示
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
    print('-'*20, f"问题：\n{q}", f"\n答案：\n{answer[0]}", f"\n回复：\n{responses[0]}", f"\n提取内容：\n{extracted_responses[0]}")
    return [2.0 if r == a else 0.0 for r, a in zip(extracted_responses, answer)]
def int_reward_func(completions, **kwargs) -> list[float]:
    responses = [completion[0]['content'] for completion in completions]
    extracted_responses = [extract_xml_answer(r) for r in responses]
    return [0.5 if r.isdigit() else 0.0 for r in extracted_responses]
def strict_format_reward_func(completions, **kwargs) -> list[float]:
    """检查完成内容是否具有特定格式的奖励函数。"""
    pattern = r"^<reasoning>\n.*?\n</reasoning>\n<answer>\n.*?\n</answer>\n$"
    responses = [completion[0]["content"] for completion in completions]
    matches = [re.match(pattern, r) for r in responses]
    return [0.5 if match else 0.0 for match in matches]
def soft_format_reward_func(completions, **kwargs) -> list[float]:
    """检查完成内容是否具有特定格式的奖励函数。"""
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
gradient_accumulation_steps = 1, # 增加至4以实现更平滑的训练
num_generations = 6, # 若内存不足则减少
max_prompt_length = max_prompt_length,
max_completion_length = max_seq_length - max_prompt_length,
# num_train_epochs = 1, # 设置为1以进行完整训练
max_steps = 250,
save_steps = 250,
max_grad_norm = 0.1,
report_to = "none", # 可使用 Weights & Biases
output_dir = "outputs",
```

```

现在你可以运行训练器。向上滚动查看奖励表。目标是看到 `reward`。

列增加！

可能需要等待150到200步才能看到任何动作。前100步内可能不会获得任何奖励。请耐心等待！

| Step | 训练损失 | 奖励 | 奖励标准差 | 完成长度 | kl |
|---|---|---|---|---|---|---|
| 1 | 0.000000 | 0.125000 | 0.000000 | 200.000000 | 0.000000 |
| 2 | 0.000000 | 0.072375 | 0.248112 | 200.000000 | 0.000000 |
| 3 | 0.000000 | -0.079000 | 0.163776 | 182.500000 | 0.000005 |

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

现在尝试你刚刚训练好的模型。首先尝试没有经过任何GRPO训练的模型：

```
text = tokenizer.apply_chat_template([
{"role" : "user", "content" : "Calculate pi."},
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

现在用你刚刚用GRPO训练的LoRA试一试，但先保存该LoRA。

```
model.save_lora("grpo_saved_lora")
```

```

现在您可以加载LoRA并进行测试：

```
text = tokenizer.apply_chat_template([
{"role" : "system", "content" : SYSTEM_PROMPT},
{"role" : "user", "content" : "Calculate pi."},
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

推理模型好多了。它并不总是正确的，因为你只训练了大约一个小时。如果你延长序列长度并训练更长时间，它会更好。

### 为VLLM保存为float16[#](#saving-to-float16-for-vllm)

Unsloth 还支持保存为 `float16`

直接。选择 `merged_16bit`

对于 `float16`

或 `merged_4bit`

对于 `int4`

. 它也允许 `lora`

适配器作为后备方案。使用 `push_to_hub_merged`

要上传到您的Hugging Face账户。请访问[Hugging Face令牌设置](https://huggingface.co/settings/tokens)以获取您的个人令牌。

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

现在你完成了！如果你对Unsloth有任何疑问、需要帮助或想保持更新，他们有一个[Discord](https://discord.gg/unsloth)频道和一个[GitHub](https://github.com/unslothai/unsloth)。你也可以查阅他们的[文档](https://docs.unsloth.ai/)获取更多信息。