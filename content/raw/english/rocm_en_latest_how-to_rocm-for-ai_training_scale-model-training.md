---
title: "Scaling model training"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/scale-model-training.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item
- [](../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../index.html){.nav-link}
- [Use ROCm for training](index.html){.nav-link}
- Scaling\...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# Scaling model training

## Contents

- [PyTorch distributed](#pytorch-distributed){.reference .internal .nav-link}
  - [PyTorch FSDP](#pytorch-fsdp){.reference .internal .nav-link}
  - [DeepSpeed](#deepspeed){.reference .internal .nav-link}
  - [Automatic mixed precision (AMP)](#automatic-mixed-precision-amp){.reference .internal .nav-link}
- [Fine-tuning your model](#fine-tuning-your-model){.reference .internal .nav-link}


# Scaling model training[\#](#scaling-model-training "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 6 min read time

Applies to Linux


To train a large-scale model like OpenAI GPT-2 or Meta Llama 2 70B, a single GPU cannot store all the model parameters required for training. This immense scale presents a fundamental challenge: no single GPU can simultaneously store and process the entire model's parameters during training. PyTorch provides an answer to this computational constraint through its distributed training frameworks.


## PyTorch distributed[\#](#pytorch-distributed "Link to this heading"){.headerlink}

Features in [`torch.distributed`{.docutils .literal .notranslate}]{.pre} are categorized into three main components:

- [Distributed data-parallel training](https://pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html){.reference .external} (DDP)

- [RPC-Based distributed training](https://pytorch.org/docs/stable/rpc.html){.reference .external} (RPC)

- [Collective communication](https://pytorch.org/docs/stable/distributed.html){.reference .external}

In this topic, the focus is on the distributed data-parallelism strategy as it's the most popular. To get started with DDP, you need to first understand how to coordinate the model and its training data across multiple GPUs.

The DDP workflow on multiple GPUs is as follows:

1.  Split the current global training batch into small local batches on each GPU. For instance, if you have 8 GPUs and the global batch is set at 32 samples, each of the 8 GPUs will have a local batch size of 4 samples.

2.  Copy the model to every device so each can process its local batches independently.

3.  Run a forward pass, then a backward pass, and output the gradient of the weights with respect to the loss of the model for that local batch. This happens in parallel on multiple devices.

4.  Synchronize the local gradients computed by each device and combine them to update the model weights. The updated weights are then redistributed to each device.

In DDP training, each process or worker owns a replica of the model and processes a batch of data, and then the reducer uses [`allreduce`{.docutils .literal .notranslate}]{.pre} to sum up gradients over different workers.

See the following developer blogs for more in-depth explanations and examples.

- [Multi GPU training with DDP --- PyTorch Tutorials](https://docs.pytorch.org/tutorials/beginner/ddp_series_multigpu.html){.reference .external}

- [Building a decoder transformer model on AMD GPUs --- ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/decoder-transformer/README.html#distributed-training-on-multiple-gpus){.reference .external}


### PyTorch FSDP[\#](#pytorch-fsdp "Link to this heading"){.headerlink}

As noted in [[PyTorch distributed]{.std .std-ref}](#rocm-for-ai-pytorch-distributed){.reference .internal}, DDP model weights and optimizer states are evenly replicated across all workers. Fully Sharded Data Parallel (FSDP) is a type of data parallelism that shards model parameters, optimizer states, and gradients across DDP ranks.

When training with FSDP, the GPU memory footprint is smaller than when training with DDP across all workers. This makes training some very large models feasible by allowing larger models or batch sizes to fit on-device. However, this comes with the cost of increased communication volume. The communication overhead is reduced by internal optimizations like overlapping communication and computation.

For a high-level overview of how FSDP works, review [Getting started with Fully Sharded Data Parallel](https://pytorch.org/tutorials/intermediate/FSDP_tutorial.html#how-fsdp-works){.reference .external}.

For detailed training steps, see [PyTorch FSDP examples](https://github.com/pytorch/examples/tree/main/distributed/FSDP){.reference .external}.


### DeepSpeed[\#](#deepspeed "Link to this heading"){.headerlink}

[DeepSpeed](https://deepspeed.ai){.reference .external} offers system innovations that make large-scale deep learning training effective, efficient, and easy to use. Innovations such as ZeRO, 3D-Parallelism, DeepSpeed-MoE, ZeRO-Infinity, and so on fall under the training pillar.

See [Pre-training a large language model with Megatron-DeepSpeed on multiple AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/megatron-deepspeed-pretrain/README.html){.reference .external} for a detailed example of training with DeepSpeed on an AMD GPU.


### Automatic mixed precision (AMP)[\#](#automatic-mixed-precision-amp "Link to this heading"){.headerlink}

As models increase in size, so do the time and memory needed to train them; their cost also increases. Any measure we can take to reduce training time and memory usage through [automatic mixed precision](https://pytorch.org/docs/stable/amp.html){.reference .external} (AMP) is highly beneficial for most use cases.

See [Automatic mixed precision in PyTorch using AMD GPUs --- ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/automatic-mixed-precision/README.html#automatic-mixed-precision-in-pytorch-using-amd-gpus){.reference .external} for more information about running AMP on an AMD Instinct-Series GPU.


## Fine-tuning your model[\#](#fine-tuning-your-model "Link to this heading"){.headerlink}

ROCm supports multiple techniques for [[optimizing fine-tuning]{.std .std-ref}](../fine-tuning/overview.html#fine-tuning-llms-concept-optimizations){.reference .internal}, for example, LoRA, QLoRA, PEFT, and FSDP.

Learn more about challenges and solutions for model fine-tuning in [[Use ROCm for fine-tuning LLMs]{.doc}](../fine-tuning/index.html){.reference .internal}.

The following developer blogs showcase examples of fine-tuning a model on an AMD GPU.

- Fine-tuning Llama2 with LoRA

  - [Fine-tune Llama 2 with LoRA: Customizing a large language model for question-answering](https://rocm.blogs.amd.com/artificial-intelligence/llama2-lora/README.html){.reference .external}

- Fine-tuning Llama2 with QLoRA

  - [Enhancing LLM accessibility: A deep dive into QLoRA through fine-tuning Llama 2 on a single AMD GPU](https://rocm.blogs.amd.com/artificial-intelligence/llama2-Qlora/README.html){.reference .external}

- Fine-tuning a BERT-based LLM for a text classification task using JAX

  - [LLM distributed supervised fine-tuning with JAX](https://rocm.blogs.amd.com/artificial-intelligence/distributed-sft-jax/README.html){.reference .external}

- Fine-tuning StarCoder using PEFT

  - [Instruction fine-tuning of StarCoder with PEFT on multiple AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/starcoder-fine-tune/README.html){.reference .external}

- Recipes for fine-tuning Llama2 and 3 with [`llama-recipes`{.docutils .literal .notranslate}]{.pre}

  - [meta-llama/llama-recipes: Scripts for fine-tuning Meta Llama3 with composable FSDP & PEFT methods to cover single/multi-node GPUs](https://github.com/meta-llama/llama-cookbook/tree/main/getting-started/finetuning){.reference .external}

::::: prev-next-area
[](benchmark-docker/mpt-llm-foundry.html "previous page"){.left-prev}

::: prev-next-info
previous

Training MPT-30B with LLM Foundry on ROCm

[](../fine-tuning/index.html "next page"){.right-next}

::: prev-next-info
next

Use ROCm for fine-tuning LLMs

:::: sidebar-secondary-item
Contents

- [PyTorch distributed](#pytorch-distributed){.reference .internal .nav-link}
  - [PyTorch FSDP](#pytorch-fsdp){.reference .internal .nav-link}
  - [DeepSpeed](#deepspeed){.reference .internal .nav-link}
  - [Automatic mixed precision (AMP)](#automatic-mixed-precision-amp){.reference .internal .nav-link}
- [Fine-tuning your model](#fine-tuning-your-model){.reference .internal .nav-link}
