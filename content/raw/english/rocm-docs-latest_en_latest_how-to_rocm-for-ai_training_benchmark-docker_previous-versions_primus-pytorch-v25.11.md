---
title: "Training a model with Primus and PyTorch"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/primus-pytorch-v25.11.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:57:13.072026+00:00
content_hash: "ce7c7089670135d8"
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
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
# Training a model with Primus and PyTorch

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#training-a-model-with-primus-and-pytorch .section}
# Training a model with Primus and PyTorch[\#](#training-a-model-with-primus-and-pytorch "Link to this heading"){.headerlink}

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
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 15 min read time

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

::::
:::::
::::::
:::::::
::::::::

{.admonition .caution}
Caution

This documentation does not reflect the latest version of ROCm Primus PyTorch training performance benchmark documentation. See [[Training a model with Primus and PyTorch]{.doc}](../primus-pytorch.html){.reference .internal} for the latest version.

[Primus](https://github.com/AMD-AGI/Primus){.reference .external} is a unified and flexible LLM training framework designed to streamline training. It streamlines LLM training on AMD Instinct GPUs using a modular, reproducible configuration paradigm. Primus now supports the PyTorch torchtitan backend.

{.admonition .note}
Note

For a unified training solution on AMD GPUs with ROCm, the [rocm/pytorch-training](https://hub.docker.com/r/rocm/pytorch-training/){.reference .external} Docker Hub registry will be deprecated soon in favor of [rocm/primus](https://hub.docker.com/r/rocm/primus){.reference .external}. The [`rocm/primus`{.docutils .literal .notranslate}]{.pre} Docker containers will cover PyTorch training ecosystem frameworks, including torchtitan and [[Megatron-LM]{.doc}](../primus-megatron.html){.reference .internal}.

Primus with the PyTorch torchtitan backend is designed to replace the [[ROCm PyTorch training]{.doc}](../pytorch-training.html){.reference .internal} workflow. See [[Training a model with PyTorch on ROCm]{.doc}](../pytorch-training.html){.reference .internal} to see steps to run workloads without Primus.

AMD provides a ready-to-use Docker image for MI355X, MI350X, MI325X, and MI300X GPUs containing essential components for Primus and PyTorch training with Primus Turbo optimizations.

::
{.sd-tab-set .docutils}
rocm/primus:v25.11

:
{.sd-tab-content .docutils}

pst-scrollable-table-container
  Software component   Version
  -------------------- ----------------------------
  ROCm                 7.1.0
  PyTorch              2.10.0.dev20251112+rocm7.1
  Python               3.10
  Transformer Engine   2.4.0.dev0+32e2d1d4
  Flash Attention      2.8.3
  hipBLASLt            1.2.0-09ab7153e2

:
::

:::::::::::::
{#supported-models .section}
[]{#amd-primus-pytorch-model-support-v25-11}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are pre-optimized for performance on the AMD Instinct MI325X and MI300X GPUs. Some instructions, commands, and training recommendations in this documentation might vary by model -- select one to get started.

:::::::::::
{#vllm-benchmark-ud-params-picker .container-fluid}
::::
{.row .gx-0}

{.col-2 .me-1 .px-2 .model-param-head}
Model

::
{.row .col-10 .pe-0}

{.col-6 .px-2 .model-param param-k="model-group" param-v="llama" tabindex="0"}
Meta Llama

{.col-6 .px-2 .model-param param-k="model-group" param-v="deepseek" tabindex="0"}
DeepSeek

::
::::

:::::
{.row .gx-0 .pt-1}

{.col-2 .me-1 .px-2 .model-param-head}
Variant

{.row .col-10 .pe-0}

{.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="primus_pyt_train_llama-3.1-8b" tabindex="0"}
Llama 3.1 8B

{.col-6 .px-2 .model-param param-group="llama" param-k="model" param-v="primus_pyt_train_llama-3.1-70b" tabindex="0"}
Llama 3.1 70B

{.col-6 .px-2 .model-param param-group="deepseek" param-k="model" param-v="primus_pyt_train_deepseek-v3-16b" tabindex="0"}
DeepSeek V3 16B

:::::
:::::::::::

{.admonition .seealso}
See also

For additional workloads, including Llama 3.3, Llama 3.2, Llama 2, GPT OSS, Qwen, and Flux models, see the documentation [[Training a model with PyTorch on ROCm]{.doc}](../pytorch-training.html){.reference .internal} (without Primus)

:::::::::::::

{#system-validation .section}
[]{#amd-primus-pytorch-performance-measurements-v25-11}

## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting training.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.

This Docker image is optimized for specific model configurations outlined below. Performance can vary for other training workloads, as AMD doesn't test configurations and run conditions outside those described.

::
{#pull-the-docker-image .section}
## Pull the Docker image[\#](#pull-the-docker-image "Link to this heading"){.headerlink}

Use the following command to pull the Docker image from Docker Hub.

:
{.highlight-shell .notranslate}

highlight
    docker pull rocm/primus:v25.11

:
::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#run-training .section}
## Run training[\#](#run-training "Link to this heading"){.headerlink}

Once the setup is complete, choose between the following two workflows to start benchmarking training. For fine-tuning workloads and multi-node training examples, see [[Training a model with PyTorch on ROCm]{.doc}](../pytorch-training.html){.reference .internal} (without Primus). For best performance on MI325X, MI350X, and MI355X GPUs, you might need to tweak some configurations (such as batch sizes).

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

{.sd-tab-content .docutils}

{.model-doc .primus-pyt-train-llama-3-1-8b .docutils .container}
The following run command is tailored to Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#amd-primus-pytorch-model-support-v25-11){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :
{.highlight-shell .notranslate}
    
highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    
    :

2.  For example, use this command to run the performance benchmark test on the Llama 3.1 8B model using one node with the BF16 data type on the host machine.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags primus_pyt_train_llama-3.1-8b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    
    :

    MAD launches a Docker container with the name [`container_ci-primus_pyt_train_llama-3.1-8b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.

{.model-doc .primus-pyt-train-llama-3-1-70b .docutils .container}
The following run command is tailored to Llama 3.1 70B. See [[Supported models]{.std .std-ref}](#amd-primus-pytorch-model-support-v25-11){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :
{.highlight-shell .notranslate}
    
highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    
    :

2.  For example, use this command to run the performance benchmark test on the Llama 3.1 70B model using one node with the BF16 data type on the host machine.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags primus_pyt_train_llama-3.1-70b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    
    :

    MAD launches a Docker container with the name [`container_ci-primus_pyt_train_llama-3.1-70b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.

{.model-doc .primus-pyt-train-deepseek-v3-16b .docutils .container}
The following run command is tailored to DeepSeek V3 16B. See [[Supported models]{.std .std-ref}](#amd-primus-pytorch-model-support-v25-11){.reference .internal} to switch to another available model.

1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :
{.highlight-shell .notranslate}
    
highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    
    :

2.  For example, use this command to run the performance benchmark test on the DeepSeek V3 16B model using one node with the BF16 data type on the host machine.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags primus_pyt_train_deepseek-v3-16b \
            --keep-model-dir \
            --live-output \
            --timeout 28800
    
    :

    MAD launches a Docker container with the name [`container_ci-primus_pyt_train_deepseek-v3-16b`{.docutils .literal .notranslate}]{.pre}. The latency and throughput reports of the model are collected in [`~/MAD/perf.csv`{.docutils .literal .notranslate}]{.pre}.

Primus benchmarking

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{.sd-tab-content .docutils}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{.model-doc .primus-pyt-train-llama-3-1-8b .docutils .container}
The following run commands are tailored to Llama 3.1 8B. See [[Supported models]{.std .std-ref}](#amd-primus-pytorch-model-support-v25-11){.reference .internal} to switch to another available model.

Download the Docker image and required packages

1.  Pull the [`rocm/primus:v25.11`{.docutils .literal .notranslate}]{.pre} Docker image from Docker Hub.

    :
{.highlight-shell .notranslate}
    
highlight
        docker pull rocm/primus:v25.11
    
    :

2.  Run the Docker container.

    :
{.highlight-shell .notranslate}
    
highlight
        docker run -it \
            --device /dev/dri \
            --device /dev/kfd \
            --network host \
            --ipc host \
            --group-add video \
            --cap-add SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --privileged \
            -v $HOME:$HOME \
            -v $HOME/.ssh:/root/.ssh \
            --shm-size 64G \
            --name training_env \
            rocm/primus:v25.11
    
    :

    Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :
{.highlight-shell .notranslate}
    
highlight
        docker start training_env
        docker exec -it training_env bash
    
    :

    The Docker container hosts verified commit [`c4c083de`{.docutils .literal .notranslate}]{.pre} of the [Primus](https://github.com/AMD-AGI/Primus/tree/c4c083de64ba3e8f19ccc9629411267108931f9e/){.reference .external} repository.

Prepare training datasets and dependencies

The following benchmarking examples require downloading models and datasets from Hugging Face. To ensure successful access to gated repos, set your [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-shell .notranslate}

highlight
    export HF_TOKEN=$your_personal_hugging_face_access_token

:

Pretraining

To get started, navigate to the [`Primus`{.docutils .literal .notranslate}]{.pre} directory in your container.

:
{.highlight-default .notranslate}

highlight
    cd /workspace/Primus

:

Now, to start the pretraining benchmark, use the [`run_pretrain.sh`{.docutils .literal .notranslate}]{.pre} script included with Primus with the appropriate options.

Benchmarking examples

::::::::::::::::::::
{.model-doc .primus-pyt-train-llama-3-1-8b .docutils .container}
Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/llama3.1_8B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 6

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::

To train Llama 3.1 8B with FP8 precision, use the following command.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/llama3.1_8B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 7

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::
::::::::::::::::::::

::::::::::::::::::::
{.model-doc .primus-pyt-train-llama-3-1-70b .docutils .container}
Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/llama3.1_70B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 6

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::

To train Llama 3.1 70B with FP8 precision, use the following command.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 5

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::
::::::::::::::::::::

::::::::::
{.model-doc .primus-pyt-train-deepseek-v3-16b .docutils .container}
Use the following command to run train DeepSeek V3 16B with BF16 precision using Primus torchtitan.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/deepseek_v3_16b-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 10

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::
::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{.model-doc .primus-pyt-train-llama-3-1-70b .docutils .container}
The following run commands are tailored to Llama 3.1 70B. See [[Supported models]{.std .std-ref}](#amd-primus-pytorch-model-support-v25-11){.reference .internal} to switch to another available model.

Download the Docker image and required packages

1.  Pull the [`rocm/primus:v25.11`{.docutils .literal .notranslate}]{.pre} Docker image from Docker Hub.

    :
{.highlight-shell .notranslate}
    
highlight
        docker pull rocm/primus:v25.11
    
    :

2.  Run the Docker container.

    :
{.highlight-shell .notranslate}
    
highlight
        docker run -it \
            --device /dev/dri \
            --device /dev/kfd \
            --network host \
            --ipc host \
            --group-add video \
            --cap-add SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --privileged \
            -v $HOME:$HOME \
            -v $HOME/.ssh:/root/.ssh \
            --shm-size 64G \
            --name training_env \
            rocm/primus:v25.11
    
    :

    Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :
{.highlight-shell .notranslate}
    
highlight
        docker start training_env
        docker exec -it training_env bash
    
    :

    The Docker container hosts verified commit [`c4c083de`{.docutils .literal .notranslate}]{.pre} of the [Primus](https://github.com/AMD-AGI/Primus/tree/c4c083de64ba3e8f19ccc9629411267108931f9e/){.reference .external} repository.

Prepare training datasets and dependencies

The following benchmarking examples require downloading models and datasets from Hugging Face. To ensure successful access to gated repos, set your [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-shell .notranslate}

highlight
    export HF_TOKEN=$your_personal_hugging_face_access_token

:

Pretraining

To get started, navigate to the [`Primus`{.docutils .literal .notranslate}]{.pre} directory in your container.

:
{.highlight-default .notranslate}

highlight
    cd /workspace/Primus

:

Now, to start the pretraining benchmark, use the [`run_pretrain.sh`{.docutils .literal .notranslate}]{.pre} script included with Primus with the appropriate options.

Benchmarking examples

::::::::::::::::::::
{.model-doc .primus-pyt-train-llama-3-1-8b .docutils .container}
Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/llama3.1_8B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 6

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::

To train Llama 3.1 8B with FP8 precision, use the following command.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/llama3.1_8B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 7

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::
::::::::::::::::::::

::::::::::::::::::::
{.model-doc .primus-pyt-train-llama-3-1-70b .docutils .container}
Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/llama3.1_70B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 6

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::

To train Llama 3.1 70B with FP8 precision, use the following command.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 5

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::
::::::::::::::::::::

::::::::::
{.model-doc .primus-pyt-train-deepseek-v3-16b .docutils .container}
Use the following command to run train DeepSeek V3 16B with BF16 precision using Primus torchtitan.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/deepseek_v3_16b-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 10

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::
::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{.model-doc .primus-pyt-train-deepseek-v3-16b .docutils .container}
The following run commands are tailored to DeepSeek V3 16B. See [[Supported models]{.std .std-ref}](#amd-primus-pytorch-model-support-v25-11){.reference .internal} to switch to another available model.

Download the Docker image and required packages

1.  Pull the [`rocm/primus:v25.11`{.docutils .literal .notranslate}]{.pre} Docker image from Docker Hub.

    :
{.highlight-shell .notranslate}
    
highlight
        docker pull rocm/primus:v25.11
    
    :

2.  Run the Docker container.

    :
{.highlight-shell .notranslate}
    
highlight
        docker run -it \
            --device /dev/dri \
            --device /dev/kfd \
            --network host \
            --ipc host \
            --group-add video \
            --cap-add SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --privileged \
            -v $HOME:$HOME \
            -v $HOME/.ssh:/root/.ssh \
            --shm-size 64G \
            --name training_env \
            rocm/primus:v25.11
    
    :

    Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :
{.highlight-shell .notranslate}
    
highlight
        docker start training_env
        docker exec -it training_env bash
    
    :

    The Docker container hosts verified commit [`c4c083de`{.docutils .literal .notranslate}]{.pre} of the [Primus](https://github.com/AMD-AGI/Primus/tree/c4c083de64ba3e8f19ccc9629411267108931f9e/){.reference .external} repository.

Prepare training datasets and dependencies

The following benchmarking examples require downloading models and datasets from Hugging Face. To ensure successful access to gated repos, set your [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre}.

:
{.highlight-shell .notranslate}

highlight
    export HF_TOKEN=$your_personal_hugging_face_access_token

:

Pretraining

To get started, navigate to the [`Primus`{.docutils .literal .notranslate}]{.pre} directory in your container.

:
{.highlight-default .notranslate}

highlight
    cd /workspace/Primus

:

Now, to start the pretraining benchmark, use the [`run_pretrain.sh`{.docutils .literal .notranslate}]{.pre} script included with Primus with the appropriate options.

Benchmarking examples

::::::::::::::::::::
{.model-doc .primus-pyt-train-llama-3-1-8b .docutils .container}
Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/llama3.1_8B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 6

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::

To train Llama 3.1 8B with FP8 precision, use the following command.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/llama3.1_8B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 7

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::
::::::::::::::::::::

::::::::::::::::::::
{.model-doc .primus-pyt-train-llama-3-1-70b .docutils .container}
Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/llama3.1_70B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 6

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::

To train Llama 3.1 70B with FP8 precision, use the following command.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 5

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::
::::::::::::::::::::

::::::::::
{.model-doc .primus-pyt-train-deepseek-v3-16b .docutils .container}
Use the following command to run train DeepSeek V3 16B with BF16 precision using Primus torchtitan.

:::::::::
{.sd-tab-set .docutils}
MI355X and MI350X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI355X/deepseek_v3_16b-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::

MI325X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml \
    bash examples/run_pretrain.sh --training.local_batch_size 10

:
::

MI300X

::
{.sd-tab-content .docutils}
:
{.highlight-shell .notranslate}

highlight
    EXP=examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml \
    bash examples/run_pretrain.sh

:
::
:::::::::
::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

{#further-reading .section}
## Further reading[\#](#further-reading "Link to this heading"){.headerlink}

- For an introduction to Primus, see [Primus: A Lightweight, Unified Training Framework for Large Models on AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/primus/README.html){.reference .external}.

- To learn more about MAD and the [`madengine`{.docutils .literal .notranslate}]{.pre} CLI, see the [MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide){.reference .external}.

- To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see [AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html){.reference .external}.

- For a list of other ready-made Docker images for AI with ROCm, see [AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models){.reference .external}.

{#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[PyTorch training performance testing version history]{.doc}](pytorch-training-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/pytorch-training`{.docutils .literal .notranslate}]{.pre} Docker image.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
