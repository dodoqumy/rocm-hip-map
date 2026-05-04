---
title: "Running inference with Hugging Face Transformers &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/1_inference_ver3_HF_transformers.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:51.022734+00:00
content_hash: "004020422cbf414d"
---

# Running inference with Hugging Face Transformers[#](#running-inference-with-hugging-face-transformers)

**Authors**: Seungrok Jung and Hyukjoon Lee

**Knowledge level**: Beginner

This tutorial explores how to leverage Hugging Face Transformers on AMD hardware. Learn how to install and configure ROCm for AMD Instinct™ GPUs and launch your favorite models. By following these steps, you’ll be able to run advanced LLMs in a ROCm-accelerated environment, capitalizing on AMD’s GPU performance for innovative natural language processing tasks.

## Prerequisites[#](#prerequisites)

This tutorial was developed and tested using the following setup.

### Operating system[#](#operating-system)

**Ubuntu 22.04**: Ensure your system is running Ubuntu version 22.04.

### Hardware[#](#hardware)

**AMD Instinct GPUs**: This tutorial was tested on an AMD Instinct MI300X GPU. Ensure you are using an AMD Instinct GPU or compatible hardware with ROCm support and that your system meets the[official requirements](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html).

### Software[#](#software)

**ROCm 6.2 or 6.3**: Install and verify ROCm by following the[ROCm install guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html). After installation, confirm your setup using:This command lists your AMD GPUs with relevant details.

**Note**: For ROCm 6.4 and earlier, use the`rocm-smi`

command instead.**Docker**: Ensure Docker is installed and configured correctly. Follow the Docker installation guide for your operating system.**Note**: Ensure the Docker permissions are correctly configured. To configure permissions to allow non-root access, run the following commands:usermod -aG docker $USER newgrp docker

Verify Docker is working correctly:

run hello-world


### Hugging Face API access[#](#hugging-face-api-access)

Obtain an API token from

[Hugging Face](https://huggingface.co)for downloading models.Ensure the Hugging Face API token has the necessary permissions and approval to access

[Meta’s Llama checkpoints](https://huggingface.co/meta-llama/Llama-3.1-8B).

## Inference on Hugging Face Transformers[#](#inference-on-hugging-face-transformers)

Hugging Face Transformers is a popular open-source library that provides an easy-to-use interface for working with widely used language models, such as BERT, GPT, and the Llama variants. These models can be fine-tuned or used off-the-shelf for tasks like text generation, question answering, and sentiment analysis.

This tutorial demonstrates how to run inference on Hugging Face Transformers models using AMD Instinct GPUs. It covers configuring ROCm for GPU support, installing the necessary libraries, and running an LLM (meta-llama/Meta-Llama-3.1-8B-Instruct) in a containerized environment.

## Prepare the inference environment[#](#prepare-the-inference-environment)

To set up the inference environment, follow these steps.

### 1. Launch the Docker container[#](#launch-the-docker-container)

Run the following command in your terminal to pull the prebuilt Docker image containing all necessary dependencies and launch the Docker container with the proper configuration:

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
--hostname=ROCm-FT \
--env HUGGINGFACE_HUB_CACHE=/workspace \
-v $(pwd):/workspace \
-w /workspace/notebooks \
rocm/pytorch:rocm6.3.1_ubuntu22.04_py3.10_pytorch
```

**Note**: This command mounts the current directory to the `/workspace`

directory in the container. Ensure the notebook file is either copied to this directory before running the Docker command or uploaded into the Jupyter Notebook environment after it starts. Save the token or URL provided in the terminal output to access the notebook from your web browser. You can download this notebook from the [AI Developer Hub GitHub repository](https://github.com/ROCm/gpuaidev).

### 2. Install and launch Jupyter[#](#install-and-launch-jupyter)

Inside the Docker container, install Jupyter using the following command:

```
install jupyter
```

Then start the Jupyter server:

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

**Note**: Ensure port `8888`

is not already in use on your system before running the above command. If it is, you can specify a different port by replacing `--port=8888`

with another port number, for example, `--port=8890`

.

### 3. Install the required libraries[#](#install-the-required-libraries)

Install the libraries needed for this tutorial. Run the following commands inside the Jupyter notebook running within the Docker container:

```
!pip install accelerate transformers
```

Verify the installation:

```
!pip list | grep transformer
!pip list | grep accelerate
```

### 4. Provide your Hugging Face token[#](#provide-your-hugging-face-token)

You’ll require a Hugging Face API token to access meta-llama/Llama-3.1-8B-Instruct. Generate your token at Hugging Face Tokens and request access for [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct). Tokens typically start with “hf_”.

Run the following interactive block in your Jupyter notebook to set up the token:

**Note**: Uncheck the “Add token as Git credential?” option.

```
from huggingface_hub import notebook_login, HfApi
# Prompt the user to log in
notebook_login()
```

Verify that your token was accepted correctly:

```
# Validate the token
try:
api = HfApi()
user_info = api.whoami()
print(f"Token validated successfully! Logged in as: {user_info['name']}")
except Exception as e:
print(f"Token validation failed. Error: {e}")
```

## Run LLM inference using Hugging Face Transformers[#](#run-llm-inference-using-hugging-face-transformers)

Inside the Docker container, run the following code sample using Jupyter Notebook:

```
import transformers
import torch
model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
pipeline = transformers.pipeline(
"text-generation",
model=model_id,
model_kwargs={"torch_dtype": torch.bfloat16},
device_map="auto",
)
query = "Explain the concept of AI."
messages = [
{"role": "system", "content": "You are an expert in the field of AI. Make sure to provide an explanation in few sentences."},
{"role": "user", "content": query},
]
outputs = pipeline(
messages,
max_new_tokens=512,
top_p = 0.7,
temperature=0.2,
)
response = outputs[0]["generated_text"][-1]['content']
print('-------------------------------')
print('Query:\n', query)
print('-------------------------------')
print('Response:\n', response)
```

After a successful run, the output will look like this:

Query:

```
Explain the concept of AI.
```

Response:

```
Artificial Intelligence (AI) refers to the development of computer systems that can perform tasks that typically require human intelligence, such as learning, problem-solving, decision-making, and perception. These systems use algorithms and data to simulate human-like behavior, enabling them to adapt to new situations and improve their performance over time. AI can be categorized into two main types: Narrow or Weak AI, which is designed to perform a specific task, and General or Strong AI, which aims to replicate human intelligence and reasoning across a wide range of tasks.
```
