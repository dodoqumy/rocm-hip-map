---
title: "Model quantization techniques"
source_url: "https://rocm.docs.amd.com/en/docs-6.2.0/how-to/llm-fine-tuning-optimization/model-quantization.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:17:36.665961+00:00
content_hash: "e2782e0b783dad78"
---

# Model quantization techniques[#](#model-quantization-techniques)



Quantization reduces the model size compared to its native full-precision version, making it easier to fit large models onto accelerators or GPUs with limited memory usage. This section explains how to perform LLM quantization using GPTQ and bitsandbytes on AMD Instinct hardware.

## GPTQ[#](#gptq)

GPTQ is a post-training quantization technique where each row of the weight matrix is quantized independently to find a
version of the weights that minimizes error. These weights are quantized to `int4`

but are restored to `fp16`

on the
fly during inference. This can save your memory usage by a factor of four. A speedup in inference is expected because
inference of GPTQ models uses a lower bit width, which takes less time to communicate.

Before setting up the GPTQ configuration in Transformers, ensure the [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ) library
is installed.

### Installing AutoGPTQ[#](#installing-autogptq)

The AutoGPTQ library implements the GPTQ algorithm.

Use the following command to install the latest stable release of AutoGPTQ from pip.

# This will install pre-built wheel for a specific ROCm version. pip install auto-gptq --no-build-isolation --extra-index-url https://huggingface.github.io/autogptq-index/whl/rocm573/

Or, install AutoGPTQ from source for the appropriate ROCm version (for example, ROCm 6.1).

# Clone the source code. git clone https://github.com/AutoGPTQ/AutoGPTQ.git cd AutoGPTQ # Speed up the compilation by specifying PYTORCH_ROCM_ARCH to target device. PYTORCH_ROCM_ARCH=gfx942 ROCM_VERSION=6.1 pip install . # Show the package after the installation

Run

`pip show auto-gptq`

to print information for the installed`auto-gptq`

package. Its output should look like this:auto-gptq Version: 0.8.0.dev0+rocm6.1 ...


### Using GPTQ with AutoGPTQ[#](#using-gptq-with-autogptq)

Run the following code snippet.

from transformers import AutoTokenizer, TextGenerationPipeline from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig base_model_name = "NousResearch/Llama-2-7b-hf" quantized_model_name = "llama-2-7b-hf-gptq" tokenizer = AutoTokenizer.from_pretrained(base_model_name, use_fast=True) examples = [ tokenizer( "auto-gptq is an easy-to-use model quantization library with user-friendly apis, based on GPTQ algorithm." ) ] print(examples)

The resulting examples should be a list of dictionaries whose keys are

`input_ids`

and`attention_mask`

.Set up the quantization configuration using the following snippet.

