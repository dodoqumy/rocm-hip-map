---
title: "Model quantization techniques"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/model-quantization.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-03
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../index.html){.nav-link}
- [Use ROCm for AI inference optimization](index.html){.nav-link}
- Model\...
:::
:::::

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}
:::
::::
:::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# Model quantization techniques

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [AMD Quark](#amd-quark){.reference .internal .nav-link}
  - [Installing Quark](#installing-quark){.reference .internal .nav-link}
  - [Using Quark for quantization](#using-quark-for-quantization){.reference .internal .nav-link}
  - [Evaluating the quantized model with vLLM](#evaluating-the-quantized-model-with-vllm){.reference .internal .nav-link}
- [GPTQ](#gptq){.reference .internal .nav-link}
  - [Installing AutoGPTQ](#installing-autogptq){.reference .internal .nav-link}
  - [Using GPTQ with AutoGPTQ](#using-gptq-with-autogptq){.reference .internal .nav-link}
  - [Using GPTQ with Hugging Face Transformers](#using-gptq-with-hugging-face-transformers){.reference .internal .nav-link}
  - [ExLlama-v2 support](#exllama-v2-support){.reference .internal .nav-link}
- [bitsandbytes](#bitsandbytes){.reference .internal .nav-link}
  - [Installing bitsandbytes](#installing-bitsandbytes){.reference .internal .nav-link}
  - [Using bitsandbytes primitives](#using-bitsandbytes-primitives){.reference .internal .nav-link}
  - [Using bitsandbytes with Hugging Face Transformers](#using-bitsandbytes-with-hugging-face-transformers){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::: {#model-quantization-techniques .section}
# Model quantization techniques[\#](#model-quantization-techniques "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 11 min read time
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
:::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::

Quantization reduces the model size compared to its native full-precision version, making it easier to fit large models onto GPUs with limited memory usage. This section explains how to perform LLM quantization using AMD Quark, GPTQ and bitsandbytes on AMD Instinct hardware.

:::::::::::: {#amd-quark .section}
[]{#quantize-llms-quark}

## AMD Quark[\#](#amd-quark "Link to this heading"){.headerlink}

[AMD Quark](https://quark.docs.amd.com/latest/){.reference .external} offers the leading efficient and scalable quantization solution tailored to AMD Instinct GPUs. It supports [`FP8`{.docutils .literal .notranslate}]{.pre} and [`INT8`{.docutils .literal .notranslate}]{.pre} quantization for activations, weights, and KV cache, including [`FP8`{.docutils .literal .notranslate}]{.pre} attention. For very large models, it employs a two-level [`INT4-FP8`{.docutils .literal .notranslate}]{.pre} scheme---storing weights in [`INT4`{.docutils .literal .notranslate}]{.pre} while computing with [`FP8`{.docutils .literal .notranslate}]{.pre}---for nearly 4× compression without sacrificing accuracy. Quark scales efficiently across multiple GPUs, efficiently handling ultra-large models like Llama-3.1-405B. Quantized [`FP8`{.docutils .literal .notranslate}]{.pre} models like Llama, Mixtral, and Grok-1 are available under the [AMD organization on Hugging Face](https://huggingface.co/collections/amd/quark-quantized-ocp-fp8-models-66db7936d18fcbaf95d4405c){.reference .external}, and can be deployed directly via [vLLM](https://github.com/vllm-project/vllm/tree/main/vllm){.reference .external}.

::::: {#installing-quark .section}
### Installing Quark[\#](#installing-quark "Link to this heading"){.headerlink}

The latest release of Quark can be installed with pip

:::: {.highlight-shell .notranslate}
::: highlight
    pip install amd-quark
:::
::::

For detailed installation instructions, refer to the [Quark documentation](https://quark.docs.amd.com/latest/install.html){.reference .external}.
:::::

::: {#using-quark-for-quantization .section}
### Using Quark for quantization[\#](#using-quark-for-quantization "Link to this heading"){.headerlink}

1.  First, load the pre-trained model and its corresponding tokenizer using the Hugging Face [`transformers`{.docutils .literal .notranslate}]{.pre} library.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from transformers import AutoTokenizer, AutoModelForCausalLM

        MODEL_ID = "meta-llama/Llama-2-70b-chat-hf"
        MAX_SEQ_LEN = 512

        model = AutoModelForCausalLM.from_pretrained(
            MODEL_ID, device_map="auto", torch_dtype="auto",
        )
        model.eval()

        tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, model_max_length=MAX_SEQ_LEN)
        tokenizer.pad_token = tokenizer.eos_token
    :::
    ::::

2.  Prepare the calibration DataLoader (static quantization requires calibration data).

    :::: {.highlight-python .notranslate}
    ::: highlight
        from datasets import load_dataset
        from torch.utils.data import DataLoader

        BATCH_SIZE = 1
        NUM_CALIBRATION_DATA = 512

        dataset = load_dataset("mit-han-lab/pile-val-backup", split="validation")
        text_data = dataset["text"][:NUM_CALIBRATION_DATA]

        tokenized_outputs = tokenizer(
        text_data, return_tensors="pt", padding=True, truncation=True, max_length=MAX_SEQ_LEN
        )
        calib_dataloader = DataLoader(
        tokenized_outputs['input_ids'], batch_size=BATCH_SIZE, drop_last=True
        )
    :::
    ::::

3.  Define the quantization configuration. See the comments in the following code snippet for descriptions of each configuration option.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from quark.torch.quantization import (Config, QuantizationConfig,
                                             FP8E4M3PerTensorSpec)

        # Define fp8/per-tensor/static spec.
        FP8_PER_TENSOR_SPEC = FP8E4M3PerTensorSpec(observer_method="min_max",
            is_dynamic=False).to_quantization_spec()

        # Define global quantization config, input tensors and weight apply FP8_PER_TENSOR_SPEC.
        global_quant_config = QuantizationConfig(input_tensors=FP8_PER_TENSOR_SPEC,
            weight=FP8_PER_TENSOR_SPEC)

        # Define quantization config for kv-cache layers, output tensors apply FP8_PER_TENSOR_SPEC.
        KV_CACHE_SPEC = FP8_PER_TENSOR_SPEC
        kv_cache_layer_names_for_llama = ["*k_proj", "*v_proj"]
        kv_cache_quant_config = {name :
            QuantizationConfig(input_tensors=global_quant_config.input_tensors,
                               weight=global_quant_config.weight,
                               output_tensors=KV_CACHE_SPEC)
            for name in kv_cache_layer_names_for_llama}
        layer_quant_config = kv_cache_quant_config.copy()

        EXCLUDE_LAYERS = ["lm_head"]
        quant_config = Config(
            global_quant_config=global_quant_config,
            layer_quant_config=layer_quant_config,
            kv_cache_quant_config=kv_cache_quant_config,
            exclude=EXCLUDE_LAYERS)
    :::
    ::::

4.  Quantize the model and export

    :::: {.highlight-python .notranslate}
    ::: highlight
        import torch
        from quark.torch import ModelQuantizer, ModelExporter
        from quark.torch.export import ExporterConfig, JsonExporterConfig

        # Apply quantization.
        quantizer = ModelQuantizer(quant_config)
        quant_model = quantizer.quantize_model(model, calib_dataloader)

        # Freeze quantized model to export.
        freezed_model = quantizer.freeze(model)

        # Define export config.
        LLAMA_KV_CACHE_GROUP = ["*k_proj", "*v_proj"]
        export_config = ExporterConfig(json_export_config=JsonExporterConfig())
        export_config.json_export_config.kv_cache_group = LLAMA_KV_CACHE_GROUP

        EXPORT_DIR = MODEL_ID.split("/")[1] + "-w-fp8-a-fp8-kvcache-fp8-pertensor"
        exporter = ModelExporter(config=export_config, export_dir=EXPORT_DIR)
        with torch.no_grad():
            exporter.export_safetensors_model(freezed_model,
                quant_config=quant_config, tokenizer=tokenizer)
    :::
    ::::
:::

::::::: {#evaluating-the-quantized-model-with-vllm .section}
### Evaluating the quantized model with vLLM[\#](#evaluating-the-quantized-model-with-vllm "Link to this heading"){.headerlink}

The exported Quark-quantized model can be loaded directly by vLLM for inference. You need to specify the model path and inform vLLM about the quantization method ([`quantization='quark'`{.docutils .literal .notranslate}]{.pre}) and the KV cache data type ([`kv_cache_dtype='fp8'`{.docutils .literal .notranslate}]{.pre}). Use the [`LLM`{.docutils .literal .notranslate}]{.pre} interface to load the model:

:::: {.highlight-python .notranslate}
::: highlight
    from vllm import LLM, SamplingParamsinterface

    # Sample prompts.
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]
    # Create a sampling params object.
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

    # Create an LLM.
    llm = LLM(model="Llama-2-70b-chat-hf-w-fp8-a-fp8-kvcache-fp8-pertensor",
              kv_cache_dtype='fp8',quantization='quark')
    # Generate texts from the prompts. The output is a list of RequestOutput objects
    # that contain the prompt, generated text, and other information.
    outputs = llm.generate(prompts, sampling_params)
    # Print the outputs.
    print("\nGenerated Outputs:\n" + "-" * 60)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt:    {prompt!r}")
        print(f"Output:    {generated_text!r}")
        print("-" * 60)
:::
::::

You can also evaluate the quantized model's accuracy on standard benchmarks using the [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness){.reference .external}. Pass the necessary vLLM arguments to [`lm_eval`{.docutils .literal .notranslate}]{.pre} via [`--model_args`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-shell .notranslate}
::: highlight
    lm_eval --model vllm \
      --model_args pretrained=Llama-2-70b-chat-hf-w-fp8-a-fp8-kvcache-fp8-pertensor,kv_cache_dtype='fp8',quantization='quark' \
      --tasks gsm8k
:::
::::

This provides a standardized way to measure the performance impact of quantization. .. \_fine-tune-llms-gptq:
:::::::
::::::::::::

::::::::: {#gptq .section}
## GPTQ[\#](#gptq "Link to this heading"){.headerlink}

GPTQ is a post-training quantization technique where each row of the weight matrix is quantized independently to find a version of the weights that minimizes error. These weights are quantized to [`int4`{.docutils .literal .notranslate}]{.pre} but are restored to [`fp16`{.docutils .literal .notranslate}]{.pre} on the fly during inference. This can save your memory usage by a factor of four. A speedup in inference is expected because inference of GPTQ models uses a lower bit width, which takes less time to communicate.

Before setting up the GPTQ configuration in Transformers, ensure the [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ){.reference .external} library is installed.

::: {#installing-autogptq .section}
### Installing AutoGPTQ[\#](#installing-autogptq "Link to this heading"){.headerlink}

The AutoGPTQ library implements the GPTQ algorithm.

1.  Use the following command to install the latest stable release of AutoGPTQ from pip.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # This will install pre-built wheel for a specific ROCm version.

        pip install auto-gptq --no-build-isolation --extra-index-url https://huggingface.github.io/autogptq-index/whl/rocm573/
    :::
    ::::

    Or, install AutoGPTQ from source for the appropriate ROCm version (for example, ROCm 6.1).

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Clone the source code.
        git clone https://github.com/AutoGPTQ/AutoGPTQ.git
        cd AutoGPTQ

        # Speed up the compilation by specifying PYTORCH_ROCM_ARCH to target device.
        PYTORCH_ROCM_ARCH=gfx942 ROCM_VERSION=6.1 pip install .

        # Show the package after the installation
    :::
    ::::

2.  Run [`pip`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`show`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`auto-gptq`{.docutils .literal .notranslate}]{.pre} to print information for the installed [`auto-gptq`{.docutils .literal .notranslate}]{.pre} package. Its output should look like this:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        Name: auto-gptq
        Version: 0.8.0.dev0+rocm6.1
        ...
    :::
    ::::
:::

::: {#using-gptq-with-autogptq .section}
### Using GPTQ with AutoGPTQ[\#](#using-gptq-with-autogptq "Link to this heading"){.headerlink}

1.  Run the following code snippet.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from transformers import AutoTokenizer, TextGenerationPipeline
        from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
        base_model_name = "NousResearch/Llama-2-7b-hf"
        quantized_model_name = "llama-2-7b-hf-gptq"
        tokenizer = AutoTokenizer.from_pretrained(base_model_name, use_fast=True)
        examples = [
            tokenizer(
                "auto-gptq is an easy-to-use model quantization library with user-friendly apis, based on GPTQ algorithm."
            )
        ]
        print(examples)
    :::
    ::::

    The resulting examples should be a list of dictionaries whose keys are [`input_ids`{.docutils .literal .notranslate}]{.pre} and [`attention_mask`{.docutils .literal .notranslate}]{.pre}.

2.  Set up the quantization configuration using the following snippet.

    :::: {.highlight-python .notranslate}
    ::: highlight
        quantize_config = BaseQuantizeConfig(
            bits=4,               # quantize model to 4-bit
            group_size=128,       # it is recommended to set the value to 128
            desc_act=False,
        )
    :::
    ::::

3.  Load the non-quantized model using the AutoGPTQ class and run the quantization.

    :::: {.highlight-python .notranslate}
    ::: highlight
        # Import auto_gptq class.
        from auto_gptq import AutoGPTQForCausalLM

        # Load non-quantized model.
        base_model = AutoGPTQForCausalLM.from_pretrained(base_model_name, quantize_config, device_map = "auto")
        base_model.quantize(examples)

        # Save quantized model.
        base_model.save_quantized(quantized_model_name)
    :::
    ::::
:::

::: {#using-gptq-with-hugging-face-transformers .section}
### Using GPTQ with Hugging Face Transformers[\#](#using-gptq-with-hugging-face-transformers "Link to this heading"){.headerlink}

1.  To perform a GPTQ quantization using Hugging Face Transformers, you need to create a [`GPTQConfig`{.docutils .literal .notranslate}]{.pre} instance and set the number of bits to quantize to, and a dataset to calibrate the weights.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from transformers import AutoModelForCausalLM, AutoTokenizer, GPTQConfig

        base_model_name = " NousResearch/Llama-2-7b-hf"
        tokenizer = AutoTokenizer.from_pretrained(base_model_name)
        gptq_config = GPTQConfig(bits=4, dataset="c4", tokenizer=tokenizer)
    :::
    ::::

2.  Load a model to quantize using [`AutoModelForCausalLM`{.docutils .literal .notranslate}]{.pre} and pass the [`gptq_config`{.docutils .literal .notranslate}]{.pre} to its [`from_pretained`{.docutils .literal .notranslate}]{.pre} method. Set [`device_map=”auto”`{.docutils .literal .notranslate}]{.pre} to automatically offload the model to available GPU resources.

    :::: {.highlight-python .notranslate}
    ::: highlight
        quantized_model = AutoModelForCausalLM.from_pretrained(
                                base_model_name,
                                device_map="auto",
                                quantization_config=gptq_config)
    :::
    ::::

3.  Once the model is quantized, you can push the model and tokenizer to Hugging Face Hub for easy share and access.

    :::: {.highlight-python .notranslate}
    ::: highlight
        quantized_model.push_to_hub("llama-2-7b-hf-gptq")
        tokenizer.push_to_hub("llama-2-7b-hf-gptq")
    :::
    ::::

    Or, you can save the model locally using the following snippet.

    :::: {.highlight-python .notranslate}
    ::: highlight
        quantized_model.save_pretrained("llama-2-7b-gptq")
        tokenizer.save_pretrained("llama-2-7b-gptq")
    :::
    ::::
:::

::::: {#exllama-v2-support .section}
### ExLlama-v2 support[\#](#exllama-v2-support "Link to this heading"){.headerlink}

ExLlama is a Python/C++/CUDA implementation of the Llama model that is designed for faster inference with 4-bit GPTQ weights. The ExLlama kernel is activated by default when users create a [`GPTQConfig`{.docutils .literal .notranslate}]{.pre} object. To boost inference speed even further on Instinct GPUs, use the ExLlama-v2 kernels by configuring the [`exllama_config`{.docutils .literal .notranslate}]{.pre} parameter as the following.

:::: {.highlight-python .notranslate}
::: highlight
    from transformers import AutoModelForCausalLM, GPTQConfig
    #pretrained_model_dir = "meta-llama/Llama-2-7b"
    base_model_name = "NousResearch/Llama-2-7b-hf"
    gptq_config = GPTQConfig(bits=4, dataset="c4", exllama_config={"version":2})
    quantized_model = AutoModelForCausalLM.from_pretrained(
                            base_model_name,
                            device_map="auto",
                            quantization_config=gptq_config)
:::
::::
:::::
:::::::::

:::::::::::: {#bitsandbytes .section}
## bitsandbytes[\#](#bitsandbytes "Link to this heading"){.headerlink}

The [ROCm-aware bitsandbytes](https://github.com/ROCm/bitsandbytes){.reference .external} library is a lightweight Python wrapper around CUDA custom functions, in particular 8-bit optimizer, matrix multiplication, and 8-bit and 4-bit quantization functions. The library includes quantization primitives for 8-bit and 4-bit operations through [`bitsandbytes.nn.Linear8bitLt`{.docutils .literal .notranslate}]{.pre} and [`bitsandbytes.nn.Linear4bit`{.docutils .literal .notranslate}]{.pre} and 8-bit optimizers through the [`bitsandbytes.optim`{.docutils .literal .notranslate}]{.pre} module. These modules are supported on AMD Instinct GPUs.

::: {#installing-bitsandbytes .section}
### Installing bitsandbytes[\#](#installing-bitsandbytes "Link to this heading"){.headerlink}

1.  To install bitsandbytes for ROCm 6.0 (and later), use the following commands.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Clone the github repo
        git clone --recurse https://github.com/ROCm/bitsandbytes.git
        cd bitsandbytes
        git checkout rocm_enabled_multi_backend

        # Install dependencies
        pip install -r requirements-dev.txt

        # Use -DBNB_ROCM_ARCH to specify target GPU arch
        cmake -DBNB_ROCM_ARCH="gfx942" -DCOMPUTE_BACKEND=hip -S .

        # Compile the project
        make

        # Install
        python setup.py install
    :::
    ::::

2.  Run [`pip`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`show`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`bitsandbytes`{.docutils .literal .notranslate}]{.pre} to show the information about the installed bitsandbytes package. Its output should look like the following.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        Name: bitsandbytes
        Version: 0.44.0.dev0
        ...
    :::
    ::::
:::

::::: {#using-bitsandbytes-primitives .section}
### Using bitsandbytes primitives[\#](#using-bitsandbytes-primitives "Link to this heading"){.headerlink}

To get started with bitsandbytes primitives, use the following code as reference.

:::: {.highlight-python .notranslate}
::: highlight
    import bitsandbytes as bnb

    # Use Int8 Matrix Multiplication
    bnb.matmul(..., threshold=6.0)

    # Use bitsandbytes 8-bit Optimizers
    adam = bnb.optim.Adam8bit(model.parameters(), lr=0.001, betas=(0.9, 0.995))
:::
::::
:::::

::::::: {#using-bitsandbytes-with-hugging-face-transformers .section}
### Using bitsandbytes with Hugging Face Transformers[\#](#using-bitsandbytes-with-hugging-face-transformers "Link to this heading"){.headerlink}

To load a Transformers model in 4-bit, set [`load_in_4bit=true`{.docutils .literal .notranslate}]{.pre} in [`BitsAndBytesConfig`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-python .notranslate}
::: highlight
    from transformers import AutoModelForCausalLM, BitsAndBytesConfig

    base_model_name = "NousResearch/Llama-2-7b-hf"
    quantization_config = BitsAndBytesConfig(load_in_4bit=True)
    bnb_model_4bit = AutoModelForCausalLM.from_pretrained(
            base_model_name,
            device_map="auto",
            quantization_config=quantization_config)

    # Check the memory footprint with get_memory_footprint method
    print(bnb_model_4bit.get_memory_footprint())
:::
::::

To load a model in 8-bit for inference, use the [`load_in_8bit`{.docutils .literal .notranslate}]{.pre} option.

:::: {.highlight-python .notranslate}
::: highlight
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
:::
::::
:::::::
::::::::::::
:::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](index.html "previous page"){.left-prev}

::: prev-next-info
previous

Use ROCm for AI inference optimization
:::

[](model-acceleration-libraries.html "next page"){.right-next}

::: prev-next-info
next

Model acceleration libraries
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [AMD Quark](#amd-quark){.reference .internal .nav-link}
  - [Installing Quark](#installing-quark){.reference .internal .nav-link}
  - [Using Quark for quantization](#using-quark-for-quantization){.reference .internal .nav-link}
  - [Evaluating the quantized model with vLLM](#evaluating-the-quantized-model-with-vllm){.reference .internal .nav-link}
- [GPTQ](#gptq){.reference .internal .nav-link}
  - [Installing AutoGPTQ](#installing-autogptq){.reference .internal .nav-link}
  - [Using GPTQ with AutoGPTQ](#using-gptq-with-autogptq){.reference .internal .nav-link}
  - [Using GPTQ with Hugging Face Transformers](#using-gptq-with-hugging-face-transformers){.reference .internal .nav-link}
  - [ExLlama-v2 support](#exllama-v2-support){.reference .internal .nav-link}
- [bitsandbytes](#bitsandbytes){.reference .internal .nav-link}
  - [Installing bitsandbytes](#installing-bitsandbytes){.reference .internal .nav-link}
  - [Using bitsandbytes primitives](#using-bitsandbytes-primitives){.reference .internal .nav-link}
  - [Using bitsandbytes with Hugging Face Transformers](#using-bitsandbytes-with-hugging-face-transformers){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
