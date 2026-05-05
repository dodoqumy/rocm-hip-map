---
title: "Training a model"
source_url: "https://rocm.docs.amd.com/en/docs-6.2.0/how-to/rocm-for-ai/train-a-model.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:22:46.543261+00:00
content_hash: "cdbe4312935a77ff"
---

# Training a model[#](#training-a-model)



The following is a brief overview of popular component paths per AI development use-case, such as training, LLMs, and inferencing.

## Accelerating model training[#](#accelerating-model-training)

To train a large model like GPT2 or Llama 2 70B, a single accelerator or GPU cannot store all the model parameters required for training. What if you could convert the single-GPU training code to run on multiple accelerators or GPUs? PyTorch offers distributed training solutions to facilitate this.

### PyTorch distributed[#](#pytorch-distributed)

As of PyTorch 1.6.0, features in `torch.distributed`

are categorized into three main components:

In this guide, the focus is on the distributed data-parallelism strategy as it’s the most popular. To get started with DDP, let’s first understand how to coordinate the model and its training data across multiple accelerators or GPUs.

The DDP workflow on multiple accelerators or GPUs is as follows:

Split the current global training batch into small local batches on each GPU. For instance, if you have 8 GPUs and the global batch is set at 32 samples, each of the 8 GPUs will have a local batch size of 4 samples.

Copy the model to every device so each device can process its local batches independently.

Run a forward pass, then a backward pass, and output the gradient of the weights with respect to the loss of the model for that local batch. This happens in parallel on multiple devices.

Synchronize the local gradients computed by each device and combine them to update the model weights. The updated weights are then redistributed to each device.


In DDP training, each process or worker owns a replica of the model and processes a batch of data, then the reducer uses
`allreduce`

to sum up gradients over different workers.

See the following developer blogs for more in-depth explanations and examples.

### PyTorch FSDP[#](#pytorch-fsdp)

As noted in [PyTorch distributed](#rocm-for-ai-pytorch-distributed), in DDP model weights and optimizer states
are evenly replicated across all workers. Fully Sharded Data Parallel (FSDP) is a type of data parallelism that shards
model parameters, optimizer states, and gradients across DDP ranks.

When training with FSDP, the GPU memory footprint is smaller than when training with DDP across all workers. This makes the training of some very large models feasible by allowing larger models or batch sizes to fit on-device. However, this comes with the cost of increased communication volume. The communication overhead is reduced by internal optimizations like overlapping communication and computation.

For a high-level overview of how FSDP works, review [Getting started with Fully Sharded Data Parallel](https://pytorch.org/tutorials/intermediate/FSDP_tutorial.html#how-fsdp-works).

For detailed training steps, refer to the [PyTorch FSDP examples](https://github.com/pytorch/examples/tree/main/distributed/FSDP).

### DeepSpeed[#](#deepspeed)

[DeepSpeed](https://deepspeed.ai) offers system innovations that make large-scale deep learning training effective,
efficient, and easy to use. Innovations such as ZeRO, 3D-Parallelism, DeepSpeed-MoE, ZeRO-Infinity, and so on fall under
the training pillar.

See [Pre-training a large language model with Megatron-DeepSpeed on multiple AMD GPUs — ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/megatron-deepspeed-pretrain/README.html) for a detailed example of
training with DeepSpeed on an AMD accelerator or GPU.

### Automatic mixed precision (AMP)[#](#automatic-mixed-precision-amp)

As models increase in size, the time and memory needed to train them; that is, their cost also increases. Any measure we
can take to reduce training time and memory usage through [automatic mixed precision](https://pytorch.org/docs/stable/amp.html) (AMP) is highly beneficial for most use cases.

See [Automatic mixed precision in PyTorch using AMD GPUs — ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/automatic-mixed-precision/README.html#automatic-mixed-precision-in-pytorch-using-amd-gpus)
for more information about running AMP on an AMD accelerator.

## Fine-tuning your model[#](#fine-tuning-your-model)

ROCm supports multiple techniques for [optimizing fine-tuning](../llm-fine-tuning-optimization/overview.html#fine-tuning-llms-concept-optimizations), for
example, LoRA, QLoRA, PEFT, and FSDP.

Learn more about challenges and solutions for model fine-tuning in [Fine-tuning LLMs and inference optimization](../llm-fine-tuning-optimization/index.html).

The following developer blogs showcase examples of how to fine-tune a model on an AMD accelerator or GPU.

Fine-tuning Llama2 with LoRA

Fine-tuning Llama2 with QLoRA

Fine-tuning a BERT-based LLM for a text classification task using JAX

Fine-tuning StarCoder using PEFT

Recipes for fine-tuning Llama2 and 3 with

`llama-recipes`
