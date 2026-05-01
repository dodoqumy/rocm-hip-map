---
title: "Training a model with PyTorch for ROCm"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.3.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:56:50.457644+00:00
content_hash: "197b6011ff7eb004"
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::::::::::::::::::::::::::::::::::::
bd-content
::::::::::::::::::::::::::::::::::::::::::::::::
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
# Training a model with PyTorch for ROCm

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

::::::::::::::::::::::::::::::::::
{#training-a-model-with-pytorch-for-rocm .section}
# Training a model with PyTorch for ROCm[\#](#training-a-model-with-pytorch-for-rocm "Link to this heading"){.headerlink}

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
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 8 min read time

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

This documentation does not reflect the latest version of ROCm PyTorch training performance documentation. See [[Training a model with PyTorch on ROCm]{.doc}](../pytorch-training.html){.reference .internal} for the latest version.

PyTorch is an open-source machine learning framework that is widely used for model training with GPU-optimized components for transformer-based models.

The PyTorch for ROCm training Docker ([`rocm/pytorch-training:v25.3`{.docutils .literal .notranslate}]{.pre}) image provides a prebuilt optimized environment for fine-tuning and pretraining a model on AMD Instinct MI325X and MI300X GPUs. It includes the following software components to accelerate training workloads:

pst-scrollable-table-container
  Software component   Version
  -------------------- -------------------
  ROCm                 6.3.0
  PyTorch              2.7.0a0+git637433
  Python               3.10
  Transformer Engine   1.11
  Flash Attention      3.0.0
  hipBLASLt            git258a2162
  Triton               3.1

:
{#supported-models .section}
[]{#amd-pytorch-training-model-support-v253}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are pre-optimized for performance on the AMD Instinct MI300X GPU.

- Llama 3.1 8B

- Llama 3.1 70B

- FLUX.1-dev

{.admonition .note}
Note

Only these models are supported in the following steps.

Some models, such as Llama 3, require an external license agreement through a third party (for example, Meta).

:

{#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

If you have already validated your system settings, skip this step. Otherwise, complete the [[system validation and optimization steps]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#train-a-model-system-validation){.reference .internal} to set up your system before starting training.

::
{#disable-numa-auto-balancing .section}
### Disable NUMA auto-balancing[\#](#disable-numa-auto-balancing "Link to this heading"){.headerlink}

Generally, application performance can benefit from disabling NUMA auto-balancing. However, it might be detrimental to performance with certain types of workloads.

Run the command [`cat`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/proc/sys/kernel/numa_balancing`{.docutils .literal .notranslate}]{.pre} to check your current NUMA (Non-Uniform Memory Access) settings. Output [`0`{.docutils .literal .notranslate}]{.pre} indicates this setting is disabled. If there is no output or the output is [`1`{.docutils .literal .notranslate}]{.pre}, run the following command to disable NUMA auto-balancing.

:
{.highlight-shell .notranslate}

highlight
    sudo sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'

:

See [[System validation and optimization]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} for more information.
::

:::::
{#environment-setup .section}
## Environment setup[\#](#environment-setup "Link to this heading"){.headerlink}

This Docker image is optimized for specific model configurations outlined below. Performance can vary for other training workloads, as AMD doesn't validate configurations and run conditions outside those described.

{#download-the-docker-image .section}
#

1.  Use the following command to pull the Docker image from Docker Hub.

    :
{.highlight-shell .notranslate}
    
highlight
        docker pull rocm/pytorch-training:v25.3
    
    :

2.  Run the Docker container.

    :
{.highlight-shell .notranslate}
    
highlight
        docker run -it --device /dev/dri --device /dev/kfd --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v $HOME:$HOME -v  $HOME/.ssh:/root/.ssh --shm-size 64G --name training_env rocm/pytorch-training:v25.3
    
    :

3.  Use these commands if you exit the [`training_env`{.docutils .literal .notranslate}]{.pre} container and need to return to it.

    :
{.highlight-shell .notranslate}
    
highlight
        docker start training_env
        docker exec -it training_env bash
    
    :

4.  In the Docker container, clone the [ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external} repository and navigate to the benchmark scripts directory.

    :
{.highlight-shell .notranslate}
    
highlight
        git clone https://github.com/ROCm/MAD
        cd MAD/scripts/pytorch-train
    
    :

{#prepare-training-datasets-and-dependencies .section}
### Prepare training datasets and dependencies[\#](#prepare-training-datasets-and-dependencies "Link to this heading"){.headerlink}

The following benchmarking examples may require downloading models and datasets from Hugging Face. To ensure successful access to gated repos, set your [`HF_TOKEN`{.docutils .literal .notranslate}]{.pre}.

Run the setup script to install libraries and datasets needed for benchmarking.

:
{.highlight-shell .notranslate}

highlight
    ./pytorch_benchmark_setup.sh

:

[`pytorch_benchmark_setup.sh`{.docutils .literal .notranslate}]{.pre} installs the following libraries:

pst-scrollable-table-container
  Library                                                             Benchmark model           Reference
  ------------------------------------------------------------------- ------------------------- ------------------------------------------------------------------------------------------------------------
  [`accelerate`{.docutils .literal .notranslate}]{.pre}               Llama 3.1 8B, FLUX        [Hugging Face Accelerate](https://huggingface.co/docs/accelerate/en/index){.reference .external}
  [`datasets`{.docutils .literal .notranslate}]{.pre}                 Llama 3.1 8B, 70B, FLUX   [Hugging Face Datasets](https://huggingface.co/docs/datasets/v3.2.0/en/index){.reference .external} 3.2.0
  [`torchdata`{.docutils .literal .notranslate}]{.pre}                Llama 3.1 70B             [TorchData](https://pytorch.org/data/beta/index.html){.reference .external}
  [`tomli`{.docutils .literal .notranslate}]{.pre}                    Llama 3.1 70B             [Tomli](https://pypi.org/project/tomli/){.reference .external}
  [`tiktoken`{.docutils .literal .notranslate}]{.pre}                 Llama 3.1 70B             [tiktoken](https://github.com/openai/tiktoken){.reference .external}
  [`blobfile`{.docutils .literal .notranslate}]{.pre}                 Llama 3.1 70B             [blobfile](https://pypi.org/project/blobfile/){.reference .external}
  [`tabulate`{.docutils .literal .notranslate}]{.pre}                 Llama 3.1 70B             [tabulate](https://pypi.org/project/tabulate/){.reference .external}
  [`wandb`{.docutils .literal .notranslate}]{.pre}                    Llama 3.1 70B             [Weights & Biases](https://github.com/wandb/wandb){.reference .external}
  [`sentencepiece`{.docutils .literal .notranslate}]{.pre}            Llama 3.1 70B, FLUX       [SentencePiece](https://github.com/google/sentencepiece){.reference .external} 0.2.0
  [`tensorboard`{.docutils .literal .notranslate}]{.pre}              Llama 3.1 70 B, FLUX      [TensorBoard](https://www.tensorflow.org/tensorboard){.reference .external} 2.18.0
  [`csvkit`{.docutils .literal .notranslate}]{.pre}                   FLUX                      [csvkit](https://csvkit.readthedocs.io/en/latest/){.reference .external} 2.0.1
  [`deepspeed`{.docutils .literal .notranslate}]{.pre}                FLUX                      [DeepSpeed](https://github.com/deepspeedai/DeepSpeed){.reference .external} 0.16.2
  [`diffusers`{.docutils .literal .notranslate}]{.pre}                FLUX                      [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/en/index){.reference .external} 0.31.0
  [`GitPython`{.docutils .literal .notranslate}]{.pre}                FLUX                      [GitPython](https://github.com/gitpython-developers/GitPython){.reference .external} 3.1.44
  [`opencv-python-headless`{.docutils .literal .notranslate}]{.pre}   FLUX                      [opencv-python-headless](https://pypi.org/project/opencv-python-headless/){.reference .external} 4.10.0.84
  [`peft`{.docutils .literal .notranslate}]{.pre}                     FLUX                      [PEFT](https://huggingface.co/docs/peft/en/index){.reference .external} 0.14.0
  [`protobuf`{.docutils .literal .notranslate}]{.pre}                 FLUX                      [Protocol Buffers](https://github.com/protocolbuffers/protobuf){.reference .external} 5.29.2
  [`pytest`{.docutils .literal .notranslate}]{.pre}                   FLUX                      [PyTest](https://docs.pytest.org/en/stable/){.reference .external} 8.3.4
  [`python-dotenv`{.docutils .literal .notranslate}]{.pre}            FLUX                      [python-dotenv](https://pypi.org/project/python-dotenv/){.reference .external} 1.0.1
  [`seaborn`{.docutils .literal .notranslate}]{.pre}                  FLUX                      [Seaborn](https://seaborn.pydata.org/){.reference .external} 0.13.2
  [`transformers`{.docutils .literal .notranslate}]{.pre}             FLUX                      [Transformers](https://huggingface.co/docs/transformers/en/index){.reference .external} 4.47.0

[`pytorch_benchmark_setup.sh`{.docutils .literal .notranslate}]{.pre} downloads the following models from Hugging Face:

- [meta-llama/Llama-3.1-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct){.reference .external}

- [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev){.reference .external}

Along with the following datasets:

- [WikiText](https://huggingface.co/datasets/Salesforce/wikitext){.reference .external}

- [bghira/pseudo-camera-10k](https://huggingface.co/datasets/bghira/pseudo-camera-10k){.reference .external}

:::::

:::::::::
{#start-training-on-amd-instinct-gpus .section}
## Start training on AMD Instinct GPUs[\#](#start-training-on-amd-instinct-gpus "Link to this heading"){.headerlink}

The prebuilt PyTorch with ROCm training environment allows users to quickly validate system performance, conduct training benchmarks, and achieve superior performance for models like Llama 3.1 and Llama 2. This container should not be expected to provide generalized performance across all training workloads. You can expect the container to perform in the model configurations described in the following section, but other configurations are not validated by AMD.

Use the following instructions to set up the environment, configure the script to train models, and reproduce the benchmark results on MI300X Series GPUs with the AMD PyTorch training Docker image.

Once your environment is set up, use the following commands and examples to start benchmarking.

::::
{#pretraining .section}
### Pretraining[\#](#pretraining "Link to this heading"){.headerlink}

To start the pretraining benchmark, use the following command with the appropriate options. See the following list of options and their descriptions.

:
{.highlight-shell .notranslate}

highlight
    ./pytorch_benchmark_report.sh -t $training_mode -m $model_repo -p $datatype -s $sequence_length

:

:
{#options-and-available-models .section}
#### Options and available models[\#](#options-and-available-models "Link to this heading"){.headerlink}

pst-scrollable-table-container
  Name                                                        Options                                                    Description
  ----------------------------------------------------------- ---------------------------------------------------------- -------------------------------------------------------------------------------------------------
  [`$training_mode`{.docutils .literal .notranslate}]{.pre}   [`pretrain`{.docutils .literal .notranslate}]{.pre}        Benchmark pretraining
                                                              [`finetune_fw`{.docutils .literal .notranslate}]{.pre}     Benchmark full weight fine-tuning (Llama 3.1 70B with BF16)
                                                              [`finetune_lora`{.docutils .literal .notranslate}]{.pre}   Benchmark LoRA fine-tuning (Llama 3.1 70B with BF16)
  [`$datatype`{.docutils .literal .notranslate}]{.pre}        FP8 or BF16                                                Only Llama 3.1 8B supports FP8 precision.
  [`$model_repo`{.docutils .literal .notranslate}]{.pre}      Llama-3.1-8B                                               [Llama 3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct){.reference .external}
                                                              Llama-3.1-70B                                              [Llama 3.1 70B](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct){.reference .external}
                                                              Flux                                                       [FLUX.1 \[dev\]](https://huggingface.co/black-forest-labs/FLUX.1-dev){.reference .external}

:
::::

::
{#fine-tuning .section}
### Fine-tuning[\#](#fine-tuning "Link to this heading"){.headerlink}

To start the fine-tuning benchmark, use the following command. It will run the benchmarking example of Llama 2 70B with the WikiText dataset using the AMD fork of [torchtune](https://github.com/AMD-AIG-AIMA/torchtune){.reference .external}.

:
{.highlight-shell .notranslate}

highlight
    ./pytorch_benchmark_report.sh -t {finetune_fw, finetune_lora} -p BF16 -m Llama-3.1-70B

:
::

{#benchmarking-examples .section}
### Benchmarking examples[\#](#benchmarking-examples "Link to this heading"){.headerlink}

Here are some examples of how to use the command.

- Example 1: Llama 3.1 70B with BF16 precision with [torchtitan](https://github.com/ROCm/torchtitan){.reference .external}.

  :
{.highlight-shell .notranslate}
  
highlight
      ./pytorch_benchmark_report.sh -t pretrain -p BF16 -m Llama-3.1-70B -s 8192
  
  :

- Example 2: Llama 3.1 8B with FP8 precision using Transformer Engine (TE) and Hugging Face Accelerator.

  :
{.highlight-shell .notranslate}
  
highlight
      ./pytorch_benchmark_report.sh -t pretrain -p FP8 -m Llama-3.1-70B -s 8192
  
  :

- Example 3: FLUX.1-dev with BF16 precision with FluxBenchmark.

  :
{.highlight-shell .notranslate}
  
highlight
      ./pytorch_benchmark_report.sh -t pretrain -p BF16 -m Flux
  
  :

- Example 4: Torchtune full weight fine-tuning with Llama 3.1 70B

  :
{.highlight-shell .notranslate}
  
highlight
      ./pytorch_benchmark_report.sh -t finetune_fw -p BF16 -m Llama-3.1-70B
  
  :

- Example 5: Torchtune LoRA fine-tuning with Llama 3.1 70B

  :
{.highlight-shell .notranslate}
  
highlight
      ./pytorch_benchmark_report.sh -t finetune_lora -p BF16 -m Llama-3.1-70B
  
  :

:::::::::

{#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[PyTorch training performance testing version history]{.doc}](pytorch-training-history.html){.reference .internal} to find documentation for previous releases of the [`ROCm/pytorch-training`{.docutils .literal .notranslate}]{.pre} Docker image.

::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::
