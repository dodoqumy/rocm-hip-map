---
title: "Fine-tuning and inference using multiple GPUs"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/fine-tuning/multi-gpu-fine-tuning-and-inference.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../index.html){.nav-link}
- 
- [Fine-tuning and inference](fine-tuning-and-inference.html){.nav-link}
- Fine-tuning\...
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
# Fine-tuning and inference using multiple GPUs

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Environment setup](#environment-setup){.reference .internal .nav-link}
  - [Setting up the base implementation environment](#setting-up-the-base-implementation-environment){.reference .internal .nav-link}
- [Hugging Face Accelerate for fine-tuning and inference](#hugging-face-accelerate-for-fine-tuning-and-inference){.reference .internal .nav-link}
- [torchtune for fine-tuning and inference](#torchtune-for-fine-tuning-and-inference){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::: {#fine-tuning-and-inference-using-multiple-gpus .section}
# Fine-tuning and inference using multiple GPUs[\#](#fine-tuning-and-inference-using-multiple-gpus "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 7 min read time
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

This section explains how to fine-tune a model on a multi-accelerator system. See [[Single-accelerator fine-tuning]{.doc}](single-gpu-fine-tuning-and-inference.html){.reference .internal} for a single GPU setup.

:::::: {#environment-setup .section}
[]{#fine-tuning-llms-multi-gpu-env}

## Environment setup[\#](#environment-setup "Link to this heading"){.headerlink}

This section was tested using the following hardware and software environment.

::: pst-scrollable-table-container
  ------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Hardware     4 AMD Instinct MI300X GPUs
  Software     ROCm 6.1, Ubuntu 22.04, PyTorch 2.1.2, Python 3.10
  Libraries    [`transformers`{.docutils .literal .notranslate}]{.pre} [`datasets`{.docutils .literal .notranslate}]{.pre} [`accelerate`{.docutils .literal .notranslate}]{.pre} [`huggingface-hub`{.docutils .literal .notranslate}]{.pre} [`peft`{.docutils .literal .notranslate}]{.pre} [`trl`{.docutils .literal .notranslate}]{.pre} [`scipy`{.docutils .literal .notranslate}]{.pre}
  Base model   [`meta-llama/Llama-2-7b-chat-hf`{.docutils .literal .notranslate}]{.pre}
  ------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

:::: {#setting-up-the-base-implementation-environment .section}
[]{#fine-tuning-llms-multi-gpu-env-setup}

### Setting up the base implementation environment[\#](#setting-up-the-base-implementation-environment "Link to this heading"){.headerlink}

1.  Install PyTorch for ROCm. Refer to the [[PyTorch installation guide]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html "(in ROCm installation on Linux v7.2.2)"){.reference .external}. For consistent installation, it's recommended to use official ROCm prebuilt Docker images with the framework pre-installed.

2.  In the Docker container, check the availability of ROCm-capable GPUs using the following command.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        amd-smi static --board
    :::
    ::::

3.  Check that your GPUs are available to PyTorch.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import torch
        print("Is a ROCm-GPU detected? ", torch.cuda.is_available())
        print("How many ROCm-GPUs are detected? ", torch.cuda.device_count())
    :::
    ::::

    If successful, your output should look like this:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        >>> print("Is a ROCm-GPU detected? ", torch.cuda.is_available())
        Is a ROCm-GPU detected?  True
        >>> print("How many ROCm-GPUs are detected? ", torch.cuda.device_count())
        How many ROCm-GPUs are detected?  4
    :::
    ::::

::: {.admonition .tip}
Tip

During training and inference, you can check the memory usage by running the [`amd-smi`{.docutils .literal .notranslate}]{.pre} command in your terminal. This tool helps you see which GPUs are involved.
:::
::::
::::::

:::::: {#hugging-face-accelerate-for-fine-tuning-and-inference .section}
[]{#fine-tuning-llms-multi-gpu-hugging-face-accelerate}

## Hugging Face Accelerate for fine-tuning and inference[\#](#hugging-face-accelerate-for-fine-tuning-and-inference "Link to this heading"){.headerlink}

[Hugging Face Accelerate](https://huggingface.co/docs/accelerate/en/index){.reference .external} is a library that simplifies turning raw PyTorch code for a single GPU into code for multiple GPUs for LLM fine-tuning and inference. It is integrated with [Transformers](https://huggingface.co/docs/transformers/en/index){.reference .external}, so you can scale your PyTorch code while maintaining performance and flexibility.

As a brief example of model fine-tuning and inference using multiple GPUs, let's use Transformers and load in the Llama 2 7B model.

Here, let's reuse the code in [[Single-accelerator fine-tuning]{.std .std-ref}](single-gpu-fine-tuning-and-inference.html#fine-tuning-llms-single-gpu-download-model-dataset){.reference .internal} to load the base model and tokenizer.

Now, it's important to adjust how you load the model. Add the [`device_map`{.docutils .literal .notranslate}]{.pre} parameter to your base model configuration.

:::: {.highlight-python .notranslate}
::: highlight
    ...
    base_model_name = "meta-llama/Llama-2-7b-chat-hf"

    # Load base model to GPU memory
    base_model = AutoModelForCausalLM.from_pretrained(
            base_model_name,
            device_map = "auto",
            trust_remote_code = True)
    ...
    # Run training
    sft_trainer.train()
:::
::::

::: {.admonition .note}
Note

You can let Accelerate handle the device map computation by setting [`device_map`{.docutils .literal .notranslate}]{.pre} to one of the supported options ([`"auto"`{.docutils .literal .notranslate}]{.pre}, [`"balanced"`{.docutils .literal .notranslate}]{.pre}, [`"balanced_low_0"`{.docutils .literal .notranslate}]{.pre}, [`"sequential"`{.docutils .literal .notranslate}]{.pre}).

It's recommended to set the [`device_map`{.docutils .literal .notranslate}]{.pre} parameter to [`“auto”`{.docutils .literal .notranslate}]{.pre} to allow Accelerate to automatically and efficiently allocate the model given the available resources (four GPUs in this case).

When you have more GPU memory available than the model size, here is the difference between each [`device_map`{.docutils .literal .notranslate}]{.pre} option:

- [`"auto"`{.docutils .literal .notranslate}]{.pre} and [`"balanced"`{.docutils .literal .notranslate}]{.pre} evenly split the model on all available GPUs, making it possible for you to use a batch size greater than 1.

- [`"balanced_low_0"`{.docutils .literal .notranslate}]{.pre} evenly splits the model on all GPUs except the first one, and only puts on GPU 0 what does not fit on the others. This option is great when you need to use GPU 0 for some processing of the outputs, like when using the generate function for Transformers models.

- [`"sequential"`{.docutils .literal .notranslate}]{.pre} will fit what it can on GPU 0, then move on GPU 1 and so forth. Not all GPUs might be used.
:::

After loading the model in this way, the model is fully ready to use the resources available to it.
::::::

::: {#torchtune-for-fine-tuning-and-inference .section}
[]{#fine-tuning-llms-multi-gpu-torchtune}

## torchtune for fine-tuning and inference[\#](#torchtune-for-fine-tuning-and-inference "Link to this heading"){.headerlink}

[torchtune](https://meta-pytorch.org/torchtune/main/){.reference .external} is a PyTorch-native library for easy single and multi-GPU model fine-tuning and inference with LLMs.

1.  Install torchtune using pip.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        # Install torchtune with PyTorch release 2.2.2+
        pip install torchtune

        # To confirm that the package is installed correctly
        tune --help
    :::
    ::::

    The output should look like this:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        usage: tune [-h] {download,ls,cp,run,validate} ...

        Welcome to the TorchTune CLI!

        options:
          -h, --help            show this help message and exit

        subcommands:
          {download,ls,cp,run,validate}
    :::
    ::::

2.  torchtune recipes are designed around easily composable components and workable training loops, with minimal abstraction getting in the way of fine-tuning. Run [`tune`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`ls`{.docutils .literal .notranslate}]{.pre} to show built-in torchtune configuration recipes.

    :::: {.highlight-shell .notranslate}
    ::: highlight
        RECIPE                                   CONFIG
        full_finetune_single_device              llama2/7B_full_low_memory
                                                 llama3/8B_full_single_device
                                                 mistral/7B_full_low_memory
        full_finetune_distributed                llama2/7B_full
                                                 llama2/13B_full
                                                 llama3/8B_full
                                                 mistral/7B_full
                                                 gemma/2B_full
        lora_finetune_single_device              llama2/7B_lora_single_device
                                                 llama2/7B_qlora_single_device
                                                 llama3/8B_lora_single_device
                                                 llama3/8B_qlora_single_device
                                                 llama2/13B_qlora_single_device
                                                 mistral/7B_lora_single_device
    :::
    ::::

    The [`RECIPE`{.docutils .literal .notranslate}]{.pre} column shows the easy-to-use and workable fine-tuning and inference recipes for popular fine-tuning techniques (such as LoRA). The [`CONFIG`{.docutils .literal .notranslate}]{.pre} column lists the YAML configurations for easily configuring training, evaluation, quantization, or inference recipes.

    The snippet shows the architecture of a model's YAML configuration file:

    :::: {.highlight-yaml .notranslate}
    ::: highlight
        # Model arguments
        model:
          _component_: torchtune.models.llama2.lora_llama2_7b
          lora_attn_modules: ['q_proj', 'v_proj']
          apply_lora_to_mlp: False
          apply_lora_to_output: False
          lora_rank: 8
          lora_alpha: 16

        tokenizer:
          _component_: torchtune.models.llama2.llama2_tokenizer
          path: /tmp/Llama-2-7b-hf/tokenizer.model

        # Dataset and sampler
        dataset:
          _component_: torchtune.datasets.alpaca_cleaned_dataset
          train_on_input: True
    :::
    ::::

3.  This configuration file defines the fine-tuning base model path, data set, hyper-parameters for optimizer and scheduler, and training data type. To download the base model for fine-tuning, run the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        tune download meta-llama/Llama-2-7b-hf --output-dir /tmp/Llama-2-7b-hf --hf-token
    :::
    ::::

    The output directory argument for [`--output-dir`{.docutils .literal .notranslate}]{.pre} should map the model path specified in YAML config file.

4.  To launch [`lora_finetune_distributed`{.docutils .literal .notranslate}]{.pre} on four devices, run the following command:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        tune run --nnodes 1 --nproc_per_node 4 lora_finetune_distributed --config llama2/7B_lora
    :::
    ::::

    If successful, you should something like the following output:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        INFO:torchtune.utils.logging:FSDP is enabled. Instantiating Model on CPU for Rank 0 ...
        INFO:torchtune.utils.logging:Model instantiation took 7.32 secs
        INFO:torchtune.utils.logging:Memory Stats after model init:
        {'peak_memory_active': 9.478172672, 'peak_memory_alloc': 8.953868288, 'peak_memory_reserved': 11.112808448}
        INFO:torchtune.utils.logging:Optimizer and loss are initialized.
        INFO:torchtune.utils.logging:Dataset and Sampler are initialized.
        INFO:torchtune.utils.logging:Learning rate scheduler is initialized.
        1|111|Loss: 1.5790324211120605:   7%|█                                          | 114/1618
    :::
    ::::

Read more about inference frameworks in [[LLM inference frameworks]{.doc}](../inference/llm-inference-frameworks.html){.reference .internal}.
:::
:::::::::::::::::::::

::::: prev-next-area
[](single-gpu-fine-tuning-and-inference.html "previous page"){.left-prev}

::: prev-next-info
previous

Fine-tuning and inference using a single GPU
:::

[](../inference/index.html "next page"){.right-next}

::: prev-next-info
next

Use ROCm for AI inference
:::
:::::
::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Environment setup](#environment-setup){.reference .internal .nav-link}
  - [Setting up the base implementation environment](#setting-up-the-base-implementation-environment){.reference .internal .nav-link}
- [Hugging Face Accelerate for fine-tuning and inference](#hugging-face-accelerate-for-fine-tuning-and-inference){.reference .internal .nav-link}
- [torchtune for fine-tuning and inference](#torchtune-for-fine-tuning-and-inference){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::
