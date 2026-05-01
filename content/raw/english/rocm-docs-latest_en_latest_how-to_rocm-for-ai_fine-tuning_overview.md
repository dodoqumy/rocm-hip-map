---
title: "Conceptual overview of fine-tuning LLMs"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/fine-tuning/overview.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../index.html){.nav-link}
- [Use ROCm for fine-tuning LLMs](index.html){.nav-link}
- Conceptual\...
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
# Conceptual overview of fine-tuning LLMs

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [The challenge of fine-tuning models](#the-challenge-of-fine-tuning-models){.reference .internal .nav-link}
- [Optimizations for model fine-tuning](#optimizations-for-model-fine-tuning){.reference .internal .nav-link}
- [Walkthrough](#walkthrough){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::: {#conceptual-overview-of-fine-tuning-llms .section}
# Conceptual overview of fine-tuning LLMs[\#](#conceptual-overview-of-fine-tuning-llms "Link to this heading"){.headerlink}

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

Large language models (LLMs) are trained on massive amounts of text data to generate coherent and fluent text. The underlying *transformer* architecture is the fundamental building block of all LLMs. Transformers enable LLMs to understand and generate text by capturing contextual relationships and long-range dependencies. To better understand the philosophy of the transformer architecture, review the foundational [Attention is all you need](https://arxiv.org/pdf/1706.03762.pdf){.reference .external} paper.

By further training pre-trained LLMs, the fine-tuned model can gain knowledge related to specific fields or tasks, thereby significantly improving its performance in that field or task. The core idea of fine-tuning is to use the parameters of the pre-trained model as the starting point for new tasks and shape it through a small amount of specific domain or task data, expanding the original model's capability to new tasks or datasets.

Fine-tuning can effectively improve the performance of existing pre-trained models in specific application scenarios. Continuous training and adjustment of the parameters of the base model in the target domain or task can better capture the semantic characteristics and patterns in specific scenarios, thereby significantly improving the key indicators of the model in that domain or task. For example, by fine-tuning the Llama 2 model, its performance in certain applications can be improve over the base model.

::: {#the-challenge-of-fine-tuning-models .section}
[]{#fine-tuning-llms-concept-challenge}

## The challenge of fine-tuning models[\#](#the-challenge-of-fine-tuning-models "Link to this heading"){.headerlink}

However, the computational cost of fine-tuning is still high, especially for complex models and large datasets, which poses distinct challenges related to substantial computational and memory requirements. This might be a barrier for GPUs with low computing power or limited device memory resources.

For example, suppose we have a language model with 7 billion (7B) parameters, represented by a weight matrix [\\(W\\)]{.math .notranslate .nohighlight}. During backpropagation, the model needs to learn a [\\(ΔW\\)]{.math .notranslate .nohighlight} matrix, which updates the original weights to minimize the value of the loss function.

The weight update is as follows: [\\(W\_{updated} = W + ΔW\\)]{.math .notranslate .nohighlight}.

If the weight matrix [\\(W\\)]{.math .notranslate .nohighlight} contains 7B parameters, then the weight update matrix [\\(ΔW\\)]{.math .notranslate .nohighlight} should also contain 7B parameters. Therefore, the [\\(ΔW\\)]{.math .notranslate .nohighlight} calculation is computationally and memory intensive.

<figure id="id1" class="align-default">
<img src="../../../_images/weight-update.png" alt="Weight update diagram" />
<figcaption><p><span class="caption-text">(a) Weight update in regular fine-tuning. (b) Weight update in LoRA where the product of matrix A (<span class="math notranslate nohighlight">\(M\times K\)</span>) and matrix B (<span class="math notranslate nohighlight">\(K\times N\)</span>) is <span class="math notranslate nohighlight">\(ΔW(M\times N)\)</span>; dimension K is a hyperparameter. By representing <span class="math notranslate nohighlight">\(ΔW\)</span> as the product of two smaller matrices (A and B) with a lower rank K, the number of trainable parameters is significantly reduced.</span><a href="#id1" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>
:::

::: {#optimizations-for-model-fine-tuning .section}
[]{#fine-tuning-llms-concept-optimizations}

## Optimizations for model fine-tuning[\#](#optimizations-for-model-fine-tuning "Link to this heading"){.headerlink}

Low-Rank Adaptation (LoRA) is a technique allowing fast and cost-effective fine-tuning of state-of-the-art LLMs that can overcome this issue of high memory consumption.

LoRA accelerates the adjustment process and reduces related memory costs. To be precise, LoRA decomposes the portion of weight changes [\\(ΔW\\)]{.math .notranslate .nohighlight} into high-precision low-rank representations, which do not require the calculations of all [\\(ΔW\\)]{.math .notranslate .nohighlight}. It learns the decomposition representation of [\\(ΔW\\)]{.math .notranslate .nohighlight} during training, as shown in the [[weight update diagram]{.std .std-ref}](#fine-tuning-llms-concept-challenge){.reference .internal}. This is how LoRA saves on computing resources.

LoRA is integrated into the [Hugging Face Parameter-Efficient Fine-Tuning (PEFT)](https://huggingface.co/docs/peft/en/index){.reference .external} library, as well as other computation and memory efficiency optimization variants for model fine-tuning such as [AdaLoRA](https://huggingface.co/docs/peft/en/package_reference/adalora){.reference .external}. This library efficiently adapts large pre-trained models to various downstream applications without fine-tuning all model parameters. PEFT methods only fine-tune a few model parameters, significantly decreasing computational and storage costs while yielding performance comparable to a fully fine-tuned model. PEFT is integrated with the [Hugging Face Transformers](https://huggingface.co/docs/transformers/en/index){.reference .external} library, providing a faster and easier way to load, train, and use large models for inference.

To simplify running a fine-tuning implementation, the [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/en/index){.reference .external} library provides a set of tools to train transformer language models with reinforcement learning, from the Supervised Fine-Tuning step (SFT), Reward Modeling step (RM), to the Proximal Policy Optimization (PPO) step. The [`SFTTrainer`{.docutils .literal .notranslate}]{.pre} API in TRL encapsulates these PEFT optimizations so you can easily import their custom training configuration and run the training process.
:::

::: {#walkthrough .section}
[]{#fine-tuning-llms-walkthrough-desc}

## Walkthrough[\#](#walkthrough "Link to this heading"){.headerlink}

To demonstrate the benefits of LoRA and the ideal compute compatibility of using PEFT and TRL libraries on AMD ROCm-compatible GPUs, let's step through a comprehensive implementation of the fine-tuning process using the Llama 2 7B model with LoRA tailored specifically for question-and-answer tasks on AMD MI300X GPUs.

Before starting, review and understand the key components of this walkthrough:

- [Llama 2](https://huggingface.co/meta-llama){.reference .external}: a family of large language models developed and publicly released by Meta. Its variants range in scale from 7 billion to 70 billion parameters.

- Fine-tuning: a critical process that refines LLMs for specialized tasks and optimizes performance.

- LoRA: a memory-efficient implementation of LLM fine-tuning that significantly reduces the number of trainable parameters.

- [SFTTrainer](https://huggingface.co/docs/trl/v0.8.6/en/sft_trainer#supervised-fine-tuning-trainer){.reference .external}: an optimized trainer with a simple interface to easily fine-tune pre-trained models with PEFT adapters, for example, LoRA, for memory efficiency purposes on a custom dataset.

Continue the walkthrough in [[Fine-tuning and inference]{.doc}](fine-tuning-and-inference.html){.reference .internal}.
:::
:::::::::::::::

::::: prev-next-area
[](index.html "previous page"){.left-prev}

::: prev-next-info
previous

Use ROCm for fine-tuning LLMs
:::

[](fine-tuning-and-inference.html "next page"){.right-next}

::: prev-next-info
next

Fine-tuning and inference
:::
:::::
::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [The challenge of fine-tuning models](#the-challenge-of-fine-tuning-models){.reference .internal .nav-link}
- [Optimizations for model fine-tuning](#optimizations-for-model-fine-tuning){.reference .internal .nav-link}
- [Walkthrough](#walkthrough){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::