quantize_config = BaseQuantizeConfig( bits=4, # quantize model to 4-bit group_size=128, # it is recommended to set the value to 128 desc_act=False, )

Load the non-quantized model using the AutoGPTQ class and run the quantization.

# Import auto_gptq class. from auto_gptq import AutoGPTQForCausalLM # Load non-quantized model. base_model = AutoGPTQForCausalLM.from_pretrained(base_model_name, quantize_config, device_map = "auto") base_model.quantize(examples) # Save quantized model. base_model.save_quantized(quantized_model_name)


### Using GPTQ with Hugging Face Transformers[#](#using-gptq-with-hugging-face-transformers)

To perform a GPTQ quantization using Hugging Face Transformers, you need to create a

`GPTQConfig`

instance and set the number of bits to quantize to, and a dataset to calibrate the weights.from transformers import AutoModelForCausalLM, AutoTokenizer, GPTQConfig base_model_name = " NousResearch/Llama-2-7b-hf" tokenizer = AutoTokenizer.from_pretrained(base_model_name) gptq_config = GPTQConfig(bits=4, dataset="c4", tokenizer=tokenizer)

Load a model to quantize using

`AutoModelForCausalLM`

and pass the`gptq_config`

to its`from_pretained`

method. Set`device_map=”auto”`

to automatically offload the model to available GPU resources.quantized_model = AutoModelForCausalLM.from_pretrained( base_model_name, device_map="auto", quantization_config=gptq_config)

Once the model is quantized, you can push the model and tokenizer to Hugging Face Hub for easy share and access.

quantized_model.push_to_hub("llama-2-7b-hf-gptq") tokenizer.push_to_hub("llama-2-7b-hf-gptq")

Or, you can save the model locally using the following snippet.

quantized_model.save_pretrained("llama-2-7b-gptq") tokenizer.save_pretrained("llama-2-7b-gptq")


### ExLlama-v2 support[#](#exllama-v2-support)

ExLlama is a Python/C++/CUDA implementation of the Llama model that is
designed for faster inference with 4-bit GPTQ weights. The ExLlama
kernel is activated by default when users create a `GPTQConfig`

object. To
boost inference speed even further on Instinct accelerators, use the ExLlama-v2
kernels by configuring the `exllama_config`

parameter as the following.

```
from transformers import AutoModelForCausalLM, GPTQConfig
#pretrained_model_dir = "meta-llama/Llama-2-7b"
base_model_name = "NousResearch/Llama-2-7b-hf"
gptq_config = GPTQConfig(bits=4, dataset="c4", exllama_config={"version":2})
quantized_model = AutoModelForCausalLM.from_pretrained(
base_model_name,
device_map="auto",
quantization_config=gptq_config)
```

## bitsandbytes[#](#bitsandbytes)

The [ROCm-aware bitsandbytes](https://github.com/ROCm/bitsandbytes) library is
a lightweight Python wrapper around CUDA custom functions, in particular 8-bit optimizer, matrix multiplication, and
8-bit and 4-bit quantization functions. The library includes quantization primitives for 8-bit and 4-bit operations
through `bitsandbytes.nn.Linear8bitLt`

and `bitsandbytes.nn.Linear4bit`

and 8-bit optimizers through the
`bitsandbytes.optim`

module. These modules are supported on AMD Instinct accelerators.

### Installing bitsandbytes[#](#installing-bitsandbytes)

To install bitsandbytes for ROCm 6.0 (and later), use the following commands.

# Clone the github repo git clone --recurse https://github.com/ROCm/bitsandbytes.git cd bitsandbytes git checkout rocm_enabled # Install dependencies pip install -r requirements-dev.txt # Use -DBNB_ROCM_ARCH to specify target GPU arch cmake -DBNB_ROCM_ARCH="gfx942" -DCOMPUTE_BACKEND=hip -S . # Compile the project make # Install python setup.py install

Run

`pip show bitsandbytes`

to show the information about the installed bitsandbytes package. Its output should look like the following.bitsandbytes Version: 0.44.0.dev0 ...


### Using bitsandbytes primitives[#](#using-bitsandbytes-primitives)

To get started with bitsandbytes primitives, use the following code as reference.

```
import bitsandbytes as bnb
# Use Int8 Matrix Multiplication
bnb.matmul(..., threshold=6.0)
# Use bitsandbytes 8-bit Optimizers
adam = bnb.optim.Adam8bit(model.parameters(), lr=0.001, betas=(0.9, 0.995))
```

### Using bitsandbytes with Hugging Face Transformers[#](#using-bitsandbytes-with-hugging-face-transformers)

To load a Transformers model in 4-bit, set `load_in_4bit=true`

in `BitsAndBytesConfig`

.

```
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
base_model_name = "NousResearch/Llama-2-7b-hf"
quantization_config = BitsAndBytesConfig(load_in_4bit=True)
bnb_model_4bit = AutoModelForCausalLM.from_pretrained(
base_model_name,
device_map="auto",
quantization_config=quantization_config)
# Check the memory footprint with get_memory_footprint method
print(bnb_model_4bit.get_memory_footprint())
```

To load a model in 8-bit for inference, use the `load_in_8bit`

option.

```
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
base_model_name = "NousResearch/Llama-2-7b-hf"
tokenizer = AutoTokenizer.from_pretrained(base_model_name)
quantization_config = BitsAndBytesConfig(load_in_8bit=True)
tokenizer = AutoTokenizer.from_pretrained(base_model_name)
bnb_model_8bit = AutoModelForCausalLM.from_pretrained(
base_model_name,
device_map="auto",
quantization_config=quantization_config)
prompt = "What is a large language model?"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
generated_ids = model.generate(**inputs)
outputs = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
```
