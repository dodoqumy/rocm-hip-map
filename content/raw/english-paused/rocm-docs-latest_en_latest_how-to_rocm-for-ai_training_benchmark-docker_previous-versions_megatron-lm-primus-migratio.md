---
title: "Migrating workloads to Primus (Megatron backend) from Megatron-LM"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/megatron-lm-primus-migration-guide.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:57:47.634698+00:00
content_hash: "99afa091d74f38e1"
---

::::::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

::::::::::::::::::::::::::::::::::::::::::::::
bd-content
:::::::::::::::::::::::::::::::::::::::::
bd-article-container
:::::::
{.bd-header-article .d-print-none}
::::::
{.header-article-items .header-article__inner}
::
header-article-items__start

header-article-item
[]{.fa-solid .fa-angle-right}

header-article-item

::

::
header-article-items__end
:
header-article-item

article-header-buttons
[]{.fa-solid .fa-list}

:
::
::::::
:::::::

{#jb-print-docs-body .onlyprint}
# Migrating workloads to Primus (Megatron backend) from Megatron-LM

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

:::::::::::::::::::::::::::
{#migrating-workloads-to-primus-megatron-backend-from-megatron-lm .section}
# Migrating workloads to Primus (Megatron backend) from Megatron-LM[\#](#migrating-workloads-to-primus-megatron-backend-from-megatron-lm "Link to this heading"){.headerlink}

::::::::
{#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::
{.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::
{.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::
{.sd-container-fluid .sd-sphinx-override .docutils}
::::
{.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 5 min read time

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

::::
:::::
::::::
:::::::
::::::::

Primus supports Megatron-Core as backend optimization library, replacing ROCm Megatron-LM. This document outlines the steps to migrate workload from ROCm Megatron-LM to Primus with the Megatron backend.

:::::::::
{#model-architecture .section}
## Model architecture[\#](#model-architecture "Link to this heading"){.headerlink}

ROCm Megatron-LM defines model architecture parameters in the training scripts; for example, the Llama 3 8B model parameters are defined in [examples/llama/train_llama3.sh](https://github.com/ROCm/Megatron-LM/blob/rocm_dev/examples/llama/train_llama3.sh#L117){.reference .external} as shown below:

:
{.highlight-bash .notranslate}

highlight
    HIDDEN_SIZE=4096
    FFN_HIDDEN_SIZE=14336
    NUM_LAYERS=32
    NUM_HEADS=32
    NUM_KV_HEADS=8

:

Primus defines the model architecture through model YAML configuration files inside the [`primus/configs/models/megatron/`{.docutils .literal .notranslate}]{.pre} repository. For example, Llama 3 8B model architecture parameters are defined in [primus/configs/models/megatron/llama3_8B.yaml](https://github.com/AMD-AIG-AIMA/Primus/blob/v0.1.0-rc1/primus/configs/models/megatron/llama3_8B.yaml){.reference .external} as shown below:

:
{.highlight-yaml .notranslate}

highlight
    bases:
      - llama3_base.yaml

    tokenizer_type: Llama3Tokenizer
    tokenizer_model: meta-llama/Llama-3.1-8B

    ffn_hidden_size: 14336
    hidden_size: 4096
    num_attention_heads: 32
    num_layers: 32
    num_query_groups: 8

:

Primus' model config files follow a hierarchical design, meaning that new model config YAMLs can inherit existing model config files by importing them as bases. For example, [llama3.1_8B.yaml](https://github.com/AMD-AIG-AIMA/Primus/blob/v0.1.0-rc1/primus/configs/models/megatron/llama3.1_8B.yaml){.reference .external} uses [`llama3_8B.yaml`{.docutils .literal .notranslate}]{.pre} as a base config and overrides few parameters, as shown below. In this example, [`llama3.1_8B`{.docutils .literal .notranslate}]{.pre} overrides the [`max_position_embeddings`{.docutils .literal .notranslate}]{.pre} value:

:
{.highlight-yaml .notranslate}

highlight
    bases:
      - llama3_8B.yaml

    tokenizer_type: Llama3Tokenizer
    tokenizer_model: meta-llama/Llama-3.1-8B

    max_position_embeddings: 131072

:

::
{.admonition .tip}
Tip

Primus provides [`llama_base.yaml`{.docutils .literal .notranslate}]{.pre} as the base configuration, which can be used as bases for additional model architectures. For example, [mixtral_base.yaml](https://github.com/AMD-AIG-AIMA/Primus/blob/v0.1.0-rc1/primus/configs/models/megatron/mixtral_base.yaml){.reference .external} and [deepseek_v3_base.yaml](https://github.com/AMD-AIG-AIMA/Primus/blob/v0.1.0-rc1/primus/configs/models/megatron/deepseek_v3_base.yaml){.reference .external} define [`llama_base.yaml`{.docutils .literal .notranslate}]{.pre} as its base.

:
{.highlight-yaml .notranslate}

highlight
    # Example mixtral_base.yaml:

    bases:
      - llama_base.yaml

    init_method_std: 0.01
    rotary_base: 1000000
    qk_layernorm: false

    group_query_attention: true
    num_query_groups: 8

    # moe parameters
    num_experts: 8
    moe_router_topk: 2
    moe_router_load_balancing_type: aux_loss
    moe_aux_loss_coeff: 1e-2
    moe_grouped_gemm: true
    moe_token_dispatcher_type: alltoall

:
::

It is recommended to add a new [`${MODEL_NAME}_base.yaml`{.docutils .literal .notranslate}]{.pre} to add a new category of model and define new models on top of it. For example, to add Qwen2.5 models in Primus, we define [qwen2.5_base.yaml](https://github.com/AMD-AIG-AIMA/Primus/blob/v0.1.0-rc1/primus/configs/models/megatron/qwen2.5_base.yaml){.reference .external} and build [qwen2.5_7B.yaml](https://github.com/AMD-AIG-AIMA/Primus/blob/v0.1.0-rc1/primus/configs/models/megatron/qwen2.5_7B.yaml){.reference .external} and [qwen2.5_72B.yaml](https://github.com/AMD-AIG-AIMA/Primus/blob/v0.1.0-rc1/primus/configs/models/megatron/qwen2.5_72B.yaml){.reference .external} using [`qwen2.5_base.yaml`{.docutils .literal .notranslate}]{.pre} as the base config.
:::::::::

::::
{#training-parameters .section}
## Training parameters[\#](#training-parameters "Link to this heading"){.headerlink}

ROCm Megatron-LM also defines the training parameters, like batch size, tensor-parallelism, precision, as so on, in the training scripts. For example, Llama3 8B model parameters are defined in [examples/llama/train_llama3.sh](https://github.com/ROCm/Megatron-LM/blob/rocm_dev/examples/llama/train_llama3.sh){.reference .external} as shown below:

:
{.highlight-bash .notranslate}

highlight
    TP="${TP:-8}"
    PP="${PP:-1}"
    CP="${CP:-1}"
    MBS="${MBS:-1}"
    BS="${BS:-8}"

:

Primus defines the training parameters in top-level YAML files -- see [examples/megatron/configs/](https://github.com/AMD-AIG-AIMA/Primus/tree/v0.1.0-rc1/examples/megatron/configs){.reference .external}. For example, the [llama3.1_8B-pretrain.yaml](https://github.com/AMD-AIG-AIMA/Primus/blob/v0.1.0-rc1/examples/megatron/configs/llama3.1_8B-pretrain.yaml){.reference .external} configuration imports the [`llama3.1_8B.yaml`{.docutils .literal .notranslate}]{.pre} model architecture file. Users can then override the default training parameters in [`llama3.1_8B-pretrain.yaml`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-yaml .notranslate}

highlight
    # model to run
    model: llama3.1_8B.yaml  # Model architecture yaml
    overrides:
      # log
      # disable_wandb: false
      # disable_tensorboard: false
      stderr_sink_level: DEBUG

      log_avg_skip_iterations: 2
      log_avg_reset_interval: 50

      train_iters: 50
      micro_batch_size: 2
      global_batch_size: 128

      seq_length: 8192
      max_position_embeddings: 8192

      lr: 1.0e-5
      min_lr: 0.0
      lr_warmup_iters: 2
      lr_decay_iters: null
      lr_decay_style: cosine
      weight_decay: 0.1
      adam_beta1: 0.9
      adam_beta2: 0.95
      eod_mask_loss: true
      init_method_std: 0.008
      norm_epsilon: 1.0e-6

:
::::

::
{#backward-compatibility-with-megatron-lm .section}
## Backward compatibility with Megatron-LM[\#](#backward-compatibility-with-megatron-lm "Link to this heading"){.headerlink}

The Dockerized environment used for Primus maintains compatibility with Megatron-LM with limited support. To roll back to using Megatron-LM, follow these steps.

:
{.highlight-shell .notranslate}

highlight
    cd /workspace/Megatron-LM/
    pip uninstall megatron-core
    pip install -e .

:

Once Megatron-LM is installed, follow [[the documentation]{.doc}](../megatron-lm.html){.reference .internal} to run workloads as usual.
::
:::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::
